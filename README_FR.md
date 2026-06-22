![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen)
![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet)
![Project](https://img.shields.io/badge/Project-AFRINTEL-black)
![Dark Web](https://img.shields.io/badge/Source-Dark%20Web%20%2F%20OSINT-black)
![License](https://img.shields.io/badge/Licence-MIT-blue)

<p align="left">
<img src="comparison/afrintel_logo.png" width="90" align="left" style="margin-right:15px"/>

# AFRINTEL - African Threat Intelligence
</p>

👉🏾 [English version](README.md)

---

**AFRINTEL** est un projet CTI open source dédié au suivi des cyberattaques visant les organisations africaines : ransomwares, fuites de données, ventes d'accès et activité des marchés underground, sur 54 pays, via des sources dark web, leak sites et OSINT.

| Pays surveillés | Acteurs suivis | Période couverte | Formats |
| :---: | :---: | :---: | :---: |
| 54 | 100+ | 2024-2026 | Markdown, STIX 2.1, Visual CTI |

> Toutes les publications issues de leak sites et forums underground sont traitées comme des revendications non vérifiées, sauf corroboration indépendante.

---

## Dernières analyses

### Mai 2026

- **54 incidents** en Afrique | Égypte (16) et Afrique du Sud (14) concentrent 56 % des incidents
- Secteur éducatif égyptien : 28 millions d'enregistrements élèves et enseignants exposés
- Coalition OpSouthAfrica : 8 institutions publiques sud-africaines ciblées
- Trésor Public du Sénégal : ransomware AuditTeam, ~1,66 million d'enregistrements exfiltrés
- Databasehooligan : 8 victimes dans 4 pays
- Messagerie de la police tanzanienne : 10 000 comptes officiers avec mots de passe en clair mis en vente

📄 [Rapport CTI mai 2026](CyberAttackAfrica/2026/05-may/README_FR.md)

---

### Juin 2026 (collecte en cours - au 22 juin 2026)

- **5 incidents** | Fuites de données et ventes d'accès uniquement, 0 ransomware
- **Jeroid.co (Nigéria) :** 312 433 utilisateurs, 759 900 portefeuilles (TVL 306 M$), 110 282 BVN, 64 300 NIN, 70 956 photos biométriques sur un bucket S3 public
- **Ventes d'identifiants forces de l'ordre :** deux acteurs ("Convince" et "Governor") vendent des accès EDR/LEP ciblant au moins 11 pays africains
- **NILDS Nigéria :** institution de recherche parlementaire revendiquée par 404Crew CT x NullSec Nigeria
- **Base de données pilotes égyptiens :** données de personnel aviation militaire et civile mises en vente

📄 [Incidents de juin 2026](CyberAttackAfrica/2026/06-june/victims_FR.md)

---

## Rapports mensuels CTI

| Mois | FR | EN |
| :--- | :--- | :--- |
| Janvier 2026 | [Rapport](CyberAttackAfrica/2026/01-january/README_FR.md) | [Report](CyberAttackAfrica/2026/01-january/README.md) |
| Février 2026 | [Rapport](CyberAttackAfrica/2026/02-february/README_FR.md) | [Report](CyberAttackAfrica/2026/02-february/README.md) |
| Mars 2026 | [Rapport](CyberAttackAfrica/2026/03-march/README_FR.md) | [Report](CyberAttackAfrica/2026/03-march/README.md) |
| Avril 2026 | [Rapport](CyberAttackAfrica/2026/04-april/README_FR.md) | [Report](CyberAttackAfrica/2026/04-april/README.md) |
| Mai 2026 | [Rapport](CyberAttackAfrica/2026/05-may/README_FR.md) | [Report](CyberAttackAfrica/2026/05-may/README.md) |
| Juin 2026 | [Rapport](CyberAttackAfrica/2026/06-june/README_FR.md) | [Report](CyberAttackAfrica/2026/06-june/README.md) |

---

## Statistiques

| Mois | FR | EN |
| :--- | :--- | :--- |
| Janvier 2026 | [Statistiques](statistics/2026/01-january/README_FR.md) | [Statistics](statistics/2026/01-january/README.md) |
| Février 2026 | [Statistiques](statistics/2026/02-february/README_FR.md) | [Statistics](statistics/2026/02-february/README.md) |
| Mars 2026 | [Statistiques](statistics/2026/03-march/README_FR.md) | [Statistics](statistics/2026/03-march/README.md) |
| Avril 2026 | [Statistiques](statistics/2026/04-april/README_FR.md) | [Statistics](statistics/2026/04-april/README.md) |
| Mai 2026 | [Statistiques](statistics/2026/05-may/README_FR.md) | [Statistics](statistics/2026/05-may/README.md) |
| Juin 2026 | [Statistiques](statistics/2026/06-june/README_FR.md) | [Statistics](statistics/2026/06-june/README.md) |

---

## Analyses comparatives

| Comparaison | FR | EN |
| :--- | :--- | :--- |
| Janvier vs février 2026 | [FR](comparison/2026/01-january-february/README_FR.md) | [EN](comparison/2026/01-january-february/README.md) |
| Février vs mars 2026 | [FR](comparison/2026/02-february-march/README_FR.md) | [EN](comparison/2026/02-february-march/README.md) |
| Mars vs avril 2026 | [FR](comparison/2026/03-march-april/README_FR.md) | [EN](comparison/2026/03-march-april/README.md) |
| Avril vs mai 2026 | [FR](comparison/2026/04-april-may/README_FR.md) | [EN](comparison/2026/04-april-may/README.md) |
| Mai vs juin 2026 | [FR](comparison/2026/05-may-june/README_FR.md) | [EN](comparison/2026/05-may-june/README.md) |

---

## Visual intelligence

📊 [Tableau de bord mai 2026](visual-intelligence/05-may/README_FR.md) - cartographies écosystème, acteurs, pays, secteurs

📊 [Tableau de bord avril 2026](visual-intelligence/04-april/README_FR.md)

---

## Jeux de données STIX / OpenCTI

| Dataset | Fichier |
| :--- | :--- |
| Janvier 2026 | [STIX Bundle](stix/2026/01-january/afrintel_january_2026_opencti.json) |
| Février 2026 | [STIX Bundle](stix/2026/02-february/afrintel_february_2026_opencti.json) |
| Mars 2026 | [STIX Bundle](stix/2026/03-march/afrintel_march_2026_opencti.json) |
| Avril 2026 | [STIX Bundle](stix/2026/04-april/afrintel_april_2026_opencti.json) |
| Mai 2026 | [STIX Bundle](stix/2026/05-may/afrintel_may_2026_opencti.json) |
| Juin 2026 | [STIX Bundle](stix/2026/06-june/afrintel_june_2026_opencti.json) |

Bundles STIX 2.1 compatibles OpenCTI, incluant acteurs, victimes, secteurs ciblés et mapping MITRE ATT&CK contextuel.

---

## Structure du projet

```text
AFRINTEL/
├── CyberAttackAfrica/   # Listes de victimes et rapports CTI mensuels (2024-2026)
├── statistics/          # Statistiques mensuelles
├── comparison/          # Comparaisons mois par mois
├── visual-intelligence/ # Cartographies et diagrammes
├── stix/                # Bundles STIX 2.1 / OpenCTI
├── scripts/             # Scripts de validation et utilitaires
└── workflows/           # Workflows d'automatisation
```

---

## Auteur

**Adama ASSIONGBON** - Consultant SOC & Cyber Threat Intelligence

🔗 [LinkedIn](https://www.linkedin.com/in/adama-assiongbon-9029893a/) | 📄 [Licence MIT](LICENSE)
