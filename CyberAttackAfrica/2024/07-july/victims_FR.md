[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%7C%20Data%20Leak-red)

# Cyberattaques en Afrique - Juillet 2024 : Liste de 11 victimes
👉🏾 [**English version available here**](./victims.md)

## 📅 Juillet 2024

## Synthèse mensuelle

Juillet 2024 contient **11 fiches incident documentées** : **7 Ransomware**, **4 Data Leak**, **0 Access Sale**, **0 DDoS**, **0 Defacement** et **0 Operational Fraud**, dans **7 pays africains**.

Trois des quatre Data Leak correspondent à des republications de juillet de jeux de données algériens plus anciens et ne doivent pas être interprétés comme trois nouvelles compromissions de juillet.

### 01 Juillet 2024
#### 🇹🇳 Tunisie - Maxcess-logistics
- **Groupe ransomware:** killsec
- **Secteur:** Transport / Logistics
- **Site web:** [maxcess-logistics.com](https://www.maxcess-logistics.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** Maxcess-logistics est une organisation basée en Tunisie, classée dans Transport / Logistics dans le corpus AFRINTEL.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.
### 02 Juillet 2024
#### 🇪🇹 Éthiopie - F.D.R.E Defence War College (domaine cité : nwc.ndu.edu)

- **Acteur / Groupe:** TheColorYellow
- **Contexte source:** Publication de vente de données sur RaidForums
- **Secteur:** Defense / Security
- **Statut:** Claim - Data Sample Published
- **Site web:** [dwc.edu.et](https://dwc.edu.et/wc/) (organisation observée dans les échantillons) ; domaine cité par l'acteur : nwc.ndu.edu
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 4
- **Type d'incident:** Data Leak
- **Date de découverte:** 02 juillet 2024

- **Note de fiabilité:**
  La publication de TheColorYellow annonce une victime présentée comme le « National War College of Ethiopia » et cite le domaine nwc.ndu.edu. Ce domaine correspond au National War College de la National Defense University des États-Unis. Toutefois, les cinq fichiers PNG fournis localement présentent l'emblème et l'en-tête en amharique du « F.D.R.E Defence War College » éthiopien, ainsi que des documents internes, un inventaire de 29 postes et un tableau de 17 entrées téléphoniques. Une erreur de domaine dans l'annonce, une confusion de nom ou une attribution technique incorrecte restent donc possibles. AFRINTEL retient comme organisation observée le F.D.R.E Defence War College et conserve nwc.ndu.edu comme domaine annoncé mais non vérifié.

- **Description:**
  Les éléments visibles correspondent au F.D.R.E Defence War College, établissement d’enseignement militaire éthiopien. Le lien officiel observé pour cette organisation est [dwc.edu.et](https://dwc.edu.et/wc/). Le domaine nwc.ndu.edu reste uniquement le domaine cité dans l’annonce de l’acteur.

- **Analyse:**
  L'acteur TheColorYellow affirme détenir 747 Mo de courriels confidentiels prétendument volés directement sur le serveur Exchange de l'établissement, exportés sous forme de fichiers de boîtes aux lettres PST, et propose ces données pour 500 $ avec recours à un escrow. Le répertoire local fourni contient cinq PNG, mais aucun PST, EML, MSG ou export Exchange. Les images comprennent des documents institutionnels, un avis en chinois pour les étudiants internationaux, un inventaire visible de 29 postes et un tableau visible de 17 entrées téléphoniques. Ces éléments sont cohérents avec des documents internes du F.D.R.E Defence War College et renforcent l'attribution de l'échantillon, mais ne confirment ni l'accès au serveur Exchange, ni l'existence des 747 Mo, ni l'exhaustivité ou l'origine des données. L'OCR amharique et chinois n'a pas été utilisé pour transcrire les valeurs ; aucun nom, numéro, identifiant matériel ou numéro de téléphone n'est reproduit.

### 5 Juillet 2024
#### 🇿🇦 Afrique du Sud - National health laboratory services (NHLS)
- **Groupe ransomware:** blacksuit
- **Secteur:** Healthcare / Medical
- **Site web:** [nhls.ac.za](https://www.nhls.ac.za)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** Le National Health Laboratory Service (NHLS) est une organisation sud-africaine de services de laboratoires publics, classée dans Healthcare / Medical.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.
### 11 Juillet 2024
#### 🇩🇿 Algérie - Hôpital Chahids Mahmoudi (hcm-dz.com)

- **Acteur / Groupe:** Unknown
- **Contexte source:** Republication par Addka72424 de matériel attribué à FriendlyChemist
- **Secteur:** Healthcare / Medical
- **Statut:** Claim - Data Sample Published
- **Site web:** [hcm-dz.com](https://hcm-dz.com)
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Date de la fuite:** 21 septembre 2023
- **Date de découverte:** 11 juillet 2024

- **Note de fiabilité:**
  Le post est explicitement présenté comme une republication ("REPOST") d'une compilation intitulée « Algerian Databases Collection », elle-même republiée d'un post initial attribué au compte FriendlyChemist. La date et le contenu du post d'origine ne sont pas fournis, et la méthode de collecte ou d'accès initial n'est pas précisée.

- **Description:**
  L'Hôpital Chahids Mahmoudi est un établissement hospitalier algérien basé à Tizi Ouzou, spécialisé notamment en oncologie et médecine nucléaire, avec une extension à Alger et une clinique ouverte à Constantine en 2024. Il exploite le domaine hcm-dz.com pour ses communications professionnelles.

- **Analyse:**
  Le fichier associé à hcm-dz.com dans la compilation republiée le 11 juillet 2024 est daté du 21 septembre 2023 et présenté comme concernant environ 1 900 utilisateurs. L'échantillon examiné par AFRINTEL correspond à des journaux de filtrage de messagerie (type passerelle anti-spam), et non à un export de dossiers médicaux ou de boîtes de messagerie complètes.

  Les lignes visibles indiquent, pour chaque message, l'expéditeur, le destinataire, l'adresse IP source, l'objet, la taille, un score de filtrage, la direction (entrant, sortant ou interne) et un identifiant de message. Plusieurs objets de messages font référence à des noms de patients et à des types d'examens médicaux (résultats de laboratoire, imagerie, cardiologie), ce qui indique un usage professionnel de la messagerie hospitalière pour la transmission de résultats, sans que le contenu des messages ne soit lui-même visible dans l'échantillon.

  La cohérence du format des journaux et le volume de lignes observé appuient un niveau de confiance moyen quant à l'origine de ces journaux. AFRINTEL n'a toutefois pas pu confirmer un accès effectif aux boîtes de messagerie elles-mêmes, ni l'exhaustivité d'une éventuelle compromission au-delà des lignes republiées. La présence d'objets de messages faisant référence à des patients nommés constitue une exposition de métadonnées de santé sensibles, pouvant faciliter le phishing ciblé, l'usurpation de personnel médical ou administratif, et la reconstitution partielle de parcours de soins. AFRINTEL ne reproduit aucun nom de patient, adresse email, adresse IP ni objet de message issu de l'échantillon examiné.

### 11 Juillet 2024
#### 🇩🇿 Algérie - Université de Tlemcen (univ-tlemcen.dz)

- **Acteur / Groupe:** Unknown
- **Contexte source:** Republication par Addka72424 de matériel attribué à FriendlyChemist
- **Secteur:** Education / University
- **Statut:** Claim - Data Sample Published
- **Site web:** [univ-tlemcen.dz](https://www.univ-tlemcen.dz)
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Date de la fuite:** 27 juin 2022
- **Date de découverte:** 11 juillet 2024

- **Note de fiabilité:**
  Comme pour les autres fichiers de la même compilation, l'origine exacte, la méthode d'accès initiale et la date du premier post par FriendlyChemist ne sont pas précisées. L'échantillon montre en revanche une structure de table applicative complète et des enregistrements individuels cohérents.

- **Description:**
  L'Université de Tlemcen (Abou Bekr Belkaïd) est un établissement public algérien d'enseignement supérieur. Elle exploite une plateforme d'apprentissage en ligne Moodle accessible via le domaine univ-tlemcen.dz.

- **Analyse:**
  Le fichier associé à univ-tlemcen.dz dans la compilation republiée le 11 juillet 2024 est daté du 27 juin 2022 et présenté comme concernant environ 80 000 utilisateurs. L'échantillon examiné par AFRINTEL montre la structure de la table `mdl_user`, propre au système de gestion de l'apprentissage Moodle, ainsi qu'un extrait d'enregistrements utilisateurs réels.

  Les champs structurels comprennent notamment l'identifiant, le nom d'utilisateur, le mot de passe haché, le prénom, le nom, l'adresse email, l'établissement, le département, le pays, la langue et les dates de création et de dernière connexion. Les enregistrements visibles incluent un compte administrateur associé au domaine univ-tlemcen.dz, ainsi que des comptes rattachés à des adresses email d'autres établissements universitaires algériens, ce qui suggère une fédération d'authentification partagée entre plusieurs universités via ce système Moodle plutôt qu'un périmètre limité à Tlemcen seule. Les mots de passe sont hachés selon des formats hétérogènes, dont un format bcrypt pour certains comptes récents et des formats plus anciens et plus faibles pour d'autres comptes, sans que leur robustesse effective ne puisse être confirmée par AFRINTEL.

  La cohérence de la structure de table Moodle avec les enregistrements observés, combinée à la présence d'un compte administrateur nommément identifiable, justifie un niveau de confiance élevé quant à l'authenticité de cette base. Une compromission de cette ampleur pourrait faciliter la prise de contrôle de comptes étudiants et enseignants, l'usurpation d'identité académique, et un accès en cascade vers d'autres établissements algériens partageant potentiellement la même fédération d'authentification. AFRINTEL ne reproduit aucun identifiant, mot de passe haché, email ni enregistrement individuel issu de l'échantillon examiné.

### 11 Juillet 2024
#### 🇩🇿 Algérie - Algeria.com (portail web)

- **Acteur / Groupe:** Unknown
- **Contexte source:** Republication par Addka72424 de matériel attribué à FriendlyChemist
- **Secteur:** Media / Entertainment
- **Statut:** Claim - Data Sample Published
- **Site web:** [algeria.com](https://www.algeria.com)
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Type d'incident:** Data Leak
- **Date de la fuite:** Septembre 2019
- **Date de découverte:** 11 juillet 2024

- **Note de fiabilité:**
  Les données de ce fichier sont nettement plus anciennes (2019) que les autres éléments de la compilation. Le domaine algeria.com est un portail générique consacré à l'Algérie et non un domaine national .dz ; l'origine exacte de la fuite et la période durant laquelle le service de comptes utilisateurs associé a été actif ne sont pas précisées.

- **Description:**
  Algeria.com est un portail web consacré à l'Algérie (tourisme, actualités et style de vie), qui a proposé par le passé des comptes utilisateurs et des adresses email sous son propre domaine à une partie de ses visiteurs.

- **Analyse:**
  Le fichier associé à algeria.com dans la compilation republiée le 11 juillet 2024 est daté de septembre 2019 et présenté comme concernant environ 3 600 comptes utilisateurs. L'échantillon examiné par AFRINTEL comprend les champs identifiant utilisateur, nom d'utilisateur, adresse IP, adresse email, un jeton et un second champ qualifié de « secret ».

  Les valeurs observées dans les champs jeton et secret ne correspondent à aucun format de hachage cryptographique standard clairement identifiable par AFRINTEL, et pourraient correspondre à un ancien mécanisme propriétaire du portail plutôt qu'à un mot de passe directement exploitable. L'ancienneté des données et le caractère générique du domaine, distinct des domaines institutionnels algériens .dz, limitent la pertinence opérationnelle actuelle de cette exposition, bien que les adresses email et noms d'utilisateurs associés puissent encore être réutilisés ailleurs par les personnes concernées.

  Compte tenu de l'ancienneté des données, du volume limité et de l'absence de champ de mot de passe clairement identifiable, AFRINTEL évalue cette revendication avec un niveau de confiance faible et un impact limité. AFRINTEL ne reproduit aucun identifiant, adresse email, adresse IP ni valeur de jeton issu de l'échantillon examiné.

### 13 Juillet 2024
#### 🇰🇪 Kenya - Kenya urban roads authority (KURA)
- **Groupe ransomware:** hunters
- **Secteur:** Transport / Logistics
- **Site web:** [kura.go.ke](https://www.kura.go.ke)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** La Kenya Urban Roads Authority (KURA) est une autorité publique kenyane chargée des infrastructures routières urbaines, classée dans Transport / Logistics.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.
### 17 Juillet 2024
#### 🇿🇼 Zimbabwe - Zb financial holdings
- **Groupe ransomware:** madliberator
- **Secteur:** Finance / Banking
- **Site web:** [zb.co.zw](https://www.zb.co.zw)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** ZB Financial Holdings est une organisation financière zimbabwéenne classée dans Finance / Banking.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.
### 17 Juillet 2024
#### 🇿🇦 Afrique du Sud - Cities network
- **Groupe ransomware:** madliberator
- **Secteur:** Professional / Business Services
- **Site web:** [sacities.net](https://www.sacities.net)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** South African Cities Network est classé dans Professional / Business Services dans le corpus AFRINTEL.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.
### 17 Juillet 2024
#### 🇪🇬 Égypte - Assih
- **Groupe ransomware:** lockbit3
- **Secteur:** Professional / Business Services
- **Site web:** [assih.com](https://www.assih.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** Assih est une organisation basée en Égypte, classée dans Professional / Business Services dans le corpus AFRINTEL.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.
### 22 Juillet 2024
#### 🇿🇦 Afrique du Sud - Sibanye-stillwater
- **Groupe ransomware:** ransomhouse
- **Secteur:** Mining / Extractive Industries
- **Site web:** [sibanyestillwater.com](https://www.sibanyestillwater.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** Sibanye-Stillwater est une organisation minière basée en Afrique du Sud, classée dans Mining / Extractive Industries.

---

- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.
## ✍🏿 Auteur
*Adama ASSIONGBON* *Consultant Senior SOC & Cyber Threat Intelligence (CTI)*
