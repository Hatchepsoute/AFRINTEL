[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Afrique-orange)
![Threat Type](https://img.shields.io/badge/Menace-Ransomware-red)
![Data Source](https://img.shields.io/badge/Source%20des%20données-RQL%20export-darkgreen)
![Intel Type](https://img.shields.io/badge/Type%20d'Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques - Mars 2026 (41 victimes)
👉🏾 [**English version available here**](./victims.md)

## Portée et méthodologie
Cette liste recense les incidents de ransomware et fuites de données ciblant des entités africaines pour le mois de mars 2026. Les données sont extraites et normalisées à partir des exports de surveillance des sites de fuite (DLS) et de sources OSINT complémentaires.

**Points de contrôle appliqués :**
- **Intégrité :** Chaque ligne du dataset source est conservée comme un incident distinct.
- **Normalisation :** Harmonisation visuelle des noms de groupes (ex: LockBit 5.0, Qilin, APT73/Bashe).
- **Vérification :** Validation des URLs institutionnelles et enrichissement des descriptions techniques.

## Synthèse rapide
- **Victimes recensées :** 41
- **Pays touchés :** 14
- **Acteurs observés :** 27
- **Pays les plus touchés :** Afrique du Sud (13), Maroc (8), Égypte (8)

### Typologie des incidents
- **Ransomware (chiffrement + rançon) :** 19 incidents (46,3 %)
- **Fuites de données / intrusions système :** 22 incidents (53,7 %)

### Répartition par pays
- 🇿🇦 Afrique du Sud : **13** victimes
- 🇲🇦 Maroc : **8** victimes
- 🇪🇬 Égypte : **8** victimes
- 🇳🇬 Nigeria : **2** victimes
- 🇨🇲 Cameroun : **1** victime
- 🇩🇿 Algérie : **1** victime
- 🇸🇳 Sénégal : **1** victime
- 🇬🇳 Guinée : **1** victime
- 🇿🇲 Zambie : **1** victime
- 🇲🇬 Madagascar : **1** victime
- 🇹🇳 Tunisie : **1** victime
- 🇳🇦 Namibie : **1** victime
- 🇹🇿 Tanzanie : **1** victime
- 🇨🇩 RDC : **1** victime

### Répartition par acteur
- **CrowStealer** : 5 victimes
- **APT73/BASHE** : 4 victimes
- **XP95** : 3 victimes
- **xNov** : 3 victimes
- **Qilin** : 2 victimes
- **The Gentlemen** : 2 victimes
- **INC Ransom** : 2 victimes
- **LockBit 5.0** : 1 victime
- **Crypto24** : 1 victime
- **PEAR** : 1 victime
- **Lynx** : 1 victime
- **Payload** : 1 victime
- **DragonForce** : 1 victime
- **NightSpire** : 1 victime
- **Morpheus** : 1 victime
- **Coinbase Cartel** : 1 victime
- **Spirigatito** : 1 victime
- **TelephoneHooliganism** : 1 victime
- **anisanas2** : 1 victime
- **AshleyWood2022** : 1 victime
- **Bytetobreach** : 1 victime
- **privillege** : 1 victime
- **Réseau coordonné (UBA Sénégal)** : 1 victime
- **Grubder (Bridges)** : 1 victime
- **Blackwinter99 (UNISA)** : 1 victime
- **zimablue (Loozap)** : 1 victime
- **Keymous (Santé Guinée)** : 1 victime

### Comparaison ransomware vs fuites par pays
| Pays                  | Ransomware | Fuites de données |
|-----------------------|------------|-------------------|
| 🇿🇦 Afrique du Sud     | 7          | 6                 |
| 🇲🇦 Maroc              | 5          | 3                 |
| 🇪🇬 Égypte             | 3          | 5                 |
| 🇳🇬 Nigeria            | 0          | 2                 |
| 🇨🇲 Cameroun           | 0          | 1                 |
| 🇩🇿 Algérie            | 0          | 1                 |
| 🇸🇳 Sénégal            | 0          | 1                 |
| 🇬🇳 Guinée             | 0          | 1                 |
| 🇿🇲 Zambie             | 0          | 1                 |
| 🇲🇬 Madagascar         | 1          | 0                 |
| 🇹🇳 Tunisie            | 1          | 0                 |
| 🇳🇦 Namibie            | 1          | 0                 |
| 🇹🇿 Tanzanie           | 1          | 0                 |
| 🇨🇩 RDC                | 0          | 1                 |

## Mars 2026

### 01 Mars 2026
#### 🇿🇦 Afrique du Sud - Diesel-Electric Group
- **Groupe ransomware :** LockBit 5.0
- **Secteur :** Automobile (Distribution et Services)
- **Site web :** [diesel-electric.co.za](https://diesel-electric.co.za)
- **Statut :** Revendication
- **Description victime :** Distributeur majeur de composants automobiles en Afrique australe, incluant les franchises Bosch Service et les centres e-CAR.

#### 🇪🇬 Égypte - Canadian International College (CIC)
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [cic-cairo.edu.eg](https://www.cic-cairo.edu.eg/)
- **Statut :** Fuite de base de données
- **Description victime :** Premier fournisseur d'enseignement canadien en Égypte, associé à la Cape Breton University (CBU). La fuite (studentsdata.csv) contient 2 925 enregistrements : noms, filières, niveaux, GPA, années.

#### 🇿🇲 Zambie - Ministère du Développement Communautaire et des Services Sociaux
- **Acteur / Groupe :** Spirigatito
- **Secteur :** Gouvernement / Services sociaux
- **Site web :** [mcdss.gov.zm](https://www.mcdss.gov.zm)
- **Statut :** Fuite de base de données massive
- **Description victime :** Institution chargée de la protection sociale et de l'autonomisation. Fuite du système "Social Cash Transfer" (SCT) : identités complètes (noms, NRC, dates de naissance), coordonnées, montants des aides.

#### 🇿🇦 Afrique du Sud - Eventing South Africa
- **Acteur / Groupe :** xNov
- **Secteur :** Sport / Loisirs
- **Site web :** [eventingsa.co.za](https://www.eventingsa.co.za)
- **Date de la fuite :** 16 Janvier 2026 (Identifiée en Mars 2026)
- **Statut :** Fuite de base de données (Publique)
- **Description victime :** Eventing South Africa est l'organisme officiel régissant les compétitions de concours complet d'équitation. xNov a divulgué une base de données contenant des informations sur les clubs et les membres : noms, adresses e-mail, identifiants de connexion (mots de passe), détails d'affiliation, registres des chevaux et cavaliers, données de compétition, ainsi que des informations administratives et financières (paiements, factures).

#### 🇩🇿 Algérie - Bridges (tebridges.dz)
- **Acteur / Groupe :** Grubder
- **Secteur :** Technologie / Services aux entreprises (CRM)
- **Site web :** [tebridges.dz](https://www.tebridges.dz)
- **Date de l'incident :** 02 Février 2026
- **Statut :** Base de données en vente (1 743 $)
- **Description victime :** Bridges est un fournisseur de solutions technologiques en Algérie. Grubder a mis en vente une base de données d'environ 672 000 enregistrements actifs (PII et CRM) incluant noms complets, numéros de téléphone principaux, adresses locales détaillées, codes postaux et statuts de compte. Un échantillon de données (CSV) a validé l'extraction.

#### 🇨🇲 Cameroun - Loozap (loozap.com)
- **Acteur / Groupe :** zimablue
- **Secteur :** E-commerce / Petites annonces en ligne
- **Site web :** [loozap.com](http://loozap.com/)
- **Date de l'incident :** 28 janvier 2026 (identifiée en mars 2026)
- **Statut :** Base de données divulguée (~34 000 utilisateurs)
- **Description victime :** Loozap est une plateforme de petites annonces en ligne utilisée principalement en Afrique centrale. Un acteur malveillant a publié une base de données contenant environ 34 000 comptes utilisateurs. L’analyse de l’échantillon révèle la présence de données personnelles (emails, noms, localisation), adresses IP, ainsi que des mots de passe hashés en SHA1. Les données incluent également des informations de profil (genre, ville, interactions sociales) et des métadonnées d’activité utilisateur, confirmant une compromission complète de la base applicative.

### 02 Mars 2026
#### 🇪🇬 Égypte - Autorité de Régulation de la Gestion des Déchets (WMRA)
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Gouvernement / Environnement
- **Site web :** [garb.gov.eg](https://garb.gov.eg)
- **Statut :** Fuite de base de données
- **Description victime :** Organisme dépendant du Ministère de l'Environnement chargé de réguler la gestion des déchets. Base de données contenant des données administratives, registres internes, informations sur partenaires et personnel.

#### 🇪🇬 Égypte - Orascom Construction
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Ingénierie et construction
- **Site web :** [orascom.com](https://orascom.com/)
- **Statut :** Fuite de base de données
- **Description victime :** Leader de l'ingénierie et construction au Moyen-Orient, Afrique du Nord et États-Unis. Données compromises : staff_id, noms complets, emails professionnels, départements, postes.

#### 🇪🇬 Égypte - Ministère de la Santé et de la Population (E-Portal)
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Gouvernement / Santé
- **Site web :** [mohp.gov.eg](https://www.mohp.gov.eg)
- **Statut :** Fuite massive (vente à 2 500 $)
- **Description victime :** Base de données de 3,8 millions d'enregistrements (2019-2026) incluant noms complets, National ID, téléphones, adresses, diagnostics médicaux précis, types de chirurgies, établissements de traitement.

### 03 Mars 2026
#### 🇿🇦 Afrique du Sud - Walter Sisulu University (WSU)
- **Acteur / Groupe :** TelephoneHooliganism
- **Secteur :** Éducation / Université
- **Site web :** [wsu.ac.za](https://www.wsu.ac.za)
- **Statut :** Fuite de base de données (vente à 1 150 $)
- **Description victime :** Université publique du Cap Oriental. Données structurées en trois sections (Contacts, Inscriptions, Tickets) : dates de naissance, emails, adresses, GPA, bourses, historiques de support.

#### 🇪🇬 Égypte - Ministère de l'Éducation et de l'Enseignement Technique
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Gouvernement / Éducation
- **Site web :** [moe.gov.eg](https://moe.gov.eg)
- **Statut :** Fuite de base de données
- **Description victime :** Données sur étudiants et personnel : identifiants nationaux, noms complets, adresses, dossiers académiques.

#### 🇲🇦 Maroc - Office National des Œuvres Universitaires Sociales et Culturelles (ONOUSC)
- **Acteur / Groupe :** xNov
- **Secteur :** Éducation / Gouvernement
- **Site web :** [amo.onousc.ma](https://amo.onousc.ma)
- **Statut :** Fuite de données
- **Description victime :** Organisme chargé de la gestion des œuvres sociales pour les étudiants au Maroc (bourses, cités universitaires, couverture santé). Exposition des dossiers de 3 631 étudiants liés à l’Assurance Maladie Obligatoire (AMO) : noms, prénoms, CINE, numéros d’immatriculation universitaire, CNE, dates de naissance, statuts d’inscription.

### 04 Mars 2026
#### 🇲🇦 Maroc - Outsourcia
- **Groupe ransomware :** Qilin
- **Secteur :** Business Process Outsourcing (BPO)
- **Site web :** [outsourcia.com](https://www.outsourcia.com)
- **Statut :** Revendication
- **Description victime :** Opérateur majeur de la relation client basé à Casablanca, gérant des processus métiers pour des comptes internationaux.

### 05 Mars 2026
#### 🇪🇬 Égypte - Rowad Modern Engineering
- **Groupe ransomware :** Crypto24
- **Secteur :** Ingénierie et construction
- **Site web :** [rowad-rme.com](http://www.rowad-rme.com)
- **Statut :** Revendication
- **Description victime :** Société de construction égyptienne spécialisée dans les projets d'infrastructure et les bâtiments commerciaux.

### 06 Mars 2026
#### 🇪🇬 Égypte - INTERACT TECHNOLOGY SOLUTIONS
- **Groupe ransomware :** PEAR
- **Secteur :** IT Consulting
- **Site web :** [interactts.com](http://interactts.com)
- **Statut :** Revendication
- **Description victime :** Entreprise fournissant des solutions technologiques et d'infrastructure critique en Égypte.

#### 🇲🇬 Madagascar - Orange Madagascar
- **Groupe ransomware :** Qilin
- **Secteur :** Télécommunications
- **Site web :** [orange.mg](https://www.orange.mg/)
- **Statut :** Revendication
- **Description victime :** Leader des télécommunications à Madagascar, opérant sur l'internet, le mobile et le mobile banking.

### 09 Mars 2026
#### 🇹🇳 Tunisie - K.PROPHA (Karray Produits Pharmaceutiques)
- **Groupe ransomware :** The Gentlemen
- **Secteur :** Santé / Pharmaceutique
- **Site web :** [kpropha.com](http://kpropha.com)
- **Statut :** Revendication
- **Description victime :** Entreprise tunisienne spécialisée dans la distribution de produits pharmaceutiques et parapharmaceutiques.

### 12 Mars 2026
#### 🇲🇦 Maroc - HACA (Haute Autorité de la Communication Audiovisuelle)
- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Gouvernement / Médias
- **Site web :** [haca.ma](http://haca.ma)
- **Statut :** Revendication
- **Description victime :** Instance constitutionnelle chargée de la régulation de la communication audiovisuelle au Maroc.

### 13 Mars 2026
#### 🇿🇦 Afrique du Sud - Lion of Africa Insurance
- **Groupe ransomware :** Lynx
- **Secteur :** Services d'assurance
- **Site web :** [lionsureins.com](http://lionsureins.com/)
- **Statut :** Revendication
- **Description victime :** Compagnie d'assurance sud-africaine traitant des volumes importants de données personnelles et financières.

#### 🇿🇦 Afrique du Sud - Gouvernement Provincial de Gauteng
- **Acteur / Groupe :** XP95
- **Secteur :** Gouvernement / Administration publique
- **Site web :** [gauteng.gov.za](https://www.gauteng.gov.za)
- **Statut :** Fuite massive (vente à 25 000 $)
- **Description victime :** Gestion de la province la plus peuplée d'Afrique du Sud (Johannesburg, Pretoria). 3,8 To de données (3,6 millions de fichiers) exfiltrés : santé, éducation, logement, développement économique.

### 14 Mars 2026
#### 🇪🇬 Égypte - Grid Fine Finishes
- **Groupe ransomware :** Payload
- **Secteur :** Aménagement / Construction
- **Site web :** [gridff.com](http://gridff.com)
- **Statut :** Revendication
- **Description victime :** Société égyptienne spécialisée dans l'aménagement intérieur haut de gamme pour les secteurs commerciaux et résidentiels.

### 17 Mars 2026
#### 🇿🇦 Afrique du Sud - University of South Africa (UNISA)
- **Acteur / Groupe :** Blackwinter99
- **Secteur :** Éducation / Enseignement Supérieur
- **Site web :** [unisa.ac.za](https://www.unisa.ac.za)
- **Statut :** Fuite de données (divulgation d'identifiants admin)
- **Description victime :** L'UNISA est la plus grande institution d'enseignement à distance en Afrique. Blackwinter99 a divulgué publiquement sur un forum clandestin les identifiants de connexion de la page d'administration du site, offrant un accès direct aux privilèges élevés de la plateforme, permettant l'exfiltration massive de données étudiantes, la modification des dossiers académiques ou une prise de contrôle totale de l'infrastructure web.

### 19 Mars 2026
#### 🇳🇦 Namibie - Namibia Airports Company
- **Groupe ransomware :** INC Ransom
- **Secteur :** Transport aérien
- **Site web :** [airports.com.na](http://airports.com.na)
- **Statut :** Revendication
- **Description victime :** Gestionnaire officiel des aéroports nationaux en Namibie.

### 20 Mars 2026
#### 🇿🇦 Afrique du Sud - The Unlimited
- **Groupe ransomware :** DragonForce
- **Secteur :** Services d'assurance
- **Site web :** [theunlimited.co.za](http://theunlimited.co.za)
- **Statut :** Revendication (137 Go exfiltrés)
- **Description victime :** Fournisseur de produits d'assurance incluant la santé, l'auto, le juridique et la vie.

#### 🇲🇦 Maroc - Ministère de la Justice
- **Acteur / Groupe :** anisanas2
- **Secteur :** Gouvernement / Justice
- **Site web :** [justice.gov.ma](https://www.justice.gov.ma)
- **Statut :** Fuite massive (300 Go)
- **Description victime :** Exfiltration de 300 Go incluant plus de 150 000 dossiers de procédures judiciaires (2019-2026). Litiges opposant grandes entreprises marocaines à des particuliers (12 Mds MAD). Documents : pièces d'identité, relevés bancaires, actes judiciaires, factures.

### 21 Mars 2026
#### 🇿🇦 Afrique du Sud - Elundini Local Municipality
- **Groupe ransomware :** The Gentlemen
- **Secteur :** Administration locale
- **Site web :** [elundini.gov.za](http://elundini.gov.za)
- **Statut :** Revendication
- **Description victime :** Administration municipale dédiée au développement durable dans la province du Cap Oriental.

### 22 Mars 2026
#### 🇿🇦 Afrique du Sud - Semenya Furumele Consulting Engineers
- **Groupe ransomware :** NightSpire
- **Secteur :** Ingénierie conseil
- **Site web :** [sfce.co.za](http://www.sfce.co.za)
- **Statut :** Revendication
- **Description victime :** Cabinet de conseil en ingénierie basé en Afrique du Sud.

### 24 Mars 2026
#### 🇸🇳 Sénégal - United Bank for Africa (UBA Sénégal)
- **Acteur / Groupe :** Réseau coordonné (suspicions de complicités internes)
- **Secteur :** Finance / Banque
- **Site web :** [ubasenegal.com](https://www.ubasenegal.com)
- **Date de l’attaque :** 30-31 janvier 2026 (révélée le 24 mars 2026)
- **Statut :** Intrusion système & fraude massive (1,143 milliard FCFA ~ 1,9 million USD)
- **Description victime :** UBA Sénégal a subi une cyberattaque d’une ampleur exceptionnelle. En quelques heures, plus de 3 400 retraits frauduleux ont été effectués dans les GAB de plusieurs villes (Dakar, Thiès, Kaolack). Les attaquants ont compromis le système d’information interne, manipulé les bases de données (création/modification de comptes, augmentation des plafonds de retrait, transferts de fonds depuis des clients légitimes), puis ont coordonné des retraits simultanés pour vider les distributeurs avant détection. Vulnérabilités probables : absence de supervision SOC en temps réel, procédures antifraude insuffisantes sur les retraits massifs, possible complicité interne, et mauvaise configuration des dispositifs de sécurité. Cet incident est un signal d’alarme majeur pour les institutions financières ouest‑africaines.

### 26 Mars 2026
#### 🇿🇦 Afrique du Sud - ETFSA
- **Groupe ransomware :** INC Ransom
- **Secteur :** Wealth Management
- **Site web :** [etfsa.co.za](http://ETFSA.co.za)
- **Statut :** Revendication (données clients exfiltrées)
- **Description victime :** Plateforme sud-africaine de services financiers spécialisée dans les fonds négociés en bourse (ETF).

#### 🇲🇦 Maroc - Maroc Telecom
- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Télécommunications
- **Site web :** [iam.ma](http://iam.ma)
- **Statut :** Revendication
- **Description victime :** Opérateur historique de télécommunications au Maroc, fournissant services mobiles, internet et fixes.

#### 🇲🇦 Maroc - 2M TV
- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Médias et audiovisuel
- **Site web :** [2m.ma](http://2m.ma)
- **Statut :** Revendication
- **Description victime :** Chaîne de télévision nationale marocaine.

#### 🇲🇦 Maroc - Institut Royal des Études Stratégiques (IRES)
- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Recherche / Think tank
- **Site web :** [ires.ma](http://ires.ma)
- **Statut :** Revendication
- **Description victime :** Centre d'analyse stratégique rattaché au Cabinet Royal marocain.

### 29 Mars 2026
#### 🇿🇦 Afrique du Sud - Statistics South Africa (Stats SA)
- **Groupe ransomware :** XP95
- **Secteur :** Gouvernement / Statistiques Nationales
- **Site web :** [statssa.gov.za](https://www.statssa.gov.za)
- **Statut :** Ransomware / Vente de base de données (100 000 $)
- **Description victime :** Stats SA est l'agence nationale de statistique de l'Afrique du Sud. XP95 a exfiltré 154 Go de données (453 362 fichiers). La brèche compromet potentiellement des données socio-économiques sensibles, des recensements, des informations sur l'emploi, l'inflation et des registres administratifs nationaux. Une rançon de 100 000 $ a été exigée avant une mise en vente publique prévue pour le 20 avril 2026.

#### 🇿🇦 Afrique du Sud - Gauteng City Region Academy (GCRA)
- **Groupe ransomware :** XP95
- **Secteur :** Éducation / Formation (Gouvernement provincial)
- **Site web :** [gcra.gauteng.gov.za](https://gcra.gauteng.gov.za)
- **Statut :** Ransomware / Vente de base de données
- **Description victime :** La GCRA est l'agence responsable du développement des compétences pour la province de Gauteng. L'exfiltration de 147 Go de données compromet potentiellement les dossiers des étudiants (bourses, inscriptions, PII), les données des programmes de formation et les documents administratifs de l'académie. XP95 a fixé une date limite pour le paiement de la rançon avant la mise en vente publique des fichiers.

### 30 Mars 2026
#### 🇹🇿 Tanzanie - SBC Tanzania Limited
- **Groupe ransomware :** Morpheus
- **Secteur :** Agroalimentaire
- **Site web :** [sbctanzania.co.tz](http://sbctanzania.co.tz)
- **Statut :** Revendication
- **Description victime :** Fabricant et distributeur de boissons, embouteilleur officiel de PepsiCo en Tanzanie.

#### 🇿🇦 Afrique du Sud - Nashua
- **Groupe ransomware :** Coinbase Cartel
- **Secteur :** IT & Managed Services
- **Site web :** [nashua.co.za](http://nashua.co.za)
- **Statut :** Revendication
- **Description victime :** Fournisseur majeur de solutions technologiques intégrées et de services gérés pour entreprises.

#### 🇳🇬 Nigeria - Université Ahmadu Bello (ABU Zaria)
- **Acteur / Groupe :** AshleyWood2022
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [abu.edu.ng](https://www.abu.edu.ng)
- **Statut :** Fuite de base de données
- **Description victime :** L'une des plus grandes universités de recherche du Nigeria. Base de données (`tbl_flattened.csv` & `abu.sql`) avec plus de 11 000 enregistrements : personnel académique et non-académique (noms, départements, rangs, qualifications, sexe, date de naissance, districts d'origine).

### 31 Mars 2026
#### 🇳🇬 Nigeria - Remita (SystemSpecs)
- **Acteur / Groupe :** Bytetobreach
- **Secteur :** Fintech / Services de paiement
- **Site web :** [remita.net](https://www.remita.net)
- **Statut :** Fuite massive (3 To)
- **Description victime :** Plateforme de paiement majeure au Nigeria utilisée par particuliers, entreprises et gouvernement. Brèche de 3 To : 800 Go de documents KYC (pièces d'identité, passeports, relevés bancaires, factures), bases MySQL/Postgres, codes sources, registres Docker, clés HSM gouvernementales, plus de 35 000 hashes de mots de passe.

#### 🇲🇦 Maroc - Smarteez (Prestataire L’Oréal Maroc - Supply Chain)
- **Acteur / Groupe :** xNov
- **Secteur :** Marketing Digital / Cosmétique (Supply Chain L'Oréal)
- **Site web :** [smarteez.eu](https://smarteez.eu)
- **Statut :** Compromission supply chain / Fuite de base de données
- **Description victime :** Smarteez est un prestataire digital marocain utilisé par L’Oréal Maroc pour la gestion de ses opérations terrain. Exposition de données critiques : informations sur 296 pharmacies (GPS, segmentation), 361 000 enregistrements de ventes/KPI, 22 secrets d’applications OAuth2 en clair, logs administratifs complets. Une APK de production a également été divulguée.

#### 🇨🇩 RDC - Fonds pour la Réforme de l'Administration Publique (FRAP)
- **Acteur / Groupe :** privillege
- **Secteur :** Gouvernement / Administration
- **Site web :** [frap.cd](https://frap.cd/)
- **Date de la fuite :** Septembre 2025 (identifiée en mars 2026)
- **Statut :** Fuite de base de données (archive historique)
- **Description victime :** Organisme en charge de la modernisation de l'administration en RDC. Données exfiltrées en septembre 2025 : dossiers administratifs et informations sur les agents de l'État.

#### 🇬🇳 Guinée - Ministère de la Santé (sante.gov.gn)
- **Acteur / Groupe :** Keymous
- **Secteur :** Gouvernement / Santé publique
- **Site web :** [sante.gov.gn](https://sante.gov.gn/)
- **Date de l'incident :** Juillet 2025 (activité observée, identifiée en mars 2026)
- **Statut :** Compromission suspectée (corrélée à accès systèmes internes et fuites de données)
- **Description victime :** Le site officiel du Ministère de la Santé de Guinée est directement lié aux systèmes internes compromis, notamment les dashboards DHIS2 exposés par Keymous. La corrélation entre l’accès aux outils de surveillance sanitaire, les données gouvernementales divulguées (emails, personnels) et les infrastructures ministérielles suggère une compromission plus large de l’écosystème numérique du ministère. Cette exposition pourrait permettre des attaques ciblées, de la manipulation de données sanitaires et des opérations d’influence.
