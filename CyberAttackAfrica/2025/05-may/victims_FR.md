[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# Liste des victimes africaines de cyberattaques en Mai 2025 (21 victimes)
👉🏾 [**English version available here**](./victims.md)
## Mai 2025

### 01 Mai 2025
#### 🇿🇦 Afrique du Sud - South African IT firm - iOCO (Filiale de EOH)
- **Groupe ransomware:** devman
- **Secteur:** Technologies / Services managés (MSP) / Cloud
- **Site web:** https://www.eoh.co.za / ioco.tech
- **Statut:** Claim - Unverified
- **Description victime:** EOH est l'un des plus grands prestataires de services technologiques et de conseil en Afrique du Sud, fournissant des solutions de transformation numérique et d'infrastructure. Le groupe Devman a utilisé une description générique ("South African IT firm") sur son site de fuite, une tactique courante pour maintenir la pression pendant les phases de négociation.

### 01 Mai 2025
#### 🇿🇦 Afrique du Sud - DovesIT
- **Groupe ransomware:** devman
- **Secteur:** Technologies de l'Information (IT) / Services Managés (MSP)
- **Site web:** https://dovesit.co.za
- **Statut:** Claim - Unverified
- **Description victime:** DovesIT est un fournisseur de services informatiques (MSP) sud-africain. L'entreprise propose des solutions de sauvegarde, d'hébergement cloud, de maintenance réseau et de cybersécurité pour les petites et moyennes entreprises (PME) en Afrique du Sud.

### 01 Mai 2025
#### 🇿🇦 Afrique du Sud - South African Hr company 
- **Groupe ransomware:** devman
- **Secteur:** Services aux entreprises / Ressources Humaines
- **Site web:** Non précisé
- **Statut:** Claim - Unverified
- **Description victime:** Il s'agit d'un cabinet ou d'un prestataire de services en ressources humaines basé en Afrique du Sud, gérant les données contractuelles, salariales et personnelles de nombreux employés pour le compte de tiers (externalisation RH).

### 05 Mai 2025
#### 🇪🇬 Égypte - Future Association for Microfinance
- **Groupe ransomware:** nightspire
- **Secteur:** Finance / Association
- **Site web:** https://fam-eg.org
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description victime:** ONG égyptienne, spécialisée dans l'octroi de micro-crédits aux micro-entrepreneurs et aux populations rurales.
- **Analyse :** Des éléments datés (preuves) du 6 au 7 mai 2025 comprennent des vues d'interface et des fichiers d'export structurés. Un panneau d'administration web actif, accessible uniquement en HTTP (« Not secure ») à une adresse IP, est utilisé pour gérer des factures de prêts/paiements ; sur l'une des vues, le champ « Customer Name » d'au moins une douzaine d'enregistrements de facture consécutifs a été modifié pour afficher « NightSpire », une technique de preuve d'accès démontrant un accès en écriture à l'application de production plutôt qu'une simple revendication passive. Une liste paginée de gestion de prêts (noms de clients, numéros de référence de type numéro d'identité nationale, dates, montants) s'étale sur des dizaines de pages, et une arborescence de dossiers sur un lecteur partagé interne est organisée par service (Audit, Financial, HR, IT, Legal, MIS, Operation, Risks et leurs combinaisons croisées, plus des dossiers Backup et Meeting Room), cohérente avec la structure interne d'une institution financière de taille moyenne. Les exports structurés examinés (champs incluant REFERENCE_NUMBER, DUE_AMOUNT, MIN/MAX_AMOUNT, DUE_DATE, EXPIRY_DATE, CUSTOMER_NAME, STATUS, PAID_AMOUNT, BRANCH_CODE, CLIENT_NUMBER et LOAN_NUMBER) comprennent plusieurs fichiers allant d'environ 470 à un peu plus de 2 000 lignes chacun, couvrant des données de prêts et de paiements datées d'avril 2024 et avril 2025 sur plusieurs codes d'agence, ce qui indique une extraction récurrente ou en masse plutôt qu'un échantillon limité unique. La combinaison d'un accès en écriture démontré à un panneau d'administration actif et de plusieurs exports de prêts/paiements volumineux et structurellement cohérents soutient une évaluation à confiance très élevée d'une compromission réelle et en cours du système de gestion des prêts de l'association. Compte tenu de l'ampleur des dossiers de prêts et de paiements exposés (noms de clients, identifiants nationaux, montants de prêts et données au niveau des agences) au sein d'une institution de microfinance servant des emprunteurs individuels, l'impact potentiel inclut une fraude à l'identité à grande échelle, une fraude au crédit et une ingénierie sociale ciblée contre une clientèle financièrement vulnérable. Aucun nom de client, identifiant national, montant de prêt ou de paiement, code d'agence ni numéro de référence n'est reproduit.

