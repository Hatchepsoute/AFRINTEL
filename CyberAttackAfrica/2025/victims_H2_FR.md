# AFRINTEL - Victimes africaines - S2 2025

**114 cyberincidents documentés sous AFRINTEL**

> **Lecture des dates :** `Date de l'incident` indique quand l'événement s'est produit ou a été détecté selon les éléments disponibles. `Date de publication initiale` indique quand l'incident a été rendu public, revendiqué ou communiqué pour la première fois. Ces deux dates peuvent appartenir à des mois différents.

## Juillet 2025

### 01 Juillet 2025
#### 🇳🇬 Nigeria - Chartered Institute of Bankers of Nigeria (CIBN)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Hepd
- **Secteur:** Services Financiers / Organisme de Régulation Professionnelle.
- **Site web:** https://cibng.org
- **Statut:** Claim - Data Sample Published
- **Description victime:** Institution faîtière de la profession bancaire au Nigeria, responsable de l'accréditation et de l'éthique des banquiers, incluant des membres de la Banque Centrale (CBN). L'acteur affirme avoir publié sur le deep web une base de données incluant des informations sensibles sur l'élite bancaire du pays. AFRINTEL a examiné structurellement l'archive CIBN fournie : 472 fichiers et environ 18 Mo, comprenant des adresses de membres, des coordonnées bancaires, des informations d'emploi, des qualifications, des documents, des wallets, des tables liées aux connexions, des listes de personnel, ainsi que des exports de bases éducatives et fintech et des éléments de journalisation. L'archive contient également des fichiers correspondant à des enregistrements de membres et d'utilisateurs. AFRINTEL ne reproduit aucune donnée personnelle, aucun identifiant, jeton ou document. L'archive étaye une publication substantielle de données, mais son authenticité, son exhaustivité et son rattachement direct à CIBN n'ont pas été vérifiés indépendamment.

### 03 Juillet 2025
#### 🇩🇿 Algérie - Algérie Poste / ECCP
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** sanji_shi5
- **Secteur:** Services postaux / Services financiers
- **Site web:** [poste.dz](https://www.poste.dz)
- **Date de publication de la source :** 3 juillet 2025
- **Statut:** Claim - Data Sample Published
- **Description victime:** Algérie Poste exploite le service ECCP, qui permet aux utilisateurs algériens de consulter le solde de leur compte postal et d'effectuer des achats en ligne. Le post de forum fourni affiche un échantillon présenté sous forme d'identifiants de comptes et de valeurs ressemblant à des mots de passe associés à ECCP/Algérie Poste. Aucun identifiant n'est reproduit ni validé, et le jeu de données sous-jacent n'a pas été collecté.
- **Analyse:** L'échantillon observé suggère une exposition potentielle de données d'accès à un service postal et financier public. Si elles étaient valides, ces données pourraient permettre une prise de contrôle de comptes, des fraudes et des campagnes de phishing ciblées. Le post identifie sanji_shi5 comme compte source, ce qui ne confirme pas indépendamment la compromission, la provenance du jeu de données ni la validité des valeurs affichées.

### 08 Juillet 2025
#### 🇿🇦 Afrique du Sud - MAFATE BUSINESS ENTERPRISE
- **Groupe ransomware:** d4rk4rmy
- **Secteur:** Fournitures Industrielles / Services à l'Exploitation Minière.
- **Site web:** https://mafate.co.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Mafate Business Enterprise est un fournisseur de services industriels établi à Middelburg (Mpumalanga), au cœur de la région minière sud-africaine.

### 09 Juillet 2025
#### 🇲🇦 Maroc - Fédération Nationale du Bâtiment et des Travaux Publics (FNBTP)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Evil_BYTE_Officiel
- **Secteur:** Bâtiment / Travaux publics / Organisation professionnelle
- **Site web:** [fnbtp.ma](https://www.fnbtp.ma)
- **Statut:** Data Fully Published
- **Description victime:** La Fédération Nationale du Bâtiment et des Travaux Publics (FNBTP) est une organisation professionnelle représentant les entreprises marocaines du secteur du bâtiment et des travaux publics. Le 9 juillet 2025, l'acteur Evil_BYTE_Officiel a publié sur un forum underground une base de données attribuée à la FNBTP, en indiquant la mettre gratuitement à disposition.
- **Analyse:** La publication expose une table nommée `societe` contenant des informations relatives à des entreprises du secteur du BTP. Les champs annoncés dans la publication sont : `Id`, `nb_national`, `nb_regional`, `ENTREPRISE`, `secteur`, `adher`, `MONTANT_COTISATION`, `Responsable`, `Adress`, `Téléphone`, `Fax`, `GSM`, `VILLE` et `E-MAIL`.

  Le fichier CSV analysé par AFRINTEL contient 180 lignes et 14 colonnes. Les données observées comprennent des noms d'entreprises, des références internes, des informations d'adhésion, des noms de responsables, des adresses, des numéros de téléphone, fax et mobiles, des villes et des adresses électroniques professionnelles.

  Parmi les 179 lignes structurées comme des fiches d'entreprises, 166 comportent une ville, principalement Rabat, Salé, Témara et Khémisset. 146 contiennent un nom de responsable, 145 un numéro de téléphone, 139 un fax, 111 un numéro mobile et 81 au moins une adresse électronique. Certaines fiches regroupent plusieurs coordonnées pour une même entreprise.

  Une anomalie est présente dans le fichier fourni. La première ligne contient des valeurs qui ne correspondent pas à la structure métier observée dans le reste de la base. Les enregistrements suivants, notamment ceux visibles dans le post du forum, correspondent en revanche à la structure annoncée par l'acteur.

  Ces données permettent de cartographier des entreprises du secteur du BTP et d'identifier directement leurs responsables et moyens de contact. Elles peuvent être exploitées pour préparer des campagnes de spear phishing, des tentatives d'usurpation d'identité ou des scénarios d'ingénierie sociale ciblant des entreprises et leurs interlocuteurs.

  Les données sont publiées gratuitement par l'acteur. Aucun prix ni demande de rançon n'est visible. La publication contient directement des enregistrements de la base et le fichier analysé confirme la présence de données structurées. Il ne s'agit donc pas uniquement d'une annonce sans données associées. AFRINTEL ne reproduit aucun nom d'entreprise, nom de contact ni coordonnée issus de l'échantillon examiné.

### 10 Juillet 2025
#### Tunisie - University network / Centre Al-Khwarizmi
- **Acteur / Groupe:** Unknown
- **Secteur:** Education / University
- **Site web:** University network / Centre Al-Khwarizmi
- **Date de l'incident:** Au plus tard le 10 juillet 2025 - date exacte de début non communiquée publiquement
- **Date de publication initiale:** 10 juillet 2025
- **Statut:** Attempted - Outcome Unknown
- **Type d'incident:** System Intrusion
- **Sous-type:** Attempted attack against university-network infrastructure
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Type de source:** Institutional Statement + Public Media
- **Analyse:** Le Centre Al-Khwarizmi et les autorités tunisiennes ont signalé une tentative de cyberattaque visant les infrastructures et les données du réseau universitaire. La source disponible ne confirme pas une fuite de données réussie. AFRINTEL suit donc cette tentative séparément des six types d'incidents principaux.
- **Sources:** [Source](https://www.tunisienumerique.com/cyberattaque-ciblant-les-universites-tunisiennes-mesures-durgence-et-renforcement-de-la-securite/)

### 13 Juillet 2025
#### 🇹🇿 Tanzanie - Twaweza
- **Groupe ransomware:** nightspire
- **Secteur:** ONG (Éducation & Gouvernance)
- **Site web:** https://twaweza.org
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Twaweza East Africa est une organisation panafricaine de premier plan, basée en Tanzanie (avec des bureaux au Kenya et en Ouganda).

### 14 Juillet 2025
#### 🇲🇦 Maroc - IWACLUB (iwaclub.ma)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Keymous
- **Secteur:** Télécommunications / Distribution & Retail.
- **Site web:** https://iwaclub.ma
- **Statut:** Claim - Unverified
- **Description victime:** IWACLUB est l'application professionnelle dédiée au réseau de revendeurs de la société IWACO, l'un des plus importants distributeurs de solutions de télécommunications (notamment l'opérateur inwi) et de produits technologiques au Maroc.

### 14 Juillet 2025
#### 🇩🇿 Algérie - Ministère de l'Énergie, des Mines et des Énergies Renouvelables / SARL SOPRETA
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Phantom Atlas
- **Secteur:** Gouvernement / Énergie et mines ; tiers cité : industrie chimique / étanchéité du bâtiment
- **Site web:** Non précisé pour le ministère ; SOPRETA n'a pas de site officiel identifié
- **Statut:** Claim - Data Sample Published
- **Description victime:** Le Ministère de l'Énergie, des Mines et des Énergies Renouvelables est l'autorité algérienne délivrant les autorisations d'acquisition de matières et produits chimiques dangereux. SARL SOPRETA (Société des Produits d'Étanchéité Algériens), basée à Ain El Arbaa, wilaya d'Ain Témouchent, est une entreprise citée nommément dans le document divulgué.
- **Analyse:** Phantom Atlas a publié le 14 juillet 2025 une accusation visant le ministre Mohamed Arkab, affirmant que le ministère aurait délivré, en mars 2025, une autorisation d'importation de plus de 10 tonnes de substances chimiques dangereuses à une société qualifiée de « pratiquement inconnue, n'apparaissant dans aucun registre industriel connu », en l'absence de tout contrôle ou de rapport environnemental transparent, insinuant une opération aux objectifs troubles.

  AFRINTEL a examiné les documents joints à la publication : l'autorisation n°1000 du 06 mars 2025 délivrée par le ministère à SARL SOPRETA, la liste annexée des matières autorisées (acide chlorhydrique anhydre, nonylphénol éthoxylé sous les désignations commerciales Indulin W-5 et Indulin AA-83, jusqu'à 10 et 8 tonnes respectivement), ainsi qu'une facture proforma de la société belge MBM International SA (Bruxelles) adressée à SOPRETA pour 6 531,60 kg d'Indulin W5 et 2 517,30 kg d'Indulin AA-83, pour un total de 43 257,54 €, avec livraison au port d'Oran. Les trois documents sont cohérents entre eux (même numéro d'autorisation, même adresse d'entreprise, mêmes désignations commerciales de produits).

  Contrairement à l'insinuation de Phantom Atlas, AFRINTEL a identifié SARL SOPRETA (Société des Produits d'Étanchéité Algériens) dans plusieurs annuaires d'entreprises algériennes publics, à l'adresse exacte mentionnée dans l'autorisation ; il s'agit d'une société établie spécialisée dans l'étanchéité du bâtiment et la fabrication de produits chimiques inorganiques de base, notamment des produits bitumineux. Les produits « Indulin » sont des émulsifiants à base de lignine commercialisés pour la fabrication d'émulsions bitumineuses et de produits d'étanchéité routière, ce qui correspond directement à l'activité déclarée de SOPRETA plutôt qu'à un usage détourné ou non identifié. La procédure d'autorisation elle-même (déclaration mensuelle, conformité à la réglementation sur les produits chimiques dangereux, contrôle par la direction de l'énergie et des mines de la wilaya, validité limitée à un an) correspond à un dispositif réglementaire existant, ce qui contredit l'affirmation d'une « absence de tout contrôle effectif ».

  AFRINTEL considère donc que le document divulgué est probablement authentique et cohérent avec une importation industrielle légitime déclarée, mais que le cadrage accusatoire de Phantom Atlas (société « inconnue », absence de contrôle, objectifs opaques) n'est pas corroboré par les informations publiques disponibles sur SOPRETA. Cette fuite constitue néanmoins une divulgation non autorisée d'un document administratif interne du ministère ainsi que de données commerciales d'une entreprise tierce (coordonnées bancaires du fournisseur belge, détails contractuels). AFRINTEL ne reproduit aucune donnée bancaire, ni aucune information susceptible d'identifier des personnes physiques associées à ce dossier.

