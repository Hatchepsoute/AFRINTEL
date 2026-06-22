[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Afrique-orange)
![Threat Type](https://img.shields.io/badge/Menace-Ransomware%20%26%20Data%20Breach-red)
![Period](https://img.shields.io/badge/Période-Mars%202026-lightgrey)
![Intel Type](https://img.shields.io/badge/Type%20d'Intel-CTI-purple)

# Rapport CTI - Cyberattaques en Afrique (Mars 2026)
👉🏾 [**English version available here**](./README.md)
## 1. Synthèse exécutive

En mars 2026, **41 incidents cyber** ciblant des entités africaines ont été revendiqués ou détectés publiquement. Le continent fait face à une double menace : **ransomware** (chiffrement avec rançon) et **fuites de données / intrusions système** (exfiltration sans chiffrement ou fraude financière directe). Principales conclusions :

- **19 attaques de ransomware (46,3 %)** et **22 fuites de données / intrusions (53,7 %)**.
- **14 pays touchés** ; **Afrique du Sud** (13 incidents), **Maroc** (8) et **Égypte** (8) représentent 71 % des victimes.
- **27 acteurs distincts** ; **CrowStealer** (5 incidents), **APT73/BASHE** (4) et **XP95** (3) sont les plus actifs.
- **Secteurs gouvernemental et éducatif** : 41,5 % des victimes, montrant un ciblage stratégique des institutions publiques.
- Fuites massives : ministère de la Santé égyptien (3,8 M d’enregistrements), province de Gauteng (3,8 To), Remita Nigeria (3 To), Stats SA (154 Go). Au Maroc, plusieurs fuites majeures ont touché des institutions gouvernementales, dont le Ministère de la Justice (300 Go de dossiers judiciaires).
- Nouvel incident majeur : **UBA Sénégal** - un braquage cyber coordonné avec compromission du système, manipulation de bases de données et plus de 3 400 retraits frauduleux en GAB totalisant 1,143 milliard FCFA (~1,9 M USD), révélé en mars mais exécuté fin janvier.
- Menaces émergentes : **Loozap (Cameroun)** - 34 000 comptes utilisateurs divulgués (mots de passe en SHA1) ; **Ministère de la Santé de Guinée** - compromission suspectée des tableaux de bord DHIS2 par l’acteur Keymous.

### 📋 Liste des victimes

👉🏾 [Voir la liste complète des victimes](./victims_FR.md)

## 2. Méthodologie

- **Périmètre** : 54 pays africains.
- **Période** : 1er - 31 mars 2026 (incidents révélés ou revendiqués durant ce mois ; les attaques peuvent être antérieures).
- **Sources** : Dark web, DLS (sites de fuite), OSINT, canaux Telegram, forums underground, rapports médiatiques.
- **Inclusion** : incidents publiquement revendiqués ou attribués avec victime, pays et secteur identifiés.
- **Typologie** :
  - *Ransomware* : chiffrement + rançon (revendication sur DLS).
  - *Fuite de données / intrusion* : exfiltration non chiffrée, base de données vendue ou publiée, ou compromission système menant à une fraude financière.

## 3. Vue d’ensemble

| Indicateur                     | Valeur |
|--------------------------------|--------|
| Nombre total de victimes       | 41     |
| Pays touchés                   | 14     |
| Acteurs distincts              | 27     |
| Incidents de ransomware        | 19 (46,3 %) |
| Fuites de données / intrusions | 22 (53,7 %) |

**Pays les plus ciblés :**
- 🇿🇦 Afrique du Sud : 13 victimes
- 🇲🇦 Maroc : 8 victimes
- 🇪🇬 Égypte : 8 victimes
- 🇳🇬 Nigeria : 2 victimes
- 🇨🇲 Cameroun : 1 victime
- 🇩🇿 Algérie : 1 victime
- 🇸🇳 Sénégal : 1 victime
- 🇬🇳 Guinée : 1 victime
- 🇿🇲 Zambie : 1 victime
- 🇲🇬 Madagascar : 1 victime
- 🇹🇳 Tunisie : 1 victime
- 🇳🇦 Namibie : 1 victime
- 🇹🇿 Tanzanie : 1 victime
- 🇨🇩 RDC : 1 victime

```mermaid
pie
 title Nombre de victimes / pays (mars 2026)
 "Afrique du Sud (13)" : 13
 "Maroc (8)" : 8
 "Égypte (8)" : 8
 "Nigeria (2)" : 2
 "Cameroun (1)" : 1
 "Algérie (1)" : 1
 "Sénégal (1)" : 1
 "Guinée (1)" : 1
 "Zambie (1)" : 1
 "Madagascar (1)" : 1
 "Tunisie (1)" : 1
 "Namibie (1)" : 1
 "Tanzanie (1)" : 1
 "RDC (1)" : 1
```

**Comparaison ransomware vs fuites de données par pays :**
| Pays                  | Ransomware | Fuites de données |
|-----------------------|------------|-------------------|
| Afrique du Sud        | 7          | 6                 |
| Maroc                 | 5          | 3                 |
| Égypte                | 3          | 5                 |
| Nigeria               | 0          | 2                 |
| Cameroun              | 0          | 1                 |
| Algérie               | 0          | 1                 |
| Sénégal               | 0          | 1                 |
| Guinée                | 0          | 1                 |
| Zambie                | 0          | 1                 |
| Madagascar            | 1          | 0                 |
| Tunisie               | 1          | 0                 |
| Namibie               | 1          | 0                 |
| Tanzanie              | 1          | 0                 |
| RDC                   | 0          | 1                 |

```mermaid
pie
 title Attaques ransomware par pays
 "Afrique du Sud (7)" : 7
 "Maroc (5)" : 5
 "Égypte (3)" : 3
 "Madagascar (1)" : 1
 "Tunisie (1)" : 1
 "Namibie (1)" : 1
 "Tanzanie (1)" : 1
```
```mermaid
pie
 title Fuites de données par pays
 "Afrique du Sud (6)" : 6
 "Égypte (5)" : 5
 "Maroc (3)" : 3
 "Nigeria (2)" : 2
 "Cameroun (1)" : 1
 "Algérie (1)" : 1
 "Sénégal (1)" : 1
 "Guinée (1)" : 1
 "Zambie (1)" : 1
 "RDC (1)" : 1
```

**Répartition sectorielle :**
| Secteur                    | Incidents | Pourcentage |
|----------------------------|-----------|-------------|
| Gouvernement / Admin       | 10        | 24,4 %      |
| Éducation / Université     | 7         | 17,1 %      |
| Santé                      | 4         | 9,8 %       |
| Assurance                  | 3         | 7,3 %       |
| Télécommunications         | 3         | 7,3 %       |
| Ingénierie/Construction    | 3         | 7,3 %       |
| Finance / Banque           | 2         | 4,9 %       |
| IT/Consulting              | 2         | 4,9 %       |
| Fintech                    | 1         | 2,4 %       |
| E-commerce / Petites annonces | 1      | 2,4 %       |
| Sport / Loisirs            | 1         | 2,4 %       |
| Autres                     | 4         | 9,8 %       |

```mermaid
pie
 title Répartition sectorielle (mars 2026)
 "Gouvernement (10)" : 10
 "Éducation (7)" : 7
 "Santé (4)" : 4
 "Assurance (3)" : 3
 "Télécoms (3)" : 3
 "Ingénierie/Construction (3)" : 3
 "Finance/Banque (2)" : 2
 "IT/Consulting (2)" : 2
 "Fintech (1)" : 1
 "E-commerce/Annonces (1)" : 1
 "Sport/Loisirs (1)" : 1
 "Autres (4)" : 4
```

**Acteurs les plus prolifiques :**
| Acteur           | Type           | Incidents | Cibles principales |
|------------------|----------------|-----------|---------------------|
| CrowStealer      | Courtier de données | 5    | Gouvernement et éducation égyptiens |
| APT73/BASHE      | Ransomware     | 4         | Institutions d’État marocaines |
| XP95             | Ransomware     | 3         | Gouvernement sud-africain |
| xNov             | Fuite de données | 3       | Supply chain marocaine, sport sud-africain, éducation |
| Qilin            | Ransomware     | 2         | Maroc, Madagascar |
| The Gentlemen    | Ransomware     | 2         | Tunisie, Afrique du Sud |
| INC Ransom       | Ransomware     | 2         | Namibie, Afrique du Sud |

## 4. Vue d’ensemble pays par pays

> Tous les éléments présentés proviennent d’incidents revendiqués sur le dark web, sur les sites web des groupes de ransomware et les forums underground.

### 🇿🇦 Afrique du Sud (13 incidents : 7 ransomwares, 6 fuites de données)

L’Afrique du Sud enregistre le plus grand nombre de victimes en mars avec 13 incidents couvrant les secteurs gouvernemental, éducatif, assurantiel, de l’ingénierie et des technologies. L’acteur malveillant XP95 est à l’origine des événements les plus impactants : le gouvernement provincial du Gauteng, avec 3,8 To de données provinciales mis en vente pour 25 000 $ ; Stats SA, l’autorité nationale des statistiques, avec 154 Go exfiltrés et une rançon de 100 000 $ ; et la GCRA, l’académie régionale du Gauteng, avec 147 Go prélevés. Il s’agit d’incidents d’extorsion par exfiltration de données, pas de ransomware classique : l’acteur malveillant XP95 vend les données plutôt que de chiffrer les systèmes. La brèche du Gauteng compromet potentiellement des données de santé, d’éducation, de logement et d’activité économique pour la province la plus peuplée d’Afrique du Sud. L’acteur malveillant Blackwinter99 a publié des identifiants administrateur de l’UNISA, la plus grande université d’enseignement à distance d’Afrique, exposant un risque de compromission directe. L’acteur malveillant LockBit 5.0 a revendiqué Diesel-Electric Group, un grand distributeur de composants automobiles. L’acteur malveillant Lynx a revendiqué Lion of Africa Insurance, un assureur spécialisé. L’acteur malveillant DragonForce a revendiqué The Unlimited, une société de services d’assurance, avec 137 Go allégués. L’acteur malveillant TheGentlemen a revendiqué Elundini Municipality, une entité de gouvernement local. L’acteur malveillant NightSpire a revendiqué Semenya Furumele Consulting, une société de services professionnels. L’acteur malveillant INC Ransom a revendiqué ETFSA, un gestionnaire de patrimoine. L’acteur malveillant TelephoneHooliganism a proposé des identifiants d’accès à l’université Walter Sisulu pour 1 150 $. L’acteur malveillant Coinbase Cartel a revendiqué Nashua, un prestataire de services IT managés. L’acteur malveillant xNov a exposé une base de données équestre issue d’Eventing South Africa.

---

### 🇲🇦 Maroc (8 incidents : 5 ransomwares, 3 fuites de données)

Le Maroc a été lourdement ciblé en mars, avec une concentration notable sur les institutions d’État. L’acteur malveillant APT73/BASHE a frappé quatre entités stratégiques marocaines : la HACA, régulateur de l’audiovisuel ; Maroc Telecom, l’opérateur national de télécommunications ; 2M TV, la chaîne nationale publique ; et l’IRES, le think tank du Cabinet Royal. Cette concentration sur les médias et télécoms d’État marocains suggère une motivation géopolitique possible derrière la campagne. L’acteur malveillant xNov a exposé les données de la mutuelle étudiante ONOUSC (3 631 entrées) et publié des données de la supply chain Smarteez pour le réseau L’Oréal Maroc, incluant 22 secrets OAuth2 et les coordonnées GPS de 296 pharmacies. L’acteur malveillant anisanas2 a divulgué 300 Go du ministère de la Justice, dont environ 150 000 dossiers judiciaires. L’acteur malveillant Qilin a revendiqué Outsourcia, une grande société de BPO et de services aux entreprises.

---

### 🇪🇬 Égypte (8 incidents : 3 ransomwares, 5 fuites de données)

L’Égypte enregistre huit incidents en mars, avec l’acteur malveillant CrowStealer dominant par cinq fuites systématiques ciblant les infrastructures gouvernementales et éducatives. L’acteur malveillant CrowStealer a revendiqué le Canadian International College (CIC Cairo) avec 2 925 dossiers étudiants ; l’Autorité de régulation des déchets (WMRA) ; Orascom Construction, l’un des plus grands groupes d’ingénierie d’Égypte ; le ministère de la Santé avec 3,8 millions de dossiers patients vendus 2 500 $ ; et le ministère de l’Éducation. La fuite du ministère de la Santé représente la plus grande exposition individuelle de données de santé enregistrée par AFRINTEL sur le continent en mars. L’acteur malveillant Crypto24 a revendiqué Rowad Modern Engineering. L’acteur malveillant PEAR a revendiqué INTERACT Technology Solutions. L’acteur malveillant Payload a revendiqué Grid Fine Finishes, une société de services de finition en construction.

---

### 🇳🇬 Nigeria (2 incidents : 2 fuites de données)

Le Nigeria enregistre deux fuites de haute gravité. L’acteur malveillant Bytetobreach a revendiqué Remita, opéré par SystemSpecs et servant de colonne vertébrale des paiements gouvernementaux du Nigeria, avec 3 To de données incluant des documents KYC, du code source, des registres Docker et des clés HSM de chiffrement gouvernementales. L’exposition des clés HSM constitue un risque souverain pour l’infrastructure financière nationale. L’acteur malveillant AshleyWood2022 a divulgué plus de 11 000 dossiers de personnels de l’université Ahmadu Bello, l’une des plus grandes universités fédérales du Nigeria.

---

### 🇸🇳 Sénégal (1 incident : intrusion système)

UBA Sénégal a subi une cyberattaque coordonnée exécutée les 30 et 31 janvier mais rendue publique le 24 mars. Les attaquants ont compromis les systèmes internes de la banque, manipulé les bases de données pour augmenter les plafonds de retrait et transférer des fonds, puis coordonné plus de 3 400 retraits GAB frauduleux dans plusieurs villes, causant des pertes de 1,143 milliard FCFA (environ 1,9 M$). Cet incident illustre une catégorie d’attaque distincte : fraude financière directe par compromission système, sans déploiement de ransomware. Le vecteur d’attaque et l’identité de l’acteur n’ont pas été confirmés publiquement.

---

### 🇿🇲 Zambie (1 incident : fuite critique gouvernementale)

ZISPIS, le système national d’information de protection sociale, a été revendiqué par l’acteur malveillant Spirigatito avec environ 34,1 millions d’enregistrements (500 Go) prétendument exfiltrés, pouvant affecter jusqu’à 15 millions de personnes. Les catégories de données exposées incluent des données personnelles, socioéconomiques, financières et GPS complètes. L’une des plus grandes fuites gouvernementales d’Afrique subsaharienne recensées par AFRINTEL.

---

### 🇨🇲 Cameroun (1 incident)

Loozap, une plateforme de petites annonces et de commerce en ligne, a eu 34 000 comptes utilisateurs divulgués par l’acteur malveillant zimablue, incluant des mots de passe hashés en SHA1, des adresses IP et des données personnelles. L’utilisation du SHA1 témoigne de pratiques de sécurité insuffisantes. Date de l’incident : 28 janvier, identifié en mars.

---

### 🇩🇿 Algérie (1 incident)

Bridges (tebridges.dz), un prestataire de services CRM, a eu une base de données de 672 000 enregistrements vendue 1 743 $ par l’acteur malveillant Grubder. Date d’attaque : 2 février, identifiée en mars.

---

### 🇬🇳 Guinée (1 incident : suspecté)

Les tableaux de bord DHIS2 du ministère de la Santé de Guinée auraient été compromis par l’acteur malveillant Keymous. L’activité a été observée en juillet 2025 et identifiée en mars 2026. Des données personnelles du personnel gouvernemental et des outils de surveillance sanitaire ont été potentiellement exposés. Les artefacts publiés suggèrent un accès par identifiants plutôt qu’un dump conventionnel. Partiellement confirmé.

---

### 🇲🇬 Madagascar (1 incident)

Orange Madagascar, l’opérateur télécom national de référence et leader du marché, a été revendiqué par l’acteur malveillant Qilin. Cibler un opérateur télécom national critique fait peser des risques sur la connectivité et les communications.

---

### 🇹🇳 Tunisie (1 incident)

K.PROPHA, une entreprise de distribution pharmaceutique, a été revendiquée par l’acteur malveillant TheGentlemen.

---

### 🇳🇦 Namibie (1 incident)

Namibia Airports Company, l’autorité gérant les infrastructures aéroportuaires nationales, a été revendiquée par l’acteur malveillant INC Ransom. Les aéroports constituent des infrastructures nationales critiques aux implications sécuritaires à la fois physiques et numériques.

---

### 🇹🇿 Tanzanie (1 incident)

SBC Tanzania, partenaire d’embouteillage PepsiCo et distributeur de boissons, a été revendiquée par l’acteur malveillant Morpheus.

---

### 🇨🇩 RDC (1 incident : historique)

Le FRAP, fonds de réforme de l’administration publique, a subi une intrusion en septembre 2025 par l’acteur malveillant privillege, avec l’incident identifié et signalé en mars 2026. Ce cas illustre le délai fréquent entre l’intrusion et la divulgation publique dans les entités d’administration publique.

---

## 5. Analyse détaillée par type d’incident

### 5.1 Ransomware (19 incidents)

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

```mermaid
pie
 title les acteurs les plus actifs
 "CrowStealer (5)" : 5
 "APT73/BASHE (4)" : 4
 "XP95 (3)" : 3
 "xNov (3)" : 3
 "Qilin (2)" : 2
 "The Gentlemen (2)" : 2
 "INC Ransom (2)" : 2
```

### 5.2 Fuites de données / intrusions système (22 incidents)

| Pays             | Fuites/Intrusions | Acteurs principaux |
|------------------|-------------------|---------------------|
| Égypte           | 5                 | CrowStealer (5) |
| Afrique du Sud   | 6                 | xNov (2), TelephoneHooliganism, Blackwinter99, XP95|
| Maroc            | 3                 | xNov (2), anisanas2 |
| Nigeria          | 2                 | AshleyWood2022, Bytetobreach |
| Cameroun         | 1                 | zimablue |
| Algérie          | 1                 | Grubder |
| Sénégal          | 1                 | Réseau coordonné |
| Guinée           | 1                 | Keymous |
| Zambie           | 1                 | Spirigatito |
| RDC              | 1                 | privillege |

**Observations clés** :
- **CrowStealer** domine les fuites égyptiennes, y compris une base de données médicale de 3,8 millions de patients (ministère de la Santé) vendue 2 500 $.
- **xNov** a exposé des dossiers étudiants (ONOUSC, 3 631 entrées), les données supply chain de L’Oréal Maroc (296 pharmacies, 361 000 ventes, secrets OAuth2), et la base de données d’Eventing South Africa (équitation).
- **UBA Sénégal** (révélé en mars, exécuté fin janvier) : les attaquants ont compromis le système d’information interne, manipulé les bases de données (création/modification de comptes, augmentation des plafonds de retrait, transferts de fonds), puis coordonné plus de 3 400 retraits GAB en quelques heures, emportant 1,143 milliard FCFA (~1,9 M USD). Vulnérabilités probables : absence de SOC temps réel, procédures antifraude insuffisantes, possible complicité interne.
- **Loozap (Cameroun)** - 34 000 comptes utilisateurs divulgués avec mots de passe hashés en SHA1, adresses IP, données personnelles.
- **Ministère de la Santé de Guinée** - compromission suspectée des tableaux de bord DHIS2 par Keymous, exposant des outils de surveillance sanitaire et des données gouvernementales (emails, personnels).
- Fuites massives au Nigeria : Remita (3 To, incluant documents KYC et clés HSM gouvernementales) et université Ahmadu Bello (11 000+ dossiers).

## 6. Impact sectoriel

| Secteur                  | Incidents | Pourcentage |
|--------------------------|-----------|-------------|
| Gouvernement / Admin     | 10        | 24,4 %      |
| Éducation / Université   | 7         | 17,1 %      |
| Santé                    | 4         | 9,8 %       |
| Assurance                | 3         | 7,3 %       |
| Télécommunications       | 3         | 7,3 %       |
| Ingénierie/Construction  | 3         | 7,3 %       |
| Finance / Banque         | 2         | 4,9 %       |
| IT/Consulting            | 2         | 4,9 %       |
| Fintech                  | 1         | 2,4 %       |
| E-commerce / Annonces    | 1         | 2,4 %       |
| Sport / Loisirs          | 1         | 2,4 %       |
| Autres                   | 4         | 9,8 %       |

**Enseignements** :
- Le secteur public (gouvernement + éducation) représente **41,5 %** des incidents.
- Les données de santé restent très valorisées : fuite du ministère de la Santé égyptien (3,8 M d’enregistrements), fuites d’assurances sud-africaines, compromission du ministère de la Santé guinéen.
- Les télécoms (Orange Madagascar, Maroc Telecom) sont des cibles stratégiques.
- L’incident UBA Sénégal illustre une nouvelle tendance : **fraude financière directe par compromission système**, contournant le ransomware classique.
- Les plateformes de e‑commerce (Loozap) sont de plus en plus ciblées pour le vol d’identifiants.

## 7. Profil des acteurs

| Acteur           | Type           | Incidents | Cibles principales |
|------------------|----------------|-----------|---------------------|
| CrowStealer      | Courtier de données | 5    | Gouvernement et éducation égyptiens |
| APT73/BASHE      | Ransomware     | 4         | Institutions d’État marocaines |
| XP95             | Ransomware     | 3         | Gouvernement sud-africain |
| xNov             | Fuite de données | 3       | Supply chain marocaine, sport sud-africain, éducation |
| Qilin            | Ransomware     | 2         | Maroc, Madagascar |
| The Gentlemen    | Ransomware     | 2         | Tunisie, Afrique du Sud |
| INC Ransom       | Ransomware     | 2         | Namibie, Afrique du Sud |

**Acteurs émergents** : xNov (ciblage supply chain), XP95 (gouvernement sud-africain), zimablue (e‑commerce camerounais), Keymous (ministères de la santé ouest-africains), Grubder (secteur tech algérien).

### 7.1 Niveau de risque

| Pays | Risque |
|------|--------|
| Afrique du Sud | 🔴 Critique |
| Maroc | 🔴 Élevé |
| Égypte | 🔴 Élevé |
| Nigeria | 🟠 Moyen-Élevé |
| Sénégal | 🟠 Moyen (post-UBA) |
| Cameroun | 🟠 Moyen (émergent) |
| Guinée | 🟠 Moyen |
| Autres | 🟠 Moyen |

## 8. Tendances clés et lacunes de renseignement

### Tendances
1. **Évolution des ransomwares** - XP95 et d’autres vendent les données exfiltrées plutôt que de simplement chiffrer.
2. **Attaques de la supply chain** - Smarteez (prestataire de L’Oréal Maroc) montre la vulnérabilité des sous-traitants digitaux.
3. **Fuites massives de données de santé** - Ministère de la Santé égyptien (3,8 M d’enregistrements) révèle des failles dans la sécurité des systèmes publics.
4. **Ciblage géopolitique** - APT73/BASHE concentré sur les médias et télécoms d’État marocains.
5. **Fraude financière directe par compromission système** - UBA Sénégal démontre que les attaquants contournent le ransomware pour aller directement à l’argent, exploitant des SOC et contrôles antifraude faibles.
6. **Vol d’identifiants sur les plateformes e‑commerce** - Loozap (Cameroun) : fuite de 34 000 comptes avec hashage SHA1 faible.

### Lacunes
- De nombreuses attaques restent non détectées ou non déclarées ; cette liste ne couvre que les incidents publics.
- Les volumes de données annoncés peuvent être gonflés.
- L’attaque UBA Sénégal a eu lieu fin janvier mais n’a été révélée qu’en mars - délai important dans la prise de conscience publique.
- La compromission du ministère de la Santé guinéen reste partiellement confirmée (accès corrélé, pas de divulgation complète).

## 9. Mapping MITRE ATT&CK (contextuel)

| Incident | Techniques |
|----------|-----------|
| Smarteez | T1552 |
| Gauteng | T1041 |
| ONOUSC | T1078 |
| Santé Égypte | T1005 |
| UBA Sénégal | T1190, T1078, T1048, T1531 |
| Loozap | T1190, T1005 (stockage SHA1 faible) |
| Santé Guinée | T1190, T1078 (suspecté) |

**Techniques observées couramment** :
- T1566 - Phishing  
- T1190 - Exploitation web  
- T1041 - Exfiltration  
- T1078 - Comptes valides  
- T1486 - Ransomware  
- T1531 - Manipulation de comptes (UBA Sénégal)

## 10. Recommandations

### Pour les gouvernements et entreprises africains
- **Sécurité des bases de données** : chiffrement des données sensibles, contrôles d’accès, audits réguliers.
- **Gestion des risques tiers** : auditer les prestataires de services digitaux, imposer des clauses de cybersécurité.
- **Réponse aux incidents** : sauvegardes hors ligne, exercices de simulation, protocoles de communication.
- **Formation des utilisateurs** : sensibilisation au phishing (vecteur initial principal).
- **Supervision en temps réel** : déployer ou renforcer un SOC 24/7 ; mettre en place une détection d’anomalies transactionnelles (particulièrement pour les banques).
- **Mécanismes antifraude** : plafonds de retrait dynamiques, blocage automatique en cas de schéma anormal, analyse comportementale.
- **Sécurité des mots de passe** : imposer un hashage fort (bcrypt, Argon2) au lieu de SHA1 ; activer la MFA pour tous les comptes utilisateurs.

### Pour les analystes CTI
- Surveiller **XP95**, **xNov**, **zimablue**, **Keymous** pour de nouvelles campagnes.
- Cartographier les expositions de la supply chain (notamment marketing digital et logistique).
- Prioriser la surveillance des secteurs gouvernemental, éducatif et de la santé en Afrique du Nord, Ouest et Australe.
- Surveiller les **intrusions financières non ransomware** - UBA Sénégal n’est probablement pas un cas isolé.

## 11. Recommandations SOC tactiques

- Détection exfiltration (T1041)  
- Surveillance comptes privilégiés  
- Analyse trafic sortant  
- Monitoring API / OAuth  
- Pour les banques : détection en temps réel des anomalies de retraits GAB (vélocité, localisation, pics de montants)

## 12. Recommandations stratégiques

- Activer MFA  
- Segmenter le réseau (séparer réseau GAB du cœur bancaire)  
- Auditer les prestataires  
- Maintenir des sauvegardes offline  
- Effectuer des exercices de crise incluant des simulations red-team  
- **Cadre réglementaire** : les banques centrales devraient imposer des standards minimaux de SOC et de détection de fraude

## 13. Conclusion

Mars 2026 confirme que **l’Afrique est une cible privilégiée pour la cybercriminalité industrialisée**. La convergence des groupes ransomware, courtiers de données, attaques supply chain, intrusions financières directes (UBA Sénégal) et vols d’identifiants sur plateformes e‑commerce (Loozap) crée un environnement à haut risque. L’Afrique du Sud, le Maroc et l’Égypte restent les plus touchés, mais **l’Afrique de l’Ouest et centrale émergent comme de nouveaux points chauds** (Sénégal, Cameroun, Guinée). Les ministères de la santé sont de plus en plus ciblés, comme en Égypte et en Guinée. Les institutions financières et les plateformes de e‑commerce doivent urgemment renforcer leur supervision en temps réel, leurs capacités antifraude et la sécurité des mots de passe. AFRINTEL continuera de suivre ces évolutions.

**AFRINTEL** - Cyber Threat Intelligence africaine  
[GitHub AFRINTEL](https://github.com/Hatchepsoute/AFRINTEL)
