![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen)
![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet)
![Focus](https://img.shields.io/badge/Focus-Ransomware%20Monitoring-red)
![Threat Landscape](https://img.shields.io/badge/Threat%20Landscape-Africa-orange)
![Dark Web](https://img.shields.io/badge/Data%20Source-Dark%20Web-black)
![Deep Web](https://img.shields.io/badge/Data%20Source-Deep%20Web-darkgrey)
![OSINT](https://img.shields.io/badge/Data%20Source-OSINT-blue)
![Project](https://img.shields.io/badge/Project-AFRINTEL-black)
![License](https://img.shields.io/badge/License-MIT-blue)

<p align="left">
<img src="comparison/afrintel_logo.png" width="90" align="left" style="margin-right:15px"/>

# AFRINTEL - African Threat Intelligence
</p>

👉🏾 [French version](README_FR.md)

---

## 🌍 About AFRINTEL

**AFRINTEL** is an open-source **Cyber Threat Intelligence (CTI)** initiative dedicated to tracking, documenting, and analyzing cyberattacks targeting organizations across Africa.

The project focuses on:

- ransomware operations
- data leaks and extortion campaigns
- initial access broker (IAB) activity
- underground marketplace monitoring
- cybercriminal ecosystem mapping
- Africa-focused CTI reporting

AFRINTEL analysis relies on monitoring:

- ransomware leak sites (**dark web**)
- underground cybercriminal forums
- data broker marketplaces
- exposed database listings
- public OSINT sources
- Telegram and underground channels

The objective is to provide **strategic visibility on cyber threats affecting the African continent**.

---

## 🔬 Methodology

AFRINTEL tracks publicly claimed cyber incidents affecting African organizations.

### Sources

- Ransomware leak sites (DLS)
- Underground forums
- Data broker marketplaces
- Telegram channels
- Open-source intelligence (OSINT)

### Classification

- **Ransomware** → encryption and extortion activity
- **Data Leak** → data exposure, database publication or sale
- **Access Sale** → sale of compromised access to systems/networks

### Reliability Note

Leak-site publications and underground claims are treated as:

```text
Claim - Unverified
```

unless corroborated by:

- victim confirmation
- technical evidence
- validated data samples
- multiple trusted sources

---

## 📊 AFRINTEL Coverage

| Category | Coverage |
|---|---|
| African countries monitored | 54 |
| Threat actors tracked | 100+ |
| Ransomware groups monitored | 70+ |
| Data leak actors monitored | 50+ |
| Years covered | 2024 - 2026 |
| Intelligence formats | Markdown / STIX / Visual CTI |

---

## 🚨 Latest Intelligence

### April 2026 Highlights

- 60 publicly claimed cyber incidents across Africa
- Morocco, Egypt, and South Africa remain primary hotspots
- Surge in data broker and initial access broker activity
- Government and healthcare sectors heavily targeted
- Large-scale KYC and identity document exposure observed
- Kenya Airports Authority claimed compromise (2 TB)
- CNSS Benin mailbox scraping campaign documented

📄 [Read April 2026 CTI Report](CyberAttackAfrica/2026/04-april/README.md)

---

## 📊 Monthly CTI Reports

| Month | French | English |
|------|--------|--------|
| **January 2026** | [Voir le rapport](CyberAttackAfrica/2026/01-january/README_FR.md) | [View report](CyberAttackAfrica/2026/01-january/README.md) |
| **February 2026** | [Voir le rapport](CyberAttackAfrica/2026/02-february/README_FR.md) | [View report](CyberAttackAfrica/2026/02-february/README.md) |
| **March 2026** | [Voir le rapport](CyberAttackAfrica/2026/03-march/README_FR.md) | [View report](CyberAttackAfrica/2026/03-march/README.md) |
| **April 2026** | [Voir le rapport](CyberAttackAfrica/2026/04-april/README_FR.md) | [View report](CyberAttackAfrica/2026/04-april/README.md) |

---

## 📈 Statistics & Trend Analysis

| Month | French | English |
|------|--------|--------|
| **January 2026** | [Statistics](statistics/2026/01-january/README_FR.md) | [Statistics](statistics/2026/01-january/README.md) |
| **February 2026** | [Statistics](statistics/2026/02-february/README_FR.md) | [Statistics](statistics/2026/02-february/README.md) |
| **March 2026** | [Statistics](statistics/2026/03-march/README_FR.md) | [Statistics](statistics/2026/03-march/README.md) |
| **April 2026** | [Statistics](statistics/2026/04-april/README_FR.md) | [Statistics](statistics/2026/04-april/README.md) |

---

## 🔍 Comparative Intelligence Analysis

| Comparison | French | English |
|---|---|---|
| January vs February 2026 | [FR](comparison/2026/01-january-february/README_FR.md) | [EN](comparison/2026/01-january-february/README.md) |
| February vs March 2026 | [FR](comparison/2026/02-february-march/README_FR.md) | [EN](comparison/2026/02-february-march/README.md) |
| March vs April 2026 | [FR](comparison/2026/03-march-april/README_FR.md) | [EN](comparison/2026/03-march-april/README.md) |

Focus areas:

- ransomware ecosystem evolution
- targeted countries and sectors
- actor operational patterns
- regional threat escalation
- leak market evolution

---

## 🧠 Visual Intelligence

📊 [Visual Intelligence Dashboard](visual-intelligence/04-april/README.md)

Includes:

- Africa cyber threat maps
- actor → victim → country diagrams
- ransomware vs leak heatmaps
- sector intelligence mapping
- regional exposure visualization
- threat actor ecosystem mapping

### CTI Ecosystem Maps

- [April 2026 Ecosystem Map](visual-intelligence/04-april/ecosystem-map_april_2026.md)
- [Ransomware vs Leaks](visual-intelligence/04-april/ransomware-vs-leaks_april_2026.md)
- [Country Hotspots](visual-intelligence/04-april/country-hotspots_april_2026.md)
- [Sector Map](visual-intelligence/04-april/sector-map_april_2026.md)

---

## 📦 STIX / OpenCTI Intelligence Datasets

AFRINTEL provides structured CTI datasets in **STIX 2.1 / OpenCTI-ready format**.

### Available STIX Bundles

| Dataset | File |
|---|---|
| January 2026 | [STIX Bundle](stix/2026/01-january/afrintel_january_2026_opencti.json) |
| February 2026 | [STIX Bundle](stix/2026/02-february/afrintel_february_2026_opencti.json) |
| March 2026 | [STIX Bundle](stix/2026/03-march/afrintel_march_2026_opencti.json) |
| April 2026 | [STIX Bundle](stix/2026/04-april/afrintel_april_2026_opencti.json) |

These datasets contain:

- threat actors
- ransomware groups
- victims
- targeted sectors
- geographic intelligence
- contextual MITRE ATT&CK mapping

---

## 📂 Project Structure

```text
AFRINTEL
├── comparison/
├── CyberAttackAfrica/
│   ├── 2024/
│   ├── 2025/
│   └── 2026/
├── scripts/
├── statistics/
├── stix/
├── visual-intelligence/
├── workflows/
├── README.md
├── README_FR.md
└── LICENSE
```

---

## 🛡️ Strategic Goals

AFRINTEL aims to:

- improve visibility on cyber threats targeting Africa
- document ransomware and extortion ecosystems
- support SOC and CTI teams with actionable intelligence
- facilitate OpenCTI/STIX enrichment workflows
- promote Africa-focused cyber threat research
- strengthen regional cyber threat awareness

---

## 📄 License

MIT License - see [LICENSE](LICENSE)

---

## ✍🏿 Author

**Adama ASSIONGBON**

Consultant SOC & Cyber Threat Intelligence

🔗 [LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)

---

*AFRINTEL - Open African CTI Monitoring Initiative*
