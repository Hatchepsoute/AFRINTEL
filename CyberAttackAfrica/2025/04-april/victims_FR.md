[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# Liste des victimes africaines de cyberattaques en Avril 2025 (17 victimes)
[**English version available here**](./victims.md)

## Résumé du mois

Avril 2025 compte **17 incidents uniques** : **7 Ransomware**, **9 Data Leak**, **1 Access Sale**, **0 DDoS**, **0 Defacement** et **0 Operational Fraud**, dans **7 pays africains**.

> `victims_FR.md` est le fichier éditorial de contrôle. Après validation, `victims.md` est synchronisé avec les mêmes faits, classifications et valeurs structurées.

## Avril 2025
### 04 Avril 2025
#### 🇸🇳 Sénégal - Forces Armées Sénégalaises (armee.sn)
- **Type d'incident:** Access Sale
- **Acteur / Groupe:** oblivion666
- **Secteur:** Défense / Sécurité Nationale
- **Site web:** armee.sn (Army.sn, Sigrh.armee.sn, Srvmail.armee.sn, Spami.armee.sn)
- **Statut:** Claim - Unverified
- **Description victime:** armee.sn est l'infrastructure de domaines des forces armées sénégalaises, couvrant plusieurs sous-domaines administratifs et de services internes (Army.sn, Sigrh.armee.sn, Srvmail.armee.sn, Spami.armee.sn).
- **Analyse:** L'acteur oblivion666 propose à la vente les domaines ci-dessus dans une publication de forum, ainsi qu'un accès administrateur revendiqué aux serveurs et à un pare-feu associés, publiée autour de la période de l'indépendance sénégalaise. Aucun fichier, identifiant ni autre preuve technique n'accompagne la publication ; il s'agit d'une simple annonce de vente d'accès sans échantillon accessible. Rien ne permet de vérifier si l'accès revendiqué est authentique, toujours valide ou encore disponible. Compte tenu de la cible (infrastructure de défense nationale), une compromission confirmée présenterait un impact potentiel élevé, mais il s'agit à ce stade d'une revendication non vérifiée en l'absence de preuve indépendante.

### 06 Avril 2025
#### 🇪🇬 Égypte - IACC Holdings
- **Groupe ransomware:** dragonforce
- **Secteur:** Finance / Logistique
- **Site web:** www.iacc.holdings
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Holding d'investissement privé égyptien axé sur le transport maritime et la logistique. L'acteur revendique l'exfiltration de 27,75 Go de données ; ce volume n'est pas vérifié indépendamment dans les éléments disponibles.

### 07 Avril 2025
#### 🇿🇦 Afrique du Sud - Cell C
- **Groupe ransomware:** ransomhouse
- **Secteur:** Technologies (Télécommunications)
- **Site web:** cellc.co.za
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d’impact:** Level 4
- **Description victime:** Opérateur de télécommunications sud-africain, l'un des principaux fournisseurs de services mobiles dans le pays.
- **Analyse:** AFRINTEL a examiné 20 captures de la publication de RansomHouse. Elles couvrent des données Cell C relatives aux clients et employés, des passeports, des appels, des SMS, l'activité vocale internationale, des contrats, des franchises, des accords de confidentialité, des documents internes et un résumé des revenus. Cette diversité est cohérente avec une exposition importante de données télécoms. Les impacts potentiels comprennent l'atteinte à la vie privée des abonnés, le phishing et la fraude, le ciblage des employés, l'exposition des métadonnées d'appels et de messages, l'espionnage commercial et la reconnaissance opérationnelle. Les captures ne confirment pas le vecteur d'accès initial, l'exhaustivité du jeu de données, le nombre d'abonnés touchés ni l'impact opérationnel. AFRINTEL ne reproduit aucune donnée personnelle, aucun détail de passeport, numéro de téléphone, contrat ni lien de téléchargement.

### 08 Avril 2025
#### 🇪🇬 Égypte - International Business Service
- **Groupe ransomware:** crypto24
- **Secteur:** Services aux entreprises / Externalisation (BPO)
- **Site web:** ibsns.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** International Business Service (IBS) est l'un des plus grands prestataires de services d'externalisation en Égypte. L'entreprise est spécialisée dans la gestion des ressources humaines, le recrutement de masse, l'externalisation de la paie et les services de maintenance/logistique pour les grandes entreprises et multinationales opérant en Égypte.

### 08 Avril 2025
#### 🇲🇦 Maroc - CNSS (Caisse Nationale de Sécurité Sociale)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Jabaroot DZ
- **Secteur:** Administrations publiques (Sécurité sociale)
- **Site web:** www.cnss.ma
- **Statut:** Claim - Data Sample Published
- **Description victime:** Caisse nationale de sécurité sociale du Maroc.
- **Analyse:** AFRINTEL a examiné deux exports structurés volumineux correspondant aux bases de données centrales de la CNSS, datés du même jour que la revendication. Le premier, une table employeurs/affiliés, contient environ 1 094 000 enregistrements avec des champs incluant le nom de l'entreprise, le numéro d'affiliation, les dates d'affiliation, le type d'employeur, la modalité de télépaiement, l'agence et la direction régionale, ainsi que le prénom, le nom, le numéro de carte d'identité nationale (CIN), l'adresse email et le numéro de téléphone de l'administrateur, plus des coordonnées bancaires (identifiant de compte, code banque) liées à l'employeur. Le second, une table des assurés, contient environ 1 996 000 enregistrements avec des champs incluant prénom, nom, numéro de CIN, numéro de passeport, numéro de carte de séjour, un numéro d'immatriculation interne, la date de création, le canal de la demande et le nom de l'employeur affilié. L'ampleur et la structure de ces deux tables sont cohérentes avec un extrait quasi complet et authentique des registres nationaux employeurs et assurés de la CNSS. La combinaison de numéros de CIN, de coordonnées et d'affiliations employeurs pour près de deux millions d'individus et plus d'un million d'employeurs représente une exposition à très fort impact, créant un risque substantiel de fraude à l'identité, de campagnes d'ingénierie sociale et de phishing ciblé à l'échelle nationale. AFRINTEL ne reproduit aucun nom, numéro de CIN, coordonnée ni référence bancaire issus de l'échantillon examiné.

### 08 Avril 2025
#### 🇲🇦 Maroc - Ministère de l'Industrie et du Commerce (miepeec.gov.ma)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Jabaroot DZ
- **Secteur:** Gouvernement / Économie et Industrie.
- **Site web:** miepeec.gov.ma
- **Statut:** Claim - Unverified
- **Description victime:** Le MIEPEEC est l'organe gouvernemental marocain chargé de piloter la stratégie industrielle, de promouvoir l'investissement et de réguler le commerce. Il gère des plateformes critiques d'interaction entre l'État et le secteur privé.

### 08 Avril 2025
#### 🇩🇿 Algérie - CNAS (Caisse Nationale des Assurances Sociales des Travailleurs Salariés)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Phantom Atlas
- **Secteur:** Gouvernement / Sécurité sociale
- **Site web:** [cnas.dz](https://www.cnas.dz)
- **Statut:** Claim - Data Sample Published
- **Description victime:** La CNAS est l'organisme public algérien gérant l'assurance maladie et les prestations sociales en nature des travailleurs salariés, au travers d'un réseau d'agences et de centres payeurs répartis sur le territoire national.
- **Analyse:** Phantom Atlas a publié le 8 avril 2025 une revendication présentée comme une réponse directe à des attaques informatiques récentes visant l'acteur, affirmant avoir mené une intrusion complète dans les bases de données de la CNAS et en avoir extrait plus de 860 200 documents. La publication ajoute des accusations générales de circuits financiers et logistiques opaques impliquant des entreprises algériennes et Dubaï, présentées comme devant être révélées dans une diffusion ultérieure ; ces accusations ne sont pas documentées dans le matériel examiné par AFRINTEL et sont rapportées ici uniquement comme éléments de discours de l'acteur, sans validation.

  AFRINTEL a examiné un échantillon local de 214 fichiers image (environ 97 Mo) associé à cette revendication. L'échantillon est homogène et correspond à des « Attestations d'ouverture des droits aux prestations en nature » délivrées par plusieurs agences CNAS (notamment Tizi Ouzou/Boghni et Alger/Belcourt), datées principalement de 2022 à 2024. Chaque document comporte l'identité complète de l'assuré (nom, prénom, date de naissance, adresse, numéro d'immatriculation à la sécurité sociale, centre d'affiliation) ainsi que celle de la personne couverte (assuré, conjoint, enfant ou ascendant), le taux de prise en charge, la date d'établissement, le nom de l'agent ayant délivré le document, un cachet et une signature.

  La cohérence du format sur l'ensemble de l'échantillon, la diversité des agences et centres payeurs représentés, ainsi que la présence de cachets et signatures plausibles, soutiennent un niveau de confiance élevé quant à l'authenticité d'un accès aux systèmes ou archives de la CNAS. Le volume observé (214 documents) reste toutefois très inférieur aux 860 200 revendiqués et ne permet pas de confirmer l'ampleur totale annoncée de la fuite. L'exposition de ces attestations pourrait faciliter l'usurpation d'identité, la fraude aux prestations sociales et le phishing ciblé contre les assurés et leurs ayants droit. AFRINTEL ne reproduit aucun nom, date de naissance, adresse, numéro d'immatriculation ni autre donnée personnelle issus des documents examinés.

### 09 Avril 2025
#### 🇩🇿 Algérie - MGPTT / Mutuelle Générale des Travailleurs de la Poste et des Télécoms
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Phantom Atlas
- **Secteur:** Social / Mutuelle de Santé.
- **Site web:** mgptt.dz
- **Statut:** Claim - Data Sample Published
- **Description victime:** La MGPTT est une institution sociale majeure en Algérie, couvrant les employés du secteur de la Poste, des Télécommunications et de l'Information. Elle gère les remboursements de soins et les aides sociales de dizaines de milliers de fonctionnaires et contractuels. La publication revendique plus de 13 Go de données internes de la MGPTT, comprenant des données personnelles ainsi que des documents et bases de données stratégiques, et mentionne également des fichiers sensibles du Ministère du Travail.
- **Analyse:** La publication de Phantom Atlas s'accompagne d'un message présentant l'opération comme une réponse directe à un piratage antérieur visant la CNSS, et adopte une tonalité hacktiviste explicitement liée au différend territorial du Sahara occidental entre le Maroc et l'Algérie ; ce cadrage politique est rapporté tel quel par AFRINTEL, sans validation ni prise de position sur les revendications territoriales ou les accusations réciproques de piratage.

  AFRINTEL a examiné un échantillon de 4 images (environ 496 Ko au total) associé à cette publication. Les images montrent des documents d'identité et de protection sociale photographiés ou scannés : des cartes d'assuré social algérien, une carte d'adhérent retraité MGPTT, une attestation d'affiliation délivrée par la CNAS, ainsi qu'un reçu de versement postal et un certificat d'hospitalisation associés à une clinique privée. Ces documents comportent des noms complets, dates de naissance, numéros d'immatriculation à la sécurité sociale, adresses et, pour certains, des photographies et des informations médicales ou financières de personnes nommément identifiées.

  Le volume observé (quatre images) est très inférieur aux 13 Go revendiqués et ne permet pas de corroborer l'ampleur annoncée de la fuite ni de confirmer qu'il s'agit d'un extrait représentatif d'un système d'information interne de la MGPTT. Une des images porte en outre le filigrane visible d'un service tiers de vente de documents en ligne, ce qui suggère que cet échantillon particulier pourrait provenir, au moins en partie, d'une source de documents déjà en circulation plutôt que d'une extraction directe des systèmes de la MGPTT. Ces éléments incitent à une évaluation prudente de la revendication : la présence de données personnelles et sociales réelles semble établie, mais l'origine exacte, l'exhaustivité et le lien direct avec une compromission des systèmes internes de la MGPTT restent incertains. AFRINTEL ne reproduit aucun nom, numéro d'immatriculation, date de naissance, adresse, photographie ni information médicale ou financière issus des images examinées.

### 09 Avril 2025
#### 🇩🇿 Algérie - Ministère du Travail
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Phantom Atlas
- **Secteur:** Gouvernement / Administration du travail
- **Site web:** Non précisé
- **Date de publication de la source:** 9 avril 2025
- **Statut:** Claim - Unverified
- **Description victime:** La publication fournie affirme que Phantom Atlas a accédé à des fichiers sensibles du Ministère algérien du Travail. Aucun échantillon spécifique au ministère n'est fourni ; cette cible est donc enregistrée séparément de la MGPTT sans confirmation indépendante de la compromission.
- **Analyse:** La revendication figure dans la même publication Phantom Atlas que celle concernant la MGPTT et peut correspondre à une même opération visant plusieurs institutions publiques algériennes. Aucun jeu de données spécifique au ministère n'a été collecté ni reproduit.

### 13 Avril 2025
#### 🇲🇷 Mauritanie - BMI / SEDAD Mobile Wallet
- **Acteur / Groupe:** Killer_Bee
- **Secteur:** Finance / Paiement mobile
- **Site web:** [bmi.mr](https://bmi.mr)
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Date de publication de la source:** 13 avril 2025
- **Dates observées dans l'échantillon:** 6 avril 2025

- **Description:**
  La publication affirme exposer une base associée à SEDAD, le service de banque digitale et de portefeuille mobile de BMI en Mauritanie. L'acteur revendique plus de 90 000 enregistrements liés à des réclamations de portefeuille et à des actions administratives.

- **Analyse:**
  L'échantillon visible est un enregistrement JSON structuré provenant d'un workflow de réclamations clients. Il contient des champs d'identité client, un numéro d'identification nationale, un numéro de téléphone, l'attribution à un utilisateur interne, des horodatages de création et de modification, un statut de traitement et un type de réclamation lié à l'activation. AFRINTEL ne reproduit aucune valeur personnelle visible dans l'échantillon. L'échantillon confirme la présence apparente de données structurées sensibles, mais le volume revendiqué, l'exhaustivité, l'origine et la compromission ne sont pas confirmés indépendamment. Le site officiel de BMI identifie SEDAD comme son service de banque digitale et de portefeuille électronique.

- **Recommandations:**
  1. Vérifier la revendication dans les journaux applicatifs, de base de données, d'API et d'administration de SEDAD, préserver les éléments de preuve et déterminer si des données d'identité et de téléphone ont été consultées.
  2. Faire pivoter les identifiants ou jetons administratifs exposés si nécessaire, examiner les actions privilégiées, imposer le MFA, surveiller les prises de contrôle de comptes et le phishing, puis notifier les utilisateurs et autorités compétentes si l'exposition est confirmée.

### 13 Avril 2025
#### 🇪🇬 Égypte - Tawasol
- **Groupe ransomware:** devman
- **Secteur:** Technologies de l'Information
- **Site web:** tawasol-it.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** C'est un intégrateur de solutions technologiques basé au Caire qui installe des systèmes de sécurité et d'infrastructure réseau pour les entreprises et les bâtiments intelligents.

### 13 Avril 2025
#### 🇲🇦 Maroc - Institut Supérieur des Métiers de l’Audiovisuel et du Cinéma (ISMAC)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** p4xar
- **Secteur:** Éducation / Enseignement supérieur / Audiovisuel et cinéma
- **Site web:** [ismac.ma](https://ismac.ma)
- **Statut:** Claim - Data Sample Published

- **Description:**
  L’Institut Supérieur des Métiers de l’Audiovisuel et du Cinéma (ISMAC) est un établissement public marocain d’enseignement supérieur basé à Rabat. Il forme des professionnels du cinéma, de l’audiovisuel, de la réalisation, de la production, de l’image et du son, sous la tutelle du ministère marocain de la Jeunesse, de la Culture et de la Communication.

- **Analyse:**
  Une publication attribuée à p4xar sur un forum présenté comme RaidForums affirme la compromission de l’application accessible à l’adresse `sul.ismac.ac.ma/app/` et la diffusion gratuite, via un canal Telegram, d’un fichier nommé `db.sql` présenté comme la base complète. L’échantillon visible est un export SQL substantiel de la table `n_etudiants`, dont la syntaxe et la structure sont compatibles avec MySQL ou MariaDB. Il contient des données personnelles d’étudiants, notamment des champs relatifs aux documents d’identité, à la naissance, aux adresses postales, aux adresses électroniques, aux numéros de téléphone, à la nationalité, au statut étudiant et aux comptes utilisateurs. Le croisement de ces données peut faciliter l’usurpation d’identité, le phishing ciblé, l’ingénierie sociale, la fraude documentaire et la récupération abusive de comptes. Certaines lignes comportent des valeurs nulles ou incomplètes et des anomalies d’encodage. L’échantillon établit la présence de données structurées sensibles, mais ne permet pas de confirmer le volume total, le nombre d’enregistrements, l’exhaustivité du fichier diffusé ni la compromission revendiquée par une source indépendante.

### 13 Avril 2025
#### 🇲🇦 Maroc - Ministère de l'Habitat et de la Politique de la Ville (mhpv.gov.ma)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** B4baYega
- **Secteur:** Gouvernement / Habitat / Politique de la ville
- **Site web:** mhpv.gov.ma
- **Statut:** Claim - Unverified
- **Description victime:** Le Ministère de l'Habitat et de la Politique de la Ville est l'administration marocaine chargée de la politique du logement et du développement urbain.
- **Analyse:** AFRINTEL a identifié une archive protégée par mot de passe dont le commentaire interne l'attribue explicitement à l'acteur B4baYega, avec un canal Telegram de contact pour d'autres bases de données « fraîches et privées ». Le contenu accessible de l'archive se limitait à une seule petite image ; AFRINTEL n'a pas pu accéder au jeu de données revendiqué ni le vérifier en raison de la protection par mot de passe, et ne peut donc confirmer ni son contenu, ni son volume, ni son authenticité. Cette entrée est consignée comme une revendication non vérifiée dans l'attente d'éléments complémentaires.

### 17 Avril 2025
#### 🇪🇬 Égypte - INI Investments
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** nightspire
- **Secteur:** Services financiers / Banque d'investissement / Conseil en financement de projets
- **Site web:** Non identifié avec certitude
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 2
- **Description victime:** INI Investments est une société égyptienne de banque d'investissement et de conseil en financement de projets, basée au Caire, intervenant dans les études de faisabilité, le montage financier et la clôture de financements pour des projets industriels et d'infrastructure.
- **Analyse:** AFRINTEL a examiné un échantillon local de documents cohérents avec la revendication du cybercriminel nightspire, incluant des modèles financiers internes de faisabilité (projections de TRI pluriannuelles allant de 39 % à 58 %, structure du capital et sources de financement) pour un projet de fabrication de tuyaux UPVC, une étude de marché concurrentielle comparant les volumes de production et parts de marché de plusieurs fabricants égyptiens d'UPVC nommés, un tableau de suivi de portefeuille de projets intitulé « Pipe line projects for Allweiler Farid Hassanein Pumps co » listant plusieurs contrats clients avec valeurs de projet en EGP, USD et EUR, statut et dates de soumission (référençant des clients et projets en Égypte, en Russie et en Arabie saoudite), une étude juridique et un procès-verbal de réunion, un rapport d'évaluation foncière pour le site du projet UPVC d'une société nommée, ainsi qu'un document référençant une extension de commande pour Hassan Allam, un grand groupe égyptien de construction et d'ingénierie. Les métadonnées des fichiers situent la preuve entre le 15 et le 17 avril 2025 ; cette date est traitée comme une date de preuve/découverte et non comme une date de publication confirmée. La cohérence interne des modèles financiers, la mention de contreparties industrielles égyptiennes réelles (Allweiler Farid Hassanein Pumps, Hassan Allam) et la cohérence entre l'étude de faisabilité, l'étude de marché et la documentation juridique soutiennent une évaluation à confiance élevée d'une compromission réelle des fichiers de projets internes d'INI Investments. Le matériel exposé consiste en des données confidentielles de transactions, de financement et de renseignement de marché plutôt qu'en des enregistrements personnels ou de consommateurs, créant un risque d'exposition de renseignement concurrentiel, de compromission de messagerie professionnelle et d'ingénierie sociale ciblée visant INI Investments ainsi que ses clients et contreparties industriels. AFRINTEL ne reproduit aucun nom de client, valeur de projet, montant financier ni référence de document issu du matériel examiné.
- **Note de double revendication :** Les fiches de mars et d’avril sont conservées séparément, car les dates et les éléments de preuve diffèrent. Elles concernent le même acteur, le même domaine et le même nom de victime, mais AFRINTEL ne peut pas déterminer avec les éléments disponibles si la publication d’avril actualise la revendication de mars ou correspond à une revendication distincte. Aucune fusion n’est effectuée dans l’attente d’une confirmation.
### 20 Avril 2025
#### 🇿🇦 Afrique du Sud - Premier Meats South Africa
- **Groupe ransomware:** devman
- **Secteur:** Agroalimentaire
- **Site web:** premiermeats.co.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Premier Meats est une entreprise sud-africaine spécialisée dans la transformation et la distribution de viandes de qualité.

### 22 Avril 2025
#### 🇹🇳 Tunisie - Natilait
- **Groupe ransomware:** cicada3301
- **Secteur:** Agroalimentaire / Industrie Laitière
- **Site web:** natilait.com.tn
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Description victime:** Natilait est un acteur majeur du secteur agroalimentaire en Tunisie, spécialisé dans la production et la commercialisation de lait (UHT), de yaourts et de produits dérivés.
- **Analyse:** Les 12 images JPG/PNG fournies comprennent au moins un tableau interne structuré de produits et de stocks, avec des codes articles, des descriptions de produits laitiers, des quantités et des champs d'inventaire ou de stock ; les autres images semblent liées à des documents opérationnels, mais plusieurs ne sont pas suffisamment lisibles pour permettre une extraction fiable. Ces éléments sont cohérents avec un échantillon de données issu de l'environnement de fabrication ou de distribution de Natilait et pourraient faciliter la veille concurrentielle, la fraude documentaire ou le ciblage de la chaîne d'approvisionnement. Le vecteur d'intrusion, l'étendue complète du jeu de données et la production des images par cicada3301 ne sont pas établis indépendamment. Aucun enregistrement produit ni montant commercial n'est reproduit.

### 23 Avril 2025
#### 🇪🇬 Égypte - Dar Al Teb
- **Groupe ransomware:** gunra
- **Secteur:** Santé
- **Site web:** daralteb.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** Dar Al Teb est l'un des centres médicaux les plus renommés d'Égypte, spécialisé dans la médecine de la reproduction, la fécondation in vitro (FIV) et la santé de la femme.
- **Analyse:** Le groupe ransomware gunra revendique la compromission de Dar Al Teb (daralteb.com) et affiche des échantillons de données sur sa page de fuite. Les échantillons montrent des tableaux de suivi de patients/cycles comportant nom du mari, nom de l'épouse, numéro de dossier, âge, deux numéros de téléphone, ainsi que des champs cliniques spécifiques à la fécondation in vitro (statut du sperme frais/congelé, nombre d'ovocytes/embryons attendus, andrologue référent, médecin traitant, et codes de résultat embryologique). Un jeu local plus large comprend sept classeurs mensuels (décembre 2022, puis mars à août 2023) totalisant environ 2 300 lignes de dossiers patients/cycles, ainsi que deux classeurs supplémentaires plus courts et une base de données Access (non ouverte). Le matériel technique examiné inclut un export de profil Wi-Fi contenant une clé pré-partagée en clair, des commandes réseau associées faisant référence à un partage de fichiers interne, un script PowerShell de déploiement d'une forêt Active Directory nommée « DarAlteb.local », ainsi qu'un fichier de connexion RDP préconfiguré vers un hôte interne avec redirection de presse-papiers et de lecteurs de cartes à puce activée. La combinaison d'échantillons de données cliniques nommément identifiables, d'un jeu de données patients pluriannuel et de matériel de configuration réseau et d'accès distant interne soutient une évaluation à confiance élevée d'une compromission réelle et étendue dépassant une simple revendication de site de fuite. La nature des données observées, à la fois des informations de santé reproductive nommément identifiables portant sur plusieurs milliers de patients et des éléments d'accès à l'infrastructure interne, justifie un niveau d'impact de niveau 4. AFRINTEL ne reproduit aucun nom de patient, numéro de téléphone, numéro de dossier, clé Wi-Fi, adresse IP ni autre donnée personnelle ou secret issu du matériel examiné.

