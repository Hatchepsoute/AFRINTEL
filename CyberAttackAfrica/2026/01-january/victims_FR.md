[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Afrique-orange)
![Threat Type](https://img.shields.io/badge/Menace-Ransomware-red)
![Data Source](https://img.shields.io/badge/Source%20des%20données-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Type%20d'Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en Janvier 2026 (30 fiches)
👉🏾 [**English version available here**](./victims.md)

## Résumé du mois

Janvier 2026 compte **30 incidents uniques** : **18 ransomwares**, **10 fuites de données**, **1 vente d'accès** et **1 défacement coordonné**, répartis dans **13 pays africains**.

### Incidents marquants

- **Niger :** défacement coordonné de plus de sept sites de l’État nigérien affichant des messages politiques sur la situation géopolitique du pays.
- **Sénégal :** publication d’une base de données financières attribuée à PixPay.
- **Maroc :** publication d’une base de données aéronautiques attribuée à AOM Aviation Group.
- **Togo :** vente revendiquée d'accès à des infrastructures gouvernementales par Bigbrother.

> Les fiches ci-dessous documentent des revendications ou publications observées. AFRINTEL ne confirme pas une compromission sans élément indépendant.

## Janvier 2026

### 03 janvier 2026

#### 🇹🇬 Togo - Gouvernement du Togo (gouv.tg)
- **Date de publication initiale :** 3 janvier 2026

- **Acteur / Groupe :** Bigbrother (Initial Access Broker)
- **Secteur :** Administration publique centrale
- **Site web :** gouv.tg
- **Statut :** Claim - Unverified
- **Type d'incident :** Vente d'accès
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Description victime :** Infrastructure du gouvernement togolais. L'acteur prétend détenir de nouveaux accès à plusieurs plateformes officielles.

#### 🇿🇦 Afrique du Sud - Constantia Pharmacy
- **Date de publication initiale :** 3 janvier 2026


- **Date de l'incident :** 03 janvier 2026
- **Date de publication / confirmation :** 05 janvier 2026
- **Acteur / Groupe :** Ransomware `Want_to_cry` observé ; opérateur humain non attribué
- **Secteur :** Santé / Pharmacie
- **Statut :** Corroborated
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 2
- **Description :** **Constantia Pharmacy** est une pharmacie de proximité implantée au **Constantia Village Shopping Centre**, au Cap, en Afrique du Sud. Elle propose des services de dispensation de médicaments, de conseil pharmaceutique et une activité de clinique/soins de proximité. Son activité implique des systèmes métiers pharmaceutiques et des données nécessaires au service des patients ([site officiel](https://constantiapharmacy.co.za/)).

- **Vérification indépendante au 18 octobre 2026 :** **Incident antérieur confirmé par enquête journalistique :** MyBroadband a documenté début janvier 2026 l’intervention d’un tiers face à un logiciel de chiffrement sur un serveur de Constantia Pharmacy. Le piratage concernait janvier, pas septembre ; cette fiche ne décrit pas une nouvelle attaque.

- **Sources de vérification complémentaires :** [Source 1](https://mybroadband.co.za/news/security/623956-hacker-rescues-south-african-pharmacy-from-cyber-attack.html)

- **Sources / Éléments de preuve :** [MyBroadband, 5 janvier 2026](https://mybroadband.co.za/news/security/623956-hacker-rescues-south-african-pharmacy-from-cyber-attack.html)

Constantia Pharmacy est une pharmacie indépendante située au Cap. Le 3 janvier, un chercheur a observé via Shodan un serveur Windows exposé appartenant à son environnement alors qu'un ransomware était en cours d'exécution. La pharmacie et son fournisseur ProPharm ont été alertés et sont intervenus. L'observation et la réponse coordonnée corroborent l'incident ; l'exfiltration, le volume chiffré et l'identité de l'opérateur restent inconnus.

### 04 janvier 2026

#### 🇳🇪 Niger - Sites gouvernementaux (Défacement massif)
- **Date de publication initiale :** 4 janvier 2026

- **Acteur / Groupe :** Non revendiqué
- **Secteur :** Administration publique
- **Sites web :** erp.ansi.ne, startups.ansi.ne, stagiaires.ansi.ne, magel.gouv.ne, urbanisme.gouv.ne, promotionfemme.gouv.ne, industrie.gouv.ne
- **Type d'incident :** Défacement
- **Statut :** Under Investigation
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 2
- **Description victime :** Plusieurs plateformes officielles du gouvernement nigérien touchées par une attaque coordonnée affichant un message à caractère politique.

### 06 janvier 2026

#### 🇿🇦 Afrique du Sud - Hytec South Africa
- **Date de publication initiale :** 6 janvier 2026

- **Groupe ransomware :** vect
- **Secteur :** Ingénierie Hydraulique et Mécanique
- **Site web :** hytec.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 2
- **Description victime :** Entreprise sud-africaine spécialisée dans les solutions d'ingénierie hydraulique et mécanique.

### 07 janvier 2026

#### 🇬🇭 Ghana - Nerasolgh (nerasolgh.com)
- **Date de publication initiale :** 7 janvier 2026


- **Acteur / Groupe :** Solonik, publication sur un forum cybercriminel
- **Secteur :** Service public / Gestion des déchets (proche du gouvernement)
- **Site web :** [nerasolgh.com](https://nerasolgh.com)
- **Statut AFRINTEL :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Très élevé
- **Niveau d'impact :** Niveau 4

- **Description :**

  Nerasolgh (nerasolgh.com) exploite un système de facturation de gestion des déchets utilisé pour gérer les comptes clients, les tournées de collecte et les paiements des services d'assainissement/de collecte des déchets au Ghana, avec un paiement des factures par USSD via mobile money.

- **Analyse :**

  AFRINTEL a examiné une publication du 7 janvier 2026 par l'acteur Solonik, intitulée « NERASOLGH.COM - 26M FULL PII + BANK DATA + GEO + HASHES (SQL DUMP) », et a obtenu et examiné de façon indépendante les fichiers de base de données référencés dans la publication. L'acteur revendique 26 082 134 enregistrements au total au format SQL, couvrant nom complet, numéro de téléphone, adresse email, adresse physique, coordonnées GPS, genre, mots de passe hachés et coordonnées bancaires, avec une archive complète proposée au téléchargement.

  L'examen par AFRINTEL de trois exports de base de données référencés confirme le schéma et les marqueurs géographiques décrits par l'acteur : une table clients de 293 232 lignes (`iwms_new.customers`) contenant nom complet, numéros de téléphone principal et secondaire, adresse postale/rue, adresse numérique Ghana Post GPS, coordonnées GPS, genre, un champ de coordonnées bancaires et des mots de passe hachés en bcrypt ; une table utilisateurs/agents de 2 604 lignes (`iwms_new.users`) contenant nom, email, numéro de téléphone, rôle (administrateur, agent de collecte des déchets, abonné), mot de passe haché en bcrypt, jeton d'accès API et jeton de session ; et un journal de transactions mobile money par USSD de 1 357 156 lignes enregistrant identifiant client, nom du client, montant du paiement, MSISDN, opérateur mobile, statut de transaction et horodatages, systématiquement rattachés à des numéros de téléphone ghanéens (+233). L'ensemble des quelque 1,65 million de lignes examinées est structurellement cohérent avec la revendication de l'acteur, mais nettement inférieur aux 26 millions d'enregistrements annoncés, ce qui indique que le dump complet annoncé inclut probablement des tables supplémentaires absentes des éléments examinés.

  L'exposition des coordonnées bancaires et des mots de passe hachés des clients, ainsi que des jetons d'accès API et de session des administrateurs, crée un risque de prise de contrôle de comptes, de détournement frauduleux des paiements de factures, de credential stuffing sur des mots de passe réutilisés, et de compromission supplémentaire du back-office de la plateforme si les jetons restent valides. La correspondance exacte, tant structurelle que géographique, entre les fichiers examinés et la revendication de l'acteur, combinée à l'ampleur et à la sensibilité des éléments examinés, justifie un niveau de confiance très élevé dans l'attribution de l'échantillon. Elle ne valide ni le volume annoncé de 26 millions d'enregistrements, ni la méthode d'acquisition, ni une confirmation officielle par la victime. AFRINTEL ne reproduit aucun nom de client, numéro de téléphone, adresse, mot de passe haché, coordonnée bancaire, enregistrement de transaction ni identifiant issu des éléments examinés.

### 11 janvier 2026

#### 🇪🇬 Égypte - Real Tech
- **Date de publication initiale :** 11 janvier 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Technologie / Sécurité Informatique
- **Site web :** realtech-eg.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 2
- **Description victime :** Firme égyptienne opérant dans le secteur des technologies et de la sécurité informatique.

### 12 janvier 2026

#### 🇿🇦 Afrique du Sud - Land and Agricultural Development Bank of South Africa (Land Bank)
- **Date de publication initiale :** 12 janvier 2026


- **Date de l'incident :** 12 janvier 2026
- **Date de confirmation publique détaillée :** 09 mars 2026
- **Acteur / Groupe :** Non attribué publiquement
- **Secteur :** Gouvernement / Banque publique / Finance
- **Statut :** Victim Confirmed
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** La **Land and Agricultural Development Bank of South Africa (Land Bank)** est une institution financière de développement spécialisée dans l'**agriculture sud-africaine**. Elle finance les exploitations, les entreprises agro-industrielles et les nouveaux entrants dans les filières agricoles afin de soutenir la production et la transformation du secteur. Elle constitue une banque publique de développement sectorielle, distincte d'une banque commerciale généraliste ([présentation officielle](https://www.landbank.co.za/About-Us/Pages/Our-Business.aspx)).

- **Vérification indépendante au 18 octobre 2026 :** **Reconnaissance publique corroborée :** ITWeb a rapporté l’attaque ransomware contre Land Bank survenue en janvier 2026 et les mesures de renforcement prises. Cette fiche a été intégrée en septembre, mais l’incident ne date pas de septembre.

- **Sources de vérification complémentaires :** [Source 1](https://www.itweb.co.za/article/land-bank-tightens-security-after-ransomware-attack/raYAyMorlOl7J38N)

- **Sources / Éléments de preuve :** [ITWeb, 9 mars 2026](https://www.itweb.co.za/article/land-bank-tightens-security-after-ransomware-attack/raYAyMorlOl7J38N) ; [ITWeb, 16 janvier 2026](https://www.itweb.co.za/article/land-bank-flags-it-systems-disruption/Kjlyr7wBDRZvk6am)

Le ministre sud-africain des Finances a confirmé une attaque ransomware détectée le 12 janvier après une activité non autorisée. Une partie des serveurs et ordinateurs portables a été chiffrée et des fichiers ont été exfiltrés ; les systèmes ERP, core banking et CRM critiques n'auraient pas été compromis. L'acteur, le volume exact et la durée de présence restent inconnus.

### 13 janvier 2026

#### 🇪🇬 Égypte - Tepco-Group
- **Date de publication initiale :** 13 janvier 2026

- **Groupe ransomware :** direwolf
- **Secteur :** Ingénierie Électrique
- **Site web :** tepco-group.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 2
- **Description victime :** Groupe égyptien spécialisé dans l'ingénierie électrique.

### 14 janvier 2026

#### 🇲🇺 Maurice - Rogers Capital
- **Date de publication initiale :** 14 janvier 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Services Financiers et Technologie
- **Site web :** rogerscapital.mu
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 3
- **Description victime :** Prestataire de services financiers et technologiques basé à Maurice.

- **Analyse :**
  AFRINTEL a examiné un corpus d'environ 102 fichiers associés à cette revendication, comprenant des documents PDF, DOC/DOCX, RTF et des tableurs. Le contenu correspond à une documentation de conformité et d'entrée en relation typique d'une activité d'administration de licences Global Business (GBL) et de trusts : rapports de classification FATCA et CRS, certificats de constitution, licences GBL, actes de trust, états financiers audités, business plans, documents de gestion de fonds et organigrammes de structure. Le corpus fait référence à plusieurs fonds d'investissement, trusts et entités connexes administrés ou traités par Rogers Capital. Il contient des informations corporatives, financières, fiscales, de déclaration réglementaire, de détention et liées aux bénéficiaires, ainsi que des références à des contacts professionnels et à des comptes. Les documents concernent principalement des structures de fonds et de trusts plutôt que des clients particuliers, mais leur divulgation exposerait des informations réglementaires et commerciales confidentielles pour plusieurs entités, créant des risques de phishing ciblé, de fraude au président, d'usurpation d'identité, de fraude aux paiements et de pression réputationnelle sur les gestionnaires de fonds et les contreparties concernés. AFRINTEL n'a identifié aucun dump confirmé de mots de passe en clair, aucune preuve de chiffrement ni aucun vecteur d'intrusion technique dans les éléments consultés ; le mode d'accès initial reste inconnu. La présence de ces documents justifie la classification comme échantillon de données publié, mais ne confirme pas indépendamment l'intrusion sous-jacente.

### 16 janvier 2026

#### 🇸🇳 Sénégal - PixPay
- **Date de publication initiale :** 16 janvier 2026

- **Acteur / Groupe :** breach3d
- **Secteur :** FinTech (Paiement Mobile)
- **Site web :** pay.pixpay.sn
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4
- **Description victime :** Plateforme sénégalaise de paiement mobile.

- **Analyse :**
  AFRINTEL a consulté la publication et l'échantillon associé. L'acteur breach3d indique que le contenu publié concerne les API de paiement et des données associées, et cite parmi le contenu des jetons JWT, des clés API, des jetons d'accès et des identifiants d'accès à la base de données. L'échantillon accessible correspond à un fichier de configuration d'environnement de production contenant des points d'accès de services, des paramètres de connexion à la base de données et des clés secrètes pour la plateforme pay.pixpay.sn, plutôt qu'à une base de données clients. Si son authenticité est confirmée, l'exposition de ce type d'éléments permettrait à un attaquant d'interagir directement avec le back-end de paiement de PixPay, avec un risque d'appels API non autorisés, de falsification de jetons ou de sessions, et de compromission latérale de systèmes connectés. AFRINTEL ne peut pas confirmer si les identifiants étaient encore valides au moment de la collecte ou s'ils ont depuis été révoqués.

#### 🇲🇿 Mozambique - CFM Mozambique (Portos e Caminhos de Ferro de Moçambique)
- **Date de publication initiale :** 16 janvier 2026

- **Groupe ransomware :** qilin
- **Secteur :** Transport et Logistique (Rail et Ports)
- **Site web :** cfm.co.mz
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Description victime :** Autorité nationale des chemins de fer et des ports du Mozambique.

#### 🇰🇪 Kenya - Plateforme de financement d'appareils PAYGO non identifiée (basée sur Angaza)
- **Date de publication initiale :** 16 janvier 2026


- **Date de l'incident :** Non établie
- **Acteur / Groupe :** OriginalCrazyOldFart, republication sur un forum cybercriminel d'un bucket cloud exposé publiquement
- **Secteur :** Services financiers / Financement d'appareils PAYGO / Commerce de détail
- **Site web :** Non identifié avec certitude
- **Statut AFRINTEL :** Data Fully Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4

- **Description :**

  Les éléments examinés décrivent les opérations kényanes d'une plateforme non identifiée de financement d'appareils en paiement échelonné (PAYGO), construite sur le système SaaS Angaza, utilisée pour vendre des smartphones de marque (modèles Tecno Spark et Tecno Pop observés) à crédit via des agents de terrain locaux. La même archive contiendrait des données pour des opérations parallèles dans au moins une douzaine de marchés supplémentaires en Afrique et en Asie.

- **Analyse :**

  AFRINTEL a examiné une publication du 16 janvier 2026 par le membre de forum OriginalCrazyOldFart (compte ancien, à forte réputation), intitulée « Kenya & other countries Phones.7z FREE (has their names & cities too) ». La publication ne décrit pas une intrusion revendiquée ; elle pointe vers un bucket de stockage cloud exposé publiquement, indexé par le service de scan de buckets grayhatwarfare.com, et diffuse en miroir une archive de 1,28 Go sur un hébergeur de fichiers tiers. L'auteur précise que le matériel n'a pas été obtenu via une intrusion qu'il revendique, et avertit que certains liens peuvent déjà être rompus, sans proposer de nouvelle mise en ligne le cas échéant.

  Le fichier décrit contient à lui seul 27 526 lignes suivant un schéma d'export cohérent de la plateforme Angaza : nom complet du client, numéro de téléphone, ville/région, produit financé, prix journalier de l'échéance, montant cumulé payé, solde restant dû, statut du compte, date d'inscription, ainsi que le nom et le numéro de téléphone de l'agent de recouvrement assigné. Un second fichier mentionné dans la même publication, couvrant plusieurs pays au-delà du Kenya (dont l'Ouganda, le Nigeria, la Tanzanie, le Togo, le Malawi, la Zambie, le Bénin et le Myanmar), suit un schéma plus court : nom du client, numéro de téléphone et un identifiant numérique de compte/appareil. AFRINTEL n'a pas pu déterminer si l'ensemble des pays listés appartient à un seul opérateur multinational ou à plusieurs organisations distinctes partageant la même infrastructure Angaza, ni identifier la marque commerciale précise exploitant la partie kényane du jeu de données à partir des éléments examinés.

  L'ampleur, la cohérence structurelle et la plausibilité des échantillons justifient un niveau de confiance élevé quant à l'exposition de véritables dossiers clients et de financement, indépendamment de la question non résolue de l'identité exacte de l'entreprise. Compte tenu du volume, la combinaison de données financières (montants dus, historique de paiement), de coordonnées personnelles et d'agents de recouvrement nommément identifiés crée un risque significatif de fraude de type recouvrement de créances, d'usurpation d'agents, de phishing et de harcèlement visant les clients de financement dans les pays concernés. AFRINTEL ne reproduit aucun nom de client, numéro de téléphone, identifiant de compte, adresse ni montant financier issu des éléments examinés.

#### 🇪🇬 Égypte - BazookaEgy (bazookaegy.com)
- **Date de publication initiale :** 16 janvier 2026


- **Qualification chronologique :** Publication traitée comme une fuite nouvelle et rapportée en temps réel en janvier 2026 ; la publication de septembre 2024 n'a été identifiée qu'ultérieurement lors d'une revue rétrospective
- **Publication antérieure observée :** 19 septembre 2024, par MrMeeseeks ; relation avec la publication de janvier 2026 non établie
- **Acteur / Groupe :** MrMeeseeks (fuite initiale) ; republié par Sphere sur un forum cybercriminel (RaidForums)
- **Secteur :** Restauration rapide / Commerce de détail
- **Site web :** [bazookaegy.com](https://www.bazookaegy.com)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4

- **Description :**

  Bazooka est une chaîne de restauration rapide égyptienne, présente également au Koweït, aux Émirats arabes unis, au Qatar et à Bahreïn, disposant d'un site de commande et d'inscription en ligne.

- **Analyse :**

  Le compte Sphere a republié le 16 janvier 2026, pour la deuxième fois selon le titre du post (« [REPOST][REPOST] »), une fuite initialement attribuée à l'acteur MrMeeseeks et intitulée « Egypt 1M Costumer information's bazookaegy.com ». L'échantillon affiché dans le post comprend un schéma de champs incluant le canal d'inscription (mobile_ios, mobile_android, IOS, web_site), un identifiant, le prénom, le nom, l'adresse email et le numéro de mobile.

  Une trentaine d'enregistrements complets sont directement visibles dans l'échantillon, avec des noms (en caractères latins et arabes), des adresses email (dont plusieurs adresses de relais privé Apple) et des numéros de téléphone égyptiens. La cohérence du schéma avec une plateforme de commande en ligne et la présence de nombreux enregistrements individuels appuient un niveau de confiance élevé quant à l'authenticité de cette fuite, bien que le volume total d'un million de clients revendiqué dans le titre n'ait pas pu être vérifié indépendamment au-delà de l'échantillon observé. L'exposition de ces données pourrait faciliter le phishing ciblé et le spam commercial contre les clients de l'enseigne. AFRINTEL ne reproduit aucun nom, adresse email ni numéro de téléphone issus de l'échantillon examiné.

  **Relation avec la publication de septembre 2024.** Éléments observés : la publication de septembre 2024 attribuée à MrMeeseeks revendiquait plus d'un million d'enregistrements, plus de 752 000 emails uniques, des noms et des téléphones ; la publication de janvier 2026, traitée comme une fuite nouvelle au moment de sa diffusion et marquée « [REPOST][REPOST] », présente un schéma compatible avec une plateforme de commande et un échantillon visible. Hypothèses non établies : (1) republication du même jeu de données ; (2) seconde fuite issue du même système après une nouvelle vulnérabilité ou un nouvel accès ; (3) ajout ou extraction incrémentale de nouveaux enregistrements ; (4) réutilisation ou revente du corpus par un tiers ; (5) copie partielle avec métadonnées ou titre modifiés ; (6) données provenant d'un prestataire, d'une plateforme de commande ou d'un environnement distinct ; (7) échantillon fabriqué, exagéré ou mal attribué ; (8) négociation, partage ou transfert des données entre acteurs. Inconnus : aucun hash, fichier complet, comparaison de recouvrement, chronologie technique, preuve d'accès initial, transaction, paiement ou confirmation de BazookaEgy ne permet de départager ces scénarios. AFRINTEL conserve donc les publications de 2024 et de 2026 comme deux événements documentaires distincts, sans conclure à deux compromissions indépendantes.

#### 🇩🇿 Algérie - Ligue Régionale de Football d’Alger (LRFA) / Foot’Up [Fuite de données]
- **Date de publication initiale :** 16 janvier 2026


- **Acteur / Groupe :** dark07x
- **Secteur :** Sport / Fédération sportive
- **Site web :** [lrfa.org.dz](https://lrfa.org.dz)
- **Plateforme concernée :** Foot’Up
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 3
- **Description :** Une publication sur un forum cybercriminel revendique la compromission de la plateforme officielle de gestion de la Ligue Régionale de Football d’Alger (LRFA). L’acteur affirme avoir extrait des données liées à plusieurs clubs algériens ainsi qu’aux infrastructures administratives du football régional.

- **Clubs mentionnés dans les artefacts :**
  - Omar Ansar Club
  - Wifaq Sour Ghozlane
  - Chabab Amel Kouba

- **Données observées dans les captures et documents divulgués :**
  - cartes nationales d’identité,
  - licences et documents sportifs,
  - informations de joueurs,
  - données d’entraîneurs et dirigeants,
  - feuilles de matchs,
  - documents administratifs,
  - formulaires internes,
  - signatures et cachets,
  - interfaces d’administration Foot’Up,
  - scans de documents personnels.

- **Analyse CTI :**
  Les éléments publiés suggèrent un accès à une plateforme centralisée de gestion sportive contenant des données administratives et personnelles sensibles liées à plusieurs clubs de football algériens.

  Les captures d’écran montrent également :
  - des accès au portail administratif Foot’Up,
  - des répertoires contenant de nombreux scans de documents,
  - ainsi que des fichiers potentiellement liés aux joueurs, dirigeants et structures sportives régionales.

  Les données exposées peuvent favoriser :
  - usurpation d’identité,
  - fraude documentaire,
  - spear phishing ciblé,
  - compromission d’écosystèmes sportifs,
  - ou exploitation d’informations administratives internes.

- **Note CTI :**
  L’acteur affirme disposer d’un accès étendu à l’infrastructure du football régional algérien. Toutefois, l’étendue exacte de la compromission et l’authenticité complète des accès revendiqués ne peuvent pas être confirmées indépendamment à ce stade.

### 17 janvier 2026

#### 🇹🇿 Tanzanie - CCBRT (Comprehensive Community Based Rehabilitation in Tanzania)
- **Date de publication initiale :** 17 janvier 2026

- **Groupe ransomware :** benzona
- **Secteur :** Santé / Soins Spécialisés
- **Site web :** ccbrt.org
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Description victime :** ONG de santé tanzanienne fournissant des services de réadaptation spécialisés.

#### 🇲🇦 Maroc - Nafae Sanitaire
- **Date de publication initiale :** 17 janvier 2026

- **Groupe ransomware :** tengu
- **Secteur :** Construction (Plomberie et Chauffage)
- **Site web :** nafaesanitaire.com
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 3
- **Description victime :** Entreprise marocaine opérant dans le secteur du bâtiment et du sanitaire.

- **Analyse :**
  AFRINTEL a consulté la fiche du site de fuite du groupe tengu pour cette victime, marquée Encrypted. Le groupe décrit un volume revendiqué de 18,2 Go structuré en huit catégories : journaux de caisse quotidiens couvrant 2022 à 2026, situations financières clients (créances et dettes), un numéro de compte bancaire de l'entreprise (RIB), des bases de données comptables et commerciales Sage 100, des données RH incluant le suivi des absences, des contrats de travail et accords commerciaux, des données de contact fournisseurs et clients, ainsi que des sauvegardes complètes des systèmes comptables. Ce niveau de détail est cohérent avec un accès direct à l'environnement comptable de l'entreprise. AFRINTEL n'a pas eu accès aux fichiers eux-mêmes et ne peut pas confirmer de façon indépendante leur intégrité, leur exhaustivité ni le vecteur d'accès initial exact.

#### 🇹🇳 Tunisie - Exscape App [Fuite de données]
- **Date de publication initiale :** 17 janvier 2026


- **Acteur / Groupe :** forrest
- **Secteur :** Application mobile / Réseau social
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 3
- **Date de fuite :** 17 Janvier 2026

- **Description :** Une publication sur un forum cybercriminel revendique la vente d’une base de données attribuée à Exscape App contenant environ 5 000 profils utilisateurs tunisiens.

- **Données observées :**
  - noms et prénoms
  - noms d’utilisateur
  - emails
  - numéros de téléphone
  - dates de naissance
  - sexe
  - biographies utilisateurs
  - coordonnées GPS
  - niveaux d’abonnement
  - catégories d’âge

- **Analyse CTI :**
  Les données exposées suggèrent une fuite issue d’une base applicative mobile/sociale avec présence d’informations de géolocalisation précises et de profils potentiellement mineurs (“TEEN15”). Les risques incluent doxxing, stalking numérique, phishing ciblé et corrélation d’identité via géolocalisation.

- **Note CTI :**
  L’authenticité complète du dataset n’est pas confirmée indépendamment, mais la structure observée est cohérente avec une base backend d’application mobile.

### 19 janvier 2026

#### 🇩🇿 Algérie - Inter Partner Assistance Algeria [Fuite de données]
- **Date de publication initiale :** 19 janvier 2026


- **Acteur / Groupe :** dark07x
- **Secteur :** Assurance / Assistance automobile / Services d’assistance
- **Site web :** [ipassistance-dz.com](https://ipassistance-dz.com)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 4

- **Description :** Une publication sur un forum cybercriminel revendique la compromission du site officiel d’Inter Partner Assistance Algeria, société spécialisée dans l’assistance automobile, santé, voyage et assurance.

- **Éléments observés dans les documents divulgués :**
  - constats amiables d’accidents automobiles,
  - cartes nationales d’identité algériennes,
  - informations d’assurance automobile,
  - rapports d’expertise automobile,
  - ordres de service CRMA,
  - coordonnées personnelles,
  - signatures et cachets officiels,
  - numéros d’immatriculation,
  - informations sur véhicules et conducteurs,
  - documents administratifs internes.

- **Analyse CTI :**
  Les documents observés contiennent des données personnelles et administratives sensibles permettant potentiellement :
  - usurpation d’identité,
  - fraude à l’assurance,
  - falsification documentaire,
  - spear phishing ciblé,
  - ou exploitation des informations administratives et véhicules.

  Plusieurs artefacts montrent également l’exposition de scans de documents officiels et de dossiers liés à des sinistres automobiles réels.

- **Note CTI :**
  Les captures publiées semblent indiquer un accès à des portails internes et à des données clients/partenaires. L’authenticité complète de l’ensemble des accès revendiqués n’est toutefois pas confirmée indépendamment à ce stade.

### 20 janvier 2026

#### 🇰🇪 Kenya - CPF Financial Services
- **Date de publication initiale :** 20 janvier 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Services Financiers (Fonds de pension)
- **Site web :** cpf.or.ke
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Description victime :** Prestataire de services financiers au Kenya axé sur la gestion des fonds de retraite.

#### 🇰🇪 Kenya - NSSF (National Social Security Fund)
- **Date de publication initiale :** 20 janvier 2026

- **Groupe ransomware :** devman
- **Secteur :** Sécurité Sociale (Retraite)
- **Site web :** nssf.or.ke
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Description victime :** Caisse nationale de sécurité sociale et de retraite du Kenya.

#### 🇿🇦 Afrique du Sud - Paltrack
- **Date de publication initiale :** 20 janvier 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Logiciels Logistiques (Agroalimentaire)
- **Site web :** paltrack.co.za
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 2
- **Description victime :** Fournisseur de solutions logicielles logistiques pour l'industrie agroalimentaire en Afrique du Sud.

#### 🇿🇦 Afrique du Sud - Rola Motor Group
- **Date de publication initiale :** 20 janvier 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Distribution Automobile
- **Site web :** rola.co.za
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 2
- **Description victime :** Groupe sud-africain de concessionnaires et de distribution automobile.

#### 🇿🇦 Afrique du Sud - Municipalité de Witzenberg
- **Date de publication initiale :** 20 janvier 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Administration Publique / Gouvernement Local
- **Site web :** witzenberg.gov.za
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Description victime :** Autorité gouvernementale locale dans le Cap-Occidental, Afrique du Sud.

### 26 janvier 2026

#### 🇰🇪 Kenya - namico.go.ke (National Mining Corporation)
- **Date de publication initiale :** 26 janvier 2026

- **Groupe ransomware :** tengu
- **Secteur :** Mines et Ressources Minérales
- **Site web :** namico.go.ke
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 4
- **Description victime :** Entreprise minière d'État du Kenya.

- **Analyse :**
  AFRINTEL a consulté la fiche du site de fuite du groupe tengu pour NAMICO, marquée Encrypted. Le groupe revendique un volume de 15 Go et affiche une arborescence de fichiers comprenant des répertoires DB, ERP et PORTALS, plusieurs versions compressées d'une application de portail du personnel (CO.STAFFPORTAL), un fichier de sauvegarde complète de base de données (environ 4,8 Go) et des fichiers de base de données SQL Server dépassant 7 Go. Ces éléments sont cohérents avec un accès à l'infrastructure ERP, au portail du personnel et aux bases de données internes de NAMICO, plutôt qu'à un simple ensemble de documents. AFRINTEL n'a pas eu accès au contenu de la base de données et ne peut pas confirmer quelles catégories d'enregistrements elle contient, ni le vecteur d'accès initial.

#### 🇲🇦 Maroc - Portail Marocain des Marchés Publics
- **Date de publication initiale :** 26 janvier 2026


- **Acteur / Groupe :** B4baYega, publication sur un forum cybercriminel
- **Secteur :** Gouvernement / Administration publique / Commande publique
- **Site web :** [marchespublics.gov.ma](https://marchespublics.gov.ma)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3

- **Description :**

  Le Portail Marocain des Marchés Publics est la plateforme nationale d'échange entre les acheteurs publics et les fournisseurs. Il permet la publication et la consultation des appels d'offres, bons de commande, résultats, procès-verbaux et programmes prévisionnels de la commande publique, et il est associé à la Trésorerie Générale du Royaume.

- **Analyse :**

  Une publication attribuée à B4baYega sur un forum cybercriminel, initialement publiée le 26 janvier 2026 et réexaminée par AFRINTEL le 02 juillet 2026, annonce la compromission alléguée de la base du portail et propose les données à la vente pour 300 dollars. L'acteur revendique environ 35 000 enregistrements, 25 000 documents et une archive RAR d'environ 16 Go, avec des données structurées au format CSV et des documents comprenant notamment des fichiers PDF et DOCX. Les éléments fournis ne montrent aucune structure de base, aucun nom de colonne ni contenu documentaire. Bien que la publication mentionne des échantillons textuels et photographiques, aucun échantillon exploitable n'est directement visible ; l'authenticité, l'origine, l'ancienneté, le nombre réel de documents et l'exhaustivité de l'archive restent donc non vérifiés. Compte tenu du rôle du portail, les données revendiquées pourraient faciliter l'identification des acheteurs publics, fournisseurs, procédures contractuelles et relations commerciales avec les administrations, ainsi que le phishing ciblé, la fraude aux appels d'offres, l'usurpation de fournisseurs et l'ingénierie sociale. Les éléments visibles établissent l'existence et les caractéristiques déclarées d'une offre de vente, mais ne démontrent pas indépendamment la compromission du portail ni la possession de la base complète.

### 27 janvier 2026

#### 🇹🇳 Tunisie - FRUIT-BONTÉ
- **Date de publication initiale :** 27 janvier 2026

- **Groupe ransomware :** tengu
- **Secteur :** Industrie Agroalimentaire
- **Site web :** fruit-bonte.com.tn
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Description victime :** Entreprise tunisienne opérant dans l'industrie agroalimentaire et la transformation de fruits.

#### 🇪🇬 Égypte - skyegtours.com
- **Date de publication initiale :** 27 janvier 2026

- **Groupe ransomware :** tengu
- **Secteur :** Tourisme / Voyages et Transport
- **Site web :** skyegtours.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 2
- **Description victime :** Agence de voyages et de tourisme égyptienne.

### 28 janvier 2026

#### 🇩🇿 Algérie - Groupe Tahkout
- **Date de publication initiale :** 28 janvier 2026

- **Groupe ransomware :** tengu
- **Secteur :** Industrie Automobile et Transport
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4
- **Description victime :** Important conglomérat industriel algérien impliqué dans l'assemblage automobile et le transport.

- **Analyse :**
  AFRINTEL a consulté la fiche du site de fuite du groupe tengu pour le Groupe Tahkout, marquée Encrypted, avec un volume revendiqué de 83 Go. Outre la page du site de fuite, AFRINTEL a consulté les images de preuve publiées par le groupe, apparemment prises depuis un hôte Windows Server compromis : une console Server Manager affichant les rôles Active Directory Domain Services, DHCP et DNS configurés (cohérent avec un contrôleur de domaine), un partage réseau nommé « Shares » contenant des dossiers intitulés COMMERCIAL, DLG PAIE, PATRIMOINE, Pointage, POINTAGE FACIAL, Ressources Humaines, RH et Suivi Contrats, ainsi qu'un écran de demande de rançon en plein écran indiquant « YOUR SYSTEM HAS BEEN BLOCKED BY TENGU RANSOMWARE ». Ces éléments indiquent que le groupe a obtenu un accès privilégié à l'infrastructure d'identité principale ainsi qu'aux partages liés à la paie, aux RH, au pointage biométrique et aux contrats, et qu'un ransomware a été exécuté sur au moins un hôte. AFRINTEL n'a pas eu accès aux fichiers divulgués eux-mêmes et ne peut pas confirmer le volume de données exfiltrées, l'impact opérationnel complet ni le vecteur d'accès initial.

### 29 janvier 2026

#### 🇩🇿 Algérie - Algeria Post [Fuite de données]
- **Date de publication initiale :** 29 janvier 2026


- **Acteur / Groupe :** BlueEx
- **Secteur :** Services postaux / Gouvernement / Télécommunications
- **Site web :** [poste.dz](https://www.poste.dz/)
- **Date de fuite :** 29 Janvier 2026
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 4

- **Description :** Une publication sur un forum cybercriminel revendique la vente de plus de 500 000 enregistrements attribués à Algeria Post. Les échantillons publiés incluent des informations personnelles associées à des citoyens algériens ainsi que des photographies de cartes nationales d’identité algériennes.

- **Données observées :**
  - noms et prénoms
  - adresses email
  - numéros de téléphone
  - photographies de cartes d’identité nationales
  - informations personnelles associées aux utilisateurs

- **Analyse CTI :**
  Les données publiées suggèrent une fuite impliquant des informations personnelles sensibles potentiellement liées à des services postaux ou administratifs algériens. La présence simultanée :
  - d’informations de contact,
  - de données d’identité,
  - et de documents officiels

  augmente fortement les risques :
  - d’usurpation d’identité,
  - de fraude administrative,
  - de phishing ciblé,
  - de SIM swapping,
  - ou d’ouverture frauduleuse de comptes et services.

- **Note CTI :**
  L’authenticité complète du dataset ne peut pas être confirmée indépendamment à ce stade. Toutefois, la présence d’échantillons structurés, de données personnelles cohérentes et de photographies de documents d’identité augmente la crédibilité potentielle de la fuite revendiquée.

### 30 janvier 2026

#### 🇲🇦 Maroc - AOM Aviation Group (Air Ocean Maroc)
- **Date de publication initiale :** 30 janvier 2026

- **Acteur / Groupe :** skra1a
- **Secteur :** Transport Aérien / Aviation Civile
- **Site web :** airoceangroup.ma
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 3
- **Description victime :** Groupe marocain fournissant des services de transport aérien et d'aviation civile.
- **Analyse :** L’échantillon publié présente des instructions SQL `INSERT INTO` visant une table de fournisseurs. Les enregistrements visibles contiennent des identifiants de fournisseurs, des noms d’entreprises, des responsables, des adresses professionnelles, des pays, des numéros de téléphone, des adresses e-mail et des dates de création ou de mise à jour. L’extrait associe AOM Aviation Group à un environnement de gestion de fournisseurs du secteur aéronautique et comprend des organisations marocaines ainsi que des partenaires internationaux. La présence de données de contact professionnelles et de références internes expose les personnes et entreprises concernées à des risques de fraude ciblée, d’hameçonnage et d’usurpation de relation commerciale. L’analyse est limitée à l’échantillon visible ; elle ne permet pas d’établir le volume total, l’intégralité des tables concernées, le vecteur d’accès initial ou l’authenticité complète de la base.