### 10 Mai 2025
#### 🇿🇦 Afrique du Sud - Pienaar Brothers
- **Groupe ransomware:** devman
- **Secteur:** Équipements de protection individuelle (EPI) / Industrie
- **Site web:** pienaarbrothers.co.za
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** Leader sud-africain dans la fourniture et la distribution d'équipements de protection individuelle (EPI) et de solutions de sécurité pour les secteurs minier, industriel et manufacturier.
- **Analyse:** Des éléments datés du 9 au 10 mai 2025 sont cohérents avec une intrusion active contre l'infrastructure de Pienaar Bros. Un utilitaire d'archivage côté serveur compresse une archive d'environ 2,75 Go et 3 274 fichiers de données de catalogue et de tarification (incluant des grilles tarifaires de gants EPI de marque) en vue d'un envoi vers un service de stockage cloud, aux côtés d'un envoi déjà terminé d'une archive de contrats. Des preuves en ligne de commande montrent l'utilisation d'un compte de service lié aux sauvegardes, compromis, pour parcourir un domaine Windows listant plusieurs serveurs et postes nommés, ainsi qu'un partage de sauvegarde serveur contenant un fichier de demande de rançon daté du 10 mai 2025. Un bon de livraison/feuille de route portant l'en-tête d'une entité commerciale régionale de Pienaar Bros liste des comptes clients professionnels tiers, des numéros de facture et des adresses de livraison. La combinaison d'une exfiltration en cours, de preuves de mouvement latéral sur le domaine et d'une note de rançon déployée sur l'infrastructure interne soutient une évaluation à confiance élevée d'une compromission réelle. Aucun identifiant de service compromis, ni aucun nom de client professionnel, adresse, numéro de facture ou autre enregistrement individuel n'est reproduit.


