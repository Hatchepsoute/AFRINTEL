# Victimes africaines - Mai 2026

## Résumé du mois

Mai 2026 compte **57 incidents uniques** : **16 ransomwares** et **41 fuites de données ou ventes d’accès**. Les fiches concernent **18 pays africains** : 12 pays directement touchés et 6 pays supplémentaires uniquement exposés par l’intermédiaire de trois incidents multi-pays.

### Incidents marquants

- **Égypte :** le secteur éducatif a été concerné par plusieurs revendications importantes, dont 26,8 millions de dossiers d’étudiants attribués au ministère de l’Éducation.
- **Afrique du Sud :** plusieurs institutions publiques ont été ciblées pendant la campagne coordonnée OpSouthAfrica.
- **Tanzanie :** plus de 10 000 comptes de messagerie de la police avec des mots de passe en clair ont été proposés à la vente.
- **Sénégal :** AuditTeam revendique une exfiltration au Trésor public, comprenant environ 1,66 million d’enregistrements issus de bases de données.

> Les fiches ci-dessous documentent des revendications ou publications observées. AFRINTEL ne confirme pas une compromission sans élément indépendant.

### 02 Mai 2026
#### 🇪🇬 Égypte - Ministère du Travail (Ministry of Labour / Manpower) [Fuite de données]
- **Acteur / Groupe:** CrowStealer
- **Secteur :** Gouvernement
- **Site web :** [manpower.gov.eg](https://www.manpower.gov.eg/)
- **Statut :** Fuite de données / Revendication
- **Description :** Le ministère égyptien du Travail (anciennement Ministry of Manpower) est l’organisme gouvernemental chargé de la gestion de l’emploi, des travailleurs, des permis de travail et des affaires sociales liées au marché du travail en Égypte. Une publication revendique la fuite de 34 528 enregistrements liés au ministère égyptien du Travail. Les échantillons contiennent notamment des noms complets, numéros d’identité nationale, dates de naissance, adresses, numéros de téléphone, emails et informations de passeport de travailleurs égyptiens, y compris des expatriés.
- **Analyse des échantillons :** Les échantillons analysés contiennent des noms complets, numéros d’identité nationale, dates de naissance, adresses, numéros de téléphone, adresses email, informations professionnelles, numéros de passeport, dates d’expiration de passeport et données administratives associées aux travailleurs.
---
### 3 Mai 2026
#### 🇹🇿 Tanzanie - Base de données personnelles (120 000+ enregistrements)

- **Acteur / Groupe:** XOverStm (via le forum [Citizen])
- **Secteur :** Données personnelles / Base de données
- **Statut :** Offre de vente active
- **Site web :** Non spécifié

- **Description :**  
  Un cybercriminel propose à la vente une base de données contenant plus de **120 000 enregistrements** de citoyens tanzaniens. Les données incluent :
  - noms complets (*Name*)
  - adresses physiques (*Address*)
  - numéros de téléphone (*Mobile*)
  - villes de résidence (*City*)

  Toutes les entrées sont présentées comme **actives et validées** (*Valid/Active*). Le vendeur affirme que les données sont fraîches et opérationnelles. Le prix demandé est de **350 $**, avec possibilité de recourir à un séquestre (*escrow*).

- **Analyse :**  
  Cette fuite expose des informations personnelles identifiables (PII) extrêmement précises, directement exploitables pour :
  - des **campagnes de phishing et d'hameçonnage** ciblant les citoyens tanzaniens ;
  - des **escroqueries téléphoniques** (*vishing* ou *smishing*) utilisant les numéros de téléphone pour usurper l'identité des contacts ;
  - du **harcèlement** ou de l'**intimidation** à domicile, grâce aux adresses physiques précises ;
  - des **tentatives de fraude bancaire** ou d'**usurpation d'identité** pour souscrire à des services financiers.

  Le volume important (120 000+ enregistrements) couvre probablement plusieurs régions du pays, notamment Dar es Salaam, Zanzibar et Kibaha (visibles dans l'échantillon). La mention "actif" suggère que les données ont été récemment vérifiées, ce qui en accroît la valeur pour les cybercriminels et le danger pour les citoyens tanzaniens. L'acteur XOverStm est également connu pour d'autres fuites (notamment le CGCSA en Afrique du Sud), ce qui renforce la crédibilité de la menace.
---
### 04 Mai 2026
#### 🇩🇿 Algérie - Ministère de l’Industrie Pharmaceutique [Fuite de données]
- **Acteur / Groupe :** kamalsheikhxx
- **Secteur :** Gouvernement / Santé / Industrie pharmaceutique
- **Statut :** Publication de dump complet revendiquée
- **Site web :** [miph.gov.dz/](https://miph.gov.dz/)
- **Description :** Une publication sur un forum cybercriminel revendique la fuite d’environ 34,3 Go de données attribuées au Ministère algérien de l’Industrie Pharmaceutique, comprenant plus de 52 000 fichiers et 17 800 dossiers couvrant la période 2019–2025.
- **Données observées :**
  - rapports d’importation de médicaments
  - factures et déclarations douanières
  - registres commerciaux pharmaceutiques
  - données personnelles de responsables
  - autorisations officielles
  - inventaires pharmaceutiques
  - listes de substances psychotropes
  - documents PDF, Excel, Word et ZIP
  
  
#### 🇪🇬 Égypte - Bases de données éducatives & RH

- **Acteur / Groupe:** bigF  
- **Secteur :** Éducation / Ressources humaines  
- **Statut :** Fuite de données / Revendication de vente  
- **Sites web observés :** [mans.edu.eg](https://www.mans.edu.eg) ; [gu.edu.eg](https://gu.edu.eg)
- **Description :**  
  Un cybercriminel revendique la possession d’environ **37 Go** de bases de données liées à des établissements éducatifs égyptiens et à des systèmes RH.
- **Analyse :**  
  Les échantillons publiés mentionnent plus de **1,5 million de dossiers étudiants** et près de **60 millions d’enregistrements** contenant des informations personnelles, académiques et administratives sensibles :
  ▫️ noms complets  
  ▫️ numéros d’identité nationale égyptienne  
  ▫️ adresses et coordonnées  
  ▫️ données académiques  
  ▫️ scans de pièces d’identité et passeports  
  ▫️ données RH et salaires  
  
#### 🇿🇦 Afrique du Sud - Standard Bank Group
- **Groupe ransomware :** PrinzEugen
- **Secteur :** Banque/finance
- **Site web :** [www.standardbank.com](https://www.standardbank.com)
- **Statut :** Revendication ransomware
- **Description :** Standard Bank Group est l'un des plus grands groupes bancaires d'Afrique. Le 4 mai 2026, l'acteur **PrinzEugen** a revendiqué la possession de données associées à cette institution financière.

#### 🇪🇬 Égypte - Luna Group
- **Groupe ransomware :** Lamashtu
- **Secteur :** Agroalimentaire, emballage, produits d'entretien et chimie industrielle
- **Site web :** [lunagroupeg.com](https://lunagroupeg.com)
- **Statut :** Revendication ransomware
- **Description :** Luna Group est un conglomérat opérant dans divers secteurs industriels et commerciaux en Égypte. Le groupe **Lamashtu** a revendiqué une compromission de l'organisation le 4 mai 2026.

---
### 05 Mai 2026
#### 🇳🇬 Nigeria - ActionAid / TACOSA
- **Groupe ransomware :** MedusaLocker
- **Secteur :** ONG / Humanitaire
- **Site web :** [www.actionaid.org](https://www.actionaid.org)
- **Statut :** Revendication ransomware
- **Description :**  ActionAid est une organisation internationale de lutte contre la pauvreté et les injustices sociales, collaborant avec des entités locales telles que TACOSA (The ActionAid Community and Social Action). Le groupe de ransomware MedusaLocker a revendiqué une compromission des systèmes informatiques affectant ces entités, mettant en péril des données sensibles liées aux programmes de développement communautaire et aux informations des bénéficiaires.

#### 🇿🇦 Afrique du Sud - Consumer Goods Council of South Africa (CGCSA)
- **Acteur / Groupe:** Stormous (XOverStm)
- **Secteur :** Commerce de détail / Industrie des biens de consommation
- **Site web :** [cgcsa.co.za](https://www.cgcsa.co.za)
- **Statut :** Fuite de données
- **Description :**
  Le groupe Stormous a publié ce qu'il présente comme une fuite de données du Consumer Goods Council of South Africa (CGCSA), organisation représentant les acteurs du commerce de détail, de la distribution et des biens de consommation en Afrique du Sud.
- **Analyse :**
  Selon la publication, environ **20 Go de données** auraient été divulgués après l'échec présumé de négociations avec l'organisation.
  Les données revendiquées comprennent notamment :
        -▫️ rapports internes complets
         -▫️ bases de données clients contenant plusieurs milliers d'enregistrements
         -▫️ scripts et documents techniques
         -▫️ factures
         -▫️ rapports de direction (CEO Reports)
        -▫️ sauvegardes comptables et financières
        -▫️ base complète Sage 200 Evolution (SAGE200EVOSQL)
  Les fichiers observés dans les échantillons montrent la présence de documents financiers, de données comptables, de comptes clients, de factures, de rapports financiers et d'inventaires d'actifs informatiques associés au CGCSA.
  L'exposition de ce type d'informations pourrait permettre à des acteurs malveillants d'obtenir une visibilité détaillée sur les opérations financières, les relations commerciales, les adhérents, les fournisseurs et l'environnement informatique de l'organisation.
  La fuite semble également inclure des sauvegardes de systèmes métiers et comptables susceptibles de contenir des informations financières sensibles ainsi que des données relatives aux entreprises membres du CGCSA.

#### 🇰🇪 Kenya / 🇪🇹 Éthiopie / 🇳🇬 Nigéria / 🇿🇼 Zimbabwe – Fuite de données de CV (Resume docs)
- **Acteur / Groupe:** attackercompany (via le forum [Citizen])
- **Secteur :** Recrutement / Données personnelles
- **Statut :** Fuite de données revendiquée
- **Site web :** Non spécifié (coordonnées du vendeur volontairement omises)
- **Description :**  
  Un cybercriminel revendique une fuite massive de documents CV (*resume docs*) à l’échelle mondiale. Les données concerneraient des centaines de milliers de personnes réparties dans plus de 200 pays.
  Parmi les pays africains explicitement listés dans le décompte publié, on retrouve :
  * 🇰🇪 **Kenya** : 435 enregistrements
  * 🇪🇹 **Éthiopie** : 335 enregistrements
  * 🇳🇬 **Nigeria** : 332 enregistrements
  * 🇿🇼 **Zimbabwe** : 328 enregistrements
  L’extrait de données publié en échantillon contient des champs sensibles tels que :
  - noms et prénoms (*firstName, lastName*)
  - adresses postales complètes, villes et codes postaux
  - numéros de téléphone
  - identifiants clients (*customerId*) et d’abonnement (*subscriptionId*)
  - dates de création et de mise à jour des comptes
  - un champ `country` (dans l’échantillon, la valeur `FR` est systématiquement affichée, ce qui suggère que les données pourraient concerner des ressortissants africains résidant en France, ou bien une valeur par défaut dans la base)
- **Analyse :**  
  Cette fuite expose des informations personnelles extrêmement détaillées (PII), particulièrement utiles pour des campagnes de **phishing ciblé**, de **fraude à l’emploi**, d’**usurpation d’identité** ou d’**ingénierie sociale** à l’encontre de professionnels africains. La présence de numéros de téléphone et d’adresses physiques précises facilite également les tentatives de harcèlement, d’escroqueries téléphoniques (*vishing*) ou de fraude bancaire. Bien que le champ `country` indique `FR` dans l’échantillon, le vendeur identifie clairement ces enregistrements comme appartenant à des citoyens ou résidents du Kenya, d’Éthiopie, du Nigeria et du Zimbabwe, ce qui rend la menace directement applicable à ces pays. Le volume relativement faible par pays (moins de 500) suggère une collecte ciblée ou un segment d’une base plus vaste, mais la précision des données la rend tout aussi dangereuse.

--- 
### 06 Mai 2026
#### 🇬🇭 Ghana - Kasapreko
- **Groupe ransomware :** TheGentlemen
- **Secteur :** Agroalimentaire
- **Site web :** [kasapreko.com](https://kasapreko.com)
- **Statut :** Revendication ransomware
- **Description :** Kasapreko est l'un des principaux producteurs de boissons au Ghana. Le groupe **TheGentlemen** a revendiqué une cyberattaque contre l'entreprise le 6 mai 2026.
---
### 07 Mai 2026
#### 🇪🇬 Égypte - Rhactus Hotel
- **Groupe ransomware :** LockBit 5.0
- **Secteur :** Hôtellerie
- **Site web :** [rhactushotel.com](https://rhactushotel.com)
- **Statut :** Revendication ransomware
- **Description :** Rhactus Hotel est un établissement hôtelier égyptien. Le groupe **LockBit 5.0** a revendiqué une compromission de l'organisation le 7 mai 2026.
---
### 08 Mai 2026
#### 🇪🇬 Égypte - Imex International
- **Groupe ransomware :** Qilin
- **Secteur :** Logistique
- **Site web :** [imex-logistics.com](https://www.imex-logistics.com)
- **Statut :** Revendication ransomware
- **Description :** *Imex International* est une entreprise égyptienne de logistique et de transport international. Le groupe **Qilin** a revendiqué une cyberattaque contre l'organisation le 8 mai 2026.

---
### 09 Mai 2026
#### 🇪🇬 Égypte - Misr Chemical Industries (MCI)
- **Groupe ransomware :** TheGentlemen
- **Secteur :** Industrie chimique
- **Site web :** [mci.com.eg](http://mci.com.eg)
- **Statut :** Revendication ransomware
- **Description :** Misr Chemical Industries est un acteur industriel majeur spécialisé dans la fabrication de produits chimiques. Le groupe **TheGentlemen** a revendiqué une compromission de l'entreprise le 9 mai 2026.

#### 🇳🇬 Nigeria - MRS Holdings
- **Groupe ransomware :** KillSec
- **Secteur :** Énergie
- **Site web :** [www.mrsholdings.com](https://www.mrsholdings.com)
- **Statut :** Revendication ransomware
- **Description :** MRS Holdings est un conglomérat énergétique opérant dans les secteurs pétrolier et gazier au Nigéria. Le groupe **KillSec** revendique la possession et la publication de données exfiltrées appartenant à l'organisation.

----
### 10 Mai 2026
#### 🇪🇬 Égypte - Mansoura University
- **Acteur / Groupe:** INT3X  
- **Secteur :** Éducation / Université  
- **Site web :** [mans.edu.eg](https://www.mans.edu.eg)  
- **Statut :** Fuite de données / Revendication  
- **Description :**  
  Mansoura University est l’une des plus grandes et anciennes universités d’Égypte, accueillant un important volume d’étudiants et de données académiques.
- **Analyse :**  
  L’acteur revendique la fuite de plus de **10 Go** de données comprenant environ **989 000 enregistrements étudiants** couvrant la période 2012–2026, ainsi que des documents internes, travaux de recherche et images d’étudiants.  
  Les données exposées incluraient notamment des identifiants, noms, numéros d’identité nationale, e-mails, mots de passe, informations académiques et documents internes.  
  Une telle exposition pourrait favoriser le vol d’identité, l’accès non autorisé aux comptes universitaires, des campagnes de phishing ciblé et la réutilisation de mots de passe contre d’autres services institutionnels.  
  À ce stade, il s’agit d’une revendication publiée sur un forum clandestin et l’authenticité complète des données n’a pas encore été confirmée indépendamment.
---
### 12 Mai 2026
#### 🇲🇦 Maroc - SDTM / Groupe Barid Al-Maghrib
- **Acteur /Groupe :** Sejjil
- **Secteur :** Logistique / Transport / Services postaux / ERP
- **Site web :**  [groupesdtm.com](https://www.groupesdtm.com/)
- **Statut :** Fuite de données / Revendication
- **Description :**    SDTM est une filiale logistique du Groupe Barid Al-Maghrib spécialisée dans le transport, la distribution, la gestion de flotte et les services associés aux opérations postales et financières au Maroc.
Le 12 mai 2026, le cybercriminel *Sejjil*  revendique l’exposition complète de l’infrastructure ERP et financière de SDTM. L’auteur affirme détenir 129 fichiers CSV structurés provenant de systèmes SAGE ERP, passerelles SMS, données bancaires et plateformes internes associées aux opérations logistiques et financières.
- **Analyse des échantillons :**  
  Les échantillons observés contiennent des métadonnées administratives, comptes utilisateurs ERP, hashes MD5 de mots de passe, tokens de session actifs, adresses email professionnelles, informations d’agences, numéros de téléphone, données financières internes, identifiants RIB, désignations de comptes et informations clients incluant CIN et adresses physiques.

#### 🇹🇳 Tunisie - SETCAR
- **Groupe ransomware :** TheGentlemen
- **Secteur :** Automobile
- **Site web :** [www.setcar.com.tn](https://www.setcar.com.tn)
- **Statut :** Revendication ransomware
- **Description :** SETCAR est une entreprise tunisienne spécialisée dans les équipements automobiles. Le 12 mai 2026, le groupe **TheGentlemen** a revendiqué une cyberattaque contre l'organisation.

#### 🇪🇬 Égypte - FutureShop [Fuite de données / API exposée]

- **Acteur / Groupe :** cc5ab (forum [Citizen])
- **Secteur :** E-commerce / Livraison de courses
- **Statut :** Fuite de données / API exposée
- **Site web :** [futureshop.eg](https://futureshop.eg)
- **Description :**  
  API entièrement exposée sans authentification. Données exposées :
  - 3 893 clients (noms, téléphones, emails, dates d'inscription)
  - 5 181 commandes (prix, notes, statuts, horodatages)
  - 2 438 adresses de livraison (GPS, points de repère, adresses complètes)
  - 643 commandes de magasins (panneau admin)
  - 60 profils de magasins (infos entreprises, contrats, documents d'enregistrement commercial)
  Bucket S3 exposé : futureshopbucket.s3.eu-west-1.amazonaws.com
- **Analyse :**  
  Mauvaise configuration critique de l'API exposant des PII, des adresses de livraison avec GPS et des contrats internes. Permet harcèlement, vols physiques, espionnage concurrentiel et fraudes. Le bucket S3 exposé avec contrats signés et documents commerciaux facilite l'espionnage industriel et la fraude documentaire.
---
### 13 Mai 2026
#### 🇪🇬 Égypte - Ministry of Education
- **Acteur / Groupe :** Revesky
- **Secteur :** Gouvernement / Éducation
- **Site web :** [moe.gov.eg](https://moe.gov.eg/)
- **Statut :** Fuite de données / Vente d’accès
- **Description victime :**  
  Le Ministère égyptien de l’Éducation est l’institution gouvernementale chargée de l’administration du système éducatif national en Égypte, incluant les établissements scolaires, la gestion des élèves, des enseignants et des plateformes éducatives numériques. Le 13 mai 2026, l’acteur *Revesky* revendique la fuite de plusieurs bases de données totalisant environ 22,6 Go de données liées aux élèves, enseignants et administrateurs.
- **Analyse des échantillons :** 
  Les éléments publiés évoquent environ 26,8 millions d’enregistrements d’élèves et 3,8 millions d’enregistrements liés au personnel éducatif et administratif. L’acteur affirme également disposer de privilèges administratifs complets permettant la gestion des comptes enseignants et étudiants, la réinitialisation de mots de passe, la modification d’informations administratives et l’accès à certaines fonctionnalités sensibles de la plateforme éducative.


#### 🇲🇿 Mozambique / 🇱🇷 Liberia / 🇳🇬 Nigéria / 🇹🇬 Togo / 🇸🇱 Sierra Leone – DHIS2 / Ministères de la Santé
- **Acteur / Groupe:** Keymous  
- **Secteur :** Santé / Gouvernement  
- **Plateformes ciblées :** DHIS2 (District Health Information System)  
- **Statut :** Vente d’accès / Compromission présumée  
- **Description :**  **DHIS2** est une plateforme open-source largement utilisée par les ministères de la Santé pour la gestion des données sanitaires, la surveillance épidémiologique et les campagnes de vaccination.
- **Analyse :** L’acteur malveillant revendique plusieurs accès à des instances DHIS2 utilisées par des institutions sanitaires et ministères de la Santé dans plusieurs pays africains et internationaux.  Les artefacts publiés incluent plusieurs couples **URL / identifiant / mot de passe** associés à des plateformes gouvernementales de santé, suggérant une compromission crédible d’identifiants administratifs ou opérationnels.  Les accès revendiqués concernent notamment des infrastructures au :
 ▫️🇲🇿 Mozambique  
  ▫️🇱🇷 Liberia  
  ▫️🇳🇬 Nigeria  
  ▫️🇧🇹 Bhoutan  
  ▫️🇭🇳 Honduras  
  ▫️🇹🇬 Togo  
  ▫️🇸🇱 Sierra Leone  
Une telle compromission pourrait permettre :
  ▫️ accès non autorisé à des données sanitaires nationales  
  ▫️ manipulation ou suppression de données épidémiologiques  
  ▫️ compromission des systèmes de suivi vaccinal  
  ▫️ exfiltration de données médicales et administratives  
  ▫️ perturbation des opérations de santé publique  
AFRINTEL n’a effectué aucune tentative d’authentification afin d’éviter toute interaction non autorisée avec les systèmes concernés.
 ---
### 15 Mai 2026
#### 🇪🇹 Éthiopie - Base de données des ONG [Fuite / Vente de données]

- **Acteur / Groupe :** 404Crew Cyber Team (forum [Citizen])
- **Secteur :** Gouvernement / Société civile / Régulation des ONG
- **Statut :** Fuite / Vente de base de données
- **Site web :** [csogov.et] (agence gouvernementale d’enregistrement et d’audit des ONG)
- **Description :**  
  Vente de la base de données complète de l’agence éthiopienne d’enregistrement des ONG. L’ensemble contient **3 668 enregistrements** d’organisations de la société civile. Chaque fiche comprend le nom en anglais et en amharique, la date d’enregistrement, le numéro de certificat, la catégorie (organisation locale), le type (association caritative, professionnelle, etc.), l’adresse du siège et l’e-mail de contact.
- **Analyse :**  
  L’exposition de l’intégralité du registre des ONG compromet des données opérationnelles sensibles, notamment les contacts dirigeants et les localisations. Cela permet du phishing ciblé, du harcèlement physique et de l’espionnage contre les organisations humanitaires. Les données révèlent également la structure de contrôle gouvernementale, facilitant d’éventuelles attaques contre les autorités de régulation.

#### 🇿🇦 Afrique du Sud - Ephraim Mogale Local Municipality
- **Acteur / Groupe :** NullSec Nigeria x 404Crew Cyber Team x Infernalis
- **Secteur :** Gouvernement local / Administration municipale
- **Site web :** [ephraimmogalelm.gov.za](https://www.ephraimmogalelm.gov.za)
- **Statut :** Fuite de données / Revendication
- **Description :**  
  Ephraim Mogale Local Municipality est une municipalité locale sud-africaine chargée de l'administration publique, de la gestion des services municipaux et du développement local au sein de la province du Limpopo.
- **Analyse :**  
  Les acteurs revendiquent la compromission du site web et de systèmes associés à la municipalité. Les échantillons publiés contiennent des documents administratifs internes, des correspondances officielles et des documents liés à la gestion municipale. Les attaquants affirment détenir environ **111 Go** de données et avoir divulgué un premier échantillon pour appuyer leur revendication. Une telle exposition pourrait entraîner la divulgation d'informations administratives sensibles, faciliter des opérations d'ingénierie sociale et fournir des renseignements exploitables sur l'organisation interne de la municipalité. À ce stade, la portée complète de la compromission n'a pas été confirmée de manière indépendante.
  
#### 🇿🇦 Afrique du Sud - Bellavista School
- **Acteur / Groupe:** 404Crew Cyber Team
- **Secteur :** Éducation
- **Site web :** [bellavista.org.za](https://www.bellavista.org.za)
- **Statut :** Fuite de données
- **Description :**
  Bellavista School est un établissement éducatif sud-africain spécialisé dans l'accompagnement scolaire et le soutien pédagogique des élèves présentant des besoins éducatifs spécifiques.
- **Analyse :**
  Un acteur malveillant a publié un échantillon de données présenté comme provenant du site web de Bellavista School.
  L'échantillon observé contient des informations personnelles associées à des utilisateurs enregistrés sur la plateforme de l'établissement. Les données visibles incluent notamment des identifiants, noms, prénoms, adresses électroniques, dates d'inscription, numéros de téléphone ainsi que diverses informations administratives associées aux comptes.
  Plusieurs adresses e-mail observées appartiennent à des domaines scolaires, éducatifs ou personnels, suggérant la présence de profils d'élèves, de parents, d'enseignants ou de membres du personnel administratif.
  Les dates d'enregistrement visibles s'étendent sur plusieurs années, ce qui pourrait indiquer l'exposition d'une base historique d'utilisateurs de la plateforme.
  Une telle fuite pourrait être exploitée pour mener des campagnes de phishing ciblé contre les familles, les enseignants et les établissements scolaires, faciliter des tentatives d'usurpation d'identité ou permettre la collecte d'informations utiles à des attaques d'ingénierie sociale.
  Les éléments publiés montrent l'exposition effective de données personnelles et constituent un indicateur crédible d'un accès non autorisé à une base liée à l'établissement.


#### 🇪🇬 Égypte - Baitzakat.org.eg [Fuite de données]

- **Acteur / Groupe :** DR-X-LOL (forum [Citizen])
- **Secteur :** Association caritative / Zakat (aumône islamique) / Organisme à but non lucratif
- **Statut :** Fuite de données
- **Site web :** [baitzakat.org.eg](https://baitzakat.org.eg)
- **Description :**  
  Fuite de plus de **300 000 enregistrements** de citoyens égyptiens provenant d'une organisation de zakat. Données exposées : numéro d'identité nationale, numéro de téléphone, affiliation gouvernementale, noms complets et adresses email. Aucun prix demandé (probablement un dump public).
- **Analyse :**  
  Exposition extrêmement sensible : les identifiants nationaux sont des marqueurs irréversibles permettant usurpation d'identité, fraude administrative, contournement KYC et fraude financière. La mention "affiliation gouvernementale" suggère que de nombreux fonctionnaires ou agents publics sont concernés, amplifiant les risques pour la sécurité nationale. La confiance dans le secteur caritatif est gravement compromise.
---
### 16 Mai 2026
#### 🇪🇬 Égypte - Professional Academy for Teachers (PAT)
- **Acteur / Groupe :** INT3X
- **Secteur :** Gouvernement / Éducation
- **Organisation ciblée :** Professional Academy for Teachers (PAT)
- **Site web :** [pat.edu.eg](https://pat.edu.eg)
- **Statut :** Vente de données / Exfiltration massive
- **Description victime :**  
  La Professional Academy for Teachers (PAT), institution égyptienne liée au ministère de l’Éducation et chargée de la gestion, de la formation et de l’accréditation des enseignants, a été revendiquée par l’acteur INT3X.  
  L’auteur affirme détenir entre 8 et 10 Go de données compressées et plus de 80 Go de données non compressées, incluant des informations concernant environ 1,2 million d’enseignants, des étudiants STEM, des contenus académiques, des sauvegardes MSSQL, des bases Microsoft Access ainsi que des images d’identité et documents administratifs.
- **Analyse des échantillons :**  
  Les échantillons observés montrent des exports structurés contenant des noms complets, numéros de téléphone, adresses email, numéros d’identification nationale, codes enseignants, postes occupés, matières enseignées, établissements scolaires, académies régionales, niveaux scolaires et informations administratives internes.  
  
#### 🇿🇦 Afrique du Sud - Department of Correctional Services (DCS)

- **Acteur / Groupe:** NullSec Nigeria x 404Crew Cyber Team x Infernalis
- **Secteur :** Gouvernement / Administration pénitentiaire
- **Site web :** [dcs.gov.za](https://www.dcs.gov.za)
- **Statut :** Fuite de documents / Revendication
- **Description :**
  Le Department of Correctional Services (DCS) est l'administration pénitentiaire sud-africaine chargée de la gestion des établissements correctionnels, de la réinsertion des détenus et des services pénitentiaires à l'échelle nationale.
- **Analyse :**
  Le groupe revendique une compromission du Department of Correctional Services dans le cadre de sa campagne « OpSouthAfrica ».
  Les documents publiés en échantillon semblent être des documents administratifs authentiques du DCS, notamment une communication interne relative aux procédures d'approvisionnement (procurement) ainsi qu'un communiqué officiel du Commissaire National concernant les examens scolaires organisés au sein des établissements correctionnels.
  Les documents observés contiennent des coordonnées de responsables administratifs, des adresses institutionnelles et des informations opérationnelles internes liées au fonctionnement du département.
  À ce stade, les éléments publiés suggèrent principalement une fuite de documents internes plutôt qu'une compromission majeure de systèmes d'information ou une exposition de données personnelles à grande échelle.
  La publication s'inscrit dans une campagne revendiquée comme étant motivée par des considérations politiques et des représailles liées aux tensions xénophobes évoquées par les auteurs.
  
#### 🇰🇪 Kenya - Land Surveyors Board of Kenya (LSB)
- **Acteur / Groupe:** cc5ab
- **Secteur :** Administration publique / Régulation foncière
- **Statut :** Fuite de données / Compromission revendiquée
- **Site web :** [lsb.go.ke](https://www.lsb.go.ke)
- **Description :**
  Un acteur malveillant affirme avoir compromis le système du Land Surveyors Board of Kenya (LSB), organisme gouvernemental chargé de la réglementation et de l'accréditation des géomètres au Kenya.
- **Analyse :**
  Selon la revendication publiée, plusieurs catégories de données et d'informations techniques auraient été exposées.
  Les éléments revendiqués incluent notamment :
        -▫️ 175 géomètres agréés avec noms complets, adresses e-mail personnelles, adresses postales, entreprises associées, numéros de licence et statut d'accréditation
         -▫️ 730 assistants géomètres approuvés contenant noms complets, numéros d'identification nationaux, numéros d'enregistrement et informations sur leurs superviseurs
        -▫️ informations personnelles supplémentaires via des points de vérification exposés (numéros de téléphone, identifiants nationaux, profils utilisateurs)
        -▫️ documentation complète de l'API exposant les endpoints, paramètres de requêtes et mécanismes d'authentification
          -▫️ panneau d'administration Django accessible via un formulaire de connexion
         -▫️ divulgation de paramètres de configuration sensibles comprenant notamment la technologie utilisée (PostgreSQL), les comptes applicatifs, la configuration de messagerie et certains paramètres JWT
        -▫️ structure complète des URL de l'application permettant de cartographier l'ensemble des fonctionnalités accessibles
          -▫️ plus de 45 documents officiels gouvernementaux relatifs à la législation foncière, aux procédures cadastrales et à la réglementation du secteur

  Cette revendication est particulièrement préoccupante car elle ne concerne pas uniquement des données personnelles, mais également des informations techniques susceptibles de faciliter des attaques ultérieures contre l'infrastructure de l'organisation.
  La présence de données d'identification nationales associées à des informations professionnelles augmente également les risques d'usurpation d'identité, de fraude documentaire et d'ingénierie sociale ciblée.

---
### 17 Mai 2026
#### 🇿🇦 Afrique du Sud - Statistics South Africa (Stats SA)
- **Acteur / Groupe :** Kazu  
- **Secteur :** Gouvernement / Statistiques nationales / Administration publique  
- **Site web :** [statssa.gov.za](https://www.statssa.gov.za/)  
- **Statut :** Vente de données  
- **Description :** Statistics South Africa (Stats SA) est l’organisme officiel sud-africain chargé de la collecte, du traitement et de la publication des statistiques nationales démographiques, économiques et sociales.  
- **Analyse :**  
  L’acteur malveillant revendique la possession d’environ **154 Go** de données contenant plus de **453 000 fichiers** attribués à Statistics South Africa.
  Les échantillons diffusés montrent notamment :
        - des cartes d’identité sud-africaines  
         - des relevés académiques et certificats scolaires  
        - des CV contenant des informations personnelles  
        - des documents liés aux opérations de recensement  
         - des fichiers administratifs et éducatifs sensibles  

#### 🇲🇦 Maroc - Multiples plateformes gouvernementales marocaines
- **Acteur / Groupe :** superstarkmc
- **Secteur :** Gouvernement / Éducation / Fiscalité / Services publics
- **Sites web :** [men.gov.ma](https://www.men.gov.ma); [tax.gov.ma](https://www.tax.gov.ma) ; [tgr.gov.ma](https://www.tgr.gov.ma)
- **Statut :** Fuite de données / Vente d’accès / Exposition d’identifiants
- **Description victime :**  Plusieurs plateformes gouvernementales marocaines liées à l’éducation, la fiscalité, la trésorerie publique, la culture, la justice, le transport et les services administratifs ont été citées dans une publication revendiquant une fuite massive d’identifiants d’accès. Les domaines mentionnés incluent notamment Massar, Moutamadris, Waliye, Tax.gov.ma, TGR et plusieurs services administratifs marocains.  
  L’auteur affirme détenir environ 827 000 lignes de données (~16 MB) et propose la vente des accès.
- **Analyse des échantillons :**  Les données observées contiennent des centaines d’identifiants associés à des plateformes gouvernementales marocaines, incluant adresses email *@taalim.ma*, noms d’utilisateurs, mots de passe en clair, accès fiscaux, comptes administratifs éducatifs, services RH, plateformes de concours, systèmes de gestion scolaire, services de trésorerie et plateformes liées aux infractions routières. Plusieurs entrées semblent exposer des accès liés à des services financiers, éducatifs et administratifs sensibles. 
---
### 18 Mai 2026
#### 🇹🇳 Tunisie - CRIT Tunisie
- **Acteur / Groupe :** Titan
- **Secteur :** Conseil / Services RH
- **Site web :** [crit-tunisie.net](https://www.crit-tunisie.net)
- **Statut :** Revendication ransomware
- **Description :**
  CRIT Tunisie est une filiale du groupe français CRIT, spécialisée dans les ressources humaines, le recrutement (CDI/CDD) et le travail temporaire. Implantée en Tunisie pour accompagner les entreprises locales et internationales, la structure gère le sourcing, la sélection et la mise à disposition de personnel qualifié dans divers secteurs clés du pays (industrie, logistique, services, relation client).
  
#### 🇸🇳 Sénégal - Trésor Public du Sénégal

- **Groupe ransomware :** AuditTeam
- **Secteur :** Gouvernement / Finances Publiques
- **Statut :** Claim - Data Sample Published
- **Site web :** [www.tresor.sn](https://www.tresor.sn)
- **Description :**
  Le Trésor Public du Sénégal est l'institution étatique responsable de la gestion des finances publiques, de l'exécution du budget national et du suivi du recouvrement fiscal et des dépenses de l'État. Le groupe ransomware **AuditTeam** a revendiqué la compromission de l'institution les 17-18 mai 2026. Les fichiers analysés sont présentés comme provenant de deux systèmes internes et comportent des dates antérieures à la revendication publique. La durée et la méthode d'accès restent inconnues.
- **Analyse :**
  Les fichiers analysés sont présentés comme des données extraites de deux systèmes internes. Ils ne permettent pas d'établir indépendamment la séquence complète de l'intrusion ni le déploiement d'un ransomware.
  **Serveur 10.6.0.61 (Oracle Database 12.2.0, port 1555) :** Trois dumps de bases de données ont été extraits par l'acteur le 9 mai 2026 :
  - `COLLOC.CO_PERSONNELS` (~40 394 enregistrements) : registre du personnel et de la paie des agents de l'État. Champs présents : identifiants des employés, prénoms et noms, numéros de téléphone, données bancaires (code banque, code guichet, numéro de compte, RIB), codes de service, année de gestion et montants de rémunération.
  - `COLLOC.REDEVABLES` (~960 146 enregistrements) : registre national des contribuables et débiteurs fiscaux. Champs présents : numéro d'identification fiscale (N_C_CONTRIB), dénomination ou nom complet, adresse, téléphone et numéro de registre de commerce. Les données couvrent la période à partir de 2017.
  - `GFORD.ORD_MANDATS` (~659 195 enregistrements) : base complète des ordres de paiement publics. Champs présents : numéro de mandat, date, objet de la transaction, montants (HT et TTC), coordonnées bancaires du bénéficiaire (code banque, guichet, compte, RIB), dénomination du bénéficiaire, NINEA (Numéro d'Identification Nationale des Entreprises et Associations) et libellé de l'opération. Les données couvrent au moins la période d'avril 2024 jusqu'à la date d'extraction.
  **Serveur 10.6.0.26 (Système SICA - Gestion de la Paie et des Salaires) :** Des fichiers opérationnels couvrant la période du 2 janvier 2025 au 8 mai 2026 (18 mois d'opérations financières) ont été extraits, notamment :
  - Fichiers de paie pour les agents de l'État pour mars 2026, par zone géographique.
  - Fichiers de virement datés du 8 mai 2026, au format CSV bancaire standard (code banque, code guichet, numéro de compte, RIB, montant, nom du bénéficiaire, libellé de l'opération). Types observés : salaires, indemnités de correction d'examens, achats de fournitures. Les dates montrent que les fichiers contiennent des informations opérationnelles récentes, sans confirmer indépendamment un accès direct aux systèmes à cette date.
  - Fichiers de mandat de paiement (série MD26-XXXXXX) pour les autorisations de paie individuelles.
  - Virements pour les indemnités d'examen (CFEE 2025), connectant le système du Trésor aux flux de paiement du cycle national d'examens primaires.

  Total des enregistrements représentés dans les éléments analysés : environ **1 659 735 enregistrements** répartis dans trois tables, auxquels s'ajoutent 323 jours de fichiers opérationnels SICA.

  **Observations CTI :**
  - Les dates visibles dans les bases de données et les fichiers d’activité SICA précèdent la publication de la revendication AuditTeam d’environ neuf jours. Cet écart indique que les données présentées comme exfiltrées sont antérieures à la publication, mais ne permet pas de confirmer la durée d’accès, un chiffrement ou la séquence complète de l’incident.
  - La table REDEVABLES (~960 146 enregistrements) représente l'une des plus importantes expositions de données personnelles jamais enregistrées par AFRINTEL pour une institution financière publique en Afrique de l'Ouest.
  - La base GFORD.ORD_MANDATS expose les NINEA et les coordonnées bancaires de l'ensemble des fournisseurs et prestataires de l'État, créant un risque significatif de fraude aux fournisseurs, de BEC (Business Email Compromise) et d'ingénierie sociale financière ciblée contre la chaîne d'approvisionnement publique.
  - Les données de salaires et de virements (comptes bancaires, montants, identités des agents) permettent des fraudes financières directes visant les employés du secteur public.
  - La présence de virements liés aux indemnités d'examen CFEE dans les éléments SICA indique une dépendance inter-institutionnelle concernant les flux de paiement du Ministère de l'Éducation.
  - **Niveau de confiance : Élevé. Niveau d'impact : Niveau 4** (infrastructure financière nationale critique et exposition à grande échelle de données financières et d'identité sensibles).

#### 🇪🇬 Égypte / 🇱🇾 Libye – Scans de passeports [Fuite de données]
- **Acteur / Groupe :** raylie (forum [Citizen])
- **Secteur :** Données personnelles / Documents de voyage / Gouvernement
- **Statut :** Fuite de données (publique)
- **Site web :** Non applicable (lien de téléchargement supprimé)
- **Description :**  
  Fuite publique de scans de passeports provenant de plus de 20 pays. Pays africains concernés : **Égypte** et **Libye**. Autres pays : Azerbaïdjan, Australie, Bosnie, Chine, Colombie, Iran, Irak, Israël, Japon, Jordanie, Koweït, Norvège, Arabie Saoudite, Corée du Sud, Suède, Tadjikistan, États-Unis, Venezuela.
- **Analyse :**  
  Exposition PII extrêmement grave. Les scans de passeports complets permettent des usurpations d'identité massives, des fraudes transfrontalières, des demandes de visa frauduleuses et des crimes financiers. Les victimes égyptiennes et libyennes risquent le clonage d'identité, la falsification de documents et des menaces pour la sécurité nationale.
---
### 19 Mai 2026
#### 🇩🇿 Algérie - OGEBC (Office de Gestion des Biens Culturels) [Fuite / Vente de base de données]

- **Acteur / Groupe :** Databasehooligan (via le forum [Citizen])
- **Secteur :** Gouvernement / Patrimoine culturel / Gestion des biens
- **Statut :** Offre de vente active
- **Site web :** [www.ogebc.com](https://www.ogebc.com)
- **Description :**  
  Un cybercriminel propose à la vente une base de données complète provenant du site officiel de l'**Office de Gestion des Biens Culturels (OGEBC)** en Algérie. L'ensemble contiendrait **425 000 enregistrements** structurés en trois sections principales :
  1. **Clients** : informations de contact et comptes (noms, emails, téléphones, fax, adresses postales, pays, statut du compte, segment client, revenus, crédits, etc.)
  2. **Historique des commandes** : détails des achats, suivi des livraisons, montants, modes de paiement, factures, remises, notes de suivi
  3. **Tickets de support** : historique des interactions, cas clients, priorités, descriptions, agent assigné, évaluations de satisfaction

  Les données sont présentées comme fraîches et organisées. Le prix demandé est de **900 $**, avec possibilité de recourir à un séquestre (*escrow*).
- **Analyse :**  
  Cette fuite est particulièrement sensible car elle concerne une institution publique chargée de la gestion du **patrimoine culturel algérien**. L'exposition de 425 000 enregistrements incluant des données personnelles détaillées (identités, coordonnées, historiques d'achats et de support) présente des risques majeurs :
  - **Usurpation d'identité** et **fraude administrative** utilisant les informations personnelles des citoyens et des professionnels du secteur culturel ;
  - **Ingénierie sociale ciblée** contre les gestionnaires, les artistes, les conservateurs ou les fournisseurs du ministère de la Culture ;
  - **Espionnage économique** sur les flux financiers, les commandes et les relations commerciales de l'institution ;
  - **Phishing** auprès des contacts enregistrés (clients, fournisseurs, partenaires) en exploitant la légitimité de l'institution.

  La structure très complète des données (incluant des notes internes et des tickets de support) suggère un accès profond aux systèmes internes de l'organisation. La vente de ces données pourrait compromettre non seulement la vie privée des citoyens, mais aussi la sécurité des opérations de l'Office et la confiance dans les institutions culturelles algériennes.
---
### 20 Mai 2026
#### 🇲🇦 Maroc - Watiqa.ma
- **Acteur / Groupe:** JBT2026  
- **Secteur :** Gouvernement / État civil  
- **Site web :** [watiqa.ma](https://www.watiqa.ma)  
- **Statut :** Fuite de base de données / Revendication  
- **Description :**  Watiqa.ma est la plateforme officielle marocaine permettant aux citoyens de demander en ligne des documents d’état civil et administratifs.
- **Analyse :** L'acteur revendique la fuite d’environ **695 400 enregistrements** contenant des données personnelles et familiales sensibles, notamment noms, dates de naissance, adresses, téléphones et informations d’état civil.  Les données observées pourraient être exploitées pour des opérations d’usurpation d’identité, de fraude administrative, de phishing ciblé et d’ingénierie sociale contre des citoyens marocains.  
---
### 21 Mai 2026
#### 🇲🇦 Maroc - Avito.ma
- **Acteur / Groupe:** fexus  
- **Secteur :** E-commerce / Marketplace  
- **Site web :** [avito.ma](https://www.avito.ma) 
- **Statut :** Fuite de données 
- **Description :**  Avito.ma est l’une des principales plateformes marocaines de petites annonces et de marketplace, utilisée pour les ventes entre particuliers et professionnels.
- **Analyse :**  L’acteur revendique une fuite contenant des informations d’utilisateurs d’Avito.ma, incluant notamment adresses e-mail, numéros de téléphone, villes et mots de passe.  
  Les échantillons publiés montrent plusieurs profils associés au secteur immobilier (“Crédit Immobilier”) avec des données personnelles marocaines réparties dans différentes villes telles que Casablanca, Khouribga, Kénitra, Guelmim et Oued Zem.  
Les mots de passe publiés semblent être stockés en clair ou réutilisés, ce qui augmente significativement les risques de :
  ▫️ compromission de comptes  
  ▫️ credential stuffing  
  ▫️ phishing ciblé  
  ▫️ fraude et usurpation d’identité  
  ▫️ attaques contre d’autres services utilisant les mêmes identifiants 
  AFRINTEL n’a réalisé aucune tentative d’authentification ni interaction avec les systèmes concernés.
 ---
### 22 Mai 2026
#### 🇲🇦 Maroc - Spacex.ma
- **Acteur / Groupe:** DarkMafiaX  
- **Secteur :** E-commerce / Boutique en ligne  
- **Site web :** [spacex.ma](https://spacex.ma) 
- **Statut :** Fuite de données / Divulgation d’accès administrateur  
- **Description :**  Spacex.ma est présenté comme une plateforme de boutique en ligne marocaine.
- **Analyse :**  L’acteur malveillant a publiquement partagé un accès présumé à l’interface d’administration du site, incluant une URL d’administration ainsi qu’un couple identifiant/mot de passe associé à un compte “admin”.  
  Une telle exposition pourrait permettre :
  ▫️ prise de contrôle du panneau d’administration  
  ▫️ modification du contenu du site  
  ▫️ accès aux données clients et commandes  
  ▫️ déploiement de contenus malveillants ou phishing  
  ▫️ compromission de l’infrastructure web sous-jacente  
AFRINTEL n’a effectué aucune tentative d’authentification afin d’éviter toute interaction non autorisée avec les systèmes concernés.

#### 🇹🇿 Tanzanie - Police (Webmail) [Fuite / Vente de base de données]

- **Acteur / Groupe:** [Citizen] Kampuchean
- **Secteur :** Gouvernement / Forces de l'ordre
- **Statut :** Offre de vente active
- **Site web :** [tpf.go.tz](https://tpf.go.tz)
- **Description :**  
  Un cybercriminel propose à la vente la base de données complète des webmails de la police tanzanienne, correspondant au domaine `tpf.go.tz`. L'ensemble contient plus de **10 000 comptes email policiers complets**, avec les mots de passe en clair (déhashed) ainsi que leurs hashs. Le prix demandé est de **550 $**, avec possibilité de négociation et d'utilisation d'un séquestre (*escrow*).
- **Analyse :**  
  Cette offre est extrêmement critique. L'accès à plus de 10 000 comptes email officiels de la police donne aux acheteurs :
  - un accès direct aux communications internes et aux enquêtes en cours ;
  - la possibilité d'usurper l'identité des officiers pour envoyer des courriels frauduleux depuis un domaine gouvernemental légitime (`@tpf.go.tz`) ;
  - un levier pour réinitialiser d'autres accès administratifs liés à l'institution.

  Cela expose la police tanzanienne à des risques majeurs : espionnage, fuite d'informations judiciaires sensibles, et utilisation des identifiants pour accéder à d'autres services gouvernementaux. La vente de ce type d'accès amplifie considérablement les menaces pesant sur les institutions répressives du pays, d'autant que la base contient des mots de passe en clair, rendant les comptes immédiatement exploitables sans effort de décryptage.


#### 🇲🇦 Maroc - RADEM Meknès [Fuite de données massive – Infrastructure critique]
- **Acteur / Groupe :** anisanas2
- **Secteur :** Eau / Électricité / Infrastructure critique / Services publics
- **Statut :** Fuite de données massive
- **Site web :** [www.radem.ma](http://www.radem.ma)
- **Description :**  
  Fuite de données massive concernant la RADEM (Régie Autonome Intercommunale de Distribution d'Eau et d'Électricité de Meknès), l'entreprise publique chargée de la production, de la distribution et de la maintenance de l'eau potable et de l'électricité à Meknès et ses communes environnantes. L'attaquant revendique l'extraction de près de **1,1 million de documents**. Une première salve de **18 000 documents PDF** est mise en ligne, avec promesse de publier l'intégralité de la base de données et tous les documents dans les 24 heures sur Telegram. Données exposées :
  - **Informations clients** : noms, adresses complètes, numéros de contrat, numéros de client.
  - **Données opérationnelles** : tournées, agences de rattachement, et autres données techniques liées à la distribution d'eau et d'électricité.
- **Analyse :**  
  La compromission d'une régie publique gérant des infrastructures critiques (eau et électricité) représente une menace majeure pour la sécurité nationale et la continuité des services essentiels. Créée en 1969 et employant entre 501 et 1 000 personnes, la RADEM est un acteur central de la région Fès-Meknès. L'exposition des données clients (nom, adresse, numéros de contrat) permet des campagnes de phishing ciblées, des usurpations d'identité et des escroqueries financières. Les données opérationnelles (tournées, agences) pourraient être exploitées pour cartographier les infrastructures sensibles, planifier des sabotages ou des actes de malveillance. La taille massive de la fuite (1,1 million de documents) en fait l'une des plus importantes concernant une infrastructure publique au Maroc. La publication échelonnée (18 000 documents puis le reste) suggère une stratégie de pression ou de monnayage de la donnée. La RADEM, opérant sous tutelle des autorités locales, devra répondre de la protection des données de ses usagers et de la sécurité de ses infrastructures critiques.
  
---
### 23 Mai 2026
#### 🇿🇦 Afrique du Sud - SITA (State Information Technology Agency)

- **Acteur / Groupe:** NullSec Nigeria x NullSec Philippines
- **Secteur :** Technologies de l’information / Services gouvernementaux
- **Site web :** [sita.co.za](https://www.sita.co.za)
- **Statut :** Fuite de données / Revendication
- **Description :**
  SITA (State Information Technology Agency) est l’agence gouvernementale sud-africaine chargée de fournir des services informatiques et des infrastructures numériques aux administrations publiques.
- **Analyse :**
  Le groupe revendique la compromission de SITA et la publication d’un échantillon de données présenté comme provenant de l’organisation. Selon la publication, les informations exposées incluraient des noms d’utilisateurs, des adresses Gmail, des mots de passe (hachés et potentiellement en clair) ainsi que des informations relatives aux plateformes d’accès.
  Si la revendication est authentique, une telle exposition pourrait favoriser des tentatives de compromission de comptes, des campagnes de phishing ciblé, des attaques par réutilisation d’identifiants et des accès non autorisés à des systèmes liés à l’administration publique.
  

#### 🇿🇦 Afrique du Sud - South African Revenue Service (SARS)
- **Acteur / Groupe:** NullSec Nigeria x NullSec Philippines
- **Secteur :** Gouvernement / Administration fiscale
- **Site web :** [sars.gov.za](https://www.sars.gov.za)
- **Statut :** Fuite de données / Revendication
- **Description :**
  Le South African Revenue Service (SARS) est l'administration fiscale nationale d'Afrique du Sud, chargée de la collecte des impôts, des droits de douane et de la gestion des services fiscaux du pays.
- **Analyse :**
  Le groupe revendique la compromission de SARS et affirme détenir des données comprenant des adresses e-mail, des mots de passe et des identifiants associés à des portails liés à l'organisation.
  L'échantillon partagé contient plusieurs couples **e-mail / mot de passe** associés à des URLs de connexion liées au domaine SARS. Toutefois, les adresses e-mail observées appartiennent principalement à des entreprises tierces internationales et ne permettent pas, à elles seules, de confirmer une compromission directe des systèmes de SARS.
  À ce stade, il pourrait s'agir de données issues de campagnes de credential stuffing, de journaux d'infostealers ou d'autres sources de compromission réutilisées dans un contexte lié à SARS. Une validation technique supplémentaire serait nécessaire pour confirmer l'origine exacte des données.

---
### 24 Mai 2026
#### 🇪🇬 Égypte - Papa John's Egypt
- **Groupe ransomware  :** NightSpire
- **Secteur :** Restauration
- **Site web :** [papajohnsegypt.com](https://www.papajohnsegypt.com)
- **Statut :** Revendication ransomware
- **Description :**
  Papa John's Egypt opère la franchise locale de la chaîne internationale de restauration rapide. Le 24 mai 2026, le groupe **NightSpire** a revendiqué une compromission des systèmes de l'organisation.
  
#### 🇪🇬 Égypte - Rawaj Consumer Finance
- **Groupe ransomware :** NightSpire
- **Secteur :** Finance
- **Site web :** [rawaj-finance.com](https://www.rawaj-finance.com)
- **Statut :** Revendication ransomware
- **Description :**
  Rawaj Consumer Finance est un établissement spécialisé dans le crédit à la consommation en Égypte. Le groupe **NightSpire** a revendiqué une cyberattaque contre l'entreprise le 24 mai 2026.

#### 🇿🇦 Afrique du Sud - CERVI My Private Care
- **Acteur / Groupe:** 404Crew Cyber Team
- **Secteur :** Santé numérique (HealthTech) / Services médicaux
- **Site web :** [cervi.co.za](https://www.cervi.co.za)
- **Statut :** Fuite de données
- **Description :**
  CERVI My Private Care est une plateforme sud-africaine de santé numérique utilisée pour la gestion et la coordination de professionnels de santé, pharmacies, cliniques et autres prestataires médicaux.
- **Analyse :**
  Un acteur malveillant a publié un échantillon de données attribué à la plateforme CERVI.
  L'échantillon observé contient des informations détaillées sur des professionnels de santé et établissements médicaux répartis dans plusieurs provinces d'Afrique du Sud.
  Les données exposées incluent notamment des noms et prénoms, numéros BHF (Board of Healthcare Funders), adresses professionnelles, coordonnées téléphoniques, adresses électroniques, informations fiscales ainsi que des coordonnées bancaires associées aux structures médicales concernées.
  Les éléments observés suggèrent l'exposition d'une base de données centralisée de prestataires de santé affiliés à la plateforme.
  Une telle fuite pourrait favoriser des fraudes financières, des tentatives d'usurpation d'identité professionnelle, des attaques de type Business Email Compromise (BEC), la falsification de coordonnées bancaires lors de paiements ainsi que des campagnes de phishing ciblant le secteur médical.
  Les données visibles sont cohérentes avec les services proposés par la plateforme et indiquent une exposition de données opérationnelles sensibles liées à l'écosystème de santé sud-africain.


#### 🇿🇦 Afrique du Sud - mevent.
- **Acteur / Groupe:** 404Crew Cyber Team
- **Secteur :** Événementiel / Gestion d'événements (présumé)
- **Site web :** [mevent.co.za](https://www.mevent.co.za)
- **Statut :** Fuite de données
- **Description :**
  mevent. est une société sud-africaine spécialisée dans l'organisation d'événements, conférences, voyages d'affaires et services MICE (Meetings, Incentives, Conferences & Events).
- **Analyse :**
  Un acteur malveillant a publié un échantillon de données présenté comme provenant de l'organisation.
  Les informations visibles contiennent notamment des noms, numéros de téléphone, localisations et références à des professionnels de santé identifiés comme "Clinic Nurse Practitioner".
  Les localisations observées incluent plusieurs établissements répartis dans différentes régions d'Afrique du Sud, notamment Sandton, Ballito, Bedford Square, Athol Oaklands et Baywest Mall.
  Les données exposées pourraient correspondre à une base de contacts professionnels, un système de gestion de personnel médical ou une plateforme de réservation et de gestion de rendez-vous utilisée par des établissements de santé partenaires.
  Une telle exposition pourrait permettre des campagnes de phishing ciblé, des tentatives d'usurpation d'identité professionnelle et la collecte d'informations sur des personnels médicaux et leurs coordonnées.


#### 🇿🇦 Afrique du Sud - Sheriff Randburg West
- **Acteur / Groupe:** 404Crew Cyber Team
- **Secteur :** Services judiciaires / Exécution des décisions de justice
- **Site web :** [sheriffrandburgwest.co.za](https://www.sheriffrandburgwest.co.za)
- **Statut :** Fuite de données
- **Description :**
  Le Sheriff Randburg West est un bureau officiel de shérif judiciaire en Afrique du Sud, chargé notamment de l'exécution des décisions de justice, des significations d'actes judiciaires et de diverses procédures légales.
- **Analyse :**
  Un acteur malveillant a publié un échantillon de données attribué au site web du Sheriff Randburg West.
  L'échantillon observé contient des informations personnelles de particuliers ayant interagi avec le site ou les services de l'organisation. Les données exposées comprennent notamment des noms complets, adresses électroniques et numéros de téléphone mobiles.
  Plusieurs dizaines d'enregistrements sont visibles dans l'échantillon publié, incluant des adresses Gmail, Outlook, iCloud ainsi que des adresses professionnelles appartenant à diverses organisations sud-africaines.
  La présence de données réelles et cohérentes suggère l'exposition d'une base de contacts ou d'un formulaire de soumission utilisé par des citoyens, clients ou partenaires de l'institution.
  Une telle fuite peut faciliter des campagnes de phishing ciblé, des tentatives d'usurpation d'identité, des fraudes téléphoniques (vishing) ou des opérations d'ingénierie sociale exploitant la confiance accordée à une autorité judiciaire.
  Les éléments publiés démontrent l'exposition effective d'informations personnelles et constituent un indicateur crédible d'un accès non autorisé à des données associées au Sheriff Randburg West.
  
#### 🇪🇬 Égypte - Wuzzuf.net [Fuite / Vente de base de données]
- **Acteur / Groupe :** Databasehooligan 
- **Secteur :** Recrutement / Plateforme d'emploi en ligne
- **Statut :** Fuite / Vente de base de données
- **Site web :** [www.wuzzuf.net](https://www.wuzzuf.net)
- **Description :**  
  Vente d'une base de données de la plateforme égyptienne Wuzzuf.net, contenant environ **672 000 enregistrements** structurés en trois sections :
  - **Contacts** : données personnelles des chercheurs d'emploi (noms, emails, téléphones, adresses, dates de naissance, genre, LinkedIn, Twitter, etc.).
  - **Candidatures** : historique, intitulés de postes, universités, années de diplôme, entretiens, notes des recruteurs, etc.
  - **Authentification** : données de vérification d'identité (numéros d'ID, images de documents, vidéos de vérification, scores de risque, infos appareil, etc.).  
  Prix demandé : **1 100 $**.
- **Analyse :**  
  Fuite extrêmement critique. Au-delà des PII classiques, la section "Authentification" expose des documents d'identité, des vidéos de vérification et des scores de risque. Cela permet des usurpations d'identité massives, des contournements de KYC, des fraudes par deepfake et de l'ingénierie sociale sophistiquée. La plateforme, très utilisée en Égypte, risque d'importantes poursuites et une perte de confiance des utilisateurs.
---
### 26 Mai 2026
#### 🇪🇬 Égypte - B Investments (Basata / Basatamfi)
- **Groupe ransomware  :** NightSpire
- **Secteur :** Services financiers et investissements
- **Site web :** [binvestmentsegypt.com](https://www.binvestmentsegypt.com)
- **Statut :** Revendication ransomware
- **Description :**
  **B Investments Holding** est une importante société égyptienne de capital-investissement et de capital-risque cotée à la bourse égyptienne (EGX), gérant un portefeuille diversifié incluant Basata Financial Holding (services fintech et e-paiement). L'infrastructure numérique de l'organisation a été ciblée par le groupe de ransomware NightSpire, qui a officiellement publié l'entité sur son site de fuite (leak site).
---
### 27 Mai 2026
#### 🇹🇳 Tunisie - Keejob

- **Acteur / Groupe:** Databasehooligan
- **Secteur :** Recrutement / Emploi en ligne
- **Statut :** Fuite de données / Vente de données
- **Site web :** [keejob.com](https://www.keejob.com)
- **Description :**
  Un cybercriminel propose à la vente pour **1 400 USD** une base de données qu'il attribue à la plateforme tunisienne de recrutement Keejob. Selon la publication, l'ensemble contiendrait environ **137 000 enregistrements** liés aux contacts, campagnes e-mail et candidatures.

- **Analyse :**
  Les échantillons publiés montrent la présence de données personnelles et professionnelles comprenant notamment des noms, adresses e-mail, numéros de téléphone, informations de candidature, lettres de motivation, postes recherchés, prétentions salariales, données de recrutement ainsi que des informations relatives aux campagnes e-mail et à leur suivi. L'acteur affirme également que la base complète contiendrait des coordonnées directes, des descriptions de projets et des informations financières.
  
#### 🇹🇳 Tunisie - MyTelnet
* **Acteur / Groupe:** Databasehooligan
* **Secteur :** Télécommunications / Fournisseur d'accès Internet (ISP)
* **Statut :** Fuite de données / Vente de données
* **Site web :** [mytelnet.tn](https://www.mytelnet.tn)
* **Description :** Un cybercriminel propose à la vente pour **1 100 USD** une base de données qu'il attribue à l'opérateur tunisien MyTelnet. Selon la publication, l'ensemble regrouperait des informations clients, des profils d'utilisation de services ainsi que des données démographiques détaillées liées aux abonnés.
* **Analyse :**
  Les échantillons publiés montrent la présence de données personnelles et marketing comprenant notamment des noms, prénoms, adresses e-mail, numéros de téléphone, adresses postales, âges, genres, identifiants utilisateurs, informations de connexion, produits souscrits, historiques d'utilisation, niveaux d'accès, points de fidélité, préférences clients ainsi que des données démographiques telles que la situation familiale, le nombre d'enfants, le niveau d'éducation, la situation professionnelle et les catégories de revenus. L'acteur affirme également que la base complète contient des informations CRM et des profils détaillés de clients destinés aux activités marketing et commerciales.

---
### 27 Mai 2026
#### 🇿🇦 Afrique du Sud - MIDAS

- **Acteur / Groupe:** Databasehooligan
- **Secteur :** Distribution automobile / Pièces détachées / Logistique
- **Site web :** [midas.co.za](https://www.midas.co.za)
- **Statut :** Fuite de données / Vente de données

- **Description :**
  MIDAS est un acteur sud-africain spécialisé dans la distribution de pièces automobiles, d’accessoires et de solutions logistiques destinées aux professionnels et aux particuliers.

- **Analyse :**
  L’acteur revendique la vente d’une base de données contenant environ **463 000 enregistrements** issus des systèmes de gestion de la relation client et des opérations commerciales de MIDAS.

  Selon la publication, les données seraient organisées autour de trois ensembles principaux : **CustomerContact**, **DeliveryAddress** et **SalesOrder**. Les informations exposées incluraient notamment des coordonnées clients, adresses de livraison, numéros de téléphone, adresses e-mail, numéros de TVA, informations commerciales, statuts de comptes, commandes, paiements, factures et données logistiques.

  Une telle exposition pourrait faciliter des campagnes de phishing ciblé, des fraudes commerciales, l’usurpation d’identité d’entreprises clientes, ainsi que la collecte de renseignements sur les opérations et chaînes d’approvisionnement de l’organisation.

  La base de données est proposée à la vente pour **1 100 USD** sur un forum cybercriminel. À ce stade, l’authenticité complète des données revendiquées n’a pas été confirmée de manière indépendante.

#### 🇿🇦 Afrique du Sud - Wanderers Club

- **Acteur / Groupe:** Databasehooligan
- **Secteur :** Sport / Loisirs / Club privé
- **Site web :** [wanderers.co.za](https://www.wanderers.co.za)
- **Statut :** Fuite de données / Vente de données

- **Description :**
  The Wanderers Club est l’un des principaux clubs sportifs et de loisirs d’Afrique du Sud, proposant diverses activités sportives, adhésions et événements à ses membres.

- **Analyse :**
  L’acteur revendique la vente d’une base de données contenant environ **674 000 enregistrements** issus des systèmes de gestion des membres et des événements du club.

  Selon la publication, les données seraient réparties en trois ensembles principaux : **Contacts**, **Sports Memberships** et **Event Bookings**. Les informations exposées incluraient notamment les coordonnées des membres, numéros de téléphone, adresses e-mail, catégories d’adhésion, statuts de membres, historiques d’activités sportives, informations de paiement et réservations d’événements.

  Une telle exposition pourrait favoriser des campagnes de phishing ciblé, l’usurpation d’identité de membres, des fraudes liées aux paiements ainsi que la collecte de renseignements sur les habitudes et activités des adhérents.

  La base de données est proposée à la vente pour **1 400 USD** sur un forum cybercriminel. À ce stade, l’authenticité complète des données revendiquées n’a pas été confirmée de manière indépendante.
  
#### 🇿🇦 Afrique du Sud - Telkom

- **Acteur / Groupe:** Databasehooligan
- **Secteur :** Télécommunications / Fournisseur d’accès Internet
- **Site web :** [telkom.co.za](https://www.telkom.co.za)
- **Statut :** Fuite de données / Vente de données

- **Description :**
  Telkom est l’un des principaux opérateurs télécoms d’Afrique du Sud, fournissant des services de téléphonie fixe et mobile, Internet, fibre optique et solutions numériques aux particuliers et aux entreprises.
- **Analyse :**
  L’acteur revendique la vente d’une base de données contenant environ **742 000 enregistrements** liés aux clients de Telkom.
  Selon la publication, les données seraient organisées autour de trois ensembles principaux : **Contacts**, **Subscription Contracts** et **Support Tickets**. Les informations exposées incluraient notamment des données personnelles de clients (noms, adresses e-mail, numéros de téléphone, dates de naissance, numéros d’identification), des informations contractuelles, des détails de facturation, des soldes de comptes, ainsi que des historiques de tickets de support et d’interactions avec le service client.

  Une telle exposition pourrait faciliter des campagnes de phishing ciblé, l’usurpation d’identité, la fraude aux abonnements, les escroqueries liées au support technique et la collecte de renseignements sur les clients et leurs services souscrits.

  La base de données est proposée à la vente pour **900 USD** sur un forum cybercriminel. À ce stade, l’authenticité complète des données revendiquées n’a pas été confirmée de manière indépendante.
---
### 28 Mai 2026
#### 🇪🇬 Égypte - Citex Systems
- **Acteur / Groupe:** Keymous
- **Secteur :** Télécommunications / TIC
- **Site web :** [citexltd.com](https://www.citexltd.com)
- **Statut :** Fuite de données / Revendication
- **Description :** Citex Systems est une société égyptienne spécialisée dans les télécommunications, les infrastructures réseau, les solutions fintech et les services informatiques.
- **Analyse :**
  L’acteur affirme avoir obtenu un accès à plusieurs bases de données internes de l’entreprise, incluant des informations sur les employés, des données de gestion de projets ainsi que des informations issues du système de messagerie.
  Les échantillons publiés contiennent notamment :
  ▫️ noms et coordonnées professionnelles d’employés  
  ▫️ adresses e-mail d’entreprise  
  ▫️ fonctions et rôles internes  
  ▫️ données RH relatives au personnel  
  ▫️ informations de suivi et de gestion de projets  

  Une telle exposition pourrait faciliter l’ingénierie sociale, le phishing ciblé, l’usurpation d’identité professionnelle et la collecte de renseignements sur les opérations internes de l’entreprise.
  
#### 🇨🇮 Côte d'Ivoire - Mayelia Automotive
- **Groupe ransomware  :** TheGentlemen
- **Secteur :** Automobile
- **Site web :** [mayelia.com](https://www.mayelia.com)
- **Statut :** Revendication ransomware
- **Description :**
  Mayelia Automotive est une entreprise ivoirienne spécialisée dans les services liés à l'automobile, incluant le contrôle technique et la gestion de données véhicules. L'organisation a été ciblée par le gang de ransomware TheGentlemen, qui a officiellement revendiqué l'intrusion en publiant des données exfiltrées sur son site de fuite (leak site).
  
#### 🇳🇬 Nigeria - XL Africa Group
-  **Groupe ransomware:** 0day Syndicate
- **Secteur :** Services aux entreprises
- **Site web :**[xlafricagroup.com](https://www.xlafricagroup.com)
- **Statut :** Revendication ransomware
- **Description :**
  XL Africa Group est un conglomérat de services diversifiés d'origine nigériane. Fondé par Charles Nwodo Jr., le groupe est spécialisé dans l'externalisation (outsourcing) et propose une large gamme de services aux entreprises (B2B), incluant la gestion des ressources humaines, la sécurité, la logistique et le transport, la gestion d'installations (facility management), ainsi que des services de gestion de trésorerie. Le groupe possède une présence opérationnelle étendue au-delà du Nigeria, notamment au Ghana, au Liberia, en Sierra Leone et aux États-Unis. L'organisation a été revendiquée comme victime par l'acteur 0day Syndicate.
  
### 31 Mai 2026
#### 🇹🇳 Tunisie - OptionCarriere.tn [Fuite / Vente de base de données]
- **Acteur /Groupe:** Databasehooligan (forum [Citizen])
- **Secteur :** Recrutement / Plateforme d'emploi
- **Statut :** Fuite / Vente de base de données
- **Site web :** [www.optioncarriere.tn](https://www.optioncarriere.tn)
- **Description :**  
  Vente d'une base de données de la plateforme tunisienne OptionCarriere.tn, contenant environ **274 000 enregistrements** structurés en trois sections :  
  - **Contacts** (chercheurs d'emploi) : noms, emails, téléphones, adresses, date de naissance, genre, profils LinkedIn, etc.  
  - **Candidatures** : historique, dates, lettres de motivation.  
  - **Employeurs** : informations sur les entreprises recruteuses.  
  Prix demandé : **1 300 $**.
- **Analyse :**  
  Exposition massive de données personnelles sensibles. Risques principaux : usurpation d'identité, fraudes à l'emploi, phishing ciblé, ingénierie sociale contre les entreprises. La présence de champs comme LinkedIn, date de naissance et contact d'urgence rend cette base particulièrement dangereuse. La plateforme risque une perte de confiance et des poursuites.
 
#### 🇲🇦 Maroc - Vente massive de bases de données marocaines [Fuite de données / Mise en vente]

- **Acteur / Groupe :** [VIP] anisanas2 / PKA291
- **Secteur :** Gouvernement / Justice / Transport / Formation / Assurance / Logistique
- **Statut :** Mise en vente de données volées
- **Site web :** Multiples entités (voir description)
- **Description :**  
  Un acteur proposant à la vente un ensemble de bases de données marocaines volées, représentant un total combiné de plus de **12 millions de lignes et documents**. Les données, initialement extraites par le groupe PKA291, couvrent plusieurs secteurs sensibles. Offre globale à **5 500 USD** ou vente à l'unité :

  **Entités gouvernementales :**
  - **Ministère de la Justice** : 2 millions de documents / 150 000 dossiers judiciaires – 3 000 USD.
  - **NARSA** (Agence Nationale de la Sécurité Routière) : 2 millions de lignes – 800 USD.
  - **RADEM Meknès** (Régie d'eau et d'électricité) : 1,1 million de documents – 600 USD.
  - **OFPPT** (Office de la Formation Professionnelle) : 400 000 lignes – 300 USD.
  - **LNM6** (institution non identifiée) : 95 000 documents – 500 USD.

  **Entreprises privées :**
  - **Sociétés de livraison** : 8 millions de lignes – 1 800 USD.
  - **Compagnie d'assurance** : accès initial – 600 USD.
  - **Autres sociétés** : 500 000 lignes – 350 USD.

- **Analyse :**  
  Cette vente concerne à la fois des institutions publiques et des entreprises privées au Maroc. Les données judiciaires, routières et de formation professionnelle revendiquées pourraient créer des risques de fraude, d’usurpation d’identité, de phishing et de chantage. Le même acteur a également publié des revendications concernant des institutions marocaines en avril 2026, ce qui indique une activité répétée à suivre. Les sources disponibles ne permettent pas d’établir le vecteur d’accès initial, l’état de la remédiation ni une éventuelle réponse institutionnelle.
