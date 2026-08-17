# Fiches victimes AFRINTEL 2025

[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Type de menace](https://img.shields.io/badge/Menace-Ransomware-red)
![Source](https://img.shields.io/badge/Source-OSINT-darkgreen)
![Type d'intelligence](https://img.shields.io/badge/Intel-CTI-purple)

Les fiches ci-dessous sont compilées à partir des fichiers mensuels AFRINTEL de 2025. Les dates de publication, de découverte et les niveaux d'incertitude sont conservés lorsqu'ils figurent dans la source.

## Janvier 2025

### 06 Janvier 2025
#### 🇰🇪 Kenya - Molars Dental Practice
- **Groupe ransomware:** ransomhub
- **Secteur:** Santé (Dentaire)
- **Site web:** https://molars.co.ke
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d’impact:** Level 3
- **Analyse:** AFRINTEL a examiné le classeur fourni et huit fichiers de preuve supplémentaires. Le classeur contient des éléments de structure salariale et des feuilles distinctes pour les médecins, la comptabilité, les ressources humaines, les opérations et plusieurs fonctions de support. Les preuves comprennent également une capture de paiement bancaire et des documents cohérents avec l’administration du personnel ou de la paie. L’échantillon soutient une exposition potentielle des rémunérations, des structures départementales, des opérations internes et d’informations liées au traitement financier. Le volume revendiqué de 19 Go, le vecteur d’accès et l’exhaustivité des données restent non vérifiés. AFRINTEL ne reproduit aucun nom, salaire, coordonnée bancaire ni autre donnée personnelle.
- **Description victime:** Molars est un réseau de cliniques dentaires de premier plan basé à Nairobi, fournissant des soins spécialisés allant de l'orthodontie à la chirurgie dentaire pour une clientèle locale et internationale. L'acteur revendique l'exfiltration de 19 Go de données ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 09 Janvier 2025
#### 🇪🇬 Égypte - General Authority for Government Services
- **Groupe ransomware:** funksec
- **Secteur:** Administrations publiques/ Finances / Marchés Publics.
- **Site web:** gags.gov.eg
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** La GAGS est l'autorité régulatrice des services gouvernementaux en Égypte. Elle supervise les procédures d'appel d'offres, la gestion des stocks de l'État et l'aliénation des biens publics.
- **Analyse:** AFRINTEL a examiné un ensemble local de captures d'écran cohérentes avec la revendication du cybercriminel funksec, montrant un accès authentifié de niveau administrateur à deux modules internes de la plateforme GAGS : une interface de gestion des réclamations et appels d'offres publics listant des dossiers avec numéros de référence, dates et objets, et une interface de gestion des biens et bâtiments publics listant des noms d'entités, des superficies et des évaluations financières. Une capture montre un motif d'injection SQL aveugle de type booléen dans un champ de recherche applicatif, indiquant la technique employée pour obtenir ou sonder l'accès à la base de données. AFRINTEL n'a pas observé d'export structuré ni d'échantillon massif au-delà de ces captures d'interface. La combinaison d'une session administrateur authentifiée, de chemins applicatifs internes et d'un motif d'injection visible soutient une évaluation à confiance élevée d'une intrusion réelle dans les systèmes backend de la GAGS, bien que l'ampleur exacte des données réellement exfiltrées reste non confirmée. Compte tenu du rôle de la GAGS dans les marchés publics égyptiens et la gestion du patrimoine de l'État, cet incident présente un risque pour l'intégrité et la confidentialité des procédures d'appel d'offres et des données patrimoniales publiques. AFRINTEL ne reproduit aucune référence de marché, nom d'entité ni donnée financière issue du matériel examiné.

### 09 Janvier 2025
#### 🇿🇦 Afrique du Sud - Pick n Pay (pnp.co.za)
- **Groupe ransomware:** apt73
- **Secteur:** Commerce de détail/Grande distribution (Retail).
- **Site web:** pnp.co.za
- **Statut:** Claim - Unverified
- **Description victime:** **Pick n Pay Group Ltd** est le deuxième plus grand détaillant de produits alimentaires en Afrique du Sud.

### 11 Janvier 2025
#### 🇲🇦 Maroc - SEOCOM Marrakech (seocommarrakech.com)
- **Groupe ransomware:** funksec
- **Secteur:** Technologies / Marketing Digital / SEO.
- **Site web:** seocommarrakech.com
- **Statut:** Claim - Unverified
- **Description victime:** EOCOM est une agence marocaine fournissant des services de SEO (Search Engine Optimization), de gestion de campagnes publicitaires (SEA) et de développement web pour des entreprises locales et internationales.

### 14 Janvier 2025
#### 🇳🇬 Nigeria - INTELS Nigeria Limited (intelservice.com)
- **Groupe ransomware:** ransomhub
- **Secteur:** Logistique Pétrolière et Gazière / Services Portuaires.
- **Site web:** intelservices.com
- **Statut:** Claim - Unverified
- **Description victime:** Intels est un pilier de l'économie nigériane, gérant 90 % des activités de soutien à l'exploration pétrolière offshore. Le groupe affirme avoir exfiltré environ 1,5 To de données sensibles ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 14 Janvier 2025
#### 🇪🇬 Égypte - Sharm Reef Hotel
- **Groupe ransomware:** spacebears
- **Secteur:** Hôtellerie / Tourisme.
- **Site web:** sharmreefhotel.com / sharmelsheikh.com
- **Statut:** Claim - Unverified
- **Description victime:** Le Sharm Reef Hotel est un complexe hôtelier 4 étoiles situé sur le plateau d'Om El Seid à Charm el-Cheikh en Egypte.

### 15 Janvier 2025
#### 🇪🇬 Égypte - Misr Technology Services (MTS / mts.gov.eg)
- **Groupe ransomware:** funksec
- **Secteur:** Administrations publiques
- **Site web:** mts.gov.eg
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** Misr Technology Services (MTS) est l'entité gouvernementale égyptienne responsable du développement et de la gestion de la plateforme nationale de facilitation du commerce, notamment le système Nafeza.
- **Analyse:** AFRINTEL a examiné un ensemble local de captures d'écran et de documents PDF générés par les systèmes internes du secteur du Transport Maritime et de la Logistique, notamment l'Egyptian Maritime Data Bank, cohérents avec la revendication du cybercriminel funksec. Le matériel examiné inclut une demande individuelle de permis nommant un demandeur, une agence maritime affiliée et une date de dépôt ; un rapport comparatif de trafic portuaire listant des statistiques d'escales par port pour 2023 et 2024 ; une liste de projets et opportunités d'investissement portuaire ; ainsi que des rapports détaillés de recouvrement sectoriel couvrant plusieurs périodes entre janvier et avril 2024, listant des noms de clients, types d'opérations, numéros de référence et montants encaissés via le canal point de vente du secteur. Deux des documents examinés portent un horodatage d'impression système daté du 14 et du 15 janvier 2025, cohérent avec la date de publication de la revendication. La présence de rapports générés en interne, datés et nommant des demandeurs et clients, combinée à l'en-tête propre de la plateforme et aux métadonnées d'impression, soutient une évaluation à confiance élevée d'un accès réel aux systèmes de reporting internes de MTS. Compte tenu du rôle de MTS dans la gestion de la plateforme nationale égyptienne de facilitation du commerce, notamment le système Nafeza, cet incident présente un risque pour le personnel des agences maritimes, les données financières clients et la confidentialité des opérations nationales de facilitation du commerce. AFRINTEL ne reproduit aucun nom de demandeur, nom de client, donnée financière ni référence documentaire issue du matériel examiné.

### 21 Janvier 2025
#### 🇩🇿 Algérie - Centre Universitaire de Barika (cu-barika.dz)
- **Groupe ransomware:** funksec
- **Secteur:** Éducation / Enseignement Supérieur / Recherche.
- **Site web:** cu-barika.dz
- **Statut:** Claim - Unverified
- **Description victime:** Le Centre Universitaire de Barika (Ahmed Ben Abderrezak El Hamouda) est un pôle d'enseignement supérieur situé dans la wilaya de Batna, proposant des formations en sciences technologiques, droit, et sciences humaines.

### 21 Janvier 2025
#### 🇩🇿 Algérie - Clinique Inaya (inayaclinic.org)
- **Groupe ransomware:** spacebears
- **Secteur:** Santé
- **Site web:** inayaclinic.org
- **Statut:** Claim - Unverified
- **Description victime:** La Clinique Inaya est une structure médicale pluridisciplinaire en Algérie, réputée pour ses pôles d'excellence en cardiologie, chirurgie cardiovasculaire et gynécologie-obstétrique.

### 24 Janvier 2025
#### 🇳🇬 Nigeria - Lower Niger River Basin Development Authority (LNRBDA)
- **Groupe ransomware:** GDLockerSec
- **Secteur:** Administrations publiques / Ressources en Eau / Agriculture.
- **Site web:** lnrbda.gov.ng
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Description victime:** La LNRBDA est une agence stratégique sous la tutelle du ministère fédéral des Ressources en Eau du Nigeria. Elle gère des projets de barrages, d'irrigation, d'approvisionnement en eau potable et de développement rural.
- **Analyse :** AFRINTEL a examiné un échantillon local de fichiers cohérents avec la revendication du cybercriminel GDLockerSec, comprenant des exports bruts de base de données du backend applicatif de l'agence ainsi qu'un fichier de base de données de sessions. Les tables examinées incluent une table d'informations candidats (66 enregistrements) avec nom complet, date de naissance, zone d'administration locale (LGA), téléphone, email, nom/email/téléphone/adresse d'un répondant/référent, adresse de contact, institution et un champ libre « motif de candidature », cohérent avec un formulaire de candidature à un programme d'insertion professionnelle pour diplômés ; une table utilisateurs stockant des emails accompagnés de mots de passe en clair ; une table d'utilisateurs administratifs contenant des identifiants de compte de niveau administrateur (« AD ») hachés ; ainsi qu'une table de validation associant des codes à usage unique à des numéros de téléphone. Une table d'actualités distincte contient du contenu public courant et n'est pas sensible. La combinaison d'un export structuré multi-tables réellement issu du backend applicatif, d'une base de données de sessions associée, et de la présence de mots de passe utilisateurs en clair et d'identifiants administrateur, soutient une évaluation à très haute confiance d'une compromission réelle et profonde des systèmes de l'agence, plutôt qu'une simple revendication. Compte tenu du statut du LNRBDA en tant qu'agence fédérale nigériane, l'exposition d'identifiants en clair, de comptes administrateur, de données personnelles de candidats et de codes à usage unique liés à des numéros de téléphone crée un risque sévère de prise de contrôle de comptes, de compromission latérale supplémentaire des systèmes gouvernementaux, ainsi que de fraude à l'identité ou de phishing ciblé visant les candidats et leurs référents. AFRINTEL ne reproduit aucun nom, date de naissance, adresse, numéro de téléphone, email, mot de passe ni code issu de l'échantillon examiné.

### 24 Janvier 2025
#### 🇲🇦 Maroc - Université Sidi Mohamed Ben Abdellah (www.usmba.ac.ma)
- **Groupe ransomware:** GDLockerSec
- **Secteur:** Éducation / Enseignement Supérieur / Recherche.
- **Site web:** usmba.ac.ma
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 2
- **Description victime:** L'USMBA est une université multidisciplinaire comprenant de nombreux établissements (Facultés de Médecine, des Sciences, des Lettres, ENCG, ENSA, etc.).
- **Analyse :** AFRINTEL a examiné un échantillon local de matériel cohérent avec la revendication du cybercriminel GDLockerSec, constitué de captures affichant une base de données interne structurée des laboratoires et équipes de recherche, restituée via l'outil de visualisation CSV propre à l'acteur. Les enregistrements examinés listent des unités et départements de recherche cohérents avec l'École Normale Supérieure de Fès, rattachée à l'USMBA, ainsi que leurs thématiques de recherche déclarées et projets en cours (couvrant des domaines tels que la chimie de la matière condensée, l'écologie fonctionnelle, le génie mécanique, l'intelligence artificielle et les réseaux de neurones, le traitement automatique du langage, l'entreposage de données et le traitement d'images). Des personnes nommément associées à chaque unité de recherche figurent dans les données sous-jacentes mais ont été caviardées dans le matériel examiné par AFRINTEL. La cohérence entre les unités de recherche listées, leurs thématiques et la structure académique connue de l'USMBA soutient une évaluation à confiance élevée selon laquelle le matériel reflète une base de données interne réelle d'administration de la recherche plutôt qu'un échantillon fabriqué. Le jeu de données exposé concerne principalement l'organisation institutionnelle de la recherche et son personnel plutôt que des dossiers étudiants ou financiers, créant un risque modéré de phishing ciblé et d'usurpation d'identité visant des chercheurs et directeurs de laboratoire nommément identifiés. AFRINTEL ne reproduit aucun nom, identifiant de laboratoire ni détail de projet de recherche au-delà de ce qui est nécessaire pour caractériser la nature de l'exposition.

### 26 Janvier 2025
#### 🇳🇬 Nigeria - Achievers Journal of Scientific Research
- **Groupe ransomware:** funksec
- **Secteur:** Éducation / Recherche Scientifique / Publication Académique.
- **Site web:** achieverssciencejournal.org
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 2
- **Description victime:** L'AJSR est une revue multidisciplinaire à comité de lecture qui publie des travaux de recherche originaux dans les domaines des sciences appliquées, de l'ingénierie et des technologies.
- **Analyse:** AFRINTEL a examiné un échantillon local de matériel cohérent avec la revendication du cybercriminel funksec, incluant deux captures du panneau d'administration « Users & Roles » de la plateforme Open Journal Systems (OJS) de la revue, un export CSV de 64 enregistrements utilisateurs avec des champs prénom, nom, email, téléphone, pays, adresse postale, date d'inscription et rôles attribués (administrateur du site, rédacteur, auteur, relecteur et rôles associés), ainsi qu'une page de divulgation phpinfo() (PHP 8.1.31 sur un serveur cPanel/CloudLinux) confirmant un accès réel aux détails de configuration du serveur. Les enregistrements utilisateurs sont systématiquement associés à des institutions académiques nigérianes (domaines email incluant federalpolyilaro.edu.ng, wellspringuniversity.edu.ng et uniosun.edu.ng), cohérent avec le périmètre académique déclaré de la revue. Un enregistrement utilisateur contient un lien de spam injecté à la place d'un champ de nom, indiquant que les champs de saisie de la plateforme n'étaient pas correctement assainis, cohérent avec une application web mal sécurisée et exploitable. La combinaison d'un export réel du panneau d'administration, d'une divulgation phpinfo() correspondante et de domaines email académiques nigérians soutient une évaluation à confiance élevée d'une compromission réelle. Le jeu de données exposé comprend des noms, emails, pays et rôles de plateforme de contributeurs académiques plutôt que des données financières ou de santé, créant un risque de phishing ciblé et de prise de contrôle de comptes visant les auteurs, relecteurs et rédacteurs de la revue. AFRINTEL ne reproduit aucun nom, adresse email, nom d'utilisateur ni chemin serveur issu de l'échantillon examiné.

### 26 Janvier 2025
#### 🇪🇬 Égypte - FGSE, Université du Caire (fgse.cu.edu.eg)
- **Groupe ransomware:** GDLockerSec
- **Secteur:** Éducation / Enseignement Supérieur / Recherche Pédagogique.
- **Site web:** fgse.cu.edu.eg
- **Statut:** Claim - Unverified
- **Description victime:** La FGSE (Faculty of Graduate Studies for Education) est l'une des institutions de recherche les plus anciennes et les plus respectées d'Égypte.

### 27 Janvier 2025
#### 🇺🇬 Ouganda - QED (qed.co.ug)
- **Groupe ransomware:** funksec
- **Secteur:** Services de Conseil / SMS en masse et messagerie broadcast
- **Site web:** qed.co.ug
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Description victime:** QED est un cabinet leader en Ouganda spécialisé dans le "Monitoring, Evaluation and Learning" (MEL). Il accompagne des projets financés par des organisations internationales dans les secteurs de la santé, de l'éducation et de la gouvernance, et exploite une plateforme de SMS en masse et de messagerie broadcast utilisée pour des campagnes auprès de bénéficiaires pour le compte de clients.
- **Analyse:** AFRINTEL a examiné un ensemble local de captures d'écran cohérentes avec la revendication du cybercriminel funksec, montrant un accès administrateur authentifié à une plateforme de SMS en masse et de messagerie broadcast hébergée sur un sous-domaine de QED et brandée pour un client identifié dans l'interface comme « d.lightUganda » (un fournisseur de services d'énergie solaire en paiement à l'usage actif en Ouganda). Une capture montre un module de gestion des contacts listant 1 847 472 enregistrements individuels (numéro de téléphone, prénom et nom) utilisés pour les campagnes SMS en masse. Une autre capture montre le panneau de gestion des utilisateurs de la plateforme, dans lequel un compte nommé « Funksec » avec un rôle administrateur et une adresse email associée avait été créé, indiquant que l'acteur a conservé un accès administrateur persistant à l'application plutôt qu'une simple consultation. Séparément, AFRINTEL a examiné quatre fichiers CSV exportés cohérents avec la même plateforme (rapports de livraison et de SMS entrants) totalisant près de 89 000 enregistrements, contenant des numéros MSISDN expéditeur/destinataire, un statut de message et des horodatages allant jusqu'au 27 janvier 2025, correspondant à la date de publication de la revendication. La combinaison d'un compte administrateur auto-créé laissé dans l'application de la victime, d'un volume de contacts concordant sur deux captures indépendantes, et de journaux de livraison exportés et datés, soutient une évaluation à très haute confiance d'une compromission réelle et durable. Compte tenu de l'ampleur de la base de contacts exposée et de son lien apparent avec un client de services financiers énergétiques grand public, cet incident présente un risque significatif de campagnes de smishing, de fraude et d'usurpation d'identité à grande échelle visant les abonnés mobiles ougandais. AFRINTEL ne reproduit aucun numéro de téléphone, nom, contenu de message ni identifiant de compte issu du matériel examiné.

### 27 Janvier 2025
#### 🇿🇲 Zambie - Workers (workers.com.zm)
- **Groupe ransomware:** babuk2
- **Secteur:** Services RH / Recrutement
- **Site web:** workers.com.zm
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** Entreprise zambienne de services de recrutement et de travail temporaire.
- **Analyse:** AFRINTEL a examiné un export local de base de données MySQL cohérent avec la plateforme WordPress du site, daté du 22 octobre 2024, contenant le schéma complet et les données des tables cœur de WordPress (dont la table des comptes utilisateurs), des tables de commandes WooCommerce, ainsi qu'un module de dons basé sur l'extension GiveWP (tables donateurs, métadonnées de dons et abonnements), aux côtés d'un module personnalisé de commandes et paiement. La structure et l'exhaustivité de cet export sont cohérentes avec une sauvegarde complète de la base backend plutôt qu'avec une revendication partielle ou un échantillon superficiel. AFRINTEL signale, à titre de point d'attention, que le fichier examiné ne portait aucune marque propre à un acteur permettant de confirmer l'attribution ; l'attribution à babuk2 est conservée telle qu'actuellement enregistrée, et une vérification manuelle de cette attribution, incluant une analyse de possible double revendication, est recommandée. Compte tenu de la présence de comptes utilisateurs, d'enregistrements de commandes et de tables liées aux donateurs et paiements, cet incident présente un risque de prise de contrôle de comptes, de fraude liée aux paiements et d'exposition de données de donateurs. AFRINTEL ne reproduit aucun nom d'utilisateur, hash de mot de passe, enregistrement de commande ni détail de donateur issu du matériel examiné.

### 27 Janvier 2025
#### 🇰🇪 Kenya - Zetech University (zetech.ac.ke)
- **Groupe ransomware:** babuk2
- **Secteur:** Éducation / Enseignement Supérieur
- **Site web:** zetech.ac.ke
- **Statut:** Claim - Unverified
- **Description victime:** Zetech University est une institution d'enseignement supérieur de premier plan au Kenya.

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

## Mars 2025

### 02 Mars 2025
#### 🇧🇼 Botswana - IT-IQ Botswana
- **Groupe ransomware:** play
- **Secteur:** Conseil en technologies
- **Site web:** www.itiq.co.bw
- **Statut:** Claim - Unverified
- **Description victime:** IT-IQ Botswana est l'un des principaux fournisseurs de solutions informatiques et de formations certifiées (Microsoft, Cisco, VMware) au Botswana.

### 02 Mars 2025
#### 🇳🇬 Nigeria - Workforce Group
- **Groupe ransomware:** killsec
- **Secteur:** Éducation / Services RH
- **Site web:** workforcegroup.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Description victime:** Entreprise nigériane de services éducatifs et de gestion des ressources humaines.
- **Analyse :** AFRINTEL a examiné un échantillon local de documents ainsi qu'un export structuré de données de personnel associés à cette revendication, ainsi qu'une archive téléchargée mais incomplète (un seul volume d'environ 26 Mo appartenant apparemment à une archive fractionnée plus vaste ; AFRINTEL n'a ni extrait ni ouvert son contenu). Le matériel examiné comprend un vaste jeu de données de personnel couvrant identifiants employés, noms, coordonnées, champs démographiques, informations de référents et données de placement chez des employeurs, faisant référence à d'importantes banques nigérianes, cohérent avec le rôle de Workforce Group en tant que prestataire d'externalisation RH et de placement de personnel. L'échantillon comprend également des documents RH à en-tête de Workforce Group (formulaire d'accusé de réception du livret d'accueil, formulaire de demande de congé, lettre d'offre d'emploi avec clause de confidentialité) ainsi que des documents d'intégration liés au secteur financier, dont des formulaires de demande de prêt personnel comportant des numéros BVN (Bank Verification Number), dates de naissance, numéros de téléphone, adresses personnelles et coordonnées de personnes à contacter, ainsi qu'un formulaire de garant émis par une banque commerciale nigériane. Les documents sont cohérents avec l'image de marque de Workforce Group et son rôle d'externalisation auprès de plusieurs institutions financières nigérianes. Compte tenu de l'ampleur du jeu de données de personnel et de la présence de numéros BVN et de données de personnel bancaire couvrant plusieurs grandes banques, l'exposition potentielle dépasse une seule organisation et touche l'écosystème plus large de l'externalisation RH du secteur bancaire nigérian, créant un risque significatif de fraude à l'identité, de prise de contrôle de comptes et d'ingénierie sociale ciblée. AFRINTEL ne reproduit aucun nom, numéro BVN, coordonnée, adresse ni information de compte issus du matériel examiné, et n'a pas vérifié si l'archive disponible représente l'intégralité du jeu de données revendiqué.

### 03 Mars 2025
#### 🇿🇦 Afrique du Sud - LINKGROUP
- **Groupe ransomware:** arcusmedia
- **Secteur:** Conseil en technologies
- **Site web:** linkgroup.co.za
- **Statut:** Claim - Unverified
- **Description victime:** LINKGROUP est une société sud-africaine de conseil en informatique et de services télécoms.

### 03 Mars 2025
#### 🇹🇿 Tanzanie - synaptic.co.tz
- **Groupe ransomware:** arcusmedia
- **Secteur:** Conseil en technologies
- **Site web:** synaptic.co.tz
- **Statut:** Claim - Unverified
- **Description victime:** Société tanzanienne de conseil en informatique.

### 05 Mars 2025
#### 🇳🇬 Nigeria - Medical Rehabilitation Therapists Board (MRTB)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** MisterSam
- **Secteur :** Administration publique / Régulation de la santé
- **Site web :** Non précisé
- **Statut :** Claim - Unverified
- **Description victime :** Le Medical Rehabilitation Therapists Board of Nigeria (MRTB) est un organisme public nigérian de régulation des professions de la réadaptation médicale.
- **Analyse :** Une publication de forum affirme que des sauvegardes de plusieurs instances CMS associées à l'organisme contiennent des accès à des bases de données et d'autres identifiants pouvant permettre un accès plus large aux serveurs. Le contenu caché, le domaine, les identifiants et un échantillon de base vérifiable ne sont pas exposés dans le matériel disponible. Il s'agit d'une revendication non vérifiée d'exposition de CMS et de sauvegardes ; aucun identifiant ni donnée personnelle n'est reproduit.

### 07 Mars 2025
#### 🇿🇦 Afrique du Sud - ACDC Express
- **Groupe ransomware:** lynx
- **Secteur:** Commerce de détail (Distribution)
- **Site web:** acdcdynamics.co.za
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime:** ACDC Dynamics est un important fabricant, importateur et distributeur sud-africain de composants électriques, d'outils et d'équipements de sécurité.
- **Analyse :** La fiche de publication du site de fuite Lynx concernant ACDC Express (ACDC Dynamics) classe la publication dans les catégories Encrypted, Proof et AD Dump, et décrit une divulgation unique intitulée « Data » couvrant les RH, des données financières, des contrats et du matériel confidentiel, pour un volume revendiqué de 800 Go. Elle indique une date de publication du 7 mars 2025 et cite un chiffre d'affaires estimé de la victime à 123 000 000 $, une métrique auto-déclarée par l'acteur et non vérifiée de façon indépendante. La description de la victime sur le site de fuite correspond au profil public connu d'ACDC Dynamics (fondée en 1984, distributeur de matériel électrique et électronique basé à Edenvale, Johannesburg, avec des succursales à Germiston, Cape Town, Pinetown et Riverhorse). Le contenu des fichiers référencés par les catégories « Proof » et « AD Dump » n'a pas été examiné et n'est pas reproduit.


### 11 Mars 2025
#### 🇪🇬 Égypte - ISEE (International School of Elite Education)
- **Groupe ransomware:** funksec
- **Secteur:** Éducation / Enseignement privé.
- **Site web:** isee-eg.com
- **Statut:** Claim - Unverified
- **Description victime:** International School of Elite Education (ISEE) est un établissement scolaire privé prestigieux situé au Caire.

### 25 Mars 2025
#### 🇪🇬 Égypte - MISR AL MAHABA HOSPITAL
- **Groupe ransomware:** nightspire
- **Secteur:** Santé / Secteur Hospitalier
- **Site web:** misralmahaba.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Description victime:** L'hôpital Misr Al Mahaba est un centre de soins privé important au Caire.
- **Analyse :** La fiche de publication du site de fuite NightSpire concernant l'hôpital Misr Al Mahaba, publiée le 24 mars 2025, annonce un délai/compte à rebours au 27 mars 2025 et un volume revendiqué de 100 Go. Un échantillon local de documents cohérents avec la revendication comprend une carte d'assurance maladie nationale égyptienne et une carte d'identité nationale (chacune montrant une photo de patient et des identifiants partiellement visibles), deux formulaires hospitaliers de transfert externe adressés à l'Autorité générale d'assurance maladie et portant le cachet de l'hôpital, ainsi qu'un relevé de facturation détaillé pour une admission en cathétérisme cardiaque/CCU listant des postes liés au diagnostic, les médicaments administrés individuellement et les montants totaux, tamponné par le service comptabilité de l'hôpital. Les documents sont cohérents avec l'image de marque et le format de facturation de l'hôpital Misr Al Mahaba. L'échantillon indique une exposition de documents identifiant des patients et de dossiers cliniques/de facturation détaillés, créant un risque significatif d'usurpation d'identité médicale, de fraude à l'assurance et de phishing ciblé contre les patients concernés. Aucun nom de patient, numéro de carte d'identité nationale, numéro d'assurance maladie, diagnostic ni montant de facturation n'est reproduit.

### 30 Mars 2025
#### 🇪🇬 Égypte - INI Investments
- **Groupe ransomware:** nightspire
- **Secteur:** Finance
- **Site web:** iniholdings.com
- **Statut:** Claim - Unverified
- **Description victime:** INI Investments est une société de portefeuille (holding) égyptienne diversifiée. Elle investit dans des secteurs stratégiques tels que l'immobilier, l'énergie, la technologie et les services financiers. L'acteur revendique l'exfiltration de 400 Go de données ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.
- **Note de double revendication :** Les fiches de mars et d’avril sont conservées séparément, car les dates et les éléments de preuve diffèrent. Elles concernent le même acteur, le même domaine et le même nom de victime, mais AFRINTEL ne peut pas déterminer avec les éléments disponibles si la publication d’avril actualise la revendication de mars ou correspond à une revendication distincte. Aucune fusion n’est effectuée dans l’attente d’une confirmation.
### 26 Mars 2025
#### 🇧🇫 Burkina Faso - Tableau de bord gouvernemental COVID-19/vaccination
- **Acteur / Groupe :** Ghudra
- **Secteur :** Santé / Santé publique
- **Site web :** Non précisé
- **Statut :** Claim - Unverified
- **Niveau de confiance :** Medium
- **Niveau d’impact :** Level 3
- **Type d’incident :** Vente d’accès
- **Description :** Une publication propose un accès administrateur à un tableau de bord gouvernemental burkinabè de suivi de la COVID-19 et de la vaccination, pour un prix revendiqué de 300 $.
- **Analyse :** La publication affiche des indicateurs COVID-19, de tests et de vaccinations, et propose un accès administrateur à la vente. Le domaine, la validité, la provenance et le lien avec les revendications Sentap restent inconnus. Il s'agit d'une revendication non vérifiée d'accès à la vente ; aucun identifiant ni donnée personnelle n'est reproduit.

### 31 Mars 2025
#### 🇷🇼 Rwanda - moh.gov.rw
- **Groupe ransomware:** babuk2
- **Secteur:** Administrations publiques (Santé)
- **Site web:** moh.gov.rw
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description victime:** Ministère de la Santé du Rwanda.
- **Analyse :** Un ensemble d'éléments et un échantillon texte brut sont directement associés à cette revendication. L'élément le plus significatif est un webshell PHP actif déployé sur un serveur Linux dont le nom d'hôte est « covid-mass-testing », exécutant PHP 7.4 sous l'utilisateur www-data avec le safe mode désactivé et un répertoire de travail sous /var/www ; le webshell expose des modules gestionnaire de fichiers, console, SQL, exécution PHP et bruteforce, indiquant une capacité d'exécution de code à distance complète plutôt qu'une simple revendication de données. Un panneau d'administration de base de données phpMyAdmin liste 23 tables avec des nombres de lignes approximatifs, incluant des tables cohérentes avec des candidatures (~110 500 lignes), des données de session (~155 400 lignes), des cliniciens (~29 500 lignes), des données RH (~9 400 lignes), des documents (~9 700 lignes) et des enregistrements de mots de passe/authentification (~4 800 lignes), indiquant un accès direct au niveau base de données d'un système de gestion des candidatures/effectifs du secteur de la santé, et non uniquement au site web public du ministère. Un élément supplémentaire, provenant apparemment du même portail de gestion des candidatures ou d'un portail lié, montre des statistiques de tableau de bord de 112 102 candidatures au total, 7 917 postes vacants, 4 165 candidats employés et 107 937 candidats sur liste d'attente, cohérentes avec les nombres de lignes observés dans le panneau de base de données. Un échantillon texte brut local d'environ 25 enregistrements utilisateurs correspondant à un rôle intitulé « Student » est également examiné, chacun contenant un identifiant séquentiel, une adresse email et un hash de mot de passe au format MD5. La combinaison d'un webshell actif et complet, d'un accès administratif direct à la base de données avec des nombres de lignes par table, et d'un échantillon brut d'enregistrements utilisateurs comportant des identifiants soutient une évaluation à confiance très élevée d'une compromission réelle et profonde, dépassant une simple revendication de site web pour atteindre les systèmes de back-end traitant les candidatures du secteur de la santé, les dossiers de cliniciens et les données d'authentification de bien plus de 100 000 individus. Compte tenu de l'ampleur de l'exposition et de la sensibilité des données de cliniciens, RH et d'authentification au sein du secteur de la santé rwandais, l'impact potentiel inclut un risque important de credential stuffing et de prise de contrôle de comptes, du phishing ciblé contre des candidats et agents du secteur de la santé, et une compromission plus large des processus de gestion des effectifs de santé. Aucune adresse email, hash de mot de passe, enregistrement individuel de candidature ni autre donnée personnelle n'est reproduit à partir du matériel examiné.

## Avril 2025

### 04 Avril 2025
#### 🇸🇳 Sénégal - Forces Armées Sénégalaises (armee.sn)
- **Type d'incident:** Vente d’accès
- **Acteur / Groupe :** oblivion666
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
- **Description victime:** Holding d'investissement privé égyptien axé sur le transport maritime et la logistique. 27,75 Go de données exfiltrées.

### 07 Avril 2025
#### 🇿🇦 Afrique du Sud - Cell C
- **Groupe ransomware:** ransomhouse
- **Secteur:** Technologies (Télécommunications)
- **Site web:** cellc.co.za
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d’impact:** Level 4
- **Description victime:** Opérateur de télécommunications sud-africain, l'un des principaux fournisseurs de services mobiles dans le pays.
- **Analyse:** AFRINTEL a examiné 20 captures de la publication de RansomHouse. Elles couvrent des données Cell C relatives aux clients et employés, des passeports, des appels, des SMS, l'activité vocale internationale, des contrats, des franchises, des accords de confidentialité, des documents internes et un résumé des revenus. Cette diversité est cohérente avec une exposition importante de données télécoms. Les impacts potentiels comprennent l'atteinte à la vie privée des abonnés, le phishing et la fraude, le ciblage des employés, l'exposition des métadonnées d'appels et de messages, l'espionnage commercial et la reconnaissance opérationnelle. Les captures ne confirment pas le vecteur d'accès initial, l'exhaustivité du jeu de données, le nombre d'abonnés touchés ni l'impact opérationnel. AFRINTEL ne reproduit aucune donnée personnelle, aucun détail de passeport, numéro de téléphone, contrat ni lien de téléchargement.

### 08 Avril 2025
#### 🇪🇬 Égypte - International Busines Service
- **Groupe ransomware:** crypto24
- **Secteur:** Services aux entreprises / Externalisation (BPO)
- **Site web:** ibsns.com
- **Statut:** Claim - Unverified
- **Description victime:** International Business Service (IBS) est l'un des plus grands prestataires de services d'externalisation en Égypte. L'entreprise est spécialisée dans la gestion des ressources humaines, le recrutement de masse, l'externalisation de la paie et les services de maintenance/logistique pour les grandes entreprises et multinationales opérant en Égypte.

### 08 Avril 2025
#### 🇲🇦 Maroc - CNSS (Caisse Nationale de Sécurité Sociale)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Jabaroot DZ
- **Secteur:** Administrations publiques (Sécurité sociale)
- **Site web:** www.cnss.ma
- **Statut:** Claim - Data Sample Published
- **Description victime:** Caisse nationale de sécurité sociale du Maroc.
- **Analyse:** AFRINTEL a examiné deux exports structurés volumineux correspondant aux bases de données centrales de la CNSS, datés du même jour que la revendication. Le premier, une table employeurs/affiliés, contient environ 1 094 000 enregistrements avec des champs incluant le nom de l'entreprise, le numéro d'affiliation, les dates d'affiliation, le type d'employeur, la modalité de télépaiement, l'agence et la direction régionale, ainsi que le prénom, le nom, le numéro de carte d'identité nationale (CIN), l'adresse email et le numéro de téléphone de l'administrateur, plus des coordonnées bancaires (identifiant de compte, code banque) liées à l'employeur. Le second, une table des assurés, contient environ 1 996 000 enregistrements avec des champs incluant prénom, nom, numéro de CIN, numéro de passeport, numéro de carte de séjour, un numéro d'immatriculation interne, la date de création, le canal de la demande et le nom de l'employeur affilié. L'ampleur et la structure de ces deux tables sont cohérentes avec un extrait quasi complet et authentique des registres nationaux employeurs et assurés de la CNSS. La combinaison de numéros de CIN, de coordonnées et d'affiliations employeurs pour près de deux millions d'individus et plus d'un million d'employeurs représente une exposition à très fort impact, créant un risque substantiel de fraude à l'identité, de campagnes d'ingénierie sociale et de phishing ciblé à l'échelle nationale. AFRINTEL ne reproduit aucun nom, numéro de CIN, coordonnée ni référence bancaire issus de l'échantillon examiné.

### 08 Avril 2025
#### 🇲🇦 Maroc - Ministère de l'Industrie et du Commerce (miepeec.gov.ma)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Jabaroot DZ
- **Secteur:** Gouvernement / Économie et Industrie.
- **Site web:** miepeec.gov.ma
- **Statut:** Claim - Unverified
- **Description victime:** Le MIEPEEC est l'organe gouvernemental marocain chargé de piloter la stratégie industrielle, de promouvoir l'investissement et de réguler le commerce. Il gère des plateformes critiques d'interaction entre l'État et le secteur privé.

### 08 Avril 2025
#### 🇩🇿 Algérie - CNAS (Caisse Nationale des Assurances Sociales des Travailleurs Salariés)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Phantom Atlas
- **Secteur:** Gouvernement / Sécurité sociale
- **Site web:** [cnas.dz](https://www.cnas.dz)
- **Statut:** Claim - Data Sample Published
- **Description victime:** La CNAS est l'organisme public algérien gérant l'assurance maladie et les prestations sociales en nature des travailleurs salariés, au travers d'un réseau d'agences et de centres payeurs répartis sur le territoire national.
- **Analyse :** Phantom Atlas a publié le 8 avril 2025 une revendication présentée comme une réponse directe à des attaques informatiques récentes visant l'acteur, affirmant avoir mené une intrusion complète dans les bases de données de la CNAS et en avoir extrait plus de 860 200 documents. La publication ajoute des accusations générales de circuits financiers et logistiques opaques impliquant des entreprises algériennes et Dubaï, présentées comme devant être révélées dans une diffusion ultérieure ; ces accusations ne sont pas documentées dans le matériel examiné par AFRINTEL et sont rapportées ici uniquement comme éléments de discours de l'acteur, sans validation.

  AFRINTEL a examiné un échantillon local de 214 fichiers image (environ 97 Mo) associé à cette revendication. L'échantillon est homogène et correspond à des « Attestations d'ouverture des droits aux prestations en nature » délivrées par plusieurs agences CNAS (notamment Tizi Ouzou/Boghni et Alger/Belcourt), datées principalement de 2022 à 2024. Chaque document comporte l'identité complète de l'assuré (nom, prénom, date de naissance, adresse, numéro d'immatriculation à la sécurité sociale, centre d'affiliation) ainsi que celle de la personne couverte (assuré, conjoint, enfant ou ascendant), le taux de prise en charge, la date d'établissement, le nom de l'agent ayant délivré le document, un cachet et une signature.

  La cohérence du format sur l'ensemble de l'échantillon, la diversité des agences et centres payeurs représentés, ainsi que la présence de cachets et signatures plausibles, soutiennent un niveau de confiance élevé quant à l'authenticité d'un accès aux systèmes ou archives de la CNAS. Le volume observé (214 documents) reste toutefois très inférieur aux 860 200 revendiqués et ne permet pas de confirmer l'ampleur totale annoncée de la fuite. L'exposition de ces attestations pourrait faciliter l'usurpation d'identité, la fraude aux prestations sociales et le phishing ciblé contre les assurés et leurs ayants droit. AFRINTEL ne reproduit aucun nom, date de naissance, adresse, numéro d'immatriculation ni autre donnée personnelle issus des documents examinés.

### 09 Avril 2025
#### 🇩🇿 Algérie - MGPTT / Mutuelle Générale des Travailleurs de la Poste et des Télécoms
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Phantom Atlas
- **Secteur:** Social / Mutuelle de Santé.
- **Site web:** mgptt.dz
- **Statut:** Claim - Data Sample Published
- **Description victime:** La MGPTT est une institution sociale majeure en Algérie, couvrant les employés du secteur de la Poste, des Télécommunications et de l'Information. Elle gère les remboursements de soins et les aides sociales de dizaines de milliers de fonctionnaires et contractuels. La publication revendique plus de 13 Go de données internes de la MGPTT, comprenant des données personnelles ainsi que des documents et bases de données stratégiques, et mentionne également des fichiers sensibles du Ministère du Travail.
- **Analyse :** La publication de Phantom Atlas s'accompagne d'un message présentant l'opération comme une réponse directe à un piratage antérieur visant la CNSS, et adopte une tonalité hacktiviste explicitement liée au différend territorial du Sahara occidental entre le Maroc et l'Algérie ; ce cadrage politique est rapporté tel quel par AFRINTEL, sans validation ni prise de position sur les revendications territoriales ou les accusations réciproques de piratage.

  AFRINTEL a examiné un échantillon de 4 images (environ 496 Ko au total) associé à cette publication. Les images montrent des documents d'identité et de protection sociale photographiés ou scannés : des cartes d'assuré social algérien, une carte d'adhérent retraité MGPTT, une attestation d'affiliation délivrée par la CNAS, ainsi qu'un reçu de versement postal et un certificat d'hospitalisation associés à une clinique privée. Ces documents comportent des noms complets, dates de naissance, numéros d'immatriculation à la sécurité sociale, adresses et, pour certains, des photographies et des informations médicales ou financières de personnes nommément identifiées.

  Le volume observé (quatre images) est très inférieur aux 13 Go revendiqués et ne permet pas de corroborer l'ampleur annoncée de la fuite ni de confirmer qu'il s'agit d'un extrait représentatif d'un système d'information interne de la MGPTT. Une des images porte en outre le filigrane visible d'un service tiers de vente de documents en ligne, ce qui suggère que cet échantillon particulier pourrait provenir, au moins en partie, d'une source de documents déjà en circulation plutôt que d'une extraction directe des systèmes de la MGPTT. Ces éléments incitent à une évaluation prudente de la revendication : la présence de données personnelles et sociales réelles semble établie, mais l'origine exacte, l'exhaustivité et le lien direct avec une compromission des systèmes internes de la MGPTT restent incertains. AFRINTEL ne reproduit aucun nom, numéro d'immatriculation, date de naissance, adresse, photographie ni information médicale ou financière issus des images examinées.

### 09 Avril 2025
#### 🇩🇿 Algérie - Ministère du Travail
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Phantom Atlas
- **Secteur :** Gouvernement / Administration du travail
- **Site web :** Non précisé
- **Date de publication de la source :** 9 avril 2025
- **Statut :** Claim - Unverified
- **Description victime :** La publication fournie affirme que Phantom Atlas a accédé à des fichiers sensibles du Ministère algérien du Travail. Aucun échantillon spécifique au ministère n'est fourni ; cette cible est donc enregistrée séparément de la MGPTT sans confirmation indépendante de la compromission.
- **Analyse :** La revendication figure dans la même publication Phantom Atlas que celle concernant la MGPTT et peut correspondre à une même opération visant plusieurs institutions publiques algériennes. Aucun jeu de données spécifique au ministère n'a été collecté ni reproduit.

### 13 Avril 2025
#### 🇲🇷 Mauritanie - BMI / SEDAD Mobile Wallet
- **Acteur / Groupe :** Killer_Bee
- **Secteur :** Finance / Paiement mobile
- **Site web :** [bmi.mr](https://bmi.mr)
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Date de publication de la source :** 13 avril 2025
- **Dates observées dans l'échantillon :** 6 avril 2025

- **Description :**
  La publication affirme exposer une base associée à SEDAD, le service de banque digitale et de portefeuille mobile de BMI en Mauritanie. L'acteur revendique plus de 90 000 enregistrements liés à des réclamations de portefeuille et à des actions administratives.

- **Analyse :**
  L'échantillon visible est un enregistrement JSON structuré provenant d'un workflow de réclamations clients. Il contient des champs d'identité client, un numéro d'identification nationale, un numéro de téléphone, l'attribution à un utilisateur interne, des horodatages de création et de modification, un statut de traitement et un type de réclamation lié à l'activation. AFRINTEL ne reproduit aucune valeur personnelle visible dans l'échantillon. L'échantillon confirme la présence apparente de données structurées sensibles, mais le volume revendiqué, l'exhaustivité, l'origine et la compromission ne sont pas confirmés indépendamment. Le site officiel de BMI identifie SEDAD comme son service de banque digitale et de portefeuille électronique.

- **Recommandations :**
  1. Vérifier la revendication dans les journaux applicatifs, de base de données, d'API et d'administration de SEDAD, préserver les éléments de preuve et déterminer si des données d'identité et de téléphone ont été consultées.
  2. Faire pivoter les identifiants ou jetons administratifs exposés si nécessaire, examiner les actions privilégiées, imposer le MFA, surveiller les prises de contrôle de comptes et le phishing, puis notifier les utilisateurs et autorités compétentes si l'exposition est confirmée.

### 13 Avril 2025
#### 🇪🇬 Égypte - Tawasol
- **Groupe ransomware:** devman
- **Secteur:** Technologies de l'Information
- **Site web:** tawasol-it.com
- **Statut:** Claim - Unverified
- **Description victime:** C'est un intégrateur de solutions technologiques basé au Caire qui installe des systèmes de sécurité et d'infrastructure réseau pour les entreprises et les bâtiments intelligents.

### 13 Avril 2025
#### 🇲🇦 Maroc - Institut Supérieur des Métiers de l’Audiovisuel et du Cinéma (ISMAC)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** p4xar
- **Secteur :** Éducation / Enseignement supérieur / Audiovisuel et cinéma
- **Site web :** [ismac.ma](https://ismac.ma)
- **Statut :** Claim - Data Sample Published

- **Description :**
  L’Institut Supérieur des Métiers de l’Audiovisuel et du Cinéma (ISMAC) est un établissement public marocain d’enseignement supérieur basé à Rabat. Il forme des professionnels du cinéma, de l’audiovisuel, de la réalisation, de la production, de l’image et du son, sous la tutelle du ministère marocain de la Jeunesse, de la Culture et de la Communication.

- **Analyse :**
  Une publication attribuée à p4xar sur un forum présenté comme RaidForums affirme la compromission de l’application accessible à l’adresse `sul.ismac.ac.ma/app/` et la diffusion gratuite, via un canal Telegram, d’un fichier nommé `db.sql` présenté comme la base complète. L’échantillon visible est un export SQL substantiel de la table `n_etudiants`, dont la syntaxe et la structure sont compatibles avec MySQL ou MariaDB. Il contient des données personnelles d’étudiants, notamment des champs relatifs aux documents d’identité, à la naissance, aux adresses postales, aux adresses électroniques, aux numéros de téléphone, à la nationalité, au statut étudiant et aux comptes utilisateurs. Le croisement de ces données peut faciliter l’usurpation d’identité, le phishing ciblé, l’ingénierie sociale, la fraude documentaire et la récupération abusive de comptes. Certaines lignes comportent des valeurs nulles ou incomplètes et des anomalies d’encodage. L’échantillon établit la présence de données structurées sensibles, mais ne permet pas de confirmer le volume total, le nombre d’enregistrements, l’exhaustivité du fichier diffusé ni la compromission revendiquée par une source indépendante.

### 13 Avril 2025
#### 🇲🇦 Maroc - Ministère de l'Habitat et de la Politique de la Ville (mhpv.gov.ma)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** B4baYega
- **Secteur :** Gouvernement / Habitat / Politique de la ville
- **Site web :** mhpv.gov.ma
- **Statut :** Claim - Unverified
- **Description victime :** Le Ministère de l'Habitat et de la Politique de la Ville est l'administration marocaine chargée de la politique du logement et du développement urbain.
- **Analyse :** AFRINTEL a identifié une archive protégée par mot de passe dont le commentaire interne l'attribue explicitement à l'acteur B4baYega, avec un canal Telegram de contact pour d'autres bases de données « fraîches et privées ». Le contenu accessible de l'archive se limitait à une seule petite image ; AFRINTEL n'a pas pu accéder au jeu de données revendiqué ni le vérifier en raison de la protection par mot de passe, et ne peut donc confirmer ni son contenu, ni son volume, ni son authenticité. Cette entrée est consignée comme une revendication non vérifiée dans l'attente d'éléments complémentaires.

### 17 Avril 2025
#### 🇪🇬 Égypte - INI Investments
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** nightspire
- **Secteur :** Services financiers / Banque d'investissement / Conseil en financement de projets
- **Site web :** Non identifié avec certitude
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 2
- **Description victime :** INI Investments est une société égyptienne de banque d'investissement et de conseil en financement de projets, basée au Caire, intervenant dans les études de faisabilité, le montage financier et la clôture de financements pour des projets industriels et d'infrastructure.
- **Analyse :** AFRINTEL a examiné un échantillon local de documents cohérents avec la revendication du cybercriminel nightspire, incluant des modèles financiers internes de faisabilité (projections de TRI pluriannuelles allant de 39 % à 58 %, structure du capital et sources de financement) pour un projet de fabrication de tuyaux UPVC, une étude de marché concurrentielle comparant les volumes de production et parts de marché de plusieurs fabricants égyptiens d'UPVC nommés, un tableau de suivi de portefeuille de projets intitulé « Pipe line projects for Allweiler Farid Hassanein Pumps co » listant plusieurs contrats clients avec valeurs de projet en EGP, USD et EUR, statut et dates de soumission (référençant des clients et projets en Égypte, en Russie et en Arabie saoudite), une étude juridique et un procès-verbal de réunion, un rapport d'évaluation foncière pour le site du projet UPVC d'une société nommée, ainsi qu'un document référençant une extension de commande pour Hassan Allam, un grand groupe égyptien de construction et d'ingénierie. Les métadonnées des fichiers situent la preuve entre le 15 et le 17 avril 2025 ; cette date est traitée comme une date de preuve/découverte et non comme une date de publication confirmée. La cohérence interne des modèles financiers, la mention de contreparties industrielles égyptiennes réelles (Allweiler Farid Hassanein Pumps, Hassan Allam) et la cohérence entre l'étude de faisabilité, l'étude de marché et la documentation juridique soutiennent une évaluation à confiance élevée d'une compromission réelle des fichiers de projets internes d'INI Investments. Le matériel exposé consiste en des données confidentielles de transactions, de financement et de renseignement de marché plutôt qu'en des enregistrements personnels ou de consommateurs, créant un risque d'exposition de renseignement concurrentiel, de compromission de messagerie professionnelle et d'ingénierie sociale ciblée visant INI Investments ainsi que ses clients et contreparties industriels. AFRINTEL ne reproduit aucun nom de client, valeur de projet, montant financier ni référence de document issu du matériel examiné.
- **Note de double revendication :** Les fiches de mars et d’avril sont conservées séparément, car les dates et les éléments de preuve diffèrent. Elles concernent le même acteur, le même domaine et le même nom de victime, mais AFRINTEL ne peut pas déterminer avec les éléments disponibles si la publication d’avril actualise la revendication de mars ou correspond à une revendication distincte. Aucune fusion n’est effectuée dans l’attente d’une confirmation.
### 20 Avril 2025
#### 🇿🇦 Afrique du Sud - Premier Meats South Africa
- **Groupe ransomware:** devman
- **Secteur:** Agroalimentaire
- **Site web:** premiermeats.co.za
- **Statut:** Claim - Unverified
- **Description victime:** Premier Meats est une entreprise sud-africaine spécialisée dans la transformation et la distribution de viandes de qualité.

### 22 Avril 2025
#### 🇹🇳 Tunisie - Natilait
- **Groupe ransomware:** cicada3301
- **Secteur:** Agroalimentaire / Industrie Laitière
- **Site web:** natilait.com.tn
- **Statut:** Claim - Data Sample Published
- **Description victime:** Natilait est un acteur majeur du secteur agroalimentaire en Tunisie, spécialisé dans la production et la commercialisation de lait (UHT), de yaourts et de produits dérivés.
- **Analyse :** Les 12 images JPG/PNG fournies comprennent au moins un tableau interne structuré de produits et de stocks, avec des codes articles, des descriptions de produits laitiers, des quantités et des champs d'inventaire ou de stock ; les autres images semblent liées à des documents opérationnels, mais plusieurs ne sont pas suffisamment lisibles pour permettre une extraction fiable. Ces éléments sont cohérents avec un échantillon de données issu de l'environnement de fabrication ou de distribution de Natilait et pourraient faciliter la veille concurrentielle, la fraude documentaire ou le ciblage de la chaîne d'approvisionnement. Le vecteur d'intrusion, l'étendue complète du jeu de données et la production des images par cicada3301 ne sont pas établis indépendamment. Aucun enregistrement produit ni montant commercial n'est reproduit.

### 23 Avril 2025
#### 🇪🇬 Égypte - Dar Al Teb
- **Groupe ransomware:** gunra
- **Secteur:** Santé
- **Site web:** daralteb.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Description victime:** Dar Al Teb est l'un des centres médicaux les plus renommés d'Égypte, spécialisé dans la médecine de la reproduction, la fécondation in vitro (FIV) et la santé de la femme.
- **Analyse :** Le groupe ransomware gunra revendique la compromission de Dar Al Teb (daralteb.com) et affiche des échantillons de données sur sa page de fuite. Les échantillons montrent des tableaux de suivi de patients/cycles comportant nom du mari, nom de l'épouse, numéro de dossier, âge, deux numéros de téléphone, ainsi que des champs cliniques spécifiques à la fécondation in vitro (statut du sperme frais/congelé, nombre d'ovocytes/embryons attendus, andrologue référent, médecin traitant, et codes de résultat embryologique). Un jeu local plus large comprend sept classeurs mensuels (décembre 2022, puis mars à août 2023) totalisant environ 2 300 lignes de dossiers patients/cycles, ainsi que deux classeurs supplémentaires plus courts et une base de données Access (non ouverte). Le matériel technique examiné inclut un export de profil Wi-Fi contenant une clé pré-partagée en clair, des commandes réseau associées faisant référence à un partage de fichiers interne, un script PowerShell de déploiement d'une forêt Active Directory nommée « DarAlteb.local », ainsi qu'un fichier de connexion RDP préconfiguré vers un hôte interne avec redirection de presse-papiers et de lecteurs de cartes à puce activée. La combinaison d'échantillons de données cliniques nommément identifiables, d'un jeu de données patients pluriannuel et de matériel de configuration réseau et d'accès distant interne soutient une évaluation à confiance élevée d'une compromission réelle et étendue dépassant une simple revendication de site de fuite. La nature des données observées, à la fois des informations de santé reproductive nommément identifiables portant sur plusieurs milliers de patients et des éléments d'accès à l'infrastructure interne, justifie un niveau d'impact de niveau 4. AFRINTEL ne reproduit aucun nom de patient, numéro de téléphone, numéro de dossier, clé Wi-Fi, adresse IP ni autre donnée personnelle ou secret issu du matériel examiné.

## Mai 2025

### 01 Mai 2025
#### 🇿🇦 Afrique du Sud - South African IT firm - iOCO (Filiale de EOH)
- **Groupe ransomware:** devman
- **Secteur:** Technologies / Services managés (MSP) / Cloud
- **Site web:** https://www.eoh.co.za / ioco.tech
- **Statut:** Claim - Unverified
- **Description victime:** EOH est l'un des plus grands prestataires de services technologiques et de conseil en Afrique du Sud, fournissant des solutions de transformation numérique et d'infrastructure. Le groupe Devman a utilisé une description générique ("South African IT firm") sur son site de fuite, une tactique courante pour maintenir la pression pendant les phases de négociation.

### 01 Mai 2025
#### 🇿🇦 Afrique du Sud - DovesIT
- **Groupe ransomware:** devman
- **Secteur:** Technologies de l'Information (IT) / Services Managés (MSP)
- **Site web:** https://dovesit.co.za
- **Statut:** Claim - Unverified
- **Description victime:** DovesIT est un fournisseur de services informatiques (MSP) sud-africain. L'entreprise propose des solutions de sauvegarde, d'hébergement cloud, de maintenance réseau et de cybersécurité pour les petites et moyennes entreprises (PME) en Afrique du Sud.

### 01 Mai 2025
#### 🇿🇦 Afrique du Sud - South African Hr company
- **Groupe ransomware:** devman
- **Secteur:** Services aux entreprises / Ressources Humaines
- **Site web:** Non précisé
- **Statut:** Claim - Unverified
- **Description victime:** Il s'agit d'un cabinet ou d'un prestataire de services en ressources humaines basé en Afrique du Sud, gérant les données contractuelles, salariales et personnelles de nombreux employés pour le compte de tiers (externalisation RH).

### 05 Mai 2025
#### 🇪🇬 Égypte - Future Association for Microfinance
- **Groupe ransomware:** nightspire
- **Secteur:** Finance / Association
- **Site web:** https://fam-eg.org
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description victime:** ONG égyptienne, spécialisée dans l'octroi de micro-crédits aux micro-entrepreneurs et aux populations rurales.
- **Analyse :** Des éléments datés (preuves) du 6 au 7 mai 2025 comprennent des vues d'interface et des fichiers d'export structurés. Un panneau d'administration web actif, accessible uniquement en HTTP (« Not secure ») à une adresse IP, est utilisé pour gérer des factures de prêts/paiements ; sur l'une des vues, le champ « Customer Name » d'au moins une douzaine d'enregistrements de facture consécutifs a été modifié pour afficher « NightSpire », une technique de preuve d'accès démontrant un accès en écriture à l'application de production plutôt qu'une simple revendication passive. Une liste paginée de gestion de prêts (noms de clients, numéros de référence de type numéro d'identité nationale, dates, montants) s'étale sur des dizaines de pages, et une arborescence de dossiers sur un lecteur partagé interne est organisée par service (Audit, Financial, HR, IT, Legal, MIS, Operation, Risks et leurs combinaisons croisées, plus des dossiers Backup et Meeting Room), cohérente avec la structure interne d'une institution financière de taille moyenne. Les exports structurés examinés (champs incluant REFERENCE_NUMBER, DUE_AMOUNT, MIN/MAX_AMOUNT, DUE_DATE, EXPIRY_DATE, CUSTOMER_NAME, STATUS, PAID_AMOUNT, BRANCH_CODE, CLIENT_NUMBER et LOAN_NUMBER) comprennent plusieurs fichiers allant d'environ 470 à un peu plus de 2 000 lignes chacun, couvrant des données de prêts et de paiements datées d'avril 2024 et avril 2025 sur plusieurs codes d'agence, ce qui indique une extraction récurrente ou en masse plutôt qu'un échantillon limité unique. La combinaison d'un accès en écriture démontré à un panneau d'administration actif et de plusieurs exports de prêts/paiements volumineux et structurellement cohérents soutient une évaluation à confiance très élevée d'une compromission réelle et en cours du système de gestion des prêts de l'association. Compte tenu de l'ampleur des dossiers de prêts et de paiements exposés (noms de clients, identifiants nationaux, montants de prêts et données au niveau des agences) au sein d'une institution de microfinance servant des emprunteurs individuels, l'impact potentiel inclut une fraude à l'identité à grande échelle, une fraude au crédit et une ingénierie sociale ciblée contre une clientèle financièrement vulnérable. Aucun nom de client, identifiant national, montant de prêt ou de paiement, code d'agence ni numéro de référence n'est reproduit.

### 10 Mai 2025
#### 🇿🇦 Afrique du Sud - Pienaar Brothers
- **Groupe ransomware:** devman
- **Secteur:** Équipements de protection individuelle (EPI) / Industrie
- **Site web:** pienaarbrothers.co.za
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** Leader sud-africain dans la fourniture et la distribution d'équipements de protection individuelle (EPI) et de solutions de sécurité pour les secteurs minier, industriel et manufacturier.
- **Analyse:** Des éléments datés du 9 au 10 mai 2025 sont cohérents avec une intrusion active contre l'infrastructure de Pienaar Bros. Un utilitaire d'archivage côté serveur compresse une archive d'environ 2,75 Go et 3 274 fichiers de données de catalogue et de tarification (incluant des grilles tarifaires de gants EPI de marque) en vue d'un envoi vers un service de stockage cloud, aux côtés d'un envoi déjà terminé d'une archive de contrats. Des preuves en ligne de commande montrent l'utilisation d'un compte de service lié aux sauvegardes, compromis, pour parcourir un domaine Windows listant plusieurs serveurs et postes nommés, ainsi qu'un partage de sauvegarde serveur contenant un fichier de demande de rançon daté du 10 mai 2025. Un bon de livraison/feuille de route portant l'en-tête d'une entité commerciale régionale de Pienaar Bros liste des comptes clients professionnels tiers, des numéros de facture et des adresses de livraison. La combinaison d'une exfiltration en cours, de preuves de mouvement latéral sur le domaine et d'une note de rançon déployée sur l'infrastructure interne soutient une évaluation à confiance élevée d'une compromission réelle. Aucun identifiant de service compromis, ni aucun nom de client professionnel, adresse, numéro de facture ou autre enregistrement individuel n'est reproduit.


### 15 Mai 2025
#### 🇲🇷 Mauritanie - Banque Al-Wava Mauritanienne Islamique (BAMIS)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Data Sample Published
- **Description victime :** BAMIS est une banque islamique mauritanienne proposant des services bancaires de détail et aux entreprises conformes à la charia.
- **Analyse :** AFRINTEL a examiné un post DarkForums publié le 15 mai 2025 par l'acteur kill9, intitulé « Mauritanian Banks Data Leak », revendiquant une intrusion coordonnée dans les réseaux internes de six institutions financières mauritaniennes, dont BAMIS. Le post affiche des enregistrements clients non attribués (nom, solde de compte négatif en MRU, identifiant client et mot de passe partiellement masqués) qui n'ont pas pu être rattachés à une banque précise, ainsi qu'un tableau de six échantillons de cartes bancaires partiellement masqués (BIN 471360, catégorie Platinum, dates d'expiration s'échelonnant de 2025 à 2027) explicitement attribués à BAMIS. L'acteur indique que l'ensemble des données sera vendu 48 heures après la publication, avec un contact via Telegram. Le post inclut également un échantillon de carte supplémentaire attribué à un établissement distinct, Banque El Amana, qui ne fait pas partie de la liste des six cibles revendiquées par l'acteur ; AFRINTEL ne peut expliquer cette incohérence. La présence d'échantillons de cartes spécifiquement attribués justifie un niveau de confiance moyen pour BAMIS, alors que l'ampleur, le volume et l'authenticité globale de l'intrusion revendiquée restent non vérifiés. AFRINTEL ne reproduit aucun nom de client, identifiant de compte, mot de passe ni numéro de carte issu du post examiné.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - Banque Mauritanienne pour le Commerce International
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Data Sample Published
- **Description victime :** Banque Mauritanienne pour le Commerce International est une banque commerciale opérant en Mauritanie, offrant des services bancaires de détail et aux entreprises.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite Banque Mauritanienne pour le Commerce International parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Le post inclut un tableau de six échantillons de cartes bancaires partiellement masqués (BIN 488985, catégorie Platinum, dates d'expiration s'échelonnant de 2025 à 2028) explicitement attribués à cette banque, ainsi que des enregistrements clients non attribués (nom, solde négatif, identifiant client et mot de passe partiellement masqués) qui n'ont pas pu être rattachés à un établissement précis. L'ensemble des données est proposé à la vente 48 heures après la publication, via un contact Telegram. La présence d'échantillons de cartes spécifiquement attribués justifie un niveau de confiance moyen, alors que l'ampleur, le volume et l'authenticité globale de l'intrusion revendiquée restent non vérifiés. AFRINTEL ne reproduit aucun nom de client, identifiant de compte, mot de passe ni numéro de carte issu du post examiné.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - Banque pour le Commerce et l'Industrie (BCI)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Data Sample Published
- **Description victime :** BCI est une banque commerciale opérant en Mauritanie, au service d'une clientèle de particuliers et d'entreprises/industriels.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite BCI parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Le post inclut un tableau de six échantillons de cartes bancaires partiellement masqués (BIN 411697, catégorie Platinum, dates d'expiration s'échelonnant de 2025 à 2029) explicitement attribués à BCI, ainsi que des enregistrements clients non attribués (nom, solde négatif, identifiant client et mot de passe partiellement masqués) qui n'ont pas pu être rattachés à un établissement précis. L'ensemble des données est proposé à la vente 48 heures après la publication, via un contact Telegram. La présence d'échantillons de cartes spécifiquement attribués justifie un niveau de confiance moyen, alors que l'ampleur, le volume et l'authenticité globale de l'intrusion revendiquée restent non vérifiés. AFRINTEL ne reproduit aucun nom de client, identifiant de compte, mot de passe ni numéro de carte issu du post examiné.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - Orabank Mauritanie-SA
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Data Sample Published
- **Description victime :** Orabank Mauritanie-SA est la filiale mauritanienne du réseau panafricain Oragroup/Orabank, offrant des services bancaires de détail et aux entreprises.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite Orabank Mauritanie-SA parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Le post inclut un tableau de six échantillons de cartes bancaires partiellement masqués (BIN 455143, catégorie Platinum, dates d'expiration s'échelonnant de 2025 à 2028) explicitement attribués à Orabank, ainsi que des enregistrements clients non attribués (nom, solde négatif, identifiant client et mot de passe partiellement masqués) qui n'ont pas pu être rattachés à un établissement précis. L'ensemble des données est proposé à la vente 48 heures après la publication, via un contact Telegram. La présence d'échantillons de cartes spécifiquement attribués justifie un niveau de confiance moyen, alors que l'ampleur, le volume et l'authenticité globale de l'intrusion revendiquée restent non vérifiés. AFRINTEL ne reproduit aucun nom de client, identifiant de compte, mot de passe ni numéro de carte issu du post examiné.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - Banque Islamique de Mauritanie (BIM Bank)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Unverified
- **Description victime :** BIM Bank est une banque islamique mauritanienne proposant des services bancaires conformes à la charia.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite BIM Bank parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Contrairement à quatre des autres banques citées, le post ne contient aucun échantillon de carte bancaire ni aucune autre donnée spécifiquement attribuée à BIM Bank ; les enregistrements clients non attribués figurant dans le post (nom, solde négatif, identifiant client et mot de passe partiellement masqués) n'ont pas pu être rattachés à cet établissement ni à aucun autre en particulier. En l'absence de preuve spécifique à cette banque, AFRINTEL évalue cette revendication avec un niveau de confiance faible, dans l'attente d'une vérification indépendante.

### 15 Mai 2025
#### 🇲🇷 Mauritanie - General Bank of Mauritania (GBM)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** kill9
- **Secteur :** Banque / Services financiers
- **Site web :** Non précisé
- **Statut :** Claim - Unverified
- **Description victime :** General Bank of Mauritania (GBM) est une banque commerciale opérant en Mauritanie, offrant des services bancaires de détail et aux entreprises.
- **Analyse :** AFRINTEL a examiné le même post DarkForums publié le 15 mai 2025 par l'acteur kill9 (« Mauritanian Banks Data Leak »), qui cite General Bank of Mauritania parmi six institutions financières mauritaniennes dont la compromission est revendiquée. Contrairement à quatre des autres banques citées, le post ne contient aucun échantillon de carte bancaire ni aucune autre donnée spécifiquement attribuée à GBM ; les enregistrements clients non attribués figurant dans le post (nom, solde négatif, identifiant client et mot de passe partiellement masqués) n'ont pas pu être rattachés à cet établissement ni à aucun autre en particulier. En l'absence de preuve spécifique à cette banque, AFRINTEL évalue cette revendication avec un niveau de confiance faible, dans l'attente d'une vérification indépendante.

### 16 Mai 2025
#### 🇿🇦 Afrique du Sud - south african airways (SAA)
- **Groupe ransomware:** incransom
- **Secteur:** Transport aérien
- **Site web:** www.flysaa.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** South African Airways (SAA) est la compagnie aérienne nationale et la plus grande d'Afrique du Sud, assurant des vols domestiques et internationaux.
- **Analyse:** AFRINTEL a examiné un échantillon local de documents cohérents avec la revendication du cybercriminel incransom, correspondant à des dossiers internes de SAA Technical, la division de maintenance, réparation et révision (MRO) de la compagnie. Le matériel comprend des documents réglementaires EASA/SACAA Part-145 (exposé de l'organisme de maintenance, liste de capacités, liste du personnel certificateur et de soutien), un certificat d'autorité d'un mécanicien certificateur comportant un nom, une photo, un numéro d'employé et d'approbation ainsi qu'un périmètre de licence multi-pays, des devis commerciaux et des documents financiers (fiches d'autorisation de crédit, codes débiteurs, analyses de coûts, exports de réconciliation de composants référençant le système de gestion de maintenance AMOS), ainsi qu'un contrat de bail entre Dube TradePort Corporation et Air Chefs SOC Limited, une filiale de la SAA. Les documents font référence à plusieurs clients tiers du MRO, dont Comair, Air Namibia, Yemenia et l'organisme public sud-africain d'acquisition de matériel de défense Armscor. La présence de dossiers opérationnels, réglementaires et financiers cohérents entre eux, s'étalant sur plusieurs années et nommant des systèmes et filiales précis de SAA Technical, soutient une évaluation à confiance élevée d'une compromission interne réelle. L'exposition de données d'identité et de licence du personnel certificateur, associée à la documentation d'approbation réglementaire et aux dossiers commerciaux de clients tiers et liés à la défense, crée un risque de phishing ciblé, de perturbation de la supervision de la sécurité aérienne et d'impact sur la chaîne clients/fournisseurs au-delà de la SAA elle-même. AFRINTEL ne reproduit aucun nom d'employé, photo, numéro de licence ni détail financier client issu de l'échantillon examiné.


### 19 Mai 2025
#### 🇰🇪 Kenya - NSSF(National Social Security Fund) KENYA
- **Groupe ransomware:** devman
- **Secteur:** Gouvernement / Services Sociaux
- **Site web:** www.nssf.go.ke
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Description victime:** Caisse nationale de sécurité sociale du Kenya, l'organisme statutaire gérant les cotisations obligatoires de retraite et de sécurité sociale des travailleurs kényans. L'acteur exige 4,5 millions USD.
- **Analyse :** Un ensemble d'éléments daté du 15 au 18 mai 2025 est cohérent avec un accès administratif réel à l'environnement Windows interne du NSSF. Le matériel inclut un fichier texte de demande de rançon ouvert sur un bureau compromis, affirmant que le « DevMan Cybersecurity Collective » a compromis les systèmes du NSSF à 21h UTC le 17 mai 2025, chiffré les systèmes et fichiers critiques, détruit les sauvegardes cloud et réseau, et exfiltré des données sensibles incluant des dossiers personnels d'employés, des informations financières clients et des détails de pension ; la note cite la loi kényane sur la protection des données de 2019 et menace de sanctions réglementaires et de poursuites clients. Des éléments distincts montrent des sessions Server Manager Windows pour au moins deux serveurs de production joints à un domaine (un hôte de messagerie/web et un hôte de gestion documentaire à grande capacité, tous deux joints à un domaine NSSF), datées des 15 et 16 mai 2025, ainsi qu'une vue de l'explorateur de fichiers listant des disques cohérents avec une base de données Exchange et une infrastructure de virtualisation, datée du 17 mai 2025. Le matériel supplémentaire examiné consiste en des dizaines de formulaires physiques scannés de versement de prestations de retraite portant l'en-tête du Board of Trustees du NSSF, des numéros de référence membre et employeur, et des montants de paiement. La combinaison d'une note de rançon détaillée correspondant au mode opératoire habituel de l'acteur, d'éléments montrant un accès réel de niveau domaine à plusieurs systèmes de production, et de dossiers de retraite archivés scannés, soutient une évaluation à très haute confiance d'une compromission à grande échelle affectant une infrastructure nationale critique de sécurité sociale. Le volume total revendiqué de 2,5 To et la demande de rançon de 4,5 millions de dollars ne sont pas vérifiés indépendamment au-delà de ce qui est affirmé dans le matériel de l'acteur lui-même ; aucun nom d'employé ou de membre, numéro de compte ou de référence, identifiant, ni aucun autre enregistrement individuel n'est reproduit.

### 20 Mai 2025
#### 🇧🇼 Botswana - Medswana
- **Groupe ransomware:** killsec
- **Secteur:** Pharmacie / Santé
- **Site web:** medswana.co.bw
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** Medswana (Pty) Ltd est l'un des principaux distributeurs pharmaceutiques du Botswana.
- **Analyse:** Le groupe ransomware killsec revendique la compromission de Medswana (medswana.co.bw) et affiche des échantillons de données sur sa page de fuite, datés des 22 et 23 mai 2025. Les échantillons couvrent trois catégories de données distinctes. Des comptes clients/débiteurs rattachés à un réseau d'officines opérant sous l'enseigne « Pharma » (Pharma Acacia, Pharma Nord, Pharma Ouest, Pharma Sud, Pharma Afrique, Pharma Kweneng, entre autres) dans plusieurs villes du Botswana (Gaborone, Kasane, Maun, Francistown), comportant nom, adresse postale, numéros de téléphone fixe et mobile et adresse e-mail. Des fiches d'ayants droit rattachées à des régimes d'assurance maladie, comportant nom, date de naissance, sexe, numéro d'affilié, lien de parenté, coordonnées du médecin traitant et champs d'allergies. Des données de stock et de dispensation pharmaceutique (codes produits, désignations de médicaments, quantités, prix d'achat et de vente, numéros d'ordonnance), avec des horodatages couvrant plusieurs années d'activité, de 2021 à 2025. La page de fuite affiche un compte à rebours avant échéance, un prix de rançon non précisé et un compteur de divulgations à 0/1, ce qui indique qu'aucune publication complète n'est encore intervenue à ce stade. La cohérence entre les enseignes commerciales visibles dans les échantillons et le profil de distributeur pharmaceutique attribué à Medswana justifie un niveau de confiance moyen. La nature des données observées, à la fois des informations de santé de patients et des coordonnées clients, justifie un niveau d'impact de niveau 3. Aucun nom de patient, de client ni aucune donnée personnelle brute n'est reproduit dans cette fiche.

### 20 Mai 2025
#### 🇩🇿 Algérie - Université Sétif 1 - Ferhat Abbas (univ-setif.dz)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Phantom Atlas
- **Secteur:** Éducation / Enseignement supérieur
- **Site web:** [univ-setif.dz](https://www.univ-setif.dz)
- **Statut:** Claim - Unverified
- **Description victime:** L'Université Sétif 1 - Ferhat Abbas est un établissement public algérien d'enseignement supérieur.
- **Analyse :** L'acteur Phantom Atlas revendique une intrusion sur le site de l'université et annonce la publication prochaine de fichiers qualifiés d'importants, pour un volume revendiqué de 3,5 Go. Aucun échantillon ni preuve technique n'accompagne cette publication ; AFRINTEL n'a pas collecté ni analysé de données sous-jacentes et ne peut donc pas confirmer la compromission.

### 21 Mai 2025
#### 🇿🇦 Afrique du Sud - Anglo American plc
- **Groupe ransomware:** arkana
- **Secteur:** Mines
- **Statut:** Claim - Unverified
- **Site web:** angloamerican.com
- **Description victime:** Anglo American plc est une multinationale minière basée à Johannesburg et Londres. C'est le plus grand producteur mondial de platine et de diamants, avec des opérations dans plus de 40 pays. Elle exploite également du cuivre, du nickel, du minerai de fer et du charbon.

### 23 Mai 2025
#### 🇿🇦 Afrique du Sud - netstar
- **Groupe ransomware:** devman
- **Secteur:** Technologie / Télématique / Sécurité IoT
- **Site web:** netstar.co.za
- **Statut:** Claim - Unverified
- **Description victime:** Netstar, une filiale du groupe Altron, est le pionnier de l'industrie du suivi et de la récupération de véhicules volés (SVR) en Afrique du Sud.

### 26 Mai 2025
#### 🇿🇦 Afrique du Sud - Mediclinic Group
- **Groupe ransomware:** everest
- **Secteur:** Santé
- **Site web:** https://www.mediclinic.co.za / www.mediclinic.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Description victime:** Mediclinic International (Groupe Mediclinic) est l'un des trois plus grands opérateurs hospitaliers privés en Afrique du Sud. Le groupe gère des dizaines d'hôpitaux multidisciplinaires et de centres de soins de jour à travers le pays (et à l'international, notamment aux Émirats Arabes Unis et en Suisse via Hirslanden).
- **Analyse :** Un ensemble local d'éléments est associé à cette revendication. Le matériel comprend deux vues d'une interface libre-service RH SAP SuccessFactors « People Profile » pour un profil nommé Gregory van Wyk, affiché avec le titre Chief Executive Officer, Office of the CEO, Mediclinic Southern Africa Corporate Office (Johannesburg) ; l'adresse email associée suit un schéma « sftest@mediclinic.com », cohérent avec un compte de test/bac à sable plutôt qu'une donnée de production confirmée, sans exclure qu'il s'agisse d'un enregistrement utilisateur réel. Les modules visibles incluent les informations de paie (accès libre-service au bulletin de salaire et liens Admin Services vers Social Insurance, External Transfers, Loans, Taxes, Employee Remuneration Info, Cost Distribution et Company Car), les informations de rémunération (un montant de salaire de base mensuel sous le groupe de paie « MEDICLINIC Salaries - Management (M1) »), ainsi que des métadonnées d'emploi et d'organisation référençant les entités juridiques Mediclinic (Pty) Ltd et Mediclinic Southern Africa (Pty) Ltd, des codes de compte général (GL) et des champs de classification de poste. Une arborescence de dossiers projet distincte (Requirements, Change Request, LMS Handover, Meetings & Trackers, Configuration, Integrations, Documentation, Migration, ainsi qu'un fichier vidéo « Mediclinic JAM Walkthrough ») présente des tailles de dossiers allant de moins d'1 Mo à environ 1,6 Go pour le dossier Migration, ce qui est cohérent avec un espace de travail de projet ou d'implémentation SuccessFactors plutôt qu'une simple fuite de documents. La cohérence de l'image de marque Mediclinic, des noms d'entités juridiques et de la structure des modules SuccessFactors entre les éléments examinés soutient une évaluation à confiance élevée d'un accès réel à l'environnement du système d'information RH de Mediclinic, bien que la portée, le caractère production ou non, et le volume total de la compromission sous-jacente ne soient pas établis à partir de cet échantillon limité. Aucun montant de salaire, numéro de téléphone, identifiant employé ni autre donnée personnelle n'est reproduit.

### 26 Mai 2025
#### 🇿🇦 Afrique du Sud - FrontierCo
- **Groupe ransomware:** Datacarry
- **Secteur:** Retail / Distribution (Vêtements et chaussures).
- **Site web:** http://frontierco.co.za/
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description victime:** FrontierCo est un acteur majeur de la distribution en Afrique du Sud. La société détient les licences de distribution exclusive et les droits de vente pour plusieurs marques internationales de renom (vêtements, chaussures et accessoires) à travers un large réseau de boutiques physiques et de plateformes d'e-commerce.
- **Analyse :** AFRINTEL a examiné des exports structurés de données clients ainsi que des éléments de reconnaissance réseau associés à cette revendication. Six fichiers CSV, correspondant au schéma de la table « Customer » de Microsoft Dynamics 365 Business Central (champs incluant nom de l'entreprise/du contact, adresse, ville, téléphone, mobile, email, numéro de TVA, limite de crédit, conditions de paiement et autres métadonnées commerciales), totalisent ensemble environ 120 000 fiches clients. Un fichier distinct cohérent avec un export de base de données supplémentaire (environ 99 Mo non compressé) était également présent mais n'a pas été ouvert par AFRINTEL. Un journal de reconnaissance réseau montre un balayage d'énumération SMB contre 256 cibles internes sur une plage /24 interne, dans lequel un identifiant Windows « Administrator » (non reproduit) apparaît authentifié avec succès sur plus d'une douzaine de serveurs, incluant des hôtes nommés de façon cohérente avec un serveur de base de données SQL, deux serveurs de sauvegarde/Veeam, un serveur lié aux RH, un serveur UAT et plusieurs hôtes Hyper-V, aux côtés de tentatives échouées contre d'autres hôtes. Cela indique un accès administratif à l'échelle du domaine obtenu par réutilisation d'identifiants, et non une compromission limitée à un seul système. La combinaison d'un export volumineux et structurellement cohérent de la base clients et d'un mouvement latéral démontré à l'échelle du domaine avec un identifiant administrateur fonctionnel soutient une évaluation à confiance très élevée d'une compromission réelle et étendue de l'environnement informatique de FrontierCo. Compte tenu de l'ampleur des fiches clients exposées (coordonnées, numéros de TVA, conditions commerciales) combinée à un accès de niveau administrateur de domaine confirmé s'étendant à l'infrastructure de base de données, de sauvegarde et RH, l'impact potentiel inclut une fraude à grande échelle visant les clients professionnels, du phishing ciblé et une compromission supplémentaire des systèmes de sauvegarde et financiers. AFRINTEL ne reproduit aucun nom de client, coordonnée, numéro de TVA, hash d'identifiant ni correspondance IP/nom d'hôte issus du matériel examiné.

### 31 Mai 2025
#### 🇨🇲 Cameroun - ASCOMA Cameroon
- **Groupe ransomware:** worldleaks
- **Secteur:** Assurance
- **Site web:** ascoma.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Description victime:** ASCOMA Cameroun est la branche camerounaise du groupe Ascoma, premier réseau indépendant de courtage d'assurances en Afrique subsaharienne.
- **Analyse :** AFRINTEL a examiné un échantillon local de fichiers cohérents avec la revendication du cybercriminel worldleaks, récupérés depuis un partage de fichiers interne (hôte 192.168.1.20) comprenant des dossiers nommés « Automobile_Transport » et « Sinistre_Sante ». L'échantillon inclut une page de configuration réseau d'une imprimante HP OfficeJet Pro interne, confirmant le domaine interne « ascoma.local », un plan d'adressage IP interne (192.168.1.0/24) ainsi qu'un mot de passe Wi-Fi Direct faible et non modifié, ainsi que des journaux internes de routage scanner/fax listant des destinations de documents rattachées aux services sinistres et médical de l'entreprise (« Sinistre IARD », « Sinistre Santé », « Indemnisation IARDT », « Medical », « Production Santé »). La cohérence entre le nom de domaine interne, la configuration réseau et les noms de dossiers de partage examinés soutient une évaluation à confiance élevée d'un accès réel au réseau interne. Compte tenu du rôle d'ASCOMA en tant que courtier d'assurance traitant des sinistres santé et IARD, et de la présence confirmée d'un partage dédié aux sinistres santé, cet incident présente un risque d'exposition de données de santé et de données personnelles d'assurés, en plus d'une valeur de reconnaissance réseau interne pour une compromission ultérieure. AFRINTEL ne reproduit aucune correspondance IP/nom d'hôte interne, identifiant réseau ni contenu de document du service sinistres issu du matériel examiné.

### 31 Mai 2025
#### 🇹🇬 Togo - Netmaster (netmaster.tg)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** cache
- **Secteur:** Technologie / Services Numériques (Hébergement & Domaines).
- **Site web:** netmaster.tg
- **Statut:** Data Fully Published
- **Description victime:** Netmaster est un prestataire de services numériques de premier plan au Togo. Il agit en tant que registrar (bureau d'enregistrement) pour le domaine national .tg et fournit des solutions d'hébergement web, d'e-mails professionnels et de certificats SSL à de nombreuses entreprises et institutions togolaises.
- **Analyse:** AFRINTEL a examiné le post DarkForums ainsi que l'export de base de données référencé, qui correspond à une base WHMCS complète de facturation et de gestion d'hébergement, incluant des tables clients, facturation, hébergement, domaines, tickets de support, administrateurs et passerelles de paiement. Aux côtés de cette base, un fichier annexe liste les codes de transfert EPP de plusieurs centaines de domaines `.tg`, ce qui est cohérent avec le rôle de Netmaster en tant que registrar du domaine national togolais ; l'exposition de ces codes crée un risque de transfert non autorisé de domaines pour les entreprises et institutions togolaises dépendant de Netmaster, en plus des données de facturation et de support propres à la clientèle de Netmaster. La structure et l'ampleur de l'export examiné sont cohérentes avec la revendication du cybercriminel cache concernant une fuite complète de la base de données. AFRINTEL ne reproduit aucun enregistrement client, facture, identifiant ni code EPP issu des éléments examinés.

## Juin 2025

### 02 Juin 2025
#### 🇲🇦 Maroc - ANCFCC (Agence Nationale de la Conservation Foncière)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** nightspire
- **Secteur:** Gouvernement / Immobilier et Foncier.
- **Site web:** https://www.ancfcc.gov.ma/
- **Statut:** Claim - Data Sample Published
- **Description victime:** L'ANCFCC est l'organisme vital chargé de l'immatriculation foncière, du cadastre et de la cartographie au Maroc. La revendication initiale de NightSpire évoquait une fuite de 3,1 Go comprenant plus de 10 080 certificats de propriété.
  Une publication attribuée à vyngrich sur un forum cybercriminel annonce plusieurs collections présentées comme provenant de l’ANCFCC : plus de 10 000 certificats de propriété en échantillon, un ensemble sous-jacent revendiqué à plus de 10 millions de certificats, ainsi que 20 000 documents en échantillon issus d’une collection annoncée à plus de 4 millions de documents et 4 To. Les catégories revendiquées comprennent notamment des actes fonciers, des documents d’état civil, des pièces d’identité, des passeports et des documents bancaires, ainsi qu’un dossier qui concernerait de hauts responsables et des personnalités publiques. AFRINTEL ne reproduit aucune identité. AFRINTEL a par la suite obtenu et examiné des copies d'archives locales de la publication revendiquée, confirmant la présence de plusieurs milliers de fichiers PDF individuels de certificats de propriété, nommés séquentiellement (par exemple CERTIFICAT_1.pdf jusqu'à des numéros de l'ordre du millier), cohérente avec la taille de l'échantillon revendiqué, ainsi qu'un dossier distinctement nommé faisant référence à de hauts responsables et personnalités publiques ; AFRINTEL n'a ni ouvert ni analysé le contenu de ce dossier et n'en reproduit aucune identité. La proximité entre l’échantillon de plus de 10 000 certificats et les 10 080 certificats publiés par NightSpire suggère un chevauchement, une republication, une revente ou une amplification possible. La publication de juillet est conservée comme information complémentaire et n’est pas comptabilisée comme un incident distinct. L’authenticité, l’ancienneté, l’exhaustivité et l’origine technique des collections supplémentaires revendiquées restent inconnues.

### 02 Juin 2025
#### 🇲🇦 Maroc - Portail de l'Ordre des Avocats (avocatsmaroc.com / mossaada.ma)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** B4baYega
- **Secteur :** Services juridiques / Association professionnelle
- **Site web :** avocatsmaroc.com / mossaada.ma
- **Statut :** Claim - Data Sample Published
- **Description victime :** avocatsmaroc.com est un portail marocain de la profession juridique appuyant les avocats dans la gestion de leurs dossiers et procédures d'exécution ; mossaada.ma est une plateforme d'aide juridictionnelle associée.
- **Analyse :** AFRINTEL a examiné du code source applicatif et des sauvegardes de base de données SQL référençant les domaines bureau.avocatsmaroc.com et app2.mossaada.ma, diffusés par l'acteur B4baYega aux côtés d'une archive protégée par mot de passe. Les fichiers source PHP de l'application utilisent des noms de fonctions et de champs translittérés de l'arabe correspondant à une terminologie de gestion de dossiers judiciaires et de procédures d'exécution (par ex. « Tanfid »/exécution, « Khazina »/trésorerie ou caisse, « Tabligh »/notification, « Diligence », « Tribunal »), ainsi que des fonctions de recherche de clients, de modification de dossiers clients et de suivi de diligences, et plusieurs fichiers de sauvegarde SQL datés. Cela indique la compromission d'une application de gestion de dossiers juridiques utilisée par ou pour des avocats marocains, plutôt qu'un simple site vitrine. AFRINTEL n'a pas extrait ni examiné le contenu ligne par ligne des sauvegardes SQL et ne reproduit aucun nom de client, référence de dossier ni autre donnée personnelle issus de l'échantillon examiné. L'ampleur et le volume réels des enregistrements contenus dans les sauvegardes n'ont pas pu être confirmés de manière indépendante.

### 06 Juin 2025
#### 🇲🇦 Maroc - MTT EXPERTISES
- **Groupe ransomware:** incransom
- **Secteur:** Services aux entreprises
- **Site web:** https://mttexpertises.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** MTT Expertises est un cabinet d'ingénierie et d'expertise multidisciplinaire basé à Casablanca (avec des bureaux à Agadir et Tanger).
- **Analyse:** AFRINTEL a examiné un petit échantillon local de documents cohérents avec la revendication du cybercriminel incransom, incluant un chèque client non caviardé émis par une société basée à Casablanca et payable via le Crédit du Maroc, affichant un numéro de compte bancaire complet, une attestation bancaire du Crédit du Maroc confirmant un compte détenu par MTT Expertise, une facture client référençant une société agroalimentaire (Quality Tomatos Morocco) avec ses coordonnées bancaires, ainsi qu'un plan de masse de site industriel portant le logo MTT Expertises, cohérent avec une mission d'expertise d'assurance et d'évaluation d'actifs. La présence d'instruments bancaires authentiques et de documents d'expertise de site rattachés à des clients tiers distincts, ainsi que l'attestation bancaire propre à MTT Expertises, soutient une évaluation à confiance moyenne d'une compromission réelle des fichiers internes du cabinet. L'exposition de coordonnées bancaires de clients et du cabinet crée un risque de fraude au paiement et de compromission de messagerie professionnelle visant MTT Expertises et ses clients. AFRINTEL ne reproduit aucun numéro de compte bancaire, numéro de chèque ni nom de client issu de l'échantillon examiné.

### 06 Juin 2025
#### 🇿🇦 Afrique du Sud - Ingonyama Trust Board
- **Groupe ransomware:** nightspire
- **Secteur:** Administration Foncière / Secteur Public.
- **Site web:** ingonyamatrust.org.za
- **Statut:** Claim - Unverified
- **Description victime:** L'Ingonyama Trust Board (ITB) est une autorité administrative sud-africaine chargée de gérer environ 2,8 millions d'hectares de terres communales dans la province du KwaZulu-Natal.

### 06 Juin 2025
#### 🇲🇦 Maroc - Best Profil (bestprofil.ma)
- **Groupe ransomware:** lynx
- **Secteur:** Ressources Humaines / Recrutement / Intérim.
- **Site web:** https://bestprofil.ma
- **Statut:** Data Fully Published
- **Description victime:** Best Profil est l'un des leaders du recrutement et de l'intérim au Maroc. Le groupe Lynx décrit cet incident comme une exfiltration totale de 26 Go, désormais en libre accès sur son site de fuite après l'échec, selon ses affirmations, des négociations de rançon.
- **Analyse:** AFRINTEL a examiné un échantillon local des données divulguées, composé de documents administratifs et opérationnels internes référençant « PEGASE » (un système/outil interne), de tableurs de suivi de présence et de paie du personnel, de fichiers de vérification de factures et de détail de facturation, ainsi que d'un dossier de réclamation client pour un site industriel. La présence de manuels de systèmes internes, de données de paie et de pointage, ainsi que de correspondance administrative au niveau des sites, est cohérente avec une compromission réelle des systèmes internes plutôt qu'une simple revendication superficielle. L'exposition des données de présence, de paie et de facturation du personnel crée un risque de fraude à la paie, de compromission de messagerie professionnelle (BEC) et d'ingénierie sociale contre le personnel et les clients corporate de Best Profil. AFRINTEL ne reproduit aucun nom d'employé, nom de client ni montant financier issus de l'échantillon examiné.

### 08 Juin 2025
#### 🇩🇿 Algérie - Crédit Populaire d’Algérie (cpa-bank.dz)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** TajineSec / Tajinesec_MA (revendication publiée)
- **Secteur:** Banque / Services Financiers.
- **Site web:** https://cpa-bank.dz
- **Statut:** Claim - Unverified
- **Description victime :** Crédit Populaire d'Algérie (CPA) est l'une des principales banques publiques du pays. TajineSec affirme avoir exfiltré plus de 30 Go, comprenant des documents d'identité, des informations sur les employés et les clients, des données de comptes bancaires et de transferts d'argent, ainsi que des documents administratifs internes. Un échantillon de 500 Mo est annoncé, mais il n'est pas visible dans la preuve fournie.
- **Analyse :** La publication documente une revendication publique attribuée à TajineSec / Tajinesec_MA et décrit des données bancaires et d'identité potentiellement très sensibles. La compromission, le volume annoncé, l'attribution marocaine alléguée et la publication de l'échantillon annoncé ne sont pas vérifiés indépendamment. Le statut reste donc **Claim - Unverified**.

### 09 Juin 2025
#### 🇩🇿 Algérie - Algérie Télécom (algerietelecom.dz)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Phantom Atlas
- **Secteur:** Télécommunications / Infrastructure Internet nationale
- **Site web:** [algerietelecom.dz](https://www.algerietelecom.dz)
- **Statut:** Claim - Data Sample Published
- **Description victime:** Algérie Télécom est l'opérateur historique et principal fournisseur d'accès Internet fixe et de téléphonie fixe en Algérie, exploitant l'infrastructure réseau nationale reliant les points d'accès régionaux aux serveurs de contenu internationaux.
- **Analyse :** Phantom Atlas revendique un accès complet à la cartographie interne du réseau internet d'Algérie Télécom pour les wilayas de Tizi Ouzou, Boumerdes et Bouira, affirmant détenir des informations détaillées sur l'infrastructure critique reliant les points d'accès (BNG) aux serveurs de contenu mondiaux (FNA, GGC), ainsi que les routeurs cœur de réseau, les anneaux de distribution de contenu et la consommation de données par commune.

  Les éléments examinés montrent des interfaces d'un outil de supervision réseau de type « Network Weathermap », affichant plusieurs cartes topologiques distinctes : un schéma du projet BNG Tizi-Ouzou avec des routeurs identifiés (PE-01, PE-02, ASBR-01, ASBR-02) et des liens de peering vers Google (GGC) et Facebook (FNA) avec charges de trafic en Gbit/s ; un schéma de la boucle métropolitaine régionale nommant des dizaines de sites et communes des wilayas concernées ; et un tableau de consommation de bande passante détaillé par commune pour Tizi Ouzou, Boumerdes et Bouira. Un second message précise que l'accès a été maintenu depuis au moins le 28 mai 2025 (mention d'une coupure de connexion lors d'un test à cette date) et affirme détenir des données allant au-delà de simples cartes.

  La cohérence technique des interfaces observées (outil de supervision réseau réel, désignations d'équipements et de sites plausibles, chiffres de trafic cohérents entre les différentes vues) soutient un niveau de confiance élevé quant à l'authenticité d'un accès à un système de supervision interne d'Algérie Télécom, au moins pour les wilayas mentionnées. La divulgation de cartes réseau détaillées d'un opérateur télécom national constitue une exposition critique pouvant faciliter la cartographie ciblée de l'infrastructure en vue d'intrusions ultérieures, des attaques par déni de service ciblées sur des liens identifiés, ou une perturbation du service dans les zones concernées. AFRINTEL ne reproduit aucun détail topologique, identifiant d'équipement ni chiffre de trafic supplémentaire au-delà de ce qui est nécessaire pour qualifier la nature de l'exposition.

### 09 Juin 2025
#### 🇬🇭 Ghana - Priority Insurance Company Limited
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** 0x0day, publication postée sur le forum cybercriminel DarkForums
- **Secteur :** Assurance / Services financiers
- **Site web :** priorityinsuranceghana.net
- **Statut :** Claim - Data Sample Published
- **Description victime :** Priority Insurance Company Limited est une compagnie d'assurance non-vie ghanéenne basée à Accra, agréée par la National Insurance Commission (NIC), qui exploite un réseau de plus de 30 agences à travers le pays, notamment à Accra, Kumasi, Tema, Cape Coast et Ho.
- **Analyse :** AFRINTEL a identifié la publication d'origine, intitulée « GHANA Inusrance database », publiée sur le forum cybercriminel DarkForums par le compte 0x0day le 9 juin 2025, ce qui remplace un enregistrement précédent en cours d'investigation, provisoirement placé en février 2025 sur la seule base d'une date de modification de fichier, sans publication source retrouvée. La publication affiche un échantillon JSON cohérent avec un export interne de gestion de polices d'assurance, avec des champs incluant un identifiant client, un numéro de police, un identifiant et un nom d'agence (Tema), un type de client, un nom complet, une adresse email, un numéro de téléphone, des adresses numérique/postale/de résidence, un numéro d'identification fiscale, un identifiant et un nom d'entreprise (explicitement « Priority Insurance Company Limited »), ainsi qu'un champ d'identification nationale. Cela correspond à la structure et au réseau d'agences (Accra, Kumasi, Tema, Cape Coast, Ho, Bolga) du fichier de base de données clients précédemment examiné par AFRINTEL, qui contenait 349 288 enregistrements dont environ 159 000 avec une adresse email et environ 159 000 avec un numéro d'identification nationale. La combinaison d'un compte source confirmé, d'une date de publication explicite et d'un échantillon correspondant au jeu de données précédemment examiné permet de faire passer le niveau de confiance d'en cours d'investigation à une revendication datée et attribuée. Compte tenu du volume d'enregistrements et de la combinaison de numéros d'identification nationale, de dates de naissance, de professions, de coordonnées et d'association à des polices d'assurance, l'exposition de ce jeu de données créerait un risque significatif d'usurpation d'identité, de fraude à l'assurance et de phishing ciblé visant les assurés. AFRINTEL ne reproduit aucun nom de client, numéro de téléphone, adresse, numéro d'identification nationale ni date de naissance issu des éléments examinés.

### 11 Juin 2025
#### 🇲🇺 Maurice - Currimjee Jeewanjee & Co
- **Groupe ransomware:** warlock
- **Secteur:** Conglomérat / multi-sectoriel
- **Site web:** https://www.currimjee.com
- **Statut:** Claim - Unverified
- **Description victime:** L'un des plus anciens et importants conglomérats de l'île Maurice, opérant dans les télécoms (Emtel), l'énergie, l'immobilier, le tourisme et les services financiers.

### 11 Juin 2025
#### 🇩🇿 Algérie - Banque Nationale d’Algérie (bna.dz)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Phantom Atlas
- **Secteur:** Banque / Services Financiers.
- **Site web:** https://bna.dz / https://ebanking.bna.dz
- **Statut:** Claim - Unverified
- **Description victime:** La Banque Nationale d'Algérie (BNA) est la première banque commerciale de l'État algérien. L'acteur revendique une exfiltration massive de 90 Go avec une publication partielle de 7 Go ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.
- **Analyse :** Un message Phantom Atlas antérieur, publié le 10 juin 2025 sur la chaîne Telegram de l'acteur, précise cette revendication : le groupe affirme détenir plus de 90 Go de documents couvrant la période 2016-2025, avec une diffusion annoncée en plusieurs temps (« nous commencerons par ceux de 2016 »), l'archive étant protégée par le mot de passe `phantomatlas`. Le lien de téléchargement mentionné sur DarkForums n'est plus accessible au moment de la rédaction de cette fiche ; AFRINTEL n'a donc pas pu collecter ni examiner l'archive revendiquée, et ne peut confirmer ni l'exhaustivité ni l'authenticité du contenu annoncé.

### 11 Juin 2025
#### 🇿🇦 Afrique du Sud - carducci
- **Groupe ransomware:** warlock
- **Secteur:** Commerce de détail (Mode)
- **Site web:** http://carducci.co.za/
- **Statut:** Claim - Unverified
- **Description victime:** Carducci est une marque de mode sud-africaine basée au Cap, fondée en 1978. Elle est spécialisée dans les vêtements pour hommes élégants, notamment les costumes, les tenues décontractées et les accessoires. La marque est réputée pour son savoir-faire et ses tissus raffinés. Carducci fait partie du groupe Seardel

### 14 Juin 2025
#### 🇪🇬 Égypte - Ministère de la Solidarité sociale
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Keymous
- **Secteur:** Gouvernement / Administration publique / Affaires sociales
- **Site web:** [moss.gov.eg](https://www.moss.gov.eg)
- **Statut:** Claim - Data Sample Published
- **Description victime:** Le Ministère de la Solidarité sociale est une administration gouvernementale égyptienne chargée notamment de politiques et services liés à la protection et à l'action sociales.
- **Analyse:** Une publication attribuée à l'acteur Keymous présente des données supposément obtenues auprès du ministère et concernant également des responsables et représentants institutionnels de plusieurs pays. La publication annonce des documents confidentiels et des informations personnelles concernant des ministres, responsables gouvernementaux et représentants institutionnels de plusieurs pays africains, arabes et asiatiques, mentionnant notamment des passeports ou pièces d'identité, noms, numéros de téléphone et adresses électroniques ; l'acteur revendique un total de 237 éléments, décrit dans la publication comme « Line and file ».

  L'échantillon CSV analysé par AFRINTEL contient 26 enregistrements répartis sur 8 colonnes : `Name`, `Phone`, `Email`, `Title / Position`, `Country`, `City`, `Passport / ID` et `Photos`. Les données couvrent notamment l'Égypte, Djibouti, le Bénin, le Burkina Faso, le Sénégal, le Maroc, le Soudan, la Turquie, les Émirats arabes unis, la Malaisie, l'Indonésie et le Koweït, ainsi que des organisations affiliées à l'OCI. Les 26 enregistrements contiennent des noms, numéros de téléphone, adresses électroniques, fonctions professionnelles et références de passeport ou de pièce d'identité, et certaines fonctions correspondent à des responsables gouvernementaux, diplomatiques ou institutionnels. La colonne `Photos` contient également la mention `Back` pour 5 enregistrements, sans image directement intégrée au fichier CSV fourni ; plusieurs valeurs de localisation sont absentes ou remplacées par un marqueur, et au moins une adresse électronique apparaît partiellement masquée.

  La combinaison d'informations d'identité, de coordonnées directes et de fonctions institutionnelles présente un risque élevé de spear phishing, usurpation d'identité, fraude documentaire et ingénierie sociale ciblée, et les fonctions professionnelles exposées pourraient permettre à un acteur de sélectionner des profils à forte valeur et de contextualiser des campagnes visant des administrations ou organisations partenaires. La publication affiche un lien de téléchargement présenté comme « Full file », mais le fichier CSV transmis à AFRINTEL ne contient que 26 enregistrements face aux 237 éléments revendiqués ; le matériel examiné doit donc être considéré comme un échantillon observé et ne permet pas de confirmer que l'intégralité du jeu de données revendiqué a été obtenue. Aucun prix n'est indiqué et les données ne sont pas présentées comme étant proposées à la vente. AFRINTEL ne reproduit aucun nom, numéro de téléphone, adresse électronique, référence de passeport/pièce d'identité ni autre donnée personnelle issus de l'échantillon examiné.

### 14 Juin 2025
#### 🇩🇿 Algérie - Ministère de la Jeunesse et des Sports (MJS) / Directions de la Jeunesse et des Sports (DJS)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** mrdump, publication sur un forum cybercriminel (DarkForums)
- **Secteur:** Gouvernement / Administration publique / Jeunesse et sports
- **Site web:** [mjs.gov.dz](https://www.mjs.gov.dz)
- **Statut:** Data Fully Published
- **Description victime:** Le Ministère de la Jeunesse et des Sports (MJS) est l'administration algérienne chargée des politiques publiques de jeunesse et de sport, appuyée sur un réseau de Directions de la Jeunesse et des Sports (DJS) dans chaque wilaya. Les documents examinés concernent majoritairement la direction de la wilaya de Boumerdes, ainsi que des correspondances émanant d'autres wilayas (Illizi, El Meghaier, Tlemcen, Béchar) et du ministère central.
- **Analyse:** L'acteur mrdump a publié sur un forum cybercriminel (DarkForums) une revendication de compromission de la base de données du ministère, accompagnée d'un lien vers un canal Telegram externe présenté comme la source de la publication complète. La publication affirme avoir « publié tous les fichiers sensibles et les données internes » du ministère.

  AFRINTEL a examiné directement l'ensemble des fichiers associés à cette publication, représentant environ 730 Mo répartis sur 772 fichiers (610 PDF, 109 images, 22 archives RAR non extraites, 20 classeurs Excel, ainsi que quelques documents Word, vidéos et fichiers texte). Le contenu correspond à de la correspondance administrative interne authentique : notes de suivi budgétaire et d'exécution de programmes (notes DIEEP, avant-projets de loi de règlement, besoins en crédits de paiement), inventaires d'infrastructures sportives (stades, piscines, salles omnisports), programmes de vacances et de camps de jeunesse, accords de jumelage entre wilayas, une banque d'informations recensant les établissements de jeunesse, ainsi qu'une circulaire adressée aux directeurs de la jeunesse et des sports de plusieurs wilayas. Les dates des documents s'étendent d'environ 2014 à début juin 2025, la date la plus récente précédant de quelques jours la publication du 14 juin 2025.

  Deux classeurs Excel affichent un nombre de lignes anormalement élevé (environ 1 047 700 lignes chacun) en raison d'un artefact de mise en forme lors de l'export depuis un système comptable ; seules une douzaine de lignes contiennent réellement des données dans chaque fichier, correspondant à des nomenclatures budgétaires (programme, sous-programme, action, catégorie, ordonnateur) et non à un volume massif d'enregistrements individuels.

  Un fichier texte isolé contient un extrait de dossier individuel de carrière d'un agent du ministère (nom, grade d'origine, date d'entrée en fonction), confirmant une exposition de données RH nominatives en plus de la correspondance administrative. Les 22 archives RAR jointes n'ont pas été extraites par AFRINTEL et leur contenu exact reste donc non vérifié au-delà de leurs noms de fichiers, évoquant notamment des bilans d'activité, des dossiers de financement associatif et des documents relatifs à des partenariats.

  La cohérence interne du corpus (en-têtes officiels, structure administrative algérienne conforme, chronologie plausible, mention nominative d'un agent) et son volume soutiennent un niveau de confiance élevé quant à l'authenticité d'un accès aux données internes du ministère ou d'une de ses directions déconcentrées. Cette exposition pourrait faciliter l'usurpation d'identité de fonctionnaires, le phishing ciblé contre le réseau des directions de wilaya, la reconstitution de l'organisation budgétaire interne du ministère et l'exploitation de données de carrière RH. AFRINTEL ne reproduit aucun nom, donnée RH, coordonnée personnelle ni document issu du corpus examiné.

### 18 Juin 2025
#### 🇩🇿 Algérie - Ministère de la Défense Nationale (MDN)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** mrdump, publication sur un forum cybercriminel (DarkForums)
- **Secteur:** Défense / Sécurité nationale
- **Site web:** Non précisé (fichier interne, aucun domaine institutionnel visible)
- **Statut:** Claim - Unverified
- **Description victime:** Le Ministère de la Défense Nationale (MDN) est l'administration algérienne chargée de la défense du pays. La publication revendique l'obtention de documents internes classifiés relatifs à la logistique et à la chaîne d'approvisionnement du ministère.
- **Analyse:** L'acteur mrdump, déjà à l'origine d'une publication visant le Ministère de la Jeunesse et des Sports le 14 juin 2025, a publié le 18 juin 2025 une nouvelle revendication concernant cette fois le Ministère de la Défense Nationale, annonçant l'obtention de « documents internes classifiés » relatifs aux opérations logistiques et à la chaîne d'approvisionnement.

  Un fichier Excel intitulé « جدول اللوجستيك لوزارة الدفاع » (« Tableau logistique du ministère de la Défense ») a été transmis à AFRINTEL en lien avec cette publication. Compte tenu de la nature revendiquée du document (matériel présenté comme classifié, relatif à la défense nationale), AFRINTEL a effectué un examen structurel limité et non intrusif : le classeur est un fichier XLSX d'environ 15 Ko comprenant une feuille, 77 lignes et 14 colonnes ; environ 65 lignes remplies forment un tableau structuré répétitif, les autres lignes correspondant à des en-têtes ou à du contenu documentaire non assimilable à des enregistrements. AFRINTEL n'a ni reproduit ni extrait de noms, identifiants, lieux, quantités, informations d'approvisionnement ou autres valeurs potentiellement sensibles.

  La structure du fichier est cohérente avec un tableau administratif lié à la logistique, mais cet examen structurel ne permet pas d'établir que le document est authentique, classifié, actuel, complet ou issu du Ministère de la Défense Nationale. La revendication reste donc enregistrée comme non vérifiée. Si la provenance revendiquée était confirmée, l'exposition d'informations sur la logistique ou la chaîne d'approvisionnement militaire pourrait présenter un risque élevé pour la sécurité nationale ; il s'agit d'une évaluation conditionnelle de l'impact et non d'une confirmation de compromission.

### 18 Juin 2025
#### 🇲🇦 Maroc - Ministère de l'Éducation Nationale (men.gov.ma / massar.men.gov.ma)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** RiseAgainLuigi & B4baYega
- **Secteur:** Gouvernement / Éducation.
- **Site web:** https://men.gov.ma / massar.men.gov.ma
- **Statut:** Claim - Unverified
- **Description victime:** Le Ministère de l'Éducation Nationale du Maroc. La plateforme Massar est l'épine dorsale numérique du ministère, centralisant les notes, les inscriptions et le suivi de tous les élèves du Royaume. Les acteurs revendiquent une fuite de données et une mise en vente de plus de 6 millions de dossiers ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 19 Juin 2025
#### 🇩🇿 Algérie - Direction Générale des Douanes (DGD) / Service de contrôle des exportations et importations
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** mrdump (canal Telegram « Server dump »)
- **Secteur:** Gouvernement / Douanes et commerce extérieur
- **Site web:** [douane.gov.dz](https://www.douane.gov.dz)
- **Statut:** Claim - Unverified
- **Description victime:** La Direction Générale des Douanes (DGD) est l'administration algérienne chargée du contrôle douanier, de la perception des droits et taxes et de la régulation des échanges extérieurs, via notamment son Service de contrôle des exportations et importations.
- **Analyse:** Le 19 juin 2025, le canal Telegram « Server dump » (attribué au même acteur mrdump que les publications des 14 et 18 juin 2025) a diffusé une image tamponnée « HACKED » montrant un tableau de bord présenté comme celui de la Direction Générale des Douanes algérienne, avec un message affirmant la « prise de contrôle du système informatique » et un « accès confirmé à l'infrastructure numérique et au panneau d'administration ». Un second message annonce la mise en avant de documents douaniers qui montreraient que l'Algérie exporterait des marchandises vers Israël, en contradiction avec la position officielle algérienne, et promet la publication prochaine de fichiers PDF détaillés.

  Une archive ZIP contenant deux fichiers PDF a été transmise à AFRINTEL en lien avec cette publication : un « registre de cargaison maritime et commercial » concernant le navire « Captain Christos » (IMO 9475410) et un « certificat de conservation de documents » présenté comme émis par le Service de contrôle des exportations et importations de la DGD, tous deux relatifs à une exportation depuis le port de Béjaïa vers le port d'Ashdod (Israël) entre le 20 et le 28 avril 2025.

  L'examen technique de ces deux PDF par AFRINTEL a révélé plusieurs indices convergents de fabrication plutôt que d'une extraction authentique d'un système douanier : les métadonnées des deux fichiers indiquent un auteur nommé « Yassine », une création via Microsoft Word 2016 et une conversion par le service en ligne ilovepdf.com, avec des horodatages de création correspondant exactement au jour de la publication (19 juin 2025), ce qui est incompatible avec des documents scannés ou exportés directement d'un système d'information réel. Le numéro OMI (IMO) cité pour le navire, 9475410, échoue au calcul standard de la clé de contrôle des numéros IMO (chiffre de contrôle attendu : 6 ; chiffre indiqué : 0), ce qui constitue une preuve technique objective que cet identifiant de navire est invalide. Le document de certification cite par ailleurs un « décret exécutif n° 2021-10 » daté du « 15 juin 2010 », une incohérence interne entre le numéro et la date du texte réglementaire invoqué. Les noms d'entreprises importatrices israéliennes mentionnées (ChemImport LTD, Precious Metals Ltd, GasTech Israel, Fashion Importers) n'ont pas pu être vérifiés et présentent un caractère générique.

  Ces éléments convergent vers une évaluation de faible confiance concernant l'authenticité des documents examinés, qui semblent avoir été rédigés pour appuyer une narration politique préexistante plutôt qu'extraits d'un système compromis. Cette conclusion technique porte spécifiquement sur les deux PDF examinés ; elle ne permet pas de confirmer ni d'exclure indépendamment la revendication distincte d'accès au tableau de bord d'administration de la DGD, visible uniquement par une image publiée et non vérifiée. Compte tenu de la fabrication identifiée dans le matériel documentaire associé, l'ensemble de la revendication est évalué avec un niveau de confiance faible. Aucune donnée nominative, numéro de dossier douanier complet ni autre élément susceptible de valider ou d'amplifier la narration de l'acteur n'est reproduit.

### 19 Juin 2025
#### 🇲🇦 Maroc - Fédération Royale Marocaine de Football (FRMF)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Keymous
- **Secteur:** Sport / Administration Publique.
- **Site web:** https://frmf.ma/
- **Statut:** Claim - Data Sample Published
- **Description victime:** Fondée en 1956, la FRMF est l'organisme chargé d'organiser, de gérer et de développer le football au Maroc. Elle supervise les sélections nationales, les compétitions professionnelles et amateurs, ainsi que les ligues régionales.
- **Analyse:** AFRINTEL a identifié la publication source : un post DarkForums de l'acteur Keymous, intitulé « Football federation morocco Leak », revendiquant une base de données de joueurs et de personnel de la FRMF couvrant plus de 4 289 enregistrements nominatifs. AFRINTEL a examiné un échantillon local de documents cohérents avec les registres officiels d'enregistrement et de licence de la FRMF. L'échantillon comprend un enregistrement d'officiel d'équipe issu de FIFA Connect et une licence d'entraîneur CAF Pro, contenant chacun un nom complet, une date de naissance, le sexe, la nationalité, une adresse personnelle, un numéro de téléphone, un identifiant FIFA ou de licence, une date de validité et une photographie, ainsi qu'un formulaire de demande d'enregistrement de club mentionnant le nom complet du titulaire de licence, sa date et son lieu de naissance, son numéro de CIN/passeport, sa nationalité et son club d'affiliation. Deux extraits de tableur, structurés comme un registre d'officiels/membres de football (identifiant d'enregistrement, statut, nom, nationalité, date et année de naissance, région, ville, adresse, code postal, téléphone, email, club et code d'insigne/autorisation), étaient également présents, couvrant au total une trentaine d'enregistrements, et correspondent à la structure de champs décrite dans le post de Keymous. Ceci est cohérent avec l'exposition de parties de la base officielle et de licence de la FRMF plutôt qu'avec de simples documents administratifs génériques. Au moins un enregistrement examiné concerne une personne dont la date de naissance indique qu'elle était mineure au moment de l'enregistrement. AFRINTEL ne reproduit aucun nom, adresse, numéro d'identification, coordonnée ni photographie issus de l'échantillon examiné. L'ampleur totale, l'exhaustivité et la validité actuelle de la base de données sous-jacente n'ont pas pu être confirmées au-delà de l'échantillon limité disponible.

### 20 Juin 2025
#### 🇲🇦 Maroc - INWI (inwi.ma)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Evil_BYTE_Officiel
- **Secteur:** Télécommunications.
- **Site web:** https://inwi.ma
- **Statut:** Claim - Data Sample Published
- **Description victime:** INWI est l'un des trois principaux opérateurs de télécommunications au Maroc, fournissant des services de téléphonie mobile, fixe et d'internet (ADSL/Fibre). L'acteur a publié un échantillon de données sensibles incluant des PII (nom, CIN), des données de contact et des hashs de mots de passe (bcrypt).

### 26 Juin 2025
#### 🇩🇿 Algérie - Ministère des Transports
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** KickingPigs
- **Secteur:** Gouvernement / Transports
- **Site web:** Non précisé
- **Statut:** Claim - Data Sample Published
- **Description victime:** Le ministère algérien des Transports est l'administration publique chargée de la politique nationale des transports et des services administratifs associés.
- **Analyse:** Une publication sur un forum, datée du 26 juin 2025 et attribuée à KickingPigs, présente une fuite supposée du ministère algérien des Transports. Le post énumère des données d'immatriculation et d'administration des transports, notamment des noms, numéros d'identification nationale, noms des parents, numéros d'immatriculation d'entreprises, informations sur les véhicules et leurs immatriculations, documents de permis de conduire et fichiers Excel internes. L'échantillon visible contient des enregistrements structurés de véhicules et des champs de données personnelles sensibles ; AFRINTEL ne reproduit aucun enregistrement ni identifiant. L'authenticité, l'exhaustivité et l'origine technique du jeu de données n'ont pas pu être confirmées indépendamment.

### 20 Juin 2025
#### 🇹🇳 Tunisie - Ministère de la Défense Nationale / Forces armées
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** mrdump (publication sur le canal Telegram « Server dump »)
- **Secteur:** Défense / Sécurité nationale
- **Site web:** Non précisé
- **Statut:** Claim - Data Sample Published
- **Description victime:** Le Ministère tunisien de la Défense Nationale est l'administration gouvernementale chargée de la défense nationale et des forces armées.
- **Analyse:** Une publication datée du 20 juin 2025, attribuée à mrdump, revendique un accès réussi à plusieurs systèmes du Ministère tunisien de la Défense Nationale, plus précisément à sa division des forces armées. La publication affirme qu'un dépôt souterrain d'armes aurait été découvert au mont Chaâmbi, dans le gouvernorat de Kasserine, et fait référence à des images thermiques, des plans d'ingénierie et des informations relatives aux armes et munitions entreposées. Une archive ZIP associée a été transmise à AFRINTEL ; un examen structurel sans lecture du contenu a identifié 10 éléments (six images PNG, un classeur XLSX, un PDF et une image JPG), pour environ 6,2 Mo compressés et 6,3 Mo décompressés. AFRINTEL n'a pas ouvert ni reproduit les fichiers, le matériel étant présenté comme militaire et potentiellement sensible sur le plan opérationnel. La structure de l'archive ne permet pas d'établir indépendamment l'authenticité, la provenance, la classification ou l'exhaustivité du matériel ; l'accès revendiqué reste non vérifié.

### 29 Juin 2025
#### 🇩🇯 Djibouti - Ambassade de Djibouti au Maroc
- **Type d'incident:** Fuite de données

- **Acteur / Groupe :** MdHackersArmy (publication postée par Doxeur23azi sur un forum cybercriminel, DarkForums)
- **Secteur :** Gouvernement / Diplomatie
- **Statut :** Claim - Unverified
- **Site web :** Non précisé

- **Description :**
  L'ambassade de Djibouti au Maroc est la représentation diplomatique de Djibouti accréditée auprès du Royaume du Maroc.

- **Analyse :**
  Une publication intitulée « Leak db of the Embassy of Djibouti in Morocco » a été publiée le 29 juin 2025 sur le forum cybercriminel DarkForums par le compte Doxeur23azi, qui attribue la revendication à MdHackersArmy. La publication se limite à un lien de téléchargement externe et ne décrit ni le type de données, ni la structure des champs, ni le volume d'enregistrements, ni la sensibilité de la base de données annoncée ; aucun échantillon n'est visible. AFRINTEL n'a pas accédé au lien externe. Les données concernées, la population affectée et l'origine technique de la revendication restent inconnues à ce stade.

## Juillet 2025

### 01 Juillet 2025
#### 🇳🇬 Nigeria - Chartered Institute of Bankers of Nigeria (CIBN)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Hepd
- **Secteur:** Services Financiers / Organisme de Régulation Professionnelle.
- **Site web:** https://cibng.org
- **Statut:** Claim - Data Sample Published
- **Description victime:** Institution faîtière de la profession bancaire au Nigeria, responsable de l'accréditation et de l'éthique des banquiers, incluant des membres de la Banque Centrale (CBN). L'acteur affirme avoir publié sur le deep web une base de données incluant des informations sensibles sur l'élite bancaire du pays. AFRINTEL a examiné structurellement l'archive CIBN fournie : 472 fichiers et environ 18 Mo, comprenant des adresses de membres, des coordonnées bancaires, des informations d'emploi, des qualifications, des documents, des wallets, des tables liées aux connexions, des listes de personnel, ainsi que des exports de bases éducatives et fintech et des éléments de journalisation. L'archive contient également des fichiers correspondant à des enregistrements de membres et d'utilisateurs. AFRINTEL ne reproduit aucune donnée personnelle, aucun identifiant, jeton ou document. L'archive étaye une publication substantielle de données, mais son authenticité, son exhaustivité et son rattachement direct à CIBN n'ont pas été vérifiés indépendamment.

### 03 Juillet 2025
#### 🇩🇿 Algérie - Algérie Poste / ECCP
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** sanji_shi5 (compte source)
- **Secteur :** Services postaux / Services financiers
- **Site web :** [poste.dz](https://www.poste.dz)
- **Date de publication de la source :** 3 juillet 2025
- **Statut :** Claim - Data Sample Published
- **Description victime :** Algérie Poste exploite le service ECCP, qui permet aux utilisateurs algériens de consulter le solde de leur compte postal et d'effectuer des achats en ligne. Le post de forum fourni affiche un échantillon présenté sous forme d'identifiants de comptes et de valeurs ressemblant à des mots de passe associés à ECCP/Algérie Poste. Aucun identifiant n'est reproduit ni validé, et le jeu de données sous-jacent n'a pas été collecté.
- **Analyse :** L'échantillon observé suggère une exposition potentielle de données d'accès à un service postal et financier public. Si elles étaient valides, ces données pourraient permettre une prise de contrôle de comptes, des fraudes et des campagnes de phishing ciblées. Le post identifie sanji_shi5 comme compte source, ce qui ne confirme pas indépendamment la compromission, la provenance du jeu de données ni la validité des valeurs affichées.

### 08 Juillet 2025
#### 🇿🇦 Afrique du Sud - MAFATE BUSINESS ENTERPRISE
- **Groupe ransomware:** d4rk4rmy
- **Secteur:** Fournitures Industrielles / Services à l'Exploitation Minière.
- **Site web:** https://mafate.co.za
- **Statut:** Claim - Unverified
- **Description victime:** Mafate Business Enterprise est un fournisseur de services industriels établi à Middelburg (Mpumalanga), au cœur de la région minière sud-africaine.

### 09 Juillet 2025
#### 🇲🇦 Maroc - Fédération Nationale du Bâtiment et des Travaux Publics (FNBTP)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Evil_BYTE_Officiel
- **Secteur :** Bâtiment / Travaux publics / Organisation professionnelle
- **Site web :** [fnbtp.ma](https://www.fnbtp.ma)
- **Statut :** Data Fully Published
- **Description victime :** La Fédération Nationale du Bâtiment et des Travaux Publics (FNBTP) est une organisation professionnelle représentant les entreprises marocaines du secteur du bâtiment et des travaux publics. Le 9 juillet 2025, l'acteur Evil_BYTE_Officiel a publié sur un forum underground une base de données attribuée à la FNBTP, en indiquant la mettre gratuitement à disposition.
- **Analyse :** La publication expose une table nommée `societe` contenant des informations relatives à des entreprises du secteur du BTP. Les champs annoncés dans la publication sont : `Id`, `nb_national`, `nb_regional`, `ENTREPRISE`, `secteur`, `adher`, `MONTANT_COTISATION`, `Responsable`, `Adress`, `Téléphone`, `Fax`, `GSM`, `VILLE` et `E-MAIL`.

  Le fichier CSV analysé par AFRINTEL contient 180 lignes et 14 colonnes. Les données observées comprennent des noms d'entreprises, des références internes, des informations d'adhésion, des noms de responsables, des adresses, des numéros de téléphone, fax et mobiles, des villes et des adresses électroniques professionnelles.

  Parmi les 179 lignes structurées comme des fiches d'entreprises, 166 comportent une ville, principalement Rabat, Salé, Témara et Khémisset. 146 contiennent un nom de responsable, 145 un numéro de téléphone, 139 un fax, 111 un numéro mobile et 81 au moins une adresse électronique. Certaines fiches regroupent plusieurs coordonnées pour une même entreprise.

  Une anomalie est présente dans le fichier fourni. La première ligne contient des valeurs qui ne correspondent pas à la structure métier observée dans le reste de la base. Les enregistrements suivants, notamment ceux visibles dans le post du forum, correspondent en revanche à la structure annoncée par l'acteur.

  Ces données permettent de cartographier des entreprises du secteur du BTP et d'identifier directement leurs responsables et moyens de contact. Elles peuvent être exploitées pour préparer des campagnes de spear phishing, des tentatives d'usurpation d'identité ou des scénarios d'ingénierie sociale ciblant des entreprises et leurs interlocuteurs.

  Les données sont publiées gratuitement par l'acteur. Aucun prix ni demande de rançon n'est visible. La publication contient directement des enregistrements de la base et le fichier analysé confirme la présence de données structurées. Il ne s'agit donc pas uniquement d'une annonce sans données associées. AFRINTEL ne reproduit aucun nom d'entreprise, nom de contact ni coordonnée issus de l'échantillon examiné.

### 13 Juillet 2025
#### 🇹🇿 Tanzanie - Twaweza
- **Groupe ransomware:** nightspire
- **Secteur:** ONG (Éducation & Gouvernance)
- **Site web:** https://twaweza.org
- **Statut:** Claim - Unverified
- **Description victime:** Twaweza East Africa est une organisation panafricaine de premier plan, basée en Tanzanie (avec des bureaux au Kenya et en Ouganda).

### 14 Juillet 2025
#### 🇲🇦 Maroc - IWACLUB (iwaclub.ma)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Keymous
- **Secteur:** Télécommunications / Distribution & Retail.
- **Site web:** https://iwaclub.ma
- **Statut:** Claim - Unverified
- **Description victime:** IWACLUB est l'application professionnelle dédiée au réseau de revendeurs de la société IWACO, l'un des plus importants distributeurs de solutions de télécommunications (notamment l'opérateur inwi) et de produits technologiques au Maroc.

### 14 Juillet 2025
#### 🇩🇿 Algérie - Ministère de l'Énergie, des Mines et des Énergies Renouvelables / SARL SOPRETA
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Phantom Atlas
- **Secteur:** Gouvernement / Énergie et mines ; tiers cité : industrie chimique / étanchéité du bâtiment
- **Site web:** Non précisé pour le ministère ; SOPRETA n'a pas de site officiel identifié
- **Statut:** Claim - Data Sample Published
- **Description victime:** Le Ministère de l'Énergie, des Mines et des Énergies Renouvelables est l'autorité algérienne délivrant les autorisations d'acquisition de matières et produits chimiques dangereux. SARL SOPRETA (Société des Produits d'Étanchéité Algériens), basée à Ain El Arbaa, wilaya d'Ain Témouchent, est une entreprise citée nommément dans le document divulgué.
- **Analyse :** Phantom Atlas a publié le 14 juillet 2025 une accusation visant le ministre Mohamed Arkab, affirmant que le ministère aurait délivré, en mars 2025, une autorisation d'importation de plus de 10 tonnes de substances chimiques dangereuses à une société qualifiée de « pratiquement inconnue, n'apparaissant dans aucun registre industriel connu », en l'absence de tout contrôle ou de rapport environnemental transparent, insinuant une opération aux objectifs troubles.

  AFRINTEL a examiné les documents joints à la publication : l'autorisation n°1000 du 06 mars 2025 délivrée par le ministère à SARL SOPRETA, la liste annexée des matières autorisées (acide chlorhydrique anhydre, nonylphénol éthoxylé sous les désignations commerciales Indulin W-5 et Indulin AA-83, jusqu'à 10 et 8 tonnes respectivement), ainsi qu'une facture proforma de la société belge MBM International SA (Bruxelles) adressée à SOPRETA pour 6 531,60 kg d'Indulin W5 et 2 517,30 kg d'Indulin AA-83, pour un total de 43 257,54 €, avec livraison au port d'Oran. Les trois documents sont cohérents entre eux (même numéro d'autorisation, même adresse d'entreprise, mêmes désignations commerciales de produits).

  Contrairement à l'insinuation de Phantom Atlas, AFRINTEL a identifié SARL SOPRETA (Société des Produits d'Étanchéité Algériens) dans plusieurs annuaires d'entreprises algériennes publics, à l'adresse exacte mentionnée dans l'autorisation ; il s'agit d'une société établie spécialisée dans l'étanchéité du bâtiment et la fabrication de produits chimiques inorganiques de base, notamment des produits bitumineux. Les produits « Indulin » sont des émulsifiants à base de lignine commercialisés pour la fabrication d'émulsions bitumineuses et de produits d'étanchéité routière, ce qui correspond directement à l'activité déclarée de SOPRETA plutôt qu'à un usage détourné ou non identifié. La procédure d'autorisation elle-même (déclaration mensuelle, conformité à la réglementation sur les produits chimiques dangereux, contrôle par la direction de l'énergie et des mines de la wilaya, validité limitée à un an) correspond à un dispositif réglementaire existant, ce qui contredit l'affirmation d'une « absence de tout contrôle effectif ».

  AFRINTEL considère donc que le document divulgué est probablement authentique et cohérent avec une importation industrielle légitime déclarée, mais que le cadrage accusatoire de Phantom Atlas (société « inconnue », absence de contrôle, objectifs opaques) n'est pas corroboré par les informations publiques disponibles sur SOPRETA. Cette fuite constitue néanmoins une divulgation non autorisée d'un document administratif interne du ministère ainsi que de données commerciales d'une entreprise tierce (coordonnées bancaires du fournisseur belge, détails contractuels). AFRINTEL ne reproduit aucune donnée bancaire, ni aucune information susceptible d'identifier des personnes physiques associées à ce dossier.

### 14 Juillet 2025
#### 🇰🇪 Kenya - ICT Authority (icta.go.ke)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Inconnu
- **Secteur :** Gouvernement / Infrastructure numérique
- **Site web :** [icta.go.ke](http://icta.go.ke)
- **Statut :** Claim - Data Sample Published
- **Description victime :** L'ICT Authority du Kenya est une institution publique chargée de coordonner et de soutenir les infrastructures et services gouvernementaux liés aux technologies de l'information et de la communication.
- **Analyse :** AFRINTEL a examiné l'export CSV fourni sans reproduire de données personnelles. Le fichier contient 1 697 lignes de données et des champs relatifs au nom affiché, au téléphone, à l'adresse email, à l'identifiant, au contact mobile, au nom, à des champs d'adresse, aux références utilisateurs et aux liens web. La structure est cohérente avec un export d'annuaire organisationnel contenant des contacts de l'ICT Authority, du secteur public kényan et de prestataires technologiques associés. Les métadonnées du fichier situent la preuve au 14 juillet 2025 ; cette date est traitée comme date de preuve/découverte et non comme une date confirmée de publication ou d'intrusion. Le matériel disponible n'identifie ni l'acteur, ni le forum, ni la méthode d'accès, ni l'étendue complète du jeu de données. L'exposition de coordonnées professionnelles et d'informations organisationnelles peut faciliter le phishing ciblé, l'usurpation et l'ingénierie sociale contre des acteurs publics et technologiques kényans. AFRINTEL classe donc le cas comme une revendication de fuite avec échantillon publié et ne reproduit aucun nom, numéro de téléphone, email, identifiant ni adresse.
### 15 Juillet 2025
#### 🇰🇪 Kenya - Adrian Kenya
- **Groupe ransomware:** lynx
- **Secteur:** Télécommunications / Infrastructures Énergétiques / TIC.
- **Site web:** adrian.co.ke / www.adriankenya.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime:** Adrian Group (Adrian Kenya) est un leader kényan de l'ingénierie technologique.
- **Analyse :** AFRINTEL a examiné un petit échantillon local de quatre documents associés à cette revendication : une facture d'un prestataire pour des travaux d'installation de site télécom (antennes, câbles de liaison et installation RRU) adressée à Adrian Kenya, un avis de paiement de TVA de la Kenya Revenue Authority (KRA) pour Adrian Group Limited couvrant janvier à mars 2025, une note de crédit d'un fournisseur de carburant adressée à Adrian Kenya Limited comportant des informations de véhicules, bancaires et de règlement, ainsi qu'un fil d'emails internes entre des collaborateurs d'Adrian Kenya et d'Adrian Group (domaines adriankenya.com et adriangroup.tech) évoquant le déploiement d'un site télécom au niveau d'un entrepôt. Les documents sont cohérents entre eux, référencent les mêmes noms d'entreprise, domaines et contexte de projet, et contiennent des identifiants personnels complets, des coordonnées bancaires et un numéro fiscal, qu'AFRINTEL ne reproduit pas ici. L'échantillon indique une exposition de documents financiers, fiscaux, fournisseurs et de correspondance interne, mais sa portée se limite à quatre documents et ne permet pas d'établir le volume total ni l'étendue de la compromission sous-jacente. AFRINTEL ne confirme pas l'intrusion de façon indépendante.

### 15 Juillet 2025
#### 🇪🇬 Égypte - Egyptian Electricity Holding Company (EEHC, eehc.gov.eg)
- **Groupe ransomware:** devman
- **Secteur:** Gouvernement / Énergie (Électricité)
- **Site web:** https://eehc.gov.eg
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** L'Egyptian Electricity Holding Company (EEHC) est la société holding publique supervisant la production, le transport et la distribution d'électricité en Égypte, y compris ses filiales de distribution régionales. L'acteur exige 2 270 000 USD.
- **Analyse:** AFRINTEL a examiné un inventaire de répertoires (et non le contenu des fichiers eux-mêmes) d'un partage de fichiers interne présumé, hébergé sur un point de montage MEGA, comprenant environ 8 000 dossiers et plus de 50 000 entrées de fichiers. Les types de fichiers dominants sont les tableurs (plus de 31 000 fichiers Excel) et les PDF (près de 4 000), ainsi que des documents Word, des images et un petit nombre d'exports d'emails. La structure des dossiers inclut des sous-répertoires nommés d'après les sociétés de distribution régionales de l'EEHC (correspondant à la structure réelle de distribution électrique égyptienne : Alexandrie, Canal, Béheira, Moyenne-Égypte, Delta Nord, Caire Sud et Delta Sud), des dossiers personnels nommés d'après des employés, ainsi que du matériel faisant référence aux systèmes Oracle Utilities Customer Care & Billing (CC&B), Meter Data Management (MDM) et Customer Self Service (CSS), accompagnés de propositions techniques et de comptes rendus de réunions liés à un programme de déploiement de compteurs intelligents (AMI). La cohérence entre cette structure de dossiers et l'architecture régionale et système connue de l'EEHC soutient une évaluation à confiance élevée quant à un accès interne réel, bien qu'AFRINTEL n'ait ouvert ni vérifié le contenu des fichiers individuels. Compte tenu de l'ampleur de l'inventaire et du rôle de l'EEHC en tant que société holding nationale de l'électricité en Égypte, une exposition potentielle combinerait des données personnelles d'employés, de la documentation opérationnelle et de facturation interne, ainsi que des enregistrements techniques d'infrastructure pour un service public national critique. AFRINTEL ne reproduit aucun nom d'employé, contenu de fichier ni chemin de dossier contenant des identifiants personnels issu de l'inventaire examiné.

### 15 Juillet 2025
#### 🇳🇦 Namibie - Otjiwarongo Municipality
- **Groupe ransomware:** incransom
- **Secteur:** Administrations publique / Gouvernement Local.
- **Site web:** https://www.otjimun.org.na
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Description victime:** La municipalité d'Otjiwarongo est l'organe de gouvernement local de la ville d'Otjiwarongo, chef-lieu de la région d'Otjozondjupa en Namibie.
- **Analyse:** AFRINTEL a examiné un échantillon local de documents cohérents avec la revendication du cybercriminel incransom, correspondant à un extrait non caviardé du système de paie VIP Payroll System de la municipalité, une liste de rémunération pour la période de paie se terminant le 28 février 2025, recensant des dizaines de dossiers d'employés avec code employé, service, nom complet, montant net de paie en dollars namibiens, code banque et numéro de compte bancaire. Le document porte des en-têtes système authentiques l'identifiant comme une exécution officielle de paie municipale (« 001 Municipality of Otjiwarongo »), cohérent avec une compromission réelle du système RH/paie interne plutôt qu'un échantillon fabriqué. La combinaison de l'identité des employés, de leur rémunération et de leurs coordonnées bancaires complètes pour la paie d'une administration locale soutient une évaluation à très haute confiance. L'exposition de ces données crée un risque important de fraude à la paie, de phishing ciblé et de fraude à l'identité visant les employés municipaux. AFRINTEL ne reproduit aucun nom d'employé, code employé, montant de salaire ni numéro de compte bancaire issu de l'échantillon examiné.

### 15 Juillet 2025
#### 🇲🇷 Mauritanie - Portail QCE (qce.gov.mr)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Inconnu
- **Secteur :** Gouvernement / Marchés publics (Qualification des entreprises et du personnel)
- **Site web :** qce.gov.mr
- **Statut :** Claim - Data Sample Published
- **Description victime :** qce.gov.mr est une plateforme en ligne du gouvernement mauritanien utilisée pour héberger et traiter des dossiers de qualification de personnel et d'entreprises, cohérente avec une vérification des entreprises contractantes et de leur personnel technique dans le cadre de marchés publics ; sa mission institutionnelle précise n'a pas pu être confirmée de manière indépendante à partir de l'échantillon examiné.
- **Analyse :** AFRINTEL a examiné un échantillon local de fichiers cohérents avec des dossiers de qualification de personnel soumis via la plateforme, comprenant des curriculum vitae, des cartes d'identité nationale (CIN), des diplômes, des actes notariés de dépôt de contrats de travail et d'autres pièces justificatives pour des personnes employées par plusieurs entreprises privées mauritaniennes distinctes (notamment dans les secteurs de la construction, du forage et des services techniques). Les documents affichent des en-têtes officiels authentiques, des cachets de notaire et des champs de données personnelles structurés (nom complet, numéro national d'identification, date et lieu de naissance, employeur, poste, signature, photographie), cohérents avec un véritable dépôt de dossiers de qualification/marchés publics plutôt qu'un contenu fabriqué. Aucun acteur revendicateur, lieu de publication ni post de forum n'a pu être identifié pour ce jeu de données ; l'échantillon a été daté à partir des métadonnées des fichiers locaux (mi-juillet 2025) en l'absence de date de publication explicite. La combinaison de numéros d'identification nationale, de diplômes et de dossiers d'emploi pour de nombreuses personnes privées crée un risque significatif de fraude à l'identité, de falsification de documents et d'ingénierie sociale ciblée contre les candidats concernés et leurs employeurs. AFRINTEL ne reproduit aucun nom, numéro d'identification nationale, date de naissance, coordonnée d'employeur ni signature issus de l'échantillon examiné.

### 18 Juillet 2025
#### 🇲🇦 Maroc - Université Mohammed VI Polytechnique (UM6P)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Mercobyte
- **Secteur:** Éducation / Enseignement Supérieur
- **Site web:** https://um6p.ma
- **Statut:** Claim - Unverified
- **Description victime:** Institution (Université) d'excellence basée à Benguerir, pôle stratégique pour la recherche, l'innovation et la formation des cadres au Maroc. L'acteur revendique une fuite de données ciblée et une opération d'influence, publiant des photos d'identité d'étudiants accompagnées d'un message politique ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 25 Juillet 2025
#### 🇹🇳 Tunisie - Ministère des Finances (finances.gov.tn)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Dark 07x Team
- **Secteur:** Gouvernement / Administration Fiscale.
- **Site web:** https://finances.gov.tn
- **Statut:** Claim - Unverified
- **Description victime:** Ministère des Finances Tunisien
- **Analyse:** AFRINTEL n'a pas examiné de preuve technique directement propre à finances.gov.tn au-delà de la revendication « Full Access » de l'acteur. Toutefois, un export de type gestionnaire d'identifiants, examiné en parallèle de cette revendication et attribué à la même campagne Dark 07x Team à la même date, contenait des dizaines de couples identifiant/mot de passe en clair pour un autre établissement tunisien (l'Académie des Banques et des Finances, ABF), suggérant que l'acteur a rebondi entre plusieurs organisations compromises et réutilisé des identifiants collectés au fil de cette campagne. AFRINTEL ne reproduit aucun des identifiants exposés.

### 25 Juillet 2025
#### 🇹🇳 Tunisie - Académie des Banques et des Finances (abf.tn)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Dark 07x Team
- **Secteur:** Formation Professionnelle / Secteur Bancaire.
- **Site web:** https://abf.tn
- **Statut:** Claim - Data Sample Published
- **Description victime:** L'Académie des Banques et des Finances (ABF) est l'organisme de formation continue de l'Association Professionnelle Tunisienne des Banques et des Établissements Financiers (APTBEF).
- **Analyse:** Le matériel montre une session administrative authentifiée sur le site de l'ABF sous un compte nominatif du personnel, confirmant un accès allant au-delà d'une simple revendication. Un export distinct de type gestionnaire d'identifiants, associé à la même campagne, contenait plusieurs dizaines de couples identifiant/mot de passe en clair pour des plateformes liées à l'ABF, notamment son système de visioconférence/webinaire, son portail de formation à distance et un accès d'administration WordPress, ainsi que quelques adresses email associées. Aucun des identifiants ou adresses email exposés n'est reproduit.

### 25 Juillet 2025
#### 🇹🇳 Tunisie - BTK Bank
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Dark 07x Team
- **Secteur:** Banque / Services Financiers.
- **Site web:** https://btknet.com
- **Statut:** Claim - Data Sample Published
- **Description victime:** BTK Bank (Banque Tuniso-Koweïtienne) est une institution bancaire tunisienne issue d'une coentreprise tuniso-koweïtienne.
- **Analyse:** Le matériel montre une session e-banking authentifiée et active sur btknet.com, incluant une liste de comptes, un écran de saisie de virement affichant une liste de bénéficiaires, et un relevé d'identité bancaire (RIB/IBAN) au nom d'un titulaire de compte identifié, confirmant une réelle prise de contrôle de compte plutôt qu'une simple revendication. La publication associée, attribuée à une collaboration entre les pseudonymes Dark 07x, Jokeir 07x et Dr. SHell 08x opérant sous le nom « Dark Hell 07X », annonçait une vente échelonnée des données volées : base de données complète pour 4 000 USD, fichier de données de comptes bancaires pour 2 000 USD, et comptes bancaires individuels de 100 USD (un compte) à 450 USD (cinq comptes). Aucun numéro de compte, IBAN ni identité de client n'est reproduit à partir de l'échantillon examiné.

### 25 Juillet 2025
#### 🇹🇳 Tunisie - Banque de Tunisie (bt.com.tn)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Dark 07x Team
- **Secteur:** Banque / Services Financiers.
- **Site web:** bt.com.tn
- **Statut:** Claim - Data Sample Published
- **Description victime:** Banque de Tunisie (BT) est l'une des plus anciennes et des plus importantes banques privées du pays
- **Analyse:** Le matériel montre un tableau de bord client authentifié et actif sur bt.com.tn, affichant plusieurs soldes de comptes, un module de taux de change, un aperçu de portefeuille de titres et un graphique d'historique de transactions, confirmant un accès réel au niveau du compte plutôt qu'une simple revendication. Aucun numéro de compte ni solde n'est reproduit à partir de l'échantillon examiné.

### 27 Juillet 2025
#### 🇪🇷 Érythrée - Ambassade d'Érythrée aux États-Unis
- **Type d'incident:** Fuite de données

- **Acteur / Groupe :** Gh1nDar
- **Secteur :** Gouvernement / Diplomatie
- **Statut :** Claim - Unverified
- **Site web :** [us.eriembassy.org](https://us.eriembassy.org)

- **Description :**
  L'ambassade d'Érythrée aux États-Unis est la représentation diplomatique officielle de l'État érythréen sur le territoire américain.

- **Analyse :**
  Un cybercriminel utilisant le pseudonyme Gh1nDar affirme, dans une publication sur BreachForums datée du 27 juillet 2025, avoir mis en ligne une fuite de données concernant environ 5 000 citoyens liés à l'ambassade d'Érythrée aux États-Unis. Les données prétendument exposées incluraient numéro de carte d'identité, nom complet, nom de la mère, numéro de passeport, adresse e-mail, numéro de téléphone, date de naissance, religion et profession actuelle. Aucun échantillon vérifiable n'était accessible dans la source collectée. Le compte à l'origine de la publication est récent et ne dispose d'aucun historique de fiabilité. À ce stade, AFRINTEL ne confirme pas l'intrusion ni l'authenticité des données.

### 28 Juillet 2025
#### 🇹🇳 Tunisie - BH Bank
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Dark 07x Team
- **Secteur:** Banque / Services Financiers.
- **Site web:** https://bhbank.tn/
- **Statut:** Claim - Data Sample Published
- **Description victime:** Institution bancaire historique et systémique en Tunisie (Banque de l'Habitat), pilier du financement de l'immobilier et de l'économie nationale.
- **Analyse:** La publication de l'acteur, publiée sous le pseudonyme Jokeir07x dans le cadre de la collaboration « Dark Hell 07X » avec Dr. SHell 08x (également responsable de la revendication BTK Bank), affirme que le groupe a pris le contrôle total de l'infrastructure du site, vidé et analysé toutes les bases de données, et confirmé la compromission des points d'accès back-end et front-end ; la publication annonce séparément une liste de 200 comptes « Yankee » mis en vente pour 100 USDT. Le matériel associé montre des sessions bancaires en ligne authentifiées et actives pour au moins deux comptes clients distincts, dont un compte professionnel « BH Capital Plus », avec soldes visibles, ainsi qu'un historique de transactions de carte bancaire incluant un retrait. Aucun numéro de compte, numéro de carte, identité de client ni solde n'est reproduit à partir de l'échantillon examiné.
### 29 Juillet 2025
#### 🇲🇦 Maroc - Ministère de l’Éducation nationale, du Préscolaire et des Sports
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Wieko
- **Secteur :** Gouvernement / Administration publique / Éducation
- **Site web :** [men.gov.ma](https://men.gov.ma)
- **Statut :** Claim - Data Sample Published

- **Description :**
  Le Ministère de l’Éducation nationale, du Préscolaire et des Sports est l’administration publique marocaine chargée de la politique gouvernementale relative à l’enseignement préscolaire, primaire et secondaire ainsi qu’au sport scolaire. Son portail institutionnel officiel utilise le domaine `men.gov.ma`.

- **Analyse :**
  Une publication attribuée à Wieko sur un forum cybercriminel annonce un fichier texte contenant 223 501 lignes au format `mail:pass`. L’échantillon visible comprend des comptes associés à plusieurs domaines marocains de l’enseignement, notamment des universités et des établissements de formation. Les identifiants individuels ne sont pas reproduits. Une section de téléchargement est visible mais masquée par le forum, ce qui empêche de vérifier le fichier annoncé, son intégrité, l’unicité des lignes ou la validité de tous les couples d’identifiants. Le contenu ressemble davantage à une liste combinée d’identifiants qu’à un export structuré d’une base ministérielle. La présence de comptes issus de plusieurs établissements ne démontre pas une compromission directe du système d’information central du ministère ; l’origine des identifiants, la méthode de collecte et le lien technique avec l’administration centrale restent inconnus. Ces combinaisons peuvent faciliter le credential stuffing, la prise de contrôle de comptes, l’accès non autorisé aux plateformes pédagogiques, le phishing ciblé et l’usurpation d’identité numérique, notamment en cas de réutilisation des mots de passe. Aucun prix, groupe ransomware, volume en octets, délai ou demande d’extorsion n’est mentionné.

- **Note de double revendication :**
  AFRINTEL a recensé séparément, le 18 juin 2025, une revendication concernant la plateforme Massar du ministère. Les acteurs et les jeux de données annoncés diffèrent, et les éléments disponibles ne permettent pas d’établir que les deux publications proviennent de la même compromission.

---
[Rapport de Juillet 2025](./report/README_FR.md)
---

## Août 2025

### 06 Août 2025
#### 🇹🇳 Tunisie - Yasat (yasat.tn)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** RainbowDF
- **Secteur:** Technologies / Distribution Multimédia.
- **Site web:** yasat.tn
- **Statut:** Claim - Data Sample Published
- **Description victime:** Plateforme tunisienne de vente en gros de services multimédia et d'abonnements numériques, servant de fournisseur à de nombreux propriétaires de magasins et revendeurs locaux.
- **Analyse:** AFRINTEL a examiné les données structurées correspondant à la revendication de l'acteur, issues d'exports de la base de données de production de la plateforme d'abonnements IPTV/satellite en gros de Yasat, incluant des produits sous la marque beIN Sports et des offres IPTV génériques avec des champs de liens de flux M3U. Les tables examinées comprennent 52 733 lignes de facturation (produits, quantités, prix, remises, taxes, montants payés/dus), 46 522 enregistrements de ventes générales incluant numéros de mobile, adresses email et liens de flux IPTV (M3U) des clients, 8 623 enregistrements de ventes spécifiques beIN avec des champs de contact client similaires, 211 profils clients (nom, prénom, société, adresse, téléphone, genre, date de naissance) et une table de 22 comptes utilisateurs contenant un champ mot de passe. L'ensemble des données indique des dizaines de milliers d'enregistrements clients et transactionnels exposés, créant un risque significatif de fraude aux abonnements, de réutilisation d'identifiants et de phishing ciblé contre la base de revendeurs et de clients de Yasat. AFRINTEL ne reproduit aucun nom de client, coordonnée, lien de flux ni identifiant issus de l'échantillon examiné.


### 06 Août 2025
#### 🇰🇪 Kenya - KenGen
- **Groupe ransomware:** qilin
- **Secteur:** Énergie / Infrastructures Critiques (Production d'Électricité).
- **Site web:** www.kengen.co.ke
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Description victime:** Kenya Electricity Generating Company PLC (KenGen) est le principal producteur d'électricité du Kenya, fournissant environ 70 % de l'énergie consommée dans le pays.
- **Analyse :** AFRINTEL a examiné un ensemble de documents locaux associés à cette revendication. L'échantillon comprend des documents internes de gestion contractuelle de KenGen relatifs à un projet de construction d'un centre de formation géothermique (une note de l'équipe de mise en œuvre du contrat, un bon de commande officiel et une lettre de garantie bancaire de bonne exécution émise par une banque commerciale), un budget CAPEX détaillé pour la division Geothermal Development, un registre financier de type paie, un tableau d'effectifs du département Geothermal Development listant identifiants employés, noms, genre, intitulés de poste et niveaux de grade, une déclaration de confidentialité d'appel d'offres signée liée à un marché informatique interne, un courrier officiel du ministère kényan de l'Énergie et du Pétrole adressé aux directeurs généraux de KenGen et d'autres entités du secteur énergétique national concernant un cadre de renforcement des ressources humaines et de recherche-développement, ainsi qu'un plan technique d'un local auxiliaire/tableau électrique d'une installation. Les documents présentent un en-tête, des cachets, des signatures et des numéros de contrat cohérents et croisés entre des fichiers de structure indépendante, ce qui renforce la confiance quant à une origine interne aux systèmes de KenGen. L'ensemble combine des données personnelles d'employés, des documents financiers et de passation de marchés internes, de la documentation technique et des correspondances avec des institutions du secteur énergétique national, indiquant une exposition touchant plusieurs systèmes internes plutôt qu'une seule application. AFRINTEL ne reproduit aucun nom d'employé, identifiant, signature ni valeur monétaire issus de l'échantillon, et ne confirme pas l'intrusion de façon indépendante.

### 06 Août 2025
#### 🇲🇦 Maroc - New Era Com
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Chucky_BF
- **Secteur:** Télécoms / Infrastructures / Services IT.
- **Site web:** neweracom.ma
- **Statut:** Data Fully Published
- **Description victime:** Société marocaine spécialisée dans l'ingénierie des télécoms, l'installation d'infrastructures réseaux et les solutions ERP/CRM. L'acteur a publié un dump SQL de 607 Mo contenant plus de 476 000 enregistrements.

### 09 Août 2025
#### 🇳🇬 Nigeria - Zenith Bank Plc
- **Acteur / Groupe :** KaruHunters
- **Secteur:** Banque / Services Financiers.
- **Site web:** zenithbank.com
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** L'une des plus grandes institutions financières du Nigeria et d'Afrique anglophone, cotée à la Bourse du Nigeria et à celle de Londres. L'acteur revendique l'exfiltration et la mise en vente de plus de 1,8 million de dossiers clients, ainsi que des données d'employés. AFRINTEL a examiné un échantillon CSV local de 18 lignes et huit colonnes couvrant un index, un code, un identifiant, un nom, un montant, une adresse, un téléphone et une adresse email. Aucune valeur brute n'est reproduite.
- **Note de corrélation :** La même organisation et le même domaine ont été listés de nouveau le 26 juillet 2026 par ExfilSquad dans une revendication ransomware. Cela établit une corrélation d’identité et de temporalité, mais pas une connexion confirmée entre les deux événements. L’entrée de 2025 concerne une mise en vente alléguée de 1,8 million de dossiers avec un échantillon de 18 lignes examiné ; l’entrée de 2026 ne fournit ni échantillon, ni volume, ni preuve de chiffrement, ni confirmation de la victime. Aucun archivage correspondant, schéma de données, infrastructure partagée ou lien explicite ne relie les deux revendications. AFRINTEL les suit donc comme des entrées liées / revendications possiblement distinctes, avec une relation non résolue.

### 13 Août 2025
#### 🇩🇿 Algérie - Cevital
- **Groupe ransomware:** akira
- **Secteur:** Agroalimentaire/ Industrie / Logistique
- **Site web:** www.cevital.com
- **Statut:** Claim - Unverified
- **Description victime:** Leader de l'industrie agroalimentaire en Algérie, actif dans l'électronique, l'acier, le verre et la distribution.


### 17 Août 2025
#### 🇿🇦 Afrique du Sud - SYSPRO
- **Groupe ransomware:** warlock
- **Secteur:** Technologies (Éditeur de logiciels)
- **Site web:** syspro.com
- **Statut:** Claim - Unverified
- **Description victime:** SYSPRO est un éditeur de logiciels ERP (Enterprise Resource Planning) sud-africain, fournissant des solutions de gestion intégrées pour les entreprises de fabrication et de distribution.

### 18 Août 2025
#### 🇺🇬 Ouganda - Uganda Electricity Transmission Company Limited
- **Groupe ransomware:** qilin
- **Secteur:** Énergie (Électricité)
- **Site web:** https://www.uetcl.go.ug / www.uetcl.com
- **Statut:** Claim - Unverified
- **Description victime:** Société publique ougandaise responsable du transport de l'électricité.


### 11 Août 2025
#### 🇿🇦 Afrique du Sud - Body Graphics Tattoo Supply
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** N1KA
- **Secteur:** Commerce de détail / E-commerce.
- **Site web:** bodygraphicstattoosupply.co.za
- **Date de publication de la source :** 11 août 2025
- **Statut:** Data Fully Published
- **Description victime:** Détaillant en ligne majeur basé à Johannesburg, spécialisé dans la fourniture de matériel de tatouage professionnel et de produits de soin en Afrique du Sud.
- **Analyse:** AFRINTEL a examiné deux fichiers d'export structurés référencés dans une publication observée sur DarkForums, totalisant 6 501 enregistrements, soit un volume cohérent avec celui revendiqué par l'acteur. Le jeu de données correspond à un export de clients et d'administrateurs WordPress/WooCommerce, incluant identifiants de connexion, adresses email, mots de passe hachés (format phpass), adresses postales, numéros de téléphone, adresses IP, chaînes d'user-agent et jetons de session. La cohérence structurelle entre le volume revendiqué et les fichiers examinés, ainsi que la correspondance des champs avec la plateforme e-commerce de la victime, justifie un niveau de confiance élevé, et la publication identifie le compte source N1KA. AFRINTEL ne reproduit aucun nom de client, coordonnée, adresse ni identifiant issu de l'échantillon examiné.

### 18 Août 2025
#### 🇹🇳 Tunisie - International Freight & Commerce
- **Groupe ransomware:** direwolf
- **Secteur:** Logistique
- **Site web:** ifc-tunisie.com
- **Statut:** Claim - Unverified
- **Description victime:** Entreprise tunisienne qui assure des services de transport maritime, aérien et terrestre, ainsi que la gestion logistique et les formalités douanières pour des entreprises importatrices et exportatrices.


### 20 Août 2025
#### 🇿🇦 Afrique du Sud - Netstar South Africa (deuxième attaque)
- **Groupe ransomware:** incransom
- **Secteur:** Technologie / Télématique / Sécurité IoT
- **Site web:** www.netstar.co.za
- **Statut:** Claim - Unverified
- **Description victime:** Netstar, une filiale du groupe Altron, est le pionnier de l'industrie du suivi et de la récupération de véhicules volés (SVR) en Afrique du Sud.
- **Analyse :** AFRINTEL avait déjà enregistré une revendication contre cette même entreprise par devman le 23 mai 2025. Cette seconde revendication, publiée environ trois mois plus tard par un acteur différent, pourrait refléter soit une intrusion distincte réelle, soit une republication/revente de la revendication précédente ; AFRINTEL n'a pas pu confirmer de manière indépendante quel scénario s'applique.

### 23 Août 2025
#### 🇪🇬 Égypte - TEAM4 Security
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** GhostCrawl
- **Secteur:** Services de Sécurité / Défense / Ressources Humaines.
- **Site web:** team4security.com
- **Statut:** Claim - Data Sample Published
- **Description victime:** Société égyptienne spécialisée dans les services de sécurité privée, la protection d'infrastructures et le conseil en gestion des risques. TEAM4 Security est une société de sécurité multidimensionnelle fondée en 2017, opérant depuis le Royaume-Uni et l'Égypte, proposant des solutions intégrées de sécurité numérique et physique, de gardiennage humain et de systèmes K-9 professionnels, ciblant les infrastructures critiques, les villes sûres, ainsi que les clients gouvernementaux et du secteur de la défense.
- **Analyse:** AFRINTEL a examiné les lots de fuite publiés par l'acteur GhostCrawl sur DarkForums ; les horodatages propres au fil de discussion s'échelonnent du 29 au 31 août 2025 (la partie 1 a été publiée le 29 août 2025 à 23h55), soit légèrement après la date de détection du 23 août retenue dans ce fichier. Le matériel correspond à une boîte de messagerie administrative/support exfiltrée (contacts, emails reçus et envoyés au format .eml/.mbox), accompagnée de plusieurs centaines de documents bureautiques et d'images en pièces jointes répartis sur les cinq lots. Les échantillons examinés incluent des feuilles de paie mensuelles du personnel de sécurité sur plusieurs périodes de paie 2025 (agents, superviseurs et personnel de l'unité K-9), un tableau RH/paie détaillé listant numéro d'employé, nom complet, numéro de carte d'identité nationale, poste, date de naissance, date d'embauche, assurance sociale, salaire fixe et variable et primes pour plus de vingt employés, des mémorandums d'incidents internes (dont un rapport d'enquête pour vol daté du 3 novembre 2024), des formulaires mensuels d'effectifs et d'évaluation du personnel, un annuaire téléphonique interne des postes, ainsi que des documents individuels de dossiers employés, accompagnés du papier à en-tête officiel confirmant les adresses du siège égyptien et des agences de TEAM4 Security. La combinaison de numéros de carte d'identité nationale, de dates de naissance, de dates d'embauche et de données salariales du personnel de sécurité crée un risque significatif de fraude à l'identité et d'ingénierie sociale ciblée contre le personnel, tandis que les dossiers d'incidents internes et d'opérations sur site pourraient exposer des informations relatives aux sites clients protégés. AFRINTEL ne reproduit aucun nom d'employé, numéro de carte d'identité nationale, montant de salaire ni autre donnée personnelle issue de l'échantillon examiné.

### 25 Août 2025
#### 🇲🇺 Maurice - SWAN Mauritius
- **Groupe ransomware:** qilin
- **Secteur:** Assurances / Services Financiers.
- **Site web:** www.swan.mu / swanforlife.com
- **Statut:** Claim - Unverified
- **Description victime:** WAN (Swan General Ltd et Swan Life Ltd) est le leader du marché des assurances et des services financiers à l'Île Maurice.

### 25 Août 2025
#### 🇹🇬 Togo - Infrastructures Gouvernementales
- **Type d'incident:** Vente d’accès
- **Acteur / Groupe :** BIGBROTHER
- **Secteur:** Gouvernement / Infrastructures Critiques.
- **Site web:** gouv.tg
- **Statut:** Claim - Data Sample Published
- **Description victime:** Portail officiel et infrastructures numériques de la République Togolaise, hébergeant les services administratifs et les données étatiques.
- **Analyse:** Des éléments corroborent la revendication de l'acteur, incluant le post DarkForums lui-même ainsi que plusieurs éléments montrant un accès administratif actif à plusieurs plateformes numériques gouvernementales togolaises : le système de gestion de l'état civil et de l'identité DSNIC (justice.xflow.gouv.tg), une plateforme de partage de fichiers et de collaboration de type Nextcloud (cloud.numerique.gouv.tg) avec des dossiers partagés et des fichiers de configuration, une instance de collecte de données KoboToolbox (kf.form.gouv.tg) hébergeant plusieurs dizaines d'enquêtes et formulaires gouvernementaux actifs, ainsi qu'un système de reporting statistique de l'éducation (stateduc.planifeducation.gouv.tg). Les éléments montrent un accès administratif réel à des tableaux de bord actifs, et non un simple échantillon public, ce qui est cohérent avec la description de l'offre par l'acteur comme une vulnérabilité 0day donnant un accès privilégié. Cette étendue d'accès à des systèmes et sous-domaines distincts sous le domaine gouv.tg justifie un niveau de confiance élevé quant à une compromission active et non corrigée affectant plusieurs services numériques gouvernementaux, indépendamment du prix en Monero avancé par l'acteur, qu'AFRINTEL ne peut vérifier. AFRINTEL ne reproduit aucun identifiant, valeur de configuration, donnée citoyenne ni détail de session issu des éléments examinés.
---
[Rapport d'Août 2025](./report/README_FR.md)
---

## Septembre 2025

### 02 Septembre 2025
#### 🇩🇿 Algérie - Université des Frères Mentouri Constantine 1 (UMC1)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Fire Wire
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** university-dz.net
- **Statut :** Claim - Data Sample Published
- **Description victime :** L'Université des Frères Mentouri Constantine 1 (UMC1) est une grande université publique algérienne. L'acteur revendicateur affirme une exfiltration de plus de 10 Go, un volume qu'AFRINTEL n'a pas collecté ni analysé. Les fichiers examinés, exfiltrés via ce qui semble être une plateforme web académique partagée (university-dz.net), comprennent les plannings d'examens du Master 2 semestre 1 (janvier 2025) avec dates, modules, salles et départements ; un ensemble de plus de 200 dossiers étudiants détaillés (nom complet, numéro d'inscription universitaire, groupe TD et notes par matière, avec annotations de statut telles qu'exclusion/admission) d'étudiants de L1 (promotion 2015-2016) ; un annuaire de conformité véhicules avec numéros de téléphone et emails ; et un modèle de conférence listant des contacts et affiliations pour un événement académique 2024 (NCME). La combinaison de dossiers académiques, de coordonnées personnelles et de documents administratifs crée un risque significatif de fraude à l'identité, de phishing ciblé et de vishing contre les étudiants, le personnel et les contacts affiliés. L'acteur revendicateur s'identifie sous le nom « Fire Wire ».

### 04 Septembre 2025
#### 🇳🇬 Nigeria - MobileSub
- **Acteur / Groupe :** Non précisé
- **Secteur :** Fintech / Services de paiement
- **Site web :** [mobilesub.com.ng](https://mobilesub.com.ng)
- **Date du fichier source :** 4 septembre 2025
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** MobileSub est une plateforme nigériane de services numériques fournissant des fonctions d'achat de crédit mobile, de données, d'électricité, de télévision par câble, de paris et de paiement associées.
- **Analyse :** AFRINTEL a examiné un dump SQL local d'environ 14,3 Mo contenant 42 tables et 306 blocs INSERT. Le schéma comprend des comptes utilisateurs, la KYC, des clés API, l'historique des transactions, les transferts, l'airtime, les données mobiles, l'électricité, les inscriptions aux examens, les paris, la télévision par câble et d'autres modules de paiement, ainsi que des tables de sauvegarde d'utilisateurs. L'horodatage du fichier source est le 4 septembre 2025 ; il est traité comme un horodatage de découverte/source AFRINTEL, et non comme la date prouvée de la compromission initiale. Le jeu de données peut exposer des informations d'identité, de contact, de KYC, de transaction et d'authentification. Aucune valeur personnelle, clé API ou identifiant n'est reproduit. L'authenticité, l'exhaustivité et le contexte de publication restent non vérifiés.
- **Note d'analyse source :** Le dump contient des catégories de tables sensibles aux identifiants et aux secrets ; AFRINTEL n'a tenté aucune authentification, aucun accès ni récupération de secret.

### 05 Septembre 2025
#### 🇪🇬 Égypte - MeamarGroup
- **Groupe ransomware:** obscura
- **Secteur:** Immobilier / Construction / Ingénierie.
- **Site web:** https://meamargroup.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 3
- **Description victime:** MeamarGroup (incluant Meamar Real Estate Development et Meamar Construction) est un acteur majeur du secteur de la construction en Égypte depuis plus de 25 ans. Basé au Caire (New Cairo), le groupe gère plus de 400 projets allant des complexes résidentiels de luxe aux installations industrielles et médicales (comme l'usine Biogeneric Pharma).
- **Analyse :** AFRINTEL a examiné une archive locale côté serveur (491 fichiers et dossiers, tous appartenant au compte du serveur web www-data) cohérente avec cette revendication. Les horodatages de dossiers de cette collecte se regroupent autour du 05 septembre 2025, correspondant à la date de revendication de cette fiche, tandis que la majorité des fichiers sous-jacents porte un horodatage antérieur du 27 août 2025, suggérant une étape initiale de préparation des données avant la revendication publique. Voir l'analyse complète sous la fiche du 13 octobre 2025 (« meamargroup.com (troisième attaque) »), qui documente en détail la même archive, incluant des grands livres comptables internes, une importante archive de centre d'appels commercial/contacts prospects, des CV d'employés, et des copies de fichiers portant l'extension de chiffrement ransomware « .obscura ». AFRINTEL considère ces éléments comme des enregistrements liés à la même compromission sous-jacente plutôt que comme des incidents indépendants. AFRINTEL ne reproduit aucun nom de client, numéro de contact, nom d'employé ni montant financier issu du matériel examiné.

### 06 Septembre 2025
#### 🇨🇮 Côte d'Ivoire - NSIA Assurances
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Tanaka
- **Secteur:** Assurances / Services Financiers.
- **Site web:** https://www.nsiaassurances.com
- **Statut:** Claim - Unverified
- **Description victime:** Leader de l'assurance et de la banque en Afrique de l'Ouest et Centrale, acteur systémique basé à Abidjan en Côte d'Ivoire. L'acteur affirme faire circuler une base de données de plus de 2,5 millions d'enregistrements transactionnels et financiers ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 08 Septembre 2025
#### 🇳🇬 Nigeria - The Promise Nigeria
- **Groupe ransomware:** yurei
- **Secteur:** Restauration / Services alimentaires / Traiteur.
- **Site web:** https://www.thepromisenig.com
- **Statut:** Claim - Unverified
- **Description victime:** The Promise est une chaîne de restauration rapide (QSR) et un service de traiteur industriel de premier plan au Nigeria, particulièrement implantée à Port Harcourt et dans la région du Delta du Niger.

### 09 Septembre 2025
#### 🇲🇦 Maroc - Dolidol
- **Groupe ransomware:** thegentlemen
- **Secteur:** Industrie Manufacturière / Literie / Ameublement.
- **Site web:** https://www.dolidol.ma
- **Statut:** Claim - Unverified
- **Description victime:** Dolidol (filiale du groupe Palmeraie Industries et Services) est le leader incontesté de la literie et de la mousse polyuréthane au Maroc.

### 09 Septembre 2025
#### 🇿🇼 Zimbabwe - Proplastics Limited
- **Groupe ransomware:** thegentlemen
- **Secteur:** Industrie manufacturière (Plastiques)
- **Site web:** https://www.proplastics.co.zw
- **Statut:** Claim - Unverified
- **Description victime:** Proplastics Limited est le principal fabricant et fournisseur de systèmes de tuyauterie en plastique (PVC, PEHD) au Zimbabwe.
- **Analyse :** Le jeu local fourni contient 63 fichiers associés à Proplastics, notamment des PDF, des tableurs, des fichiers image et des fichiers texte. Les noms de fichiers indiquent des documents métier relatifs aux factures et notes de crédit, soldes de comptes, nomenclatures, reliquats de commandes, livraisons, analyses de ventes et rapports par agence. Les fichiers portent des dates couvrant 2023-2024, tandis que les métadonnées du répertoire situent la collecte en septembre 2025 ; ces dates sont considérées comme contexte de preuve et non comme date confirmée d intrusion ou de publication. Le matériel soutient la plausibilité et la sensibilité potentielle de la revendication de septembre 2025, mais ne permet pas d établir indépendamment le vecteur d accès, le périmètre complet des données ni l attribution à thegentlemen. AFRINTEL ne reproduit aucun nom, détail de compte, montant financier, enregistrement client ou contenu documentaire.

### 10 Septembre 2025
#### 🇳🇬 Nigeria - Princeps Credit Systems Limited
- **Groupe ransomware:** killsec
- **Secteur:** Finance
- **Site web:** https://princepsfinance.com
- **Statut:** Claim - Unverified
- **Description victime:** Institution financière basée à Lagos, spécialisée dans le crédit à la consommation et le financement des PME.

### 11 Septembre 2025
#### 🇳🇦 Namibie - Epia Financial Services
- **Groupe ransomware:** radar
- **Secteur:** Services financiers
- **Site web:** https://epiafs.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Description victime:** Institution financière basée à Windhoek, offrant des services de gestion de patrimoine, de conseil en investissement et de courtage en Namibie.
- **Analyse:** Des éléments de messagerie exfiltrés rattachés à la revendication (correspondance envoyée depuis et vers les boîtes de réception et d'administration d'EPIA avec Bank Windhoek/Capricorn Group, First National Bank of Namibia et NamPost, relative à des vérifications de comptes clients) sont examinés, ainsi que la structure d'un échantillon représentatif de fichiers d'administration de fonds de pension au niveau des champs/colonnes, sans ouvrir ni extraire de ligne individuelle d'adhérent. Les éléments examinés correspondent au rôle d'EPIA en tant qu'administrateur du Namibia Building Workers Pension Fund (NBWPF) et d'autres clients institutionnels. Les classeurs de données d'adhérents (par exemple un extrait de janvier 2025) contiennent plusieurs feuilles de plusieurs milliers d'enregistrements chacune (Actives, Deferred, Unclaimed, Exits) partageant un schéma de champs cohérent : numéro de membre, nom, prénom, autres prénoms, référence entreprise, date de naissance, numéro d'identité nationale, numéro de passeport, statut cotisant, statut du membre, nom de l'employeur, genre, dates d'emploi et d'adhésion au fonds, salaire mensuel et annuel, montant et date du solde du fonds (fund credit), date de dernière cotisation, date de sortie et détails de paiement. Un extrait de données actuarielles distinct couvre la période de septembre 2022 à avril 2024 avec un schéma et une ampleur comparables. D'autres fichiers inspectés structurellement incluent des rapports d'administration et d'allocation de revenus pluriannuels (résumés agrégés de transactions financières par période) et des formulaires d'autorisation client signés, le plus récent daté de juin 2025. AFRINTEL n'a pas ouvert chaque fichier de l'ensemble ; la cohérence des noms de fichiers et la correspondance par e-mail indiquent que les mêmes catégories d'enregistrements se répètent sur toute la période 2022-2025. La combinaison de numéros d'identification nationale, de dates de naissance, de données salariales et de solde de fonds de pension pour plusieurs milliers d'individus, avec la correspondance employeur et bancaire, représente une exposition à fort impact. L'étendue, la continuité jusqu'à mi-2025 et la spécificité organisationnelle des éléments examinés soutiennent un niveau de confiance élevé quant à la compromission de la messagerie et des fichiers, indépendamment de la revendication publique du groupe ransomware. L'ensemble local contient 73 fichiers pour environ 79,8 Mo, comprenant des tableurs, des rapports, des présentations, un fichier DOCX d'employeur et des fichiers image. Le classeur d'adhérents de janvier 2025 contient une feuille de synthèse et des feuilles d'état des membres (Actives, Deferred, Unclaimed et Exits), avec une feuille de synthèse allant jusqu'à 8 652 lignes et des feuilles allant jusqu'à 35 colonnes ; la structure examinée comprend des champs relatifs aux membres, employeurs, identités, emplois, salaires, crédits de pension, cotisations, sorties et paiements. L'extrait actuariel contient 8 168 lignes et 167 colonnes pour une période allant de septembre 2022 à avril 2024. Les éléments horodatés du 11 septembre 2025 sont cohérents avec le contexte de découverte de septembre. Aucun nom d'adhérent, numéro d'identification, coordonnée bancaire, signature, montant de salaire ni contenu de correspondance n'est reproduit à partir de l'échantillon examiné.


### 11 Septembre 2025
#### 🇦🇴 Angola - Base de données des employés du gouvernement angolais (pape.gov.ao)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** privilege, publication sur un forum cybercriminel
- **Secteur :** Gouvernement / Administration publique
- **Site web :** [pape.gov.ao](https://pape.gov.ao)
- **Statut :** Claim - Data Sample Published
- **Description victime :** La source présente pape.gov.ao comme une plateforme liée au gouvernement angolais et affirme proposer des dossiers d'employés de différents secteurs et domaines administratifs.
- **Analyse :** La publication du 11 septembre 2025 revendique une base de données de 245 employés du gouvernement angolais et énumère des champs relatifs aux identifiants d'employés, noms, dates de naissance, zones administratives et fonctions. Le fichier TXT local fourni pour examen contient 244 lignes non vides séparées par des virgules, dont une ligne d'en-tête et environ 243 lignes de données, avec six champs par ligne. Cela confirme l'existence d'un échantillon structuré de données d'employés, mais ne permet pas de confirmer indépendamment le total annoncé, l'organisme gouvernemental exact, l'authenticité ou l'exhaustivité du jeu de données. AFRINTEL ne reproduit aucun nom, identifiant, date de naissance ni autre donnée personnelle issue du fichier.
### 12 Septembre 2025
#### 🇨🇩 Congo (RDC) - Fonds pour la Réforme de l'Administration Publique (FRAP)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** privilege
- **Secteur :** Gouvernement / Administration
- **Site web :** [frap.cd](https://frap.cd/)
- **Statut :** Data Fully Published
- **Description victime :** Organisme en charge de la modernisation de l'administration en RDC.
- **Analyse :** AFRINTEL a examiné le post DarkForums lui-même, publié le 12 septembre 2025 par le cybercriminel privilege (statut VIP, compte créé en septembre 2025), intitulé « FRAP.CD — 1,136 LINES | Full User Data | Gov/Staff Access ». Le post décrit une base de données de 1 136 enregistrements comprenant des identifiants de connexion et des mots de passe hachés (plusieurs formats de hachage), des identifiants personnels (nom, prénom, sexe), des coordonnées (email, téléphone) lorsque disponibles, des champs de référence et de désignation de documents internes, ainsi que des métadonnées système (date de création, dernière connexion, dernière mise à jour du mot de passe, créé/modifié par, statut du compte). L'acteur décrit ces données comme couvrant des comptes d'administrateurs et de personnel sectoriel du portail FRAP.CD, ce qui est cohérent avec le rôle de la plateforme dans la gestion des profils administratifs et des comptes internes du personnel du Fonds pour la Réforme de l'Administration Publique. L'ensemble complet des données est proposé via un lien d'hébergement externe et n'est pas montré directement dans le post ; AFRINTEL n'a pas pu valider de façon indépendante l'authenticité ni l'exhaustivité du fichier hébergé. Compte tenu des identifiants de connexion et des données personnelles décrits, l'exposition de ce matériel créerait un risque d'accès au portail par réutilisation d'identifiants et de phishing ciblé contre le personnel de l'administration publique congolaise. AFRINTEL ne reproduit aucun identifiant, mot de passe, donnée personnelle ni coordonnée issu du post examiné.

### 14 Septembre 2025
#### 🇰🇪 Kenya - Office Of The Registrar Of Political Parties
- **Groupe ransomware:** qilin
- **Secteur:** Administrations publiques
- **Site web:** https://www.orpp.go.ke
- **Statut:** Claim - Unverified
- **Description victime:** Organisme d'État kenyan chargé de l'enregistrement, de la régulation et de la supervision du financement des partis politiques.

### 16 Septembre 2025
#### 🇰🇪 Kenya - Jubilee Life Insurance
- **Groupe ransomware:** warlock
- **Secteur:** Assurances / Services financiers
- **Site web:** https://jubileelife.com
- **Statut:** Claim - Unverified
- **Description victime:** Acteur majeur de l'assurance-vie et de la gestion de fonds au Kenya, filiale de Jubilee Holdings Limited.

### 17 Septembre 2025
#### 🇪🇬 Égypte - Accflex ERP
- **Groupe ransomware:** arcusmedia
- **Secteur:** Technologies / Édition de logiciels ERP.
- **Site web:** https://www.accflex.com
- **Statut:** Claim - Unverified
- **Description victime:** Éditeur égyptien de solutions de gestion intégrées (comptabilité, RH, production) utilisé par de nombreuses entreprises au Moyen-Orient et en Afrique.

### 22 Septembre 2025
#### 🇲🇦 Maroc - Fractalite (fractalite.com)
- **Groupe ransomware:** killsec
- **Secteur:** Technologies/ Services Numériques / Développement Logiciel.
- **Site web:** https://fractalite.com
- **Statut:** Claim - Unverified
- **Description victime:** Fractalite est une agence de conseil et d'ingénierie numérique marocaine, spécialisée dans le développement de solutions logicielles et l'accompagnement digital des entreprises.


### 24 Septembre 2025
#### 🇳🇬 Nigeria - Kolomoni Microfinance Bank
- **Acteur / Groupe :** Non précisé
- **Secteur :** Microfinance / Banque
- **Site web :** [kolomonimfb.com](https://kolomonimfb.com)
- **Date de l'archive source :** 24 septembre 2025
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Fuite de données
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime :** Kolomoni Microfinance Bank est une institution financière nigériane qui fournit des services de microfinance et de banque numérique à ses titulaires de comptes.
- **Analyse :** AFRINTEL a examiné l'extraction RAR fournie et son fichier CSV Kolomoni. Le fichier contient 37 825 lignes et 12 colonnes couvrant le nom et le numéro de compte, l'email, le téléphone, le genre, la date de naissance, le statut du compte, l'adresse, la zone de gouvernement local, l'État, la dernière connexion et la date de l'enregistrement. La combinaison d'identifiants financiers, de coordonnées, de données démographiques, de localisation et de métadonnées de connexion crée des risques de phishing, de prise de contrôle de comptes, de fraude à l'identité et d'escroqueries financières ciblées. L'horodatage de l'archive est le 24 septembre 2025, tandis que les métadonnées internes du CSV contiennent une date de fichier antérieure au 24 août 2025 ; aucune de ces dates ne prouve la date de compromission initiale. Aucune valeur personnelle n'est reproduite. L'acteur, le forum de publication, l'authenticité et l'exhaustivité restent non précisés ou non vérifiés.

### 29 Septembre 2025
#### 🇸🇳 Sénégal - Direction Générale des Impôts et des Domaines (DGID)
- **Groupe ransomware:** BlackShrantac
- **Secteur:** Administration Publique / Finances / Fiscalité.
- **Site web:** https://www.impots.gouv.sn
- **Statut:** Claim - Unverified
- **Description victime:** La **DGID** est l'organe central du Ministère des Finances du Sénégal, responsable de la collecte des impôts, de la gestion du domaine national et du cadastre. Le groupe ransomware affirme avoir divulgué 1 téraoctet (1 To) de données sensibles, comprenant des bases de données fiscales structurées, des registres fonciers et des informations bancaires de contribuables ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 30 Septembre 2025
#### 🇪🇬 Égypte - Telecom Egypt (TE Data)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** KILLUAX
- **Secteur :** Télécommunications
- **Site web :** te.eg
- **Statut :** Claim - Data Sample Published
- **Description victime :** Telecom Egypt exploite le service d'accès internet TE Data. L'échantillon examiné contient des enregistrements de type comptabilité RADIUS (identifiants abonnés au format tedata.net.eg, adresses IP de NAS, adresses MAC, adresses IP attribuées, horodatages de début/fin de session et type de connexion). Seul un nombre restreint d'enregistrements (36) était disponible pour analyse, ce qui limite l'évaluation de l'ampleur totale ; l'exposition pourrait néanmoins faciliter l'identification d'abonnés et la reconnaissance réseau.

## Octobre 2025

### 01 Octobre 2025
#### 🇿🇦 Afrique du Sud - Climatron (Pty) Ltd
- **Groupe ransomware:** incransom
- **Secteur:** Construction / CVC
- **Site web:** https://climatron.co.za
- **Statut:** Claim - Unverified
- **Description victime:** Climatron (Pty) Ltd est une entreprise spécialisée dans les solutions de climatisation industrielle et commerciale, basée à Johannesburg.

### 05 Octobre 2025
#### 🇿🇦 Afrique du Sud - The Methodist Church of Southern Africa
- **Groupe ransomware:** beast
- **Secteur:** Religion / Organisation caritative
- **Site web:** www.methodist.org.za
- **Statut:** Claim - Unverified
- **Description victime:** The Methodist Church of Southern Africa (MCSA) est l'une des dénominations chrétiennes les plus influentes de la région. Elle opère non seulement en Afrique du Sud, mais aussi au Botswana, au Lesotho, en Namibie, au Swaziland et au Mozambique.

### 10 Octobre 2025
#### 🇿🇦 Afrique du Sud - Momentum Logistics
- **Groupe ransomware:** brotherhood
- **Secteur:** Transport / Logistique
- **Site web:** www.momentumlogistics.co.za
- **Statut:** Claim - Unverified
- **Description victime:** Momentum Logistics est un prestataire logistique sud-africain basé à Johannesburg.

### 13 Octobre 2025
#### 🇲🇦 Maroc - LA VOIE EXPRESS
- **Groupe ransomware:** medusa
- **Secteur:** Logistique
- **Site web:** https://lavoieexpress.ma / https://lavoieexpress.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 3
- **Description victime:** Société marocaine de logistique basée à Casablanca, offrant des services de messagerie, transport et entreposage.
- **Analyse :** AFRINTEL a examiné un échantillon local d'exports de tableurs multi-feuilles cohérents avec la revendication du cybercriminel medusa, chacun filigrané avec l'adresse du site de fuite Tor du groupe. Le matériel examiné comprend un grand livre comptable (écritures bancaires et journal datées de 2020-2021), des classeurs d'entrepôt et de logistique couvrant les mouvements de réception, d'expédition, de mise en stock préparé et de transfert interne de marchandises pour de grandes marques d'électroménager (référençant des gammes de produits BSH/Bosch-Siemens) rattachés à du personnel interne nommément identifié gérant ces opérations, ainsi qu'un rapport de balance âgée des comptes clients listant plusieurs dizaines de clients corporate nommés dans plusieurs villes marocaines (Casablanca, Agadir, Tanger, Marrakech, Fès, Settat et autres), incluant des comptes nationaux et multinationaux reconnus (parmi lesquels des entités affiliées à Procter & Gamble, Savola Maroc, Centrale Laitière, Ciment du Maroc, BSH Electroménager et Ecolab), avec les contacts clients nommés, numéros de téléphone, soldes impayés, conditions de paiement et statut de recouvrement/contentieux. La cohérence interne des données entre les modules comptable, entrepôt et commercial, la présence de comptes clients marocains et multinationaux réels et identifiables, ainsi que la période couverte sur plusieurs années (2020-2023) et plusieurs agences, soutiennent une évaluation à très haute confiance d'une compromission réelle et étendue des systèmes ERP et comptables internes de La Voie Express. Compte tenu de l'ampleur des données de comptes clients et du grand livre bancaire exposées, et de leur extension à la clientèle d'un opérateur logistique national majeur, cet incident crée un risque important de fraude à la facture, de compromission de messagerie professionnelle et d'ingénierie sociale ciblée visant La Voie Express et ses clients corporate, au-delà de la seule exposition opérationnelle de l'entreprise. AFRINTEL ne reproduit aucun nom de client, nom de contact, numéro de téléphone, montant financier ni identifiant de personnel issu du matériel examiné.

### 13 Octobre 2025
#### 🇪🇬 Égypte - meamargroup.com (troisième attaque)
- **Groupe ransomware:** obscura
- **Secteur:** Immobilier / Construction / Ingénierie
- **Site web:** https://meamargroup.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 3
- **Description victime:** Société égyptienne spécialisée dans le développement immobilier.
- **Analyse :** AFRINTEL a examiné une archive locale côté serveur (491 fichiers et dossiers, tous appartenant au compte du serveur web www-data) cohérente avec la revendication du cybercriminel obscura. Les horodatages des fichiers se répartissent en deux groupes : la majorité du matériel (484 entrées) datée du 27 août 2025, et un plus petit ensemble d'entrées de dossiers datées du 05 septembre 2025, correspondant à la première revendication publique du groupe contre cette victime. Le contenu examiné comprend des classeurs comptables internes pluriannuels (grands livres annuels couvrant 2015-2024, un fichier financier « main data 2024 », des feuilles de comparaison de coûts de projets), une archive étendue de centre d'appels commercial d'environ 249 tableurs datés couvrant des journaux d'appels manqués et de contacts prospects de septembre 2024 à juillet 2025, au moins 21 CV et résumés d'employés, ainsi que du matériel interne de conception, de brochure et de plans CAO pour des projets immobiliers nommés (dont les projets Clove Mall et Prime Mall). Une archive imbriquée au sein de la collection contient un mélange de fichiers originaux et de copies portant l'extension de chiffrement ransomware « .obscura » (par exemple plusieurs classeurs de grands livres annuels et des fichiers du service informatique), mettant directement en évidence l'étape de chiffrement des fichiers de l'attaque plutôt qu'une simple revendication d'exfiltration. Un court fichier texte cohérent avec un compte à rebours de portail de négociation Tor (« 240 hours. Not available yet! ») était également présent. La combinaison de la propriété des fichiers par le serveur web, d'horodatages pluriannuels internement cohérents et de la présence de copies de fichiers chiffrées par l'acteur, soutient une évaluation à très haute confiance d'une compromission réelle et étendue du serveur de fichiers interne de MeamarGroup. Compte tenu de l'ampleur des grands livres financiers, des données de contacts prospects commerciaux et des informations personnelles d'employés exposées, cet incident crée un risque de fraude à la facture, de phishing ciblé visant les prospects et employés, et d'exposition concurrentielle des données internes de projets et de tarification. AFRINTEL ne reproduit aucun nom de client, numéro de contact, nom d'employé ni montant financier issu du matériel examiné.


### 15 Octobre 2025
#### 🇰🇪 Kenya - Turnkey Africa
- **Groupe ransomware:** qilin
- **Secteur:** Technologies/ Fintech (Solutions pour l'Assurance).
- **Site web:** https://turnkeyafrica.com
- **Statut:** Claim - Unverified
- **Description victime:** Turnkey Africa est un leader technologique panafricain. L'entreprise développe et fournit des solutions logicielles de gestion (Core Insurance Systems) pour les compagnies d'assurance et de réassurance dans plus de 10 pays d'Afrique.

### 17 Octobre 2025
#### 🇲🇬 Madagascar - Madagascar Airlines
- **Groupe ransomware:** thegentlemen
- **Secteur:** Transport aérien
- **Site web:** www.madagascarairlines.com
- **Statut:** Claim - Unverified
- **Description victime:** Madagascar Airlines est la compagnie aérienne nationale de la République de Madagascar.

### 18 Octobre 2025
#### 🇨🇩 Congo (RDC) - TK HOLDINGS GROUP
- **Groupe ransomware:** radar
- **Secteur:** Exploitation minière / Conglomérat
- **Site web:** https://congomineralservices.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d’impact:** Level 4
- **Description victime:** Holding congolais avec des activités dans le bois, la logistique et l'exploration minière.
- **Analyse:** AFRINTEL a examiné le classeur CTI fourni par l'analyste et 32 captures associées à la publication de radar. L'ensemble comprend sept catégories de documents : textes douaniers et juridiques de la RDC, documents de marchés publics et de gouvernance, politiques salariales et de recrutement de TK Holdings, rapport géologique de Congo Mineral Services concernant le projet d'exploration cuprifère Mikuba Mining, ainsi qu'un arrêté de contrôle environnemental. Le classeur classe la politique salariale et le rapport géologique Mikuba au niveau de sensibilité critique. Le rapport géologique mentionne des campagnes de forage et des teneurs en cuivre, ce qui crée un risque plausible d'espionnage industriel et de renseignement sur une ressource stratégique. Les politiques RH exposent des procédures internes relatives aux salaires, primes, congés, recrutement et confidentialité, avec des risques de ciblage des employés, d'abus interne et d'atteinte réputationnelle. Les documents juridiques et réglementaires pourraient faciliter la fraude documentaire, la corruption ou la manipulation des processus de conformité et d'importation si leur authenticité et leur validité étaient établies. Les éléments confirment l'affichage de documents apparemment sensibles, mais ne permettent pas de confirmer indépendamment le vecteur d'intrusion, l'exhaustivité du jeu publié, l'authenticité de chaque document ni l'impact opérationnel. AFRINTEL ne reproduit pas le contenu des documents, les noms, signatures ou autres informations sensibles.

### 18 Octobre 2025
#### 🇿🇦 Afrique du Sud - Université du Witwatersrand (WITS)
- **Groupe ransomware:** clop
- **Secteur:** Éducation (Université)
- **Site web:** https://www.wits.ac.za
- **Statut:** Data Fully Published
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3
- **Description victime:** L'Université du Witwatersrand, située à Johannesburg, est l'une des institutions de recherche les plus prestigieuses d'Afrique.
- **Analyse :** AFRINTEL a examiné une capture de la page de revendication du site de fuite de Clop pour wits.ac.za, utilisant le modèle standard de fiche victime du groupe (champs Headquarters, Phone, Website, Revenue et Industry). Contrairement aux pages examinées pour d'autres entrées africaines sur le même site de fuite, cette page inclut une section dédiée « Torrent Magnet Link » référençant wits.ac.za, indiquant que l'acteur a mis à disposition un jeu de données téléchargeable plutôt qu'une simple page de revendication. Le profil d'entreprise affiché (secteur Colleges & Universities, Education) est cohérent avec le profil public de l'Université du Witwatersrand. AFRINTEL n'a ni téléchargé ni examiné le contenu du torrent référencé ; le volume, le contenu et la sensibilité du jeu de données publié ne sont donc pas évalués de manière indépendante. La présence d'une section de lien magnet fonctionnelle, distincte des pages de simple revendication observées pour d'autres entrées, soutient une évaluation à confiance élevée selon laquelle des données ont bien été mises à disposition au téléchargement. Compte tenu du statut de WITS en tant qu'université de recherche majeure, un jeu de données confirmé pourrait inclure des données personnelles d'étudiants, de personnel ou de recherche, créant un risque de fraude à l'identité et de phishing ciblé visant la communauté universitaire. AFRINTEL ne reproduit ni le lien magnet, ni l'adresse du siège, ni le numéro de téléphone issus du matériel examiné.

### 19 Octobre 2025
#### 🇬🇦 Gabon - SANgel
- **Groupe ransomware:** qilin
- **Secteur:** Agroalimentaire
- **Site web:** https://sangel-gabon.com
- **Statut:** Claim - Unverified
- **Description victime:** Entreprise gabonaise de production et de distribution alimentaire basée à Libreville, spécialisée dans les produits surgelés.

### 20 Octobre 2025
#### 🇪🇬 Égypte - Al Ahly Leasing & Factoring Company
- **Groupe ransomware:** blackshrantac
- **Secteur:** Finance
- **Site web:** https://alahlyleasing.com
- **Statut:** Claim - Unverified
- **Description victime:** Institution financière égyptienne spécialisée dans le crédit-bail et l'affacturage, filiale de la Banque Nationale d'Égypte.

### 23 Octobre 2025
#### 🇲🇦 Maroc - STAR LÉGUMES
- **Groupe ransomware:** tengu
- **Secteur:** Commerce de gros (Produits alimentaires)
- **Site web:** https://starlegumes.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 3
- **Description victime:** Grossiste marocain en fruits, légumes, épices et graines séchées basé à Casablanca.
- **Analyse :** AFRINTEL a examiné la page du site de fuite ainsi qu'un échantillon local de documents cohérents avec la revendication du cybercriminel tengu. La page du site de fuite elle-même a été capturée (compteur de vues et indicateur de temps écoulé visibles), accompagnée d'un extrait du registre de commerce marocain (Tribunal de Commerce de Casablanca) confirmant l'identité juridique de l'entreprise, sa date d'immatriculation, son capital social, son adresse enregistrée et le nom de son gérant ; de plusieurs factures clients datées entre novembre 2021 et mars 2025 portant le numéro d'enregistrement ONSSA de l'entreprise, des noms de clients, adresses et montants de transaction ; ainsi qu'un export de grand livre comptable généré par le système (« Journal Factures Clients ») couvrant octobre 2024, imprimé en février 2025, listant environ 50 enregistrements de factures séquentielles avec noms de clients, numéros de facture et montants HT/TVA/TTC. Un tableau de synthèse analytique structuré construit à partir de ce matériel détaille par ailleurs un enregistrement d'identité légale, un échantillon de contacts clients (nom, identifiant fiscal/ICE, adresse) et un échantillon de factures. La combinaison d'une inscription officielle sur le site de fuite, d'un extrait de registre de commerce authentique, d'exports comptables générés par le système et datés, et d'une cohérence de marque interne entre documents couvrant plus de trois années, soutient une évaluation à très haute confiance d'une compromission réelle des systèmes de facturation et de comptabilité de Star Légumes. Compte tenu de l'ampleur des données de contacts clients et de transactions exposées, cet incident crée un risque de fraude fournisseur/client, de compromission de messagerie professionnelle et de revente de la base clients. AFRINTEL ne reproduit aucun nom de client, adresse, identifiant fiscal ni montant financier issu du matériel examiné.

### 24 Octobre 2025
#### 🇲🇦 Maroc - Le MULTI LABORATOIRE LC2A
- **Groupe ransomware:** tengu
- **Secteur:** Industrie pharmaceutique / Laboratoire
- **Site web:** https://multi-laboratoire-lc2a.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 2
- **Description victime:** Laboratoire marocain proposant une plateforme de configuration de projets analytiques pour les entreprises.
- **Analyse :** AFRINTEL a examiné un échantillon local de documents internes cohérents avec la revendication du cybercriminel tengu, adressés à LC2A ou générés par ce dernier. Le matériel examiné comprend un devis fournisseur d'un vendeur d'équipements de laboratoire (daté de mai 2022) adressé au service achats de LC2A, détaillant réactifs et équipements analytiques avec tarification unitaire et totale, ainsi qu'un journal interne de contrôle d'équipement (« Carte de contrôle des équipements », formulaire qualité référencé FOR06/PRT06) pour une balance de laboratoire, enregistrant des vérifications quotidiennes de calibration jusqu'en octobre 2021. Le nom de l'entreprise, les références de formulaires internes et la cohérence de marque entre les deux fichiers soutiennent une évaluation à confiance élevée selon laquelle l'échantillon provient des systèmes internes de LC2A plutôt que d'une revendication fabriquée. Un paquet de données volumineux référencé aux côtés de cet échantillon n'a pas terminé son transfert et n'a pas pu être examiné ; cette analyse se limite aux deux documents décrits ci-dessus. Compte tenu de la nature opérationnelle et fournisseur du matériel examiné, cet incident présente un risque modéré d'usurpation d'identité fournisseur et de divulgation des pratiques internes de contrôle qualité et d'approvisionnement, aucune donnée patient ou clinique n'ayant été observée dans l'échantillon examiné. AFRINTEL ne reproduit aucun nom de fournisseur, détail tarifaire, code équipement ni identifiant de personnel issu du matériel examiné.

### 24 Octobre 2025
#### 🇳🇬 Nigeria - Henrietta Ezeoke Law Firm
- **Groupe ransomware:** qilin
- **Secteur:** Services juridiques
- **Site web:** https://houstonwrongfuldeathlawyers.com
- **Statut:** Claim - Unverified
- **Description victime:** Cabinet d'avocats nigérian.

### 28 Octobre 2025
#### 🇹🇿 Tanzanie - Alios Finance Group
- **Groupe ransomware:** incransom
- **Secteur:** Finance
- **Site web:** https://aliosfinance.co.tz
- **Statut:** Claim - Unverified
- **Description victime:** Opérateur financier panafricain présent en Tanzanie, proposant des solutions de financement spécialisées. Lors de cette attaque, le groupe incransom a revendiqué l'exfiltration de 100 Go de données.

### 28 Octobre 2025
#### 🇹🇳 Tunisie - Alios Finance Group
- **Groupe ransomware:** incransom
- **Secteur:** Finance
- **Site web:** https://aliosfinance.tn
- **Statut:** Claim - Unverified
- **Description victime:** Opérateur financier panafricain présent en Tunisie, spécialisé dans le financement des entreprises et des particuliers. Lors de cette intrusion, 100 Go de données ont été exfiltrés par le groupe incransom.


### 31 Octobre 2025
#### 🇩🇿 Algérie - TMF Logistics
- **Groupe ransomware:** incransom
- **Secteur:** Logistique
- **Site web:** https://tmf-logistics.com
- **Statut:** Claim - Data Sample Published
- **Description victime:** TMF Logistics est une entreprise algérienne spécialisée dans les solutions de transport et de logistique. Lors de cette attaque, le groupe incransom a revendiqué l'exfiltration de 39 Go de données sensibles de l'entreprise.
- **Analyse:** Des documents financiers et opérationnels internes examinés par AFRINTEL corroborent la revendication d'incransom. Un tableau de chiffre d'affaires par client de novembre 2024 recense une trentaine de clients professionnels de TMF Logistics, dont de grandes entreprises agroalimentaires et pharmaceutiques opérant en Algérie (par exemple Danone Algérie, l'Institut Pasteur d'Algérie, GlaxoSmithKline Algérie, Fromagerie Bel Algérie), ainsi que des catégories de prestations de transport frigorifique et général (frigo, bâché, plateau). Un export de facturation détaillée couvre des opérations de transport au niveau de chaque facture, réparties sur de nombreuses wilayas algériennes (dont Béjaïa, Bouira, Batna, Constantine, Djelfa, Ghardaïa, Ouargla et Tindouf), révélant un réseau de livraison à l'échelle nationale. Un document de décharge de livraison confirme l'identité officielle de l'entreprise : SPA TMF Logistics, basée dans la zone d'activité de Taharacht, Akbou (wilaya de Béjaïa), avec ses coordonnées enregistrées et ses références d'immatriculation professionnelle. La combinaison d'un portefeuille client national, de données de réseau de livraison et de références d'immatriculation crée un risque de chaîne d'approvisionnement (usurpation de client, fraude à la facturation, intelligence concurrentielle) qui dépasse la seule exposition opérationnelle de TMF Logistics.

### 31 Octobre 2025
#### 🇲🇦 Maroc - Institut Agronomique et Vétérinaire Hassan II (IAV Hassan II)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** DBhacker_BF
- **Secteur :** Éducation / Enseignement supérieur / Agronomie et sciences vétérinaires
- **Site web :** iav.ac.ma
- **Statut :** Claim - Data Sample Published
- **Description victime :** L'IAV Hassan II est un établissement public marocain de référence pour l'enseignement supérieur agronomique et vétérinaire, basé à Rabat. La base examinée contient 4 208 enregistrements de candidats et couvre les candidats et comprend nom complet, date et lieu de naissance, nationalité, genre, adresse, numéro de carte d'identité nationale (CIN), numéro de téléphone, adresse email, statut d'inscription, filière et un champ mot de passe (majoritairement vide dans l'échantillon examiné). La combinaison du CIN, des coordonnées et des données académiques crée un risque de fraude à l'identité, de phishing ciblé et d'abus de récupération de compte ; l'exhaustivité et l'origine du fichier n'ont pas été confirmées de manière indépendante.

### 31 Octobre 2025
#### 🇲🇦 Maroc - Ministère de l'Enseignement Supérieur, de la Recherche Scientifique et de l'Innovation (enssup.gov.ma)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** EternalRed
- **Secteur :** Gouvernement / Éducation / Enseignement supérieur
- **Site web :** enssup.gov.ma
- **Date de publication de la source :** 25 octobre 2025
- **Statut :** Claim - Data Sample Published
- **Description victime :** enssup.gov.ma est le Ministère marocain de l'Enseignement Supérieur, de la Recherche Scientifique et de l'Innovation. Le fichier texte fourni contient exactement 942 930 lignes, ce qui correspond au volume annoncé ; il s'agit d'une extraction nationale d'étudiants couvrant 942 930 enregistrements, avec des champs incluant le numéro de carte d'identité nationale (CIN), l'identifiant national étudiant (code Massar), le nom complet en arabe et en français, le genre, la date de naissance, la nationalité, le code et le nom de l'établissement, la filière et le niveau d'étude. Les métadonnées internes du fichier indiquent que l'extraction a été initialement compilée vers décembre 2022, bien qu'AFRINTEL l'ait examinée dans le cadre d'une collecte de données de 2025. L'ampleur et la structure du jeu de données indiquent une exposition nationale significative de dossiers d'étudiants de l'enseignement supérieur, créant des risques de fraude à l'identité et de phishing ciblé contre les étudiants et les établissements ; l'exhaustivité et la source exacte de l'extraction n'ont pas été confirmées de manière indépendante.

## Novembre 2025

### 04 Novembre 2025
#### 🇲🇦 Maroc - DOVERN Import
- **Groupe ransomware:** spacebears
- **Secteur:** Logistique
- **Site web:** https://dovern-import.com/
- **Statut:** Claim - Unverified
- **Description victime:** Société d'importation basée au Maroc, spécialisée dans la distribution de vins fins, spiritueux et champagnes de prestige.

### 04 Novembre 2025
#### 🇿🇦 Afrique du Sud - Wannabees (wannabees.co.za)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** Inconnu
- **Secteur :** Ressources humaines / Recrutement
- **Site web :** wannabees.co.za
- **Statut :** Claim - Data Sample Published
- **Description victime :** Wannabees semble être une plateforme sud-africaine de recrutement et d'emploi temporaire, d'après la structure et le contenu de la base de candidats examinée.
- **Analyse :** AFRINTEL a examiné deux fichiers identiques dans l'ensemble de preuves fourni (DB.txt et HoJmS, avec une correspondance SHA-256), contenant un export de cinq dossiers de candidats. Le schéma comprend des identifiants de candidats, des numéros d'identité nationale, des noms, adresses, numéros de téléphone, champs d'adresse email, dates de naissance, nationalité, historique d'emploi, profession actuelle, prétentions salariales et champs relatifs à la rémunération, ainsi qu'un champ de mot de passe. L'échantillon est structurellement cohérent avec une base de recrutement ou de gestion de personnel et contient des informations personnelles et professionnelles hautement sensibles. Les fichiers sont datés du 4 novembre 2025 dans le répertoire de preuve ; cette date est traitée comme date de découverte/de preuve et non comme une date confirmée de publication ou d'intrusion. Le matériel disponible n'identifie ni acteur, ni forum, ni méthode d'accès, ni volume complet du jeu de données. AFRINTEL classe donc le cas comme une revendication de fuite avec échantillon publié et ne reproduit aucun nom, numéro d'identité, contact, mot de passe ni autre donnée personnelle brute.
### 05 Novembre 2025
#### 🇨🇮 Côte d'Ivoire - Anka (Anka.africa)
- **Acteur / Groupe :** Spirigatito, publication postée sur un forum cybercriminel
- **Secteur :** Logistique
- **Site web :** https://www.anka.africa/
- **Statut :** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Type d'incident :** Fuite de données
- **Description victime :** Plateforme ivoirienne leader facilitant l'exportation, les paiements et la logistique pour les créateurs et commerçants africains vers le marché mondial.
- **Analyse :** La publication sur le forum annonce la vente d'une base de données attribuée à Anka, revendiquant 537 877 utilisateurs uniques et un volume de 12,1 Go, avec une liste de champs annoncée comprenant id, username, fullname, email, token, avatar, gender, date de naissance et téléphone, entre autres. AFRINTEL a examiné des extraits structurés dérivés de l'échantillon publié avec le post, comprenant un petit nombre d'enregistrements utilisateurs individuels (moins de 30). Le schéma examiné correspond à la liste de champs annoncée dans la publication, en l'étendant avec des attributs supplémentaires : date de dernière connexion, indicateurs de verrouillage et de suppression de compte, type de compte, nombre et montant des achats, solde du portefeuille, et champs de ventes vendeur sur la marketplace. Les enregistrements examinés montrent des horodatages de création de compte s'étalant de mai 2017 à mai 2024, des devises incluant l'EUR, l'USD et le GMD, et des paramètres régionaux en français et en anglais, cohérents avec une base d'utilisateurs internationale pour une plateforme africaine de commerce transfrontalier et de paiements. La cohérence structurelle entre la liste de champs annoncée et l'échantillon examiné, ainsi que la plausibilité des valeurs enregistrées (horodatages sur plusieurs années, devises mixtes, paramètres régionaux mixtes), permettent de faire passer ce cas d'une revendication non vérifiée à une revendication accompagnée d'un échantillon de données publié. AFRINTEL n'a pas vérifié indépendamment le volume total revendiqué de 537 877 utilisateurs / 12,1 Go, l'origine ou la méthode de compromission, ni l'affirmation distincte de l'acteur selon laquelle la plateforme génère 10 millions de dollars de revenus. L'exposition de ce jeu de données combinerait noms complets, coordonnées, dates de naissance, genre, jetons de compte et informations de portefeuille/achats, créant un risque significatif de prise de contrôle de comptes, de phishing ciblé et de fraude financière visant les utilisateurs de la plateforme. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone, jeton, nom d'utilisateur ni autre enregistrement individuel issu de l'échantillon examiné.

### 06 Novembre 2025
#### 🇪🇬 Égypte - ELSEWEDYELECTRIC.COM
- **Groupe ransomware:** clop
- **Secteur:** Technologies / Industrie
- **Site web:** www.elsewedyelectric.com
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 2
- **Description victime:** Principal fabricant égyptien de câbles, de systèmes électriques et de produits d'ingénierie.
- **Analyse :** AFRINTEL a examiné une capture de la page de revendication du site de fuite de Clop pour elsewedyelectric.com, utilisant le modèle standard de fiche victime du groupe (champs Headquarters, Phone, Website, Revenue et Industry, suivis du texte d'avertissement récurrent du groupe). Le profil d'entreprise affiché (chiffre d'affaires d'environ 4,9 milliards de dollars, secteur manufacturing/wire & cable) est cohérent avec le profil public connu d'Elsewedy Electric en tant que grand fabricant égyptien de câbles et de systèmes électriques. Cette fiche apparaissait aux côtés de nombreuses autres organisations multinationales sur la même page du site de fuite de Clop, cohérent avec la campagne d'exploitation de masse du groupe visant les clients d'Oracle E-Business Suite révélée en 2025. La correspondance du profil d'entreprise soutient une évaluation à confiance moyenne quant à l'authenticité de la fiche, bien qu'AFRINTEL n'ait examiné aucun fichier exfiltré sous-jacent, lien magnet ou échantillon de données au-delà de la page de revendication elle-même ; l'ampleur, le volume et la sensibilité des données réellement détenues par l'acteur restent non vérifiés. AFRINTEL ne reproduit ni l'adresse du siège ni le numéro de téléphone de l'entreprise issus du matériel examiné.

### 06 Novembre 2025
#### 🇿🇲 Zambie - ZANACO.CO.ZM
- **Groupe ransomware:** clop
- **Secteur:** Services financiers (Banque)
- **Site web:** www.zanaco.co.zm
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3
- **Description victime:** Zambia National Commercial Bank, l'une des principales banques commerciales de Zambie.
- **Analyse :** AFRINTEL a examiné des captures de la page de revendication du site de fuite de Clop pour zanaco.co.zm, incluant la barre de navigation du groupe montrant cette fiche aux côtés de nombreuses autres organisations multinationales (parmi lesquelles Logitech, The Washington Post, Trimble et Elsewedy Electric), cohérent avec la campagne d'exploitation de masse de Clop visant les clients d'Oracle E-Business Suite révélée en 2025. Le profil d'entreprise affiché (chiffre d'affaires d'environ 337,9 millions de dollars, secteur finance/banking) est cohérent avec le profil public connu de la Zambia National Commercial Bank. La fiche utilise le même modèle standard et le même texte d'avertissement récurrent observés sur d'autres pages victimes de Clop, ce qui soutient une évaluation à confiance moyenne quant à l'authenticité de l'entrée, bien qu'AFRINTEL n'ait examiné aucun fichier exfiltré sous-jacent, lien magnet ou échantillon de données au-delà des pages de revendication ; l'ampleur, le volume et la sensibilité des données clients ou bancaires réellement détenues par l'acteur restent non vérifiés. Compte tenu du rôle de ZANACO en tant que banque commerciale majeure, toute exposition de données confirmée présenterait un risque important de fraude financière et de phishing ciblé visant sa clientèle. AFRINTEL ne reproduit ni l'adresse du siège ni le numéro de téléphone de la banque issus du matériel examiné.

### 06 Novembre 2025
#### 🇲🇦 Maroc - www.marjane.ma
- **Groupe ransomware:** stormous
- **Secteur:** Commerce de détail / Grande distribution / E-commerce.
- **Site web:** www.marjane.ma
- **Statut:** Data Fully Published
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Description victime:** Groupe Marjane est le plus grand groupe marocain de grande distribution, exploitant des hypermarchés et supermarchés.
- **Analyse :** AFRINTEL a examiné une capture de preuve publiée en lien avec la revendication du cybercriminel stormous, montrant une session active sur un portail SSL-VPN Fortinet daté du 10 novembre 2025. La liste de favoris du portail référence une infrastructure interne cohérente avec l'environnement de Marjane, incluant un sous-domaine marjane.ma, une instance de wiki Confluence hébergée sous un sous-domaine confluence.marjane, un favori de collaboration intitulé « huddle/Store Managers » cohérent avec la gestion multi-magasins de l'enseigne, ainsi qu'un favori d'accès SSH direct vers un hôte interne. La présence de noms d'hôtes internes spécifiques à Marjane et d'un point d'accès SSH fonctionnel soutient une évaluation à confiance élevée selon laquelle la capture reflète un accès réel au réseau interne plutôt qu'une preuve fabriquée. À la suite de cet échantillon initial, l'acteur aurait publié l'intégralité du jeu de données revendiqué sur son site de fuite ; AFRINTEL n'a pas pu collecter ni examiner cette publication ultérieure, dont le contenu, le volume et l'authenticité ne sont donc pas évalués de manière indépendante. L'accès interne démontré, au niveau VPN et SSH, au réseau du plus grand groupe de grande distribution du Maroc crée un risque dépassant toute catégorie de données isolée, incluant une perturbation potentielle ou une compromission supplémentaire des systèmes de point de vente, de logistique et de gestion des magasins à l'échelle du réseau de succursales de Marjane. AFRINTEL ne reproduit aucun identifiant, jeton de session, adresse IP ni nom d'hôte interne issu du matériel examiné.

### 08 Novembre 2025
#### 🇲🇦 Maroc - NARSA (Agence Nationale de la Sécurité Routière)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** anisanas2
- **Secteur :** Gouvernement / Transport / Sécurité routière
- **Site web :** Non identifié avec certitude
- **Statut :** Claim - Data Sample Published
- **Description victime :** La NARSA est l'agence nationale marocaine chargée de la sécurité routière, de l'immatriculation des véhicules et du contrôle technique.
- **Analyse :** AFRINTEL a examiné un export CSV structuré correspondant à un ensemble d'enregistrements d'immatriculation de véhicules, avec des champs incluant le nom complet du propriétaire, l'adresse, le numéro de carte d'identité nationale (CIN), la marque du véhicule, la catégorie, le type, le numéro de châssis, la cylindrée, les dates du centre d'immatriculation et de mise en circulation, le prix d'achat et le numéro de plaque d'immatriculation. La taille de l'échantillon et la structure des champs sont cohérentes avec le jeu de données revendiqué d'environ 150 000 lignes, bien qu'AFRINTEL n'ait pas pu confirmer de manière indépendante l'identité de l'acteur revendicateur ni l'ampleur totale exacte à partir du matériel examiné. La combinaison de numéros de CIN, d'adresses personnelles et de données d'identification de véhicules crée un risque de fraude à l'identité, de fraude liée aux véhicules (y compris de faux documents d'immatriculation) et de risques pour la sécurité physique liés à l'exposition d'adresses. AFRINTEL ne reproduit aucun nom de propriétaire, adresse, numéro de CIN ni numéro de plaque issus de l'échantillon examiné.


### 09 Novembre 2025
#### 🇿🇦 Afrique du Sud - Eastern Cape Department of Human Settlements (ECDHS)
- **Groupe ransomware:** nightspire
- **Secteur:** Administrations publiques/ Logement social.
- **Site web:** ecdhs.gov.za
- **Statut:** Claim - Unverified
- **Description victime:** Le Département des Établissements Humains du Cap Oriental sud-africain est l'organe provincial chargé de la politique du logement, de l'aménagement urbain et de l'accès à la propriété pour les populations vulnérables en Afrique du Sud.

### 09 Novembre 2025
#### 🇳🇬 Nigeria - Fidelity Pension Managers, Nigeria
- **Groupe ransomware:** nightspire
- **Secteur:** Services financiers (Gestion de pension)
- **Site web:** fidelitypensionmanagers.com
- **Statut:** Claim - Unverified
- **Description victime:** Gestionnaire de fonds de pension nigérian.


### 11 Novembre 2025
#### 🇪🇬 Égypte - Samcrete Holding
- **Groupe ransomware:** clop
- **Secteur:** Construction
- **Site web:** www.samcrete.com
- **Statut:** Claim - Unverified
- **Description victime:** Samcrete Holding est une société entièrement intégrée d'ingénierie, de sous-traitance, de développement, de fabrication et d'investissement créée en 1963.

### 25 Novembre 2025
#### 🇪🇬 Égypte - LAMAICA, Egypt
- **Groupe ransomware:** nightspire
- **Secteur:** Industrie manufacturière du bois et des matériaux de construction.
- **Site web:** lamaica.com
- **Statut:** Claim - Unverified
- **Description victime:** LAMAICA est l'un des leaders du marché égyptien dans la production de panneaux de particules mélaminés, de stratifiés haute pression (HPL), de bandes de chant et de composants pour l'ameublement.

### 26 Novembre 2025
#### 🇪🇬 Égypte - Arabia Holding
- **Groupe ransomware:** qilin
- **Secteur:** Immobilier / Investissement / Développement Urbain.
- **Site web:** arabia-holding.com
- **Statut:** Claim - Unverified
- **Description victime:** Holding égyptienne avec des intérêts dans divers secteurs, dont l'immobilier et la gestion.

### 26 Novembre 2025
#### 🇨🇮 Côte d'Ivoire - Santé Espoir Vie Côte d’Ivoire (SEV-CI)
- **Groupe ransomware:** benzona
- **Secteur:** Santé / ONG / Humanitaire.
- **Site web:** sevci.org
- **Statut:** Claim - Unverified
- **Description victime:** Santé Espoir Vie Côte d’Ivoire (SEV-CI) est une organisation non gouvernementale ivoirienne de premier plan. Elle œuvre pour l'amélioration de la santé des populations, avec un focus particulier sur la lutte contre le VIH/SIDA, la tuberculose, et le renforcement des systèmes de santé communautaires.

### 30 Novembre 2025
#### 🇲🇦 Maroc - Joutech
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** RL000
- **Secteur :** Technologie / Services numériques (activité exacte non confirmée de manière indépendante)
- **Site web :** joutech.ma
- **Statut :** Claim - Data Sample Published
- **Description victime :** Joutech est une entreprise marocaine exploitant le domaine joutech.ma. Le fichier examiné est un export de liste de diffusion/contacts de 1 350 enregistrements, contenant civilité, prénom, nom, adresse email, champ société, indicateurs marketing/ventes et date d'inscription. Aucun mot de passe ni donnée financière n'a été observé dans l'échantillon examiné. Cette exposition pourrait faciliter des campagnes de phishing ciblé et de spam contre les contacts listés ; l'exhaustivité et l'origine du fichier n'ont pas été confirmées de manière indépendante.

## Décembre 2025

### 05 Décembre 2025
#### 🇪🇬 Égypte - 3S Software (Secured Smart Systems Overview Metrics)
- **Groupe ransomware:** dragonforce
- **Secteur:** Technologies
- **Site web:** 3s-software.com
- **Statut:** Claim - Unverified
- **Description victime:** Prestataire de services technologiques égyptien spécialisé dans le développement de logiciels.


### 05 Décembre 2025
#### 🇿🇲 Zambie - National Health Insurance Management Authority
- **Groupe ransomware:** nova
- **Secteur:** Assurances (Santé)
- **Site web:** https://nhima.co.zm/
- **Statut:** Claim - Unverified
- **Description victime:** Autorité zambienne gérant le régime national d'assurance maladie.

### 06 Décembre 2025
#### 🇬🇭 Ghana - Kasapreko Company Limited
- **Groupe ransomware:** qilin
- **Secteur:** Agroalimentaire / Boissons (Alcoolisées et non alcoolisées).
- **Site web:** www.kasapreko.com
- **Statut:** Claim - Unverified
- **Description victime:** Kasapreko est l'un des plus grands fabricants de boissons au Ghana et un acteur majeur à l'exportation dans toute la région CEDEAO.

### 06 Décembre 2025
#### 🇿🇦 Afrique du Sud - Diesel Electric
- **Groupe ransomware:** qilin
- **Secteur:** Distribution automobile / Équipement de diagnostic
- **Site web:** diesel-electric.co.za
- **Statut:** Claim - Unverified
- **Description victime:** Diesel-Electric est l'un des plus grands distributeurs d'Afrique du Sud spécialisé dans les composants automobiles, les systèmes d'injection diesel et l'équipement de diagnostic (partenaire majeur de Bosch).

### 07 Décembre 2025
#### 🇪🇬 Égypte - incolease.com
- **Groupe ransomware:** lockbit5
- **Secteur:** Finance
- **Site web:** www.incolease.com
- **Statut:** Claim - Unverified
- **Description victime:** Société de leasing égyptienne.

### 07 Décembre 2025
#### 🇿🇦 Afrique du Sud - elundini.gov.za
- **Groupe ransomware:** lockbit5
- **Secteur:** Administration Publique / Gouvernement Local.
- **Site web:** elundini.gov.za
- **Statut:** Claim - Unverified
- **Description victime:** La Municipalité locale d'Elundini est une autorité administrative clé située dans le district de Joe Gqabi (Cap oriental), englobant les villes de Maclear, Ugie et Mount Fletcher.

### 08 Décembre 2025
#### 🇪🇬 Égypte - Arkan
- **Groupe ransomware:** ransomhouse
- **Secteur:** Finance / Commerce
- **Site web:** arkanonline.com
- **Statut:** Claim - Unverified
- **Description victime:** Conglomérat égyptien, Arkan Group, actif dans l'industrie, l'agriculture et le commerce de gros.


### 11 Décembre 2025
#### 🇳🇬 Nigeria - Leadway Assurance / Leadway Health
- **Groupe ransomware:** kazu
- **Secteur:** Assurances
- **Site web:** leadwayhealth.com
- **Statut:** Claim - Unverified
- **Description victime:** Leadway Assurance est la plus grande compagnie d'assurance privée au Nigeria.

### 12 Décembre 2025
#### 🇹🇳 Tunisie - Hopital La Rabta (Centre Hospitalier Universitaire)
- **Groupe ransomware:** devman
- **Secteur:** Santé
- **Site web:** www.chularabta.tn
- **Statut:** Claim - Unverified
- **Description victime:** L'Hôpital La Rabta est l'un des plus grands pôles hospitaliers de Tunisie.


### 15 Décembre 2025
#### 🇹🇳 Tunisie - Société Tunisienne de Radiologie (strtn.org)
- **Groupe ransomware:** nova
- **Secteur:** Santé / Association Médicale / Éducation.
- **Site web:** strtn.org
- **Statut:** Claim - Unverified
- **Description victime:** La Société Tunisienne de Radiologie (STR) est l'organisme de référence pour les radiologues en Tunisie.

### 22 Décembre 2025
#### 🇪🇬 Égypte - Polaris Parks
- **Groupe ransomware:** direwolf
- **Secteur:** Développement Immobilier / Gestion de Parcs Industriels et de Loisirs.
- **Site web:** polarisparks.com
- **Statut:** Claim - Unverified
- **Description victime:** Polaris Parks est l'un des principaux développeurs de parcs industriels privés en Égypte.

### 24 Décembre 2025
#### 🇿🇦 Afrique du Sud - National Credit Regulator (NCR)
- **Groupe ransomware:** dragonforce
- **Secteur:** Administrations publiques (Régulation financière)
- **Site web:** www.ncr.org.za
- **Statut:** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4
- **Description victime:** Organisme public sud-africain chargé de réguler le secteur du crédit à la consommation.
- **Analyse :** AFRINTEL a examiné un échantillon local de documents associés à cette revendication. Le matériel comprend environ 25 dossiers de cas consommateurs nommés individuellement, cohérents avec des dossiers de réexamen de dette/conseil en désendettement traités par le NCR, une vingtaine d'emails référençant des individus nommés accompagnés d'identifiants partiels ressemblant à des préfixes de date de naissance de numéros d'identité sud-africains, ainsi qu'un mémo d'enquête interne daté du 24 juin 2022, adressé par le responsable du service Plaintes du NCR au responsable par intérim des Enquêtes et de l'Application de la réglementation, ouvrant une enquête sur une entité désignée « Debt Accord Solutions » soupçonnée d'exercer comme conseiller en désendettement non enregistré. L'échantillon comprend également un tableur administratif interne suivant les volumes d'emails liés aux dossiers sur une base quasi quotidienne à mensuelle d'août 2020 à décembre 2024, des fichiers logo à l'image du NCR, des formulaires réglementaires (dont un Form 29 et un document de consentement écrit au titre du Règlement 50(5)), un document de mandat et un relevé de coordonnées bancaires. Les documents sont cohérents avec l'image de marque du NCR, sa structure organisationnelle (responsables et services nommés) et le format de ses dossiers réglementaires. L'échantillon indique une exposition de dossiers consommateurs de réexamen de dette, de documents d'enquête et d'application de la réglementation, ainsi que de données opérationnelles pluriannuelles, créant un risque significatif de fraude à l'identité et de phishing ciblé contre des consommateurs nommés et des agents du NCR, ainsi qu'un risque d'interférence avec des enquêtes réglementaires en cours. AFRINTEL ne reproduit aucun nom de consommateur, identifiant, contenu de dossier, nom d'agent ni détail d'enquête issus du matériel examiné.

### 26 Décembre 2025
#### 🇹🇳 Tunisie - Hopital La Rabta (deuxième cyberattaque)
- **Groupe ransomware:** qilin
- **Secteur:** Santé
- **Site web:** www.chularabta.tn
- **Statut:** Claim - Unverified
- **Description victime:** L'Hôpital La Rabta est l'un des plus grands pôles hospitaliers de Tunisie.
- **Analyse :** AFRINTEL avait déjà enregistré une revendication contre ce même hôpital par devman le 12 décembre 2025. Cette seconde revendication, publiée deux semaines plus tard par un acteur différent, pourrait refléter soit une intrusion distincte réelle, soit une republication/revente de la revendication précédente ; AFRINTEL n'a pas pu confirmer de manière indépendante quel scénario s'applique.

### 26 Décembre 2025
#### 🇿🇼 Zimbabwe - Proplastics Limited (deuxième cyberattaque)
- **Groupe ransomware:** lockbit5
- **Secteur:** Industrie manufacturière (Plastiques)
- **Site web:** proplastics.co.zw
- **Statut:** Claim - Unverified
- **Description victime:** Proplastics Limited est le principal fabricant et fournisseur de systèmes de tuyauterie en plastique (PVC, PEHD) au Zimbabwe.
- **Analyse :** AFRINTEL avait déjà enregistré une revendication contre cette même entreprise par thegentlemen le 9 septembre 2025. Cette seconde revendication, publiée environ trois mois et demi plus tard par un acteur différent, pourrait refléter soit une intrusion distincte réelle, soit une republication/revente de la revendication précédente ; AFRINTEL n'a pas pu confirmer de manière indépendante quel scénario s'applique.

### 29 Décembre 2025
#### 🇩🇿 Algérie - Université d'Oran 1 Ahmed Ben Bella
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** GhostVector (compte source)
- **Secteur :** Éducation / Université
- **Site web :** Non précisé
- **Date de publication de la source :** 29 décembre 2025
- **Statut :** Claim - Data Sample Published
- **Description victime :** L'Université d'Oran 1 Ahmed Ben Bella est un établissement public d'enseignement supérieur situé à Oran, en Algérie. Le post fourni annonce une base datée de 2023 comprenant environ 58 000 enregistrements et des champs incluant les noms, dates de naissance, numéros de téléphone, genre, adresses e-mail, hachages de mots de passe et nationalité.
- **Analyse :** Le post affiche un échantillon structuré associé à l'université et identifie GhostVector comme compte source. Si elles étaient valides, ces données pourraient permettre des fraudes à l'identité, du phishing et des attaques ciblant les comptes d'étudiants ou de personnel. Aucun enregistrement personnel, identifiant, hachage ou coordonnée n'est reproduit ; la revendication et la provenance du jeu de données n'ont pas été confirmées indépendamment.

### 29 Décembre 2025
#### 🇪🇬 Égypte - 100 Watt Plast (100wattplast.com)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** camillabf, publication sur un forum cybercriminel (RaidForums)
- **Secteur :** Industrie / Fabrication de produits électriques et plastiques
- **Site web :** [100wattplast.com](https://100wattplast.com)
- **Statut :** Claim - Data Sample Published
- **Description victime :** 100 Watt Plast est une entreprise industrielle basée en Égypte, avec des activités également au Liban et en Arabie saoudite, spécialisée dans la fabrication de produits électriques et plastiques.
- **Analyse :** L'acteur camillabf a publié le 29 décembre 2025 une revendication concernant 100wattplast.com, décrite comme un jeu de données de 180 000 enregistrements au format CSV, comprenant prénom, nom, email, téléphone et mot de passe. L'échantillon affiché dans le post montre un schéma de champs incluant deux valeurs de mot de passe par enregistrement : un hachage de type MD5 (32 caractères hexadécimaux) et une seconde valeur nettement plus complexe et de longueur variable, ainsi que trois champs supplémentaires non documentés (`aa`, `bb`, `already`).

  Une vingtaine d'enregistrements complets sont directement visibles dans l'échantillon, avec des noms, adresses email et numéros de téléphone égyptiens associés aux deux valeurs de mot de passe. La cohérence du schéma et le volume d'enregistrements individuels observés appuient un niveau de confiance élevé quant à l'authenticité de cette fuite, bien que le volume total de 180 000 lignes revendiqué n'ait pas pu être vérifié indépendamment au-delà de l'échantillon observé, et que la nature exacte du second champ de mot de passe (hachage alternatif ou valeur en clair) n'ait pas pu être déterminée avec certitude. L'exposition de ces données pourrait faciliter la prise de contrôle de comptes, la réutilisation de mots de passe sur d'autres services et le phishing ciblé contre les clients de l'entreprise. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone ni valeur de mot de passe issus de l'échantillon examiné.

### 31 Décembre 2025
#### 🇲🇦 Maroc - Pharmacie.ma
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** KaruHunters
- **Secteur :** Santé / E-commerce pharmaceutique
- **Site web :** pharmacie.ma
- **Statut :** Claim - Data Sample Published
- **Description victime :** Pharmacie.ma est une plateforme marocaine d'annuaire et de commerce électronique dédiée aux pharmacies. Deux sauvegardes SQL complètes, datées de septembre 2025, ont été examinées, couvrant l'ensemble du schéma applicatif de la plateforme (clients, adresses, médicaments, pharmaciens, newsletters, articles et tables associées). La structure de la table `clients` indique jusqu'à environ 27 900 comptes enregistrés (pharmaciens, médecins, personnel officinal, étudiants en pharmacie et autres utilisateurs) avec adresse email, mot de passe haché, nom, adresse professionnelle, ville, spécialité, numéros de téléphone/mobile, pays et date de naissance. Le volume et la structure des sauvegardes indiquent une exposition significative de comptes professionnels du secteur de la santé ; l'exhaustivité de l'extraction et son origine n'ont pas été confirmées de manière indépendante.

### 31 Décembre 2025
#### 🇰🇪 Kenya - Kenya Electricity Transmission Company (KETRACO)
- **Type d'incident:** Fuite de données
- **Acteur / Groupe :** LindaBF, publication sur un forum cybercriminel (RaidForums)
- **Secteur :** Énergie / Transport d'électricité (Infrastructure critique)
- **Site web :** [ketraco.co.ke](https://ketraco.co.ke)
- **Statut :** Claim - Data Sample Published
- **Description victime :** La Kenya Electricity Transmission Company (KETRACO) est une entreprise publique kényane chargée du développement, de l'exploitation et de la maintenance du réseau national de transport d'électricité haute tension.
- **Analyse :** L'acteur LindaBF a publié le 31 décembre 2025 un post intitulé « ketraco.co.ke database Kenya », le lien de téléchargement étant réservé aux membres du forum ayant répondu au fil de discussion. L'échantillon visible montre un export structuré d'un annuaire d'utilisateurs (champs USER_ID, USER_NAME, USER_PASSWORD, USER_FIRSTNAME, USER_LASTNAME, USER_EMAIL, USER_LASTLOGIN, USER_FLAGS, USER_OU, USER_DATECREATED) associé à une unité organisationnelle nommée « nl_KETRACO_Newsletter_Unit », cohérent avec une liste de comptes d'abonnés à une newsletter ou d'un service d'annuaire plutôt qu'avec des systèmes opérationnels critiques. Des noms, adresses email et horodatages de création de compte kényans d'apparence réaliste sont visibles, mais de nombreuses lignes de l'échantillon partagent une valeur de mot de passe identique, ce qui est incohérent avec des empreintes générées individuellement par utilisateur et pourrait indiquer une valeur par défaut partagée, un espace réservé, ou un échantillon partiellement fabriqué ; cette anomalie ramène le niveau de confiance d'AFRINTEL à un niveau moyen. Compte tenu du rôle de KETRACO dans l'infrastructure nationale de transport d'électricité, toute compromission confirmée, même limitée à un service de newsletter ou d'annuaire, serait préoccupante pour un opérateur d'infrastructure critique et pourrait indiquer un point d'accès plus large. AFRINTEL ne reproduit aucun nom d'utilisateur, adresse email, valeur de mot de passe ni enregistrement de l'échantillon, et n'a pas accédé au lien de téléchargement.

---

*Compilation AFRINTEL — source unique : fichiers mensuels.*
