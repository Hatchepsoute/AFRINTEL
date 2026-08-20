# 📑 RAPPORT D'INTELLIGENCE SUR LES MENACES CYBER (CTI)
**Périmètre :** Continent Africain | **Période :** Mars 2024  
**Classification :** TLP:CLEAR  
**Projet :** AFRINTEL (African Threat Intelligence Repository)
👉🏾 [English version available here](./README.md)
### Vue agrégée mensuelle de l’exposition

La vue CTI mensuelle regroupe les fuites de données et les ventes d’accès sous **exposition des données** : **1 fiches** (12.5% du corpus mensuel). Les fiches sources restent la référence ; une vente d’accès ne prouve pas à elle seule l’exfiltration de données.

---

## 1. RÉSUMÉ EXÉCUTIF

Le mois de mars 2024 a été marqué par une activité soutenue des groupes de ransomware ciblant des infrastructures critiques, des institutions financières et des entités publiques majeures sur le continent africain, ainsi qu'une revendication de fuite de données non attribuée visant un établissement d'enseignement supérieur. Au total, **8 incidents critiques** ont été officiellement répertoriés et analysés dans le cadre du projet AFRINTEL.

Les cybercriminels continuent d'exploiter les vulnérabilités des périmètres exposés et d'exfiltrer des volumes massifs de données à des fins de double extorsion. La répartition géographique met en évidence une concentration des attaques en **Égypte** (3 incidents) et en **Afrique du Sud** (2 incidents), suivies par la **Tunisie**, la **Namibie** et le **Maroc**.

### Indicateurs Clés de Mars 2024
* **Total des Victimes validées :** 8
* **Acteurs de Menaces Identifiés :** LockBit 3.0 (4 attaques), RansomHub (2 attaques), Hunters International (1 attaque), ainsi qu'une revendication de fuite de données non attribuée (ESGC.MA, Maroc).
* **Secteurs les plus touchés :** Services Financiers/Bancaires (2), Infrastructures d'État (1), Santé/Pharmaceutique (1), Énergie (1), Industrie (1), Médias (1), Éducation / Enseignement supérieur (1).

---

## 2. PAYSAGE DES ACTEURS DE MENACES (RANSOMWARE)

Trois syndicats du crime organisé se partagent les sept attaques attribuées à un ransomware ce mois-ci, aux côtés d'une revendication de fuite de données non attribuée traitée séparément ci-dessous :

1. **LockBit 3.0 (50% des incidents) :** Malgré les opérations de démantèlement international (Opération Cronos) subies plus tôt en 2024, la franchise LockBit démontre sa résilience sur le continent africain en frappant 4 entités de premier plan grâce à son réseau d'affiliés actifs.
2. **RansomHub (25% des incidents) :** Ce groupe émergent confirme sa montée en puissance rapide, ciblant spécifiquement des infrastructures de l'énergie et des médias numériques à forte visibilité en Égypte.
3. **Hunters International (12,5% des incidents) :** Acteur opportuniste exploitant le code source de Hive, identifié ce mois-ci sur le secteur financier nord-africain.
4. **Revendication de fuite de données non attribuée (12,5% des incidents) :** Une publication de forum du 26 mars 2024, sous le compte UnknownMember, revendique un échantillon d'une base de données de 2021 provenant de la Higher School of Commerce and Management (ESGC.MA) au Maroc. Il s'agit d'une revendication de fuite de données et non d'un incident ransomware ; elle n'est attribuée à aucun des trois groupes ci-dessus.

---

## 3. CARTOGRAPHIE DÉTAILLÉE DES INCIDENTS (MARS 2024)

