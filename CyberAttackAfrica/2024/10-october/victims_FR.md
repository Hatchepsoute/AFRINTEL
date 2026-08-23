[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%7C%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Cyberattaques en Afrique: Octobre 2024 : Liste de 12 victimes

👉🏾 [**English version available here**](./victims.md)

## Octobre 2024

## Synthèse mensuelle

Octobre 2024 contient **12 fiches incident documentées** : **8 Ransomware**, **4 Data Leak**, **0 Access Sale**, **0 DDoS**, **0 Defacement** et **0 Operational Fraud**, dans **8 pays africains**.

La maturité des preuves varie fortement : National Edging dispose d'un échantillon local de documents internes examiné ; trois Data Leak présentent des échantillons visibles de profondeur variable ; la revendication University of Antananarivo est restée verrouillée et inaccessible ; sept autres listings ransomware restent des revendications non vérifiées.

### 3 Octobre 2024

#### 🇲🇬 Madagascar - Université d'Antananarivo (univ-antananarivo.mg)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Unknown
- **Contexte source:** RainbowBF est le compte du forum affiché comme ayant publié la revendication d'accès à une base verrouillée.
- **Secteur:** Education / University
- **Site web:** [univ-antananarivo.mg](https://www.univ-antananarivo.mg)
- **Statut:** Claim - Unverified
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** L'Université d'Antananarivo est la plus ancienne et la plus grande université publique de Madagascar, regroupant plusieurs facultés et instituts d'enseignement supérieur dans la région de la capitale.
- **Analyse :** AFRINTEL a examiné une publication sur la plateforme Breached, postée par le compte RainbowBF le 3 octobre 2024, intitulée « Madagascar univ-antananarivo.mg Database Access » et classée sous la catégorie de contenu « Breached » de la plateforme. Le contenu sous-jacent est verrouillé derrière le système de crédits internes du forum et n'a pas été débloqué par AFRINTEL ; aucun export de base de données, capture d'écran d'enregistrements ni autre échantillon vérifiable n'était accessible lors de la collecte. AFRINTEL traite ceci comme une revendication non confirmée d'accès à une base de données et ne confirme ni l'existence, ni le périmètre, ni l'authenticité d'une quelconque donnée sous-jacente. Les catégories de données potentiellement concernées et l'impact ne peuvent actuellement pas être évalués car le contenu sous-jacent n'était pas accessible. AFRINTEL ne reproduit aucun contenu de la publication au-delà de son titre et de ses métadonnées.

----------------------------

### 4 Octobre 2024

#### 🇿🇦 Afrique du Sud - Enterpriseoutsourcing
- **Groupe ransomware:** ransomhub
- **Secteur:** Technology / IT
- **Site web:** [enterpriseoutsourcing.com](https://www.enterpriseoutsourcing.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** Enterpriseoutsourcing est une organisation sud-africaine opérant dans le secteur du conseil en technologies de l'information.

----------------------------

- **Note de fiabilité:** La fiche documente une publication ransomware, mais le matériel fourni ne contient ni échantillon technique ni rapport DFIR public permettant de confirmer le chiffrement, l'exfiltration ou une perturbation opérationnelle.
### 5 Octobre 2024

#### 🇿🇦 Afrique du Sud - Winwinza
- **Groupe ransomware:** ransomhub
- **Secteur:** Education / University
- **Site web:** [winwinza.com](https://www.winwinza.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** Winwinza est une organisation sud-africaine opérant dans le secteur de l'éducation.

----------------------------

- **Note de fiabilité:** La fiche documente une publication ransomware, mais le matériel fourni ne contient ni échantillon technique ni rapport DFIR public permettant de confirmer le chiffrement, l'exfiltration ou une perturbation opérationnelle.
### 7 Octobre 2024

#### 🇩🇿 Algérie - Yassir
- **Groupe ransomware:** killsec
- **Secteur:** Technology / IT
- **Site web:** [yassir.com](https://www.yassir.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** Yassir est une super-app algérienne fournissant des services de VTC, livraison, courses et services numériques en Algérie et sur des marchés régionaux.

----------------------------

- **Note de fiabilité:** La fiche documente une publication ransomware, mais le matériel fourni ne contient ni échantillon technique ni rapport DFIR public permettant de confirmer le chiffrement, l'exfiltration ou une perturbation opérationnelle.
### 9 Octobre 2024

#### 🇳🇬 Nigeria - Prestataire non identifié d’établissements de santé
- **Acteur / Groupe:** grep/cn
- **Contexte source:** La publication du 9 octobre a été postée par Tanaka et attribue la fuite à grep/cn.
- **Secteur:** Healthcare / Medical
- **Site web:** Non identifié
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Description victime:** La source décrit un prestataire nigérian non identifié opérant plusieurs établissements de santé. Le nom de l’organisation et les établissements concernés n’ont pas pu être établis à partir des éléments disponibles.
- **Analyse :** Une publication du forum attribuée à Tanaka et datée du 9 octobre 2024 affirme qu’environ 130 000 dossiers de patients provenant de plusieurs établissements de santé nigérians ont été divulgués par l’acteur grep/cn. Le classeur local fourni pour analyse contient 84 lignes de données, et non 129 825 ou 130 000 lignes ; le volume annoncé ne peut donc pas être confirmé indépendamment à partir du fichier disponible. Le classeur contient des champs relatifs à des patients, notamment des noms, identifiants, numéros de téléphone, âge, dates de naissance, sexe, statut matrimonial et identifiants liés aux établissements ; les enregistrements bruts n’ont pas été reproduits. Les éléments soutiennent une revendication d’exposition de données de santé à fort impact potentiel, mais le prestataire exact, le périmètre des établissements, le mode d’obtention, l’exhaustivité et le volume total restent inconnus.

### 9 Octobre 2024

#### 🇿🇦 Afrique du Sud - GMG Mining Supplies
- **Groupe ransomware:** sarcoma
- **Secteur:** Manufacturing / Industry
- **Site web:** [gmgminingsupplies.com](https://www.gmgminingsupplies.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** GMG Mining Machines and Supplies est une entreprise sud-africaine spécialisée dans la fourniture, reconstruction et location d'équipements miniers, machines mobiles sans rail, pièces et services associés.

----------------------------

- **Note de fiabilité:** La fiche documente une publication ransomware, mais le matériel fourni ne contient ni échantillon technique ni rapport DFIR public permettant de confirmer le chiffrement, l'exfiltration ou une perturbation opérationnelle.
### 9 Octobre 2024

#### 🇿🇦 Afrique du Sud - National Edging
- **Groupe ransomware:** sarcoma
- **Secteur:** Manufacturing / Industry
- **Site web:** [nationaledging.com](https://www.nationaledging.com)
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Description victime:** National Edging est une entreprise sud-africaine spécialisée dans la fourniture de chants, adhésifs, matériaux de finition et composants industriels pour les secteurs du meuble, de la cuisine et de l'agencement.
- **Analyse :** AFRINTEL a examiné un échantillon local de documents cohérents avec la revendication du cybercriminel sarcoma, comprenant des scans complets de passeports d'au moins trois personnes (deux ressortissants sud-africains et un ressortissant indien titulaire d'un permis de résidence aux Émirats arabes unis), un contrat signé avec Freitan Group of Companies (Pty) Ltd portant la signature d'un directeur financier, un formulaire de réservation de voyage d'entreprise référençant l'entité juridique National Converting Agencies (Pty) Ltd, une adresse email au domaine nationaledging.co.za ainsi qu'un passeport et un numéro d'identité sud-africains, et un bon de livraison documentant un envoi de produits de chant et de colle entre succursales de l'entreprise (Gauteng) avec une collecte ultérieure référencée au Zimbabwe. La référence directe au domaine nationaledging.co.za, associée à une identité d'entreprise cohérente (National Converting Agencies/National Edging), à du matériel contractuel signé et à plusieurs documents d'identité complets, soutient une évaluation à très haute confiance d'une compromission interne réelle. L'exposition de données complètes de passeport et d'identité nationale pour plusieurs personnes, ainsi que de contrats signés et de dossiers logistiques s'étendant à une chaîne d'approvisionnement transfrontalière (Zimbabwe), crée un risque important de fraude à l'identité, de falsification de documents et d'ingénierie sociale ciblée contre les employés, partenaires commerciaux et voyageurs associés à l'entreprise. AFRINTEL ne reproduit aucun nom, numéro de passeport, numéro d'identité, date de naissance ni coordonnée issus de l'échantillon examiné.

----------------------------

- **Note de fiabilité:** La fiche documente une publication ransomware, mais le matériel fourni ne contient ni échantillon technique ni rapport DFIR public permettant de confirmer le chiffrement, l'exfiltration ou une perturbation opérationnelle.
- **Qualification de la preuve:** L'échantillon examiné soutient fortement une compromission de données internes associée à National Edging. Il n'établit pas indépendamment un chiffrement ransomware, la méthode d'accès initiale ni le volume complet d'exfiltration.
### 11 Octobre 2024

#### 🇬🇭 Ghana - Volta River Authority (VRA)
- **Groupe ransomware:** blacksuit
- **Secteur:** Energy / Utilities
- **Site web:** [vra.com](https://www.vra.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** La Volta River Authority (VRA) est le principal producteur public d'électricité du Ghana, responsable de centrales hydroélectriques, thermiques et d'infrastructures énergétiques stratégiques du pays.

----------------------------

- **Note de fiabilité:** La fiche documente une publication ransomware, mais le matériel fourni ne contient ni échantillon technique ni rapport DFIR public permettant de confirmer le chiffrement, l'exfiltration ou une perturbation opérationnelle.
### 16 Octobre 2024

#### 🇱🇾 Libye - Ministère de l'Intérieur (moi.gov.ly)
- **Groupe ransomware:** killsec
- **Secteur:** Government / Administration
- **Site web:** [moi.gov.ly](https://www.moi.gov.ly)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** Le Ministère de l'Intérieur libyen est l'institution gouvernementale chargée de la sécurité intérieure, des forces de police et de la gestion des affaires administratives sécuritaires du pays.

----------------------------

- **Note de fiabilité:** La fiche documente une publication ransomware, mais le matériel fourni ne contient ni échantillon technique ni rapport DFIR public permettant de confirmer le chiffrement, l'exfiltration ou une perturbation opérationnelle.
### 17 Octobre 2024

#### 🇩🇿 Algérie - Ministère de l'Éducation Nationale (education.gov.dz)
- **Acteur / Groupe:** Moroccan Empire
- **Contexte source:** Republication par AmeliaBeaumont sur un forum cybercriminel ; le post examiné référence un dump plus ancien.
- **Secteur:** Education / University
- **Site web:** [education.gov.dz](https://www.education.gov.dz)
- **Date de la fuite initiale revendiquée:** 06 octobre 2022
- **Date de publication du post examiné:** 17 octobre 2024 (le post inclut directement le lien vers le dump d'origine, initialement partagé le 18 septembre 2023)
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Description victime:** Le Ministère de l'Éducation Nationale est l'administration algérienne chargée du système éducatif public. La publication revendique le vol d'une base de données contenant les informations d'environ 90 000 élèves, incluant des comptes administrateurs et des identifiants de connexion.
- **Analyse :** Le compte AmeliaBeaumont a publié le 17 octobre 2024 une revendication décrivant une intrusion attribuée à l'acteur « Moroccan Empire » et datée du 6 octobre 2022. Le lien de téléchargement d'origine (une adresse .onion sur un forum de fuite) n'étant plus fonctionnel, le post inclut directement un lien vers le dump, initialement partagé le 18 septembre 2023, qui affiche un échantillon SQL/CSV avec un schéma de champs incluant notamment : numéro d'acte de naissance, type de contrat, établissement, commune, nom, prénom (en français et en arabe), date de naissance, lieu de naissance, numéro d'assurance, numéro de téléphone, diplôme, spécialité, identifiants de compte (`compte`, `cle`), adresse email et un champ de mot de passe en clair. Au moins deux enregistrements complets sont visibles dans l'échantillon, comportant des noms, dates de naissance, numéros de téléphone, une adresse email et un mot de passe en texte brut associés à des personnes identifiées.

  La présence d'un schéma cohérent avec un système de gestion scolaire administratif, incluant des données d'identité, de scolarité et des identifiants de connexion en clair, soutient un niveau de confiance élevé quant à l'authenticité d'un accès à une base de données du ministère ou d'un établissement qui lui est rattaché. Le volume total de 90 000 élèves revendiqué n'a pas pu être vérifié indépendamment au-delà de l'échantillon observé. Le fait que le même dump reste partagé et référencé plus de deux ans après la fuite initialement revendiquée indique une recirculation prolongée de ce jeu de données. L'exposition de mots de passe en clair, combinée aux données d'identité et de scolarité, présente un risque élevé de prise de contrôle de comptes, d'usurpation d'identité et de phishing ciblé contre les élèves, leurs familles et le personnel administratif. AFRINTEL ne reproduit aucun nom, date de naissance, numéro de téléphone, adresse email, mot de passe ni autre donnée personnelle issus de l'échantillon examiné.

----------------------------

### 21 Octobre 2024

#### 🇲🇦 Maroc - Résidences universitaires Al Massira
- **Acteur / Groupe:** bxxxx1
- **Secteur:** Education / University
- **Site web:** [ruam.ma](https://ruam.ma)
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak

- **Description :**
  Les Résidences universitaires Al Massira proposent des logements destinés aux étudiants à Kénitra. Le réseau comprend notamment les résidences Al Massira 1, Al Massira 2 et Al Massira 3, situées à proximité des établissements universitaires de la ville.

- **Analyse :**
  Une publication attribuée à bxxxx1 sur un forum cybercriminel présente des adresses électroniques associées à des personnes ayant recherché ou demandé un hébergement auprès des Résidences universitaires Al Massira. L’acteur affirme avoir obtenu les données après s’être connecté au panneau de contrôle de `ruam.ma`, ce qui suggère la compromission possible d’un compte d’administration ou d’une interface de gestion ; la capture ne contient toutefois aucune preuve technique permettant d’identifier la méthode d’accès. L’échantillon visible contient uniquement des adresses électroniques, principalement issues de services de messagerie publics, avec quelques domaines universitaires, administratifs ou professionnels. Aucun mot de passe, numéro d’identité, numéro de téléphone, document étudiant ou renseignement financier n’est visible. La publication indique une extraction en octobre 2024 et comporte un lien vers un fichier texte ainsi qu’un mot de passe d’archive ou d’accès, qu’AFRINTEL ne reproduit pas. Aucun nombre total d’adresses, volume de fichier, prix ou délai n’est indiqué, et la capture ne permet pas d’établir si la liste visible est complète. Les adresses peuvent alimenter des campagnes de phishing imitant les services de logement étudiant, de fausses notifications d’admission ou de paiement et des listes de cibles pour le password spraying. Aucun mot de passe n’étant visible, une prise de contrôle directe de compte ne peut pas être déduite de l’échantillon.

----------------------------

### 25 Octobre 2024

#### 🇪🇬 Égypte - Matouk Bassiouny
- **Groupe ransomware:** raworld
- **Secteur:** Legal / Justice
- **Site web:** [matoukbassiouny.com](https://www.matoukbassiouny.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** Matouk Bassiouny est un important cabinet d'avocats égyptien basé au Caire, reconnu pour le droit des affaires, l'arbitrage, le contentieux et le conseil juridique.

----------------------------

- **Note de fiabilité:** La fiche documente une publication ransomware, mais le matériel fourni ne contient ni échantillon technique ni rapport DFIR public permettant de confirmer le chiffrement, l'exfiltration ou une perturbation opérationnelle.
## ✍🏿 Auteur
*Adama ASSIONGBON*
*Consultant SOC & Cyber Threat Intelligence*
[Profil LinkedIn](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)
