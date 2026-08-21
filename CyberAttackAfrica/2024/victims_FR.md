# Fiches victimes AFRINTEL 2024

[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Type de menace](https://img.shields.io/badge/Menace-Ransomware-red)
![Source](https://img.shields.io/badge/Source-OSINT-darkgreen)
![Type d'intelligence](https://img.shields.io/badge/Intel-CTI-purple)

Les fiches ci-dessous sont compilées à partir des fichiers mensuels AFRINTEL de 2024. Les dates de publication, de découverte et les niveaux d'incertitude sont conservés lorsqu'ils figurent dans la source. Cette édition a été entièrement recalculée à partir des 12 fichiers victimes mensuels AFRINTEL 2024 (`CyberAttackAfrica/2024/*/victims_FR.md`), qui constituent la source de vérité du projet, et totalise **115 fiches**.

## Janvier 2024

### 1 Janvier 2024

#### 🇰🇪 Kenya - Kenya News Broadcasting Company (K24)

- **Acteur / Groupe :** Tanaka
- **Secteur :** Médias / Audiovisuel
- **Statut :** Claim - Data Sample Published
- **Site web :** [24tv.co.ke](https://24tv.co.ke)
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 2
- **Type d'incident :** Fuite de données
- **Date de la fuite :** 2023 (date exacte non précisée)
- **Date de découverte :** Janvier 2024 (jour exact non précisé ; classement mensuel fixé au 1er janvier)
- **Date de publication de la source :** 19 juin 2023

- **Note de fiabilité :**
  La capture identifie une revendication concernant la base K24 attribuée à Tanaka, le domaine 24tv.co.ke, un fichier SQL annoncé de 28 Mo et environ 56 000 lignes. Le fichier local fourni pour examen n'est pas un SQL lisible : il contient 30,1 Mo d'octets 0xFF, sans lignes ni en-tête SQL exploitable. La date exacte de la compromission et toute confirmation indépendante restent inconnues.

- **Description :**
  Kenya News Broadcasting Company exploite la plateforme d'information K24 au Kenya. La publication présente une revendication de base de données associée au site WordPress de K24.

- **Analyse :**
  L'échantillon visible référence la table WordPress wp_options et des champs de configuration ou de gestion de contenu, notamment les paramètres de bannière de cookies, les catégories et menus, le CSS personnalisé et d'autres options du site. La capture ne permet pas d'établir si des données personnelles, identifiants ou enregistrements utilisateurs complets figuraient dans le fichier SQL revendiqué. AFRINTEL ne reproduit aucune valeur de base de données issue de l'échantillon.

- **Recommandations :**
  1. Vérifier la revendication dans les journaux WordPress, de base de données, de serveur web et d'administration, examiner la table wp_options et les comptes administrateurs actifs, puis faire pivoter les identifiants si une exposition est confirmée.
  2. Auditer les extensions et thèmes, restreindre les exports de base, imposer le MFA aux comptes privilégiés et surveiller le domaine K24 contre le défacement, le phishing ou les modifications non autorisées.

----------------------------

### 1 Janvier 2024

#### 🇩🇿 Algérie - Université d'Oran

- **Acteur / Groupe :** zebi, republication sur un forum cybercriminel
- **Secteur :** Éducation / Enseignement supérieur
- **Statut :** Claim - Data Sample Published
- **Site web :** Non identifié avec certitude
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 2
- **Type d'incident :** Fuite de données
- **Date de la fuite :** 12 septembre 2023
- **Date de découverte :** 1er janvier 2024

- **Note de fiabilité :**
  La publication est explicitement présentée comme un « repost ». Elle contient un échantillon de données attribué à une « University of Oran », mais ne précise pas l'établissement exact, la date de la compromission initiale, le volume total de la base ou la méthode d'accès utilisée. La publication d'origine n'est pas fournie.

- **Description :**
  L'acteur malveillant `zebi` a republié une base de données présentée comme provenant d'une université d'Oran en Algérie. Un échantillon est directement visible dans la publication et un téléchargement supplémentaire est proposé via un contenu verrouillé sur le forum.

- **Analyse :**
  L'échantillon présente une structure de base de données contenant les champs `numero`, `nom`, `prenom`, `datenaiss`, `teleph`, `sexe`, `email`, `mot_passe` et `nationalite`.

  Les enregistrements visibles exposent ainsi des données personnelles et de compte, notamment des identités, dates de naissance, numéros de téléphone, adresses électroniques, sexe et nationalité. Le champ `mot_passe` contient des chaînes ressemblant à des empreintes cryptographiques plutôt qu'à des mots de passe directement lisibles ; l'algorithme utilisé et leur sécurité ne peuvent toutefois pas être confirmés à partir de la capture.

  La présence de plusieurs enregistrements cohérents renforce la crédibilité de la possession d'un jeu de données par l'acteur. En revanche, la capture ne permet pas de confirmer l'origine technique des données, le nombre total de personnes concernées ou l'attribution précise à une université spécifique d'Oran.

  Les données divulguées peuvent faciliter le phishing ciblé, l'usurpation d'identité, la constitution de profils sur les étudiants ou utilisateurs concernés et des tentatives de réutilisation d'identifiants sur d'autres services.

- **Recommandations :**
  1. Identifier l'établissement et l'application potentiellement concernés, puis vérifier les journaux d'authentification et procéder à la réinitialisation des comptes exposés si la fuite est confirmée.
  2. Rechercher toute réutilisation des données dans d'autres publications et sensibiliser les utilisateurs concernés aux risques de phishing et de compromission de comptes.

----------------------------
### 1 Janvier 2024

#### 🇧🇫 Burkina Faso - BIA-Market

- **Acteur / Groupe :** Tanaka, publication sur le forum SQL.ticanalyse.org
- **Secteur :** E-commerce / Retail
- **Statut :** Claim - Data Sample Published
- **Site web :** [bia-market.com](https://www.bia-market.com)
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 2
- **Type d'incident :** Fuite de données
- **Date de la fuite :** 2023 (date exacte non précisée)
- **Date de découverte :** Janvier 2024 (jour exact non précisé ; classement mensuel fixé au 1er janvier)
- **Date de publication de la source :** 23 juin 2023

- **Note de fiabilité :**
  La capture examinée identifie bia-market.com, un filtre de pays correspondant au Burkina Faso (BF-60) et un échantillon SQL. La source indique une date en 2023 et précise que la publication a été mise en ligne le 23 juin 2023. La date exacte de la compromission, le jour de détection, l'application concernée et toute confirmation indépendante restent inconnus.

- **Description :**
  BIA-Market est une plateforme e-commerce opérant au Burkina Faso. La publication présente un fichier SQL de 4,5 Go contenant environ 5 000 lignes et montre des enregistrements issus de la structure de base de données du site. AFRINTEL classe ce cas en janvier 2024 comme période de détection demandée pour cet incident.

- **Analyse :**
  L'échantillon visible référence la table vb_users et des champs tels que l'identifiant de connexion, l'adresse électronique, l'URL utilisateur, la date d'inscription, la clé d'activation, le statut et le nom d'affichage. L'échantillon suggère une exposition de métadonnées de comptes et de plateforme, mais aucune donnée brute d'identification ou donnée personnelle n'est reproduite ici. La capture ne prouve ni l'authenticité ni l'exhaustivité du jeu de données et ne confirme pas comment ou quand BIA-Market aurait été accédé.

- **Recommandations :**
  1. Vérifier la revendication dans les journaux applicatifs, de base de données et de serveur web, faire pivoter les identifiants potentiellement exposés et invalider les sessions ou clés d'activation actives si le jeu de données est confirmé.
  2. Examiner les comptes clients et administrateurs, imposer le MFA lorsqu'il est disponible, surveiller la réutilisation de mots de passe et les campagnes de phishing, et préserver les éléments nécessaires à l'enquête.

----------------------------



### 1 Janvier 2024

#### 🇲🇦 Maroc - Morocco Forum Site

- **Acteur / Groupe :** r57
- **Secteur :** Technologie / Communauté en ligne
- **Statut :** Claim - Data Sample Published
- **Site web :** Non précisé
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Date de découverte :** Janvier 2024 (classement mensuel demandé)
- **Date de publication de la source :** 29 septembre 2023

- **Note de fiabilité :**
  Une publication de forum cybercriminel intitulée « Morocco Forum Site » annonce un jeu de données revendiqué de 180 000 enregistrements et affiche un prix de 50 dollars américains. L'échantillon visible contient des comptes avec des noms d'utilisateur, adresses électroniques, valeurs liées aux mots de passe et champs d'adresses IP. AFRINTEL ne reproduit aucun enregistrement brut, identifiant, empreinte, adresse IP ni information d'accès. La capture ne permet pas d'établir la propriété du forum, l'authenticité du jeu de données, la population exacte concernée ou la date de la compromission sous-jacente.

- **Description :**
  Morocco Forum Site est présenté par la source comme un forum ou une plateforme communautaire en ligne associée à des utilisateurs marocains. L'entité juridique exacte et le domaine ne sont pas identifiés dans la publication.

- **Analyse :**
  L'échantillon visible suggère une exposition de données de comptes utilisateurs et de champs liés à l'authentification. S'il était authentique, le jeu de données pourrait faciliter le phishing ciblé, les tentatives de prise de contrôle de comptes, le credential stuffing ou l'abus de procédures de réinitialisation. Le volume et le prix annoncés restent des revendications de l'acteur. La publication source étant antérieure au classement demandé en janvier 2024, AFRINTEL conserve séparément la date de publication et ne considère pas janvier comme la date de l'incident ou de la publication.

### 1 Janvier 2024

#### 🇷🇼 Rwanda - Gouvernement du Rwanda (plusieurs domaines)

- **Acteur / Groupe :** Milad, publication sur un forum cybercriminel (compte depuis affiché comme banni)
- **Secteur :** Gouvernement / Administration publique
- **Statut :** Claim - Data Sample Published
- **Site web :** [cheno.gov.rw](https://cheno.gov.rw), [cnlg.gov.rw](https://cnlg.gov.rw), [nurc.gov.rw](https://nurc.gov.rw), [yego.gov.rw](https://yego.gov.rw)
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4
- **Type d'incident :** Fuite de données
- **Date de découverte :** Janvier 2024 (classement mensuel demandé)
- **Date de publication de la source :** 17 juin 2023

- **Note de fiabilité :**
  Une publication de forum intitulée « Government Rwanda Database [ Full Backup ] », publiée le 17 juin 2023 par le compte Milad, revendique une sauvegarde SQL combinée de 329 Mo couvrant quatre domaines gouvernementaux rwandais (cheno.gov.rw, cnlg.gov.rw, nurc.gov.rw, yego.gov.rw), indiquant uniquement « 2023 » comme date de fuite et classant les données comme sensibilité « Normal » selon la propre classification de l'auteur. Le compte à l'origine de la publication est actuellement affiché comme banni sur le forum ; le motif du bannissement n'est pas visible dans la publication examinée. L'échantillon affiché montre un export SQL brut d'une table de comptes administrateurs `be_users` contenant des noms d'utilisateur backend, des empreintes de mot de passe (formats phpass et MD5) et de nombreuses données de session/configuration du CMS, ainsi que des contenus en kinyarwanda cohérents avec une communication du secteur public rwandais. AFRINTEL ne reproduit aucun nom d'utilisateur, empreinte de mot de passe, jeton de session ni autre valeur liée aux identifiants présents dans l'échantillon.

- **Description :**
  La revendication cite quatre domaines web gouvernementaux rwandais. D'après leur nom, cnlg.gov.rw correspond à la Commission Nationale de Lutte contre le Génocide (CNLG) et nurc.gov.rw correspond à la Commission Nationale pour l'Unité et la Réconciliation (NURC) ; les institutions précises derrière cheno.gov.rw et yego.gov.rw ne sont pas identifiées dans la source et ne sont pas présumées ici. Le contenu en kinyarwanda visible dans l'échantillon, incluant des références de commémoration liées au génocide, est cohérent avec, sans confirmer de manière indépendante, un lien avec l'un de ces organismes.

- **Analyse :**
  La publication revendique une seule sauvegarde SQL « complète » de 329 Mo couvrant quatre domaines gouvernementaux distincts, une portée inhabituellement large pour un export unique et non corroborée indépendamment au-delà de l'échantillon visible. L'échantillon lui-même affiche une table d'administration backend cohérente (`be_users`) avec des noms d'utilisateur réalistes, des identifiants hachés dans des formats reconnus et des métadonnées de session CMS, ce qui est cohérent avec un export de base de données authentique ; cependant, l'auteur qualifie le CMS de « Custom » alors que la structure de table et les noms de champs visibles dans l'échantillon sont caractéristiques du système de gestion de contenu TYPO3, une incohérence qu'AFRINTEL ne peut pas résoudre à partir des éléments disponibles. Si elle était authentique, la compromission d'identifiants administrateurs backend touchant des institutions gouvernementales nationales et liées à la réconciliation pourrait permettre une manipulation non autorisée de contenu, un accès latéral supplémentaire à des systèmes internes, ainsi qu'un impact réputationnel ou de confiance sur des institutions étatiques liées au mandat rwandais de mémoire du génocide et d'unité nationale. AFRINTEL traite cette publication comme une revendication avec échantillon de données publié ; l'authenticité, la validité actuelle des identifiants et l'étendue de la fuite au-delà de la table examinée ne sont pas vérifiées de manière indépendante.

### 2 Janvier 2024

#### 🇬🇭 Ghana - Financial Intelligence Centre (FIC)

- **Acteur / Groupe :** DataHoes, publication sur un forum cybercriminel
- **Secteur :** Gouvernement / Renseignement financier / Lutte anti-blanchiment
- **Statut :** Data Fully Published
- **Site web :** [fic.gov.gh](https://fic.gov.gh)
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Type d'incident :** Fuite de données
- **Date de la fuite :** 3 décembre 2023
- **Date de découverte :** 2 janvier 2024

- **Note de fiabilité :**
  La publication est attribuée au compte de forum « DataHoes » (depuis banni) et indique une date d'extraction, une taille d'archive, un nombre de fichiers et de dossiers, ainsi qu'un lien vers une liste complète de l'arborescence hébergée sur un service tiers de partage de fichiers. AFRINTEL a examiné la publication et l'échantillon d'arborescence, mais n'a pas téléchargé ni ouvert l'archive référencée ni le fichier de liste complète.

- **Description :**
  Le Financial Intelligence Centre (FIC) est l'agence nationale ghanéenne chargée de recevoir et d'analyser les déclarations de transactions suspectes et autres informations liées au blanchiment de capitaux, au financement du terrorisme et au financement de la prolifération, et de diffuser des renseignements exploitables aux autorités compétentes.

- **Analyse :**
  L'acteur indique que les données ont été extraites le 3 décembre 2023, et décrit une archive de 2,0 Gio répartie sur 6 025 fichiers et 663 sous-dossiers, avec une liste complète de l'arborescence publiée séparément. L'échantillon d'arborescence montre des dossiers intitulés « FIC HR DOCS » et « Finance_Scans », contenant des documents internes de gouvernance et de ressources humaines (manuel comptable, manuel d'audit, charte du conseil d'administration, documents relatifs aux conditions de service et aux politiques RH, fichiers d'effectifs) ainsi que des correspondances financières scannées sur plusieurs années (demandes de relevés bancaires, autorisations de paiement, demandes de change, avis de paie mensuels). Un nom de fichier fait explicitement référence à la réponse du FIC à une procédure de nomination GIABA/ICRG, ce qui est cohérent avec le mandat connu du FIC en matière de lutte anti-blanchiment et appuie l'authenticité du jeu de données. Plusieurs noms de fichiers de l'échantillon font également référence à des certificats académiques et documents de paie de membres du personnel nommément identifiés.

  Compte tenu de la sensibilité des documents internes RH, de paie, bancaires et de gouvernance d'une unité nationale de renseignement financier, l'exposition de ce matériel pourrait faciliter l'ingénierie sociale ou le phishing ciblé visant le personnel du FIC, la divulgation de dispositifs bancaires internes, ainsi qu'un impact réputationnel ou opérationnel sur un organisme central du dispositif ghanéen de lutte anti-blanchiment et de financement du terrorisme. AFRINTEL n'a pas accédé à l'archive référencée ni au fichier de liste d'arborescence, et ne reproduit aucun nom de membre du personnel, chiffre financier ou contenu de document au-delà des noms de dossiers et de fichiers visibles dans la publication examinée.

- **Recommandations :**
  1. Le FIC devrait vérifier si l'extraction décrite provient effectivement de ses propres systèmes, examiner les journaux d'accès antérieurs et autour du 3 décembre 2023, et évaluer l'exposition des données bancaires, de paie et RH mentionnées dans la publication.
  2. Faire pivoter tout identifiant ou référence de correspondance bancaire nommé dans les documents exposés, et surveiller toute réutilisation ultérieure de l'arborescence divulguée dans des campagnes de phishing visant le personnel du FIC ou des institutions partenaires.

----------------------------

### 3 Janvier 2024

#### 🇳🇬 Nigeria - The Citizens' Watch

- **Acteur / Groupe :** X0Frankenstein, publication sur un forum cybercriminel
- **Secteur :** Société civile / Gouvernance / Organisation à but non lucratif
- **Statut :** Claim - Data Sample Published
- **Site web :** [thecitizenswatch.com](https://thecitizenswatch.com/)
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Date de découverte :** 3 janvier 2024
- **Date de fuite revendiquée :** 2023 (année uniquement, aucune date précise fournie par la source)

- **Note de fiabilité :**
  Une publication de forum intitulée « SQL Database The Citizens Watch », publiée le 3 janvier 2024 par le compte X0Frankenstein, revendique une fuite de base de données SQL associée à thecitizenswatch.com, décrivant plus de 56 000 lignes et indiquant uniquement « 2023 » comme date de fuite. La publication affiche des extraits SQL bruts couvrant plusieurs structures de table distinctes, notamment des comptes utilisateur/administrateur avec des empreintes de mot de passe au format bcrypt, des enregistrements d'inscription à des événements et formations, des candidatures/CV, ainsi qu'une table de référence géographique apparemment sans lien direct, incluse dans le même extrait. AFRINTEL ne reproduit aucun nom, adresse électronique, numéro de téléphone, empreinte de mot de passe, chemin de fichier téléversé ni autre donnée personnelle visible dans l'échantillon.

- **Description :**
  The Citizens' Watch (thecitizenswatch.com) est présenté comme une plateforme de suivi des promesses permettant aux citoyens, à la société civile, aux journalistes, chercheurs et analystes de politiques publiques de suivre les engagements de campagne des responsables gouvernementaux. Elle est décrite comme une initiative de The Reformers Initiative for Development in Africa (« Reformers of Africa »), une organisation panafricaine de civic-tech à but non lucratif, présentée comme active dans plusieurs pays africains dont le Nigeria, le Soudan du Sud, la Namibie, la République démocratique du Congo, la Tunisie, les Comores et l'Afrique du Sud. Le pays précis d'enregistrement ou le siège de l'organisation n'est pas indiqué dans la source ; l'échantillon visible montre une forte concentration de coordonnées nigérianes (Lagos, Ekiti, Oyo, Ogun, Kogi, Anambra), ce qui conduit AFRINTEL à classer cette entrée sous le Nigeria, tout en signalant la portée panafricaine de l'organisation.

- **Analyse :**
  L'extrait visible mélange plusieurs structures de table distinctes plutôt qu'un schéma cohérent unique, ce qui est cohérent soit avec un export multi-tables réellement compromis, soit avec un extrait assemblé ; AFRINTEL ne peut pas confirmer indépendamment l'origine de chaque segment de table. Lorsqu'ils sont lisibles, les enregistrements de l'échantillon comprennent des comptes utilisateur avec noms, adresses électroniques, numéros de téléphone, une empreinte de mot de passe au format bcrypt, des références de fichiers CV téléversés, des dates de naissance et des champs de statut de compte, ainsi que des inscriptions à des événements/formations et une table géographique apparemment sans lien. Si elle est authentique, l'exposition de ces données pourrait exposer les données personnelles de citoyens et d'inscrits à des événements (noms, coordonnées, documents CV) à des risques de phishing, d'ingénierie sociale et de prise de contrôle de compte, et toute empreinte de mot de passe exposée pourrait faire l'objet d'un cassage hors ligne si le schéma de hachage est faible ou réutilisé ailleurs. AFRINTEL classe cette publication comme une revendication avec échantillon de données publié, compte tenu du volume et de la structure des enregistrements visibles, tout en précisant que la propriété de chaque segment de table et l'étendue complète de la base de données sous-jacente ne sont pas vérifiées de manière indépendante.

----------------------------

### 7 Janvier 2024

#### 🇨🇲 Cameroun - University of Buea (UB)

- **Acteur / Groupe :** cnHunter, publication sur un forum cybercriminel
- **Secteur :** Éducation / Enseignement supérieur / Recherche
- **Statut :** Claim - Unverified
- **Site web :** [ubuea.cm](https://ubuea.cm)
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Vente d'accès
- **Date de découverte :** 7 janvier 2024

- **Note de fiabilité :**
  Une publication de forum intitulée « [Admin Access] ubuea.cm », publiée le 7 janvier 2024 et modifiée le même jour, revendique un accès de niveau administrateur à une instance REDCap hébergée sur redcap.ubuea.cm, en référençant un chemin de gestionnaire d'importation/upload et un fichier externe hébergé sur un service de partage de fichiers présenté comme « preuve ». AFRINTEL n'a pas accédé au fichier de preuve référencé ni au système ciblé revendiqué. Le compte à l'origine de la publication, cnHunter, a ensuite été définitivement banni du forum pour suspicion d'arnaque, ce qui réduit fortement la fiabilité de la revendication.

- **Description :**
  L'University of Buea (UB) est une université publique située dans la région du Sud-Ouest du Cameroun, proposant des formations dans plusieurs facultés dont les sciences, les sciences de la santé, l'ingénierie, les lettres, le droit et les sciences sociales et de gestion. Les instances REDCap déployées par les universités sont généralement utilisées pour gérer des données académiques, d'enquête ou de recherche clinique.

- **Analyse :**
  La publication revendique un accès administrateur à une instance REDCap associée au domaine de l'université, marquée ultérieurement comme « Unlocked » dans une modification, mais ne fournit aucun échantillon de données visible, aucune preuve indépendamment vérifiable ni prix indiqué. Combiné au bannissement définitif ultérieur du compte pour suspicion d'arnaque, AFRINTEL traite cette publication comme une revendication non vérifiée à faible niveau de confiance. Si elle était authentique, un accès administrateur non autorisé à une instance REDCap pourrait exposer des données académiques, d'enquête ou de recherche liées à des étudiants, membres du personnel ou participants à des études ; ni l'accès ni un éventuel jeu de données sous-jacent ne sont confirmés.

----------------------------

### 10 Janvier 2024

#### 🇿🇦 Afrique du Sud - TiAuto Investments
- **Groupe ransomware :** lockbit3
- **Secteur :** Industrie automobile & Distribution
- **Site web :** [tiautoinvestments.co.za](https://www.tiautoinvestments.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** TiAuto Investments est un groupe de premier plan en Afrique du Sud spécialisé dans le commerce de gros et de détail de jantes, de pneus et de produits automobiles. Fondé en 2006 et basé à Midrand, il détient des marques phares du continent telles que Tiger Wheel & Tyre et Tyres & More.

----------------------------

### 10 Janvier 2024

#### 🇿🇦 Afrique du Sud - Tiger Wheel & Tyre
- **Groupe ransomware :** lockbit3
- **Secteur :** Automobile & Services de maintenance
- **Site web :** [twt.co.za](https://twt.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Tiger Wheel & Tyre est une filiale majeure du groupe TiAuto Investments, forte de plus de 50 ans d'existence et exploitant plus de 100 centres de services à travers l'Afrique du Sud et l'Afrique australe. Elle est spécialisée dans les services de géométrie, d'équilibrage et la vente de pneumatiques toutes catégories.

----------------------------

### 26 Janvier 2024

#### 🇪🇬 Égypte - Btech.com
- **Acteur / Groupe :** Tanaka, publication sur un forum cybercriminel (RaidForums)
- **Secteur :** Commerce de détail / Électronique
- **Site web :** [btech.com](https://www.btech.com)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 2
- **Type d'incident :** Fuite de données
- **Description victime :** Btech.com est une chaîne égyptienne de vente au détail d'appareils électroniques et électroménagers.
- **Analyse :** L'acteur Tanaka, modérateur du forum, a publié le 26 janvier 2024 une revendication concernant Btech.com, décrite comme un export CSV de 20 Mo daté du 23 février 2023 et totalisant 203 265 lignes. L'en-tête de champs annoncé comprend : ID, Name, Email, Phone, ZIP, Country, State/Province, Customer Since, Billing Address, Shipping Address, Date of Birth, Gender, Street Address, City, Company.

  L'échantillon affiché dans le post montre des enregistrements clients réels avec noms, adresses email, adresses postales détaillées en arabe, dates de naissance (majoritairement non renseignées) et genre. Plusieurs lignes de l'échantillon contiennent en outre des valeurs supplémentaires au-delà des 15 champs annoncés dans l'en-tête, correspondant à des numéros à 14 chiffres au format des numéros d'identification nationale égyptiens, ainsi qu'à un nom et un numéro de téléphone distincts de ceux du titulaire principal du compte, suggérant une structure de données plus riche que celle décrite dans l'en-tête public du post.

  La cohérence du format CSV, le volume annoncé et la présence d'enregistrements clients plausibles avec adresses détaillées appuient un niveau de confiance élevé quant à l'authenticité de cette fuite, bien que le volume total de 203 265 lignes n'ait pas pu être vérifié indépendamment au-delà de l'échantillon observé. La présence possible de numéros d'identification nationale non documentés dans l'en-tête constitue un facteur aggravant, cette donnée étant particulièrement sensible en Égypte. L'exposition de ces données pourrait faciliter l'usurpation d'identité, la fraude et le phishing ciblé contre les clients de l'enseigne. AFRINTEL ne reproduit aucun nom, adresse email, adresse postale, date de naissance ni numéro d'identification issus de l'échantillon examiné.

### 29 Janvier 2024

#### 🇿🇦 Afrique du Sud - Crowe Southern Africa
- **Groupe ransomware :** lockbit3
- **Secteur :** Audit, Conseil & Comptabilité
- **Site web :** [crowe.com/za](https://www.crowe.com/za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Crowe Southern Africa est un cabinet de services professionnels de premier plan et membre indépendant du réseau mondial Crowe Global. Établi de longue date avec des bureaux à Johannesburg, Cape Town et Stellenbosch, il fournit des services d'audit, de fiscalité, de juricomptabilité (forensics) et de conseil financier.

----------------------------

## Février 2024

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

## Mars 2024

### 1 Mars 2024

#### 🇪🇹 Éthiopie - Portails fédéraux eTrade et eRIS
- **Acteur / Groupe :** ThreatSec
- **Secteur :** Gouvernement / Services publics numériques
- **Site web :** [etrade.gov.et](https://etrade.gov.et) ; [eris.efda.gov.et](https://eris.efda.gov.et)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Description victime :** La publication associe le portail eTrade du ministère éthiopien du Commerce et de l'Intégration régionale au système eRIS de l'Ethiopian Food and Drug Authority. Il s'agit de deux services fédéraux distincts réunis dans une même revendication.

- **Analyse :**
  - **Observé :** la fiche est classée au 1er mars 2024 à la demande du mainteneur. La publication de forum, relayée par Tanaka et datée du 24 août 2023, attribue à ThreatSec une revendication d’accès aux deux portails et de collecte de 43 fichiers, dont des PDF, des images et des documents d'identité gouvernementaux. Un PDF fourni localement a été examiné en lecture seule : 3 023 068 octets, cinq pages scannées, SHA-256 `5184bdfc94dfd42e4d78da290ea3860ac074360c684a715354e0447241bfc642`. Les cinq pages contiennent un document administratif et contractuel en amharique, avec des cachets officiels, des signatures manuscrites et des montants financiers. Aucune donnée personnelle brute n'est reproduite.
  - **Hypothèse :** les caractéristiques documentaires sont cohérentes avec un document administratif éthiopien et renforcent la plausibilité structurelle de l'échantillon, sans établir sa provenance technique.
  - **Inconnu :** la méthode d'acquisition, le lien direct du PDF avec chacun des deux portails, l'existence et le contenu des 42 autres fichiers revendiqués, ainsi qu'une confirmation par les organismes concernés restent non vérifiés. L'examen visuel couvre les cinq pages, mais l'OCR complet de l'amharique n'a pas pu être validé.

----------------------------

----------------------------

### 9 Mars 2024

#### 🇪🇬 Égypte - Go4Kora
- **Groupe ransomware :** ransomhub
- **Secteur :** Médias sportifs & Divertissement
- **Site web :** [go4kora.tv](https://go4kora.tv)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Go4Kora est un portail d'actualités sportives et de streaming en direct largement suivi en Égypte et dans la région MENA pour la diffusion du football.

----------------------------

### 11 Mars 2024

#### 🇿🇦 Afrique du Sud - Government Printing Works (GPW)
- **Groupe ransomware :** lockbit3
- **Secteur :** Administrations publiques & Impressions de sécurité d'État
- **Site web :** [gpw.gov.za](https://www.gpw.gov.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Le Government Printing Works d'Afrique du Sud est une entité publique sous la tutelle du ministère de l'Intérieur, chargée de la production des documents d'identité sécurisés, des passeports et des bulletins officiels.

----------------------------

### 15 Mars 2024

#### 🇹🇳 Tunisie - ATL Leasing
- **Groupe ransomware :** hunters
- **Secteur :** Services financiers & Crédit-bail
- **Site web :** [atlleasing.com.tn](https://www.atlleasing.com.tn)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Arab Tunisian Leasing (ATL) est une institution financière de premier plan cotée à la Bourse de Tunis, spécialisée dans le financement par crédit-bail d'équipements professionnels et immobiliers.

----------------------------

### 15 Mars 2024

#### 🇪🇬 Égypte - El Ezaby Pharmacy
- **Groupe ransomware :** lockbit3
- **Secteur :** Santé & Distribution pharmaceutique
- **Site web :** [elezabypharmacy.com](https://www.elezabypharmacy.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Pharmacies El Ezaby représente l'un des plus grands réseaux de distribution pharmaceutique en Égypte, exploitant de nombreuses officines et une logistique de livraison nationale.

----------------------------

### 16 Mars 2024

#### 🇳🇦 Namibie - Agribank Namibia
- **Groupe ransomware :** lockbit3
- **Secteur :** Secteur bancaire & Financement agricole
- **Site web :** [agribank.com.na](https://www.agribank.com.na)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** L'Agricultural Bank of Namibia est une institution bancaire étatique spécialisée dans le financement de l'expansion agricole, de l'aquaculture et de l'acquisition de terres rurales.

----------------------------

### 22 Mars 2024

#### 🇪🇬 Égypte - PGESCo
- **Groupe ransomware :** ransomhub
- **Secteur :** Énergie & Ingénierie des infrastructures
- **Site web :** [pgesco.com](https://www.pgesco.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** La Power Generation Engineering and Services Company (PGESCo) est une firme d'ingénierie égyptienne majeure fournissant des services de conseil et de gestion de projet pour les centrales électriques et les infrastructures pétrolières.

----------------------------

### 26 Mars 2024

#### 🇲🇦 Maroc - Higher School of Commerce and Management (ESGC.MA)
- **Acteur / Groupe :** Non attribué ; publication par UnknownMember
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [esgc.ma](https://esgc.ma)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Description victime :** ESGC.MA est présentée comme un établissement marocain d'enseignement supérieur spécialisé dans le commerce et le management.

- **Analyse :** La publication de forum du 26 mars 2024 affirme qu'une base de 2021 contenait environ 500 entrées avec des noms, adresses électroniques, hashes de mots de passe, numéros de téléphone et dates de création de comptes. Un échantillon était affiché, mais le jeu de données complet et la compromission alléguée n'ont pas été vérifiés indépendamment. Les données personnelles et identifiants de l'échantillon ne sont pas reproduits ici.

----------------------------

### 27 Mars 2024

#### 🇿🇦 Afrique du Sud - Nampak
- **Groupe ransomware :** lockbit3
- **Secteur :** Industrie manufacturière (Emballages industriels)
- **Site web :** [nampak.com](https://www.nampak.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Nampak est le plus grand fabricant d'emballages du continent africain, basé en Afrique du Sud, fournissant des solutions de conditionnement en métal, plastique, papier et verre.

----------------------------

## Avril 2024

### 04 Avril 2024
#### 🇸🇨 Seychelles - Remitano (Cryptocurrency Exchange)
- **Groupe ransomware :** incransom
- **Secteur :** Institutions bancaires et financières / Crypto-actifs
- **Site web :** N/A (Application mobile & Plateforme d'échange)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Remitano (Cryptocurrency Exchange) figure sur le site de fuite du groupe incransom. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Remitano est une plateforme internationale d'échange de crypto-monnaies en pair-à-pair (P2P) sécurisée par séquestre, permettant l'achat, la vente et le stockage d'actifs numériques avec des devises fiduciaires.

- **Analyse :**
  AFRINTEL a recensé Remitano (Cryptocurrency Exchange) (Seychelles) comme victime revendiquée par le groupe ransomware incransom. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Institutions bancaires et financières / Crypto-actifs, une compromission de ce type exposerait généralement des données de comptes clients, de paiement ou financières, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par incransom, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de paiement et de réponse à incident adaptées au secteur financier en cas d'éléments de compromission avérés.

### 19 Avril 2024
#### 🇪🇬 Égypte - Vezeeta Pharmacy (vezeeta.com)

- **Date de publication initiale :** 19 avril 2024
- **Date de détection AFRINTEL :** 21 août 2026
- **Acteur / Groupe :** EgyptLeaks, publication sur un forum cybercriminel
- **Secteur :** Santé / Pharmacie en ligne
- **Site web :** [vezeeta.com](https://www.vezeeta.com)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données

- **Description :**

  Vezeeta est une plateforme égyptienne de réservation de soins et de services de pharmacie en ligne. La publication vise spécifiquement Vezeeta Pharmacy et annonce des données de commandes.

- **Analyse :**

  **Observed :** Une publication attribuée à EgyptLeaks, datée du 19 avril 2024, propose à la vente environ 133 000 enregistrements de commandes de Vezeeta Pharmacy couvrant 2021, 2022 et 2023. La publication affiche un échantillon de lignes de commandes comprenant des champs de contact, de zone, de statut de commande, de paiement, de branche, de produits et d'adresses de livraison. Les valeurs personnelles visibles dans l'échantillon n'ont pas été reprises dans AFRINTEL.

  **Assumption :** La concordance entre le nom de Vezeeta Pharmacy, le domaine vezeeta.com, les noms de branches et la structure d'un export de commandes est compatible avec une exposition de données clients en Égypte. Si les données sont authentiques, elles pourraient faciliter le phishing ciblé, la fraude à la livraison, l'usurpation de personnel ou de pharmacies et l'exposition d'informations de santé indirectement déduites des produits commandés.

  **Unknown :** AFRINTEL n'a pas reçu l'archive complète ni confirmé les 133 000 commandes, la méthode d'acquisition, l'exhaustivité, la validité actuelle des coordonnées, la présence de données médicales protégées ou une confirmation de Vezeeta. L'analyse repose sur la capture et l'extrait visibles ; aucun nom, téléphone, adresse, produit associé à une personne ou identifiant de commande n'est reproduit.

### 13 Avril 2024
#### 🇿🇦 Afrique du Sud - Caxton and CTP Publishers and Printers
- **Groupe ransomware :** hunters
- **Secteur :** Médias, édition et audiovisuel
- **Site web :** https://www.caxton.co.za
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Caxton and CTP Publishers and Printers figure sur le site de fuite du groupe hunters. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Caxton & CTP est l'un des plus grands éditeurs et imprimeurs de journaux, de magazines et d'emballages commerciaux en Afrique du Sud.

- **Analyse :**
  AFRINTEL a recensé Caxton and CTP Publishers and Printers (Afrique du Sud) comme victime revendiquée par le groupe ransomware hunters. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Médias, édition et audiovisuel, une compromission de ce type exposerait généralement des données employés, clients ou opérationnelles, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par hunters, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données et de réponse à incident en cas d'éléments de compromission avérés.

### 23 Avril 2024
#### 🇧🇫 Burkina Faso - ONEF (Observatoire national de l’emploi et de la formation)
- **Acteur / Groupe :** Pedi
- **Secteur :** Gouvernement / Emploi et formation
- **Site web :** [onef.gov.bf](https://onef.gov.bf)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d’impact :** Level 3
- **Type d’incident :** Fuite de données
- **Description :** L’Observatoire national de l’emploi et de la formation (ONEF) est une institution publique burkinabè consacrée aux informations sur l’emploi et la formation professionnelle.
- **Analyse :** Une publication sur un forum présente une base associée à onef.gov.bf comme une diffusion SQL gratuite et montre la structure d’une table applicative nommée `actualite`, avec des champs liés aux actualités et aux métadonnées de publication. La capture ne permet pas d’établir l’authenticité, l’exhaustivité ou la méthode d’accès initiale. AFRINTEL enregistre cette publication comme une revendication accompagnée d’un échantillon et ne reproduit aucune valeur de la base.

### 29 Avril 2024
#### 🇲🇦 Maroc - SM EMBALLAGE
- **Groupe ransomware :** spacebears
- **Secteur :** Industrie manufacturière / Emballages industriels
- **Site web :** https://smemballage.com/
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  SM EMBALLAGE figure sur le site de fuite du groupe spacebears. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  SM Emballage est une entreprise marocaine spécialisée dans la conception et la fabrication d'emballages personnalisés et de solutions de protection pour le secteur agroalimentaire et industriel.

- **Analyse :**
  AFRINTEL a recensé SM EMBALLAGE (Maroc) comme victime revendiquée par le groupe ransomware spacebears. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Industrie manufacturière / Emballages industriels, une compromission de ce type exposerait généralement des données fournisseurs, clients ou opérationnelles, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par spacebears, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données opérationnelles et de réponse à incident en cas d'éléments de compromission avérés.

### 29 Avril 2024
#### 🇿🇦 Afrique du Sud - Thinkadam
- **Groupe ransomware :** spacebears
- **Secteur :** Technologies de l'information / Téléphonie
- **Site web :** https://www.thinkadam.co/
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Thinkadam figure sur le site de fuite du groupe spacebears. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Thinkadam fournit des solutions technologiques avancées de verrouillage d'appareils à destination de l'industrie du crédit sur smartphones, visant à réduire les défauts de paiement.

- **Analyse :**
  AFRINTEL a recensé Thinkadam (Afrique du Sud) comme victime revendiquée par le groupe ransomware spacebears. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Technologies de l'information / Téléphonie, une compromission de ce type exposerait généralement des données clients, partenaires ou techniques internes, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par spacebears, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de réponse à incident adaptées au secteur technologique en cas d'éléments de compromission avérés.

### 30 Avril 2024
#### 🇱🇾 Libye - Mellitah Oil & Gas (Eni / NOC Joint Venture)
- **Groupe ransomware :** ransomhub
- **Secteur :** Énergie / Pétrole & Gaz
- **Site web :** N/A
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Mellitah Oil & Gas (Eni / NOC Joint Venture) figure sur le site de fuite du groupe ransomhub. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Mellitah Oil & Gas est un consortium d'exploration et d'exploitation énergétique majeur en Libye, opéré conjointement par la National Oil Corporation (NOC) et la major italienne Eni.

- **Analyse :**
  AFRINTEL a recensé Mellitah Oil & Gas (Eni / NOC Joint Venture) (Libye) comme victime revendiquée par le groupe ransomware ransomhub. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Énergie / Pétrole & Gaz, une compromission de ce type exposerait généralement des données employés, clients ou opérationnelles, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par ransomhub, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données et de réponse à incident en cas d'éléments de compromission avérés.

----------------------------

## Mai 2024

### 6 Mai 2024

#### 🇳🇬 Nigeria - Nestoil
- **Groupe ransomware :** blacksuit
- **Secteur :** Construction
- **Site web :** [nestoilgroup.com](https://www.nestoilgroup.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Nestoil est une entreprise commerciale majeure opérant dans le secteur des construction, contribuant de manière significative au tissu économique régional en Nigeria.

----------------------------

### 6 Mai 2024

#### 🇪🇬 Égypte - Elarabygroup
- **Groupe ransomware :** lockbit3
- **Secteur :** Business Services
- **Site web :** [elarabygroup.com](https://www.elarabygroup.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Elarabygroup est une entreprise commerciale majeure opérant dans le secteur des business services, contribuant de manière significative au tissu économique régional en Egypt.

----------------------------

### 7 Mai 2024

#### 🇿🇦 Afrique du Sud - Lenmed
- **Groupe ransomware :** lockbit3
- **Secteur :** Healthcare services
- **Site web :** [lenmed.co.za](https://www.lenmed.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Lenmed est une entreprise commerciale majeure opérant dans le secteur des healthcare services, contribuant de manière significative au tissu économique régional en South Africa.

----------------------------

### 7 Mai 2024

#### 🇿🇦 Afrique du Sud - Kamo jou trading
- **Groupe ransomware :** ransomhub
- **Secteur :** Services financiers & Assurances
- **Site web :** [kamojou.co.za](https://www.kamojou.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Kamo jou trading est une entreprise commerciale majeure opérant dans le secteur des finance, contribuant de manière significative au tissu économique régional en South Africa.

----------------------------

### 9 Mai 2024

#### 🇳🇦 Namibie - Eif.na
- **Groupe ransomware :** lockbit3
- **Secteur :** Financial organizations
- **Site web :** [eif.org.na](https://www.eif.org.na)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Eif.na est une entreprise commerciale majeure opérant dans le secteur des financial organizations, contribuant de manière significative au tissu économique régional en Namibia.

----------------------------

### 13 Mai 2024

#### 🇨🇮 Côte d'Ivoire - Treasury of cote d'ivoire
- **Groupe ransomware :** hunters
- **Secteur :** Services financiers & Assurances
- **Site web :** [tresor.gouv.ci](https://www.tresor.gouv.ci)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Treasury of cote d'ivoire est une entreprise commerciale majeure opérant dans le secteur des finance, contribuant de manière significative au tissu économique régional en Côte d'Ivoire.

----------------------------

### 16 Mai 2024

#### 🇪🇬 Égypte - Egyptian sudanese
- **Groupe ransomware :** arcusmedia
- **Secteur :** Services
- **Site web :** [egyptian sudanese.com](https://www.egyptian sudanese.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Egyptian sudanese est une entreprise commerciale majeure opérant dans le secteur des services, contribuant de manière significative au tissu économique régional en Egypt.

----------------------------

### 25 Mai 2024

#### 🇸🇳 Sénégal - Sysroad
- **Groupe ransomware :** lockbit3
- **Secteur :** Information Technologies Consulting
- **Site web :** [sysroad.com](https://www.sysroad.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Sysroad est une entreprise commerciale majeure opérant dans le secteur des information technologies consulting, contribuant de manière significative au tissu économique régional en Senegal.

----------------------------

## Juin 2024

### 4 Juin 2024

#### 🇿🇦 Afrique du Sud - Botselo
- **Groupe ransomware :** arcusmedia
- **Secteur :** Agriculture and agribusiness
- **Site web :** [botselo.com](https://www.botselo.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Botselo figure sur le site de fuite du groupe arcusmedia. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Botselo est une entreprise commerciale majeure opérant dans le secteur des agriculture and agribusiness, contribuant de manière significative au tissu économique régional en South Africa.

- **Analyse :**
  AFRINTEL a recensé Botselo (Afrique du Sud) comme victime revendiquée par le groupe ransomware arcusmedia. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Agriculture and agribusiness, une compromission de ce type exposerait généralement des données fournisseurs, clients ou opérationnelles, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par arcusmedia, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données opérationnelles et de réponse à incident en cas d'éléments de compromission avérés.

----------------------------

### 6 Juin 2024

#### 🇨🇬 Congo - Burotec.biz
- **Groupe ransomware :** eldorado
- **Secteur :** Services
- **Site web :** [burotec.biz](https://www.burotec.biz)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Burotec.biz figure sur le site de fuite du groupe eldorado. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Burotec.biz est une entreprise commerciale majeure opérant dans le secteur des services, contribuant de manière significative au tissu économique régional en Congo.

- **Analyse :**
  AFRINTEL a recensé Burotec.biz (Congo) comme victime revendiquée par le groupe ransomware eldorado. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Services, une compromission de ce type exposerait généralement des données employés, clients ou opérationnelles, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par eldorado, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données et de réponse à incident en cas d'éléments de compromission avérés.

----------------------------

### 23 Juin 2024

#### 🇿🇦 Afrique du Sud - Www.glynmarais
- **Groupe ransomware :** cactus
- **Secteur :** Attorney
- **Site web :** [glynmarais.co.za](https://www.glynmarais.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Www.glynmarais figure sur le site de fuite du groupe cactus. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Www.glynmarais est une entreprise commerciale majeure opérant dans le secteur des attorney, contribuant de manière significative au tissu économique régional en South Africa.

- **Analyse :**
  AFRINTEL a recensé Www.glynmarais (Afrique du Sud) comme victime revendiquée par le groupe ransomware cactus. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Attorney, une compromission de ce type exposerait généralement des données clients et des informations liées aux dossiers, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par cactus, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de confidentialité des données clients et de réponse à incident en cas d'éléments de compromission avérés.

----------------------------

## Juillet 2024

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
#### 🇪🇹 Éthiopie - F.D.R.E Defence War College (domaine cité : nwc.ndu.edu)

- **Acteur / Groupe :** TheColorYellow, publication postée sur RaidForums
- **Secteur :** Défense / Enseignement militaire
- **Statut :** Claim - Data Sample Published
- **Site web :** [dwc.edu.et](https://dwc.edu.et/wc/) (organisation observée dans les échantillons) ; domaine cité par l'acteur : nwc.ndu.edu
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4
- **Type d'incident :** Fuite de données
- **Date de découverte :** 02 juillet 2024

- **Note de fiabilité :**
  La publication de TheColorYellow annonce une victime présentée comme le « National War College of Ethiopia » et cite le domaine nwc.ndu.edu. Ce domaine correspond au National War College de la National Defense University des États-Unis. Toutefois, les cinq fichiers PNG fournis localement présentent l'emblème et l'en-tête en amharique du « F.D.R.E Defence War College » éthiopien, ainsi que des documents internes, un inventaire de 29 postes et un tableau de 17 entrées téléphoniques. Une erreur de domaine dans l'annonce, une confusion de nom ou une attribution technique incorrecte restent donc possibles. AFRINTEL retient comme organisation observée le F.D.R.E Defence War College et conserve nwc.ndu.edu comme domaine annoncé mais non vérifié.

- **Description :**
  Les éléments visibles correspondent au F.D.R.E Defence War College, établissement d’enseignement militaire éthiopien. Le lien officiel observé pour cette organisation est [dwc.edu.et](https://dwc.edu.et/wc/). Le domaine nwc.ndu.edu reste uniquement le domaine cité dans l’annonce de l’acteur.

- **Analyse CTI :**
  L'acteur TheColorYellow affirme détenir 747 Mo de courriels confidentiels prétendument volés directement sur le serveur Exchange de l'établissement, exportés sous forme de fichiers de boîtes aux lettres PST, et propose ces données pour 500 $ avec recours à un escrow. Le répertoire local fourni contient cinq PNG, mais aucun PST, EML, MSG ou export Exchange. Les images comprennent des documents institutionnels, un avis en chinois pour les étudiants internationaux, un inventaire visible de 29 postes et un tableau visible de 17 entrées téléphoniques. Ces éléments sont cohérents avec des documents internes du F.D.R.E Defence War College et renforcent l'attribution de l'échantillon, mais ne confirment ni l'accès au serveur Exchange, ni l'existence des 747 Mo, ni l'exhaustivité ou l'origine des données. L'OCR amharique et chinois n'a pas été utilisé pour transcrire les valeurs ; aucun nom, numéro, identifiant matériel ou numéro de téléphone n'est reproduit.

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

----------------------------

## Août 2024

### 01 Août 2024

#### 🇸🇨 Seychelles - Remitano
- **Groupe ransomware :** meow
- **Secteur :** Services financiers & Assurances
- **Site web :** [remitano.com](https://www.remitano.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Remitano figure sur le site de fuite du groupe meow. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Remitano est une entreprise commerciale majeure opérant dans le secteur des finance, contribuant de manière significative au tissu économique régional en Seychelles.

- **Analyse :**
  AFRINTEL a recensé Remitano (Seychelles) comme victime revendiquée par le groupe ransomware meow. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Services financiers & Assurances, une compromission de ce type exposerait généralement des données de comptes clients, de paiement ou financières, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par meow, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de paiement et de réponse à incident adaptées au secteur financier en cas d'éléments de compromission avérés.

----------------------------

### 11 Août 2024

#### 🇿🇦 Afrique du Sud - Acdcexpress
- **Groupe ransomware :** lockbit3
- **Secteur :** Retail (distribution)
- **Site web :** [acdcexpress.com](https://www.acdcexpress.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Acdcexpress figure sur le site de fuite du groupe lockbit3. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Acdcexpress est une entreprise commerciale majeure opérant dans le secteur des retail (distribution), contribuant de manière significative au tissu économique régional en South Africa.

- **Analyse :**
  AFRINTEL a recensé Acdcexpress (Afrique du Sud) comme victime revendiquée par le groupe ransomware lockbit3. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Retail (distribution), une compromission de ce type exposerait généralement des données clients et de transaction, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par lockbit3, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de réponse à incident adaptées au secteur du commerce en cas d'éléments de compromission avérés.

----------------------------

### 13 Août 2024

#### 🇿🇼 Zimbabwe - Netone
- **Groupe ransomware :** hunters
- **Secteur :** Télécommunications
- **Site web :** [netone.co.zw](https://www.netone.co.zw)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Netone figure sur le site de fuite du groupe hunters. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Netone est un opérateur de réseau mobile de premier plan fournissant des infrastructures de télécommunications, des services de téléphonie et des données haut débit.

- **Analyse :**
  AFRINTEL a recensé Netone (Zimbabwe) comme victime revendiquée par le groupe ransomware hunters. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Télécommunications, une compromission de ce type exposerait généralement des données employés, clients ou opérationnelles, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par hunters, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données et de réponse à incident en cas d'éléments de compromission avérés.

----------------------------

### 13 Août 2024

#### 🇿🇦 Afrique du Sud - Lenmed
- **Groupe ransomware :** darkvault
- **Secteur :** Healthcare services
- **Site web :** [lenmed.co.za](https://www.lenmed.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Lenmed figure sur le site de fuite du groupe darkvault. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Note de double revendication :**
  Lenmed (lenmed.co.za) avait déjà été enregistrée comme revendiquée par lockbit3 le 7 mai 2024 (Claim - Unverified). L'acteur et la date diffèrent, et aucun élément n'indique une republication du même matériel ou une revente du même jeu de données. AFRINTEL enregistre cette publication de darkvault comme une revendication indépendante, en l'état des éléments disponibles.

- **Description :**
  Lenmed est une entreprise commerciale majeure opérant dans le secteur des healthcare services, contribuant de manière significative au tissu économique régional en South Africa.

- **Analyse :**
  AFRINTEL a recensé Lenmed (Afrique du Sud) comme victime revendiquée par le groupe ransomware darkvault. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Healthcare services, une compromission de ce type exposerait généralement des informations relatives aux patients, au personnel ou à l'administration sanitaire, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par darkvault, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données patients et de réponse à incident adaptées au secteur de la santé en cas d'éléments de compromission avérés.

----------------------------

### 13 Août 2024

#### 🇿🇦 Afrique du Sud - Gpf.za
- **Groupe ransomware :** darkvault
- **Secteur :** Services financiers & Assurances
- **Site web :** [gpf.org.za](https://www.gpf.org.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Gpf.za figure sur le site de fuite du groupe darkvault. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Gpf.za est une entreprise commerciale majeure opérant dans le secteur des finance, contribuant de manière significative au tissu économique régional en South Africa.

- **Analyse :**
  AFRINTEL a recensé Gpf.za (Afrique du Sud) comme victime revendiquée par le groupe ransomware darkvault. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Services financiers & Assurances, une compromission de ce type exposerait généralement des données de comptes clients, de paiement ou financières, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par darkvault, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de paiement et de réponse à incident adaptées au secteur financier en cas d'éléments de compromission avérés.

----------------------------

### 17 Août 2024

#### 🇿🇦 Afrique du Sud - Wwwconfig
- **Groupe ransomware :** ransomhub
- **Secteur :** Télécommunications
- **Site web :** [netconfig.co.za](https://www.netconfig.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Wwwconfig figure sur le site de fuite du groupe ransomhub. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Wwwconfig est un opérateur de réseau mobile de premier plan fournissant des infrastructures de télécommunications, des services de téléphonie et des données haut débit.

- **Analyse :**
  AFRINTEL a recensé Wwwconfig (Afrique du Sud) comme victime revendiquée par le groupe ransomware ransomhub. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Télécommunications, une compromission de ce type exposerait généralement des données employés, clients ou opérationnelles, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par ransomhub, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données et de réponse à incident en cas d'éléments de compromission avérés.

----------------------------

### 19 Août 2024

#### 🇹🇳 Tunisie - Eventizer
- **Acteur / Groupe :** Bambi, publication sur un forum cybercriminel
- **Secteur :** Événementiel / Plateforme numérique / Services aux entreprises
- **Site web :** [eventizer.io](https://www.eventizer.io)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Fuite de données
- **Niveau de confiance :** Medium
- **Niveau d’impact :** Level 3
- **Description victime :** Eventizer est une agence événementielle tunisienne et une plateforme numérique centralisant les inscriptions, paiements, contrôles d’accès, hébergements et tableaux de bord liés aux événements.
- **Analyse :** La publication attribuée à Bambi annonce environ 60 000 enregistrements associés à Eventizer et présente un échantillon structuré avec des identifiants utilisateurs, noms, adresses électroniques, numéros de téléphone, pays et informations de rôle de connexion. Le titre de la publication revendique une couverture de la Tunisie et du Nigeria, tandis que l’échantillon visible contient des enregistrements associés à plusieurs pays. L’échantillon démontre l’exposition de données de contact et de contexte de comptes, mais le volume total, l’exhaustivité, la provenance et le rattachement technique direct à Eventizer n’ont pas été vérifiés indépendamment. Les champs exposés pourraient faciliter le phishing ciblé, l’usurpation, l’énumération de comptes et l’ingénierie sociale. Les enregistrements et coordonnées bruts ne sont pas reproduits.

----------------------------

### 21 Août 2024

#### 🇨🇮 Côte d'Ivoire - Codival
- **Groupe ransomware :** spacebears
- **Secteur :** Retail (distribution)
- **Site web :** [codival.ci](https://www.codival.ci)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Codival figure sur le site de fuite du groupe spacebears. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Codival est une entreprise commerciale majeure opérant dans le secteur des retail (distribution), contribuant de manière significative au tissu économique régional en Côte d'Ivoire.

- **Analyse :**
  AFRINTEL a recensé Codival (Côte d'Ivoire) comme victime revendiquée par le groupe ransomware spacebears. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Retail (distribution), une compromission de ce type exposerait généralement des données clients et de transaction, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par spacebears, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de réponse à incident adaptées au secteur du commerce en cas d'éléments de compromission avérés.

----------------------------

### 22 Août 2024

#### 🇿🇦 Afrique du Sud - Don’t waste group
- **Groupe ransomware :** incransom
- **Secteur :** Services
- **Site web :** [don’t waste group.com](https://www.don’t waste group.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Don’t waste group figure sur le site de fuite du groupe incransom. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Don’t waste group est une entreprise commerciale majeure opérant dans le secteur des services, contribuant de manière significative au tissu économique régional en South Africa.

- **Analyse :**
  AFRINTEL a recensé Don’t waste group (Afrique du Sud) comme victime revendiquée par le groupe ransomware incransom. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Services, une compromission de ce type exposerait généralement des données employés, clients ou opérationnelles, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par incransom, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données et de réponse à incident en cas d'éléments de compromission avérés.

----------------------------

### 22 Août 2024

#### 🇰🇪 Kenya - Instadriver.co
- **Groupe ransomware :** killsec
- **Secteur :** Retail (distribution)
- **Site web :** [instadriver.co](https://www.instadriver.co)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Instadriver.co figure sur le site de fuite du groupe killsec. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Instadriver.co est une entreprise commerciale majeure opérant dans le secteur des retail (distribution), contribuant de manière significative au tissu économique régional en Kenya.

- **Analyse :**
  AFRINTEL a recensé Instadriver.co (Kenya) comme victime revendiquée par le groupe ransomware killsec. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Retail (distribution), une compromission de ce type exposerait généralement des données clients et de transaction, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par killsec, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de réponse à incident adaptées au secteur du commerce en cas d'éléments de compromission avérés.

----------------------------

### 24 Août 2024

#### 🇸🇨 Seychelles - Ingotbrokers
- **Groupe ransomware :** darkvault
- **Secteur :** Financial organizations
- **Site web :** [ingotbrokers.com](https://www.ingotbrokers.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Ingotbrokers figure sur le site de fuite du groupe darkvault. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Ingotbrokers est une entreprise commerciale majeure opérant dans le secteur des financial organizations, contribuant de manière significative au tissu économique régional en Seychelles.

- **Analyse :**
  AFRINTEL a recensé Ingotbrokers (Seychelles) comme victime revendiquée par le groupe ransomware darkvault. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Financial organizations, une compromission de ce type exposerait généralement des données de comptes clients, de paiement ou financières, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par darkvault, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de paiement et de réponse à incident adaptées au secteur financier en cas d'éléments de compromission avérés.

----------------------------

### 26 Août 2024

#### 🇿🇦 Afrique du Sud - Onedayonly
- **Groupe ransomware :** killsec
- **Secteur :** Shops
- **Site web :** [onedayonly.co.za](https://www.onedayonly.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Onedayonly figure sur le site de fuite du groupe killsec. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Onedayonly est une entreprise commerciale majeure opérant dans le secteur des shops, contribuant de manière significative au tissu économique régional en South Africa.

- **Analyse :**
  AFRINTEL a recensé Onedayonly (Afrique du Sud) comme victime revendiquée par le groupe ransomware killsec. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Shops, une compromission de ce type exposerait généralement des données clients et de transaction, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par killsec, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de réponse à incident adaptées au secteur du commerce en cas d'éléments de compromission avérés.

----------------------------

### 28 Août 2024

#### 🇩🇯 Djibouti - Dpfza.gov.dj
- **Groupe ransomware :** ransomhub
- **Secteur :** Government and administrations
- **Site web :** [dpfza.gov.dj](https://www.dpfza.gov.dj)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Dpfza.gov.dj figure sur le site de fuite du groupe ransomhub. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Dpfza.gov.dj est une institution publique ou une autorité de régulation étatique essentielle, chargée des services administratifs et de la gestion publique.

- **Analyse :**
  AFRINTEL a recensé Dpfza.gov.dj (Djibouti) comme victime revendiquée par le groupe ransomware ransomhub. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Government and administrations, une compromission de ce type exposerait généralement des données citoyennes ou des informations administratives internes, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par ransomhub, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données citoyennes et de réponse à incident adaptées au secteur public en cas d'éléments de compromission avérés.

----------------------------

### 28 Août 2024

#### 🇿🇼 Zimbabwe - Success microfinance bank
- **Groupe ransomware :** meow
- **Secteur :** Banking institutions
- **Site web :** [success microfinance bank.com](https://www.success microfinance bank.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Success microfinance bank figure sur le site de fuite du groupe meow. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Success microfinance bank est une entreprise commerciale majeure opérant dans le secteur des banking institutions, contribuant de manière significative au tissu économique régional en Zimbabwe.

- **Analyse :**
  AFRINTEL a recensé Success microfinance bank (Zimbabwe) comme victime revendiquée par le groupe ransomware meow. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Banking institutions, une compromission de ce type exposerait généralement des données de comptes clients, de paiement ou financières, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par meow, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de paiement et de réponse à incident adaptées au secteur financier en cas d'éléments de compromission avérés.

----------------------------

### 28 Août 2024

#### 🇬🇭 Ghana - Ghanare
- **Groupe ransomware :** BrainCipher
- **Secteur :** Technologies
- **Site web :** [ghanare.com](https://www.ghanare.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type d'incident :** Ransomware

- **Note de fiabilité :**
  Ghanare figure sur le site de fuite du groupe BrainCipher. AFRINTEL n'a observé aucun échantillon, capture ou extrait de données accessible associé à cette publication au moment de la collecte, et la revendication n'a pas été confirmée de manière indépendante par l'organisation.

- **Description :**
  Ghanare est une entreprise commerciale majeure opérant dans le secteur des technologies, contribuant de manière significative au tissu économique régional en Ghana.

- **Analyse :**
  AFRINTEL a recensé Ghanare (Ghana) comme victime revendiquée par le groupe ransomware BrainCipher. Aucun fichier divulgué, extrait de base de données ou capture d'écran n'était accessible pour analyse, ce qui ne permet pas d'évaluer l'ampleur, le volume ni la sensibilité des données éventuellement exposées. Compte tenu de l'activité de l'organisation dans le secteur Technologies, une compromission de ce type exposerait généralement des données clients, partenaires ou techniques internes, avec des risques associés de phishing, de fraude ou de perturbation de l'activité. AFRINTEL ne confirme ni l'intrusion, ni l'exfiltration de données, ni l'existence d'un jeu de données complet sur la seule base de cette publication.

- **Recommandations :**
  1. Examiner la surface d'attaque externe, les services d'accès distant et l'intégrité des sauvegardes à la suite de cette publication par BrainCipher, et vérifier la disponibilité de sauvegardes hors ligne ou immuables.
  2. Surveiller toute publication ultérieure d'échantillons de données liés à cette revendication et préparer des procédures de protection des données clients et de réponse à incident adaptées au secteur technologique en cas d'éléments de compromission avérés.

----------------------------

## Septembre 2024

### 6 Septembre 2024

#### 🇸🇳 Sénégal - SESAM Informatics
- **Groupe ransomware :** hunters
- **Secteur :** Technologies / Développement logiciel
- **Site web :** [sesam-informatics.com](https://www.sesam-informatics.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** SESAM Informatics est une entreprise sénégalaise de technologies et de services logiciels opérant dans les solutions numériques et le développement informatique.

----------------------------

### 12 Septembre 2024

#### 🇨🇲 Cameroun - CNPS Cameroun
- **Groupe ransomware :** spacebears
- **Secteur :** Gouvernement / Sécurité sociale
- **Site web :** [cnps.cm](https://www.cnps.cm)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** La Caisse Nationale de Prévoyance Sociale (CNPS) du Cameroun est l'organisme public chargé de la gestion de la sécurité sociale et des prestations sociales des travailleurs.

----------------------------

### 15 Septembre 2024

#### 🇲🇺 Maurice - Emtel
- **Groupe ransomware :** arcusmedia
- **Secteur :** Télécommunications
- **Site web :** [emtel.com](https://www.emtel.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Emtel est un opérateur mobile mauricien fournissant des infrastructures de télécommunications, services voix, données et haut débit.

----------------------------

### 16 Septembre 2024

#### 🇹🇳 Tunisie - Excelplast Tunisie
- **Groupe ransomware :** orca
- **Secteur :** Industrie manufacturière / Plasturgie
- **Site web :** [excelplastunisie.com](https://www.excelplastunisie.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Excelplast Tunisie est une entreprise manufacturière tunisienne spécialisée dans la production de plastique, la transformation des matières premières et l'emballage.

----------------------------

### 7 Septembre 2024
#### 🇳🇬 Nigeria - Nigerian Navy (navy.mil.ng)
- **Acteur / Groupe :** NizaarFarah (compte source)
- **Secteur :** Défense / Sécurité Nationale
- **Site web :** https://navy.mil.ng
- **Date de publication de la source :** 7 septembre 2024
- **Date de fuite revendiquée :** 8 novembre 2020
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4
- **Type d'incident :** Fuite de données
- **Description victime :** La Nigerian Navy est la branche navale des forces armées nigérianes. La capture fournie revendique des centaines de fichiers confidentiels et 1 200 identifiants e-mail, avec environ 300 fichiers et une archive annoncée à 228,4 Mo. Elle montre des échantillons de documents et d'équipements, mais AFRINTEL n'a pas collecté ni reproduit les fichiers ou identifiants sous-jacents. NizaarFarah est enregistré comme le compte source affiché dans la publication ; cela ne confirme pas indépendamment la compromission ni l'identité du compte au-delà de la publication observée.

----------------------------

## Octobre 2024

### 3 Octobre 2024

#### 🇲🇬 Madagascar - Université d'Antananarivo (univ-antananarivo.mg)
- **Type d'incident :** Fuite de données
- **Acteur / Groupe :** RainbowBF
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [univ-antananarivo.mg](https://www.univ-antananarivo.mg)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** L'Université d'Antananarivo est la plus ancienne et la plus grande université publique de Madagascar, regroupant plusieurs facultés et instituts d'enseignement supérieur dans la région de la capitale.
- **Analyse :** AFRINTEL a examiné une publication sur la plateforme Breached, postée par le compte RainbowBF le 3 octobre 2024, intitulée « Madagascar univ-antananarivo.mg Database Access » et classée sous la catégorie de contenu « Breached » de la plateforme. Le contenu sous-jacent est verrouillé derrière le système de crédits internes du forum et n'a pas été débloqué par AFRINTEL ; aucun export de base de données, capture d'écran d'enregistrements ni autre échantillon vérifiable n'était accessible lors de la collecte. AFRINTEL traite ceci comme une revendication non confirmée d'accès à une base de données et ne confirme ni l'existence, ni le périmètre, ni l'authenticité d'une quelconque donnée sous-jacente. Compte tenu du statut de l'université en tant que principale institution publique d'enseignement supérieur de Madagascar, une compromission réelle représenterait un risque matériel d'exposition de données personnelles d'étudiants et de personnel ; ce risque ne peut actuellement être évalué en raison de l'absence de preuve accessible. AFRINTEL ne reproduit aucun contenu de la publication au-delà de son titre et de ses métadonnées.

----------------------------

### 4 Octobre 2024

#### 🇿🇦 Afrique du Sud - Enterpriseoutsourcing
- **Groupe ransomware :** ransomhub
- **Secteur :** Conseil en technologies de l'information
- **Site web :** [enterpriseoutsourcing.com](https://www.enterpriseoutsourcing.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Enterpriseoutsourcing est une organisation sud-africaine opérant dans le secteur du conseil en technologies de l'information.

----------------------------

### 5 Octobre 2024

#### 🇿🇦 Afrique du Sud - Winwinza
- **Groupe ransomware :** ransomhub
- **Secteur :** Éducation / Écoles
- **Site web :** [winwinza.com](https://www.winwinza.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Winwinza est une organisation sud-africaine opérant dans le secteur de l'éducation.

----------------------------

### 7 Octobre 2024

#### 🇩🇿 Algérie - Yassir
- **Groupe ransomware :** killsec
- **Secteur :** Technologies / Mobilité et livraison
- **Site web :** [yassir.com](https://www.yassir.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Yassir est une super-app algérienne fournissant des services de VTC, livraison, courses et services numériques en Algérie et sur des marchés régionaux.

----------------------------

### 9 Octobre 2024

#### 🇳🇬 Nigeria - Prestataire non identifié d’établissements de santé
- **Acteur / Groupe :** Tanaka
- **Secteur :** Santé / Services médicaux
- **Site web :** Non identifié
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Description victime :** La source décrit un prestataire nigérian non identifié opérant plusieurs établissements de santé. Le nom de l’organisation et les établissements concernés n’ont pas pu être établis à partir des éléments disponibles.
- **Analyse :** Une publication du forum attribuée à Tanaka et datée du 9 octobre 2024 affirme qu’environ 130 000 dossiers de patients provenant de plusieurs établissements de santé nigérians ont été divulgués par l’acteur grep/cn. Le classeur local fourni pour analyse contient 84 lignes de données, et non 129 825 ou 130 000 lignes ; le volume annoncé ne peut donc pas être confirmé indépendamment à partir du fichier disponible. Le classeur contient des champs relatifs à des patients, notamment des noms, identifiants, numéros de téléphone, âge, dates de naissance, sexe, statut matrimonial et identifiants liés aux établissements ; les enregistrements bruts n’ont pas été reproduits. Les éléments soutiennent une revendication d’exposition de données de santé à fort impact potentiel, mais le prestataire exact, le périmètre des établissements, le mode d’obtention, l’exhaustivité et le volume total restent inconnus.

### 9 Octobre 2024

#### 🇿🇦 Afrique du Sud - GMG Mining Supplies
- **Groupe ransomware :** sarcoma
- **Secteur :** Industrie minière / Équipements industriels
- **Site web :** [gmgminingsupplies.com](https://www.gmgminingsupplies.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** GMG Mining Machines and Supplies est une entreprise sud-africaine spécialisée dans la fourniture, reconstruction et location d'équipements miniers, machines mobiles sans rail, pièces et services associés.

----------------------------

### 9 Octobre 2024

#### 🇿🇦 Afrique du Sud - National Edging
- **Groupe ransomware :** sarcoma
- **Secteur :** Industrie / Fournitures industrielles
- **Site web :** [nationaledging.com](https://www.nationaledging.com)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 3
- **Description victime :** National Edging est une entreprise sud-africaine spécialisée dans la fourniture de chants, adhésifs, matériaux de finition et composants industriels pour les secteurs du meuble, de la cuisine et de l'agencement.
- **Analyse :** AFRINTEL a examiné un échantillon local de documents cohérents avec la revendication du cybercriminel sarcoma, comprenant des scans complets de passeports d'au moins trois personnes (deux ressortissants sud-africains et un ressortissant indien titulaire d'un permis de résidence aux Émirats arabes unis), un contrat signé avec Freitan Group of Companies (Pty) Ltd portant la signature d'un directeur financier, un formulaire de réservation de voyage d'entreprise référençant l'entité juridique National Converting Agencies (Pty) Ltd, une adresse email au domaine nationaledging.co.za ainsi qu'un passeport et un numéro d'identité sud-africains, et un bon de livraison documentant un envoi de produits de chant et de colle entre succursales de l'entreprise (Gauteng) avec une collecte ultérieure référencée au Zimbabwe. La référence directe au domaine nationaledging.co.za, associée à une identité d'entreprise cohérente (National Converting Agencies/National Edging), à du matériel contractuel signé et à plusieurs documents d'identité complets, soutient une évaluation à très haute confiance d'une compromission interne réelle. L'exposition de données complètes de passeport et d'identité nationale pour plusieurs personnes, ainsi que de contrats signés et de dossiers logistiques s'étendant à une chaîne d'approvisionnement transfrontalière (Zimbabwe), crée un risque important de fraude à l'identité, de falsification de documents et d'ingénierie sociale ciblée contre les employés, partenaires commerciaux et voyageurs associés à l'entreprise. AFRINTEL ne reproduit aucun nom, numéro de passeport, numéro d'identité, date de naissance ni coordonnée issus de l'échantillon examiné.

----------------------------

### 11 Octobre 2024

#### 🇬🇭 Ghana - Volta River Authority (VRA)
- **Groupe ransomware :** blacksuit
- **Secteur :** Énergie / Production électrique
- **Site web :** [vra.com](https://www.vra.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** La Volta River Authority (VRA) est le principal producteur public d'électricité du Ghana, responsable de centrales hydroélectriques, thermiques et d'infrastructures énergétiques stratégiques du pays.

----------------------------

### 16 Octobre 2024

#### 🇱🇾 Libye - Ministère de l'Intérieur (moi.gov.ly)
- **Groupe ransomware :** killsec
- **Secteur :** Gouvernement / Ministère de l'Intérieur
- **Site web :** [moi.gov.ly](https://www.moi.gov.ly)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Le Ministère de l'Intérieur libyen est l'institution gouvernementale chargée de la sécurité intérieure, des forces de police et de la gestion des affaires administratives sécuritaires du pays.

----------------------------

### 17 Octobre 2024

#### 🇩🇿 Algérie - Ministère de l'Éducation Nationale (education.gov.dz)
- **Acteur / Groupe :** Moroccan Empire ; republié par AmeliaBeaumont sur un forum cybercriminel
- **Secteur :** Gouvernement / Éducation nationale
- **Site web :** [education.gov.dz](https://www.education.gov.dz)
- **Date de la fuite initiale revendiquée :** 06 octobre 2022
- **Date de publication du post examiné :** 17 octobre 2024 (le post inclut directement le lien vers le dump d'origine, initialement partagé le 18 septembre 2023)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Description victime :** Le Ministère de l'Éducation Nationale est l'administration algérienne chargée du système éducatif public. La publication revendique le vol d'une base de données contenant les informations d'environ 90 000 élèves, incluant des comptes administrateurs et des identifiants de connexion.
- **Analyse :** Le compte AmeliaBeaumont a publié le 17 octobre 2024 une revendication décrivant une intrusion attribuée à l'acteur « Moroccan Empire » et datée du 6 octobre 2022. Le lien de téléchargement d'origine (une adresse .onion sur un forum de fuite) n'étant plus fonctionnel, le post inclut directement un lien vers le dump, initialement partagé le 18 septembre 2023, qui affiche un échantillon SQL/CSV avec un schéma de champs incluant notamment : numéro d'acte de naissance, type de contrat, établissement, commune, nom, prénom (en français et en arabe), date de naissance, lieu de naissance, numéro d'assurance, numéro de téléphone, diplôme, spécialité, identifiants de compte (`compte`, `cle`), adresse email et un champ de mot de passe en clair. Au moins deux enregistrements complets sont visibles dans l'échantillon, comportant des noms, dates de naissance, numéros de téléphone, une adresse email et un mot de passe en texte brut associés à des personnes identifiées.

  La présence d'un schéma cohérent avec un système de gestion scolaire administratif, incluant des données d'identité, de scolarité et des identifiants de connexion en clair, soutient un niveau de confiance élevé quant à l'authenticité d'un accès à une base de données du ministère ou d'un établissement qui lui est rattaché. Le volume total de 90 000 élèves revendiqué n'a pas pu être vérifié indépendamment au-delà de l'échantillon observé. Le fait que le même dump reste partagé et référencé plus de deux ans après la fuite initialement revendiquée indique une recirculation prolongée de ce jeu de données. L'exposition de mots de passe en clair, combinée aux données d'identité et de scolarité, présente un risque élevé de prise de contrôle de comptes, d'usurpation d'identité et de phishing ciblé contre les élèves, leurs familles et le personnel administratif. AFRINTEL ne reproduit aucun nom, date de naissance, numéro de téléphone, adresse email, mot de passe ni autre donnée personnelle issus de l'échantillon examiné.

----------------------------

### 21 Octobre 2024

#### 🇲🇦 Maroc - Résidences universitaires Al Massira
- **Acteur / Groupe :** bxxxx1
- **Secteur :** Éducation / Hébergement étudiant
- **Site web :** [ruam.ma](https://ruam.ma)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données

- **Description :**
  Les Résidences universitaires Al Massira proposent des logements destinés aux étudiants à Kénitra. Le réseau comprend notamment les résidences Al Massira 1, Al Massira 2 et Al Massira 3, situées à proximité des établissements universitaires de la ville.

- **Analyse :**
  Une publication attribuée à bxxxx1 sur un forum cybercriminel présente des adresses électroniques associées à des personnes ayant recherché ou demandé un hébergement auprès des Résidences universitaires Al Massira. L’acteur affirme avoir obtenu les données après s’être connecté au panneau de contrôle de `ruam.ma`, ce qui suggère la compromission possible d’un compte d’administration ou d’une interface de gestion ; la capture ne contient toutefois aucune preuve technique permettant d’identifier la méthode d’accès. L’échantillon visible contient uniquement des adresses électroniques, principalement issues de services de messagerie publics, avec quelques domaines universitaires, administratifs ou professionnels. Aucun mot de passe, numéro d’identité, numéro de téléphone, document étudiant ou renseignement financier n’est visible. La publication indique une extraction en octobre 2024 et comporte un lien vers un fichier texte ainsi qu’un mot de passe d’archive ou d’accès, qu’AFRINTEL ne reproduit pas. Aucun nombre total d’adresses, volume de fichier, prix ou délai n’est indiqué, et la capture ne permet pas d’établir si la liste visible est complète. Les adresses peuvent alimenter des campagnes de phishing imitant les services de logement étudiant, de fausses notifications d’admission ou de paiement et des listes de cibles pour le password spraying. Aucun mot de passe n’étant visible, une prise de contrôle directe de compte ne peut pas être déduite de l’échantillon.

----------------------------

### 25 Octobre 2024

#### 🇪🇬 Égypte - Matouk Bassiouny
- **Groupe ransomware :** raworld
- **Secteur :** Services juridiques / Cabinet d'avocats
- **Site web :** [matoukbassiouny.com](https://www.matoukbassiouny.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Matouk Bassiouny est un important cabinet d'avocats égyptien basé au Caire, reconnu pour le droit des affaires, l'arbitrage, le contentieux et le conseil juridique.

----------------------------

## Novembre 2024

### 2 Novembre 2024

#### 🇿🇦 Afrique du Sud - Sumitomo Rubber South Africa
- **Groupe ransomware :** killsec
- **Secteur :** Industrie manufacturière / Pneumatiques
- **Site web :** [srigroup.co.za](https://www.srigroup.co.za)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description victime :** Sumitomo Rubber South Africa est une entreprise de fabrication de pneumatiques opérant en Afrique du Sud et liée au groupe Sumitomo Rubber Industries.
- **Analyse :** AFRINTEL a examiné un échantillon local de l'archive associée à cette revendication, comprenant environ 239 600 fichiers PDF individuels (soit environ 23 Go non compressés), chacun nommé par un UUID aléatoire plutôt que par un nom de fichier d'origine. Les fichiers examinés par AFRINTEL sont des relevés de compte clients authentiques émis à en-tête de Sumitomo Rubber South Africa (Pty) Ltd, spécifiquement sa division « Export DQC - Africa East (USD) », listant l'historique des transactions par compte (références de facture SAP, dates, montants crédités et soldes courants) rattaché à un numéro de compte nommé et à un contact commercial export nommé, avec une adresse email au domaine srigroup.co.za. La cohérence de l'en-tête d'entreprise, des noms de contacts réels et de la numérotation des factures liée à SAP dans l'échantillon examiné, ainsi que le volume très important et le schéma de nommage par UUID cohérent avec un export en masse depuis une archive de gestion documentaire ou un ERP, soutiennent une évaluation à très haute confiance d'une compromission réelle et à grande échelle. Compte tenu de l'ampleur de l'archive et de sa couverture des comptes clients export de l'entreprise à l'échelle du continent, cet incident présente un risque de fraude à la facture à grande échelle, de compromission de messagerie professionnelle et d'exposition de renseignement concurrentiel s'étendant à la clientèle export de Sumitomo Rubber South Africa sur le continent. AFRINTEL ne reproduit aucun numéro de compte, nom de contact, adresse email, référence de facture ni montant financier issu du matériel examiné.

----------------------------

### 4 Novembre 2024

#### 🇹🇿 Tanzanie - College of Business Education (CBE)
- **Groupe ransomware :** hellcat
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [cbe.ac.tz](https://www.cbe.ac.tz)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Le College of Business Education (CBE) est un établissement tanzanien d'enseignement supérieur proposant des formations en commerce, gestion, comptabilité et domaines professionnels associés.

----------------------------

### 4 Novembre 2024

#### 🇸🇩 Soudan - Kenana Sugar Company
- **Groupe ransomware :** ransomhub
- **Secteur :** Agriculture / Industrie sucrière
- **Site web :** [kenanasugarcompany.com](https://www.kenanasugarcompany.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Kenana Sugar Company est un important complexe agro-industriel soudanais spécialisé dans la culture de la canne à sucre, la production de sucre et les activités agricoles et industrielles associées.

----------------------------

### 12 Novembre 2024

#### 🇲🇦 Maroc - Arab Civil Aviation Organization (ACAO)
- **Acteur / Groupe :** Non attribué ; republié par Hxp7
- **Secteur :** Aviation / Organisation intergouvernementale
- **Site web :** [acao.org.ma](https://acao.org.ma)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Type d'incident :** Data Leak
- **Description victime :** L'Arab Civil Aviation Organization (ACAO) est une organisation intergouvernementale basée à Rabat, au Maroc, chargée de coordonner les politiques de sécurité et de régulation de l'aviation civile entre les États arabes.
- **Analyse :** Une publication de forum datée du 12 novembre 2024 republie une revendication antérieure selon laquelle la base de données de l'ACAO (acao.org.ma) aurait été compromise, mentionnant environ 800 fichiers décrits comme des colonnes de base de données et un lien de téléchargement externe. Aucun extrait ni échantillon de données n'était directement visible dans la publication observée, ce qui empêche d'évaluer le contenu, l'authenticité et l'étendue de la base de données revendiquée. AFRINTEL n'accède pas au lien fourni et ne le reproduit pas. Cette entrée est enregistrée comme une revendication non vérifiée, dans l'attente d'une confirmation indépendante.

----------------------------

### 14 Novembre 2024

#### 🇳🇬 Nigeria - Environmental Design International
- **Groupe ransomware :** akira
- **Secteur :** Ingénierie / Conseil
- **Site web :** [environmentaldesigninternational.com](http://environmentaldesigninternational.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Environmental Design International est une entreprise nigériane d'ingénierie et de conseil ; la revendication mentionnait des documents d'ingénierie, financiers et personnels.

----------------------------

### 17 Novembre 2024

#### 🇪🇬 Égypte - Egyptian Tax Authority (ETA)
- **Groupe ransomware :** moneymessage
- **Secteur :** Gouvernement / Administration fiscale
- **Site web :** [eta.gov.eg](https://www.eta.gov.eg)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** L'Egyptian Tax Authority (ETA) est l'administration fiscale publique égyptienne chargée de la collecte des impôts, de la conformité, des services aux contribuables et de la gestion fiscale.

----------------------------

### 24 Novembre 2024

#### 🇰🇪 Kenya - EFI Sales
- **Groupe ransomware :** killsec
- **Secteur :** Distribution / Équipements industriels
- **Site web :** [efisales.co.ke](https://www.efisales.co.ke)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** EFI Sales est une entreprise basée au Kenya dans le secteur de la distribution, associée à la fourniture d'équipements industriels et services connexes.

----------------------------

### 27 Novembre 2024

#### 🇪🇹 Éthiopie - Habesha Cement
- **Groupe ransomware :** lockbit3
- **Secteur :** Industrie lourde / Matériaux de construction
- **Site web :** [habeshacement.com](https://www.habeshacement.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Habesha Cement est une cimenterie éthiopienne fondée en 2008, spécialisée dans la production de ciment et de matériaux de construction pour les infrastructures et le secteur immobilier.

----------------------------

### 27 Novembre 2024

#### 🇪🇬 Égypte - Contrack Facilities Management
- **Groupe ransomware :** raworld
- **Secteur :** Services aux entreprises / Facility management
- **Site web :** [contrackfm.com](https://www.contrackfm.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Contrack Facilities Management est une société égyptienne de facility management fournissant des services de maintenance, d'exploitation et de support pour les bâtiments et sites d'entreprise.

----------------------------

### 28 Novembre 2024

#### 🇧🇫 Burkina Faso - Portail du système de santé publique du Burkina Faso
- **Acteur / Groupe :** Sentap
- **Secteur :** Santé / Santé publique
- **Site web :** Non précisé
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d’impact :** Level 3
- **Type d’incident :** Vente d’accès
- **Description :** Une publication décrit un portail public burkinabè qui pourrait gérer les informations du personnel de santé, le suivi des services sanitaires, les campagnes de vaccination, la planification des ressources et les communications internes.
- **Analyse :** La publication présente des fonctions potentielles et des catégories de données, mais ne fournit ni domaine vérifiable, ni preuve technique d’accès, ni échantillon. AFRINTEL l’enregistre comme une revendication non vérifiée de vente d’accès attribuée à Sentap. Un lien possible avec le système COVID-19 publié plus tard reste non démontré.

----------------------------

### 28 Novembre 2024

#### 🇧🇫 Burkina Faso - Système gouvernemental de gestion des données COVID-19
- **Acteur / Groupe :** Sentap
- **Secteur :** Santé / Santé publique
- **Site web :** Non précisé
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d’impact :** Level 3
- **Type d’incident :** Vente d’accès
- **Description :** Une publication présente un tableau de bord gouvernemental burkinabè de gestion des données COVID-19 couvrant les résultats PCR/TDR, les vaccinations et les historiques.
- **Analyse :** Les captures montrent des indicateurs, des synthèses de vaccination et une interface historique, avec un total revendiqué d’environ 3,795 millions d’enregistrements. Le domaine, la provenance, l’exhaustivité et l’authenticité ne sont pas vérifiés indépendamment. AFRINTEL ne reproduit aucun enregistrement personnel. Cette revendication reste séparée du portail de santé publique.

----------------------------

### 28 Novembre 2024

#### 🇳🇬 Nigeria - Briatek
- **Groupe ransomware :** killsec
- **Secteur :** Conseil IT / Intégration logicielle
- **Site web :** [briatek.com.ng](https://www.briatek.com.ng)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Briatek est une entreprise technologique nigériane spécialisée dans le conseil informatique, l'intégration logicielle et les solutions numériques pour les organisations.

----------------------------

### 28 Novembre 2024

#### 🇨🇲 Cameroun - Chanas Assurances S.A.
- **Groupe ransomware :** fog
- **Secteur :** Services d'assurance
- **Site web :** [chanasassurances.com](https://www.chanasassurances.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Chanas Assurances S.A. est une société camerounaise d'assurance opérant dans le secteur des services d'assurance.

----------------------------

### 29 Novembre 2024

#### 🇳🇦 Namibie - Namforce Life Insurance
- **Groupe ransomware :** spacebears
- **Secteur :** Assurance-vie / Services financiers
- **Site web :** [namforce.com.na](https://www.namforce.com.na)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Namforce Life Insurance est une société namibienne spécialisée dans les produits d'assurance-vie, de protection financière et de gestion des risques pour les particuliers et les organisations.

----------------------------

### 29 Novembre 2024

#### 🇿🇦 Afrique du Sud - PPOTTS
- **Groupe ransomware :** ransomhub
- **Secteur :** Technologies / Services numériques
- **Site web :** [ppotts.com](https://www.ppotts.com)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Analyse :** AFRINTEL a examiné huit captures d’écran issues de l’ensemble de preuves de RansomHub. Les éléments visibles comprennent un certificat du Uganda National Examinations Board, des résultats de laboratoire de pathologie sud-africains et des formulaires de divulgation de données d’identification contenant des informations sur des candidats et des entreprises. Le caractère sensible des documents est établi, mais les captures ne permettent pas de déterminer s’ils proviennent directement de PPOTTS, d’un environnement client, d’un système tiers ou d’un jeu de données plus large. Les éléments justifient l’enregistrement d’un échantillon publié, tout en maintenant l’attribution et la provenance des données sous analyse. AFRINTEL ne reproduit aucun nom, numéro d’identité, résultat médical ni coordonnée.
- **Description victime :** PPOTTS est une entreprise technologique sud-africaine opérant dans les logiciels, services numériques ou solutions technologiques d'entreprise.

----------------------------

## Décembre 2024

### 3 Décembre 2024

#### 🇸🇩 Soudan - DAL Group
- **Groupe ransomware :** ransomhub
- **Secteur :** Agroalimentaire / Boissons
- **Site web :** [dalgroup.com](https://www.dalgroup.com)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4
- **Type d'incident :** Fuite de données
- **Analyse :** AFRINTEL a examiné douze captures d’écran issues de l’ensemble de preuves de RansomHub. Le matériel comprend des clauses financières, des éléments de comptes bancaires et de transactions, des documents liés à des passeports, des dossiers de comptes clients et des documents internes de DAL Group. Les éléments visibles suggèrent une exposition touchant les opérations financières, les documents d’identité et l’administration de l’entreprise, plutôt qu’un fichier isolé. Les impacts possibles comprennent la fraude financière, l’usurpation d’identité, le phishing ciblé, l’imitation de fournisseurs ou de clients et l’espionnage commercial visant un grand conglomérat soudanais. Les captures ne permettent pas de confirmer le vecteur d’accès initial, l’exhaustivité du jeu de données, le nombre exact de personnes concernées ni une interruption opérationnelle. AFRINTEL ne reproduit aucune donnée personnelle, coordonnée bancaire, détail de passeport ni lien de téléchargement.
- **Description victime :** DAL Group est le plus grand conglomérat privé du Soudan, opérant dans les secteurs agroalimentaire, industriel, agricole, de la distribution et des boissons.

----------------------------

### 9 Décembre 2024

#### 🇲🇷 Mauritanie - Bankily
- **Groupe ransomware :** apt73/bashe
- **Secteur :** Mobile banking / Services financiers
- **Site web :** [bankily.mr](https://www.bankily.mr)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Bankily est une plateforme de mobile banking mauritanienne exploitée par la Banque Populaire de Mauritanie (BPM), fournissant des services financiers numériques et de paiement mobile.

----------------------------

### 10 Décembre 2024

#### 🇳🇦 Namibie - Telecom Namibia
- **Groupe ransomware :** hunters
- **Secteur :** Télécommunications
- **Site web :** [telecom.na](https://www.telecom.na)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Telecom Namibia est l'opérateur national historique de télécommunications fournissant des services de voix, de haut débit, de connectivité de données et d'infrastructure en Namibie.

----------------------------

### 13 Décembre 2024

#### 🇪🇬 Égypte - Kazyon
- **Groupe ransomware :** moneymessage
- **Secteur :** Grande distribution / Hard-discount
- **Site web :** [kazyon.com](https://www.kazyon.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Kazyon est une grande chaîne égyptienne de supermarchés hard-discount proposant des produits alimentaires, ménagers et de consommation via un large réseau de magasins.

----------------------------

### 15 Décembre 2024

#### 🇿🇲 Zambie - Tumeny Payments Limited
- **Groupe ransomware :** killsec
- **Secteur :** Fintech / Infrastructures de paiement
- **Site web :** [tumenypay.com](https://www.tumenypay.com)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Tumeny Payments Limited est une fintech zambienne fournissant des services de paiement numérique, transfert d'argent et infrastructures de paiement.

----------------------------

### 16 Décembre 2024

#### 🇳🇬 Nigeria - Gouvernement de l'État d'Ekiti
- **Groupe ransomware :** funksec
- **Secteur :** Administrations publiques / Gouvernement d'État
- **Site web :** [ekitistate.gov.ng](https://ekitistate.gov.ng)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description victime :** Le gouvernement de l'État d'Ekiti est l'administration exécutive de cet État du sud-ouest du Nigeria. Son portail officiel héberge des informations sur les ministères, agences et services publics, y compris des contenus liés au recrutement, à destination des résidents et des agents de l'État.
- **Analyse :** AFRINTEL a examiné une archive locale cohérente avec la revendication du cybercriminel funksec, comprenant un avis de fuite référençant ekitistate.gov.ng et décrivant une base de données de plus de 300 Mo, ainsi qu'une bibliothèque documentaire du site de plus de 17 000 fichiers image individuels (environ 530 Mo) collectée depuis le dépôt de fichiers du portail. L'échantillon examiné inclut des documents d'identification personnelle (scans de type passeport), des curriculum vitae comportant des champs de données personnelles tels que date de naissance, adresse, numéro de téléphone, email et religion, ainsi qu'un tableau de présélection de candidats de la Police Service Commission listant des candidats retenus par nom, zone d'administration locale, village et sexe pour une campagne de recrutement de 2019. Le volume et la structure du matériel examiné, des schémas de nommage de fichiers systématiquement rattachés à des personnes nommées, et la présence d'un modèle de document officiel du gouvernement d'État, soutiennent une évaluation à très haute confiance d'une exposition de données réelle plutôt qu'une simple revendication. Compte tenu du rôle de l'État d'Ekiti en tant qu'administration publique infranationale et de la présence de documents d'identité de citoyens et d'agents publics, cet incident présente un risque significatif d'usurpation d'identité, de phishing ciblé et d'imposture. AFRINTEL ne reproduit aucun nom, numéro de passeport, coordonnée ni autre identifiant personnel issu du matériel examiné.

----------------------------

### 20 Décembre 2024

#### 🇧🇼 Botswana - Water Utilities Corporation (WUC)
- **Groupe ransomware :** killsec
- **Secteur :** Distribution d'eau / Service public
- **Site web :** [wuc.bw](https://www.wuc.bw)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Water Utilities Corporation (WUC) est l'entreprise publique botswanaise chargée de l'approvisionnement, de la distribution et de la gestion des services d'eau.

----------------------------

### 21 Décembre 2024

#### 🇹🇳 Tunisie - Groupe SETCAR
- **Groupe ransomware :** ransomhub
- **Secteur :** Automobile / Véhicules industriels
- **Site web :** [groupe-setcar.com.tn](https://www.groupe-setcar.com.tn)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** Le Groupe SETCAR est un groupe industriel tunisien spécialisé dans les bus, autocars, véhicules industriels, activités automobiles et solutions de transport associées.

----------------------------

### 24 Décembre 2024

#### 🇿🇦 Afrique du Sud - Baker Tilly Morrison Murray
- **Groupe ransomware :** sarcoma
- **Secteur :** Audit / Comptabilité / Conseil
- **Site web :** [bakertillymm.co.za](https://www.bakertillymm.co.za)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** Baker Tilly Morrison Murray est un cabinet sud-africain de services professionnels fournissant des services de comptabilité, audit, fiscalité et conseil.
- **Analyse :** AFRINTEL a examiné des captures conservées dans le répertoire de preuves `bakertillymm.co.za` et y a observé des documents d’identité sud-africains, dont un passeport, ainsi que des documents contractuels et liés à l’emploi. L’échantillon est cohérent avec le type de dossiers sensibles susceptibles d’être traités par un cabinet de comptabilité et de conseil, mais il ne permet pas d’établir l’étendue totale de la divulgation alléguée ni le nombre complet de personnes concernées. L’association de documents d’identité et de pièces contractuelles crée un risque de fraude à l’identité, d’ingénierie sociale ciblée, d’usurpation d’employés et de fraude secondaire visant des clients ou des partenaires. Le matériel examiné justifie une évaluation à confiance moyenne selon laquelle un échantillon de données a été publié dans le cadre de la revendication de Sarcoma ; AFRINTEL ne reproduit aucun nom, numéro de document, date de naissance, adresse ni autre donnée personnelle issue des captures.

----------------------------

### 24 Décembre 2024

#### 🇩🇿 Algérie - ASJP (Algerian Scientific Journal Platform)
- **Groupe ransomware :** funksec
- **Secteur :** Éducation / Recherche Scientifique / Publication Académique
- **Site web :** [asjp.cerist.dz](https://asjp.cerist.dz)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description victime :** L'ASJP (Algerian Scientific Journal Platform) est une plateforme nationale de publication électronique développée et exploitée par le CERIST (Centre de Recherche sur l'Information Scientifique et Technique), un organisme de recherche public algérien. Elle indexe et héberge le texte intégral de plus de 700 revues scientifiques algériennes couvrant toutes les disciplines académiques.
- **Analyse :** AFRINTEL a examiné une archive locale cohérente avec la revendication du cybercriminel funksec, comprenant une sauvegarde du système de fichiers côté serveur (archive tar, propriété des fichiers attribuée au compte du serveur web www-data) de l'arborescence des avatars utilisateurs de la plateforme, contenant plus de 1 700 dossiers utilisateurs individuels avec des photos de profil liées aux comptes, datées entre 2017 et 2024, ainsi qu'une liste structurée distincte de 499 enregistrements nom/email. Les dossiers utilisateurs sont majoritairement rattachés à des domaines email d'universités algériennes (dont univ-biskra.dz, univ-tlemcen.dz, univ-batna.dz, univ-tiaret.dz, univ-guelma.dz, univ-alger2.dz, univ-alger3.dz, univ-constantine2.dz, univ-constantine3.dz, univ-msila.dz, univ-mosta.dz, lagh-univ.dz et edu.univ-oran1.dz, entre autres), cohérent avec le rôle de l'ASJP en tant que plateforme nationale algérienne de publication de revues académiques, aux côtés d'une part plus réduite de contributeurs académiques internationaux soumettant à des revues hébergées en Algérie. La présence d'une sauvegarde côté serveur authentique, avec une propriété de fichiers du serveur web et des horodatages cohérents sur plusieurs années, corroborée par un export nom/email distinct, soutient une évaluation à très haute confiance d'une compromission réelle au niveau du système de fichiers plutôt qu'une simple revendication. Compte tenu du rôle de l'ASJP en tant qu'infrastructure nationale de publication scientifique exploitée par un organisme d'État (CERIST), de l'ampleur de la base d'utilisateurs exposée et de la nature de l'accès au niveau du système de fichiers, cet incident présente un risque systémique pour l'écosystème algérien de publication académique, incluant du phishing à grande échelle, la prise de contrôle de comptes et l'usurpation d'identité de chercheurs et de personnel de revues. AFRINTEL ne reproduit aucun nom, adresse email ni identifiant de compte utilisateur issu du matériel examiné.

----------------------------

### 28 Décembre 2024

#### 🇿🇦 Afrique du Sud - Cell C
- **Groupe ransomware :** ransomhouse
- **Secteur :** Télécommunications
- **Site web :** [cellc.co.za](https://www.cellc.co.za)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** Cell C est un opérateur mobile sud-africain fournissant des services de voix, données, messagerie et télécommunications mobiles.

----------------------------

### 29 Décembre 2024

#### 🇹🇿 Tanzanie - WOSAC
- **Groupe ransomware :** arcusmedia
- **Secteur :** Transport maritime / Agence maritime
- **Site web :** [wosac.co.tz](https://www.wosac.co.tz)
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Description victime :** WOSAC est une entreprise tanzanienne de transport maritime et d'agence maritime fournissant des services de fret, shipping et logistique associée.

----------------------------

---

*Compilation AFRINTEL - source unique : fichiers mensuels.*
