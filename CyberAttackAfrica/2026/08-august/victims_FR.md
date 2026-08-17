![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en août 2026 (4 victimes)

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

  AFRINTEL a examiné une publication du 7 août 2026 par l'acteur exfilar (compte de forum de niveau VIP), intitulée « mpowa.mobi — 2,585 Youth CVs Exposed via 0day Firebase Scanner », et a obtenu de façon indépendante l'export de la base de données Firebase Realtime Database référencée dans la publication. L'acteur affirme que la base RTDB Firebase de préproduction de la plateforme (staging.mpowa.mobi) était librement accessible en lecture, sans authentification, jeton ni vérification de referer, et qu'un outil de scan propriétaire l'a identifiée.

  L'examen par AFRINTEL de la base exportée confirme les chiffres annoncés dans la publication : 2 585 CV/curriculum vitae complets, 26 675 points de géolocalisation de prestations de services, 11 fiches d'un annuaire de prestataires de services, 19 comptes utilisateurs de la plateforme et 3 entrées de clés d'accès API. Chaque CV comprend un bloc d'informations personnelles (nom complet, téléphone, email, date de naissance, genre, nationalité, statut marital, statut de handicap, code de permis de conduire, plus haut diplôme), ainsi que des sections qualification, expérience professionnelle, langues, compétences et références personnelles ; ces dernières exposent en outre le nom, l'employeur, le poste et le numéro de téléphone de tiers désignés comme référents. Les 19 comptes utilisateurs incluent le nom complet, la date de naissance et les coordonnées géographiques de membres du personnel de la plateforme. Le jeu de données contient également 3 clés d'accès API d'apparence active, accompagnées de libellés descriptifs.

  La combinaison d'un statut de handicap, d'une date de naissance et de données d'identité complètes pour des mineurs et jeunes demandeurs d'emploi nommément identifiés constitue une catégorie spéciale de données personnelles au sens du cadre sud-africain POPIA. L'exposition de la base de préproduction d'une plateforme jeunesse proche du gouvernement, incluant des clés API actives, crée un risque significatif de détournement d'identifiants contre l'infrastructure associée, en plus des risques de fraude à l'identité, de phishing ciblé et d'atteinte à la sécurité physique des jeunes concernés et des tiers cités en référence. Le nom d'hôte de préproduction suggère qu'un environnement de production correspondant pourrait exister, avec une exposition similaire voire supérieure. La correspondance exacte entre les chiffres publiés par l'acteur et ceux observés indépendamment dans l'export examiné justifie un niveau de confiance très élevé. AFRINTEL ne reproduit aucun nom de candidat, coordonnée, date de naissance, déclaration de handicap, information de référence, dossier de personnel ni clé API issu des éléments examinés.

  La publication complète présente mpowa.mobi comme l'élément « 11/25 » d'une campagne en cours, décrivant un outil propriétaire (« CredHarvest V6 ») utilisé pour scanner et collecter en masse des instances Firebase Realtime Database mal configurées, et affirmant que des centaines de bases similaires ont déjà été récupérées par la même méthode. L'acteur propose à la fois la vente de cet outil de scan et des services d'intrusion/d'accès payants distincts sur le même forum. Cela indique que mpowa.mobi est une victime parmi une campagne plus large et systématique visant des déploiements Firebase mal configurés, et que des expositions comparables touchent vraisemblablement d'autres organisations africaines utilisant le même backend, indépendamment de tout ciblage spécifique à mpowa.mobi.

## Notes (non comptabilisées dans le total mensuel de victimes)

### 17 août 2026
#### 🇰🇪 Kenya - Kenya Electricity Transmission Company (KETRACO), republication d'un incident déjà documenté

- **Référence :** initialement documenté comme incident distinct le 31 décembre 2025, voir `CyberAttackAfrica/2025/12-december/victims_FR.md`.
- **Observation :** AFRINTEL a observé le même échantillon divulgué (mêmes champs, même unité organisationnelle « nl_KETRACO_Newsletter_Unit », et la même anomalie de valeur de mot de passe partagée entre les enregistrements) republié sur le forum DarkForums sous l'alias Linda2000, environ huit mois après la publication initiale sur RaidForums attribuée à LindaBF.
- **Évaluation :** ce constat est interprété comme une republication du même jeu de données plutôt que comme une nouvelle compromission, et n'est pas comptabilisé comme un incident supplémentaire d'août 2026. Il indique que la donnée continue de circuler et pourrait encore être échangée entre acteurs malveillants. AFRINTEL ne reproduit aucun nom d'utilisateur, adresse email, valeur de mot de passe, lien de téléchargement ni enregistrement de l'échantillon.

