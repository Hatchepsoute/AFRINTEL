# Cyberincidents AFRINTEL - Février 2024 - corpus canonique (8 fiches)

👉🏾 [English version](./victims.md)

> Ce fichier contient uniquement les incidents retenus dans les statistiques canoniques 2024. Les découvertes historiques, republications, doublons et dossiers à chronologie non résolue sont conservés séparément à la racine 2024.


### 6 Février 2024

#### 🇪🇬 Égypte - ArpuPlus
- **Acteur / Groupe:** medusa
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
- **Acteur / Groupe:** hunters
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
- **Acteur / Groupe:** lockbit3
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
- **Acteur / Groupe:** lockbit3
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

### 27 Février 2024

#### 🇨🇮 Côte d'Ivoire - Nouvelle Parfumerie Gandour (NPGCI)
- **Acteur / Groupe:** lockbit3
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
- **Acteur / Groupe:** dragonforce
- **Secteur:** Water / Utilities
- **Site web:** [erwat.co.za](https://erwat.co.za)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** ERWAT (Ekurhuleni Water Care Company) est une entreprise publique sud-africaine de premier plan créée en 1992, spécialisée dans l'assainissement et le traitement des eaux usées industrielles et domestiques. Elle assure la gestion des infrastructures d'épuration pour des milliers d'industries et plus de 3,5 millions d'habitants.

----------------------------

### Février 2024 - date exacte de l'incident non établie publiquement

#### 🇲🇼 Malawi - Department of Immigration and Citizenship Services - Passport Issuance System
- **Date de l'incident:** Février 2024 - date exacte non établie publiquement
- **Date de publication initiale:** 21 février 2024
- **Date de correction AFRINTEL:** 23 août 2026
- **Acteur / Groupe:** Unknown
- **Secteur:** Government / Administration
- **Site web:** [immigration.gov.mw](https://www.immigration.gov.mw/)
- **Statut:** Government Confirmed
- **Type d'incident:** System Intrusion
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Note de taxonomie:** La violation cyber et la perturbation du service sont confirmées. La demande de rançon a été déclarée publiquement, mais la cause technique exacte et le déploiement d'un ransomware restent contestés ou non résolus ; `System Intrusion` est retenu comme type principal.
- **Description victime:** Le Department of Immigration and Citizenship Services du Malawi exploite l'infrastructure nationale de délivrance des passeports.
- **Analyse:** Le président du Malawi a publiquement décrit l'indisponibilité du système de passeports comme une grave violation de cybersécurité et déclaré que des attaquants exigeaient une rançon. Le Department of Immigration a ensuite confirmé que les services de passeports avaient été perturbés par une violation de cybersécurité et que les données démographiques perdues avaient été récupérées. Toutefois, des organisations de la société civile et des déclarations de fournisseurs ont contesté certains aspects du récit technique gouvernemental et suggéré que des problèmes de licence ou de gestion du système avaient également pu contribuer à la panne. AFRINTEL enregistre donc la perturbation du service et la déclaration officielle de violation comme confirmées tout en maintenant la cause technique exacte et le déploiement d'un ransomware comme contestés.
- **Sources publiques:** [Communiqué du gouvernement du Malawi](https://www.malawi.gov.mw/index.php/resources/documents/press-releases?download=145%3Aofficial-passport-press-release-from-the-department-of-immigration-and-citizenship-services) | [Malawi Broadcasting Corporation](https://mbc.mw/?p=10487) | [Contexte VOA](https://www.voanews.com/a/some-question-malawi-president-s-claim-that-cyberattack-caused-passport-problems-/7498879.html)

----------------------------
