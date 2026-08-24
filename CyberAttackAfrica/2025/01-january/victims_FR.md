[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# Victimes africaines - Janvier 2025

👉🏾 [**English version available here**](./victims.md)

## Synthèse mensuelle

**19 cyberincidents documentés** sous AFRINTEL Taxonomy v2 : Ransomware 16, Data Leak 2, Account Takeover 1.

> Les liens de sources sont ajoutés aux incidents complémentaires identifiés via des recherches publiques pour combler le corpus. Ils ne sont pas imposés rétrospectivement aux fiches historiques issues des observations AFRINTEL, notamment Dark Web.

## Janvier 2025

### 06 Janvier 2025
#### 🇰🇪 Kenya - Molars Dental Practice
- **Groupe ransomware:** ransomhub
- **Secteur:** Santé (Dentaire)
- **Site web:** https://molars.co.ke
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Analyse:** AFRINTEL a examiné le classeur fourni et huit fichiers de preuve supplémentaires. Le classeur contient des éléments de structure salariale et des feuilles distinctes pour les médecins, la comptabilité, les ressources humaines, les opérations et plusieurs fonctions de support. Les preuves comprennent également une capture de paiement bancaire et des documents cohérents avec l’administration du personnel ou de la paie. L’échantillon soutient une exposition potentielle des rémunérations, des structures départementales, des opérations internes et d’informations liées au traitement financier. Le volume revendiqué de 19 Go, le vecteur d’accès et l’exhaustivité des données restent non vérifiés. AFRINTEL ne reproduit aucun nom, salaire, coordonnée bancaire ni autre donnée personnelle.
- **Description victime:** Molars est un réseau de cliniques dentaires de premier plan basé à Nairobi, fournissant des soins spécialisés allant de l'orthodontie à la chirurgie dentaire pour une clientèle locale et internationale. L'acteur revendique l'exfiltration de 19 Go de données ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 09 Janvier 2025
#### 🇪🇬 Égypte - General Authority for Government Services
- **Groupe ransomware:** funksec
- **Secteur:** Administrations publiques/ Finances / Marchés Publics.
- **Site web:** gags.gov.eg
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
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
- **Type d'incident:** Ransomware
- **Description victime:** **Pick n Pay Group Ltd** est le deuxième plus grand détaillant de produits alimentaires en Afrique du Sud.

### 11 Janvier 2025
#### 🇲🇦 Maroc - SEOCOM Marrakech (seocommarrakech.com)
- **Groupe ransomware:** funksec
- **Secteur:** Technologies / Marketing Digital / SEO.
- **Site web:** seocommarrakech.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** EOCOM est une agence marocaine fournissant des services de SEO (Search Engine Optimization), de gestion de campagnes publicitaires (SEA) et de développement web pour des entreprises locales et internationales.

### 14 Janvier 2025
#### 🇳🇬 Nigeria - INTELS Nigeria Limited (intelservice.com)
- **Groupe ransomware:** ransomhub
- **Secteur:** Logistique Pétrolière et Gazière / Services Portuaires.
- **Site web:** intelservices.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Intels est un pilier de l'économie nigériane, gérant 90 % des activités de soutien à l'exploration pétrolière offshore. Le groupe affirme avoir exfiltré environ 1,5 To de données sensibles ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 14 Janvier 2025
#### 🇪🇬 Égypte - Sharm Reef Hotel
- **Groupe ransomware:** spacebears
- **Secteur:** Hôtellerie / Tourisme.
- **Site web:** sharmreefhotel.com / sharmelsheikh.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Le Sharm Reef Hotel est un complexe hôtelier 4 étoiles situé sur le plateau d'Om El Seid à Charm el-Cheikh en Egypte.

### 15 Janvier 2025
#### 🇪🇬 Égypte - Misr Technology Services (MTS / mts.gov.eg)
- **Groupe ransomware:** funksec
- **Secteur:** Administrations publiques
- **Site web:** mts.gov.eg
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** Misr Technology Services (MTS) est l'entité gouvernementale égyptienne responsable du développement et de la gestion de la plateforme nationale de facilitation du commerce, notamment le système Nafeza.
- **Analyse:** AFRINTEL a examiné un ensemble local de captures d'écran et de documents PDF générés par les systèmes internes du secteur du Transport Maritime et de la Logistique, notamment l'Egyptian Maritime Data Bank, cohérents avec la revendication du cybercriminel funksec. Le matériel examiné inclut une demande individuelle de permis nommant un demandeur, une agence maritime affiliée et une date de dépôt ; un rapport comparatif de trafic portuaire listant des statistiques d'escales par port pour 2023 et 2024 ; une liste de projets et opportunités d'investissement portuaire ; ainsi que des rapports détaillés de recouvrement sectoriel couvrant plusieurs périodes entre janvier et avril 2024, listant des noms de clients, types d'opérations, numéros de référence et montants encaissés via le canal point de vente du secteur. Deux des documents examinés portent un horodatage d'impression système daté du 14 et du 15 janvier 2025, cohérent avec la date de publication de la revendication. La présence de rapports générés en interne, datés et nommant des demandeurs et clients, combinée à l'en-tête propre de la plateforme et aux métadonnées d'impression, soutient une évaluation à confiance élevée d'un accès réel aux systèmes de reporting internes de MTS. Compte tenu du rôle de MTS dans la gestion de la plateforme nationale égyptienne de facilitation du commerce, notamment le système Nafeza, cet incident présente un risque pour le personnel des agences maritimes, les données financières clients et la confidentialité des opérations nationales de facilitation du commerce. AFRINTEL ne reproduit aucun nom de demandeur, nom de client, donnée financière ni référence documentaire issue du matériel examiné.

### 16 Janvier 2025
#### 🇿🇦 Afrique du Sud - North-West University (NWU)
- **Acteur / Groupe:** SevenZeroDay404
- **Secteur:** Éducation / Université
- **Site web:** [nwu.ac.za](https://www.nwu.ac.za/)
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** North-West University (NWU) est une université sud-africaine d'enseignement supérieur. Le domaine `nwu.ac.za` et l'identité visuelle utilisés dans la publication de l'acteur correspondent à cette université, qui est explicitement présentée comme la victime de la revendication.
- **Analyse:** Le 16 janvier 2025, SevenZeroDay404 a publié sur un forum underground une entrée intitulée **« 29K NWU Student Database »**, accompagnée du logo de North-West University et d'un ensemble de données présenté comme une base d'étudiants. L'acteur revendique environ **29 000 enregistrements**. Le fichier fourni contient des noms, des résultats académiques sous forme de GPA, des cursus universitaires et des années d'études. L'examen du contenu identifie **2 893 occurrences de valeurs de GPA structurées**, sans permettre de les assimiler automatiquement à 2 893 étudiants distincts. Le volume de 29 000 enregistrements annoncé ne peut donc pas être validé à partir de cet échantillon. L'attribution du jeu de données à `nwu.ac.za` reste incertaine : aucun marqueur explicite tel que le domaine `nwu.ac.za`, une référence à l'Afrique du Sud ou à un campus de North-West University n'a été identifié dans les données fournies. La nomenclature de plusieurs formations et l'utilisation d'un système de notation sur 4.00 présentent également des similitudes avec une autre université utilisant l'acronyme NWU. Ces éléments ne permettent pas de réattribuer la revendication, mais empêchent de confirmer que l'échantillon provient effectivement des systèmes de North-West University en Afrique du Sud. Les éléments disponibles établissent donc **North-West University en Afrique du Sud comme victime revendiquée par SevenZeroDay404**, sans confirmer indépendamment l'origine du jeu de données, l'exhaustivité des 29 000 enregistrements annoncés ni une compromission effective des systèmes de l'université. Si les données sont authentiques, leur exposition pourrait faciliter des campagnes de phishing ciblé et des tentatives d'usurpation d'identité visant des étudiants ou anciens étudiants.

### 21 Janvier 2025
#### 🇩🇿 Algérie - Centre Universitaire de Barika (cu-barika.dz)
- **Groupe ransomware:** funksec
- **Secteur:** Éducation / Enseignement Supérieur / Recherche.
- **Site web:** cu-barika.dz
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Le Centre Universitaire de Barika (Ahmed Ben Abderrezak El Hamouda) est un pôle d'enseignement supérieur situé dans la wilaya de Batna, proposant des formations en sciences technologiques, droit, et sciences humaines.

### 21 Janvier 2025
#### 🇩🇿 Algérie - Clinique Inaya (inayaclinic.org)
- **Groupe ransomware:** spacebears
- **Secteur:** Santé
- **Site web:** inayaclinic.org
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** La Clinique Inaya est une structure médicale pluridisciplinaire en Algérie, réputée pour ses pôles d'excellence en cardiologie, chirurgie cardiovasculaire et gynécologie-obstétrique.

### 24 Janvier 2025
#### 🇳🇬 Nigeria - Lower Niger River Basin Development Authority (LNRBDA)
- **Groupe ransomware:** GDLockerSec
- **Secteur:** Administrations publiques / Ressources en Eau / Agriculture.
- **Site web:** lnrbda.gov.ng
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Description victime:** La LNRBDA est une agence stratégique sous la tutelle du ministère fédéral des Ressources en Eau du Nigeria. Elle gère des projets de barrages, d'irrigation, d'approvisionnement en eau potable et de développement rural.
- **Analyse:** AFRINTEL a examiné un échantillon local de fichiers cohérents avec la revendication du cybercriminel GDLockerSec, comprenant des exports bruts de base de données du backend applicatif de l'agence ainsi qu'un fichier de base de données de sessions. Les tables examinées incluent une table d'informations candidats (66 enregistrements) avec nom complet, date de naissance, zone d'administration locale (LGA), téléphone, email, nom/email/téléphone/adresse d'un répondant/référent, adresse de contact, institution et un champ libre « motif de candidature », cohérent avec un formulaire de candidature à un programme d'insertion professionnelle pour diplômés ; une table utilisateurs stockant des emails accompagnés de mots de passe en clair ; une table d'utilisateurs administratifs contenant des identifiants de compte de niveau administrateur (« AD ») hachés ; ainsi qu'une table de validation associant des codes à usage unique à des numéros de téléphone. Une table d'actualités distincte contient du contenu public courant et n'est pas sensible. La combinaison d'un export structuré multi-tables réellement issu du backend applicatif, d'une base de données de sessions associée, et de la présence de mots de passe utilisateurs en clair et d'identifiants administrateur, soutient une évaluation à très haute confiance d'une compromission réelle et profonde des systèmes de l'agence, plutôt qu'une simple revendication. Compte tenu du statut du LNRBDA en tant qu'agence fédérale nigériane, l'exposition d'identifiants en clair, de comptes administrateur, de données personnelles de candidats et de codes à usage unique liés à des numéros de téléphone crée un risque sévère de prise de contrôle de comptes, de compromission latérale supplémentaire des systèmes gouvernementaux, ainsi que de fraude à l'identité ou de phishing ciblé visant les candidats et leurs référents. AFRINTEL ne reproduit aucun nom, date de naissance, adresse, numéro de téléphone, email, mot de passe ni code issu de l'échantillon examiné.

### 24 Janvier 2025
#### 🇲🇦 Maroc - Université Sidi Mohamed Ben Abdellah (www.usmba.ac.ma)
- **Groupe ransomware:** GDLockerSec
- **Secteur:** Éducation / Enseignement Supérieur / Recherche.
- **Site web:** usmba.ac.ma
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 2
- **Description victime:** L'USMBA est une université multidisciplinaire comprenant de nombreux établissements (Facultés de Médecine, des Sciences, des Lettres, ENCG, ENSA, etc.).
- **Analyse:** AFRINTEL a examiné un échantillon local de matériel cohérent avec la revendication du cybercriminel GDLockerSec, constitué de captures affichant une base de données interne structurée des laboratoires et équipes de recherche, restituée via l'outil de visualisation CSV propre à l'acteur. Les enregistrements examinés listent des unités et départements de recherche cohérents avec l'École Normale Supérieure de Fès, rattachée à l'USMBA, ainsi que leurs thématiques de recherche déclarées et projets en cours (couvrant des domaines tels que la chimie de la matière condensée, l'écologie fonctionnelle, le génie mécanique, l'intelligence artificielle et les réseaux de neurones, le traitement automatique du langage, l'entreposage de données et le traitement d'images). Des personnes nommément associées à chaque unité de recherche figurent dans les données sous-jacentes mais ont été caviardées dans le matériel examiné par AFRINTEL. La cohérence entre les unités de recherche listées, leurs thématiques et la structure académique connue de l'USMBA soutient une évaluation à confiance élevée selon laquelle le matériel reflète une base de données interne réelle d'administration de la recherche plutôt qu'un échantillon fabriqué. Le jeu de données exposé concerne principalement l'organisation institutionnelle de la recherche et son personnel plutôt que des dossiers étudiants ou financiers, créant un risque modéré de phishing ciblé et d'usurpation d'identité visant des chercheurs et directeurs de laboratoire nommément identifiés. AFRINTEL ne reproduit aucun nom, identifiant de laboratoire ni détail de projet de recherche au-delà de ce qui est nécessaire pour caractériser la nature de l'exposition.

### 26 Janvier 2025
#### 🇳🇬 Nigeria - Achievers Journal of Scientific Research
- **Groupe ransomware:** funksec
- **Secteur:** Éducation / Recherche Scientifique / Publication Académique.
- **Site web:** achieverssciencejournal.org
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
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
- **Type d'incident:** Ransomware
- **Description victime:** La FGSE (Faculty of Graduate Studies for Education) est l'une des institutions de recherche les plus anciennes et les plus respectées d'Égypte.

### 27 Janvier 2025
#### 🇺🇬 Ouganda - QED (qed.co.ug)
- **Groupe ransomware:** funksec
- **Secteur:** Services de Conseil / SMS en masse et messagerie broadcast
- **Site web:** qed.co.ug
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
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
- **Type d'incident:** Ransomware
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
- **Type d'incident:** Ransomware
- **Description victime:** Zetech University est une institution d'enseignement supérieur de premier plan au Kenya.

### 31 Janvier 2025 - date rapportée
#### Kenya - Business Registration Service (BRS)
- **Acteur / Groupe:** Unknown
- **Secteur:** Government / Administration
- **Site web:** https://brs.go.ke/
- **Date de l'incident:** Nuit du 31 janvier 2025 - date rapportée, présentée publiquement comme probable
- **Date de publication initiale:** 2 février 2025
- **Statut:** Government Confirmed
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Description victime:** Le Business Registration Service du Kenya administre le registre national des sociétés et entreprises, comprenant notamment des informations sur les sociétés, administrateurs, actionnaires et bénéficiaires effectifs.
- **Analyse:** Le 2 février 2025, le Business Registration Service (BRS) a indiqué avoir ouvert une enquête après des signalements de violation potentielle affectant le registre des sociétés. Les informations publiques situaient alors l'attaque dans la nuit du 31 janvier 2025, en la présentant comme une date probable plutôt que comme une date techniquement établie. Le 6 février, le ministère kényan de l'Information, des Communications et de l'Économie numérique a confirmé qu'une violation de données avait eu lieu et qu'une publication non autorisée d'informations avait été supprimée. Les systèmes et bases de données du BRS ont ensuite été annoncés comme sécurisés. Le vecteur d'accès, l'acteur et le périmètre complet des données affectées ne sont pas publiquement établis.
- **Type de source:** Déclarations gouvernementales rapportées par des médias publics
- **Sources publiques:** [The Star - BRS statement](https://www.the-star.co.ke/news/realtime/2025-02-02-business-registration-service-assures-of-data-security-amid-alleged-breach) | [The Star - ICT Ministry update](https://www.the-star.co.ke/news/2025-02-06-kabogo-weve-addressed-data-breach-at-business-registration-service)

---

### 31 Janvier 2025
#### Kenya - Kenya Broadcasting Corporation (KBC)
- **Acteur / Groupe:** Unknown
- **Secteur:** Media / Entertainment
- **Site web:** https://www.kbc.co.ke/
- **Date de l'incident:** 31 janvier 2025 - date rapportée par Pulse Kenya; la compromission du compte a été confirmée par KBC
- **Date de publication initiale:** 1 février 2025
- **Statut:** Victim Confirmed
- **Type d'incident:** Account Takeover
- **Sous-type:** Compromised X account / cryptocurrency scam
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Type de source:** Victim Confirmation + Public Media
- **Analyse:** Pulse Kenya a rapporté le 1er février 2025 que des attaquants avaient pris le contrôle du compte X officiel de KBC le vendredi 31 janvier. KBC a confirmé que le compte `KBCChannel1` avait été compromis et travaillait à en restaurer l'accès. Le compte avait été renommé "DeepSeek AI" et utilisé pour diffuser du contenu lié à des arnaques aux cryptomonnaies. La date de publication publique est donc le 1er février, tandis que l'incident est classé au 31 janvier sur la base de la chronologie rapportée. Les éléments disponibles n'établissent ni une compromission plus large du système d'information de KBC ni l'identité technique de l'acteur.
- **Sources:** [Pulse Kenya - KBC confirme la compromission de son compte X](https://www.pulse.co.ke/story/kbcs-x-account-hacked-and-name-changed-to-deepseek-ai-2025020111532480629)
