[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Cyberattaques en Afrique: Janvier 2024 : liste des 12 victimes

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

## ✍🏿 Author
*Adama ASSIONGBON*
*Consultant SOC & Cyber Threat Intelligence*
[LinkedIn profile](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)
