[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# Liste des victimes africaines de cyberattaques en Novembre 2025 (14 victimes)
👉🏾 [**English version available here**](./victims.md)

## Résumé du mois

Novembre 2025 compte **14 incidents uniques** : **10 Ransomware**, **4 Data Leak**, **0 Access Sale**, **0 DDoS**, **0 Defacement** et **0 Operational Fraud**, dans **6 pays africains**.

> `victims_FR.md` est le fichier éditorial de contrôle. Après validation, `victims.md` est synchronisé avec les mêmes faits, classifications et valeurs structurées.

## Novembre 2025

### 04 Novembre 2025
#### 🇲🇦 Maroc - DOVERN Import
- **Groupe ransomware:** spacebears
- **Secteur:** Logistique
- **Site web:** https://dovern-import.com/
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Société d'importation basée au Maroc, spécialisée dans la distribution de vins fins, spiritueux et champagnes de prestige.

### 04 Novembre 2025
#### 🇿🇦 Afrique du Sud - Wannabees (wannabees.co.za)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Unknown
- **Secteur:** Ressources humaines / Recrutement
- **Site web:** wannabees.co.za
- **Statut:** Claim - Data Sample Published
- **Description victime:** Wannabees semble être une plateforme sud-africaine de recrutement et d'emploi temporaire, d'après la structure et le contenu de la base de candidats examinée.
- **Analyse:** AFRINTEL a examiné deux fichiers identiques dans l'ensemble de preuves fourni (DB.txt et HoJmS, avec une correspondance SHA-256), contenant un export de cinq dossiers de candidats. Le schéma comprend des identifiants de candidats, des numéros d'identité nationale, des noms, adresses, numéros de téléphone, champs d'adresse email, dates de naissance, nationalité, historique d'emploi, profession actuelle, prétentions salariales et champs relatifs à la rémunération, ainsi qu'un champ de mot de passe. L'échantillon est structurellement cohérent avec une base de recrutement ou de gestion de personnel et contient des informations personnelles et professionnelles hautement sensibles. Les fichiers sont datés du 4 novembre 2025 dans le répertoire de preuve ; cette date est traitée comme date de découverte/de preuve et non comme une date confirmée de publication ou d'intrusion. Le matériel disponible n'identifie ni acteur, ni forum, ni méthode d'accès, ni volume complet du jeu de données. AFRINTEL classe donc le cas comme une revendication de fuite avec échantillon publié et ne reproduit aucun nom, numéro d'identité, contact, mot de passe ni autre donnée personnelle brute.
### 05 Novembre 2025
#### 🇨🇮 Côte d'Ivoire - Anka (Anka.africa)
- **Acteur / Groupe:** Spirigatito
- **Secteur:** Logistique
- **Site web:** https://www.anka.africa/
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Description victime:** Plateforme ivoirienne leader facilitant l'exportation, les paiements et la logistique pour les créateurs et commerçants africains vers le marché mondial.
- **Analyse:** La publication sur le forum annonce la vente d'une base de données attribuée à Anka, revendiquant 537 877 utilisateurs uniques et un volume de 12,1 Go, avec une liste de champs annoncée comprenant id, username, fullname, email, token, avatar, gender, date de naissance et téléphone, entre autres. AFRINTEL a examiné des extraits structurés dérivés de l'échantillon publié avec le post, comprenant un petit nombre d'enregistrements utilisateurs individuels (moins de 30). Le schéma examiné correspond à la liste de champs annoncée dans la publication, en l'étendant avec des attributs supplémentaires : date de dernière connexion, indicateurs de verrouillage et de suppression de compte, type de compte, nombre et montant des achats, solde du portefeuille, et champs de ventes vendeur sur la marketplace. Les enregistrements examinés montrent des horodatages de création de compte s'étalant de mai 2017 à mai 2024, des devises incluant l'EUR, l'USD et le GMD, et des paramètres régionaux en français et en anglais, cohérents avec une base d'utilisateurs internationale pour une plateforme africaine de commerce transfrontalier et de paiements. La cohérence structurelle entre la liste de champs annoncée et l'échantillon examiné, ainsi que la plausibilité des valeurs enregistrées (horodatages sur plusieurs années, devises mixtes, paramètres régionaux mixtes), permettent de faire passer ce cas d'une revendication non vérifiée à une revendication accompagnée d'un échantillon de données publié. AFRINTEL n'a pas vérifié indépendamment le volume total revendiqué de 537 877 utilisateurs / 12,1 Go, l'origine ou la méthode de compromission, ni l'affirmation distincte de l'acteur selon laquelle la plateforme génère 10 millions de dollars de revenus. L'exposition de ce jeu de données combinerait noms complets, coordonnées, dates de naissance, genre, jetons de compte et informations de portefeuille/achats, créant un risque significatif de prise de contrôle de comptes, de phishing ciblé et de fraude financière visant les utilisateurs de la plateforme. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone, jeton, nom d'utilisateur ni autre enregistrement individuel issu de l'échantillon examiné.

### 06 Novembre 2025
#### 🇪🇬 Égypte - ELSEWEDYELECTRIC.COM
- **Groupe ransomware:** clop
- **Secteur:** Technologies / Industrie
- **Site web:** www.elsewedyelectric.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 2
- **Description victime:** Principal fabricant égyptien de câbles, de systèmes électriques et de produits d'ingénierie.
- **Analyse:** AFRINTEL a examiné une capture de la page de revendication du site de fuite de Clop pour elsewedyelectric.com, utilisant le modèle standard de fiche victime du groupe (champs Headquarters, Phone, Website, Revenue et Industry, suivis du texte d'avertissement récurrent du groupe). Le profil d'entreprise affiché (chiffre d'affaires d'environ 4,9 milliards de dollars, secteur manufacturing/wire & cable) est cohérent avec le profil public connu d'Elsewedy Electric en tant que grand fabricant égyptien de câbles et de systèmes électriques. Cette fiche apparaissait aux côtés de nombreuses autres organisations multinationales sur la même page du site de fuite de Clop, cohérent avec la campagne d'exploitation de masse du groupe visant les clients d'Oracle E-Business Suite révélée en 2025. La correspondance du profil d'entreprise soutient une évaluation à confiance moyenne quant à l'authenticité de la fiche, bien qu'AFRINTEL n'ait examiné aucun fichier exfiltré sous-jacent, lien magnet ou échantillon de données au-delà de la page de revendication elle-même ; l'ampleur, le volume et la sensibilité des données réellement détenues par l'acteur restent non vérifiés. AFRINTEL ne reproduit ni l'adresse du siège ni le numéro de téléphone de l'entreprise issus du matériel examiné.

### 06 Novembre 2025
#### 🇿🇲 Zambie - ZANACO.CO.ZM
- **Groupe ransomware:** clop
- **Secteur:** Services financiers (Banque)
- **Site web:** www.zanaco.co.zm
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** Zambia National Commercial Bank, l'une des principales banques commerciales de Zambie.
- **Analyse:** AFRINTEL a examiné des captures de la page de revendication du site de fuite de Clop pour zanaco.co.zm, incluant la barre de navigation du groupe montrant cette fiche aux côtés de nombreuses autres organisations multinationales (parmi lesquelles Logitech, The Washington Post, Trimble et Elsewedy Electric), cohérent avec la campagne d'exploitation de masse de Clop visant les clients d'Oracle E-Business Suite révélée en 2025. Le profil d'entreprise affiché (chiffre d'affaires d'environ 337,9 millions de dollars, secteur finance/banking) est cohérent avec le profil public connu de la Zambia National Commercial Bank. La fiche utilise le même modèle standard et le même texte d'avertissement récurrent observés sur d'autres pages victimes de Clop, ce qui soutient une évaluation à confiance moyenne quant à l'authenticité de l'entrée, bien qu'AFRINTEL n'ait examiné aucun fichier exfiltré sous-jacent, lien magnet ou échantillon de données au-delà des pages de revendication ; l'ampleur, le volume et la sensibilité des données clients ou bancaires réellement détenues par l'acteur restent non vérifiés. Compte tenu du rôle de ZANACO en tant que banque commerciale majeure, toute exposition de données confirmée présenterait un risque important de fraude financière et de phishing ciblé visant sa clientèle. AFRINTEL ne reproduit ni l'adresse du siège ni le numéro de téléphone de la banque issus du matériel examiné.

### 06 Novembre 2025
#### 🇲🇦 Maroc - www.marjane.ma
- **Groupe ransomware:** stormous
- **Secteur:** Commerce de détail / Grande distribution / E-commerce.
- **Site web:** www.marjane.ma
- **Statut:** Data Fully Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** Groupe Marjane est le plus grand groupe marocain de grande distribution, exploitant des hypermarchés et supermarchés.
- **Analyse:** AFRINTEL a examiné une capture de preuve publiée en lien avec la revendication du cybercriminel stormous, montrant une session active sur un portail SSL-VPN Fortinet daté du 10 novembre 2025. La liste de favoris du portail référence une infrastructure interne cohérente avec l'environnement de Marjane, incluant un sous-domaine marjane.ma, une instance de wiki Confluence hébergée sous un sous-domaine confluence.marjane, un favori de collaboration intitulé « huddle/Store Managers » cohérent avec la gestion multi-magasins de l'enseigne, ainsi qu'un favori d'accès SSH direct vers un hôte interne. La présence de noms d'hôtes internes spécifiques à Marjane et d'un point d'accès SSH fonctionnel soutient une évaluation à confiance élevée selon laquelle la capture reflète un accès réel au réseau interne plutôt qu'une preuve fabriquée. À la suite de cet échantillon initial, l'acteur aurait publié l'intégralité du jeu de données revendiqué sur son site de fuite ; AFRINTEL n'a pas pu collecter ni examiner cette publication ultérieure, dont le contenu, le volume et l'authenticité ne sont donc pas évalués de manière indépendante. L'accès interne démontré, au niveau VPN et SSH, au réseau du plus grand groupe de grande distribution du Maroc crée un risque dépassant toute catégorie de données isolée, incluant une perturbation potentielle ou une compromission supplémentaire des systèmes de point de vente, de logistique et de gestion des magasins à l'échelle du réseau de succursales de Marjane. AFRINTEL ne reproduit aucun identifiant, jeton de session, adresse IP ni nom d'hôte interne issu du matériel examiné.

### 08 Novembre 2025
#### 🇲🇦 Maroc - NARSA (Agence Nationale de la Sécurité Routière)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** anisanas2
- **Secteur:** Gouvernement / Transport / Sécurité routière
- **Site web:** Non identifié avec certitude
- **Statut:** Claim - Data Sample Published
- **Description victime:** La NARSA est l'agence nationale marocaine chargée de la sécurité routière, de l'immatriculation des véhicules et du contrôle technique.
- **Analyse:** AFRINTEL a examiné un export CSV structuré correspondant à un ensemble d'enregistrements d'immatriculation de véhicules, avec des champs incluant le nom complet du propriétaire, l'adresse, le numéro de carte d'identité nationale (CIN), la marque du véhicule, la catégorie, le type, le numéro de châssis, la cylindrée, les dates du centre d'immatriculation et de mise en circulation, le prix d'achat et le numéro de plaque d'immatriculation. La taille de l'échantillon et la structure des champs sont cohérentes avec le jeu de données revendiqué d'environ 150 000 lignes, bien qu'AFRINTEL n'ait pas pu confirmer de manière indépendante l'identité de l'acteur revendicateur ni l'ampleur totale exacte à partir du matériel examiné. La combinaison de numéros de CIN, d'adresses personnelles et de données d'identification de véhicules crée un risque de fraude à l'identité, de fraude liée aux véhicules (y compris de faux documents d'immatriculation) et de risques pour la sécurité physique liés à l'exposition d'adresses. AFRINTEL ne reproduit aucun nom de propriétaire, adresse, numéro de CIN ni numéro de plaque issus de l'échantillon examiné.


### 09 Novembre 2025
#### 🇿🇦 Afrique du Sud - Eastern Cape Department of Human Settlements (ECDHS)
- **Groupe ransomware:** nightspire
- **Secteur:** Administrations publiques/ Logement social.
- **Site web:** ecdhs.gov.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Le Département des Établissements Humains du Cap Oriental sud-africain est l'organe provincial chargé de la politique du logement, de l'aménagement urbain et de l'accès à la propriété pour les populations vulnérables en Afrique du Sud. 

### 09 Novembre 2025
#### 🇳🇬 Nigeria - Fidelity Pension Managers, Nigeria
- **Groupe ransomware:** nightspire
- **Secteur:** Services financiers (Gestion de pension)
- **Site web:** fidelitypensionmanagers.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Gestionnaire de fonds de pension nigérian.


### 11 Novembre 2025
#### 🇪🇬 Égypte - Samcrete Holding
- **Groupe ransomware:** clop
- **Secteur:** Construction
- **Site web:** www.samcrete.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Samcrete Holding est une société entièrement intégrée d'ingénierie, de sous-traitance, de développement, de fabrication et d'investissement créée en 1963.

### 25 Novembre 2025
#### 🇪🇬 Égypte - LAMAICA, Egypt 
- **Groupe ransomware:** nightspire
- **Secteur:** Industrie manufacturière du bois et des matériaux de construction.
- **Site web:** lamaica.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** LAMAICA est l'un des leaders du marché égyptien dans la production de panneaux de particules mélaminés, de stratifiés haute pression (HPL), de bandes de chant et de composants pour l'ameublement.

### 26 Novembre 2025
#### 🇪🇬 Égypte - Arabia Holding
- **Groupe ransomware:** qilin
- **Secteur:** Immobilier / Investissement / Développement Urbain.
- **Site web:** arabia-holding.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Holding égyptienne avec des intérêts dans divers secteurs, dont l'immobilier et la gestion.

### 26 Novembre 2025
#### 🇨🇮 Côte d'Ivoire - Santé Espoir Vie Côte d’Ivoire (SEV-CI)
- **Groupe ransomware:** benzona
- **Secteur:** Santé / ONG / Humanitaire.
- **Site web:** sevci.org
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Santé Espoir Vie Côte d’Ivoire (SEV-CI) est une organisation non gouvernementale ivoirienne de premier plan. Elle œuvre pour l'amélioration de la santé des populations, avec un focus particulier sur la lutte contre le VIH/SIDA, la tuberculose, et le renforcement des systèmes de santé communautaires.

### 30 Novembre 2025
#### 🇲🇦 Maroc - Joutech
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** RL000
- **Secteur:** Technologie / Services numériques (activité exacte non confirmée de manière indépendante)
- **Site web:** joutech.ma
- **Statut:** Claim - Data Sample Published
- **Description victime:** Joutech est une entreprise marocaine exploitant le domaine joutech.ma. Le fichier examiné est un export de liste de diffusion/contacts de 1 350 enregistrements, contenant civilité, prénom, nom, adresse email, champ société, indicateurs marketing/ventes et date d'inscription. Aucun mot de passe ni donnée financière n'a été observé dans l'échantillon examiné. Cette exposition pourrait faciliter des campagnes de phishing ciblé et de spam contre les contacts listés ; l'exhaustivité et l'origine du fichier n'ont pas été confirmées de manière indépendante.