### 14 Juillet 2025
#### 🇰🇪 Kenya - ICT Authority (icta.go.ke)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Unknown
- **Secteur:** Gouvernement / Infrastructure numérique
- **Site web:** [icta.go.ke](http://icta.go.ke)
- **Statut:** Claim - Data Sample Published
- **Description victime:** L'ICT Authority du Kenya est une institution publique chargée de coordonner et de soutenir les infrastructures et services gouvernementaux liés aux technologies de l'information et de la communication.
- **Analyse:** AFRINTEL a examiné l'export CSV fourni sans reproduire de données personnelles. Le fichier contient 1 697 lignes de données et des champs relatifs au nom affiché, au téléphone, à l'adresse email, à l'identifiant, au contact mobile, au nom, à des champs d'adresse, aux références utilisateurs et aux liens web. La structure est cohérente avec un export d'annuaire organisationnel contenant des contacts de l'ICT Authority, du secteur public kényan et de prestataires technologiques associés. Les métadonnées du fichier situent la preuve au 14 juillet 2025 ; cette date est traitée comme date de preuve/découverte et non comme une date confirmée de publication ou d'intrusion. Le matériel disponible n'identifie ni l'acteur, ni le forum, ni la méthode d'accès, ni l'étendue complète du jeu de données. L'exposition de coordonnées professionnelles et d'informations organisationnelles peut faciliter le phishing ciblé, l'usurpation et l'ingénierie sociale contre des acteurs publics et technologiques kényans. AFRINTEL classe donc le cas comme une revendication de fuite avec échantillon publié et ne reproduit aucun nom, numéro de téléphone, email, identifiant ni adresse.

### 15 Juillet 2025
#### 🇰🇪 Kenya - Adrian Kenya
- **Groupe ransomware:** lynx
- **Secteur:** Télécommunications / Infrastructures Énergétiques / TIC.
- **Site web:** adrian.co.ke / www.adriankenya.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** Adrian Group (Adrian Kenya) est un leader kényan de l'ingénierie technologique.
- **Analyse:** AFRINTEL a examiné un petit échantillon local de quatre documents associés à cette revendication : une facture d'un prestataire pour des travaux d'installation de site télécom (antennes, câbles de liaison et installation RRU) adressée à Adrian Kenya, un avis de paiement de TVA de la Kenya Revenue Authority (KRA) pour Adrian Group Limited couvrant janvier à mars 2025, une note de crédit d'un fournisseur de carburant adressée à Adrian Kenya Limited comportant des informations de véhicules, bancaires et de règlement, ainsi qu'un fil d'emails internes entre des collaborateurs d'Adrian Kenya et d'Adrian Group (domaines adriankenya.com et adriangroup.tech) évoquant le déploiement d'un site télécom au niveau d'un entrepôt. Les documents sont cohérents entre eux, référencent les mêmes noms d'entreprise, domaines et contexte de projet, et contiennent des identifiants personnels complets, des coordonnées bancaires et un numéro fiscal, qu'AFRINTEL ne reproduit pas ici. L'échantillon indique une exposition de documents financiers, fiscaux, fournisseurs et de correspondance interne, mais sa portée se limite à quatre documents et ne permet pas d'établir le volume total ni l'étendue de la compromission sous-jacente. AFRINTEL ne confirme pas l'intrusion de façon indépendante.

### 15 Juillet 2025
#### 🇪🇬 Égypte - Egyptian Electricity Holding Company (EEHC, eehc.gov.eg)
- **Groupe ransomware:** devman
- **Secteur:** Gouvernement / Énergie (Électricité)
- **Site web:** https://eehc.gov.eg
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
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
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Description victime:** La municipalité d'Otjiwarongo est l'organe de gouvernement local de la ville d'Otjiwarongo, chef-lieu de la région d'Otjozondjupa en Namibie.
- **Analyse:** AFRINTEL a examiné un échantillon local de documents cohérents avec la revendication du cybercriminel incransom, correspondant à un extrait non caviardé du système de paie VIP Payroll System de la municipalité, une liste de rémunération pour la période de paie se terminant le 28 février 2025, recensant des dizaines de dossiers d'employés avec code employé, service, nom complet, montant net de paie en dollars namibiens, code banque et numéro de compte bancaire. Le document porte des en-têtes système authentiques l'identifiant comme une exécution officielle de paie municipale (« 001 Municipality of Otjiwarongo »), cohérent avec une compromission réelle du système RH/paie interne plutôt qu'un échantillon fabriqué. La combinaison de l'identité des employés, de leur rémunération et de leurs coordonnées bancaires complètes pour la paie d'une administration locale soutient une évaluation à très haute confiance. L'exposition de ces données crée un risque important de fraude à la paie, de phishing ciblé et de fraude à l'identité visant les employés municipaux. AFRINTEL ne reproduit aucun nom d'employé, code employé, montant de salaire ni numéro de compte bancaire issu de l'échantillon examiné.

### 15 Juillet 2025
#### 🇲🇷 Mauritanie - Portail QCE (qce.gov.mr)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Unknown
- **Secteur:** Gouvernement / Marchés publics (Qualification des entreprises et du personnel)
- **Site web:** qce.gov.mr
- **Statut:** Claim - Data Sample Published
- **Description victime:** qce.gov.mr est une plateforme en ligne du gouvernement mauritanien utilisée pour héberger et traiter des dossiers de qualification de personnel et d'entreprises, cohérente avec une vérification des entreprises contractantes et de leur personnel technique dans le cadre de marchés publics ; sa mission institutionnelle précise n'a pas pu être confirmée de manière indépendante à partir de l'échantillon examiné.
- **Analyse:** AFRINTEL a examiné un échantillon local de fichiers cohérents avec des dossiers de qualification de personnel soumis via la plateforme, comprenant des curriculum vitae, des cartes d'identité nationale (CIN), des diplômes, des actes notariés de dépôt de contrats de travail et d'autres pièces justificatives pour des personnes employées par plusieurs entreprises privées mauritaniennes distinctes (notamment dans les secteurs de la construction, du forage et des services techniques). Les documents affichent des en-têtes officiels authentiques, des cachets de notaire et des champs de données personnelles structurés (nom complet, numéro national d'identification, date et lieu de naissance, employeur, poste, signature, photographie), cohérents avec un véritable dépôt de dossiers de qualification/marchés publics plutôt qu'un contenu fabriqué. Aucun acteur revendicateur, lieu de publication ni post de forum n'a pu être identifié pour ce jeu de données ; l'échantillon a été daté à partir des métadonnées des fichiers locaux (mi-juillet 2025) en l'absence de date de publication explicite. La combinaison de numéros d'identification nationale, de diplômes et de dossiers d'emploi pour de nombreuses personnes privées crée un risque significatif de fraude à l'identité, de falsification de documents et d'ingénierie sociale ciblée contre les candidats concernés et leurs employeurs. AFRINTEL ne reproduit aucun nom, numéro d'identification nationale, date de naissance, coordonnée d'employeur ni signature issus de l'échantillon examiné.

### 18 Juillet 2025
#### 🇲🇦 Maroc - Université Mohammed VI Polytechnique (UM6P)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Mercobyte
- **Secteur:** Éducation / Enseignement Supérieur
- **Site web:** https://um6p.ma
- **Statut:** Claim - Unverified
- **Description victime:** Institution (Université) d'excellence basée à Benguerir, pôle stratégique pour la recherche, l'innovation et la formation des cadres au Maroc. L'acteur revendique une fuite de données ciblée et une opération d'influence, publiant des photos d'identité d'étudiants accompagnées d'un message politique ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 22 Juillet 2025
#### Afrique du Sud - National Treasury - Infrastructure Reporting Model (IRM) website
- **Acteur / Groupe:** Unknown
- **Secteur:** Government / Administration
- **Site web:** https://www.treasury.gov.za/
- **Date de l'incident:** 22 juillet 2025 - date de détection du malware indiquée par le National Treasury
- **Date de publication initiale:** 23 juillet 2025
- **Statut:** Government Confirmed
- **Type d'incident:** Malware
- **Sous-type:** Malware intrusion on public-facing reporting system
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Type de source:** Government Statement
- **Analyse:** Le National Treasury sud-africain a identifié un malware sur le site Infrastructure Reporting Model et isolé les serveurs concernés. Les autres systèmes du Treasury ont continué à fonctionner normalement et aucune exfiltration de données n'a été confirmée. AFRINTEL conserve l'intrusion malware confirmée comme observation supplémentaire, Malware ne faisant pas partie des six types principaux.
- **Sources:** [National Treasury South Africa - communiqué officiel](https://www.treasury.gov.za/comm_media/press/2025/2020072301%20Media%20Statement%20-%20Malware%20Intrusion%20on%20National%20Treasury%E2%80%99s%20Infrastructure%20Reporting%20Model%20Website%20.pdf)

### 25 Juillet 2025
#### 🇹🇳 Tunisie - Ministère des Finances (finances.gov.tn)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Dark 07x Team
- **Secteur:** Gouvernement / Administration Fiscale.
- **Site web:** https://finances.gov.tn
- **Statut:** Claim - Unverified
- **Description victime:** Ministère des Finances Tunisien
- **Analyse:** AFRINTEL n'a pas examiné de preuve technique directement propre à finances.gov.tn au-delà de la revendication « Full Access » de l'acteur. Toutefois, un export de type gestionnaire d'identifiants, examiné en parallèle de cette revendication et attribué à la même campagne Dark 07x Team à la même date, contenait des dizaines de couples identifiant/mot de passe en clair pour un autre établissement tunisien (l'Académie des Banques et des Finances, ABF), suggérant que l'acteur a rebondi entre plusieurs organisations compromises et réutilisé des identifiants collectés au fil de cette campagne. AFRINTEL ne reproduit aucun des identifiants exposés.

### 25 Juillet 2025
#### 🇹🇳 Tunisie - Académie des Banques et des Finances (abf.tn)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Dark 07x Team
- **Secteur:** Formation Professionnelle / Secteur Bancaire.
- **Site web:** https://abf.tn
- **Statut:** Claim - Data Sample Published
- **Description victime:** L'Académie des Banques et des Finances (ABF) est l'organisme de formation continue de l'Association Professionnelle Tunisienne des Banques et des Établissements Financiers (APTBEF).
- **Analyse:** Le matériel montre une session administrative authentifiée sur le site de l'ABF sous un compte nominatif du personnel, confirmant un accès allant au-delà d'une simple revendication. Un export distinct de type gestionnaire d'identifiants, associé à la même campagne, contenait plusieurs dizaines de couples identifiant/mot de passe en clair pour des plateformes liées à l'ABF, notamment son système de visioconférence/webinaire, son portail de formation à distance et un accès d'administration WordPress, ainsi que quelques adresses email associées. Aucun des identifiants ou adresses email exposés n'est reproduit.

### 25 Juillet 2025
#### 🇹🇳 Tunisie - BTK Bank
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Dark 07x Team
- **Secteur:** Banque / Services Financiers.
- **Site web:** https://btknet.com
- **Statut:** Claim - Data Sample Published
- **Description victime:** BTK Bank (Banque Tuniso-Koweïtienne) est une institution bancaire tunisienne issue d'une coentreprise tuniso-koweïtienne.
- **Analyse:** Le matériel montre une session e-banking authentifiée et active sur btknet.com, incluant une liste de comptes, un écran de saisie de virement affichant une liste de bénéficiaires, et un relevé d'identité bancaire (RIB/IBAN) au nom d'un titulaire de compte identifié, confirmant une réelle prise de contrôle de compte plutôt qu'une simple revendication. La publication associée, attribuée à une collaboration entre les pseudonymes Dark 07x, Jokeir 07x et Dr. SHell 08x opérant sous le nom « Dark Hell 07X », annonçait une vente échelonnée des données volées : base de données complète pour 4 000 USD, fichier de données de comptes bancaires pour 2 000 USD, et comptes bancaires individuels de 100 USD (un compte) à 450 USD (cinq comptes). Aucun numéro de compte, IBAN ni identité de client n'est reproduit à partir de l'échantillon examiné.

### 25 Juillet 2025
#### 🇹🇳 Tunisie - Banque de Tunisie (bt.com.tn)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Dark 07x Team
- **Secteur:** Banque / Services Financiers.
- **Site web:** bt.com.tn
- **Statut:** Claim - Data Sample Published
- **Description victime:** Banque de Tunisie (BT) est l'une des plus anciennes et des plus importantes banques privées du pays
- **Analyse:** Le matériel montre un tableau de bord client authentifié et actif sur bt.com.tn, affichant plusieurs soldes de comptes, un module de taux de change, un aperçu de portefeuille de titres et un graphique d'historique de transactions, confirmant un accès réel au niveau du compte plutôt qu'une simple revendication. Aucun numéro de compte ni solde n'est reproduit à partir de l'échantillon examiné.

### 27 Juillet 2025
#### 🇪🇷 Érythrée - Ambassade d'Érythrée aux États-Unis
- **Type d'incident:** Data Leak

- **Acteur / Groupe:** Gh1nDar
- **Secteur:** Gouvernement / Diplomatie
- **Statut:** Claim - Unverified
- **Site web:** [us.eriembassy.org](https://us.eriembassy.org)

- **Description :**
  L'ambassade d'Érythrée aux États-Unis est la représentation diplomatique officielle de l'État érythréen sur le territoire américain.

- **Analyse:**
  Un cybercriminel utilisant le pseudonyme Gh1nDar affirme, dans une publication sur BreachForums datée du 27 juillet 2025, avoir mis en ligne une fuite de données concernant environ 5 000 citoyens liés à l'ambassade d'Érythrée aux États-Unis. Les données prétendument exposées incluraient numéro de carte d'identité, nom complet, nom de la mère, numéro de passeport, adresse e-mail, numéro de téléphone, date de naissance, religion et profession actuelle. Aucun échantillon vérifiable n'était accessible dans la source collectée. Le compte à l'origine de la publication est récent et ne dispose d'aucun historique de fiabilité. À ce stade, AFRINTEL ne confirme pas l'intrusion ni l'authenticité des données.

### 28 Juillet 2025
#### 🇹🇳 Tunisie - BH Bank
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Dark 07x Team
- **Secteur:** Banque / Services Financiers.
- **Site web:** https://bhbank.tn/
- **Statut:** Claim - Data Sample Published
- **Description victime:** Institution bancaire historique et systémique en Tunisie (Banque de l'Habitat), pilier du financement de l'immobilier et de l'économie nationale.
- **Analyse:** La publication de l'acteur, publiée sous le pseudonyme Jokeir07x dans le cadre de la collaboration « Dark Hell 07X » avec Dr. SHell 08x (également responsable de la revendication BTK Bank), affirme que le groupe a pris le contrôle total de l'infrastructure du site, vidé et analysé toutes les bases de données, et confirmé la compromission des points d'accès back-end et front-end ; la publication annonce séparément une liste de 200 comptes « Yankee » mis en vente pour 100 USDT. Le matériel associé montre des sessions bancaires en ligne authentifiées et actives pour au moins deux comptes clients distincts, dont un compte professionnel « BH Capital Plus », avec soldes visibles, ainsi qu'un historique de transactions de carte bancaire incluant un retrait. Aucun numéro de compte, numéro de carte, identité de client ni solde n'est reproduit à partir de l'échantillon examiné.

### 29 Juillet 2025
#### 🇲🇦 Maroc - Ministère de l’Éducation nationale, du Préscolaire et des Sports
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Wieko
- **Secteur:** Gouvernement / Administration publique / Éducation
- **Site web:** [men.gov.ma](https://men.gov.ma)
- **Statut:** Claim - Data Sample Published

- **Description :**
  Le Ministère de l’Éducation nationale, du Préscolaire et des Sports est l’administration publique marocaine chargée de la politique gouvernementale relative à l’enseignement préscolaire, primaire et secondaire ainsi qu’au sport scolaire. Son portail institutionnel officiel utilise le domaine `men.gov.ma`.

- **Analyse:**
  Une publication attribuée à Wieko sur un forum cybercriminel annonce un fichier texte contenant 223 501 lignes au format `mail:pass`. L’échantillon visible comprend des comptes associés à plusieurs domaines marocains de l’enseignement, notamment des universités et des établissements de formation. Les identifiants individuels ne sont pas reproduits. Une section de téléchargement est visible mais masquée par le forum, ce qui empêche de vérifier le fichier annoncé, son intégrité, l’unicité des lignes ou la validité de tous les couples d’identifiants. Le contenu ressemble davantage à une liste combinée d’identifiants qu’à un export structuré d’une base ministérielle. La présence de comptes issus de plusieurs établissements ne démontre pas une compromission directe du système d’information central du ministère ; l’origine des identifiants, la méthode de collecte et le lien technique avec l’administration centrale restent inconnus. Ces combinaisons peuvent faciliter le credential stuffing, la prise de contrôle de comptes, l’accès non autorisé aux plateformes pédagogiques, le phishing ciblé et l’usurpation d’identité numérique, notamment en cas de réutilisation des mots de passe. Aucun prix, groupe ransomware, volume en octets, délai ou demande d’extorsion n’est mentionné.

- **Note de double revendication :**
  AFRINTEL a recensé séparément, le 18 juin 2025, une revendication concernant la plateforme Massar du ministère. Les acteurs et les jeux de données annoncés diffèrent, et les éléments disponibles ne permettent pas d’établir que les deux publications proviennent de la même compromission.

### 30 Juillet 2025
#### 🇧🇮 Burundi - PesaBay

- **Type d'incident:** Data Leak
- **Acteur / Groupe:** BabayoSysteam
- **Secteur:** Commerce / E-commerce
- **Statut:** Data Fully Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 2
- **Site web:** [pesabay.bi](https://pesabay.bi)

- **Description :**
  PesaBay est une place de marché électronique burundaise exploitée par AFRIREGISTER S.A. Elle permet à des vendeurs de publier des produits et à des utilisateurs d'acheter ou de prendre contact avec les commerçants présents sur la plateforme.

- **Analyse:**
  Une publication attribuée au compte BabayoSysteam, datée du 30 juillet 2025, met à disposition une base de données PesaBay présentée comme complète et contenant 1 850 enregistrements. Les champs publiés comprennent le prénom, le nom, l'adresse e-mail, le numéro de téléphone et le statut du compte. La présence de nombreux numéros utilisant l'indicatif burundais `+257`, combinée à l'identité visuelle de PesaBay et à la structure cohérente des enregistrements, étaye avec une confiance moyenne l'attribution du jeu de données à la plateforme. AFRINTEL classe donc le cas `Data Fully Published`. Cette qualification décrit la publication du jeu annoncé comme complet ; elle ne confirme pas indépendamment la méthode d'acquisition, l'intrusion initiale, l'unicité des lignes ni la couverture de l'ensemble de la base de production de PesaBay. Les données de contact publiées présentent un risque de phishing ciblé, de fraude, de spam et d'usurpation d'identité numérique, correspondant à un impact de niveau 2. Aucun nom, e-mail, numéro de téléphone ni autre donnée personnelle brute n'est reproduit.

---
[Rapport de Juillet 2025](./report/README_FR.md)
---

### 31 Juillet 2025
#### Tunisie - Le Groupement Pharmaceutique (LGP)
- **Acteur / Groupe:** Jokeir 07x / Dr Shell 08x (claim)
- **Secteur:** Healthcare / Medical
- **Site web:** Not independently confirmed
- **Date de l'incident:** 31 juillet 2025 - date rapportée par la source CTI secondaire
- **Date de publication initiale:** 31 juillet 2025
- **Statut:** Claim - Secondary Evidence / Screenshots
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 4
- **Description victime:** Le Groupement Pharmaceutique a été identifié dans une source CTI secondaire concernant l'exposition alléguée d'un accès à un portail interne.
- **Analyse:** Des identifiants d'accès et des captures d'un portail interne auraient été publiés, exposant potentiellement des informations commerciales, références, prix, marges et fournisseurs. Aucune confirmation de la victime n'a été identifiée dans l'audit fourni. AFRINTEL enregistre le cas avec une confiance moyenne et ne reproduit aucun identifiant ni valeur sensible.
- **Type de source:** Secondary CTI
- **Sources publiques:** [CyHawk Africa](https://cyhawk-africa.com/compromised-credentials/tunisian-pharmaceutical-group-breached-internal-portal-access-shared-publicly/)

### Juillet 2025 - date exacte de l'incident non communiquée publiquement
#### Seychelles - Seychelles Commercial Bank
- **Acteur / Groupe:** Unknown
- **Secteur:** Finance / Banking
- **Site web:** Seychelles Commercial Bank
- **Date de l'incident:** Juillet 2025 - date exacte de l'incident non communiquée publiquement
- **Date de publication initiale:** 29 juillet 2025
- **Statut:** Bank + Central Bank Confirmed
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Description victime:** Seychelles Commercial Bank est un établissement bancaire opérant aux Seychelles.
- **Analyse:** La banque a annoncé avoir identifié et contenu un cyberincident au cours duquel certaines informations personnelles de clients de la banque en ligne ont été exposées. Aucun fonds client n'a été annoncé comme compromis. La communication publique ne fournissant pas de date précise de compromission, AFRINTEL place l'événement en juillet sans inventer un jour d'incident.
- **Type de source:** Bank / Central Bank Confirmation via Public Reporting
- **Sources publiques:** [Security Affairs](https://securityaffairs.com/180513/data-breach/seychelles-commercial-bank-reported-cybersecurity-incident.html)

---

## Août 2025

### 06 Août 2025
#### 🇹🇳 Tunisie - Yasat (yasat.tn)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** RainbowDF
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
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** Kenya Electricity Generating Company PLC (KenGen) est le principal producteur d'électricité du Kenya, fournissant environ 70 % de l'énergie consommée dans le pays.
- **Analyse:** AFRINTEL a examiné un ensemble de documents locaux associés à cette revendication. L'échantillon comprend des documents internes de gestion contractuelle de KenGen relatifs à un projet de construction d'un centre de formation géothermique (une note de l'équipe de mise en œuvre du contrat, un bon de commande officiel et une lettre de garantie bancaire de bonne exécution émise par une banque commerciale), un budget CAPEX détaillé pour la division Geothermal Development, un registre financier de type paie, un tableau d'effectifs du département Geothermal Development listant identifiants employés, noms, genre, intitulés de poste et niveaux de grade, une déclaration de confidentialité d'appel d'offres signée liée à un marché informatique interne, un courrier officiel du ministère kényan de l'Énergie et du Pétrole adressé aux directeurs généraux de KenGen et d'autres entités du secteur énergétique national concernant un cadre de renforcement des ressources humaines et de recherche-développement, ainsi qu'un plan technique d'un local auxiliaire/tableau électrique d'une installation. Les documents présentent un en-tête, des cachets, des signatures et des numéros de contrat cohérents et croisés entre des fichiers de structure indépendante, ce qui renforce la confiance quant à une origine interne aux systèmes de KenGen. L'ensemble combine des données personnelles d'employés, des documents financiers et de passation de marchés internes, de la documentation technique et des correspondances avec des institutions du secteur énergétique national, indiquant une exposition touchant plusieurs systèmes internes plutôt qu'une seule application. AFRINTEL ne reproduit aucun nom d'employé, identifiant, signature ni valeur monétaire issus de l'échantillon, et ne confirme pas l'intrusion de façon indépendante.

### 06 Août 2025
#### 🇲🇦 Maroc - New Era Com
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Chucky_BF
- **Secteur:** Télécoms / Infrastructures / Services IT.
- **Site web:** neweracom.ma
- **Statut:** Data Fully Published
- **Description victime:** Société marocaine spécialisée dans l'ingénierie des télécoms, l'installation d'infrastructures réseaux et les solutions ERP/CRM. L'acteur a publié un dump SQL de 607 Mo contenant plus de 476 000 enregistrements.

### 08 Août 2025
#### Égypte - Multiple government and institutional portals
- **Acteur / Groupe:** Hider_Nex / Keymous Plus (claim)
- **Secteur:** Government / Administration
- **Site web:** Multiple Egyptian government and institutional portals
- **Date de l'incident:** 8 août 2025 - date rapportée pour la campagne DDoS
- **Date de publication initiale:** 8 août 2025
- **Statut:** Claim - OSINT Availability Evidence
- **Type d'incident:** DDoS
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 4
- **Description victime:** La campagne signalée visait plusieurs services web gouvernementaux et institutionnels égyptiens.
- **Analyse:** Une campagne DDoS a été revendiquée contre plusieurs services gouvernementaux et institutionnels égyptiens, avec des indisponibilités rapportées. L'attribution reste auto-revendiquée et la validation indépendante de chaque cible n'était pas disponible dans l'audit fourni. AFRINTEL enregistre la campagne comme un seul incident avec des réserves explicites.
- **Type de source:** Secondary CTI + Availability Evidence
- **Sources publiques:** [CyHawk Africa](https://cyhawk-africa.com/ddos/multiple-egyptian-government-and-institutional-websites-allegedly-attacked-by-hacktivist-group/)

### 09 Août 2025
#### 🇳🇬 Nigeria - Zenith Bank Plc
- **Acteur / Groupe:** KaruHunters
- **Secteur:** Banque / Services Financiers.
- **Site web:** zenithbank.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** L'une des plus grandes institutions financières du Nigeria et d'Afrique anglophone, cotée à la Bourse du Nigeria et à celle de Londres. L'acteur revendique l'exfiltration et la mise en vente de plus de 1,8 million de dossiers clients, ainsi que des données d'employés. AFRINTEL a examiné un échantillon CSV local de 18 lignes et huit colonnes couvrant un index, un code, un identifiant, un nom, un montant, une adresse, un téléphone et une adresse email. Aucune valeur brute n'est reproduite.

### 11 Août 2025
#### 🇿🇦 Afrique du Sud - Body Graphics Tattoo Supply
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** N1KA
- **Secteur:** Commerce de détail / E-commerce.
- **Site web:** bodygraphicstattoosupply.co.za
- **Date de publication de la source :** 11 août 2025
- **Statut:** Data Fully Published
- **Description victime:** Détaillant en ligne majeur basé à Johannesburg, spécialisé dans la fourniture de matériel de tatouage professionnel et de produits de soin en Afrique du Sud.
- **Analyse:** AFRINTEL a examiné deux fichiers d'export structurés référencés dans une publication observée sur DarkForums, totalisant 6 501 enregistrements, soit un volume cohérent avec celui revendiqué par l'acteur. Le jeu de données correspond à un export de clients et d'administrateurs WordPress/WooCommerce, incluant identifiants de connexion, adresses email, mots de passe hachés (format phpass), adresses postales, numéros de téléphone, adresses IP, chaînes d'user-agent et jetons de session. La cohérence structurelle entre le volume revendiqué et les fichiers examinés, ainsi que la correspondance des champs avec la plateforme e-commerce de la victime, justifie un niveau de confiance élevé, et la publication identifie le compte source N1KA. AFRINTEL ne reproduit aucun nom de client, coordonnée, adresse ni identifiant issu de l'échantillon examiné.

### 13 Août 2025
#### 🇩🇿 Algérie - Cevital
- **Groupe ransomware:** akira
- **Secteur:** Agroalimentaire/ Industrie / Logistique
- **Site web:** www.cevital.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Leader de l'industrie agroalimentaire en Algérie, actif dans l'électronique, l'acier, le verre et la distribution.

### 17 Août 2025
#### 🇿🇦 Afrique du Sud - SYSPRO
- **Groupe ransomware:** warlock
- **Secteur:** Technologies (Éditeur de logiciels)
- **Site web:** syspro.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** SYSPRO est un éditeur de logiciels ERP (Enterprise Resource Planning) sud-africain, fournissant des solutions de gestion intégrées pour les entreprises de fabrication et de distribution.

### 18 Août 2025
#### 🇺🇬 Ouganda - Uganda Electricity Transmission Company Limited
- **Groupe ransomware:** qilin
- **Secteur:** Énergie (Électricité)
- **Site web:** https://www.uetcl.go.ug / www.uetcl.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Société publique ougandaise responsable du transport de l'électricité.

### 18 Août 2025
#### 🇹🇳 Tunisie - International Freight & Commerce
- **Groupe ransomware:** direwolf
- **Secteur:** Logistique
- **Site web:** ifc-tunisie.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Entreprise tunisienne qui assure des services de transport maritime, aérien et terrestre, ainsi que la gestion logistique et les formalités douanières pour des entreprises importatrices et exportatrices.

### 20 Août 2025
#### 🇿🇦 Afrique du Sud - Netstar South Africa (deuxième attaque)
- **Groupe ransomware:** incransom
- **Secteur:** Technologie / Télématique / Sécurité IoT
- **Site web:** www.netstar.co.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Netstar, une filiale du groupe Altron, est le pionnier de l'industrie du suivi et de la récupération de véhicules volés (SVR) en Afrique du Sud.
- **Analyse:** AFRINTEL avait déjà enregistré une revendication contre cette même entreprise par devman le 23 mai 2025. Cette seconde revendication, publiée environ trois mois plus tard par un acteur différent, pourrait refléter soit une intrusion distincte réelle, soit une republication/revente de la revendication précédente ; AFRINTEL n'a pas pu confirmer de manière indépendante quel scénario s'applique.

### 23 Août 2025
#### 🇪🇬 Égypte - TEAM4 Security
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** GhostCrawl
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
- **Type d'incident:** Ransomware
- **Description victime:** WAN (Swan General Ltd et Swan Life Ltd) est le leader du marché des assurances et des services financiers à l'Île Maurice.

### 25 Août 2025
#### 🇹🇬 Togo - Infrastructures Gouvernementales
- **Type d'incident:** Access Sale
- **Acteur / Groupe:** BIGBROTHER
- **Secteur:** Gouvernement / Infrastructures Critiques.
- **Site web:** gouv.tg
- **Statut:** Claim - Data Sample Published
- **Description victime:** Portail officiel et infrastructures numériques de la République Togolaise, hébergeant les services administratifs et les données étatiques.
- **Analyse:** Des éléments corroborent la revendication de l'acteur, incluant le post DarkForums lui-même ainsi que plusieurs éléments montrant un accès administratif actif à plusieurs plateformes numériques gouvernementales togolaises : le système de gestion de l'état civil et de l'identité DSNIC (justice.xflow.gouv.tg), une plateforme de partage de fichiers et de collaboration de type Nextcloud (cloud.numerique.gouv.tg) avec des dossiers partagés et des fichiers de configuration, une instance de collecte de données KoboToolbox (kf.form.gouv.tg) hébergeant plusieurs dizaines d'enquêtes et formulaires gouvernementaux actifs, ainsi qu'un système de reporting statistique de l'éducation (stateduc.planifeducation.gouv.tg). Les éléments montrent un accès administratif réel à des tableaux de bord actifs, et non un simple échantillon public, ce qui est cohérent avec la description de l'offre par l'acteur comme une vulnérabilité 0day donnant un accès privilégié. Cette étendue d'accès à des systèmes et sous-domaines distincts sous le domaine gouv.tg justifie un niveau de confiance élevé quant à une compromission active et non corrigée affectant plusieurs services numériques gouvernementaux, indépendamment du prix en Monero avancé par l'acteur, qu'AFRINTEL ne peut vérifier. AFRINTEL ne reproduit aucun identifiant, valeur de configuration, donnée citoyenne ni détail de session issu des éléments examinés.
---
[Rapport d'Août 2025](./report/README_FR.md)
---

### 27 Août 2025
#### Maroc - Multiple Moroccan websites (OurSec campaign)
- **Acteur / Groupe:** OurSec (claim)
- **Secteur:** Not specified
- **Site web:** Multiple Moroccan websites
- **Date de l'incident:** 27 août 2025 - date rapportée pour la campagne; publication secondaire le 31 août
- **Date de publication initiale:** 31 août 2025
- **Statut:** Claim - OSINT Corroborated
- **Type d'incident:** Defacement
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** La campagne signalée concernait plusieurs sites marocains qui auraient été défacés dans le cadre d'une action hacktiviste coordonnée.
- **Analyse:** OurSec a revendiqué le défacement de plusieurs sites marocains. Des messages ou images de défacement et des références d'archives ont été rapportés, mais l'audit fourni recommande de valider séparément chaque domaine affecté et chaque horodatage. AFRINTEL enregistre donc la campagne avec une confiance moyenne et conserve l'acteur comme revendication.
- **Type de source:** Secondary CTI + Archive References
- **Sources publiques:** [CyHawk Africa](https://cyhawk-africa.com/ddos/oursec-claims-responsibility-for-moroccan-website-defacements/)

### 30 Août 2025
#### Égypte - cg.eg; gags.gov.eg; kayani.gov.eg; shmft.gov.eg
- **Acteur / Groupe:** BIGBROTHER (claimed seller)
- **Secteur:** Government / Administration
- **Site web:** cg.eg / gags.gov.eg / kayani.gov.eg / shmft.gov.eg
- **Date de l'incident:** 30 août 2025 - date de la publication de vente d'accès rapportée
- **Date de publication initiale:** 30 août 2025
- **Statut:** Claim - Marketplace Listing / Screenshots
- **Type d'incident:** Access Sale
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 4
- **Description victime:** Des accès non autorisés à quatre domaines gouvernementaux égyptiens ont été proposés à la vente.
- **Analyse:** Un acteur a proposé à la vente des accès non autorisés à quatre domaines gouvernementaux, avec des captures mentionnées dans la source secondaire. La validité des accès n'a pas été confirmée indépendamment. La fiche n'est pas fusionnée avec la revendication ransomware distincte de janvier concernant gags.gov.eg, car les éléments décrivent une publication de vente d'accès différente et datée d'une autre période.
- **Type de source:** Secondary CTI + Marketplace Screenshots
- **Sources publiques:** [CyHawk Africa](https://cyhawk-africa.com/initial-access/alleged-sale-of-access-to-four-egyptian-government-sites/)

## Septembre 2025

### 02 Septembre 2025
#### 🇩🇿 Algérie - Université des Frères Mentouri Constantine 1 (UMC1)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Fire Wire
- **Secteur:** Éducation / Enseignement supérieur
- **Site web:** university-dz.net
- **Statut:** Claim - Data Sample Published
- **Description victime:** L'Université des Frères Mentouri Constantine 1 (UMC1) est une grande université publique algérienne. L'acteur revendicateur affirme une exfiltration de plus de 10 Go, un volume qu'AFRINTEL n'a pas collecté ni analysé. Les fichiers examinés, exfiltrés via ce qui semble être une plateforme web académique partagée (university-dz.net), comprennent les plannings d'examens du Master 2 semestre 1 (janvier 2025) avec dates, modules, salles et départements ; un ensemble de plus de 200 dossiers étudiants détaillés (nom complet, numéro d'inscription universitaire, groupe TD et notes par matière, avec annotations de statut telles qu'exclusion/admission) d'étudiants de L1 (promotion 2015-2016) ; un annuaire de conformité véhicules avec numéros de téléphone et emails ; et un modèle de conférence listant des contacts et affiliations pour un événement académique 2024 (NCME). La combinaison de dossiers académiques, de coordonnées personnelles et de documents administratifs crée un risque significatif de fraude à l'identité, de phishing ciblé et de vishing contre les étudiants, le personnel et les contacts affiliés. L'acteur revendicateur s'identifie sous le nom « Fire Wire ».

### 03 Septembre 2025
#### Maroc - Government portals + Maroc Telecom (campaign)
- **Acteur / Groupe:** Keymous (claim)
- **Secteur:** Government / Administration
- **Site web:** Multiple government portals / Maroc Telecom
- **Date de l'incident:** 3 septembre 2025 - date rapportée pour la campagne; publication secondaire le 10 septembre
- **Date de publication initiale:** 10 septembre 2025
- **Statut:** Claim - OSINT Availability Evidence
- **Type d'incident:** DDoS
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 4
- **Description victime:** La campagne signalée a affecté des portails gouvernementaux marocains et des services de télécommunications, avec des références à Maroc Telecom.
- **Analyse:** Plusieurs portails gouvernementaux marocains et services de télécommunications auraient subi des perturbations lors d'une campagne DDoS revendiquée, avec notamment des erreurs HTTP 522-525 et des délais d'attente. L'attribution est auto-revendiquée et le périmètre exact des cibles reste incomplètement validé. AFRINTEL enregistre un seul incident de campagne avec une confiance moyenne.
- **Type de source:** Secondary CTI + Availability Evidence
- **Sources publiques:** [CyHawk Africa](https://cyhawk-africa.com/ddos/multiple-government-websites-reportedly-disrupted-in-retaliatory-cyber-campaign/)

### 04 Septembre 2025
#### 🇳🇬 Nigeria - MobileSub
- **Acteur / Groupe:** Not specified
- **Secteur:** Fintech / Services de paiement
- **Site web:** [mobilesub.com.ng](https://mobilesub.com.ng)
- **Date du fichier source :** 4 septembre 2025
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** MobileSub est une plateforme nigériane de services numériques fournissant des fonctions d'achat de crédit mobile, de données, d'électricité, de télévision par câble, de paris et de paiement associées.
- **Analyse:** AFRINTEL a examiné un dump SQL local d'environ 14,3 Mo contenant 42 tables et 306 blocs INSERT. Le schéma comprend des comptes utilisateurs, la KYC, des clés API, l'historique des transactions, les transferts, l'airtime, les données mobiles, l'électricité, les inscriptions aux examens, les paris, la télévision par câble et d'autres modules de paiement, ainsi que des tables de sauvegarde d'utilisateurs. L'horodatage du fichier source est le 4 septembre 2025 ; il est traité comme un horodatage de découverte/source AFRINTEL, et non comme la date prouvée de la compromission initiale. Le jeu de données peut exposer des informations d'identité, de contact, de KYC, de transaction et d'authentification. Aucune valeur personnelle, clé API ou identifiant n'est reproduit. L'authenticité, l'exhaustivité et le contexte de publication restent non vérifiés.
- **Note d'analyse source :** Le dump contient des catégories de tables sensibles aux identifiants et aux secrets ; AFRINTEL n'a tenté aucune authentification, aucun accès ni récupération de secret.

### 05 Septembre 2025
#### 🇪🇬 Égypte - MeamarGroup
- **Groupe ransomware:** obscura
- **Secteur:** Immobilier / Construction / Ingénierie.
- **Site web:** https://meamargroup.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Description victime:** MeamarGroup (incluant Meamar Real Estate Development et Meamar Construction) est un acteur majeur du secteur de la construction en Égypte depuis plus de 25 ans. Basé au Caire (New Cairo), le groupe gère plus de 400 projets allant des complexes résidentiels de luxe aux installations industrielles et médicales (comme l'usine Biogeneric Pharma).
- **Analyse:** AFRINTEL a examiné une archive locale côté serveur (491 fichiers et dossiers, tous appartenant au compte du serveur web www-data) cohérente avec cette revendication. Les horodatages de dossiers de cette collecte se regroupent autour du 05 septembre 2025, correspondant à la date de revendication de cette fiche, tandis que la majorité des fichiers sous-jacents porte un horodatage antérieur du 27 août 2025, suggérant une étape initiale de préparation des données avant la revendication publique. Le contenu examiné comprend des classeurs comptables internes pluriannuels, une importante archive de centre d'appels commercial/contacts prospects, des CV d'employés ainsi que du matériel interne de conception et de plans CAO pour des projets immobiliers. Une archive imbriquée contient des fichiers originaux ainsi que des copies portant l'extension de chiffrement `.obscura`, ce qui soutient directement l'existence d'une étape de chiffrement et non une simple revendication d'exfiltration. Un court fichier texte cohérent avec un compte à rebours de portail de négociation Tor était également présent. La combinaison de la propriété des fichiers par le serveur web, d'horodatages cohérents et de copies chiffrées par l'acteur soutient une évaluation à très haute confiance d'une compromission réelle de l'environnement de fichiers interne de MeamarGroup. AFRINTEL ne reproduit aucun nom de client, numéro de contact, nom d'employé ni montant financier issu du matériel examiné.

### 06 Septembre 2025
#### 🇨🇮 Côte d'Ivoire - NSIA Assurances
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Tanaka
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
- **Type d'incident:** Ransomware
- **Description victime:** The Promise est une chaîne de restauration rapide (QSR) et un service de traiteur industriel de premier plan au Nigeria, particulièrement implantée à Port Harcourt et dans la région du Delta du Niger.

### 09 Septembre 2025
#### 🇲🇦 Maroc - Dolidol
- **Groupe ransomware:** TheGentlemen
- **Secteur:** Industrie Manufacturière / Literie / Ameublement.
- **Site web:** https://www.dolidol.ma
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Dolidol (filiale du groupe Palmeraie Industries et Services) est le leader incontesté de la literie et de la mousse polyuréthane au Maroc.

### 09 Septembre 2025
#### 🇿🇼 Zimbabwe - Proplastics Limited
- **Groupe ransomware:** TheGentlemen
- **Secteur:** Industrie manufacturière (Plastiques)
- **Site web:** https://www.proplastics.co.zw
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Proplastics Limited est le principal fabricant et fournisseur de systèmes de tuyauterie en plastique (PVC, PEHD) au Zimbabwe.
- **Analyse:** Le jeu local fourni contient 63 fichiers associés à Proplastics, notamment des PDF, des tableurs, des fichiers image et des fichiers texte. Les noms de fichiers indiquent des documents métier relatifs aux factures et notes de crédit, soldes de comptes, nomenclatures, reliquats de commandes, livraisons, analyses de ventes et rapports par agence. Les fichiers portent des dates couvrant 2023-2024, tandis que les métadonnées du répertoire situent la collecte en septembre 2025 ; ces dates sont considérées comme contexte de preuve et non comme date confirmée d intrusion ou de publication. Le matériel soutient la plausibilité et la sensibilité potentielle de la revendication de septembre 2025, mais ne permet pas d établir indépendamment le vecteur d accès, le périmètre complet des données ni l attribution à TheGentlemen. AFRINTEL ne reproduit aucun nom, détail de compte, montant financier, enregistrement client ou contenu documentaire.

### 10 Septembre 2025
#### 🇳🇬 Nigeria - Princeps Credit Systems Limited
- **Groupe ransomware:** killsec
- **Secteur:** Finance
- **Site web:** https://princepsfinance.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Institution financière basée à Lagos, spécialisée dans le crédit à la consommation et le financement des PME.

### 11 Septembre 2025
#### 🇳🇦 Namibie - Epia Financial Services
- **Groupe ransomware:** radar
- **Secteur:** Services financiers
- **Site web:** https://epiafs.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** Institution financière basée à Windhoek, offrant des services de gestion de patrimoine, de conseil en investissement et de courtage en Namibie.
- **Analyse:** Des éléments de messagerie exfiltrés rattachés à la revendication (correspondance envoyée depuis et vers les boîtes de réception et d'administration d'EPIA avec Bank Windhoek/Capricorn Group, First National Bank of Namibia et NamPost, relative à des vérifications de comptes clients) sont examinés, ainsi que la structure d'un échantillon représentatif de fichiers d'administration de fonds de pension au niveau des champs/colonnes, sans ouvrir ni extraire de ligne individuelle d'adhérent. Les éléments examinés correspondent au rôle d'EPIA en tant qu'administrateur du Namibia Building Workers Pension Fund (NBWPF) et d'autres clients institutionnels. Les classeurs de données d'adhérents (par exemple un extrait de janvier 2025) contiennent plusieurs feuilles de plusieurs milliers d'enregistrements chacune (Actives, Deferred, Unclaimed, Exits) partageant un schéma de champs cohérent : numéro de membre, nom, prénom, autres prénoms, référence entreprise, date de naissance, numéro d'identité nationale, numéro de passeport, statut cotisant, statut du membre, nom de l'employeur, genre, dates d'emploi et d'adhésion au fonds, salaire mensuel et annuel, montant et date du solde du fonds (fund credit), date de dernière cotisation, date de sortie et détails de paiement. Un extrait de données actuarielles distinct couvre la période de septembre 2022 à avril 2024 avec un schéma et une ampleur comparables. D'autres fichiers inspectés structurellement incluent des rapports d'administration et d'allocation de revenus pluriannuels (résumés agrégés de transactions financières par période) et des formulaires d'autorisation client signés, le plus récent daté de juin 2025. AFRINTEL n'a pas ouvert chaque fichier de l'ensemble ; la cohérence des noms de fichiers et la correspondance par e-mail indiquent que les mêmes catégories d'enregistrements se répètent sur toute la période 2022-2025. La combinaison de numéros d'identification nationale, de dates de naissance, de données salariales et de solde de fonds de pension pour plusieurs milliers d'individus, avec la correspondance employeur et bancaire, représente une exposition à fort impact. L'étendue, la continuité jusqu'à mi-2025 et la spécificité organisationnelle des éléments examinés soutiennent un niveau de confiance élevé quant à la compromission de la messagerie et des fichiers, indépendamment de la revendication publique du groupe ransomware. L'ensemble local contient 73 fichiers pour environ 79,8 Mo, comprenant des tableurs, des rapports, des présentations, un fichier DOCX d'employeur et des fichiers image. Le classeur d'adhérents de janvier 2025 contient une feuille de synthèse et des feuilles d'état des membres (Actives, Deferred, Unclaimed et Exits), avec une feuille de synthèse allant jusqu'à 8 652 lignes et des feuilles allant jusqu'à 35 colonnes ; la structure examinée comprend des champs relatifs aux membres, employeurs, identités, emplois, salaires, crédits de pension, cotisations, sorties et paiements. L'extrait actuariel contient 8 168 lignes et 167 colonnes pour une période allant de septembre 2022 à avril 2024. Les éléments horodatés du 11 septembre 2025 sont cohérents avec le contexte de découverte de septembre. Aucun nom d'adhérent, numéro d'identification, coordonnée bancaire, signature, montant de salaire ni contenu de correspondance n'est reproduit à partir de l'échantillon examiné.

### 11 Septembre 2025
#### 🇦🇴 Angola - Base de données des employés du gouvernement angolais (pape.gov.ao)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** privilege
- **Secteur:** Gouvernement / Administration publique
- **Site web:** [pape.gov.ao](https://pape.gov.ao)
- **Statut:** Claim - Data Sample Published
- **Description victime:** La source présente pape.gov.ao comme une plateforme liée au gouvernement angolais et affirme proposer des dossiers d'employés de différents secteurs et domaines administratifs.
- **Analyse:** La publication du 11 septembre 2025 revendique une base de données de 245 employés du gouvernement angolais et énumère des champs relatifs aux identifiants d'employés, noms, dates de naissance, zones administratives et fonctions. Le fichier TXT local fourni pour examen contient 244 lignes non vides séparées par des virgules, dont une ligne d'en-tête et environ 243 lignes de données, avec six champs par ligne. Cela confirme l'existence d'un échantillon structuré de données d'employés, mais ne permet pas de confirmer indépendamment le total annoncé, l'organisme gouvernemental exact, l'authenticité ou l'exhaustivité du jeu de données. AFRINTEL ne reproduit aucun nom, identifiant, date de naissance ni autre donnée personnelle issue du fichier.

### 12 Septembre 2025
#### 🇨🇩 Congo (RDC) - Fonds pour la Réforme de l'Administration Publique (FRAP)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** privilege
- **Secteur:** Gouvernement / Administration
- **Site web:** [frap.cd](https://frap.cd/)
- **Statut:** Data Fully Published
- **Description victime:** Organisme en charge de la modernisation de l'administration en RDC.
- **Analyse:** AFRINTEL a examiné le post DarkForums lui-même, publié le 12 septembre 2025 par le cybercriminel privilege (statut VIP, compte créé en septembre 2025), intitulé « FRAP.CD - 1,136 LINES | Full User Data | Gov/Staff Access ». Le post décrit une base de données de 1 136 enregistrements comprenant des identifiants de connexion et des mots de passe hachés (plusieurs formats de hachage), des identifiants personnels (nom, prénom, sexe), des coordonnées (email, téléphone) lorsque disponibles, des champs de référence et de désignation de documents internes, ainsi que des métadonnées système (date de création, dernière connexion, dernière mise à jour du mot de passe, créé/modifié par, statut du compte). L'acteur décrit ces données comme couvrant des comptes d'administrateurs et de personnel sectoriel du portail FRAP.CD, ce qui est cohérent avec le rôle de la plateforme dans la gestion des profils administratifs et des comptes internes du personnel du Fonds pour la Réforme de l'Administration Publique. L'ensemble complet des données est proposé via un lien d'hébergement externe et n'est pas montré directement dans le post ; AFRINTEL n'a pas pu valider de façon indépendante l'authenticité ni l'exhaustivité du fichier hébergé. Compte tenu des identifiants de connexion et des données personnelles décrits, l'exposition de ce matériel créerait un risque d'accès au portail par réutilisation d'identifiants et de phishing ciblé contre le personnel de l'administration publique congolaise. AFRINTEL ne reproduit aucun identifiant, mot de passe, donnée personnelle ni coordonnée issu du post examiné.

### 14 Septembre 2025
#### 🇰🇪 Kenya - Office Of The Registrar Of Political Parties
- **Groupe ransomware:** qilin
- **Secteur:** Administrations publiques
- **Site web:** https://www.orpp.go.ke
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Organisme d'État kenyan chargé de l'enregistrement, de la régulation et de la supervision du financement des partis politiques.

### 16 Septembre 2025
#### 🇰🇪 Kenya - Jubilee Life Insurance
- **Groupe ransomware:** warlock
- **Secteur:** Assurances / Services financiers
- **Site web:** https://jubileelife.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Acteur majeur de l'assurance-vie et de la gestion de fonds au Kenya, filiale de Jubilee Holdings Limited.

### 17 Septembre 2025
#### 🇪🇬 Égypte - Accflex ERP
- **Groupe ransomware:** arcusmedia
- **Secteur:** Technologies / Édition de logiciels ERP.
- **Site web:** https://www.accflex.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Éditeur égyptien de solutions de gestion intégrées (comptabilité, RH, production) utilisé par de nombreuses entreprises au Moyen-Orient et en Afrique.

### 22 Septembre 2025
#### 🇲🇦 Maroc - Fractalite (fractalite.com)
- **Groupe ransomware:** killsec
- **Secteur:** Technologies/ Services Numériques / Développement Logiciel.
- **Site web:** https://fractalite.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Fractalite est une agence de conseil et d'ingénierie numérique marocaine, spécialisée dans le développement de solutions logicielles et l'accompagnement digital des entreprises.

### 24 Septembre 2025
#### 🇳🇬 Nigeria - Kolomoni Microfinance Bank
- **Acteur / Groupe:** Not specified
- **Secteur:** Microfinance / Banque
- **Site web:** [kolomonimfb.com](https://kolomonimfb.com)
- **Date de l'archive source :** 24 septembre 2025
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** Kolomoni Microfinance Bank est une institution financière nigériane qui fournit des services de microfinance et de banque numérique à ses titulaires de comptes.
- **Analyse:** AFRINTEL a examiné l'extraction RAR fournie et son fichier CSV Kolomoni. Le fichier contient 37 825 lignes et 12 colonnes couvrant le nom et le numéro de compte, l'email, le téléphone, le genre, la date de naissance, le statut du compte, l'adresse, la zone de gouvernement local, l'État, la dernière connexion et la date de l'enregistrement. La combinaison d'identifiants financiers, de coordonnées, de données démographiques, de localisation et de métadonnées de connexion crée des risques de phishing, de prise de contrôle de comptes, de fraude à l'identité et d'escroqueries financières ciblées. L'horodatage de l'archive est le 24 septembre 2025, tandis que les métadonnées internes du CSV contiennent une date de fichier antérieure au 24 août 2025 ; aucune de ces dates ne prouve la date de compromission initiale. Aucune valeur personnelle n'est reproduite. L'acteur, le forum de publication, l'authenticité et l'exhaustivité restent non précisés ou non vérifiés.

### 29 Septembre 2025
#### 🇸🇳 Sénégal - Direction Générale des Impôts et des Domaines (DGID)
- **Groupe ransomware:** BlackShrantac
- **Secteur:** Administration Publique / Finances / Fiscalité.
- **Site web:** https://www.impots.gouv.sn
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** La **DGID** est l'organe central du Ministère des Finances du Sénégal, responsable de la collecte des impôts, de la gestion du domaine national et du cadastre. Le groupe ransomware affirme avoir divulgué 1 téraoctet (1 To) de données sensibles, comprenant des bases de données fiscales structurées, des registres fonciers et des informations bancaires de contribuables ; AFRINTEL a consulté cette revendication sur le site de l'acteur mais n'a pas collecté ni analysé les données sous-jacentes.

### 30 Septembre 2025
#### 🇪🇬 Égypte - Telecom Egypt (TE Data)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** KILLUAX
- **Secteur:** Télécommunications
- **Site web:** te.eg
- **Statut:** Claim - Data Sample Published
- **Description victime:** Telecom Egypt exploite le service d'accès internet TE Data. L'échantillon examiné contient des enregistrements de type comptabilité RADIUS (identifiants abonnés au format tedata.net.eg, adresses IP de NAS, adresses MAC, adresses IP attribuées, horodatages de début/fin de session et type de connexion). Seul un nombre restreint d'enregistrements (36) était disponible pour analyse, ce qui limite l'évaluation de l'ampleur totale ; l'exposition pourrait néanmoins faciliter l'identification d'abonnés et la reconnaissance réseau.

## Octobre 2025

### 01 Octobre 2025
#### 🇿🇦 Afrique du Sud - Climatron (Pty) Ltd
- **Groupe ransomware:** incransom
- **Secteur:** Construction / CVC
- **Site web:** https://climatron.co.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Climatron (Pty) Ltd est une entreprise spécialisée dans les solutions de climatisation industrielle et commerciale, basée à Johannesburg.

### 05 Octobre 2025
#### 🇿🇦 Afrique du Sud - The Methodist Church of Southern Africa
- **Groupe ransomware:** beast
- **Secteur:** Religion / Organisation caritative
- **Site web:** www.methodist.org.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** The Methodist Church of Southern Africa (MCSA) est l'une des dénominations chrétiennes les plus influentes de la région. Elle opère non seulement en Afrique du Sud, mais aussi au Botswana, au Lesotho, en Namibie, au Swaziland et au Mozambique.

### 10 Octobre 2025
#### 🇿🇦 Afrique du Sud - Momentum Logistics
- **Groupe ransomware:** brotherhood
- **Secteur:** Transport / Logistique
- **Site web:** www.momentumlogistics.co.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Momentum Logistics est un prestataire logistique sud-africain basé à Johannesburg.

### 13 Octobre 2025
#### 🇲🇦 Maroc - LA VOIE EXPRESS
- **Groupe ransomware:** medusa
- **Secteur:** Logistique
- **Site web:** https://lavoieexpress.ma / https://lavoieexpress.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Description victime:** Société marocaine de logistique basée à Casablanca, offrant des services de messagerie, transport et entreposage.
- **Analyse:** AFRINTEL a examiné un échantillon local d'exports de tableurs multi-feuilles cohérents avec la revendication du cybercriminel medusa, chacun filigrané avec l'adresse du site de fuite Tor du groupe. Le matériel examiné comprend un grand livre comptable (écritures bancaires et journal datées de 2020-2021), des classeurs d'entrepôt et de logistique couvrant les mouvements de réception, d'expédition, de mise en stock préparé et de transfert interne de marchandises pour de grandes marques d'électroménager (référençant des gammes de produits BSH/Bosch-Siemens) rattachés à du personnel interne nommément identifié gérant ces opérations, ainsi qu'un rapport de balance âgée des comptes clients listant plusieurs dizaines de clients corporate nommés dans plusieurs villes marocaines (Casablanca, Agadir, Tanger, Marrakech, Fès, Settat et autres), incluant des comptes nationaux et multinationaux reconnus (parmi lesquels des entités affiliées à Procter & Gamble, Savola Maroc, Centrale Laitière, Ciment du Maroc, BSH Electroménager et Ecolab), avec les contacts clients nommés, numéros de téléphone, soldes impayés, conditions de paiement et statut de recouvrement/contentieux. La cohérence interne des données entre les modules comptable, entrepôt et commercial, la présence de comptes clients marocains et multinationaux réels et identifiables, ainsi que la période couverte sur plusieurs années (2020-2023) et plusieurs agences, soutiennent une évaluation à très haute confiance d'une compromission réelle et étendue des systèmes ERP et comptables internes de La Voie Express. Compte tenu de l'ampleur des données de comptes clients et du grand livre bancaire exposées, et de leur extension à la clientèle d'un opérateur logistique national majeur, cet incident crée un risque important de fraude à la facture, de compromission de messagerie professionnelle et d'ingénierie sociale ciblée visant La Voie Express et ses clients corporate, au-delà de la seule exposition opérationnelle de l'entreprise. AFRINTEL ne reproduit aucun nom de client, nom de contact, numéro de téléphone, montant financier ni identifiant de personnel issu du matériel examiné.

### 15 Octobre 2025
#### 🇰🇪 Kenya - Turnkey Africa
- **Groupe ransomware:** qilin
- **Secteur:** Technologies/ Fintech (Solutions pour l'Assurance).
- **Site web:** https://turnkeyafrica.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Turnkey Africa est un leader technologique panafricain. L'entreprise développe et fournit des solutions logicielles de gestion (Core Insurance Systems) pour les compagnies d'assurance et de réassurance dans plus de 10 pays d'Afrique.

### 17 Octobre 2025
#### 🇲🇬 Madagascar - Madagascar Airlines
- **Groupe ransomware:** TheGentlemen
- **Secteur:** Transport aérien
- **Site web:** www.madagascarairlines.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Madagascar Airlines est la compagnie aérienne nationale de la République de Madagascar.

### 18 Octobre 2025
#### 🇨🇩 Congo (RDC) - TK HOLDINGS GROUP
- **Groupe ransomware:** radar
- **Secteur:** Exploitation minière / Conglomérat
- **Site web:** https://congomineralservices.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 4
- **Description victime:** Holding congolais avec des activités dans le bois, la logistique et l'exploration minière.
- **Analyse:** AFRINTEL a examiné le classeur CTI fourni par l'analyste et 32 captures associées à la publication de radar. L'ensemble comprend sept catégories de documents : textes douaniers et juridiques de la RDC, documents de marchés publics et de gouvernance, politiques salariales et de recrutement de TK Holdings, rapport géologique de Congo Mineral Services concernant le projet d'exploration cuprifère Mikuba Mining, ainsi qu'un arrêté de contrôle environnemental. Le classeur classe la politique salariale et le rapport géologique Mikuba au niveau de sensibilité critique. Le rapport géologique mentionne des campagnes de forage et des teneurs en cuivre, ce qui crée un risque plausible d'espionnage industriel et de renseignement sur une ressource stratégique. Les politiques RH exposent des procédures internes relatives aux salaires, primes, congés, recrutement et confidentialité, avec des risques de ciblage des employés, d'abus interne et d'atteinte réputationnelle. Les documents juridiques et réglementaires pourraient faciliter la fraude documentaire, la corruption ou la manipulation des processus de conformité et d'importation si leur authenticité et leur validité étaient établies. Les éléments confirment l'affichage de documents apparemment sensibles, mais ne permettent pas de confirmer indépendamment le vecteur d'intrusion, l'exhaustivité du jeu publié, l'authenticité de chaque document ni l'impact opérationnel. AFRINTEL ne reproduit pas le contenu des documents, les noms, signatures ou autres informations sensibles.

### 18 Octobre 2025
#### 🇿🇦 Afrique du Sud - Université du Witwatersrand (WITS)
- **Groupe ransomware:** clop
- **Secteur:** Éducation (Université)
- **Site web:** https://www.wits.ac.za
- **Statut:** Data Fully Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Description victime:** L'Université du Witwatersrand, située à Johannesburg, est l'une des institutions de recherche les plus prestigieuses d'Afrique.
- **Analyse:** AFRINTEL a examiné une capture de la page de revendication du site de fuite de Clop pour wits.ac.za, utilisant le modèle standard de fiche victime du groupe (champs Headquarters, Phone, Website, Revenue et Industry). Contrairement aux pages examinées pour d'autres entrées africaines sur le même site de fuite, cette page inclut une section dédiée « Torrent Magnet Link » référençant wits.ac.za, indiquant que l'acteur a mis à disposition un jeu de données téléchargeable plutôt qu'une simple page de revendication. Le profil d'entreprise affiché (secteur Colleges & Universities, Education) est cohérent avec le profil public de l'Université du Witwatersrand. AFRINTEL n'a ni téléchargé ni examiné le contenu du torrent référencé ; le volume, le contenu et la sensibilité du jeu de données publié ne sont donc pas évalués de manière indépendante. La présence d'une section de lien magnet fonctionnelle, distincte des pages de simple revendication observées pour d'autres entrées, soutient une évaluation à confiance élevée selon laquelle des données ont bien été mises à disposition au téléchargement. Compte tenu du statut de WITS en tant qu'université de recherche majeure, un jeu de données confirmé pourrait inclure des données personnelles d'étudiants, de personnel ou de recherche, créant un risque de fraude à l'identité et de phishing ciblé visant la communauté universitaire. AFRINTEL ne reproduit ni le lien magnet, ni l'adresse du siège, ni le numéro de téléphone issus du matériel examiné.

### 19 Octobre 2025
#### 🇬🇦 Gabon - SANgel
- **Groupe ransomware:** qilin
- **Secteur:** Agroalimentaire
- **Site web:** https://sangel-gabon.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Entreprise gabonaise de production et de distribution alimentaire basée à Libreville, spécialisée dans les produits surgelés.

### 20 Octobre 2025
#### 🇪🇬 Égypte - Al Ahly Leasing & Factoring Company
- **Groupe ransomware:** BlackShrantac
- **Secteur:** Finance
- **Site web:** https://alahlyleasing.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Institution financière égyptienne spécialisée dans le crédit-bail et l'affacturage, filiale de la Banque Nationale d'Égypte.

### 20 Octobre 2025
#### Afrique du Sud - Companies and Intellectual Property Commission (CIPC) eServices
- **Acteur / Groupe:** fuckoverflow (claimed seller)
- **Secteur:** Government / Administration
- **Site web:** https://www.cipc.co.za/
- **Date de l'incident:** 20 octobre 2025 - date de la publication de vente d'accès rapportée
- **Date de publication initiale:** 20 octobre 2025
- **Statut:** Claim - Unverified Marketplace Listing
- **Type d'incident:** Access Sale
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 4
- **Description victime:** La Companies and Intellectual Property Commission gère les services sud-africains d'enregistrement des sociétés et de propriété intellectuelle.
- **Analyse:** Un acteur a annoncé la vente de comptes CIPC eServices prétendument compromis, permettant potentiellement la modification de dossiers et la collecte de données. CIPC n'a pas confirmé la validité de ces comptes dans l'audit fourni. AFRINTEL enregistre la revendication de marketplace avec une confiance moyenne et ne traite pas l'accès réussi comme indépendamment confirmé.
- **Type de source:** Secondary CTI + Marketplace Claim
- **Sources publiques:** [CyHawk Africa](https://cyhawk-africa.com/compromised-credentials/threat-actor-advertises-alleged-compromised-cipc-eservices-accounts-on-a-dark-web-forum/)

### 23 Octobre 2025
#### 🇲🇦 Maroc - STAR LÉGUMES
- **Groupe ransomware:** tengu
- **Secteur:** Commerce de gros (Produits alimentaires)
- **Site web:** https://starlegumes.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 3
- **Description victime:** Grossiste marocain en fruits, légumes, épices et graines séchées basé à Casablanca.
- **Analyse:** AFRINTEL a examiné la page du site de fuite ainsi qu'un échantillon local de documents cohérents avec la revendication du cybercriminel tengu. La page du site de fuite elle-même a été capturée (compteur de vues et indicateur de temps écoulé visibles), accompagnée d'un extrait du registre de commerce marocain (Tribunal de Commerce de Casablanca) confirmant l'identité juridique de l'entreprise, sa date d'immatriculation, son capital social, son adresse enregistrée et le nom de son gérant ; de plusieurs factures clients datées entre novembre 2021 et mars 2025 portant le numéro d'enregistrement ONSSA de l'entreprise, des noms de clients, adresses et montants de transaction ; ainsi qu'un export de grand livre comptable généré par le système (« Journal Factures Clients ») couvrant octobre 2024, imprimé en février 2025, listant environ 50 enregistrements de factures séquentielles avec noms de clients, numéros de facture et montants HT/TVA/TTC. Un tableau de synthèse analytique structuré construit à partir de ce matériel détaille par ailleurs un enregistrement d'identité légale, un échantillon de contacts clients (nom, identifiant fiscal/ICE, adresse) et un échantillon de factures. La combinaison d'une inscription officielle sur le site de fuite, d'un extrait de registre de commerce authentique, d'exports comptables générés par le système et datés, et d'une cohérence de marque interne entre documents couvrant plus de trois années, soutient une évaluation à très haute confiance d'une compromission réelle des systèmes de facturation et de comptabilité de Star Légumes. Compte tenu de l'ampleur des données de contacts clients et de transactions exposées, cet incident crée un risque de fraude fournisseur/client, de compromission de messagerie professionnelle et de revente de la base clients. AFRINTEL ne reproduit aucun nom de client, adresse, identifiant fiscal ni montant financier issu du matériel examiné.

### 24 Octobre 2025
#### 🇲🇦 Maroc - Le MULTI LABORATOIRE LC2A
- **Groupe ransomware:** tengu
- **Secteur:** Industrie pharmaceutique / Laboratoire
- **Site web:** https://multi-laboratoire-lc2a.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 2
- **Description victime:** Laboratoire marocain proposant une plateforme de configuration de projets analytiques pour les entreprises.
- **Analyse:** AFRINTEL a examiné un échantillon local de documents internes cohérents avec la revendication du cybercriminel tengu, adressés à LC2A ou générés par ce dernier. Le matériel examiné comprend un devis fournisseur d'un vendeur d'équipements de laboratoire (daté de mai 2022) adressé au service achats de LC2A, détaillant réactifs et équipements analytiques avec tarification unitaire et totale, ainsi qu'un journal interne de contrôle d'équipement (« Carte de contrôle des équipements », formulaire qualité référencé FOR06/PRT06) pour une balance de laboratoire, enregistrant des vérifications quotidiennes de calibration jusqu'en octobre 2021. Le nom de l'entreprise, les références de formulaires internes et la cohérence de marque entre les deux fichiers soutiennent une évaluation à confiance élevée selon laquelle l'échantillon provient des systèmes internes de LC2A plutôt que d'une revendication fabriquée. Un paquet de données volumineux référencé aux côtés de cet échantillon n'a pas terminé son transfert et n'a pas pu être examiné ; cette analyse se limite aux deux documents décrits ci-dessus. Compte tenu de la nature opérationnelle et fournisseur du matériel examiné, cet incident présente un risque modéré d'usurpation d'identité fournisseur et de divulgation des pratiques internes de contrôle qualité et d'approvisionnement, aucune donnée patient ou clinique n'ayant été observée dans l'échantillon examiné. AFRINTEL ne reproduit aucun nom de fournisseur, détail tarifaire, code équipement ni identifiant de personnel issu du matériel examiné.

### 24 Octobre 2025
#### 🇳🇬 Nigeria - Henrietta Ezeoke Law Firm
- **Groupe ransomware:** qilin
- **Secteur:** Services juridiques
- **Site web:** https://houstonwrongfuldeathlawyers.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Cabinet d'avocats nigérian.

### 28 Octobre 2025
#### 🇹🇿 Tanzanie - Alios Finance Group
- **Groupe ransomware:** incransom
- **Secteur:** Finance
- **Site web:** https://aliosfinance.co.tz
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Opérateur financier panafricain présent en Tanzanie, proposant des solutions de financement spécialisées. Lors de cette attaque, le groupe incransom a revendiqué l'exfiltration de 100 Go de données.

### 28 Octobre 2025
#### 🇹🇳 Tunisie - Alios Finance Group
- **Groupe ransomware:** incransom
- **Secteur:** Finance
- **Site web:** https://aliosfinance.tn
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Opérateur financier panafricain présent en Tunisie, spécialisé dans le financement des entreprises et des particuliers. Lors de cette intrusion, 100 Go de données ont été exfiltrés par le groupe incransom.

### 28 Octobre 2025
#### 🇰🇪 Kenya - M-TIBA / CarePay
- **Date de l'incident:** Octobre 2025 - date exacte de compromission non établie dans les sources publiques retenues
- **Date de publication initiale:** 28 octobre 2025
- **Acteur / Groupe:** Kazu (revendication)
- **Secteur:** Healthcare / Health Technology
- **Site web:** https://www.mtiba.com/
- **Statut:** Corroborated - Data Sample Independently Reviewed + Regulator Investigation
- **Type d'incident:** Data Leak
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** M-TIBA est une plateforme de technologies de santé opérée par CarePay au Kenya, utilisée pour la gestion de services, programmes et paiements liés à la santé.
- **Analyse:** Le 28 octobre 2025, TechCabal a rapporté une revendication du groupe Kazu concernant un accès non autorisé aux serveurs de M-TIBA. Kazu revendiquait plus de 17 millions de fichiers et environ 2,15 To de données, mais ces volumes globaux ne sont pas considérés comme indépendamment confirmés par AFRINTEL. TechCabal indique avoir examiné un échantillon de 2 Go contenant des données attribuées à environ 114 000 personnes, notamment des identités, numéros nationaux, dates de naissance, coordonnées téléphoniques et, dans certains cas, des informations médicales et de facturation. Le 29 octobre 2025, l'Office of the Data Protection Commissioner (ODPC) du Kenya a annoncé l'ouverture d'une enquête afin d'établir la nature et l'étendue de la violation possible. CarePay n'avait pas confirmé la fuite dans le premier article et avait demandé des éléments afin de conduire sa propre investigation. AFRINTEL retient donc le Data Leak sur la base de l'échantillon examiné indépendamment et de l'enquête réglementaire, tout en conservant comme revendiqués les volumes globaux annoncés par Kazu.
- **Type de source:** Independent Media Sample Review + Regulator Investigation
- **Sources publiques:** [TechCabal - Safaricom-backed M-Tiba hit by massive data breach exposing patient records](https://techcabal.com/2025/10/28/safaricom-backed-m-tiba-hacked-exposing-4-8-patient-records/) | [The Star - ODPC probes possible M-Tiba data breach](https://www.the-star.co.ke/news/2025-10-29-odpc-probes-possible-m-tiba-data-breach)

### 31 Octobre 2025
#### 🇩🇿 Algérie - TMF Logistics
- **Groupe ransomware:** incransom
- **Secteur:** Logistique
- **Site web:** https://tmf-logistics.com
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Description victime:** TMF Logistics est une entreprise algérienne spécialisée dans les solutions de transport et de logistique. Lors de cette attaque, le groupe incransom a revendiqué l'exfiltration de 39 Go de données sensibles de l'entreprise.
- **Analyse:** Des documents financiers et opérationnels internes examinés par AFRINTEL corroborent la revendication d'incransom. Un tableau de chiffre d'affaires par client de novembre 2024 recense une trentaine de clients professionnels de TMF Logistics, dont de grandes entreprises agroalimentaires et pharmaceutiques opérant en Algérie (par exemple Danone Algérie, l'Institut Pasteur d'Algérie, GlaxoSmithKline Algérie, Fromagerie Bel Algérie), ainsi que des catégories de prestations de transport frigorifique et général (frigo, bâché, plateau). Un export de facturation détaillée couvre des opérations de transport au niveau de chaque facture, réparties sur de nombreuses wilayas algériennes (dont Béjaïa, Bouira, Batna, Constantine, Djelfa, Ghardaïa, Ouargla et Tindouf), révélant un réseau de livraison à l'échelle nationale. Un document de décharge de livraison confirme l'identité officielle de l'entreprise : SPA TMF Logistics, basée dans la zone d'activité de Taharacht, Akbou (wilaya de Béjaïa), avec ses coordonnées enregistrées et ses références d'immatriculation professionnelle. La combinaison d'un portefeuille client national, de données de réseau de livraison et de références d'immatriculation crée un risque de chaîne d'approvisionnement (usurpation de client, fraude à la facturation, intelligence concurrentielle) qui dépasse la seule exposition opérationnelle de TMF Logistics.

### 31 Octobre 2025
#### 🇲🇦 Maroc - Institut Agronomique et Vétérinaire Hassan II (IAV Hassan II)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** DBhacker_BF
- **Secteur:** Éducation / Enseignement supérieur / Agronomie et sciences vétérinaires
- **Site web:** iav.ac.ma
- **Statut:** Claim - Data Sample Published
- **Description victime:** L'IAV Hassan II est un établissement public marocain de référence pour l'enseignement supérieur agronomique et vétérinaire, basé à Rabat. La base examinée contient 4 208 enregistrements de candidats et couvre les candidats et comprend nom complet, date et lieu de naissance, nationalité, genre, adresse, numéro de carte d'identité nationale (CIN), numéro de téléphone, adresse email, statut d'inscription, filière et un champ mot de passe (majoritairement vide dans l'échantillon examiné). La combinaison du CIN, des coordonnées et des données académiques crée un risque de fraude à l'identité, de phishing ciblé et d'abus de récupération de compte ; l'exhaustivité et l'origine du fichier n'ont pas été confirmées de manière indépendante.

### 31 Octobre 2025
#### 🇲🇦 Maroc - Ministère de l'Enseignement Supérieur, de la Recherche Scientifique et de l'Innovation (enssup.gov.ma)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** EternalRed
- **Secteur:** Gouvernement / Éducation / Enseignement supérieur
- **Site web:** enssup.gov.ma
- **Date de publication de la source :** 25 octobre 2025
- **Statut:** Claim - Data Sample Published
- **Description victime:** enssup.gov.ma est le Ministère marocain de l'Enseignement Supérieur, de la Recherche Scientifique et de l'Innovation. Le fichier texte fourni contient exactement 942 930 lignes, ce qui correspond au volume annoncé ; il s'agit d'une extraction nationale d'étudiants couvrant 942 930 enregistrements, avec des champs incluant le numéro de carte d'identité nationale (CIN), l'identifiant national étudiant (code Massar), le nom complet en arabe et en français, le genre, la date de naissance, la nationalité, le code et le nom de l'établissement, la filière et le niveau d'étude. Les métadonnées internes du fichier indiquent que l'extraction a été initialement compilée vers décembre 2022, bien qu'AFRINTEL l'ait examinée dans le cadre d'une collecte de données de 2025. L'ampleur et la structure du jeu de données indiquent une exposition nationale significative de dossiers d'étudiants de l'enseignement supérieur, créant des risques de fraude à l'identité et de phishing ciblé contre les étudiants et les établissements ; l'exhaustivité et la source exacte de l'extraction n'ont pas été confirmées de manière indépendante.

## Novembre 2025

### 04 Novembre 2025
#### 🇲🇦 Maroc - DOVERN Import
- **Groupe ransomware:** spacebears
- **Secteur:** Logistique
- **Site web:** https://dovern-import.com/
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Société d'importation basée au Maroc, spécialisée dans la distribution de vins fins, spiritueux et champagnes de prestige.

### 04 Novembre 2025
#### 🇿🇦 Afrique du Sud - Wannabees (wannabees.co.za)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** Unknown
- **Secteur:** Ressources humaines / Recrutement
- **Site web:** wannabees.co.za
- **Statut:** Claim - Data Sample Published
- **Description victime:** Wannabees semble être une plateforme sud-africaine de recrutement et d'emploi temporaire, d'après la structure et le contenu de la base de candidats examinée.
- **Analyse:** AFRINTEL a examiné deux fichiers identiques dans l'ensemble de preuves fourni (DB.txt et HoJmS, avec une correspondance SHA-256), contenant un export de cinq dossiers de candidats. Le schéma comprend des identifiants de candidats, des numéros d'identité nationale, des noms, adresses, numéros de téléphone, champs d'adresse email, dates de naissance, nationalité, historique d'emploi, profession actuelle, prétentions salariales et champs relatifs à la rémunération, ainsi qu'un champ de mot de passe. L'échantillon est structurellement cohérent avec une base de recrutement ou de gestion de personnel et contient des informations personnelles et professionnelles hautement sensibles. Les fichiers sont datés du 4 novembre 2025 dans le répertoire de preuve ; cette date est traitée comme date de découverte/de preuve et non comme une date confirmée de publication ou d'intrusion. Le matériel disponible n'identifie ni acteur, ni forum, ni méthode d'accès, ni volume complet du jeu de données. AFRINTEL classe donc le cas comme une revendication de fuite avec échantillon publié et ne reproduit aucun nom, numéro d'identité, contact, mot de passe ni autre donnée personnelle brute.

### 05 Novembre 2025
#### 🇨🇮 Côte d'Ivoire - Anka (Anka.africa)
- **Acteur / Groupe:** Spirigatito
- **Secteur:** Logistique
- **Site web:** https://www.anka.africa/
- **Statut:** Claim - Data Sample Published
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Type d'incident:** Data Leak
- **Description victime:** Plateforme ivoirienne leader facilitant l'exportation, les paiements et la logistique pour les créateurs et commerçants africains vers le marché mondial.
- **Analyse:** La publication sur le forum annonce la vente d'une base de données attribuée à Anka, revendiquant 537 877 utilisateurs uniques et un volume de 12,1 Go, avec une liste de champs annoncée comprenant id, username, fullname, email, token, avatar, gender, date de naissance et téléphone, entre autres. AFRINTEL a examiné des extraits structurés dérivés de l'échantillon publié avec le post, comprenant un petit nombre d'enregistrements utilisateurs individuels (moins de 30). Le schéma examiné correspond à la liste de champs annoncée dans la publication, en l'étendant avec des attributs supplémentaires : date de dernière connexion, indicateurs de verrouillage et de suppression de compte, type de compte, nombre et montant des achats, solde du portefeuille, et champs de ventes vendeur sur la marketplace. Les enregistrements examinés montrent des horodatages de création de compte s'étalant de mai 2017 à mai 2024, des devises incluant l'EUR, l'USD et le GMD, et des paramètres régionaux en français et en anglais, cohérents avec une base d'utilisateurs internationale pour une plateforme africaine de commerce transfrontalier et de paiements. La cohérence structurelle entre la liste de champs annoncée et l'échantillon examiné, ainsi que la plausibilité des valeurs enregistrées (horodatages sur plusieurs années, devises mixtes, paramètres régionaux mixtes), permettent de faire passer ce cas d'une revendication non vérifiée à une revendication accompagnée d'un échantillon de données publié. AFRINTEL n'a pas vérifié indépendamment le volume total revendiqué de 537 877 utilisateurs / 12,1 Go, l'origine ou la méthode de compromission, ni l'affirmation distincte de l'acteur selon laquelle la plateforme génère 10 millions de dollars de revenus. L'exposition de ce jeu de données combinerait noms complets, coordonnées, dates de naissance, genre, jetons de compte et informations de portefeuille/achats, créant un risque significatif de prise de contrôle de comptes, de phishing ciblé et de fraude financière visant les utilisateurs de la plateforme. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone, jeton, nom d'utilisateur ni autre enregistrement individuel issu de l'échantillon examiné.

### 06 Novembre 2025
#### 🇪🇬 Égypte - ELSEWEDYELECTRIC.COM
- **Groupe ransomware:** clop
- **Secteur:** Technologies / Industrie
- **Site web:** www.elsewedyelectric.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 2
- **Description victime:** Principal fabricant égyptien de câbles, de systèmes électriques et de produits d'ingénierie.
- **Analyse:** AFRINTEL a examiné une capture de la page de revendication du site de fuite de Clop pour elsewedyelectric.com, utilisant le modèle standard de fiche victime du groupe (champs Headquarters, Phone, Website, Revenue et Industry, suivis du texte d'avertissement récurrent du groupe). Le profil d'entreprise affiché (chiffre d'affaires d'environ 4,9 milliards de dollars, secteur manufacturing/wire & cable) est cohérent avec le profil public connu d'Elsewedy Electric en tant que grand fabricant égyptien de câbles et de systèmes électriques. Cette fiche apparaissait aux côtés de nombreuses autres organisations multinationales sur la même page du site de fuite de Clop, cohérent avec la campagne d'exploitation de masse du groupe visant les clients d'Oracle E-Business Suite révélée en 2025. La correspondance du profil d'entreprise soutient une évaluation à confiance moyenne quant à l'authenticité de la fiche, bien qu'AFRINTEL n'ait examiné aucun fichier exfiltré sous-jacent, lien magnet ou échantillon de données au-delà de la page de revendication elle-même ; l'ampleur, le volume et la sensibilité des données réellement détenues par l'acteur restent non vérifiés. AFRINTEL ne reproduit ni l'adresse du siège ni le numéro de téléphone de l'entreprise issus du matériel examiné.

### 06 Novembre 2025
#### 🇿🇲 Zambie - ZANACO.CO.ZM
- **Groupe ransomware:** clop
- **Secteur:** Services financiers (Banque)
- **Site web:** www.zanaco.co.zm
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** Zambia National Commercial Bank, l'une des principales banques commerciales de Zambie.
- **Analyse:** AFRINTEL a examiné des captures de la page de revendication du site de fuite de Clop pour zanaco.co.zm, incluant la barre de navigation du groupe montrant cette fiche aux côtés de nombreuses autres organisations multinationales (parmi lesquelles Logitech, The Washington Post, Trimble et Elsewedy Electric), cohérent avec la campagne d'exploitation de masse de Clop visant les clients d'Oracle E-Business Suite révélée en 2025. Le profil d'entreprise affiché (chiffre d'affaires d'environ 337,9 millions de dollars, secteur finance/banking) est cohérent avec le profil public connu de la Zambia National Commercial Bank. La fiche utilise le même modèle standard et le même texte d'avertissement récurrent observés sur d'autres pages victimes de Clop, ce qui soutient une évaluation à confiance moyenne quant à l'authenticité de l'entrée, bien qu'AFRINTEL n'ait examiné aucun fichier exfiltré sous-jacent, lien magnet ou échantillon de données au-delà des pages de revendication ; l'ampleur, le volume et la sensibilité des données clients ou bancaires réellement détenues par l'acteur restent non vérifiés. Compte tenu du rôle de ZANACO en tant que banque commerciale majeure, toute exposition de données confirmée présenterait un risque important de fraude financière et de phishing ciblé visant sa clientèle. AFRINTEL ne reproduit ni l'adresse du siège ni le numéro de téléphone de la banque issus du matériel examiné.

### 06 Novembre 2025
#### 🇲🇦 Maroc - www.marjane.ma
- **Groupe ransomware:** stormous
- **Secteur:** Commerce de détail / Grande distribution / E-commerce.
- **Site web:** www.marjane.ma
- **Statut:** Data Fully Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** Groupe Marjane est le plus grand groupe marocain de grande distribution, exploitant des hypermarchés et supermarchés.
- **Analyse:** AFRINTEL a examiné une capture de preuve publiée en lien avec la revendication du cybercriminel stormous, montrant une session active sur un portail SSL-VPN Fortinet daté du 10 novembre 2025. La liste de favoris du portail référence une infrastructure interne cohérente avec l'environnement de Marjane, incluant un sous-domaine marjane.ma, une instance de wiki Confluence hébergée sous un sous-domaine confluence.marjane, un favori de collaboration intitulé « huddle/Store Managers » cohérent avec la gestion multi-magasins de l'enseigne, ainsi qu'un favori d'accès SSH direct vers un hôte interne. La présence de noms d'hôtes internes spécifiques à Marjane et d'un point d'accès SSH fonctionnel soutient une évaluation à confiance élevée selon laquelle la capture reflète un accès réel au réseau interne plutôt qu'une preuve fabriquée. À la suite de cet échantillon initial, l'acteur aurait publié l'intégralité du jeu de données revendiqué sur son site de fuite ; AFRINTEL n'a pas pu collecter ni examiner cette publication ultérieure, dont le contenu, le volume et l'authenticité ne sont donc pas évalués de manière indépendante. L'accès interne démontré, au niveau VPN et SSH, au réseau du plus grand groupe de grande distribution du Maroc crée un risque dépassant toute catégorie de données isolée, incluant une perturbation potentielle ou une compromission supplémentaire des systèmes de point de vente, de logistique et de gestion des magasins à l'échelle du réseau de succursales de Marjane. AFRINTEL ne reproduit aucun identifiant, jeton de session, adresse IP ni nom d'hôte interne issu du matériel examiné.

### 08 Novembre 2025
#### 🇲🇦 Maroc - NARSA (Agence Nationale de la Sécurité Routière)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** anisanas2
- **Secteur:** Gouvernement / Transport / Sécurité routière
- **Site web:** Non identifié avec certitude
- **Statut:** Claim - Data Sample Published
- **Description victime:** La NARSA est l'agence nationale marocaine chargée de la sécurité routière, de l'immatriculation des véhicules et du contrôle technique.
- **Analyse:** AFRINTEL a examiné un export CSV structuré correspondant à un ensemble d'enregistrements d'immatriculation de véhicules, avec des champs incluant le nom complet du propriétaire, l'adresse, le numéro de carte d'identité nationale (CIN), la marque du véhicule, la catégorie, le type, le numéro de châssis, la cylindrée, les dates du centre d'immatriculation et de mise en circulation, le prix d'achat et le numéro de plaque d'immatriculation. La taille de l'échantillon et la structure des champs sont cohérentes avec le jeu de données revendiqué d'environ 150 000 lignes, bien qu'AFRINTEL n'ait pas pu confirmer de manière indépendante l'identité de l'acteur revendicateur ni l'ampleur totale exacte à partir du matériel examiné. La combinaison de numéros de CIN, d'adresses personnelles et de données d'identification de véhicules crée un risque de fraude à l'identité, de fraude liée aux véhicules (y compris de faux documents d'immatriculation) et de risques pour la sécurité physique liés à l'exposition d'adresses. AFRINTEL ne reproduit aucun nom de propriétaire, adresse, numéro de CIN ni numéro de plaque issus de l'échantillon examiné.

### 09 Novembre 2025
#### 🇿🇦 Afrique du Sud - Eastern Cape Department of Human Settlements (ECDHS)
- **Groupe ransomware:** nightspire
- **Secteur:** Administrations publiques/ Logement social.
- **Site web:** ecdhs.gov.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Le Département des Établissements Humains du Cap Oriental sud-africain est l'organe provincial chargé de la politique du logement, de l'aménagement urbain et de l'accès à la propriété pour les populations vulnérables en Afrique du Sud.

### 09 Novembre 2025
#### 🇳🇬 Nigeria - Fidelity Pension Managers, Nigeria
- **Groupe ransomware:** nightspire
- **Secteur:** Services financiers (Gestion de pension)
- **Site web:** fidelitypensionmanagers.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Gestionnaire de fonds de pension nigérian.

### 11 Novembre 2025
#### 🇪🇬 Égypte - Samcrete Holding
- **Groupe ransomware:** clop
- **Secteur:** Construction
- **Site web:** www.samcrete.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Samcrete Holding est une société entièrement intégrée d'ingénierie, de sous-traitance, de développement, de fabrication et d'investissement créée en 1963.

### 17 Novembre 2025
#### Kenya - Multiple Government of Kenya websites
- **Acteur / Groupe:** PCP@Kenya (preliminary government attribution)
- **Secteur:** Government / Administration
- **Site web:** Multiple government domains
- **Date de l'incident:** 17 novembre 2025 - date de l'incident confirmée publiquement par les autorités kényanes
- **Date de publication initiale:** 17 novembre 2025
- **Statut:** Government Confirmed + Preliminary Actor Attribution
- **Type d'incident:** Defacement
- **Niveau de confiance:** Very High
- **Niveau d'impact:** Level 4
- **Description victime:** L'incident a affecté plusieurs sites du gouvernement kényan couvrant des ministères, State House et des agences publiques.
- **Analyse:** Les autorités kényanes ont confirmé que le 17 novembre 2025 un incident de cybersécurité avait rendu temporairement indisponibles plusieurs sites gouvernementaux, tandis que les informations contemporaines documentaient des messages de défacement sur plusieurs ministères et agences. Les premières investigations pointaient vers un groupe se présentant sous le nom PCP@Kenya. AFRINTEL enregistre un seul incident de Defacement coordonné multi-organismes, conserve PCP@Kenya comme attribution préliminaire et ne déduit pas de vol de données.
- **Type de source:** Government Confirmation + Public Media
- **Sources publiques:** [The Star - restoration statement](https://www.the-star.co.ke/news/2025-11-17-state-websites-restored-after-cyber-breach) | [The Star - affected sites](https://www.the-star.co.ke/news/2025-11-17-hackers-take-down-key-government-websites)

### 25 Novembre 2025
#### 🇪🇬 Égypte - LAMAICA, Egypt
- **Groupe ransomware:** nightspire
- **Secteur:** Industrie manufacturière du bois et des matériaux de construction.
- **Site web:** lamaica.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** LAMAICA est l'un des leaders du marché égyptien dans la production de panneaux de particules mélaminés, de stratifiés haute pression (HPL), de bandes de chant et de composants pour l'ameublement.

### 26 Novembre 2025
#### 🇪🇬 Égypte - Arabia Holding
- **Groupe ransomware:** qilin
- **Secteur:** Immobilier / Investissement / Développement Urbain.
- **Site web:** arabia-holding.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Holding égyptienne avec des intérêts dans divers secteurs, dont l'immobilier et la gestion.

### 26 Novembre 2025
#### 🇨🇮 Côte d'Ivoire - Santé Espoir Vie Côte d’Ivoire (SEV-CI)
- **Groupe ransomware:** benzona
- **Secteur:** Santé / ONG / Humanitaire.
- **Site web:** sevci.org
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Santé Espoir Vie Côte d’Ivoire (SEV-CI) est une organisation non gouvernementale ivoirienne de premier plan. Elle œuvre pour l'amélioration de la santé des populations, avec un focus particulier sur la lutte contre le VIH/SIDA, la tuberculose, et le renforcement des systèmes de santé communautaires.

### 30 Novembre 2025
#### 🇲🇦 Maroc - Joutech
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** RL000
- **Secteur:** Technologie / Services numériques (activité exacte non confirmée de manière indépendante)
- **Site web:** joutech.ma
- **Statut:** Claim - Data Sample Published
- **Description victime:** Joutech est une entreprise marocaine exploitant le domaine joutech.ma. Le fichier examiné est un export de liste de diffusion/contacts de 1 350 enregistrements, contenant civilité, prénom, nom, adresse email, champ société, indicateurs marketing/ventes et date d'inscription. Aucun mot de passe ni donnée financière n'a été observé dans l'échantillon examiné. Cette exposition pourrait faciliter des campagnes de phishing ciblé et de spam contre les contacts listés ; l'exhaustivité et l'origine du fichier n'ont pas été confirmées de manière indépendante.

## Décembre 2025

### 05 Décembre 2025
#### 🇪🇬 Égypte - 3S Software (Secured Smart Systems Overview Metrics)
- **Groupe ransomware:** dragonforce
- **Secteur:** Technologies
- **Site web:** 3s-software.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Prestataire de services technologiques égyptien spécialisé dans le développement de logiciels.

### 05 Décembre 2025
#### 🇿🇲 Zambie - National Health Insurance Management Authority
- **Groupe ransomware:** nova
- **Secteur:** Assurances (Santé)
- **Site web:** https://nhima.co.zm/
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Autorité zambienne gérant le régime national d'assurance maladie.

### 06 Décembre 2025
#### 🇬🇭 Ghana - Kasapreko Company Limited
- **Groupe ransomware:** qilin
- **Secteur:** Agroalimentaire / Boissons (Alcoolisées et non alcoolisées).
- **Site web:** www.kasapreko.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Kasapreko est l'un des plus grands fabricants de boissons au Ghana et un acteur majeur à l'exportation dans toute la région CEDEAO.

### 06 Décembre 2025
#### 🇿🇦 Afrique du Sud - Diesel Electric
- **Groupe ransomware:** qilin
- **Secteur:** Distribution automobile / Équipement de diagnostic
- **Site web:** diesel-electric.co.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Diesel-Electric est l'un des plus grands distributeurs d'Afrique du Sud spécialisé dans les composants automobiles, les systèmes d'injection diesel et l'équipement de diagnostic (partenaire majeur de Bosch).

### 07 Décembre 2025
#### 🇪🇬 Égypte - incolease.com
- **Groupe ransomware:** lockbit5
- **Secteur:** Finance
- **Site web:** www.incolease.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Société de leasing égyptienne.

### 07 Décembre 2025
#### 🇿🇦 Afrique du Sud - elundini.gov.za
- **Groupe ransomware:** lockbit5
- **Secteur:** Administration Publique / Gouvernement Local.
- **Site web:** elundini.gov.za
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** La Municipalité locale d'Elundini est une autorité administrative clé située dans le district de Joe Gqabi (Cap oriental), englobant les villes de Maclear, Ugie et Mount Fletcher.

### 08 Décembre 2025
#### 🇪🇬 Égypte - Arkan
- **Groupe ransomware:** ransomhouse
- **Secteur:** Finance / Commerce
- **Site web:** arkanonline.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Conglomérat égyptien, Arkan Group, actif dans l'industrie, l'agriculture et le commerce de gros.

### 11 Décembre 2025
#### 🇳🇬 Nigeria - Leadway Assurance / Leadway Health
- **Groupe ransomware:** kazu
- **Secteur:** Assurances
- **Site web:** leadwayhealth.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Leadway Assurance est la plus grande compagnie d'assurance privée au Nigeria.

### 12 Décembre 2025
#### 🇹🇳 Tunisie - Hopital La Rabta (Centre Hospitalier Universitaire)
- **Groupe ransomware:** devman
- **Secteur:** Santé
- **Site web:** www.chularabta.tn
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** L'Hôpital La Rabta est l'un des plus grands pôles hospitaliers de Tunisie.

### 15 Décembre 2025
#### 🇹🇳 Tunisie - Société Tunisienne de Radiologie (strtn.org)
- **Groupe ransomware:** nova
- **Secteur:** Santé / Association Médicale / Éducation.
- **Site web:** strtn.org
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** La Société Tunisienne de Radiologie (STR) est l'organisme de référence pour les radiologues en Tunisie.

### 22 Décembre 2025
#### 🇪🇬 Égypte - Polaris Parks
- **Groupe ransomware:** direwolf
- **Secteur:** Développement Immobilier / Gestion de Parcs Industriels et de Loisirs.
- **Site web:** polarisparks.com
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Polaris Parks est l'un des principaux développeurs de parcs industriels privés en Égypte.

### 24 Décembre 2025
#### 🇿🇦 Afrique du Sud - National Credit Regulator (NCR)
- **Groupe ransomware:** dragonforce
- **Secteur:** Administrations publiques (Régulation financière)
- **Site web:** www.ncr.org.za
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Ransomware
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** Organisme public sud-africain chargé de réguler le secteur du crédit à la consommation.
- **Analyse:** AFRINTEL a examiné un échantillon local de documents associés à cette revendication. Le matériel comprend environ 25 dossiers de cas consommateurs nommés individuellement, cohérents avec des dossiers de réexamen de dette/conseil en désendettement traités par le NCR, une vingtaine d'emails référençant des individus nommés accompagnés d'identifiants partiels ressemblant à des préfixes de date de naissance de numéros d'identité sud-africains, ainsi qu'un mémo d'enquête interne daté du 24 juin 2022, adressé par le responsable du service Plaintes du NCR au responsable par intérim des Enquêtes et de l'Application de la réglementation, ouvrant une enquête sur une entité désignée « Debt Accord Solutions » soupçonnée d'exercer comme conseiller en désendettement non enregistré. L'échantillon comprend également un tableur administratif interne suivant les volumes d'emails liés aux dossiers sur une base quasi quotidienne à mensuelle d'août 2020 à décembre 2024, des fichiers logo à l'image du NCR, des formulaires réglementaires (dont un Form 29 et un document de consentement écrit au titre du Règlement 50(5)), un document de mandat et un relevé de coordonnées bancaires. Les documents sont cohérents avec l'image de marque du NCR, sa structure organisationnelle (responsables et services nommés) et le format de ses dossiers réglementaires. L'échantillon indique une exposition de dossiers consommateurs de réexamen de dette, de documents d'enquête et d'application de la réglementation, ainsi que de données opérationnelles pluriannuelles, créant un risque significatif de fraude à l'identité et de phishing ciblé contre des consommateurs nommés et des agents du NCR, ainsi qu'un risque d'interférence avec des enquêtes réglementaires en cours. AFRINTEL ne reproduit aucun nom de consommateur, identifiant, contenu de dossier, nom d'agent ni détail d'enquête issus du matériel examiné.

### 26 Décembre 2025
#### 🇹🇳 Tunisie - Hopital La Rabta (deuxième revendication ransomware)
- **Groupe ransomware:** qilin
- **Secteur:** Santé
- **Site web:** www.chularabta.tn
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** L'Hôpital La Rabta est l'un des plus grands pôles hospitaliers de Tunisie.
- **Analyse:** AFRINTEL avait déjà enregistré une revendication contre ce même hôpital par devman le 12 décembre 2025. Cette seconde revendication, publiée deux semaines plus tard par un acteur différent, pourrait refléter soit une intrusion distincte réelle, soit une republication/revente de la revendication précédente ; AFRINTEL n'a pas pu confirmer de manière indépendante quel scénario s'applique.

### 26 Décembre 2025
#### 🇿🇼 Zimbabwe - Proplastics Limited (deuxième revendication ransomware)
- **Groupe ransomware:** lockbit5
- **Secteur:** Industrie manufacturière (Plastiques)
- **Site web:** proplastics.co.zw
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Description victime:** Proplastics Limited est le principal fabricant et fournisseur de systèmes de tuyauterie en plastique (PVC, PEHD) au Zimbabwe.
- **Analyse:** AFRINTEL avait déjà enregistré une revendication contre cette même entreprise par TheGentlemen le 9 septembre 2025. Cette seconde revendication, publiée environ trois mois et demi plus tard par un acteur différent, pourrait refléter soit une intrusion distincte réelle, soit une republication/revente de la revendication précédente ; AFRINTEL n'a pas pu confirmer de manière indépendante quel scénario s'applique.

### 26 Décembre 2025
#### 🇪🇬 Égypte - Yalla Tager Marketplace
- **Acteur / Groupe:** Habibi
- **Secteur:** Commerce / E-commerce
- **Site web:** yallatager.com
- **Date de l'incident:** Inconnue
- **Date de publication initiale:** 26 décembre 2025
- **Statut:** Claim - Data Sample Published
- **Type d'incident:** Data Leak
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 3
- **Description victime:** Yalla Tager Marketplace est l'organisation explicitement nommée dans la publication du forum et associée au domaine `yallatager.com`. La publication présente le jeu de données comme un fichier CSV de 2025 contenant environ 20 000 utilisateurs.
- **Analyse:** Le 26 décembre 2025, l'acteur `Habibi` a publié sur un forum une entrée intitulée **« Yalla Tager Marketplace - Database »** et présenté un jeu de données CSV attribué à `yallatager.com`. Le schéma annoncé comprend des identifiants internes, noms, adresses email, codes clients, noms de boutiques, groupes de clients, numéros de téléphone, centres d'intérêt, champs postaux et géographiques, un horodatage `Customer Since` ainsi que le canal web d'origine. AFRINTEL a examiné la publication fournie et un extrait textuel comprenant **23 enregistrements visibles**. L'échantillon est structurellement cohérent avec des fiches clients et commerçants d'une marketplace égyptienne : plusieurs entrées indiquent l'Égypte ainsi que des gouvernorats/villes égyptiens, certains numéros utilisent l'indicatif national `+20`, et certains profils sont identifiés comme commerçants de gros avec des informations liées à leur boutique. Les valeurs `Customer Since` visibles dans l'extrait comprennent des dates de juillet 2025 ; il s'agit d'horodatages de compte/client et **elles ne permettent pas d'établir la date de compromission ou d'extraction**. Le volume global revendiqué d'environ **20 000 utilisateurs** ne peut pas être vérifié à partir de l'échantillon fourni. Le vecteur d'accès initial, le système source, la date d'extraction, l'exhaustivité du jeu de données et toute confirmation officielle restent inconnus. La combinaison identité, coordonnées, localisation et profil commerçant crée un risque crédible de phishing ciblé, smishing, usurpation et fraude. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone, adresse de boutique ni autre donnée personnelle issue de l'échantillon.

### 29 Décembre 2025
#### 🇩🇿 Algérie - Université d'Oran 1 Ahmed Ben Bella
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** GhostVector
- **Secteur:** Éducation / Université
- **Site web:** Non précisé
- **Date de publication de la source :** 29 décembre 2025
- **Statut:** Claim - Data Sample Published
- **Description victime:** L'Université d'Oran 1 Ahmed Ben Bella est un établissement public d'enseignement supérieur situé à Oran, en Algérie. Le post fourni annonce une base datée de 2023 comprenant environ 58 000 enregistrements et des champs incluant les noms, dates de naissance, numéros de téléphone, genre, adresses e-mail, hachages de mots de passe et nationalité.
- **Analyse:** Le post affiche un échantillon structuré associé à l'université et identifie GhostVector comme compte source. Si elles étaient valides, ces données pourraient permettre des fraudes à l'identité, du phishing et des attaques ciblant les comptes d'étudiants ou de personnel. Aucun enregistrement personnel, identifiant, hachage ou coordonnée n'est reproduit ; la revendication et la provenance du jeu de données n'ont pas été confirmées indépendamment.

### 29 Décembre 2025
#### 🇪🇬 Égypte - 100 Watt Plast (100wattplast.com)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** camillabf
- **Secteur:** Industrie / Fabrication de produits électriques et plastiques
- **Site web:** [100wattplast.com](https://100wattplast.com)
- **Statut:** Claim - Data Sample Published
- **Description victime:** 100 Watt Plast est une entreprise industrielle basée en Égypte, avec des activités également au Liban et en Arabie saoudite, spécialisée dans la fabrication de produits électriques et plastiques.
- **Analyse:** L'acteur camillabf a publié le 29 décembre 2025 une revendication concernant 100wattplast.com, décrite comme un jeu de données de 180 000 enregistrements au format CSV, comprenant prénom, nom, email, téléphone et mot de passe. L'échantillon affiché dans le post montre un schéma de champs incluant deux valeurs de mot de passe par enregistrement : un hachage de type MD5 (32 caractères hexadécimaux) et une seconde valeur nettement plus complexe et de longueur variable, ainsi que trois champs supplémentaires non documentés (`aa`, `bb`, `already`).

  Une vingtaine d'enregistrements complets sont directement visibles dans l'échantillon, avec des noms, adresses email et numéros de téléphone égyptiens associés aux deux valeurs de mot de passe. La cohérence du schéma et le volume d'enregistrements individuels observés appuient un niveau de confiance élevé quant à l'authenticité de cette fuite, bien que le volume total de 180 000 lignes revendiqué n'ait pas pu être vérifié indépendamment au-delà de l'échantillon observé, et que la nature exacte du second champ de mot de passe (hachage alternatif ou valeur en clair) n'ait pas pu être déterminée avec certitude. L'exposition de ces données pourrait faciliter la prise de contrôle de comptes, la réutilisation de mots de passe sur d'autres services et le phishing ciblé contre les clients de l'entreprise. AFRINTEL ne reproduit aucun nom, adresse email, numéro de téléphone ni valeur de mot de passe issus de l'échantillon examiné.

### 31 Décembre 2025
#### 🇲🇦 Maroc - Pharmacie.ma
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** KaruHunters
- **Secteur:** Santé / E-commerce pharmaceutique
- **Site web:** pharmacie.ma
- **Statut:** Claim - Data Sample Published
- **Description victime:** Pharmacie.ma est une plateforme marocaine d'annuaire et de commerce électronique dédiée aux pharmacies. Deux sauvegardes SQL complètes, datées de septembre 2025, ont été examinées, couvrant l'ensemble du schéma applicatif de la plateforme (clients, adresses, médicaments, pharmaciens, newsletters, articles et tables associées). La structure de la table `clients` indique jusqu'à environ 27 900 comptes enregistrés (pharmaciens, médecins, personnel officinal, étudiants en pharmacie et autres utilisateurs) avec adresse email, mot de passe haché, nom, adresse professionnelle, ville, spécialité, numéros de téléphone/mobile, pays et date de naissance. Le volume et la structure des sauvegardes indiquent une exposition significative de comptes professionnels du secteur de la santé ; l'exhaustivité de l'extraction et son origine n'ont pas été confirmées de manière indépendante.

### 31 Décembre 2025
#### 🇰🇪 Kenya - Kenya Electricity Transmission Company (KETRACO)
- **Type d'incident:** Data Leak
- **Acteur / Groupe:** LindaBF
- **Secteur:** Énergie / Transport d'électricité (Infrastructure critique)
- **Site web:** [ketraco.co.ke](https://ketraco.co.ke)
- **Statut:** Claim - Data Sample Published
- **Description victime:** La Kenya Electricity Transmission Company (KETRACO) est une entreprise publique kényane chargée du développement, de l'exploitation et de la maintenance du réseau national de transport d'électricité haute tension.
- **Analyse:** L'acteur LindaBF a publié le 31 décembre 2025 un post intitulé « ketraco.co.ke database Kenya », le lien de téléchargement étant réservé aux membres du forum ayant répondu au fil de discussion. L'échantillon visible montre un export structuré d'un annuaire d'utilisateurs (champs USER_ID, USER_NAME, USER_PASSWORD, USER_FIRSTNAME, USER_LASTNAME, USER_EMAIL, USER_LASTLOGIN, USER_FLAGS, USER_OU, USER_DATECREATED) associé à une unité organisationnelle nommée « nl_KETRACO_Newsletter_Unit », cohérent avec une liste de comptes d'abonnés à une newsletter ou d'un service d'annuaire plutôt qu'avec des systèmes opérationnels critiques. Des noms, adresses email et horodatages de création de compte kényans d'apparence réaliste sont visibles, mais de nombreuses lignes de l'échantillon partagent une valeur de mot de passe identique, ce qui est incohérent avec des empreintes générées individuellement par utilisateur et pourrait indiquer une valeur par défaut partagée, un espace réservé, ou un échantillon partiellement fabriqué ; cette anomalie ramène le niveau de confiance d'AFRINTEL à un niveau moyen. Compte tenu du rôle de KETRACO dans l'infrastructure nationale de transport d'électricité, toute compromission confirmée, même limitée à un service de newsletter ou d'annuaire, serait préoccupante pour un opérateur d'infrastructure critique et pourrait indiquer un point d'accès plus large. AFRINTEL ne reproduit aucun nom d'utilisateur, adresse email, valeur de mot de passe ni enregistrement de l'échantillon, et n'a pas accédé au lien de téléchargement.

---

*Compilation AFRINTEL - source unique : fichiers mensuels.*

