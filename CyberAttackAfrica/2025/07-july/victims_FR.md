[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# Liste des victimes africaines de cyberattaques en Juillet 2025 (20 victimes)
👉🏾 [**English version available here**](./victims.md)
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
## ✍🏿 Auteur
*Adama ASSIONGBON*  
*Consultant SOC & Cyber Threat Intelligence*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)

---
*AFRINTEL - Initiative ouverte de veille CTI sur l’Afrique*

