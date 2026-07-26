#!/usr/bin/env python3
"""
AFRINTEL victims.md -> STIX 2.1 bundles for OpenCTI

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
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

AFRINTEL_ID = "identity--d3497218-f905-57e1-a219-a8700a85eb4a"
TLP_CLEAR_ID = "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487"
STIX_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_URL, "https://github.com/Hatchepsoute/AFRINTEL")

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
STIX_ID_RE = re.compile(r"^[a-z0-9-]+--[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")


@dataclass(frozen=True)
class VictimRecord:
    index: int
    date_display: str
    date_iso: str
    country: str
    organization: str
    domain: str
    sector: str
    actor: str
    status: str
    incident_type: str
    description: str
    source_path: str


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


def clean_inline(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", value)
    value = re.sub(r"[`*_]", "", value)
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


def classify_incident(fields: Dict[str, str], status: str) -> str:
    joined_keys = " ".join(fields.keys())
    text = f"{joined_keys} {status}".lower()
    if "ransomware" in text:
        return "ransomware"
    if "access" in text or "credential" in text or "identifiant" in text:
        return "access-sale"
    return "data-leak"


def normalize_status(status: str, incident_type: str) -> Tuple[str, List[str]]:
    text = status.lower()
    labels = ["afrintel", "africa", "claim-unverified", incident_type]
    if "sample" in text or "échantillon" in text:
        labels.append("data-sample-published")
        return "Claim - Data Sample Published", labels
    if "full" in text or "public" in text or "published" in text or "dump" in text:
        labels.append("data-fully-published")
        return "Data Fully Published", labels
    if "confirmed" in text or "confirm" in text:
        return "Incident Confirmed by Victim", labels
    return "Claim - Unverified", labels


def normalize_sector(raw: str) -> str:
    value = raw.lower()
    mapping = {
        "government": "government", "public": "government", "administration": "government", "ministry": "government",
        "education": "education", "university": "education", "school": "education", "teacher": "education",
        "health": "healthcare", "medical": "healthcare", "dhis2": "healthcare",
        "finance": "financial-services", "bank": "financial-services", "treasury": "financial-services",
        "recruit": "professional-services", "job": "professional-services", "human resources": "professional-services", "hr": "professional-services",
        "telecom": "telecommunications", "ict": "technology", "technology": "technology", "digital": "technology",
        "e-commerce": "retail", "retail": "retail", "marketplace": "retail",
        "logistics": "transport", "transport": "transport", "postal": "transport",
        "automotive": "automotive", "food": "food-and-beverage", "beverage": "food-and-beverage", "hospitality": "hospitality",
        "ngo": "non-profit", "charity": "non-profit", "civil society": "non-profit",
        "energy": "energy", "oil": "energy", "gas": "energy", "sports": "sports", "legal": "legal-services",
    }
    for key, output in mapping.items():
        if key in value:
            return output
    return slugify(raw)


def normalize_dashes(value: str) -> str:
    return value.replace("—", "-").replace("–", "-")


def safe_description(rec: VictimRecord) -> str:
    incident_label = rec.incident_type.replace("-", " ")
    base = (
        f"AFRINTEL recorded a publicly claimed {incident_label} affecting {rec.organization} "
        f"in {rec.country} on {rec.date_display}. The source actor is listed as {rec.actor}. "
        f"Status: {rec.status}. Sector: {rec.sector}."
    )
    if rec.description:
        base += " Source summary: " + rec.description[:2000]
    return normalize_dashes(base)


def safe_description_fr(rec: VictimRecord) -> str:
    incident_label = "ransomware" if rec.incident_type == "ransomware" else "fuite de données ou vente d'accès"
    base = (
        f"AFRINTEL a recensé une revendication publique de type {incident_label} concernant {rec.organization} "
        f"en {rec.country}, à la date du {rec.date_display}. L'acteur source est indiqué comme {rec.actor}. "
        f"Statut : {rec.status}. Secteur : {rec.sector}."
    )
    if rec.description:
        base += " Résumé de la source : " + rec.description[:2000]
    return normalize_dashes(base)


def bilingual_incident_description(rec_en: VictimRecord, rec_fr: Optional[VictimRecord]) -> str:
    english = safe_description(rec_en)
    if rec_fr is None:
        return english
    french = safe_description_fr(rec_fr)
    return f"## English\n\n{english}\n\n## Français\n\n{french}"


def bilingual_victim_description(rec_en: VictimRecord, rec_fr: Optional[VictimRecord]) -> str:
    english = (
        f"Victim entity or affected dataset recorded by AFRINTEL in {rec_en.country}. "
        f"Sector: {rec_en.sector}."
    )
    if rec_fr is None:
        return normalize_dashes(english)
    french = (
        f"Entité victime ou jeu de données affecté recensé par AFRINTEL en {rec_fr.country}. "
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
            fields = parse_fields(entry_block)

            country, organization = split_country_org(header)
            actor = first_matching(fields, ["ransomware group", "actor", "threat actor", "groupe ransomware", "acteur"])
            sector = first_matching(fields, ["sector", "secteur"])
            status = first_matching(fields, ["status", "statut"])
            website = first_matching(fields, ["website", "websites", "observed websites", "site web"])
            description = first_matching(fields, ["description", "victim description", "leak description", "analysis", "sample analysis"])

            actor = clean_actor(actor) if actor else "Unknown"
            sector = sector or "Unknown"
            status = status or "Claim - Unverified"
            incident_type = classify_incident(fields, status)

            records.append(VictimRecord(
                index=len(records) + 1,
                date_display=date_display,
                date_iso=date_iso,
                country=country,
                organization=organization,
                domain=extract_url(website),
                sector=clean_inline(sector),
                actor=actor,
                status=clean_inline(status),
                incident_type=incident_type,
                description=description,
                source_path=str(md_path.relative_to(repo)),
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
            "description": "African Cyber Threat Intelligence project monitoring ransomware, data leaks, access sales, and extortion activity affecting African organizations.",
            "external_references": [{"source_name": "AFRINTEL", "url": "https://github.com/Hatchepsoute/AFRINTEL"}],
        },
    ]


def build_month_bundle(
    records: List[VictimRecord],
    records_fr: List[VictimRecord],
    year: str,
    month_dir: str,
    github_base: str,
    report_documents: Dict[str, str],
) -> dict:
    if not records:
        raise ValueError("No victim records to convert")

    created = now_iso()
    source_url = f"{github_base.rstrip('/')}/CyberAttackAfrica/{year}/{month_dir}/victims.md"
    source_url_fr = f"{github_base.rstrip('/')}/CyberAttackAfrica/{year}/{month_dir}/victims_FR.md"
    source_ref = {"source_name": "AFRINTEL victims.md", "url": source_url}
    source_ref_fr = {"source_name": "AFRINTEL victims_FR.md", "url": source_url_fr}

    objects: List[dict] = base_objects(created)
    actor_ids: Dict[str, str] = {}
    victim_ids: List[str] = []
    incident_ids: List[str] = []
    relationship_ids: List[str] = []
    records_fr_by_index = {rec.index: rec for rec in records_fr}

    for rec in records:
        rec_fr = records_fr_by_index.get(rec.index)
        actor_key = rec.actor.lower()
        actor_id = actor_ids.get(actor_key)
        if not actor_id:
            actor_id = stix_id("intrusion-set", f"{year}:{month_dir}:actor:{rec.actor}")
            actor_ids[actor_key] = actor_id
            objects.append({
                "type": "intrusion-set",
                "spec_version": "2.1",
                "id": actor_id,
                "created": created,
                "modified": created,
                "name": rec.actor,
                "description": f"Threat actor, ransomware group, or source referenced by AFRINTEL for {month_dir} {year}. Claims are unverified unless stated otherwise.",
                "labels": ["afrintel", "africa", "claim-unverified", slugify(year), slugify(month_dir)],
                "created_by_ref": AFRINTEL_ID,
                "object_marking_refs": [TLP_CLEAR_ID],
                "external_references": [source_ref, source_ref_fr],
            })

        victim_id = stix_id("identity", f"{year}:{month_dir}:victim:{rec.index}:{rec.country}:{rec.organization}")
        victim_ids.append(victim_id)
        victim_refs = [source_ref, source_ref_fr]
        if rec.domain:
            victim_refs.append({"source_name": "website", "url": rec.domain})

        objects.append({
            "type": "identity",
            "spec_version": "2.1",
            "id": victim_id,
            "created": created,
            "modified": created,
            "name": rec.organization,
            "identity_class": "organization" if "/" not in rec.country else "group",
            "sectors": [normalize_sector(rec.sector)],
            "description": bilingual_victim_description(rec, rec_fr),
            "labels": ["afrintel", "victim", slugify(rec.country), normalize_sector(rec.sector)],
            "created_by_ref": AFRINTEL_ID,
            "object_marking_refs": [TLP_CLEAR_ID],
            "external_references": victim_refs,
            "x_afrintel_country": rec.country,
            "x_afrintel_source_path": rec.source_path,
        })

        normalized_status, labels = normalize_status(rec.status, rec.incident_type)
        incident_id = stix_id("incident", f"{year}:{month_dir}:incident:{rec.index}:{rec.date_iso}:{rec.country}:{rec.organization}")
        incident_ids.append(incident_id)
        incident_refs = [source_ref, source_ref_fr]
        if rec.domain:
            incident_refs.append({"source_name": "website", "url": rec.domain})

        objects.append({
            "type": "incident",
            "spec_version": "2.1",
            "id": incident_id,
            "created": created,
            "modified": created,
            "name": f"AFRINTEL {month_dir.split(chr(45), 1)[1].title() if chr(45) in month_dir else month_dir.title()} {year} incident {rec.index:02d}: {rec.organization}",
            "description": bilingual_incident_description(rec, rec_fr),
            "first_seen": f"{rec.date_iso}T00:00:00Z",
            "labels": labels + [slugify(rec.country), normalize_sector(rec.sector)],
            "created_by_ref": AFRINTEL_ID,
            "object_marking_refs": [TLP_CLEAR_ID],
            "external_references": incident_refs,
            "x_opencti_incident_type": "ransomware" if rec.incident_type == "ransomware" else "data-leak",
            "x_afrintel_incident_index": rec.index,
            "x_afrintel_status": normalized_status,
            "x_afrintel_country": rec.country,
            "x_afrintel_sector_raw": rec.sector,
            "x_afrintel_actor": rec.actor,
            "x_afrintel_date_display": rec.date_display,
            "x_afrintel_source_path": rec.source_path,
        })

        for suffix, relationship_type, source_ref_id, target_ref_id in [
            ("attributed", "attributed-to", incident_id, actor_id),
            ("actor-targets", "targets", actor_id, victim_id),
            ("incident-targets", "targets", incident_id, victim_id),
        ]:
            rel_id = stix_id("relationship", f"{year}:{month_dir}:{rec.index}:{suffix}")
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

    ransomware_count = sum(1 for rec in records if rec.incident_type == "ransomware")
    leak_count = len(records) - ransomware_count
    month_name = month_dir.split("-", 1)[1] if "-" in month_dir else month_dir
    report_refs = list(actor_ids.values()) + victim_ids + incident_ids

    report_names = {
        "en": f"AFRINTEL monthly CTI report - {month_name.title()} {year}",
        "fr": f"Rapport CTI mensuel AFRINTEL - {MONTH_NAMES_FR.get(month_name, month_name.title())} {year}",
    }
    report_files = {"en": "README.md", "fr": "README_FR.md"}

    for language in ("en", "fr"):
        content = report_documents.get(language)
        if not content:
            continue
        report_file = report_files[language]
        report_base = re.sub(r"/blob/[^/]+$", "/tree/main", github_base.rstrip("/"))
        report_url = f"{report_base}/CyberAttackAfrica/{year}/{month_dir}"
        objects.append({
            "type": "report",
            "spec_version": "2.1",
            "id": stix_id("report", f"{year}:{month_dir}:report:{language}"),
            "created": created,
            "modified": created,
            "name": report_names[language],
            "description": content,
            "lang": language,
            "published": f"{max(rec.date_iso for rec in records)}T00:00:00Z",
            "report_types": ["threat-report"],
            "labels": [
                "afrintel", "africa", "monthly-report", "cti-report", language,
                f"{month_name}-{year}", "ransomware", "data-leaks", "access-sales", "osint",
            ],
            "created_by_ref": AFRINTEL_ID,
            "object_marking_refs": [TLP_CLEAR_ID],
            "external_references": [{"source_name": f"AFRINTEL {report_file}", "url": report_url}],
            "object_refs": report_refs,
            "x_afrintel_source_path": f"CyberAttackAfrica/{year}/{month_dir}/{report_file}",
            "x_afrintel_total_incidents": len(records),
            "x_afrintel_ransomware_count": ransomware_count,
            "x_afrintel_data_leak_access_sale_count": leak_count,
            "x_afrintel_victim_identity_count": len(victim_ids),
        })

    bundle = {"type": "bundle", "id": stix_id("bundle", f"{year}:{month_dir}:bundle"), "objects": objects}
    validate_bundle(
        bundle,
        expected_victims=len(records),
        expected_incidents=len(records),
        expected_reports=len(report_documents),
    )
    return bundle


def validate_bundle(bundle: dict, expected_victims: int, expected_incidents: int, expected_reports: int) -> None:
    objects = bundle.get("objects", [])
    ids = [obj.get("id") for obj in objects if obj.get("id")]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate STIX IDs detected")
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


def process_month(repo: Path, year: str, month_dir: str, github_base: str, output_root: Optional[Path] = None) -> Path:
    root = reports_root(repo)
    month_path = root / year / month_dir
    victims_md = month_path / "victims.md"
    victims_fr_md = month_path / "victims_FR.md"
    if not victims_md.exists():
        raise FileNotFoundError(f"victims.md not found: {victims_md}")
    if not victims_fr_md.exists():
        raise FileNotFoundError(f"victims_FR.md not found: {victims_fr_md}")

    records = parse_month_victims(victims_md, repo)
    records_fr = parse_month_victims(victims_fr_md, repo)
    if not records:
        raise ValueError(f"No victim records parsed from {victims_md}")
    if len(records_fr) != len(records):
        raise ValueError(f"Bilingual victim count mismatch: {len(records)} EN != {len(records_fr)} FR")
    for rec_en, rec_fr in zip(records, records_fr):
        if rec_en.date_iso != rec_fr.date_iso:
            raise ValueError(
                f"Bilingual victim date mismatch at incident {rec_en.index}: "
                f"{rec_en.date_iso} != {rec_fr.date_iso}"
            )

    report_documents: Dict[str, str] = {}
    for language, filename in (("en", "README.md"), ("fr", "README_FR.md")):
        report_path = month_path / filename
        if report_path.exists():
            report_documents[language] = clean_report_markdown(report_path.read_text(encoding="utf-8"))

    bundle = build_month_bundle(records, records_fr, year, month_dir, github_base, report_documents)
    out_root = output_root or (repo / "stix" / year / month_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    month_slug = month_dir.split("-", 1)[1] if "-" in month_dir else month_dir
    out_path = out_root / f"afrintel_{month_slug}_{year}_opencti.json"
    out_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out_path


def find_month_dirs(year_path: Path) -> List[str]:
    return [child.name for child in sorted(year_path.iterdir()) if child.is_dir() and re.match(r"^\d{2}-", child.name)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate AFRINTEL OpenCTI STIX bundles from victims.md files.")
    parser.add_argument("--repo", required=True, help="Path to AFRINTEL repository root")
    parser.add_argument("--year", help="Specific year, e.g. 2026")
    parser.add_argument("--month", help="Specific month folder, e.g. 05-may")
    parser.add_argument("--github-base", default="https://github.com/Hatchepsoute/AFRINTEL/blob/main", help="Base GitHub URL used to build source references")
    parser.add_argument("--output-root", help="Optional custom output root. Default: <repo>/stix/<year>/<month>/")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    root = reports_root(repo)
    output_root = Path(args.output_root).resolve() if args.output_root else None
    generated: List[Path] = []

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
