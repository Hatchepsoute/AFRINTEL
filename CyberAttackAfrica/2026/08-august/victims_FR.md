![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en août 2026 (9 victimes)

👉🏾 [**English version available here**](./victims.md)

## Août 2026

### 01 août 2026
#### 🇿🇦 Afrique du Sud - South African Reserve Bank (SARB)

- **Date de publication initiale :** 01 août 2026
- **Date de détection AFRINTEL :** 15 août 2026
- **Acteur / Groupe :** NullSec Nigeria (alias « voss », compte de forum NullsecNg), publication sur le forum cybercriminel DarkForums
- **Secteur :** Gouvernement / Banque centrale / Services financiers
- **Site web :** Non précisé
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 4

- **Description :**

  La South African Reserve Bank (SARB) est la banque centrale d'Afrique du Sud, responsable de la politique monétaire, de l'émission de la monnaie et de la stabilité du système financier national.

- **Analyse :**

  AFRINTEL a examiné une publication du 1er août 2026 sur le forum DarkForums, publiée par le compte NullsecNg (membre depuis avril 2026), intitulée « [SA] SOUTH AFRICA RESERVE BANK », signée par un individu utilisant l'alias « voss » au nom d'un groupe se présentant comme « NullSec Nigeria ». La publication se présente comme une riposte aux violences xénophobes visant des ressortissants nigérians et d'autres nationalités non sud-africaines en Afrique du Sud, et ne comporte pas de demande de rançon, ce qui la distingue d'une revendication d'extorsion à motivation financière classique.

  La publication revendique une « fuite de données » touchant la South African Reserve Bank et liste les catégories suivantes de matériel prétendument inclus : détails des employés, journaux d'accès, journaux d'accès fournisseurs, tickets de service informatique, et une catégorie rendue par « transactional logo » dans la publication d'origine (vraisemblablement une coquille pour « transactional logs »). Quatre liens vers un service d'hébergement de fichiers tiers sont fournis ; AFRINTEL n'a ni consulté, ni téléchargé, ni vérifié le contenu de ces liens, et la publication elle-même ne contient aucune capture d'écran, extrait de données ni autre preuve technique de l'intrusion revendiquée.

  AFRINTEL ne peut confirmer de façon indépendante ni l'intrusion alléguée, ni l'historique du profil « NullSec Nigeria », ni l'authenticité des fichiers liés, ni un quelconque lien entre cette revendication et l'infrastructure réelle de la SARB. Compte tenu des catégories de données revendiquées et du rôle de la SARB en tant que banque centrale et institution financière d'importance systémique pour l'Afrique du Sud, une compromission confirmée aurait un impact potentiel élevé ; à ce stade toutefois, la revendication repose sur des affirmations de forum non vérifiées et des liens de téléchargement non validés. AFRINTEL ne reproduit ni les liens de téléchargement ni aucun autre indicateur technique issu de la publication.


### 01 août 2026

#### 🇪🇬 Égypte - Egyptian Football Association (EFA)

* **Date de publication initiale :** 26 juillet 2026 à 18:20 (fuseau horaire non indiqué)

* **Date de détection AFRINTEL :** 01 août 2026

* **Acteur / Groupe :** Revesky, publication sur un forum cybercriminel

* **Secteur :** Sports / Fédérations sportives

* **Site web :** [efa.com.eg](https://www.efa.com.eg)

* **Statut :** Claim - Data Sample Published

* **Type d'incident :** Fuite de données

* **Niveau de confiance :** Élevé

* **Niveau d'impact :** Niveau 4

* **Description :**
  L'Egyptian Football Association (EFA) est l'instance nationale chargée de la gouvernance et de l'organisation du football en Égypte. Elle est affiliée à la FIFA et à la Confédération Africaine de Football (CAF).

* **Analyse :**
  **Observed :** Le 26 juillet 2026, l'acteur utilisant l'alias Revesky a publié un message affirmant avoir divulgué « toutes les bases de données » de l'Egyptian Football Association. La publication revendique un ensemble total d'environ **9,6 Go de données** concernant approximativement **350 000 joueurs**.

  Un ensemble de documents représentant environ **1,3 Go** a effectivement été divulgué par l'acteur. Les éléments examinés comprennent notamment des bases de données structurées ainsi que des documents administratifs associés aux joueurs.

  AFRINTEL a examiné trois fichiers CSV issus des éléments disponibles. `data.csv` et `simple_famous_player.csv` contiennent le même ensemble de **82 enregistrements sur 31 colonnes**, tandis que `simple_normal_player.csv` contient **802 enregistrements sur 45 colonnes**. Après déduplication des deux premiers fichiers, les données examinées représentent ainsi **884 lignes provenant de deux extractions distinctes**.

  Les champs observés couvrent notamment l'identité des joueurs, les numéros nationaux d'identification, les dates et lieux de naissance, la nationalité, des informations familiales, les équipes, transferts, contrats, saisons sportives et différentes informations administratives. Dans l'extrait contenant 802 lignes, **798 enregistrements comportent un numéro national d'identification numérique à 14 chiffres**.

  L'échantillon documentaire contient également plusieurs catégories de documents directement associées aux processus administratifs de l'EFA : formulaires d'inscription de joueurs portant l'identité visuelle de la fédération, copies de pièces d'identité, actes de naissance, contrats de joueurs professionnels, attestations d'assurance et documents de formation. Certains formulaires comportent également des photographies, signatures et empreintes. Ces éléments corroborent plusieurs catégories de données annoncées par Revesky.
  **Assumption :** La cohérence entre les bases structurées, les documents administratifs et l'identité visuelle de l'EFA permet d'évaluer avec un **niveau de confiance élevé** que les éléments examinés proviennent de données associées à la fédération. Cette évaluation concerne l'authenticité structurelle et l'attribution des échantillons ; elle ne confirme pas la méthode par laquelle Revesky les aurait obtenus.

  **Unknown :** AFRINTEL n'a pas validé l'intégralité du volume revendiqué de **9,6 Go**, ni le chiffre d'environ **350 000 joueurs**. Le corpus effectivement identifié représente environ **1,3 Go**, ce qui ne permet pas de confirmer que l'ensemble des bases revendiquées a réellement été rendu public. La présence de formulaires militaires dans l'ensemble complet n'a pas non plus été vérifiée dans les documents examinés. Le vecteur d'accès initial, la méthode d'extraction, la chronologie de la compromission et une éventuelle confirmation officielle de l'EFA restent inconnus.

  La nature des informations observées, comprenant des données d'identité, documents officiels, données contractuelles et dossiers pouvant concerner de jeunes joueurs ou des mineurs, crée un risque élevé de fraude documentaire, usurpation d'identité, phishing ciblé, ingénierie sociale et exploitation abusive des informations personnelles. AFRINTEL ne reproduit aucune identité, numéro national, adresse, signature, photographie ou autre donnée personnelle issue des éléments examinés.


### 05 août 2026
#### 🇩🇿 Algérie - Ministère du Commerce

- **Date de publication initiale :** 05 août 2026
- **Date de détection AFRINTEL :** 05 août 2026
- **Acteur / Groupe :** Florence, publication sur un forum cybercriminel
- **Secteur :** Gouvernement / Administration publique / Commerce
- **Site web :** Non précisé
- **Statut AFRINTEL :** Claim - Unverified
- **Type d’incident :** Vente d’accès
- **Niveau de confiance :** Faible
- **Niveau d’impact :** Niveau 4

- **Description :**

  Le ministère algérien du Commerce est l’administration publique chargée de la politique commerciale nationale, de la régulation des marchés et des services administratifs associés.

- **Analyse :**

  Une publication attribuée à Florence propose à la vente un accès VPN présenté comme appartenant au ministère algérien du Commerce, au prix de 500 USD. Le vendeur décrit les identifiants comme vérifiés et ne fournit aucune indication de revenus. La publication ne montre ni les identifiants, ni le point d’accès, ni le compte concerné, ni les privilèges disponibles, ni de preuve technique confirmant que l’accès fonctionne.

  L’accès annoncé pourrait permettre une entrée non autorisée dans des services gouvernementaux internes, une reconnaissance ultérieure, des opérations de phishing, un accès à des données ou des déplacements latéraux. La revendication reste non vérifiée et aucune confirmation indépendante du ministère, de l’accès VPN ou des identifiants n’est disponible dans la publication.

### 08 août 2026
#### 🇰🇪 Kenya - Plateforme de financement d'appareils PAYGO non identifiée (basée sur Angaza)

- **Date de publication initiale :** 16 janvier 2026
- **Date de détection AFRINTEL :** 08 août 2026
- **Acteur / Groupe :** OriginalCrazyOldFart, republication sur un forum cybercriminel d'un bucket cloud exposé publiquement
- **Secteur :** Services financiers / Financement d'appareils PAYGO / Commerce de détail
- **Site web :** Non identifié avec certitude
- **Statut AFRINTEL :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4

- **Description :**

  Les éléments examinés décrivent les opérations kényanes d'une plateforme non identifiée de financement d'appareils en paiement échelonné (PAYGO), construite sur le système SaaS Angaza, utilisée pour vendre des smartphones de marque (modèles Tecno Spark et Tecno Pop observés) à crédit via des agents de terrain locaux. La même archive contiendrait des données pour des opérations parallèles dans au moins une douzaine de marchés supplémentaires en Afrique et en Asie.

- **Analyse :**

  AFRINTEL a examiné une publication du 16 janvier 2026 par le membre de forum OriginalCrazyOldFart (compte ancien, à forte réputation), intitulée « Kenya & other countries Phones.7z FREE (has their names & cities too) ». La publication ne décrit pas une intrusion revendiquée ; elle pointe vers un bucket de stockage cloud exposé publiquement, indexé par le service de scan de buckets grayhatwarfare.com, et diffuse en miroir une archive de 1,28 Go sur un hébergeur de fichiers tiers. L'auteur précise que le matériel n'a pas été obtenu via une intrusion qu'il revendique, et avertit que certains liens peuvent déjà être rompus, sans proposer de nouvelle mise en ligne le cas échéant.

  Le fichier décrit contient à lui seul 27 526 lignes suivant un schéma d'export cohérent de la plateforme Angaza : nom complet du client, numéro de téléphone, ville/région, produit financé, prix journalier de l'échéance, montant cumulé payé, solde restant dû, statut du compte, date d'inscription, ainsi que le nom et le numéro de téléphone de l'agent de recouvrement assigné. Un second fichier mentionné dans la même publication, couvrant plusieurs pays au-delà du Kenya (dont l'Ouganda, le Nigeria, la Tanzanie, le Togo, le Malawi, la Zambie, le Bénin et le Myanmar), suit un schéma plus court : nom du client, numéro de téléphone et un identifiant numérique de compte/appareil. AFRINTEL n'a pas pu déterminer si l'ensemble des pays listés appartient à un seul opérateur multinational ou à plusieurs organisations distinctes partageant la même infrastructure Angaza, ni identifier la marque commerciale précise exploitant la partie kényane du jeu de données à partir des éléments examinés.

  L'ampleur, la cohérence structurelle et la plausibilité des échantillons justifient un niveau de confiance élevé quant à l'exposition de véritables dossiers clients et de financement, indépendamment de la question non résolue de l'identité exacte de l'entreprise. Compte tenu du volume, la combinaison de données financières (montants dus, historique de paiement), de coordonnées personnelles et d'agents de recouvrement nommément identifiés crée un risque significatif de fraude de type recouvrement de créances, d'usurpation d'agents, de phishing et de harcèlement visant les clients de financement dans les pays concernés. AFRINTEL ne reproduit aucun nom de client, numéro de téléphone, identifiant de compte, adresse ni montant financier issu des éléments examinés.

### 08 août 2026
#### 🇿🇦 Afrique du Sud - mpowa.mobi (Plateforme de services jeunesse)

- **Date de publication initiale :** 07 août 2026
- **Date de détection AFRINTEL :** 08 août 2026
- **Acteur / Groupe :** exfilar, publication sur un forum cybercriminel, opérateur/vendeur d'un outil de scan Firebase de masse
- **Secteur :** Développement de la jeunesse / Services à l'emploi (proche du gouvernement)
- **Site web :** [mpowa.mobi](https://mpowa.mobi) (instance exposée : staging.mpowa.mobi)
- **Statut AFRINTEL :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Très élevé
- **Niveau d'impact :** Niveau 4

- **Description :**

  mpowa.mobi est une plateforme sud-africaine de développement de la jeunesse et d'aide à l'emploi, proche des dispositifs publics, mettant en relation de jeunes demandeurs d'emploi avec des opportunités et des services d'accompagnement, développée dans le cadre d'une initiative liée à Code for South Africa.

- **Analyse :**

  AFRINTEL a examiné une publication du 7 août 2026 par l'acteur exfilar (compte de forum de niveau VIP), intitulée « mpowa.mobi - 2,585 Youth CVs Exposed via 0day Firebase Scanner », et a obtenu de façon indépendante l'export de la base de données Firebase Realtime Database référencée dans la publication. L'acteur affirme que la base RTDB Firebase de préproduction de la plateforme (staging.mpowa.mobi) était librement accessible en lecture, sans authentification, jeton ni vérification de referer, et qu'un outil de scan propriétaire l'a identifiée.

  L'examen par AFRINTEL de la base exportée confirme les chiffres annoncés dans la publication : 2 585 CV/curriculum vitae complets, 26 675 points de géolocalisation de prestations de services, 11 fiches d'un annuaire de prestataires de services, 19 comptes utilisateurs de la plateforme et 3 entrées de clés d'accès API. Chaque CV comprend un bloc d'informations personnelles (nom complet, téléphone, email, date de naissance, genre, nationalité, statut marital, statut de handicap, code de permis de conduire, plus haut diplôme), ainsi que des sections qualification, expérience professionnelle, langues, compétences et références personnelles ; ces dernières exposent en outre le nom, l'employeur, le poste et le numéro de téléphone de tiers désignés comme référents. Les 19 comptes utilisateurs incluent le nom complet, la date de naissance et les coordonnées géographiques de membres du personnel de la plateforme. Le jeu de données contient également 3 clés d'accès API d'apparence active, accompagnées de libellés descriptifs.

  La combinaison d'un statut de handicap, d'une date de naissance et de données d'identité complètes pour des mineurs et jeunes demandeurs d'emploi nommément identifiés constitue une catégorie spéciale de données personnelles au sens du cadre sud-africain POPIA. L'exposition de la base de préproduction d'une plateforme jeunesse proche du gouvernement, incluant des clés API actives, crée un risque significatif de détournement d'identifiants contre l'infrastructure associée, en plus des risques de fraude à l'identité, de phishing ciblé et d'atteinte à la sécurité physique des jeunes concernés et des tiers cités en référence. Le nom d'hôte de préproduction suggère qu'un environnement de production correspondant pourrait exister, avec une exposition similaire voire supérieure. La correspondance exacte entre les chiffres publiés par l'acteur et ceux observés indépendamment dans l'export examiné justifie un niveau de confiance très élevé. AFRINTEL ne reproduit aucun nom de candidat, coordonnée, date de naissance, déclaration de handicap, information de référence, dossier de personnel ni clé API issu des éléments examinés.

  La publication complète présente mpowa.mobi comme l'élément « 11/25 » d'une campagne en cours, décrivant un outil propriétaire (« CredHarvest V6 ») utilisé pour scanner et collecter en masse des instances Firebase Realtime Database mal configurées, et affirmant que des centaines de bases similaires ont déjà été récupérées par la même méthode. L'acteur propose à la fois la vente de cet outil de scan et des services d'intrusion/d'accès payants distincts sur le même forum. Cela indique que mpowa.mobi est une victime parmi une campagne plus large et systématique visant des déploiements Firebase mal configurés, et que des expositions comparables touchent vraisemblablement d'autres organisations africaines utilisant le même backend, indépendamment de tout ciblage spécifique à mpowa.mobi.

### 08 août 2026
#### 🇳🇬 Nigeria - Daily Trust

- **Date de publication initiale :** 08 août 2026
- **Date de détection de la source :** 08 août 2026, 19:21:01 (fuseau horaire non indiqué)
- **Date de détection AFRINTEL :** 11 août 2026
- **Acteur / Groupe :** Panzer
- **Secteur :** Médias / Édition / Audiovisuel
- **Site web :** [dailytrust.com](https://dailytrust.com)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4

- **Description :**

  Daily Trust est une organisation nigériane d'information et d'édition exploitée par Media Trust Limited. Ses services comprennent le journalisme imprimé et en ligne, Trust TV et Trust Radio.

- **Analyse :**

  **Observed :** Un enregistrement de source observé identifie Daily Trust, le groupe criminel Panzer, le Nigeria et `dailytrust.com`, avec un horodatage de détection au 8 août 2026 à 19:21:01 et des données publiées indiquées « N/D ». Une publication Panzer distincte datée du 8 août revendique 320 Go, propose un échantillon téléchargeable et affichait un compte à rebours actif de 17 jours, 11 heures, 3 minutes et 44 secondes lors de la capture du 11 août. L'échéance exacte et le fuseau horaire ne sont pas indiqués dans les éléments fournis.

  AFRINTEL a examiné l'intégralité du classeur `sample.xlsx` fourni en lecture seule. Ce fichier de 44 996 octets a pour empreinte SHA-256 `83516d93de48d2e53465071a418e50dd4b678baedef05277ab93ebb6f0034fa6` et contient deux feuilles. La feuille principale comporte 443 enregistrements non vides sous les champs Name, Email Address, New Password, Comments et Status. Les 443 cellules d'adresse email utilisent le domaine de la victime et sont uniques ; 438 lignes contiennent une valeur dans le champ New Password. La seconde feuille contient 19 entrées d'adresse du domaine cible, dont 18 recoupent la feuille principale, soit 444 adresses distinctes du domaine cible dans les champs d'adresse. Aucune des deux feuilles ne contient de formule ni de ligne complète dupliquée. Le classeur contient également 461 hyperliens HTTP externes pointant vers le domaine de la victime ; AFRINTEL ne les a pas suivis. Un composant `jsaProject.bin` incorporé a été identifié mais n'a pas été exécuté. Aucun nom, adresse email, mot de passe, commentaire, valeur de statut ou cible d'hyperlien de l'échantillon n'est reproduit.

  **Assumption :** Le schéma structuré de réinitialisation de comptes, l'utilisation exclusive du domaine de la victime dans les champs d'adresse, les relations cohérentes entre les feuilles et les hyperliens vers le domaine cible permettent d'évaluer avec un niveau de confiance élevé que l'échantillon est associé à Daily Trust. Si les mots de passe restent valides, ces éléments pourraient permettre des prises de contrôle de comptes, des compromissions de messagerie professionnelle, des usurpations, du phishing ciblé et l'accès à des communications éditoriales, de sources ou commerciales confidentielles. Cette évaluation porte sur l'authenticité structurelle et l'attribution de l'échantillon ; elle ne confirme pas la manière dont Panzer l'a obtenu.

  **Unknown :** AFRINTEL n'a pas établi si les mots de passe sont actuels, temporaires, anciennement utilisés ou déjà révoqués, ni si le classeur représente l'ensemble des comptes de Daily Trust. L'échantillon ne contient pas de plage temporelle fiable au niveau des enregistrements et ne valide pas le volume revendiqué de 320 Go. La méthode d'accès initial, la méthode d'extraction, un éventuel chiffrement ou impact opérationnel, l'échéance exacte de divulgation, la publication intégrale des données, la confirmation par la victime, la négociation, le paiement de rançon et la revente restent inconnus. La publication observée et l'échantillon cohérent ne constituent donc ni une confirmation officielle d'une intrusion ransomware ni une preuve d'exfiltration complète.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-08T19:21:01
listing_last_observed_at: 2026-08-11T01:56:25+01:00
sample_status: sample-reviewed
deadline_at:
deadline_status: active
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-20T01:35:32+01:00
-->

### 16 août 2026
#### 🇿🇦 Afrique du Sud - The Courier Guy

- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 16 août 2026 à 15:19:49 (fuseau horaire non affiché)
- **Date de détection AFRINTEL :** 19 août 2026
- **Acteur / Groupe :** medusalocker
- **Secteur :** Logistique / Services de courrier
- **Site web :** [thecourierguy.co.za](https://thecourierguy.co.za)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d’impact :** Niveau 2

- **Description :**

  The Courier Guy est une organisation sud-africaine de courrier et de logistique. Un enregistrement source observé attribue à medusalocker une entrée liée à un ransomware concernant `thecourierguy.co.za`.

- **Analyse :**

  **Observed :** L'enregistrement source fourni nomme « Thecourierguy », identifie le groupe criminel comme medusalocker, situe la cible en Afrique du Sud et indique `thecourierguy.co.za` comme domaine ciblé. Il affiche une détection le 16 août 2026 à 15:19:49, sans fuseau horaire visible, mentionne « N/D » pour les données publiées et revendique l'extraction de 2 018 emails. Cet enregistrement n'affiche ni échantillon, ni échéance de publication, ni prix de rançon, ni téléchargement de données.

  **Assumption :** La concordance entre le nom de l'organisation et son domaine soutient l'évaluation selon laquelle la publication vise spécifiquement cette cible. Si la revendication est exacte, une liste d'adresses email professionnelles ou de clients pourrait faciliter le phishing, la compromission de messagerie professionnelle, les attaques contre les identifiants et l'usurpation. La capture seule n'établit pas que medusalocker a obtenu ces adresses.

  **Unknown :** Aucun échantillon visible ne corrobore le chiffre de 2 018 emails ni n'établit la nature, la propriété, l'unicité ou la validité actuelle des enregistrements allégués. La date de publication, les méthodes d'accès initial et d'acquisition, le chiffrement ou la perturbation opérationnelle, la confirmation de la victime, la négociation, le paiement de rançon, la divulgation et la revente restent inconnus. Cette entrée est distincte de la publication incransom concernant SpearFin Ltd à Maurice.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-16T15:19:49
listing_last_observed_at: 2026-08-19T05:35:53+01:00
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-19T05:35:53+01:00
-->

### 17 août 2026
#### 🇰🇪 Kenya - SnapStar Talent (snapstartalent.com)

- **Date de publication initiale :** 17 août 2026
- **Date de détection AFRINTEL :** 18 août 2026
- **Acteur / Groupe :** exfilar, publication sur un forum cybercriminel, opérateur/vendeur d'un outil de scan Firebase de masse
- **Secteur :** Ressources humaines / Recrutement
- **Site web :** [snapstartalent.com](https://snapstartalent.com)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4

- **Description :**

  SnapStar Talent est présentée dans la publication observée comme une plateforme kényane de recrutement détenant des profils de candidats, des dossiers de candidature et des enregistrements relatifs aux entreprises clientes.

- **Analyse :**

  **Observed :** AFRINTEL a analysé les deux fichiers d'échantillon fournis avec la publication au lieu de s'appuyer uniquement sur les captures du forum. Le fichier CSV contient 300 dossiers de candidature structurellement valides répartis sur 36 colonnes, sans ligne mal formée ni doublon exact ; le fichier TXT contient 300 blocs détaillés correspondants. Les 300 identifiants de candidature concordent entre les deux fichiers dans le même ordre, et chaque champ scalaire renseigné comparé entre les représentations CSV et TXT est cohérent. L'échantillon couvre 207 profils de candidats distincts et six valeurs d'employeur, avec des horodatages de candidature allant du 13 au 16 août 2026. Les fichiers contiennent des marqueurs internes répétés de l'environnement elevated-talent, tandis que la représentation TXT contient également des libellés SnapStar Talent répétés. Leurs empreintes SHA-256 sont 8b358e7efcebd5002687f6dab193be24cb7535ce77dec411359bf33ffd42a834 (CSV) et 31cfc806bd28aeab2d79dc23c07cff59c31881a120aa481edfd192b09c403741 (TXT).

  Au niveau des profils uniques, les 207 profils contiennent une adresse email, un numéro de téléphone, une date de naissance, une valeur de salaire et une URL de CV. Des numéros nationaux d'identité ne sont présents que pour 11 profils (5,3 %), des URL d'entretien vidéo pour 50 profils (24,2 %) et des photographies de profil pour 41 profils (19,8 %). Des données de référence sont également présentes : 87 profils contiennent le nom d'un référent, 61 son adresse email et 74 son numéro de téléphone. Une date de naissance est objectivement incohérente car elle produit un âge de zéro an. L'échantillon ne confirme donc pas la formulation générale de l'acteur selon laquelle chaque dossier candidat contient un numéro national d'identité ou un entretien vidéo.

  L'export au niveau des candidatures contient 299 URL de CV représentant 209 liens distincts et 78 URL vidéo représentant 57 liens distincts. Tous les liens CV et vidéo observés utilisent Firebase Storage et contiennent des paramètres média avec jeton. AFRINTEL n'a pas interrogé ces URL ni récupéré les documents liés ; leur validité actuelle n'est donc pas établie. Les candidatures répétées appartenant à un même profil sont cohérentes pour l'email, le téléphone, la date de naissance et le numéro national d'identité ; un profil présente une variation de nom et deux profils plusieurs URL de CV, ce qui est compatible avec des mises à jour ordinaires de profil ou de document plutôt qu'avec une incohérence généralisée.

  **Assumption :** La correspondance exacte entre les fichiers CSV et TXT, les relations cohérentes entre candidatures et profils, les marqueurs internes propres à la cible, les horodatages récents et la structure homogène de Firebase Storage permettent d'évaluer avec un niveau de confiance élevé que l'échantillon est un véritable jeu de données de recrutement lié à l'environnement elevated-talent/SnapStar Talent. L'échantillon soutient matériellement la revendication selon laquelle des données d'identité, de contact, d'emploi, de rémunération, de CV, de vidéo et de références tierces ont été exposées ou mises à disposition de l'acteur. Il ne valide pas les volumes annoncés pour le jeu complet. L'échantillon vérifié suffit à créer un risque élevé de fraude au recrutement, de phishing ciblé, d'usurpation, de détournement d'identité et d'atteinte à la vie privée ; les liens de CV et vidéos contenant des jetons créent un risque supplémentaire d'accès aux documents s'ils restent actifs.

  **Unknown :** AFRINTEL n'a pas vérifié indépendamment l'accès Firestore prétendument non authentifié, la méthode d'extraction de l'acteur, les volumes annoncés de 93 462 profils, 83 237 candidatures et 176 795 documents, les 249,1 Go de fichiers, la présence de 83 entreprises clientes dans le jeu complet, ni une éventuelle réponse de SnapStar Talent. Les 300 candidatures les plus récentes constituent un échantillon non aléatoire ; leurs taux de complétude ne peuvent pas être extrapolés à l'ensemble du jeu proposé. L'incident reste donc classé comme une revendication accompagnée d'un échantillon publié, et non comme la confirmation de l'extraction complète de l'environnement de production. AFRINTEL ne reproduit aucun enregistrement personnel, lien de téléchargement, jeton d'URL, instruction de paiement ni coordonnée de l'acteur.

### 18 août 2026
#### 🇲🇺 Maurice - SpearFin Ltd

- **Date de publication initiale :** 18 août 2026
- **Date de détection AFRINTEL :** 18 août 2026
- **Acteur / Groupe :** incransom
- **Secteur :** Services financiers / Administration de fonds / Services aux entreprises
- **Site web :** [spearfin.net](https://spearfin.net)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 4

- **Description :**

  SpearFin Ltd est présentée dans la publication observée comme un prestataire mauricien de services d'administration de fonds, de services aux entreprises, de conformité et de relations investisseurs. La source revendique également 10 milliards USD d'actifs sous administration et 30 millions USD de chiffre d'affaires ; AFRINTEL n'a pas vérifié ces chiffres indépendamment.

- **Analyse :**

  **Observed :** Les captures fournies montrent une publication attribuée à incransom qui nomme SpearFin Ltd, identifie `spearfin.net` et localise la cible à Maurice. La publication est horodatée au 18 août 2026 à 09:35, sans fuseau horaire visible, et affirme qu'une fuite est survenue le 26 juin 2026, pour un volume de 416 Go. Elle mentionne des accords de confidentialité, correspondances clients, dossiers KYC, pièces d'identité, certificats, documents d'investissement et d'actionnariat, audits LBC/AML, contrats, formulaires, relevés bancaires, éléments de paie, documents de prêt et registres d'administrateurs. Elle revendique également 10 milliards USD d'actifs sous administration et 30 millions USD de chiffre d'affaires. AFRINTEL n'a pas vérifié ces chiffres indépendamment.

  La publication affiche plusieurs miniatures présentées comme des échantillons, comprenant des documents d'identité, d'entreprise, administratifs et financiers. Un échantillon agrandi est une annexe de confirmation/reconnaissance d'un contributeur structurée en sept sections et datée de juin 2026. Le texte visible contient une référence à un siège social à Maurice, un engagement de capital en USD à sept chiffres et des clauses relatives à la catégorie d'unités, aux frais de gestion, aux dépenses opérationnelles, au taux de rendement minimal et aux commissions de performance ; un sceau d'entreprise est partiellement visible. Ces éléments structurels sont cohérents avec des documents d'administration de fonds et d'investissement. Les noms, adresses, montants financiers exacts, pièces d'identité et autres valeurs confidentielles visibles ne sont pas reproduits. La publication annonce une divulgation intégrale à venir. Analyse limitée aux données visibles dans l'échantillon fourni ; les fichiers sources originaux n'étaient pas disponibles, n'ont pas été consultés ni téléchargés.

  **Assumption :** La combinaison des détails de publication propres à la cible, d'un échantillon contractuel lié à Maurice, d'une terminologie cohérente avec les fonds d'investissement, de dates contractuelles récentes et de plusieurs catégories de documents soutient avec un niveau de confiance moyen l'évaluation selon laquelle une partie au moins des éléments visibles est associée aux services attribués à SpearFin. S'ils sont authentiques, les dossiers KYC, d'identité, bancaires, de paie, de gouvernance d'entreprise et d'investissement créeraient un risque élevé de fraude à l'identité, de compromission de messagerie professionnelle, de fraude au paiement, de phishing ciblé et d'atteinte à la confidentialité des clients et investisseurs. Cette évaluation n'authentifie pas chaque miniature, signature ou sceau et n'établit pas la méthode d'acquisition.

  **Unknown :** En l'absence des fichiers originaux, AFRINTEL n'a pas pu examiner les métadonnées, signatures, sceaux, l'intégrité des documents, les doublons, la cohérence interne de l'ensemble des échantillons ni une éventuelle manipulation. AFRINTEL n'a pas confirmé indépendamment l'accès non autorisé, l'exfiltration de données, le chiffrement par ransomware, une perturbation opérationnelle, le volume revendiqué de 416 Go, la date alléguée du 26 juin 2026, les chiffres financiers annoncés ni la publication d'une archive complète. Aucun communiqué de la victime ni élément technique indépendant n'a été fourni. La fiche documente donc une publication incransom observée avec des échantillons visibles concernant une victime mauricienne distincte, et non une compromission ou une divulgation intégrale confirmée.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-18T09:35:00
listing_last_observed_at: 2026-08-18T21:15:30+01:00
sample_status: preview-visible
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-19T06:02:04+01:00
-->

### 20 août 2026
#### 🇩🇿 Algérie - Afribaba (dz.afribaba.com)

- **Date de publication initiale :** 20 août 2026
- **Date de détection AFRINTEL :** 20 août 2026
- **Acteur / Groupe :** TelephoneHooliganism, publication sur un forum cybercriminel
- **Secteur :** Commerce en ligne / Marketplace
- **Site web :** [dz.afribaba.com](https://dz.afribaba.com) (site régional observé) ; domaine cité par l'acteur : www.afribaba.dz
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 3

- **Description :**

  Afribaba est une plateforme de petites annonces destinée aux particuliers et aux professionnels en Algérie. Les sources publiques consultées décrivent le service régional sous le domaine dz.afribaba.com ; la publication de l'acteur cite toutefois www.afribaba.dz.

- **Analyse :**

  **Observed :** La publication du 20 août 2026 attribuée à TelephoneHooliganism affirme proposer environ 642 000 contacts de détaillants vérifiés, avec numéros de téléphone, historique de commandes et tickets de support, pour 1 400 USD négociables. Elle décrit trois sections d'export et affiche plusieurs liens d'échantillon que AFRINTEL n'a pas suivis. Le fichier local fourni est uniquement Order_History_Algeria.csv, d'une taille de 5 123 octets, composé de 20 lignes de données et 32 colonnes. Son empreinte SHA-256 est 6c5ecf4641436931b8dd5036a13300ffb04c38f6d2c275cb4c5172d02bffe196.

  L'analyse complète du CSV relève 20 lignes structurellement lisibles, sans ligne complète dupliquée, mais seulement deux valeurs distinctes de order_id, avec 18 répétitions d'identifiant de commande. Les dates de commande couvrent mars 2022 à septembre 2024. Les statuts de commande observés sont Completed (9), Pending (4), Processing (4) et Canceled (3) ; les statuts de paiement sont Paid (12), Pending (5) et Refunded (3). Les champs monétaires sont tous en USD ; les montants observés totalisent 4 453,55 USD avant de considérer la signification commerciale de cet échantillon.

  **Assumption :** Le nom de domaine cité, le titre de la publication et la structure d'un export de commandes sont compatibles avec une revendication visant l'écosystème Afribaba. La présence de pays d'expédition Brazil (13 lignes), Bulgaria (2), Cambodia (2), Cameroon (2) et Brunei (1), sans ligne d'expédition algérienne, constitue toutefois une incohérence avec l'intitulé « Algeria » et empêche de relier fermement cet extrait au périmètre algérien ou à la plateforme Afribaba. L'échantillon peut correspondre à un environnement multi-pays, à des données de démonstration, à une attribution erronée ou à un extrait dont le contexte est incomplet.

  **Unknown :** AFRINTEL n'a pas reçu les tables Customer Contacts ou Support Tickets annoncées, ni l'archive d'environ 642 000 contacts. Les liens d'échantillon n'ont pas été suivis, aucun numéro de téléphone, nom, adresse, identifiant client ou ticket n'est reproduit, et aucune confirmation d'Afribaba n'est disponible. Le fichier fourni ne permet pas de confirmer le volume revendiqué, l'origine technique, la validité des données, la méthode d'accès, l'exposition de numéros de téléphone ou le prix proposé.

### 22 août 2026
#### 🇲🇦 Maroc - RAMED (Régime d’Assistance Médicale)

- **Acteur / Groupe :** JBT2026
- **Secteur :** Gouvernement / Administration
- **Statut :** Claim - Data Sample Published
- **Site web :** Non précisé dans les éléments fournis

- **Description :**
  RAMED, le Régime d’Assistance Médicale, est l’ancien dispositif marocain destiné à faciliter l’accès aux soins des populations à faibles revenus et vulnérables. La publication observée concerne une base présentée comme associée aux bénéficiaires de ce régime.

- **Analyse :**
  Le 22 août 2026, l’acteur JBT2026 a publié sur un forum underground des données présentées comme provenant du système RAMED. Il affirme détenir plus de **17 millions d’entrées** et avoir rendu publiques environ **1 million d’entrées**, avec l’intention annoncée de publier ultérieurement l’ensemble de la base.

  L’analyse du fichier principal fourni met en évidence **1 098 685 enregistrements**, répartis sur **17 colonnes**, pour une taille d’environ **183,1 Mo**. Les données comprennent notamment des identifiants administratifs, noms et prénoms en caractères latins et arabes, sexe, dates de naissance, numéros de CIN lorsqu’ils sont renseignés ainsi que des informations géographiques et administratives.

  Des éléments complémentaires renforcent la cohérence de la publication. Quatre fichiers CSV supplémentaires contiennent **10 enregistrements**, tous retrouvés à l’identique dans le fichier principal. Sept photographies de type portrait d’identité ont également été fournies ; chacune correspond, par son nom de fichier, à une personne présente dans ces données structurées.

  Ces éléments permettent désormais d’établir la présence effective de **photographies d’identité associées à certains enregistrements de l’échantillon analysé**. Ils renforcent la cohérence de l’affirmation de l’acteur concernant l’existence de photos, sans permettre de conclure que l’ensemble des plus de 17 millions d’entrées revendiquées contient une photographie.

  Sur les **1 098 685 enregistrements**, **666 103** comportent une valeur dans le champ CIN, tandis que **432 582**, soit environ **39,4 %**, n’en comportent pas. Les dates de naissance sont disponibles dans un format complet pour **842 259 enregistrements**, tandis que **256 426** présentent des valeurs partielles.

  L’association de données d’identité structurées, de numéros de CIN et de photographies augmente sensiblement le risque d’**usurpation d’identité, de fraude documentaire, de phishing ciblé et de recoupement avec d’autres bases compromises**.

  La structure des données, leur contenu bilingue, les références administratives marocaines et la correspondance entre certains enregistrements et les photographies renforcent la cohérence de l’échantillon avec des données concernant des bénéficiaires au Maroc.

  **Limites de preuve :** les éléments analysés ne permettent pas de confirmer le système technique d’origine, le vecteur d’accès initial, la méthode d’extraction, la possession effective des plus de 17 millions d’entrées revendiquées ni une confirmation officielle de l’incident par une institution marocaine. La présence de photographies est établie uniquement pour les éléments fournis et ne doit pas être extrapolée à l’ensemble de la base revendiquée.
 ---
### 24 août 2026
#### 🇲🇦 Maroc - Direction générale de la Sûreté nationale (DGSN) / Direction générale de la Surveillance du territoire (DGST)

* **Date de publication initiale :** 24 août 2026
* **Date de détection AFRINTEL :** 24 août 2026
* **Acteur / Groupe :** JabaR00t, publication relayée par le compte JBT2026 sur un forum cybercriminel
* **Secteur :** Gouvernement / Administration / Sécurité et renseignement
* **Site web :** [dgsn.gov.ma](https://dgsn.gov.ma) / `dgst.gov.ma` (domaine associé à la DGST, portail public non confirmé)
* **Statut AFRINTEL :** Data Fully Published
* **Type d'incident :** Fuite de données
* **Niveau de confiance :** Élevé
* **Niveau d'impact :** Niveau 4
* **Description :**
  La Direction générale de la Sûreté nationale (DGSN) est le corps national de police du Maroc. La Direction générale de la Surveillance du territoire (DGST) est le service marocain chargé du renseignement intérieur et de la sécurité territoriale. Les deux institutions occupent une fonction stratégique au sein de l'appareil de sécurité nationale marocain.

* **Analyse :**
  **Observed :** Le 24 août 2026, une publication relayée par le compte JBT2026 et attribuée à JabaR00t a présenté sous l'intitulé `#OP_CEUTA` une base décrite comme contenant environ **70 000 personnels associés à la DGSN et à la DGST**. L'acteur présente cette base comme publiée intégralement et affirme parallèlement que les données diffusées ne représenteraient qu'une partie d'un ensemble plus large prétendument exfiltré.
  L'analyse des fichiers fournis identifie **70 381 enregistrements** dans le fichier principal. Les données observées comprennent notamment des informations d'identité, numéros PPR, numéros de CIN/CNI, dates de naissance et années de recrutement.
  Trois fichiers complémentaires contiennent respectivement **8 789**, **1 456** et **21 enregistrements**. Ils apportent notamment des informations relatives au grade et aux coordonnées bancaires RIB. Plusieurs recoupements existent entre ces différents jeux de données ; leurs volumes ne doivent donc pas être additionnés aux 70 381 enregistrements du fichier principal comme s'il s'agissait de populations indépendantes.

  La correspondance entre le volume de **70 381 enregistrements** effectivement observé et la revendication publique d'une base d'environ 70 000 personnes constitue un élément important de cohérence. Les différents fichiers présentent également des structures compatibles entre elles et des données administratives correspondant au contexte marocain.

  **Assumption :** La cohérence structurelle du corpus, les informations administratives observées et les recoupements entre plusieurs fichiers permettent d'évaluer avec un **niveau de confiance élevé** que les données publiées sont associées à des personnels relevant de l'écosystème DGSN/DGST. Cette évaluation concerne l'attribution et la cohérence des données examinées ; elle ne confirme pas la méthode utilisée par JabaR00t pour les obtenir.

  Le statut `Data Fully Published` s'applique à la base d'environ 70 000 enregistrements que l'acteur présente comme publiée intégralement. Il ne signifie pas que l'ensemble des autres données que JabaR00t affirme avoir exfiltrées a été rendu public ou vérifié.

  La combinaison d'informations d'identité, d'identifiants administratifs, de données professionnelles, de grades et de coordonnées bancaires représente un **niveau d'impact critique**. Elle peut faciliter l'usurpation d'identité, la fraude financière, le spear-phishing, l'ingénierie sociale ciblée et la cartographie de personnels. Dans le contexte d'organismes de police et de renseignement, cette exposition présente également des enjeux de sécurité opérationnelle, de profilage de personnels et de contre-ingérence.

  **Unknown :** Les éléments disponibles ne permettent pas d'établir le vecteur d'accès initial, les systèmes sources concernés, la méthode d'extraction, la date exacte de l'acquisition des données ni l'étendue globale de ce que l'acteur affirme avoir obtenu. Il n'est pas non plus possible d'établir, à partir des seuls fichiers analysés, que chacun des 70 381 enregistrements correspond à un agent de renseignement actif, ni de déterminer la répartition exacte des enregistrements entre la DGSN et la DGST.

  Aucune confirmation publique indépendante de la DGSN ou de la DGST concernant l'intégralité de la compromission revendiquée n'est établie dans les éléments analysés. AFRINTEL ne reproduit aucun nom, numéro PPR, CIN/CNI, RIB, date de naissance ou autre donnée personnelle issue des fichiers examinés.

