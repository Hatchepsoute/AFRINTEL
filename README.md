![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen)
![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet)
![Focus](https://img.shields.io/badge/Focus-Ransomware%20%26%20Data%20Leaks-red)
![Dark Web](https://img.shields.io/badge/Data%20Source-Dark%20Web%20%2F%20OSINT-black)
![Project](https://img.shields.io/badge/Project-AFRINTEL-black)
![License](https://img.shields.io/badge/License-MIT-blue)

<p align="left">
<img src="comparison/afrintel_logo.png" width="90" align="left" style="margin-right:15px"/>

# AFRINTEL - African Threat Intelligence
</p>

👉🏾 [Version française](README_FR.md)

---

**AFRINTEL** is an open-source CTI project tracking cyberattacks targeting African organizations: ransomware, data leaks, access sales, and underground marketplace activity across 54 countries, monitored from dark web sources, leak sites, and OSINT.

| Countries monitored | Threat actors tracked | Period covered | Formats |
| :---: | :---: | :---: | :---: |
| 54 | 100+ | 2024-2026 | Markdown, STIX 2.1, Visual CTI |

> All claims from leak sites and underground forums are treated as unverified unless independently corroborated.

---

## Cyber threats in Africa - June 2026

June 2026 recorded **40 publicly claimed cyber incidents**: ransomware reached parity with data leaks for the first time in 2026 (20/20, up from 28% ransomware in May). Morocco (9 incidents) was the most targeted country, driven almost entirely by a single actor cluster, anisanas2, active for a third consecutive month. The month's most severe incidents include a severe biometric/KYC data exposure at Nigerian fintech Jeroid.co, a plaintext credential leak from the Nigerian Army's webmail domain, and a reported 10.2M-record exposure at Tanzania's business registration agency (BRELA).

📄 [Full CTI report - June 2026](CyberAttackAfrica/2026/06-june/README.md)
📋 [Victim list - June 2026](CyberAttackAfrica/2026/06-june/victims.md)

---

## Monthly CTI reports

| Month | FR | EN |
| :--- | :--- | :--- |
| January 2026 | [Rapport](CyberAttackAfrica/2026/01-january/README_FR.md) | [Report](CyberAttackAfrica/2026/01-january/README.md) |
| February 2026 | [Rapport](CyberAttackAfrica/2026/02-february/README_FR.md) | [Report](CyberAttackAfrica/2026/02-february/README.md) |
| March 2026 | [Rapport](CyberAttackAfrica/2026/03-march/README_FR.md) | [Report](CyberAttackAfrica/2026/03-march/README.md) |
| April 2026 | [Rapport](CyberAttackAfrica/2026/04-april/README_FR.md) | [Report](CyberAttackAfrica/2026/04-april/README.md) |
| May 2026 | [Rapport](CyberAttackAfrica/2026/05-may/README_FR.md) | [Report](CyberAttackAfrica/2026/05-may/README.md) |
| June 2026 | [Rapport](CyberAttackAfrica/2026/06-june/README_FR.md) | [Report](CyberAttackAfrica/2026/06-june/README.md) |
| July 2026 | *in progress* | *in progress* |

---

## Statistics

| Month | FR | EN |
| :--- | :--- | :--- |
| January 2026 | [Statistiques](statistics/2026/01-january/README_FR.md) | [Statistics](statistics/2026/01-january/README.md) |
| February 2026 | [Statistiques](statistics/2026/02-february/README_FR.md) | [Statistics](statistics/2026/02-february/README.md) |
| March 2026 | [Statistiques](statistics/2026/03-march/README_FR.md) | [Statistics](statistics/2026/03-march/README.md) |
| April 2026 | [Statistiques](statistics/2026/04-april/README_FR.md) | [Statistics](statistics/2026/04-april/README.md) |
| May 2026 | [Statistiques](statistics/2026/05-may/README_FR.md) | [Statistics](statistics/2026/05-may/README.md) |
| June 2026 | [Statistiques](statistics/2026/06-june/README_FR.md) | [Statistics](statistics/2026/06-june/README.md) |
| July 2026 | *in progress* | *in progress* |

---

## Month-over-month comparisons

| Comparison | FR | EN |
| :--- | :--- | :--- |
| January vs February 2026 | [FR](comparison/2026/01-january-february/README_FR.md) | [EN](comparison/2026/01-january-february/README.md) |
| February vs March 2026 | [FR](comparison/2026/02-february-march/README_FR.md) | [EN](comparison/2026/02-february-march/README.md) |
| March vs April 2026 | [FR](comparison/2026/03-march-april/README_FR.md) | [EN](comparison/2026/03-march-april/README.md) |
| April vs May 2026 | [FR](comparison/2026/04-april-may/README_FR.md) | [EN](comparison/2026/04-april-may/README.md) |
| May vs June 2026 | [FR](comparison/2026/05-may-june/README_FR.md) | [EN](comparison/2026/05-may-june/README.md) |
| H1 2026 report | [FR](comparison/2026/01-january-june/README_FR.md) | [EN](comparison/2026/01-january-june/README.md) |


---

## Visual intelligence

📊 [May 2026 dashboard](visual-intelligence/05-may/README.md) — ecosystem maps, actor diagrams, country hotspots, sector exposure

📊 [April 2026 dashboard](visual-intelligence/04-april/README.md)

---

## STIX / OpenCTI datasets

| Dataset | File |
| :--- | :--- |
| January 2026 | [STIX Bundle](stix/2026/01-january/afrintel_january_2026_opencti.json) |
| February 2026 | [STIX Bundle](stix/2026/02-february/afrintel_february_2026_opencti.json) |
| March 2026 | [STIX Bundle](stix/2026/03-march/afrintel_march_2026_opencti.json) |
| April 2026 | [STIX Bundle](stix/2026/04-april/afrintel_april_2026_opencti.json) |
| May 2026 | [STIX Bundle](stix/2026/05-may/afrintel_may_2026_opencti.json) |
| June 2026 | [STIX Bundle](stix/2026/06-june/afrintel_june_2026_opencti.json) |

STIX 2.1 bundles are compatible with OpenCTI and include threat actors, victims, targeted sectors, and contextual MITRE ATT&CK mapping.

---

## Project structure

```text
AFRINTEL/
├── CyberAttackAfrica/   # Monthly victim lists and CTI reports (2024-2026)
├── statistics/          # Monthly statistics
├── comparison/          # Month-over-month comparisons
├── visual-intelligence/ # Ecosystem maps and diagrams
├── stix/                # STIX 2.1 / OpenCTI bundles
├── scripts/             # Validation and utility scripts
└── workflows/           # Automation workflows
```

---

## Author

**Adama ASSIONGBON** - SOC & Cyber Threat Intelligence Consultant

🔗 [LinkedIn](https://www.linkedin.com/in/adama-assiongbon-9029893a/) | 📄 [MIT License](LICENSE)
