# ⚙️ AFRINTEL Automation Scripts

This directory contains automation tools designed to transform AFRINTEL datasets into actionable Cyber Threat Intelligence (CTI) formats.

These scripts enable seamless integration with platforms such as **OpenCTI**, **MISP**, and SIEM/SOC environments.

---

##  Available scripts

### `afrintel_victims_to_stix.py`

Convert AFRINTEL bilingual victim datasets and analytical reports into **STIX 2.1 bundles** compatible with OpenCTI.

---

## Purpose

This script is a core component of the AFRINTEL intelligence pipeline:

```text
OSINT (victims.md) → Structured CTI → STIX 2.1 → OpenCTI / SOC
```

It allows analysts to operationalize publicly observed ransomware activity into structured intelligence.

---

## 🔍 Features

* 📥 Parses AFRINTEL monthly datasets (`victims.md` and `victims_FR.md`)
* 📊 Includes monthly CTI reports and statistics in English and French
* 📈 Includes the previous-to-current month comparison in the current month's bundle
*  Extracts:

  * Threat actors (ransomware groups)
  * Victim organizations
  * Sectors and countries
  * Attack dates and status
*  Generates STIX 2.1 objects:

  * `threat-actor`
  * `identity`
  * `incident`
  * `relationship`
  * `report`
* 🔗 Automatically includes AFRINTEL source references
* 📂 Outputs ready-to-import bundles for OpenCTI

---

## 📁 Expected Repository Structure

```bash
CyberAttackAfrica/
└── 2026/
    ├── 01-january/
    │   ├── victims.md
    │   ├── victims_FR.md
    │   ├── README.md
    │   └── README_FR.md
    ├── 05-may/
    │   ├── victims.md
    │   ├── victims_FR.md
    │   ├── README.md
    │   └── README_FR.md
    └── ...
statistics/
└── 2026/
    └── 05-may/
        ├── README.md
        └── README_FR.md
comparison/
└── 2026/
    └── 04-april-may/
        ├── README.md
        └── README_FR.md
```

---

## ⚙️ Usage

### ▶️ Run for all data

```bash
python3 scripts/afrintel_victims_to_stix.py --repo .
```

---

### 📅 Run for a specific year

```bash
python3 scripts/afrintel_victims_to_stix.py --repo . --year 2026
```

---

### 📆 Run for a specific month

```bash
python3 scripts/afrintel_victims_to_stix.py --repo . --year 2026 --month 05-may
```

---

### Generate the first-half bundle

```bash
python3 scripts/afrintel_victims_to_stix.py --repo . --year 2026 --h1
```

The H1 bundle merges the January through June objects without changing their STIX IDs. It also includes the bilingual first-half reports, monthly statistics and month-over-month comparisons.

---

## 📦 Output

Generated STIX bundles are stored in:

```bash
stix/<year>/<month>/afrintel_<month>_<year>_opencti.json
```

Example:

```bash
stix/2026/05-may/afrintel_may_2026_opencti.json
```

First-half output:

```bash
stix/2026/afrintel_h1_2026_opencti.json
```

---

## CTI / SOC Integration

This script enables:

* 📊 Threat intelligence ingestion into OpenCTI
* 🔄 Correlation with existing CTI datasets
* 🛡️ Enrichment of SOC detections (SIEM, EDR, XDR)
* 📈 Strategic ransomware activity tracking across Africa

---

##  Future enhancements

* GitHub Actions automation (auto-generate STIX on commit)
* Direct OpenCTI connector integration
* Export to MISP format
* IOC extraction (IPs, domains, hashes)
* Timeline & campaign correlation

---

## 🛠️ Requirements

* Python 3.8+
* No external dependencies (standard library only)

---

## 📜 License

This script is part of the AFRINTEL project and is released under the MIT License.

---

## 🤝🏿 Contribution

Contributions are welcome to improve parsing, enrich data, and expand CTI capabilities.

---

**AFRINTEL - Turning African cyber threat signals into actionable intelligence.**
