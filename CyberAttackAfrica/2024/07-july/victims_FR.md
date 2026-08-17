[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)

# Cyberattaques en Afrique - Juillet 2024 : Liste de 11 victimes
👉🏾 [**English version available here**](./victims.md)

## 📅 Juillet 2024

### 01 Juillet 2024
#### 🇹🇳 Tunisie - Maxcess-logistics
- **Groupe ransomware :** killsec
- **Secteur :** Logistique & Chaîne d'approvisionnement
- **Site web :** [maxcess-logistics.com](https://www.maxcess-logistics.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Maxcess-logistics est une entreprise commerciale majeure opérant dans le secteur de la logistique, contribuant de manière significative au tissu économique régional en Tunisie.

### 02 Juillet 2024
#### 🇪🇹 Éthiopie - National War College (nwc.ndu.edu)

- **Acteur / Groupe :** TheColorYellow, publication postée sur RaidForums
- **Secteur :** Défense / Enseignement militaire
- **Statut :** Claim - Data Sample Published
- **Site web :** nwc.ndu.edu (tel qu'indiqué dans la publication ; voir note de fiabilité)
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4
- **Type d'incident :** Fuite de données
- **Date de découverte :** 02 juillet 2024

- **Note de fiabilité :**
  Le titre et le texte de la publication citent le domaine « nwc.ndu.edu », qui correspond au National War College de la National Defense University (États-Unis). Cependant, les deux échantillons de documents portant un en-tête institutionnel dans la publication affichent tous deux l'emblème et l'en-tête en amharique du « F.D.R.E Defence War College » (République Fédérale Démocratique d'Éthiopie), et non une institution américaine. AFRINTEL ne peut résoudre cette incohérence à partir des éléments examinés et considère le domaine cité par l'acteur comme non vérifié ; l'évaluation ci-dessous s'appuie sur l'en-tête éthiopien visible dans les échantillons, cohérent avec l'affirmation du vendeur selon laquelle la victime est un collège militaire éthiopien.

- **Description :**
  Le National War College mentionné dans la publication correspond, d'après l'en-tête visible dans les échantillons, au FDRE Defence War College, un établissement d'enseignement militaire de la République Fédérale Démocratique d'Éthiopie.

- **Analyse CTI :**
  L'acteur TheColorYellow affirme détenir 747 Mo de courriels confidentiels prétendument volés directement sur le serveur Exchange de l'établissement, exportés sous forme de fichiers de boîtes aux lettres PST, et propose ces données pour 500 $ avec recours à un escrow. Trois images de documents sont présentées en échantillon : un document interne en amharique évoquant le service informatique du collège et une note de plan de travail/discipline interne portant l'emblème du FDRE Defence War College ; un modèle bilingue (amharique/anglais) d'« engagement de confidentialité » sur le même en-tête, avec des champs vierges pour le nom, le numéro d'identité, le service et les signatures ; et un avis distinct en chinois adressé aux étudiants internationaux concernant les modalités d'entrée pour le semestre d'automne 2021, dont le lien avec la compromission Exchange revendiquée n'est pas établi par les éléments montrés. AFRINTEL n'a pas eu accès au jeu de données de 747 Mo sous-jacent et ne peut confirmer ni l'exhaustivité, ni l'authenticité, ni l'origine réelle en boîtes aux lettres de l'export revendiqué au-delà de ces images de documents. La présence d'un modèle d'engagement de confidentialité interne et d'une correspondance du service informatique portant un en-tête institutionnel d'apparence authentique est cohérente avec un ensemble de documents internes d'un établissement d'enseignement militaire, sans pour autant confirmer à elle seule une compromission de l'ensemble du serveur Exchange. Si la revendication sous-jacente est exacte, l'exposition des communications électroniques du personnel et des étudiants du collège militaire présenterait une sensibilité relevant du secteur souverain (données personnelles, correspondance administrative interne et potentiellement liée à la formation). AFRINTEL ne reproduit aucun nom, numéro d'identité, adresse e-mail ni contenu de document au-delà de ce qui est décrit ci-dessus.

### 5 Juillet 2024
#### 🇿🇦 Afrique du Sud - National health laboratory services (NHLS)
- **Groupe ransomware :** blacksuit
- **Secteur :** Santé / Services de laboratoires médicaux publics
- **Site web :** [nhls.ac.za](https://www.nhls.ac.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Les National Health Laboratory Services constituent une entité publique et commerciale majeure gérant les services de laboratoires de santé publique à l'échelle nationale en Afrique du Sud.

### 11 Juillet 2024
#### 🇩🇿 Algérie - Hôpital Chahids Mahmoudi (hcm-dz.com)

- **Acteur / Groupe :** Addka72424, republication d'un post initial attribué à FriendlyChemist, sur un forum cybercriminel
- **Secteur :** Santé / Établissement hospitalier privé
- **Statut :** Claim - Data Sample Published
- **Site web :** [hcm-dz.com](https://hcm-dz.com)
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Date de la fuite :** 21 septembre 2023
- **Date de découverte :** 11 juillet 2024

- **Note de fiabilité :**
  Le post est explicitement présenté comme une republication ("REPOST") d'une compilation intitulée « Algerian Databases Collection », elle-même republiée d'un post initial attribué au compte FriendlyChemist. La date et le contenu du post d'origine ne sont pas fournis, et la méthode de collecte ou d'accès initial n'est pas précisée.

- **Description :**
  L'Hôpital Chahids Mahmoudi est un établissement hospitalier algérien basé à Tizi Ouzou, spécialisé notamment en oncologie et médecine nucléaire, avec une extension à Alger et une clinique ouverte à Constantine en 2024. Il exploite le domaine hcm-dz.com pour ses communications professionnelles.

- **Analyse :**
  Le fichier associé à hcm-dz.com dans la compilation republiée le 11 juillet 2024 est daté du 21 septembre 2023 et présenté comme concernant environ 1 900 utilisateurs. L'échantillon examiné par AFRINTEL correspond à des journaux de filtrage de messagerie (type passerelle anti-spam), et non à un export de dossiers médicaux ou de boîtes de messagerie complètes.

  Les lignes visibles indiquent, pour chaque message, l'expéditeur, le destinataire, l'adresse IP source, l'objet, la taille, un score de filtrage, la direction (entrant, sortant ou interne) et un identifiant de message. Plusieurs objets de messages font référence à des noms de patients et à des types d'examens médicaux (résultats de laboratoire, imagerie, cardiologie), ce qui indique un usage professionnel de la messagerie hospitalière pour la transmission de résultats, sans que le contenu des messages ne soit lui-même visible dans l'échantillon.

  La cohérence du format des journaux et le volume de lignes observé appuient un niveau de confiance moyen quant à l'origine de ces journaux. AFRINTEL n'a toutefois pas pu confirmer un accès effectif aux boîtes de messagerie elles-mêmes, ni l'exhaustivité d'une éventuelle compromission au-delà des lignes republiées. La présence d'objets de messages faisant référence à des patients nommés constitue une exposition de métadonnées de santé sensibles, pouvant faciliter le phishing ciblé, l'usurpation de personnel médical ou administratif, et la reconstitution partielle de parcours de soins. AFRINTEL ne reproduit aucun nom de patient, adresse email, adresse IP ni objet de message issu de l'échantillon examiné.

### 11 Juillet 2024
#### 🇩🇿 Algérie - Université de Tlemcen (univ-tlemcen.dz)

- **Acteur / Groupe :** Addka72424, republication d'un post initial attribué à FriendlyChemist, sur un forum cybercriminel
- **Secteur :** Éducation / Enseignement supérieur
- **Statut :** Claim - Data Sample Published
- **Site web :** [univ-tlemcen.dz](https://www.univ-tlemcen.dz)
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Date de la fuite :** 27 juin 2022
- **Date de découverte :** 11 juillet 2024

- **Note de fiabilité :**
  Comme pour les autres fichiers de la même compilation, l'origine exacte, la méthode d'accès initiale et la date du premier post par FriendlyChemist ne sont pas précisées. L'échantillon montre en revanche une structure de table applicative complète et des enregistrements individuels cohérents.

- **Description :**
  L'Université de Tlemcen (Abou Bekr Belkaïd) est un établissement public algérien d'enseignement supérieur. Elle exploite une plateforme d'apprentissage en ligne Moodle accessible via le domaine univ-tlemcen.dz.

- **Analyse :**
  Le fichier associé à univ-tlemcen.dz dans la compilation republiée le 11 juillet 2024 est daté du 27 juin 2022 et présenté comme concernant environ 80 000 utilisateurs. L'échantillon examiné par AFRINTEL montre la structure de la table `mdl_user`, propre au système de gestion de l'apprentissage Moodle, ainsi qu'un extrait d'enregistrements utilisateurs réels.

  Les champs structurels comprennent notamment l'identifiant, le nom d'utilisateur, le mot de passe haché, le prénom, le nom, l'adresse email, l'établissement, le département, le pays, la langue et les dates de création et de dernière connexion. Les enregistrements visibles incluent un compte administrateur associé au domaine univ-tlemcen.dz, ainsi que des comptes rattachés à des adresses email d'autres établissements universitaires algériens, ce qui suggère une fédération d'authentification partagée entre plusieurs universités via ce système Moodle plutôt qu'un périmètre limité à Tlemcen seule. Les mots de passe sont hachés selon des formats hétérogènes, dont un format bcrypt pour certains comptes récents et des formats plus anciens et plus faibles pour d'autres comptes, sans que leur robustesse effective ne puisse être confirmée par AFRINTEL.

  La cohérence de la structure de table Moodle avec les enregistrements observés, combinée à la présence d'un compte administrateur nommément identifiable, justifie un niveau de confiance élevé quant à l'authenticité de cette base. Une compromission de cette ampleur pourrait faciliter la prise de contrôle de comptes étudiants et enseignants, l'usurpation d'identité académique, et un accès en cascade vers d'autres établissements algériens partageant potentiellement la même fédération d'authentification. AFRINTEL ne reproduit aucun identifiant, mot de passe haché, email ni enregistrement individuel issu de l'échantillon examiné.

### 11 Juillet 2024
#### 🇩🇿 Algérie - Algeria.com (portail web)

- **Acteur / Groupe :** Addka72424, republication d'un post initial attribué à FriendlyChemist, sur un forum cybercriminel
- **Secteur :** Médias / Portail web (voyage, actualités, style de vie)
- **Statut :** Claim - Data Sample Published
- **Site web :** [algeria.com](https://www.algeria.com)
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Fuite de données
- **Date de la fuite :** Septembre 2019
- **Date de découverte :** 11 juillet 2024

- **Note de fiabilité :**
  Les données de ce fichier sont nettement plus anciennes (2019) que les autres éléments de la compilation. Le domaine algeria.com est un portail générique consacré à l'Algérie et non un domaine national .dz ; l'origine exacte de la fuite et la période durant laquelle le service de comptes utilisateurs associé a été actif ne sont pas précisées.

- **Description :**
  Algeria.com est un portail web consacré à l'Algérie (tourisme, actualités et style de vie), qui a proposé par le passé des comptes utilisateurs et des adresses email sous son propre domaine à une partie de ses visiteurs.

- **Analyse :**
  Le fichier associé à algeria.com dans la compilation republiée le 11 juillet 2024 est daté de septembre 2019 et présenté comme concernant environ 3 600 comptes utilisateurs. L'échantillon examiné par AFRINTEL comprend les champs identifiant utilisateur, nom d'utilisateur, adresse IP, adresse email, un jeton et un second champ qualifié de « secret ».

  Les valeurs observées dans les champs jeton et secret ne correspondent à aucun format de hachage cryptographique standard clairement identifiable par AFRINTEL, et pourraient correspondre à un ancien mécanisme propriétaire du portail plutôt qu'à un mot de passe directement exploitable. L'ancienneté des données et le caractère générique du domaine, distinct des domaines institutionnels algériens .dz, limitent la pertinence opérationnelle actuelle de cette exposition, bien que les adresses email et noms d'utilisateurs associés puissent encore être réutilisés ailleurs par les personnes concernées.

  Compte tenu de l'ancienneté des données, du volume limité et de l'absence de champ de mot de passe clairement identifiable, AFRINTEL évalue cette revendication avec un niveau de confiance faible et un impact limité. AFRINTEL ne reproduit aucun identifiant, adresse email, adresse IP ni valeur de jeton issu de l'échantillon examiné.

### 13 Juillet 2024
#### 🇰🇪 Kenya - Kenya urban roads authority (KURA)
- **Groupe ransomware :** hunters
- **Secteur :** Infrastructures publiques / Transport routier urbain
- **Site web :** [kura.go.ke](https://www.kura.go.ke)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** La Kenya Urban Roads Authority est une institution publique et une autorité de régulation étatique essentielle, chargée du développement, de la gestion et de la maintenance des infrastructures routières urbaines.

### 17 Juillet 2024
#### 🇿🇼 Zimbabwe - Zb financial holdings
- **Groupe ransomware :** madliberator
- **Secteur :** Institutions financières / Banque & Assurance
- **Site web :** [zb.co.zw](https://www.zb.co.zw)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Zb financial holdings est une institution financière et commerciale de premier plan offrant des services bancaires, d'investissement et d'assurance au Zimbabwe.

### 17 Juillet 2024
#### 🇿🇦 Afrique du Sud - Cities network
- **Groupe ransomware :** madliberator
- **Secteur :** Services de conseil urbain / Développement territorial
- **Site web :** [sacities.net](https://www.sacities.net)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** South African Cities Network est une structure de services et de partenariat stratégique encourageant l'échange d'expertises et le développement durable des grandes agglomérations en Afrique du Sud.

### 17 Juillet 2024
#### 🇪🇬 Égypte - Assih
- **Groupe ransomware :** lockbit3
- **Secteur :** Services aux entreprises / Conseil
- **Site web :** [assih.com](https://www.assih.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Assih est une entreprise commerciale d'importance opérant dans le secteur des services et du commerce général en Égypte.

### 22 Juillet 2024
#### 🇿🇦 Afrique du Sud - Sibanye-stillwater
- **Groupe ransomware :** ransomhouse
- **Secteur :** Industrie lourde / Extraction minière (Or & Métaux du groupe du platine)
- **Site web :** [sibanyestillwater.com](https://www.sibanyestillwater.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Sibanye-Stillwater est un groupe minier international de premier plan, comptant parmi les plus grands producteurs d'or et de platinoïdes au monde, basé en Afrique du Sud.

---
## ✍🏿 Auteur
*Adama ASSIONGBON* *Consultant Senior SOC & Cyber Threat Intelligence (CTI)*
