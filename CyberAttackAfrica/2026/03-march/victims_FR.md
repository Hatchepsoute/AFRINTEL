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
- **Pays touchés :** 12 (plus 1 incident multi-pays)
- **Acteurs observés :** 26 acteurs attribués ; 1 incident sans attribution publique
- **Pays les plus touchés :** Afrique du Sud (13), Maroc (8), Égypte (9)

### Typologie des incidents
- **Revendications ou publications ransomware :** 19 incidents (46,3 %)
- **Fuites de données / intrusions système :** 22 incidents (53,7 %)

### Incidents marquants

- **Égypte :** 3,8 millions d’enregistrements revendiqués dans un incident attribué au ministère de la Santé.
- **Maroc :** une publication de 300 Go attribuée au ministère de la Justice comprenait des dossiers judiciaires.
- **Sénégal :** selon l’avis ngCERT ngCERT-2026-060005, l’opération de cash-out visant UBA Sénégal a impliqué 3 421 transactions GAB. Les pertes avaient été précédemment rapportées à 1,143 milliard de FCFA ; le ngCERT les présente comme supérieures à 2 millions USD.
- **Afrique du Sud :** une exposition de 3,8 To a été attribuée au gouvernement provincial du Gauteng.

> Les fiches ci-dessous documentent des revendications, publications ou incidents signalés. AFRINTEL ne confirme pas une compromission sans élément indépendant.

### Répartition par pays
- 🇿🇦 Afrique du Sud : **13** victimes
- 🇲🇦 Maroc : **8** victimes
- 🇪🇬 Égypte : **9** victimes
- 🇳🇬 Nigeria : **2** victimes
- 🌍 Multi-pays (Afrique) : **1** victime
- 🇩🇿 Algérie : **1** victime
- 🇸🇳 Sénégal : **1** victime
- 🇬🇳 Guinée : **1** victime
- 🇿🇲 Zambie : **1** victime
- 🇲🇬 Madagascar : **1** victime
- 🇹🇳 Tunisie : **1** victime
- 🇳🇦 Namibie : **1** victime
- 🇹🇿 Tanzanie : **1** victime

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
- **Al-Sheikh** : 1 victime
- **Grubder (Bridges)** : 1 victime
- **Blackwinter99 (UNISA)** : 1 victime
- **zimablue (Loozap)** : 1 victime
- **Keymous (Santé Guinée)** : 1 victime

### Comparaison ransomware vs fuites par pays
| Pays                  | Ransomware | Fuites de données |
|-----------------------|------------|-------------------|
| 🇿🇦 Afrique du Sud     | 7          | 6                 |
| 🇲🇦 Maroc              | 5          | 3                 |
| 🇪🇬 Égypte             | 3          | 6                 |
| 🇳🇬 Nigeria            | 0          | 2                 |
| 🌍 Multi-pays          | 0          | 1                 |
| 🇩🇿 Algérie            | 0          | 1                 |
| 🇸🇳 Sénégal            | 0          | 1                 |
| 🇬🇳 Guinée             | 0          | 1                 |
| 🇿🇲 Zambie             | 0          | 1                 |
| 🇲🇬 Madagascar         | 1          | 0                 |
| 🇹🇳 Tunisie            | 1          | 0                 |
| 🇳🇦 Namibie            | 1          | 0                 |
| 🇹🇿 Tanzanie           | 1          | 0                 |

## Mars 2026

