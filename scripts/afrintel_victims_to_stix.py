#!/usr/bin/env python3
"""
AFRINTEL synchronized victims_FR.md / victims.md -> STIX 2.1 bundles for OpenCTI

Usage:
  python3 scripts/afrintel_victims_to_stix.py --repo .
  python3 scripts/afrintel_victims_to_stix.py --repo . --year 2026
  python3 scripts/afrintel_victims_to_stix.py --repo . --year 2026 --month 05-may
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlsplit

AFRINTEL_ID = "identity--d3497218-f905-57e1-a219-a8700a85eb4a"
TLP_CLEAR_ID = "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487"
STIX_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_URL, "https://github.com/Hatchepsoute/AFRINTEL")
AFRINTEL_AUTHOR_ID = f"identity--{uuid.uuid5(STIX_NAMESPACE, 'identity:author:adama-assiongbon')}"

MONTHS_EN = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
}
MONTHS_FR = {
    "janvier": 1, "février": 2, "fevrier": 2, "mars": 3, "avril": 4, "mai": 5,
    "juin": 6, "juillet": 7, "août": 8, "aout": 8, "septembre": 9, "octobre": 10,
    "novembre": 11, "décembre": 12, "decembre": 12,
}

MONTH_NAMES_FR = {
    "january": "Janvier", "february": "Février", "march": "Mars", "april": "Avril",
    "may": "Mai", "june": "Juin", "july": "Juillet", "august": "Août",
    "september": "Septembre", "october": "Octobre", "november": "Novembre", "december": "Décembre",
}

DATE_RE = re.compile(r"^###\s+(.+?)\s*$", re.M)
ENTRY_RE = re.compile(r"^####\s+(.+?)\s*$", re.M)
FIELD_RE = re.compile(r"^\s*[-*]\s+\*\*(.+?)\*\*\s*:?\s*(.*?)\s*$")
RANSOMWARE_LIFECYCLE_RE = re.compile(
    r"<!--\s*afrintel:ransomware-lifecycle\s*(.*?)\s*-->",
    re.I | re.S,
)
STIX_ID_RE = re.compile(r"^[a-z0-9-]+--[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")
STIX_INDUSTRY_SECTORS = {
    "agriculture", "aerospace", "automotive", "chemical", "commercial",
    "communications", "construction", "defense", "education", "energy",
    "entertainment", "financial-services", "government", "emergency-services",
    "government-local", "government-national", "government-public-services",
    "government-regional", "healthcare", "hospitality-leisure", "infrastructure",
    "insurance", "manufacturing", "mining", "non-profit", "pharmaceuticals",
    "retail", "technology", "telecommunications", "transportation", "utilities",
}
RANSOMWARE_LIFECYCLE_STIX_FIELDS = {
    "listing_status": "x_afrintel_ransomware_listing_status",
    "listing_first_observed_at": "x_afrintel_listing_first_observed_at",
    "listing_last_observed_at": "x_afrintel_listing_last_observed_at",
    "sample_status": "x_afrintel_sample_status",
    "deadline_at": "x_afrintel_deadline_at",
    "deadline_status": "x_afrintel_deadline_status",
    "disclosure_status": "x_afrintel_disclosure_status",
    "victim_confirmation": "x_afrintel_victim_confirmation",
    "negotiation_status": "x_afrintel_negotiation_status",
    "ransom_payment_status": "x_afrintel_ransom_payment_status",
    "resale_status": "x_afrintel_resale_status",
    "last_checked_at": "x_afrintel_last_checked_at",
}
RANSOMWARE_LIFECYCLE_VALUES = {
    "listing_status": {"observed", "removed", "not-observed", "unknown"},
    "sample_status": {"none-observed", "preview-visible", "sample-available", "sample-reviewed", "unknown"},
    "deadline_status": {"active", "expired", "not-stated", "unknown"},
    "disclosure_status": {"not-observed", "partial", "full-claimed", "release-reviewed", "unknown"},
    "victim_confirmation": {"none-observed", "acknowledged", "confirmed", "unknown"},
    "negotiation_status": {"unknown", "publicly-reported", "confirmed"},
    "ransom_payment_status": {"unknown", "publicly-reported", "confirmed"},
    "resale_status": {"unknown", "actor-claimed", "independently-observed", "confirmed"},
}


@dataclass(frozen=True)
class VictimRecord:
    index: int
    date_display: str
    date_iso: str
    country: str
    country_codes: Tuple[str, ...]
    organization: str
    domain: str
    sector: str
    actor: str
    status: str
    incident_type: str
    confidence_level: str
    impact_level: str
    description: str
    reference_url: str
    source_path: str
    ransomware_lifecycle: Dict[str, str]


@dataclass(frozen=True)
class ReportDocument:
    language: str
    kind: str
    name: str
    content: str
    source_path: str
    labels: Tuple[str, ...]
    comparison_periods: Tuple[str, ...] = ()


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stix_id(object_type: str, key: str) -> str:
    return f"{object_type}--{uuid.uuid5(STIX_NAMESPACE, object_type + ':' + key)}"


def slugify(value: str) -> str:
    value = strip_flags(value).strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "unknown"


def strip_flags(value: str) -> str:
    return re.sub(r"[\U0001F1E6-\U0001F1FF]{2}\s*", "", value).strip()


def extract_country_codes(value: str) -> Tuple[str, ...]:
    """Return ISO-like alpha-2 codes encoded by flag emoji in a card header."""
    codes: List[str] = []
    for flag in re.findall(r"[\U0001F1E6-\U0001F1FF]{2}", value):
        codes.append("".join(chr(ord(char) - 0x1F1E6 + ord("A")) for char in flag))
    return tuple(codes)


def clean_inline(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", value)
    # Strip markdown emphasis/code delimiters but keep literal underscores or
    # asterisks that are part of a word (e.g. an actor handle like "N0ull_0X"),
    # mirroring GFM's rule that intraword underscores/asterisks are not emphasis.
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\*\*(.+?)\*\*", r"\1", value)
    value = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"\1", value)
    value = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", value)
    value = value.replace("–", "-").strip()
    return re.sub(r"\s+", " ", value)


def clean_actor(value: str) -> str:
    value = clean_inline(value)
    value = re.sub(r"^\[[^\]]+\]\s*", "", value).strip()
    value = re.split(r"\s+\(via\b|\s+\(forum\b|\s+-\s+Contacts?:", value, maxsplit=1, flags=re.I)[0]
    return value.strip() or "Unknown"


def extract_url(value: str) -> str:
    value = value.strip()
    if not value or re.search(r"not\s+(specified|applicable)|non précisé", value, re.I):
        return ""
    match = re.search(r"https?://[^\s)]+", value)
    if match:
        return match.group(0).rstrip(".,;")
    match = re.search(r"\[([^\]]+)\]", value)
    if match and "." in match.group(1):
        return "https://" + match.group(1).strip().rstrip("/")
    first = re.split(r"\s*/\s*|\s*;\s*|,", value, maxsplit=1)[0].strip()
    first = clean_inline(first).rstrip("/")
    if "." in first and not re.search(r"\s", first):
        return first if re.match(r"^https?://", first, re.I) else "https://" + first
    return ""


def normalize_domain_identity(value: str) -> str:
    """Normalize a parsed website URL for bilingual equality checks."""
    if not value:
        return ""
    parsed = urlsplit(value if "://" in value else f"https://{value}")
    host = (parsed.hostname or "").lower().rstrip(".")
    if host.startswith("www."):
        host = host[4:]
    path = parsed.path.rstrip("/")
    return host + path


def normalize_confidence_level(value: str) -> str:
    text = clean_inline(value).lower()
    text = text.replace("é", "e").replace("è", "e").replace("ê", "e")
    if not text:
        return ""
    if "very high" in text or "tres eleve" in text or "tres haute" in text:
        return "Very High"
    if "medium" in text or "moyen" in text or "modere" in text:
        return "Medium"
    if "high" in text or "eleve" in text or "haute" in text:
        return "High"
    if "low" in text or "faible" in text:
        return "Low"
    return clean_inline(value)


def normalize_impact_level(value: str) -> str:
    text = clean_inline(value)
    if not text:
        return ""
    match = re.search(r"(?:level|niveau)\s*([1-4])", text, re.I)
    return f"Level {match.group(1)}" if match else text


def extract_confidence_level(block: str, fields: Dict[str, str]) -> str:
    direct = normalize_confidence_level(first_matching(fields, ["confidence level", "niveau de confiance"]))
    if direct in {"Low", "Medium", "High", "Very High"}:
        return direct
    match = re.search(
        r"(?:confidence level|niveau de confiance)\s*:\s*"
        r"(very high|high|medium|low|tr[eè]s [ée]lev[ée]e?|[ée]lev[ée]e?|moyen(?:ne)?|faible)",
        block,
        re.I,
    )
    return normalize_confidence_level(match.group(1)) if match else ""


def extract_impact_level(block: str, fields: Dict[str, str]) -> str:
    direct = normalize_impact_level(first_matching(fields, ["impact level", "niveau d'impact", "niveau d’impact"]))
    if re.fullmatch(r"Level [1-4]", direct):
        return direct
    match = re.search(r"(?:impact level|niveau d['’]impact)\s*:\s*(?:level|niveau)\s*([1-4])", block, re.I)
    return f"Level {match.group(1)}" if match else ""


def parse_date_to_iso(date_text: str) -> str:
    text = re.sub(r"\s+", " ", date_text.strip().replace(",", " "))
    text = re.sub(r"\s+", " ", text)

    # May 02 2026 / Juin 6 2026
    m = re.match(r"([A-Za-zÀ-ÿ]+)\s+(\d{1,2})\s+(\d{4})$", text)
    if m:
        month_name, day, year = m.group(1).lower(), int(m.group(2)), int(m.group(3))
        month = MONTHS_EN.get(month_name) or MONTHS_FR.get(month_name)
        if month:
            return f"{year:04d}-{month:02d}-{day:02d}"

    # 02 May 2026 / 02 mai 2026
    m = re.match(r"(\d{1,2})\s+([A-Za-zÀ-ÿ]+)\s+(\d{4})$", text)
    if m:
        day, month_name, year = int(m.group(1)), m.group(2).lower(), int(m.group(3))
        month = MONTHS_EN.get(month_name) or MONTHS_FR.get(month_name)
        if month:
            return f"{year:04d}-{month:02d}-{day:02d}"

    # Month YYYY / Mois AAAA (no day given in the section header): default to
    # the first of the month so the entry is still captured with a sortable
    # ISO date instead of being silently dropped.
    m = re.match(r"([A-Za-zÀ-ÿ]+)\s+(\d{4})$", text)
    if m:
        month_name, year = m.group(1).lower(), int(m.group(2))
        month = MONTHS_EN.get(month_name) or MONTHS_FR.get(month_name)
        if month:
            return f"{year:04d}-{month:02d}-01"

    raise ValueError(f"Unable to parse date: {date_text}")


def split_country_org(header: str) -> Tuple[str, str]:
    text = header.strip()
    parts = re.split(r"\s+[-–]\s+", text, maxsplit=1)
    if len(parts) == 1:
        return "Unknown", clean_inline(strip_flags(text))
    country = clean_inline(strip_flags(parts[0]))
    organization = clean_inline(parts[1])
    organization = re.sub(r"\s+\[[^\]]+\]\s*$", "", organization).strip()
    return country or "Unknown", organization or "Unknown"


def parse_fields(block: str) -> Dict[str, str]:
    fields: Dict[str, List[str]] = {}
    current: Optional[str] = None
    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        match = FIELD_RE.match(line)
        if match:
            key = match.group(1).strip().strip(":").lower()
            key = re.sub(r"\s+", " ", key)
            current = key
            fields.setdefault(current, [])
            value = match.group(2).strip()
            if value:
                fields[current].append(value)
            continue
        if current and line.strip() and not line.lstrip().startswith(("###", "---")):
            fields[current].append(line.strip())
    return {key: clean_inline(" ".join(value)) for key, value in fields.items()}


def first_matching(fields: Dict[str, str], needles: Iterable[str]) -> str:
    for key, value in fields.items():
        if any(needle in key for needle in needles):
            return value
    return ""


def parse_ransomware_lifecycle(block: str) -> Dict[str, str]:
    match = RANSOMWARE_LIFECYCLE_RE.search(block)
    if not match:
        return {}

    lifecycle: Dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()
        if key not in RANSOMWARE_LIFECYCLE_STIX_FIELDS:
            continue
        allowed = RANSOMWARE_LIFECYCLE_VALUES.get(key)
        if value and allowed and value not in allowed:
            raise ValueError(f"Invalid ransomware lifecycle value for {key}: {value}")
        lifecycle[key] = value
    return lifecycle


def classify_incident(fields: Dict[str, str], status: str, default_incident_type: str = "") -> str:
    explicit_type = first_matching(fields, ["incident type", "type d'incident", "type d’incident"]).lower()
    if explicit_type:
        if "ransomware" in explicit_type:
            return "ransomware"
        if "ddos" in explicit_type or "denial of service" in explicit_type:
            return "ddos"
        if "defacement" in explicit_type or "défacement" in explicit_type:
            return "defacement"
        if "access" in explicit_type or "accès" in explicit_type:
            return "access-sale"
        if "leak" in explicit_type or "fuite" in explicit_type:
            return "data-leak"

    joined_text = " ".join([*fields.keys(), *fields.values()]).lower()
    status_text = status.lower()
    if "defacement" in status_text or "défacement" in status_text or "defacement" in joined_text or "défacement" in joined_text:
        return "defacement"
    if "ddos" in status_text or "ddos" in joined_text or "denial of service" in joined_text:
        return "ddos"
    if "ransomware" in status_text or "ransomware" in " ".join(fields.keys()).lower():
        return "ransomware"
    if "access" in status_text or "accès" in status_text or "credential" in status_text or "identifiant" in status_text:
        return "access-sale"
    if any(term in status_text for term in (
        "data leak", "data leaked", "database", "massive leak", "system intrusion",
        "supply chain compromise", "suspected compromise", "fuite", "base de données",
    )):
        return "data-leak"
    if default_incident_type:
        return default_incident_type
    return "data-leak"


def normalize_status(status: str, incident_type: str) -> Tuple[str, List[str]]:
    text = status.lower()
    labels = ["afrintel", "africa", "claim-unverified", incident_type]
    if "under investigation" in text:
        labels.remove("claim-unverified")
        labels.append("under-investigation")
        return "Under Investigation", labels
    if is_unattributed("", status):
        labels.remove("claim-unverified")
        labels.append("unattributed")
        return "Under Investigation", labels
    if "sample" in text or "échantillon" in text:
        labels.remove("claim-unverified")
        labels.append("data-sample-published")
        return "Claim - Data Sample Published", labels
    if "full" in text or "public" in text or "published" in text or "dump" in text:
        labels.remove("claim-unverified")
        labels.append("data-fully-published")
        return "Data Fully Published", labels
    if "confirmed" in text or "confirm" in text:
        labels.remove("claim-unverified")
        labels.append("incident-confirmed")
        return "Incident Confirmed by Victim", labels
    if "resolved" in text or "résolu" in text:
        labels.remove("claim-unverified")
        labels.append("resolved")
        return "Resolved", labels
    return "Claim - Unverified", labels


def normalize_sector(raw: str) -> Optional[str]:
    value = raw.lower()
    # "Fund administration" is a financial service, not public administration.
    if "fund administration" in value or "administration de fonds" in value:
        return "financial-services"
    mapping = {
        "local government": "government-local", "collectivité": "government-local",
        "municipal": "government-local", "municipality": "government-local",
        "national government": "government-national", "central public": "government-national",
        "administration centrale": "government-national", "ministry": "government-national",
        "ministère": "government-national",
        "government": "government", "public": "government", "administration": "government",
        "education": "education", "university": "education", "school": "education",
        "teacher": "education", "academic": "education",
        "health": "healthcare", "santé": "healthcare", "medical": "healthcare", "dhis2": "healthcare",
        "pharma": "pharmaceuticals",
        "finance": "financial-services", "financial": "financial-services", "bank": "financial-services",
        "treasury": "financial-services", "wealth": "financial-services", "pension": "financial-services",
        "fintech": "financial-services", "payment": "financial-services", "paiement": "financial-services",
        "insurance": "insurance", "assurance": "insurance",
        "recruit": "commercial", "job": "commercial", "human resources": "commercial",
        "ressources humaines": "commercial", "legal": "commercial", "juridique": "commercial",
        "accounting": "commercial", "outsourcing": "commercial", "business services": "commercial",
        "services / crm": "commercial", "real estate": "commercial",
        "telecom": "telecommunications", "ict": "technology", "technology": "technology", "digital": "technology",
        "software": "technology", "informatique": "technology", "numérique": "technology",
        "it consulting": "technology", "it &": "technology", "it infrastructure": "technology",
        "mobile application": "technology", "social network": "technology",
        "e-commerce": "retail", "commerce": "retail", "retail": "retail", "marketplace": "retail",
        "logistics": "transportation", "transport": "transportation", "postal": "transportation",
        "aviation": "transportation", "airline": "transportation", "port": "transportation",
        "rail": "transportation",
        "automotive": "automotive", "automobile": "automotive",
        "food": "manufacturing", "beverage": "manufacturing", "aliment": "manufacturing",
        "engineering": "manufacturing", "ingénierie": "manufacturing", "mechanical": "manufacturing",
        "mécanique": "manufacturing", "manufactur": "manufacturing", "industrie": "manufacturing",
        "construction": "construction", "mining": "mining", "minier": "mining",
        "hospitality": "hospitality-leisure", "tourism": "hospitality-leisure", "tourisme": "hospitality-leisure",
        "ngo": "non-profit", "charity": "non-profit", "civil society": "non-profit",
        "think tank": "non-profit", "political": "non-profit",
        "energy": "energy", "énergie": "energy", "oil": "energy", "gas": "energy",
        "water": "utilities", "eau": "utilities", "utility": "utilities",
        "sports": "entertainment", "sport": "entertainment", "media": "entertainment",
        "law enforcement": "emergency-services", "anti-corruption": "government",
        "internet service": "telecommunications",
        "personal data": "commercial", "data aggregation": "commercial",
        "security": "commercial", "sécurité": "commercial",
        "agriculture": "agriculture", "agri": "agriculture",
    }
    for key, output in mapping.items():
        if key in value:
            return output
    return None


def is_unattributed(actor: str, status: str = "") -> bool:
    value = f"{actor} {status}".lower()
    return any(term in value for term in (
        "unclaimed", "unattributed", "unknown", "not specified", "non précisé",
        "non revendiqué", "non revendique", "non attribué", "non attribue",
        "acteur inconnu", "inconnu",
    ))


def normalize_text_identity(value: str) -> str:
    text = unicodedata.normalize("NFKD", clean_inline(value))
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def actor_identity_key(actor: str, status: str = "") -> str:
    """Return a language-neutral comparison key for the primary source actor."""
    if is_unattributed(actor, status):
        return "unattributed"
    primary = re.split(r"[,;(]", clean_inline(actor), maxsplit=1)[0]
    return normalize_text_identity(primary)


def country_identity_key(record: VictimRecord) -> Tuple[str, ...]:
    if record.country_codes:
        return record.country_codes
    aliases = {
        "afrique multi pays": "africa multi country",
        "afrique du sud": "south africa",
        "algerie": "algeria",
        "cote d ivoire": "ivory coast",
        "egypte": "egypt",
        "maroc": "morocco",
        "maurice": "mauritius",
        "senegal": "senegal",
        "soudan": "sudan",
        "tanzanie": "tanzania",
        "tunisie": "tunisia",
    }
    countries = [part.strip() for part in re.split(r"\s*/\s*", record.country)]
    return tuple(aliases.get(normalize_text_identity(country), normalize_text_identity(country)) for country in countries)


def validate_bilingual_records(
    records_fr: List[VictimRecord],
    records_en: List[VictimRecord],
    context: str,
) -> None:
    """Block STIX generation when structured FR/EN incident data diverges."""
    if len(records_fr) != len(records_en):
        raise ValueError(
            f"Bilingual victim count mismatch for {context}: "
            f"{len(records_fr)} FR != {len(records_en)} EN"
        )

    mismatches: List[str] = []
    for rec_fr, rec_en in zip(records_fr, records_en):
        checks = {
            "date": (rec_fr.date_iso, rec_en.date_iso),
            "country": (country_identity_key(rec_fr), country_identity_key(rec_en)),
            "actor": (
                actor_identity_key(rec_fr.actor, rec_fr.status),
                actor_identity_key(rec_en.actor, rec_en.status),
            ),
            "status": (
                normalize_status(rec_fr.status, rec_fr.incident_type)[0],
                normalize_status(rec_en.status, rec_en.incident_type)[0],
            ),
            "incident type": (rec_fr.incident_type, rec_en.incident_type),
            "domain": (
                normalize_domain_identity(rec_fr.domain),
                normalize_domain_identity(rec_en.domain),
            ),
            "reference": (rec_fr.reference_url, rec_en.reference_url),
            "confidence": (rec_fr.confidence_level, rec_en.confidence_level),
            "impact": (rec_fr.impact_level, rec_en.impact_level),
            "ransomware lifecycle": (
                rec_fr.ransomware_lifecycle,
                rec_en.ransomware_lifecycle,
            ),
        }
        for field, (fr_value, en_value) in checks.items():
            if fr_value != en_value:
                mismatches.append(
                    f"card {rec_fr.index} {field}: FR={fr_value!r} EN={en_value!r}"
                )

    if mismatches:
        preview = "; ".join(mismatches[:10])
        extra = f"; plus {len(mismatches) - 10} additional mismatch(es)" if len(mismatches) > 10 else ""
        raise ValueError(f"Bilingual parity check failed for {context}: {preview}{extra}")


def incident_label_fr(incident_type: str) -> str:
    return {
        "ransomware": "ransomware",
        "data-leak": "fuite de données",
        "access-sale": "vente d'accès",
        "defacement": "défacement",
        "ddos": "DDoS",
    }.get(incident_type, incident_type)


def french_country_location(country: str) -> str:
    """Return the idiomatic French location phrase for known country labels."""
    return {
        "Afrique du Sud": "en Afrique du Sud",
        "Algérie": "en Algérie",
        "Kenya": "au Kenya",
        "Maurice": "à Maurice",
        "Nigeria": "au Nigeria",
    }.get(country, f"en {country}")


def normalize_dashes(value: str) -> str:
    return value.replace("—", "-").replace("–", "-")


def safe_description(rec: VictimRecord) -> str:
    incident_label = rec.incident_type.replace("-", " ")
    if is_unattributed(rec.actor, rec.status):
        base = (
            f"AFRINTEL recorded an observed {incident_label} affecting {rec.organization} "
            f"in {rec.country} on {rec.date_display}. No actor attribution is recorded. "
            f"Status: {rec.status}. Sector: {rec.sector}."
        )
    else:
        base = (
            f"AFRINTEL recorded a publicly claimed {incident_label} affecting {rec.organization} "
            f"in {rec.country} on {rec.date_display}. The source actor is listed as {rec.actor}. "
            f"Status: {rec.status}. Sector: {rec.sector}."
        )
    if rec.description:
        base += " Source summary: " + rec.description[:2000]
    return normalize_dashes(base)


def safe_description_fr(rec: VictimRecord, incident_type: Optional[str] = None) -> str:
    incident_label = incident_label_fr(incident_type or rec.incident_type)
    location = french_country_location(rec.country)
    if is_unattributed(rec.actor, rec.status):
        base = (
            f"AFRINTEL a recensé un {incident_label} observé concernant {rec.organization} "
            f"{location}, à la date du {rec.date_display}. Aucune attribution à un acteur n'est enregistrée. "
            f"Statut : {rec.status}. Secteur : {rec.sector}."
        )
    else:
        base = (
            f"AFRINTEL a recensé une revendication publique de type {incident_label} concernant {rec.organization} "
            f"{location}, à la date du {rec.date_display}. L'acteur source est indiqué comme {rec.actor}. "
            f"Statut : {rec.status}. Secteur : {rec.sector}."
        )
    if rec.description:
        base += " Résumé de la source : " + rec.description[:2000]
    return normalize_dashes(base)


def bilingual_incident_description(rec_en: VictimRecord, rec_fr: Optional[VictimRecord]) -> str:
    english = safe_description(rec_en)
    if rec_fr is None:
        return english
    french = safe_description_fr(rec_fr, rec_en.incident_type)
    return f"## English\n\n{english}\n\n## Français\n\n{french}"


def bilingual_victim_description(rec_en: VictimRecord, rec_fr: Optional[VictimRecord]) -> str:
    english = (
        f"Victim entity or affected dataset recorded by AFRINTEL in {rec_en.country}. "
        f"Sector: {rec_en.sector}."
    )
    if rec_fr is None:
        return normalize_dashes(english)
    french = (
        f"Entité victime ou jeu de données affecté recensé par AFRINTEL {french_country_location(rec_fr.country)}. "
        f"Secteur : {rec_fr.sector}."
    )
    return normalize_dashes(f"## English\n\n{english}\n\n## Français\n\n{french}")


def clean_report_markdown(text: str) -> str:
    """Prepare a monthly README for use as an OpenCTI report description."""
    cleaned: List[str] = []
    in_mermaid = False

    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "```mermaid":
            in_mermaid = True
            continue
        if in_mermaid:
            if stripped == "```":
                in_mermaid = False
            continue
        if stripped.startswith("[![") or stripped.startswith("!["):
            continue
        if stripped.startswith("👉🏾"):
            continue
        cleaned.append(line.rstrip())

    content = normalize_dashes("\n".join(cleaned).strip())
    content = re.sub(r"\n{3,}", "\n\n", content)
    if not content:
        raise ValueError("Monthly report is empty after Markdown cleanup")
    return content


def parse_month_victims(md_path: Path, repo: Path) -> List[VictimRecord]:
    text = md_path.read_text(encoding="utf-8")
    # Entries under a level-two Notes section are contextual observations and
    # are explicitly excluded from monthly victim totals.
    text = re.split(r"^##\s+Notes\b", text, maxsplit=1, flags=re.I | re.M)[0]

    default_incident_type = (
        "ransomware"
        if re.search(r"no standalone data leak or access sale classified separately", text, re.I)
        else ""
    )
    date_matches = list(DATE_RE.finditer(text))
    records: List[VictimRecord] = []

    for date_index, date_match in enumerate(date_matches):
        date_display = date_match.group(1).strip()
        try:
            date_iso = parse_date_to_iso(date_display)
        except ValueError:
            continue
        date_start = date_match.end()
        date_end = date_matches[date_index + 1].start() if date_index + 1 < len(date_matches) else len(text)
        date_block = text[date_start:date_end]
        entry_matches = list(ENTRY_RE.finditer(date_block))

        for entry_index, entry_match in enumerate(entry_matches):
            header = entry_match.group(1).strip()
            entry_start = entry_match.end()
            entry_end = entry_matches[entry_index + 1].start() if entry_index + 1 < len(entry_matches) else len(date_block)
            entry_block = date_block[entry_start:entry_end]
            ransomware_lifecycle = parse_ransomware_lifecycle(entry_block)
            fields = parse_fields(RANSOMWARE_LIFECYCLE_RE.sub("", entry_block))

            country, organization = split_country_org(header)
            country_codes = extract_country_codes(header)
            actor = first_matching(fields, ["ransomware group", "actor", "threat actor", "groupe ransomware", "acteur"])
            sector = first_matching(fields, ["sector", "secteur"])
            status = first_matching(fields, ["status", "statut"])
            website = first_matching(fields, [
                "website", "websites", "web site", "observed websites", "site web", "sites web",
            ])
            confidence_level = extract_confidence_level(entry_block, fields)
            impact_level = extract_impact_level(entry_block, fields)
            description = first_matching(fields, ["description", "victim description", "leak description", "analysis", "sample analysis"])
            reference = first_matching(fields, ["reference", "référence"])

            actor = clean_actor(actor) if actor else "Unknown"
            sector = sector or "Unknown"
            status = status or "Claim - Unverified"
            incident_type = classify_incident(fields, status, default_incident_type)
            if ransomware_lifecycle and incident_type != "ransomware":
                raise ValueError(
                    f"Ransomware lifecycle metadata found on non-ransomware record: {header}"
                )

            records.append(VictimRecord(
                index=len(records) + 1,
                date_display=date_display,
                date_iso=date_iso,
                country=country,
                country_codes=country_codes,
                organization=organization,
                domain=extract_url(website),
                sector=clean_inline(sector),
                actor=actor,
                status=clean_inline(status),
                incident_type=incident_type,
                confidence_level=confidence_level,
                impact_level=impact_level,
                description=description,
                reference_url=extract_url(reference),
                source_path=str(md_path.relative_to(repo)),
                ransomware_lifecycle=ransomware_lifecycle,
            ))

    return records


def base_objects(created: str) -> List[dict]:
    return [
        {
            "type": "identity",
            "spec_version": "2.1",
            "id": AFRINTEL_ID,
            "created": "2024-01-01T00:00:00Z",
            "modified": created,
            "name": "AFRINTEL",
            "identity_class": "organization",
            "description": "African Cyber Threat Intelligence project monitoring ransomware, data leaks, access sales, and extortion activity affecting African organizations. Maintained by Adama ASSIONGBON, SOC & Cyber Threat Intelligence Consultant.",
            "external_references": [{"source_name": "AFRINTEL", "url": "https://github.com/Hatchepsoute/AFRINTEL"}],
        },
        {
            "type": "identity",
            "spec_version": "2.1",
            "id": AFRINTEL_AUTHOR_ID,
            "created": "2024-01-01T00:00:00Z",
            "modified": created,
            "name": "Adama ASSIONGBON",
            "identity_class": "individual",
            "roles": ["SOC Consultant", "Cyber Threat Intelligence Consultant", "AFRINTEL Maintainer"],
            "description": "Author and maintainer of the AFRINTEL project.",
            "external_references": [{
                "source_name": "LinkedIn",
                "url": "https://www.linkedin.com/in/adama-assiongbon-9029893a/",
            }],
        },
    ]


def build_month_bundle(
    records_fr: List[VictimRecord],
    records_en: List[VictimRecord],
    year: str,
    month_dir: str,
    github_base: str,
    report_documents: List[ReportDocument],
) -> dict:
    if not records_fr:
        raise ValueError("No victim records to convert")

    created = now_iso()
    source_url_en = f"{github_base.rstrip('/')}/CyberAttackAfrica/{year}/{month_dir}/victims.md"
    source_url_fr = f"{github_base.rstrip('/')}/CyberAttackAfrica/{year}/{month_dir}/victims_FR.md"
    source_ref_en = {"source_name": "AFRINTEL victims.md", "url": source_url_en}
    source_ref_fr = {"source_name": "AFRINTEL victims_FR.md", "url": source_url_fr}

    objects: List[dict] = base_objects(created)
    actor_ids: Dict[str, str] = {}
    victim_ids: List[str] = []
    incident_ids: List[str] = []
    relationship_ids: List[str] = []
    records_en_by_index = {rec.index: rec for rec in records_en}

    for rec_fr in records_fr:
        rec_en = records_en_by_index[rec_fr.index]
        sector_ov = normalize_sector(rec_fr.sector)
        unattributed = is_unattributed(rec_fr.actor, rec_fr.status)
        actor_key = rec_en.actor.lower()
        actor_id = actor_ids.get(actor_key) if not unattributed else None
        if not unattributed and not actor_id:
            actor_id = stix_id("threat-actor", f"{year}:{month_dir}:actor:{rec_en.actor}")
            actor_ids[actor_key] = actor_id
            objects.append({
                "type": "threat-actor",
                "spec_version": "2.1",
                "id": actor_id,
                "created": created,
                "modified": created,
                "name": rec_en.actor,
                "description": f"Threat actor, ransomware group, or source referenced by AFRINTEL for {month_dir} {year}. Claims are unverified unless stated otherwise.",
                "labels": ["afrintel", "africa", "claim-unverified", slugify(year), slugify(month_dir)],
                "created_by_ref": AFRINTEL_ID,
                "object_marking_refs": [TLP_CLEAR_ID],
                "external_references": [source_ref_fr, source_ref_en],
            })

        victim_id = stix_id(
            "identity",
            f"{year}:{month_dir}:victim:{rec_en.index}:{rec_en.country}:{rec_en.organization}",
        )
        victim_ids.append(victim_id)
        victim_refs = [source_ref_fr, source_ref_en]
        if rec_fr.domain:
            victim_refs.append({"source_name": "website", "url": rec_fr.domain})
        if rec_fr.reference_url:
            victim_refs.append({"source_name": "incident source", "url": rec_fr.reference_url})

        victim_object = {
            "type": "identity",
            "spec_version": "2.1",
            "id": victim_id,
            "created": created,
            "modified": created,
            "name": rec_en.organization,
            "identity_class": "organization" if "/" not in rec_fr.country else "group",
            "description": bilingual_victim_description(rec_en, rec_fr),
            "labels": ["afrintel", "victim", slugify(rec_en.country)] + ([sector_ov] if sector_ov else []),
            "created_by_ref": AFRINTEL_ID,
            "object_marking_refs": [TLP_CLEAR_ID],
            "external_references": victim_refs,
            "x_afrintel_country": rec_en.country,
            "x_afrintel_country_fr": rec_fr.country,
            "x_afrintel_organization_fr": rec_fr.organization,
            "x_afrintel_sector_raw": rec_fr.sector,
            "x_afrintel_sector_raw_en": rec_en.sector,
            "x_afrintel_source_path": rec_fr.source_path,
            "x_afrintel_source_path_en": rec_en.source_path,
        }
        if sector_ov:
            victim_object["sectors"] = [sector_ov]
        objects.append(victim_object)

        normalized_status, labels = normalize_status(rec_fr.status, rec_fr.incident_type)
        if unattributed and "unattributed" not in labels:
            labels.append("unattributed")
        incident_id = stix_id(
            "incident",
            f"{year}:{month_dir}:incident:{rec_en.index}:{rec_fr.date_iso}:{rec_en.country}:{rec_en.organization}",
        )
        incident_ids.append(incident_id)
        incident_refs = [source_ref_fr, source_ref_en]
        if rec_fr.domain:
            incident_refs.append({"source_name": "website", "url": rec_fr.domain})
        if rec_fr.reference_url:
            incident_refs.append({"source_name": "incident source", "url": rec_fr.reference_url})

        incident_object = {
            "type": "incident",
            "spec_version": "2.1",
            "id": incident_id,
            "created": created,
            "modified": created,
            "name": f"AFRINTEL {month_dir.split(chr(45), 1)[1].title() if chr(45) in month_dir else month_dir.title()} {year} incident {rec_en.index:02d}: {rec_en.organization}",
            "description": bilingual_incident_description(rec_en, rec_fr),
            "first_seen": f"{rec_fr.date_iso}T00:00:00Z",
            "labels": list(dict.fromkeys(labels + [slugify(rec_en.country)] + ([sector_ov] if sector_ov else []))),
            "created_by_ref": AFRINTEL_ID,
            "object_marking_refs": [TLP_CLEAR_ID],
            "external_references": incident_refs,
            "x_opencti_incident_type": rec_fr.incident_type,
            "x_afrintel_incident_index": rec_fr.index,
            "x_afrintel_status": normalized_status,
            "x_afrintel_country": rec_en.country,
            "x_afrintel_country_fr": rec_fr.country,
            "x_afrintel_sector_raw": rec_fr.sector,
            "x_afrintel_sector_raw_en": rec_en.sector,
            "x_afrintel_actor": rec_en.actor,
            "x_afrintel_actor_fr": rec_fr.actor,
            "x_afrintel_date_display": rec_fr.date_display,
            "x_afrintel_date_display_en": rec_en.date_display,
            "x_afrintel_source_path": rec_fr.source_path,
            "x_afrintel_source_path_en": rec_en.source_path,
        }
        if rec_fr.confidence_level:
            incident_object["x_afrintel_confidence_level"] = rec_fr.confidence_level
        if rec_fr.impact_level:
            incident_object["x_afrintel_impact_level"] = rec_fr.impact_level
        for lifecycle_key, lifecycle_value in rec_fr.ransomware_lifecycle.items():
            if lifecycle_value:
                incident_object[RANSOMWARE_LIFECYCLE_STIX_FIELDS[lifecycle_key]] = lifecycle_value
        if rec_fr.ransomware_lifecycle.get("disclosure_status") == "release-reviewed":
            incident_object["labels"] = list(dict.fromkeys([
                *incident_object["labels"],
                "data-release-reviewed",
            ]))
        objects.append(incident_object)

        relationships = [("incident-targets", "targets", incident_id, victim_id)]
        if actor_id:
            relationships[0:0] = [
                ("attributed", "attributed-to", incident_id, actor_id),
                ("actor-targets", "targets", actor_id, victim_id),
            ]
        for suffix, relationship_type, source_ref_id, target_ref_id in relationships:
            rel_id = stix_id("relationship", f"{year}:{month_dir}:{rec_fr.index}:{suffix}")
            relationship_ids.append(rel_id)
            objects.append({
                "type": "relationship",
                "spec_version": "2.1",
                "id": rel_id,
                "created": created,
                "modified": created,
                "relationship_type": relationship_type,
                "source_ref": source_ref_id,
                "target_ref": target_ref_id,
                "created_by_ref": AFRINTEL_ID,
                "object_marking_refs": [TLP_CLEAR_ID],
            })

    ransomware_count = sum(1 for rec in records_fr if rec.incident_type == "ransomware")
    leak_count = sum(1 for rec in records_fr if rec.incident_type == "data-leak")
    access_sale_count = sum(1 for rec in records_fr if rec.incident_type == "access-sale")
    defacement_count = sum(1 for rec in records_fr if rec.incident_type == "defacement")
    month_name = month_dir.split("-", 1)[1] if "-" in month_dir else month_dir
    report_refs = list(actor_ids.values()) + victim_ids + incident_ids

    for document in report_documents:
        report_url = f"{github_base.rstrip('/')}/{document.source_path}"
        report_key = (
            f"{year}:{month_dir}:report:{document.language}"
            if document.kind == "monthly-cti"
            else f"{year}:{month_dir}:report:{document.kind}:{document.language}"
        )
        report_object = {
            "type": "report",
            "spec_version": "2.1",
            "id": stix_id("report", report_key),
            "created": created,
            "modified": created,
            "name": document.name,
            "description": document.content,
            "lang": document.language,
            "published": f"{max(rec.date_iso for rec in records_fr)}T00:00:00Z",
            "report_types": ["threat-report"],
            "labels": [
                "afrintel", "africa", document.language, f"{month_name}-{year}",
                "ransomware", "data-leaks", "access-sales", "osint", *document.labels,
            ],
            "created_by_ref": AFRINTEL_ID,
            "object_marking_refs": [TLP_CLEAR_ID],
            "external_references": [{
                "source_name": f"AFRINTEL {Path(document.source_path).name}",
                "url": report_url,
            }],
            "object_refs": [AFRINTEL_AUTHOR_ID, *report_refs],
            "x_afrintel_source_path": document.source_path,
            "x_afrintel_report_kind": document.kind,
            "x_afrintel_author_ref": AFRINTEL_AUTHOR_ID,
            "x_afrintel_total_incidents": len(records_fr),
            "x_afrintel_ransomware_count": ransomware_count,
            "x_afrintel_data_leak_count": leak_count,
            "x_afrintel_access_sale_count": access_sale_count,
            "x_afrintel_defacement_count": defacement_count,
            "x_afrintel_victim_identity_count": len(victim_ids),
        }
        if document.comparison_periods:
            report_object["x_afrintel_comparison_periods"] = list(document.comparison_periods)
        objects.append(report_object)

    bundle = {"type": "bundle", "id": stix_id("bundle", f"{year}:{month_dir}:bundle"), "objects": objects}
    validate_bundle(
        bundle,
        expected_victims=len(records_fr),
        expected_incidents=len(records_fr),
        expected_reports=len(report_documents),
    )
    return bundle


def validate_bundle(bundle: dict, expected_victims: int, expected_incidents: int, expected_reports: int) -> None:
    objects = bundle.get("objects", [])
    intrusion_sets = [obj.get("id") for obj in objects if obj.get("type") == "intrusion-set"]
    if intrusion_sets:
        raise ValueError(
            "AFRINTEL publication sources must be modeled as threat-actor, not intrusion-set: "
            f"{intrusion_sets[:5]}"
        )
    bad_sectors = [
        (obj.get("id"), sector)
        for obj in objects
        if obj.get("type") == "identity"
        for sector in obj.get("sectors", [])
        if sector not in STIX_INDUSTRY_SECTORS
    ]
    if bad_sectors:
        raise ValueError(f"Non-standard STIX industry sectors detected: {bad_sectors[:5]}")
    ids = [obj.get("id") for obj in objects if obj.get("id")]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate STIX IDs detected")
    duplicate_labels = [
        obj.get("id") for obj in objects
        if len(obj.get("labels", [])) != len(set(obj.get("labels", [])))
    ]
    if duplicate_labels:
        raise ValueError(f"Duplicate STIX labels detected: {duplicate_labels[:5]}")
    bad_ids = [obj_id for obj_id in ids if not STIX_ID_RE.match(obj_id)]
    if bad_ids:
        raise ValueError(f"Invalid STIX IDs detected: {bad_ids[:5]}")
    id_set = set(ids)
    external_common_refs = {TLP_CLEAR_ID}
    missing_refs = []
    for obj in objects:
        for key, value in obj.items():
            if key.endswith("_ref") and isinstance(value, str) and "--" in value and value not in id_set and value not in external_common_refs:
                missing_refs.append((obj.get("id"), key, value))
            elif key.endswith("_refs") and isinstance(value, list):
                for item in value:
                    if isinstance(item, str) and "--" in item and item not in id_set and item not in external_common_refs:
                        missing_refs.append((obj.get("id"), key, item))
    if missing_refs:
        raise ValueError(f"Dangling STIX references detected: {missing_refs[:5]}")

    victim_count = sum(1 for obj in objects if obj.get("type") == "identity" and "victim" in obj.get("labels", []))
    incident_count = sum(1 for obj in objects if obj.get("type") == "incident")
    report_count = sum(1 for obj in objects if obj.get("type") == "report")
    if victim_count != expected_victims:
        raise ValueError(f"Victim identity count mismatch: {victim_count} != {expected_victims}")
    if incident_count != expected_incidents:
        raise ValueError(f"Incident count mismatch: {incident_count} != {expected_incidents}")
    if report_count != expected_reports:
        raise ValueError(f"Report count mismatch: {report_count} != {expected_reports}")


def reports_root(repo: Path) -> Path:
    current = repo / "CyberAttackAfrica"
    if current.exists():
        return current
    legacy = repo / "reports"
    if legacy.exists():
        return legacy
    raise FileNotFoundError(f"Neither CyberAttackAfrica nor reports directory found under {repo}")


def require_bilingual_file_pair(en_path: Path, fr_path: Path, label: str) -> None:
    if en_path.exists() != fr_path.exists():
        missing = fr_path if en_path.exists() else en_path
        raise FileNotFoundError(f"Missing bilingual counterpart for {label}: {missing}")


def process_month(repo: Path, year: str, month_dir: str, github_base: str, output_root: Optional[Path] = None) -> Path:
    root = reports_root(repo)
    month_path = root / year / month_dir
    victims_md = month_path / "victims.md"
    victims_fr_md = month_path / "victims_FR.md"
    if not victims_md.exists():
        raise FileNotFoundError(f"victims.md not found: {victims_md}")
    if not victims_fr_md.exists():
        raise FileNotFoundError(f"victims_FR.md not found: {victims_fr_md}")

    records_fr = parse_month_victims(victims_fr_md, repo)
    records_en = parse_month_victims(victims_md, repo)
    if not records_fr:
        raise ValueError(f"No victim records parsed from canonical source {victims_fr_md}")
    validate_bilingual_records(records_fr, records_en, f"{year}/{month_dir}")

    month_name = month_dir.split("-", 1)[1] if "-" in month_dir else month_dir
    month_name_fr = MONTH_NAMES_FR.get(month_name, month_name.title())
    report_documents: List[ReportDocument] = []

    monthly_names = {
        "en": f"AFRINTEL monthly CTI report - {month_name.title()} {year}",
        "fr": f"Rapport CTI mensuel AFRINTEL - {month_name_fr} {year}",
    }
    require_bilingual_file_pair(
        month_path / "README.md",
        month_path / "README_FR.md",
        f"monthly report {year}/{month_dir}",
    )
    for language, filename in (("en", "README.md"), ("fr", "README_FR.md")):
        report_path = month_path / filename
        if report_path.exists():
            report_documents.append(ReportDocument(
                language=language,
                kind="monthly-cti",
                name=monthly_names[language],
                content=clean_report_markdown(report_path.read_text(encoding="utf-8")),
                source_path=str(report_path.relative_to(repo)),
                labels=("monthly-report", "cti-report"),
            ))

    statistics_path = repo / "statistics" / year / month_dir
    statistics_names = {
        "en": f"AFRINTEL monthly statistics - {month_name.title()} {year}",
        "fr": f"Statistiques mensuelles AFRINTEL - {month_name_fr} {year}",
    }
    require_bilingual_file_pair(
        statistics_path / "README.md",
        statistics_path / "README_FR.md",
        f"monthly statistics {year}/{month_dir}",
    )
    for language, filename in (("en", "README.md"), ("fr", "README_FR.md")):
        document_path = statistics_path / filename
        if document_path.exists():
            report_documents.append(ReportDocument(
                language=language,
                kind="monthly-statistics",
                name=statistics_names[language],
                content=clean_report_markdown(document_path.read_text(encoding="utf-8")),
                source_path=str(document_path.relative_to(repo)),
                labels=("monthly-report", "statistics-report"),
            ))

    month_dirs = find_month_dirs(root / year)
    if month_dir in month_dirs:
        month_index = month_dirs.index(month_dir)
        if month_index > 0:
            previous_month_dir = month_dirs[month_index - 1]
            previous_month_name = previous_month_dir.split("-", 1)[1]
            comparison_dir = f"{previous_month_dir}-{month_name}"
            comparison_path = repo / "comparison" / year / comparison_dir
            comparison_names = {
                "en": (
                    f"AFRINTEL monthly comparison - {previous_month_name.title()} vs "
                    f"{month_name.title()} {year}"
                ),
                "fr": (
                    f"Comparaison mensuelle AFRINTEL - "
                    f"{MONTH_NAMES_FR.get(previous_month_name, previous_month_name.title())} "
                    f"et {month_name_fr} {year}"
                ),
            }
            require_bilingual_file_pair(
                comparison_path / "README.md",
                comparison_path / "README_FR.md",
                f"monthly comparison {year}/{comparison_dir}",
            )
            for language, filename in (("en", "README.md"), ("fr", "README_FR.md")):
                document_path = comparison_path / filename
                if document_path.exists():
                    report_documents.append(ReportDocument(
                        language=language,
                        kind="monthly-comparison",
                        name=comparison_names[language],
                        content=clean_report_markdown(document_path.read_text(encoding="utf-8")),
                        source_path=str(document_path.relative_to(repo)),
                        labels=("comparison-report", "month-over-month"),
                        comparison_periods=(previous_month_dir, month_dir),
                    ))

    bundle = build_month_bundle(records_fr, records_en, year, month_dir, github_base, report_documents)
    out_root = output_root or (repo / "stix" / year / month_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    month_slug = month_dir.split("-", 1)[1] if "-" in month_dir else month_dir
    out_path = out_root / f"afrintel_{month_slug}_{year}_opencti.json"
    out_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out_path


def process_h1_bundle(repo: Path, year: str, github_base: str, output_root: Optional[Path] = None) -> Path:
    root = reports_root(repo)
    year_path = root / year
    month_dirs = [
        month_dir for month_dir in find_month_dirs(year_path)
        if 1 <= int(month_dir.split("-", 1)[0]) <= 6
    ]
    if len(month_dirs) != 6:
        raise ValueError(f"H1 requires six monthly folders, found {len(month_dirs)}: {month_dirs}")

    objects_by_id: Dict[str, dict] = {}
    for month_dir in month_dirs:
        month_slug = month_dir.split("-", 1)[1]
        bundle_path = repo / "stix" / year / month_dir / f"afrintel_{month_slug}_{year}_opencti.json"
        if not bundle_path.exists():
            raise FileNotFoundError(f"Monthly STIX bundle not found: {bundle_path}")
        monthly_bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
        for obj in monthly_bundle.get("objects", []):
            object_id = obj.get("id")
            if not object_id:
                raise ValueError(f"STIX object without id in {bundle_path}")
            objects_by_id[object_id] = obj

    created = now_iso()
    merged_objects = list(objects_by_id.values())
    merged_refs = [obj["id"] for obj in merged_objects]
    h1_documents = [
        ReportDocument(
            language="en",
            kind="half-year-cti",
            name=f"AFRINTEL first-half cyber threat report - H1 {year}",
            content=clean_report_markdown((year_path / "README_H1.md").read_text(encoding="utf-8")),
            source_path=f"CyberAttackAfrica/{year}/README_H1.md",
            labels=("half-year-report", "cti-report", "statistics-report"),
            comparison_periods=(f"{year}-01-01", f"{year}-06-30"),
        ),
        ReportDocument(
            language="fr",
            kind="half-year-cti",
            name=f"Rapport AFRINTEL sur les cybermenaces du premier semestre {year}",
            content=clean_report_markdown((year_path / "README_H1_FR.md").read_text(encoding="utf-8")),
            source_path=f"CyberAttackAfrica/{year}/README_H1_FR.md",
            labels=("half-year-report", "cti-report", "statistics-report"),
            comparison_periods=(f"{year}-01-01", f"{year}-06-30"),
        ),
    ]

    incident_count = sum(obj.get("type") == "incident" for obj in merged_objects)
    victim_count = sum(
        obj.get("type") == "identity" and "victim" in obj.get("labels", [])
        for obj in merged_objects
    )
    ransomware_count = sum(
        obj.get("type") == "incident" and "ransomware" in obj.get("labels", [])
        for obj in merged_objects
    )
    data_leak_count = sum(
        obj.get("type") == "incident" and "data-leak" in obj.get("labels", [])
        for obj in merged_objects
    )
    access_sale_count = sum(
        obj.get("type") == "incident" and "access-sale" in obj.get("labels", [])
        for obj in merged_objects
    )
    defacement_count = sum(
        obj.get("type") == "incident" and "defacement" in obj.get("labels", [])
        for obj in merged_objects
    )

    for document in h1_documents:
        report = {
            "type": "report",
            "spec_version": "2.1",
            "id": stix_id("report", f"{year}:h1:report:{document.language}"),
            "created": created,
            "modified": created,
            "name": document.name,
            "description": document.content,
            "lang": document.language,
            "published": f"{year}-06-30T23:59:59Z",
            "report_types": ["threat-report"],
            "labels": [
                "afrintel", "africa", "h1", f"h1-{year}", document.language,
                "half-year-report", "cti-report", "statistics-report", "osint",
            ],
            "created_by_ref": AFRINTEL_ID,
            "object_marking_refs": [TLP_CLEAR_ID],
            "external_references": [{
                "source_name": f"AFRINTEL {Path(document.source_path).name}",
                "url": f"{github_base.rstrip('/')}/{document.source_path}",
            }],
            "object_refs": merged_refs,
            "x_afrintel_source_path": document.source_path,
            "x_afrintel_report_kind": document.kind,
            "x_afrintel_author_ref": AFRINTEL_AUTHOR_ID,
            "x_afrintel_comparison_periods": list(document.comparison_periods),
            "x_afrintel_total_incidents": incident_count,
            "x_afrintel_ransomware_count": ransomware_count,
            "x_afrintel_data_leak_count": data_leak_count,
            "x_afrintel_access_sale_count": access_sale_count,
            "x_afrintel_defacement_count": defacement_count,
            "x_afrintel_victim_identity_count": victim_count,
            "x_afrintel_months_covered": month_dirs,
        }
        merged_objects.append(report)

    bundle = {
        "type": "bundle",
        "id": stix_id("bundle", f"{year}:h1:bundle"),
        "objects": merged_objects,
    }
    monthly_report_count = sum(obj.get("type") == "report" for obj in objects_by_id.values())
    validate_bundle(
        bundle,
        expected_victims=victim_count,
        expected_incidents=incident_count,
        expected_reports=monthly_report_count + len(h1_documents),
    )

    out_root = output_root or (repo / "stix" / year)
    out_root.mkdir(parents=True, exist_ok=True)
    out_path = out_root / f"afrintel_h1_{year}_opencti.json"
    out_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out_path


def find_month_dirs(year_path: Path) -> List[str]:
    return [child.name for child in sorted(year_path.iterdir()) if child.is_dir() and re.match(r"^\d{2}-", child.name)]


def process_full_year_bundle(repo: Path, year: str, github_base: str, output_root: Optional[Path] = None) -> List[Path]:
    """Merge all monthly STIX bundles for a year into two annual bundles (EN/FR).

    Unlike the H1 bundle, this does not synthesize a combined annual report
    object; each output keeps the existing per-month 'monthly-cti' report,
    filtered to its own language, matching the pre-existing
    afrintel_<year>_victims_<LANG>_opencti.json convention.
    """
    root = reports_root(repo)
    year_path = root / year
    month_dirs = find_month_dirs(year_path)
    if not month_dirs:
        raise ValueError(f"No monthly folders found for {year}")

    objects_by_id: Dict[str, dict] = {}
    for month_dir in month_dirs:
        month_slug = month_dir.split("-", 1)[1]
        bundle_path = repo / "stix" / year / month_dir / f"afrintel_{month_slug}_{year}_opencti.json"
        if not bundle_path.exists():
            raise FileNotFoundError(f"Monthly STIX bundle not found: {bundle_path}")
        monthly_bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
        for obj in monthly_bundle.get("objects", []):
            object_id = obj.get("id")
            if not object_id:
                raise ValueError(f"STIX object without id in {bundle_path}")
            objects_by_id[object_id] = obj

    out_root = output_root or (repo / "stix" / year)
    out_root.mkdir(parents=True, exist_ok=True)
    outputs: List[Path] = []

    require_bilingual_file_pair(
        year_path / "README.md",
        year_path / "README_FR.md",
        f"annual report {year}",
    )

    for language, suffix in (("en", "EN"), ("fr", "FR")):
        objects = [
            obj for obj in objects_by_id.values()
            if obj.get("type") != "report"
            or (obj.get("lang") == language and obj.get("x_afrintel_report_kind") == "monthly-cti")
        ]
        victim_count = sum(
            obj.get("type") == "identity" and "victim" in obj.get("labels", [])
            for obj in objects
        )
        incident_count = sum(obj.get("type") == "incident" for obj in objects)
        report_count = sum(obj.get("type") == "report" for obj in objects)

        annual_path = year_path / ("README.md" if language == "en" else "README_FR.md")
        if annual_path.exists():
            annual_source = f"CyberAttackAfrica/{year}/{annual_path.name}"
            annual_report = {
                "type": "report",
                "spec_version": "2.1",
                "id": stix_id("report", f"{year}:annual:report:{language}"),
                "created": now_iso(),
                "modified": now_iso(),
                "name": f"AFRINTEL annual CTI report - {year}" if language == "en" else f"Rapport CTI annuel AFRINTEL - {year}",
                "description": clean_report_markdown(annual_path.read_text(encoding="utf-8")),
                "lang": language,
                "published": f"{year}-12-31T23:59:59Z",
                "report_types": ["threat-report"],
                "labels": ["afrintel", "africa", "annual", f"annual-{year}", language, "annual-report", "cti-report", "statistics-report", "osint"],
                "created_by_ref": AFRINTEL_ID,
                "object_marking_refs": [TLP_CLEAR_ID],
                "external_references": [{"source_name": f"AFRINTEL {annual_path.name}", "url": f"{github_base.rstrip(chr(47))}/{annual_source}"}],
                "object_refs": [obj["id"] for obj in objects],
                "x_afrintel_source_path": annual_source,
                "x_afrintel_report_kind": "annual-cti",
                "x_afrintel_author_ref": AFRINTEL_AUTHOR_ID,
                "x_afrintel_comparison_periods": [f"{year}-01-01", f"{year}-12-31"],
                "x_afrintel_total_incidents": incident_count,
                "x_afrintel_ransomware_count": sum(obj.get("type") == "incident" and "ransomware" in obj.get("labels", []) for obj in objects),
                "x_afrintel_data_leak_count": sum(obj.get("type") == "incident" and "data-leak" in obj.get("labels", []) for obj in objects),
                "x_afrintel_access_sale_count": sum(obj.get("type") == "incident" and "access-sale" in obj.get("labels", []) for obj in objects),
                "x_afrintel_defacement_count": sum(obj.get("type") == "incident" and "defacement" in obj.get("labels", []) for obj in objects),
                "x_afrintel_victim_identity_count": victim_count,
                "x_afrintel_months_covered": month_dirs,
            }
            objects.append(annual_report)
            report_count += 1

        bundle = {
            "type": "bundle",
            "id": stix_id("bundle", f"{year}:victims:{language}"),
            "objects": objects,
        }
        validate_bundle(bundle, expected_victims=victim_count, expected_incidents=incident_count, expected_reports=report_count)

        out_path = out_root / f"afrintel_{year}_victims_{suffix}_opencti.json"
        out_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        outputs.append(out_path)

    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate AFRINTEL OpenCTI STIX bundles from synchronized "
            "French-first victims_FR.md and victims.md files."
        )
    )
    parser.add_argument("--repo", required=True, help="Path to AFRINTEL repository root")
    parser.add_argument("--year", help="Specific year, e.g. 2026")
    parser.add_argument("--month", help="Specific month folder, e.g. 05-may")
    parser.add_argument("--h1", action="store_true", help="Build a first-half bundle from January through June monthly bundles")
    parser.add_argument("--full-year", action="store_true", help="Merge all monthly bundles for --year into annual EN/FR bundles (requires monthly bundles to already exist)")
    parser.add_argument("--github-base", default="https://github.com/Hatchepsoute/AFRINTEL/blob/main", help="Base GitHub URL used to build source references")
    parser.add_argument("--output-root", help="Optional custom output root. Default: <repo>/stix/<year>/<month>/")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    root = reports_root(repo)
    output_root = Path(args.output_root).resolve() if args.output_root else None
    generated: List[Path] = []

    if args.h1:
        if not args.year:
            print("[ERROR] --h1 requires --year.", file=sys.stderr)
            return 2
        try:
            out = process_h1_bundle(repo, args.year, args.github_base, output_root)
            print(f"[OK] Generated and validated: {out}")
            print("Generated 1 bundle(s).")
            return 0
        except Exception as exc:
            print(f"[ERROR] {args.year}/H1: {exc}", file=sys.stderr)
            return 2

    if args.full_year:
        if not args.year:
            print("[ERROR] --full-year requires --year.", file=sys.stderr)
            return 2
        try:
            outs = process_full_year_bundle(repo, args.year, args.github_base, output_root)
            for out in outs:
                print(f"[OK] Generated and validated: {out}")
            print(f"Generated {len(outs)} bundle(s).")
            return 0
        except Exception as exc:
            print(f"[ERROR] {args.year}/full-year: {exc}", file=sys.stderr)
            return 2

    years = [args.year] if args.year else [p.name for p in sorted(root.iterdir()) if p.is_dir() and re.match(r"^\d{4}$", p.name)]
    for year in years:
        year_path = root / year
        if not year_path.exists():
            print(f"[WARN] year not found: {year_path}", file=sys.stderr)
            continue
        months = [args.month] if args.month else find_month_dirs(year_path)
        for month_dir in months:
            try:
                out = process_month(repo, year, month_dir, args.github_base, output_root)
                generated.append(out)
                print(f"[OK] Generated and validated: {out}")
            except Exception as exc:
                print(f"[ERROR] {year}/{month_dir}: {exc}", file=sys.stderr)

    if not generated:
        print("[ERROR] No STIX bundles generated.", file=sys.stderr)
        return 2
    print(f"Generated {len(generated)} bundle(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
