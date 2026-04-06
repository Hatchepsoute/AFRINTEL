[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Afrique-orange)
![Threat Type](https://img.shields.io/badge/Menace-Ransomware%20%26%20Data%20Breach-red)
![Period](https://img.shields.io/badge/Période-Mars%202026-lightgrey)
![Intel Type](https://img.shields.io/badge/Type%20d'Intel-CTI-purple)

# Rapport CTI - Cyberattaques en Afrique (Mars 2026)

## 1. Synthèse exécutive

En mars 2026, **36 incidents cyber** ciblant des entités africaines ont été revendiqués ou détectés publiquement. Le continent fait face à une double menace : **ransomware** (chiffrement avec rançon) et **fuites de données / intrusions système** (exfiltration sans chiffrement ou fraude financière directe). Principales conclusions :

- **19 attaques de ransomware (53 %)** et **17 fuites de données / intrusions (47 %)**.
- **11 pays touchés** ; **Afrique du Sud** (11 incidents), **Maroc** (8) et **Égypte** (8) représentent 75 % des victimes.
- **23 acteurs distincts** ; **CrowStealer** (5 incidents), **APT73/BASHE** (4) et **XP95** (3) sont les plus actifs.
- **Secteurs gouvernemental et éducatif** : 44 % des victimes, montrant un ciblage stratégique des institutions publiques.
- Fuites massives : ministère de la Santé égyptien (3,8 M d’enregistrements), province de Gauteng (3,8 To), Remita Nigeria (3 To), Stats SA (154 Go).
- Nouvel incident majeur : **UBA Sénégal** – un braquage cyber coordonné avec compromission du système, manipulation de bases de données et plus de 3 400 retraits frauduleux en GAB totalisant 1,143 milliard FCFA (~1,9 M USD), révélé en mars mais exécuté fin janvier.

## 2. Méthodologie

- **Périmètre** : 54 pays africains.
- **Période** : 1er – 31 mars 2026 (incidents révélés ou revendiqués durant ce mois ; les attaques peuvent être antérieures).
- **Sources** : DLS (sites de fuite), OSINT, canaux Telegram, forums underground, rapports médiatiques.
- **Inclusion** : incidents publiquement revendiqués ou attribués avec victime, pays et secteur identifiés.
- **Typologie** :
  - *Ransomware* : chiffrement + rançon (revendication sur DLS).
  - *Fuite de données / intrusion* : exfiltration non chiffrée, base de données vendue ou publiée, ou compromission système menant à une fraude financière.

## 3. Vue d’ensemble

| Indicateur                     | Valeur |
|--------------------------------|--------|
| Nombre total de victimes       | 36     |
| Pays touchés                   | 11     |
| Acteurs distincts              | 23     |
| Incidents de ransomware        | 19 (53 %) |
| Fuites de données / intrusions | 17 (47 %) |

**Pays les plus ciblés :**
- 🇿🇦 Afrique du Sud : 11 victimes
- 🇲🇦 Maroc : 8 victimes
- 🇪🇬 Égypte : 8 victimes
- 🇳🇬 Nigeria : 2 victimes
- 🇸🇳 Sénégal : 1 victime
- 🇿🇲 Zambie : 1 victime
- 🇲🇬 Madagascar : 1 victime
- 🇹🇳 Tunisie : 1 victime
- 🇳🇦 Namibie : 1 victime
- 🇹🇿 Tanzanie : 1 victime
- 🇨🇩 RDC : 1 victime

**Comparaison ransomware vs fuites/intrusions par pays :**
| Pays                  | Ransomware | Fuites/Intrusions |
|-----------------------|------------|-------------------|
| 🇿🇦 Afrique du Sud     | 7          | 4                 |
| 🇲🇦 Maroc              | 5          | 3                 |
| 🇪🇬 Égypte             | 3          | 5                 |
| 🇳🇬 Nigeria            | 0          | 2                 |
| 🇸🇳 Sénégal            | 0          | 1                 |
| 🇿🇲 Zambie             | 0          | 1                 |
| 🇲🇬 Madagascar         | 1          | 0                 |
| 🇹🇳 Tunisie            | 1          | 0                 |
| 🇳🇦 Namibie            | 1          | 0                 |
| 🇹🇿 Tanzanie           | 1          | 0                 |
| 🇨🇩 RDC                | 0          | 1                 |

**Répartition sectorielle :**
| Secteur                    | Incidents | Pourcentage |
|----------------------------|-----------|-------------|
| Gouvernement / Admin       | 9         | 25 %        |
| Éducation / Université     | 7         | 19 %        |
| Santé                      | 3         | 8 %         |
| Assurance                  | 3         | 8 %         |
| Télécommunications         | 3         | 8 %         |
| Ingénierie/Construction    | 3         | 8 %         |
| Finance / Banque           | 2         | 6 %         |
| IT/Consulting              | 2         | 6 %         |
| Fintech                    | 1         | 3 %         |
| Autres                     | 3         | 8 %         |

**Acteurs les plus prolifiques :**
| Acteur           | Type           | Incidents | Cibles principales |
|------------------|----------------|-----------|---------------------|
| CrowStealer      | Courtier de données | 5    | Gouvernement et éducation égyptiens |
| APT73/BASHE      | Ransomware     | 4         | Institutions d’État marocaines |
| XP95             | Ransomware     | 3         | Gouvernement sud-africain |
| Qilin            | Ransomware     | 2         | Maroc, Madagascar |
| The Gentlemen    | Ransomware     | 2         | Tunisie, Afrique du Sud |
| INC Ransom       | Ransomware     | 2         | Namibie, Afrique du Sud |
| xNov             | Fuite de données | 2       | Supply chain marocaine |

**Chronologie quotidienne (mars 2026 – dates de révélation) :**
- 01/03 : 3 incidents
- 02/03 : 3
- 03/03 : 3
- 04/03 : 1
- 05/03 : 1
- 06/03 : 2
- 09/03 : 1
- 12/03 : 1
- 13/03 : 2
- 14/03 : 1
- 19/03 : 1
- 20/03 : 2
- 21/03 : 1
- 22/03 : 1
- 24/03 : 1 (révélation UBA Sénégal)
- 26/03 : 4
- 29/03 : 2
- 30/03 : 3
- 31/03 : 3

## 4. Analyse détaillée par type d’incident

### 4.1 Ransomware (19 incidents)

| Pays             | Attaques ransomware | Acteurs principaux |
|------------------|---------------------|---------------------|
| Afrique du Sud   | 7                   | XP95 (3), LockBit 5.0, Lynx, DragonForce, The Gentlemen, NightSpire, INC Ransom, Coinbase Cartel |
| Maroc            | 5                   | APT73/BASHE (3), Qilin, The Gentlemen |
| Égypte           | 3                   | Crypto24, PEAR, Payload |
| Madagascar       | 1                   | Qilin |
| Tunisie          | 1                   | The Gentlemen |
| Namibie          | 1                   | INC Ransom |
| Tanzanie         | 1                   | Morpheus |

**Observations clés** :
- **XP95** est devenu une menace majeure en Afrique du Sud : gouvernement de Gauteng (3,8 To), Stats SA (154 Go) et GCRA (147 Go). Les données sont vendues, pas seulement chiffrées.
- **APT73/BASHE** a ciblé des institutions stratégiques marocaines (HACA, Maroc Telecom, 2M TV, IRES), suggérant une motivation géopolitique.
- Le secteur des assurances lourdement touché en Afrique du Sud (Lion of Africa, The Unlimited).

### 4.2 Fuites de données / intrusions système (17 incidents)

| Pays             | Fuites/Intrusions | Acteurs principaux |
|------------------|-------------------|---------------------|
| Égypte           | 5                 | CrowStealer (5) |
| Maroc            | 3                 | xNov (2), anisanas2 |
| Afrique du Sud   | 4                 | TelephoneHooliganism, XP95 (déjà compté dans ransomware), Walter Sisulu University (fuite) |
| Nigeria          | 2                 | AshleyWood2022, Bytetobreach |
| Sénégal          | 1                 | Réseau coordonné |
| Zambie           | 1                 | Spirigatito |
| RDC              | 1                 | privillege |

**Observations clés** :
- **CrowStealer** domine les fuites égyptiennes, y compris une base de données médicale de 3,8 millions de patients (ministère de la Santé) vendue 2 500 $.
- **xNov** a exposé des dossiers étudiants (ONOUSC, 3 631 entrées) et les données supply chain de L’Oréal Maroc (296 pharmacies, 361 000 ventes, secrets OAuth2).
- **UBA Sénégal** (révélé en mars, exécuté fin janvier) : les attaquants ont compromis le système d’information interne, manipulé les bases de données (création/modification de comptes, augmentation des plafonds de retrait, transferts de fonds), puis coordonné plus de 3 400 retraits GAB en quelques heures, emportant 1,143 milliard FCFA (~1,9 M USD). Vulnérabilités probables : absence de SOC temps réel, procédures antifraude insuffisantes, possible complicité interne.
- Fuites massives au Nigeria : Remita (3 To, incluant documents KYC et clés HSM gouvernementales) et université Ahmadu Bello (11 000+ dossiers).

## 5. Impact sectoriel

| Secteur                  | Incidents | Pourcentage |
|--------------------------|-----------|-------------|
| Gouvernement / Admin     | 9         | 25 %        |
| Éducation / Université   | 7         | 19 %        |
| Santé                    | 3         | 8 %         |
| Assurance                | 3         | 8 %         |
| Télécommunications       | 3         | 8 %         |
| Ingénierie/Construction  | 3         | 8 %         |
| Finance / Banque         | 2         | 6 %         |
| IT/Consulting            | 2         | 6 %         |
| Fintech                  | 1         | 3 %         |
| Autres                   | 3         | 8 %         |

**Enseignements** :
- Le secteur public (gouvernement + éducation) représente **44 %** des incidents.
- Les données de santé restent très valorisées : fuite du ministère de la Santé égyptien (3,8 M d’enregistrements) et fuites d’assurances sud-africaines.
- Les télécoms (Orange Madagascar, Maroc Telecom) sont des cibles stratégiques.
- L’incident UBA Sénégal illustre une nouvelle tendance : **fraude financière directe par compromission système**, contournant le ransomware classique.

## 6. Profil des acteurs

| Acteur           | Type           | Incidents | Cibles principales |
|------------------|----------------|-----------|---------------------|
| CrowStealer      | Courtier de données | 5    | Gouvernement et éducation égyptiens |
| APT73/BASHE      | Ransomware     | 4         | Institutions d’État marocaines |
| XP95             | Ransomware     | 3         | Gouvernement sud-africain |
| Qilin            | Ransomware     | 2         | Maroc, Madagascar |
| The Gentlemen    | Ransomware     | 2         | Tunisie, Afrique du Sud |
| INC Ransom       | Ransomware     | 2         | Namibie, Afrique du Sud |
| xNov             | Fuite de données | 2       | Supply chain marocaine |

**Acteurs émergents** : xNov (ciblage supply chain), XP95 (gouvernement sud-africain). L’attaque UBA Sénégal implique un **réseau coordonné** (possiblement avec complicité interne) – pas un groupe ransomware classique mais une équipe d’intrusion à motivation financière.

### 6.1 Niveau de risque

| Pays | Risque |
|------|--------|
| Afrique du Sud | 🔴 Critique |
| Maroc | 🔴 Élevé |
| Égypte | 🔴 Élevé |
| Nigeria | 🟠 Moyen-Élevé |
| Sénégal | 🟠 Moyen (post-UBA) |
| Autres | 🟠 Moyen |

## 7. Tendances clés et lacunes de renseignement

### Tendances
1. **Évolution des ransomwares** – XP95 et d’autres vendent les données exfiltrées plutôt que de simplement chiffrer.
2. **Attaques de la supply chain** – Smarteez (prestataire de L’Oréal Maroc) montre la vulnérabilité des sous-traitants digitaux.
3. **Fuites massives de données de santé** – Ministère de la Santé égyptien (3,8 M d’enregistrements) révèle des failles dans la sécurité des systèmes publics.
4. **Ciblage géopolitique** – APT73/BASHE concentré sur les médias et télécoms d’État marocains.
5. **Fraude financière directe par compromission système** – UBA Sénégal démontre que les attaquants contournent le ransomware pour aller directement à l’argent, exploitant des SOC et contrôles antifraude faibles.

### Lacunes
- De nombreuses attaques restent non détectées ou non déclarées ; cette liste ne couvre que les incidents publics.
- Attribution incertaine pour certains groupes (CrowStealer pourrait être un revendeur, pas l’attaquant initial).
- Les volumes de données annoncés peuvent être gonflés.
- L’attaque UBA Sénégal a eu lieu fin janvier mais n’a été révélée qu’en mars – délai important dans la prise de conscience publique.

## 8. Mapping MITRE ATT&CK (contextuel)

| Incident | Techniques |
|----------|-----------|
| Smarteez | T1552 |
| Gauteng | T1041 |
| ONOUSC | T1078 |
| Santé Égypte | T1005 |
| UBA Sénégal | T1190, T1078, T1048, T1531 |

**Techniques observées couramment** :
- T1566 – Phishing  
- T1190 – Exploitation web  
- T1041 – Exfiltration  
- T1078 – Comptes valides  
- T1486 – Ransomware  
- T1531 – Manipulation de comptes (UBA Sénégal)

## 9. Recommandations

### Pour les gouvernements et entreprises africains
- **Sécurité des bases de données** : chiffrement des données sensibles, contrôles d’accès, audits réguliers.
- **Gestion des risques tiers** : auditer les prestataires de services digitaux, imposer des clauses de cybersécurité.
- **Réponse aux incidents** : sauvegardes hors ligne, exercices de simulation, protocoles de communication.
- **Formation des utilisateurs** : sensibilisation au phishing (vecteur initial principal).
- **Supervision en temps réel** : déployer ou renforcer un SOC 24/7 ; mettre en place une détection d’anomalies transactionnelles (particulièrement pour les banques).
- **Mécanismes antifraude** : plafonds de retrait dynamiques, blocage automatique en cas de schéma anormal, analyse comportementale.

### Pour les analystes CTI
- Surveiller **XP95** et **xNov** pour de nouvelles campagnes.
- Cartographier les expositions de la supply chain (notamment marketing digital et logistique).
- Prioriser la surveillance des secteurs gouvernemental, éducatif et de la santé en Afrique du Nord et australe.
- Surveiller les **intrusions financières non ransomware** – UBA Sénégal n’est probablement pas un cas isolé.

## 10. Recommandations SOC

- Détection exfiltration (T1041)  
- Surveillance comptes privilégiés  
- Analyse trafic sortant  
- Monitoring API / OAuth  
- Pour les banques : détection en temps réel des anomalies de retraits GAB (vélocité, localisation, pics de montants)

## 11. Recommandations stratégiques

- Activer MFA  
- Segmenter le réseau (séparer réseau GAB du cœur bancaire)  
- Auditer les prestataires  
- Maintenir des sauvegardes offline  
- Effectuer des exercices de crise incluant des simulations red-team  
- **Cadre réglementaire** : les banques centrales devraient imposer des standards minimaux de SOC et de détection de fraude

## 12. Conclusion

Mars 2026 confirme que **l’Afrique est une cible privilégiée pour la cybercriminalité industrialisée**. La convergence des groupes ransomware, courtiers de données, attaques supply chain, et désormais **intrusions financières directes** (UBA Sénégal) crée un environnement à haut risque. L’Afrique du Sud, le Maroc et l’Égypte restent les plus touchés, mais l’incident UBA montre que **l’Afrique de l’Ouest est également sérieusement menacée**. Les institutions financières doivent urgemment renforcer leur supervision en temps réel et leurs capacités antifraude. AFRINTEL continuera de suivre ces évolutions.

**AFRINTEL** - Cyber Threat Intelligence africaine  
[GitHub AFRINTEL](https://github.com/Hatchepsoute/AFRINTEL)