### 01 Mars 2026
#### 🇿🇦 Afrique du Sud - Diesel-Electric Group
- **Groupe ransomware :** LockBit 5.0
- **Secteur :** Automobile (Distribution et Services)
- **Site web :** [diesel-electric.co.za](https://diesel-electric.co.za)
- **Statut :** Claim - Unverified
- **Description victime :** Distributeur majeur de composants automobiles en Afrique australe, incluant les franchises Bosch Service et les centres e-CAR.

#### 🇪🇬 Égypte - Canadian International College (CIC)
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [cic-cairo.edu.eg](https://www.cic-cairo.edu.eg/)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Premier fournisseur d'enseignement canadien en Égypte, associé à la Cape Breton University (CBU). La fuite (studentsdata.csv) contient 2 925 enregistrements : noms, filières, niveaux, GPA, années.

#### 🇿🇲 Zambie - ZISPIS (Zambia Integrated Social Protection Information System)
- **Acteur / Groupe :** Spirigatito
- **Secteur :** Gouvernement / Protection sociale
- **Site web :** [mcdss.gov.zm](https://www.mcdss.gov.zm)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Le système ZISPIS, registre national unifié utilisé par le gouvernement zambien pour gérer les programmes de protection sociale, a été compromis. L’attaque aurait impacté environ 15 millions de bénéficiaires avec plus de 34 millions d’enregistrements exposés. Les données incluent des informations personnelles complètes (nom, date de naissance, genre, identifiants nationaux), des données socio-économiques détaillées (situation du foyer, niveau d’éducation, conditions de vie), ainsi que des données financières (paiements, cycles, soldes) et géographiques (coordonnées GPS). Les échantillons publiés confirment également l’exposition de logs systèmes et d’activités utilisateurs, indiquant une compromission profonde de la plateforme applicative.

- **Analyse :**
  AFRINTEL a consulté la publication de l'acteur malveillant Spirigatito sur un forum cybercriminel, intitulée « Government of Zambia (ZIPSIS) - 34M », ainsi qu'un échantillon de données associé. L'échantillon se compose d'exports au format JSON provenant du système ZISPIS, exploité par le Ministry of Community Development and Social Services (mcdss.gov.zm) dans le cadre du programme de transferts monétaires sociaux (Social Cash Transfer). Les enregistrements de bénéficiaires observés incluent nom complet, genre, date de naissance, identifiant national, coordonnées GPS du foyer, district et village de résidence, situation socio-économique détaillée (type d'habitation, accès à l'eau et à l'électricité, sécurité alimentaire, situation de handicap) ainsi que des données de paiement (montants, cycles, canal de versement, agent de paiement et ses coordonnées). L'échantillon inclut également des journaux d'activité applicatifs associés à des comptes d'agents gouvernementaux nommément identifiés (adresses e-mail aux domaines mcdss.gov.zm et cbt.gov.zm), avec des actions telles que la mise à jour de dossiers bénéficiaires, la validation de paiements, la génération de rapports et la clôture de dossiers pour cause de décès. Ces éléments sont cohérents avec un accès direct à la base de données applicative de ZISPIS et à ses journaux d'audit, plutôt qu'avec un simple export partiel. AFRINTEL ne reproduit aucun nom, identifiant national, numéro de téléphone ni coordonnée GPS individuels issus de cet échantillon. AFRINTEL n'a pas eu accès à l'intégralité des 34 millions d'enregistrements revendiqués et ne peut pas confirmer ce volume total ni le vecteur d'accès initial.

#### 🇿🇦 Afrique du Sud - Eventing South Africa
- **Acteur / Groupe :** xNov
- **Secteur :** Sport / Loisirs
- **Site web :** [eventingsa.co.za](https://www.eventingsa.co.za)
- **Date de la fuite :** 16 Janvier 2026 (Identifiée en Mars 2026)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Eventing South Africa est l'organisme officiel régissant les compétitions de concours complet d'équitation. xNov a divulgué une base de données contenant des informations sur les clubs et les membres : noms, adresses e-mail, identifiants de connexion (mots de passe), détails d'affiliation, registres des chevaux et cavaliers, données de compétition, ainsi que des informations administratives et financières (paiements, factures).

#### 🇩🇿 Algérie - Bridges (tebridges.dz)
- **Acteur / Groupe :** Grubder
- **Secteur :** Technologie / Services aux entreprises (CRM)
- **Site web :** [tebridges.dz](https://www.tebridges.dz)
- **Date de l'incident :** 02 Février 2026
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Bridges est un fournisseur de solutions technologiques en Algérie. Grubder a mis en vente une base de données d'environ 672 000 enregistrements actifs (PII et CRM) incluant noms complets, numéros de téléphone principaux, adresses locales détaillées, codes postaux et statuts de compte. Un échantillon de données (CSV) a validé l'extraction.

  Le même jour (02 février 2026), un second compte, Dripper, a publié une annonce distincte proposant le même volume revendiqué (~672 000 enregistrements) pour le même domaine, avec un prix de 143 dollars et un contact Telegram/Session. AFRINTEL considère qu'il s'agit très probablement d'une republication ou d'une revente de la même base plutôt que d'une intrusion distincte. Le compte Dripper a depuis été banni par le forum pour tentative d'arnaque sur des données publiques, et l'échantillon associé à cette republication mélangeait un enregistrement libellé Afghanistan avec des enregistrements algériens, ce qui affaiblit la fiabilité de cette republication spécifique sans remettre en cause l'existence de la revendication initiale de Grubder.

#### 🌍 Afrique (Multi-pays) - Loozap (loozap.com)
- **Acteur / Groupe :** zimablue
- **Secteur :** E-commerce / Petites annonces en ligne
- **Site web :** [loozap.com](http://loozap.com/)
- **Date de l'incident :** 28 janvier 2026 (identifiée en mars 2026)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Description victime :** Loozap est une plateforme panafricaine de petites annonces en ligne (anciennement Listings360), exploitant des sections nationales dans des dizaines de marchés africains à partir d'une application unique partagée, plutôt qu'un service propre à un seul pays. Un acteur malveillant a publié une base de données contenant environ 34 000 comptes utilisateurs.
- **Analyse :** AFRINTEL a examiné un échantillon structuré de la table utilisateurs publiée. Les enregistrements ne sont pas rattachés à un seul pays : les entrées examinées listent des utilisateurs situés notamment en Égypte, au Kenya, au Ghana, en Éthiopie, au Nigeria et au Mozambique, cohérent avec le rôle de Loozap en tant que base de données partagée unique alimentant ses sous-domaines nationaux plutôt qu'un déploiement pays par pays. Les champs examinés incluent le nom complet, l'adresse email, un hash de mot de passe au format SHA1, l'adresse IP d'inscription, des coordonnées de géolocalisation précises, la date de naissance, le genre et des métadonnées d'activité sociale (abonnés, mentions « j'aime », appartenance à des groupes). La cohérence du schéma de base de données entre les enregistrements de différents pays, ainsi que le volume et la structure interne de l'échantillon, soutiennent une évaluation à confiance élevée d'une compromission réelle et complète de la base utilisateurs partagée de la plateforme, plutôt qu'une revendication limitée à une seule instance nationale. Compte tenu de la portée multi-pays, de la présence de données de géolocalisation précises et d'un hachage de mot de passe faible (SHA1), cet incident crée un risque de prise de contrôle de comptes à grande échelle, de credential stuffing sur des mots de passe réutilisés, et de phishing ciblé affectant simultanément des utilisateurs de plusieurs pays africains. AFRINTEL ne reproduit aucun nom, adresse email, hash de mot de passe, adresse IP ni coordonnée de géolocalisation issus de l'échantillon examiné.

### 02 Mars 2026
#### 🇪🇬 Égypte - Autorité de Régulation de la Gestion des Déchets (WMRA)
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Gouvernement / Environnement
- **Site web :** [garb.gov.eg](https://garb.gov.eg)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Organisme dépendant du Ministère de l'Environnement chargé de réguler la gestion des déchets. Base de données contenant des données administratives, registres internes, informations sur partenaires et personnel.

#### 🇪🇬 Égypte - Orascom Construction
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Ingénierie et construction
- **Site web :** [orascom.com](https://orascom.com/)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Leader de l'ingénierie et construction au Moyen-Orient, Afrique du Nord et États-Unis. Données compromises : staff_id, noms complets, emails professionnels, départements, postes.

#### 🇪🇬 Égypte - Ministère de la Santé et de la Population (E-Portal)
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Gouvernement / Santé
- **Site web :** [mohp.gov.eg](https://www.mohp.gov.eg)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Base de données de 3,8 millions d'enregistrements (2019-2026) incluant noms complets, National ID, téléphones, adresses, diagnostics médicaux précis, types de chirurgies, établissements de traitement.

### 03 Mars 2026
#### 🇿🇦 Afrique du Sud - Walter Sisulu University (WSU)
- **Acteur / Groupe :** TelephoneHooliganism
- **Secteur :** Éducation / Université
- **Site web :** [wsu.ac.za](https://www.wsu.ac.za)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Université publique du Cap Oriental. Données structurées en trois sections (Contacts, Inscriptions, Tickets) : dates de naissance, emails, adresses, GPA, bourses, historiques de support.

- **Analyse :**
  AFRINTEL a consulté un échantillon de données correspondant à la section Tickets de cette revendication : un export de tickets d'assistance informatique interne (helpdesk), structuré avec identifiant de contact, e-mail, téléphone, nom et prénom, statut et catégorie du ticket, priorité, canal d'origine, agent assigné, dates d'ouverture et de clôture, résumé de résolution, notes internes de l'agent, indicateur de dépassement de SLA et région (parmi lesquelles Western Cape, Gauteng, KwaZulu-Natal, Cap-Oriental et Cap-Nord). Les catégories de tickets observées couvrent notamment des problèmes d'accès au portail étudiant, des accès e-mail, des installations logicielles et un cas classé Security lié à une activité suspecte sur un compte. Cet échantillon est cohérent avec un système de gestion des tickets du service d'assistance de l'université et confirme, en complément des sections Contacts et Inscriptions déjà mentionnées dans la description, une exposition de coordonnées de contact et de contenu opérationnel interne du support. AFRINTEL n'a pas eu accès aux sections Contacts et Inscriptions elles-mêmes lors de cette analyse et ne peut pas confirmer le volume total de tickets concernés ni le vecteur d'accès initial.

#### 🇪🇬 Égypte - Ministère de l'Éducation et de l'Enseignement Technique
- **Acteur / Groupe :** CrowStealer
- **Secteur :** Gouvernement / Éducation
- **Site web :** [moe.gov.eg](https://moe.gov.eg)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Données sur étudiants et personnel : identifiants nationaux, noms complets, adresses, dossiers académiques.

#### 🇲🇦 Maroc - Office National des Œuvres Universitaires Sociales et Culturelles (ONOUSC)
- **Acteur / Groupe :** xNov
- **Secteur :** Éducation / Gouvernement
- **Site web :** [amo.onousc.ma](https://amo.onousc.ma)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Organisme chargé de la gestion des œuvres sociales pour les étudiants au Maroc (bourses, cités universitaires, couverture santé). Exposition des dossiers de 3 631 étudiants liés à l’Assurance Maladie Obligatoire (AMO) : noms, prénoms, CINE, numéros d’immatriculation universitaire, CNE, dates de naissance, statuts d’inscription.

### 04 Mars 2026
#### 🇲🇦 Maroc - Outsourcia
- **Groupe ransomware :** Qilin
- **Secteur :** Business Process Outsourcing (BPO)
- **Site web :** [outsourcia.com](https://www.outsourcia.com)
- **Statut :** Claim - Unverified
- **Description victime :** Opérateur majeur de la relation client basé à Casablanca, gérant des processus métiers pour des comptes internationaux.

### 05 Mars 2026
#### 🇪🇬 Égypte - Rowad Modern Engineering
- **Groupe ransomware :** Crypto24
- **Secteur :** Ingénierie et construction
- **Site web :** [rowad-rme.com](http://www.rowad-rme.com)
- **Statut :** Claim - Unverified
- **Description victime :** Société de construction égyptienne spécialisée dans les projets d'infrastructure et les bâtiments commerciaux.

### 06 Mars 2026
#### 🇪🇬 Égypte - INTERACT TECHNOLOGY SOLUTIONS
- **Groupe ransomware :** PEAR
- **Secteur :** IT Consulting
- **Site web :** [interactts.com](http://interactts.com)
- **Statut :** Claim - Unverified
- **Description victime :** Entreprise fournissant des solutions technologiques et d'infrastructure critique en Égypte.

#### 🇲🇬 Madagascar - Orange Madagascar
- **Groupe ransomware :** Qilin
- **Secteur :** Télécommunications
- **Site web :** [orange.mg](https://www.orange.mg/)
- **Statut :** Claim - Unverified
- **Description victime :** Leader des télécommunications à Madagascar, opérant sur l'internet, le mobile et le mobile banking.

### 09 Mars 2026
#### 🇹🇳 Tunisie - K.PROPHA (Karray Produits Pharmaceutiques)
- **Groupe ransomware :** The Gentlemen
- **Secteur :** Santé / Pharmaceutique
- **Site web :** [kpropha.com](http://kpropha.com)
- **Statut :** Claim - Unverified
- **Description victime :** Entreprise tunisienne spécialisée dans la distribution de produits pharmaceutiques et parapharmaceutiques.

### 12 Mars 2026
#### 🇲🇦 Maroc - HACA (Haute Autorité de la Communication Audiovisuelle)
- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Gouvernement / Médias
- **Site web :** [haca.ma](http://haca.ma)
- **Statut :** Claim - Unverified
- **Description victime :** Instance constitutionnelle chargée de la régulation de la communication audiovisuelle au Maroc.

### 13 Mars 2026
#### 🇿🇦 Afrique du Sud - Lion of Africa Insurance
- **Groupe ransomware :** Lynx
- **Secteur :** Services d'assurance
- **Site web :** [lionsureins.com](http://lionsureins.com/)
- **Statut :** Claim - Unverified
- **Description victime :** Compagnie d'assurance sud-africaine traitant des volumes importants de données personnelles et financières.

#### 🇿🇦 Afrique du Sud - Gouvernement Provincial de Gauteng
- **Acteur / Groupe :** XP95
- **Secteur :** Gouvernement / Administration publique
- **Site web :** [gauteng.gov.za](https://www.gauteng.gov.za)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Gestion de la province la plus peuplée d'Afrique du Sud (Johannesburg, Pretoria). 3,8 To de données (3,6 millions de fichiers) exfiltrés : santé, éducation, logement, développement économique.

### 14 Mars 2026
#### 🇪🇬 Égypte - Grid Fine Finishes
- **Groupe ransomware :** Payload
- **Secteur :** Aménagement / Construction
- **Site web :** [gridff.com](http://gridff.com)
- **Statut :** Claim - Unverified
- **Description victime :** Société égyptienne spécialisée dans l'aménagement intérieur haut de gamme pour les secteurs commerciaux et résidentiels.

### 17 Mars 2026
#### 🇿🇦 Afrique du Sud - University of South Africa (UNISA)
- **Acteur / Groupe :** Blackwinter99
- **Secteur :** Éducation / Enseignement Supérieur
- **Site web :** [unisa.ac.za](https://www.unisa.ac.za)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** L'UNISA est la plus grande institution d'enseignement à distance en Afrique. Blackwinter99 a divulgué publiquement sur un forum clandestin les identifiants de connexion de la page d'administration du site, offrant un accès direct aux privilèges élevés de la plateforme, permettant l'exfiltration massive de données étudiantes, la modification des dossiers académiques ou une prise de contrôle totale de l'infrastructure web.

### 19 Mars 2026
#### 🇳🇦 Namibie - Namibia Airports Company
- **Groupe ransomware :** INC Ransom
- **Secteur :** Transport aérien
- **Site web :** [airports.com.na](http://airports.com.na)
- **Statut :** Claim - Unverified
- **Description victime :** Gestionnaire officiel des aéroports nationaux en Namibie.

### 20 Mars 2026
#### 🇿🇦 Afrique du Sud - The Unlimited
- **Groupe ransomware :** DragonForce
- **Secteur :** Services d'assurance
- **Site web :** [theunlimited.co.za](http://theunlimited.co.za)
- **Statut :** Claim - Unverified
- **Description victime :** Fournisseur de produits d'assurance incluant la santé, l'auto, le juridique et la vie.

#### 🇲🇦 Maroc - Ministère de la Justice
- **Acteur / Groupe :** anisanas2
- **Secteur :** Gouvernement / Justice
- **Site web :** [justice.gov.ma](https://www.justice.gov.ma)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Exfiltration de 300 Go incluant plus de 150 000 dossiers de procédures judiciaires (2019-2026). Litiges opposant grandes entreprises marocaines à des particuliers (12 Mds MAD). Documents : pièces d'identité, relevés bancaires, actes judiciaires, factures.

### 21 Mars 2026
#### 🇿🇦 Afrique du Sud - Elundini Local Municipality
- **Groupe ransomware :** The Gentlemen
- **Secteur :** Administration locale
- **Site web :** [elundini.gov.za](http://elundini.gov.za)
- **Statut :** Claim - Unverified
- **Description victime :** Administration municipale dédiée au développement durable dans la province du Cap Oriental.

### 22 Mars 2026
#### 🇿🇦 Afrique du Sud - Semenya Furumele Consulting Engineers
- **Groupe ransomware :** NightSpire
- **Secteur :** Ingénierie conseil
- **Site web :** [sfce.co.za](http://www.sfce.co.za)
- **Statut :** Claim - Unverified
- **Description victime :** Cabinet de conseil en ingénierie basé en Afrique du Sud.

### 24 Mars 2026
#### 🇸🇳 Sénégal - United Bank for Africa (UBA Sénégal)
- **Acteur / Groupe :** Non attribué
- **Secteur :** Finance / Banque
- **Site web :** [ubasenegal.com](https://www.ubasenegal.com)
- **Date de l’attaque :** 30-31 janvier 2026 (révélée le 24 mars 2026)
- **Statut :** Under Investigation
- **Référence :** https://cert.gov.ng/advisories/alert-on-cyber-enabled-atm-cash-out-attacks-targeting-african-financial-institutions
- **Note de taxonomie :** Cet incident ne correspond à aucun des quatre types d'incident AFRINTEL (Ransomware, Fuite de données, Vente d'accès, Défacement). Il s'agit d'une fraude opérationnelle confirmée via un accès privilégié compromis à l'infrastructure d'autorisation de cartes, pas d'une revendication sur site de fuite, d'une publication de données ou d'une vente d'accès annoncée. Aucun type d'incident n'est attribué ; cette fiche est exclue des compteurs structurés Ransomware/Fuite de données/Vente d'accès/Défacement.
- **Description victime :** Selon le ngCERT, une opération de cash-out cyber visant UBA Sénégal a impliqué 3 421 transactions GAB. Les pertes avaient été précédemment rapportées à 1,143 milliard de FCFA ; l’avis du ngCERT les présente comme supérieures à 2 millions USD. Le ngCERT estime qu’un accès privilégié à l’infrastructure d’autorisation des cartes aurait permis la modification de contrôles transactionnels et la coordination des retraits. Le vecteur d’accès initial, la séquence technique exacte et une éventuelle implication interne restent inconnus. Le phishing, les faiblesses de la chaîne d’approvisionnement, l’accès interne et les malwares ATM sont présentés par le ngCERT comme des scénarios possibles pour cette classe d’attaque, et non comme des faits confirmés pour UBA Sénégal.

### 26 Mars 2026
#### 🇿🇦 Afrique du Sud - ETFSA
- **Groupe ransomware :** INC Ransom
- **Secteur :** Wealth Management
- **Site web :** [etfsa.co.za](http://ETFSA.co.za)
- **Statut :** Claim - Data Sample Published
- **Description victime :** Plateforme sud-africaine de services financiers spécialisée dans les fonds négociés en bourse (ETF).

- **Analyse :**
  AFRINTEL a consulté la publication d'extorsion relative à cette victime, qui mentionne un chiffre d'affaires revendiqué d'environ 8 millions de dollars et nomme une personne identifiée comme directeur général de la plateforme. La publication indique que des données clients confidentielles et personnelles seraient publiées, et affiche des aperçus miniatures de nombreux documents. AFRINTEL a consulté un échantillon accessible : un extrait d'acte de décès délivré par le Department of Home Affairs sud-africain, contenant un numéro d'identité, un nom complet, une date de naissance et une cause de décès. Cela indique que les éléments exposés incluent des documents d'identité clients de type KYC et liés à des successions, et pas uniquement des données de compte ou de transaction, ce qui est cohérent avec une clientèle de gestion de patrimoine et de conseil financier. AFRINTEL n'a pas eu accès aux autres fichiers et ne peut pas confirmer le nombre total de clients concernés ni le vecteur d'accès initial.

#### 🇲🇦 Maroc - Maroc Telecom
- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Télécommunications
- **Site web :** [iam.ma](http://iam.ma)
- **Statut :** Claim - Data Sample Published
- **Description victime :** Opérateur historique de télécommunications au Maroc, fournissant services mobiles, internet et fixes.

- **Analyse :**
  AFRINTEL a consulté des captures d'écran échantillons publiées dans le cadre de cette revendication. Le contenu montre des écrans internes de relation client et de support technique (interfaces GRC/suivi de réclamations) faisant référence à des identifiants clients, des coordonnées, des adresses d'installation et des tickets d'incident liés à des problèmes de service fixe et fibre optique. Ces éléments sont cohérents avec un accès aux systèmes de support client et de gestion des réclamations de Maroc Telecom, plutôt qu'avec un export massif de base d'abonnés. AFRINTEL n'a pas eu accès aux systèmes sous-jacents et ne peut pas confirmer le volume d'enregistrements concernés ni le vecteur d'accès initial.

#### 🇲🇦 Maroc - 2M TV
- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Médias et audiovisuel
- **Site web :** [2m.ma](http://2m.ma)
- **Statut :** Claim - Data Sample Published
- **Description victime :** Chaîne de télévision nationale marocaine.

- **Analyse :**
  AFRINTEL a consulté des documents échantillons publiés dans le cadre de cette revendication, correspondant à du matériel RH interne : un curriculum vitae d'un salarié du service audiovisuel, une liste interne d'employés titulaires du permis de conduire, ainsi qu'un modèle d'attestation de travail à en-tête 2M. Cela indique une exposition de dossiers du personnel plutôt que des systèmes de diffusion ou des données clients. AFRINTEL a également consulté un ensemble de données distinct : une exportation complète de boîte de messagerie au format .eml (1 777 messages), dont les métadonnées associées (identifiants de message au format Microsoft Exchange/Office 365 et horodatage de dernière réception daté de novembre 2025) indiquent une compromission d'un compte de messagerie professionnel individuel, vraisemblablement rattaché au service Rédaction/News de 2M, plutôt qu'un simple lot de documents statiques. La correspondance couvre 123 adresses internes 2m.ma distinctes et porte notamment sur la planification éditoriale d'une émission interne, des démarches administratives (dont une demande de carte de presse) et des échanges RH ; environ 348 messages comportent des pièces jointes (images, PDF, documents Word et tableurs Excel). Plusieurs objets de messages ne correspondent à aucune activité éditoriale identifiable et sont cohérents avec du courrier indésirable ou des tentatives d'ingénierie sociale reçues sur cette boîte. AFRINTEL ne nomme pas le titulaire du compte et ne reproduit ni le contenu des messages ni l'identité des correspondants tiers. AFRINTEL n'a pas eu accès à d'autres fichiers et ne peut pas confirmer le nombre total de dossiers d'employés concernés, l'état actuel d'accès à cette boîte de messagerie, ni le vecteur d'accès initial.

#### 🇲🇦 Maroc - Institut Royal des Études Stratégiques (IRES)
- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Recherche / Think tank
- **Site web :** [ires.ma](http://ires.ma)
- **Statut :** Claim - Data Sample Published
- **Description victime :** Centre d'analyse stratégique rattaché au Cabinet Royal marocain.

- **Analyse :**
  AFRINTEL a consulté des documents échantillons publiés dans le cadre de cette revendication, correspondant à des curriculums vitae de chercheurs et de consultants associés à l'institut, couvrant des profils académiques (recherches doctorales et de master en droit public et relations internationales), des références d'expérience professionnelle et, dans un cas, des coordonnées incluant une adresse e-mail et un numéro de téléphone. Cela indique une exposition de dossiers du personnel et des chercheurs. AFRINTEL n'a pas eu accès à d'autres fichiers et ne peut pas confirmer le nombre total d'enregistrements concernés ni le vecteur d'accès initial.

### 29 Mars 2026
#### 🇿🇦 Afrique du Sud - Statistics South Africa (Stats SA)
- **Groupe ransomware :** XP95
- **Secteur :** Gouvernement / Statistiques Nationales
- **Site web :** [statssa.gov.za](https://www.statssa.gov.za)
- **Statut :** Claim - Data Sample Published
- **Description victime :** Stats SA est l'agence nationale de statistique de l'Afrique du Sud. XP95 a exfiltré 154 Go de données (453 362 fichiers). La brèche compromet potentiellement des données socio-économiques sensibles, des recensements, des informations sur l'emploi, l'inflation et des registres administratifs nationaux. Une rançon de 100 000 $ a été exigée avant une mise en vente publique prévue pour le 20 avril 2026.

#### 🇿🇦 Afrique du Sud - Gauteng City Region Academy (GCRA)
- **Groupe ransomware :** XP95
- **Secteur :** Éducation / Formation (Gouvernement provincial)
- **Site web :** [gcra.gauteng.gov.za](https://gcra.gauteng.gov.za)
- **Statut :** Claim - Data Sample Published
- **Description victime :** La GCRA est l'agence responsable du développement des compétences pour la province de Gauteng. L'exfiltration de 147 Go de données compromet potentiellement les dossiers des étudiants (bourses, inscriptions, PII), les données des programmes de formation et les documents administratifs de l'académie. XP95 a fixé une date limite pour le paiement de la rançon avant la mise en vente publique des fichiers.

### 30 Mars 2026
#### 🇹🇿 Tanzanie - SBC Tanzania Limited
- **Groupe ransomware :** Morpheus
- **Secteur :** Agroalimentaire
- **Site web :** [sbctanzania.co.tz](http://sbctanzania.co.tz)
- **Statut :** Claim - Unverified
- **Description victime :** Fabricant et distributeur de boissons, embouteilleur officiel de PepsiCo en Tanzanie.

#### 🇿🇦 Afrique du Sud - Nashua
- **Groupe ransomware :** Coinbase Cartel
- **Secteur :** IT & Managed Services
- **Site web :** [nashua.co.za](http://nashua.co.za)
- **Statut :** Claim - Unverified
- **Description victime :** Fournisseur majeur de solutions technologiques intégrées et de services gérés pour entreprises.

#### 🇳🇬 Nigeria - Université Ahmadu Bello (ABU Zaria)
- **Acteur / Groupe :** AshleyWood2022
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [abu.edu.ng](https://www.abu.edu.ng)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** L'une des plus grandes universités de recherche du Nigeria. Base de données (`tbl_flattened.csv` & `abu.sql`) avec plus de 11 000 enregistrements : personnel académique et non-académique (noms, départements, rangs, qualifications, sexe, date de naissance, districts d'origine).

- **Note de fiabilité :**
  AFRINTEL a examiné la publication de forum d'AshleyWood2022 datée du 30 mars 2026, accompagnée d'un lien de téléchargement (gofile.io) et d'un échantillon de données visible. L'échantillon examiné couvre le personnel rattaché au bureau du Vice-Chancelier et à ses sous-unités (ABU/FM Radio, ABUCONS, Central Procurement Unit, Academic Planning, University Advancement, Equipment Maintenance and Development Centre, Internal Audit, ITF/SIWES Coordination Centre, Procurement et Security Division), avec 237 lignes pour cette seule section, cohérent en échelle avec la revendication globale de plus de 11 000 enregistrements.

- **Analyse :**
  L'échantillon suit un schéma cohérent : zone de gouvernement local et circonscription sénatoriale d'origine, État, zone géopolitique, date de naissance, sexe, faculté, département, catégorie de personnel (académique ou non-académique), rang et plus haute qualification. Dans les lignes examinées, le champ date de naissance est uniformément masqué (`0000-00-00`) et aucun nom, numéro de téléphone ou identifiant national n'est visible ; la publication de l'acteur affirme que les noms et d'autres champs personnels figurent dans le jeu de données complet, qu'AFRINTEL n'a pas téléchargé ni vérifié de manière indépendante. La cohérence structurelle sur 237 lignes et la présence d'un lien de téléchargement fonctionnel appuient une évaluation plus solide qu'une simple revendication, sans que l'exhaustivité, l'authenticité ou le contenu complet de l'archive soient confirmés. Si la revendication complète s'avère exacte, l'exposition de données démographiques et organisationnelles du personnel pourrait faciliter l'ingénierie sociale ciblée, le profilage par région, sexe ou département, et l'usurpation d'identité de membres du personnel universitaire. AFRINTEL ne reproduit aucun enregistrement, valeur de champ ni lien de téléchargement issu du matériel examiné.

### 31 Mars 2026
#### 🇳🇬 Nigeria - Remita (SystemSpecs)
- **Acteur / Groupe :** Bytetobreach
- **Secteur :** Fintech / Services de paiement
- **Site web :** [remita.net](https://www.remita.net)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Plateforme de paiement majeure au Nigeria utilisée par particuliers, entreprises et gouvernement. Brèche de 3 To : 800 Go de documents KYC (pièces d'identité, passeports, relevés bancaires, factures), bases MySQL/Postgres, codes sources, registres Docker, clés HSM gouvernementales, plus de 35 000 hashes de mots de passe.

- **Analyse :**
  AFRINTEL a consulté un ensemble d'éléments techniques associés à cette revendication. Un fichier d'informations de connexion recense environ 35 800 paires adresse e-mail / hachage de mot de passe (format bcrypt), couvrant à la fois des comptes internes (agents, opérateurs) et vraisemblablement des comptes clients de la plateforme ; AFRINTEL n'a extrait ni tenté de casser aucun hachage. Des captures d'écran montrent une instance restaurée des bases de données de la plateforme dans un outil d'administration SQL, incluant une table de propriétaires d'entreprise (numéro BVN, type et numéro de pièce d'identité, document d'identité encodé en base64), une table de transactions interbancaires (montants, codes banque bénéficiaire, canal, référence de paiement), une table de comptes administrateurs internes (agents SystemSpecs avec rôle et statut) et une table d'informations personnelles clients (date de naissance, e-mail, téléphone, statut KYC, mot de passe haché). D'autres captures montrent une archive de code source couvrant plusieurs microservices de la plateforme, incluant un module de communication chiffrée par SFTP avec la Banque Centrale du Nigeria (CBN) pour l'échange d'instructions de paiement, une intégration avec le système panafricain de paiement et de règlement PAPSS, un système de portefeuille virtuel développé en partenariat avec OPay, ainsi qu'une logique de vérification OTP. Une capture supplémentaire montre un répertoire de fichiers de clés nommés d'après plus de vingt banques nigérianes (dont GTBank, Zenith, UBA, First Bank, Access, FCMB, Fidelity, Sterling, Stanbic, Ecobank, UBN, Wema, Unity, Providus, Heritage et Citibank), cohérent avec des clés maîtresses de chiffrement liées à l'intégration interbancaire ; AFRINTEL n'a pas vérifié le contenu ni la validité de ces fichiers. Des résultats d'outils de détection de secrets exécutés sur les dépôts de code source montrent la détection de clés d'API, de jetons d'accès cloud et d'identifiants de base de données codés en dur dans plusieurs fichiers de configuration, associés à des adresses e-mail d'employés de SystemSpecs. AFRINTEL a par ailleurs examiné la structure d'une archive de sauvegarde Git (environ 34 800 fichiers) couvrant une quarantaine de dépôts internes distincts, avec historique de commits complet, correspondant à l'ensemble de l'organisation GitLab interne « remitacenta » : composants de paiement interbancaire et panafricain (dont un connecteur PAPSS et un générateur de messages de paiement au format ISO 20022, standard utilisé pour la messagerie interbancaire), moteur de détection de fraude, kit de tokenisation de cartes, infrastructure Kubernetes sous forme de code (trois jeux de manifestes distincts) et un module d'analyse décisionnelle (Superset), ce dernier représentant à lui seul plus du quart des fichiers de l'archive. L'archive contient environ 200 fichiers de configuration de production, 354 fichiers Helm « values.yaml » et plus de 400 noms de fichiers faisant explicitement référence à des secrets, ce qui est cohérent avec une exposition potentielle de nombreux identifiants supplémentaires au-delà de ceux déjà identifiés par les outils de détection ; AFRINTEL n'a pas ouvert individuellement ces fichiers et ne reproduit aucun secret supplémentaire. Un fichier supplémentaire, désigné comme téléchargement non finalisé, correspond à une image de sauvegarde au format Veeam Backup & Replication (signature XBSTCK01, version d'outil 12.1.2) référençant des fichiers journaux InnoDB, cohérent avec une sauvegarde de niveau système incluant une base de données MySQL/MariaDB ; ce fichier étant incomplet, AFRINTEL n'a pas pu le monter ni en examiner le contenu. Une dernière capture montre un accès, via des identifiants cloud extraits du code source, à un compartiment de stockage cloud dédié aux documents KYC contenant environ 657 000 fichiers pour un volume propre d'environ 588 Go, ainsi qu'à plusieurs autres compartiments liés à l'infrastructure GitLab interne de l'entreprise (sauvegardes, artefacts, registre de conteneurs). AFRINTEL ne reproduit aucun identifiant, clé, jeton, hachage, nom de compte ni document d'identité individuel issu de ces éléments. L'ensemble de ces observations est cohérent avec une compromission approfondie de l'infrastructure de développement et de production de Remita, pouvant s'étendre aux systèmes d'intégration bancaire et panafricaine, mais AFRINTEL n'a pas vérifié l'authenticité ni l'actualité de chaque élément pris individuellement et ne peut pas confirmer l'étendue exacte de l'accès obtenu ni le vecteur d'accès initial.

#### 🇲🇦 Maroc - Smarteez (Prestataire L’Oréal Maroc - Supply Chain)
- **Acteur / Groupe :** xNov
- **Secteur :** Marketing Digital / Cosmétique (Supply Chain L'Oréal)
- **Site web :** [smarteez.eu](https://smarteez.eu)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Smarteez est un prestataire digital marocain utilisé par L’Oréal Maroc pour la gestion de ses opérations terrain. Exposition de données critiques : informations sur 296 pharmacies (GPS, segmentation), 361 000 enregistrements de ventes/KPI, 22 secrets d’applications OAuth2 en clair, logs administratifs complets. Une APK de production a également été divulguée.

#### 🇪🇬 Égypte - Semsar Masr (semsarmasr.com)
- **Acteur / Groupe :** Al-Sheikh
- **Secteur :** Immobilier / Petites annonces en ligne
- **Site web :** [semsarmasr.com](https://www.semsarmasr.com)
- **Date de la fuite :** Janvier 2026 (identifiée en mars 2026)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Semsar Masr est une plateforme égyptienne de petites annonces immobilières, active depuis 2007, permettant la publication et la consultation d'annonces d'appartements, terrains et autres biens à la vente ou à la location en Égypte.
- **Analyse :** AFRINTEL a examiné un post publié le 28 janvier 2026 par l'acteur Al-Sheikh concernant la table `tb_members_Profiles` de semsarmasr.com, affirmant qu'elle contient 185 024 lignes et que les mots de passe des utilisateurs y figurent en clair. L'échantillon affiché dans le post comprend un schéma de champs incluant identifiant utilisateur, statut du compte, adresse email, numéro de téléphone, mot de passe, rôle utilisateur, nom de contact, nom d'entreprise, adresse, réseaux sociaux (WhatsApp, Telegram, LinkedIn, Twitter, Facebook), date de naissance, profession, genre, statut matrimonial, indicateurs de vérification email/téléphone et dates de création/mise à jour du compte. Dix enregistrements complets sont directement visibles dans l'échantillon, avec des adresses email, numéros de téléphone égyptiens et internationaux, noms complets et mots de passe en texte clair associés à des comptes créés le 28 janvier 2026. La cohérence du schéma avec une plateforme de petites annonces immobilières et la présence de mots de passe non hachés dans l'échantillon appuient un niveau de confiance élevé quant à l'authenticité de cette fuite, bien que le volume total de 185 024 lignes revendiqué n'ait pas pu être vérifié indépendamment au-delà de l'échantillon observé. L'exposition de mots de passe en clair, combinée aux coordonnées et à l'identité des utilisateurs, présente un risque élevé de prise de contrôle de comptes, de réutilisation de mots de passe sur d'autres services et de phishing ciblé. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone ni mot de passe issus de l'échantillon examiné.

#### 🇬🇳 Guinée - Ministère de la Santé (sante.gov.gn)
- **Acteur / Groupe :** Keymous
- **Secteur :** Gouvernement / Santé publique
- **Site web :** [sante.gov.gn](https://sante.gov.gn/)
- **Date de l'incident :** Juillet 2025 (activité observée, identifiée en mars 2026)
- **Statut :** Under Investigation
- **Type d'incident :** Fuite de données
- **Description victime :** Le site officiel du Ministère de la Santé de Guinée est directement lié aux systèmes internes compromis, notamment les dashboards DHIS2 exposés par Keymous. La corrélation entre l’accès aux outils de surveillance sanitaire, les données gouvernementales divulguées (emails, personnels) et les infrastructures ministérielles suggère une compromission plus large de l’écosystème numérique du ministère. Cette exposition pourrait permettre des attaques ciblées, de la manipulation de données sanitaires et des opérations d’influence.