### 🗓️ 19 Mars 2024
#### 🇪🇬 Égypte - Go4Kora
* **Identifiant Incident :** AFRINTEL-2024-13649
* **Groupe Ransomware :** RansomHub
* **Secteur d'Activité :** Médias sportifs & Divertissement d'audience
* **Site Web :** [go4kora.tv](https://go4kora.tv)
* **Statut de l'Attaque :** Revendication officielle et exfiltration de bases de données.
* **Description & Contexte :** Go4Kora est l'un des portails d'actualités sportives et de streaming de football les plus consultés en Égypte et dans la région MENA. L'attaque visait l'infrastructure de diffusion et les données des abonnés, impactant l'intégrité de la plateforme.

---

### 🗓️ 20 Mars 2024
#### 🇿🇦 Afrique du Sud - Government Printing Works (GPW)
* **Identifiant Incident :** AFRINTEL-2024-13658
* **Groupe Ransomware :** LockBit 3.0
* **Secteur d'Activité :** Administrations publiques & Impressions de sécurité d'État
* **Site Web :** [gpw.gov.za](https://www.gpw.gov.za)
* **Statut de l'Attaque :** Revendication confirmée, menace de divulgation de documents régaliens.
* **Description & Contexte :** Entité étatique sud-africaine stratégique sous la tutelle du ministère de l'Intérieur, le GPW est responsable de l'impression des documents d'identité sécurisés, des passeports, des visas et des bulletins officiels du gouvernement. Une compromission majeure touchant la souveraineté numérique.

---

### 🗓️ 25 Mars 2024
#### 🇹🇳 Tunisie - Arab Tunisian Leasing (ATL Leasing)
* **Identifiant Incident :** AFRINTEL-2024-13740
* **Groupe Ransomware :** Hunters International
* **Secteur d'Activité :** Services financiers & Crédit-bail (Leasing)
* **Site Web :** [atlleasing.com.tn](https://www.atlleasing.com.tn)
* **Statut de l'Attaque :** Revendication sur le site de fuite, exfiltration de données financières d'entreprises.
* **Description & Contexte :** Cotée à la Bourse de Tunis, l'ATL est une institution financière tunisienne de premier plan spécialisée dans le financement par crédit-bail d'équipements professionnels et immobiliers pour les PME.

---

### 🗓️ 25 Mars 2024
#### 🇪🇬 Égypte - Pharmacies El Ezaby
* **Identifiant Incident :** AFRINTEL-2024-13743
* **Groupe Ransomware :** LockBit 3.0
* **Secteur d'Activité :** Santé publique & Distribution pharmaceutique
* **Site Web :** [elezabypharmacy.com](https://www.elezabypharmacy.com)
* **Statut de l'Attaque :** Chiffrement des systèmes de gestion et revendication de données clients/fournisseurs.
* **Description & Contexte :** Représente l'une des plus grandes chaînes de pharmacies de détail en Égypte, gérant un réseau national de méga-officines et un écosystème de distribution critique.

---

### 🗓️ 26 Mars 2024
#### 🇳🇦 Namibie - Agricultural Bank of Namibia (Agribank)
* **Identifiant Incident :** AFRINTEL-2024-13757
* **Groupe Ransomware :** LockBit 3.0
* **Secteur d'Activité :** Secteur bancaire & Financement agricole
* **Site Web :** [agribank.com.na](https://www.agribank.com.na)
* **Statut de l'Attaque :** Publication sur le site de fuite LockBit après échec des négociations.
* **Description & Contexte :** Institution bancaire d'État cruciale pour l'économie namibienne, dédiée exclusivement au financement de l'expansion agricole, de l'aquaculture et de l'acquisition de terres rurales.

---

### 🗓️ 26 Mars 2024
#### 🇲🇦 Maroc - Higher School of Commerce and Management (ESGC.MA)
* **Identifiant Incident :** AFRINTEL-2024-TBD
* **Acteur / Groupe :** Non attribué, publication par le compte de forum UnknownMember
* **Secteur d'Activité :** Éducation / Enseignement supérieur
* **Site Web :** [esgc.ma](https://esgc.ma)
* **Statut de l'Attaque :** Revendication avec échantillon de données publié ; non attribuée à un groupe ransomware.
* **Description & Contexte :** ESGC.MA est présentée comme un établissement marocain d'enseignement supérieur spécialisé dans le commerce et le management. Une publication de forum datée du 26 mars 2024 revendique une base de données de 2021 comptant environ 500 entrées, avec un échantillon affiché montrant des noms, adresses électroniques, hashes de mots de passe, numéros de téléphone et dates de création de comptes. Le jeu de données complet et la compromission alléguée ne sont pas vérifiés de manière indépendante. AFRINTEL ne reproduit aucune donnée personnelle ni identifiant issu de l'échantillon.

---

### 🗓️ 29 Mars 2024
#### 🇪🇬 Égypte - PGESCo (Power Generation Engineering and Services Company)
* **Identifiant Incident :** AFRINTEL-2024-13908
* **Groupe Ransomware :** RansomHub
* **Secteur d'Activité :** Énergie, Pétrole/Gaz & Ingénierie des infrastructures
* **Site Web :** [pgesco.com](https://www.pgesco.com)
* **Statut de l'Attaque :** Revendication et chiffrement des partages réseau d'ingénierie.
* **Description & Contexte :** Firme d'ingénierie égyptienne d'envergure internationale, fournissant la gestion de projet et l'ingénierie pour les centrales électriques majeures et les infrastructures industrielles de la région.

---

### 🗓️ 31 Mars 2024
#### 🇿🇦 Afrique du Sud - Nampak
* **Identifiant Incident :** AFRINTEL-2024-13957
* **Groupe Ransomware :** LockBit 3.0
* **Secteur d'Activité :** Industrie manufacturière (Conditionnement & Emballages industriels)
* **Site Web :** [nampak.com](https://www.nampak.com)
* **Statut de l'Attaque :** Divulgation de données corporatives sensibles.
* **Description & Contexte :** Plus grand fabricant et exportateur d'emballages du continent africain, basé en Afrique du Sud et opérant de nombreuses usines à travers les réseaux sub-sahariens.

---

## 4. RECOMMANDATIONS ET AXES DE MITIGATION (RECOMMANDATIONS SOC)

Face aux modes opératoires observés (LockBit 3.0 et RansomHub), le SOC et l'équipe Threat Intelligence recommandent le déploiement immédiat des mesures suivantes :

1. **Surveillance Active des Identités & Accès :** Renforcer l'authentification multifacteur (MFA) sur tous les accès distants (VPN, serveurs de rebond, portails cloud) et auditer les comptes à privilèges élevés.
2. **Durcissement face à RansomHub :** Ce groupe exploitant fréquemment des identifiants légitimes compromis ou des vulnérabilités connues non corrigées sur les serveurs Edge, un scan complet des actifs externes (Exposition Shodan/Censys) est requis.
3. **Segmentation Réseau Strict :** Isoler les environnements industriels (OT/Scada) ou de production critique (ex: chaînes logistiques d'emballages ou d'impressions sécurisées) des réseaux bureautiques standards.
4. **Analyse de la Persistance :** Surveiller les scripts PowerShell anormaux et l'usage détourné d'outils d'administration légitimes (Living-off-the-Land) tels que AnyDesk, NetSupport ou Rclone.
5. **Hygiène des Applications Web & des Identifiants (Secteur Éducation) :** Pour les plateformes traitant des données personnelles d'étudiants et de personnel, comme dans le cas revendiqué visant ESGC.MA, imposer un hachage robuste des mots de passe (bcrypt/Argon2), faire pivoter les identifiants en cas d'exposition confirmée et surveiller toute redistribution du jeu de données revendiqué sur d'autres forums cybercriminels.

---

## 5. RECONNAISSANCE ET ÉQUIPE ÉDITORIALE

**Auteur principal :** *Adama ASSIONGBON* *Consultant Senior SOC & Cyber Threat Intelligence (CTI)* Casablanca, Maroc.  
[Profil Professionnel LinkedIn](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)

**Source de Données :** Registre OSINT & Dark Web Monitoring du projet AFRINTEL 2024.
