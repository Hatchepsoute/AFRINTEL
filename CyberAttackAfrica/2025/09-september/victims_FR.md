[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# Liste des victimes africaines de cyberattaques en Septembre 2025 (18 victimes)
👉🏾 [**English version available here**](./victims.md)
## Septembre 2025

### 02 Septembre 2025
#### 🇩🇿 Algérie - Université des Frères Mentouri Constantine 1 (UMC1)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Fire Wire
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** university-dz.net
- **Statut :** Claim - Data Sample Published
- **Description victime :** L'Université des Frères Mentouri Constantine 1 (UMC1) est une grande université publique algérienne. L'acteur revendicateur affirme une exfiltration de plus de 10 Go, un volume qu'AFRINTEL n'a pas collecté ni analysé. Les fichiers examinés, exfiltrés via ce qui semble être une plateforme web académique partagée (university-dz.net), comprennent les plannings d'examens du Master 2 semestre 1 (janvier 2025) avec dates, modules, salles et départements ; un ensemble de plus de 200 dossiers étudiants détaillés (nom complet, numéro d'inscription universitaire, groupe TD et notes par matière, avec annotations de statut telles qu'exclusion/admission) d'étudiants de L1 (promotion 2015-2016) ; un annuaire de conformité véhicules avec numéros de téléphone et emails ; et un modèle de conférence listant des contacts et affiliations pour un événement académique 2024 (NCME). La combinaison de dossiers académiques, de coordonnées personnelles et de documents administratifs crée un risque significatif de fraude à l'identité, de phishing ciblé et de vishing contre les étudiants, le personnel et les contacts affiliés. L'acteur revendicateur s'identifie sous le nom « Fire Wire ».

### 04 Septembre 2025
#### 🇳🇬 Nigeria - MobileSub
- **Acteur / Groupe :** Non précisé
- **Secteur :** Fintech / Services de paiement
- **Site web :** [mobilesub.com.ng](https://mobilesub.com.ng)
- **Date du fichier source :** 4 septembre 2025
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** MobileSub est une plateforme nigériane de services numériques fournissant des fonctions d'achat de crédit mobile, de données, d'électricité, de télévision par câble, de paris et de paiement associées.
- **Analyse :** AFRINTEL a examiné un dump SQL local d'environ 14,3 Mo contenant 42 tables et 306 blocs INSERT. Le schéma comprend des comptes utilisateurs, la KYC, des clés API, l'historique des transactions, les transferts, l'airtime, les données mobiles, l'électricité, les inscriptions aux examens, les paris, la télévision par câble et d'autres modules de paiement, ainsi que des tables de sauvegarde d'utilisateurs. L'horodatage du fichier source est le 4 septembre 2025 ; il est traité comme un horodatage de découverte/source AFRINTEL, et non comme la date prouvée de la compromission initiale. Le jeu de données peut exposer des informations d'identité, de contact, de KYC, de transaction et d'authentification. Aucune valeur personnelle, clé API ou identifiant n'est reproduit. L'authenticité, l'exhaustivité et le contexte de publication restent non vérifiés.
- **Note d'analyse source :** Le dump contient des catégories de tables sensibles aux identifiants et aux secrets ; AFRINTEL n'a tenté aucune authentification, aucun accès ni récupération de secret.

### 05 Septembre 2025
#### 🇪🇬 Égypte - MeamarGroup
- **Groupe ransomware:** obscura
- **Secteur:** Immobilier / Construction / Ingénierie.
- **Site web:** https://meamargroup.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 3
- **Description victime:** MeamarGroup (incluant Meamar Real Estate Development et Meamar Construction) est un acteur majeur du secteur de la construction en Égypte depuis plus de 25 ans. Basé au Caire (New Cairo), le groupe gère plus de 400 projets allant des complexes résidentiels de luxe aux installations industrielles et médicales (comme l'usine Biogeneric Pharma).
- **Analyse :** AFRINTEL a examiné une archive locale côté serveur (491 fichiers et dossiers, tous appartenant au compte du serveur web www-data) cohérente avec cette revendication. Les horodatages de dossiers de cette collecte se regroupent autour du 05 septembre 2025, correspondant à la date de revendication de cette fiche, tandis que la majorité des fichiers sous-jacents porte un horodatage antérieur du 27 août 2025, suggérant une étape initiale de préparation des données avant la revendication publique. Voir l'analyse complète sous la fiche du 13 octobre 2025 (« meamargroup.com (troisième attaque) »), qui documente en détail la même archive, incluant des grands livres comptables internes, une importante archive de centre d'appels commercial/contacts prospects, des CV d'employés, et des copies de fichiers portant l'extension de chiffrement ransomware « .obscura ». AFRINTEL considère ces éléments comme des enregistrements liés à la même compromission sous-jacente plutôt que comme des incidents indépendants. AFRINTEL ne reproduit aucun nom de client, numéro de contact, nom d'employé ni montant financier issu du matériel examiné.

### 06 Septembre 2025
#### 🇨🇮 Côte d'Ivoire - NSIA Assurances
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Tanaka
- **Secteur:** Assurances / Services Financiers.
- **Site web:** https://www.nsiaassurances.com
- **Statut:** Claim - Unverified
- **Description victime:** Leader de l'assurance et de la banque en Afrique de l'Ouest et Centrale, acteur systémique basé à Abidjan en Côte d'Ivoire. L'acteur affirme faire circuler une base de données de plus de 2,5 millions d'enregistrements transactionnels et financiers ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 08 Septembre 2025
#### 🇳🇬 Nigeria - The Promise Nigeria
- **Groupe ransomware:** yurei
- **Secteur:** Restauration / Services alimentaires / Traiteur.
- **Site web:** https://www.thepromisenig.com
- **Statut:** Claim - Unverified
- **Description victime:** The Promise est une chaîne de restauration rapide (QSR) et un service de traiteur industriel de premier plan au Nigeria, particulièrement implantée à Port Harcourt et dans la région du Delta du Niger.

### 09 Septembre 2025
#### 🇲🇦 Maroc - Dolidol
- **Groupe ransomware:** TheGentlemen
- **Secteur:** Industrie Manufacturière / Literie / Ameublement.
- **Site web:** https://www.dolidol.ma
- **Statut:** Claim - Unverified
- **Description victime:** Dolidol (filiale du groupe Palmeraie Industries et Services) est le leader incontesté de la literie et de la mousse polyuréthane au Maroc.

### 09 Septembre 2025
#### 🇿🇼 Zimbabwe - Proplastics Limited
- **Groupe ransomware:** TheGentlemen
- **Secteur:** Industrie manufacturière (Plastiques)
- **Site web:** https://www.proplastics.co.zw
- **Statut:** Claim - Unverified
- **Description victime:** Proplastics Limited est le principal fabricant et fournisseur de systèmes de tuyauterie en plastique (PVC, PEHD) au Zimbabwe.
- **Analyse :** Le jeu local fourni contient 63 fichiers associés à Proplastics, notamment des PDF, des tableurs, des fichiers image et des fichiers texte. Les noms de fichiers indiquent des documents métier relatifs aux factures et notes de crédit, soldes de comptes, nomenclatures, reliquats de commandes, livraisons, analyses de ventes et rapports par agence. Les fichiers portent des dates couvrant 2023-2024, tandis que les métadonnées du répertoire situent la collecte en septembre 2025 ; ces dates sont considérées comme contexte de preuve et non comme date confirmée d intrusion ou de publication. Le matériel soutient la plausibilité et la sensibilité potentielle de la revendication de septembre 2025, mais ne permet pas d établir indépendamment le vecteur d accès, le périmètre complet des données ni l attribution à TheGentlemen. AFRINTEL ne reproduit aucun nom, détail de compte, montant financier, enregistrement client ou contenu documentaire.

### 10 Septembre 2025
#### 🇳🇬 Nigeria - Princeps Credit Systems Limited
- **Groupe ransomware:** killsec
- **Secteur:** Finance
- **Site web:** https://princepsfinance.com
- **Statut:** Claim - Unverified
- **Description victime:** Institution financière basée à Lagos, spécialisée dans le crédit à la consommation et le financement des PME.

### 11 Septembre 2025
#### 🇳🇦 Namibie - Epia Financial Services
- **Groupe ransomware:** radar
- **Secteur:** Services financiers
- **Site web:** https://epiafs.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Description victime:** Institution financière basée à Windhoek, offrant des services de gestion de patrimoine, de conseil en investissement et de courtage en Namibie.
- **Analyse:** Des éléments de messagerie exfiltrés rattachés à la revendication (correspondance envoyée depuis et vers les boîtes de réception et d'administration d'EPIA avec Bank Windhoek/Capricorn Group, First National Bank of Namibia et NamPost, relative à des vérifications de comptes clients) sont examinés, ainsi que la structure d'un échantillon représentatif de fichiers d'administration de fonds de pension au niveau des champs/colonnes, sans ouvrir ni extraire de ligne individuelle d'adhérent. Les éléments examinés correspondent au rôle d'EPIA en tant qu'administrateur du Namibia Building Workers Pension Fund (NBWPF) et d'autres clients institutionnels. Les classeurs de données d'adhérents (par exemple un extrait de janvier 2025) contiennent plusieurs feuilles de plusieurs milliers d'enregistrements chacune (Actives, Deferred, Unclaimed, Exits) partageant un schéma de champs cohérent : numéro de membre, nom, prénom, autres prénoms, référence entreprise, date de naissance, numéro d'identité nationale, numéro de passeport, statut cotisant, statut du membre, nom de l'employeur, genre, dates d'emploi et d'adhésion au fonds, salaire mensuel et annuel, montant et date du solde du fonds (fund credit), date de dernière cotisation, date de sortie et détails de paiement. Un extrait de données actuarielles distinct couvre la période de septembre 2022 à avril 2024 avec un schéma et une ampleur comparables. D'autres fichiers inspectés structurellement incluent des rapports d'administration et d'allocation de revenus pluriannuels (résumés agrégés de transactions financières par période) et des formulaires d'autorisation client signés, le plus récent daté de juin 2025. AFRINTEL n'a pas ouvert chaque fichier de l'ensemble ; la cohérence des noms de fichiers et la correspondance par e-mail indiquent que les mêmes catégories d'enregistrements se répètent sur toute la période 2022-2025. La combinaison de numéros d'identification nationale, de dates de naissance, de données salariales et de solde de fonds de pension pour plusieurs milliers d'individus, avec la correspondance employeur et bancaire, représente une exposition à fort impact. L'étendue, la continuité jusqu'à mi-2025 et la spécificité organisationnelle des éléments examinés soutiennent un niveau de confiance élevé quant à la compromission de la messagerie et des fichiers, indépendamment de la revendication publique du groupe ransomware. L'ensemble local contient 73 fichiers pour environ 79,8 Mo, comprenant des tableurs, des rapports, des présentations, un fichier DOCX d'employeur et des fichiers image. Le classeur d'adhérents de janvier 2025 contient une feuille de synthèse et des feuilles d'état des membres (Actives, Deferred, Unclaimed et Exits), avec une feuille de synthèse allant jusqu'à 8 652 lignes et des feuilles allant jusqu'à 35 colonnes ; la structure examinée comprend des champs relatifs aux membres, employeurs, identités, emplois, salaires, crédits de pension, cotisations, sorties et paiements. L'extrait actuariel contient 8 168 lignes et 167 colonnes pour une période allant de septembre 2022 à avril 2024. Les éléments horodatés du 11 septembre 2025 sont cohérents avec le contexte de découverte de septembre. Aucun nom d'adhérent, numéro d'identification, coordonnée bancaire, signature, montant de salaire ni contenu de correspondance n'est reproduit à partir de l'échantillon examiné.


### 11 Septembre 2025
#### 🇦🇴 Angola - Base de données des employés du gouvernement angolais (pape.gov.ao)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** privilege, publication sur un forum cybercriminel
- **Secteur :** Gouvernement / Administration publique
- **Site web :** [pape.gov.ao](https://pape.gov.ao)
- **Statut :** Claim - Data Sample Published
- **Description victime :** La source présente pape.gov.ao comme une plateforme liée au gouvernement angolais et affirme proposer des dossiers d'employés de différents secteurs et domaines administratifs.
- **Analyse :** La publication du 11 septembre 2025 revendique une base de données de 245 employés du gouvernement angolais et énumère des champs relatifs aux identifiants d'employés, noms, dates de naissance, zones administratives et fonctions. Le fichier TXT local fourni pour examen contient 244 lignes non vides séparées par des virgules, dont une ligne d'en-tête et environ 243 lignes de données, avec six champs par ligne. Cela confirme l'existence d'un échantillon structuré de données d'employés, mais ne permet pas de confirmer indépendamment le total annoncé, l'organisme gouvernemental exact, l'authenticité ou l'exhaustivité du jeu de données. AFRINTEL ne reproduit aucun nom, identifiant, date de naissance ni autre donnée personnelle issue du fichier.
### 12 Septembre 2025
#### 🇨🇩 Congo (RDC) - Fonds pour la Réforme de l'Administration Publique (FRAP)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** privilege
- **Secteur :** Gouvernement / Administration
- **Site web :** [frap.cd](https://frap.cd/)
- **Statut :** Data Fully Published
- **Description victime :** Organisme en charge de la modernisation de l'administration en RDC.
- **Analyse :** AFRINTEL a examiné le post DarkForums lui-même, publié le 12 septembre 2025 par le cybercriminel privilege (statut VIP, compte créé en septembre 2025), intitulé « FRAP.CD — 1,136 LINES | Full User Data | Gov/Staff Access ». Le post décrit une base de données de 1 136 enregistrements comprenant des identifiants de connexion et des mots de passe hachés (plusieurs formats de hachage), des identifiants personnels (nom, prénom, sexe), des coordonnées (email, téléphone) lorsque disponibles, des champs de référence et de désignation de documents internes, ainsi que des métadonnées système (date de création, dernière connexion, dernière mise à jour du mot de passe, créé/modifié par, statut du compte). L'acteur décrit ces données comme couvrant des comptes d'administrateurs et de personnel sectoriel du portail FRAP.CD, ce qui est cohérent avec le rôle de la plateforme dans la gestion des profils administratifs et des comptes internes du personnel du Fonds pour la Réforme de l'Administration Publique. L'ensemble complet des données est proposé via un lien d'hébergement externe et n'est pas montré directement dans le post ; AFRINTEL n'a pas pu valider de façon indépendante l'authenticité ni l'exhaustivité du fichier hébergé. Compte tenu des identifiants de connexion et des données personnelles décrits, l'exposition de ce matériel créerait un risque d'accès au portail par réutilisation d'identifiants et de phishing ciblé contre le personnel de l'administration publique congolaise. AFRINTEL ne reproduit aucun identifiant, mot de passe, donnée personnelle ni coordonnée issu du post examiné.

### 14 Septembre 2025
#### 🇰🇪 Kenya - Office Of The Registrar Of Political Parties
- **Groupe ransomware:** qilin
- **Secteur:** Administrations publiques
- **Site web:** https://www.orpp.go.ke
- **Statut:** Claim - Unverified
- **Description victime:** Organisme d'État kenyan chargé de l'enregistrement, de la régulation et de la supervision du financement des partis politiques.

### 16 Septembre 2025
#### 🇰🇪 Kenya - Jubilee Life Insurance
- **Groupe ransomware:** warlock
- **Secteur:** Assurances / Services financiers
- **Site web:** https://jubileelife.com
- **Statut:** Claim - Unverified
- **Description victime:** Acteur majeur de l'assurance-vie et de la gestion de fonds au Kenya, filiale de Jubilee Holdings Limited.

### 17 Septembre 2025
#### 🇪🇬 Égypte - Accflex ERP
- **Groupe ransomware:** arcusmedia
- **Secteur:** Technologies / Édition de logiciels ERP.
- **Site web:** https://www.accflex.com
- **Statut:** Claim - Unverified
- **Description victime:** Éditeur égyptien de solutions de gestion intégrées (comptabilité, RH, production) utilisé par de nombreuses entreprises au Moyen-Orient et en Afrique.

### 22 Septembre 2025
#### 🇲🇦 Maroc - Fractalite (fractalite.com)
- **Groupe ransomware:** killsec
- **Secteur:** Technologies/ Services Numériques / Développement Logiciel.
- **Site web:** https://fractalite.com
- **Statut:** Claim - Unverified
- **Description victime:** Fractalite est une agence de conseil et d'ingénierie numérique marocaine, spécialisée dans le développement de solutions logicielles et l'accompagnement digital des entreprises. 


### 24 Septembre 2025
#### 🇳🇬 Nigeria - Kolomoni Microfinance Bank
- **Acteur / Groupe :** Non précisé
- **Secteur :** Microfinance / Banque
- **Site web :** [kolomonimfb.com](https://kolomonimfb.com)
- **Date de l'archive source :** 24 septembre 2025
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** Kolomoni Microfinance Bank est une institution financière nigériane qui fournit des services de microfinance et de banque numérique à ses titulaires de comptes.
- **Analyse :** AFRINTEL a examiné l'extraction RAR fournie et son fichier CSV Kolomoni. Le fichier contient 37 825 lignes et 12 colonnes couvrant le nom et le numéro de compte, l'email, le téléphone, le genre, la date de naissance, le statut du compte, l'adresse, la zone de gouvernement local, l'État, la dernière connexion et la date de l'enregistrement. La combinaison d'identifiants financiers, de coordonnées, de données démographiques, de localisation et de métadonnées de connexion crée des risques de phishing, de prise de contrôle de comptes, de fraude à l'identité et d'escroqueries financières ciblées. L'horodatage de l'archive est le 24 septembre 2025, tandis que les métadonnées internes du CSV contiennent une date de fichier antérieure au 24 août 2025 ; aucune de ces dates ne prouve la date de compromission initiale. Aucune valeur personnelle n'est reproduite. L'acteur, le forum de publication, l'authenticité et l'exhaustivité restent non précisés ou non vérifiés.

### 29 Septembre 2025
#### 🇸🇳 Sénégal - Direction Générale des Impôts et des Domaines (DGID)
- **Groupe ransomware:** BlackShrantac
- **Secteur:** Administration Publique / Finances / Fiscalité.
- **Site web:** https://www.impots.gouv.sn
- **Statut:** Claim - Unverified
- **Description victime:** La **DGID** est l'organe central du Ministère des Finances du Sénégal, responsable de la collecte des impôts, de la gestion du domaine national et du cadastre. Le groupe ransomware affirme avoir divulgué 1 téraoctet (1 To) de données sensibles, comprenant des bases de données fiscales structurées, des registres fonciers et des informations bancaires de contribuables ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 30 Septembre 2025
#### 🇪🇬 Égypte - Telecom Egypt (TE Data)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** KILLUAX
- **Secteur :** Télécommunications
- **Site web :** te.eg
- **Statut :** Claim - Data Sample Published
- **Description victime :** Telecom Egypt exploite le service d'accès internet TE Data. L'échantillon examiné contient des enregistrements de type comptabilité RADIUS (identifiants abonnés au format tedata.net.eg, adresses IP de NAS, adresses MAC, adresses IP attribuées, horodatages de début/fin de session et type de connexion). Seul un nombre restreint d'enregistrements (36) était disponible pour analyse, ce qui limite l'évaluation de l'ampleur totale ; l'exposition pourrait néanmoins faciliter l'identification d'abonnés et la reconnaissance réseau.

## ✍🏿 Auteur
*Adama ASSIONGBON*  
*Consultant SOC & Cyber Threat Intelligence*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)
