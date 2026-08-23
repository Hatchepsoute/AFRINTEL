[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%7C%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes de cyberattaques en Afrique - Février 2024 (12 victimes)
👉🏾 [**English version available here**](./victims.md)

## Synthèse mensuelle

Février 2024 contient **12 fiches incident documentées** : **7 Ransomware**, **5 Data Leak**, **0 Access Sale**, **0 DDoS**, **0 Defacement** et **0 Operational Fraud**, dans **7 pays africains**.

### 1 Février 2024

#### 🇪🇬 Égypte - 8WORX
- **Date de publication de la source:** 30 juin 2023
- **Date de découverte AFRINTEL:** 1 février 2024
- **Acteur / Groupe:** Tanaka
- **Secteur:** Technology / IT
- **Site web:** [8worx.com](https://8worx.com)
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Description victime:** 8WORX est un prestataire de solutions technologiques légalement enregistré dans le Delaware, aux États-Unis, qui déclare concentrer son activité sur l'Égypte et le Moyen-Orient, en développant des applications web et des systèmes pour des clients des secteurs privé et public.
- **Analyse:** La publication est signée par le compte Tanaka, qui porte un badge de modérateur sur le forum, si bien que l'acteur à l'origine de l'intrusion n'est pas identifié. La publication sur le forum annonce un export SQL de 1,3 Go daté de 2023, comptant environ 4 millions de lignes réparties sur des tables incluant des numéros de téléphone, des journaux d'activité et des comptes sociaux, structurées autour d'un module « Leads » cohérent avec un système de CRM ou de gestion de prospects. L'échantillon visible montre des instructions SQL INSERT à l'apparence authentique, avec des champs détaillés de contact, de suivi d'activité et de compte, et une grande part des enregistrements téléphoniques porte un indicatif pays Égypte (EG), cohérent avec le positionnement régional déclaré de 8WORX. La cohérence structurelle du schéma et la plausibilité des enregistrements échantillonnés soutiennent une évaluation à confiance élevée quant à l'authenticité de l'échantillon, bien qu'AFRINTEL n'ait pas confirmé indépendamment l'intrusion, l'étendue complète de la base sous-jacente, ni l'exhaustivité du volume annoncé de 4 millions de lignes. L'exposition de ce jeu de données combinerait numéros de téléphone, adresses email, activité de prospects et de comptes, et références internes d'utilisateurs pour un très grand nombre d'individus, créant un risque important de phishing ciblé, d'ingénierie sociale et de fraude. AFRINTEL ne reproduit aucun numéro de téléphone, adresse email, nom ni enregistrement interne issu de l'échantillon.

----------------------------

### 6 Février 2024

#### 🇪🇬 Égypte - ArpuPlus
- **Groupe ransomware:** medusa
- **Secteur:** Technology / IT
- **Site web:** [arpuplus.com](https://www.arpuplus.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** ArpuPlus, fondée en 2003 au Caire en tant que filiale du groupe A15, est un constructeur de projets numériques (*venture builder*) et un fournisseur de services mobiles de premier plan dans la région MENA. Présente via 11 bureaux, elle fournit des plateformes de vidéo à la demande, de distribution musicale, de télésanté et de communication d'entreprise.

----------------------------

### 10 Février 2024

#### 🇹🇳 Tunisie - SOPEM Tunisie
- **Groupe ransomware:** hunters
- **Secteur:** Manufacturing / Industry
- **Site web:** [sopem.com.tn](https://www.sopem.com.tn)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** SOPEM Tunisie (Société Tunisienne de Profilage de Métaux) est une entreprise manufacturière spécialisée dans le profilage et la transformation industrielle des métaux. Basée en Tunisie, elle fournit des composants industriels et des structures métalliques pour les secteurs du bâtiment et de l'ingénierie.

----------------------------

### 13 Février 2024

#### 🇿🇦 Afrique du Sud - The Aurum Institute
- **Groupe ransomware:** lockbit3
- **Secteur:** Healthcare / Medical
- **Site web:** [auruminstitute.org](https://www.auruminstitute.org)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** The Aurum Institute est une organisation africaine d'utilité publique de premier plan fondée en 1998 et basée à Johannesburg. Axée sur la recherche médicale et la santé publique, l'organisation génère des données scientifiques et déploie des programmes sanitaires mondiaux d'envergure, notamment contre le VIH et la tuberculose.

----------------------------

### 16 Février 2024

#### 🇿🇦 Afrique du Sud - Government Pensions Administration Agency (GPAA) / Government Employees Pension Fund (GEPF)
- **Date de l'incident:** 16 février 2024
- **Date de publication initiale:** 12 mars 2024
- **Date de correction AFRINTEL:** 23 août 2026
- **Groupe ransomware:** lockbit3
- **Secteur:** Government / Administration
- **Site web:** [gepf.co.za](https://www.gepf.co.za/)
- **Statut:** Victim Confirmed + Threat Actor Claim
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Note de preuve:** L'événement ransomware et la compromission de données personnelles sont confirmés par la victime. Les affirmations de l'acteur sur l'exhaustivité ou une portée supplémentaire des données publiées restent séparées des faits confirmés.
- **Description victime:** La GPAA administre les prestations de retraite pour le compte du GEPF, l'un des plus importants fonds de pension d'Afrique, au service des fonctionnaires, retraités et bénéficiaires.
- **Analyse:** La GPAA a subi une cyberattaque le 16 février 2024. Le GEPF a ensuite confirmé que des criminels avaient lancé un ransomware contre les systèmes de la GPAA et qu'environ **168 000 dossiers de personnes** avaient été consultés. Les catégories de données confirmées incluent des informations d'identité, de pension, d'emploi, de salaire, d'état civil, bancaires et fiscales. LockBit a publié des données et revendiqué l'attaque. L'événement ransomware et la compromission de données sont confirmés par la victime ; AFRINTEL conserve l'impact confirmé de 168 000 dossiers séparément de toute revendication plus large de l'acteur.
- **Sources publiques:** [Notification officielle GEPF](https://www.gepf.co.za/notice/notification-of-security-compromise-as-per-section-22-of-the-protection-of-personal-information-act-4-of-2013-popia/2/) | [Communiqué GEPF](https://www.gepf.co.za/government-pensions-administration-agency-gpaa-data-breach/)

----------------------------

### 23 Février 2024

#### 🇿🇦 Afrique du Sud - Companies and Intellectual Property Commission (CIPC)
- **Date de l'incident:** 23 février 2024
- **Date de publication initiale:** 29 février 2024
- **Date de correction AFRINTEL:** 23 août 2026
- **Acteur / Groupe:** Unknown
- **Secteur:** Government / Administration
- **Site web:** [cipc.co.za](https://www.cipc.co.za/)
- **Statut:** Victim Confirmed - Multi-effect Incident
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Note de taxonomie:** `Data Leak` est retenu comme type AFRINTEL principal car l'accès non autorisé à des informations personnelles et leur exposition sont étayés par des sources officielles. Le comportement d'extorsion et le défacement du site sont conservés comme effets secondaires ; le déploiement d'un malware ransomware n'est pas établi.
- **Description victime:** La CIPC est l'autorité sud-africaine chargée des sociétés et de la propriété intellectuelle et conserve des dossiers relatifs aux entreprises, clients et employés.
- **Analyse:** Les rapports officiels de la CIPC indiquent qu'une violation de données a été détectée le 23 février 2024 et impliquait un accès non autorisé à ses systèmes. Des informations personnelles de clients et d'employés ont été illégalement consultées et exposées. Le rapport annuel de la CIPC précise également que les intrus ont menacé de chiffrer et de publier les données contre rançon, défiguré le site e-Services et envoyé des courriels malveillants à des employés. Les systèmes ont été isolés puis restaurés et les autorités policières et réglementaires ont été notifiées. L'attaquant reste non attribué publiquement. AFRINTEL enregistre donc `Data Leak` comme type contrôlé principal et conserve l'extorsion et le défacement comme effets secondaires.
- **Sources publiques:** [Notification POPIA CIPC](https://www.cipc.co.za/?p=20614) | [Rapport Q4 CIPC](https://www.cipc.co.za/wp-content/uploads/2026/04/CIPC_2023-24_Q4-Report-Narrative_vf_20240430.pdf) | [Rapport annuel CIPC](https://www.cipc.co.za/wp-content/uploads/2025/01/CIPC-Annual-Report-2023-2024.pdf)

----------------------------

### Février 2024 - date exacte de l'incident non établie publiquement

#### 🇲🇼 Malawi - Department of Immigration and Citizenship Services - Passport Issuance System
- **Date de l'incident:** Février 2024 - date exacte non établie publiquement
- **Date de publication initiale:** 21 février 2024
- **Date de correction AFRINTEL:** 23 août 2026
- **Acteur / Groupe:** Unknown
- **Secteur:** Government / Administration
- **Site web:** [immigration.gov.mw](https://www.immigration.gov.mw/)
- **Statut:** Government Confirmed - Technical Details Contested
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Note de taxonomie:** `Ransomware` est un mapping AFRINTEL principal provisoire car le gouvernement a publiquement décrit une violation de cybersécurité accompagnée d'une demande de rançon. La cause racine exacte, l'identité de l'attaquant et le déploiement technique d'un ransomware restent contestés ou non résolus.
- **Description victime:** Le Department of Immigration and Citizenship Services du Malawi exploite l'infrastructure nationale de délivrance des passeports.
- **Analyse:** Le président du Malawi a publiquement décrit l'indisponibilité du système de passeports comme une grave violation de cybersécurité et déclaré que des attaquants exigeaient une rançon. Le Department of Immigration a ensuite confirmé que les services de passeports avaient été perturbés par une violation de cybersécurité et que les données démographiques perdues avaient été récupérées. Toutefois, des organisations de la société civile et des déclarations de fournisseurs ont contesté certains aspects du récit technique gouvernemental et suggéré que des problèmes de licence ou de gestion du système avaient également pu contribuer à la panne. AFRINTEL enregistre donc la perturbation du service et la déclaration officielle de violation comme confirmées tout en maintenant la cause technique exacte et le déploiement d'un ransomware comme contestés.
- **Sources publiques:** [Communiqué du gouvernement du Malawi](https://www.malawi.gov.mw/index.php/resources/documents/press-releases?download=145%3Aofficial-passport-press-release-from-the-department-of-immigration-and-citizenship-services) | [Malawi Broadcasting Corporation](https://mbc.mw/?p=10487) | [Contexte VOA](https://www.voanews.com/a/some-question-malawi-president-s-claim-that-cyberattack-caused-passport-problems-/7498879.html)

----------------------------

### 24 Février 2024

#### 🇪🇹 Éthiopie - Regional Trade and Integration Ministries of Ethiopia
- **Date de publication de la source:** 24 août 2023
- **Date de découverte AFRINTEL:** 24 février 2024
- **Acteur / Groupe:** ThreatSec
- **Secteur:** Government / Administration
- **Sites web:** [etrade.gov.et](https://etrade.gov.et) and [eris.efda.gov.et](https://eris.efda.gov.et)
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Description victime:** Les portails gouvernementaux éthiopiens mentionnés dans la publication soutiennent le commerce régional, l’intégration, l’enregistrement des importateurs/exportateurs et les processus de certification associés.
- **Analyse:** La publication affirme que ThreatSec a compromis les deux portails gouvernementaux éthiopiens et collecté 43 fichiers, notamment des documents gouvernementaux, des PDF et des images contenant des identifiants administratifs. La capture confirme l’existence de la publication et le périmètre annoncé, mais AFRINTEL n’a pas vérifié indépendamment la compromission, l’origine des fichiers, ni l’exhaustivité et l’authenticité de l’archive. Les impacts possibles comprennent l’exposition de documents officiels, le phishing ciblé, la fraude à l’identité et l’utilisation abusive d’informations d’enregistrement commercial. Les identifiants visibles dans la source ne sont pas reproduits.

----------------------------

### 24 Février 2024

#### 🇬🇭 Ghana - National Teaching Council (tpg.ntc.gov.gh)
- **Date de publication de la source:** 16 juillet 2023
- **Date de découverte AFRINTEL:** 24 février 2024
- **Acteur / Groupe:** Tanaka
- **Secteur:** Government / Administration
- **Site web:** [tpg.ntc.gov.gh](https://tpg.ntc.gov.gh/)
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Description victime:** Le National Teaching Council (NTC) du Ghana est l'organisme statutaire chargé de délivrer les licences et de réguler la profession enseignante. Le portail tpg.ntc.gov.gh soutient son processus de « Teaching Practice Guidelines » destiné aux élèves-enseignants inscrits dans les collèges d'éducation du pays.
- **Analyse:** La publication du forum, attribuée au compte modérateur Tanaka, annonce un export SQL de la table `students`, daté de données 2019 et annoncé à environ 41 000 lignes. L'échantillon visible montre des instructions `INSERT INTO` d'apparence authentique avec un large ensemble de champs (identifiant étudiant, statut, noms, numéro d'index, sexe, téléphone, programme, niveau, date de naissance, nationalité, statut matrimonial, lieu de résidence, ville d'origine, adresse de contact, région, email, totaux de crédits et de moyenne, collège et promotion, classe, statut de handicap, statut d'examen, établissement précédent, dates de certificat et champs d'inscription associés), renseigné avec des enregistrements individuels d'élèves-enseignants répartis sur plusieurs collèges d'éducation. La cohérence structurelle de l'ensemble de champs et la plausibilité des codes de collèges et des valeurs enregistrées soutiennent un niveau de confiance élevé quant à l'authenticité de l'échantillon, bien qu'AFRINTEL n'ait pas confirmé indépendamment l'intrusion, le périmètre complet de la base sous-jacente, ni l'exhaustivité du volume annoncé de 41 000 lignes. L'exposition de ce jeu de données combinerait noms complets, coordonnées, origine nationale, statut matrimonial, adresse du domicile et dossiers académiques pour un grand nombre d'élèves-enseignants, créant un risque significatif de fraude à l'identité, de phishing ciblé et d'usurpation d'identité. AFRINTEL ne reproduit aucun nom d'étudiant, adresse email, numéro de téléphone, adresse ni dossier académique issu de l'échantillon examiné.

### 24 Février 2024

#### 🇨🇮 Côte d'Ivoire - Agence Emploi Jeunes
- **Date de publication de la source:** 21 juillet 2023
- **Date de découverte AFRINTEL:** 24 février 2024
- **Acteur / Groupe:** Tanaka
- **Secteur:** Government / Administration
- **Site web:** [agenceemploijeunes.ci](https://agenceemploijeunes.ci)
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Description victime:** L'Agence Emploi Jeunes est un service public ivoirien consacré à l'accompagnement des jeunes vers l'emploi et les opportunités professionnelles.
- **Analyse:** La publication sur le forum annonce un fichier SQL de 3,2 Go associé à agenceemploijeunes.ci, avec environ 2 300 lignes et 296 000 utilisateurs ou adresses email uniques. Le schéma visible comprend des champs liés aux candidats, aux comptes utilisateurs, à l'identité, aux coordonnées, à la formation, à l'emploi et au placement, tandis que la capture montre des instructions SQL INSERT contenant des enregistrements personnels. Les chiffres annoncés sont incohérents entre eux et le jeu de données complet n'a pas été vérifié indépendamment ; AFRINTEL classe donc cette publication comme un échantillon de données à confiance moyenne, et non comme une compromission confirmée. Si les données sont authentiques, elles pourraient faciliter la fraude à l'identité, le phishing ciblé, l'ingénierie sociale liée à l'emploi et l'exploitation d'informations sur les demandeurs d'emploi. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone, mot de passe ni autre donnée personnelle issue de l'échantillon.

----------------------------


----------------------------

### 27 Février 2024

#### 🇨🇮 Côte d'Ivoire - Nouvelle Parfumerie Gandour (NPGCI)
- **Groupe ransomware:** lockbit3
- **Secteur:** Manufacturing / Industry
- **Site web:** [npgandour.com](https://npgandour.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** La Nouvelle Parfumerie Gandour (NPGCI) est une entreprise industrielle cosmétique leader en Afrique de l'Ouest, basée dans la zone industrielle de Yopougon à Abidjan, en Côte d'Ivoire. Fondée sur des principes de fabrication rigoureux, elle produit une vaste gamme de produits corporels, capillaires, bucco-dentaires et de parfumerie.

----------------------------

### 29 Février 2024

#### 🇿🇦 Afrique du Sud - ERWAT (Ekurhuleni Water Care Company)
- **Groupe ransomware:** dragonforce
- **Secteur:** Water / Utilities
- **Site web:** [erwat.co.za](https://erwat.co.za)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** ERWAT (Ekurhuleni Water Care Company) est une entreprise publique sud-africaine de premier plan créée en 1992, spécialisée dans l'assainissement et le traitement des eaux usées industrielles et domestiques. Elle assure la gestion des infrastructures d'épuration pour des milliers d'industries et plus de 3,5 millions d'habitants.

----------------------------

## ✍🏿 Author
*Adama ASSIONGBON*
*Consultant SOC & Cyber Threat Intelligence*
[LinkedIn profile](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)
