[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL) ![Périmètre](https://img.shields.io/badge/P%C3%A9rim%C3%A8tre-Afrique-orange) ![Diffusion](https://img.shields.io/badge/TLP-CLEAR-green)

# Victimes africaines - Mars 2026 (45 fiches documentaires)
👉🏾 [English version](./victims.md) | [Rapport CTI](./README_FR.md)

## Méthodologie et fiabilité

**45 fiches observées ou indexées en mars 2026 dans 12 pays africains, plus un dossier multi-pays** : 19 revendications ransomware, 24 fuites de données, 1 vente d’accès et 1 fraude opérationnelle. Ces fiches ne démontrent pas 45 compromissions indépendantes. Les dates de **publication initiale**, de **survenue technique**, de **découverte AFRINTEL** et de **mise à jour** doivent être distinguées. Les données anciennes découvertes en mars restent décrites avec leur chronologie propre. La fiche Diesel-Electric peut recouper celle de février ; le dossier Gauteng/Kazu de mai demeure une revendication liée non canonique. La publication de données ou d’un échantillon ne constitue pas une confirmation officielle.

### Types
| Typologie | Fiches | Part |
|---|---:|---:|
| Fuite de données | 24 | 53,3 % |
| Ransomware | 19 | 42,2 % |
| Vente d’accès | 1 | 2,2 % |
| Fraude opérationnelle | 1 | 2,2 % |
| **Total** | **45** | **100 %** |

### Répartition par pays/périmètre
| Pays / zone | Fiches |
|---|---:|
| Afrique du Sud | 17 |
| Maroc | 8 |
| Égypte | 8 |
| Nigeria | 2 |
| Sénégal | 2 |
| Algérie | 1 |
| Guinée | 1 |
| Madagascar | 1 |
| Multi-pays Afrique | 1 |
| Namibie | 1 |
| Tanzanie | 1 |
| Tunisie | 1 |
| Zambie | 1 |
| **Total** | **45** |

> **Revue éditoriale du 6 novembre 2026.** Les corrections de domaines identifient les sites institutionnels ; elles ne valident pas les revendications. Les descriptions historiques sont conservées pour traçabilité, avec compléments CTI signalés. Aucune donnée personnelle ni clé n’est ajoutée.

## Fiches détaillées - Mars 2026

### 01 mars 2026

#### 🇿🇦 Afrique du Sud - Diesel-Electric Group
- **Date de publication initiale :** 1 mars 2026

- **Groupe ransomware :** LockBit 5.0
- **Secteur :** Automobile (Distribution et Services)
- **Site web :** [diesel-electric.co.za](https://diesel-electric.co.za)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Distributeur majeur de composants automobiles en Afrique australe, incluant les franchises Bosch Service et les centres e-CAR.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Revendication publiée sous LockBit 5.0 concernant la même organisation que la fiche de février 2026. Les deux annonces peuvent correspondre à une republication ou à un épisode distinct : ne pas comptabiliser deux intrusions prouvées avant rapprochement des échantillons et des dates. Contrôles prioritaires : journaux d’accès distants, EDR, accès aux sauvegardes et partages documentaires.

#### 🇿🇲 Zambie - ZISPIS (Zambia Integrated Social Protection Information System)
- **Date de publication initiale :** 1 mars 2026

- **Acteur / Groupe :** Spirigatito
- **Secteur :** Gouvernement / Protection sociale
- **Site web :** [mcdss.gov.zm](https://www.mcdss.gov.zm)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Le système ZISPIS, registre national unifié utilisé par le gouvernement zambien pour gérer les programmes de protection sociale, fait l’objet d’une revendication de compromission. L’acteur affirme avoir affecté environ 15 millions de bénéficiaires avec plus de 34 millions d’enregistrements exposés. Les données incluent des informations personnelles complètes (nom, date de naissance, genre, identifiants nationaux), des données socio-économiques détaillées (situation du foyer, niveau d’éducation, conditions de vie), ainsi que des données financières (paiements, cycles, soldes) et géographiques (coordonnées GPS). Les échantillons publiés confirment également l’exposition de logs systèmes et d’activités utilisateurs, indiquant une compromission profonde de la plateforme applicative.

- **Analyse :**
  AFRINTEL a consulté la publication de l'acteur malveillant Spirigatito sur un forum cybercriminel, intitulée « Government of Zambia (ZIPSIS) - 34M », ainsi qu'un échantillon de données associé. L'échantillon se compose d'exports au format JSON provenant du système ZISPIS, exploité par le Ministry of Community Development and Social Services (mcdss.gov.zm) dans le cadre du programme de transferts monétaires sociaux (Social Cash Transfer). Les enregistrements de bénéficiaires observés incluent nom complet, genre, date de naissance, identifiant national, coordonnées GPS du foyer, district et village de résidence, situation socio-économique détaillée (type d'habitation, accès à l'eau et à l'électricité, sécurité alimentaire, situation de handicap) ainsi que des données de paiement (montants, cycles, canal de versement, agent de paiement et ses coordonnées). L'échantillon inclut également des journaux d'activité applicatifs associés à des comptes d'agents gouvernementaux nommément identifiés (adresses e-mail aux domaines mcdss.gov.zm et cbt.gov.zm), avec des actions telles que la mise à jour de dossiers bénéficiaires, la validation de paiements, la génération de rapports et la clôture de dossiers pour cause de décès. Ces éléments sont cohérents avec un accès direct à la base de données applicative de ZISPIS et à ses journaux d'audit, plutôt qu'avec un simple export partiel. AFRINTEL ne reproduit aucun nom, identifiant national, numéro de téléphone ni coordonnée GPS individuels issus de cet échantillon. AFRINTEL n'a pas eu accès à l'intégralité des 34 millions d'enregistrements revendiqués et ne peut pas confirmer ce volume total ni le vecteur d'accès initial.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche recense une publication ou une fuite présumée ; l’authenticité et le périmètre des données ne sont pas confirmés au-delà des éléments décrits. Un audit défensif des accès et exports est recommandé.

#### 🇿🇦 Afrique du Sud - Eventing South Africa
- **Date de publication initiale :** 1 mars 2026

- **Acteur / Groupe :** xNov
- **Secteur :** Sport / Loisirs
- **Site web :** [eventingsa.co.za](https://www.eventingsa.co.za)
- **Date de la fuite :** 16 Janvier 2026 (Identifiée en Mars 2026)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Eventing South Africa est l'organisme officiel régissant les compétitions de concours complet d'équitation. xNov a divulgué une base de données contenant des informations sur les clubs et les membres : noms, adresses e-mail, identifiants de connexion (mots de passe), détails d'affiliation, registres des chevaux et cavaliers, données de compétition, ainsi que des informations administratives et financières (paiements, factures).


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche recense une publication ou une fuite présumée ; l’authenticité et le périmètre des données ne sont pas confirmés au-delà des éléments décrits. Un audit défensif des accès et exports est recommandé.

#### 🇩🇿 Algérie - Bridges (tebridges.dz)
- **Date de publication initiale :** 1 mars 2026

- **Acteur / Groupe :** Grubder
- **Secteur :** Technologie / Services aux entreprises (CRM)
- **Site web :** [tebridges.dz](https://www.tebridges.dz)
- **Date de l'incident :** 02 Février 2026
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Bridges est un fournisseur de solutions technologiques en Algérie. Grubder a mis en vente une base de données d'environ 672 000 enregistrements actifs (PII et CRM) incluant noms complets, numéros de téléphone principaux, adresses locales détaillées, codes postaux et statuts de compte. Un échantillon de données (CSV) a validé l'extraction.

  Le même jour (02 février 2026), un second compte, Dripper, a publié une annonce distincte proposant le même volume revendiqué (~672 000 enregistrements) pour le même domaine, avec un prix de 143 dollars et un contact Telegram/Session. AFRINTEL considère qu'il s'agit très probablement d'une republication ou d'une revente de la même base plutôt que d'une intrusion distincte. Le compte Dripper a depuis été banni par le forum pour tentative d'arnaque sur des données publiques, et l'échantillon associé à cette republication mélangeait un enregistrement libellé Afghanistan avec des enregistrements algériens, ce qui affaiblit la fiabilité de cette republication spécifique sans remettre en cause l'existence de la revendication initiale de Grubder.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche recense une publication ou une fuite présumée ; l’authenticité et le périmètre des données ne sont pas confirmés au-delà des éléments décrits. Un audit défensif des accès et exports est recommandé.

#### 🌍 Afrique (Multi-pays) - Loozap (loozap.com)
- **Date de publication initiale :** 1 mars 2026

- **Acteur / Groupe :** zimablue
- **Secteur :** E-commerce / Petites annonces en ligne
- **Site web :** [loozap.com](http://loozap.com/)
- **Date de l'incident :** 28 janvier 2026 (identifiée en mars 2026)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Description victime :** Loozap est une plateforme panafricaine de petites annonces en ligne (anciennement Listings360), exploitant des sections nationales dans des dizaines de marchés africains à partir d'une application unique partagée, plutôt qu'un service propre à un seul pays. Un acteur malveillant a publié une base de données contenant environ 34 000 comptes utilisateurs.
- **Analyse :** AFRINTEL a examiné un échantillon structuré de la table utilisateurs publiée. Les enregistrements ne sont pas rattachés à un seul pays : les entrées examinées listent des utilisateurs situés notamment en Égypte, au Kenya, au Ghana, en Éthiopie, au Nigeria et au Mozambique, cohérent avec le rôle de Loozap en tant que base de données partagée unique alimentant ses sous-domaines nationaux plutôt qu'un déploiement pays par pays. Les champs examinés incluent le nom complet, l'adresse email, un hash de mot de passe au format SHA1, l'adresse IP d'inscription, des coordonnées de géolocalisation précises, la date de naissance, le genre et des métadonnées d'activité sociale (abonnés, mentions « j'aime », appartenance à des groupes). La cohérence du schéma de base de données entre les enregistrements de différents pays, ainsi que le volume et la structure interne de l'échantillon, soutiennent une évaluation à confiance élevée d'une compromission réelle et complète de la base utilisateurs partagée de la plateforme, plutôt qu'une revendication limitée à une seule instance nationale. Compte tenu de la portée multi-pays, de la présence de données de géolocalisation précises et d'un hachage de mot de passe faible (SHA1), cet incident crée un risque de prise de contrôle de comptes à grande échelle, de credential stuffing sur des mots de passe réutilisés, et de phishing ciblé affectant simultanément des utilisateurs de plusieurs pays africains. AFRINTEL ne reproduit aucun nom, adresse email, hash de mot de passe, adresse IP ni coordonnée de géolocalisation issus de l'échantillon examiné.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche recense une publication ou une fuite présumée ; l’authenticité et le périmètre des données ne sont pas confirmés au-delà des éléments décrits. Un audit défensif des accès et exports est recommandé.

### 02 mars 2026

#### 🇪🇬 Égypte - Autorité de Régulation de la Gestion des Déchets (WMRA)
- **Date de publication initiale :** 2 mars 2026

- **Acteur / Groupe :** CrowStealer
- **Secteur :** Gouvernement / Environnement
- **Site web :** [wmra.gov.eg](https://wmra.gov.eg/en/)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Organisme dépendant du Ministère de l'Environnement chargé de réguler la gestion des déchets. Base de données contenant des données administratives, registres internes, informations sur partenaires et personnel.


- **Domaine initialement cité :** `garb.gov.eg` - relation non démontrée.

- **Vérification institutionnelle :** [source publique](https://wmra.gov.eg/en/). Cette vérification de domaine ne confirme pas la compromission alléguée.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La page institutionnelle WMRA est identifiée sur wmra.gov.eg ; le domaine garb.gov.eg repris par la fiche initiale n’a pas été rattaché techniquement à cette publication. L’existence d’un organisme public ne valide ni l’origine ni l’authenticité de la base revendiquée. Prioriser la vérification des jeux de données et des éventuelles données partenaires, sans attribuer d’intrusion au portail officiel.

#### 🇪🇬 Égypte - Orascom Construction
- **Date de publication initiale :** 2 mars 2026

- **Acteur / Groupe :** CrowStealer
- **Secteur :** Ingénierie et construction
- **Site web :** [orascom.com](https://orascom.com/)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Leader de l'ingénierie et construction au Moyen-Orient, Afrique du Nord et États-Unis. Données compromises : staff_id, noms complets, emails professionnels, départements, postes.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche recense une publication ou une fuite présumée ; l’authenticité et le périmètre des données ne sont pas confirmés au-delà des éléments décrits. Un audit défensif des accès et exports est recommandé.

#### 🇪🇬 Égypte - Ministère de la Santé et de la Population (E-Portal)
- **Date de publication initiale :** 2 mars 2026

- **Acteur / Groupe :** CrowStealer
- **Secteur :** Gouvernement / Santé
- **Site web :** [mohp.gov.eg](https://www.mohp.gov.eg)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Base de données de 3,8 millions d'enregistrements (2019-2026) incluant noms complets, National ID, téléphones, adresses, diagnostics médicaux précis, types de chirurgies, établissements de traitement.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Les 3,8 millions de dossiers et les diagnostics médicaux représentent une revendication non vérifiée sur le volume global. Le risque principal, si l’origine est confirmée, concerne la confidentialité des données de santé et leur réutilisation pour le ciblage et l’usurpation. Vérifier le périmètre des bases et prestataires avant de conclure à une compromission du ministère entier.

### 03 mars 2026

#### 🇿🇦 Afrique du Sud - Walter Sisulu University (WSU)
- **Date de publication initiale :** 3 mars 2026

- **Acteur / Groupe :** TelephoneHooliganism
- **Secteur :** Éducation / Université
- **Site web :** [wsu.ac.za](https://www.wsu.ac.za)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Université publique du Cap Oriental. Données structurées en trois sections (Contacts, Inscriptions, Tickets) : dates de naissance, emails, adresses, GPA, bourses, historiques de support.

- **Analyse :**
  AFRINTEL a consulté un échantillon de données correspondant à la section Tickets de cette revendication : un export de tickets d'assistance informatique interne (helpdesk), structuré avec identifiant de contact, e-mail, téléphone, nom et prénom, statut et catégorie du ticket, priorité, canal d'origine, agent assigné, dates d'ouverture et de clôture, résumé de résolution, notes internes de l'agent, indicateur de dépassement de SLA et région (parmi lesquelles Western Cape, Gauteng, KwaZulu-Natal, Cap-Oriental et Cap-Nord). Les catégories de tickets observées couvrent notamment des problèmes d'accès au portail étudiant, des accès e-mail, des installations logicielles et un cas classé Security lié à une activité suspecte sur un compte. Cet échantillon est cohérent avec un système de gestion des tickets du service d'assistance de l'université et confirme, en complément des sections Contacts et Inscriptions déjà mentionnées dans la description, une exposition de coordonnées de contact et de contenu opérationnel interne du support. AFRINTEL n'a pas eu accès aux sections Contacts et Inscriptions elles-mêmes lors de cette analyse et ne peut pas confirmer le volume total de tickets concernés ni le vecteur d'accès initial.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche recense une publication ou une fuite présumée ; l’authenticité et le périmètre des données ne sont pas confirmés au-delà des éléments décrits. Un audit défensif des accès et exports est recommandé.

#### 🇪🇬 Égypte - Ministère de l'Éducation et de l'Enseignement Technique
- **Date de publication initiale :** 3 mars 2026

- **Acteur / Groupe :** CrowStealer
- **Secteur :** Gouvernement / Éducation
- **Site web :** [moe.gov.eg](https://moe.gov.eg)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Données sur étudiants et personnel : identifiants nationaux, noms complets, adresses, dossiers académiques.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La mention « Data Fully Published » décrit l’état annoncé d’une publication, pas une confirmation institutionnelle de l’accès initial ni de l’exhaustivité du contenu. La priorité défensive porte sur l’intégrité des dossiers scolaires, les identifiants et la surveillance des comptes administratifs.

#### 🇲🇦 Maroc - Office National des Œuvres Universitaires Sociales et Culturelles (ONOUSC)
- **Date de publication initiale :** 3 mars 2026

- **Acteur / Groupe :** xNov
- **Secteur :** Éducation / Gouvernement
- **Site web :** [amo.onousc.ma](https://amo.onousc.ma)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Organisme chargé de la gestion des œuvres sociales pour les étudiants au Maroc (bourses, cités universitaires, couverture santé). Exposition des dossiers de 3 631 étudiants liés à l’Assurance Maladie Obligatoire (AMO) : noms, prénoms, CINE, numéros d’immatriculation universitaire, CNE, dates de naissance, statuts d’inscription.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Les 3 631 dossiers AMO mentionnés correspondent à une exposition alléguée de données sociales étudiantes. Une vérification technique du contenu publié et des systèmes affectés reste indispensable. Les risques portent sur fraude à l’identité, ciblage individuel et échanges frauduleux avec les services administratifs.

### 04 mars 2026

#### 🇲🇦 Maroc - Outsourcia
- **Date de publication initiale :** 4 mars 2026

- **Groupe ransomware :** Qilin
- **Secteur :** Business Process Outsourcing (BPO)
- **Site web :** [outsourcia.com](https://www.outsourcia.com)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Opérateur majeur de la relation client basé à Casablanca, gérant des processus métiers pour des comptes internationaux.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La revendication visant un prestataire BPO peut présenter un risque indirect pour ses clients si des données, accès distants ou opérations externalisées sont concernés. Aucun périmètre de client final ni technique d’accès n’est démontré dans la fiche ; recommander une revue contractuelle et IAM des comptes de prestataires, sans présumer un impact client.

### 05 mars 2026

#### 🇪🇬 Égypte - Rowad Modern Engineering
- **Date de publication initiale :** 5 mars 2026

- **Groupe ransomware :** Crypto24
- **Secteur :** Ingénierie et construction
- **Site web :** [rowad-rme.com](http://www.rowad-rme.com)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Société de construction égyptienne spécialisée dans les projets d'infrastructure et les bâtiments commerciaux.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

### 06 mars 2026

#### 🇪🇬 Égypte - INTERACT TECHNOLOGY SOLUTIONS
- **Date de publication initiale :** 6 mars 2026

- **Groupe ransomware :** PEAR
- **Secteur :** IT Consulting
- **Site web :** [interactts.com](http://interactts.com)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Entreprise fournissant des solutions technologiques et d'infrastructure critique en Égypte.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

#### 🇲🇬 Madagascar - Orange Madagascar
- **Date de publication initiale :** 6 mars 2026

- **Groupe ransomware :** Qilin
- **Secteur :** Télécommunications
- **Site web :** [orange.mg](https://www.orange.mg/)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Leader des télécommunications à Madagascar, opérant sur l'internet, le mobile et le mobile banking.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La revendication portant sur un opérateur télécom et de services financiers doit être suivie sous l’angle de la continuité et des comptes interconnectés. La fiche ne démontre ni compromission du cœur de réseau ni atteinte aux transactions de mobile money ; les deux scénarios restent des hypothèses de risque.

### 08 mars 2026

#### 🇸🇳 Sénégal - Direction Générale de la Comptabilité Publique et du Trésor (DGCPT) [Vente d'accès]
- **Date de publication initiale :** 8 mars 2026


- **Acteur / Groupe :** w00l_ysh1
- **Secteur :** Gouvernement / Finances publiques
- **Site web :** [sentresor.org](https://www.sentresor.org/)
- **Statut :** Claim - Unverified
- **Type d’incident :** Vente d’accès

- **Description :** Une publication sur un forum cybercriminel revendique la vente d’accès à l’infrastructure de la Direction Générale de la Comptabilité Publique et du Trésor (DGCPT) du Sénégal.

- **Accès revendiqués :**
  - identifiants VPN
  - accès administrateur Windows Server
  - accès Domain Controller (DC)
  - accès à un réseau de plus de 200 machines
  - accès à des bases financières et serveurs internes

- **Tarification observée :**
  - accès VPN : 500 USD
  - accès administrateur à deux serveurs : 2 000 USD
  - accès Domain Controller : 15 000 USD

- **Analyse CTI :**
  Les éléments publiés suggèrent potentiellement une compromission avancée d’un environnement gouvernemental financier. Un accès Domain Controller pourrait permettre :
  - mouvement latéral,
  - persistance,
  - exfiltration de données,
  - déploiement de ransomware,
  - ou compromission complète de l’Active Directory.

- **Note CTI :**
  Aucun élément technique indépendant ne permet actuellement de confirmer l’authenticité des accès revendiqués. Toutefois, la présence d’offres segmentées (VPN, serveurs, DC) correspond aux modes opératoires observés sur les marchés d’accès initiaux (Initial Access Brokers).
---

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Vente d’accès présumée, distincte des ransomware et des fuites. La proposition d’un accès au contrôleur de domaine n’établit pas la validité de tels privilèges. Hypothèses SOC : connexions VPN atypiques, changements de groupes à privilèges, création de services distants, authentifications sur contrôleurs de domaine et administration depuis comptes prestataires.

### 09 mars 2026

#### 🇹🇳 Tunisie - K.PROPHA (Karray Produits Pharmaceutiques)
- **Date de publication initiale :** 9 mars 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Santé / Pharmaceutique
- **Site web :** [kpropha.com](http://kpropha.com)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Entreprise tunisienne spécialisée dans la distribution de produits pharmaceutiques et parapharmaceutiques.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

### 12 mars 2026

#### 🇲🇦 Maroc - HACA (Haute Autorité de la Communication Audiovisuelle)
- **Date de publication initiale :** 12 mars 2026

- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Gouvernement / Médias
- **Site web :** [haca.ma](http://haca.ma)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Instance constitutionnelle chargée de la régulation de la communication audiovisuelle au Maroc.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

### 13 mars 2026

#### 🇿🇦 Afrique du Sud - Lion of Africa Insurance
- **Date de publication initiale :** 13 mars 2026

- **Groupe ransomware :** Lynx
- **Secteur :** Services d'assurance
- **Site web :** [lionsureins.com](http://lionsureins.com/)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Compagnie d'assurance sud-africaine traitant des volumes importants de données personnelles et financières.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

#### 🇿🇦 Afrique du Sud - Gouvernement Provincial de Gauteng
- **Date de publication initiale :** 13 mars 2026

- **Acteur / Groupe :** XP95
- **Secteur :** Gouvernement / Administration publique
- **Site web :** [gauteng.gov.za](https://www.gauteng.gov.za)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Gestion de la province la plus peuplée d'Afrique du Sud (Johannesburg, Pretoria). 3,8 To de données (3,6 millions de fichiers) exfiltrés : santé, éducation, logement, développement économique.

- **Type de la revendication Kazu liée :** Ransomware / contexte d'extorsion. Il s'agit d'une revendication secondaire liée, non comptée comme incident canonique distinct ; les éléments disponibles n'établissent ni chiffrement ni intrusion distincte.

**Revendication secondaire liée - non comptée comme nouvel incident canonique :** Une publication distincte de Kazu datée du **16 mai 2026** cite également le Gouvernement provincial du Gauteng. Elle annonce **3 673 556 fichiers**, environ **3,8 To**, et un prix de **25 000 USD**. L'archive fournie localement contient **1 905 fichiers** et environ **1,905 Go** ; son SHA-256 est `3fd8dcb059e77bad240e50d7e5691fdcf75fd81d4c9680e6f56e431ed6e42261`. Le recoupement entre la victime et le volume revendiqué par rapport à la fiche XP95 est compatible avec une double revendication, un transfert/revente ou une exposition distincte, mais les éléments disponibles ne permettent pas de trancher entre ces hypothèses. La revendication Kazu est donc conservée comme revendication liée non canonique et n'augmente pas le total des incidents.

Cette chronologie est enregistrée comme **deux revendications observées** - XP95 en mars et Kazu en mai - mais comme **un seul incident canonique**, dans l'attente d'éléments démontrant que les données Kazu proviennent d'une compromission distincte.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Les volumes avancés (3,8 To) sont des assertions d’acteur ; une revendication secondaire de mai associée à Kazu doit rester liée, sans ajout d’un deuxième incident canonique. Mettre l’accent sur le risque transversal pour les administrations provinciales et la comparaison des métadonnées, plutôt que sur une attribution forensique non disponible.

#### 🇿🇦 Afrique du Sud - Buffalo City Metropolitan Municipality [Fuite de données]
- **Date de publication initiale :** 13 mars 2026


- **Acteur / Groupe :** wh6ami
- **Secteur :** Gouvernement / Administration municipale
- **Site web :** [buffalocitymetro.gov.za](https://www.buffalocitymetro.gov.za/)
- **Date de fuite :** 13 Mars 2026
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Fuite de données

- **Description :** Une publication sur un forum cybercriminel revendique la vente d’une base de données attribuée à Buffalo City Metropolitan Municipality en Afrique du Sud. L’acteur affirme disposer d’un accès administrateur aux systèmes et publie plusieurs échantillons liés aux services municipaux, aux utilisateurs internes et aux journaux d’administration.

- **Données observées :**
  - noms et prénoms
  - emails gouvernementaux
  - numéros de téléphone
  - départements internes
  - rôles utilisateurs
  - journaux de connexion
  - actions administrateur
  - données liées aux appels d’offres
  - informations d’employés municipaux
  - adresses de bureaux

- **Analyse CTI :**
  Les éléments publiés suggèrent l’exposition d’une base backend gouvernementale contenant données utilisateurs, journaux administratifs et informations liées aux services municipaux. Les journaux observés montrent notamment :
  - créations/suppressions de comptes,
  - modifications de mots de passe,
  - connexions administrateur,
  - publications de contenus et appels d’offres.

  Les risques incluent :
  - compromission de comptes gouvernementaux,
  - spear phishing ciblé,
  - fraude aux appels d’offres,
  - ou exploitation d’accès administratifs persistants.

- **Note CTI :**
  Les échantillons publiés contiennent des données cohérentes avec une plateforme municipale opérationnelle ainsi que des journaux d’administration détaillés.

- **Vérification institutionnelle :** [source publique](https://www.gov.za/nso/about-government/contact-directory/ec-municipalities/buffalo-city-metropolitan-municipality). Cette vérification de domaine ne confirme pas la compromission alléguée.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Le nom du domaine municipal est vérifié par des sources institutionnelles, mais les journaux présentés dans le post ne prouvent pas un accès administrateur actuel. Risques prioritaires : fraude aux marchés publics, hameçonnage administratif et abus éventuel de comptes internes ; exploiter les journaux IAM et d’édition applicative pour qualifier la portée.

### 14 mars 2026

#### 🇪🇬 Égypte - Grid Fine Finishes
- **Date de publication initiale :** 14 mars 2026

- **Groupe ransomware :** Payload
- **Secteur :** Aménagement / Construction
- **Site web :** [gridff.com](http://gridff.com)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Société égyptienne spécialisée dans l'aménagement intérieur haut de gamme pour les secteurs commerciaux et résidentiels.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

### 16 mars 2026

#### 🇿🇦 Afrique du Sud - Northern Cape Department of Roads & Public Works [Fuite de données]
- **Date de publication initiale :** 16 mars 2026


- **Acteur / Groupe :** wh6ami
- **Secteur :** Gouvernement / Infrastructures publiques / Transport
- **Site web :** [ncrpw.ncpg.gov.za](http://ncrpw.ncpg.gov.za/)
- **Date de fuite :** 16 Mars 2026
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Fuite de données

- **Description :** Une publication sur un forum cybercriminel revendique la vente d’une base de données attribuée au Department of Roads & Public Works de la province du Northern Cape en Afrique du Sud. Les échantillons publiés contiennent des données issues de formulaires de contact et d’échanges administratifs liés aux infrastructures publiques, appels d’offres, stages, candidatures et demandes institutionnelles.

- **Données observées :**
  - noms et prénoms
  - adresses email
  - numéros de téléphone
  - contenus complets de messages
  - demandes liées aux appels d’offres
  - candidatures et stages
  - demandes fournisseurs
  - informations liées aux infrastructures routières

- **Analyse CTI :**
  Les éléments observés suggèrent l’exposition d’une base backend de formulaires gouvernementaux et de communications administratives. Les données publiées pourraient être exploitées pour :
  - spear phishing ciblé,
  - fraude aux appels d’offres,
  - usurpation d’identité,
  - ou attaques BEC visant des fournisseurs et partenaires gouvernementaux.

- **Note CTI :**
  Les échantillons publiés montrent des échanges réels liés à des infrastructures publiques, fournisseurs, projets routiers et processus administratifs gouvernementaux.

- **Vérification institutionnelle :** [source publique](https://provincialgovernment.co.za/units/view/94/northern-cape/roads-and-public-works). Cette vérification de domaine ne confirme pas la compromission alléguée.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Le domaine institutionnel apparaît dans un annuaire provincial. Les contenus de formulaires et correspondances présentés sont cohérents avec une exposition de back-office, sans démontrer un accès privilégié ou l’étendue des données. Surveiller les changements de coordonnées fournisseurs et l’utilisation anormale des boîtes de réception administratives.

### 17 mars 2026

#### 🇿🇦 Afrique du Sud - University of South Africa (UNISA)
- **Date de publication initiale :** 17 mars 2026

- **Acteur / Groupe :** Blackwinter99
- **Secteur :** Éducation / Enseignement Supérieur
- **Site web :** [unisa.ac.za](https://www.unisa.ac.za)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** L'UNISA est la plus grande institution d'enseignement à distance en Afrique. Blackwinter99 a divulgué publiquement sur un forum clandestin les identifiants de connexion de la page d'administration du site, susceptibles, s’ils étaient valides, de donner des privilèges élevés de la plateforme, permettant l'exfiltration massive de données étudiantes, la modification des dossiers académiques ou une prise de contrôle totale de l'infrastructure web.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La publication d’identifiants prétendument administratifs ne démontre pas que ces accès restent valides. Les scénarios de détournement du portail étudiant et d’exfiltration massive doivent être présentés comme risques potentiels, non comme actions effectivement menées.

### 19 mars 2026

#### 🇳🇦 Namibie - Namibia Airports Company
- **Date de publication initiale :** 19 mars 2026

- **Groupe ransomware :** INC Ransom
- **Secteur :** Transport aérien
- **Site web :** [airports.com.na](http://airports.com.na)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Gestionnaire officiel des aéroports nationaux en Namibie.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

### 20 mars 2026

#### 🇿🇦 Afrique du Sud - The Unlimited
- **Date de publication initiale :** 20 mars 2026

- **Groupe ransomware :** DragonForce
- **Secteur :** Services d'assurance
- **Site web :** [theunlimited.co.za](http://theunlimited.co.za)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Fournisseur de produits d'assurance incluant la santé, l'auto, le juridique et la vie.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

#### 🇲🇦 Maroc - Ministère de la Justice
- **Date de publication initiale :** 20 mars 2026

- **Acteur / Groupe :** anisanas2
- **Secteur :** Gouvernement / Justice
- **Site web :** [justice.gov.ma](https://www.justice.gov.ma)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** L’acteur revendique une exfiltration de 300 Go incluant plus de 150 000 dossiers de procédures judiciaires (2019-2026). Litiges opposant grandes entreprises marocaines à des particuliers (12 Mds MAD). Documents : pièces d'identité, relevés bancaires, actes judiciaires, factures.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Les 300 Go et 150 000 dossiers judiciaires sont revendiqués dans le corpus ; l’échantillon et les sources publiques disponibles ici ne permettent pas d’en confirmer indépendamment la totalité. La priorité est la protection du secret judiciaire et des documents sensibles, et non l’affirmation d’une extraction complète.

### 21 mars 2026

#### 🇿🇦 Afrique du Sud - Elundini Local Municipality
- **Date de publication initiale :** 21 mars 2026

- **Groupe ransomware :** TheGentlemen
- **Secteur :** Administration locale
- **Site web :** [elundini.gov.za](http://elundini.gov.za)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Administration municipale dédiée au développement durable dans la province du Cap Oriental.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

### 22 mars 2026

#### 🇿🇦 Afrique du Sud - Semenya Furumele Consulting Engineers
- **Date de publication initiale :** 22 mars 2026

- **Groupe ransomware :** NightSpire
- **Secteur :** Ingénierie conseil
- **Site web :** [sfce.co.za](http://www.sfce.co.za)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Cabinet de conseil en ingénierie basé en Afrique du Sud.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

### 23 mars 2026

#### 🇿🇦 Afrique du Sud - Standard Bank South Africa
- **Date de publication initiale :** 23 mars 2026


- **Date de l'incident / première communication :** 23 mars 2026
- **Mises à jour publiques :** 02, 13 et 14 avril 2026
- **Acteur / Groupe :** Non attribué officiellement ; revendication distincte de PrinzEugen non corroborée
- **Secteur :** Finance / Banque
- **Site web :** [standardbank.co.za](https://www.standardbank.co.za/southafrica/personal)
- **Statut :** Incident Confirmed by Victim
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** **Standard Bank South Africa** est l'activité bancaire sud-africaine du **Standard Bank Group**, groupe financier proposant notamment des comptes, paiements, financements, services aux entreprises et solutions d'investissement. La **Standard Bank of South Africa Limited** fait partie des entités juridiques identifiées par le groupe dans sa documentation institutionnelle ([déclaration officielle de confidentialité](https://www.standardbank.co.za/southafrica/personal/about-us/legal/privacy-statement)).

- **Vérification indépendante au 18 octobre 2026 :** **Confirmation de première main :** Standard Bank a déclaré le 23 mars 2026 un accès non autorisé à certaines données, tout en précisant que les systèmes transactionnels et les fonds des clients n’étaient pas touchés. L’événement est antérieur à septembre.

- **Sources de vérification complémentaires :** [Source 1](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank)

- **Sources / Éléments de preuve :** [Standard Bank, 23 mars 2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank) ; [Standard Bank, 14 avril 2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-data-incident-update-14-april)

Standard Bank a confirmé un accès non autorisé à des systèmes administratifs et espaces documentaires internes, avec exposition possible de noms, identifiants, coordonnées, adresses et numéros de compte. Les systèmes transactionnels et centraux n'auraient pas été accédés. Le vecteur, le nombre de personnes et le volume copié restent inconnus. Cette fiche est distincte de la revendication Standard Bank Group de mai.


- **Source officielle :** [Standard Bank – 23/03/2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank) ; [14/04/2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-data-incident-update-14-april).

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Confirmation de première main : Standard Bank a reconnu le 23 mars un accès non autorisé à certaines données. Sa mise à jour du 14 avril précise des systèmes administratifs et documentaires affectés, tandis que les systèmes bancaires transactionnels et de cœur de métier n’auraient pas été accédés. Risque principal : usurpation et fraude ciblée ; ne pas étendre sans preuve l’incident aux services de paiement.

#### 🇿🇦 Afrique du Sud - Pick n Pay ASAP / Bottles.com [Fuite de données]
- **Date de publication initiale :** 23 mars 2026

- **Acteur / Groupe :** p4pr1k4
- **Secteur :** E-commerce / Livraison / Retail
- **Site web :** [bottles.com](https://bottles.com)
- **Date de fuite :** 23 Mars 2026
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Fuite de données

- **Description :** Une publication sur un forum cybercriminel revendique la vente d’une base de données attribuée à Bottles.com, devenu Pick n Pay ASAP après son acquisition par Pick n Pay. Les données publiées concernent des utilisateurs sud-africains de la plateforme de livraison.

- **Données observées :**
  - noms et prénoms
  - emails
  - numéros de téléphone
  - dates de naissance
  - mots de passe
  - informations de cartes bancaires
  - cartes VISA et Mastercard
  - données 3DS
  - adresses et historiques de livraison
  - coordonnées GPS
  - notes du service client

- **Analyse CTI :**
  Les échantillons publiés suggèrent l’exposition d’une base e-commerce sensible contenant données personnelles, historiques d’adresses et informations de paiement. Les risques incluent fraude bancaire, usurpation d’identité, phishing ciblé et compromission de comptes clients.

- **Note CTI :**
  Les données observées incluent des extraits SQL structurés, historiques d’adresses et informations liées aux cartes bancaires et systèmes 3DS.
---

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Le schéma de la publication suggère des données de livraison et des informations de paiement ; les données 3DS et cartes restent à caractériser indépendamment. Le fait que Bottles ait été intégré à Pick n Pay ASAP ne démontre pas que les systèmes actuels de l’acquéreur ont été compromis. Prioriser le rapprochement de la provenance des données et la détection de fraude clients.

### 24 mars 2026

#### 🇸🇳 Sénégal - United Bank for Africa (UBA Sénégal)
- **Date de publication initiale :** 24 mars 2026


- **Date de l'incident :** 30-31 janvier 2026
- **Acteur / Groupe :** Non attribué
- **Secteur :** Finance / Banque
- **Site web :** [ubasenegal.com](https://www.ubasenegal.com)
- **Statut AFRINTEL :** Under Investigation
- **Type d'incident :** Fraude opérationnelle / Cyber-enabled ATM Cash-Out
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4

- **Description :**

  UBA Sénégal a été touchée par une opération coordonnée de retraits frauduleux aux distributeurs automatiques, facilitée par des moyens cyber, menée entre le 30 et le 31 janvier 2026.

- **Analyse :**

  Selon l'avis ngCERT `ngCERT-2026-060005`, l'opération a impliqué 3 421 transactions de retrait aux distributeurs automatiques et causé des pertes supérieures à 2 millions de dollars américains.
  Des informations antérieures estimaient les pertes à environ 1,143 milliard de FCFA.

  Le ngCERT estime qu'un accès privilégié à l'infrastructure d'autorisation des cartes a probablement permis aux attaquants de manipuler les contrôles transactionnels et de coordonner les retraits frauduleux.

  L'existence et l'impact financier de l'opération frauduleuse sont donc corroborés par une source CERT nationale. Toutefois, le vecteur d'accès initial, la séquence technique exacte, l'identité de l'acteur de menace
  et une éventuelle implication interne restent non confirmés.

  Le phishing, la compromission de la chaîne d'approvisionnement, l'accès par un initié et les malwares visant les distributeurs automatiques sont des scénarios possibles évoqués par le ngCERT pour cette catégorie
  d'attaque et ne doivent pas être présentés comme des techniques confirmées utilisées contre UBA Sénégal.

- **Note de correction AFRINTEL :**

  L'incident s'est produit les 30-31 janvier 2026, mais a été identifié et documenté par AFRINTEL le 24 mars 2026. Il reste rattaché au corpus du mois  de mars conformément à la méthodologie AFRINTEL fondée sur la date de détection AFRINTEL.
Le précédent statut `Under Investigation` devrait être précisé, car la  fraude opérationnelle elle-même est corroborée. Ce qui reste en cours d'investigation concerne le chemin technique de l'intrusion et l'attribution à un acteur de menace.

- **Note taxonomique :**
  `Operational Fraud` est conservé comme une catégorie d'incident AFRINTEL non standard.
  L'incident reste exclu des compteurs `Ransomware`, `Data Leak`, `Access Sale` et `Defacement`.

- **Source externe corroborante :** [ngCERT, 25/06/2026, ngCERT-2026-060005](https://cert.gov.ng/advisories/alert-on-cyber-enabled-atm-cash-out-attacks-targeting-african-financial-institutions). Aucune confirmation de la victime recensée dans les sources examinées.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** L’événement de fraude s’est déroulé fin janvier et est suivi dans le corpus de mars par date de documentation. L’avis ngCERT daté du 25 juin cite 3 421 retraits et des pertes dépassant 2 MUSD ; il corrobore l’opération, pas l’identité des auteurs ni le chemin d’intrusion. Les scénarios phishing, insider ou malware ATM sont des hypothèses génériques de l’alerte et non des techniques démontrées contre UBA.

### 26 mars 2026

#### 🇿🇦 Afrique du Sud - ETFSA
- **Date de publication initiale :** 26 mars 2026

- **Groupe ransomware :** INC Ransom
- **Secteur :** Wealth Management
- **Site web :** [etfsa.co.za](http://ETFSA.co.za)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Ransomware
- **Description victime :** Plateforme sud-africaine de services financiers spécialisée dans les fonds négociés en bourse (ETF).

- **Analyse :**
  AFRINTEL a consulté la publication d'extorsion relative à cette victime, qui mentionne un chiffre d'affaires revendiqué d'environ 8 millions de dollars et nomme une personne identifiée comme directeur général de la plateforme. La publication indique que des données clients confidentielles et personnelles seraient publiées, et affiche des aperçus miniatures de nombreux documents. AFRINTEL a consulté un échantillon accessible : un extrait d'acte de décès délivré par le Department of Home Affairs sud-africain, contenant un numéro d'identité, un nom complet, une date de naissance et une cause de décès. Cela indique que les éléments exposés incluent des documents d'identité clients de type KYC et liés à des successions, et pas uniquement des données de compte ou de transaction, ce qui est cohérent avec une clientèle de gestion de patrimoine et de conseil financier. AFRINTEL n'a pas eu accès aux autres fichiers et ne peut pas confirmer le nombre total de clients concernés ni le vecteur d'accès initial.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

#### 🇲🇦 Maroc - Maroc Telecom
- **Date de publication initiale :** 26 mars 2026

- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Télécommunications
- **Site web :** [iam.ma](http://iam.ma)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Ransomware
- **Description victime :** Opérateur historique de télécommunications au Maroc, fournissant services mobiles, internet et fixes.

- **Analyse :**
  AFRINTEL a consulté des captures d'écran échantillons publiées dans le cadre de cette revendication. Le contenu montre des écrans internes de relation client et de support technique (interfaces GRC/suivi de réclamations) faisant référence à des identifiants clients, des coordonnées, des adresses d'installation et des tickets d'incident liés à des problèmes de service fixe et fibre optique. Ces éléments sont cohérents avec un accès aux systèmes de support client et de gestion des réclamations de Maroc Telecom, plutôt qu'avec un export massif de base d'abonnés. AFRINTEL n'a pas eu accès aux systèmes sous-jacents et ne peut pas confirmer le volume d'enregistrements concernés ni le vecteur d'accès initial.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Les captures décrites se rapportent au support client fixe/fibre et aux réclamations ; elles ne démontrent pas un export national de la base abonnés ni une compromission des équipements réseau. Détecter les consultations massives de tickets et les accès hors rôle au CRM.

#### 🇲🇦 Maroc - 2M TV
- **Date de publication initiale :** 26 mars 2026

- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Médias et audiovisuel
- **Site web :** [2m.ma](http://2m.ma)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Ransomware
- **Description victime :** Chaîne de télévision nationale marocaine.

- **Analyse :**
  AFRINTEL a consulté des documents échantillons publiés dans le cadre de cette revendication, correspondant à du matériel RH interne : un curriculum vitae d'un salarié du service audiovisuel, une liste interne d'employés titulaires du permis de conduire, ainsi qu'un modèle d'attestation de travail à en-tête 2M. Cela indique une exposition de dossiers du personnel plutôt que des systèmes de diffusion ou des données clients. AFRINTEL a également consulté un ensemble de données distinct : une exportation complète de boîte de messagerie au format .eml (1 777 messages), dont les métadonnées associées (identifiants de message au format Microsoft Exchange/Office 365 et horodatage de dernière réception daté de novembre 2025) indiquent une compromission d'un compte de messagerie professionnel individuel, vraisemblablement rattaché au service Rédaction/News de 2M, plutôt qu'un simple lot de documents statiques. La correspondance couvre 123 adresses internes 2m.ma distinctes et porte notamment sur la planification éditoriale d'une émission interne, des démarches administratives (dont une demande de carte de presse) et des échanges RH ; environ 348 messages comportent des pièces jointes (images, PDF, documents Word et tableurs Excel). Plusieurs objets de messages ne correspondent à aucune activité éditoriale identifiable et sont cohérents avec du courrier indésirable ou des tentatives d'ingénierie sociale reçues sur cette boîte. AFRINTEL ne nomme pas le titulaire du compte et ne reproduit ni le contenu des messages ni l'identité des correspondants tiers. AFRINTEL n'a pas eu accès à d'autres fichiers et ne peut pas confirmer le nombre total de dossiers d'employés concernés, l'état actuel d'accès à cette boîte de messagerie, ni le vecteur d'accès initial.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La présence d’un export de boîte professionnelle et de pièces RH justifie des hypothèses de compromission de compte ou d’export documentaire, sans démontrer que les systèmes de diffusion ont été touchés. Contrôles SOC : accès M365/Exchange anormaux, règles de transfert, consentements OAuth, export eDiscovery et téléchargements massifs.

#### 🇲🇦 Maroc - Institut Royal des Études Stratégiques (IRES)
- **Date de publication initiale :** 26 mars 2026

- **Groupe ransomware :** APT73 / Bashe
- **Secteur :** Recherche / Think tank
- **Site web :** [ires.ma](http://ires.ma)
- **Statut :** Claim - Data Sample Published
- **Type d’incident :** Ransomware
- **Description victime :** Centre d'analyse stratégique rattaché au Cabinet Royal marocain.

- **Analyse :**
  AFRINTEL a consulté des documents échantillons publiés dans le cadre de cette revendication, correspondant à des curriculums vitae de chercheurs et de consultants associés à l'institut, couvrant des profils académiques (recherches doctorales et de master en droit public et relations internationales), des références d'expérience professionnelle et, dans un cas, des coordonnées incluant une adresse e-mail et un numéro de téléphone. Cela indique une exposition de dossiers du personnel et des chercheurs. AFRINTEL n'a pas eu accès à d'autres fichiers et ne peut pas confirmer le nombre total d'enregistrements concernés ni le vecteur d'accès initial.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

### 29 mars 2026

#### 🇿🇦 Afrique du Sud - Statistics South Africa (Stats SA)
- **Date de publication initiale :** 29 mars 2026

- **Groupe ransomware :** XP95
- **Secteur :** Gouvernement / Statistiques Nationales
- **Site web :** [statssa.gov.za](https://www.statssa.gov.za)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Stats SA est l'agence nationale de statistique de l'Afrique du Sud. XP95 affirme avoir exfiltré 154 Go de données (453 362 fichiers). La brèche compromet potentiellement des données socio-économiques sensibles, des recensements, des informations sur l'emploi, l'inflation et des registres administratifs nationaux. Une rançon de 100 000 $ a été exigée avant une mise en vente publique prévue pour le 20 avril 2026.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Les volumes de 154 Go et 453 362 fichiers sont revendiqués par XP95. La menace stratégique concerne confidentialité et intégrité des données statistiques, mais les datasets sensibles précis ne sont pas démontrés dans le matériel transmis. Éviter d’affirmer une compromission de l’ensemble du recensement.

#### 🇿🇦 Afrique du Sud - Gauteng City Region Academy (GCRA)
- **Date de publication initiale :** 29 mars 2026

- **Groupe ransomware :** XP95
- **Secteur :** Éducation / Formation (Gouvernement provincial)
- **Site web :** [gcra.gauteng.gov.za](https://gcra.gauteng.gov.za)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** La GCRA est l'agence responsable du développement des compétences pour la province de Gauteng. L'exfiltration de 147 Go de données compromet potentiellement les dossiers des étudiants (bourses, inscriptions, PII), les données des programmes de formation et les documents administratifs de l'académie. XP95 a fixé une date limite pour le paiement de la rançon avant la mise en vente publique des fichiers.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Les 147 Go annoncés restent un volume de revendication. Si des dossiers de bourses et d’inscriptions sont concernés, le risque porte sur fraude au programme, détournement de paiements et ciblage d’étudiants ; vérifier les applications et exports d’inscription avant de conclure.

### 30 mars 2026

#### 🇹🇿 Tanzanie - SBC Tanzania Limited
- **Date de publication initiale :** 30 mars 2026

- **Groupe ransomware :** Morpheus
- **Secteur :** Agroalimentaire
- **Site web :** [sbctanzania.co.tz](http://sbctanzania.co.tz)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Fabricant et distributeur de boissons, embouteilleur officiel de PepsiCo en Tanzanie.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

#### 🇿🇦 Afrique du Sud - Nashua
- **Date de publication initiale :** 30 mars 2026

- **Groupe ransomware :** Coinbase Cartel
- **Secteur :** IT & Managed Services
- **Site web :** [nashua.co.za](http://nashua.co.za)
- **Statut :** Claim - Unverified
- **Type d’incident :** Ransomware
- **Description victime :** Fournisseur majeur de solutions technologiques intégrées et de services gérés pour entreprises.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La fiche établit uniquement l’existence d’une revendication de ransomware. Ni chiffrement, ni interruption de service, ni exfiltration intégrale ne sont démontrés ; vérifier sauvegardes, accès privilégiés et éventuelles données tierces.

#### 🇳🇬 Nigeria - Université Ahmadu Bello (ABU Zaria)
- **Date de publication initiale :** 30 mars 2026

- **Acteur / Groupe :** AshleyWood2022
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [abu.edu.ng](https://www.abu.edu.ng)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** L'une des plus grandes universités de recherche du Nigeria. Base de données (`tbl_flattened.csv` & `abu.sql`) avec plus de 11 000 enregistrements : personnel académique et non-académique (noms, départements, rangs, qualifications, sexe, date de naissance, districts d'origine).

- **Note de fiabilité :**
  AFRINTEL a examiné la publication de forum d'AshleyWood2022 datée du 30 mars 2026, accompagnée d'un lien de téléchargement (gofile.io) et d'un échantillon de données visible. L'échantillon examiné couvre le personnel rattaché au bureau du Vice-Chancelier et à ses sous-unités (ABU/FM Radio, ABUCONS, Central Procurement Unit, Academic Planning, University Advancement, Equipment Maintenance and Development Centre, Internal Audit, ITF/SIWES Coordination Centre, Procurement et Security Division), avec 237 lignes pour cette seule section, cohérent en échelle avec la revendication globale de plus de 11 000 enregistrements.

- **Analyse :**
  L'échantillon suit un schéma cohérent : zone de gouvernement local et circonscription sénatoriale d'origine, État, zone géopolitique, date de naissance, sexe, faculté, département, catégorie de personnel (académique ou non-académique), rang et plus haute qualification. Dans les lignes examinées, le champ date de naissance est uniformément masqué (`0000-00-00`) et aucun nom, numéro de téléphone ou identifiant national n'est visible ; la publication de l'acteur affirme que les noms et d'autres champs personnels figurent dans le jeu de données complet, qu'AFRINTEL n'a pas téléchargé ni vérifié de manière indépendante. La cohérence structurelle sur 237 lignes et la présence d'un lien de téléchargement fonctionnel appuient une évaluation plus solide qu'une simple revendication, sans que l'exhaustivité, l'authenticité ou le contenu complet de l'archive soient confirmés. Si la revendication complète s'avère exacte, l'exposition de données démographiques et organisationnelles du personnel pourrait faciliter l'ingénierie sociale ciblée, le profilage par région, sexe ou département, et l'usurpation d'identité de membres du personnel universitaire. AFRINTEL ne reproduit aucun enregistrement, valeur de champ ni lien de téléchargement issu du matériel examiné.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Le libellé « Data Fully Published » provient de l’annonce ; l’analyse détaillée ne décrit directement que 237 lignes visibles dans une section, sur plus de 11 000 lignes revendiquées. La complétude de la base et l’existence de noms dans le corpus intégral restent inconnues ; le rapport ne doit pas les transformer en faits.

### 31 mars 2026

#### 🇳🇬 Nigeria - Remita (SystemSpecs)
- **Date de publication initiale :** 31 mars 2026

- **Acteur / Groupe :** Bytetobreach
- **Secteur :** Fintech / Services de paiement
- **Site web :** [remita.net](https://www.remita.net)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Plateforme de paiement majeure au Nigeria utilisée par particuliers, entreprises et gouvernement. L’acteur revendique une fuite de 3 To : 800 Go de documents KYC (pièces d'identité, passeports, relevés bancaires, factures), bases MySQL/Postgres, codes sources, registres Docker, clés HSM gouvernementales, plus de 35 000 hashes de mots de passe.

- **Analyse :**
  AFRINTEL a consulté un ensemble d'éléments techniques associés à cette revendication. Un fichier d'informations de connexion recense environ 35 800 paires adresse e-mail / hachage de mot de passe (format bcrypt), couvrant à la fois des comptes internes (agents, opérateurs) et vraisemblablement des comptes clients de la plateforme ; AFRINTEL n'a extrait ni tenté de casser aucun hachage. Des captures d'écran montrent une instance restaurée des bases de données de la plateforme dans un outil d'administration SQL, incluant une table de propriétaires d'entreprise (numéro BVN, type et numéro de pièce d'identité, document d'identité encodé en base64), une table de transactions interbancaires (montants, codes banque bénéficiaire, canal, référence de paiement), une table de comptes administrateurs internes (agents SystemSpecs avec rôle et statut) et une table d'informations personnelles clients (date de naissance, e-mail, téléphone, statut KYC, mot de passe haché). D'autres captures montrent une archive de code source couvrant plusieurs microservices de la plateforme, incluant un module de communication chiffrée par SFTP avec la Banque Centrale du Nigeria (CBN) pour l'échange d'instructions de paiement, une intégration avec le système panafricain de paiement et de règlement PAPSS, un système de portefeuille virtuel développé en partenariat avec OPay, ainsi qu'une logique de vérification OTP. Une capture supplémentaire montre un répertoire de fichiers de clés nommés d'après plus de vingt banques nigérianes (dont GTBank, Zenith, UBA, First Bank, Access, FCMB, Fidelity, Sterling, Stanbic, Ecobank, UBN, Wema, Unity, Providus, Heritage et Citibank), cohérent avec des clés maîtresses de chiffrement liées à l'intégration interbancaire ; AFRINTEL n'a pas vérifié le contenu ni la validité de ces fichiers. Des résultats d'outils de détection de secrets exécutés sur les dépôts de code source montrent la détection de clés d'API, de jetons d'accès cloud et d'identifiants de base de données codés en dur dans plusieurs fichiers de configuration, associés à des adresses e-mail d'employés de SystemSpecs. AFRINTEL a par ailleurs examiné la structure d'une archive de sauvegarde Git (environ 34 800 fichiers) couvrant une quarantaine de dépôts internes distincts, avec historique de commits complet, correspondant à l'ensemble de l'organisation GitLab interne « remitacenta » : composants de paiement interbancaire et panafricain (dont un connecteur PAPSS et un générateur de messages de paiement au format ISO 20022, standard utilisé pour la messagerie interbancaire), moteur de détection de fraude, kit de tokenisation de cartes, infrastructure Kubernetes sous forme de code (trois jeux de manifestes distincts) et un module d'analyse décisionnelle (Superset), ce dernier représentant à lui seul plus du quart des fichiers de l'archive. L'archive contient environ 200 fichiers de configuration de production, 354 fichiers Helm « values.yaml » et plus de 400 noms de fichiers faisant explicitement référence à des secrets, ce qui est cohérent avec une exposition potentielle de nombreux identifiants supplémentaires au-delà de ceux déjà identifiés par les outils de détection ; AFRINTEL n'a pas ouvert individuellement ces fichiers et ne reproduit aucun secret supplémentaire. Un fichier supplémentaire, désigné comme téléchargement non finalisé, correspond à une image de sauvegarde au format Veeam Backup & Replication (signature XBSTCK01, version d'outil 12.1.2) référençant des fichiers journaux InnoDB, cohérent avec une sauvegarde de niveau système incluant une base de données MySQL/MariaDB ; ce fichier étant incomplet, AFRINTEL n'a pas pu le monter ni en examiner le contenu. Une dernière capture montre un accès, via des identifiants cloud extraits du code source, à un compartiment de stockage cloud dédié aux documents KYC contenant environ 657 000 fichiers pour un volume propre d'environ 588 Go, ainsi qu'à plusieurs autres compartiments liés à l'infrastructure GitLab interne de l'entreprise (sauvegardes, artefacts, registre de conteneurs). AFRINTEL ne reproduit aucun identifiant, clé, jeton, hachage, nom de compte ni document d'identité individuel issu de ces éléments. L'ensemble de ces observations est cohérent avec une compromission approfondie de l'infrastructure de développement et de production de Remita, pouvant s'étendre aux systèmes d'intégration bancaire et panafricaine, mais AFRINTEL n'a pas vérifié l'authenticité ni l'actualité de chaque élément pris individuellement et ne peut pas confirmer l'étendue exacte de l'accès obtenu ni le vecteur d'accès initial.


- **Suivi institutionnel :** [NDPC / presse indépendante, 06/04/2026](https://www.premiumtimesng.com/news/top-news/869669-ndpc-investigates-remita-sterling-bank-for-alleged-data-breach.html). Enquête ouverte ; portée non confirmée.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Plusieurs éléments techniques décrits par AFRINTEL suggèrent une exposition dépassant de simples informations commerciales : sauvegardes Git, configurations, données KYC et références d’intégration financière. La NDPC a ouvert une enquête sur les allégations concernant Remita en avril 2026. Ce suivi officiel ne valide ni les 3 To revendiqués, ni la validité de toutes les clés, ni un accès effectif aux systèmes interbancaires ; priorité aux secrets, aux accès cloud, au code et aux dépendances.

#### 🇲🇦 Maroc - Smarteez (Prestataire L’Oréal Maroc - Supply Chain)
- **Date de publication initiale :** 31 mars 2026

- **Acteur / Groupe :** xNov
- **Secteur :** Marketing Digital / Cosmétique (Supply Chain L'Oréal)
- **Site web :** [smarteez.eu](https://smarteez.eu)
- **Statut :** Data Fully Published
- **Type d'incident :** Fuite de données
- **Description victime :** Smarteez est un prestataire digital marocain utilisé par L’Oréal Maroc pour la gestion de ses opérations terrain. Exposition de données critiques : informations sur 296 pharmacies (GPS, segmentation), 361 000 enregistrements de ventes/KPI, 22 secrets d’applications OAuth2 en clair, logs administratifs complets. Une APK de production a également été divulguée.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** Les secrets OAuth2 et données commerciales mentionnés dans la publication nécessitent une analyse de validité et une rotation par les opérateurs légitimes. Le lien avec la chaîne de distribution de L’Oréal Maroc présente un risque de propagation contractuelle et de fraude aux opérations terrain ; il ne démontre pas une compromission directe des systèmes de L’Oréal.

#### 🇪🇬 Égypte - Semsar Masr (semsarmasr.com)
- **Date de publication initiale :** 31 mars 2026

- **Acteur / Groupe :** Al-Sheikh
- **Secteur :** Immobilier / Petites annonces en ligne
- **Site web :** [semsarmasr.com](https://www.semsarmasr.com)
- **Date de la fuite :** Janvier 2026 (identifiée en mars 2026)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Description victime :** Semsar Masr est une plateforme égyptienne de petites annonces immobilières, active depuis 2007, permettant la publication et la consultation d'annonces d'appartements, terrains et autres biens à la vente ou à la location en Égypte.
- **Analyse :** AFRINTEL a examiné un post publié le 28 janvier 2026 par l'acteur Al-Sheikh concernant la table `tb_members_Profiles` de semsarmasr.com, affirmant qu'elle contient 185 024 lignes et que les mots de passe des utilisateurs y figurent en clair. L'échantillon affiché dans le post comprend un schéma de champs incluant identifiant utilisateur, statut du compte, adresse email, numéro de téléphone, mot de passe, rôle utilisateur, nom de contact, nom d'entreprise, adresse, réseaux sociaux (WhatsApp, Telegram, LinkedIn, Twitter, Facebook), date de naissance, profession, genre, statut matrimonial, indicateurs de vérification email/téléphone et dates de création/mise à jour du compte. Dix enregistrements complets sont directement visibles dans l'échantillon, avec des adresses email, numéros de téléphone égyptiens et internationaux, noms complets et mots de passe en texte clair associés à des comptes créés le 28 janvier 2026. La cohérence du schéma avec une plateforme de petites annonces immobilières et la présence de mots de passe non hachés dans l'échantillon appuient un niveau de confiance élevé quant à l'authenticité de cette fuite, bien que le volume total de 185 024 lignes revendiqué n'ait pas pu être vérifié indépendamment au-delà de l'échantillon observé. L'exposition de mots de passe en clair, combinée aux coordonnées et à l'identité des utilisateurs, présente un risque élevé de prise de contrôle de comptes, de réutilisation de mots de passe sur d'autres services et de phishing ciblé. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone ni mot de passe issus de l'échantillon examiné.


- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La publication analysée porte initialement la date du 28 janvier 2026 et a été détectée ultérieurement. Les dix lignes observées ne permettent pas de vérifier les 185 024 enregistrements annoncés, mais la présence de mots de passe en clair, si authentique, exige des mesures de prévention de la réutilisation et de réinitialisation des comptes.

#### 🇬🇳 Guinée - Ministère de la Santé (sante.gov.gn)
- **Date de publication initiale :** 31 mars 2026

- **Acteur / Groupe :** Keymous
- **Secteur :** Gouvernement / Santé publique
- **Site web :** [sante.gov.gn](https://sante.gov.gn/)
- **Date de l'incident :** Juillet 2025 (activité observée, identifiée en mars 2026)
- **Statut :** Under Investigation
- **Type d'incident :** Fuite de données
- **Description victime :** Le site officiel du Ministère de la Santé de Guinée est directement lié aux systèmes internes compromis, notamment les dashboards DHIS2 exposés par Keymous. La corrélation entre l’accès aux outils de surveillance sanitaire, les données gouvernementales divulguées (emails, personnels) et les infrastructures ministérielles suggère une compromission plus large de l’écosystème numérique du ministère. Cette exposition pourrait permettre des attaques ciblées, de la manipulation de données sanitaires et des opérations d’influence.

- **Complément CTI AFRINTEL (revue analytique du 06/11/2026) :** La date d’activité mentionnée dans la fiche remonte à juillet 2025, l’identification AFRINTEL ayant lieu en mars 2026. L’exposition présumée de tableaux de bord DHIS2 ne prouve pas une altération des statistiques sanitaires ni un accès persistant ; la priorité est la vérification des permissions, des journaux et de l’intégrité des indicateurs.

