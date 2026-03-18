#!/usr/bin/env python3
"""
AFRINTEL victims.md -> STIX 2.1 bundles for OpenCTI

Usage:
  python3 scripts/afrintel_victims_to_stix.py --repo .
  python3 scripts/afrintel_victims_to_stix.py --repo . --year 2025
  python3 scripts/afrintel_victims_to_stix.py --repo . --year 2025 --month 01-january
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
from typing import Dict, List, Optional, Tuple


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stix_id(object_type: str) -> str:
    return f"{object_type}--{uuid.uuid4()}"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "unknown"


def ensure_url(url: str) -> str:
    url = url.strip()
    if not url:
        return url
    if " / " in url:
        url = url.split(" / ")[0].strip()
    if not re.match(r"^https?://", url, flags=re.I):
        return "https://" + url
    return url


def normalize_status(raw: str) -> Tuple[str, List[str]]:
    text = raw.strip().lower()
    labels = ["afrintel", "ransomware", "claim-unverified"]

    if "sale" in text or "mise en vente" in text:
        labels.append("sale-listing")
    if "sample" in text or "échantillon" in text:
        labels.append("sample-published")
        return "Claim - Data Sample Published", labels
    if "full leak" in text or "fully published" in text or "publication" in text or "divulgation" in text or "leaked" in text:
        labels.append("data-published")
        return "Claim - Data Sample Published", labels

    return "Claim - Unverified", labels


def normalize_sector(raw: str) -> str:
    value = raw.lower()
    mapping = {
        "healthcare": "healthcare",
        "hospital": "healthcare",
        "santé": "healthcare",
        "insurance": "insurance",
        "assurance": "insurance",
        "finance": "financial-services",
        "financial": "financial-services",
        "bank": "financial-services",
        "education": "education",
        "research": "education",
        "technology": "technology",
        "digital": "technology",
        "seo": "technology",
        "telecom": "telecommunications",
        "telecommunications": "telecommunications",
        "retail": "retail",
        "distribution": "retail",
        "government": "government",
        "public": "government",
        "administration": "government",
        "logistics": "logistics",
        "transport": "transport",
        "tourism": "hospitality",
        "hospitality": "hospitality",
        "oil": "energy",
        "gas": "energy",
        "agriculture": "agriculture",
        "agribusiness": "agriculture",
        "mining": "mining",
        "legal": "legal-services",
        "hr": "professional-services",
        "recruitment": "professional-services",
        "consulting": "professional-services",
    }
    for key, out in mapping.items():
        if key in value:
            return out
    return slugify(raw) or "unknown"


@dataclass
class VictimRecord:
    date_display: str
    date_iso: str
    country: str
    organization: str
    domain: str
    sector: str
    actor: str
    status: str
    description: str


DATE_RE = re.compile(r"^###\s+(.+?)\s*$", re.M)
ENTRY_RE = re.compile(r"^####\s+(.+?)\s*$", re.M)

MONTHS_EN = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
}
MONTHS_FR = {
    "janvier": 1, "février": 2, "fevrier": 2, "mars": 3, "avril": 4, "mai": 5,
    "juin": 6, "juillet": 7, "août": 8, "aout": 8, "septembre": 9, "octobre": 10,
    "novembre": 11, "décembre": 12, "decembre": 12
}


def parse_date_to_iso(date_text: str) -> str:
    text = date_text.strip()
    m = re.match(r"(\d{1,2})\s+([A-Za-zÀ-ÿ]+)\s+(\d{4})", text)
    if not m:
        raise ValueError(f"Unable to parse date: {date_text}")
    day = int(m.group(1))
    month_name = m.group(2).lower()
    year = int(m.group(3))
    month = MONTHS_EN.get(month_name) or MONTHS_FR.get(month_name)
    if not month:
        raise ValueError(f"Unknown month in date: {date_text}")
    return f"{year:04d}-{month:02d}-{day:02d}"


def strip_flag_country_org(header: str) -> Tuple[str, str]:
    text = header.strip()
    text = re.sub(r"^[^\wA-Za-zÀ-ÿ]+", "", text).strip()
    if " - " not in text:
        return "Unknown", text
    country, org = text.split(" - ", 1)
    return country.strip(), org.strip()


def parse_month_victims(md_path: Path) -> List[VictimRecord]:
    text = md_path.read_text(encoding="utf-8")
    date_matches = list(DATE_RE.finditer(text))
    if not date_matches:
        return []

    records: List[VictimRecord] = []

    for idx, dmatch in enumerate(date_matches):
        date_display = dmatch.group(1).strip()
        date_iso = parse_date_to_iso(date_display)
        block_start = dmatch.end()
        block_end = date_matches[idx + 1].start() if idx + 1 < len(date_matches) else len(text)
        date_block = text[block_start:block_end]

        entry_matches = list(ENTRY_RE.finditer(date_block))
        for j, ematch in enumerate(entry_matches):
            header = ematch.group(1).strip()
            entry_start = ematch.end()
            entry_end = entry_matches[j + 1].start() if j + 1 < len(entry_matches) else len(date_block)
            entry_block = date_block[entry_start:entry_end]

            country, organization = strip_flag_country_org(header)
            actor = ""
            sector = ""
            domain = ""
            status = ""
            description = ""

            for line in entry_block.splitlines():
                line = line.strip()
                if not line.startswith("- **"):
                    continue
                key_val = re.match(r"- \*\*(.+?)\*\*:\s*(.+)\s*$", line)
                if not key_val:
                    continue
                key = key_val.group(1).strip().lower()
                val = key_val.group(2).strip()

                if "group" in key or "actor" in key or "cybercriminal" in key:
                    actor = val
                elif "sector" in key:
                    sector = val
                elif "website" in key or "site web" in key:
                    domain = val
                elif "status" in key or "statut" in key:
                    status = val
                elif "victim description" in key or "description victime" in key:
                    description = val

            if not actor:
                actor = "unknown"
            if not sector:
                sector = "unknown"
            if not status:
                status = "Claim - Unverified"

            organization = re.sub(r"\s+\((.*?)\)\s*$", "", organization).strip()

            records.append(
                VictimRecord(
                    date_display=date_display,
                    date_iso=date_iso,
                    country=country,
                    organization=organization,
                    domain=ensure_url(domain),
                    sector=sector,
                    actor=actor.strip(),
                    status=status,
                    description=description.strip(),
                )
            )

    return records


def build_month_bundle(records: List[VictimRecord], year: str, month_dir: str, github_base: str) -> dict:
    source_url = f"{github_base.rstrip('/')}/reports/{year}/{month_dir}"
    source_ref = {"source_name": "AFRINTEL", "url": source_url}

    objects: List[dict] = []
    actor_ids: Dict[str, str] = {}
    victim_ids: Dict[str, str] = {}
    incident_ids: List[str] = []

    report_name = f"AFRINTEL ransomware incidents - {month_dir} {year}"

    for rec in records:
        actor_key = rec.actor.strip()
        if actor_key not in actor_ids:
            actor_id = stix_id("intrusion-set")
            actor_ids[actor_key] = actor_id
            objects.append({
                "type": "intrusion-set",
                "spec_version": "2.1",
                "id": actor_id,
                "created": now_iso(),
                "modified": now_iso(),
                "name": actor_key,
                "description": f"Threat actor or ransomware group referenced by AFRINTEL for {month_dir} {year}.",
                "labels": ["ransomware", "afrintel", slugify(year), slugify(month_dir)],
                "external_references": [source_ref],
            })

        victim_key = f"{rec.organization}|{rec.country}"
        if victim_key not in victim_ids:
            victim_id = stix_id("identity")
            victim_ids[victim_key] = victim_id
            ext_refs = [source_ref]
            if rec.domain:
                ext_refs.append({"source_name": "website", "url": rec.domain})

            objects.append({
                "type": "identity",
                "spec_version": "2.1",
                "id": victim_id,
                "created": now_iso(),
                "modified": now_iso(),
                "name": rec.organization,
                "identity_class": "organization",
                "sectors": [normalize_sector(rec.sector)],
                "description": rec.description or f"Victim organization in {rec.country}.",
                "labels": ["victim", "organization", slugify(rec.country), "afrintel"],
                "external_references": ext_refs,
            })

        normalized_status, incident_labels = normalize_status(rec.status)
        incident_name = f"Ransomware attack against {rec.organization}"

        incident_id = stix_id("incident")
        incident_ids.append(incident_id)
        ext_refs = [source_ref]
        if rec.domain:
            ext_refs.append({"source_name": "website", "url": rec.domain})

        objects.append({
            "type": "incident",
            "spec_version": "2.1",
            "id": incident_id,
            "created": now_iso(),
            "modified": now_iso(),
            "name": incident_name,
            "description": rec.description or f"Claimed ransomware incident affecting {rec.organization} in {rec.country}.",
            "first_seen": f"{rec.date_iso}T00:00:00Z",
            "labels": incident_labels + [slugify(rec.country), normalize_sector(rec.sector)],
            "external_references": ext_refs,
            "extensions": {},
            "x_opencti_incident_type": "ransomware",
            "x_afrintel_status": normalized_status,
            "x_afrintel_country": rec.country,
            "x_afrintel_sector_raw": rec.sector,
            "x_afrintel_date_display": rec.date_display,
        })

        objects.append({
            "type": "relationship",
            "spec_version": "2.1",
            "id": stix_id("relationship"),
            "created": now_iso(),
            "modified": now_iso(),
            "relationship_type": "attributed-to",
            "source_ref": incident_id,
            "target_ref": actor_ids[actor_key],
        })

        objects.append({
            "type": "relationship",
            "spec_version": "2.1",
            "id": stix_id("relationship"),
            "created": now_iso(),
            "modified": now_iso(),
            "relationship_type": "targets",
            "source_ref": actor_ids[actor_key],
            "target_ref": victim_ids[victim_key],
        })

        objects.append({
            "type": "relationship",
            "spec_version": "2.1",
            "id": stix_id("relationship"),
            "created": now_iso(),
            "modified": now_iso(),
            "relationship_type": "targets",
            "source_ref": incident_id,
            "target_ref": victim_ids[victim_key],
        })

    report_id = stix_id("report")
    object_refs = list(actor_ids.values()) + list(victim_ids.values()) + incident_ids
    first_seen_dates = sorted({r.date_iso for r in records})
    published = f"{first_seen_dates[0]}T00:00:00Z" if first_seen_dates else now_iso()

    objects.append({
        "type": "report",
        "spec_version": "2.1",
        "id": report_id,
        "created": now_iso(),
        "modified": now_iso(),
        "name": report_name,
        "description": f"AFRINTEL monthly ransomware/extortion victim dataset for {month_dir} {year}.",
        "report_types": ["threat-report"],
        "published": published,
        "labels": ["afrintel", "monthly-report", slugify(year), slugify(month_dir)],
        "object_refs": object_refs,
        "external_references": [source_ref],
    })

    return {
        "type": "bundle",
        "id": stix_id("bundle"),
        "objects": objects,
    }


def process_month(repo: Path, year: str, month_dir: str, github_base: str, output_root: Optional[Path] = None) -> Path:
    month_path = repo / "reports" / year / month_dir
    victims_md = month_path / "victims.md"

    if not victims_md.exists():
        raise FileNotFoundError(f"victims.md not found: {victims_md}")

    records = parse_month_victims(victims_md)
    if not records:
        raise ValueError(f"No victim records parsed from {victims_md}")

    bundle = build_month_bundle(records, year, month_dir, github_base)

    out_root = output_root or (repo / "stix" / year / month_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    month_slug = month_dir.split("-", 1)[1] if "-" in month_dir else month_dir
    out_path = out_root / f"afrintel_{month_slug}_{year}_opencti.json"
    out_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False), encoding="utf-8")
    return out_path


def find_month_dirs(reports_year_path: Path) -> List[str]:
    months = []
    for child in sorted(reports_year_path.iterdir()):
        if child.is_dir() and re.match(r"^\d{2}-", child.name):
            months.append(child.name)
    return months


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate AFRINTEL OpenCTI STIX bundles from victims.md files.")
    parser.add_argument("--repo", required=True, help="Path to AFRINTEL repository root")
    parser.add_argument("--year", help="Specific year, e.g. 2025")
    parser.add_argument("--month", help="Specific month folder, e.g. 01-january")
    parser.add_argument(
        "--github-base",
        default="https://github.com/Hatchepsoute/AFRINTEL/tree/main",
        help="Base GitHub URL used to build source references",
    )
    parser.add_argument(
        "--output-root",
        help="Optional custom output root. Default: <repo>/stix/<year>/<month>/",
    )

    args = parser.parse_args()
    repo = Path(args.repo).resolve()

    reports_root = repo / "reports"
    if not reports_root.exists():
        print(f"[ERROR] reports directory not found: {reports_root}", file=sys.stderr)
        return 1

    output_root = Path(args.output_root).resolve() if args.output_root else None
    generated: List[Path] = []

    years = [args.year] if args.year else [p.name for p in sorted(reports_root.iterdir()) if p.is_dir()]
    for year in years:
        year_path = reports_root / year
        if not year_path.exists():
            print(f"[WARN] year not found: {year_path}", file=sys.stderr)
            continue

        months = [args.month] if args.month else find_month_dirs(year_path)
        for month_dir in months:
            month_path = year_path / month_dir
            if not month_path.exists():
                print(f"[WARN] month not found: {month_path}", file=sys.stderr)
                continue
            try:
                out = process_month(repo, year, month_dir, args.github_base, output_root)
                generated.append(out)
                print(f"[OK] Generated: {out}")
            except Exception as exc:
                print(f"[ERROR] {year}/{month_dir}: {exc}", file=sys.stderr)

    if not generated:
        print("[ERROR] No STIX bundles generated.", file=sys.stderr)
        return 2

    print(f"\nGenerated {len(generated)} bundle(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
