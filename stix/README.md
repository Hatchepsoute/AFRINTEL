![STIX Dataset](https://img.shields.io/badge/CTI-STIX%202.1-purple)
![OpenCTI](https://img.shields.io/badge/Platform-OpenCTI-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)

# AFRINTEL Threat Intelligence dataset (STIX)
👉🏾 [**French version available here**](./README_FR.md)

This directory contains structured Cyber Threat Intelligence datasets generated from AFRINTEL ransomware monitoring.

All bundles are provided in **STIX 2.1 format** and are designed for direct ingestion into CTI platforms such as **OpenCTI**, **MISP**, and other STIX-compatible environments.

---

## Purpose

AFRINTEL STIX datasets transform raw ransomware victim tracking into structured intelligence that can be operationalized by CTI and SOC teams.

```text
victims.md → Structured CTI → STIX 2.1 → OpenCTI / SOC
```

These datasets support:

- threat actor tracking
- victim intelligence enrichment
- campaign correlation
- operational CTI workflows
- SOC enrichment and investigation

---

## Dataset content

Each STIX bundle may include:

- `intrusion-set` → ransomware groups or malicious actors
- `identity` → victim organizations
- `incident` → ransomware incidents
- `relationship` → actor ↔ victim ↔ incident links
- `report` → AFRINTEL monthly threat report object

---

## Available datasets


### AFRINTEL 2026

| Period | STIX Bundle |
|------|------|
| First half of 2026 | [afrintel_h1_2026_opencti.json](https://raw.githubusercontent.com/Hatchepsoute/AFRINTEL/refs/heads/main/stix/2026/afrintel_h1_2026_opencti.json) |
| January 2026 | [afrintel_january_2026_opencti.json](./2026/01-january/afrintel_january_2026_opencti.json) |
| February 2026 | [afrintel_february_2026_opencti.json](./2026/02-february/afrintel_february_2026_opencti.json) |
| March 2026 | [afrintel_march_2026_opencti.json](./2026/03-march/afrintel_march_2026_opencti.json) |
| April 2026 | [afrintel_april_2026_opencti.json](./2026/04-april/afrintel_april_2026_opencti.json) |
| May 2026 | [afrintel_may_2026_opencti.json](./2026/05-may/afrintel_may_2026_opencti.json) |
| June 2026 | [afrintel_june_2026_opencti.json](./2026/06-june/afrintel_june_2026_opencti.json) |
| July 2026 | [afrintel_july_2026_opencti.json](./2026/07-july/afrintel_july_2026_opencti.json) |

### AFRINTEL 2025

| Month | STIX Bundle |
|------|------|
| January 2025 | [afrintel_january_2025_opencti.json](./2025/01-january/afrintel_january_2025_opencti.json) |
| February 2025 | [afrintel_february_2025_opencti.json](./2025/02-february/afrintel_february_2025_opencti.json) |
| March 2025 | [afrintel_march_2025_opencti.json](./2025/03-march/afrintel_march_2025_opencti.json) |
| April 2025 | [afrintel_april_2025_opencti.json](./2025/04-april/afrintel_april_2025_opencti.json) |
| May 2025 | [afrintel_may_2025_opencti.json](./2025/05-may/afrintel_may_2025_opencti.json) |
| June 2025 | [afrintel_june_2025_opencti.json](./2025/06-june/afrintel_june_2025_opencti.json) |
| July 2025 | [afrintel_july_2025_opencti.json](./2025/07-july/afrintel_july_2025_opencti.json) |
| August 2025 | [afrintel_august_2025_opencti.json](./2025/08-august/afrintel_august_2025_opencti.json) |
| September 2025 | [afrintel_september_2025_opencti.json](./2025/09-september/afrintel_september_2025_opencti.json) |
| October 2025 | [afrintel_october_2025_opencti.json](./2025/10-october/afrintel_october_2025_opencti.json) |
| November 2025 | [afrintel_november_2025_opencti.json](./2025/11-november/afrintel_november_2025_opencti.json) |
| December 2025 | [afrintel_december_2025_opencti.json](./2025/12-december/afrintel_december_2025_opencti.json) |

### AFRINTEL 2024

| Dataset | STIX Bundle |
|------|------|
| 2024 Victim List (EN) | [afrintel_2024_victims_EN_opencti.json](./2024/afrintel_2024_victims_EN_opencti.json) |
| 2024 Victim List (FR) | [afrintel_2024_victims_FR_opencti.json](./2024/afrintel_2024_victims_FR_opencti.json) |
| 2024 CTI Report (EN) | [AFRINTEL_CTI_report_2024_en.json](./2024/AFRINTEL_CTI_report_2024_en.json) |
| 2024 CTI Report (FR) | [AFRINTEL_CTI_report_2024_fr.json](./2024/AFRINTEL_CTI_report_2024_fr.json) |

---


## Integration use cases

These datasets can be imported into:

- **OpenCTI**
- **MISP**
- **Maltego**
- other **STIX-compatible CTI platforms**

They can also support SOC workflows such as:

- intelligence enrichment
- actor-to-victim correlation
- campaign tracking
- case triage support
---

## Roadmap

- automated STIX generation via GitHub Actions
- MISP export support
- IOC extraction enrichment
- ATT&CK mapping enrichment
- campaign clustering and timeline analysis

---
**AFRINTEL - Operationalizing ransomware intelligence across Africa.**
