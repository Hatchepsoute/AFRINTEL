![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en octobre 2026 (48 fiches)

👉🏾 [**English version available here**](./victims.md)

## Octobre 2026

**Statut du suivi mensuel : Published / Publié**  -  corpus de 48 fiches publiées ou signalées en octobre 2026. La clôture et les statistiques mensuelles sont publiées dans le rapport associé.

### 1 octobre 2026
#### 🇨🇩 République démocratique du Congo - ServerUnlockApp (`serverunlockapp.com`) [Data Leak]

- **Date de publication initiale :** 1 octobre 2026 à 13:32 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** SensitiveDarkForum (compte/forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Services numériques / Déverrouillage et activation de téléphones et services associés
- **Site web :** [serverunlockapp.com](https://serverunlockapp.com/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Effet revendiqué :** Divulgation de fichiers de sauvegarde d'un site web et de données applicatives
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Type de source :** Publication de forum underground et sauvegarde locale fournie à AFRINTEL

- **Description victime :** ServerUnlockApp est un service en ligne associé à la République démocratique du Congo, proposant des services de déverrouillage de téléphones, de traitement d'IMEI, d'activation d'outils et de services connexes. Le site public associe l'activité à Kinshasa et affiche des moyens de paiement et de contact destinés aux clients et revendeurs.

- **Analyse :**

  **Observed :** Une publication du forum SensitiveDarkForum, horodatée du **1 octobre 2026 à 13:32** selon l'heure affichée, présente des « Website Backup Files » associés à `serverunlockapp.com` et à la RDC. L'échantillon local correspond à une arborescence de sauvegarde applicative de **7 329 fichiers** pour **158 750 705 octets** selon la somme des tailles de fichiers. Elle comprend notamment **3 467 fichiers PHP**, **708 fichiers JavaScript**, **504 fichiers JSON**, **473 gabarits**, **249 feuilles CSS**, des ressources graphiques et des fichiers de configuration.

  Le corpus comprend une application `unlockapp`, des scripts de gestion de clients, de services, de commandes, de paiement, de messagerie et d'administration. Des fichiers `config.php`, un fichier temporaire de configuration, des certificats, des fichiers PEM et une clé sont présents ; leurs valeurs n'ont pas été reproduites, testées ou publiées. La présence de ces fichiers démontre seulement qu'ils sont inclus dans la sauvegarde fournie ; elle ne documente pas qu'ils sont encore valides ni qu'ils donnent accès au service.

  Le fichier `unlockapp/tmp/export.csv` contient **719 lignes de données** et des colonnes relatives au nom d'utilisateur, à l'adresse e-mail, à la date d'inscription, au solde disponible et aux montants dus. L'analyse complète du CSV relève **130 soldes non nuls**, pour un total de **1 493,672 USD**, avec un solde maximal de **334,649 USD**. Quatre lignes contiennent un montant dû non nul, pour un total de **39,900 USD**. Les dates d'inscription s'étendent du **13 novembre 2024** au **25 avril 2025** ; les champs de drapeau sont vides sur les **719 lignes**. Les noms d'utilisateur et adresses e-mail sont distincts dans ce fichier, sans que cela permette d'établir l'identité ou le nombre réel de personnes concernées. Deux fichiers JSON de travail contiennent respectivement **365** et **173** éléments structurés autour de services ou de groupes. Ces fichiers indiquent la présence de données commerciales et de comptes applicatifs, sans permettre de déduire le nombre total d'utilisateurs ou de transactions.

  **Assumption :** La correspondance entre le domaine publié, l'arborescence `unlockapp`, les fonctions de déverrouillage et d'IMEI, les données de comptes et les éléments commerciaux rend l'association de la sauvegarde à ServerUnlockApp fortement plausible. La structure est compatible avec une copie de site ou de serveur applicatif. Elle ne permet pas d'établir le vecteur d'accès, l'identité réelle de l'auteur, la date d'acquisition ou l'utilisation effective des éventuels secrets.

  **Unknown :** Le périmètre exact des systèmes copiés, la chronologie technique de l’accès, l'origine technique de la sauvegarde, l'exhaustivité des données, le nombre de personnes uniques, les doublons, la validité des comptes, la validité des certificats et clés, les transactions réellement concernées, l'impact opérationnel et toute confirmation de ServerUnlockApp ne sont pas renseignés dans les sources consultées. La publication ne permet pas de conclure à une compromission en temps réel du site.

- **Périmètre et limites de l'analyse :** L'arborescence locale a été inventoriée en lecture seule. Les fichiers PHP, JavaScript et autres scripts n'ont pas été exécutés. Les valeurs de configuration, clés, certificats, identifiants, e-mails et données financières n'ont pas été reproduits. L'analyse porte sur la structure de la sauvegarde et sur des agrégats du CSV/JSON ; elle ne valide ni l'exhaustivité du prétendu backup ni l'accès actuel à l'application.
- **Risques :** Réutilisation de comptes clients, fraude liée aux soldes ou paiements, phishing ciblé, usurpation de revendeurs, exposition de données commerciales, réutilisation potentielle de secrets et compromission secondaire d'intégrations de paiement ou de messagerie.
- **Recommandations SOC / CTI :** Révoquer et renouveler les secrets, clés, certificats et sessions potentiellement exposés ; examiner les journaux d'administration, de téléchargement et d'export ; vérifier les comptes clients et revendeurs ; contrôler les intégrations de paiement et de messagerie ; rechercher les modifications de code et tâches planifiées ; préserver les sauvegardes originales et ne pas exécuter les scripts divulgués.
- **Évaluation AFRINTEL :** Publication observée ; sauvegarde applicative fournie et analysée ; attribution à ServerUnlockApp fortement plausible ; données de comptes et éléments commerciaux observés ; secrets potentiels présents mais non testés ; accès non autorisé, exfiltration complète et validité actuelle des secrets non documenté dans les sources publiquess.


#### 🇲🇦 Maroc - Midipcom

- **Date de publication initiale :** 1 octobre 2026 à 21:25 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** Nameless511 (compte de forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Technologie / Distribution de matériel informatique
- **Site web :** [midipcom.ma](https://midipcom.ma/) ; `pro.midipcom.ma` cité dans la publication
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d’impact :** Level 3
- **Type de source :** Underground Forum - Publication fournie à AFRINTEL + échantillons locaux analysés en lecture seule

- **Description victime :** Midipcom est un distributeur marocain de matériel informatique, d’équipements reconditionnés, de périphériques et de solutions d’impression. Son site présente notamment des ordinateurs, composants, accessoires, écrans, imprimantes et toners.

- **Analyse :**

  **Observed :** Une publication de forum attribuée au compte **Nameless511**, horodatée du **1 octobre 2026 à 21:25** selon l’heure affichée, annonce une « base de données Midipcom » associée à `midipcom.ma` et `pro.midipcom.ma`. L’auteur affirme disposer d’un export Odoo couvrant janvier 2023 à septembre 2026, de **146 fichiers CSV** pour **158 MB**, ainsi que de totaux par fichier. Ces volumes et ces décomptes restent des revendications non validées. AFRINTEL a analysé en lecture seule les **six fichiers CSV** fournis localement, totalisant **335 319 octets** : transferts bancaires, clients, factures, courriels, commandes fournisseurs et commandes clients. Les fichiers présentent des marqueurs récurrents de Midipcom et d’Odoo, des métadonnées comptables et commerciales, ainsi que des dates visibles s’étendant de **mai 2023** à **septembre 2026**. Les catégories observables couvrent la comptabilité, les mouvements de stock, factures, commandes, partenaires commerciaux et messagerie. Des champs sensibles potentiels, dont un champ nommé `access_token`, sont présents dans le schéma ; aucune valeur n’est reproduite ni testée.

  **Assumption :** La cohérence entre les six fichiers, les références à Midipcom, les structures Odoo et les activités commerciales décrites par le site officiel soutient fortement l’association de l’échantillon avec l’environnement opérationnel de Midipcom. Les sources consultées ne précisent pas le système exact d’origine, le vecteur d'accès, l'extraction complète ni la validité actuelle d'éventuels jetons ou comptes.

  **Unknown :** Le nombre réel de fichiers et d’enregistrements, les **146 fichiers** et **158 MB** revendiqués, l’intégrité des exports originaux, les personnes ou organisations uniques concernées, les doublons, les systèmes affectés, la date et la méthode d’obtention, l’existence d’un accès non autorisé, l’exfiltration complète, l’impact opérationnel et toute confirmation par Midipcom ou une autorité ne sont pas renseignés dans les sources consultées.

- **Périmètre et limites de l’analyse :** Les six fichiers locaux ont été examinés dans leur intégralité, avec calcul des empreintes SHA-256, taille, encodage et recherche de marqueurs structurels. Chaque fichier ne contient toutefois qu’un seul séparateur de ligne : les enregistrements sont concaténés dans une ligne continue. Cette anomalie empêche une reconstruction fiable des lignes, une déduplication ou une validation indépendante des totaux annoncés. Aucun fichier additionnel, archive de 158 MB ou corpus de 146 CSV n’a été fourni. Les échantillons restent hors dépôt et aucune donnée personnelle, valeur financière, nom de partenaire, référence de paiement ou jeton n’est publié.

- **Évaluation des risques :** Si les données sont authentiques, la combinaison d’informations commerciales, de facturation, de commandes, de stocks, de partenaires et de messagerie peut soutenir la fraude à la facture, l’usurpation de fournisseur ou de client, le phishing ciblé et l’espionnage commercial. Les champs pouvant contenir des jetons imposent une vérification et une rotation contrôlées, sans présumer qu’un secret exploitable est présent ou actif.

- **Recommandations :**
  1. Préserver les journaux Odoo, bases de données, sauvegardes, applications web, messagerie et comptes d’administration couvrant au minimum la période documentée par les exports.
  2. Examiner les exports de masse, accès d’administrateurs, comptes de prestataires, connexions inhabituelles, tâches planifiées et transferts sortants.
  3. Inventorier et révoquer de manière contrôlée les jetons, clés API, sessions et liens d’accès exposés potentiellement, puis surveiller leur réutilisation.
  4. Valider le périmètre des données clients, fournisseurs et financières avant de lancer les procédures de notification appropriées.
  5. Renforcer la détection des fraudes au changement de coordonnées bancaires, faux bons de commande et demandes de paiement ciblant les partenaires.

- **Sources / Éléments de preuve :** publication de forum et image fournie le 8 octobre 2026 ; six fichiers CSV locaux fournis et analysés en lecture seule ; [site officiel de Midipcom](https://midipcom.ma/). Aucun lien vers le forum, extrait de donnée, identifiant, contact, référence financière ni secret n’est publié.


### 2 octobre 2026
#### 🇲🇦 Maroc - Ministère de l’Aménagement du territoire national, de l’Urbanisme, de l’Habitat et de la Politique de la ville

- **Date de publication initiale :** 2 octobre 2026 à 15:20 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** Nameless511 (compte de forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Gouvernement / Administration / Habitat et urbanisme
- **Site web associé :** [matnuhpv.gov.ma](https://matnuhpv.gov.ma/) (domaine affiché par l’auteur dans la publication ; lien avec le système concerné non documenté dans les sources publiques)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** Medium
- **Niveau d’impact :** Level 4
- **Type de source :** Underground Forum - Publication fournie à AFRINTEL

- **Description victime :** Le ministère marocain est chargé des politiques publiques relevant de l’aménagement du territoire, de l’urbanisme, de l’habitat et de la politique de la ville. Son identité institutionnelle et ses attributions sont documentées dans un décret d’organisation publié par l’administration marocaine.

- **Analyse :**

  **Observed :** Une publication de forum attribuée au compte **Nameless511**, horodatée du **2 octobre 2026 à 15:20** selon l’heure affichée, propose à la vente des données attribuées au ministère. Sa page de présentation affiche le domaine `matnuhpv.gov.ma`. Le titre mentionne **26 452 dossiers de candidats**, tandis que le corps du message affirme que plus de **2 772 dossiers** ont été compromis et décrit **2 772 profils complets de candidats** comme le contenu détenu et proposé à la vente. Ces deux volumes restent contradictoires et non validés. La rubrique « Samples » est distincte : les lignes visibles qui suivent constituent l’échantillon fourni dans l’échange. Cet échantillon est structuré comme des listes de candidatures à des concours de recrutement, notamment pour des postes de technicien de troisième grade et d’ingénieur d’État de premier grade. Les catégories visibles comprennent identité, numéro national d’identité, date et lieu de naissance, coordonnées, adresse, situation de candidature, diplômes, spécialités, établissement délivrant le diplôme, centre d’examen et références de pièces justificatives. Aucune valeur individuelle, aucun nom de fichier de dossier ni identifiant n’est reproduit dans cette fiche.

  **Assumption :** Le logo institutionnel, l’intitulé de l’administration, le domaine affiché et le schéma des données sont cohérents avec des processus de candidature ou de recrutement relevant du ministère. Cette cohérence ne documente pas que `matnuhpv.gov.ma` ou un autre système ministériel a été compromis : une copie historique, un prestataire, un agrégateur, une source tierce ou une présentation trompeuse restent possibles.

  **Unknown :** Le fichier source, son empreinte, le nombre réel de lignes et de personnes uniques, l’authenticité, l’actualité et l’exhaustivité des enregistrements, le système d’origine, la date et la méthode d’obtention, l’existence d’un accès non autorisé, toute exfiltration, tout impact opérationnel et toute confirmation officielle par le ministère ou une autorité ne sont pas renseignés dans les sources consultées.

- **Périmètre de l’analyse :** Analyse préliminaire fondée sur la publication et les données visibles dans l’échantillon fourni après la rubrique « Samples » ; le fichier source original n’était pas disponible. Cet échantillon ne permet ni de valider les volumes revendiqués, ni de dédupliquer les personnes concernées, ni d’établir la provenance technique des données.

- **Évaluation des risques :** Si elles sont authentiques, les catégories de données observées pourraient faciliter l’usurpation d’identité, le phishing ciblé, la fraude documentaire, l’ingénierie sociale et l’exploitation abusive de procédures de recrutement. La présence alléguée de références à des pièces justificatives peut accroître les risques pour les candidats ; elle ne documente pas que les documents eux-mêmes sont accessibles.

- **Recommandations :**
  1. Préserver les journaux des portails de candidature, des outils de recrutement, des espaces documentaires et des comptes administratifs concernés.
  2. Rechercher les exports volumineux, requêtes anormales, accès privilégiés inhabituels et accès de tiers autour de la période à déterminer par l’enquête.
  3. Vérifier, par des moyens autorisés, si les schémas de champs et les références de dossiers correspondent à des applications ou prestataires ministériels.
  4. Évaluer le périmètre de personnes potentiellement concernées avant toute notification et renforcer la détection de phishing ou de fraude ciblant les candidats.
  5. Ne pas télécharger l’offre, ne pas contacter le vendeur et ne pas tester les données individuelles divulguées.

- **Sources / Éléments de preuve :** publication de forum et échantillon visible fournis le 8 octobre 2026 ; [décret marocain relatif aux attributions et à l’organisation du ministère](https://bdj.mmsp.gov.ma/Fr/Document/10596-D%C3%A9cret-n-2-23-751-du-7-joumada-II-1445-21-d%C3%A9cemb.aspx?KeyPath=594%2F681%2F697%2F10596). Aucun lien vers le forum ni aucune donnée personnelle n’est publié.


#### 🇲🇦 Maroc - Karamtech

- **Date de publication initiale :** 2 octobre 2026 à 00:51 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** Nameless511 (compte de forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Technologie / Commerce et distribution de matériel informatique et de sécurité
- **Site web :** [karamtech.ma](https://karamtech.ma/) ; `kmt.codebarre.ma` cité dans la publication
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d’impact :** Level 4
- **Type de source :** Underground Forum - Publication fournie à AFRINTEL + échantillons locaux analysés en lecture seule

- **Description victime :** Karamtech est un site marocain de commerce électronique présentant du matériel informatique, des accessoires, des équipements réseau, des solutions d’impression, de contrôle d’accès et de sécurité.

- **Analyse :**

  **Observed :** Une publication attribuée à **Nameless511**, horodatée du **2 octobre 2026 à 00:51** selon l’heure affichée, annonce un export Odoo associé à `karamtech.ma` et `kmt.codebarre.ma`. Sa page de présentation affirme qu’une base Odoo brute comportant plus de **2 millions** d’écritures financières, des identifiants fiscaux, des identifiants en clair et l’ensemble des données personnelles des salariés a été compromise. Elle affirme également que l’organisation n’aurait pas conclu d’accord avec l’auteur. Ces déclarations restent des revendications non validées. Le message détaillé affirme par ailleurs disposer de **441 fichiers CSV** couvrant l’ensemble de l’instance, d’environ **18 GB** de données, de près de **2,08 millions** d’écritures de journal, **492 900** événements d’authentification, **207 400** commandes et **39 100** dossiers clients. Il cite aussi, sans que ces éléments soient testés, l’exposition présumée d’un secret de base de données et de jetons de session partagés.

  Cinq fichiers CSV locaux fournis, présentés comme des échantillons, ont été examinés intégralement en lecture seule : échantillons clients, salariés, coordonnées d’identité et bancaires de salariés, ventes/profits et messagerie. Ils totalisent **31 415 octets** et contiennent des catégories cohérentes avec les intitulés annoncés : identité et coordonnées, données RH, informations financières, données commerciales et messagerie. Les structures contiennent aussi des champs liés à l’authentification. Aucune valeur personnelle, bancaire, d’authentification ou secrète n’est reproduite, vérifiée ou testée.

  **Assumption :** Le logo, les domaines affichés, l’activité publique de Karamtech et la cohérence thématique des cinq échantillons soutiennent une association plausible à l’environnement commercial de Karamtech. Ils ne documentent pas que les **441 CSV**, les **18 GB**, les volumes revendiqués ou les secrets allégués proviennent d’un système compromis de l’organisation.

  **Unknown :** Le corpus source, son intégrité, le nombre réel de fichiers et d’enregistrements, les personnes uniques concernées, la validité actuelle de tout secret, mot de passe ou jeton, le système d’origine, le vecteur et la date d’accès, l’exfiltration complète, l’impact opérationnel et toute confirmation par Karamtech ou une autorité ne sont pas renseignés dans les sources consultées.

- **Périmètre et limites de l’analyse :** Les cinq échantillons ont été examinés dans leur intégralité, avec empreinte SHA-256, taille et contrôle de structure. Chaque fichier ne contient toutefois qu’un seul séparateur de ligne : les enregistrements sont concaténés dans une ligne continue. Cette anomalie empêche une reconstruction fiable des lignes, une déduplication et la validation des volumes annoncés. Aucun corpus de 441 CSV ou archive de 18 GB n’a été fourni. Les échantillons, qui contiennent des données sensibles, restent hors dépôt.

- **Évaluation des risques :** Si les éléments revendiqués sont authentiques, la combinaison de données clients, commerciales, RH, bancaires et de messagerie peut soutenir le phishing ciblé, la fraude fournisseur, l’usurpation d’identité et les fraudes de paiement. L’exposition potentielle de secrets, mots de passe ou jetons pourrait accroître le risque d’accès non autorisé et exige une rotation préventive, sans présumer qu’ils sont réels ou encore actifs.

- **Recommandations :**
  1. Préserver les journaux Odoo, IAM, bases de données, e-commerce, messagerie et intégrations afin d’établir la chronologie d’un éventuel incident.
  2. Effectuer une rotation contrôlée des secrets applicatifs, clés API, mots de passe de service, jetons et sessions ; ne jamais tester les valeurs publiées.
  3. Rechercher les exports massifs, accès privilégiés inhabituels, connexions depuis de nouvelles adresses, modifications de configuration et transferts sortants.
  4. Vérifier les données détenues sur les clients, fournisseurs et salariés, puis préparer les mesures de protection et de notification appropriées selon le périmètre établi.
  5. Renforcer les contrôles anti-fraude sur les paiements, les changements de coordonnées bancaires et les demandes d’achat ou de livraison inhabituelles.

- **Sources / Éléments de preuve :** publication de forum fournie le 8 octobre 2026 ; cinq CSV locaux fournis et analysés en lecture seule ; [site officiel de Karamtech](https://karamtech.ma/). Aucun secret, mot de passe, jeton, valeur bancaire ou donnée individuelle n’est publié.


#### 🇲🇦 Maroc - Ministère de l’Investissement, de la Convergence et de l’Évaluation des politiques publiques (MICEPP)

- **Date de publication initiale :** 2 octobre 2026 à 23:55 (horodatage affiché sur le forum ; fuseau non indiqué)
- **Acteur / Groupe :** anisanas2 (compte de forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Gouvernement / Administration / Investissement et évaluation des politiques publiques
- **Site web :** [micepp.gov.ma](https://micepp.gov.ma/)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** Medium
- **Niveau d’impact :** Level 4
- **Type de source :** Underground Forum et publications Telegram fournis à AFRINTEL

- **Description victime :** MICEPP désigne, dans les éléments disponibles, le ministère marocain de l’Investissement, de la Convergence et de l’Évaluation des politiques publiques. Son rôle institutionnel précis et les systèmes éventuellement concernés ne sont pas établis par les publications observées.

- **Analyse :**

  **Observed :** Une publication de forum attribuée au compte **anisanas2**, horodatée du **2 octobre 2026 à 23:55** selon l’heure affichée, annonce des « documents d’échantillon » et une « base de données » associés à MICEPP. Des publications Telegram fournies, datées du **2 octobre** sans année ni fuseau visibles, reprennent cette attribution. Elles affirment que plus de **150 000 dossiers** et plus de **50 000 investisseurs** seraient concernés, que le corpus dépasserait **400 GB** et qu’il serait proposé à la vente en plusieurs parties. Ces volumes, le mode d’obtention et l’existence d’une compromission restent des affirmations de l’auteur. Les publications affichent un fichier `part_1_sample.rar` de **1,6 Go** et `investors_sample_300.csv` de **26 Ko**. Ni l’archive ni le CSV n’ont été fournis localement ou examinés. Les catégories de colonnes visibles décrivent notamment des données d’identité et de contact, des références de pièce d’identité, la nationalité, l’adresse, des données administratives territoriales, ainsi que des informations d’entreprise, dont l’identifiant commun de l’entreprise (ICE). Aucun contenu individuel n’est reproduit.

  **Assumption :** Le nom, le logo institutionnel et les catégories de données affichées sont cohérents avec des procédures administratives ou des dispositifs liés à l’investissement. Cette cohérence ne documente pas que les fichiers proviennent d’un système administré par MICEPP : une copie historique, un prestataire, une autre administration, un agrégateur ou une présentation trompeuse restent possibles.

  **Unknown :** L’accès réel aux fichiers annoncés, leurs empreintes, leur structure, leur authenticité, leur actualité, le nombre de dossiers et de personnes ou organisations uniques, le système d’origine, la méthode et la date d’obtention, l’étendue d’une éventuelle exposition, l’impact opérationnel et toute confirmation par MICEPP ou une autorité ne sont pas renseignés dans les sources consultées.

- **Périmètre de l’analyse :** Analyse préliminaire fondée sur la publication et le matériel fourni ; les fichiers sources annoncés n’étaient pas disponibles. Les éléments visibles ne permettent ni de valider les volumes revendiqués, ni de confirmer l’attribution technique des données, ni d’établir une compromission.

- **Évaluation des risques :** Si les données annoncées sont authentiques, la combinaison de données d’identité, de contact, administratives et d’entreprise pourrait faciliter le phishing ciblé, l’usurpation d’identité, la fraude documentaire, l’ingénierie sociale et la fraude visant les investisseurs ou les procédures administratives. La présence alléguée d’identifiants d’entreprise et de références de pièces d’identité justifie une évaluation prioritaire du périmètre, sans présumer de la disponibilité réelle des fichiers.

- **Recommandations :**
  1. Préserver les journaux des portails, systèmes de gestion de dossiers, espaces documentaires, intégrations et comptes administratifs susceptibles de traiter des dossiers d’investissement.
  2. Rechercher les exports volumineux, accès privilégiés inhabituels, requêtes anormales, comptes de prestataires et transferts sortants autour de la période à déterminer par l’enquête.
  3. Vérifier, par des moyens autorisés, si les catégories de champs observées correspondent à des systèmes internes ou à des prestataires, sans télécharger ni manipuler les fichiers proposés par l’auteur.
  4. Évaluer le périmètre potentiel des investisseurs, entreprises et agents concernés avant toute notification, puis renforcer la détection du phishing et des fraudes documentaires ciblées.
  5. Mettre en place une vérification hors bande pour les demandes inhabituelles liées aux investissements, aux coordonnées d’entreprise ou aux procédures administratives.

- **Sources / Éléments de preuve :** publications de forum et Telegram fournies le 9 octobre 2026. Aucun lien de téléchargement, donnée individuelle, identifiant, secret ou archive n’est publié.


#### 🇿🇦 Afrique du Sud - Ampath Laboratories [Data Leak]
- **Date de publication / notification publique :** 2 octobre 2026
- **Domaine :** `ampath.co.za`
- **Acteur / Groupe :** bytetobreach (compte de publication affiché)
- **Secteur :** Santé / Laboratoires médicaux
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Description victime :** Ampath Laboratories est un réseau sud-africain de laboratoires médicaux et de services de diagnostic.
- **Analyse :** La publication du compte bytetobreach affirme que 10 bases de données sur environ 375 auraient été copiées et que l'ensemble concerné dépasserait 80 millions d'enregistrements. Elle décrit des données RH et employés, plusieurs bases de patients, des données financières, des configurations de systèmes et des composants applicatifs. Le dossier local fourni comprend des échantillons structurés analysés en lecture seule : 4 000 lignes d'employés, 5 000 lignes de patients, 1 000 dossiers Medicaid, 1 000 inscriptions de patients et 997 paiements par carte, ainsi qu'un fichier XML de 278 401 lignes structurelles. Les schémas contiennent des catégories d'identité, de contact, de santé, d'emploi, d'assurance et de paiement. Cette cohérence structurelle étaye l'existence d'un échantillon associé à Ampath, mais ne valide pas les 375 bases, le volume de 80 millions d'enregistrements, l'exhaustivité du corpus, la méthode d'accès ou l'identité réelle de l'acteur.
- **Périmètre et limites de l'analyse :** Les cinq CSV et le fichier XML disponibles ont été examinés en lecture seule, avec contrôle des types, tailles, empreintes, colonnes et volumes de lignes. L'inventaire de fichiers et les composants applicatifs ont été traités comme éléments de contexte ; aucun binaire, script, lien ou secret n'a été exécuté, testé ou publié. Les comptes, identifiants, adresses, données médicales, données financières et secrets restent hors du dépôt.
- **Évaluation des risques :** L'exposition potentielle concerne des données de santé, d'identité, de contact, d'emploi, d'assurance et de paiement. Elle pourrait faciliter l'usurpation, le phishing ciblé, la fraude documentaire, la fraude financière et le ciblage de patients ou d'employés. Aucun dossier individuel n'est reproduit.
- **Sources / Éléments de preuve :** publication et éléments visuels fournis ; échantillons locaux Ampath analysés en lecture seule. Le compte bytetobreach est conservé comme identifiant de publication ; son identité et son affiliation technique ne sont pas établies.


#### 🇪🇬 Égypte - Dar Al-Tib (`daralteb.com`) [Ransomware]
- **Date de publication initiale :** 4 octobre 2026 ; certaines sources indiquent le 2 octobre 2026
- **Domaine :** [daralteb.com](https://daralteb.com/)
- **Acteur / Groupe :** Krybit
- **Secteur :** Santé / Fertilité et procréation médicalement assistée
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 4 (potentiel)
- **Description victime :** Dar Al-Tib est un centre médical égyptien spécialisé dans le traitement de l'infertilité, la fécondation in vitro et la procréation médicalement assistée.
- **Analyse :** `daralteb.com` apparaît dans une revendication associée à Krybit en octobre 2026. Aucun échantillon, volume, communiqué de la victime, preuve de chiffrement ou preuve technique d'exfiltration n'a été identifié. Le site officiel reste accessible, ce qui ne confirme ni n'invalide la revendication.
- **Évaluation des risques :** Si la publication correspond au corpus présenté, les risques potentiels concernent des données médicales, des dossiers de patients, des informations administratives et la continuité des services. Le périmètre réel de l'exposition n'est pas précisé dans les sources consultées.
- **Sources / Éléments de preuve :** [site officiel de Dar Al-Tib](https://daralteb.com/) ; [SOCRadar](https://socradar.io/free-tools/ransomware-intelligence/victims/daralteb-com-krybit-76ff21cf) ; [Yazoul Security](https://www.yazoul.net/intel/claim/2026-10-04-dar-al-tib-ransomware-claim-by-krybit-oct-2026/). Les sources secondaires présentent le cas comme une revendication attribuée à la publication.



#### 🇨🇬 République du Congo - e-Solde (`e-solde.cg`) [Access Sale]

- **Date de publication initiale :** 2 octobre 2026 à 12:28 (horodatage affiché ; fuseau non indiqué)
- **Publication antérieure identifiée a posteriori :** 28 juin 2026 à 13:17 par le compte affiché Sensitive2025 (horodatage et fuseau tels qu'affichés)
- **Acteur / Groupe :** SensitiveDarkForum (compte affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Administration publique / Gestion de la solde
- **Site web associé :** [e-solde.cg](https://e-solde.cg/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Access Sale
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Prix revendiqué :** 110 000 USD (devise inférée du contexte de marché ; non explicitement affichée)
- **Type de source :** Publication de forum underground et échantillon de données fourni à AFRINTEL
- **Source publique :** [Note circulaire sur la plateforme e-Solde](https://lasemaineafricaine.info/wp-content/uploads/2024/04/4227.pdf)

- **Description victime :** e-solde.cg est une plateforme congolaise présentée comme un service gouvernemental de consultation des bulletins de solde et de gestion d'informations relatives aux agents publics. Une note circulaire publiée en 2024 indique que la plateforme avait été mise en production le 30 novembre 2023. La publication observée en octobre 2026 propose à la vente un « government system » associé au domaine `e-solde.cg`.

- **Analyse des échantillons fournis :**

  **Observed :** La publication suivie, datée du **2 octobre 2026**, présente e-Solde comme un système gouvernemental de la République du Congo et affiche un prix revendiqué de **110K**. Une publication antérieure portant le même domaine, le même prix et des échantillons concordants a été identifiée a posteriori le **28 juin 2026** sur un autre forum, sous le compte affiché Sensitive2025. Ces deux publications sont traitées comme une seule revendication ou exposition suivie, sans double comptabilisation. La devise n'est pas explicitement indiquée ; le montant est interprété comme **110 000 USD** uniquement comme hypothèse fondée sur la convention fréquemment utilisée dans les marchés clandestins. Le vendeur invite les intéressés à engager une transaction privée. Deux échantillons de données sont visibles dans la publication suivie et dans l'extrait fourni à AFRINTEL : un échantillon de comptes et de demandes administratives, puis un échantillon de données de paie. L'analyse porte sur les champs et les enregistrements visibles ; elle ne traite pas l'intégralité de la base revendiquée.

  **Principaux éléments observés dans l'échantillon :**

  - comptes d'utilisateurs avec identifiants, noms, adresses électroniques, numéros de téléphone, rôles applicatifs et états de validation ;
  - champs de mots de passe présents sous forme de **hashs bcrypt** commençant par `$2y$10$` ; aucun mot de passe en clair n'est reproduit ;
  - références de fichiers de profils ou de pièces justificatives ;
  - données de paie avec matricules, noms, prénoms, dates de naissance, position, sexe, catégorie d'agent et montant net ;
  - données relatives à des fonctionnaires, contractuels, policiers et membres de la force publique ;
  - dossiers de demande ou d'inscription contenant des contacts, des références de pièces d'identité, des fichiers associés et des motifs de rejet ;
  - timestamps principalement situés entre le **26 janvier et le 4 février 2026**, ainsi qu'une période de paie `202601` ;
  - les structures visibles sont cohérentes avec plusieurs tables d'une application de gestion des agents et de la solde.

  **Analyse de l'échantillon de comptes et de demandes :** Les enregistrements présentent une structure applicative avec identifiant, nom, matricule, coordonnées, statut, rôle ou agent de validation, référence de fichier et dates de création ou de mise à jour. Certains enregistrements comportent des références à des pièces d'identité et des motifs de rejet administratif. Les champs de mot de passe sont renseignés par des hashés bcrypt, ce qui montre la présence de matériel d'authentification dans l'échantillon, mais ne permet pas de déterminer si les comptes sont encore actifs ou si les hashés sont exploitables.

  **Analyse de l'échantillon de paie :** Le second extrait comporte des champs correspondant à un identifiant de ligne, un matricule, l'identité d'un agent, une date de naissance, une position administrative, le sexe, le type d'agent, un montant net, une période de paie et des timestamps. La période `202601` et les dates de création de février 2026 indiquent que l'échantillon contient des données postérieures à 2025. La présence de catégories telles que fonctionnaire, contractuel, police et force publique renforce la cohérence avec une base de gestion de la fonction publique congolaise.

  **Qualification du contenu :** Les échantillons ne sont pas de simples éléments d'interface ou de simples métadonnées : ils contiennent des enregistrements structurés avec données d'identité, coordonnées, informations professionnelles, éléments de paie, références de justificatifs et matériel d'authentification haché. Ils démontrent une exposition de données sensibles dans l'échantillon fourni, sans démontrer l'exhaustivité du jeu de données, le nombre total de personnes concernées ou l'accès interactif au système.

  **Assumption :** La combinaison du domaine `e-solde.cg`, du contexte gouvernemental congolais, des champs de paie et des catégories d'agents rend plausible l'association de l'échantillon au service e-Solde ou à un système administratif lié. L'offre de vente et la présence d'un échantillon soutiennent une qualification d'**Access Sale** avec exposition secondaire de données. Ils ne documentent pas que l'acheteur aurait obtenu un accès fonctionnel, que l'acteur contrôle encore le système ou que l'ensemble de la base provient directement de l'infrastructure officielle.

  **Unknown :** Le vecteur d'accès, la chronologie technique de l’accès, le volume total, le nombre de personnes concernées, l'existence d'un accès interactif, la validité des comptes ou des hashés, la confirmation de la devise en USD, l'identité réelle du vendeur et toute confirmation officielle par l'administration congolaise ne sont pas renseignés dans les sources consultées. Le montant « 110K » est une revendication commerciale et ne constitue pas un volume d'enregistrements confirmé.

- **Périmètre et limites de l'analyse :** Analyse limitée à la publication et à l'extrait de données fourni dans l'échange ; le fichier source complet n'a pas été fourni. Les valeurs personnelles, matricules, coordonnées, références de fichiers et hashés ne sont pas reproduits. Aucun accès n'a été testé, aucun lien de contact n'a été suivi et aucune tentative de cassage ou de réutilisation de hash n'a été effectuée.
- **Évaluation des risques :** Exposition potentielle de données d'agents publics, de paie, d'identité et de validation administrative ; risques de fraude salariale, usurpation d'identité, phishing ciblé, extorsion et compromission secondaire de comptes. Le niveau 4 reflète le caractère gouvernemental et financier du service ainsi que la présence d'éléments d'authentification.
- **Recommandations SOC/CTI :** Réinitialiser les accès potentiellement exposés et invalider les sessions ; renouveler les secrets applicatifs et contrôler les hashés de mots de passe ; rechercher les exports massifs et accès administratifs inhabituels ; vérifier les journaux de l'application et de la base ; contrôler les fichiers et documents associés ; auditer les rôles et comptes de validation ; préserver les preuves ; ne pas acheter, tester ou télécharger l'accès revendiqué.
- **Décision de comptage :** Incident conservé dans le corpus d'octobre et rattaché au suivi d'octobre, car la publication du 2 octobre constitue la première observation AFRINTEL. La publication antérieure du 28 juin est documentée comme une découverte rétrospective du même corpus. L'événement reste compté comme **un seul incident**. Le type principal reste `Access Sale`; l'exposition de données est un effet secondaire observé.


### 5 octobre 2026
#### 🇲🇦 Maroc - Tera.ma / Sté Tera.ma SARL

- **Date de publication initiale :** 5 octobre 2026 à 19:41 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** Nameless511 (compte de forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Technologie / Distribution et vente au détail de matériel informatique
- **Site web :** [tera.ma](https://www.tera.ma/) (domaine affiché dans la publication ; site marocain de commerce informatique identifié)
- **Statut :** Data Fully Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** Very High
- **Niveau d’impact :** Level 4
- **Type de source :** Underground Forum - Publication fournie à AFRINTEL + corpus local analysé en lecture seule

- **Description victime :** Tera.ma est une société marocaine de distribution et de vente au détail de matériel informatique, associée à Témara / Rabat. Les éléments disponibles sont cohérents avec une activité de ventes, d’inventaire, de commerce en ligne, de comptabilité et de gestion de partenaires.

- **Analyse :**

  **Observed :** Une publication attribuée à **Nameless511**, datée du **5 octobre 2026 à 19:41** selon l’horodatage affiché, annonce une « publication finale » d’un export Odoo associé à Tera.ma. L’auteur affirme que le corpus a été extrait le **27 septembre 2025**, qu’il comporte **2,3 GB**, **282 CSV**, **19 595 clients**, **69 197 commandes**, **124 088 écritures comptables** et **124 comptes internes**. La date d’extraction et les déclarations relatives à une négociation restent des affirmations de l’auteur. Le corpus local fourni contient **8 140 fichiers** pour **2 389 358 436 octets**, dont **282 CSV** totalisant **1 392 426 551 octets**, **3 693 PDF**, **3 152 images JPEG/JFIF/JPG**, **413 PNG**, des fichiers audio et une vidéo. Les comptes de lignes, hors en-tête, concordent avec les chiffres affichés pour `account_move.csv` (**124 088**), `res_partner.csv` (**19 595**) et `sale_order.csv` (**69 197**). Les CSV représentent au total environ **21,7 millions de lignes**, en incluant les en-têtes.

  Les structures examinées couvrent notamment écritures et factures, commandes, partenaires, inventaire, mouvements de stock, messagerie et journaux applicatifs. Le corpus inclut également des pièces jointes présentées comme factures, scans, contrats, justificatifs de livraison et images de pièces d’identité. Les noms de fichiers, structures Odoo et références à des intégrations de commerce et de logistique sont cohérents entre eux. Aucune donnée individuelle, référence bancaire, document, fichier audio ou lien de téléchargement n’est reproduit ici.

  **Assumption :** La concordance entre les chiffres publiés et les trois exports clés, la composition du corpus, les structures Odoo et les documents associés fournit une preuve structurelle très forte d’un jeu de données opérationnel lié à Tera.ma. Elle ne permet pas, à elle seule, d’établir le vecteur d’accès, l’identité de l’auteur, la date réelle d’extraction, la portée hors corpus, ni une confirmation officielle de l’incident.

  **Unknown :** Les systèmes d’origine et affectés, la méthode et la durée de l’accès, l’exhaustivité de la base de production, le nombre de personnes et organisations uniques, la validité actuelle des comptes ou intégrations, tout chiffrement, toute interruption opérationnelle, l’existence et le résultat d’une négociation, ainsi que toute confirmation par Tera.ma ou une autorité ne sont pas renseignés dans les sources consultées.

- **Périmètre de l’analyse :** L’intégralité des **8 140 fichiers** fournis a été inventoriée en lecture seule. Les **282 CSV** ont été comptés ; des contrôles structurels complets ont été effectués sur les principaux exports annoncés. Le corpus contient des données personnelles et commerciales sensibles : il demeure hors dépôt, sans extraction ni reproduction de contenu. Les sources consultées ne précisent pas l'absence de doublons ni le nombre de personnes uniques.

- **Évaluation des risques :** La publication comprend, selon le corpus examiné, des données de clients, fournisseurs et salariés, des factures et commandes, des informations bancaires ou de paiement, des journaux applicatifs, des documents commerciaux et des pièces d’identité. Si elles sont exploitées, ces données peuvent soutenir l’usurpation d’identité, la fraude au changement de coordonnées bancaires, de faux ordres de paiement, le phishing ciblé, l’atteinte à la vie privée et l’espionnage commercial. Le risque est renforcé par la présence de documents et d’éléments liés à des intégrations tierces.

- **Recommandations :**
  1. Isoler et préserver les preuves sur les environnements Odoo, bases de données, applications e-commerce, messagerie, intégrations et sauvegardes ; conserver les journaux utiles à une investigation forensique.
  2. Révoquer de façon contrôlée les sessions, clés API, jetons, comptes techniques et accès de prestataires susceptibles d’être exposés ; rechercher toute réutilisation anormale.
  3. Examiner les exports massifs, accès administratifs, requêtes inhabituelles, tâches planifiées et transferts sortants avant et après le 27 septembre 2025, sans considérer cette date comme confirmée.
  4. Prioriser les mesures de protection des clients, partenaires et salariés potentiellement concernés ; préparer les obligations de notification applicables après établissement du périmètre.
  5. Renforcer immédiatement les contrôles contre la fraude au paiement, la modification de RIB et l’usurpation de fournisseurs ; imposer une vérification hors bande pour toute demande financière inhabituelle.

- **Sources / Éléments de preuve :** publication de forum fournie le 8 octobre 2026 ; corpus local Tera.ma fourni et analysé en lecture seule. Les liens de téléchargement criminels ne sont ni suivis ni publiés.


#### 🇲🇦 Maroc - Université Cadi Ayyad (UCA)

- **Date de publication initiale :** 5 octobre 2026 à 02:25 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** Nameless511 (compte de forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Éducation / Enseignement supérieur public
- **Site web :** [uca.ma](https://www.uca.ma/)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d’impact :** Level 4
- **Type de source :** Underground Forum - Publication et échantillon fournis à AFRINTEL

- **Description victime :** L’Université Cadi Ayyad est une université publique marocaine établie à Marrakech et active dans plusieurs disciplines et établissements de la région Marrakech-Safi.

- **Analyse :**

  **Observed :** Une publication attribuée à **Nameless511**, horodatée du **5 octobre 2026 à 02:25** selon l’heure affichée, est intitulée comme une fuite de l’Université Cadi Ayyad et annonce **270 enregistrements gratuits**. Le message décrit des catégories comprenant nom en français et arabe, CIN, CNE, identifiant APOGÉE, adresse e-mail, numéro de téléphone, date et lieu de naissance, genre, filière, état d’inscription et photos. L’échantillon structuré fourni contient ces catégories et des références à des adresses institutionnelles `@uca.ac.ma`, à des identifiants APOGÉE, à des parcours académiques et à des images encodées. Les données individuelles, les photos et les métadonnées de fichiers ne sont pas reproduites.

  **Assumption :** La cohérence entre l’identité de l’université, son domaine officiel, les identifiants APOGÉE, les adresses institutionnelles et les informations académiques soutient fortement l’attribution de l’échantillon à l’écosystème UCA. Elle ne documente pas que les données proviennent directement d’un système administré par l’université : une copie historique, un prestataire ou une autre source restent possibles.

  **Unknown :** Le fichier source complet, son empreinte, le nombre réel d’enregistrements et de personnes uniques, l’authenticité et l’actualité des dossiers, le système d’origine, la méthode et la date d’obtention, l’étendue au-delà des **270** enregistrements revendiqués, toute exfiltration complète, l’impact opérationnel et une confirmation de l’UCA ou d’une autorité ne sont pas renseignés dans les sources consultées.

- **Périmètre de l’analyse :** Analyse limitée à la publication, au matériel fourni et au contenu structuré visible dans l’échantillon ; aucune archive source ni aucun lien de téléchargement n’a été ouvert. Le contenu comprend des données personnelles hautement sensibles et des photos : il n’est pas reconstruit ni conservé dans le dépôt. L’échantillon ne permet pas de valider les **270** enregistrements annoncés ni d’évaluer les doublons.

- **Évaluation des risques :** Si elles sont authentiques, les données observées peuvent faciliter l’usurpation d’identité, la fraude documentaire, l’hameçonnage ciblé contre les étudiants et les personnels, le ciblage de comptes universitaires et l’exploitation abusive de procédures administratives. La présence de photos et la combinaison d’identifiants civils et académiques aggravent le risque de fraude et d’atteinte à la vie privée.

- **Recommandations :**
  1. Préserver les journaux des systèmes APOGÉE, admissions, identité, annuaires, stockage de photos et comptes administratifs.
  2. Examiner les exports massifs, accès privilégiés inhabituels, comptes de prestataires et transferts sortants de données étudiantes.
  3. Évaluer le périmètre des étudiants, diplômés et personnels potentiellement concernés sans réutiliser les valeurs publiées.
  4. Renforcer la protection des comptes universitaires et surveiller le phishing, la fraude documentaire et les tentatives d’usurpation ciblant la communauté UCA.
  5. Appliquer les procédures de notification et de protection appropriées après établissement du périmètre réel.

- **Sources / Éléments de preuve :** publication de forum et échantillon structuré fournis le 8 octobre 2026 ; [site officiel de l’UCA](https://www.uca.ma/). Aucun lien criminel, identifiant national, adresse e-mail, numéro, photo ou autre donnée individuelle n’est publié.


#### 🇿🇦 Afrique du Sud - TechExchange (`techexchange.co.za`)

- **Date de publication initiale :** 5 octobre 2026 à 15:34 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** Sensitive2025 (compte de forum affiché ; identité non établie)
- **Secteur :** Commerce / E-commerce / Téléphonie mobile
- **Site web :** [techexchange.co.za](https://techexchange.co.za/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High pour l'existence de la publication et la cohérence du domaine ; Medium pour l'attribution de l'ensemble du corpus à TechExchange
- **Niveau d'impact :** Level 4 (potentiel)
- **Type de source :** Publication de forum avec échantillon CSV visible et extrait structuré fourni à AFRINTEL

- **Description victime :** TechExchange est présenté comme une entreprise sud-africaine spécialisée dans la vente de téléphones mobiles neufs, d'occasion, reconditionnés et de démonstration.
- **Analyse :** La publication annonce la vente de fichiers de sauvegarde du site web, présentés comme environ **6 000 fichiers CSV pour 1 Go** et couvrant la période **2014-2022**. L'en-tête et l'extrait structurés visibles correspondent à un export de commandes e-commerce comprenant notamment les identifiants de commande, dates de commande et de paiement, statuts, montants, devise, méthode de paiement, identifiants de transaction, comptes clients, adresses électroniques, téléphones, adresses de facturation et de livraison, informations géographiques, adresse IP, agent utilisateur, articles commandés, taxes, remises et notes de commande. Les champs visibles sont cohérents avec une plateforme de commerce en ligne et plusieurs éléments renvoient à l'Afrique du Sud et à la devise ZAR. Les données individuelles, coordonnées, identifiants de transaction, adresses IP et références de commande ne sont pas reproduits.
- **Observed :** La publication est datée du 5 octobre 2026 à 15:34 selon l'horodatage affiché ; le domaine `techexchange.co.za`, la description commerciale, l'en-tête CSV et les enregistrements structurés sont visibles dans le matériel fourni.
- **Assumption :** Si l'échantillon est authentique et provient des systèmes de TechExchange, l'exposition pourrait concerner des clients, commandes, paiements et livraisons, avec des risques de fraude au paiement, phishing et usurpation. La cohérence structurelle ne valide pas à elle seule l'origine technique ni l'exhaustivité du corpus.
- **Unknown :** Le vecteur d'accès, la date d'extraction, le nombre réel de fichiers et d'enregistrements, l'exhaustivité de la sauvegarde, les systèmes sources, la validité actuelle des données, l'exposition de mots de passe ou de tokens, l'identité réelle de l'acteur et toute confirmation officielle restent inconnus.
- **Périmètre et limites de l'analyse :** Analyse détaillée de la publication, des éléments visuels et de l'extrait structuré fournis ; le fichier source complet, son empreinte et les 6 000 fichiers annoncés n'étaient pas disponibles. Aucun lien de téléchargement ou contact criminel n'a été suivi et aucune donnée personnelle brute n'est conservée dans le dépôt.
- **Évaluation des risques :** L'exposition potentielle de données de commande, de contact, de livraison et de paiement pourrait faciliter la fraude transactionnelle, les faux remboursements, le phishing ciblé, l'usurpation de clients ou de fournisseurs et l'atteinte à la vie privée.
- **Sources / Éléments de preuve :** éléments visuels et extrait structurés fournis à AFRINTEL ; publication du forum attribuée au compte Sensitive2025. Les données brutes et liens de téléchargement restent hors du dépôt.


#### 🇿🇦 Afrique du Sud - Thrive Online Group (`thriveonlinegroup.com`)

- **Date de publication initiale :** 5 octobre 2026 à 19:46 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** Sorb (compte de forum affiché ; identité et affiliation non établies)
- **Secteur :** Technologie / Marketing numérique
- **Site web associé :** `thriveonlinegroup.com`
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High pour l'existence de la publication et des extraits visibles ; Medium pour l'attribution de l'ensemble des données à Thrive Online Group
- **Niveau d'impact :** Level 4 (potentiel)
- **Type de source :** Publication de forum et extraits CSV visibles fournis à AFRINTEL

- **Description victime :** Thrive Online Group est présenté comme une organisation sud-africaine active dans le marketing numérique ciblé.
- **Analyse :** La publication attribuée au compte **Sorb** annonce environ **17 millions de lignes**, plus de **10 millions de données personnelles sans doublon** et un prix de **1 000 USD**. Ces volumes et la proposition commerciale restent des revendications de l'auteur. Les deux extraits CSV visibles présentent des champs cohérents avec des données de particuliers sud-africains : identifiants utilisateur ou SMS, noms, numéros de téléphone, identifiants sud-africains, adresses électroniques, province, code postal, indicateur d'opposition et code de campagne. Le second extrait comporte notamment des numéros mobiles et des identifiants RSA. Aucune valeur individuelle n'est reproduite dans le dépôt.
- **Observed :** Publication visible datée du **5 octobre 2026 à 19:46** selon l'horodatage affiché ; domaine `thriveonlinegroup.com` ; extraits structurés montrant des champs d'identité, de contact et d'identification sud-africaine ; prix affiché de **1 000 USD**.
- **Assumption :** Si les extraits sont authentiques et proviennent de Thrive Online Group ou d'un prestataire associé, l'exposition pourrait faciliter le phishing, l'usurpation d'identité, la fraude téléphonique et le ciblage de campagnes SMS. La cohérence des champs ne valide pas l'origine technique ni les volumes revendiqués.
- **Unknown :** Le vecteur et la date d'accès, le système source, le nombre réel de personnes uniques, l'exhaustivité du corpus, la validité actuelle des données, l'existence d'une exfiltration, l'identité réelle du vendeur et toute confirmation de Thrive Online Group ou d'une autorité restent inconnus.
- **Périmètre et limites de l'analyse :** Analyse limitée à la publication, aux éléments visuels et aux extraits CSV visibles fournis ; les fichiers sources complets, leurs empreintes et les **17 millions de lignes** annoncées n'étaient pas disponibles. Aucun lien de téléchargement ou contact criminel n'a été suivi. Les données personnelles brutes restent hors dépôt.
- **Évaluation des risques :** Si les données sont authentiques, la combinaison de coordonnées, d'identifiants sud-africains et de données de campagne pourrait soutenir l'hameçonnage ciblé, l'usurpation, les fraudes par téléphone ou SMS et le recoupement d'identités.
- **Recommandations SOC/CTI :** Préserver les journaux des applications marketing, CRM, bases de données, comptes de service et intégrations SMS ; rechercher les exports massifs et accès privilégiés inhabituels ; vérifier les prestataires et campagnes associés ; surveiller les domaines, numéros et messages usurpant l'organisation ; ne pas acheter, télécharger ni tester les données proposées.
- **Sources / Éléments de preuve :** éléments visuels et extraits structurés fournis à AFRINTEL ; publication de forum attribuée au compte Sorb. Aucun identifiant, numéro, adresse électronique ou lien de marché criminel n'est publié.


#### 🇿🇦 Afrique du Sud - Lawyers for Human Rights [System Intrusion]
- **Date de publication de l'avis de sécurité :** 15 octobre 2026
- **Domaine officiel :** [lhr.org.za](https://www.lhr.org.za/)
- **Acteur / Groupe :** Non établi
- **Secteur :** ONG / Droits humains / Services juridiques
- **Statut :** Incident Confirmed by Victim
- **Type d'incident :** System Intrusion
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Description victime :** Lawyers for Human Rights est une organisation sud-africaine fournissant des services et une assistance juridiques dans le domaine des droits humains.
- **Analyse :** Dans son avis de sécurité du 15 octobre 2026, LHR indique qu'une base de données hébergée par un prestataire tiers a fait l'objet d'un accès non autorisé le 5 octobre. L'enquête de LHR conclut qu'un tiers a consulté et téléchargé des informations. L'environnement a été sécurisé, une investigation ouverte et les autorités ainsi que les personnes potentiellement concernées ont été notifiées.
- **Données concernées ou potentiellement affectées :** noms, numéros d'identité sud-africains, numéros de passeport ou de permis de réfugié/demandeur d'asile, adresses, téléphones, e-mails, dates de naissance, genre, nationalité, informations professionnelles et contractuelles, informations de locataires et de baux, dossiers de clients et bénéficiaires, informations d'organisations, documents et correspondances liés à des dossiers juridiques, ainsi que des données relatives aux partenaires, donateurs, salariés, prestataires et locataires.
- **Nombre de personnes et volume :** Non établis.
- **Évaluation des risques :** Les données juridiques, d'identité, de contact et relatives à des personnes vulnérables peuvent entraîner des risques élevés d'usurpation, de phishing, de fraude documentaire, de ciblage et d'intimidation. Aucun rançongiciel, chiffrement ou publication sur un site de fuite n'est établi.
- **Action SOC/CTI :** Préserver et rapprocher les journaux du prestataire, de la base, des comptes d'administration et des passerelles sortantes autour du 5 octobre ; révoquer les accès et secrets partagés avec le tiers ; contrôler les environnements utilisant les mêmes identités ; surveiller les faux échanges juridiques et demandes de documents ; privilégier la validation hors bande avec LHR.
- **Sources / Éléments de preuve :** [avis officiel de LHR du 15 octobre 2026](https://www.lhr.org.za/lhr-news/important-notice-regarding-a-security-incident/) ; [index des actualités LHR](https://www.lhr.org.za/lhr-news/). L'étendue exacte du corpus et le nombre de personnes concernées restent en cours d'évaluation.


#### 🇪🇬 Égypte - Millensys (`millensys.com`) [Ransomware]
- **Date de publication initiale :** 5 octobre 2026
- **Domaine :** [millensys.com](https://www.millensys.com/)
- **Acteur / Groupe :** MedUSlocker
- **Secteur :** Logiciels de santé / Technologies de l'information
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3 (potentiel)
- **Description victime :** MILLENSYS est une entreprise égyptienne de logiciels et de solutions informatiques pour les établissements de santé, notamment les systèmes d'imagerie, les dossiers médicaux et la télémédecine.
- **Analyse :** La victime apparaît dans une revendication associée à MedUSlocker. Aucun échantillon, volume, preuve de chiffrement, exfiltration ou confirmation de MILLENSYS n'a été identifié.
- **Évaluation des risques :** Une revendication authentique pourrait concerner des logiciels, des environnements de santé, des données de clients ou des systèmes d'imagerie. Aucun de ces impacts n'est établi.
- **Sources / Éléments de preuve :** [site officiel de MILLENSYS](https://www.millensys.com/about) ; publication ransomware extraite du corpus fourni à AFRINTEL.


### 6 octobre 2026
#### 🇪🇬 Égypte - Beni Suef Technological University [Ransomware]
- **Date de publication initiale :** 6 octobre 2026
- **Domaine institutionnel associé dans la source :** `bsut.edu.eg`
- **Site officiel vérifié :** [btu.edu.eg](https://btu.edu.eg/en/home/)
- **Domaine institutionnel vérifié :** `btu.edu.eg`
- **Acteur / Groupe :** UmBra
- **Secteur :** Enseignement supérieur / Technologies
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3 (potentiel)
- **Description victime :** Beni Suef Technological University est une université technologique publique égyptienne proposant notamment des formations en technologies industrielles, informatique, mécatronique et énergie.
- **Analyse :** La victime apparaît dans une revendication associée à UmBra. Aucun échantillon, volume, preuve de chiffrement, exfiltration ou confirmation de l'université n'a été identifié.
- **Évaluation des risques :** Les risques potentiels concernent les systèmes administratifs, les comptes étudiants, les plateformes pédagogiques et les données personnelles. Aucun périmètre compromis n'est établi.
- **Sources / Éléments de preuve :** [site officiel de Beni Suef Technological University](https://btu.edu.eg/en/home/) ; [portail institutionnel égyptien](https://bani-suef-tu.mohesr.gov.eg/) ; publication ransomware extraite du corpus fourni à AFRINTEL.


### 3 octobre 2026
#### 🇲🇦 Maroc - NextLevel PC

- **Date de publication initiale :** 3 octobre 2026 à 12:00 (heure affichée ; fuseau non indiqué)
- **Publication ultérieure :** 7 octobre 2026 à 01:41, avec annonce de diffusion gratuite de la base complète (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** Nameless511 (compte de forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Commerce électronique / Matériel informatique et gaming
- **Site web :** [nextlevelpc.ma](https://nextlevelpc.ma/) (domaine affiché dans la publication ; site marocain de vente de matériel informatique identifié)
- **Statut :** Data Fully Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** Very High
- **Niveau d’impact :** Level 4
- **Type de source :** Underground Forum - Publication et échantillon fournis à AFRINTEL

- **Description victime :** NextLevel PC est un site marocain de commerce électronique spécialisé, selon les éléments disponibles, dans le matériel informatique et le gaming. Le domaine et la relation technique avec un système compromis ne sont pas confirmés indépendamment.

- **Analyse :**

  **Observed :** Une première publication attribuée à **Nameless511**, datée du **3 octobre 2026 à 12:00** selon l’horodatage visible, présente la base de NextLevel PC et décrit l’entreprise, ses volumes commerciaux et les catégories de données concernées. Une publication ultérieure du **7 octobre 2026 à 01:41** annonce la diffusion gratuite de la « base complète » après une période que l’auteur décrit comme **72 heures sans réponse**. L’auteur revendique **52 545 comptes clients**, **60 262 adresses de livraison**, **47 653 commandes**, **11 comptes internes**, **14 160 règles de panier/remises** et un historique de transactions de **122,9 millions MAD**. L’intégralité du corpus local fourni et analysé contient **huit CSV**, pour **30 556 090 octets**, et confirme exactement les cinq premiers décomptes : `customers.csv` (**52 545** lignes), `addresses.csv` (**60 262**), `orders.csv` (**47 653**), `employees.csv` (**11**) et `cart_rules.csv` (**14 160**). Les **47 653 commandes** totalisent **122 865 604,60** dans le champ de paiement, un montant cohérent avec le chiffre de **122,9 millions MAD** publié par l’auteur. La devise est attribuée à la publication ; elle n’est pas validée indépendamment par ce calcul.

  Le corpus couvre comptes clients, adresses de livraison, commandes, détails de commande, produits, règles de remise, messages et comptes internes. Il contient **69 957** lignes de détail de commande et **4 168** messages. Les dates observées s’étendent de **mai 2021** à **novembre 2026**, cette dernière borne incluant des dates de fin de règles de remise. Les fichiers clients comportent des champs de coordonnées, de préférences, de mot de passe et de clé de session. Les **52 545** valeurs de mot de passe sont renseignées ; **42 743** suivent un format commençant par `$2`, tandis que les autres utilisent un format non identifié. Ces valeurs n’ont été ni reproduites, ni testées, ni soumises à une tentative de cassage. Aucune valeur individuelle, adresse e-mail, numéro, chaîne d’authentification ou donnée de commande n’est publiée.

  **Assumption :** La concordance exacte entre les volumes annoncés et les huit exports, la structure cohérente des tables de commerce électronique et le logo/domaine affichés fournissent une preuve structurelle très forte d’un corpus opérationnel lié à NextLevel PC. Elle ne permet pas, à elle seule, d’établir le vecteur d’accès, la date d’extraction, une compromission officielle ou l’exhaustivité de systèmes non inclus dans les fichiers fournis.

  **Unknown :** L’algorithme et la validité de toutes les valeurs d’authentification, le nombre de personnes uniques  -  distinct des comptes, adresses ou commandes  -  la fraîcheur des coordonnées, l’origine technique, la méthode et la date d’obtention, l’étendue hors corpus, l’impact opérationnel, toute négociation et toute confirmation par l’organisation ou une autorité ne sont pas renseignés dans les sources consultées.

- **Périmètre de l’analyse :** Les huit CSV locaux ont été examinés dans leur intégralité en lecture seule, avec calcul des empreintes SHA-256, contrôle du schéma, des largeurs de lignes, des doublons exacts et des plages de dates. Chaque fichier conserve une largeur de ligne constante et aucun doublon exact au niveau de la ligne n’a été observé. Ces contrôles ne valident pas l’absence de doublons métier, l’identité de chaque personne ni l’exhaustivité de la base de production. Aucun lien criminel n’a été ouvert et aucune donnée personnelle ou chaîne d’authentification n’est conservée dans le dépôt.

- **Évaluation des risques :** Si elles sont authentiques, la combinaison de coordonnées, adresses de livraison, historiques de commande et valeurs d’authentification peut faciliter le phishing ciblé, les tentatives de réutilisation d’identifiants, l’usurpation de client, la fraude à la livraison et l’ingénierie sociale. Les informations transactionnelles alléguées peuvent également soutenir des fraudes commerciales ciblées.

- **Recommandations :**
  1. Préserver les journaux de la boutique, des bases de données, de l’authentification, des paiements, des intégrations logistiques et des comptes d’administration.
  2. Identifier les comptes potentiellement concernés, réinitialiser les mots de passe lorsque l’enquête le justifie et invalider les sessions et clés applicatives exposées potentiellement.
  3. Vérifier les paramètres de hachage des mots de passe, les contrôles de limitation, l’authentification multifacteur des administrateurs et les accès API.
  4. Renforcer la surveillance des modifications d’adresse de livraison, des demandes de remboursement, des tentatives de prise de compte et des campagnes de phishing visant les clients.
  5. Établir le périmètre avant toute notification, sans utiliser les données publiées pour contacter ou authentifier des personnes.

- **Sources / Éléments de preuve :** publication et échantillon visible fournis le 8 octobre 2026. Aucun lien criminel, identifiant, mot de passe haché, clé de session ni donnée individuelle n’est publié.


#### 🇪🇹 Éthiopie - Ministère de la Santé (`moh.gov.et`) [Data Leak]

- **Date de publication initiale :** 7 octobre 2026 à 16:51 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** Individual (compte affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Santé publique / Administration gouvernementale
- **Site web :** [moh.gov.et](https://moh.gov.et/)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d’impact :** Level 4
- **Type de source :** Publication de forum, matériel et échantillon local fournis à AFRINTEL

- **Description victime :** Le ministère éthiopien de la Santé est l’administration nationale chargée de la politique sanitaire, de la coordination des programmes de santé et de la supervision de structures et de professionnels du secteur en Éthiopie.

- **Analyse :**

  **Observed :** Une publication attribuée au compte **Individual**, datée du **7 octobre 2026 à 16:51** selon l’horodatage visible, présente `moh.gov.et` sous le titre « Master Facilities », avec une revendication de **4 millions d’enregistrements** et **13 Go**, annoncée comme une « PART2 ». Le matériel fourni présente des cartes d’identité numériques éthiopiennes, une carte de résident d’Addis-Abeba et une carte liée au Bureau de santé d’Oromia. Les informations visibles comprennent des catégories d’identité et de santé particulièrement sensibles, notamment photographie, nom complet, date de naissance, nationalité, sexe, numéro d’enregistrement et groupe sanguin. Aucune valeur individuelle n’est reproduite ici.

  L’échantillon local `facility 83463 clean csv.txt` a été examiné intégralement en lecture seule. Il s’agit d’un fichier ASCII de **13 269 octets**, avec **une seule ligne physique** et **1 442 champs séparés par des virgules** ; il ne comporte pas de ligne d’en-tête exploitable. Les marqueurs agrégés comprennent **67 chaînes ressemblant à des adresses email**, **111 valeurs ressemblant à des numéros de téléphone**, **61 UUID**, **77 dates**, **3 URL** et des références à des domaines éthiopiens, dont `orhb.gov.et`. Le contenu comporte aussi des marqueurs relatifs à des établissements, hôpitaux, cliniques et médecins. Ces occurrences ne représentent pas des personnes uniques et ne permettent pas de reconstituer de manière fiable le schéma original.

  Le matériel fourni et le texte local présentent également des structures liées à des comptes utilisateurs, rôles, identités, établissements, professionnels de santé et champs d’authentification. Les valeurs sensibles n’ont été ni testées, ni publiées, ni utilisées pour tenter un accès. Les documents d’identité non masqués fournis sont traités comme éléments de preuve locaux et aucune donnée faciale ou identifiante n’est intégrée au dépôt.

  **Assumption :** La concordance entre le domaine `moh.gov.et`, les références à des structures sanitaires éthiopiennes, les cartes officielles visibles et le schéma de données compatible avec une plateforme sanitaire soutient fortement l’association de l’échantillon avec un environnement du ministère ou d’un organisme de santé lié. Elle ne permet pas d’établir que le système du ministère a été compromis directement, ni que toutes les données proviennent du même environnement.

  **Unknown :** Les revendications de 4 millions d’enregistrements et 13 Go, l’existence et le contenu de la partie 1, l’exhaustivité du corpus, le nombre de personnes uniques, la date d’extraction, le vecteur d’accès, l’authenticité de chaque document, la validité actuelle des identifiants ou secrets, l’impact opérationnel et toute confirmation du ministère ou d’une autorité ne sont pas renseignés dans les sources consultées.

- **Périmètre et limites de l’analyse :** L’échantillon texte local a été analysé dans son intégralité, avec empreinte SHA-256, taille, nombre de lignes, largeur apparente et comptage agrégé de marqueurs. Le matériel fourni a été examiné sans transcription des données personnelles. Le fichier n’est pas un export CSV normalisé : les champs ne peuvent pas être associés de façon fiable à des colonnes et les décomptes de motifs ne constituent pas des décomptes d’individus. Le corpus complet annoncé n’était pas disponible.
- **Risques :** Usurpation d’identité, fraude documentaire, phishing ciblé, compromission de comptes, atteinte à la confidentialité médicale, ciblage de professionnels de santé et exploitation de données relatives aux établissements sanitaires.
- **Recommandations SOC / CTI :** Préserver les journaux IAM, API, bases de données, exports et téléchargements ; révoquer les secrets ou sessions potentiellement exposés après validation ; renforcer MFA et contrôle des comptes privilégiés ; vérifier les accès aux systèmes d’identité et de santé ; rechercher les exports massifs et transferts sortants ; protéger les copies d’identité et appliquer les procédures de notification prévues par la réglementation applicable.
- **Évaluation AFRINTEL :** Publication observée et échantillon sensible analysé ; attribution à un environnement sanitaire éthiopien fortement plausible ; compromission directe du ministère, volume global et méthode d’acquisition non documenté dans les sources publiquess.
- **Sources / Éléments de preuve :** publication du forum et matériel fourni le 30 octobre 2026 ; échantillon local analysé en lecture seule. Aucun identifiant national, nom, adresse email, numéro, photographie ou secret n’est publié dans cette fiche.


### 7 octobre 2026
#### 🇪🇬 Égypte - SANAtech Global Solutions [Ransomware]
- **Date de publication :** 7 octobre 2026
- **Acteur / Groupe :** UmBra (attribution revendiquée uniquement)
- **Secteur :** Technologies / Services numériques
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** SANAtech Global Solutions est présentée comme une entreprise égyptienne de technologies et de services numériques.
- **Analyse :** La victime apparaît sur une source associée à UmBra. Aucun échantillon exploitable ni communiqué de la victime n'a été identifié. Intrusion, exfiltration, chiffrement et interruption de service ne sont pas établis.


### 8 octobre 2026
#### 🇪🇬 Égypte - FSE, Cairo University [Ransomware]
- **Date de publication initiale :** 8 octobre 2026
- **Domaine institutionnel :** [cu.edu.eg](https://cu.edu.eg/)
- **Acteur / Groupe :** UmBra
- **Secteur :** Enseignement supérieur / Université
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3 (potentiel)
- **Description victime :** FSE est présentée dans le corpus source comme une entité de la Cairo University relevant de la formation et de l'enseignement supérieur.
- **Analyse :** La victime apparaît dans une revendication associée à UmBra. Aucun échantillon, volume, système concerné, preuve de chiffrement, exfiltration ou confirmation de Cairo University n'a été identifié.
- **Évaluation des risques :** Les risques potentiels concernent les plateformes universitaires, les données d'étudiants et les documents administratifs. Ils ne sont pas établis par la publication seule.
- **Sources / Éléments de preuve :** [site officiel de Cairo University](https://cu.edu.eg/) ; publication ransomware extraite du corpus fourni à AFRINTEL.


### 9 octobre 2026
#### 🇲🇦 Maroc - Conseil national de la presse (CNP)

- **Date de publication initiale :** 9 octobre 2026 à 03:20 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** Nameless511 (compte de forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Institution publique indépendante / Régulation de la presse
- **Site web :** [cnp.press.ma](https://cnp.press.ma/fr/home-fr/)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** Medium
- **Niveau d’impact :** Level 4
- **Type de source :** Underground Forum - Publication fournie à AFRINTEL

- **Description victime :** Le Conseil national de la presse est une institution nationale indépendante chargée notamment de l’autorégulation du secteur de la presse et de l’édition, ainsi que de l’attribution de la carte de presse professionnelle au Maroc.

- **Analyse :**

  **Observed :** Une publication de forum attribuée au compte **Nameless511**, horodatée du **9 octobre 2026 à 03:20** selon l’heure affichée, désigne le Conseil national de la presse (CNP) comme cible au Maroc. L’auteur affirme détenir **39 000 enregistrements** et propose à la vente une « base complète ». Il annonce un échantillon de **30 PDF** présenté comme contenant des documents réels. Les catégories de données énumérées comprennent les noms complets, numéros CIN, adresses personnelles, numéros de téléphone, adresses e-mail, employeurs, qualifications académiques, numéros de carte de presse et dates de renouvellement. Les fichiers annoncés et les liens associés n’ont pas été ouverts, téléchargés ni examinés. Les volumes, la nature exacte des documents, leur provenance et toute compromission restent des affirmations de l’auteur. Aucune donnée individuelle n’est reproduite.

  **Assumption :** Le nom de l’institution, le logo affiché et les catégories de données citées sont cohérents avec les missions du CNP, notamment les procédures liées à la carte de presse professionnelle. Cette cohérence ne documente pas que les données proviennent d’un système exploité par le CNP : une copie historique, un prestataire, une autre source ou une présentation trompeuse restent possibles.

  **Unknown :** L’accès réel à l’échantillon ou à la base annoncée, les empreintes et la structure des fichiers, leur authenticité et leur actualité, le nombre réel de personnes uniques concernées, le système d’origine, la méthode et la date d’obtention, l’étendue de l’exposition, l’impact opérationnel et toute confirmation par le CNP ou une autorité ne sont pas renseignés dans les sources consultées.

- **Périmètre de l’analyse :** Analyse préliminaire fondée sur la publication fournie ; les PDF et la base annoncés n’étaient pas disponibles localement et n’ont pas été examinés. Cette analyse ne permet pas de valider les **39 000 enregistrements** revendiqués, l’authenticité des documents ni l’existence d’une intrusion.

- **Évaluation des risques :** Si les éléments annoncés sont authentiques, la combinaison de coordonnées, de documents d’identité, d’informations professionnelles et de données de carte de presse pourrait exposer des journalistes et d’autres professionnels à l’usurpation d’identité, au phishing ciblé, à l’ingénierie sociale, au doxxing et à la fraude documentaire. L’exposition potentielle de personnes exerçant dans la presse peut aussi accroître les risques de ciblage et de harcèlement.

- **Recommandations :**
  1. Préserver les journaux des applications de gestion des cartes de presse, portails de dépôt, systèmes documentaires, annuaires et comptes administratifs.
  2. Rechercher les exports volumineux, consultations inhabituelles de dossiers, accès privilégiés anormaux, comptes de prestataires et transferts sortants.
  3. Évaluer, par des moyens autorisés, si les catégories de données publiées correspondent aux systèmes du CNP, sans ouvrir ni télécharger les fichiers proposés par l’auteur.
  4. Préparer des mesures de protection et de communication pour les personnes potentiellement concernées après établissement du périmètre réel.
  5. Renforcer la détection des tentatives de phishing, d’usurpation, de fraude documentaire et de harcèlement ciblant les titulaires ou demandeurs de cartes de presse.

- **Sources / Éléments de preuve :** publication de forum fournie le 9 octobre 2026 ; [missions et attributions du CNP](https://cnp.press.ma/fr/2020/05/06/missions-et-pouvoirs-du-conseil-national-de-la-presse/). Aucun lien de téléchargement, document, donnée individuelle ou contact de l’auteur n’est publié.


#### 🇲🇦 Maroc - Ministère des Habous et des Affaires islamiques

- **Date de publication initiale :** 9 octobre 2026 à 03:44 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** Nameless511 (compte de forum affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Gouvernement / Administration / Affaires religieuses
- **Site web officiel :** [habous.gov.ma](https://www.habous.gov.ma/fr/)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d’impact :** Level 4
- **Type de source :** Underground Forum - Publication, matériel et corpus local fournis à AFRINTEL

- **Description victime :** Le Ministère des Habous et des Affaires islamiques est une institution publique marocaine responsable notamment des affaires religieuses et de l’administration des biens habous. Son site officiel est [habous.gov.ma](https://www.habous.gov.ma/fr/).

- **Analyse :**

  **Observed :** Une publication attribuée à **Nameless511**, horodatée du **9 octobre 2026 à 03:44** selon l’heure affichée, annonce une « base complète de candidats » liée à un concours de recrutement d’ingénieurs d’État de premier grade. L’auteur revendique environ **109 000 lignes** au format CSV, XLSX et pièces jointes PDF. Les catégories affichées comprennent notamment des noms en arabe et en caractères latins, CIN, date et lieu de naissance, genre, adresse, coordonnées, diplômes, spécialités, établissements émetteurs, état du dossier, motif de rejet, centre d’examen et documents téléversés. Le corpus local fourni comprend **33 fichiers XLSX** et un CSV, pour environ **44,2 Mo**. L’analyse de la structure XML de l’ensemble des XLSX relève **109 673 lignes**, dont **109 640 lignes de données** en supposant une ligne d’en-tête par fichier : un volume cohérent avec la revendication. L’échantillon visible présente une structure cohérente avec des dossiers de candidature. Aucune donnée individuelle, pièce d’identité ou document n’est reproduit.

  **Assumption :** La cohérence entre l’intitulé du concours, les champs administratifs et la structure des fichiers soutient un lien avec un processus de recrutement public marocain attribué au ministère. Elle ne documente pas que les fichiers proviennent directement d’un système administré par le ministère, ni que l’ensemble du volume revendiqué a été exfiltré.

  **Unknown :** Le nombre réel de candidats, le nombre de personnes uniques, la couverture exacte du corpus, le système source, la méthode et la date d’obtention, l’authenticité et l’actualité des fichiers, la présence effective de toutes les pièces jointes annoncées, l’impact opérationnel et toute confirmation officielle ne sont pas renseignés dans les sources consultées.

- **Périmètre de l’analyse :** Analyse limitée à la publication, au matériel et à un corpus local fourni. Le volume d’environ **109 000** annoncé par l’auteur est cohérent avec le comptage structurel AFRINTEL des XLSX, mais celui-ci ne confirme ni le nombre de personnes uniques ni l’exhaustivité du corpus. Les données hautement sensibles observées ne sont ni reconstruites, ni conservées dans le dépôt.

- **Évaluation des risques :** Si elles sont authentiques, les données peuvent permettre l’usurpation d’identité, le phishing ciblé contre les candidats, la fraude documentaire, l’exploitation abusive d’informations sur les candidatures et l’atteinte à la vie privée à grande échelle.

- **Recommandations :**
  1. Préserver les journaux des plateformes de recrutement, de dépôt de dossiers, de stockage documentaire et des comptes administratifs.
  2. Rechercher les exports massifs, accès privilégiés inhabituels et transferts sortants de données liés aux concours concernés.
  3. Établir le périmètre réel des candidats potentiellement affectés sans exploiter les valeurs publiées.
  4. Renforcer la protection des comptes, le contrôle des accès aux documents et la détection du phishing ciblant les candidats.
  5. Appliquer les procédures de notification et de protection appropriées après validation de l’incident et de son périmètre.

- **Sources / Éléments de preuve :** publication de forum, échantillon et corpus local fournis le 9 octobre 2026. Aucun lien criminel, identifiant national, adresse, numéro, e-mail, document ou autre donnée individuelle n’est publié.
- **Source institutionnelle :** [site officiel du Ministère des Habous et des Affaires islamiques](https://www.habous.gov.ma/fr/)


### 10 octobre 2026
#### 🇪🇬 Égypte - Helwan University (HITU) [Ransomware]
- **Date de publication initiale :** 10 octobre 2026
- **Domaine :** [helwan.edu.eg](https://www.helwan.edu.eg/)
- **Acteur / Groupe :** UmBra
- **Secteur :** Enseignement supérieur / Université
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3 (potentiel)
- **Description victime :** Helwan University est une université publique égyptienne située au Caire et dans la région du Grand Caire.
- **Analyse :** La victime apparaît dans une revendication associée à UmBra. Aucun échantillon, volume, preuve de chiffrement, exfiltration ou confirmation de l'université n'a été identifié.
- **Évaluation des risques :** Les risques potentiels concernent les systèmes administratifs, les comptes étudiants, les plateformes d'enseignement et les données personnelles. Aucun système affecté n'est établi.
- **Sources / Éléments de preuve :** [site officiel de Helwan University](https://www.helwan.edu.eg/) ; publication ransomware extraite du corpus fourni à AFRINTEL.


### 11 octobre 2026
#### 🇲🇦 Maroc - Decathlon Maroc

- **Secteur :** Commerce de détail / Distribution / E-commerce
- **Victime :** Decathlon Maroc
- **Site web :** https://www.decathlon.ma/
- **Date de publication initiale :** 11 octobre 2026
- **Date de détection AFRINTEL :** 11 octobre 2026
- **Type d'incident :** Data Leak / Fuite présumée de données personnelles
- **Acteur / Groupe :** Nameless511
- **Volume revendiqué :** Plus de 24 438 commandes clients
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium


##### Description de l'incident

Un acteur malveillant utilisant le pseudonyme Nameless511a publié sur le forum DarkForums une revendication de fuite de données concernant Decathlon Maroc, enseigne spécialisée dans la distribution d'articles de sport.

L'acteur affirme avoir divulgué une base contenant plus de 24 438 commandes clients associées à plusieurs magasins et canaux de distribution de Decathlon au Maroc.

Les magasins et entités mentionnés dans la revendication sont :

- Decathlon Kénitra
- Decathlon Corniche
- Decathlon Rabat
- Decathlon Ecom
- Decathlon Marina
- Decathlon Derb Ghallef

Selon l'acteur, les informations exposées comprennent :

- Noms et prénoms des clients
- Numéros de téléphone marocains
- Adresses de livraison
- Coordonnées GPS (latitude et longitude)
- Identifiants et références de commandes
- Montants et dates de livraison
- Modes de paiement
- Instructions de livraison
- Commentaires et notes opérationnelles
- Informations relatives aux montages, retours et réparations

##### Éléments observés

Un échantillon de données présenté dans la publication a été examiné dans le cadre de l'investigation CTI.

L'échantillon reconstitué comprend 522 enregistrements et 30 colonnes, avec des informations structurées relatives aux commandes et aux opérations de livraison.

Les enregistrements observés comportent notamment :

- Des références de commandes
- Des identifiants de magasins et dépôts
- Des statuts de livraison
- Des informations clients
- Des adresses et coordonnées GPS
- Des montants de commandes
- Des informations de paiement
- Des commentaires logistiques

Les dates observées dans l'échantillon s'étendent
du 29 septembre 2021 au 5 janvier 2022.

Des fichiers Excel supplémentaires ont également été transmis via un lien partagé dans la publication de l'acteur.

Leur appartenance au même jeu de données et leur relation exacte avec Decathlon Maroc restent à confirmer.

##### Analyse CTI

La structure de l'échantillon présente des caractéristiques compatibles avec un export d'une application de gestion des commandes, des tournées ou des livraisons.

Ces éléments renforcent la crédibilité de l'existence de données opérationnelles associées à Decathlon Maroc.

Toutefois, ils ne permettent pas de déterminer si l'exposition résulte :

- D'une compromission directe de Decathlon Maroc ;
- D'une compromission d'un prestataire logistique ;
- D'un accès non autorisé à une plateforme tierce ;
- D'une divulgation ultérieure d'une ancienne extraction.

Le volume de 24 438 commandes reste une affirmation de l'acteur et n'a pas été vérifié indépendamment.

La date de publication ne doit pas être assimilée à la chronologie technique de l’accès initiale.

##### Risques potentiels

- Phishing et smishing ciblés
- Vishing et usurpation d'identité
- Fraudes à la livraison
- Ingénierie sociale
- Exploitation des historiques de commandes
- Atteintes à la vie privée liées aux coordonnées GPS
- Ciblage géographique des personnes concernées

##### Recommandations SOC/CTI

- Vérifier l'origine et l'authenticité des données publiées.
- Identifier les systèmes ou prestataires ayant accès
  aux informations de commande et de livraison.
- Rechercher les accès suspects et les exports massifs.
- Examiner les journaux d'accès des plateformes logistiques.
- Vérifier les habilitations des comptes internes et tiers.
- Évaluer les obligations de notification applicables.
- Informer les personnes concernées lorsque cela est requis.
- Sensibiliser les clients aux tentatives de fraude
  utilisant les informations de livraison.

##### Conclusion

La publication de Nameless511 constitue une revendication crédible nécessitant une investigation complémentaire.

L'échantillon présente des données structurées cohérentes avec des opérations commerciales et logistiques associées à Decathlon Maroc.

L'authenticité complète de la base, le volume réel des données exposées et l'origine de leur extraction restent à confirmer.

Aucune compromission directe de l'infrastructure de Decathlon Maroc n'est établie à ce stade.


#### 🇲🇦 Maroc - CNESTEN [Ransomware]
- **Date de publication initiale :** 11 octobre 2026
- **Domaine institutionnel :** [cnesten.org.ma](https://www.cnesten.org.ma/)
- **Acteur / Groupe :** Qilin
- **Secteur :** Recherche nucléaire / Science et technologie
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 4 (potentiel)
- **Description victime :** Le CNESTEN est un établissement public marocain chargé de la recherche et des applications dans le domaine de l'énergie, des sciences et des technologies nucléaires.
- **Analyse :** Le CNESTEN apparaît dans une revendication associée à Qilin. La ligne source ne fournit pas de description de données ni de preuve technique. Aucun échantillon, volume, chiffrement, exfiltration ou confirmation du CNESTEN n'a été identifié.
- **Évaluation des risques :** Une revendication authentique pourrait concerner des données scientifiques, administratives ou opérationnelles sensibles. Aucun impact sur une installation nucléaire ou sur la sûreté n'est établi.
- **Sources / Éléments de preuve :** [CNESTEN](https://www.cnesten.org.ma/storage/2023/06/Brochure-CNESTEN-Eng.pdf) ; publication ransomware extraite du corpus fourni à AFRINTEL.


### 12 octobre 2026
#### 🇲🇦 Maroc - Eurogate Tanger (`eurogate-tanger.com`)

- **Date de publication initiale :** 12 octobre 2026 à 13:55:54 (horodatage affiché ; fuseau non indiqué)
- **Date de divulgation observée :** 19 octobre 2026 à 13:27 UTC (premier lot annoncé)
- **Acteur / Groupe :** N0n (nom affiché par la source ; identité et affiliation attribuée à la publication)
- **Secteur :** Transport maritime / opérations de terminal conteneurs
- **Site web :** [eurogate-tanger.com](https://www.eurogate-tanger.com/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4 (potentiel)
- **Type de source :** Site de suivi ransomware et archive publiée par l'acteur

- **Description victime :** Eurogate Tanger est un opérateur de terminal conteneurs au Maroc. Les systèmes associés à `eurogate-tanger.com` sont présentés dans la publication comme liés à des correspondances commerciales, des documents opérationnels et des fichiers de travail internes.

- **Analyse :**

  **Observed :** La fiche observée indique Eurogate Tanger, le Maroc, le secteur du transport maritime, le groupe N0n et une mention `NOT PAID – EXPOSED`. Le champ « Published data » est indiqué comme `N/D`. L'archive locale fournie sous le nom `eurogate_tanger.com-leak.zip` est intacte lors du test de lecture : **355 fichiers**, **373 065 003 octets** non compressés, **373 150 373 octets** pour l'archive, sans chiffrement ZIP. Les fichiers sont regroupés sous `eurogate-tanger.com` et comprennent notamment des documents DOCX, XLS/XLSX, PDF, MSG, PPTX, ODS, EDI, XML, journaux/traces, SQL, archives et fichiers techniques. Le README inclus décrit explicitement un **premier lot** et annonce d'éventuels lots ultérieurs.

  Une analyse statique en lecture seule a couvert les **354 fichiers extraits sous le domaine** : empreintes, types réels, structures et contenu textuel/XML lorsqu'extractible. Elle comprend notamment **98 DOCX, 86 XLSX, 11 XLS, 5 PPTX, 2 ODS, 22 PDF, 10 MSG, 32 TRC, 32 TRM, 19 RAR, 5 ZIP, 1 JAR, 1 classe Java, ainsi que des fichiers EDI/XML/WSDL/SQL et des journaux**. L'analyse XML des XLSX représente environ **652 708 éléments de lignes** et **13 686 923 éléments de cellules** ; ces valeurs sont structurelles et ne représentent pas directement le nombre de personnes ou d'opérations uniques.

  Le contenu textuel et XML fait apparaître de manière répétée des références cohérentes à **EGT, Eurogate, Tanger, OPUS Terminal, terminal, port, conteneurs, navires, cargaison, reefers, gates, grues, yard, voyages, camions et mouvements opérationnels**. Les DOCX et XLSX contiennent également des références à des notes de version, correctifs, scripts SQL, traces et échanges techniques associés à cet environnement. Les archives RAR, ZIP et le JAR ont été inventoriés sans exécution ; leurs membres et tailles ont été contrôlés.

  Aucun fichier n'a été exécuté. Aucun marqueur de macro VBA n'a été détecté dans les conteneurs Office inspectés. Les PDF et MSG ont fait l'objet d'une analyse statique de chaînes et de métadonnées, sans rendu ni interprétation complète des objets incorporés. Des marqueurs d'adresses e-mail sont présents dans plusieurs fichiers textuels ; aucune donnée individuelle n'est reproduite dans ce rapport.

  **Assumption :** Le nom du domaine dans l'arborescence, le nom de l'organisation, le secteur indiqué et la nature des fichiers annoncés sont cohérents avec une exposition de données internes d'Eurogate Tanger. Cette cohérence soutient l'attribution de l'archive à la victime, mais ne documente pas la méthode d'accès, la compromission initiale, l'exhaustivité des données ni l'absence d'un prestataire ou d'un environnement tiers.

  **Unknown :** La date et le vecteur de compromission, le volume total réellement exfiltré, l'identité et les capacités réelles de N0n, l'exhaustivité du premier lot, l'impact opérationnel, l'existence d'une confirmation par Eurogate Tanger ou une autorité, et le contenu exact des documents ne sont pas renseignés dans les sources consultées.

- **Empreinte de l'archive analysée :** SHA-256 `87bb4495b774c21919af26daf9b3ab807e57f78d7fad5879d0176bd9df28c891`.
- **Périmètre et limites de l'analyse :** Les 354 fichiers extraits sous le domaine ont été couverts par une analyse statique du type réel, des empreintes, de la structure et du contenu textuel/XML lorsqu'extractible. Cette méthode ne déchiffre pas les fichiers protégés, ne rend pas visuellement chaque page et ne valide pas chaque objet incorporé. Elle ne constitue pas une confirmation officielle de l'incident. L'archive reste hors du dépôt AFRINTEL.
- **Évaluation des risques :** L'exposition potentielle de documents opérationnels, de données de navires et conteneurs, de configurations ou notes de version, de scripts et de traces techniques pourrait faciliter l'ingénierie sociale, la fraude documentaire, le ciblage d'employés, la préparation d'une perturbation des opérations portuaires ou l'identification de dépendances applicatives. Le niveau 4 reflète le caractère potentiellement critique de cet environnement ; une perturbation réelle ou un accès aux systèmes de contrôle n'est pas établi.
- **Sources / Éléments de preuve :** fiche publique observée le 20 octobre 2026 ; archive locale fournie pour analyse ; aucune adresse onion, donnée personnelle brute ou valeur individuelle n'est publiée.


#### 🇿🇦 Afrique du Sud - Aeroklas Duys / Duys Engineering Group (`aeroklasduys.co.za`) [Ransomware]
- **Date de publication initiale :** 12 octobre 2026
- **Domaine :** [aeroklasduys.co.za](https://aeroklasduys.co.za/)
- **Acteur / Groupe :** Deadlock
- **Secteur :** Industrie automobile / Ingénierie et fabrication
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3 (potentiel)
- **Description victime :** Aeroklas Duys est une entreprise sud-africaine liée au groupe Duys Engineering, active dans la fabrication automobile, l'ingénierie mécanique et les services industriels.
- **Analyse :** Aeroklas Duys / Duys Engineering Group apparaît dans une revendication associée à Deadlock. L'identité de l'entreprise et son implantation sud-africaine sont corroborées, mais aucun échantillon, volume, preuve de chiffrement, exfiltration ou confirmation de la victime n'a été identifié.
- **Évaluation des risques :** Les risques potentiels concernent les données industrielles, les opérations de fabrication, les fournisseurs et les systèmes de production. Aucun impact opérationnel n'est établi.
- **Sources / Éléments de preuve :** [Duys Engineering Group](https://duysgroup.com/) ; [registre fournisseur Aeroklas Duys](https://cloud.procureactiv.co.za/procurement/suppliers/view/aeroklas) ; [DeXpose](https://www.dexpose.io/deadlock-ransomware-strikes-aeroklas-duys-in-south-africa/).


### 14 octobre 2026
#### 🇿🇦 Afrique du Sud - Europ Assistance South Africa / AZOZA [Ransomware]
- **Date portée par la publication :** 14 octobre 2026
- **Domaines :** `azoza.co.za` ; ancien domaine `europassistance.co.za`
- **Acteur / Groupe :** The Gentlemen
- **Secteur :** Assistance et administration de prestations d'assurance
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** AZOZA est associée à l'ancienne activité sud-africaine d'Europ Assistance et intervient dans les services d'assistance et la gestion de prestations.
- **Analyse :** L'ancienne identité Europ Assistance South Africa est apparue sur un site de fuite associé à The Gentlemen. Aucun échantillon n'a été analysé ; intrusion, exfiltration, chiffrement et impact ne sont pas confirmés.


### 15 octobre 2026
#### 🇪🇬 Égypte - Luxor Company for Drinking Water and Sanitation [Ransomware]
- **Date de publication :** 15 octobre 2026
- **Domaine :** `lcww.com.eg`
- **Acteur / Groupe :** LockBit 5.0
- **Secteur :** Eau potable et assainissement
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 4 (potentiel)
- **Description victime :** Luxor Company for Drinking Water and Sanitation est une entreprise égyptienne chargée de services d'eau potable et d'assainissement.
- **Analyse :** La victime a été publiée sur une source attribuée à LockBit 5.0. Aucun échantillon, volume ou communiqué officiel n'a été analysé. Les sources disponibles ne décrivent pas de compromission, d'exfiltration, de chiffrement ou d'atteinte aux services d'eau.


### 18 octobre 2026
#### 🇷🇼 Rwanda - Ministère de la Santé [Data Leak]

- **Date de publication initiale :** 18 octobre 2026 à 22:07 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** Lenken (compte affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Santé publique / Administration gouvernementale
- **Site web associé :** [moh.gov.rw](https://moh.gov.rw/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Type de source :** Publication de forum et corpus CSV local associé
- **Sources publiques :** [Gouvernement du Rwanda - Ministry of Health](https://www.gov.rw/government/institutions/ministries) | [Ministry of Health Rwanda](https://moh.gov.rw/about/overview)

- **Description victime :** Le ministère rwandais de la Santé est une institution gouvernementale responsable de la politique et de la coordination du secteur de la santé au Rwanda. La publication attribuée au compte Lenken présente une base de données comme « leaked » et disponible au téléchargement. Le ministère est identifié comme institution officielle par le portail du Gouvernement du Rwanda.

- **Analyse approfondie du corpus :**

  **Observed :** La publication affiche un volume revendiqué de **5,7 Go compressés** et **375 tables**. Le corpus local associé comprend **375 fichiers CSV** totalisant **6 050 914 271 octets** et **42 509 228 lignes physiques, en-têtes compris**. Ce total est un inventaire de retours à la ligne : certains champs contiennent des retours intégrés, de sorte que le nombre de lignes physiques ne doit pas être interprété comme un nombre de personnes ou d'enregistrements logiques. Par exemple, `userinfo.csv` comporte **9 776 lignes physiques**, mais **9 509 enregistrements CSV parsés** sans ligne malformée. La concordance entre le nombre de tables, le volume annoncé et le corpus local constitue un élément de corroboration structurelle important. Le fichier téléchargé depuis la publication n'a pas été récupéré directement ; l'identité cryptographique exacte entre l'archive annoncée et le corpus local n'est donc pas établie.

  **Principaux éléments observés :**

  - `userinfo.csv` contient **9 509 comptes utilisateurs** ; **9 106** lignes ont un champ de mot de passe renseigné, **27** un champ `secret`, et **8 072** une adresse e-mail ;
  - `api_token.csv` contient **40 entrées** ; `userkeyjsonvalue.csv` contient **23 812 enregistrements** liés à des valeurs de clés utilisateur ;
  - les données d'identité comprennent également des champs de téléphone, date de naissance, nationalité, employeur, éducation, dernier accès et état des comptes ;
  - `trackedentityattributevalueaudit.csv` contient **4 503 344 lignes d'audit** et `datavalueaudit.csv` **3 211 053 lignes d'audit** ;
  - `trackedentityprogramowner.csv` contient **10 202 305 relations** entre entités suivies et programmes ;
  - `programmessage.csv` contient **4 452 109 messages** ; les tables de messages et de canaux associés indiquent une capacité importante de notification et de communication ;
  - les exports d'événements et d'analytique comportent des structures compatibles avec des données de santé, d'établissements, de programmes et de mesures ;
  - les champs et valeurs analysés contiennent des marqueurs relatifs aux patients, à la santé, aux maladies, aux vaccinations, aux établissements, aux unités administratives, aux audits et aux comptes ;
  - **33 fichiers CSV sont vides** et aucun octet nul n'a été détecté dans le corpus lors du balayage global.

  Les indicateurs de contenu ont été calculés sur l'ensemble des fichiers en lecture séquentielle : environ **4,6 millions de lignes** contiennent des marqueurs de santé, **218 336** des marqueurs d'identité, **46 427** des marqueurs d'audit, **38 816** des marqueurs financiers et **796 202** des marqueurs administratifs. Ces chiffres sont des indicateurs agrégés de présence et ne représentent pas des individus uniques ni des dossiers médicaux uniques.

  Les champs de mot de passe observés sont renseignés sous forme de valeurs hachées dans les enregistrements visibles ; aucune tentative de cassage, d'authentification ou de réutilisation n'a été effectuée. Les secrets, tokens, coordonnées, identifiants et données de santé n'ont pas été reproduits.

  **Assumption :** La cohérence entre la publication, le nombre de tables, le volume annoncé et les structures locales rend plausible l'association du corpus au système d'information du ministère ou d'un service sanitaire rattaché. Les noms de tables et les relations observées sont compatibles avec une plateforme de gestion de données sanitaires. Cette compatibilité ne documente pas à elle seule l'accès initial, l'exfiltration par Lenken, l'exhaustivité du corpus ou l'absence d'un prestataire.

  **Unknown :** Le vecteur d'accès, la chronologie technique de l’accès, l'identité réelle de l'acteur, les comptes effectivement utilisés, l'exhaustivité des données, la présence de dossiers médicaux complets, l'impact opérationnel et toute confirmation officielle du ministère ne sont pas renseignés dans les sources consultées. La présence de hachages, secrets ou tokens dans une copie ne documente pas qu'ils sont encore valides.

- **Périmètre et limites de l'analyse :** Les **375 fichiers** ont été parcourus en lecture seule et en flux pour l'inventaire, le comptage des lignes physiques et la recherche agrégée de marqueurs de contenu. Les tables à plus fort impact ont fait l'objet d'un parsing CSV détaillé avec distinction entre lignes physiques et enregistrements logiques. Les indicateurs textuels sont des signaux de tri et non une classification sémantique de chaque cellule. Aucun fichier n'a été exécuté, aucun lien de téléchargement n'a été suivi et aucun secret, hachage, token ou dossier individuel n'est publié. L'analyse ne constitue pas une confirmation officielle de l'incident.
- **Évaluation des risques :** L'exposition potentielle de comptes administratifs, de données d'identité, de données sanitaires, d'historiques d'audit et de mécanismes de notification pourrait faciliter la fraude, le phishing ciblé, l'usurpation de comptes, l'extorsion, le ciblage de personnels de santé et l'atteinte à la confidentialité des patients. Le niveau 4 reflète la combinaison d'une victime gouvernementale de santé, de données potentiellement sensibles et d'éléments d'accès ; une perturbation opérationnelle réelle n'est pas établie.
- **Recommandations SOC/CTI :** Révoquer et renouveler les tokens, secrets et sessions potentiellement exposés ; imposer la rotation des mots de passe et la MFA ; rechercher les exports massifs, accès administratifs inhabituels et transferts sortants ; vérifier l'intégrité des sauvegardes et des configurations ; auditer les rôles et privilèges ; préserver les journaux ; évaluer rapidement les catégories de données de santé concernées ; coordonner la réponse avec l'autorité rwandaise compétente ; ne pas télécharger ni redistribuer l'archive publique.
- **Décision de comptage :** Incident ajouté au corpus d'octobre et comptabilisé comme **nouvel incident d'octobre**, sous réserve de la clôture mensuelle et de la validation statistique finale.
- **Manifeste local :** `/tmp/afrintel-evidence/afr-2026-10-rwanda-moh/evidence_manifest.json` ; les données brutes restent hors du dépôt.


#### 🇪🇬 Égypte - WE Academy / Telecom Egypt [Data Leak]
- **Date de publication :** 18 octobre 2026
- **Domaine :** `te.eg`
- **Acteur / Groupe :** N0n
- **Secteur :** Formation professionnelle / Télécommunications
- **Statut :** Claim - Unverified
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** WE Academy est une entité de formation associée à Telecom Egypt, opérateur égyptien de télécommunications.
- **Analyse :** L'acteur revendique des dossiers d'apprenants, supports, projets, examens et une base de formations. Aucun échantillon n'a été analysé. Le lien institutionnel est plausible, mais aucun accès au cœur du réseau télécom ou à la facturation n'est établi.


### 20 octobre 2026
#### 🇲🇿 Mozambique - Procuradoria-Geral da República (PGR) [Data Leak]

- **Date de publication initiale :** 20 octobre 2026 à 04:29 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** Kazu (compte affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Administration publique / Justice et ministère public
- **Site web :** [pgr.gov.mz](https://www.pgr.gov.mz/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Effet revendiqué :** Exposition et vente alléguées d'une sauvegarde du système public de justice
- **Volume revendiqué :** 22 GB et 158 511 fichiers ; chiffres attribué à la publications
- **Prix revendiqué :** Make an offer
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Type de source :** Publication de forum underground et échantillons locaux fournis à AFRINTEL

- **Description victime :** La Procuradoria-Geral da República (PGR) est le ministère public du Mozambique. L'institution exerce des fonctions liées à la légalité, à la poursuite des infractions et à l'administration de la justice. Le portail officiel de la PGR publie des informations institutionnelles, juridiques, administratives et judiciaires.

- **Analyse :**

  **Observed :** Une publication attribuée au compte **Kazu**, horodatée du **20 octobre 2026 à 04:29** selon l'heure affichée, propose à la vente un « Public Justice System » associé à la PGR Mozambique et au domaine `pgr.gov.mz`. L'auteur revendique **22 GB** et **158 511 fichiers**. Le corpus local fourni contient **262 fichiers** pour **75 941 802 octets** : **180 JSON**, **71 PDF**, **9 courriels EML**, un fichier DOC et une image JPG.

  Les 180 JSON sont lisibles et présentent tous une structure d'objet comportant **22 clés** ; leurs valeurs individuelles ne sont pas publiées. Les 71 PDF ont été contrôlés en lecture seule et totalisent **117 pages**. Les 9 messages EML contiennent chacun des métadonnées d'expéditeur, de destinataire, de date et d'objet. La combinaison de données structurées, de documents PDF et de messages électroniques est compatible avec une sauvegarde applicative ou documentaire d'un environnement administratif et judiciaire. Ces 262 fichiers ne valident pas le volume revendiqué de 22 GB ni le total de 158 511 fichiers.

  **Assumption :** La correspondance entre le nom de la PGR, le domaine officiel mozambicain, l'identité visuelle institutionnelle et la structure du corpus rend l'attribution au périmètre de la PGR plausible. La nature des fichiers est compatible avec des documents administratifs, juridiques ou de gestion du ministère public. Cette cohérence ne documente pas que l'acteur a compromis l'infrastructure de la PGR ni que l'échantillon représente l'intégralité du système.

  **Unknown :** Le vecteur d'accès, les systèmes affectés, la chronologie technique de l’accès, l'origine technique des fichiers, le nombre de dossiers et de personnes uniques, la présence de doublons, l'exhaustivité, la sensibilité juridique exacte des documents, l'impact opérationnel et toute confirmation officielle ne sont pas renseignés dans les sources consultées.

- **Périmètre et limites de l'analyse :** Les 262 fichiers ont été inventoriés en lecture seule. Les JSON, PDF et EML ont fait l'objet de contrôles structurels ; aucun document individuel, message, nom, adresse ou élément de procédure n'est reproduit. Aucun script, lien criminel ou contenu distant n'a été exécuté ou suivi. L'analyse confirme la composition de l'échantillon fourni, mais pas l'accès initial, l'exfiltration complète ni la compromission officielle.
- **Risques :** Exposition de dossiers judiciaires ou administratifs, atteinte à la confidentialité des personnes impliquées dans des procédures, phishing ciblé, fraude documentaire, intimidation de témoins ou de personnels et exploitation d'informations sensibles relatives à l'administration de la justice.
- **Recommandations SOC / CTI :** Préserver les journaux des portails, systèmes documentaires, messageries et comptes administratifs ; rechercher les exports massifs et téléchargements anormaux ; contrôler les accès aux dossiers judiciaires ; révoquer les sessions et secrets potentiellement exposés ; vérifier l'intégrité des sauvegardes ; coordonner la réponse avec les autorités mozambicaines compétentes ; ne pas télécharger ni redistribuer de données supplémentaires.
- **Évaluation AFRINTEL :** Publication observée ; échantillon local fourni et analysé ; attribution à la PGR plausible ; structure documentaire cohérente ; volume global et exhaustivité attribué à la publications ; accès non autorisé et exfiltration non documenté dans les sources publiquess ; confirmation officielle non observée.


#### 🇲🇬 Madagascar - `staging.sso.gov.mg` (attribution revendiquée)

- **Date de publication initiale :** 20 octobre 2026 à 05:14 (horodatage affiché ; fuseau non indiqué)
- **Date de début des échanges :** lundi 19 octobre 2026, selon la chronologie fournie ; heure non précisée
- **Acteur / Groupe :** List1 (compte affiché dans la publication ; identité et affiliation non établies)
- **Secteur :** Gouvernement / Identité numérique et authentification
- **Service web revendiqué :** `staging.sso.gov.mg`
- **Statut :** Claim - Unverified
- **Type d'incident :** Access Sale
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4 (potentiel)
- **Type de source :** Forum underground, échanges directs et matériel fourni à AFRINTEL

- **Description victime :** `staging.sso.gov.mg` est présenté comme un environnement de mise en scène ou de préproduction lié à un service d'identité numérique malgache. La relation opérationnelle exacte avec l'administration concernée n'est pas établie indépendamment.
- **Analyse :** Le post affiché le **20 octobre 2026 à 05:14** annonce la vente d'un « admin access » à `staging.sso.gov.mg`. Les échanges fournis indiquent un prix annoncé de **450 USD** et une affirmation d'accès administrateur. Le matériel présente une interface de type Keycloak avec plusieurs realms et une liste d'utilisateurs partiellement masquée. Aucun identifiant, mot de passe ou secret n'est reproduit ; aucun accès n'a été testé. Au cours du même échange, le vendeur a proposé séparément l'accès à `e-koragna.gov.mg`, traité dans une fiche distincte.
- **Évaluation analytique :** Le domaine malgache, l'interface présentée et la cohérence entre la publication et le matériel fourni soutiennent l'existence d'une offre d'accès apparente à un environnement d'administration. La réalité, la légitimité, la validité et l'étendue de cet accès restent indéterminées.
- **Éléments non établis :** méthode d'obtention, chronologie technique, étendue des privilèges, persistance, exposition de données, transaction et confirmation par le propriétaire ou une autorité.
- **Périmètre et limites de l'analyse :** Analyse fondée sur la publication, les échanges et le matériel fourni ; les systèmes, comptes et identifiants n'ont pas été testés. Les données personnelles et identifiants de session restent hors du dépôt.
- **Évaluation des risques :** Si l'accès était valide, un compte administrateur pourrait permettre la modification de realms, clients, rôles ou comptes et faciliter une prise de contrôle de services dépendants.
- **Décision de comptage :** Fiche comptabilisée comme un incident `Access Sale` distinct couvrant exclusivement `staging.sso.gov.mg`.
- **Sources / Éléments de preuve :** publication du forum fournie le 23 octobre 2026 et horodatée au 20 octobre 2026 ; échanges et éléments Keycloak fournis à AFRINTEL. Les coordonnées, identifiants de session, secrets et données personnelles ne sont pas publiés.

#### 🇲🇬 Madagascar - `e-koragna.gov.mg` (attribution revendiquée)

- **Date de publication initiale :** 20 octobre 2026 à 05:14 ; offre distincte visible dans l'échange ultérieur à 14:08 (horodatages affichés ; fuseaux non indiqués)
- **Acteur / Groupe :** List1 (compte affiché dans la publication ; identité et affiliation non établies)
- **Secteur :** Gouvernement / Identité numérique et services publics
- **Service web revendiqué :** `e-koragna.gov.mg`
- **Statut :** Claim - Unverified
- **Type d'incident :** Access Sale
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4 (potentiel)
- **Type de source :** Échange direct associé à une publication de forum et matériel fourni à AFRINTEL

- **Description victime :** **e-Koragna** est une plateforme de gestion des plaintes liée au projet PRODIGY de gouvernance numérique et de gestion de l'identité à Madagascar. Les informations publiques la rattachent à l'**Unité de Gouvernance Digitale (UGD)** ([présentation publique d'e-Koragna](https://torolalana.gov.mg/fr/services/e-koragna-mecanisme-de-gestion-de-plaintes/) ; [site de l'UGD](https://digital.gov.mg/)).
- **Analyse :** Après l'annonce de vente d'un accès administrateur à `staging.sso.gov.mg`, le vendeur a proposé `e-koragna.gov.mg` comme accès supplémentaire au cours de l'échange fourni. Le prix annoncé pour l'offre était de **450 USD**. Le matériel associé présente une interface de type Keycloak ; aucun identifiant, mot de passe ou secret n'est reproduit et aucun accès n'a été testé.
- **Évaluation analytique :** Le rattachement public d'e-Koragna à l'UGD/PRODIGY, le domaine malgache et la cohérence de l'échange soutiennent l'existence d'une offre d'accès apparente visant ce service. La réalité, la légitimité, la validité et l'étendue de l'accès restent indéterminées.
- **Éléments non établis :** méthode d'obtention, chronologie technique, étendue des privilèges, persistance, exposition de données, transaction et confirmation par le propriétaire ou une autorité.
- **Périmètre et limites de l'analyse :** Analyse fondée sur la publication, l'échange et le matériel fourni ; les systèmes, comptes et identifiants n'ont pas été testés. Les données personnelles et identifiants de session restent hors du dépôt.
- **Évaluation des risques :** Si l'accès était valide, il pourrait permettre une modification de comptes, de rôles ou de paramètres du service et faciliter une prise de contrôle de fonctions dépendantes.
- **Décision de comptage :** Fiche comptabilisée comme un incident `Access Sale` distinct couvrant exclusivement `e-koragna.gov.mg`.
- **Sources / Éléments de preuve :** publication du forum fournie le 23 octobre 2026, échanges associés et éléments Keycloak fournis à AFRINTEL. Les coordonnées, identifiants de session, secrets et données personnelles ne sont pas publiés.


#### 🇨🇩 République démocratique du Congo - MINESURSI Teacher Registration Platform [Data Leak]

- **Date de publication initiale :** 20 octobre 2026 à 06:27 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** Kazu (compte affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Administration publique / Enseignement supérieur / Recherche scientifique
- **Site web associé :** [minesursi.gouv.cd](https://minesursi.gouv.cd/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Effet revendiqué :** Exposition et vente alléguées d'un corpus lié à une plateforme d'enregistrement d'enseignants
- **Volume revendiqué :** 136 GB et 125 823 fichiers ; chiffres attribué à la publications
- **Prix revendiqué :** Make an offer
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Type de source :** Publication de forum underground et archive d'échantillons fournie à AFRINTEL

- **Description victime :** Le MINESURSI est le ministère congolais chargé de l'enseignement supérieur et universitaire, de la recherche scientifique et des innovations. Le domaine associé à la publication correspond au domaine institutionnel du ministère. Les services publics associés au domaine comprennent plusieurs plateformes numériques dédiées aux établissements, aux étudiants et aux personnels de l'enseignement supérieur.

- **Analyse :**

  **Observed :** Une publication attribuée au compte **Kazu**, datée du **20 octobre 2026 à 06:27** selon l'horodatage affiché, propose à la vente un corpus présenté comme issu d'une « Teacher Registration Platform » du MINESURSI. La publication revendique **136 GB**, **125 823 fichiers** et un dépôt daté de **2026**. Elle associe le corpus au domaine `minesursi.gouv.cd` et décrit une plateforme d'inscription et de connexion destinée à l'identification et à la gestion d'informations relatives aux enseignants de l'enseignement supérieur.

  L'archive locale fournie à AFRINTEL a été contrôlée en lecture seule. Elle possède l'empreinte SHA-256 `f70f1365d67d65d7b9f17cc14b3f19ed3f92b134ea1a6dd35ad3135c29d5cf46`, une taille compressée de **1 558 803 176 octets** et une taille extraite de **1 610 225 124 octets**. Elle contient **1 531 fichiers** : **581 PDF**, **777 JPG**, **136 JPEG** et **37 PNG**. Les **581 PDF** ont été parcourus par `pdfinfo` sans document chiffré détecté et totalisent **938 pages**. Aucun fichier exécutable correspondant aux extensions contrôlées n'a été observé.

  L'analyse des noms de fichiers met en évidence des marqueurs documentaires compatibles avec des dossiers administratifs et académiques : **187** références à des passeports, **61** à des dossiers, **46** à des certificats, **44** à des nominations et **20** à des diplômes. L'extraction textuelle des PDF a produit du texte dans **57 documents**. Parmi ces documents, des marqueurs relatifs à l'enseignement apparaissent dans **13**, à l'enseignement supérieur ou à l'université dans **14**, aux données de naissance ou personnelles dans **15**, aux diplômes ou certificats dans **7** et aux fonctions, nominations ou matricules dans **7**. Ces nombres sont des indicateurs de contenu et ne constituent ni un décompte de personnes ni une preuve d'exhaustivité.

  **Assumption :** La concordance entre le ministère, le domaine institutionnel, le thème de la plateforme, les noms de fichiers et la nature des documents rend l'attribution du corpus au périmètre MINESURSI plausible. La présence de dossiers administratifs, de pièces d'identité, de diplômes et de documents de carrière est compatible avec une plateforme d'enregistrement d'enseignants. Cette cohérence ne documente pas que l'acteur a compromis l'infrastructure du ministère ni que l'archive représente l'intégralité du dépôt annoncé.

  **Unknown :** Le vecteur d'accès, les systèmes réellement affectés, la chronologie technique de l’accès, l'origine technique des fichiers, le nombre de personnes uniques, la présence de doublons, l'exhaustivité du corpus, la nature exacte des données non textuelles, l'existence d'identifiants ou de sessions valides, l'impact opérationnel et toute confirmation officielle ne sont pas renseignés dans les sources consultées. Le volume revendiqué de 136 GB et le nombre de 125 823 fichiers ne sont pas validés par l'échantillon.

- **Périmètre et limites de l'analyse :** L'archive fournie a été inventoriée dans son intégralité et ses PDF ont fait l'objet d'un contrôle structurel et d'une extraction textuelle agrégée. Les images et les pages de documents n'ont pas été transcrites ni publiées. L'analyse établit l'existence et la composition de l'artefact fourni, mais les sources consultées ne précisent pas son origine système, sa date d'acquisition, l'accès initial, l'exfiltration ou la compromission officielle. Les données brutes restent hors du dépôt.
- **Risques :** Usurpation d'identité d'enseignants, fraude documentaire, phishing ciblé, fraude administrative, atteinte à la confidentialité des personnels et exploitation de documents de carrière ou de pièces justificatives.
- **Recommandations SOC / CTI :** Préserver les journaux de la plateforme et des comptes d'administration ; rechercher les exports massifs, téléchargements anormaux et accès depuis de nouveaux appareils ; réinitialiser les sessions et secrets potentiellement exposés ; vérifier les contrôles d'accès aux dossiers et pièces justificatives ; rechercher les campagnes de phishing visant les établissements et enseignants ; coordonner la réponse avec l'autorité congolaise compétente ; ne pas télécharger ni redistribuer de données supplémentaires.
- **Évaluation AFRINTEL :** Publication observée ; archive d'échantillons fournie et analysée ; attribution à MINESURSI plausible ; structure et catégories de documents cohérentes ; volume global et exhaustivité attribué à la publications ; accès non autorisé et exfiltration non documenté dans les sources publiquess ; confirmation officielle non observée.


### 21 octobre 2026
#### 🇬🇦 Gabon - Gabon Meca (`gabonmeca.com`)

- **Date de publication initiale :** 21 octobre 2026
- **Date d'observation AFRINTEL :** 23 octobre 2026
- **Acteur / Groupe :** HYFLOCK
- **Secteur :** Commerce et distribution / équipements informatiques et bureautiques
- **Site web :** [gabonmeca.com](https://gabonmeca.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Effet revendiqué :** Exfiltration et divulgation potentielle de données
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 2
- **Type de source :** Site de divulgation HYFLOCK et éléments fournis à AFRINTEL

- **Description victime :** **Gabon Meca** est une entreprise gabonaise spécialisée dans la distribution de fournitures scolaires et de bureau, de mobilier, de matériels informatiques, d'équipements d'impression et de solutions bureautiques. Une publication associée au domaine `gabonmeca.com` la présente comme une victime de HYFLOCK.

- **Données revendiquées :** La nature exacte des données prétendument obtenues n'est pas précisée dans les éléments publics disponibles. Un système de suivi secondaire mentionne un volume de **60 Go** ; ce chiffre n'a pas été corroboré par un échantillon, une publication technique ou une déclaration de la victime.

- **Analyse :**

  **Observed :** Les éléments fournis, issus du site de divulgation HYFLOCK, présentent une fiche intitulée `gabonmeca.com leak incident`, associée à HYFLOCK, au Gabon et au domaine `gabonmeca.com`. La page présente un compte à rebours de divulgation encore en cours au moment de la collecte, ainsi qu'une description de Gabon Meca et une page LinkedIn publique de l'entreprise. Aucun échantillon de données n'a été accessible ou analysé par AFRINTEL.

  **Assumption :** La correspondance entre le domaine publié et l'activité publique de Gabon Meca rend l'identification de la victime plausible. La publication peut être compatible avec une tentative d'extorsion fondée sur une compromission et une exfiltration alléguées, mais elle ne documente pas à elle seule un accès, une extraction ou un chiffrement.

  **Unknown :** Le vecteur d'accès, les systèmes affectés, la période de compromission, la présence d'un chiffrement, la nature des données, le volume réellement extrait, l'impact opérationnel, l'existence d'une négociation ou d'un paiement et toute confirmation publique de Gabon Meca ne sont pas renseignés dans les sources consultées.

- **Périmètre et limites :** Aucun échantillon, lien de téléchargement ou fichier n'a été ouvert ou analysé. Le volume de 60 Go reste une revendication secondaire et ne doit pas être présenté comme une mesure confirmée.
- **Évaluation des risques :** Les risques potentiels comprennent l'exposition de données de clients, employés ou fournisseurs, la fraude au fournisseur, le phishing ciblé, l'exploitation d'informations commerciales et une perturbation des activités si un chiffrement était ultérieurement démontré.
- **Recommandations SOC/CTI :** Préserver les journaux VPN, IAM, EDR, pare-feu, messagerie et applications métiers ; rechercher les connexions administratives inhabituelles, créations d'archives, exports massifs et transferts sortants ; examiner les nouveaux appareils et pays d'authentification ; révoquer les sessions suspectes ; contrôler les accès aux systèmes commerciaux et bases clients ; vérifier l'intégrité des sauvegardes ; surveiller les domaines ressemblants et les campagnes de phishing ; ne pas télécharger les données éventuellement publiées.
- **Hypothèses de détection MITRE ATT&CK :** `T1078 Valid Accounts`, `T1110 Brute Force`, `T1560 Archive Collected Data`, `T1041 Exfiltration Over C2 Channel`, `T1021 Remote Services` et `T1486 Data Encrypted for Impact` sont des pistes de détection générales ; aucune n'est établie comme exécutée dans cet incident.
- **Évaluation AFRINTEL :** Publication sur un site de divulgation observée ; identification de la victime plausible ; échantillon non observé et non analysé ; accès non autorisé, exfiltration, chiffrement et interruption de service non documenté dans les sources publiquess ; attribution à HYFLOCK fondée sur la revendication publiée.
- **Sources / Éléments de preuve :** éléments issus du site HYFLOCK et fournis le 23 octobre 2026 ; [site public de Gabon Meca](https://gabonmeca.com/). Aucun lien direct vers une ressource criminelle, donnée personnelle ou échantillon n'est publié.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at:
listing_last_observed_at:
sample_status: none-observed
deadline_at:
deadline_status: unknown
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-10-23
-->


### 23 octobre 2026
#### 🇿🇦 Afrique du Sud - Rand Mutual Assurance : Workers' Compensation Services
- **Date de publication de l'alerte / revendication publique :** 23 octobre 2026
- **Acteur / Groupe :** Acteur de forum non identifié (attribution revendiquée non précisé dans les sources consultées)
- **Secteur :** Assurance / Indemnisation des accidents du travail
- **Site web :** [randmutual.co.za](https://www.randmutual.co.za/)
- **Statut :** Under Investigation
- **Type d'incident :** System Intrusion
- **Niveau de confiance :** Medium pour l'existence de l'alerte et de l'enquête ; Low pour l'accès effectif, l'exfiltration et les volumes revendiqués
- **Niveau d'impact :** Level 4 (jeu de données d'assurance et d'indemnisation à forte sensibilité ; volume global revendiqué non renseigné dans les sources consultées par l'échantillon)
- **Échéance :** 5 novembre 2026 ; fuseau horaire non précisé
- **Rançon revendiquée :** 95 000 USD
- **Volume revendiqué :** 366 Go ; 1 683 810 dossiers de demandes d'indemnisation et 593 786 fichiers
- **Description :** Rand Mutual Assurance (RMA) est une organisation sud-africaine d'assurance fournissant des services d'indemnisation des accidents du travail et des solutions d'assurance, notamment pour les secteurs minier, métallurgique, sidérurgique et associés.
- **Analyse :** RMA a confirmé avoir reçu une alerte de sécurité le 23 octobre 2026 et avoir ouvert une investigation spécialisée. L'entreprise n'a pas confirmé qu'une information avait été consultée, acquise ou divulguée sans autorisation. La revendication publique attribue à un acteur non identifié un volume de 366 Go, 1 683 810 dossiers de demandes d'indemnisation et 593 786 fichiers ; ces chiffres sont attribués à la publication et ne correspondent pas nécessairement à autant de personnes distinctes. L'analyse en lecture seule de l'archive locale `Samples.zip` (SHA-256 `46e45f8a368a626d57fe6dbe932257bdbfc6f57dfe6c8ba65c4a9a8d5c45bbe4`) porte sur les 262 fichiers fournis : 180 JSON, 71 PDF, 9 courriels EML, 1 document DOC et 1 image JPG, pour environ 75 941 802 octets décompressés. La cohérence de cet échantillon avec l'environnement métier de RMA soutient son attribution contextuelle, mais ne documente pas à elle seule l'accès ou l'extraction allégués.

  Les 180 JSON suivent un schéma homogène d'événements de sinistres, avec 192 événements individuels imbriqués. Ils contiennent notamment des références de dossiers, des informations d'employeur, des éléments de sinistre, des données de rémunération, des réclamations et des structures de suivi médical. Les événements couvrent des dates situées entre mai 2023 et août 2026 ; les dates de signalement observées vont jusqu'en septembre 2026. Les valeurs internes comportent 135 identifiants distincts de sociétés ou sites affiliés, 22 événements avec détail d'accident, 19 avec détail de maladie et 1 événement marqué comme fatal. Les 192 événements sont marqués comme non supprimés.

  Les 71 PDF représentent 117 pages ; 35 contiennent du texte extractible et 36 n'en fournissent pas dans l'analyse automatisée. Parmi les documents textuellement exploitables, plusieurs contiennent explicitement `Rand Mutual Assurance`, `RMA`, des adresses `@randmutual.co.za`, des numéros de réclamation et des formulaires ou correspondances relatifs aux accidents du travail et à la gestion de sinistres. Les 9 EML comprennent également des objets et références de réclamation RMA, dont des échanges liés à des adresses du domaine de l'organisation. Le document DOC porte des métadonnées internes mentionnant `RMA` et un modèle de papier à en-tête RMA.

  **Conclusion d'attribution de l'échantillon :** la combinaison du schéma applicatif cohérent, des références de sinistres, des marqueurs organisationnels répétés dans les JSON, PDF, courriels et document bureautique, ainsi que l'utilisation du domaine `randmutual.co.za`, est conforme à un corpus issu de l'environnement métier de Rand Mutual Assurance. L'attribution contextuelle de l'échantillon à RMA est fortement étayée. Les sources consultées ne précisent pas si l'acteur a obtenu l'échantillon par un accès non autorisé à RMA, ni la chronologie technique de l'accès, l'exfiltration, le chiffrement, l'exhaustivité du corpus ou les volumes revendiqués.

  Aucune donnée personnelle brute, adresse, numéro de dossier ou contenu individuel n'est reproduit dans le dépôt. L'analyse a été réalisée sans exécution de fichier, sans suivi de lien et sans contact avec la victime ou l'acteur.
- **Limites de preuve :** RMA confirme l'alerte et l'enquête, mais pas l'accès effectif aux données ni leur extraction. La revendication, la demande de rançon, l'échéance et les volumes restent attribués à un acteur non identifié. Le centre média public de RMA ne comportait pas encore de bilan d'enquête au dernier contrôle.
- **Action SOC/CTI :** Préserver les journaux IAM, VPN, EDR, bases de données de sinistres, stockage documentaire et passerelles sortantes antérieurs au 23 octobre ; rechercher les consultations ou exportations massives ; révoquer les sessions et secrets suspects ; surveiller les modifications frauduleuses de coordonnées bancaires liées aux indemnisations.
- **Sources / Éléments de preuve :** [ITWeb](https://www.itweb.co.za/article/rand-mutual-probes-alleged-breach-of-168m-claims/G98YdqLGAgXMX2PD) ; [TechCentral](https://techcentral.co.za/rand-mutual-assurance-data-breach-claim/287621/) ; [centre média RMA](https://www.randmutual.co.za/media). RMA confirme l'alerte et l'investigation, pas la compromission complète.


#### 🇪🇹 Éthiopie - Horn of Africa Regional Environment Centre and Network (HoA-REC&N) [Data Leak]
- **Date de publication :** 23 octobre 2026
- **Domaine :** `hoarec.org`
- **Acteur / Groupe :** N0n
- **Secteur :** Environnement / Recherche / Coopération régionale
- **Statut :** Claim - Unverified
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** HoA-REC&N est une organisation régionale éthiopienne active dans l'environnement, la recherche et la coopération en Afrique de l'Est.
- **Analyse :** La publication revendique des données SAP Business One, de comptabilité, de partenaires, d'inventaire et d'approvisionnement. Aucun échantillon n'a été examiné. L'identité de l'organisation est vérifiée, mais l'accès, l'exfiltration et les volumes restent des affirmations de l'acteur.


#### 🇹🇳 Tunisie - PROTEX Confection [Data Leak]
- **Date de publication :** 23 octobre 2026
- **Site web officiel :** [sidt.ci](https://www.sidt.ci/)
- **Acteur / Groupe :** N0n
- **Secteur :** Industrie textile / Confection
- **Statut :** Claim - Unverified
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** PROTEX Confection est présentée comme une entreprise tunisienne du secteur textile et de la confection.
- **Analyse :** La publication revendique des données de clients, fournisseurs, articles, inventaire, devis, factures, livraisons et modèles de production. L'identité juridique exacte, le domaine, l'origine des données et les volumes ne sont pas corroborés.


### 24 octobre 2026
#### 🇪🇬 Égypte - MODON Developments S.A.E [Ransomware]
- **Date de publication :** 24 octobre 2026
- **Domaine :** `modon-egypt.com`
- **Acteur / Groupe :** KryBit
- **Secteur :** Immobilier
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3
- **Description victime :** MODON Developments S.A.E est une entreprise égyptienne du secteur immobilier et du développement de projets.
- **Analyse :** La victime apparaît sur une source associée à KryBit. Aucune nature de données, aucun volume et aucune preuve publique d'intrusion, d'exfiltration ou de chiffrement n'ont été établis.


#### 🇿🇦 Afrique du Sud - Government Communication and Information System (GCIS) [System Intrusion]
- **Date de notification et de découverte publique :** 30 octobre 2026
- **Domaine officiel :** [gcis.gov.za](https://www.gcis.gov.za/)
- **Système concerné :** [erecruitment.gcis.gov.za](http://erecruitment.gcis.gov.za/), portail de candidature référencé par le GCIS
- **Acteur / Groupe :** Non identifié
- **Secteur :** Administration publique / Communication gouvernementale
- **Statut :** Incident Confirmed by Victim
- **Type d'incident :** System Intrusion
- **Niveau de confiance :** High pour l'existence et la compromission du système ; Medium pour l'exposition effective des données
- **Niveau d'impact :** Level 3 (potentiel)
- **Description victime :** Le Government Communication and Information System (GCIS) est une administration sud-africaine chargée de coordonner la communication gouvernementale et ses services d'information.
- **Analyse :** Le GCIS a indiqué que son système de recrutement électronique avait été compromis après la détection d'une activité suspecte visant ses systèmes web le 24 octobre 2026. Le portail a été isolé et l'incident signalé à l'Information Regulator, à la South African Police Service et à la State Security Agency. Les informations potentiellement concernées comprennent des numéros d'identité, des numéros de téléphone et des adresses électroniques de candidats, mais l'accès effectif à chaque donnée et l'étendue de l'exposition restent en investigation. Aucun rançongiciel, chiffrement, publication sur un site de fuite ou arrêt de service n'est établi.
- **Observed :** Compromission du système de recrutement reconnue par le GCIS ; activité suspecte détectée le 24 octobre ; isolement du système et notifications aux autorités confirmés ; exposition de données personnelles formulée comme potentielle.
- **Unknown :** Vecteur d'accès, comptes utilisés, requêtes et objets consultés ou exportés, nombre de candidats concernés, volume, durée d'accès, persistance et éventuelle utilisation abusive des données ne sont pas renseignés dans les sources consultées.
- **Évaluation des risques :** Les candidats peuvent être exposés à l'usurpation d'identité, au phishing, aux fausses convocations, aux fausses offres d'emploi et aux demandes frauduleuses de documents d'identité.
- **Action SOC/CTI :** Préserver les journaux WAF, serveur web, base de données, IAM et EDR antérieurs au 24 octobre ; identifier les comptes, requêtes et objets consultés ou exportés ; révoquer les sessions et secrets applicatifs concernés ; surveiller les campagnes d'usurpation ciblant les candidats.
- **Sources / Éléments de preuve :** [GCIS - page officielle des offres d'emploi](https://www.gcis.gov.za/content/about-us/hr/vacancies), qui référence le portail de recrutement ; [ITWeb - GCIS warns of information breach](https://www.itweb.co.za/article/gcis-warns-of-information-breach/wbrpO7g2ea3vDLZn), publié le 30 octobre 2026.


### 25 octobre 2026
#### 🇧🇯 Bénin - YOD Ingénierie (`yodingenierie.com`) [Ransomware]
- **Date de publication initiale :** 25 octobre 2026 (horodatage affiché ; heure et fuseau non indiqués)
- **Date de découverte AFRINTEL :** 30 octobre 2026
- **Acteur / Groupe :** Panzer (groupe ransomware et d'extorsion de données ; revendication et affiliation non vérifiées)
- **Échéance affichée :** autour du 15 novembre 2026, sur la base des 12 jours restants indiqués par l'acteur le 3 novembre 2026 ; l'heure exacte n'est pas précisée
- **État de l'échéance :** En cours au 3 novembre 2026 ; l'acteur affirme que les négociations ont échoué et qu'aucun paiement de rançon n'a été effectué ; divulgation non observée dans les éléments consultés
- **Secteur :** Ingénierie / Technologies de l'information / Transformation numérique
- **Site web officiel :** [yodingenierie.com](https://yodingenierie.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Medium pour l'existence de la publication et l'identification de l'entreprise ; Low à Medium pour l'attribution technique des données
- **Niveau d'impact :** Level 4 (potentiel)
- **Type de source :** Publication d'un site de divulgation ransomware et inventaire local de fichiers examiné en lecture seule
- **Description victime :** YOD Ingénierie est une entreprise béninoise d'ingénierie et de technologies de l'information, membre du groupe NED&CO. Elle intervient dans la transformation numérique, la gouvernance des systèmes d'information et les projets liés à l'intelligence artificielle.
- **Analyse :** La publication attribuée au groupe ransomware Panzer revendique un corpus de **48 Go** dans un contexte d'extorsion, comprenant notamment des documents d'identité, des scans de passeports, des formulaires KYC, des documents bancaires, des signatures, des fiches de paie, des dossiers du personnel, des contrats, des factures, des budgets, des audits, des listes de donateurs, des correspondances internes et des documents de planification. Aucun chiffrement de systèmes n'est démontré par les éléments disponibles.

  Le dossier fourni contient uniquement un inventaire arborescent de **15 878 lignes**. Les noms de fichiers indiquent plusieurs catégories compatibles avec la description publiée, notamment des documents administratifs, des dossiers de personnel, des éléments KYC, des pièces financières, des contrats, des budgets et des documents de projets. Aucun fichier source exploitable n'était disponible dans le dossier ; les **48 Go** annoncés et la nature exacte du contenu ne sont donc pas validés.

  **Observed :** L'entreprise est reliée au Bénin par son site officiel ; la publication affiche YOD Ingénierie, un volume annoncé de 48 Go, une date du 25 octobre 2026 et le groupe Panzer. Des sources CTI publiques décrivent Panzer comme un groupe ransomware et d'extorsion de données. Le 3 novembre 2026, l'acteur indiquait 12 jours avant l'échéance et déclarait que les négociations avaient échoué, sans paiement de rançon. L'inventaire local confirme la présence de nombreuses références documentaires cohérentes avec les catégories annoncées, sans permettre de lire leur contenu.

  **Assumption :** Si la revendication est authentique, l'exposition pourrait concerner des données personnelles, financières, RH, contractuelles et opérationnelles de YOD Ingénierie et de ses partenaires. La présence de documents liés à d'autres pays africains pourrait refléter l'activité régionale du groupe, mais ne suffit pas à attribuer toutes les données au Bénin.

  **Unknown :** Le vecteur d'accès, la date d'extraction, l'authenticité des fichiers, l'exhaustivité du corpus, le nombre de personnes ou d'organisations concernées, l'existence d'un échantillon réellement téléchargeable, la validité actuelle des documents, l'issue de l'échéance, la réalité du non-paiement déclaré par l'acteur et toute confirmation par YOD Ingénierie ne sont pas établis par les éléments consultés.
- **Périmètre et limites de l'analyse :** Analyse structurelle et préliminaire fondée sur la publication, les informations publiques de l'entreprise et l'inventaire local. Le contenu des documents n'a pas pu être examiné ; aucune donnée personnelle brute, pièce d'identité, secret ou lien de téléchargement n'est reproduit dans le dépôt.
- **Évaluation des risques :** Si les données sont authentiques, les risques potentiels comprennent l'usurpation d'identité, la fraude documentaire et financière, le phishing ciblé, l'atteinte à la confidentialité des employés et partenaires, ainsi que l'exposition d'informations contractuelles et opérationnelles.
- **Sources / Éléments de preuve :** Publication attribuée à Panzer observée le 30 octobre 2026 ; image de la publication et déclaration de l'acteur concernant l'échec des négociations, les 12 jours restants et l'absence alléguée de paiement, fournies pour analyse ; inventaire local `yodingenierie-tree.txt` ; [site officiel de YOD Ingénierie](https://yodingenierie.com/) ; [profil public CTI de Panzer](https://secureresearch.com/threat-actors/panzer.html). Les fichiers potentiellement sensibles restent hors du dépôt.


### 26 octobre 2026
#### 🇿🇦 Afrique du Sud - Lydenburg Toyota [Ransomware]
- **Date de publication :** 26 octobre 2026
- **Domaine :** `lydenburg.toyota.co.za`
- **Acteur / Groupe :** The Gentlemen
- **Secteur :** Automobile / Concession et après-vente
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** Lydenburg Toyota est une concession automobile sud-africaine proposant des services de vente et d'après-vente.
- **Analyse :** La publication criminelle et l'identité du concessionnaire sont corroborées. Aucune nature de données ni aucun volume n'ont été établis ; intrusion, exfiltration et chiffrement ne sont pas confirmés par Toyota ou le concessionnaire.


### 28 octobre 2026
#### 🇳🇬 Nigeria - InvestNaija / Chapel Hill Denham [System Intrusion]
- **Date de notification publique :** 28 octobre 2026
- **Domaines officiels :** [investnaija.com](https://investnaija.com/) ; [chapelhilldenham.com](https://chapelhilldenham.com/)
- **Acteur / Groupe :** Non identifié
- **Secteur :** Services financiers / Gestion d'investissements
- **Statut :** Incident Confirmed by Victim
- **Type d'incident :** System Intrusion
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** InvestNaija et Chapel Hill Denham sont des entités nigérianes liées aux services financiers et à la gestion d'investissements.
- **Analyse :** Chapel Hill Denham a notifié les clients d'InvestNaija d'une activité inhabituelle suggérant qu'une partie de leurs informations pourrait avoir été consultée sans autorisation. L'entreprise a pris des mesures de confinement et signalé l'incident aux autorités compétentes. Moins de 1 % des informations clients pourraient être concernées ; les investissements n'auraient pas été affectés selon la notification. Les adresses électroniques et autres coordonnées pourraient avoir été obtenues, mais l'accès effectif, le nombre d'enregistrements et l'étendue restent en investigation. Aucun rançongiciel, chiffrement ou arrêt de service n'est établi.
- **Données potentiellement exposées :** adresses électroniques et autres coordonnées de contact ; le nombre de personnes et le volume en octets ne sont pas précisés dans les sources consultées.
- **Action SOC/CTI :** Préserver les journaux WAF, API, IAM, applications mobiles et canaux web antérieurs au 28 octobre ; identifier la source de l'activité inhabituelle et les comptes ou objets consultés ; révoquer les sessions et jetons concernés ; surveiller le phishing et les demandes financières inhabituelles visant les clients.
- **Sources / Éléments de preuve :** [The Sun Nigeria](https://thesun.ng/chapel-hill-denham-alerts-customers-to-potential-data-breach-says-investments-safe/) ; [InvestNaija](https://investnaija.com/) ; [Chapel Hill Denham](https://chapelhilldenham.com/).


#### 🇸🇱 Sierra Leone - GIO Dental (`giodentalsl.com`) [Ransomware]
- **Date de publication initiale :** 28 octobre 2026
- **Domaine :** [giodentalsl.com](https://www.giodentalsl.com/)
- **Acteur / Groupe :** The Gentlemen
- **Secteur :** Santé / Soins dentaires
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3 (potentiel)
- **Description victime :** GIO Dental est présentée comme une clinique et un laboratoire dentaires opérant à Freetown et à Koidu, en Sierra Leone. Le fondateur est décrit comme nigérian, mais la victime opérationnelle est située en Sierra Leone.
- **Analyse :** GIO Dental apparaît dans une revendication associée à The Gentlemen. Des sources OSINT la situent en Sierra Leone, mais aucun échantillon, volume, preuve de chiffrement, exfiltration ou confirmation de la clinique n'a été identifié.
- **Évaluation des risques :** Une revendication authentique pourrait concerner des dossiers de patients, des données administratives et des systèmes de laboratoire. Aucun de ces éléments n'est établi.
- **Sources / Éléments de preuve :** [CTIWatch](https://ctiwatch.com/victims/gio-dental-924d6f76) ; [liste The Gentlemen](https://ctiwatch.com/threats/thegentlemen/victims) ; [site de GIO Dental](https://www.giodentalsl.com/). Les sources de suivi précisent qu'il s'agit d'une revendication attribuée à la publication.

### 29 octobre 2026
#### 🇪🇬 Égypte - BlueBus (`bluebus.com.eg`) [Data Leak]
- **Date de publication initiale :** 29 octobre 2026 à 06:02 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** Lenken (compte affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Transport / Mobilité / Billetterie
- **Site web associé :** [bluebus.com.eg](https://bluebus.com.eg/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High pour l'existence et l'analyse de l'échantillon publié ; Medium pour son attribution technique à BlueBus
- **Niveau d'impact :** Level 4
- **Type de source :** Publication de forum et échantillons locaux examinés en lecture seule
- **Description victime :** BlueBus est un service égyptien de réservation et de billetterie de transport par autobus. La publication attribuée au compte Lenken associe le domaine `bluebus.com.eg` à une base de commandes et de données liées aux clients, aux billets, aux paiements et aux chauffeurs.
- **Analyse :** La publication revendique plus de **300 000 commandes**, **305 520 lignes**, **651 chauffeurs** et une base de commandes couvrant 2026. Ces volumes restent des affirmations de l'auteur et ne sont pas validés par les fichiers locaux.

  AFRINTEL a examiné intégralement en lecture seule le fichier `sample.csv` : **2 999 lignes**, **16 colonnes**, **0 ligne malformée**. Les colonnes observées couvrent les commandes ou billets, les statuts, les prix, les identifiants de clients, les coordonnées, les dates de naissance, les identifiants nationaux, les modes de paiement, les identifiants de transaction et les informations de billets. L'échantillon contient **1 178 identifiants clients distincts**, **1 178 numéros de téléphone distincts**, **350 adresses électroniques distinctes** et **358 lignes renseignant un identifiant national**. Les champs de nom et de téléphone sont présents sur l'ensemble des 2 999 lignes ; les noms de famille et dates de naissance sont renseignés sur 228 lignes. Les champs de statut ou de code sont renseignés sur 1 541 lignes, les champs de paiement et de billets sur 1 458 lignes et les identifiants de transaction sur 218 lignes.

  Les statuts observés dans l'échantillon sont `Paid` (947), `Expired` (415), `Cancelled` (135), `Pending` (26) et `Modified` (18). Les modes de paiement observés comprennent notamment `StoreCash`, `Fawry`, `PartnerCredit`, `Cash`, `Card`, `StoreCard`, `Aman` et `AutoConfirmed`. Le total arithmétique des prix du snapshot atteint environ **1 189 773,62** dans l'unité affichée par le fichier, mais les répétitions de commandes et de clients empêchent de l'interpréter comme un montant financier unique ou comme le total des ventes exposées.

  Le fichier `drivers.txt` contient **9 objets JSONL**. Ils présentent des informations imbriquées sur des utilisateurs et des chauffeurs, des stations, des montants et des horodatages. L'échantillon contient **9 identifiants de chauffeurs**, **9 identifiants d'utilisateurs** et **5 identifiants de stations** ; les horodatages observés vont du **1er au 20 octobre 2026**. Les structures comprennent également des informations de contact et des identifiants sensibles de chauffeurs ; aucune valeur individuelle n'est reproduite dans le dépôt. La présence de 9 objets locaux ne permet pas de valider les **651 chauffeurs** revendiqués.

  **Assumption :** Le domaine publié, la structure de réservation, les catégories de commandes, les références aux stations et l'organisation des données sont compatibles avec une plateforme de billetterie de transport associée à BlueBus. Cette cohérence soutient l'attribution contextuelle de l'échantillon, mais ne documente pas le vecteur d'accès, l'exfiltration par Lenken, la provenance technique de chaque enregistrement, l'exhaustivité du corpus ni une compromission confirmée par BlueBus.

  **Unknown :** La date d'accès, le système exact d'origine, le nombre de personnes uniques dans la base complète, la validité actuelle des identifiants, l'existence d'un accès non autorisé, la portée géographique, l'exhaustivité des **305 520 lignes**, le nombre réel de chauffeurs et toute confirmation officielle ne sont pas renseignés dans les sources consultées.
- **Périmètre et limites de l'analyse :** Les deux fichiers locaux ont été examinés intégralement en lecture seule ; leurs types, tailles, empreintes SHA-256, encodage, schéma, valeurs manquantes, doublons, agrégats, statuts et plages temporelles ont été contrôlés. L'archive RAR a été inspectée sans extraction active ni exécution de contenu. Les valeurs personnelles, identifiants, liens de téléchargement et secrets n'ont pas été publiés, testés ou suivis.
- **Évaluation des risques :** Si l'échantillon est authentique, l'exposition pourrait faciliter le phishing ciblé, la fraude aux billets et aux paiements, l'usurpation de clients ou de chauffeurs, l'exploitation d'identifiants nationaux et la corrélation de données de mobilité. Ces risques sont potentiels et ne constituent pas une confirmation de l'incident.
- **Sources / Éléments de preuve :** Publication du forum fournie le 30 octobre 2026 ; `sample.csv` et `drivers.txt` locaux examinés en lecture seule. L'archive et les fichiers sources restent hors du dépôt ; aucune donnée personnelle brute n'est reproduite.


#### 🇪🇬 Égypte - Organisations, cliniques, pharmacies, hôpitaux et médecins [Data Leak]
- **Date de publication initiale :** 29 octobre 2026 à 03:53 (horodatage affiché ; fuseau non indiqué)
- **Acteur / Groupe :** Marx (compte affiché ; identité et affiliation attribuée à la publication)
- **Secteur :** Santé / Répertoire de professionnels et d'organisations
- **Site web associé :** Non précisé dans la publication
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High pour l'existence et l'analyse du fichier médecin ; Medium pour son attribution au périmètre égyptien revendiqué
- **Niveau d'impact :** Level 3
- **Type de source :** Publication de forum et classeur XLSX local examiné en lecture seule
- **Description victime :** La publication attribuée au compte Marx présente un ensemble de données relatif à des médecins, cliniques, pharmacies, hôpitaux et organisations de santé en Égypte. Le fichier local disponible correspond au volet « Doctor File » et semble constituer un répertoire de professionnels de santé ; le fichier « Organizations File » annoncé dans la publication n'est pas disponible pour analyse.
- **Analyse :** La publication annonce un fichier de médecins de plus de **33 000 lignes** et un fichier d'organisations de plus de **48 000 lignes**. AFRINTEL a examiné intégralement en lecture seule le classeur `Doctor.xlsx`, dont la structure contient **33 120 lignes de données**, **11 colonnes nommées** et un champ vide supplémentaire. Les colonnes observées couvrent un code professionnel, le nom du médecin, le type, la spécialité, la classe, un champ lié au compte, des codes et noms d'organisation, un état d'activité, un numéro mobile et une adresse électronique.

  Le champ médecin contient **28 138 valeurs distinctes** sur les 33 120 lignes. Le champ de spécialité comporte **38 valeurs distinctes**, le champ de classe **16**, le champ lié au compte **9** et l'état d'activité **2**. Un numéro mobile est renseigné sur **5 746 lignes** ; aucun e-mail n'est renseigné dans ce classeur. Les champs de code et d'identification professionnelle sont présents sur l'ensemble des lignes. Les colonnes de code et nom d'organisation sont vides dans le fichier local, ce qui empêche d'établir les structures de santé précises associées à chaque professionnel.

  La correspondance entre le volume local de **33 120 lignes** et l'annonce « +33K » soutient l'existence d'un échantillon réellement structuré, mais ne valide pas le fichier d'organisations annoncé à **+48K**, qui n'a pas été fourni. La structure du classeur est compatible avec un répertoire de professionnels de santé égyptiens ; elle ne permet pas d'établir le système source, le vecteur d'accès, l'exfiltration par Marx, l'exhaustivité du corpus ou une confirmation par une organisation de santé.

  **Assumption :** Le titre de la publication, la nature du classeur et la présence de champs de médecins, spécialités, comptes, mobiles et états d'activité rendent plausible un lien avec l'écosystème de santé égyptien. Cette compatibilité ne documente pas que les données proviennent d'un registre officiel ou d'une organisation précise.

  **Unknown :** L'identité de l'organisation victime, la provenance technique du classeur, la date d'extraction, le nombre de personnes uniques dans le corpus complet, la nature des comptes, le statut actuel des données, l'existence d'un accès non autorisé, le contenu du fichier « Organizations » et toute confirmation officielle ne sont pas renseignés dans les sources consultées.
- **Périmètre et limites de l'analyse :** Le classeur `Doctor.xlsx` a été analysé intégralement en lecture seule au niveau XML/XLSX, avec contrôle de la structure, des lignes, des colonnes, des champs vides et des valeurs distinctes. Aucun fichier d'organisation n'était présent dans le répertoire local. Aucun nom, numéro, e-mail ou autre donnée personnelle brute n'est reproduit dans le dépôt.
- **Évaluation des risques :** Si le fichier est authentique, il pourrait faciliter le phishing ciblé, l'usurpation de médecins ou d'organisations, la fraude aux rendez-vous et la cartographie de professionnels de santé. Aucun dossier patient ni donnée clinique n'a été observé dans le fichier analysé.
- **Sources / Éléments de preuve :** Publication du forum fournie le 30 octobre 2026 et `Doctor.xlsx` local examiné en lecture seule. Le fichier reste hors du dépôt ; aucune donnée personnelle brute n'est publiée.


#### 🇪🇬 Égypte - Al Arabia United [System Intrusion]
- **Date de publication / confirmation publique :** 29 octobre 2026
- **Domaine officiel :** [audegypt.com](https://audegypt.com/)
- **Localisation :** axe du 26-Juillet, gouvernorat de Gizeh
- **Acteur / Groupe :** Leakers$ (revendication publique ; attribution technique attribuée à la publication)
- **Secteur :** Publicité extérieure / Infrastructure d'affichage numérique
- **Statut :** Incident Confirmed by Victim
- **Type d'incident :** System Intrusion
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 2
- **Description victime :** Al Arabia United est une entreprise égyptienne spécialisée dans la publicité extérieure et l'exploitation de panneaux publicitaires numériques.
- **Analyse :** Le 29 octobre, un panneau exploité par Al Arabia United sur l'axe du 26-Juillet à Gizeh a diffusé du contenu explicite non autorisé. L'entreprise a reconnu un accès non autorisé à l'un de ses écrans, l'a immédiatement désactivé et a indiqué coopérer avec les autorités. Le ministère égyptien de l'Intérieur a confirmé qu'une société de publicité utilisait les services d'une entreprise internationale pour diffuser électroniquement les contenus et que le site de cette entreprise avait été compromis ; le même contenu aurait alors été diffusé simultanément sur des écrans de plusieurs pays.
- **Éléments observés :** diffusion effective de contenu non autorisé ; reconnaissance de l'accès non autorisé par Al Arabia United ; arrêt préventif de l'écran ; confirmation officielle de l'incident et impact simultané rapporté dans plusieurs pays.
- **Revendiqué, mais non documenté dans les sources publiques techniquement :** Leakers$ affirme avoir exploité une vulnérabilité dans le logiciel de transmission destiné aux écrans LED. Aucune CVE, preuve technique ni identité du fournisseur compromis n'a été publiée ; les modalités exactes de l'accès initial restent inconnues.
- **Non établi :** exposition ou exfiltration de données, chiffrement de systèmes, compromission du site `audegypt.com`, compromission de l'ensemble du réseau d'Al Arabia United et persistance dans l'environnement du fournisseur.
- **Évaluation des risques :** L'incident montre un risque de détournement de contenu et de propagation coordonnée lorsqu'une plateforme centralisée de gestion d'affichage numérique est reliée à plusieurs pays. Aucun impact sur des données ou sur les systèmes internes d'Al Arabia United n'est établi.
- **Sources / Éléments de preuve :** [audegypt.com](https://audegypt.com/) ; [ministère égyptien de l'Intérieur](https://www.moi.gov.eg/news/GetDetails?newsId=bbfb00a8-b8e2-4c10-81bd-161ba437d035) ; [Al-Ahram Gate](https://gate.ahram.org.eg/News/5974509.aspx) ; [The Cairo Report](https://www.cairoreport.org/p/egypt-brazil-iraq-billboard-hack) ; [x.com/IntCyberDigest](https://x.com/IntCyberDigest/status/2116519809445675248).


### 30 octobre 2026
#### 🇨🇮 Côte d'Ivoire - Société Ivoirienne de Télédiffusion [Ransomware]
- **Date de publication de la revendication / découverte publique :** 30 octobre 2026 ; première indexation observée vers 17:26 UTC
- **Domaine :** Non établi
- **Acteur / Groupe :** Qilin (attribution revendiquée uniquement)
- **Échéance affichée :** environ 4 novembre 2026 vers 14:00, calculée à partir du compte à rebours de 108 heures et 17 minutes observé le 31 octobre 2026 vers 01:43 ; fuseau horaire non affiché
- **État de l'échéance :** En cours au moment de l'observation ; divulgation non observée
- **Secteur :** Télédiffusion / Infrastructures audiovisuelles
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Low
- **Niveau d'impact :** Level 3 (potentiel)
- **Description victime :** La Société Ivoirienne de Télédiffusion (SIDT) est une société d'État ivoirienne créée en 2017. Elle assure la diffusion de programmes radiophoniques et télévisuels, notamment via la TNT, ainsi que des services de multiplexage, d'infrastructure et de support technique.
- **Analyse :** La victime apparaît dans un dispositif public de suivi associé au site de divulgation de Qilin. La page observée affiche un compte à rebours de **108 heures et 17 minutes**, sans publication de données ni volume annoncé. Les éléments observés se limitent à la publication de la fiche et à l'échéance affichée ; aucun élément technique relatif à l'accès, à l'exfiltration, au chiffrement ou à l'interruption des services de diffusion n'a été fourni.
- **Observed :** Publication attribuée à Qilin, victime identifiée comme la Société Ivoirienne de Télédiffusion, première indexation observée le 30 octobre 2026 vers 17:26 UTC ; compte à rebours affiché de 108 heures et 17 minutes lors de l'observation du 31 octobre 2026 vers 01:43.
- **Unknown :** Domaine, vecteur d'accès, systèmes concernés, chronologie technique de l’accès, nature des données, volume, chiffrement, interruption de service, issue de l'échéance, confirmation de la victime et déclaration d'une autorité ivoirienne ou d'un CERT ne sont pas renseignés dans les sources consultées.
- **Évaluation des risques :** Si la revendication était authentique, les risques pourraient concerner la continuité de diffusion, les systèmes audiovisuels, les données administratives et les relations avec les prestataires. Ces risques restent potentiels.
- **Sources / Éléments de preuve :** Indexation publique d'une revendication Qilin observée le 30 octobre 2026 et état de la page vérifié le 31 octobre 2026 ; [site officiel de la SIDT](https://www.sidt.ci/). Aucun échantillon, lien criminel direct ou donnée brute n'est reproduit dans le dépôt.
