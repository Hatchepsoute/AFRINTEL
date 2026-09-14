![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en août 2026 (29 fiches)

👉🏾 [**English version available here**](./victims.md)

## Août 2026

### 01 août 2026

#### 🇪🇬 Égypte - Portail des services locaux égyptiens (attribution probable)

* **Date de publication initiale:** 5 juin 2026
- **Date de détection AFRINTEL :** 1 août 2026
* **Acteur / Groupe:** R3D3MPTION
* **Secteur:** Gouvernement / Administration
* **Site web:** [lgs.gov.eg](https://www.lgs.gov.eg/)
* **Statut:** Claim - Data Sample Published
* **Type d'incident:** Data Leak
* **Niveau de confiance:** High
* **Niveau d'impact:** Level 4
* **Type de source:** Underground Forum - Direct AFRINTEL Observation
* **Description victime:**
  Le Portail des services locaux égyptiens, `lgs.gov.eg` (بوابة خدمات المحليات), est une plateforme gouvernementale permettant aux citoyens et aux entreprises d'accéder à différents services administratifs locaux en ligne. Le portail s'inscrit dans la numérisation des services des gouvernorats, villes et centres technologiques locaux en Égypte. L'attribution de l'incident à cette plateforme est considérée comme probable sur la base de la convergence entre le schéma des données analysées, les documents publiés et les fonctions connues du portail.

* **Analyse:**
  Le 5 juin 2026, l'acteur R3D3MPTION a publié une offre affirmant avoir compromis un service gouvernemental égyptien lié aux services locaux. Il revendique plus de **70 Go de documents**, plus de **5 Go de données personnelles** et un fichier `CITIZENS.CSV` contenant **13 117 317 enregistrements**. La publication mentionne également des ensembles relatifs aux utilisateurs, véhicules et entreprises, ainsi qu'environ **118 000 documents citoyens**, comprenant selon l'acteur des images de pièces d'identité, contrats et autres documents administratifs. Ces volumes globaux restent des revendications et n'ont pas été validés.

  L'échantillon `citizens_sample.csv` fourni et analysé contient **9 938 enregistrements et 42 colonnes**, pour **9 933 identifiants citoyens distincts**. L'analyse met en évidence des données structurées comprenant notamment des noms, identifiants nationaux, identifiants de passeport, adresses, dates de naissance, coordonnées, informations de nationalité et d'état civil, données professionnelles, informations liées au handicap ainsi que différents identifiants administratifs. Sur les **9 805 identifiants nationaux renseignés**, **9 408** présentent une longueur de 14 chiffres, cohérente avec le format utilisé pour les identifiants nationaux égyptiens.

  Le jeu analysé présente également une temporalité récente. Le champ applicatif `InsertDate` est renseigné pour **9 435 enregistrements**, dont **3 544** portent la date du **3 juin 2026** et **778** celle du **2 juin 2026**. Ces valeurs suggèrent que certaines données présentes dans l'échantillon étaient encore alimentées peu avant la publication du 5 juin. Elles ne permettent cependant pas d'établir la date de l'accès initial, de l'exfiltration ou de la compromission.

  Les documents visibles dans la publication comprennent des pièces d'identité égyptiennes, formulaires administratifs, plans, documents immobiliers et différents justificatifs associés à des procédures locales. La combinaison de ces documents avec la structure du fichier citoyens et les ensembles `Users`, `Cars` et `Companies` annoncés présente une forte cohérence fonctionnelle avec l'écosystème du Portail des services locaux égyptiens. Cette convergence soutient une **attribution probable à `lgs.gov.eg` ou à une infrastructure back-end associée**, mais ne constitue pas une confirmation officielle de compromission de la plateforme.

  L'échantillon analysé représente environ **0,076 %** des 13 117 317 enregistrements revendiqués. Il ne permet donc pas de confirmer l'exhaustivité du corpus annoncé, les volumes de **70+ Go de documents**, les **5+ Go de PII** ou les **118 000 documents** revendiqués. Le vecteur d'accès initial, les systèmes effectivement touchés, la méthode d'exfiltration et l'étendue complète de l'incident restent inconnus.

  La sensibilité des données observées, leur caractère administratif, la présence de documents d'identité et la portée nationale potentielle justifient un niveau d'impact **Level 4**. Les principaux risques concernent l'usurpation d'identité, la fraude documentaire, le spear-phishing fortement contextualisé et l'exploitation croisée de données administratives.

* **Recommandations:**

  * Rechercher dans les journaux applicatifs, IAM, API, bases de données et systèmes de stockage toute extraction massive, requête anormale ou accès inhabituel intervenu avant le 5 juin 2026, avec une attention particulière aux 2 et 3 juin.
  * Renforcer la surveillance des comptes administratifs et techniques, réévaluer les droits d'accès aux données citoyens et mettre en place des contrôles de détection sur les exports volumineux, les accès API inhabituels et les transferts sortants de documents sensibles.



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


#### 🇩🇿 Algérie - Direction générale de la recherche scientifique et du développement technologique (DGRSDT)

- **Date de l'incident :** 8 juillet 2026 (date fournie pour l'incident ; date d'accès initial non établie)
- **Date de publication initiale :** 8 juillet 2026 à 18:33 (fuseau horaire non indiqué)
- **Date de découverte AFRINTEL :** 1 août 2026
- **Acteur / Groupe :** anisanas2
- **Secteur :** Gouvernement / Recherche scientifique
- **Site web :** [dgrsdt.dz](https://www.dgrsdt.dz/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Type de source :** Underground Forum and Messaging Channel - Direct AFRINTEL Observation
- **Sources publiques :** [Présentation officielle de la DGRSDT](https://www.dgrsdt.dz/public/index.php/fr/about_dgrsdt)

- **Description victime :**

  La Direction générale de la recherche scientifique et du développement technologique (DGRSDT) est une direction générale algérienne placée sous l'autorité du ministre chargé de la recherche scientifique. Elle met en œuvre la politique nationale de recherche scientifique et de développement technologique, notamment pour la programmation, l'évaluation, la recherche universitaire, les ressources humaines et le financement des programmes.

- **Analyse :**

  **Observed :** La publication observée, attribuée à anisanas2, date du 8 juillet 2026 à 18:33 selon l'horodatage visible. Elle affirme une compromission de la DGRSDT et propose un ensemble présenté comme contenant les identifiants gouvernementaux de doctorants et de scientifiques, leurs informations personnelles, des certificats d'inscription, des autoportraits et des dossiers de projets doctoraux. Le prix annoncé est de **800 USD** ; la publication revendique **6 000 identifiants** et **6 000 profils**. Ces chiffres et la compromission restent des revendications de l'acteur.

  Le CSV fourni et analysé intégralement contient **1 000 enregistrements et 29 colonnes**, avec une largeur constante. Il comprend des champs relatifs aux chercheurs, encadrants, établissements, diplômes, situations, coordonnées et identifiants nationaux. **16 lignes sont des doublons exacts au-delà de la première occurrence**. Les champs d'identifiant national renseignés présentent majoritairement 18 chiffres dans les deux blocs de profil ; aucune valeur personnelle n'est reproduite ici.

  L'archive de profils contient **4 123 fichiers** pour environ **2,46 Go** non compressés. L'analyse des empreintes distingue **2 185 contenus uniques**, avec **1 938 fichiers en doublon exact** au-delà de la première occurrence. Les signatures identifient principalement des images ; 3 950 fichiers image ont été vérifiés par lecture, tandis que 172 n'ont pas pu être validés par la bibliothèque d'image utilisée. L'archive de certificats contient **100 fichiers**, soit 51 PDF et 49 images, représentant 58 pages PDF ; aucun fichier n'est chiffré et aucun doublon exact n'a été détecté.

  Les noms de fichiers de l'archive de profils correspondent à des noms ou identifiants du CSV pour **1 042 fichiers et 444 lignes**. Dans l'archive de certificats, **25 fichiers** correspondent à des noms présents dans **26 lignes** du CSV. Ces rapprochements, la structure des champs, les documents et les éléments visuels associés à la publication soutiennent une attribution à des données liées à la DGRSDT avec un niveau de confiance élevé pour l'authenticité structurelle et l'attribution de l'échantillon.

  **Assumption :** La cohérence entre la mission officielle de la DGRSDT, le schéma doctoral du CSV, les certificats, les images de profils et les correspondances de noms rend plausible l'association du corpus à l'écosystème de la DGRSDT. Elle ne permet pas d'établir le vecteur d'accès, l'extraction ou la compromission officielle de l'organisation.

  **Unknown :** Le nombre réel de personnes concernées, l'exhaustivité du jeu complet, la validité des **6 000 profils** revendiqués, la date et la méthode d'accès, les systèmes touchés, l'exfiltration, l'impact opérationnel, la confirmation de la victime et la divulgation de l'ensemble complet restent inconnus. Les archives ont été examinées localement en lecture seule ; aucune donnée personnelle brute n'est publiée. L'analyse des documents visuels reste limitée par les 172 fichiers image non validés et par l'absence de modèle OCR français ou arabe disponible.


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


### 02 août 2026

#### 🇿🇦 Afrique du Sud - Buzz Trading 104

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 02 août 2026 à 13:26:24 (fuseau horaire non indiqué)
- **Acteur / Groupe :** krybit
- **Secteur :** Fabrication de plastiques / Articles ménagers
- **Site web :** [buzztrading104.co.za](https://buzztrading104.co.za/)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 2
- **Sources publiques :** [Présentation de Buzz Trading 104](https://buzztrading104.co.za/about-buzz-trading/) | [Site officiel](https://buzztrading104.co.za/)

- **Description :**

  Buzz Trading 104 est un fabricant sud-africain de produits plastiques moulés par injection et de biens destinés aux marchés grand public et industriels, actif depuis 2003. Son portefeuille comprend notamment des articles ménagers et de rangement, des produits de plein air, des conteneurs roulants industriels, du mobilier pour enfants, des emballages plastiques et des échelles en aluminium.

- **Analyse :**

  **Observed :** L'enregistrement source fourni associe krybit à Buzz Trading 104, situe la cible en Afrique du Sud et cite www.buzztrading104.co.za. Il est horodaté au 2 août 2026 à 13:26:24, sans fuseau horaire indiqué. Aucun échantillon, volume, délai de divulgation, type de données ou élément technique de compromission n'est fourni.

  **Assumption :** La concordance du domaine avec le site public de l'entreprise rend l'identification de la cible plausible. Elle ne confirme ni un accès non autorisé, ni une exfiltration, ni un chiffrement.

  **Unknown :** La date et la méthode d'accès initial, les systèmes affectés, l'existence d'un impact opérationnel, la nature des données éventuellement obtenues, la confirmation de la victime, la négociation, le paiement et la revente restent inconnus.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-02T13:26:24
listing_last_observed_at: 2026-08-02T13:26:24
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-02T13:26:24
-->

#### 🇳🇬 Nigeria - ASHA Microfinance Bank Limited (ASA Nigeria)

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 02 août 2026 à 14:24:27 (fuseau horaire non indiqué)
- **Acteur / Groupe :** krybit
- **Secteur :** Microfinance / Banque
- **Site web :** [nigeria.asa-international.com](https://nigeria.asa-international.com/)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4
- **Sources publiques :** [Présentation institutionnelle](https://nigeria.asa-international.com/about-us/) | [Profil synthétique](https://nigeria.asa-international.com/about-us/at-a-glance/) | [Compte rendu de la revendication KRYBIT](https://www.dexpose.io/krybit-ransomware-strikes-asha-microfinance-bank-in-nigeria/)

- **Description :**

  ASHA Microfinance Bank Limited, ou ASA Nigeria, est une banque nigériane de microfinance acceptant les dépôts et filiale d'ASA International. Elle a commencé ses activités en 2010 et accorde principalement de petits prêts à vocation sociale à des entrepreneures à faibles revenus, dans le cadre d'une licence nationale de microfinance.

- **Analyse :**

  **Observed :** L'enregistrement source associe KRYBIT à ASHA Microfinance Bank et a été observé le 2 août 2026 à 14:24:27, sans fuseau horaire indiqué. Le corpus fourni est attribué à la divulgation de données par KRYBIT. Selon les informations de provenance transmises avec le corpus, cette divulgation aurait suivi l'échec des négociations entre les deux parties ; ce déroulement n'a pas été corroboré indépendamment par une source publique. L'analyse en lecture seule du dossier complet a recensé 1 498 fichiers (environ 7,15 Go) : 1 101 ne contiennent que des octets nuls et 397 contiennent des données non nulles. Seize tables textuelles représentent environ 14,6 millions de lignes physiques ; 5 164 lignes ont été échantillonnées et huit irrégularités de largeur ont été relevées. Le corpus comprend également des classeurs et documents bureautiques ainsi que des fichiers RTF ; plusieurs archives sont endommagées ou illisibles. Les éléments lisibles présentent des champs financiers ou transactionnels et des motifs de contact dans une partie des fichiers. Les dates structurées observées vont du 27 avril 2022 au 16 juillet 2026.

  **Assumption :** Le chemin de collecte, le domaine associé et la nature structurée du corpus sont cohérents avec ASHA. Les documents lisibles ne portent toutefois pas tous de marqueur institutionnel explicite. Les lignes physiques ne représentent pas nécessairement des enregistrements uniques ou des clients distincts. Si les données financières ou de clientèle sont authentiques, elles peuvent favoriser l'hameçonnage ciblé, l'usurpation d'identité et la fraude.

  **Unknown :** La méthode et la date d'accès initial, les systèmes touchés, le mécanisme de chiffrement, l'exhaustivité du corpus, le nombre d'enregistrements uniques et l'impact opérationnel ne sont pas établis. La confirmation officielle de l'incident n'a pas été observée. Le statut des négociations reste non corroboré publiquement ; aucun paiement ou transfert à un tiers n'est établi.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-02T14:24:27
listing_last_observed_at: 2026-08-02T14:24:27
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: release-reviewed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-13T02:32:51Z
-->

#### 🇿🇦 Afrique du Sud - DC Partner

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 02 août 2026 à 14:25:08 (fuseau horaire non indiqué)
- **Acteur / Groupe :** krybit
- **Secteur :** Services financiers / Distribution de paiements / Accompagnement du désendettement
- **Site web :** [dcpartner.co.za](https://www.dcpartner.co.za/)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Sources publiques :** [Site officiel de DC Partner](https://www.dcpartner.co.za/)

- **Description :**

  DC Partner (Pty) Ltd est une agence sud-africaine de distribution des paiements (Payment Distribution Agency, PDA), basée à George, dans le Western Cape. Selon son profil public, elle figure parmi les quatre PDA agréées par le National Credit Regulator en Afrique du Sud et collecte puis distribue, pour le compte de conseillers en désendettement, les fonds de consommateurs en debt review conformément au National Credit Act. L'entreprise présente également ses services DebiCheck intégrés à FNB, son logiciel Finwise Debt Management, ses rapports et métriques, la vérification de prestataires et son réseau de représentants nationaux. Son profil indique qu'elle sert des centaines de conseillers en dette et emploie plus de 65 personnes.

- **Analyse :**

  **Observed :** L'enregistrement source associe krybit à DC Partner, situe la cible en Afrique du Sud et cite www.dcpartner.co.za. Il a été relevé le 2 août 2026 à 14:25:08, sans fuseau horaire indiqué. Le profil public décrit une activité de distribution de fonds liés au debt review et des services de paiement et de gestion associés. Selon le suivi communiqué le 13 septembre 2026, l'échéance de divulgation affichée était dépassée, mais aucune donnée de DC Partner n'était publiquement accessible lors du dernier contrôle rapporté. La date exacte de l'échéance et la date et l'heure du contrôle ne sont pas précisées. Aucun échantillon, volume, catégorie de données ni élément technique n'est disponible pour étayer la revendication.

  **Assumption :** La correspondance du domaine et du profil public rend l'identification de la cible plausible, sans confirmer une compromission. Si des données liées aux paiements et au debt review avaient été exfiltrées, elles pourraient présenter des risques de fraude et d'hameçonnage ciblé ; aucune exposition de ces données n'est toutefois établie. L'absence de publication accessible après l'échéance ne permet pas d'en déterminer la cause. Parmi les hypothèses figurent un règlement, éventuellement avec paiement de rançon par la victime, ou des négociations toujours en cours malgré l'échéance ; un transfert, partage ou revente à un autre groupe criminel, à un tiers ou à une organisation de veille CTI ; un report ou une indisponibilité de la publication ; ou une revendication inexacte ou exagérée. Aucune n'est corroborée par les éléments disponibles.

  **Unknown :** La date exacte de l'échéance, l'heure du dernier contrôle, les systèmes éventuellement touchés, le vecteur d'accès, l'accès non autorisé, l'exfiltration, l'exécution ou le chiffrement d'un ransomware, l'impact opérationnel, la confirmation de la victime et la nature ou l'étendue de données éventuellement concernées restent inconnus. Les négociations, un paiement, un partage privé ou une revente ne sont pas établis.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-02T14:25:08
listing_last_observed_at: 2026-08-02T14:25:08
sample_status: none-observed
deadline_at:
deadline_status: expired
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-13
-->

### 04 août 2026

#### 🇿🇦 Afrique du Sud - Sure Travel

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 04 août 2026 à 15:50:57 (fuseau horaire non indiqué)
- **Acteur / Groupe :** Orova
- **Secteur :** Agence de voyages / Voyages loisirs et professionnels
- **Référence secondaire du jeu source :** emis.com/.../Sure_Travel_Company_Limited (société homonyme enregistrée à Hong Kong)
- **Site web :** [suretravel.co.za](https://www.suretravel.co.za/)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 2
- **Sources publiques :** [Présentation de Sure Travel](https://www.suretravel.co.za/about) | [Profil institutionnel](https://www.linkedin.com/company/sure-travel-pty-ltd)

- **Description :**

  Sure Travel (Pty) Ltd est une marque d'agences de voyages d'Afrique australe proposant des services de voyages loisirs et professionnels. Son site indique plus de 30 ans d'activité et un réseau de plus de 80 agences en Afrique du Sud, en Namibie et au Botswana.

- **Analyse :**

  **Observed :** La fiche de victime a été vérifiée directement sur le site de fuite du groupe Orova. Elle identifie Sure Travel comme une victime sud-africaine, avec un horodatage au 4 août 2026 à 15:50:57. L'enregistrement du jeu source comporte également une URL secondaire renvoyant vers une société homonyme enregistrée à Hong Kong ; cette référence incohérente n'est pas retenue pour l'attribution géographique. Aucun échantillon de données n'était disponible dans les éléments fournis.

  **Assumption :** La publication peut correspondre à une opération d'extorsion visant l'organisation, mais elle ne permet pas à elle seule de confirmer un chiffrement, une exfiltration ou une perturbation opérationnelle.

  **Unknown :** L'accès initial, les systèmes affectés, les données éventuellement obtenues, l'existence d'un chiffrement, tout impact opérationnel et une confirmation de la victime restent inconnus.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-04T15:50:57
listing_last_observed_at: 2026-08-04T15:50:57
sample_status: none-observed
deadline_at:
deadline_status: unknown
disclosure_status: unknown
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-04T15:50:57
-->

#### 🇪🇬 Égypte - ADG Healthcare

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 04 août 2026 à 15:55:39 (fuseau horaire non indiqué)
- **Acteur / Groupe :** Orova
- **Secteur :** Industrie pharmaceutique
- **Domaine également cité dans le jeu source :** www.adg-healthcare.com
- **Site web :** [adghealthcare-eg.com](http://www.adghealthcare-eg.com)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 3
- **Sources publiques :** [Profil institutionnel](https://www.linkedin.com/company/adg-healthcare) | [Référence d'entreprise](https://www.bizmideast.com/EG/adg-healthcare-02-22571600)

- **Description :**

  Les informations publiques relatives à ADG Healthcare au Caire l'associent à Advocure Pharma Group, une entreprise pharmaceutique égyptienne présente notamment dans les domaines cardiovasculaire, génito-urinaire et anti-infectieux. Son profil public renvoie vers adghealthcare-eg.com.

- **Analyse :**

  **Observed :** La fiche de victime a été vérifiée directement sur le site de fuite du groupe Orova. Elle identifie ADG Healthcare comme une victime égyptienne, avec un horodatage au 4 août 2026 à 15:55:39. Le jeu source cite www.adg-healthcare.com, tandis que les profils publics de l'entreprise renvoient vers adghealthcare-eg.com ; cette divergence de domaine demeure documentée. Aucun échantillon de données n'était disponible dans les éléments fournis.

  **Assumption :** La publication peut correspondre à une opération d'extorsion visant l'organisation, mais elle ne permet pas à elle seule de confirmer un chiffrement, une exfiltration ou une perturbation opérationnelle.

  **Unknown :** Le domaine technique effectivement visé, l'accès initial, les systèmes concernés, la nature des données éventuellement obtenues, l'existence d'un chiffrement, une éventuelle perturbation et la confirmation de l'organisation restent inconnus.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-04T15:55:39
listing_last_observed_at: 2026-08-04T15:55:39
sample_status: none-observed
deadline_at:
deadline_status: unknown
disclosure_status: unknown
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-04T15:55:39
-->

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

### 07 août 2026

#### 🇿🇦 Afrique du Sud - Serengeti Golf and Wildlife Estate

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 07 août 2026 à 02:25:08 (fuseau horaire non indiqué)
- **Acteur / Groupe :** krybit
- **Secteur :** Immobilier / Domaine résidentiel et golf
- **Site web :** [serengeti-estates.co.za](https://serengeti-estates.co.za/)
- **Domaine cité par le jeu source :** www.serengetiestates.co.za
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 3
- **Sources publiques :** [Site officiel et coordonnées](https://serengeti-estates.co.za/contact-us/)

- **Description :**

  Serengeti Golf and Wildlife Estate est un domaine résidentiel et golfique haut de gamme situé à Kempton Park, dans le Gauteng, à proximité de Johannesburg et de l'aéroport international OR Tambo. Le site combine immobilier résidentiel, golf et infrastructures de loisirs.

- **Analyse :**

  **Observed :** Le dossier local associé à la publication contient 21 artefacts : 8 JPG, 5 XLSX, 1 XLS, 3 PDF, 3 DOCX et 1 PPTX. Les cinq classeurs XLSX ont été ouverts en lecture seule : 54 feuilles et 53 927 cellules non vides. Ils contiennent 1 643 cellules de formule, non exécutées, et aucun lien externe détecté. Les contenus lisibles couvrent des plannings et heures de housekeeping, des rotations de serveurs, des demandes d'achat et un modèle de réservation, sur des périodes allant de 2017 à 2020. Les trois DOCX comprennent notamment une procédure de périodes de service, un document de peinture et un modèle de réservation avec sept tableaux. Les PDF sont des documents numérisés ; les images JPG et la présentation d'une diapositive n'ont pas permis une qualification textuelle complète. Les empreintes SHA-256 des 21 artefacts ont été calculées localement et conservées hors dépôt.

  **Assumption :** La cohérence des plannings, procédures, formulaires d'achat, réservations et supports visuels avec l'activité d'un domaine résidentiel et golfique rend plausible l'association du corpus à l'environnement de la victime. L'échantillon est suffisamment structuré pour relever la confiance dans son authenticité et son attribution, mais il ne confirme ni le vecteur d'accès, ni l'exfiltration, ni le chiffrement, ni l'origine exacte de chaque fichier.

  **Unknown :** Le nombre de personnes concernées, la présence exacte de données personnelles ou financières dans les documents numérisés et images, les systèmes sources, la méthode d'acquisition, la date d'accès, l'étendue de l'exfiltration, l'impact opérationnel, la confirmation de la victime et toute divulgation complète restent inconnus. L'analyse est limitée aux structures lisibles et aux métadonnées des fichiers ; les cellules de formule n'ont pas été recalculées et aucun contenu sensible brut n'est reproduit.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-07T02:25:08
listing_last_observed_at: 2026-08-07T02:25:08
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-04
-->

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
- **Secteur :** Développement de la jeunesse / Services à l'emploi
- **Domaine historique de support :** `mpowa.mobi` (instance de préproduction citée : `staging.mpowa.mobi`)
- **Statut AFRINTEL :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Très élevé
- **Niveau d'impact :** Niveau 4

- **Description :**

  mPowa est une plateforme sud-africaine de développement de la jeunesse et de services à l’emploi, développée par mLab South Africa, une organisation à but non lucratif. Elle fait partie du SA Youth Network. La Présidence sud-africaine indique qu’elle a été développée par mLab en partenariat avec le Department of Science and Innovation et lancée dans le cadre de l’intervention présidentielle pour l’emploi des jeunes. Il s’agit donc d’un service d’emploi des jeunes lié à une initiative publique, et non d’une administration gouvernementale.

- **Vérification publique :**

  La fiche Google Play attribue l’application à mLab South Africa et utilise `app@mpowa.mobi` comme adresse de support, ce qui relie historiquement le domaine au service. Lors de la vérification du 14 septembre 2026, la racine `mpowa.mobi` affichait un contenu de casino en coréen sans rapport avec mPowa. Ce contenu actuel n’est pas attribué au programme historique et l’opérateur actuel du domaine reste inconnu.

  Sources : [Présidence sud-africaine](https://www.thepresidency.gov.za/virtual-address-president-cyril-ramaphosa-occasion-youth-day-16-june-2021) · [mLab South Africa](https://mlab.co.za/what-we-do/tech-solutions/) · [Fiche Google Play de mPowa](https://play.google.com/store/apps/details?hl=en&id=com.mlab.mpowa)

- **Analyse :**

  AFRINTEL a examiné une publication du 7 août 2026 par l'acteur exfilar (compte de forum de niveau VIP), intitulée « mpowa.mobi - 2,585 Youth CVs Exposed via 0day Firebase Scanner », et a obtenu de façon indépendante l'export de la base de données Firebase Realtime Database référencée dans la publication. L'acteur affirme que la base RTDB Firebase de préproduction de la plateforme (staging.mpowa.mobi) était librement accessible en lecture, sans authentification, jeton ni vérification de referer, et qu'un outil de scan propriétaire l'a identifiée.

  L'examen par AFRINTEL de la base exportée confirme les chiffres annoncés dans la publication : 2 585 CV/curriculum vitae complets, 26 675 points de géolocalisation de prestations de services, 11 fiches d'un annuaire de prestataires de services, 19 comptes utilisateurs de la plateforme et 3 entrées de clés d'accès API. Chaque CV comprend un bloc d'informations personnelles (nom complet, téléphone, email, date de naissance, genre, nationalité, statut marital, statut de handicap, code de permis de conduire, plus haut diplôme), ainsi que des sections qualification, expérience professionnelle, langues, compétences et références personnelles ; ces dernières exposent en outre le nom, l'employeur, le poste et le numéro de téléphone de tiers désignés comme référents. Les 19 comptes utilisateurs incluent le nom complet, la date de naissance et les coordonnées géographiques de membres du personnel de la plateforme. Le jeu de données contient également 3 clés d'accès API d'apparence active, accompagnées de libellés descriptifs.

  La combinaison d'un statut de handicap, d'une date de naissance et de données d'identité complètes pour des mineurs et jeunes demandeurs d'emploi nommément identifiés constitue une catégorie spéciale de données personnelles au sens du cadre sud-africain POPIA. L'exposition de la base de préproduction d'une plateforme de services à l’emploi des jeunes liée à une initiative publique, incluant des clés API actives, crée un risque significatif de détournement d'identifiants contre l'infrastructure associée, en plus des risques de fraude à l'identité, de phishing ciblé et d'atteinte à la sécurité physique des jeunes concernés et des tiers cités en référence. Le nom d'hôte de préproduction suggère qu'un environnement de production correspondant pourrait exister, avec une exposition similaire voire supérieure. La correspondance exacte entre les chiffres publiés par l'acteur et ceux observés indépendamment dans l'export examiné justifie un niveau de confiance très élevé. AFRINTEL ne reproduit aucun nom de candidat, coordonnée, date de naissance, déclaration de handicap, information de référence, dossier de personnel ni clé API issu des éléments examinés.

  La publication complète présente mpowa.mobi comme l'élément « 11/25 » d'une campagne en cours, décrivant un outil propriétaire (« CredHarvest V6 ») utilisé pour scanner et collecter en masse des instances Firebase Realtime Database mal configurées, et affirmant que des centaines de bases similaires ont déjà été récupérées par la même méthode. L'acteur propose à la fois la vente de cet outil de scan et des services d'intrusion/d'accès payants distincts sur le même forum. Cela indique que mpowa.mobi est une victime parmi une campagne plus large et systématique visant des déploiements Firebase mal configurés, et que des expositions comparables touchent vraisemblablement d'autres organisations africaines utilisant le même backend, indépendamment de tout ciblage spécifique à mpowa.mobi.

### 08 août 2026
#### 🇳🇬 Nigeria - Daily Trust

- **Date de l'incident :** Non précisée
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
- **Sources publiques :** [Présentation de Daily Trust](https://dailytrust.com/about-us)

- **Description :**

  Daily Trust est une marque d'information nigériane publiée par Media Trust Limited. Le groupe exerce dans l'édition, l'impression et les services médias et exploite un ensemble plus large comprenant les titres Daily Trust ainsi que Trust TV et Trust Radio, avec des implantations notamment à Abuja.

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

### 14 août 2026

#### 🇲🇦 Maroc - AVANTA Maroc

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 14 août 2026 à 05:55:47 (fuseau horaire non indiqué)
- **Acteur / Groupe :** thegentlemen
- **Secteur :** Services de ressources humaines
- **Site web :** [avanta.ma](https://www.avanta.ma/)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Sources publiques :** [Profil institutionnel AVANTA Maroc](https://www.linkedin.com/company/avanta-maroc-sa)

- **Description :**

  AVANTA Maroc est une entreprise marocaine de services de ressources humaines basée à Casablanca. Son profil institutionnel indique une activité depuis 1991 et des services de recrutement, de travail temporaire, d'externalisation, de gestion de contrats et de développement RH, avec un réseau couvrant plusieurs grands pôles économiques du Maroc.

- **Analyse :**

  **Observed :** L'enregistrement source fourni associe thegentlemen à « Avanta Maroc Ex Adecco », cite avanta.ma et situe la cible au Maroc. Il est horodaté au 14 août 2026 à 05:55:47, sans fuseau horaire indiqué. La marque publique actuelle est AVANTA Maroc. La source ne fournit ni échantillon, ni volume, ni catégorie de données, ni preuve technique de compromission.

  **Assumption :** La concordance du nom, du domaine et du pays rend l'identification de la cible plausible. Les activités RH impliquent potentiellement des données de candidats, d'employés ou de clients, mais aucune exposition de ce type n'est établie.

  **Unknown :** L'accès initial, les systèmes affectés, le chiffrement, l'exfiltration, l'impact opérationnel, la confirmation de la victime et l'état de publication restent inconnus.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-14T05:55:47
listing_last_observed_at: 2026-08-14T05:55:47
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-14T05:55:47
-->

### 16 août 2026
#### 🇿🇦 Afrique du Sud - The Courier Guy

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 16 août 2026 à 15:19:49 (fuseau horaire non affiché)
- **Date de détection AFRINTEL :** 19 août 2026
- **Acteur / Groupe :** medusalocker
- **Secteur :** Messagerie / Logistique
- **Site web :** [thecourierguy.co.za](https://thecourierguy.co.za)
- **Sources publiques :** [Présentation de The Courier Guy](https://mail.thecourierguy.co.za/about-us/) | [Site officiel](https://thecourierguy.co.za/)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d’incident :** Ransomware
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4

- **Description :**

  The Courier Guy est une entreprise sud-africaine de messagerie et de livraison de colis destinée aux particuliers et aux entreprises, avec un réseau de dépôts, de kiosques, de consignes et de chauffeurs. Sa présentation publique indique environ 25 ans d'activité et plus de 21 millions de livraisons réalisées en 2024.

- **Analyse :**

  **Observed :** Le dossier local contient 10 artefacts : six CSV et quatre XLSX. Les six CSV ont été analysés intégralement en lecture seule : 1 269 lignes de données, quatre lignes de métadonnées par fichier et 36 colonnes. Les champs comprennent notamment le nom du bénéficiaire, le compte bancaire du bénéficiaire, le type de compte, le code agence, le montant, les références et des canaux de notification par e-mail, fax et SMS. L'ensemble représente 255 noms de bénéficiaires distincts et 236 comptes distincts ; aucun doublon de ligne exact n'a été observé à l'intérieur des fichiers. Les quatre XLSX contiennent chacun 20 feuilles de calendriers de paiements locatifs. 3 409 cellules de formule ont été détectées et aucune n'a été exécutée. Des composants de liens externes sont présents dans trois des quatre classeurs ; aucun lien n'a été suivi. Les noms de fichiers couvrent des lots de juillet et août 2025 ainsi que de janvier, février et avril 2026 ; une feuille intitulée 1 August 2011 révèle aussi la présence d'un élément historique ou réutilisé. Les empreintes SHA-256 des 10 artefacts ont été calculées localement et conservées hors dépôt.

  **Assumption :** La structure homogène des fichiers, la répétition des calendriers locatifs et la présence de données de paiement et de contact rendent plausible l'association du corpus à l'environnement opérationnel de The Courier Guy. L'échantillon est suffisamment structuré pour relever la confiance dans son authenticité et son attribution. Il pourrait faciliter la fraude au paiement, l'usurpation de bénéficiaires ou de fournisseurs, le phishing ciblé et des attaques contre des comptes, mais il ne confirme ni le vecteur d'accès, ni l'exfiltration, ni l'action de medusalocker.

  **Unknown :** Le nombre exact de personnes et d'organisations concernées, l'actualité des comptes et coordonnées, les systèmes sources, la méthode d'acquisition, la date d'accès, l'étendue de l'exfiltration, l'impact opérationnel, la confirmation de la victime et la publication complète restent inconnus. Les périodes anciennes ou les feuilles héritées peuvent ne plus refléter l'état actuel. L'analyse n'a pas recalculé les formules, n'a pas suivi les liens externes et ne reproduit aucune donnée financière ou personnelle brute.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-16T15:19:49
listing_last_observed_at: 2026-08-19T05:35:53+01:00
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-04
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

- **Date de l'incident :** 26 juin 2026, date alléguée par l'acteur
- **Date de publication initiale :** 18 août 2026
- **Date de détection de la source :** 18 août 2026 à 10:27:05 (fuseau horaire non indiqué)
- **Date de détection AFRINTEL :** 18 août 2026
- **Acteur / Groupe :** incransom
- **Secteur :** Services financiers / Administration de fonds
- **Site web :** [spearfin.net](https://spearfin.net)
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 4
- **Sources publiques :** [Site officiel de SpearFin](https://spearfin.net/) | [Services d'administration de fonds](https://spearfin.net/fund-administration/)

- **Description :**

  SpearFin Ltd est une société mauricienne de services financiers et de gestion réglementée par la Financial Services Commission de Maurice. Elle fournit des services d'administration de fonds, des services aux entreprises, de conformité et d'accompagnement des investisseurs. Ses informations publiques indiquent plus de 10 milliards USD d'actifs sous administration.

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

### 19 août 2026

#### 🇿🇦 Afrique du Sud - Babcock Africa

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 19 août 2026 à 08:10:32 (fuseau horaire non indiqué)
- **Acteur / Groupe :** thegentlemen
- **Secteur :** Ingénierie / Services industriels / Soutien à la défense
- **Site web :** [babcock.co.za](https://www.babcock.co.za/)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 4
- **Sources publiques :** [Présentation de Babcock Africa](https://www.babcock.co.za/about/) | [Services d'ingénierie](https://www.babcock.co.za/products-and-services/engineered-solutions/6/)

- **Description :**

  Babcock Africa est une division de Babcock International qui fournit des services d'ingénierie critique et de gestion d'équipements industriels en Afrique. Ses activités couvrent notamment les solutions de transport, le soutien à la production d'énergie, l'ingénierie industrielle, les équipements pour les secteurs minier et de la construction, ainsi que des capacités spécialisées dans l'ingénierie marine et liée à la défense.

- **Analyse :**

  **Observed :** L'enregistrement source fourni associe thegentlemen à Babcock, cite babcock.co.za et situe la cible en Afrique du Sud. Il est horodaté au 19 août 2026 à 08:10:32, sans fuseau horaire indiqué. Le secteur source « industrie de la défense » ne couvre qu'une partie des activités publiques de Babcock Africa. Aucun échantillon, volume, catégorie de données, échéance ou élément technique n'est fourni.

  **Assumption :** La concordance du domaine et du profil d'activité rend l'identification de la cible plausible. Une compromission confirmée pourrait avoir des conséquences importantes en raison des services d'ingénierie et de soutien à des secteurs critiques, mais aucun impact n'est établi dans les éléments fournis.

  **Unknown :** Les méthodes d'accès et d'acquisition, les environnements concernés, le chiffrement, la perturbation opérationnelle, la divulgation et une éventuelle confirmation de Babcock restent inconnus.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-19T08:10:32
listing_last_observed_at: 2026-08-19T08:10:32
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-19T08:10:32
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


#### 🇨🇲 Cameroun - CCA Bank
* **Date de l'incident :** Non précisée
* **Date de publication initiale :** 20 août 2026
* **Date de détection de la source :** 20 août 2026 à 13:54:00 (fuseau horaire non indiqué)
* **Date de détection AFRINTEL :** 20 août 2026
* **Acteur / Groupe :** Everest
* **Secteur :** Banque / Services financiers
* **Site web :** [cca-bank.com](https://www.cca-bank.com/)
* **Statut AFRINTEL :** Claim - Unverified
* **Type d'incident :** Ransomware
* **Niveau de confiance :** Moyen
* **Niveau d'impact :** Niveau 4
* **Sources publiques :** [Présentation de CCA Bank](https://www.cca-bank.com/fr) | [Site officiel](https://www.cca-bank.com/)
* **Description :**
  CCA Bank, ou Crédit Communautaire d'Afrique-Bank, est un établissement bancaire camerounais dont la direction générale est située à Douala-Bonanjo. Son site public présente des services bancaires et financiers destinés aux particuliers et aux entreprises, notamment des solutions de compte, de paiement et de financement.

* **Analyse :**
  **Observed :** Le 20 août 2026, AFRINTEL a observé une publication attribuée au groupe Everest visant `cca-bank.com`. Au moment de l'observation, la fiche de la victime affichait encore un compte à rebours avant la publication annoncée des données, indiquant que la phase d'extorsion était toujours en cours.

  L'inventaire technique disponible recense **11 837 fichiers représentant 18,92 Go**, auxquels s'ajoutent **17 archives RAR imbriquées totalisant 120,31 Mo** dont les fichiers internes n'ont pas été comptabilisés. Le volume total connu atteint ainsi environ **19,04 Go**.

  Les catégories recensées couvrent plusieurs fonctions sensibles de l'activité bancaire : dossiers de crédit et analyses de financement, portefeuilles et expositions clients, données financières et de trésorerie, reporting prudentiel, documents réglementaires liés notamment à la COBAC, dossiers AML/KYC et LAB/FT, documents d'identité, éléments juridiques et de recouvrement, données RH, procédures internes, documentation SI, gestion des habilitations et des accès, ainsi que des fichiers de migration et de rapprochement de systèmes bancaires.

  Plusieurs fichiers décrits dans l'inventaire correspondent à des exports structurés de grande taille. Un classeur réglementaire contient notamment une table de base clientèle de **591 799 lignes**, une table relative aux dépôts de personnes physiques de **489 155 lignes** et une table d'engagements clientèle de **350 011 lignes**. Un autre export relatif aux crédits contient **250 688 lignes** et **67 973 identifiants clients uniques**. Des fichiers de rapprochement et de migration V10/V11 comportent également plusieurs centaines de milliers à plusieurs millions de lignes.

  **Assumption :** La profondeur fonctionnelle et la cohérence des catégories décrites dans l'inventaire sont compatibles avec un corpus provenant d'environnements métiers et techniques d'une institution bancaire. Si l'ensemble est authentique, l'exposition potentielle dépasse largement une simple fuite documentaire et pourrait concerner des données clients, financières, réglementaires, KYC, opérationnelles et techniques.

  La combinaison de données d'identité, d'informations de crédit, de données financières et de documentation interne pourrait faciliter des opérations de **spear-phishing, fraude financière, usurpation d'identité, fraude documentaire, compromission de comptes et ciblage secondaire de clients, employés, fournisseurs ou partenaires**.

  Les documents relatifs aux systèmes d'information, aux habilitations, aux procédures VPN, à la gestion des comptes et aux migrations pourraient également fournir à d'autres acteurs malveillants des informations utiles pour comprendre certains processus internes et préparer des attaques ultérieures.

  **Unknown :** AFRINTEL n'a pas examiné directement l'intégralité des **11 837 fichiers bruts** revendiqués. L'analyse repose sur la publication Everest et sur l'inventaire technique disponible. Le vecteur d'accès initial, la date réelle de compromission, les systèmes précisément affectés, la méthode d'exfiltration, l'existence éventuelle d'un chiffrement, l'étendue exacte de l'accès obtenu par Everest et une éventuelle confirmation officielle de CCA Bank restent inconnus.

  Le compte à rebours observé indique une publication annoncée, mais ne permet pas d'établir si les données seront effectivement divulguées, si une négociation est en cours ou si un accord a été conclu entre la victime et les attaquants.

  AFRINTEL ne reproduit aucune donnée personnelle, information bancaire, pièce d'identité, identifiant, donnée d'accès ou autre information sensible issue du corpus décrit.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-20T13:54:00
listing_last_observed_at: 2026-08-20T13:54:00
sample_status: none-observed
deadline_at:
deadline_status: active
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-20T13:54:00
-->

---
### 22 août 2026
#### 🇲🇦 Maroc - RAMED (Régime d’Assistance Médicale)

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** 22 août 2026

- **Acteur / Groupe :** JBT2026
- **Secteur :** Gouvernement / Administration
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High
- **Site web:** [sante.gov.ma](https://www.sante.gov.ma)
- **Domaine historique:** `ramed.ma` *(inactive)*

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

#### 🇿🇦 Afrique du Sud - Furniture Bargaining Council

- **Date de l'incident :** Août 2026, date exacte non communiquée publiquement
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 24 août 2026 à 21:21:08 (fuseau horaire non indiqué)
- **Acteur / Groupe :** Deadlock, auteur de la revendication, sans attribution par la victime
- **Secteur :** Relations sociales / Gouvernance du secteur du meuble
- **Site web :** [fbcweb.furnbed.co.za](https://fbcweb.furnbed.co.za/)
- **Statut AFRINTEL :** Victim Confirmed
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Très élevé
- **Niveau d'impact :** Niveau 4
- **Sources publiques :** [Notification officielle et site du Conseil](https://fbcweb.furnbed.co.za/) | [Présentation du Conseil](https://fbcweb.furnbed.co.za/what.php)

- **Description :**

  Le Furniture Bargaining Council est un conseil sud-africain de négociation collective pour l'industrie de la fabrication de meubles. Sa mission comprend la promotion d'une négociation collective ordonnée, de la paix sociale, de la résolution des conflits et de la gouvernance sectorielle.

- **Analyse :**

  **Observed :** Le corpus local associé à la divulgation contient 69 artefacts pour environ 94,6 Mo : 22 PDF, 13 XLSX, 31 DOCX, 2 DOCM et 1 DOC. Douze classeurs XLSX lisibles totalisent 134 feuilles et 78 605 cellules de formule détectées ; aucune formule n'a été exécutée. Des composants de liens externes sont présents dans quatre classeurs ; aucun lien n'a été suivi. Un classeur XLSX supplémentaire, chiffré au format CDFV2, n'a pas pu être ouvert. Les données et documents observés couvrent des packs financiers, suivis de caisse, comptes e-wallet, formulaires bancaires, rapprochements fiscaux SARS, prêts, avertissements disciplinaires, audits IT, rapports de sécurité, documents d'identité et documents personnels ou administratifs. En parallèle, la notification officielle du Conseil confirme un incident ayant chiffré certains serveurs.

  L'examen structurel et textuel des documents lisibles confirme la présence de catégories financières, fiscales, bancaires, RH, identitaires et opérationnelles. Il établit qu'un corpus de données a été divulgué ou rendu accessible, mais ne permet pas de déterminer si chaque fichier provient directement des systèmes du Conseil ni si l'ensemble a été acquis lors du même événement. Les PDF et documents contenant potentiellement des informations personnelles n'ont pas été reproduits.

  **Assumption :** La confirmation officielle du chiffrement établit l'incident et justifie le statut Victim Confirmed. La cohérence du corpus documentaire avec les activités administratives et financières du FBC renforce fortement son attribution à l'environnement de la victime. La présence de données financières, fiscales, bancaires, d'identité et de personnel justifie un impact de niveau 4. Elle ne confirme ni le vecteur d'accès, ni l'exfiltration de chaque fichier, ni la responsabilité technique de Deadlock.

  **Unknown :** Le nombre exact de personnes concernées, les systèmes sources, la méthode et la date d'acquisition, l'étendue complète de la divulgation, l'actualité des données, l'attribution technique à Deadlock, les conséquences opérationnelles et les notifications aux personnes concernées restent inconnus. Le classeur chiffré, les liens externes et les contenus visuels ou numérisés n'ont pas été ouverts ou suivis.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-24T21:21:08
listing_last_observed_at: 2026-08-24T21:21:08
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: confirmed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-04
-->

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

---
### 26 août 2026

#### 🇪🇬 Égypte - Mima Foods

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 26 août 2026 à 15:29:13 (fuseau horaire non indiqué)
- **Acteur / Groupe :** krybit
- **Secteur :** Industrie agroalimentaire / Export de produits surgelés
- **Site web :** [mimafoods.net](https://mimafoods.net/)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 2
- **Sources publiques :** [Site officiel](https://mimafoods.net/) | [Profil de l'entreprise](https://mimafoods.net/company-profile/)

- **Description :**

  Mima Foods est un producteur et exportateur égyptien de fruits et légumes IQF, avec une usine à Sadat City et un siège au Caire. Son site indique qu'il fournit des distributeurs, des industriels agroalimentaires et des marques de distributeur dans plus de 45 pays.

- **Analyse :**

  **Observed :** L'enregistrement source fourni associe krybit à mimafoods.net et situe la cible en Égypte. Il est horodaté au 26 août 2026 à 15:29:13, sans fuseau horaire indiqué. Selon le suivi communiqué le 12 septembre 2026, l'échéance affichée était dépassée et aucune donnée ni aucun échantillon n'était accessible publiquement lors du dernier contrôle. L'heure du contrôle et la date exacte de l'échéance ne sont pas précisées. Aucun élément technique ne confirme l'accès, l'exfiltration ou le chiffrement.

  **Assumption :** La correspondance exacte du domaine avec le site officiel rend l'identification de la cible plausible. Elle ne confirme ni l'accès, ni l'exfiltration, ni le chiffrement. L'absence de données accessibles après l'échéance peut correspondre à un accord ou à des négociations, avec ou sans paiement, un transfert, partage ou revente des données, un report, une indisponibilité de la fiche ou du lien, ou une revendication inexacte ou exagérée. Ce sont des hypothèses, aucune n'est établie. Les divulgations attribuées aux autres victimes de Krybit ne prouvent pas un transfert des données de Mima Foods.

  **Unknown :** Les systèmes éventuellement affectés, le vecteur d'accès, la portée opérationnelle, la nature des données, la confirmation de la victime, l'accès et l'exfiltration ne sont pas établis. La date exacte de l'échéance, la cause de l'absence de divulgation publique, tout partage privé, les négociations, un paiement ou une revente restent inconnus.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-26T15:29:13
listing_last_observed_at: 2026-08-26T15:29:13
sample_status: none-observed
deadline_at:
deadline_status: expired
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-12
-->

#### 🇬🇦 Gabon - Conseil Gabonais des Chargeurs (CGC) [Ransomware]

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 26 août 2026 à 15:56:16 (fuseau horaire non indiqué)
- **Acteur / Groupe :** KRYBIT
- **Secteur :** Administration publique / Transport et logistique
- **Site web :** [cgcgabon.ga](https://cgcgabon.ga/)
- **Domaine cité par le jeu source :** cgcgabon.com
- **Statut AFRINTEL :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Effet associé :** Exposition et divulgation de données
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Sources publiques :** [Site officiel du Conseil Gabonais des Chargeurs](https://cgcgabon.ga/)

- **Description :**

  Le Conseil Gabonais des Chargeurs (CGC) est un organisme public gabonais intervenant dans l'encadrement, l'assistance et la régulation des activités liées aux chargeurs, au transport et aux flux de marchandises.

- **Données exposées dans les lots analysés :**

  - données RH nominatives, notamment noms, matricules, numéros CNSS, numéros de téléphone, dates de naissance, fonctions et informations professionnelles ;
  - fiches d'évaluation individuelle et documents de gestion des carrières ;
  - organigrammes, cartographies de postes et fiches de fonction décrivant les relations hiérarchiques ;
  - informations sur la Direction des Opérations des Systèmes d'Information, les administrateurs systèmes, les bases de données, le support IT et la cybersécurité ;
  - éléments relatifs à l'environnement Active Directory interne, dont le domaine `cgc.local`, plusieurs contrôleurs de domaine, la topologie de réplication, des rôles Active Directory et des données d'administration, exposés notamment dans un artefact PowerShell ;
  - processus métier liés au BIETC/GECOP, aux importateurs, exportateurs, chargeurs, opérations de fret aérien et bases d'infractions ;
  - documents concernant la finance et la comptabilité, la communication, les relations publiques, les affaires juridiques et les représentations régionales ;
  - projets et versions préliminaires d'organisation interne.

- **Analyse :**

  L’analyse de plusieurs lots de fichiers attribués à la divulgation revendiquée par KRYBIT met en évidence une fuite documentaire interne de grande ampleur et transversale. Le corpus couvre les ressources humaines, les systèmes d'information, la cybersécurité, les bases de données, la stratégie, les opérations de fret aérien, les processus BIETC/GECOP, les affaires juridiques, la finance, la communication institutionnelle et certaines représentations régionales. Les documents présentent une forte cohérence de forme, de nomenclature, de hiérarchie et de processus internes, ce qui confère un niveau de confiance très élevé quant à leur origine CGC.

  **Observed :** Le recoupement de plusieurs lots attribués à la divulgation revendiquée par KRYBIT révèle un corpus documentaire interne couvrant les ressources humaines, la DOSI, la stratégie et l'observatoire multimodal, le Bureau Aéroport, les affaires juridiques, la communication, la finance/comptabilité et une représentation régionale à Port-Gentil. La cohérence des modèles, intitulés de postes, hiérarchies, références internes et processus renforce fortement l'association des documents au CGC.

  Un artefact PowerShell contenant des sorties de `repadmin` et `dcdiag`, daté du 22 février 2026, expose le domaine Active Directory `cgc.local`, trois contrôleurs de domaine, la topologie de réplication et les rôles AD, concentrés sur un contrôleur. Le résumé de réplication de cet instantané indique zéro échec ; il ne décrit que l'état observé à cette date. Les fiches de poste de la DOSI détaillent les responsabilités d'administration des bases et des systèmes, de sécurité informatique, de réseaux et de support. Le corpus décrit aussi les processus BIETC/GECOP, les importateurs/exportateurs, manifestes, mouvements de fret et infractions, ainsi que des fonctions d'assistance aux chargeurs, de régulation du fret aérien, de finance, de communication et de relations régionales.

  Les éléments disponibles corroborent fortement la divulgation de documents internes du CGC et fournissent une vue détaillée de son organisation, de ses responsabilités et de certains processus techniques et métiers. Aucun identifiant n'est signalé comme présent en clair dans les éléments étudiés. Les documents consultés décrivent le modèle fonctionnel des bases BIETC/GECOP et d'infractions, mais aucun dump complet de ces bases n'a été observé.

  Des événements système comportant des erreurs DCOM répétées liées au niveau d'authentification figurent également dans l'artefact. Ils peuvent résulter d'opérations d'administration légitimes, de maintenance ou d'une incompatibilité de configuration et ne constituent pas, à eux seuls, une preuve d'activité malveillante ni un lien avec le ransomware.

  **Assumption :** L'étendue et la diversité du corpus sont compatibles avec une collecte depuis un espace documentaire transverse, un partage réseau, une GED ou une sauvegarde accessible à plusieurs directions. Cette origine reste une hypothèse : les artefacts ne révèlent pas le point de collecte initial. Si elles sont exploitées après un accès initial, les informations organisationnelles et techniques peuvent réduire l'effort de reconnaissance et faciliter le ciblage des fonctions IT, RH, sécurité, finance, des partenaires et des représentations régionales.

  **Unknown :** Le vecteur d'accès initial, le système source, l'étendue complète de l'exfiltration, l'existence d'un dump complet BIETC/GECOP, l'exécution du ransomware, le mécanisme de chiffrement, l'impact opérationnel et toute confirmation officielle de la victime restent inconnus. L'attribution à KRYBIT repose sur la revendication du groupe. Les documents analysés corroborent l'exfiltration, mais ne suffisent pas à démontrer le vecteur, l'exécution ou le chiffrement du ransomware.

  La cohérence et la diversité des documents conduisent à évaluer comme **très élevée** l'authenticité probable du corpus et son association au CGC. Cette appréciation ne constitue pas une confirmation officielle de l'incident ni de l'attribution à KRYBIT.
- **Risques :**
  - spear-phishing ciblant les employés et responsables ;
  - usurpation d'identité et fraude sociale ;
  - ciblage ou compromission de comptes privilégiés ;
  - ingénierie sociale contre les fonctions IT, RH, finance et direction ;
  - fraude au président (BEC) et usurpation de dirigeants ;
  - usurpation des communications institutionnelles ;
  - ciblage des importateurs, exportateurs, chargeurs et partenaires ;
  - exploitation secondaire des informations Active Directory ;
  - renseignement économique à partir des documents juridiques, organisationnels et stratégiques ;
  - attaques secondaires contre les représentations régionales et les partenaires du CGC.

- **Évaluation AFRINTEL :**
  - **Cohérence interne du corpus :** Très élevée
  - **Authenticité probable des documents CGC :** Très élevée
  - **Étendue de la fuite :** Multi-directionnelle
  - **Exposition organisationnelle :** Critique
  - **Exposition Active Directory / infrastructure :** Critique
  - **Exposition des processus métier :** Élevée à critique
  - **Exposition RH :** Élevée
  - **Renseignement économique :** Élevé
  - **Identifiants en clair :** Non observés dans les éléments étudiés
  - **Dump complet BIETC/GECOP :** Non observé à ce stade
  - **Vecteur initial :** Non établi
  - **Chiffrement ransomware :** Non démontré par les documents eux-mêmes
  - **Confirmation officielle de la victime :** Non observée

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-26T15:56:16
listing_last_observed_at: 2026-08-26T15:56:16
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: release-reviewed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-26T15:56:16
-->

### 27 août 2026

#### 🇿🇦 Afrique du Sud - Hungry Lion

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 27 août 2026 à 06:27:50 (fuseau horaire non indiqué)
- **Acteur / Groupe :** medusalocker
- **Secteur :** Restauration / Restauration rapide
- **Site web :** [hungrylion.co.za](https://www.hungrylion.co.za/)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Faible
- **Niveau d'impact :** Niveau 3
- **Sources publiques :** [Présentation de Hungry Lion](https://www.hungrylion.co.za/about/) | [Informations juridiques](https://www.hungrylion.co.za/legal/)

- **Description :**

  Hungry Lion est une chaîne sud-africaine de restauration rapide spécialisée dans le poulet frit, les burgers et les produits associés. L'entreprise indique avoir ouvert son premier restaurant à Stellenbosch en 1997, puis s'être développée dans plusieurs marchés africains. Elle a annoncé l'ouverture de son 500e restaurant en 2025.

- **Analyse :**

  **Observed :** L'enregistrement source fourni associe medusalocker à Hungry Lion et situe la cible en Afrique du Sud. Il est horodaté au 27 août 2026 à 06:27:50, sans fuseau horaire indiqué. La description source revendique 111 établissements dans sept pays et cite trois environnements de point de vente, Unity POS, GAAP POS et CoSoft POS, avec quelques volumes ou fréquences d'exploitation. Elle se termine toutefois par la mention « Botswana », ce qui laisse la portée géographique exacte de la publication ambiguë. Aucun échantillon ou élément technique n'est fourni.

  **Assumption :** Les informations publiques confirment que Hungry Lion est une chaîne régionale dont le siège est en Afrique du Sud, mais elles ne valident pas les chiffres ni les systèmes décrits dans la revendication. Si un environnement de point de vente était compromis, des risques opérationnels et de fraude pourraient en découler.

  **Unknown :** L'entité juridique ou le pays précisément visé, l'accès initial, les terminaux ou serveurs concernés, l'exfiltration, le chiffrement, l'impact opérationnel, la confirmation de la victime et toute divulgation restent inconnus.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-27T06:27:50
listing_last_observed_at: 2026-08-27T06:27:50
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-27T06:27:50
-->

#### 🇿🇦 Afrique du Sud - Rohloff Group

- **Date de l'incident :** Non précisée
- **Date de publication initiale :** Non précisée
- **Date de détection de la source :** 27 août 2026 à 14:31:07 (fuseau horaire non indiqué)
- **Acteur / Groupe :** incransom
- **Secteur :** Restauration / Restauration rapide
- **Site web :** [Site carrière du Rohloff Group](https://rohloff-group.breezy.hr/)
- **Statut AFRINTEL :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Moyen
- **Niveau d'impact :** Niveau 4
- **Sources publiques :** [Profil institutionnel](https://www.linkedin.com/company/rohloff-group/?originalSubdomain=za) | [Site carrière géré par l'entreprise](https://rohloff-group.breezy.hr/)

- **Description :**

  Rohloff Group est un opérateur sud-africain de restauration et l'un des plus grands groupes franchisés KFC en Afrique. Fondé en 1981 et basé à Somerset West, dans le Cap-Occidental, il exploite un réseau de restaurants KFC soutenu par un centre de support aux restaurants.

- **Analyse :**

  **Observed :** L'enregistrement source fourni associe incransom à Rohloff Group et situe la cible en Afrique du Sud. Il est horodaté au 27 août 2026 à 14:31:07, sans fuseau horaire indiqué. L'acteur revendique 536 Go, 103 196 fichiers et 30 805 dossiers. Il affirme que le corpus comprend des informations personnelles et bancaires d'employés, des demandes de prêt, des pièces d'identité, des relevés bancaires, des reconnaissances de dette, des résultats d'audiences disciplinaires et des documents financiers relatifs aux redevances et aux coûts alimentaires. La publication annonce une divulgation complète ultérieure.

  Aucun échantillon ou fichier source n'accompagne les éléments fournis. Les volumes et catégories restent donc des affirmations de l'acteur.

  **Assumption :** La précision du nom et du profil de la victime rend la publication ciblée, mais ne confirme pas la compromission. Si les catégories annoncées sont authentiques, la combinaison de données d'identité, bancaires, RH et disciplinaires créerait un risque élevé d'usurpation, de fraude financière, de phishing ciblé et d'atteinte à la vie privée des employés.

  **Unknown :** L'accès initial, les systèmes touchés, l'exfiltration, le chiffrement, la validité des volumes, l'existence d'une publication accessible, la confirmation de la victime, la négociation, le paiement et la revente restent inconnus.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-27T14:31:07
listing_last_observed_at: 2026-08-27T14:31:07
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-27T14:31:07
-->

### 29 août 2026
#### 🇱🇾 Libye - Albarq Media Service / شركة البرق للاتصالات والتقنية

* **Période de l'incident :** Juin 2026, date exacte non établie
* **Date de publication initiale :** 09 juin 2026
* **Date de découverte AFRINTEL :** 29 août 2026
* **Acteur / Groupe :** Richard2002
* **Secteur :** Télécommunications / Services médias
* **Site web :** [albarq.ly](https://albarq.ly/)
* **Statut :** Claim - Data Sample Published
* **Type d'incident :** Data Leak
* **Niveau de confiance :** Medium
* **Niveau d'impact :** Level 3

* **Description :**
  Albarq Media Service est un service présenté comme lié à شركة البرق للاتصالات والتقنية (Albarq Telecommunications and Technology), opérateur libyen de télécommunications et de services associés.

* **Analyse :**
  Une publication attribuée à Richard2002, datée du 09 juin 2026, propose un échantillon présenté comme issu du service Albarq Media et revendique environ **330 000 comptes**. L'échantillon visible contient **18 lignes** et **24 champs séparés par des points-virgules**. Il comprend des identifiants de comptes, des informations d'abonnement, des dates, des localisations générales et des numéros de téléphone ; aucune donnée personnelle brute n'est reproduite par AFRINTEL.

  Les enregistrements visibles présentent des dates s'étendant d'août 2019 à avril 2025, ainsi que des valeurs d'usage incohérentes ou manquantes dans plusieurs lignes. Le corpus observé ne représente qu'un extrait visible dans la publication et ne permet pas de valider les **330 000 comptes** revendiqués, l'exhaustivité de la fuite, le système source, le vecteur d'accès ou la méthode d'extraction. Le fichier source original n'était pas disponible ; l'analyse est donc limitée aux données visibles dans l'échantillon fourni.

  **Unknown :** aucune confirmation publique indépendante de l'incident par Albarq ou une autorité libyenne n'est établie dans les éléments examinés. La période exacte de l'accès ou de l'exfiltration reste inconnue ; juin 2026 correspond à la date de la publication observée.

* **Recommandations :**
  * Vérifier les journaux d'accès aux plateformes d'abonnement et les exports de données autour du 09 juin 2026.
  * Réinitialiser les sessions et renforcer la surveillance des comptes administratifs si une exposition est confirmée.
