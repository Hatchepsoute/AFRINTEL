[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Afrique-orange)
![Threat Type](https://img.shields.io/badge/Menace-Ransomware-red)
![Data Source](https://img.shields.io/badge/Source%20des%20données-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Type%20d'Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en Janvier 2026 (21 victimes)
👉🏾 [**English version available here**](./victims.md)

## Résumé du mois

Janvier 2026 compte **21 incidents uniques** : **17 ransomwares**, **2 fuites de données**, **1 vente d’accès** et **1 défacement coordonné**, répartis dans **12 pays africains**.

### Incidents marquants

- **Niger :** défacement coordonné de plus de sept sites de l’État nigérien affichant des messages politiques sur la situation géopolitique du pays.
- **Sénégal :** publication d’une base de données financières attribuée à PixPay.
- **Maroc :** publication d’une base de données aéronautiques attribuée à AOM Aviation Group.
- **Togo :** vente revendiquée d’accès à des infrastructures gouvernementales par Bigbrother.

> Les fiches ci-dessous documentent des revendications ou publications observées. AFRINTEL ne confirme pas une compromission sans élément indépendant.

## Janvier 2026

### 03 Janvier 2026
#### 🇹🇬 Togo - Gouvernement du Togo (gouv.tg)
- **Acteur / Groupe :** Bigbrother (Initial Access Broker)
- **Secteur :** Administration publique centrale
- **Site web :** gouv.tg
- **Statut :** Claim - Unverified
- **Type d'incident :** Vente d'accès
- **Description victime :** Infrastructure du gouvernement togolais. L'acteur prétend détenir de nouveaux accès à plusieurs plateformes officielles.

### 04 Janvier 2026
#### 🇳🇪 Niger - Sites gouvernementaux (Défacement massif)
- **Acteur / Groupe :** Non revendiqué
- **Secteur :** Administration publique
- **Sites web :** erp.ansi.ne, startups.ansi.ne, stagiaires.ansi.ne, magel.gouv.ne, urbanisme.gouv.ne, promotionfemme.gouv.ne, industrie.gouv.ne
- **Type d.incident :** Défacement
- **Statut :** Under Investigation
- **Description victime :** Plusieurs plateformes officielles du gouvernement nigérien touchées par une attaque coordonnée affichant un message à caractère politique.

### 06 Janvier 2026
#### 🇿🇦 Afrique du Sud - Hytec South Africa
- **Groupe ransomware :** vect
- **Secteur :** Ingénierie Hydraulique et Mécanique
- **Site web :** hytec.com
- **Statut :** Claim - Unverified
- **Description victime :** Entreprise sud-africaine spécialisée dans les solutions d'ingénierie hydraulique et mécanique.

### 08 Janvier 2026
#### 🇰🇪 Kenya - National Water Authority
- **Groupe ransomware :** blackshrantac
- **Secteur :** Services Publics (Gestion de l'eau)
- **Site web :** nwa.go.ke
- **Statut :** Claim - Unverified
- **Description victime :** Autorité publique kenyane responsable de la gestion des ressources en eau.

### 11 Janvier 2026
#### 🇪🇬 Égypte - Real Tech
- **Groupe ransomware :** TheGentlemen
- **Secteur :** Technologie / Sécurité Informatique
- **Site web :** realtech-eg.com
- **Statut :** Claim - Unverified
- **Description victime :** Firme égyptienne opérant dans le secteur des technologies et de la sécurité informatique.

### 13 Janvier 2026
#### 🇪🇬 Égypte - Tepco-Group
- **Groupe ransomware :** direwolf
- **Secteur :** Ingénierie Électrique
- **Site web :** tepco-group.com
- **Statut :** Claim - Unverified
- **Description victime :** Groupe égyptien spécialisé dans l'ingénierie électrique.

### 14 Janvier 2026
#### 🇲🇺 Maurice - Rogers Capital
- **Groupe ransomware :** TheGentlemen
- **Secteur :** Services Financiers et Technologie
- **Site web :** rogerscapital.mu
- **Statut :** Claim - Data Sample Published
- **Description victime :** Prestataire de services financiers et technologiques basé à Maurice.

- **Analyse :**
  AFRINTEL a examiné un corpus d'environ 102 fichiers associés à cette revendication, comprenant des documents PDF, DOC/DOCX, RTF et des tableurs. Le contenu correspond à une documentation de conformité et d'entrée en relation typique d'une activité d'administration de licences Global Business (GBL) et de trusts : rapports de classification FATCA et CRS, certificats de constitution, licences GBL, actes de trust, états financiers audités, business plans, documents de gestion de fonds et organigrammes de structure. Le corpus fait référence à plusieurs fonds d'investissement, trusts et entités connexes administrés ou traités par Rogers Capital. Il contient des informations corporatives, financières, fiscales, de déclaration réglementaire, de détention et liées aux bénéficiaires, ainsi que des références à des contacts professionnels et à des comptes. Les documents concernent principalement des structures de fonds et de trusts plutôt que des clients particuliers, mais leur divulgation exposerait des informations réglementaires et commerciales confidentielles pour plusieurs entités, créant des risques de phishing ciblé, de fraude au président, d'usurpation d'identité, de fraude aux paiements et de pression réputationnelle sur les gestionnaires de fonds et les contreparties concernés. AFRINTEL n'a identifié aucun dump confirmé de mots de passe en clair, aucune preuve de chiffrement ni aucun vecteur d'intrusion technique dans les éléments consultés ; le mode d'accès initial reste inconnu. La présence de ces documents justifie la classification comme échantillon de données publié, mais ne confirme pas indépendamment l'intrusion sous-jacente.

### 16 Janvier 2026
#### 🇸🇳 Sénégal - PixPay
- **Acteur / Groupe :** breach3d
- **Secteur :** FinTech (Paiement Mobile)
- **Site web :** pay.pixpay.sn
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Plateforme sénégalese de paiement mobile.

- **Analyse :**
  AFRINTEL a consulté la publication et l'échantillon associé. L'acteur breach3d indique que le contenu publié concerne les API de paiement et des données associées, et cite parmi le contenu des jetons JWT, des clés API, des jetons d'accès et des identifiants d'accès à la base de données. L'échantillon accessible correspond à un fichier de configuration d'environnement de production contenant des points d'accès de services, des paramètres de connexion à la base de données et des clés secrètes pour la plateforme pay.pixpay.sn, plutôt qu'à une base de données clients. Si son authenticité est confirmée, l'exposition de ce type d'éléments permettrait à un attaquant d'interagir directement avec le back-end de paiement de PixPay, avec un risque d'appels API non autorisés, de falsification de jetons ou de sessions, et de compromission latérale de systèmes connectés. AFRINTEL ne peut pas confirmer si les identifiants étaient encore valides au moment de la collecte ou s'ils ont depuis été révoqués.

### 16 Janvier 2026
#### 🇲🇿 Mozambique - CFM Mozambique (Portos e Caminhos de Ferro de Moçambique)
- **Groupe ransomware :** qilin
- **Secteur :** Transport et Logistique (Rail et Ports)
- **Site web :** cfm.co.mz
- **Statut :** Claim - Unverified
- **Description victime :** Autorité nationale des chemins de fer et des ports du Mozambique.

### 17 Janvier 2026
#### 🇹🇿 Tanzanie - CCBRT (Comprehensive Community Based Rehabilitation in Tanzania)
- **Groupe ransomware :** benzona
- **Secteur :** Santé / Soins Spécialisés
- **Site web :** ccbrt.org
- **Statut :** Claim - Unverified
- **Description victime :** ONG de santé tanzanienne fournissant des services de réadaptation spécialisés.

### 17 Janvier 2026
#### 🇲🇦 Maroc - Nafae Sanitaire
- **Groupe ransomware :** tengu
- **Secteur :** Construction (Plomberie et Chauffage)
- **Site web :** nafaesanitaire.com
- **Statut :** Claim - Data Sample Published
- **Description victime :** Entreprise marocaine opérant dans le secteur du bâtiment et du sanitaire.

- **Analyse :**
  AFRINTEL a consulté la fiche du site de fuite du groupe tengu pour cette victime, marquée Encrypted. Le groupe décrit un volume revendiqué de 18,2 Go structuré en huit catégories : journaux de caisse quotidiens couvrant 2022 à 2026, situations financières clients (créances et dettes), un numéro de compte bancaire de l'entreprise (RIB), des bases de données comptables et commerciales Sage 100, des données RH incluant le suivi des absences, des contrats de travail et accords commerciaux, des données de contact fournisseurs et clients, ainsi que des sauvegardes complètes des systèmes comptables. Ce niveau de détail est cohérent avec un accès direct à l'environnement comptable de l'entreprise. AFRINTEL n'a pas eu accès aux fichiers eux-mêmes et ne peut pas confirmer de façon indépendante leur intégrité, leur exhaustivité ni le vecteur d'accès initial exact.

### 20 Janvier 2026
#### 🇰🇪 Kenya - CPF Financial Services
- **Groupe ransomware :** TheGentlemen
- **Secteur :** Services Financiers (Fonds de pension)
- **Site web :** cpf.or.ke
- **Statut :** Claim - Unverified
- **Description victime :** Prestataire de services financiers au Kenya axé sur la gestion des fonds de retraite.

### 20 Janvier 2026
#### 🇰🇪 Kenya - NSSF (National Social Security Fund)
- **Groupe ransomware :** devman
- **Secteur :** Sécurité Sociale (Retraite)
- **Site web :** nssf.or.ke
- **Statut :** Claim - Unverified
- **Description victime :** Caisse nationale de sécurité sociale et de retraite du Kenya.

### 20 Janvier 2026
#### 🇿🇦 Afrique du Sud - Paltrack
- **Groupe ransomware :** TheGentlemen
- **Secteur :** Logiciels Logistiques (Agroalimentaire)
- **Site web :** paltrack.co.za
- **Statut :** Claim - Unverified
- **Description victime :** Fournisseur de solutions logicielles logistiques pour l'industrie agroalimentaire en Afrique du Sud.

### 20 Janvier 2026
#### 🇿🇦 Afrique du Sud - Rola Motor Group
- **Groupe ransomware :** TheGentlemen
- **Secteur :** Distribution Automobile
- **Site web :** rola.co.za
- **Statut :** Claim - Unverified
- **Description victime :** Groupe sud-africain de concessionnaires et de distribution automobile.

### 20 Janvier 2026
#### 🇿🇦 Afrique du Sud - Municipalité de Witzenberg
- **Groupe ransomware :** TheGentlemen
- **Secteur :** Administration Publique / Gouvernement Local
- **Site web :** witzenberg.gov.za
- **Statut :** Claim - Unverified
- **Description victime :** Autorité gouvernementale locale dans le Cap-Occidental, Afrique du Sud.

### 26 Janvier 2026
#### 🇰🇪 Kenya - namico.go.ke (National Mining Corporation)
- **Groupe ransomware :** tengu
- **Secteur :** Mines et Ressources Minérales
- **Site web :** namico.go.ke
- **Statut :** Claim - Data Sample Published
- **Description victime :** Entreprise minière d'État du Kenya.

- **Analyse :**
  AFRINTEL a consulté la fiche du site de fuite du groupe tengu pour NAMICO, marquée Encrypted. Le groupe revendique un volume de 15 Go et affiche une arborescence de fichiers comprenant des répertoires DB, ERP et PORTALS, plusieurs versions compressées d'une application de portail du personnel (CO.STAFFPORTAL), un fichier de sauvegarde complète de base de données (environ 4,8 Go) et des fichiers de base de données SQL Server dépassant 7 Go. Ces éléments sont cohérents avec un accès à l'infrastructure ERP, au portail du personnel et aux bases de données internes de NAMICO, plutôt qu'à un simple ensemble de documents. AFRINTEL n'a pas eu accès au contenu de la base de données et ne peut pas confirmer quelles catégories d'enregistrements elle contient, ni le vecteur d'accès initial.

### 27 Janvier 2026
#### 🇹🇳 Tunisie - FRUIT-BONTÉ
- **Groupe ransomware :** tengu
- **Secteur :** Industrie Agroalimentaire
- **Site web :** fruit-bonte.com.tn
- **Statut :** Claim - Unverified
- **Description victime :** Entreprise tunisienne opérant dans l'industrie agroalimentaire et la transformation de fruits.

### 27 Janvier 2026
#### 🇪🇬 Égypte - skyegtours.com
- **Groupe ransomware :** tengu
- **Secteur :** Tourisme / Voyages et Transport
- **Site web :** skyegtours.com
- **Statut :** Claim - Unverified
- **Description victime :** Agence de voyages et de tourisme égyptienne.

### 28 Janvier 2026
#### 🇩🇿 Algérie - Groupe Tahkout
- **Groupe ransomware :** tengu
- **Secteur :** Industrie Automobile et Transport
- **Statut :** Claim - Data Sample Published
- **Description victime :** Important conglomérat industriel algérien impliqué dans l'assemblage automobile et le transport.

- **Analyse :**
  AFRINTEL a consulté la fiche du site de fuite du groupe tengu pour le Groupe Tahkout, marquée Encrypted, avec un volume revendiqué de 83 Go. Outre la page du site de fuite, AFRINTEL a consulté les images de preuve publiées par le groupe, apparemment prises depuis un hôte Windows Server compromis : une console Server Manager affichant les rôles Active Directory Domain Services, DHCP et DNS configurés (cohérent avec un contrôleur de domaine), un partage réseau nommé « Shares » contenant des dossiers intitulés COMMERCIAL, DLG PAIE, PATRIMOINE, Pointage, POINTAGE FACIAL, Ressources Humaines, RH et Suivi Contrats, ainsi qu'un écran de demande de rançon en plein écran indiquant « YOUR SYSTEM HAS BEEN BLOCKED BY TENGU RANSOMWARE ». Ces éléments indiquent que le groupe a obtenu un accès privilégié à l'infrastructure d'identité principale ainsi qu'aux partages liés à la paie, aux RH, au pointage biométrique et aux contrats, et qu'un ransomware a été exécuté sur au moins un hôte. AFRINTEL n'a pas eu accès aux fichiers divulgués eux-mêmes et ne peut pas confirmer le volume de données exfiltrées, l'impact opérationnel complet ni le vecteur d'accès initial.

### 31 Janvier 2026
#### 🇲🇦 Maroc - AOM Aviation Group (Air Ocean Maroc)
- **Acteur / Groupe :** skra1a
- **Secteur :** Transport Aérien / Aviation Civile
- **Site web :** airoceangroup.ma
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Groupe marocain fournissant des services de transport aérien et d'aviation civile.