### 15 Mai 2025
#### 🇲🇷 Mauritanie - Banque Al-Wava Mauritanienne Islamique (BAMIS)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Data Sample Published
- **Description victime :** BAMIS est une banque islamique mauritanienne proposant des services bancaires de détail et aux entreprises conformes à la charia.
- **Analyse :** AFRINTEL a examiné un post DarkForums publié le 15 mai 2025 par l'acteur kill9, intitulé « Mauritanian Banks Data Leak », revendiquant une intrusion coordonnée dans les réseaux internes de six institutions financières mauritaniennes, dont BAMIS. Le post affiche des enregistrements clients non attribués (nom, solde de compte négatif en MRU, identifiant client et mot de passe partiellement masqués) qui n'ont pas pu être rattachés à une banque précise, ainsi qu'un tableau de six échantillons de cartes bancaires partiellement masqués (BIN 471360, catégorie Platinum, dates d'expiration s'échelonnant de 2025 à 2027) explicitement attribués à BAMIS. L'acteur indique que l'ensemble des données sera vendu 48 heures après la publication, avec un contact via Telegram. Le post inclut également un échantillon de carte supplémentaire attribué à un établissement distinct, Banque El Amana, qui ne fait pas partie de la liste des six cibles revendiquées par l'acteur ; AFRINTEL ne peut expliquer cette incohérence. La présence d'échantillons de cartes spécifiquement attribués justifie un niveau de confiance moyen pour BAMIS, alors que l'ampleur, le volume et l'authenticité globale de l'intrusion revendiquée restent non vérifiés. AFRINTEL ne reproduit aucun nom de client, identifiant de compte, mot de passe ni numéro de carte issu du post examiné.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - Banque Mauritanienne pour le Commerce International
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Data Sample Published
- **Description victime :** Banque Mauritanienne pour le Commerce International est une banque commerciale opérant en Mauritanie, offrant des services bancaires de détail et aux entreprises.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite Banque Mauritanienne pour le Commerce International parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Le post inclut un tableau de six échantillons de cartes bancaires partiellement masqués (BIN 488985, catégorie Platinum, dates d'expiration s'échelonnant de 2025 à 2028) explicitement attribués à cette banque, ainsi que des enregistrements clients non attribués (nom, solde négatif, identifiant client et mot de passe partiellement masqués) qui n'ont pas pu être rattachés à un établissement précis. L'ensemble des données est proposé à la vente 48 heures après la publication, via un contact Telegram. La présence d'échantillons de cartes spécifiquement attribués justifie un niveau de confiance moyen, alors que l'ampleur, le volume et l'authenticité globale de l'intrusion revendiquée restent non vérifiés. AFRINTEL ne reproduit aucun nom de client, identifiant de compte, mot de passe ni numéro de carte issu du post examiné.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - Banque pour le Commerce et l'Industrie (BCI)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Data Sample Published
- **Description victime :** BCI est une banque commerciale opérant en Mauritanie, au service d'une clientèle de particuliers et d'entreprises/industriels.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite BCI parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Le post inclut un tableau de six échantillons de cartes bancaires partiellement masqués (BIN 411697, catégorie Platinum, dates d'expiration s'échelonnant de 2025 à 2029) explicitement attribués à BCI, ainsi que des enregistrements clients non attribués (nom, solde négatif, identifiant client et mot de passe partiellement masqués) qui n'ont pas pu être rattachés à un établissement précis. L'ensemble des données est proposé à la vente 48 heures après la publication, via un contact Telegram. La présence d'échantillons de cartes spécifiquement attribués justifie un niveau de confiance moyen, alors que l'ampleur, le volume et l'authenticité globale de l'intrusion revendiquée restent non vérifiés. AFRINTEL ne reproduit aucun nom de client, identifiant de compte, mot de passe ni numéro de carte issu du post examiné.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - Orabank Mauritanie-SA
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Data Sample Published
- **Description victime :** Orabank Mauritanie-SA est la filiale mauritanienne du réseau panafricain Oragroup/Orabank, offrant des services bancaires de détail et aux entreprises.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite Orabank Mauritanie-SA parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Le post inclut un tableau de six échantillons de cartes bancaires partiellement masqués (BIN 455143, catégorie Platinum, dates d'expiration s'échelonnant de 2025 à 2028) explicitement attribués à Orabank, ainsi que des enregistrements clients non attribués (nom, solde négatif, identifiant client et mot de passe partiellement masqués) qui n'ont pas pu être rattachés à un établissement précis. L'ensemble des données est proposé à la vente 48 heures après la publication, via un contact Telegram. La présence d'échantillons de cartes spécifiquement attribués justifie un niveau de confiance moyen, alors que l'ampleur, le volume et l'authenticité globale de l'intrusion revendiquée restent non vérifiés. AFRINTEL ne reproduit aucun nom de client, identifiant de compte, mot de passe ni numéro de carte issu du post examiné.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - Banque Islamique de Mauritanie (BIM Bank)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Unverified
- **Description victime :** BIM Bank est une banque islamique mauritanienne proposant des services bancaires conformes à la charia.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite BIM Bank parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Contrairement à quatre des autres banques citées, le post ne contient aucun échantillon de carte bancaire ni aucune autre donnée spécifiquement attribuée à BIM Bank ; les enregistrements clients non attribués figurant dans le post (nom, solde négatif, identifiant client et mot de passe partiellement masqués) n'ont pas pu être rattachés à cet établissement ni à aucun autre en particulier. En l'absence de preuve spécifique à cette banque, AFRINTEL évalue cette revendication avec un niveau de confiance faible, dans l'attente d'une vérification indépendante.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - General Bank of Mauritania (GBM)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Unverified
- **Description victime :** General Bank of Mauritania (GBM) est une banque commerciale opérant en Mauritanie, offrant des services bancaires de détail et aux entreprises.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite General Bank of Mauritania parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Contrairement à quatre des autres banques citées, le post ne contient aucun échantillon de carte bancaire ni aucune autre donnée spécifiquement attribuée à GBM ; les enregistrements clients non attribués figurant dans le post (nom, solde négatif, identifiant client et mot de passe partiellement masqués) n'ont pas pu être rattachés à cet établissement ni à aucun autre en particulier. En l'absence de preuve spécifique à cette banque, AFRINTEL évalue cette revendication avec un niveau de confiance faible, dans l'attente d'une vérification indépendante.

