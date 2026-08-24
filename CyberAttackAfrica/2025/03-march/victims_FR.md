[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# Victimes africaines - Mars 2025

👉🏾 [**English version available here**](./victims.md)

## Synthèse mensuelle

**15 cyberincidents documentés** sous AFRINTEL Taxonomy v2 : Ransomware 9, Data Leak 2, Access Sale 1, Account Takeover 2, System Intrusion 1.

> Les liens de sources sont ajoutés aux incidents complémentaires identifiés via des recherches publiques pour combler le corpus. Ils ne sont pas imposés rétrospectivement aux fiches historiques issues des observations AFRINTEL, notamment Dark Web.

## Mars 2025

### 02 Mars 2025
#### 🇧🇼 Botswana - IT-IQ Botswana
- **Groupe ransomware:** play
- **Secteur:** Conseil en technologies
- **Site web:** www.itiq.co.bw
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** IT-IQ Botswana est l'un des principaux fournisseurs de solutions informatiques et de formations certifiées (Microsoft, Cisco, VMware) au Botswana.

### 02 Mars 2025
#### 🇳🇬 Nigeria - Workforce Group
- **Groupe ransomware:** killsec
- **Secteur:** Éducation / Services RH
- **Site web:** workforcegroup.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** Entreprise nigériane de services éducatifs et de gestion des ressources humaines.
- **Analyse:** AFRINTEL a examiné un échantillon local de documents ainsi qu'un export structuré de données de personnel associés à cette revendication, ainsi qu'une archive téléchargée mais incomplète (un seul volume d'environ 26 Mo appartenant apparemment à une archive fractionnée plus vaste ; AFRINTEL n'a ni extrait ni ouvert son contenu). Le matériel examiné comprend un vaste jeu de données de personnel couvrant identifiants employés, noms, coordonnées, champs démographiques, informations de référents et données de placement chez des employeurs, faisant référence à d'importantes banques nigérianes, cohérent avec le rôle de Workforce Group en tant que prestataire d'externalisation RH et de placement de personnel. L'échantillon comprend également des documents RH à en-tête de Workforce Group (formulaire d'accusé de réception du livret d'accueil, formulaire de demande de congé, lettre d'offre d'emploi avec clause de confidentialité) ainsi que des documents d'intégration liés au secteur financier, dont des formulaires de demande de prêt personnel comportant des numéros BVN (Bank Verification Number), dates de naissance, numéros de téléphone, adresses personnelles et coordonnées de personnes à contacter, ainsi qu'un formulaire de garant émis par une banque commerciale nigériane. Les documents sont cohérents avec l'image de marque de Workforce Group et son rôle d'externalisation auprès de plusieurs institutions financières nigérianes. Compte tenu de l'ampleur du jeu de données de personnel et de la présence de numéros BVN et de données de personnel bancaire couvrant plusieurs grandes banques, l'exposition potentielle dépasse une seule organisation et touche l'écosystème plus large de l'externalisation RH du secteur bancaire nigérian, créant un risque significatif de fraude à l'identité, de prise de contrôle de comptes et d'ingénierie sociale ciblée. AFRINTEL ne reproduit aucun nom, numéro BVN, coordonnée, adresse ni information de compte issus du matériel examiné, et n'a pas vérifié si l'archive disponible représente l'intégralité du jeu de données revendiqué.

### 03 Mars 2025
#### 🇿🇦 Afrique du Sud - LINKGROUP
- **Groupe ransomware:** arcusmedia
- **Secteur:** Conseil en technologies
- **Site web:** linkgroup.co.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** LINKGROUP est une société sud-africaine de conseil en informatique et de services télécoms.

### 03 Mars 2025
#### 🇹🇿 Tanzanie - synaptic.co.tz
- **Groupe ransomware:** arcusmedia
- **Secteur:** Conseil en technologies
- **Site web:** synaptic.co.tz
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Société tanzanienne de conseil en informatique.

### 05 Mars 2025
#### 🇳🇬 Nigeria - Medical Rehabilitation Therapists Board (MRTB)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** MisterSam
- **Secteur:** Administration publique / Régulation de la santé
- **Site web:** Non précisé
- **Statut:** Claim - Unverified
- **Description victime:** Le Medical Rehabilitation Therapists Board of Nigeria (MRTB) est un organisme public nigérian de régulation des professions de la réadaptation médicale.
- **Analyse:** Une publication de forum affirme que des sauvegardes de plusieurs instances CMS associées à l'organisme contiennent des accès à des bases de données et d'autres identifiants pouvant permettre un accès plus large aux serveurs. Le contenu caché, le domaine, les identifiants et un échantillon de base vérifiable ne sont pas exposés dans le matériel disponible. Il s'agit d'une revendication non vérifiée d'exposition de CMS et de sauvegardes ; aucun identifiant ni donnée personnelle n'est reproduit.

### 07 Mars 2025
#### 🇿🇦 Afrique du Sud - ACDC Express
- **Groupe ransomware:** lynx
- **Secteur:** Commerce de détail (Distribution)
- **Site web:** acdcdynamics.co.za
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** ACDC Dynamics est un important fabricant, importateur et distributeur sud-africain de composants électriques, d'outils et d'équipements de sécurité.
- **Analyse:** La fiche de publication du site de fuite Lynx concernant ACDC Express (ACDC Dynamics) classe la publication dans les catégories Encrypted, Proof et AD Dump, et décrit une divulgation unique intitulée « Data » couvrant les RH, des données financières, des contrats et du matériel confidentiel, pour un volume revendiqué de 800 Go. Elle indique une date de publication du 7 mars 2025 et cite un chiffre d'affaires estimé de la victime à 123 000 000 $, une métrique auto-déclarée par l'acteur et non vérifiée de façon indépendante. La description de la victime sur le site de fuite correspond au profil public connu d'ACDC Dynamics (fondée en 1984, distributeur de matériel électrique et électronique basé à Edenvale, Johannesburg, avec des succursales à Germiston, Cape Town, Pinetown et Riverhorse). Le contenu des fichiers référencés par les catégories « Proof » et « AD Dump » n'a pas été examiné et n'est pas reproduit.

### 07 Mars 2025
#### Afrique du Sud - Pam Golding Properties
- **Acteur / Groupe:** Unknown
- **Secteur:** Construction / Real Estate
- **Site web:** https://www.pamgolding.co.za/
- **Date de l'incident:** 7 mars 2025 - date confirmée par la déclaration de l'entreprise
- **Date de publication initiale:** 11 mars 2025
- **Statut:** Victim Confirmed
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Description victime:** Pam Golding Properties est un important groupe immobilier sud-africain disposant d'un vaste portefeuille de clients et de biens.
- **Analyse:** Pam Golding a indiqué que le 7 mars 2025 un tiers inconnu avait obtenu un accès non autorisé à son système de gestion de la relation client au moyen d'un compte utilisateur et avait consulté certaines informations personnelles de clients. L'entreprise a précisé que les coordonnées bancaires, informations financières, informations commerciales et autres documents n'avaient pas été compromis. L'accès a été contenu et des notifications ont été effectuées. La déclaration disponible établit un accès non autorisé réussi et une exposition de données personnelles, mais n'établit pas comment le compte utilisateur a été obtenu ni l'identité de l'acteur.
- **Type de source:** Victim Statement
- **Sources publiques:** [Pam Golding media statement](https://propertyflash.co.za/2025/03/11/media-statement-issued-by-pam-golding-properties-re-a-cyber-incident/)

### 11 Mars 2025
#### 🇪🇬 Égypte - ISEE (International School of Elite Education)
- **Groupe ransomware:** funksec
- **Secteur:** Éducation / Enseignement privé.
- **Site web:** isee-eg.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** International School of Elite Education (ISEE) est un établissement scolaire privé prestigieux situé au Caire.

### 15 Mars 2025
#### Afrique du Sud - Parliament of South Africa
- **Acteur / Groupe:** Unknown
- **Secteur:** Government / Administration
- **Site web:** https://www.parliament.gov.za/
- **Date de l'incident:** 15 mars 2025 - date d'identification et de communication officielle du Parlement; début exact de la compromission non précisé
- **Date de publication initiale:** 15 mars 2025
- **Statut:** Victim Confirmed
- **Type d'incident:** Account Takeover
- **Sous-type:** Compromised YouTube / streaming service
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Type de source:** Official Victim Statement
- **Analyse:** Une ressource YouTube/streaming liée aux canaux officiels du Parlement a été compromise et du contenu non autorisé a été téléversé. L'incident a affecté un service de diffusion et n'établit pas une compromission de l'ensemble du système d'information du Parlement.
- **Sources:** [Parliament of South Africa - communiqué officiel](https://www.parliament.gov.za/press-releases/hacking-incident-parliaments-social-media)

### 16 Mars 2025
#### Afrique du Sud - Astral Foods Limited
- **Acteur / Groupe:** Unknown
- **Secteur:** Agriculture / Agribusiness
- **Site web:** https://www.astralfoods.com/
- **Date de l'incident:** 16 mars 2025 - date confirmée par Astral Foods
- **Date de publication initiale:** 24 mars 2025
- **Statut:** Victim Confirmed
- **Type d'incident:** System Intrusion
- **Sous-type:** Operational disruption - technical vector undisclosed
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Type de source:** Official Company Disclosure
- **Analyse:** Astral Foods a déclaré un incident de cybersécurité le 16 mars 2025 qui a perturbé la transformation de la volaille et les livraisons aux clients, avec un impact estimé sur le bénéfice d'environ 20 millions de rands. L'entreprise a explicitement indiqué qu'aucune information confidentielle ou sensible des parties prenantes n'avait été compromise. AFRINTEL conserve l'incident cyber opérationnel confirmé sans le reclasser en Data Leak ou Ransomware.
- **Sources:** [Astral Foods - annonce SENS officielle](https://www.astralfoods.com/assets/Documents/News/SENS/2025/25.03.24%20Announcement%20-%20Voluntary%20trading%20update.VF.pdf)

### 17 Mars 2025
#### Ghana - Office of the President - John Dramani Mahama X account
- **Acteur / Groupe:** Unknown
- **Secteur:** Government / Administration
- **Site web:** https://x.com/JDMahama
- **Date de l'incident:** 17 mars 2025 - date de signalement reçue par la Cyber Security Authority; début exact de la compromission non établi
- **Date de publication initiale:** 18 mars 2025
- **Statut:** Authority Confirmed
- **Type d'incident:** Account Takeover
- **Sous-type:** Compromised X account / cryptocurrency scam
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Type de source:** National Cyber Authority + Public Media
- **Analyse:** La Cyber Security Authority du Ghana a confirmé que le compte X du président avait été compromis et utilisé pour promouvoir un projet frauduleux de cryptomonnaie appelé "Solana Africa". Le compte a ensuite été restauré. Les éléments n'établissent pas une compromission des réseaux de Jubilee House ni d'autres systèmes gouvernementaux.
- **Sources:** [Ghana News Agency - déclaration de la CSA sur la restauration du compte X présidentiel](https://gna.org.gh/2025/03/president-mahamas-x-account-restored/)

### 25 Mars 2025
#### 🇪🇬 Égypte - MISR AL MAHABA HOSPITAL
- **Groupe ransomware:** nightspire
- **Secteur:** Santé / Secteur Hospitalier
- **Site web:** misralmahaba.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** L'hôpital Misr Al Mahaba est un centre de soins privé important au Caire.
- **Analyse:** La fiche de publication du site de fuite NightSpire concernant l'hôpital Misr Al Mahaba, publiée le 24 mars 2025, annonce un délai/compte à rebours au 27 mars 2025 et un volume revendiqué de 100 Go. Un échantillon local de documents cohérents avec la revendication comprend une carte d'assurance maladie nationale égyptienne et une carte d'identité nationale (chacune montrant une photo de patient et des identifiants partiellement visibles), deux formulaires hospitaliers de transfert externe adressés à l'Autorité générale d'assurance maladie et portant le cachet de l'hôpital, ainsi qu'un relevé de facturation détaillé pour une admission en cathétérisme cardiaque/CCU listant des postes liés au diagnostic, les médicaments administrés individuellement et les montants totaux, tamponné par le service comptabilité de l'hôpital. Les documents sont cohérents avec l'image de marque et le format de facturation de l'hôpital Misr Al Mahaba. L'échantillon indique une exposition de documents identifiant des patients et de dossiers cliniques/de facturation détaillés, créant un risque significatif d'usurpation d'identité médicale, de fraude à l'assurance et de phishing ciblé contre les patients concernés. Aucun nom de patient, numéro de carte d'identité nationale, numéro d'assurance maladie, diagnostic ni montant de facturation n'est reproduit.

### 26 Mars 2025
#### 🇧🇫 Burkina Faso - Tableau de bord gouvernemental COVID-19/vaccination
- **Acteur / Groupe:** Ghudra
- **Secteur:** Santé / Santé publique
- **Site web:** Non précisé
- **Statut:** Claim - Unverified
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Type d'incident:** Access Sale
- **Description :** Une publication propose un accès administrateur à un tableau de bord gouvernemental burkinabè de suivi de la COVID-19 et de la vaccination, pour un prix revendiqué de 300 $.
- **Analyse:** La publication affiche des indicateurs COVID-19, de tests et de vaccinations, et propose un accès administrateur à la vente. Le domaine, la validité, la provenance et le lien avec les revendications Sentap restent inconnus. Il s'agit d'une revendication non vérifiée d'accès à la vente ; aucun identifiant ni donnée personnelle n'est reproduit.

### 30 Mars 2025
#### 🇪🇬 Égypte - INI Investments
- **Groupe ransomware:** nightspire
- **Secteur:** Finance
- **Site web:** iniholdings.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** INI Investments est une société de portefeuille (holding) égyptienne diversifiée. Elle investit dans des secteurs stratégiques tels que l'immobilier, l'énergie, la technologie et les services financiers. L'acteur revendique l'exfiltration de 400 Go de données ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.
- **Note de double revendication :** Les fiches de mars et d’avril sont conservées séparément, car les dates et les éléments de preuve diffèrent. Elles concernent le même acteur, le même domaine et le même nom de victime, mais AFRINTEL ne peut pas déterminer avec les éléments disponibles si la publication d’avril actualise la revendication de mars ou correspond à une revendication distincte. Aucune fusion n’est effectuée dans l’attente d’une confirmation.

### 31 Mars 2025
#### 🇷🇼 Rwanda - moh.gov.rw
- **Groupe ransomware:** babuk2
- **Secteur:** Administrations publiques (Santé)
- **Site web:** moh.gov.rw
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Description victime:** Ministère de la Santé du Rwanda.
- **Analyse:** Un ensemble d'éléments et un échantillon texte brut sont directement associés à cette revendication. L'élément le plus significatif est un webshell PHP actif déployé sur un serveur Linux dont le nom d'hôte est « covid-mass-testing », exécutant PHP 7.4 sous l'utilisateur www-data avec le safe mode désactivé et un répertoire de travail sous /var/www ; le webshell expose des modules gestionnaire de fichiers, console, SQL, exécution PHP et bruteforce, indiquant une capacité d'exécution de code à distance complète plutôt qu'une simple revendication de données. Un panneau d'administration de base de données phpMyAdmin liste 23 tables avec des nombres de lignes approximatifs, incluant des tables cohérentes avec des candidatures (~110 500 lignes), des données de session (~155 400 lignes), des cliniciens (~29 500 lignes), des données RH (~9 400 lignes), des documents (~9 700 lignes) et des enregistrements de mots de passe/authentification (~4 800 lignes), indiquant un accès direct au niveau base de données d'un système de gestion des candidatures/effectifs du secteur de la santé, et non uniquement au site web public du ministère. Un élément supplémentaire, provenant apparemment du même portail de gestion des candidatures ou d'un portail lié, montre des statistiques de tableau de bord de 112 102 candidatures au total, 7 917 postes vacants, 4 165 candidats employés et 107 937 candidats sur liste d'attente, cohérentes avec les nombres de lignes observés dans le panneau de base de données. Un échantillon texte brut local d'environ 25 enregistrements utilisateurs correspondant à un rôle intitulé « Student » est également examiné, chacun contenant un identifiant séquentiel, une adresse email et un hash de mot de passe au format MD5. La combinaison d'un webshell actif et complet, d'un accès administratif direct à la base de données avec des nombres de lignes par table, et d'un échantillon brut d'enregistrements utilisateurs comportant des identifiants soutient une évaluation à confiance très élevée d'une compromission réelle et profonde, dépassant une simple revendication de site web pour atteindre les systèmes de back-end traitant les candidatures du secteur de la santé, les dossiers de cliniciens et les données d'authentification de bien plus de 100 000 individus. Compte tenu de l'ampleur de l'exposition et de la sensibilité des données de cliniciens, RH et d'authentification au sein du secteur de la santé rwandais, l'impact potentiel inclut un risque important de credential stuffing et de prise de contrôle de comptes, du phishing ciblé contre des candidats et agents du secteur de la santé, et une compromission plus large des processus de gestion des effectifs de santé. Aucune adresse email, hash de mot de passe, enregistrement individuel de candidature ni autre donnée personnelle n'est reproduit à partir du matériel examiné.

---
