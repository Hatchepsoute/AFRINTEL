[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# Liste des victimes africaines de cyberattaques en Février 2025 (08 victimes)
👉🏾 [**English version available here**](./victims.md)
## Février 2025
### 03 Février 2025
#### 🇪🇬 Égypte - Xlab Group
- **Groupe ransomware:** fog
- **Secteur:** Services aux entreprises / Conseil en technologie (IT & Digital Solutions).
- **Site web:**  https://xlab-group.com/
- **Statut:** Claim - Unverified
- **Description victime:** Xlab Group est une société égyptienne spécialisée dans les solutions de marketing numérique, le développement de logiciels, le conseil en stratégie de marque et la transformation digitale pour les entreprises du Moyen-Orient.

### 12 Février 2025
#### 🇲🇦 Maroc - ASK Gras Savoye (askgs.ma)
- **Groupe ransomware:** ransomhub
- **Secteur:** Assurances / Courtage
- **Site web:** askgs.ma
- **Statut:** Claim - Unverified
- **Description victime:** ASK Gras Savoye est l'un des leaders du courtage d'assurance au Maroc.

### 12 Février 2025
#### 🇿🇦 Afrique du Sud - South African Weather Service (SAWS)
- **Groupe ransomware:** ransomhub
- **Secteur:** Services publics / Environnement (Météorologie)
- **Site web:** weathersa.co.za
- **Statut:** Claim - Unverified
- **Description victime:** South African Weather Service (SAWS) est le service météorologique national de l'Afrique du Sud, fournissant des prévisions et des alertes météorologiques.

### 19 Février 2025
#### 🇿🇲 Zambie - Government Services Portal (services.gov.zm)
- **Groupe ransomware:** flocker
- **Secteur:** Gouvernement / Services Publics Numériques.
- **Site web:** http://services.gov.zm/
- **Statut:** Claim - Data Sample Published
- **Description victime:** Le portail services.gov.zm est la plateforme centrale du gouvernement zambien (Smart Zambia Institute). Il regroupe plus de 322 services en ligne, allant de la demande de visas et permis aux services fiscaux et administratifs pour les citoyens et entreprises.
- **Analyse:** AFRINTEL a ouvert et inspecté (sans les reproduire) un volumineux ensemble de fichiers rattaché à la revendication, correspondant à l'export intégral du profil d'un hôte Windows nommé GSB, collecté sous le compte Administrateur par un outil dont la sortie est systématiquement étiquetée « _throne_ », sur trois sessions de collecte distinctes et horodatées s'étalant sur environ 13 heures (du soir du 10 février à la matinée du 11 février 2025), ce qui indique une exécution répétée ou persistante de l'outil plutôt qu'un passage unique. Le matériel est réparti en 44 archives de 1,7 à 52 Mo chacune (cohérent avec une exfiltration fragmentée vers un canal à taille limitée) pour un total d'environ 1,6 Go. Contenus vérifiés : des artefacts de navigateur Chrome et Firefox (bases d'autocomplétion, sauvegardes de session, état de sécurité des sites, base de clés NSS de Firefox, et un conteneur de cache disque de navigateur de 45 Mo dont l'inspection révèle qu'il contient du trafic HTTP mis en cache vers Microsoft 365/SharePoint/OneDrive/le CDN Akamai) ; des blobs de protection DPAPI Windows et du matériel de certificats/clés privées lié à l'identifiant de sécurité Windows de l'Administrateur ; un fichier de connexion RDP dont le champ de cible, après inspection, correspond à une adresse interne (RFC1918) ; une base d'historique Firefox dont l'activité de navigation limitée inclut, après inspection, une seconde adresse interne distincte ; un fichier d'annuaire téléphonique VPN/accès distant vide et inutilisé ; ainsi que des sauvegardes de projet Visual Studio 2017. Un fichier SQL récupéré contient une requête sur la table `ASPStateTempSessions`, accompagnée d'une note de support interne mentionnant un système nommé « ZIGS », ce qui indique une application ASP.NET adossée à Microsoft SQL Server et correspond à un accès administratif réel à l'environnement d'exploitation du portail plutôt qu'à une simple revendication ; un autre fichier est le script public bien connu de maintenance SQL Server d'Ola Hallengren, confirmant SQL Server comme moteur de base de données. L'ensemble inclut également une liste d'utilisateurs d'un tenant Office 365 : après inspection, les 89 comptes listés sont tous licenciés (Microsoft 365 E3), 85 sous le domaine dotgovsolutions.net, 3 sous le domaine par défaut onmicrosoft.com du tenant, et 1 sous un domaine externe sans lien apparent (un compte invité/externe au sein du même tenant) — indiquant que le tenant Microsoft 365 du portail est exploité par un prestataire informatique tiers, avec au moins une autre partie externe disposant d'un accès. Un fichier de mot de passe de 10 octets était présent mais n'a pas été ouvert par AFRINTEL. Aucune base de mots de passe enregistrés Chrome ou Firefox n'a été trouvée dans l'ensemble examiné. L'ampleur, la cohérence interne, les sessions de collecte multiples et la présence de matériel DPAPI/certificats, d'adresses réseau internes et d'artefacts RDP soutiennent un niveau de confiance élevé quant à une compromission réelle au niveau administrateur d'un poste, indépendamment de la revendication publique du groupe ransomware ; ce constat diffère sensiblement du cadrage de l'acteur en tant que simple « fuite de données de 1,2 Go », le matériel examiné relevant essentiellement d'artefacts système, liés aux identifiants et réseau interne plutôt que de dossiers citoyens. AFRINTEL ne reproduit aucun identifiant, certificat, donnée de session, nom de compte, adresse IP ni contenu de fichier issu de l'échantillon examiné.


### 19 Février 2025
#### 🇬🇭 Ghana - Brolly
- **Groupe ransomware:** killsec
- **Secteur:** Assurances/Insurtech
- **Site web:** brolly.africa
- **Statut:** Claim - Data Sample Published
- **Description victime:** Brolly est une startup insurtech ghanéenne qui propose des solutions d'assurance automobile flexibles et abordables (modèle "pay-as-you-go"). Elle permet aux conducteurs d'étaler leurs paiements d'assurance de manière hebdomadaire ou mensuelle via une plateforme numérique.
- **Analyse :** AFRINTEL a examiné la preuve fournie par KillSec sans reproduire de données personnelles. Le répertoire contient 4 exports CSV de polices, totalisant 183 lignes de données, 77 documents PDF et environ 10,4 Mo de matériel. La structure des CSV est cohérente avec les activités d'assurance automobile de Brolly et comprend des champs relatifs aux clients et polices, au type de couverture, à l'assureur, aux véhicules, aux dates de contrat, aux primes et à l'immatriculation. Les PDF comprennent 50 accords de paiement échelonné d'assurance automobile, 25 accords de prêt et 2 échéanciers de police automobile. Les noms de fichiers indiquent des périodes d'export de polices couvrant août à octobre 2024 ; les documents comprennent quant à eux des accords générés en octobre-novembre 2024. Ces dates correspondent aux éléments de preuve et ne constituent pas une date confirmée d'intrusion ou de publication. L'échantillon contient des informations personnelles, de contact, d'assurance et relatives aux véhicules, avec des risques potentiels de phishing ciblé, de fraude à l'identité, de fraude à l'assurance et d'ingénierie sociale. Le matériel observé permet d'évaluer avec une confiance moyenne à élevée que l'échantillon est thématiquement et structurellement cohérent avec des données de Brolly, mais AFRINTEL n'a pas confirmé indépendamment l'intrusion, l'étendue complète de l'accès ni l'exhaustivité du jeu de données. KillSec est l'acteur revendiqué ; aucune attribution indépendante au-delà de la publication ransomware observée n'est établie. AFRINTEL ne reproduit aucun nom, numéro de téléphone, numéro d'immatriculation, numéro de châssis, identifiant de police ni autre donnée personnelle brute.

### 21 Février 2025
#### 🇳🇦 Namibie - Paratus
- **Groupe ransomware:** akira
- **Secteur:** Télécommunications
- **Site web:** www.paratus.africa
- **Statut:** Claim - Unverified
- **Description victime:** Opérateur de télécommunications panafricain, investissant dans les infrastructures de réseau à travers l'Afrique.

### 22 Février 2025
#### 🇪🇬 Égypte - SPEED Co
- **Groupe ransomware:** hunter
- **Secteur:** Logistique/ distribustion
- **Site web:** speed-com.eg
- **Statut:** Claim - Unverified
- **Description victime:** SPEED Co (Speed Ahmed Hassan) est l'un des plus grands prestataires de services logistiques et de distribution en Égypte. L'entreprise gère le stockage et le transport de produits de grande consommation (FMCG) pour des multinationales et des marques locales majeures, s'appuyant sur une vaste flotte de véhicules et des centres de distribution automatisés. Le groupe revendique l'extraction d'un volume de 444,8 Go de données, comprenant 285 891 fichiers ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 23 Février 2025
#### 🇪🇬 Égypte - Shaghalni
- **Groupe ransomware:** killsec
- **Secteur:** Services / Recrutement (RH Tech)
- **Site web:** shaghalni.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Description victime:** Shaghalni est l'une des principales plateformes de recrutement en Égypte, spécialisée dans la mise en relation entre les demandeurs d'emploi (notamment les profils techniques et ouvriers) et les entreprises.
- **Analyse :** La fiche de publication du site de fuite KillSec concernant Shaghalni propose les données à la vente pour 5 000 €, accompagnée d'un échantillon local de documents référencés par cette fiche. La description sur le site de fuite correspond au profil public connu de Shaghalni, plateforme égyptienne gratuite de recherche d'emploi mettant en relation candidats et employeurs. L'échantillon examiné comprend un export CSV de comptes employeurs enregistrés sur la plateforme (nom de l'entreprise, téléphone, date d'inscription, pays, secteur, taille d'entreprise, site web et texte de profil), majoritairement des entreprises égyptiennes, ainsi qu'un ensemble de documents de vérification déposés par des employeurs, incluant des cartes d'identité nationale égyptiennes, des correspondances et certificats d'immatriculation fiscale de l'administration fiscale égyptienne, une licence d'entreprise du ministère égyptien du Tourisme, et un certificat d'immatriculation d'entreprise du ministère saoudien du Commerce et de l'Investissement, indiquant que la base d'employeurs de la plateforme dépasse le cadre égyptien. Les documents sont cohérents avec l'activité déclarée de Shaghalni en tant que plateforme de recrutement orientée employeurs. AFRINTEL ne reproduit aucun numéro de carte d'identité, numéro d'immatriculation d'entreprise, référence fiscale, numéro de téléphone ni nom issus de l'échantillon examiné. Le matériel examiné concerne les comptes employeurs/entreprises et leurs documents de vérification ; il ne permet pas d'établir si des données personnelles de demandeurs d'emploi faisaient également partie du jeu de données revendiqué.

