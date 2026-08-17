[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Cyberattaques en Afrique: Février 2024 : liste des 9 victimes

### 1 Février 2024

#### 🇪🇬 Égypte - 8WORX
- **Date de publication de la source :** 30 juin 2023
- **Date de découverte AFRINTEL :** 1 février 2024
- **Acteur / Groupe :** Tanaka, publication sur un forum clandestin
- **Secteur :** Technologies / Services logiciels
- **Site web :** [8worx.com](https://8worx.com)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Description victime :** 8WORX est un prestataire de solutions technologiques légalement enregistré dans le Delaware, aux États-Unis, qui déclare concentrer son activité sur l'Égypte et le Moyen-Orient, en développant des applications web et des systèmes pour des clients des secteurs privé et public.
- **Analyse :** La publication est signée par le compte Tanaka, qui porte un badge de modérateur sur le forum, si bien que l'acteur à l'origine de l'intrusion n'est pas identifié. La publication sur le forum annonce un export SQL de 1,3 Go daté de 2023, comptant environ 4 millions de lignes réparties sur des tables incluant des numéros de téléphone, des journaux d'activité et des comptes sociaux, structurées autour d'un module « Leads » cohérent avec un système de CRM ou de gestion de prospects. L'échantillon visible montre des instructions SQL INSERT à l'apparence authentique, avec des champs détaillés de contact, de suivi d'activité et de compte, et une grande part des enregistrements téléphoniques porte un indicatif pays Égypte (EG), cohérent avec le positionnement régional déclaré de 8WORX. La cohérence structurelle du schéma et la plausibilité des enregistrements échantillonnés soutiennent une évaluation à confiance élevée quant à l'authenticité de l'échantillon, bien qu'AFRINTEL n'ait pas confirmé indépendamment l'intrusion, l'étendue complète de la base sous-jacente, ni l'exhaustivité du volume annoncé de 4 millions de lignes. L'exposition de ce jeu de données combinerait numéros de téléphone, adresses email, activité de prospects et de comptes, et références internes d'utilisateurs pour un très grand nombre d'individus, créant un risque important de phishing ciblé, d'ingénierie sociale et de fraude. AFRINTEL ne reproduit aucun numéro de téléphone, adresse email, nom ni enregistrement interne issu de l'échantillon.

----------------------------

### 6 Février 2024

#### 🇪🇬 Égypte - ArpuPlus
- **Groupe ransomware :** medusa
- **Secteur :** Technologies numériques & Télécoms
- **Site web :** [arpuplus.com](https://www.arpuplus.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** ArpuPlus, fondée en 2003 au Caire en tant que filiale du groupe A15, est un constructeur de projets numériques (*venture builder*) et un fournisseur de services mobiles de premier plan dans la région MENA. Présente via 11 bureaux, elle fournit des plateformes de vidéo à la demande, de distribution musicale, de télésanté et de communication d'entreprise.

----------------------------

### 10 Février 2024

#### 🇹🇳 Tunisie - SOPEM Tunisie
- **Groupe ransomware :** hunters
- **Secteur :** Industrie manufacturière (Métallurgie)
- **Site web :** [sopem.com.tn](https://www.sopem.com.tn)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** SOPEM Tunisie (Société Tunisienne de Profilage de Métaux) est une entreprise manufacturière spécialisée dans le profilage et la transformation industrielle des métaux. Basée en Tunisie, elle fournit des composants industriels et des structures métalliques pour les secteurs du bâtiment et de l'ingénierie.

----------------------------

### 13 Février 2024

#### 🇿🇦 Afrique du Sud - The Aurum Institute
- **Groupe ransomware :** lockbit3
- **Secteur :** Santé publique & Recherche médicale
- **Site web :** [auruminstitute.org](https://www.auruminstitute.org)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** The Aurum Institute est une organisation africaine d'utilité publique de premier plan fondée en 1998 et basée à Johannesburg. Axée sur la recherche médicale et la santé publique, l'organisation génère des données scientifiques et déploie des programmes sanitaires mondiaux d'envergure, notamment contre le VIH et la tuberculose.

----------------------------

### 24 Février 2024

#### 🇪🇹 Éthiopie - Regional Trade and Integration Ministries of Ethiopia
- **Date de publication de la source :** 24 août 2023
- **Date de découverte AFRINTEL :** 24 février 2024
- **Acteur / Groupe :** ThreatSec, publication de Tanaka sur un forum clandestin
- **Secteur :** Gouvernement / Administration publique
- **Sites web :** [etrade.gov.et](https://etrade.gov.et) et [eris.efda.gov.et](https://eris.efda.gov.et)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d’impact :** Level 3
- **Type d’incident :** Fuite de données
- **Description victime :** Les portails gouvernementaux éthiopiens mentionnés dans la publication soutiennent le commerce régional, l’intégration, l’enregistrement des importateurs/exportateurs et les processus de certification associés.
- **Analyse :** La publication affirme que ThreatSec a compromis les deux portails gouvernementaux éthiopiens et collecté 43 fichiers, notamment des documents gouvernementaux, des PDF et des images contenant des identifiants administratifs. La capture confirme l’existence de la publication et le périmètre annoncé, mais AFRINTEL n’a pas vérifié indépendamment la compromission, l’origine des fichiers, ni l’exhaustivité et l’authenticité de l’archive. Les impacts possibles comprennent l’exposition de documents officiels, le phishing ciblé, la fraude à l’identité et l’utilisation abusive d’informations d’enregistrement commercial. Les identifiants visibles dans la source ne sont pas reproduits.

----------------------------

### 24 Février 2024

#### 🇬🇭 Ghana - National Teaching Council (tpg.ntc.gov.gh)
- **Date de publication de la source :** 16 juillet 2023
- **Date de découverte AFRINTEL :** 24 février 2024
- **Acteur / Groupe :** Tanaka, publication sur un forum clandestin
- **Secteur :** Gouvernement / Éducation (régulation de la formation des enseignants)
- **Site web :** [tpg.ntc.gov.gh](https://tpg.ntc.gov.gh/)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Description victime :** Le National Teaching Council (NTC) du Ghana est l'organisme statutaire chargé de délivrer les licences et de réguler la profession enseignante. Le portail tpg.ntc.gov.gh soutient son processus de « Teaching Practice Guidelines » destiné aux élèves-enseignants inscrits dans les collèges d'éducation du pays.
- **Analyse :** La publication du forum, attribuée au compte modérateur Tanaka, annonce un export SQL de la table `students`, daté de données 2019 et annoncé à environ 41 000 lignes. L'échantillon visible montre des instructions `INSERT INTO` d'apparence authentique avec un large ensemble de champs (identifiant étudiant, statut, noms, numéro d'index, sexe, téléphone, programme, niveau, date de naissance, nationalité, statut matrimonial, lieu de résidence, ville d'origine, adresse de contact, région, email, totaux de crédits et de moyenne, collège et promotion, classe, statut de handicap, statut d'examen, établissement précédent, dates de certificat et champs d'inscription associés), renseigné avec des enregistrements individuels d'élèves-enseignants répartis sur plusieurs collèges d'éducation. La cohérence structurelle de l'ensemble de champs et la plausibilité des codes de collèges et des valeurs enregistrées soutiennent un niveau de confiance élevé quant à l'authenticité de l'échantillon, bien qu'AFRINTEL n'ait pas confirmé indépendamment l'intrusion, le périmètre complet de la base sous-jacente, ni l'exhaustivité du volume annoncé de 41 000 lignes. L'exposition de ce jeu de données combinerait noms complets, coordonnées, origine nationale, statut matrimonial, adresse du domicile et dossiers académiques pour un grand nombre d'élèves-enseignants, créant un risque significatif de fraude à l'identité, de phishing ciblé et d'usurpation d'identité. AFRINTEL ne reproduit aucun nom d'étudiant, adresse email, numéro de téléphone, adresse ni dossier académique issu de l'échantillon examiné.

### 24 Février 2024

#### 🇨🇮 Côte d'Ivoire - Agence Emploi Jeunes
- **Date de publication de la source :** 21 juillet 2023
- **Date de découverte AFRINTEL :** 24 février 2024
- **Acteur / Groupe :** Tanaka, publication sur un forum clandestin
- **Secteur :** Gouvernement / Services d'emploi
- **Site web :** [agenceemploijeunes.ci](https://agenceemploijeunes.ci)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Description victime :** L'Agence Emploi Jeunes est un service public ivoirien consacré à l'accompagnement des jeunes vers l'emploi et les opportunités professionnelles.
- **Analyse :** La publication sur le forum annonce un fichier SQL de 3,2 Go associé à agenceemploijeunes.ci, avec environ 2 300 lignes et 296 000 utilisateurs ou adresses email uniques. Le schéma visible comprend des champs liés aux candidats, aux comptes utilisateurs, à l'identité, aux coordonnées, à la formation, à l'emploi et au placement, tandis que la capture montre des instructions SQL INSERT contenant des enregistrements personnels. Les chiffres annoncés sont incohérents entre eux et le jeu de données complet n'a pas été vérifié indépendamment ; AFRINTEL classe donc cette publication comme un échantillon de données à confiance moyenne, et non comme une compromission confirmée. Si les données sont authentiques, elles pourraient faciliter la fraude à l'identité, le phishing ciblé, l'ingénierie sociale liée à l'emploi et l'exploitation d'informations sur les demandeurs d'emploi. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone, mot de passe ni autre donnée personnelle issue de l'échantillon.

----------------------------


----------------------------

### 27 Février 2024

#### 🇨🇮 Côte d'Ivoire - Nouvelle Parfumerie Gandour (NPGCI)
- **Groupe ransomware :** lockbit3
- **Secteur :** Industrie cosmétique
- **Site web :** [npgandour.com](https://npgandour.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** La Nouvelle Parfumerie Gandour (NPGCI) est une entreprise industrielle cosmétique leader en Afrique de l'Ouest, basée dans la zone industrielle de Yopougon à Abidjan, en Côte d'Ivoire. Fondée sur des principes de fabrication rigoureux, elle produit une vaste gamme de produits corporels, capillaires, bucco-dentaires et de parfumerie.

----------------------------

### 29 Février 2024

#### 🇿🇦 Afrique du Sud - ERWAT (Ekurhuleni Water Care Company)
- **Groupe ransomware :** dragonforce
- **Secteur :** Services publics (Gestion des eaux)
- **Site web :** [erwat.co.za](https://erwat.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** ERWAT (Ekurhuleni Water Care Company) est une entreprise publique sud-africaine de premier plan créée en 1992, spécialisée dans l'assainissement et le traitement des eaux usées industrielles et domestiques. Elle assure la gestion des infrastructures d'épuration pour des milliers d'industries et plus de 3,5 millions d'habitants.

----------------------------

## ✍🏿 Author
*Adama ASSIONGBON*
*Consultant SOC & Cyber Threat Intelligence*
[LinkedIn profile](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)
