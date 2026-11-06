[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Période](https://img.shields.io/badge/Période-Avril%202026-lightgrey)
![Victimes](https://img.shields.io/badge/Victimes-69-critical)
![Ransomware](https://img.shields.io/badge/Ransomware-20-red)
![Fuites](https://img.shields.io/badge/Fuites-39-orange)
![Ventes%20d'accès](https://img.shields.io/badge/Ventes%20d'accès-1-yellow)
![DDoS](https://img.shields.io/badge/DDoS-9-blue)
![Pays](https://img.shields.io/badge/Pays%20directs-16-blueviolet)
![Acteurs](https://img.shields.io/badge/Libellés%20acteurs-37-darkred)
![Type%20d'Intel](https://img.shields.io/badge/Type%20d'Intel-CTI-purple)
# Victimes africaines - Avril 2026

## Récapitulatif
- **Fiches documentées :** 70
- **Total victimes canoniques :** 69
- **Note :** Bank of Kigali est documentée comme cas rétrospectif `Under Investigation - Alleged` mais exclue du total canonique et des ventilations statistiques.
- **Ransomware :** 20
- **Fuites de données :** 39
- **Ventes d'accès :** 1
- **Revendications DDoS :** 9
- **Pays directement étiquetés :** 16
- **Pays dans la vue géographique développée :** 17
- **Libellés source distincts d'acteurs/groupes :** 37

### Incidents marquants

- **Maroc :** une base attribuée au personnel du Palais royal contiendrait 3 300 enregistrements.
- **Afrique du Sud :** l’exposition de Pick n Pay ASAP/Bottles.com comprenait des données de cartes de paiement et de localisation.
- **Kenya :** une revendication ransomware visant la Kenya Airports Authority mentionnait un volume de 2 To.
- **Bénin :** une publication de messageries de 7,1 Go a été attribuée à la CNSS du Bénin.

> Les fiches ci-dessous documentent des revendications ou publications observées. Les volumes revendiqués et les compromissions ne sont pas confirmés sans élément indépendant.

---

### 01 avril 2026

#### 🇩🇿 Algérie - Ministère de la Culture [Fuite de données]
- **Date de publication initiale :** 1 avril 2026

- **Acteur / Groupe :** Grubder
- **Secteur :** Gouvernement / Culture / Administration publique
- **Site web :** [m-culture.gov.dz](https://www.m-culture.gov.dz/)
- **Statut :** Claim - Unverified
- **Description :** Environ 247 000 enregistrements exposés (contacts administratifs, inscriptions événements culturels, demandes de subventions). Données : noms, emails, téléphones, statuts de paiement, financements, dossiers de candidature.

#### 🇪🇬 Égypte - Cairo University (cu.edu.eg) [Fuite de données]
- **Date de publication initiale :** 1 avril 2026

- **Acteur / Groupe :** Grubder
- **Secteur :** Éducation / Université
- **Site web :** [cu.edu.eg](https://cu.edu.eg/)
- **Statut :** Claim - Unverified
- **Description :** Cairo University est l’une des plus anciennes et prestigieuses universités publiques d’Égypte, basée au Caire et accueillant des centaines de milliers d’étudiants. Une base de données revendiquée sur un forum cybercriminel expose environ 284 000 enregistrements liés aux étudiants, inscriptions académiques et systèmes de support universitaire. Les données mentionnées incluent notamment des informations personnelles, numéros d’identification nationaux, emails, numéros de téléphone, informations académiques, détails d’inscription, statuts financiers et tickets de support. L’analyse préliminaire suggère l’exposition d’une base backend universitaire utilisée pour la gestion des étudiants, des admissions, des inscriptions académiques et du support administratif.

#### 🇷🇼 Rwanda - Bank of Kigali [Phishing et perturbation opérationnelle]
- **Date de publication initiale :** 1 avril 2026


- **Date de l'incident / publication initiale :** 1er avril 2026
- **Période statistique d'attribution :** Avril 2026 - H1 2026
- **Mois d'intégration au référentiel :** Octobre 2026 (découverte rétrospective)
- **Acteur / Groupe :** Unidentified
- **Secteur :** Banque et services financiers
- **Statut :** Under Investigation - Alleged
- **Type d'incident :** Operational Fraud
- **Sous-type / effets observés :** Campagne de phishing ; perturbation opérationnelle et suspension temporaire de transactions
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type de source :** Média rwandais ; article de Taarifa

- **Description victime :** **Bank of Kigali** est une banque rwandaise fournissant des services bancaires aux particuliers et aux entreprises. Taarifa décrit une campagne de phishing ciblant ses clients et une suspension temporaire des transactions internes et externes annoncée comme mesure de précaution. Le nombre de clients affectés et les pertes financières éventuelles n'étaient pas établis lors de la publication ([Taarifa Rwanda](https://taarifa.rw/2026/04/01/cyberattack-disrupts-bank-of-kigali-operations-amid-phishing-scheme/)).

- **Analyse :** Selon Taarifa, des liens frauduleux auraient été diffusés pour recueillir des informations financières sensibles. La banque aurait averti ses clients de ne pas communiquer leurs PIN, mots de passe ou données de carte par SMS, WhatsApp, e-mail ou téléphone. L'article rapporte également une suspension temporaire des transactions internes et externes, ainsi que l'implication d'une équipe de la National Bank of Rwanda dans l'investigation. Ces éléments sont rapportés par le média et ne constituent pas une confirmation technique indépendante.

  **Assumption :** La campagne décrite relève principalement d'une fraude opérationnelle cyber-activée, avec indisponibilité temporaire de services comme effet secondaire. La nature exacte des liens, le nombre de victimes et l'existence de transactions frauduleuses ne sont pas établis.

  **Unknown :** L'acteur, les domaines et numéros utilisés, le nombre de clients ciblés ou compromis, les pertes financières, l'origine de la campagne, toute prise de contrôle de compte, l'existence d'une intrusion dans l'infrastructure de Bank of Kigali et toute confirmation directe par la banque restent inconnus. Taarifa indique que ses demandes de clarification auprès de la banque n'avaient pas reçu de réponse au moment de la publication.

- **Périmètre et limites :** Analyse fondée sur l'article public de Taarifa ; aucun domaine de phishing, numéro, échantillon, journal ou donnée client n'a été fourni ou examiné. L'événement ne doit pas être présenté comme une fuite de données ou une compromission confirmée.
- **Recommandations SOC/CTI :** Collecter et bloquer les domaines, URL et numéros utilisés ; rechercher les authentifications inhabituelles et prises de contrôle de comptes ; corréler les connexions suspectes avec les transactions frauduleuses ; réinitialiser les accès des clients potentiellement compromis ; renforcer les communications antifraude sur les canaux officiels ; surveiller les campagnes usurpant l'identité de Bank of Kigali.
- **Décision de comptage :** Incident conservé dans le référentiel d'avril pour sa date d'événement, mais **exclu des statistiques canoniques** tant que le statut `Under Investigation - Alleged` n'est pas corroboré. Il ne constitue pas un nouvel incident d'octobre.
- **Source / élément observé :** [Taarifa Rwanda, 1er avril 2026](https://taarifa.rw/2026/04/01/cyberattack-disrupts-bank-of-kigali-operations-amid-phishing-scheme/).

#### 🇪🇹 Éthiopie - National Oil Ethiopia PLC (NOC) [Fuite de données]
- **Date de publication initiale :** 1 avril 2026


- **Acteur / Groupe :** ByteToBreach
- **Secteur :** Énergie / Pétrole & Gaz / Infrastructure critique
- **Site web :** [nationaloilethiopia.com](https://www.nationaloilethiopia.com/)
- **Date de la fuite :** 24 Mars 2026
- **Statut :** Claim - Data Sample Published
- **Description :** National Oil Ethiopia PLC (NOC) est une entreprise majeure du secteur énergétique éthiopien spécialisée dans les activités pétrolières, la distribution de carburants et les services associés. Une publication sur un forum cybercriminel revendique une compromission complète de l’infrastructure de l’organisation ayant conduit à l’exfiltration de plusieurs bases de données, dont une base ERP principale estimée à plus de 800 Go. L’acteur affirme avoir obtenu des informations sensibles incluant données clients, contrats, salaires, emails, adresses, informations personnelles (PII) ainsi que des données opérationnelles internes. La publication décrit également une chaîne d’intrusion complète allant d’un accès initial via une vulnérabilité Microsoft Exchange ProxyLogon jusqu’au déploiement final d’un ransomware. Les captures et descriptions publiées suggèrent une compromission avancée des systèmes internes, des accès administrateurs, des bases de données et potentiellement des solutions de sécurité déployées au sein de l’infrastructure.
---

### 02 avril 2026

#### 🇿🇦 Afrique du Sud - singita.com [Ransomware]
- **Date de publication initiale :** 2 avril 2026

- **Groupe ransomware :** dragonforce
- **Secteur :** Industrie du voyage et du tourisme
- **Site web :** [singita.com](https://singita.com)
- **Statut :** Claim - Unverified
- **Description :** Gestionnaire de lodges de luxe et de réserves naturelles en Afrique.

#### 🇿🇦 Afrique du Sud - Takealot.com [Fuite de données]
- **Date de publication initiale :** 2 avril 2026

- **Acteur / Groupe :** Grubder
- **Secteur :** E‑commerce
- **Site web :** [takealot.com](https://www.takealot.com)
- **Statut :** Claim - Data Sample Published
- **Description :** Leader sud‑africain du e‑commerce. Le fichier `DeliveryAddress_South Africa.csv` expose adresses de livraison détaillées, coordonnées GPS, numéros de téléphone, instructions d’accès privées.

#### 🇿🇦 Afrique du Sud - MySchool South Africa [Fuite de données]
- **Date de publication initiale :** 2 avril 2026

- **Acteur / Groupe :** Grubder
- **Secteur :** Éducation / Services étudiants
- **Site web :** [myschool.co.za](https://www.myschool.co.za/)
- **Statut :** Claim - Unverified
- **Description :** Environ 437 000 enregistrements : contacts étudiants, inscriptions, tickets de support, noms, emails, téléphones, dates de naissance, statuts de paiement.

#### 🇹🇳 Tunisie - Fatales.tn [Fuite de données]
- **Date de publication initiale :** 2 avril 2026


- **Acteur / Groupe :** Grubder
- **Secteur :** E-commerce / Beauté / CRM
- **Site web :** [fatales.tn](https://www.fatales.tn/)
- **Statut :** Claim - Data Sample Published
- **Description :** Une publication sur un forum cybercriminel revendique la vente d’une base de données attribuée à Fatales.tn contenant environ 431 000 enregistrements clients liés aux contacts utilisateurs, historiques de réservation et programmes de fidélité. L’acteur affirme que les données sont organisées en plusieurs ensembles structurés couvrant la gestion client, les réservations et les opérations marketing.

- **Données observées :**
  - noms et prénoms
  - emails
  - numéros de téléphone
  - adresses physiques
  - dates de naissance
  - historiques de réservation
  - statuts et méthodes de paiement
  - données CRM et fidélité
  - segmentation et préférences marketing
  - niveaux VIP et points fidélité

- **Analyse CTI :**
  Les éléments publiés suggèrent l’exposition d’une base CRM/e-commerce centralisée utilisée pour la gestion client et les opérations marketing. La combinaison de données personnelles, comportementales et transactionnelles augmente les risques de phishing ciblé, fraude marketing, spam massif et usurpation d’identité.

- **Note CTI :**
  L’authenticité complète du dataset n’est pas confirmée indépendamment à ce stade, mais la structure détaillée des champs et la cohérence CRM renforcent la crédibilité potentielle de la fuite revendiquée.

#### 🇹🇳 Tunisie - NSSTunis [Fuite de données]
- **Date de publication initiale :** 2 avril 2026

- **Acteur / Groupe :** Grubder
- **Secteur :** Services / CRM
- **Site web :** [nsstunis.com](https://www.nsstunis.com/)
- **Statut :** Claim - Unverified
- **Description :** ~312 000 enregistrements : noms, emails, téléphones, infos familiales, centres d’intérêt, statuts marketing, données démographiques.

#### 🇪🇬 Égypte - Ain Shams University (ums.asu.edu.eg) [Fuite de données]
- **Date de publication initiale :** 2 avril 2026

- **Acteur / Groupe :** Grubder
- **Secteur :** Éducation / Université
- **Site web :** [ums.asu.edu.eg](https://ums.asu.edu.eg/)
- **Statut :** Claim - Unverified
- **Description :** Ain Shams University est l’une des principales universités publiques d’Égypte, basée au Caire et reconnue pour ses programmes académiques et de recherche. Une base de données revendiquée sur un forum cybercriminel expose environ 563 000 enregistrements liés aux étudiants, aux inscriptions académiques et aux systèmes d’authentification. Les données mentionnées incluent notamment des informations personnelles, emails, numéros de téléphone, identifiants universitaires, détails d’inscription, programmes académiques, statuts financiers et éléments liés à la vérification d’identité et à l’authentification. L’analyse préliminaire suggère l’exposition d’une base backend universitaire utilisée pour la gestion des étudiants, des inscriptions et des mécanismes de vérification académique.
---

### 03 avril 2026

#### 🇪🇬 Égypte - United Finance Egypt [Ransomware]
- **Date de publication initiale :** 3 avril 2026

- **Groupe ransomware :** payload
- **Secteur :** Finance
- **Site web :** [uf-eg.com](https://uf-eg.com)
- **Statut :** Claim - Unverified
- **Description :** Institution financière non bancaire (crédit‑bail, affacturage, prêts). Infrastructure entièrement compromise, données clients exposées.

---

### 04 avril 2026

#### 🇧🇼 Botswana - lkc.ac.bw [Ransomware]
- **Date de publication initiale :** 4 avril 2026

- **Groupe ransomware :** krybit
- **Secteur :** Établissements académiques
- **Site web :** [lkc.ac.bw](https://lkc.ac.bw)
- **Statut :** Claim - Unverified
- **Description :** Livingstone Kolobeng College, école secondaire privée à Gaborone.

#### 🇪🇬 Égypte - AUG Pharma [Ransomware]
- **Date de publication initiale :** 4 avril 2026

- **Groupe ransomware :** dragonforce
- **Secteur :** Industrie pharmaceutique
- **Site web :** [augpharma.com](https://augpharma.com)
- **Statut :** Claim - Unverified
- **Description :** Société pharmaceutique égyptienne.

#### 🇦🇴 🇿🇦 🇳🇬 Afrique - Fuite de données gouvernementales et accès administrateurs [Fuite de données]
- **Date de publication initiale :** 4 avril 2026


- **Acteur / Groupe :** superduper1
- **Secteur :** Gouvernement / Défense / Santé / Renseignement
- **Statut :** Claim - Unverified
- **Site web :** N/A
- **Description :** Une publication sur un forum cybercriminel revendique la vente d’accès à plusieurs messageries gouvernementales, panneaux administrateurs et comptes liés à des institutions publiques africaines.

- **Pays concernés observés :**
  - 🇦🇴 Angola
  - 🇿🇦 Afrique du Sud
  - 🇳🇬 Nigeria

- **Accès revendiqués :**
  - panneaux administrateurs eGov
  - messageries de la police nationale angolaise
  - domaines médicaux gouvernementaux angolais
  - accès liés à des agences militaires et de renseignement
  - comptes gouvernementaux sud-africains
  - comptes liés à des départements sportifs sud-africains
  - comptes de personnels gouvernementaux nigérians

- **Analyse CTI :**
  Les éléments publiés suggèrent potentiellement une revente d’identifiants compromis ou d’accès persistants à des infrastructures gouvernementales africaines. Les risques incluent spear phishing institutionnel, espionnage, Business Email Compromise (BEC) et compromission de communications officielles.

- **Note CTI :**
  Aucun élément technique ne permet actuellement de confirmer indépendamment l’authenticité des accès revendiqués.

---

### 06 avril 2026

#### 🇪🇬 Égypte - gas.mercedes-benz.com.eg [Ransomware]
- **Date de publication initiale :** 6 avril 2026

- **Groupe ransomware :** lockbit5
- **Secteur :** Automobile
- **Site web :** [gas.mercedes-benz.com.eg](https://gas.mercedes-benz.com.eg)
- **Statut :** Claim - Unverified
- **Description :** Concessionnaire Mercedes‑Benz agréé à Gizeh.

#### 🇳🇬 Nigeria - Welfare.org.ng [Fuite de données]
- **Date de publication initiale :** 6 avril 2026

- **Acteur / Groupe :** Citizen / NormalLeVrai
- **Secteur :** ONG / Aide sociale
- **Site web :** [welfare.org.ng](https://welfare.org.ng/)
- **Statut :** Claim - Unverified
- **Description :** Plateforme nigériane de services communautaires. Compromission du site principal et sous‑domaines, avec code source, sauvegardes et base de données >12 000 enregistrements.

---

### 08 avril 2026

#### 🇪🇬 Égypte - El Wastani Petroleum Company (WASCO) [Ransomware]
- **Date de publication initiale :** 8 avril 2026

- **Groupe ransomware :** payload
- **Secteur :** Pétrole
- **Site web officiel :** Non identifié avec certitude
- **Référence publique :** [EGAS - visite des champs de WASCO](https://www.egas.com.eg/ar/w/egas-chairman-visits-wasatani-fields-to-follow-up-on-production-drilling-and-exploration-programs-and-strengthen-partnership-with-dana-gas)
- **Statut :** Claim - Unverified
- **Description :** Exploration, production et traitement de gaz naturel dans le delta du Nil et le Sinaï Nord.

#### 🇪🇬 Égypte - ACE Consulting Engineers [Ransomware]
- **Date de publication initiale :** 8 avril 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Conseil en ingénierie
- **Site web :** [ace-mb.com](https://ace-mb.com)
- **Statut :** Claim - Unverified
- **Description :** Cabinet d’ingénierie international fondé en 1950, présent dans plus de 35 pays.

#### 🇲🇦 Maroc - CNOPS [Fuite de données]
- **Date de publication initiale :** 8 avril 2026

- **Acteur / Groupe :** JBT2026 (relayé par Jabaroot)
- **Secteur :** Santé / Assurance maladie / Administration publique
- **Site web :** [cnops.org.ma](https://www.cnops.org.ma/)
- **Statut :** Claim - Unverified
- **Description :** Plus de 3 millions d’enregistrements d’assurés marocains : noms, numéros d’affiliation, CIN, adresses complètes.

---

#### 🇩🇿 Algérie - Administration publique non identifiée (accès Fortinet)
- **Date de publication initiale :** 8 avril 2026


- **Acteur / Groupe :** AckLine, publication sur un forum cybercriminel
- **Secteur :** Gouvernement / Administration publique
- **Site web :** Non identifié avec certitude
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Vente d’accès
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3

- **Description :**

La publication propose la vente d'un accès présenté comme lié à des équipements Fortinet, associé à une administration algérienne non identifiée, avec des coordonnées de contact fournies via qTox. Aucune organisation précise, aucun domaine, aucun prix chiffré ni aucune preuve technique ne sont divulgués.

- **Analyse :**

L'acteur AckLine a publié une annonce succincte proposant un accès décrit uniquement comme « Fortinet » et associé à « Algeria gov », sans nommer de ministère, d'agence ou de domaine précis. L'annonce ne donne aucun prix chiffré (« $$$ offer price »), aucun échantillon de données, et aucune preuve technique d'accès telle qu'une capture d'écran d'une console de gestion, d'un portail VPN ou d'une configuration. La négociation est orientée vers un contact qTox externe, ce qui correspond aux annonces classiques de courtiers en accès mais ne confirme pas en soi que l'accès proposé est réel.

En l'absence de victime nommée, de preuve vérifiable ou de détail de prix, cette revendication est évaluée avec un niveau de confiance faible. Si elle s'avérait authentique, un accès non autorisé à un équipement Fortinet (pare-feu/VPN) appartenant à une administration algérienne pourrait permettre une intrusion réseau, des mouvements latéraux et la compromission d'autres systèmes connectés.

- **Recommandations :**

1. Les administrations algériennes devraient auditer les équipements Fortinet exposés, appliquer les correctifs de sécurité disponibles et examiner les journaux d'accès VPN/pare-feu à la recherche d'activités anormales.
2. Surveiller les forums cybercriminels et les annonces de courtiers en accès mentionnant des infrastructures gouvernementales algériennes, afin de détecter d'éventuelles publications complémentaires permettant de confirmer ou de préciser la cible.
---

### 09 avril 2026

#### 🇸🇨 Seychelles - egov.sc [Ransomware]
- **Date de publication initiale :** 9 avril 2026

- **Groupe ransomware :** apt73/bashe
- **Secteur :** Administrations publiques
- **Site web :** [egov.sc](https://egov.sc)
- **Statut :** Claim - Unverified
- **Description :** Portail officiel e‑gouvernement des Seychelles.

#### 🇿🇦 Afrique du Sud - megasurf.co.za [Ransomware]
- **Date de publication initiale :** 9 avril 2026

- **Groupe ransomware :** krybit
- **Secteur :** Fournisseurs d’accès Internet
- **Site web :** [megasurf.co.za](https://megasurf.co.za)
- **Statut :** Claim - Unverified
- **Description :** FAI et opérateur de centre de données sud‑africain.

---

### 10 avril 2026

#### 🇩🇿 Algérie - Université Hassiba Ben Bouali de Chlef (univ-chlef.dz)
- **Date de publication initiale :** 10 avril 2026


- **Acteur / Groupe :** Phantom Atlas
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [univ-chlef.dz](https://www.univ-chlef.dz)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 3

- **Description :**

  L'Université Hassiba Ben Bouali de Chlef est un établissement public algérien d'enseignement supérieur, composé de neuf facultés et deux instituts.

- **Analyse :**

  Phantom Atlas a publié le 10 avril 2026 une revendication d'accès à l'interface phpMyAdmin du serveur de l'université, adressée directement au directeur de l'établissement et présentée comme une dénonciation de « défaillances de gouvernance interne » plutôt qu'un simple exploit technique. Le texte de la publication fait lui-même référence à un accès obtenu et maintenu depuis le 8 novembre 2025. La publication affirme disposer d'un accès complet aux panneaux d'administration et aux bases de données étudiantes, tout en indiquant explicitement ne pas vouloir divulguer les données des étudiants. Un second message publié après la mise en maintenance du site réitère la revendication d'un accès prolongé et menace de nouvelles révélations.

  L'analyse des données visibles identifie deux bases distinctes présentées via phpMyAdmin sur univ-chlef.dz. La première correspond à une base de site web de type CMS (préfixe de tables `refx_`, incluant des tables de publications, commentaires, utilisateurs et métadonnées SEO), totalisant 15 tables pour environ 152,5 Mio. La seconde correspond à une base de gestion administrative du personnel (19 tables, dont `ats`, `att_travail`, `fiche_paie`, `personne`, `grade`, `print_badge`), totalisant environ 13 630 lignes pour 1,7 Mio. Un extrait visible de la table `ats` affiche des enregistrements nominatifs du personnel incluant nom et prénom en français et en arabe, genre, grade professionnel, date et lieu de naissance, une référence de photo, une date de nomination, un code de faculté d'affectation et un mot de passe sous forme de hachage hexadécimal à 40 caractères.

  La cohérence de l'interface visible, des noms de tables et des champs, ainsi que la mise en maintenance du site peu après la publication, soutient avec un niveau de confiance élevé que les éléments publiés représentent de façon plausible un environnement de base de données universitaire. Elle n'établit pas indépendamment la méthode d'accès, la persistance de cet accès ni l'accessibilité de toutes les bases revendiquées. Les données visibles sur le personnel, incluant des dates de naissance et des mots de passe hachés, présentent un risque d'usurpation d'identité, de compromission de comptes en cas de réutilisation de mots de passe et de phishing ciblé. L'analyse est limitée aux éléments visibles, car les exports originaux n'étaient pas disponibles ; AFRINTEL ne reproduit aucun nom, date de naissance, lieu de naissance, référence de photo ni valeur de hachage.

### 11 avril 2026

#### 🇸🇩 Soudan - Site de la Rapid Support Force
- **Date de publication initiale :** 11 avril 2026


- **Acteur / Groupe :** Keymous+
- **Secteur :** Government / Administration
- **Type d incident :** DDoS
- **Site web :** [rapidsupportforce.com](https://rapidsupportforce.com)
- **Statut :** Claim - Unverified

- **Description :**
  Keymous+ a publié une revendication de disponibilité présentant le site ou le service comme indisponible.

- **Analyse :**
  Observé : un résultat Check-Host ou un test de disponibilité équivalent côté acteur a été publié les 11 ou 12 avril 2026. Inconnus : source du trafic, méthode DDoS, durée, impact indépendant sur le service et confirmation de la victime. L observation ne prouve pas indépendamment la réussite d un DDoS.

#### 🇪🇬 Égypte - Orange Egypt
- **Date de publication initiale :** 11 avril 2026


- **Acteur / Groupe :** Keymous+
- **Secteur :** Télécommunications
- **Type d incident :** DDoS
- **Site web :** [orange.eg](https://orange.eg)
- **Statut :** Claim - Unverified

- **Description :**
  Keymous+ a publié une revendication de disponibilité présentant le site ou le service comme indisponible.

- **Analyse :**
  Observé : un résultat Check-Host ou un test de disponibilité équivalent côté acteur a été publié les 11 ou 12 avril 2026. Inconnus : source du trafic, méthode DDoS, durée, impact indépendant sur le service et confirmation de la victime. L observation ne prouve pas indépendamment la réussite d un DDoS.

#### 🇪🇬 Égypte - Telecom Egypt
- **Date de publication initiale :** 11 avril 2026


- **Acteur / Groupe :** Keymous+
- **Secteur :** Télécommunications
- **Type d incident :** DDoS
- **Site web :** Non précisé
- **Statut :** Claim - Unverified

- **Description :**
  Keymous+ a publié une revendication de disponibilité présentant le site ou le service comme indisponible.

- **Analyse :**
  Observé : un résultat Check-Host ou un test de disponibilité équivalent côté acteur a été publié les 11 ou 12 avril 2026. Inconnus : source du trafic, méthode DDoS, durée, impact indépendant sur le service et confirmation de la victime. L observation ne prouve pas indépendamment la réussite d un DDoS.

### 12 avril 2026

#### 🇲🇦 Maroc - OFPPT [Fuite de données]
- **Date de publication initiale :** 12 avril 2026

- **Acteur / Groupe :** anisanas2
- **Secteur :** Formation professionnelle / Éducation
- **Site web :** [ofppt.ma](https://www.ofppt.ma)
- **Statut :** Claim - Unverified
- **Description :** Principal organisme de formation professionnelle au Maroc. Données exposées : noms, téléphones, emails, CNI, code Massar, ville, statut, logs d’activité.

#### 🇲🇦 Maroc - Documents d’identité marocains (Passeports/KYC) [Fuite de données]
- **Date de publication initiale :** 12 avril 2026

- **Acteur / Groupe :** Arnoldsudney
- **Secteur :** Identité numérique / Documents officiels
- **Site web :** N/A
- **Statut :** Claim - Unverified
- **Description :** Offre de passeports, cartes d’identité, selfies de vérification, permis de conduire et packs KYC complets.

---

#### 🇪🇬 Égypte - Portail du gouvernement égyptien
- **Date de publication initiale :** 12 avril 2026


- **Acteur / Groupe :** Keymous+
- **Secteur :** Government / Administration
- **Type d incident :** DDoS
- **Site web :** [egypt.gov.eg](https://egypt.gov.eg)
- **Statut :** Claim - Unverified

- **Description :**
  Keymous+ a publié une revendication de disponibilité présentant le site ou le service comme indisponible.

- **Analyse :**
  Observé : un résultat Check-Host ou un test de disponibilité équivalent côté acteur a été publié les 11 ou 12 avril 2026. Inconnus : source du trafic, méthode DDoS, durée, impact indépendant sur le service et confirmation de la victime. L observation ne prouve pas indépendamment la réussite d un DDoS.

#### 🇪🇬 Égypte - Ministère des Finances
- **Date de publication initiale :** 12 avril 2026


- **Acteur / Groupe :** Keymous+
- **Secteur :** Government / Administration
- **Type d incident :** DDoS
- **Site web :** [mof.gov.eg](https://mof.gov.eg)
- **Statut :** Claim - Unverified

- **Description :**
  Keymous+ a publié une revendication de disponibilité présentant le site ou le service comme indisponible.

- **Analyse :**
  Observé : un résultat Check-Host ou un test de disponibilité équivalent côté acteur a été publié les 11 ou 12 avril 2026. Inconnus : source du trafic, méthode DDoS, durée, impact indépendant sur le service et confirmation de la victime. L observation ne prouve pas indépendamment la réussite d un DDoS.

#### 🇪🇬 Égypte - Ministère de la Justice
- **Date de publication initiale :** 12 avril 2026


- **Acteur / Groupe :** Keymous+
- **Secteur :** Government / Administration
- **Type d incident :** DDoS
- **Site web :** [jp.gov.eg](https://jp.gov.eg)
- **Statut :** Claim - Unverified

- **Description :**
  Keymous+ a publié une revendication de disponibilité présentant le site ou le service comme indisponible.

- **Analyse :**
  Observé : un résultat Check-Host ou un test de disponibilité équivalent côté acteur a été publié les 11 ou 12 avril 2026. Inconnus : source du trafic, méthode DDoS, durée, impact indépendant sur le service et confirmation de la victime. L observation ne prouve pas indépendamment la réussite d un DDoS.

#### 🇪🇬 Égypte - Ministère du Commerce et de l Industrie
- **Date de publication initiale :** 12 avril 2026


- **Acteur / Groupe :** Keymous+
- **Secteur :** Government / Administration
- **Type d incident :** DDoS
- **Site web :** [mti.gov.eg](https://mti.gov.eg)
- **Statut :** Claim - Unverified

- **Description :**
  Keymous+ a publié une revendication de disponibilité présentant le site ou le service comme indisponible.

- **Analyse :**
  Observé : un résultat Check-Host ou un test de disponibilité équivalent côté acteur a été publié les 11 ou 12 avril 2026. Inconnus : source du trafic, méthode DDoS, durée, impact indépendant sur le service et confirmation de la victime. L observation ne prouve pas indépendamment la réussite d un DDoS.

#### 🇪🇬 Égypte - Ministère du Pétrole et des Ressources minérales
- **Date de publication initiale :** 12 avril 2026


- **Acteur / Groupe :** Keymous+
- **Secteur :** Government / Administration
- **Type d incident :** DDoS
- **Site web :** [petroleum.gov.eg](https://petroleum.gov.eg)
- **Statut :** Claim - Unverified

- **Description :**
  Keymous+ a publié une revendication de disponibilité présentant le site ou le service comme indisponible.

- **Analyse :**
  Observé : un résultat Check-Host ou un test de disponibilité équivalent côté acteur a été publié les 11 ou 12 avril 2026. Inconnus : source du trafic, méthode DDoS, durée, impact indépendant sur le service et confirmation de la victime. L observation ne prouve pas indépendamment la réussite d un DDoS.

#### 🇪🇬 Égypte - Service d Information de l État égyptien
- **Date de publication initiale :** 12 avril 2026


- **Acteur / Groupe :** Keymous+
- **Secteur :** Government / Administration
- **Type d incident :** DDoS
- **Site web :** [sis.gov.eg](https://sis.gov.eg)
- **Statut :** Claim - Unverified

- **Description :**
  Keymous+ a publié une revendication de disponibilité présentant le site ou le service comme indisponible.

- **Analyse :**
  Observé : un résultat Check-Host ou un test de disponibilité équivalent côté acteur a été publié les 11 ou 12 avril 2026. Inconnus : source du trafic, méthode DDoS, durée, impact indépendant sur le service et confirmation de la victime. L observation ne prouve pas indépendamment la réussite d un DDoS.

### 13 avril 2026

#### 🇰🇪 Kenya - ifmis.go.ke [Ransomware]
- **Date de publication initiale :** 13 avril 2026

- **Groupe ransomware :** apt73/bashe
- **Secteur :** Administration centrale
- **Site web :** [ifmis.go.ke](https://ifmis.go.ke)
- **Statut :** Claim - Unverified
- **Description :** Système intégré de gestion des informations financières du Kenya.

#### 🇲🇦 Maroc - GET / GENERAL ELECTRIC TRADING (gemaroc.com) [Fuite de données]
- **Date de publication initiale :** 13 avril 2026

- **Acteur / Groupe :**  bxxxx1
- **Secteur :** Services industriels / Infrastructure IT
- **Site web :** [gemaroc.com](https://gemaroc.com/)
- **Statut :** Claim - Data Sample Published
- **Description :** Dump SQL (septembre 2024) exposant Dolibarr ERP/CRM, bases WordPress, données RH, financières, tickets, logs.

---

### 14 avril 2026

#### 🇬🇭 Ghana - International Maritime Hospital [Ransomware]
- **Date de publication initiale :** 14 avril 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Services de santé
- **Site web :** [imah.gov.gh](https://imah.gov.gh)
- **Statut :** Claim - Unverified
- **Description :** Hôpital public à Tema, spécialisé en santé maritime et générale.

#### 🇲🇦 Maroc - Base attribuée au personnel du Palais Royal (Dar El Makhzen) [Fuite de données]
- **Date de publication initiale :** 14 avril 2026


- **Acteur / Groupe :** Rihana
- **Secteur :** Gouvernement / Maison Royale
- **Site web :** N/A (institution)
- **Statut :** Claim - Data Sample Published
- **Description :** Une publication diffusée sur un forum cybercriminel revendique la vente d’une base de données présentée comme liée au personnel du Palais Royal marocain (Dar El Makhzen). L’échantillon analysé contient environ 3 300 enregistrements comprenant plusieurs catégories de données personnelles et administratives sensibles.

- **Éléments observés dans les données divulguées :**
  - Nom et prénom
  - Date de naissance
  - Lieu de naissance
  - Sexe
  - Nationalité
  - Numéro de Carte Nationale d’Identité Électronique (CNIE)
  - Adresse physique
  - Date de recrutement

- **Analyse CTI préliminaire :**
  Les informations analysées suggèrent potentiellement une extraction issue :
  - d’une base RH interne,
  - d’un système administratif de gestion du personnel,
  - ou d’un export de données institutionnelles centralisées.

  La présence simultanée :
  - d’identifiants nationaux,
  - d’adresses physiques,
  - de dates de recrutement,
  - et d’informations biographiques détaillées

  augmente fortement le risque :
  - d’ingénierie sociale ciblée,
  - d’usurpation d’identité,
  - de spear-phishing,
  - de fraude documentaire,
  - ou d’opérations d’usurpation visant du personnel institutionnel sensible.

- **Note CTI :**
  À ce stade, l’authenticité complète du dataset ainsi que son origine exacte ne peuvent pas être confirmées de manière indépendante. Toutefois, la structure homogène des champs, la cohérence administrative des données et la présence de champs RH structurés renforcent la crédibilité potentielle de la fuite revendiquée.

---

### 16 avril 2026

#### 🇪🇬 Égypte - orientalweavers.com [Ransomware]
- **Date de publication initiale :** 16 avril 2026

- **Groupe ransomware :** payload
- **Secteur :** Industrie manufacturière
- **Site web :** [orientalweavers.com](https://orientalweavers.com)
- **Statut :** Claim - Unverified
- **Description :** Un des plus grands fabricants de tapis et moquettes au monde, basé au Caire.

#### 🇰🇪 Kenya - Kenya Airports Authority (KAA) [Fuite de données]
- **Date de publication initiale :** 16 avril 2026


- **Acteur / Groupe :** RubiconH4ck
- **Secteur :** Aviation / Transport / Infrastructure critique
- **Site web :** [kaa.go.ke](https://www.kaa.go.ke/)
- **Statut :** Claim - Unverified
- **Description :** Kenya Airports Authority (KAA) est l’organisme public kényan chargé de la gestion et de l’exploitation des principaux aéroports du pays, incluant les infrastructures aériennes stratégiques et les services associés. Une publication sur un forum cybercriminel revendique la vente d’environ 2 To de données attribuées à l’organisation. L’acteur affirme que les données incluent des systèmes d’information, des données utilisateurs, des services internes ainsi que des adresses complètes d’utilisateurs. L’annonce suggère une compromission potentielle d’infrastructures critiques liées au secteur aérien kényan. Bien que les éléments publiquement exposés restent limités, le volume revendiqué et la nature des informations mentionnées pourraient représenter un risque significatif pour la sécurité opérationnelle, la confidentialité des données et les infrastructures associées au transport aérien.
---

#### 🇩🇿 Algérie - ATS (Algérie Télécom Satellite)
- **Date de publication initiale :** 16 avril 2026


- **Acteur / Groupe :** Phantom Atlas
- **Secteur :** Télécommunications / Opérateur satellitaire
- **Site web :** [ats.dz](https://www.ats.dz)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 3

- **Description :**

  ATS (Algérie Télécom Satellite) est l'opérateur satellitaire algérien, filiale du groupe Algérie Télécom, fournissant des services de télécommunications par satellite à l'échelle nationale.

- **Analyse :**

  Phantom Atlas a publié le 16 avril 2026 une revendication de compromission complète des systèmes numériques d'ATS, affirmant détenir les bulletins de paie de l'ensemble des employés de l'entreprise. Le message adopte une tonalité hacktiviste explicitement pro-marocaine (reprise du slogan royal marocain « Allah, Al Watan, Al Malik »), présentant l'opération comme une réponse directe à des attaques informatiques antérieures visant le Maroc, et annonce la publication prochaine d'un échantillon de bulletins de paie ainsi que des noms et postes du personnel.

  AFRINTEL a examiné un échantillon local de 88 fichiers (environ 29 Mo), majoritairement des bulletins de paie individuels au format image, datés de juillet 2023 à novembre 2024, ainsi que quelques captures plus récentes. Les bulletins examinés concernent des employés de différentes directions régionales d'ATS (Direction Régionale Est-Constantine, Direction Sud-Est, entre autres) et affichent une structure cohérente : numéro d'employeur, matricule, nom et prénom, date d'entrée en fonction, situation familiale, numéro de sécurité sociale, fonction et catégorie/échelon, ainsi qu'un détail complet des rubriques de salaire (gains et retenues), l'assiette de cotisations sociales, le salaire imposable, le numéro de compte bancaire et le montant net à payer. Plusieurs documents portent des cachets authentiques de la Direction des Ressources Humaines ou de directions régionales d'ATS.

  La cohérence du format sur l'ensemble de l'échantillon, la diversité des employés, directions et périodes représentées, ainsi que la présence de cachets officiels plausibles, soutiennent un niveau de confiance élevé quant à l'authenticité de cette fuite. L'exposition de bulletins de paie nominatifs, incluant numéros de sécurité sociale et coordonnées bancaires, présente un risque élevé de fraude financière, d'usurpation d'identité et de phishing ciblé contre le personnel d'ATS. AFRINTEL ne reproduit aucun nom, matricule, numéro de sécurité sociale, numéro de compte ni montant de salaire issus de l'échantillon examiné.

### 18 avril 2026

#### 🇿🇦 Afrique du Sud - Ahmed Al-Kadi Private Hospital
- **Date de publication initiale :** 18 avril 2026


- **Date de l'incident :** 18 avril 2026
- **Acteur / Groupe :** Non attribué publiquement
- **Secteur :** Santé / Hôpital privé
- **Statut :** Victim Confirmed
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** **Ahmed Al-Kadi Private Hospital** est un hôpital privé de **Mayville, à Durban**, en Afrique du Sud. Développé par l'**Islamic Medical Association of South Africa**, l'établissement a ouvert en 2017 et indique disposer de **163 lits**, avec des activités de soins hospitaliers et des spécialités médicales et chirurgicales. Sa mission déclarée est d'accueillir les patients sans distinction d'origine ou de religion ([site officiel](https://ahmedalkadi.com/about-us/)).

- **Vérification indépendante au 18 octobre 2026 :** **Confirmation directe :** l’hôpital annonce un accès non autorisé le 18 avril 2026, suivi du déploiement d’un ransomware ayant chiffré une partie de son environnement ; notification POPIA et signalement au régulateur. L’incident n’est pas daté de septembre.

- **Sources de vérification complémentaires :** [Source 1](https://ahmedalkadi.com/notification-of-data-incident/)

- **Sources / Éléments de preuve :** [Notification officielle de l'hôpital](https://ahmedalkadi.com/notification-of-data-incident/)

L'hôpital a confirmé qu'un tiers avait accédé à son environnement informatique et déployé un ransomware le 18 avril. Une partie de l'environnement a été chiffrée, puis contenue et restaurée avec l'aide de spécialistes externes. Le vecteur, l'étendue du chiffrement et l'exfiltration restent inconnus.

### 19 avril 2026

#### 🇿🇦 Afrique du Sud - Sunspray Food [Ransomware]
- **Date de publication initiale :** 19 avril 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Agroalimentaire
- **Site web :** [sunspray.co.za](https://sunspray.co.za)
- **Statut :** Claim - Unverified
- **Description :** Plus grand fabricant sud‑africain d’ingrédients alimentaires lyophilisés.

#### 🇲🇦 Maroc - Al Barid Bank [Fuite de données]
- **Date de publication initiale :** 19 avril 2026

- **Acteur / Groupe :** Sejjil
- **Secteur :** Banque / Services financiers
- **Site web :** [albaridbank.ma](https://www.albaridbank.ma/)
- **Statut :** Claim - Data Sample Published
- **Description :** Logs financiers internes (2025) avec transferts instantanés, prélèvements, informations d’agences, numéros de téléphone.

### 20 avril 2026

#### 🇪🇬 Égypte - Better House [Ransomware]
- **Date de publication initiale :** 20 avril 2026

- **Groupe ransomware :** payload
- **Secteur :** Construction
- **Site web :** [betterhouse-eg.com](https://betterhouse-eg.com)
- **Statut :** Claim - Unverified
- **Description :** Promoteur immobilier égyptien (plus de 150 projets).

#### 🇲🇦 Maroc - SUPTECH SANTÉ [Fuite de données]
- **Date de publication initiale :** 20 avril 2026

- **Acteur / Groupe :** xNov
- **Secteur :** Éducation / Formation / Technologies de santé
- **Site web :** suptech-sante.ma
- **Statut :** Claim - Unverified
- **Description :** >231 dossiers étudiants : CIN, scans de diplômes, emails, téléphones, codes Massar, confirmations d’inscription.

---

### 21 avril 2026

#### 🇲🇦 Maroc - LNM6 (Laboratoire National Mohammed VI) [Fuite de données]
- **Date de publication initiale :** 21 avril 2026

- **Acteur / Groupe :** anisanas2
- **Secteur :** Santé / Laboratoire médical
- **Site web :** N/A
- **Statut :** Claim - Data Sample Published
- **Description :** Rapports médicaux PDF exposés : identité complète, résultats biologiques (VIH, HPV, IST, tuberculose, hormonaux, génétique), données pédiatriques et néonatales.

#### 🇳🇬 Nigeria - Federal Housing Authority (FHA) [Fuite de données]
- **Date de publication initiale :** 21 avril 2026

- **Acteur / Groupe :** 0xLei / Nullsec
- **Secteur :** Administration publique / Immobilier
- **Site web :** [fha.gov.ng](https://www.fha.gov.ng/)
- **Statut :** Claim - Unverified
- **Description :** ~170 Mo de code source, fichiers backend, configurations.

#### 🇳🇬 Nigeria - EFCC [Fuite de données]
- **Date de publication initiale :** 21 avril 2026

- **Acteur / Groupe :** ki4t / Nullsec Nigeria
- **Secteur :** Application de la loi / Anti‑corruption
- **Site web :** [efcc.gov.ng](https://www.efcc.gov.ng/)
- **Statut :** Claim - Data Sample Published
- **Description :** Comptes utilisateurs, emails, téléphones, rôles internes, hashs bcrypt, IP internes, données d’agents.

#### 🇲🇦 Maroc - Fédération Royale Marocaine de Football (FRMF) [Fuite de données]
- **Date de publication initiale :** 21 avril 2026

- **Acteur / Groupe :** MDGhost
- **Secteur :** Sport
- **Site web :** [frmf.ma](https://frmf.ma/)
- **Statut :** Claim - Data Sample Published
- **Description :** 1,2 To de données à vendre (10 000 USD). Échantillons : gestion des licences, identités, adresses, téléphones, données de mineurs.

#### 🇲🇦 Maroc - Pharmacie.ma [Fuite de données]
- **Date de publication initiale :** 21 avril 2026


- **Acteur / Groupe :** Tanaka
- **Secteur :** Santé / Pharmacie / E-health
- **Site web :** [pharmacie.ma](https://www.pharmacie.ma)
- **Statut :** Claim - Data Sample Published
- **Description victime :**
  Pharmacie.ma est un portail marocain spécialisé dans les informations pharmaceutiques, les médicaments et les contenus liés à la santé. La plateforme cible notamment les pharmaciens, étudiants en pharmacie et utilisateurs recherchant des informations médicales au Maroc.

- **Description de la fuite :**
  Le 27 janvier 2026, un utilisateur nommé “Tanaka” a publié sur un forum clandestin une revendication attribuée au groupe “Karuhunters”, affirmant qu’une compromission survenue le 29 septembre 2025 aurait entraîné l’exfiltration d’environ 41 772 enregistrements utilisateurs associés à Pharmacie.ma.

- **Analyse des échantillons :**
  Les échantillons SQL analysés contiennent des adresses email, noms, numéros de téléphone, profils “pharmacy_student”, informations géographiques et statuts de comptes utilisateurs.

- **Note CTI :**
  Les données observées semblent correspondre à une base utilisateurs historique associée à Pharmacie.ma. Le volume exact revendiqué reste non vérifié indépendamment.

### 22 avril 2026

#### 🇲🇦 Maroc - Equatorial Coca-Cola Bottling [Ransomware]
- **Date de publication initiale :** 22 avril 2026

- **Groupe ransomware :** worldleaks
- **Secteur :** Agroalimentaire
- **Site web :** [eccbc.com](https://eccbc.com)
- **Statut :** Claim - Unverified
- **Description :** Partenaire embouteilleur de Coca‑Cola en Afrique du Nord et de l’Ouest.

---

### 25 avril 2026

#### 🇧🇯 Bénin - CNSS Bénin [Fuite de données]
- **Date de publication initiale :** 25 avril 2026


- **Acteur / Groupe :** NormalLeVrai
- **Secteur :** Gouvernement / Sécurité sociale
- **Site web :** [cnss.bj](https://www.cnss.bj/)
- **Statut :** Claim - Data Sample Published

- **Description :** Une publication sur un forum cybercriminel revendique la fuite de données issues de la boîte officielle `info@cnss.bj` de la CNSS du Bénin. Les éléments publiés mentionnent environ 5 993 e-mails, 9 019 pièces jointes et plus de 31 000 fichiers analysés pour un volume total estimé à 7,1 Go.

- **Données observées :**
  - cartes de pension
  - certificats de vie
  - passeports et cartes consulaires
  - documents d’identité
  - dossiers allocataires
  - données RH et médicales
  - informations financières et bancaires
  - documents administratifs sensibles

- **Analyse CTI :**
  Les éléments publiés suggèrent une opération automatisée de scraping de messagerie et d’extraction massive de pièces jointes. Les données exposées présentent un risque élevé d’usurpation d’identité, fraude sociale, spear phishing et exploitation de données sensibles liées aux assurés et retraités.
---

### 26 avril 2026

#### 🇪🇬 Égypte - EEC Group [Ransomware]
- **Date de publication initiale :** 26 avril 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Industrie manufacturière
- **Site web :** [eecegypt.com](https://eecegypt.com)
- **Statut :** Claim - Unverified
- **Description :** Conglomérat égyptien d’ingénierie, construction et structures métalliques.

#### 🇲🇦 Maroc - Centre Régional d’Investissement Rabat‑Salé‑Kénitra (CRI) [Fuite de données]
- **Date de publication initiale :** 26 avril 2026

- **Acteur / Groupe :** kutam_dz
- **Secteur :** Administration publique / Investissement / Juridique
- **Site web :** [cri-rsk.ma](https://www.cri-rsk.ma/)
- **Statut :** Claim - Data Sample Published
- **Description :** Expose des données professionnelles (notaires) : noms, téléphones multiples, adresses postales, emails, province, profession.

#### 🇹🇳 Tunisie - Tawjih.tn [Fuite de données]
- **Date de publication initiale :** 26 avril 2026

- **Acteur / Groupe :** mecrobyte
- **Secteur :** Éducation / Orientation académique
- **Site web :** [tawjih.tn](https://tawjih.tn/)
- **Date de la fuite :** 26 Avril 2026
- **Statut :** Claim - Data Sample Published
- **Description :** Tawjih.tn est une plateforme tunisienne d’orientation académique destinée principalement aux étudiants et bacheliers souhaitant préparer leur parcours universitaire et professionnel. L’acteur malveillant affirme disposer d’informations liées aux utilisateurs de la plateforme, potentiellement incluant des données personnelles et académiques. Bien que le contenu complet de la base ne soit pas entièrement exposé dans la publication analysée, les éléments visibles suggèrent une compromission potentielle d’une base backend utilisée pour la gestion des comptes utilisateurs et des services d’orientation académique.

---

### 27 avril 2026

#### 🇪🇬 Égypte - alx-pc.com [Ransomware]
- **Date de publication initiale :** 27 avril 2026

- **Groupe ransomware :** apt73/bashe
- **Secteur :** Pétrole
- **Site web :** [alx-pc.com](https://alx-pc.com)
- **Statut :** Claim - Unverified
- **Description :** Alexandria Petroleum Company, raffinerie publique.

#### 🇬🇭 Ghana - providentgh.com [Ransomware]
- **Date de publication initiale :** 27 avril 2026

- **Groupe ransomware :** apt73/bashe
- **Secteur :** Gestion de patrimoine
- **Site web :** [providentgh.com](https://providentgh.com)
- **Statut :** Claim - Unverified
- **Description :** Compagnie d’assurance privée au Ghana.

#### 🇺🇬 Ouganda - Ministère de l’Agriculture (E‑Extension) [Fuite de données]
- **Date de publication initiale :** 27 avril 2026

- **Acteur / Groupe :** vicmeow
- **Secteur :** Administration publique / Agriculture
- **Site web :** [extension.agriculture.go.ug](https://extension.agriculture.go.ug/)
- **Statut :** Claim - Data Sample Published
- **Description :** Plateforme agricole ougandaise. Expose emails, noms, téléphones, adresses, mots de passe faibles/en clair, token API SMS.

#### 🇳🇬 Nigeria - Ministère du Commerce de l’État d’Oyo [Fuite de données]
- **Date de publication initiale :** 27 avril 2026

- **Acteur / Groupe :** AckLine
- **Secteur :** Administration publique / Commerce
- **Site web :** oyostate.gov.ng
- **Statut :** Claim - Unverified
- **Description :** ~275 000 cartes d’identité commerciales (21,5 Go) : noms, dates de naissance, adresses, professions, photos. Risque critique d’usurpation d’identité.

---

### 28 avril 2026

#### 🇰🇪 Kenya - TikoHUB
- **Date de publication initiale :** 28 avril 2026


- **Date de l'incident :** 28 avril 2026 (date de publication de l'offre d'accès ; compromission initiale non établie)
- **Acteur / Groupe :** DarkMafiaX (compte affiché ; identité et affiliation non vérifiées)
- **Secteur :** Billetterie / Événementiel / Services numériques
- **Site web :** [tikohub.co.ke](https://www.tikohub.co.ke/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Access Sale
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4

- **Description :** **TikoHUB** est une plateforme kényane de **billetterie et de services événementiels** destinée aux organisateurs et aux participants. Son offre est centrée sur la découverte et la gestion d'événements, avec des parcours d'achat ou de participation en ligne. L'existence d'un portail public ne valide toutefois pas les privilèges d'administration prétendument proposés par le vendeur d'accès ([présentation officielle TikoHUB](https://www.tikohub.co.ke/about_us.php)).

- **Vérification indépendante au 18 octobre 2026 :** Aucune preuve publique indépendante d’une vente d’accès à TikoHUB ni communication de la société n’a été identifiée ; la publication suspecte date d’avril 2026 et son intégration au suivi est ultérieure.

  **Incident documenté dans la fiche AFRINTEL :** Une publication attribuée au compte DarkMafiaX propose un accès administrateur présenté comme lié à TikoHUB, une plateforme kényane de billetterie et de gestion d'événements. La publication et les identifiants visibles n'ont pas été testés ; AFRINTEL ne confirme ni leur validité, ni l'accès effectif, ni une compromission de TikoHUB.

- **Analyse :**

  **Observed :** La capture montre une publication intitulée « Admin Access To Tikohub.co.ke | Kenya », datée du 28 avril 2026 à 23:26 selon l'horodatage affiché. Elle contient une URL de ressource d'administration et des champs présentés comme un nom d'utilisateur et un mot de passe. Ces valeurs sont volontairement non reproduites et n'ont pas été testées. La capture a été communiquée à AFRINTEL le 24 septembre 2026.

  **Assumption :** Le domaine `tikohub.co.ke` correspond à une plateforme kényane de billetterie ; cette correspondance rend la cible plausible. La publication peut toutefois être erronée, recyclée, falsifiée ou concerner un accès limité à un composant tiers. La date du 28 avril correspond à la publication observée, pas nécessairement à la compromission initiale.

  **Unknown :** validité actuelle des identifiants, privilèges réels, système concerné, mode d'obtention, durée d'accès, exploitation effective, données consultées ou exfiltrées, confirmation par TikoHUB et éventuelle remédiation restent inconnus.

- **Périmètre de l'échantillon observé :** une capture d'une publication de forum ; aucune connexion, validation d'identifiant, téléchargement, interaction avec l'endpoint ou copie de secret n'a été réalisée.

- **Évaluation des risques :** si l'offre est authentique, un accès administrateur pourrait permettre la modification de contenus, l'accès à des données de clients ou d'organisateurs, la fraude aux billets et la compromission de comptes. Cette fiche ne confirme aucun de ces effets.

- **Recommandations :**
1. Préserver les journaux d'authentification, d'administration, d'API et d'hébergement depuis le 28 avril 2026.
2. Réinitialiser les comptes administrateurs potentiellement concernés et révoquer les sessions selon l'enquête défensive de TikoHUB.
3. Vérifier les changements de privilèges, exports, créations de comptes et modifications de billets ou d'événements.
4. Ne pas tester les identifiants publiés ni ouvrir l'URL sensible depuis la capture.
5. Surveiller l'usurpation, la fraude aux billets et les réutilisations de secrets.

- **Sources / Éléments de preuve :** capture fournie à AFRINTEL le 24 septembre 2026 ; site public [TikoHUB](https://www.tikohub.co.ke/).

### 29 avril 2026

#### 🇲🇦 Maroc - planetsport.ma [Ransomware]
- **Date de publication initiale :** 29 avril 2026

- **Groupe ransomware :** lockbit5
- **Secteur :** Sports
- **Site web :** [planetsport.ma](https://planetsport.ma)
- **Statut :** Claim - Unverified
- **Description :** Leader marocain de la distribution d’articles de sport.

- **Analyse :**
  AFRINTEL documente la publication d’avril comme une revendication ransomware LockBit 5 non vérifiée. Le même domaine, `planetsport.ma`, est apparu dans une publication substantielle de données attribuée à Mozvo en juillet 2026. Cette chronologie soulève l’hypothèse que les données de juillet aient été téléchargées puis republiées ou redistribuées gratuitement par un tiers après une exfiltration antérieure liée à LockBit, ou que Mozvo soit un affilié ou un opérateur associé. AFRINTEL ne dispose d’aucun élément prouvant une relation entre Mozvo et LockBit 5, et la revendication d’avril ne contient aucune preuve indépendante de chiffrement, d’exfiltration ou d’accès initial. Les entrées d’avril et de juillet sont conservées comme deux événements liés mais distincts, dans l’attente d’éléments complémentaires.

#### 🇿🇲 Zambie - zsiclife.co.zm [Ransomware]
- **Date de publication initiale :** 29 avril 2026

- **Groupe ransomware :** krybit
- **Secteur :** Services d’assurance
- **Site web :** [zsiclife.co.zm](https://zsiclife.co.zm)
- **Statut :** Claim - Unverified
- **Description :** Assurance vie et gestion de patrimoine en Zambie.

#### 🇲🇦 Maroc - Fédération Royale Marocaine de Tennis (FRMT) [Fuite de données]
- **Date de publication initiale :** 29 avril 2026

- **Acteur / Groupe :** Keymous
- **Secteur :** Sports
- **Site web :** [frmtennis.ma](https://frmtennis.ma/)
- **Statut :** Claim - Unverified
- **Description :** ~20 000 enregistrements de licenciés : noms, prénoms, clubs, sexe.

#### 🇲🇦 Maroc - Liste de 4 millions d’adresses email marocaines [Fuite de données]
- **Date de publication initiale :** 29 avril 2026

- **Acteur / Groupe :** Rihana
- **Secteur :** Données personnelles / Emailing / Marketing
- **Site web :** N/A
- **Statut :** Claim - Unverified
- **Description :** Une publication sur un forum cybercriminel revendique le partage d’une liste contenant environ 4 millions d’adresses email attribuées à des utilisateurs marocains. L’acteur précise que les données seraient principalement destinées à des campagnes de spam et d’email marketing. L’annonce mentionne plusieurs domaines populaires utilisés au Maroc, notamment Gmail, Hotmail, Outlook, Yahoo et Menara.ma. Aucun organisme spécifique n’est directement identifié comme source de la fuite, ce qui suggère potentiellement une agrégation de données issues de multiples compromissions, collectes OSINT ou anciennes fuites de données. Ce type de dataset peut être exploité pour des campagnes de phishing, spam massif, credential stuffing ou ingénierie sociale ciblée.
----------
