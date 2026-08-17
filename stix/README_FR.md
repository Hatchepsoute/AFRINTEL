![STIX Dataset](https://img.shields.io/badge/CTI-STIX%202.1-purple)
![OpenCTI](https://img.shields.io/badge/Platform-OpenCTI-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)

# AFRINTEL - Jeu de données Threat Intelligence (STIX)
👉🏾 [**English version available here**](./README.md)

Ce répertoire contient des jeux de données de Cyber Threat Intelligence (CTI) structurés, générés à partir de la surveillance des activités ransomware AFRINTEL.

Tous les bundles sont fournis au format **STIX 2.1**, prêts à être ingérés dans des plateformes CTI comme **OpenCTI**, **MISP** ou tout outil compatible STIX.

---

## Objectif

Les datasets STIX AFRINTEL transforment des observations OSINT brutes en renseignement exploitable :

```text
victims.md → CTI structuré → STIX 2.1 → OpenCTI / SOC
```

Ces données permettent :

- le suivi des groupes ransomware
- l’enrichissement des victimes
- la corrélation de campagnes
- l’exploitation opérationnelle en SOC
- le threat hunting et l’investigation

---

## 📦 Contenu des datasets

Chaque bundle STIX peut contenir :

- `threat-actor` → groupes ransomware, acteurs malveillants ou personas de publication
- `identity` → organisations victimes
- `incident` → événements ransomware
- `relationship` → liens acteur ↔ victime ↔ incident
- `report` → rapport mensuel AFRINTEL

---

## 📊 Datasets disponibles


### AFRINTEL 2026

| Période | Bundle STIX |
|------|------|
| Premier semestre 2026 | [afrintel_h1_2026_opencti.json](https://raw.githubusercontent.com/Hatchepsoute/AFRINTEL/refs/heads/main/stix/2026/afrintel_h1_2026_opencti.json) |
| Janvier 2026 | [afrintel_january_2026_opencti.json](./2026/01-january/afrintel_january_2026_opencti.json) |
| Février 2026 | [afrintel_february_2026_opencti.json](./2026/02-february/afrintel_february_2026_opencti.json) |
| Mars 2026 | [afrintel_march_2026_opencti.json](./2026/03-march/afrintel_march_2026_opencti.json) |
| Avril 2026 | [afrintel_april_2026_opencti.json](./2026/04-april/afrintel_april_2026_opencti.json) |
| Mai 2026 | [afrintel_may_2026_opencti.json](./2026/05-may/afrintel_may_2026_opencti.json) |
| Juin 2026 | [afrintel_june_2026_opencti.json](./2026/06-june/afrintel_june_2026_opencti.json) |
| Juillet 2026 | [afrintel_july_2026_opencti.json](./2026/07-july/afrintel_july_2026_opencti.json) |

### AFRINTEL 2025

| Mois | Bundle STIX |
|------|------|
| Janvier 2025 | [afrintel_january_2025_opencti.json](./2025/01-january/afrintel_january_2025_opencti.json) |
| Février 2025 | [afrintel_february_2025_opencti.json](./2025/02-february/afrintel_february_2025_opencti.json) |
| Mars 2025 | [afrintel_march_2025_opencti.json](./2025/03-march/afrintel_march_2025_opencti.json) |
| Avril 2025 | [afrintel_april_2025_opencti.json](./2025/04-april/afrintel_april_2025_opencti.json) |
| Mai 2025 | [afrintel_may_2025_opencti.json](./2025/05-may/afrintel_may_2025_opencti.json) |
| Juin 2025 | [afrintel_june_2025_opencti.json](./2025/06-june/afrintel_june_2025_opencti.json) |
| Juillet 2025 | [afrintel_july_2025_opencti.json](./2025/07-july/afrintel_july_2025_opencti.json) |
| Août 2025 | [afrintel_august_2025_opencti.json](./2025/08-august/afrintel_august_2025_opencti.json) |
| Septembre 2025 | [afrintel_september_2025_opencti.json](./2025/09-september/afrintel_september_2025_opencti.json) |
| Octobre 2025 | [afrintel_october_2025_opencti.json](./2025/10-october/afrintel_october_2025_opencti.json) |
| Novembre 2025 | [afrintel_november_2025_opencti.json](./2025/11-november/afrintel_november_2025_opencti.json) |
| Décembre 2025 | [afrintel_december_2025_opencti.json](./2025/12-december/afrintel_december_2025_opencti.json) |
| Liste des victimes 2025 (EN) | [afrintel_2025_victims_EN_opencti.json](./2025/afrintel_2025_victims_EN_opencti.json) |
| Liste des victimes 2025 (FR) | [afrintel_2025_victims_FR_opencti.json](./2025/afrintel_2025_victims_FR_opencti.json) |

### AFRINTEL 2024

Les deux fichiers de rapport CTI ci-dessous sont des documents JSON analytiques, pas des bundles STIX. Les exports de victimes et les fichiers mensuels sont des bundles STIX 2.1 régénérés depuis les fiches sources bilingues.


| Dataset | Bundle STIX |
|------|------|
| Bundles mensuels 2024 | [Janvier](./2024/01-january/afrintel_january_2024_opencti.json) · [Février](./2024/02-february/afrintel_february_2024_opencti.json) · [Mars](./2024/03-march/afrintel_march_2024_opencti.json) · [Avril](./2024/04-april/afrintel_april_2024_opencti.json) · [Mai](./2024/05-may/afrintel_may_2024_opencti.json) · [Juin](./2024/06-june/afrintel_june_2024_opencti.json) · [Juillet](./2024/07-july/afrintel_july_2024_opencti.json) · [Août](./2024/08-august/afrintel_august_2024_opencti.json) · [Septembre](./2024/09-september/afrintel_september_2024_opencti.json) · [Octobre](./2024/10-october/afrintel_october_2024_opencti.json) · [Novembre](./2024/11-november/afrintel_november_2024_opencti.json) · [Décembre](./2024/12-december/afrintel_december_2024_opencti.json) |
| Liste des victimes 2024 (EN) | [afrintel_2024_victims_EN_opencti.json](./2024/afrintel_2024_victims_EN_opencti.json) |
| Liste des victimes 2024 (FR) | [afrintel_2024_victims_FR_opencti.json](./2024/afrintel_2024_victims_FR_opencti.json) |
| Rapport CTI analytique 2024 (EN, JSON non-STIX) | [AFRINTEL_CTI_report_2024_en.json](./2024/AFRINTEL_CTI_report_2024_en.json) |
| Rapport CTI analytique 2024 (FR, JSON non-STIX) | [AFRINTEL_CTI_report_2024_fr.json](./2024/AFRINTEL_CTI_report_2024_fr.json) |

---

## 🛡️ Cas d’usage

Ces datasets peuvent être utilisés dans :

- OpenCTI
- MISP
- Maltego
- SIEM / SOC

Exemples d’usage :

- enrichissement des alertes
- corrélation acteur ↔ victime
- tracking de campagnes ransomware
- support à l’investigation SOC
---

## 🚀 Roadmap

- génération automatique via GitHub Actions
- export MISP natif
- enrichissement IoC (IP, domaines, hash)
- mapping MITRE ATT&CK
- clustering de campagnes
---
**AFRINTEL - Industrialisation du renseignement ransomware en Afrique.**