### 16 Mai 2025
#### 🇿🇦 Afrique du Sud - south african airways (SAA)
- **Groupe ransomware:** incransom
- **Secteur:** Transport aérien
- **Site web:** www.flysaa.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** South African Airways (SAA) est la compagnie aérienne nationale et la plus grande d'Afrique du Sud, assurant des vols domestiques et internationaux.
- **Analyse:** AFRINTEL a examiné un échantillon local de documents cohérents avec la revendication du cybercriminel incransom, correspondant à des dossiers internes de SAA Technical, la division de maintenance, réparation et révision (MRO) de la compagnie. Le matériel comprend des documents réglementaires EASA/SACAA Part-145 (exposé de l'organisme de maintenance, liste de capacités, liste du personnel certificateur et de soutien), un certificat d'autorité d'un mécanicien certificateur comportant un nom, une photo, un numéro d'employé et d'approbation ainsi qu'un périmètre de licence multi-pays, des devis commerciaux et des documents financiers (fiches d'autorisation de crédit, codes débiteurs, analyses de coûts, exports de réconciliation de composants référençant le système de gestion de maintenance AMOS), ainsi qu'un contrat de bail entre Dube TradePort Corporation et Air Chefs SOC Limited, une filiale de la SAA. Les documents font référence à plusieurs clients tiers du MRO, dont Comair, Air Namibia, Yemenia et l'organisme public sud-africain d'acquisition de matériel de défense Armscor. La présence de dossiers opérationnels, réglementaires et financiers cohérents entre eux, s'étalant sur plusieurs années et nommant des systèmes et filiales précis de SAA Technical, soutient une évaluation à confiance élevée d'une compromission interne réelle. L'exposition de données d'identité et de licence du personnel certificateur, associée à la documentation d'approbation réglementaire et aux dossiers commerciaux de clients tiers et liés à la défense, crée un risque de phishing ciblé, de perturbation de la supervision de la sécurité aérienne et d'impact sur la chaîne clients/fournisseurs au-delà de la SAA elle-même. AFRINTEL ne reproduit aucun nom d'employé, photo, numéro de licence ni détail financier client issu de l'échantillon examiné.


### 19 Mai 2025
#### 🇰🇪 Kenya - NSSF(National Social Security Fund) KENYA
- **Groupe ransomware:** devman
- **Secteur:** Gouvernement / Services Sociaux
- **Site web:** www.nssf.go.ke
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Description victime:** Caisse nationale de sécurité sociale du Kenya, l'organisme statutaire gérant les cotisations obligatoires de retraite et de sécurité sociale des travailleurs kényans. L'acteur exige 4,5 millions USD.
- **Analyse :** Un ensemble d'éléments daté du 15 au 18 mai 2025 est cohérent avec un accès administratif réel à l'environnement Windows interne du NSSF. Le matériel inclut un fichier texte de demande de rançon ouvert sur un bureau compromis, affirmant que le « DevMan Cybersecurity Collective » a compromis les systèmes du NSSF à 21h UTC le 17 mai 2025, chiffré les systèmes et fichiers critiques, détruit les sauvegardes cloud et réseau, et exfiltré des données sensibles incluant des dossiers personnels d'employés, des informations financières clients et des détails de pension ; la note cite la loi kényane sur la protection des données de 2019 et menace de sanctions réglementaires et de poursuites clients. Des éléments distincts montrent des sessions Server Manager Windows pour au moins deux serveurs de production joints à un domaine (un hôte de messagerie/web et un hôte de gestion documentaire à grande capacité, tous deux joints à un domaine NSSF), datées des 15 et 16 mai 2025, ainsi qu'une vue de l'explorateur de fichiers listant des disques cohérents avec une base de données Exchange et une infrastructure de virtualisation, datée du 17 mai 2025. Le matériel supplémentaire examiné consiste en des dizaines de formulaires physiques scannés de versement de prestations de retraite portant l'en-tête du Board of Trustees du NSSF, des numéros de référence membre et employeur, et des montants de paiement. La combinaison d'une note de rançon détaillée correspondant au mode opératoire habituel de l'acteur, d'éléments montrant un accès réel de niveau domaine à plusieurs systèmes de production, et de dossiers de retraite archivés scannés, soutient une évaluation à très haute confiance d'une compromission à grande échelle affectant une infrastructure nationale critique de sécurité sociale. Le volume total revendiqué de 2,5 To et la demande de rançon de 4,5 millions de dollars ne sont pas vérifiés indépendamment au-delà de ce qui est affirmé dans le matériel de l'acteur lui-même ; aucun nom d'employé ou de membre, numéro de compte ou de référence, identifiant, ni aucun autre enregistrement individuel n'est reproduit.

### 20 Mai 2025
#### 🇧🇼 Botswana - Medswana
- **Groupe ransomware:** killsec
- **Secteur:** Pharmacie / Santé
- **Site web:** medswana.co.bw
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** Medswana (Pty) Ltd est l'un des principaux distributeurs pharmaceutiques du Botswana.
- **Analyse:** Le groupe ransomware killsec revendique la compromission de Medswana (medswana.co.bw) et affiche des échantillons de données sur sa page de fuite, datés des 22 et 23 mai 2025. Les échantillons couvrent trois catégories de données distinctes. Des comptes clients/débiteurs rattachés à un réseau d'officines opérant sous l'enseigne « Pharma » (Pharma Acacia, Pharma Nord, Pharma Ouest, Pharma Sud, Pharma Afrique, Pharma Kweneng, entre autres) dans plusieurs villes du Botswana (Gaborone, Kasane, Maun, Francistown), comportant nom, adresse postale, numéros de téléphone fixe et mobile et adresse e-mail. Des fiches d'ayants droit rattachées à des régimes d'assurance maladie, comportant nom, date de naissance, sexe, numéro d'affilié, lien de parenté, coordonnées du médecin traitant et champs d'allergies. Des données de stock et de dispensation pharmaceutique (codes produits, désignations de médicaments, quantités, prix d'achat et de vente, numéros d'ordonnance), avec des horodatages couvrant plusieurs années d'activité, de 2021 à 2025. La page de fuite affiche un compte à rebours avant échéance, un prix de rançon non précisé et un compteur de divulgations à 0/1, ce qui indique qu'aucune publication complète n'est encore intervenue à ce stade. La cohérence entre les enseignes commerciales visibles dans les échantillons et le profil de distributeur pharmaceutique attribué à Medswana justifie un niveau de confiance moyen. La nature des données observées, à la fois des informations de santé de patients et des coordonnées clients, justifie un niveau d'impact de niveau 3. Aucun nom de patient, de client ni aucune donnée personnelle brute n'est reproduit dans cette fiche.

### 20 Mai 2025
#### 🇩🇿 Algérie - Université Sétif 1 - Ferhat Abbas (univ-setif.dz)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Phantom Atlas
- **Secteur:** Éducation / Enseignement supérieur
- **Site web:** [univ-setif.dz](https://www.univ-setif.dz)
- **Statut:** Claim - Unverified
- **Description victime:** L'Université Sétif 1 - Ferhat Abbas est un établissement public algérien d'enseignement supérieur.
- **Analyse :** L'acteur Phantom Atlas revendique une intrusion sur le site de l'université et annonce la publication prochaine de fichiers qualifiés d'importants, pour un volume revendiqué de 3,5 Go. Aucun échantillon ni preuve technique n'accompagne cette publication ; AFRINTEL n'a pas collecté ni analysé de données sous-jacentes et ne peut donc pas confirmer la compromission.

### 21 Mai 2025
#### 🇿🇦 Afrique du Sud - Anglo American plc
- **Groupe ransomware:** arkana
- **Secteur:** Mines
- **Statut:** Claim - Unverified
- **Site web:** angloamerican.com
- **Description victime:** Anglo American plc est une multinationale minière basée à Johannesburg et Londres. C'est le plus grand producteur mondial de platine et de diamants, avec des opérations dans plus de 40 pays. Elle exploite également du cuivre, du nickel, du minerai de fer et du charbon.

### 23 Mai 2025
#### 🇿🇦 Afrique du Sud - netstar
- **Groupe ransomware:** devman
- **Secteur:** Technologie / Télématique / Sécurité IoT
- **Site web:** netstar.co.za
- **Statut:** Claim - Unverified
- **Description victime:** Netstar, une filiale du groupe Altron, est le pionnier de l'industrie du suivi et de la récupération de véhicules volés (SVR) en Afrique du Sud.

### 26 Mai 2025
#### 🇿🇦 Afrique du Sud - Mediclinic Group
- **Groupe ransomware:** everest
- **Secteur:** Santé
- **Site web:** https://www.mediclinic.co.za / www.mediclinic.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Description victime:** Mediclinic International (Groupe Mediclinic) est l'un des trois plus grands opérateurs hospitaliers privés en Afrique du Sud. Le groupe gère des dizaines d'hôpitaux multidisciplinaires et de centres de soins de jour à travers le pays (et à l'international, notamment aux Émirats Arabes Unis et en Suisse via Hirslanden).
- **Analyse :** Un ensemble local d'éléments est associé à cette revendication. Le matériel comprend deux vues d'une interface libre-service RH SAP SuccessFactors « People Profile » pour un profil nommé Gregory van Wyk, affiché avec le titre Chief Executive Officer, Office of the CEO, Mediclinic Southern Africa Corporate Office (Johannesburg) ; l'adresse email associée suit un schéma « sftest@mediclinic.com », cohérent avec un compte de test/bac à sable plutôt qu'une donnée de production confirmée, sans exclure qu'il s'agisse d'un enregistrement utilisateur réel. Les modules visibles incluent les informations de paie (accès libre-service au bulletin de salaire et liens Admin Services vers Social Insurance, External Transfers, Loans, Taxes, Employee Remuneration Info, Cost Distribution et Company Car), les informations de rémunération (un montant de salaire de base mensuel sous le groupe de paie « MEDICLINIC Salaries - Management (M1) »), ainsi que des métadonnées d'emploi et d'organisation référençant les entités juridiques Mediclinic (Pty) Ltd et Mediclinic Southern Africa (Pty) Ltd, des codes de compte général (GL) et des champs de classification de poste. Une arborescence de dossiers projet distincte (Requirements, Change Request, LMS Handover, Meetings & Trackers, Configuration, Integrations, Documentation, Migration, ainsi qu'un fichier vidéo « Mediclinic JAM Walkthrough ») présente des tailles de dossiers allant de moins d'1 Mo à environ 1,6 Go pour le dossier Migration, ce qui est cohérent avec un espace de travail de projet ou d'implémentation SuccessFactors plutôt qu'une simple fuite de documents. La cohérence de l'image de marque Mediclinic, des noms d'entités juridiques et de la structure des modules SuccessFactors entre les éléments examinés soutient une évaluation à confiance élevée d'un accès réel à l'environnement du système d'information RH de Mediclinic, bien que la portée, le caractère production ou non, et le volume total de la compromission sous-jacente ne soient pas établis à partir de cet échantillon limité. Aucun montant de salaire, numéro de téléphone, identifiant employé ni autre donnée personnelle n'est reproduit.

### 26 Mai 2025
#### 🇿🇦 Afrique du Sud - FrontierCo
- **Groupe ransomware:** Datacarry
- **Secteur:** Retail / Distribution (Vêtements et chaussures).
- **Site web:** http://frontierco.co.za/
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description victime:** FrontierCo est un acteur majeur de la distribution en Afrique du Sud. La société détient les licences de distribution exclusive et les droits de vente pour plusieurs marques internationales de renom (vêtements, chaussures et accessoires) à travers un large réseau de boutiques physiques et de plateformes d'e-commerce.
- **Analyse :** AFRINTEL a examiné des exports structurés de données clients ainsi que des éléments de reconnaissance réseau associés à cette revendication. Six fichiers CSV, correspondant au schéma de la table « Customer » de Microsoft Dynamics 365 Business Central (champs incluant nom de l'entreprise/du contact, adresse, ville, téléphone, mobile, email, numéro de TVA, limite de crédit, conditions de paiement et autres métadonnées commerciales), totalisent ensemble environ 120 000 fiches clients. Un fichier distinct cohérent avec un export de base de données supplémentaire (environ 99 Mo non compressé) était également présent mais n'a pas été ouvert par AFRINTEL. Un journal de reconnaissance réseau montre un balayage d'énumération SMB contre 256 cibles internes sur une plage /24 interne, dans lequel un identifiant Windows « Administrator » (non reproduit) apparaît authentifié avec succès sur plus d'une douzaine de serveurs, incluant des hôtes nommés de façon cohérente avec un serveur de base de données SQL, deux serveurs de sauvegarde/Veeam, un serveur lié aux RH, un serveur UAT et plusieurs hôtes Hyper-V, aux côtés de tentatives échouées contre d'autres hôtes. Cela indique un accès administratif à l'échelle du domaine obtenu par réutilisation d'identifiants, et non une compromission limitée à un seul système. La combinaison d'un export volumineux et structurellement cohérent de la base clients et d'un mouvement latéral démontré à l'échelle du domaine avec un identifiant administrateur fonctionnel soutient une évaluation à confiance très élevée d'une compromission réelle et étendue de l'environnement informatique de FrontierCo. Compte tenu de l'ampleur des fiches clients exposées (coordonnées, numéros de TVA, conditions commerciales) combinée à un accès de niveau administrateur de domaine confirmé s'étendant à l'infrastructure de base de données, de sauvegarde et RH, l'impact potentiel inclut une fraude à grande échelle visant les clients professionnels, du phishing ciblé et une compromission supplémentaire des systèmes de sauvegarde et financiers. AFRINTEL ne reproduit aucun nom de client, coordonnée, numéro de TVA, hash d'identifiant ni correspondance IP/nom d'hôte issus du matériel examiné.

### 31 Mai 2025
#### 🇨🇲 Cameroun - ASCOMA Cameroon 
- **Groupe ransomware:** worldleaks
- **Secteur:** Assurance
- **Site web:** ascoma.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Description victime:** ASCOMA Cameroun est la branche camerounaise du groupe Ascoma, premier réseau indépendant de courtage d'assurances en Afrique subsaharienne.
- **Analyse :** AFRINTEL a examiné un échantillon local de fichiers cohérents avec la revendication du cybercriminel worldleaks, récupérés depuis un partage de fichiers interne (hôte 192.168.1.20) comprenant des dossiers nommés « Automobile_Transport » et « Sinistre_Sante ». L'échantillon inclut une page de configuration réseau d'une imprimante HP OfficeJet Pro interne, confirmant le domaine interne « ascoma.local », un plan d'adressage IP interne (192.168.1.0/24) ainsi qu'un mot de passe Wi-Fi Direct faible et non modifié, ainsi que des journaux internes de routage scanner/fax listant des destinations de documents rattachées aux services sinistres et médical de l'entreprise (« Sinistre IARD », « Sinistre Santé », « Indemnisation IARDT », « Medical », « Production Santé »). La cohérence entre le nom de domaine interne, la configuration réseau et les noms de dossiers de partage examinés soutient une évaluation à confiance élevée d'un accès réel au réseau interne. Compte tenu du rôle d'ASCOMA en tant que courtier d'assurance traitant des sinistres santé et IARD, et de la présence confirmée d'un partage dédié aux sinistres santé, cet incident présente un risque d'exposition de données de santé et de données personnelles d'assurés, en plus d'une valeur de reconnaissance réseau interne pour une compromission ultérieure. AFRINTEL ne reproduit aucune correspondance IP/nom d'hôte interne, identifiant réseau ni contenu de document du service sinistres issu du matériel examiné.

### 31 Mai 2025
#### 🇹🇬 Togo - Netmaster (netmaster.tg) 
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** cache
- **Secteur:** Technologie / Services Numériques (Hébergement & Domaines).
- **Site web:** netmaster.tg
- **Statut:** Data Fully Published
- **Description victime:** Netmaster est un prestataire de services numériques de premier plan au Togo. Il agit en tant que registrar (bureau d'enregistrement) pour le domaine national .tg et fournit des solutions d'hébergement web, d'e-mails professionnels et de certificats SSL à de nombreuses entreprises et institutions togolaises.
- **Analyse:** AFRINTEL a examiné le post DarkForums ainsi que l'export de base de données référencé, qui correspond à une base WHMCS complète de facturation et de gestion d'hébergement, incluant des tables clients, facturation, hébergement, domaines, tickets de support, administrateurs et passerelles de paiement. Aux côtés de cette base, un fichier annexe liste les codes de transfert EPP de plusieurs centaines de domaines `.tg`, ce qui est cohérent avec le rôle de Netmaster en tant que registrar du domaine national togolais ; l'exposition de ces codes crée un risque de transfert non autorisé de domaines pour les entreprises et institutions togolaises dépendant de Netmaster, en plus des données de facturation et de support propres à la clientèle de Netmaster. La structure et l'ampleur de l'export examiné sont cohérentes avec la revendication du cybercriminel cache concernant une fuite complète de la base de données. AFRINTEL ne reproduit aucun enregistrement client, facture, identifiant ni code EPP issu des éléments examinés.

