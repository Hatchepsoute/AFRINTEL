[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# Liste des victimes africaines de cyberattaques en Juin 2025 (21 victimes)
👉🏾 [**English version available here**](./victims.md)

## Résumé du mois

Juin 2025 compte **21 incidents uniques** : **5 Ransomware**, **16 Data Leak**, **0 Access Sale**, **0 DDoS**, **0 Defacement** et **0 Operational Fraud**, dans **8 pays africains**.

> `victims_FR.md` est le fichier éditorial de contrôle. Après validation, `victims.md` est synchronisé avec les mêmes faits, classifications et valeurs structurées.

## Juin 2025

### 02 Juin 2025
#### 🇲🇦 Maroc - ANCFCC (Agence Nationale de la Conservation Foncière)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** nightspire
- **Secteur:** Gouvernement / Immobilier et Foncier.
- **Site web:** https://www.ancfcc.gov.ma/
- **Statut:** Claim - Data Sample Published
- **Description victime:** L'ANCFCC est l'organisme vital chargé de l'immatriculation foncière, du cadastre et de la cartographie au Maroc. La revendication initiale de NightSpire évoquait une fuite de 3,1 Go comprenant plus de 10 080 certificats de propriété.
  Une publication attribuée à vyngrich sur un forum cybercriminel annonce plusieurs collections présentées comme provenant de l’ANCFCC : plus de 10 000 certificats de propriété en échantillon, un ensemble sous-jacent revendiqué à plus de 10 millions de certificats, ainsi que 20 000 documents en échantillon issus d’une collection annoncée à plus de 4 millions de documents et 4 To. Les catégories revendiquées comprennent notamment des actes fonciers, des documents d’état civil, des pièces d’identité, des passeports et des documents bancaires, ainsi qu’un dossier qui concernerait de hauts responsables et des personnalités publiques. AFRINTEL ne reproduit aucune identité. AFRINTEL a par la suite obtenu et examiné des copies d'archives locales de la publication revendiquée, confirmant la présence de plusieurs milliers de fichiers PDF individuels de certificats de propriété, nommés séquentiellement (par exemple CERTIFICAT_1.pdf jusqu'à des numéros de l'ordre du millier), cohérente avec la taille de l'échantillon revendiqué, ainsi qu'un dossier distinctement nommé faisant référence à de hauts responsables et personnalités publiques ; AFRINTEL n'a ni ouvert ni analysé le contenu de ce dossier et n'en reproduit aucune identité. La proximité entre l’échantillon de plus de 10 000 certificats et les 10 080 certificats publiés par NightSpire suggère un chevauchement, une republication, une revente ou une amplification possible. La publication de juillet est conservée comme information complémentaire et n’est pas comptabilisée comme un incident distinct. L’authenticité, l’ancienneté, l’exhaustivité et l’origine technique des collections supplémentaires revendiquées restent inconnues.

### 02 Juin 2025
#### 🇲🇦 Maroc - Portail de l'Ordre des Avocats (avocatsmaroc.com / mossaada.ma)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** B4baYega
- **Secteur:** Services juridiques / Association professionnelle
- **Site web:** avocatsmaroc.com / mossaada.ma
- **Statut:** Claim - Data Sample Published
- **Description victime:** avocatsmaroc.com est un portail marocain de la profession juridique appuyant les avocats dans la gestion de leurs dossiers et procédures d'exécution ; mossaada.ma est une plateforme d'aide juridictionnelle associée.
- **Analyse:** AFRINTEL a examiné du code source applicatif et des sauvegardes de base de données SQL référençant les domaines bureau.avocatsmaroc.com et app2.mossaada.ma, diffusés par l'acteur B4baYega aux côtés d'une archive protégée par mot de passe. Les fichiers source PHP de l'application utilisent des noms de fonctions et de champs translittérés de l'arabe correspondant à une terminologie de gestion de dossiers judiciaires et de procédures d'exécution (par ex. « Tanfid »/exécution, « Khazina »/trésorerie ou caisse, « Tabligh »/notification, « Diligence », « Tribunal »), ainsi que des fonctions de recherche de clients, de modification de dossiers clients et de suivi de diligences, et plusieurs fichiers de sauvegarde SQL datés. Cela indique la compromission d'une application de gestion de dossiers juridiques utilisée par ou pour des avocats marocains, plutôt qu'un simple site vitrine. AFRINTEL n'a pas extrait ni examiné le contenu ligne par ligne des sauvegardes SQL et ne reproduit aucun nom de client, référence de dossier ni autre donnée personnelle issus de l'échantillon examiné. L'ampleur et le volume réels des enregistrements contenus dans les sauvegardes n'ont pas pu être confirmés de manière indépendante.

### 06 Juin 2025
#### 🇲🇦 Maroc - MTT EXPERTISES
- **Groupe ransomware:** incransom
- **Secteur:** Services aux entreprises
- **Site web:** https://mttexpertises.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
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
- **Type d'incident:** Ransomware
- **Description victime:** L'Ingonyama Trust Board (ITB) est une autorité administrative sud-africaine chargée de gérer environ 2,8 millions d'hectares de terres communales dans la province du KwaZulu-Natal.

### 06 Juin 2025
#### 🇲🇦 Maroc - Best Profil (bestprofil.ma)
- **Groupe ransomware:** lynx
- **Secteur:** Ressources Humaines / Recrutement / Intérim.
- **Site web:** https://bestprofil.ma
- **Statut:** Data Fully Published
- **Type d'incident:** Ransomware
- **Description victime:** Best Profil est l'un des leaders du recrutement et de l'intérim au Maroc. Le groupe Lynx décrit cet incident comme une exfiltration totale de 26 Go, désormais en libre accès sur son site de fuite après l'échec, selon ses affirmations, des négociations de rançon.
- **Analyse:** AFRINTEL a examiné un échantillon local des données divulguées, composé de documents administratifs et opérationnels internes référençant « PEGASE » (un système/outil interne), de tableurs de suivi de présence et de paie du personnel, de fichiers de vérification de factures et de détail de facturation, ainsi que d'un dossier de réclamation client pour un site industriel. La présence de manuels de systèmes internes, de données de paie et de pointage, ainsi que de correspondance administrative au niveau des sites, est cohérente avec une compromission réelle des systèmes internes plutôt qu'une simple revendication superficielle. L'exposition des données de présence, de paie et de facturation du personnel crée un risque de fraude à la paie, de compromission de messagerie professionnelle (BEC) et d'ingénierie sociale contre le personnel et les clients corporate de Best Profil. AFRINTEL ne reproduit aucun nom d'employé, nom de client ni montant financier issus de l'échantillon examiné.

### 08 Juin 2025
#### 🇩🇿 Algérie - Crédit Populaire d’Algérie (cpa-bank.dz)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** TajineSec / Tajinesec_MA
- **Secteur:** Banque / Services Financiers.
- **Site web:** https://cpa-bank.dz
- **Statut:** Claim - Unverified
- **Description victime:** Crédit Populaire d'Algérie (CPA) est l'une des principales banques publiques du pays. TajineSec affirme avoir exfiltré plus de 30 Go, comprenant des documents d'identité, des informations sur les employés et les clients, des données de comptes bancaires et de transferts d'argent, ainsi que des documents administratifs internes. Un échantillon de 500 Mo est annoncé, mais il n'est pas visible dans la preuve fournie.
- **Analyse:** La publication documente une revendication publique attribuée à TajineSec / Tajinesec_MA et décrit des données bancaires et d'identité potentiellement très sensibles. La compromission, le volume annoncé, l'attribution marocaine alléguée et la publication de l'échantillon annoncé ne sont pas vérifiés indépendamment. Le statut reste donc **Claim - Unverified**.

### 09 Juin 2025
#### 🇩🇿 Algérie - Algérie Télécom (algerietelecom.dz)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Phantom Atlas
- **Secteur:** Télécommunications / Infrastructure Internet nationale
- **Site web:** [algerietelecom.dz](https://www.algerietelecom.dz)
- **Statut:** Claim - Data Sample Published
- **Description victime:** Algérie Télécom est l'opérateur historique et principal fournisseur d'accès Internet fixe et de téléphonie fixe en Algérie, exploitant l'infrastructure réseau nationale reliant les points d'accès régionaux aux serveurs de contenu internationaux.
- **Analyse:** Phantom Atlas revendique un accès complet à la cartographie interne du réseau internet d'Algérie Télécom pour les wilayas de Tizi Ouzou, Boumerdes et Bouira, affirmant détenir des informations détaillées sur l'infrastructure critique reliant les points d'accès (BNG) aux serveurs de contenu mondiaux (FNA, GGC), ainsi que les routeurs cœur de réseau, les anneaux de distribution de contenu et la consommation de données par commune.

  Les éléments examinés montrent des interfaces d'un outil de supervision réseau de type « Network Weathermap », affichant plusieurs cartes topologiques distinctes : un schéma du projet BNG Tizi-Ouzou avec des routeurs identifiés (PE-01, PE-02, ASBR-01, ASBR-02) et des liens de peering vers Google (GGC) et Facebook (FNA) avec charges de trafic en Gbit/s ; un schéma de la boucle métropolitaine régionale nommant des dizaines de sites et communes des wilayas concernées ; et un tableau de consommation de bande passante détaillé par commune pour Tizi Ouzou, Boumerdes et Bouira. Un second message précise que l'accès a été maintenu depuis au moins le 28 mai 2025 (mention d'une coupure de connexion lors d'un test à cette date) et affirme détenir des données allant au-delà de simples cartes.

  La cohérence technique des interfaces observées (outil de supervision réseau réel, désignations d'équipements et de sites plausibles, chiffres de trafic cohérents entre les différentes vues) soutient un niveau de confiance élevé quant à l'authenticité d'un accès à un système de supervision interne d'Algérie Télécom, au moins pour les wilayas mentionnées. La divulgation de cartes réseau détaillées d'un opérateur télécom national constitue une exposition critique pouvant faciliter la cartographie ciblée de l'infrastructure en vue d'intrusions ultérieures, des attaques par déni de service ciblées sur des liens identifiés, ou une perturbation du service dans les zones concernées. AFRINTEL ne reproduit aucun détail topologique, identifiant d'équipement ni chiffre de trafic supplémentaire au-delà de ce qui est nécessaire pour qualifier la nature de l'exposition.

### 09 Juin 2025
#### 🇬🇭 Ghana - Priority Insurance Company Limited
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** 0x0day
- **Secteur:** Assurance / Services financiers
- **Site web:** priorityinsuranceghana.net
- **Statut:** Claim - Data Sample Published
- **Description victime:** Priority Insurance Company Limited est une compagnie d'assurance non-vie ghanéenne basée à Accra, agréée par la National Insurance Commission (NIC), qui exploite un réseau de plus de 30 agences à travers le pays, notamment à Accra, Kumasi, Tema, Cape Coast et Ho.
- **Analyse:** AFRINTEL a identifié la publication d'origine, intitulée « GHANA Inusrance database », publiée sur le forum cybercriminel DarkForums par le compte 0x0day le 9 juin 2025, ce qui remplace un enregistrement précédent en cours d'investigation, provisoirement placé en février 2025 sur la seule base d'une date de modification de fichier, sans publication source retrouvée. La publication affiche un échantillon JSON cohérent avec un export interne de gestion de polices d'assurance, avec des champs incluant un identifiant client, un numéro de police, un identifiant et un nom d'agence (Tema), un type de client, un nom complet, une adresse email, un numéro de téléphone, des adresses numérique/postale/de résidence, un numéro d'identification fiscale, un identifiant et un nom d'entreprise (explicitement « Priority Insurance Company Limited »), ainsi qu'un champ d'identification nationale. Cela correspond à la structure et au réseau d'agences (Accra, Kumasi, Tema, Cape Coast, Ho, Bolga) du fichier de base de données clients précédemment examiné par AFRINTEL, qui contenait 349 288 enregistrements dont environ 159 000 avec une adresse email et environ 159 000 avec un numéro d'identification nationale. La combinaison d'un compte source confirmé, d'une date de publication explicite et d'un échantillon correspondant au jeu de données précédemment examiné permet de faire passer le niveau de confiance d'en cours d'investigation à une revendication datée et attribuée. Compte tenu du volume d'enregistrements et de la combinaison de numéros d'identification nationale, de dates de naissance, de professions, de coordonnées et d'association à des polices d'assurance, l'exposition de ce jeu de données créerait un risque significatif d'usurpation d'identité, de fraude à l'assurance et de phishing ciblé visant les assurés. AFRINTEL ne reproduit aucun nom de client, numéro de téléphone, adresse, numéro d'identification nationale ni date de naissance issu des éléments examinés.

### 11 Juin 2025
#### 🇲🇺 Maurice - Currimjee Jeewanjee & Co
- **Groupe ransomware:** warlock
- **Secteur:** Conglomérat / multi-sectoriel
- **Site web:** https://www.currimjee.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** L'un des plus anciens et importants conglomérats de l'île Maurice, opérant dans les télécoms (Emtel), l'énergie, l'immobilier, le tourisme et les services financiers.

### 11 Juin 2025
#### 🇩🇿 Algérie - Banque Nationale d’Algérie (bna.dz)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Phantom Atlas
- **Secteur:** Banque / Services Financiers.
- **Site web:** https://bna.dz / https://ebanking.bna.dz
- **Statut:** Claim - Unverified
- **Description victime:** La Banque Nationale d'Algérie (BNA) est la première banque commerciale de l'État algérien. L'acteur revendique une exfiltration massive de 90 Go avec une publication partielle de 7 Go ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.
- **Analyse:** Un message Phantom Atlas antérieur, publié le 10 juin 2025 sur la chaîne Telegram de l'acteur, précise cette revendication : le groupe affirme détenir plus de 90 Go de documents couvrant la période 2016-2025, avec une diffusion annoncée en plusieurs temps (« nous commencerons par ceux de 2016 »), l'archive étant protégée par le mot de passe `phantomatlas`. Le lien de téléchargement mentionné sur DarkForums n'est plus accessible au moment de la rédaction de cette fiche ; AFRINTEL n'a donc pas pu collecter ni examiner l'archive revendiquée, et ne peut confirmer ni l'exhaustivité ni l'authenticité du contenu annoncé.

### 11 Juin 2025
#### 🇿🇦 Afrique du Sud - Carducci
- **Groupe ransomware:** warlock
- **Secteur:** Commerce de détail (Mode)
- **Site web:** http://carducci.co.za/
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Carducci est une marque de mode sud-africaine basée au Cap, fondée en 1978. Elle est spécialisée dans les vêtements pour hommes élégants, notamment les costumes, les tenues décontractées et les accessoires. La marque est réputée pour son savoir-faire et ses tissus raffinés. Carducci fait partie du groupe Seardel

### 14 Juin 2025
#### 🇪🇬 Égypte - Ministère de la Solidarité sociale
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Keymous
- **Secteur:** Gouvernement / Administration publique / Affaires sociales
- **Site web:** [moss.gov.eg](https://www.moss.gov.eg)
- **Statut:** Claim - Data Sample Published
- **Description victime:** Le Ministère de la Solidarité sociale est une administration gouvernementale égyptienne chargée notamment de politiques et services liés à la protection et à l'action sociales.
- **Analyse:** Une publication attribuée à l'acteur Keymous présente des données supposément obtenues auprès du ministère et concernant également des responsables et représentants institutionnels de plusieurs pays. La publication annonce des documents confidentiels et des informations personnelles concernant des ministres, responsables gouvernementaux et représentants institutionnels de plusieurs pays africains, arabes et asiatiques, mentionnant notamment des passeports ou pièces d'identité, noms, numéros de téléphone et adresses électroniques ; l'acteur revendique un total de 237 éléments, décrit dans la publication comme « Line and file ».

  L'échantillon CSV analysé par AFRINTEL contient 26 enregistrements répartis sur 8 colonnes : `Name`, `Phone`, `Email`, `Title / Position`, `Country`, `City`, `Passport / ID` et `Photos`. Les données couvrent notamment l'Égypte, Djibouti, le Bénin, le Burkina Faso, le Sénégal, le Maroc, le Soudan, la Turquie, les Émirats arabes unis, la Malaisie, l'Indonésie et le Koweït, ainsi que des organisations affiliées à l'OCI. Les 26 enregistrements contiennent des noms, numéros de téléphone, adresses électroniques, fonctions professionnelles et références de passeport ou de pièce d'identité, et certaines fonctions correspondent à des responsables gouvernementaux, diplomatiques ou institutionnels. La colonne `Photos` contient également la mention `Back` pour 5 enregistrements, sans image directement intégrée au fichier CSV fourni ; plusieurs valeurs de localisation sont absentes ou remplacées par un marqueur, et au moins une adresse électronique apparaît partiellement masquée.

  La combinaison d'informations d'identité, de coordonnées directes et de fonctions institutionnelles présente un risque élevé de spear phishing, usurpation d'identité, fraude documentaire et ingénierie sociale ciblée, et les fonctions professionnelles exposées pourraient permettre à un acteur de sélectionner des profils à forte valeur et de contextualiser des campagnes visant des administrations ou organisations partenaires. La publication affiche un lien de téléchargement présenté comme « Full file », mais le fichier CSV transmis à AFRINTEL ne contient que 26 enregistrements face aux 237 éléments revendiqués ; le matériel examiné doit donc être considéré comme un échantillon observé et ne permet pas de confirmer que l'intégralité du jeu de données revendiqué a été obtenue. Aucun prix n'est indiqué et les données ne sont pas présentées comme étant proposées à la vente. AFRINTEL ne reproduit aucun nom, numéro de téléphone, adresse électronique, référence de passeport/pièce d'identité ni autre donnée personnelle issus de l'échantillon examiné.

### 14 Juin 2025
#### 🇩🇿 Algérie - Ministère de la Jeunesse et des Sports (MJS) / Directions de la Jeunesse et des Sports (DJS)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** mrdump
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
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** mrdump
- **Secteur:** Défense / Sécurité nationale
- **Site web:** Non précisé (fichier interne, aucun domaine institutionnel visible)
- **Statut:** Claim - Unverified
- **Description victime:** Le Ministère de la Défense Nationale (MDN) est l'administration algérienne chargée de la défense du pays. La publication revendique l'obtention de documents internes classifiés relatifs à la logistique et à la chaîne d'approvisionnement du ministère.
- **Analyse:** L'acteur mrdump, déjà à l'origine d'une publication visant le Ministère de la Jeunesse et des Sports le 14 juin 2025, a publié le 18 juin 2025 une nouvelle revendication concernant cette fois le Ministère de la Défense Nationale, annonçant l'obtention de « documents internes classifiés » relatifs aux opérations logistiques et à la chaîne d'approvisionnement.

  Un fichier Excel intitulé « جدول اللوجستيك لوزارة الدفاع » (« Tableau logistique du ministère de la Défense ») a été transmis à AFRINTEL en lien avec cette publication. Compte tenu de la nature revendiquée du document (matériel présenté comme classifié, relatif à la défense nationale), AFRINTEL a effectué un examen structurel limité et non intrusif : le classeur est un fichier XLSX d'environ 15 Ko comprenant une feuille, 77 lignes et 14 colonnes ; environ 65 lignes remplies forment un tableau structuré répétitif, les autres lignes correspondant à des en-têtes ou à du contenu documentaire non assimilable à des enregistrements. AFRINTEL n'a ni reproduit ni extrait de noms, identifiants, lieux, quantités, informations d'approvisionnement ou autres valeurs potentiellement sensibles.

  La structure du fichier est cohérente avec un tableau administratif lié à la logistique, mais cet examen structurel ne permet pas d'établir que le document est authentique, classifié, actuel, complet ou issu du Ministère de la Défense Nationale. La revendication reste donc enregistrée comme non vérifiée. Si la provenance revendiquée était confirmée, l'exposition d'informations sur la logistique ou la chaîne d'approvisionnement militaire pourrait présenter un risque élevé pour la sécurité nationale ; il s'agit d'une évaluation conditionnelle de l'impact et non d'une confirmation de compromission.

### 18 Juin 2025
#### 🇲🇦 Maroc - Ministère de l'Éducation Nationale (men.gov.ma / massar.men.gov.ma)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** RiseAgainLuigi & B4baYega
- **Secteur:** Gouvernement / Éducation.
- **Site web:** https://men.gov.ma / massar.men.gov.ma
- **Statut:** Claim - Unverified
- **Description victime:** Le Ministère de l'Éducation Nationale du Maroc. La plateforme Massar est l'épine dorsale numérique du ministère, centralisant les notes, les inscriptions et le suivi de tous les élèves du Royaume. Les acteurs revendiquent une fuite de données et une mise en vente de plus de 6 millions de dossiers ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 19 Juin 2025
#### 🇩🇿 Algérie - Direction Générale des Douanes (DGD) / Service de contrôle des exportations et importations
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** mrdump
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
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Keymous
- **Secteur:** Sport / Administration Publique.
- **Site web:** https://frmf.ma/
- **Statut:** Claim - Data Sample Published
- **Description victime:** Fondée en 1956, la FRMF est l'organisme chargé d'organiser, de gérer et de développer le football au Maroc. Elle supervise les sélections nationales, les compétitions professionnelles et amateurs, ainsi que les ligues régionales.
- **Analyse:** AFRINTEL a identifié la publication source : un post DarkForums de l'acteur Keymous, intitulé « Football federation morocco Leak », revendiquant une base de données de joueurs et de personnel de la FRMF couvrant plus de 4 289 enregistrements nominatifs. AFRINTEL a examiné un échantillon local de documents cohérents avec les registres officiels d'enregistrement et de licence de la FRMF. L'échantillon comprend un enregistrement d'officiel d'équipe issu de FIFA Connect et une licence d'entraîneur CAF Pro, contenant chacun un nom complet, une date de naissance, le sexe, la nationalité, une adresse personnelle, un numéro de téléphone, un identifiant FIFA ou de licence, une date de validité et une photographie, ainsi qu'un formulaire de demande d'enregistrement de club mentionnant le nom complet du titulaire de licence, sa date et son lieu de naissance, son numéro de CIN/passeport, sa nationalité et son club d'affiliation. Deux extraits de tableur, structurés comme un registre d'officiels/membres de football (identifiant d'enregistrement, statut, nom, nationalité, date et année de naissance, région, ville, adresse, code postal, téléphone, email, club et code d'insigne/autorisation), étaient également présents, couvrant au total une trentaine d'enregistrements, et correspondent à la structure de champs décrite dans le post de Keymous. Ceci est cohérent avec l'exposition de parties de la base officielle et de licence de la FRMF plutôt qu'avec de simples documents administratifs génériques. Au moins un enregistrement examiné concerne une personne dont la date de naissance indique qu'elle était mineure au moment de l'enregistrement. AFRINTEL ne reproduit aucun nom, adresse, numéro d'identification, coordonnée ni photographie issus de l'échantillon examiné. L'ampleur totale, l'exhaustivité et la validité actuelle de la base de données sous-jacente n'ont pas pu être confirmées au-delà de l'échantillon limité disponible.

### 20 Juin 2025
#### 🇲🇦 Maroc - INWI (inwi.ma)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Evil_BYTE_Officiel
- **Secteur:** Télécommunications.
- **Site web:** https://inwi.ma
- **Statut:** Claim - Data Sample Published
- **Description victime:** INWI est l'un des trois principaux opérateurs de télécommunications au Maroc, fournissant des services de téléphonie mobile, fixe et d'internet (ADSL/Fibre). L'acteur a publié un échantillon de données sensibles incluant des PII (nom, CIN), des données de contact et des hashs de mots de passe (bcrypt).

### 20 Juin 2025
#### 🇹🇳 Tunisie - Ministère de la Défense Nationale / Forces armées
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** mrdump
- **Secteur:** Défense / Sécurité nationale
- **Site web:** Non précisé
- **Statut:** Claim - Data Sample Published
- **Description victime:** Le Ministère tunisien de la Défense Nationale est l'administration gouvernementale chargée de la défense nationale et des forces armées.
- **Analyse:** Une publication datée du 20 juin 2025, attribuée à mrdump, revendique un accès réussi à plusieurs systèmes du Ministère tunisien de la Défense Nationale, plus précisément à sa division des forces armées. La publication affirme qu'un dépôt souterrain d'armes aurait été découvert au mont Chaâmbi, dans le gouvernorat de Kasserine, et fait référence à des images thermiques, des plans d'ingénierie et des informations relatives aux armes et munitions entreposées. Une archive ZIP associée a été transmise à AFRINTEL ; un examen structurel sans lecture du contenu a identifié 10 éléments (six images PNG, un classeur XLSX, un PDF et une image JPG), pour environ 6,2 Mo compressés et 6,3 Mo décompressés. AFRINTEL n'a pas ouvert ni reproduit les fichiers, le matériel étant présenté comme militaire et potentiellement sensible sur le plan opérationnel. La structure de l'archive ne permet pas d'établir indépendamment l'authenticité, la provenance, la classification ou l'exhaustivité du matériel ; l'accès revendiqué reste non vérifié.

### 26 Juin 2025
#### 🇩🇿 Algérie - Ministère des Transports
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** KickingPigs
- **Secteur:** Gouvernement / Transports
- **Site web:** Non précisé
- **Statut:** Claim - Data Sample Published
- **Description victime:** Le ministère algérien des Transports est l'administration publique chargée de la politique nationale des transports et des services administratifs associés.
- **Analyse:** Une publication sur un forum, datée du 26 juin 2025 et attribuée à KickingPigs, présente une fuite supposée du ministère algérien des Transports. Le post énumère des données d'immatriculation et d'administration des transports, notamment des noms, numéros d'identification nationale, noms des parents, numéros d'immatriculation d'entreprises, informations sur les véhicules et leurs immatriculations, documents de permis de conduire et fichiers Excel internes. L'échantillon visible contient des enregistrements structurés de véhicules et des champs de données personnelles sensibles ; AFRINTEL ne reproduit aucun enregistrement ni identifiant. L'authenticité, l'exhaustivité et l'origine technique du jeu de données n'ont pas pu être confirmées indépendamment.

### 29 Juin 2025
#### 🇩🇯 Djibouti - Ambassade de Djibouti au Maroc
- **Type d'incident:** Data Leak

- **Acteur / Groupe:** MdHackersArmy
- **Secteur:** Gouvernement / Diplomatie
- **Statut:** Claim - Unverified
- **Site web:** Non précisé

- **Description :**
  L'ambassade de Djibouti au Maroc est la représentation diplomatique de Djibouti accréditée auprès du Royaume du Maroc.

- **Analyse:**
  Une publication intitulée « Leak db of the Embassy of Djibouti in Morocco » a été publiée le 29 juin 2025 sur le forum cybercriminel DarkForums par le compte Doxeur23azi, qui attribue la revendication à MdHackersArmy. La publication se limite à un lien de téléchargement externe et ne décrit ni le type de données, ni la structure des champs, ni le volume d'enregistrements, ni la sensibilité de la base de données annoncée ; aucun échantillon n'est visible. AFRINTEL n'a pas accédé au lien externe. Les données concernées, la population affectée et l'origine technique de la revendication restent inconnues à ce stade.
## ✍🏿 Auteur
*Adama ASSIONGBON*  
*Consultant SOC & Cyber Threat Intelligence*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)

---
*AFRINTEL - Initiative ouverte de veille CTI sur l’Afrique*
