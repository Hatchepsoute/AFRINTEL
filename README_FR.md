![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-darkgreen)
![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet)
![Focus](https://img.shields.io/badge/Focus-Incidents%20Cyber%20%26%20Activité%20de%20Menace-red)
![Dark Web](https://img.shields.io/badge/Source-Dark%20Web%20%2F%20OSINT-black)
![Projet](https://img.shields.io/badge/Projet-AFRINTEL-black)
![Licence](https://img.shields.io/badge/Licence-MIT-blue)

<p align="left">
<img src="comparison/afrintel_logo.png" width="90" align="left" style="margin-right:15px"/>

# AFRINTEL - African Threat Intelligence
</p>

👉🏾 [English version](README.md)

---

**AFRINTEL** est un projet open source de Cyber Threat Intelligence consacré aux incidents cyber affectant les organisations africaines dans les 54 pays du continent. Le projet documente les ransomwares, les fuites de données, les ventes d'accès, les DDoS, les défacements, la fraude opérationnelle ainsi que d'autres activités de menace pertinentes observées via des sources Dark Web, des leak sites, des forums underground et l'OSINT. Le type d'incident, le statut, le niveau de confiance et l'impact sont traités séparément afin qu'une revendication criminelle ne soit pas automatiquement assimilée à une compromission confirmée.

| Pays surveillés | Acteurs de menace suivis | Période couverte | Formats |
| :---: | :---: | :---: | :---: |
| 54 | 100+ | 2024-2026 | Markdown, STIX 2.1, Visual CTI |

> AFRINTEL documente ce qui a été observé : publications sur les leak sites, forums underground et sources OSINT. Chaque fiche victime conserve le statut correspondant au dernier niveau de validation effectué par AFRINTEL.

---

## Rapports à la une

### Cybermenaces en Afrique - Juillet 2026

Juillet 2026 compte **42 fiches incident** : 18 revendications ransomware, 18 Data Leak et 6 offres d'Access Sale. L'Égypte et la Tunisie arrivent en tête avec 7 incidents chacune, suivies du Maroc et de l'Afrique du Sud avec 6. Une fiche, Planet Sport, pourrait correspondre à une republication gratuite de la revendication LockBit 5 d'avril plutôt qu'à une nouvelle compromission ; le nombre réel de violations distinctes peut donc être légèrement inférieur. Les dossiers à surveiller dépassent largement le ransomware : données d'identité et foncières gouvernementales, données médicales et de laboratoire, comptes universitaires, données de paiement de services publics, résultats de concours de la fonction publique et autres informations réelles circulant sur des forums.

📄 [Rapport CTI complet - Juillet 2026](CyberAttackAfrica/2026/07-july/README_FR.md)  
📋 [Liste des victimes - Juillet 2026](CyberAttackAfrica/2026/07-july/victims_FR.md)

### Rapport cybermenaces du premier semestre 2026

Entre janvier et juin 2026, AFRINTEL a documenté **294 incidents dédupliqués** : **113 Ransomware**, **121 Data Leak**, **6 Access Sale**, **52 revendications DDoS**, **1 Defacement** et **1 incident d'Operational Fraud**. Le T1 représente **82 incidents**, contre **212 au T2**. Le Ransomware reste presque stable entre les deux trimestres, de 56 à 57, tandis que la forte hausse du T2 est principalement portée par les expositions/accès aux données et les revendications DDoS. Six fiches multi-pays développent le semestre à **317 occurrences géographiques**.

📊 [Rapport complet du S1 2026](CyberAttackAfrica/2026/README_H1_FR.md)

📊 [Full H1 2026 report](CyberAttackAfrica/2026/README_H1.md)

📦 [Bundle STIX 2.1 / OpenCTI S1 2026](stix/2026/afrintel_h1_2026_opencti.json)

🖼️ [Visuel statistique S1 2026](visual-intelligence/H1-2026/afrintel_h1_2026_statistics.png)

🗺️ [Carte visuelle S1 2026](visual-intelligence/H1-2026/afrintel_s1_2026_carte.png)

---

## Rapports CTI annuels

Chaque rapport annuel consolide le corpus mensuel validé de l'année : répartition par type d'incident, exposition par pays et région, tendances sectorielles, visibilité des acteurs, maturité des preuves et lecture CTI. Les versions française et anglaise sont maintenues avec une structure et des chiffres cohérents.

| Année | Fiches documentées | FR | EN |
| :--- | ---: | :--- | :--- |
| 2024 | **128** | [Rapport annuel](CyberAttackAfrica/2024/README_FR.md) | [Annual report](CyberAttackAfrica/2024/README.md) |
| 2025 | **197** | [Rapport annuel](CyberAttackAfrica/2025/README_FR.md) | [Annual report](CyberAttackAfrica/2025/README.md) |

**Référence 2024 corrigée :** 128 fiches cyber documentées dans 28 pays. Parmi elles, **127 appartiennent à la taxonomie AFRINTEL principale à six types** : 91 Ransomware, 31 Data Leak, 3 Access Sale, 1 Defacement et 1 Operational Fraud. **GTBank est conservé séparément comme une tentative d'attaque confirmée par la victime**, car les éléments disponibles ne permettent pas de la forcer dans une catégorie principale correspondant à une compromission réussie.

---

## Rapports CTI mensuels

| Mois | FR | EN |
| :--- | :--- | :--- |
| Janvier 2026 | [Rapport](CyberAttackAfrica/2026/01-january/README_FR.md) | [Report](CyberAttackAfrica/2026/01-january/README.md) |
| Février 2026 | [Rapport](CyberAttackAfrica/2026/02-february/README_FR.md) | [Report](CyberAttackAfrica/2026/02-february/README.md) |
| Mars 2026 | [Rapport](CyberAttackAfrica/2026/03-march/README_FR.md) | [Report](CyberAttackAfrica/2026/03-march/README.md) |
| Avril 2026 | [Rapport](CyberAttackAfrica/2026/04-april/README_FR.md) | [Report](CyberAttackAfrica/2026/04-april/README.md) |
| Mai 2026 | [Rapport](CyberAttackAfrica/2026/05-may/README_FR.md) | [Report](CyberAttackAfrica/2026/05-may/README.md) |
| Juin 2026 | [Rapport](CyberAttackAfrica/2026/06-june/README_FR.md) | [Report](CyberAttackAfrica/2026/06-june/README.md) |
| Juillet 2026 | [Rapport](CyberAttackAfrica/2026/07-july/README_FR.md) | [Report](CyberAttackAfrica/2026/07-july/README.md) |
| Août 2026 | *en cours* | *in progress* |

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
| Juillet 2026 | [Statistiques](statistics/2026/07-july/README_FR.md) | [Statistics](statistics/2026/07-july/README.md) |
| Août 2026 | *en cours* | *in progress* |

---

## Comparaisons mois par mois

| Comparaison | FR | EN |
| :--- | :--- | :--- |
| Janvier vs Février 2026 | [FR](comparison/2026/01-january-february/README_FR.md) | [EN](comparison/2026/01-january-february/README.md) |
| Février vs Mars 2026 | [FR](comparison/2026/02-february-march/README_FR.md) | [EN](comparison/2026/02-february-march/README.md) |
| Mars vs Avril 2026 | [FR](comparison/2026/03-march-april/README_FR.md) | [EN](comparison/2026/03-march-april/README.md) |
| Avril vs Mai 2026 | [FR](comparison/2026/04-april-may/README_FR.md) | [EN](comparison/2026/04-april-may/README.md) |
| Mai vs Juin 2026 | [FR](comparison/2026/05-may-june/README_FR.md) | [EN](comparison/2026/05-may-june/README.md) |
| Juin vs Juillet 2026 | [FR](comparison/2026/06-june-july/README_FR.md) | [EN](comparison/2026/06-june-july/README.md) |
| Rapport S1 2024 | [FR](CyberAttackAfrica/2024/README_H1_FR.md) | [EN](CyberAttackAfrica/2024/README_H1.md) |
| Rapport S1 2026 | [FR](CyberAttackAfrica/2026/README_H1_FR.md) | [EN](CyberAttackAfrica/2026/README_H1.md) |

---

## Visual intelligence

| Période | Tableau / Visuel |
| :--- | :--- |
| Janvier 2026 | [Visual intelligence](visual-intelligence/01-january/README.md) |
| Février 2026 | [Visual intelligence](visual-intelligence/02-february/README.md) |
| Mars 2026 | [Visual intelligence](visual-intelligence/03-march/README.md) |
| Avril 2026 | [Visual intelligence](visual-intelligence/04-april/README.md) |
| Mai 2026 | [Visual intelligence](visual-intelligence/05-may/README.md) |
| Juin 2026 | [Visual intelligence](visual-intelligence/06-june/README.md) |
| Juillet 2026 | [Visuel LinkedIn](visual-intelligence/07-july/afrintel_july_2026_linkedin_top5.png) |
| Août 2026 | *en cours* |
| S1 2026 | [Visuel statistique](visual-intelligence/H1-2026/afrintel_h1_2026_statistics.png) |
| Carte S1 2026 | [Carte visuelle](visual-intelligence/H1-2026/afrintel_s1_2026_carte.png) |

---

## Datasets STIX / OpenCTI

| Dataset | Fichier |
| :--- | :--- |
| Janvier 2026 | [Bundle STIX](stix/2026/01-january/afrintel_january_2026_opencti.json) |
| Février 2026 | [Bundle STIX](stix/2026/02-february/afrintel_february_2026_opencti.json) |
| Mars 2026 | [Bundle STIX](stix/2026/03-march/afrintel_march_2026_opencti.json) |
| Avril 2026 | [Bundle STIX](stix/2026/04-april/afrintel_april_2026_opencti.json) |
| Mai 2026 | [Bundle STIX](stix/2026/05-may/afrintel_may_2026_opencti.json) |
| Juin 2026 | [Bundle STIX](stix/2026/06-june/afrintel_june_2026_opencti.json) |
| Juillet 2026 | [Bundle STIX](stix/2026/07-july/afrintel_july_2026_opencti.json) |
| Août 2026 | *en cours* |
| S1 2026 | [Bundle STIX](stix/2026/afrintel_h1_2026_opencti.json) |

Chaque bundle mensuel STIX 2.1 contient des descriptions bilingues des incidents et victimes, le rapport CTI, les statistiques, les comparaisons mensuelles, les références de sources ainsi que les objets d'identité AFRINTEL et auteur. Les bundles S1 conservent les identifiants STIX mensuels d'origine afin qu'OpenCTI puisse corréler les enregistrements entre les différentes périodes. Lorsqu'un corpus mensuel ou semestriel est corrigé, le bundle STIX agrégé correspondant doit être régénéré avant d'être considéré comme un miroir exact de la source de vérité Markdown. Le contexte MITRE ATT&CK reste documenté dans les descriptions des rapports.

---

## Principes de qualité des données

AFRINTEL sépare **type d'incident**, **statut**, **niveau de confiance** et **impact**. Une publication ransomware sur un leak site reste une revendication tant qu'aucun élément plus solide n'est disponible. Les échantillons publiés, confirmations des victimes, confirmations gouvernementales et corroborations ultérieures sont conservés comme des états de preuve différents.

Les republications historiques sont datées séparément de la fuite revendiquée sous-jacente lorsque cette distinction est connue. Les fiches multi-pays comptent une seule fois dans les totaux dédupliqués, mais peuvent produire plusieurs occurrences géographiques. Lorsqu'un événement ne peut pas être rattaché sans distorsion à l'un des six types principaux, AFRINTEL documente explicitement l'exception au lieu d'inventer une classification.

---

## Structure du projet

```text
AFRINTEL/
├── CyberAttackAfrica/   # Listes mensuelles de victimes et rapports CTI (2024-2026)
├── statistics/          # Statistiques mensuelles
├── comparison/          # Comparaisons mois par mois
├── visual-intelligence/ # Cartes et diagrammes CTI
├── stix/                # Bundles STIX 2.1 / OpenCTI
├── scripts/             # Scripts de validation et utilitaires
└── workflows/           # Workflows d'automatisation
```

---

## ✍🏿 Auteur

**Adama ASSIONGBON** - Consultant SOC & Cyber Threat Intelligence

🔗 [LinkedIn](https://www.linkedin.com/in/adama-assiongbon-9029893a/) | 📄 [Licence MIT](LICENSE)
