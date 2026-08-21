# CHANGELOG - Mai 2026

## [1.4.0] - 2026-08-21

### Ajout rétrospectif DDoS
- Ajout de 43 incidents DDoS revendiqués ou observations d indisponibilité visant des cibles marocaines entre le 9 et le 28 mai 2026.
- Ajout d une revendication distincte de fuite de données concernant une liste de candidats du ministère des Affaires étrangères, annoncée comme 8 440 lignes.
- Total mai révisé : 57 -> 103 incidents, dont 17 ransomware, 43 fuites/ventes d accès et 43 DDoS.
- Les versions EN/FR, statistiques et bundles STIX ont été synchronisés.


## [1.3.0] - 2026-07-29

### Corrections de classification
- Consumer Goods Council of South Africa (CGCSA), 03 mai 2026 : l'acteur Stormous était indiqué sous `Actor / Group` / `Acteur / Groupe` (fuite de données) alors qu'il est traité comme groupe ransomware ailleurs dans le dépôt. Reclassé en `Ransomware group` / `Groupe ransomware` dans victims.md et victims_FR.md, cohérent avec ransomware_victims.md.
- Fichiers mis à jour : victims.md, victims_FR.md, README.md, README_FR.md, statistics/README.md, statistics/README_FR.md, stix/afrintel_may_2026_opencti.json, stix/afrintel_h1_2026_opencti.json, comparison/04-april-may (FR/EN), comparison/05-may-june (FR/EN), CyberAttackAfrica/2026/README_H1.md et README_H1_FR.md.
- Total ransomware mai : 16 -> 17. Total fuites de données / ventes d'accès mai : 41 -> 40. Total incidents mai inchangé (57).

## [1.2.0] - 2026-06-24

### Ajout
- Deux incidents marocains initialement absents du rapport ont été intégrés dans les statistiques et les analyses :
  - **RADEM Meknès** (22 mai 2026) : revendication par l'acteur malveillant anisanas2 portant sur environ 1,1 million de documents issus d'une infrastructure publique de distribution d'eau et d'électricité (données clients, données opérationnelles).
  - **Vente massive de bases de données marocaines** (31 mai 2026) : bundle coordonné attribué à anisanas2, couvrant le Ministère de la Justice (2M docs, 150 000 dossiers judiciaires), NARSA (2M lignes), OFPPT (400 000 lignes), une base logistique (8M lignes) et un accès initial à une compagnie d'assurance. Volume estimé à plus de 12 millions de lignes et documents. Prix global revendiqué : 5 500 USD.

### Corrections statistiques
- Total incidents : 55 -> 57
- Total fuites de données : 39 -> 41
- Maroc (incidents directs) : 5 -> 7
- Secteur Gouvernement / Administration : 15 -> 17
- Afrique du Nord (incidents directs) : 28 -> 30
- Ajout de l'acteur anisanas2 dans les tableaux d'acteurs (2 incidents)
- Normalisation de l’alias secondaire sous anisanas2
- Fichiers mis à jour : README.md, README_FR.md, statistics/README.md, statistics/README_FR.md

---

## [1.1.0] - 2026-06-[date antérieure]

### Ajout
- Incident Éthiopie du 15 mai 2026 : fuite de données sur des ONG, ajouté tardivement après découverte post-publication initiale.

---

## [1.0.0] - 2026-06-[date initiale]

### Publication initiale
- Rapport CTI mensuel mai 2026 : 54 incidents initiaux documentés.
- Fichiers victims_FR.md, victims.md, README_FR.md, README.md, ransomware_victims.md.
- Statistiques mensuelles (statistics/2026/05-may/).
