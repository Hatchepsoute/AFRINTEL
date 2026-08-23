[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# Liste des victimes africaines de cyberattaques en Août 2025 (13 victimes)
👉🏾 [**English version available here**](./victims.md)

## Résumé du mois

Août 2025 compte **13 incidents uniques** : **7 Ransomware**, **5 Data Leak**, **1 Access Sale**, **0 DDoS**, **0 Defacement** et **0 Operational Fraud**, dans **10 pays africains**.

> `victims_FR.md` est le fichier éditorial de contrôle. Après validation, `victims.md` est synchronisé avec les mêmes faits, classifications et valeurs structurées.

## Août 2025

### 06 Août 2025
#### 🇹🇳 Tunisie - Yasat (yasat.tn)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** RainbowDF
- **Secteur:** Technologies / Distribution Multimédia.
- **Site web:** yasat.tn
- **Statut:** Claim - Data Sample Published
- **Description victime:** Plateforme tunisienne de vente en gros de services multimédia et d'abonnements numériques, servant de fournisseur à de nombreux propriétaires de magasins et revendeurs locaux.
- **Analyse:** AFRINTEL a examiné les données structurées correspondant à la revendication de l'acteur, issues d'exports de la base de données de production de la plateforme d'abonnements IPTV/satellite en gros de Yasat, incluant des produits sous la marque beIN Sports et des offres IPTV génériques avec des champs de liens de flux M3U. Les tables examinées comprennent 52 733 lignes de facturation (produits, quantités, prix, remises, taxes, montants payés/dus), 46 522 enregistrements de ventes générales incluant numéros de mobile, adresses email et liens de flux IPTV (M3U) des clients, 8 623 enregistrements de ventes spécifiques beIN avec des champs de contact client similaires, 211 profils clients (nom, prénom, société, adresse, téléphone, genre, date de naissance) et une table de 22 comptes utilisateurs contenant un champ mot de passe. L'ensemble des données indique des dizaines de milliers d'enregistrements clients et transactionnels exposés, créant un risque significatif de fraude aux abonnements, de réutilisation d'identifiants et de phishing ciblé contre la base de revendeurs et de clients de Yasat. AFRINTEL ne reproduit aucun nom de client, coordonnée, lien de flux ni identifiant issus de l'échantillon examiné.

### 06 Août 2025
#### 🇰🇪 Kenya - KenGen
- **Groupe ransomware:** qilin
- **Secteur:** Énergie / Infrastructures Critiques (Production d'Électricité).
- **Site web:** www.kengen.co.ke
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** Kenya Electricity Generating Company PLC (KenGen) est le principal producteur d'électricité du Kenya, fournissant environ 70 % de l'énergie consommée dans le pays.
- **Analyse:** AFRINTEL a examiné un ensemble de documents locaux associés à cette revendication. L'échantillon comprend des documents internes de gestion contractuelle de KenGen relatifs à un projet de construction d'un centre de formation géothermique (une note de l'équipe de mise en œuvre du contrat, un bon de commande officiel et une lettre de garantie bancaire de bonne exécution émise par une banque commerciale), un budget CAPEX détaillé pour la division Geothermal Development, un registre financier de type paie, un tableau d'effectifs du département Geothermal Development listant identifiants employés, noms, genre, intitulés de poste et niveaux de grade, une déclaration de confidentialité d'appel d'offres signée liée à un marché informatique interne, un courrier officiel du ministère kényan de l'Énergie et du Pétrole adressé aux directeurs généraux de KenGen et d'autres entités du secteur énergétique national concernant un cadre de renforcement des ressources humaines et de recherche-développement, ainsi qu'un plan technique d'un local auxiliaire/tableau électrique d'une installation. Les documents présentent un en-tête, des cachets, des signatures et des numéros de contrat cohérents et croisés entre des fichiers de structure indépendante, ce qui renforce la confiance quant à une origine interne aux systèmes de KenGen. L'ensemble combine des données personnelles d'employés, des documents financiers et de passation de marchés internes, de la documentation technique et des correspondances avec des institutions du secteur énergétique national, indiquant une exposition touchant plusieurs systèmes internes plutôt qu'une seule application. AFRINTEL ne reproduit aucun nom d'employé, identifiant, signature ni valeur monétaire issus de l'échantillon, et ne confirme pas l'intrusion de façon indépendante.

### 06 Août 2025
#### 🇲🇦 Maroc - New Era Com
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Chucky_BF
- **Secteur:** Télécoms / Infrastructures / Services IT.
- **Site web:** neweracom.ma
- **Statut:** Data Fully Published
- **Description victime:** Société marocaine spécialisée dans l'ingénierie des télécoms, l'installation d'infrastructures réseaux et les solutions ERP/CRM. L'acteur a publié un dump SQL de 607 Mo contenant plus de 476 000 enregistrements.

### 09 Août 2025
#### 🇳🇬 Nigeria - Zenith Bank Plc
- **Acteur / Groupe:** KaruHunters
- **Secteur:** Banque / Services Financiers.
- **Site web:** zenithbank.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** L'une des plus grandes institutions financières du Nigeria et d'Afrique anglophone, cotée à la Bourse du Nigeria et à celle de Londres. L'acteur revendique l'exfiltration et la mise en vente de plus de 1,8 million de dossiers clients, ainsi que des données d'employés. AFRINTEL a examiné un échantillon CSV local de 18 lignes et huit colonnes couvrant un index, un code, un identifiant, un nom, un montant, une adresse, un téléphone et une adresse email. Aucune valeur brute n'est reproduite.
- **Note de corrélation:** La même organisation et le même domaine ont été listés de nouveau le 26 juillet 2026 par ExfilSquad dans une revendication ransomware. Cela établit une corrélation d’identité et de temporalité, mais pas une connexion confirmée entre les deux événements. L’entrée de 2025 concerne une mise en vente alléguée de 1,8 million de dossiers avec un échantillon de 18 lignes examiné ; l’entrée de 2026 ne fournit ni échantillon, ni volume, ni preuve de chiffrement, ni confirmation de la victime. Aucun archivage correspondant, schéma de données, infrastructure partagée ou lien explicite ne relie les deux revendications. AFRINTEL les suit donc comme des entrées liées / revendications possiblement distinctes, avec une relation non résolue.

### 11 Août 2025
#### 🇿🇦 Afrique du Sud - Body Graphics Tattoo Supply
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** N1KA
- **Secteur:** Commerce de détail / E-commerce.
- **Site web:** bodygraphicstattoosupply.co.za
- **Date de publication de la source:** 11 août 2025
- **Statut:** Data Fully Published
- **Description victime:** Détaillant en ligne majeur basé à Johannesburg, spécialisé dans la fourniture de matériel de tatouage professionnel et de produits de soin en Afrique du Sud.
- **Analyse:** AFRINTEL a examiné deux fichiers d'export structurés référencés dans une publication observée sur DarkForums, totalisant 6 501 enregistrements, soit un volume cohérent avec celui revendiqué par l'acteur. Le jeu de données correspond à un export de clients et d'administrateurs WordPress/WooCommerce, incluant identifiants de connexion, adresses email, mots de passe hachés (format phpass), adresses postales, numéros de téléphone, adresses IP, chaînes d'user-agent et jetons de session. La cohérence structurelle entre le volume revendiqué et les fichiers examinés, ainsi que la correspondance des champs avec la plateforme e-commerce de la victime, justifie un niveau de confiance élevé, et la publication identifie le compte source N1KA. AFRINTEL ne reproduit aucun nom de client, coordonnée, adresse ni identifiant issu de l'échantillon examiné.

### 13 Août 2025
#### 🇩🇿 Algérie - Cevital
- **Groupe ransomware:** akira
- **Secteur:** Agroalimentaire/ Industrie / Logistique
- **Site web:** www.cevital.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Leader de l'industrie agroalimentaire en Algérie, actif dans l'électronique, l'acier, le verre et la distribution.

### 17 Août 2025
#### 🇿🇦 Afrique du Sud - SYSPRO
- **Groupe ransomware:** warlock
- **Secteur:** Technologies (Éditeur de logiciels)
- **Site web:** syspro.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** SYSPRO est un éditeur de logiciels ERP (Enterprise Resource Planning) sud-africain, fournissant des solutions de gestion intégrées pour les entreprises de fabrication et de distribution.

### 18 Août 2025
#### 🇺🇬 Ouganda - Uganda Electricity Transmission Company Limited
- **Groupe ransomware:** qilin
- **Secteur:** Énergie (Électricité)
- **Site web:** https://www.uetcl.go.ug / www.uetcl.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Société publique ougandaise responsable du transport de l'électricité.

### 18 Août 2025
#### 🇹🇳 Tunisie - International Freight & Commerce
- **Groupe ransomware:** direwolf
- **Secteur:** Logistique
- **Site web:** ifc-tunisie.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Entreprise tunisienne qui assure des services de transport maritime, aérien et terrestre, ainsi que la gestion logistique et les formalités douanières pour des entreprises importatrices et exportatrices.

### 20 Août 2025
#### 🇿🇦 Afrique du Sud - Netstar South Africa (deuxième attaque)
- **Groupe ransomware:** incransom
- **Secteur:** Technologie / Télématique / Sécurité IoT
- **Site web:** www.netstar.co.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Netstar, une filiale du groupe Altron, est le pionnier de l'industrie du suivi et de la récupération de véhicules volés (SVR) en Afrique du Sud.
- **Analyse:** AFRINTEL avait déjà enregistré une revendication contre cette même entreprise par devman le 23 mai 2025. Cette seconde revendication, publiée environ trois mois plus tard par un acteur différent, pourrait refléter soit une intrusion distincte réelle, soit une republication/revente de la revendication précédente ; AFRINTEL n'a pas pu confirmer de manière indépendante quel scénario s'applique.

### 23 Août 2025
#### 🇪🇬 Égypte - TEAM4 Security
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** GhostCrawl
- **Secteur:** Services de Sécurité / Défense / Ressources Humaines.
- **Site web:** team4security.com 
- **Statut:** Claim - Data Sample Published
- **Description victime:** Société égyptienne spécialisée dans les services de sécurité privée, la protection d'infrastructures et le conseil en gestion des risques. TEAM4 Security est une société de sécurité multidimensionnelle fondée en 2017, opérant depuis le Royaume-Uni et l'Égypte, proposant des solutions intégrées de sécurité numérique et physique, de gardiennage humain et de systèmes K-9 professionnels, ciblant les infrastructures critiques, les villes sûres, ainsi que les clients gouvernementaux et du secteur de la défense.
- **Analyse:** AFRINTEL a examiné les lots de fuite publiés par l'acteur GhostCrawl sur DarkForums ; les horodatages propres au fil de discussion s'échelonnent du 29 au 31 août 2025 (la partie 1 a été publiée le 29 août 2025 à 23h55), soit légèrement après la date de détection du 23 août retenue dans ce fichier. Le matériel correspond à une boîte de messagerie administrative/support exfiltrée (contacts, emails reçus et envoyés au format .eml/.mbox), accompagnée de plusieurs centaines de documents bureautiques et d'images en pièces jointes répartis sur les cinq lots. Les échantillons examinés incluent des feuilles de paie mensuelles du personnel de sécurité sur plusieurs périodes de paie 2025 (agents, superviseurs et personnel de l'unité K-9), un tableau RH/paie détaillé listant numéro d'employé, nom complet, numéro de carte d'identité nationale, poste, date de naissance, date d'embauche, assurance sociale, salaire fixe et variable et primes pour plus de vingt employés, des mémorandums d'incidents internes (dont un rapport d'enquête pour vol daté du 3 novembre 2024), des formulaires mensuels d'effectifs et d'évaluation du personnel, un annuaire téléphonique interne des postes, ainsi que des documents individuels de dossiers employés, accompagnés du papier à en-tête officiel confirmant les adresses du siège égyptien et des agences de TEAM4 Security. La combinaison de numéros de carte d'identité nationale, de dates de naissance, de dates d'embauche et de données salariales du personnel de sécurité crée un risque significatif de fraude à l'identité et d'ingénierie sociale ciblée contre le personnel, tandis que les dossiers d'incidents internes et d'opérations sur site pourraient exposer des informations relatives aux sites clients protégés. AFRINTEL ne reproduit aucun nom d'employé, numéro de carte d'identité nationale, montant de salaire ni autre donnée personnelle issue de l'échantillon examiné.

### 25 Août 2025
#### 🇲🇺 Maurice - SWAN Mauritius
- **Groupe ransomware:** qilin
- **Secteur:** Assurances / Services Financiers.
- **Site web:** www.swan.mu / swanforlife.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** SWAN (Swan General Ltd et Swan Life Ltd) est le leader du marché des assurances et des services financiers à l'Île Maurice.

### 25 Août 2025
#### 🇹🇬 Togo - Infrastructures Gouvernementales
- **Type d'incident:** Access Sale
- **Acteur / Groupe:** BIGBROTHER
- **Secteur:** Gouvernement / Infrastructures Critiques.
- **Site web:** gouv.tg
- **Statut:** Claim - Data Sample Published
- **Description victime:** Portail officiel et infrastructures numériques de la République Togolaise, hébergeant les services administratifs et les données étatiques.
- **Analyse:** Des éléments corroborent la revendication de l'acteur, incluant le post DarkForums lui-même ainsi que plusieurs éléments montrant un accès administratif actif à plusieurs plateformes numériques gouvernementales togolaises : le système de gestion de l'état civil et de l'identité DSNIC (justice.xflow.gouv.tg), une plateforme de partage de fichiers et de collaboration de type Nextcloud (cloud.numerique.gouv.tg) avec des dossiers partagés et des fichiers de configuration, une instance de collecte de données KoboToolbox (kf.form.gouv.tg) hébergeant plusieurs dizaines d'enquêtes et formulaires gouvernementaux actifs, ainsi qu'un système de reporting statistique de l'éducation (stateduc.planifeducation.gouv.tg). Les éléments montrent un accès administratif réel à des tableaux de bord actifs, et non un simple échantillon public, ce qui est cohérent avec la description de l'offre par l'acteur comme une vulnérabilité 0day donnant un accès privilégié. Cette étendue d'accès à des systèmes et sous-domaines distincts sous le domaine gouv.tg justifie un niveau de confiance élevé quant à une compromission active et non corrigée affectant plusieurs services numériques gouvernementaux, indépendamment du prix en Monero avancé par l'acteur, qu'AFRINTEL ne peut vérifier. AFRINTEL ne reproduit aucun identifiant, valeur de configuration, donnée citoyenne ni détail de session issu des éléments examinés.

---
[Rapport d'Août 2025](./report/README_FR.md)
---
## ✍🏿 Auteur
*Adama ASSIONGBON*  
*Consultant SOC & Cyber Threat Intelligence*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)
