[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Afrique-orange)
![Threat Type](https://img.shields.io/badge/Menace-Ransomware-red)
![Data Source](https://img.shields.io/badge/Source%20des%20données-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Type%20d'Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en Février 2026 (27 fiches)
👉🏾 [**English version available here**](./victims.md)

## Résumé du mois

Février 2026 regroupe **27 dossiers documentés** : **20 Ransomware**, **7 Data Leak**, **0 Access Sale**, **0 DDoS**, **0 Defacement** et **0 Operational Fraud**, concernant **14 pays africains**. Ces dossiers sont des signalements documentaires, pas nécessairement des intrusions indépendantes confirmées.

### Incidents marquants

- **Sénégal :** Green Blood Group revendique l’exfiltration de 139 To attribués à DAF SÉNÉGAL.
- **Somalie, Ghana et Tanzanie :** 0APT a publié trois revendications représentant un volume cumulé de 6,85 To.
- **Aviation :** BlueSky Aviation, Nile Air et Air Côte d’Ivoire ont été revendiquées au cours du mois.
- **Afrique du Sud :** la revendication concernant Diesel-Electric pourrait recouper une autre fiche LockBit 5.0 enregistrée en mars et nécessite une vérification indépendante.

> Les fiches ci-dessous documentent des revendications ou publications observées. Les volumes revendiqués et les compromissions ne sont pas confirmés sans élément indépendant.

## Février 2026

### 01 février 2026

#### 🇸🇴 Somalie - BlueSky Aviation
- **Date de publication initiale :** 1 février 2026

- **Groupe ransomware :** 0APT
- **Secteur :** Aviation
- **Site web :** bluesky-air.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Compagnie aérienne somalienne fournissant des services de transport.

#### 🇪🇬 Égypte - Laboratoires médicaux égyptiens (revendication multi-organisations)
- **Date de publication initiale :** 1 février 2026


- **Acteur / Groupe :** CrowStealer
- **Secteur :** Santé / Laboratoires médicaux
- **Site web :** results.u-carelabs.com ; marzouk-labs.com ; hassablabsresults.com ; mabaralabs-results.com
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d’incident :** Fuite de données
- **Niveau de confiance :** Moyen
- **Niveau d’impact :** Niveau 3

- **Description :**

  La publication propose des données de résultats de patients qui seraient associées à quatre plateformes égyptiennes de laboratoires médicaux.

- **Analyse :**

  Le post revendique 5 529 enregistrements dans un fichier CSV nommé `egy_labs.csv`, couvrant la période de décembre 2025 à janvier 2026. Le schéma affiché comprend le nom du laboratoire, le nom du patient, le numéro de téléphone mobile, le numéro d’admission, la date de visite, le type d’analyse et une référence vers le résultat. L'échantillon présente des enregistrements structurés de laboratoires médicaux, mais l’authenticité, l’exhaustivité, la propriété exacte et le lien indépendant entre les quatre domaines ne sont pas confirmés. AFRINTEL enregistre un seul incident multi-organisations et ne reproduit aucun nom de patient, contact ni lien individuel.

### 02 février 2026

#### 🇪🇬 Égypte - Canadian International College (CIC)
- **Date de publication initiale :** 2 février 2026

- **Acteur / Groupe :** CrowStealer
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [cic-cairo.edu.eg](https://www.cic-cairo.edu.eg/)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Premier fournisseur d'enseignement canadien en Égypte, associé à la Cape Breton University (CBU). La fuite (studentsdata.csv) contient 2 925 enregistrements : noms, filières, niveaux, GPA, années.

#### 🇳🇬 Nigéria / 🇨🇮 Côte d’Ivoire - Jeu de photos de pièces d’identité
- **Date de publication initiale :** 2 février 2026


- **Acteur / Groupe :** azrekx
- **Secteur :** Gouvernement / Administration publique / Documents d’identité
- **Site web :** Non précisé
- **Statut AFRINTEL :** Claim - Unverified
- **Type d’incident :** Fuite de données
- **Niveau de confiance :** Faible
- **Niveau d’impact :** Niveau 3

- **Description :**

  Une publication de forum revendique l’accès à 10 669 photos actuelles de pièces d’identité nigérianes et ivoiriennes, comprenant des images recto-verso. L’auteur affirme que 1 500 photos ont été partagées et qu’un jeu de données supplémentaire est proposé à la vente.

- **Analyse :**

  La publication est enregistrée comme une seule revendication de fuite multi-pays concernant le Nigeria et la Côte d’Ivoire. La preuve fournie montre la déclaration de l’acteur, mais ne permet pas de vérifier indépendamment le jeu de données, les volumes annoncés, les pays représentés dans la collection complète ni le partage allégué de 1 500 photos. AFRINTEL ne collecte ni ne reproduit de photos d’identité ou de données personnelles issues de cette publication.

#### 🇪🇬 Égypte - Heliopolis University
- **Date de publication initiale :** 2 février 2026


- **Acteur / Groupe :** CrowStealer, publication sur un forum cybercriminel
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** Non précisé
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d’incident :** Fuite de données
- **Niveau de confiance :** Élevé
- **Niveau d’impact :** Niveau 3

- **Description :**

  Heliopolis University est une université privée égyptienne établie près du Caire, proposant des programmes en ingénierie, pharmacie, commerce et économie, physiothérapie et agriculture biologique.

- **Analyse :**

  Une publication de forum attribuée à CrowStealer et datée du 02 février 2026 annonce une base associée à Heliopolis University contenant 19 790 enregistrements. Le classeur local fourni pour analyse contient 62 comptes structurés, dont 38 comptes Parent et 24 comptes Student ; le volume complet annoncé n'a pas pu être vérifié indépendamment à partir du fichier disponible.

  Le schéma examiné comprend des noms d'utilisateur, noms, adresses électroniques lorsqu'elles sont renseignées, champs téléphoniques, type d'institution, champs de dernière adresse IP, horodatages de création et état de suspension. Les 62 enregistrements contiennent une valeur de mot de passe stockée, classifiée dans le classeur comme un hash hexadécimal de 32 caractères ou bcrypt (`$2y$`) ; AFRINTEL n'a tenté ni de casser, ni de reproduire, ni de publier ces valeurs. Seules 24 adresses électroniques et 8 dernières adresses IP sont renseignées dans le fichier examiné.

  La combinaison de données de comptes étudiants/parents, de coordonnées et de hashes de mots de passe pourrait faciliter le phishing, le credential stuffing et la prise de contrôle de comptes en cas de réutilisation des mots de passe. Le mode d'obtention exact, l'exhaustivité de la revendication de 19 790 enregistrements et la confirmation indépendante par l'université restent inconnus.

#### 🇪🇬 Égypte - HIMS University
- **Date de publication initiale :** 2 février 2026


- **Acteur / Groupe :** leakdealer, publication sur un forum cybercriminel
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [hims.edu.eg](https://hims.edu.eg)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 4

- **Description :**

  HIMS University est présentée dans la source comme un établissement d'enseignement supérieur égyptien. Le domaine `hims.edu.eg` est observé dans l'échantillon fourni, mais l'identité officielle de l'établissement et l'exhaustivité de l'archive annoncée n'ont pas été vérifiées indépendamment.

- **Analyse :**

  Une publication de forum datée du 02 février 2026 annonce une base prétendument associée à HIMS University, avec un total revendiqué de 28 124 enregistrements et des données personnelles d'étudiants et de membres du personnel, des données financières et des informations liées à une passerelle de paiement. La publication liste des fichiers CSV portant notamment sur les comptes étudiants, les paiements, les privilèges, les soldes, des journaux bancaires, les informations du personnel et les métadonnées système. L'acteur affirme également l'exposition de comptes en clair et d'éléments d'API de paiement ; ces affirmations n'ont pas été vérifiées indépendamment à partir des éléments visibles fournis.

  L'addition des nombres de fichiers affiches dans la source donne 28 004 enregistrements, soit 120 de moins que le total annonce de 28 124. Cette difference, ainsi que l'absence d'une archive examinee, empeche de confirmer le volume et l'etendue complets. Si elle etait authentique, la combinaison de donnees personnelles d'etudiants et de membres du personnel, d'identifiants de comptes, d'informations financieres et d'elements lies au paiement pourrait entrainer des risques importants de phishing, de prise de controle de comptes, de fraude aux paiements et d'acces non autorise supplementaire. AFRINTEL ne reproduit aucune donnee personnelle, aucun identifiant, aucune cle d'API, aucun identifiant national ni aucune donnee financiere de l'echantillon.

### 05 février 2026

#### 🇸🇳 Sénégal - DAF SÉNÉGAL (Direction de l'Administration Générale et de l'Équipement)
- **Date de publication initiale :** 5 février 2026

- **Groupe ransomware :** The Green Blood Group
- **Secteur :** Gouvernement
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Administration gouvernementale sénégalaise. Violation massive incluant les bases de données citoyens et les registres biométriques.

#### 🇬🇭 Ghana - Global Media Alliance
- **Date de publication initiale :** 5 février 2026

- **Groupe ransomware :** 0APT
- **Secteur :** Média
- **Site web :** gmaworld.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Entreprise intégrée de médias et de communications basée au Ghana.

### 06 février 2026

#### 🇹🇿 Tanzanie - Vertex Law Chambers
- **Date de publication initiale :** 6 février 2026

- **Groupe ransomware :** 0APT
- **Secteur :** Juridique
- **Site web :** vertexlaw.co.tz
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Cabinet d'avocats fournissant des services juridiques en Tanzanie.

#### 🇰🇪 Kenya - Wells Fargo
- **Date de publication initiale :** 6 février 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Banque
- **Site web :** fargo.co.ke
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Prestataire de sécurité et logistique, également impliqué dans les services bancaires/financiers au Kenya.

### 08 février 2026

#### 🇲🇦 Maroc - Al Akhawayn University (AUI) [Fuite de données]
- **Date de publication initiale :** 8 février 2026


- **Acteur / Groupe :** anisanas2
- **Secteur :** Éducation / Université
- **Site web :** [Al Akhawayn University (AUI)](https://aui.ma/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Fuite de données

- **Description :** Une publication sur un forum cybercriminel revendique la divulgation d’une base de données attribuée à Al Akhawayn University (AUI), université marocaine située à Ifrane et reconnue comme l’un des établissements académiques les plus prestigieux du pays.

- **Analyse CTI :**
  L’acteur affirme que le précédent leak attribué à AUI était “fabriqué” et présente cette nouvelle base comme “authentique et vérifiée”.

  Les éléments observés suggèrent une compromission potentielle d’environnements académiques ou administratifs liés à :
  - étudiants,
  - comptes utilisateurs,
  - bases administratives,
  - ou systèmes universitaires internes.

  Ce type de fuite peut exposer :
  - données personnelles étudiantes,
  - emails institutionnels,
  - informations académiques,
  - accès internes,
  - ou identifiants réutilisables dans d’autres systèmes.

- **Note CTI :**
  L’authenticité complète du dataset n’est pas confirmée indépendamment à ce stade. Toutefois, l’université ciblée est une institution stratégique du paysage académique marocain, ce qui augmente les risques de spear phishing ciblé, compromission de comptes universitaires et attaques BEC contre étudiants, enseignants ou personnel administratif.
---

### 09 février 2026

#### 🇳🇬 Nigeria - Getly
- **Date de publication initiale :** 9 février 2026

- **Groupe ransomware :** killsec
- **Secteur :** Fintech
- **Site web :** getly.app
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Description victime :** Application nigériane de technologie financière.

- **Analyse :**
  AFRINTEL a consulté un ensemble de documents échantillons associés à cette revendication. Le contenu accessible correspond à des attestations et cartes numériques du numéro d'identification national (NIN) nigérian pour plusieurs personnes, incluant noms complets, numéros NIN, dates de naissance, photographies et, dans certains cas, adresses de résidence. Ces éléments sont cohérents avec des données de vérification d'identité (KYC) collectées par une application fintech lors de l'ouverture de compte. L'exposition de ce type de document crée un risque important d'usurpation d'identité, de prise de contrôle de compte et d'utilisation frauduleuse des numéros d'identification nationaux. AFRINTEL n'a pas eu accès aux systèmes back-end de la plateforme et ne peut pas confirmer le volume total d'enregistrements concernés ni le vecteur d'accès initial.

### 11 février 2026

#### 🇬🇭 Ghana - Ghana Bauxite
- **Date de publication initiale :** 11 février 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Service public
- **Site web :** ghanabauxite.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Entreprise ghanéenne impliquée dans le secteur de l'extraction et de la production de bauxite.

### 12 février 2026

#### 🇳🇬 Nigeria - Midwestern Oil & Gas
- **Date de publication initiale :** 12 février 2026

- **Groupe ransomware :** incransom
- **Secteur :** Énergie
- **Site web :** midwesternog.com
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Description victime :** Entreprise nigériane du secteur pétrolier et gazier.

- **Analyse :**
  AFRINTEL a consulté la fiche du site de fuite du groupe incransom pour Midwestern Oil & Gas, qui indique un chiffre d'affaires d'environ 27,6 millions de dollars. La fiche affiche un large ensemble d'aperçus de documents échantillons couvrant plusieurs catégories : rapports financiers et d'audit internes, rapports d'affaires communautaires et d'engagement des parties prenantes, dossiers HSE et de maintenance des pipelines, documentation technique et d'ingénierie, matériel d'approvisionnement et d'inventaire, ainsi que des photographies du personnel et des opérations sur le terrain. L'étendue de ces catégories suggère un accès large à l'infrastructure de fichiers partagés de l'entreprise plutôt qu'à un seul système. AFRINTEL n'a pas eu accès à l'intégralité des fichiers et ne peut pas confirmer le volume exact de données, l'étendue de l'exfiltration ni le vecteur d'accès initial.

### 13 février 2026

#### 🇪🇬 Égypte - Nile Air
- **Date de publication initiale :** 13 février 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Compagnies aériennes
- **Site web :** nileair.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Compagnie aérienne privée égyptienne basée à l'aéroport international du Caire.

### 14 février 2026

#### 🇲🇺 Maurice - Sands Suites
- **Date de publication initiale :** 14 février 2026

- **Groupe ransomware :** LockBit 5.0.0
- **Secteur :** Hôtellerie
- **Site web :** sands.mu
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Resort de luxe situé à Maurice.

### 15 février 2026

#### 🇿🇦 Afrique du Sud - Municipalité d'Intsika Yethu
- **Date de publication initiale :** 15 février 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Administration locale
- **Site web :** intsikayethu.gov.za
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Municipalité locale dans la province du Cap Oriental en Afrique du Sud.

#### 🇹🇳 Tunisie - BITS
- **Date de publication initiale :** 15 février 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Conseil en technologies
- **Site web :** bits.com.tn
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Cabinet tunisien de conseil et de services informatiques.

### 17 février 2026

#### 🇪🇬 Égypte - sodic.com
- **Date de publication initiale :** 17 février 2026

- **Groupe ransomware :** payload
- **Secteur :** Immobilier
- **Site web :** sodic.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** L'une des plus grandes sociétés égyptiennes de développement immobilier.

### 18 février 2026

#### 🇸🇩 Soudan - Amtaar Investment
- **Date de publication initiale :** 18 février 2026

- **Groupe ransomware :** apt73/bashe
- **Secteur :** Agriculture / Agro-industrie
- **Site web :** amtaar.com
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Description victime :** Société de conseil et d'investissement agricole gérant 6 000 hectares de terres irriguées au Soudan, acteur clé de la sécurité alimentaire nationale.

### 19 février 2026

#### 🇨🇮 Côte d'Ivoire - aircotedivoire.com
- **Date de publication initiale :** 19 février 2026

- **Groupe ransomware :** incransom
- **Secteur :** Compagnies aériennes
- **Site web :** aircotedivoire.com
- **Statut :** Data Fully Published
- **Type d'incident :** Ransomware
- **Description victime :** Compagnie aérienne nationale de la Côte d'Ivoire.

- **Analyse :**
  AFRINTEL a consulté la fiche du site de fuite du groupe incransom (INC Ransom) pour cette victime, répertoriée dans la section Disclosures du groupe. La fiche indique un chiffre d'affaires annuel estimé à 40,5 millions de dollars, environ 1 000 employés et un siège à Abidjan, et confirme une divulgation de données d'environ 208 Go (208 351 284 086 octets) faisant suite à une attaque par ransomware contre la compagnie aérienne. AFRINTEL a également consulté un échantillon de données distinct de la fiche du site de fuite : un document PDF généré par Microsoft Access, intitulé « État d'opération », correspondant à un ordre de virement bancaire de paie daté du 21 juin 2022 et couvrant 529 salariés d'Air Côte d'Ivoire, pour un montant total cumulé de 676 139 136 (devise non précisée dans le document, cohérente avec le FCFA). Chaque ligne indique un nom complet, un matricule interne, la banque bénéficiaire et un relevé d'identité bancaire (RIB) complet, ainsi que le montant individuel du virement. Le nom du fichier source référencé dans le document (« E:\VIREMENTS SALAIRES JUIN 2022.txt ») est cohérent avec un export réalisé depuis l'environnement de gestion de la paie ou de virement de masse de la compagnie. AFRINTEL ne reproduit aucun nom, matricule ni coordonnée bancaire individuelle issus de cet échantillon. Cet élément, daté de 2022, confirme une exposition de données financières et RH internes distincte de la seule annonce du site de fuite, mais ne permet pas de déterminer si l'ensemble du volume revendiqué (208 Go) porte sur ce même type de contenu, ni de confirmer le vecteur d'accès initial.

### 20 février 2026

#### 🇲🇦 Maroc - Shora Advisory
- **Date de publication initiale :** 20 février 2026

- **Groupe ransomware :** tengu
- **Secteur :** Comptabilité
- **Site web :** shora.ma
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Description victime :** Cabinet marocain d'expertise comptable et de conseil financier.

- **Analyse :**
  AFRINTEL a consulté la fiche du site de fuite du groupe tengu ainsi que des documents échantillons pour cette victime. Le contenu comprend une arborescence de dossiers clients organisée par exercice comptable (dossiers « ARRETE DES COMPTES » 2018 à 2020) et par catégorie de client (associations, établissements publics, personnes physiques et sociétés), aux côtés de dossiers marketing, RH et administratifs, pour une archive globale décrite comme représentant environ 23,5 Go répartis sur environ 16 000 fichiers et 2 000 dossiers. Les documents échantillons individuels incluent un bordereau de paiement CNSS émis au nom de Shora Auditing SARL ainsi que de la correspondance client interne. Shora exerçant une activité de cabinet comptable et d'audit, cette exposition risque de concerner la confidentialité des dossiers financiers de nombreuses organisations clientes tierces, et pas seulement de Shora elle-même. AFRINTEL n'a pas eu accès à l'archive complète et ne peut pas confirmer l'étendue exacte des données clients concernées ni le vecteur d'accès initial.

#### 🇪🇬 Égypte - moa.gov.eg (Ministère de l'Agriculture)
- **Date de publication initiale :** 20 février 2026

- **Groupe ransomware :** LockBit 5.0.0
- **Secteur :** Gouvernement
- **Site web :** moa.gov.eg
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Ministère égyptien de l'Agriculture et de la Mise en valeur des terres.

### 22 février 2026

#### 🇳🇦 Namibie - CYMOT
- **Date de publication initiale :** 22 février 2026

- **Groupe ransomware :** qilin
- **Secteur :** Commerce de détail
- **Site web :** cymot.com
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Fournisseur namibien de pièces détachées, d'outils et d'équipements.

### 23 février 2026

#### 🇲🇦 Maroc - Chezpara.ma [Fuite de données]
- **Date de publication initiale :** 23 février 2026

- **Acteur / Groupe :** Richard2002
- **Secteur :** Pharmacie en ligne / E‑commerce santé
- **Site web :** [chezpara.ma](https://chezpara.ma/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Fuite de données
- **Description :** ~400 000 enregistrements clients : noms, téléphones, adresses détaillées, infos de livraison, commentaires de commandes.

---

### 24 février 2026

#### 🇿🇦 Afrique du Sud - EnerTec
- **Date de publication initiale :** 24 février 2026

- **Groupe ransomware :** vect
- **Secteur :** Énergie
- **Site web :** enertec.co.za
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Entreprise sud-africaine de solutions énergétiques et de distribution de batteries.

### 27 février 2026

#### 🇿🇦 Afrique du Sud - Diesel-Electric
- **Date de publication initiale :** 27 février 2026

- **Groupe ransomware :** LockBit 5.0.0
- **Secteur :** Automobile
- **Site web :** diesel-electric.co.za
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description victime :** Important distributeur en Afrique du Sud spécialisé dans les composants automobiles.
