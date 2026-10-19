![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en septembre 2026 (41 fiches)

👉🏾 [**English version available here**](./victims.md)

## Septembre 2026

**Statut du suivi mensuel : In Progress / En cours** - corpus de 41 fiches ; des découvertes tardives supplémentaires peuvent encore être intégrées.

> **Mise à jour de vérification OSINT  -  18 octobre 2026.** Ces 41 fiches constituent un **corpus de suivi intégré en septembre**, et non 41 cyberattaques survenues au cours de septembre. **13 fiches** documentent un incident confirmé ou corroboré chez la victime (dont RelyComply et le ministère namibien de la Défense), **2 fiches** correspondent à une exposition de données indirecte reconnue (Hollard et Guardrisk : intrusion chez la victime directe non démontrée) et **26** restent des revendications ou échantillons non confirmés indépendamment. Les statuts distinguent confirmation d’incident, attribution à un groupe, volume revendiqué, chiffrement et exfiltration. Les absences de confirmation désignent les sources publiques identifiées à la date du contrôle, non une preuve d’absence d’incident.


### 03 septembre 2026
#### 🇳🇬 Nigéria - Medical and Dental Council of Nigeria (MDCN)

- **Date de publication initiale :** 3 septembre 2026 à 20:19 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** cattier (compte de forum affiché ; identité non vérifiée)
- **Secteur :** Santé / Régulation des professions médicales et dentaires
- **Site web :** [mdcn.gov.ng](https://www.mdcn.gov.ng/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Medium (publication et extrait structurés observés ; origine et étendue non corroborées)
- **Niveau d'impact :** Level 3

- **Description :** Le **Medical and Dental Council of Nigeria (MDCN)** est l'organisme réglementaire nigérian chargé d'encadrer l'exercice de la médecine et de la chirurgie dentaire. Ses missions statutaires comprennent la fixation des normes professionnelles, la tenue des registres de praticiens et les procédures d'inscription et de licence. Son portail traite donc des informations relatives à l'identité, à la qualification et au statut professionnel de soignants ([missions officielles du MDCN](https://mdcn.gov.ng/page/about-us/our-role)).

- **Vérification indépendante au 18 octobre 2026 :** Aucune déclaration du MDCN ni notification réglementaire corroborant l’accès non autorisé ou les 65 580 personnes revendiquées n’a été identifiée. La capture et les 50 lignes analysées par AFRINTEL corroborent la présentation de données, non la compromission technique de l’institution.

  **Incident documenté dans la fiche AFRINTEL :** Un compte nommé cattier a publié une offre intitulée « Medical and Dental Council of Nigeria 65K » et attribue au domaine `mdcn.gov.ng` des données concernant **65 580 utilisateurs uniques**. Un extrait de dossiers de professionnels de santé est visible et **50 lignes ont été communiquées en texte**. Ces éléments établissent l'existence de la publication et la nature des données présentées ; ils ne confirment ni que 65 580 personnes distinctes sont concernées, ni une intrusion dans les systèmes du MDCN.

- **Analyse :**

  **Observed :** La publication datée du **3 septembre 2026** affiche le domaine `mdcn.gov.ng`, le chiffre **65 580** et une liste de **24 champs** couvrant identité, naissance, coordonnées, numéro de registre professionnel, origine et lieu de pratique, spécialisation, école médicale, emploi et date de demande. Les **50 lignes communiquées** suivent globalement cette structure et contiennent des informations personnelles et professionnelles ; elles ne sont pas assimilées à 50 personnes uniques vérifiées. Les dates de demande visibles se concentrent entre le **28 octobre et le 1er novembre 2022** ; il s'agit de dates de dossier, pas de dates d'incident. Le domaine appartient bien au [conseil médical et dentaire nigérian](https://www.mdcn.gov.ng/), qui gère l'inscription et les licences professionnelles.

  **Assumption :** Les intitulés de champs et le contenu des lignes sont compatibles avec des dossiers d'inscription ou de licence de praticiens. Cette cohérence soutient une association plausible avec l'écosystème MDCN, sans démontrer que les données proviennent directement d'un système compromis du conseil : une copie antérieure, un prestataire, une agrégation ou une autre source ne peuvent être écartés. Le champ d'âge paraît refléter une période plus récente que les dates de demande de 2022 pour certaines lignes ; sa méthode de calcul reste inconnue.

  **Unknown :** le fichier source, son empreinte et son nombre réel d'enregistrements, les doublons, l'exactitude et l'actualité des données, la méthode d'acquisition, l'existence d'un accès non autorisé, le nombre de personnes concernées, la validation des **65 580 utilisateurs uniques**, une confirmation du MDCN ou d'une autorité et tout effet opérationnel restent inconnus.

- **Périmètre de l'analyse :** une capture de forum et 50 lignes textuelles fournies dans l'échange ; aucune archive ou base complète n'a été remise. Les 50 lignes n'ont pas été vérifiées individuellement contre le fichier source original ni recopiées dans le dépôt. Un manifeste technique minimisé de la capture est conservé hors dépôt sous `/tmp/afrintel-evidence/AFR-2026-TBD-mdcn/`.

- **Évaluation des risques :** les catégories observées pourraient faciliter l'usurpation de praticiens, le phishing ciblé, l'ingénierie sociale et la fraude documentaire. Aucun dossier médical de patient ni accès valide au portail n'est établi par cet extrait.

- **Sources / Éléments de preuve :** publication de forum et extrait textuel fournis à AFRINTEL ; [site officiel du MDCN](https://www.mdcn.gov.ng/). Aucun nom, numéro de téléphone, adresse électronique, date de naissance ou identifiant professionnel individuel n'est publié.

### 04 septembre 2026
#### 🇪🇬 Égypte - Données attribuées à des propriétaires/résidents de Madinaty (source organisationnelle non identifiée)

- **Date de l'incident :** Non établie
- **Date de publication initiale :** 4 septembre 2026 à 09:59 (heure affichée, fuseau non indiqué)
- **Date de détection AFRINTEL :** 13 septembre 2026 (capture communiquée)
- **Acteur / Groupe :** sainttrojan (compte de forum affiché ; identité et affiliation à un groupe non vérifiées)
- **Secteur :** Immobilier / Communauté résidentielle / Gestion immobilière
- **Organisation détentrice des données :** Non identifiée ; la publication les présente comme liées aux propriétaires/résidents de Madinaty
- **Site web de l'organisation source :** Non identifié
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3

- **Description :** **Madinaty** est une vaste cité résidentielle planifiée à l'est du Caire, développée par **Talaat Moustafa Group (TMG)**, avec logements, infrastructures et services de proximité. Il s'agit ici d'une **communauté résidentielle**, non d'une personne morale formellement identifiée comme victime : ni le promoteur, ni un gestionnaire immobilier, ni un sous-traitant ne peut être désigné comme détenteur des données divulguées à partir de la seule revendication ([présentation TMG](https://ecommerce.tmg.com.eg/about)).

- **Vérification indépendante au 18 octobre 2026 :** Aucune confirmation indépendante d’une intrusion ni identification fiable du détenteur initial des données n’a été identifiée. Les liens avec Madinaty ne prouvent pas une compromission de Talaat Moustafa Group.

  **Incident documenté dans la fiche AFRINTEL :** Madinaty est un projet urbain résidentiel en Égypte que le groupe Talaat Moustafa présente parmi ses projets dans le pays. Cette information situe le contexte géographique ; elle ne permet pas d'identifier l'organisation ayant collecté ou détenu les données ni de confirmer que le groupe Talaat Moustafa a été compromis. ([Présentation du groupe Talaat Moustafa](https://ecommerce.tmg.com.eg/about))

- **Analyse :**

  Une publication de forum attribuée au compte **sainttrojan**, datée du 4 septembre 2026 à 09:59 (fuseau non indiqué), est intitulée comme une offre de données de propriétaires de Madinaty. L'auteur affirme que l'extrait représente **0,5 %** de son ensemble de données et cherche un partenaire pour le monétiser. Cette proportion et la possession du jeu complet sont des affirmations de l'auteur, non vérifiées.

  **Observed :** La capture fournie le 13 septembre contient le titre et le texte de la publication ainsi qu'un extrait structuré en arabe. Les lignes visibles comportent des noms, des identifiants alphanumériques de résidence/logement, des rôles présentés comme propriétaire, locataire ou mandataire, et des valeurs de contact de type numéro de téléphone. L'auteur affirme disposer de numéros personnels et d'adresses résidentielles complètes ; l'extrait ne permet pas de vérifier la couverture ou l'exactitude de ces adresses. Aucune valeur personnelle brute n'est reproduite ici.

  **Assumption :** Le titre du message et les champs visibles rendent plausible une association avec des propriétaires ou résidents de Madinaty. Ils ne permettent pas d'attribuer les enregistrements au groupe Talaat Moustafa, à l'administration du projet, à un prestataire ou à une autre organisation. Une source tierce ou une description trompeuse restent également possibles.

  **Unknown :** L'organisation source, le système d'origine, le mode et la date d'obtention, l'authenticité et l'actualité des enregistrements, le nombre de personnes uniques, l'exhaustivité du jeu, la proportion réellement publiée, l'existence d'un accès non autorisé et toute confirmation d'une organisation concernée ne sont pas établis. L'URL originale du forum et le fichier de données source n'ont pas été fournis ; l'analyse est limitée à la capture et à l'extrait communiqués.

- **Données visibles dans l'extrait, minimisées :** noms, identifiants de résidence/logement, rôles associés aux enregistrements et valeurs de contact de type téléphone. Les adresses complètes et la portée annoncée sont revendiquées par l'auteur, mais ne sont pas validées indépendamment.

- **Périmètre de l'échantillon observé :** extrait partiel visible dans une capture et un texte communiqué ; archive originale, URL source, volume, nombre de lignes distinctes et nombre de personnes non établis. L'affirmation de **0,5 %** n'est pas vérifiée. Aucun enregistrement individuel n'est reproduit dans cette fiche.

- **Évaluation des risques :** si les données sont authentiques, le rapprochement entre identité, lieu de résidence et coordonnées peut exposer les personnes au doxxing, au harcèlement, au ciblage physique, à l'hameçonnage et à la fraude. La revendication ne confirme pas à elle seule l'exfiltration ni l'organisation responsable.

- **Recommandations :**
1. Préserver la capture et les métadonnées de collecte dans un espace de preuve à accès restreint ; éviter toute nouvelle diffusion de l'extrait.
2. Identifier l'organisation ou le prestataire autorisé à détenir ce type de données avant toute attribution publique.
3. Si le détenteur est établi, comparer les schémas et identifiants avec des données internes autorisées, sans tester les numéros personnels ni extraire de nouveaux dossiers.
4. Évaluer les risques de sécurité physique et de fraude pour les personnes potentiellement concernées et leur communiquer des conseils adaptés après validation.
5. Suivre les republications du jeu de données sans ouvrir de liens de téléchargement ni engager de transaction avec l'auteur.

- **Sources / Éléments de preuve :** publication de forum visible dans une capture fournie le 13 septembre 2026 (date affichée de la publication : 4 septembre 2026 ; URL d'origine non fournie) ; [présentation publique du groupe Talaat Moustafa sur ses projets en Égypte](https://ecommerce.tmg.com.eg/about).


### 06 septembre 2026
#### 🇲🇦 Maroc - Centre Atlantique Formation

- **Date de l'incident :** Non établie
- **Date de publication initiale :** 6 septembre 2026
- **Acteur / Groupe :** xNov
- **Secteur :** Éducation / Formation professionnelle
- **Site web :** [atlantique.ma](https://atlantique.ma/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3

- **Description :** **Centre Atlantique Formation** est un réseau marocain de centres privés de formation pratique et professionnelle, proposant des parcours destinés aux étudiants, demandeurs d'emploi et professionnels. Ses offres couvrent notamment les métiers techniques, les services, l'administration et diverses spécialités manuelles, avec des implantations dans plusieurs villes marocaines. L'activité implique des processus d'inscription et la délivrance d'attestations de formation ([site officiel](https://atlantique.ma/)).

- **Vérification indépendante au 18 octobre 2026 :** Aucun communiqué public de Centre Atlantique Formation ni notification réglementaire confirmant le vecteur d’attaque n’a été identifié. L’analyse documentaire interne AFRINTEL de l’archive (1 155 dossiers) reste la corroboration disponible, distincte d’une reconnaissance officielle.

  **Incident documenté dans la fiche AFRINTEL :** Centre Atlantique Formation est un organisme marocain de formation professionnelle proposant des formations pratiques dans plusieurs domaines et au sein de différents centres. Les enregistrements observés font notamment référence au diagnostic automobile, à la comptabilité, l'infographie, la cuisine, la pâtisserie, la coiffure, au stylisme et modélisme, à l'informatique bureautique, la soudure, la plomberie et l'assistance médicale.

- **Analyse :**

  Le 6 septembre 2026, l'acteur **xNov** a publié une revendication visant atlantique.ma et diffusé une archive associée à Centre Atlantique Formation. Un relais Telegram observé le même jour annonçait une archive d'environ **2,49 Go** et affirmait que les données publiées ne représentaient que **27 % de la base**. Les **73 %** correspondent à une déduction arithmétique à partir des 27 % revendiqués et non à une mesure indépendante. Lors d'un contact direct via le canal Telegram, xNov a proposé le reste pour **300 USD** : le prix demandé est donc directement observé comme une offre de l'acteur. Cette observation ne confirme ni l'existence, ni le volume, ni la disponibilité effective des données restantes, et ne constitue pas la preuve d'une transaction.

  Après extraction, l'archive analysée occupe environ **4 Go** et contient **1 155 dossiers regroupant 3 465 éléments**, soit exactement trois éléments par dossier. La structure repose sur les informations d'inscription, les métadonnées de certificats et une attestation PDF.

  Le corpus local transmis pour analyse contient **4 644 fichiers** pour environ **3,94 Go** : **3 476 JSON**, **1 165 PDF** et **3 JPG** comprenant notamment une capture de la publication et des exemples d'attestations. Le fichier `full-details.json` est un tableau de **1 155 enregistrements** avec 13 champs structurés. Les 1 155 identifiants d'inscription sont distincts ; le corpus contient 2 identifiants de centre, 33 identifiants de formation et 1 031 dates de naissance distinctes. Ces valeurs décrivent des enregistrements et des champs observés, pas un nombre de personnes uniques.

  Les fichiers details.json contiennent notamment l'identifiant d'inscription, la civilité, le nom complet, la CIN lorsqu'elle est renseignée, la date et le lieu de naissance, l'adresse et le téléphone lorsqu'ils sont présents, la formation, le centre et la date d'inscription. Les certificates.json contiennent les identifiants de certificats reliés aux inscriptions, le nom, la CIN lorsqu'elle est renseignée, la date du certificat, l'année et l'horodatage de création. Une inscription peut avoir plusieurs certificats.

  Des attestations PDF de dossiers distincts reprennent des informations cohérentes avec les JSON : identité, CIN, date et lieu de naissance, formation, année, durée, date de délivrance, numéro d'attestation et QR code de vérification. Cette corrélation constitue une **forte corroboration interne** de l'origine opérationnelle d'une partie importante des données et de leur association avec Centre Atlantique Formation.

  Les **1 155 dossiers sont des dossiers d'apprenants ou d'inscription, pas automatiquement 1 155 personnes uniques**. Une déduplication priorisant la CIN normalisée, puis le nom et la date de naissance lorsque la CIN manque, est nécessaire. Les dates de naissance indiquent des adultes et apparemment des mineurs. Le vecteur d'accès, le système compromis, la durée d'accès, l'étendue de la compromission, l'exfiltration complète et le volume total restent inconnus.

- **Données exposées observées :** noms, civilités, CIN, dates et lieux de naissance, adresses et téléphones, identifiants d'inscription, formations et centres, dates d'inscription, identifiants et dates de certificats, années et horodatages de création, attestations PDF, numéros d'attestation et QR codes de vérification (lorsque présents).

- **Périmètre du jeu de données observé :** archive annoncée 2,49 Go ; volume extrait environ 4 Go ; 1 155 dossiers ; 3 465 éléments ; moyenne de 3 éléments par dossier ; personnes uniques non établies ; 27 % revendiqués comme publiés ; reste estimé à environ 73 % selon l'acteur, existence et volume non vérifiés ; prix demandé de 300 USD directement observé lors d'un contact avec xNov.

- **Évaluation des risques :** la combinaison d'identité, CIN, naissance, coordonnées, formation et attestations crée un risque significatif d'usurpation, phishing ciblé, fraude documentaire et ingénierie sociale. La présence apparente de mineurs renforce les enjeux de protection. Aucun élément n'établit un ransomware, une destruction ou une interruption opérationnelle.

- **Recommandations :**
1. Identifier la source applicative, base, stockage ou sauvegarde et préserver les journaux.
2. Examiner authentification, comptes privilégiés, interfaces d'administration, API, identifiants de bases et prestataires.
3. Révoquer ou renouveler mots de passe, clés API et secrets potentiellement accessibles.
4. Dédupliquer les personnes à partir de la CIN et d'attributs secondaires.
5. Identifier séparément les mineurs et appliquer des mesures adaptées.
6. Surveiller xNov et les canaux underground pour le reste revendiqué.
7. Surveiller phishing, usurpation, fraude documentaire et usage de certificats.
8. Auditer la vérification des attestations contre l'énumération par QR code ou identifiant.

- **Sources / Éléments observés :** publication xNov sur un forum underground (6 septembre 2026), relais et capture Telegram fournis (6 septembre 2026), contact direct avec xNov via son canal Telegram concernant le prix demandé, analyse AFRINTEL de l'archive et du corpus local extrait. Les fichiers bruts restent hors dépôt.


### 09 septembre 2026
#### 🇪🇬 Égypte - Badr University in Cairo (BUC)

- **Date de l'incident :** Non établie
- **Date de publication initiale :** 9 septembre 2026 à 16:50 (fuseau horaire non indiqué)
- **Acteur / Groupe :** Unknown
- **Compte auteur affiché :** elmo7areb (identité et rôle non vérifiés)
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [buc.edu.eg](https://buc.edu.eg/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3

- **Description :** **Badr University in Cairo (BUC)** est une université égyptienne implantée à Badr City, dans l'agglomération du Caire. L'établissement propose des cursus dans les sciences, les disciplines créatives et les sciences humaines, et dispose de services numériques pour les candidatures et les étudiants. Ce contexte explique l'existence potentielle d'informations administratives et universitaires, sans préjuger de leur compromission ([site officiel BUC](https://buc.edu.eg/new-undergraduate/)).

- **Vérification indépendante au 18 octobre 2026 :** Les publications OSINT secondaires relatent une revendication, sans confirmation publique de Badr University in Cairo ni preuve externe de l’extraction complète. Les identifiants partiellement masqués dans la capture ne prouvent pas un accès valide.

- **Sources de vérification complémentaires :** [Source 1](https://undercodenews.com/badr-university-in-cairo-reportedly-targeted-in-a-dark-web-data-leak-claim-video/)

  **Incident documenté dans la fiche AFRINTEL :** Badr University in Cairo (BUC) est un établissement d'enseignement supérieur égyptien situé à Badr City. Son site officiel présente ses programmes et services, notamment des démarches d'admission et un portail étudiant.

- **Analyse :**

  Une publication attribuée au compte **elmo7areb**, datée du 9 septembre 2026 à 16:50 (fuseau horaire non indiqué), revendique l'extraction complète de la base de données de BUC. L'auteur affirme que les données concernent des étudiants et leurs familles, et cite des identifiants nationaux, des adresses et des numéros de téléphone. Un extrait visible comporte des valeurs présentées comme des identifiants de type adresse courriel, mais ces champs sont incomplets : des segments, notamment après le signe « @ », sont remplacés par `****`. Les chaînes associées, présentées comme des mots de passe, sont elles aussi partiellement masquées par `****`. Aucune valeur n'est reproduite ni testée. L'échantillon source original n'était pas disponible ; l'analyse est limitée aux éléments visibles dans la capture fournie.

  **Observed :** l'existence d'une publication revendiquant une extraction, son horodatage affiché, les catégories de données mentionnées par l'auteur et un extrait de lignes de connexion où les identifiants de type courriel sont incomplets, avec le domaine masqué par `****`, et les chaînes présentées comme mots de passe comportent également des segments remplacés par `****`.

  **Assumption :** l'identité de BUC et la cohérence du sous-domaine avec ses services d'admission rendent la cible plausible. Cela ne valide ni l'authenticité ni la provenance des données, leur extraction effective ou l'exhaustivité de la base. Le texte qualifie l'échantillon de journaux administratifs chiffrés, tandis que la partie visible ressemble à des paires d'identifiants de connexion ; cette incohérence ne peut pas être résolue à partir de la capture.

  **Unknown :** nombre d'enregistrements ou de personnes concernées, validité ou actualité des identifiants, contenu et exhaustivité du jeu de données, vecteur d'accès, systèmes concernés, portée de l'incident, impact opérationnel et confirmation par BUC ou une autorité.

- **Données visibles dans l'extrait :** lignes présentées comme des connexions, avec des identifiants de type adresse courriel incomplets (domaine remplacé par `****`) et des chaînes présentées comme mots de passe partiellement occultées par `****`, ainsi qu'une URL du portail d'admission. Les valeurs originales complètes ne sont pas visibles ; leur authenticité, leur actualité et leur unicité ne peuvent pas être établies.

- **Périmètre de l'échantillon observé :** capture d'une publication et d'une partie d'un extrait textuel ; fichier source original indisponible ; volume total, nombre de lignes et nombre de personnes non établis. Aucune donnée individuelle ni aucun secret n'est reproduit dans cette fiche.

- **Évaluation des risques :** si les données revendiquées sont authentiques, l'exposition d'identifiants, de données d'identité et de coordonnées pourrait faciliter la prise de contrôle de comptes, le phishing ciblé, l'usurpation d'identité et l'ingénierie sociale visant des étudiants ou leurs familles. L'extrait ne démontre pas que les identifiants fonctionnent ni qu'un compte a été compromis.

- **Recommandations :**
1. Préserver les journaux du portail d'admission, de l'authentification, des bases de données et des systèmes d'administration couvrant la période pertinente.
2. Rechercher les accès inhabituels, extractions volumineuses, comptes privilégiés détournés et changements de configuration.
3. Évaluer les comptes potentiellement concernés ; réinitialiser les identifiants exposés et révoquer les sessions lorsque cela est justifié par l'enquête.
4. Vérifier la portée réelle des données et appliquer les procédures de notification et de protection appropriées.
5. Ne pas tester les identifiants divulgués ; surveiller les tentatives de connexion et de phishing visant les étudiants et leurs familles.

- **Sources / Éléments de preuve :** publication de forum visible dans une capture fournie le 12 septembre 2026 (URL d'origine non fournie) ; [site officiel de BUC](https://buc.edu.eg/) ; [page officielle d'admission de BUC](https://buc.edu.eg/buc-admission-application-form/).

### 12 septembre 2026
#### 🇦🇴 Angola - SEPE: Angola's E-Government Platform

- **Date de l'incident :** Non établie
- **Date de publication initiale :** 12 septembre 2026 à 18:23 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** Kazu (compte affiché ; identité et affiliation non vérifiées)
- **Secteur :** Gouvernement / Services publics numériques
- **Site web :** [sepe.gov.ao](https://www.sepe.gov.ao/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4

- **Description :** **SEPE** (*Serviços Públicos Electrónicos*) est le portail gouvernemental angolais donnant accès à un catalogue de démarches administratives numériques. Il couvre notamment des formalités relatives à l'identité, à la famille, aux entreprises, à la fiscalité et à d'autres services publics, susceptibles de nécessiter des justificatifs personnels. Le portail est un point d'accès aux services, ce qui ne démontre pas qu'il héberge lui-même toutes les données citées dans la revendication ([portail officiel SEPE](https://sepe.gov.ao/)).

- **Vérification indépendante au 18 octobre 2026 :** Des médias angolais ont examiné la revendication Kazu en octobre : ils constatent l’absence de confirmation indépendante et indiquent que le portail SEPE reste accessible. Cette disponibilité ne prouve pas l’absence d’exfiltration. Les 179 Go, l’intrusion, le chiffrement et l’affectation de SEPE ne sont toujours pas établis indépendamment ; l’échantillon AFRINTEL conserve sa valeur de preuve documentaire partielle.

- **Sources de vérification complémentaires :** [Source 1](https://pti.ao/sepe-falta-de-evidencias-coloca-em-causa-suposto-ataque-cibernetico/) ; [Source 2](https://pti.ao/sepe-mantem-servicos-online-e-acessiveis-ao-publico/)

  **Incident documenté dans la fiche AFRINTEL :** Une publication attribuée au compte Kazu vise SEPE, la plateforme officielle de services publics électroniques de l'Angola, et revendique une exposition de données dans un contexte d'extorsion ransomware. AFRINTEL a examiné un échantillon local dérivé de la publication ; cette analyse renforce la cohérence structurelle et l'association avec des données administratives angolaises, sans confirmer l'accès initial, l'exfiltration complète, le volume global revendiqué ou la compromission officielle de SEPE.

- **Analyse :**

  **Observed :** La publication affichée le 12 septembre 2026 mentionne **364 841 fichiers**, **110 021 utilisateurs avec données personnelles**, une taille revendiquée de **179 Go**, une demande de **100 000 USD** et une échéance affichée au **27 septembre 2026**. Ces valeurs restent des affirmations de l'acteur. L'échantillon local fourni contient **1 189 fichiers** pour **544 921 521 octets** : 1 030 PDF, 111 JSON, 26 JPG, 8 JPEG, 7 PNG, 4 DOCX, 2 PPTX et 1 fichier sans extension ; 15 fichiers sont vides. Les 111 JSON présentent tous une structure `formData` avec des champs de type identité, document national, nom, email, téléphone, adresse, naissance, nationalité, résidence, commune, province, fonction et parcours de formation. Aucun contenu individuel n'est reproduit dans cette fiche.

  **Assumption :** Le domaine `sepe.gov.ao`, le logo et la description de la plateforme rendent plausible le ciblage d'un service public angolais. La cohérence entre les noms de fichiers documentaires et le schéma JSON est compatible avec un jeu de dossiers administratifs ou de candidature. Elle ne prouve ni que SEPE détenait tous les fichiers, ni que l'acteur a obtenu l'accès par intrusion, ni que les 179 Go ou 110 021 utilisateurs sont réels.

  **Unknown :** le vecteur d'accès, les systèmes touchés, la date de compromission, le nombre de personnes uniques, la couverture réelle, l'exhaustivité, la validité actuelle des documents, la divulgation complète, le paiement de rançon, la confirmation par SEPE ou une autorité et l'état de l'échéance après la dernière vérification restent inconnus.

- **Périmètre de l'échantillon analysé :** 1 189 fichiers locaux ; 544 921 521 octets ; 111 JSON dont la structure a été inspectée ; documents et données personnelles non transcrits. L'empreinte du manifeste d'échantillon est conservée localement dans `/tmp/afrintel-evidence/afr-2026-09-sepe/evidence_manifest.json`. L'échantillon n'est pas le dump complet et ne permet pas d'estimer le nombre de personnes uniques.

- **Évaluation des risques :** si les revendications sont exactes, l'exposition de documents d'identité, coordonnées, parcours éducatifs et autres pièces administratives pourrait faciliter l'usurpation d'identité, le phishing ciblé, la fraude documentaire et l'atteinte à des personnes utilisant des services publics. Aucun secret, identifiant ou document individuel n'est publié par AFRINTEL.

- **Recommandations :**
1. Préserver les journaux SEPE, IAM, API, stockage documentaire et bases de données couvrant la période pertinente.
2. Rechercher les extractions volumineuses, comptes privilégiés, accès anormaux et modifications de configuration.
3. Révoquer les sessions et renouveler les secrets uniquement selon les résultats de l'enquête ; ne pas tester les données de l'échantillon.
4. Identifier les catégories de personnes concernées et préparer les mesures de notification et de protection adaptées.
5. Vérifier l'intégrité des services publics et surveiller le phishing, l'usurpation et la fraude documentaire.
6. Suivre l'échéance et les éventuelles publications ultérieures sans ouvrir de liens criminels ni négocier avec l'acteur.

- **Sources / Éléments de preuve :** capture de la publication Kazu fournie le 22 septembre 2026 ; échantillon local fourni et analysé en lecture seule ; [portail SEPE](https://www.sepe.gov.ao/).

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-12T18:23:00
listing_last_observed_at: 2026-09-22T18:23:00
sample_status: sample-reviewed
deadline_at: 2026-09-27
deadline_status: active
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-22T18:23:00
-->

### 19 septembre 2026
#### 🇿🇦 Afrique du Sud - Apollo 21

- **Date de publication initiale :** 19 septembre 2026 (date affichée dans la liste BLACKLOCKS ; heure et fuseau non indiqués)
- **Acteur / Groupe :** BLACKLOCKS
- **Secteur :** Distribution de pièces détachées / Transport routier
- **Site web :** [apollo21.co.za](https://apollo21.co.za/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Sous-type :** Exfiltration de données revendiquée ; chiffrement non établi
- **Niveau de confiance :** High (publication et lien documentaire avec Apollo 21 ; compromission et volume global non confirmés)
- **Niveau d'impact :** Level 3

- **Description :** **Apollo 21** est une entreprise sud-africaine active depuis 1972 dans l'importation et la distribution de pièces de rechange pour camions, autobus et remorques. Elle fournit notamment des pièces mécaniques, électriques et de carrosserie destinées aux transporteurs et aux professionnels de la maintenance de véhicules commerciaux. Ses activités mobilisent des relations fournisseurs, des stocks et des données commerciales ([site officiel Apollo 21](https://apollo21.co.za/home/)).

- **Vérification indépendante au 18 octobre 2026 :** La fiche BLACKLOCKS et ses images d’échantillon ont été observées, mais aucune confirmation publique d’Apollo 21 ou source indépendante établissant un accès non autorisé, un chiffrement ou 400 Go d’exfiltration n’a été identifiée.

  **Incident documenté dans la fiche AFRINTEL :** La fiche Apollo 21 apparaît dans une liste de victimes de BLACKLOCKS avec la date du **19 septembre 2026**. Une autre vue de cette fiche associe `apollo21.co.za` à l'Afrique du Sud et revendique **400 GB** de données. Les images d'échantillon examinées comprennent des tableaux commerciaux et financiers ainsi que des pièces d'identité. Elles étayent le lien documentaire avec Apollo 21, sans confirmer la méthode d'acquisition, le chiffrement ou la possession de 400 Go.

- **Analyse :**

  **Observed :** La liste fournie comporte trois entrées visibles : une organisation sud-coréenne datée du **1er septembre**, Apollo 21 datée du **19 septembre** et ARCA Unlimited Architects, en Afrique du Sud, datée du **22 septembre 2026**. Ces dates sont celles affichées pour les publications ; elles ne datent ni l'apparition certaine du groupe ni les intrusions. La fiche détaillée Apollo 21 annonce **400 GB**, sans fournir le corpus correspondant. AFRINTEL a examiné **14 images locales** totalisant **3 518 628 octets** : deux vues de la publication et **12 images d'échantillons**. Les échantillons montrent des listes de comptes débiteurs et de dépôts, une demande de crédit, des tableaux de ventes, stocks, approvisionnements et expéditions, ainsi que **trois images de pièces d'identité**. Plusieurs documents mentionnent Apollo 21 ou sa dénomination commerciale et portent un filigrane BLACKLOCKS. Des coordonnées, montants et identifiants individuels sont visibles mais ne sont pas reproduits.

  **Assumption :** La cohérence entre le domaine publié, l'activité décrite par le [site officiel d'Apollo 21](https://apollo21.co.za/about-apollo21/) et les documents commerciaux soutient une confiance élevée dans l'association de l'échantillon à l'entreprise. Le filigrane établit la présentation par l'acteur, pas la provenance technique des fichiers. Les pièces d'identité ne permettent pas, à elles seules, d'établir le rôle des personnes concernées ni le nombre total de personnes exposées.

  **Unknown :** la date et le vecteur d'accès, les systèmes concernés, l'origine exacte de chaque document, la possession et la publication effectives des **400 Go**, le nombre de personnes touchées, le chiffrement, les effets opérationnels, une confirmation par Apollo 21 ou une autorité, toute négociation, tout paiement et toute revente restent inconnus.

- **Périmètre de l'analyse :** les 14 images ont été examinées en lecture seule ; aucun fichier source de tableur, document natif ni corpus de 400 Go n'a été fourni. L'analyse établit les catégories visibles, pas l'exhaustivité ni l'authenticité indépendante de chaque pièce. Les empreintes et tailles figurent dans un manifeste local hors dépôt sous `/tmp/afrintel-evidence/AFR-2026-TBD-apollo21/`.

- **Évaluation des risques :** les pièces d'identité et données de contact visibles présentent un risque d'usurpation d'identité et de fraude documentaire ; les informations commerciales, financières et de partenaires pourraient faciliter le phishing ciblé, la fraude au paiement et l'ingénierie sociale. Aucun effet opérationnel n'est établi par ces images.

- **Sources / Éléments de preuve :** liste et fiche BLACKLOCKS fournies en capture ; douze images d'échantillon fournies localement ; [site officiel d'Apollo 21](https://apollo21.co.za/). Aucun document individuel, identifiant personnel ou lien vers le site criminel n'est publié.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-28
listing_last_observed_at: 2026-09-28
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-28
-->

### 21 septembre 2026
#### 🇳🇬 Nigéria - Federal Capital Territory Internal Revenue Service (FCT-IRS)

- **Date de publication initiale :** 21 septembre 2026 à 13:03 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** individual (compte affiché ; identité non vérifiée)
- **Secteur :** Gouvernement / Administration fiscale
- **Site web :** [fctirs.gov.ng](https://fctirs.gov.ng/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High (publication et association de l'échantillon au FCT-IRS ; origine technique non établie)
- **Niveau d'impact :** Level 3

- **Description :** Le **Federal Capital Territory Internal Revenue Service (FCT-IRS)** administre les recettes fiscales intérieures du **Territoire de la capitale fédérale d'Abuja**, au Nigéria. Créé par une loi de 2015, cet organisme intervient notamment dans l'évaluation, la collecte et la comptabilisation de taxes et prélèvements locaux, dont l'impôt sur le revenu des personnes physiques relevant de son ressort. Il ne doit pas être confondu avec l'administration fiscale fédérale nationale ([présentation officielle FCT-IRS](https://fctirs.gov.ng/about-us/)).

- **Vérification indépendante au 18 octobre 2026 :** Aucun communiqué du FCT-IRS, document de régulateur ni résultat d’enquête indépendante confirmant l’intrusion n’a été identifié. Le PDF analysé atteste de données publiées sous cette attribution, sans prouver leur origine technique.

  **Incident documenté dans la fiche AFRINTEL :** Une publication intitulée « Nigerian Tax Authority | Full Breach » affiche le logo du **Federal Capital Territory Internal Revenue Service (FCT-IRS)** et fait référence à des images de personnes et de signatures. Le PDF fourni, exporté depuis JustPaste.it, contient **314 pages** de texte et présente des données personnelles. L'expression « Full Breach » est le titre revendiqué par l'auteur ; l'exhaustivité des données et une compromission du système du FCT-IRS ne sont pas établies.

- **Analyse :**

  **Observed :** La capture montre une publication attribuée au compte **individual**, datée du **21 septembre 2026 à 13:03** selon l'horodatage affiché. Le contenu visuel identifie le FCT-IRS. Le PDF de **1 284 983 octets** a été traité en lecture seule ; les métadonnées indiquent 314 pages et une création PDF par HeadlessChrome le 28 septembre 2026, ce qui date l'export local, pas la publication ni l'incident. L'extraction complète contient **742 955 caractères** sur **12 541 lignes**. Une détection automatique a relevé **2 541 occurrences d'adresses électroniques correspondant au format**, dont **2 540 valeurs distinctes**, et **61 occurrences** correspondant au motif téléphonique nigérian utilisé. Ces occurrences ne sont ni des dossiers ni des personnes uniques validés. La capture présente aussi des vignettes de portraits et de signatures. Aucune valeur individuelle n'est reproduite.

  **Assumption :** Le logo FCT-IRS, le contexte fiscal et la concordance avec le site officiel du [Federal Capital Territory Internal Revenue Service](https://fctirs.gov.ng/) rendent plausible que les éléments se rapportent au FCT-IRS. Le titre générique « Nigerian Tax Authority » ne suffit pas à attribuer le cas à l'administration fiscale nationale (Nigeria Revenue Service) ; l'identification retenue ici est le service fiscal du Territoire de la capitale fédérale.

  **Unknown :** le fichier source avant export PDF, la structure exacte des enregistrements et leur déduplication, la provenance des images et des coordonnées, l'organisation ou le système d'origine, le vecteur et la date d'un éventuel accès, l'étendue complète des données, la validité des données, une confirmation officielle et les effets opérationnels restent inconnus. L'affirmation de compromission complète n'est pas corroborée.

- **Périmètre de l'analyse :** extraction textuelle de l'ensemble des 314 pages et revue visuelle de la capture ; analyse limitée au contenu de ce PDF et à l'image publiée. La mise en page réorganisée ne permet pas un décompte fiable des dossiers ou des personnes. Aucun texte extrait ni aucune donnée personnelle brute n'est conservé dans le dépôt. Métadonnées et statistiques agrégées conservées hors dépôt dans `/tmp/afrintel-evidence/AFR-2026-TBD-fctirs/`.

- **Évaluation des risques :** l'exposition de coordonnées et de données identifiantes de personnes pourrait faciliter l'hameçonnage ciblé, l'usurpation d'identité, la fraude et l'ingénierie sociale. L'échantillon examiné ne permet pas d'établir l'exposition de données fiscales ou financières détaillées.

- **Sources / Éléments de preuve :** capture de la publication du forum fournie le 28 septembre 2026 ; PDF JustPaste.it local analysé en lecture seule ; [site officiel du FCT-IRS](https://fctirs.gov.ng/). Aucune donnée personnelle individuelle ni lien vers le site criminel n'est publiée.

### 22 septembre 2026
#### 🇿🇦 Afrique du Sud - ARCA Unlimited Architects

- **Date de publication initiale :** 22 septembre 2026 (date affichée dans la liste BLACKLOCKS ; heure et fuseau non indiqués)
- **Acteur / Groupe :** BLACKLOCKS
- **Secteur :** Architecture / Conception et gestion de projets
- **Site web :** [arcaunlimited.com](https://arcaunlimited.com/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Sous-type :** Exfiltration de données revendiquée ; chiffrement non établi
- **Niveau de confiance :** High (publication et lien documentaire avec ARCA ; acquisition et volume global non confirmés)
- **Niveau d'impact :** Level 3

- **Description :** **ARCA Unlimited Architects** est une agence sud-africaine pluridisciplinaire de conception, basée à Pretoria. Elle propose des prestations d'architecture, de design intérieur, d'aménagement d'espaces, de gestion de projet et de conseil, avec une activité revendiquée en Afrique depuis 1995. Ces métiers impliquent la production de plans, de dossiers de projet et de documents budgétaires pour des clients ([présentation officielle ARCA](https://arcaunlimited.com/who-are-we.asp)).

- **Vérification indépendante au 18 octobre 2026 :** La liste BLACKLOCKS et les plans d’architecture portant des références cohérentes avec ARCA corroborent la présence d’échantillons, non la compromission de l’infrastructure d’ARCA. Aucune déclaration publique de la société n’a été identifiée.

  **Incident documenté dans la fiche AFRINTEL :** BLACKLOCKS présente ARCA Unlimited Architects comme victime sud-africaine et affiche un volume de **400G** sans préciser l'unité. Les images d'échantillon comprennent des plans architecturaux, des documents de projet et des tableaux de coûts. Plusieurs éléments portent le nom ou la marque ARCA et sont cohérents avec son activité. L'examen ne confirme ni la méthode d'acquisition, ni un chiffrement, ni la possession du volume revendiqué.

- **Analyse :**

  **Observed :** La liste BLACKLOCKS fournie précédemment date l'entrée ARCA du **22 septembre 2026** ; la fiche détaillée associe `arcaunlimited.com` à l'Afrique du Sud et annonce **« DATA SIZE: 400G »**. AFRINTEL a examiné en lecture seule **18 images locales** pour **3 737 321 octets** : la fiche détaillée et **17 images d'échantillon**. Celles-ci montrent des plans, coupes et élévations, un rapport de conception daté de septembre 2026, une demande d'approbation de plans, une feuille de conformité énergétique, des tableaux de coûts de projets et une pièce d'identité. Des documents récents portent la marque ARCA et son domaine ; d'autres plans concernent des tiers ou des projets historiques. Des noms, identifiants, coordonnées et détails de bâtiments sont visibles mais ne sont pas reproduits.

  **Assumption :** La correspondance entre le domaine publié, le [site officiel d'ARCA](https://arcaunlimited.com/who-are-we.asp), les documents de conception et certaines marques ARCA soutient une confiance élevée dans le lien documentaire avec l'entreprise. La présence de plans liés à des clients, y compris à un opérateur du secteur électrique, n'établit aucun incident distinct visant ces clients. Le filigrane BLACKLOCKS ne démontre pas la provenance technique des fichiers.

  **Unknown :** la date et le vecteur d'accès, les systèmes concernés, la provenance de chaque plan, les droits de diffusion antérieurs, l'étendue réelle des données détenues ou publiées, l'unité exacte de « 400G », le nombre de personnes touchées, un éventuel chiffrement ou impact opérationnel, une confirmation par ARCA ou une autorité, toute négociation, tout paiement et toute revente restent inconnus.

- **Périmètre de l'analyse :** 18 images examinées ; aucun fichier source natif de CAO, document ou tableur et aucun corpus correspondant au volume annoncé n'ont été fournis. L'échantillon démontre la diversité des supports visibles, pas leur exhaustivité ni l'authenticité indépendante de chaque document. Un manifeste SHA-256 agrégé est conservé hors dépôt sous `/tmp/afrintel-evidence/AFR-2026-TBD-arcaunlimited/`.

- **Évaluation des risques :** l'exposition éventuelle de plans détaillés, de documents de projet, de coûts et d'une pièce d'identité pourrait faciliter la fraude documentaire, le phishing ciblé, l'ingénierie sociale et la divulgation de détails de sites de clients. La sensibilité de certains plans justifie une attention particulière, sans conclure à une compromission des organisations tierces nommées.

- **Sources / Éléments de preuve :** liste BLACKLOCKS et fiche ARCA fournies en captures ; 17 images d'échantillon locales ; [site officiel d'ARCA Unlimited](https://arcaunlimited.com/). Aucun plan, détail de site, identifiant personnel ou lien vers le site criminel n'est publié.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-28
listing_last_observed_at: 2026-09-28
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-28
-->

#### 🇲🇱 Mali - AFRICA-TECH

- **Date de publication initiale :** 22 septembre 2026 (date communiquée ; heure non précisée)
- **Date de divulgation des données :** 25 septembre 2026 à 16:00 GMT (UTC), selon les informations de collecte communiquées
- **Acteur / Groupe :** N0n
- **Secteur :** Technologies / Services IT / Traitement documentaire
- **Site web :** Non identifié
- **Domaine proposé :** [africatech-mali.com](https://www.africatech-mali.com/) (attribution à la victime non établie)
- **Statut :** Data Fully Published
- **Type d'incident :** Ransomware
- **Sous-type :** Double extorsion revendiquée ; données divulguées examinées
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3

- **Description :** **AFRICA-TECH** est désignée dans la publication examinée comme une structure malienne opérant dans les **services informatiques et le traitement documentaire**. Les pièces examinées par AFRINTEL contiennent des références à l'entreprise et au Mali, mais les informations publiques accessibles ne suffisent pas à identifier de manière indépendante son statut juridique, son catalogue de prestations ou son site officiel. Le domaine `africatech-mali.com` renvoie à des activités différentes et **ne doit pas être rattaché automatiquement** à cette fiche.

- **Vérification indépendante au 18 octobre 2026 :** La publication intégrale du lot attribué à AFRICA-TECH a été observée et analysée par AFRINTEL ; les sources OSINT externes relaient surtout la déclaration N0n. Aucune reconnaissance par l’entreprise, preuve publique de chiffrement ou identification organisationnelle suffisamment certaine n’a été trouvée.

  **Incident documenté dans la fiche AFRINTEL :** AFRICA-TECH est présentée dans la publication de N0n comme une entreprise malienne de services IT et de traitement documentaire. L'ensemble des fichiers divulgués par le groupe a été fourni pour analyse. Une réclamation Word mentionne AFRICA-TECH et des références au Mali et à Bamako, ce qui étaye le lien documentaire avec l'organisation. Le domaine proposé, https://www.africatech-mali.com/, présente des activités solaires et électriques à Bamako. La comparaison avec les documents n'a pas établi de coordonnées communes ; son attribution à la victime reste non établie.

- **Analyse :**

  **Observed :** La fiche victime de N0n affichait une échéance au **25 septembre 2026 à 16:00 UTC**. Selon les informations de collecte communiquées, le groupe a divulgué l'ensemble des fichiers à **16:00 GMT**, conformément à cette échéance, et le dossier remis correspond à l'intégralité de cette publication. L'analyse locale du **26 septembre 2026** couvre **10 fichiers distincts par SHA-256**, totalisant **2 413 673 octets** : **6 PDF de 39 pages**, **2 documents Word**, **1 fichier texte** et **1 fichier temporaire Word de 162 octets**, non exploitable comme document. Le relevé bancaire représente **31 pages**. Les textes des documents ont été extraits et les **39 pages PDF** ainsi que les **4 images incorporées** au document Word ont été traitées par OCR. Le contenu comprend des documents bancaires, une réclamation relative à des services de transfert d'argent, une offre de services, un billet de voyage, un document lié à une démarche de visa et une assurance voyage. La réclamation comporte **2 occurrences** du nom AFRICA-TECH. Les références à Ecobank et Sanlam décrivent les documents ; elles ne constituent pas des incidents distincts visant ces organisations.

  **Assumption :** La diversité des pièces, leurs références au Mali et à Bamako et la mention d'AFRICA-TECH sont cohérentes avec la conservation de documents dans une activité de services documentaires. Ces éléments soutiennent une confiance élevée dans le lien documentaire avec AFRICA-TECH. Ils ne prouvent pas le mode d'acquisition des fichiers. Le README reprend des affirmations de chiffrement des documents clients et de destruction de sauvegardes et de shadow copies ; aucune preuve technique de ces opérations n'est présente dans le lot analysé.

  **Unknown :** la date et le vecteur de compromission, les systèmes concernés, l'authenticité métier de chaque pièce, le volume total éventuellement extrait avant la publication, les effets opérationnels, le chiffrement effectif, l'accès aux sauvegardes, toute négociation, tout paiement de rançon ou toute revente, ainsi qu'une confirmation par AFRICA-TECH ou une autorité restent inconnus. L'intégralité du lot publié, telle que communiquée lors de la collecte, ne démontre pas l'exhaustivité des données éventuellement détenues par le groupe.

- **Données observées dans la publication :** informations d'identité, de naissance, de passeport, de contact et de voyage ; informations bancaires et opérations financières ; documents d'assurance et correspondance professionnelle. Les repères documentaires incluent notamment **2021, 2023, 2025 et 2026** ; ils ne datent pas l'intrusion. Aucun nombre de personnes ou de transactions distinctes n'est établi.

- **Limites de l'analyse :** l'OCR utilise le modèle anglais et peut mal lire les textes français, les tableaux et les éléments graphiques. Les 4 images Word ont été traitées, mais seules 2 ont fourni un résultat textuel non vide, très court. Chaque champ n'a pas été validé visuellement. La cohérence des formats et des contenus ne constitue ni une authentification de chaque document ni une confirmation officielle de l'incident. Les résultats publiés sont agrégés ; aucune donnée personnelle brute n'est reproduite.

- **Évaluation des risques :** les catégories de données divulguées peuvent faciliter le phishing ciblé, l'usurpation d'identité, la fraude documentaire et les prétextes de paiement. L'impact est évalué à Level 3 compte tenu des informations personnelles et financières observées. Une interruption des services ou des difficultés de restauration ne sont pas établies par les fichiers examinés.

- **Sources / Éléments de preuve :** fiche victime N0n et échéance communiquées pour le 22 septembre 2026 ; dossier local fourni comme l'ensemble des fichiers divulgués par N0n le 25 septembre 2026 à 16:00 GMT ; analyse locale du 26 septembre 2026 et manifeste SHA-256 conservé hors dépôt. La provenance et l'heure de divulgation sont documentées par les informations de collecte communiquées ; aucune consultation indépendante du site du groupe n'a été effectuée pour cette mise à jour.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-22
listing_last_observed_at: 2026-09-22
sample_status: sample-reviewed
deadline_at: 2026-09-25T16:00:00Z
deadline_status: expired
disclosure_status: release-reviewed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-27
-->

### 25 septembre 2026
#### 🇲🇦 Maroc - Pharma 5

- **Date de publication initiale :** 25 septembre 2026 à 08:27 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** INC Ransom
- **Secteur :** Santé / Industrie pharmaceutique
- **Site web :** [pharma5.ma](https://www.pharma5.ma/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Sous-type :** Exfiltration de données revendiquée
- **Niveau de confiance :** High (existence de la publication et cohérence de l'échantillon visible ; périmètre et acquisition non établis)
- **Niveau d'impact :** Level 3

- **Description :** **Pharma 5** est un laboratoire pharmaceutique marocain spécialisé dans le développement, la fabrication et la commercialisation de **médicaments génériques**. Actif sur le marché national et dans plusieurs pays africains, il évolue dans une chaîne de valeur réglementée associant recherche, production, contrôle qualité et distribution. Des médicaments commercialisés par Pharma 5 apparaissent dans le répertoire public de l'autorité marocaine du médicament ([AMMPS](https://ammps.gov.ma/repertoire-medicaments-generiques)).

- **Vérification indépendante au 18 octobre 2026 :** La publication d'INC Ransom a été relayée par [Le1.ma (27 septembre 2026)](https://le1.ma/pharma-5-frappe-par-une-cyberattaque/) et [DeXpose (26 septembre 2026)](https://www.dexpose.io/incransom-targets-moroccan-pharma-leader-pharma5/). Ces relais attestent la circulation de la revendication, **pas** la confirmation de l'intrusion. Le1.ma signalait l'absence de confirmation ou de démenti public de Pharma 5 au 27 septembre ; aucune confirmation officielle ou technique indépendante de l'intrusion, du chiffrement et des **50 Go revendiqués** n'a été identifiée dans les sources examinées jusqu'au 18 octobre. Les nouveaux échantillons fournis à AFRINTEL corroborent néanmoins **la cohérence documentaire de la cible et de sa chaîne d'approvisionnement**, sans établir l'origine technique des fichiers.

- **Corroboration OSINT de l'échantillon (18 octobre 2026) :**
  1. Le document lisible porte l'en-tête **« Pharma5 Quality Management Department »**, le titre **« Specifications »**, la référence **`DE01 / PG / MQ / 036`**, la **révision 01** et l'indication **« Page: 1/5 »**. Il est associé au **salicylamide** et identifie les trois rôles « client : Pharma 5 », « fournisseur : MEDILIFE » et « fabricant : JQC-CHINE ». Des fonctions de gestion de la qualité et d'approvisionnement sont également présentes ; les coordonnées nominatives visibles ne sont pas reprises dans AFRINTEL.
  2. L'adresse professionnelle de **MEDILIFE S.R.L.** à **Via San Vincenzo 8, 20123 Milan** correspond à une [fiche d'entreprise italienne](https://www.ufficiocamerale.it/9842/medilife-srl). **JQC (Huayin) Pharmaceutical Co., Ltd.** commercialise le **salicylamide** dans son [catalogue officiel](https://www.jqcpharm.com/en/index.php/Product). Pharma 5 décrit publiquement des processus de qualité couvrant les matières premières et la fabrication dans un [communiqué de 2020](https://www.pharma5.ma/wp-content/uploads/presse/communique/CP-PHARMA5-VF-17-NOVEMBRE-2020.pdf).
  3. Ces correspondances constituent une **corroboration contextuelle de l'identité de fournisseurs et de l'activité**, et **non** une vérification indépendante d'une relation contractuelle, de l'authenticité du document source, de la compromission de Pharma 5 ou de celle de MEDILIFE/JQC. La date de création du document n'est pas déterminable à partir de la page ; la date du 25 septembre 2026 est celle de la publication criminelle.

- **Sources de vérification complémentaires :** [Le1.ma](https://le1.ma/pharma-5-frappe-par-une-cyberattaque/) ; [DeXpose](https://www.dexpose.io/incransom-targets-moroccan-pharma-leader-pharma5/) ; [fiche publique MEDILIFE](https://www.ufficiocamerale.it/9842/medilife-srl) ; [catalogue fabricant JQC](https://www.jqcpharm.com/en/index.php/Product) ; [communiqué officiel Pharma 5 sur la qualité](https://www.pharma5.ma/wp-content/uploads/presse/communique/CP-PHARMA5-VF-17-NOVEMBRE-2020.pdf).

- **Analyse :**

  **Observed :** La publication d'INC Ransom, horodatée **25 septembre 2026 à 08:27** (fuseau non indiqué), nomme `pharma5.ma`, affiche **« Leaked data: 50Gb »** et une valeur de revenus de **« 500M$ »** (affirmations de l'acteur, non vérifiées). Le groupe annonce des données corporate et financières, de produits et approvisionnements, de contrôle qualité et certification, de tests pharmaceutiques, de personnel et de partenaires. La galerie montre des aperçus de documents et tableurs ; leur faible résolution empêche d'attester l'ensemble des catégories annoncées. La seconde image fournie à AFRINTEL montre une **page de spécifications de gestion qualité** distincte et lisible : salicylamide, référence `DE01 / PG / MQ / 036`, révision `01`, `1/5`, Pharma 5 comme client, MEDILIFE (Italie) comme fournisseur et JQC-CHINE comme fabricant. Le document contient des champs professionnels et des coordonnées de personnes physiques, non reproduits. **Une page seulement** est disponible, pas les quatre pages supplémentaires ni le fichier natif.

  **Assumption :** La convergence entre l'en-tête Pharma 5, le contexte qualité/approvisionnement, le fournisseur italien localisable et le catalogue officiel du fabricant chinois soutient une **association documentaire élevée** avec l'écosystème de Pharma 5. Elle ne démontre pas que le document a été obtenu à la suite d'une intrusion dans ses systèmes : un partage commercial légitime antérieur, un tiers, une fuite préexistante, une republication ou une falsification restent possibles. Aucune compromission de MEDILIFE ou de JQC n'est démontrée.

  **Unknown :** l'origine et la date de création du document, son caractère réellement non public, son authenticité technique indépendante, le système ou l'organisation d'origine, le vecteur et la date de tout accès non autorisé, la disponibilité et le volume des fichiers revendiqués, les catégories réellement exposées au-delà de la page lisible, le nombre de personnes concernées, tout chiffrement ou interruption d'activité, les confirmations officielles, toute négociation, tout paiement et toute revente.

- **Périmètre de l'analyse :** quatre fichiers image étaient présents dans le dossier local fourni. Trois fichiers concernent la publication Pharma 5 ou son échantillon (`12.jpg`, `13.jpg` et `Capture d’écran du 2026-09-28 11-22-02.png`) ; ils montrent des vues complémentaires ou répétées de la revendication et d'une page de spécifications marquée `1/5`. Le fichier `1.png` a été exclu de cette analyse car il présente une publication relative à **atlantique.ma / Centre Atlantique**, sans lien établi avec Pharma 5. Les vignettes ne sont pas des fichiers sources vérifiés et aucune des autres pages du document n'a été fournie. Les empreintes SHA-256 ci-dessous concernent les copies reçues, pas les originaux présumés exfiltrés. Aucun nom, courriel, numéro personnel ou document brut n'est reproduit dans la présente fiche.

- **Évaluation des risques :** La divulgation d'une page comprenant des personnes de contact et les rôles d'acteurs de la chaîne d'approvisionnement pourrait alimenter du **phishing ciblé**, des fraudes au fournisseur/changement de RIB (BEC) ou des tentatives d'ingénierie sociale. Si les autres catégories revendiquées sont authentiques, des risques additionnels toucheraient la confidentialité commerciale, le contrôle qualité et les partenaires. **Aucun dossier médical de patient, aucun secret de fabrication ni aucune altération de médicament ne sont établis** par les trois fichiers Pharma 5 examinés.

- **Recommandations SOC/CTI :** préserver l'original de chaque capture et ses métadonnées ; vérifier hors ligne la provenance, la date et l'empreinte du document de spécifications dans les référentiels internes autorisés ; rechercher les accès inhabituels aux espaces qualité/achats et aux partages fournisseurs ; valider hors bande tout changement d'instructions de paiement ; sensibiliser les contacts professionnels potentiellement exposés ; suivre d'éventuelles publications supplémentaires sans acquérir ni redistribuer les données.

- **Sources / Éléments observés :** dossier local fourni à AFRINTEL en octobre 2026, comprenant trois images relatives à la publication Pharma 5 et un fichier exclu car relatif à atlantique.ma / Centre Atlantique ; recoupements publics [Pharma 5](https://www.pharma5.ma/wp-content/uploads/presse/communique/CP-PHARMA5-VF-17-NOVEMBRE-2020.pdf), [MEDILIFE S.R.L.](https://www.ufficiocamerale.it/9842/medilife-srl), [JQC Pharmaceutical](https://www.jqcpharm.com/en/index.php/Product) ; [Le1.ma](https://le1.ma/pharma-5-frappe-par-une-cyberattaque/) et [DeXpose](https://www.dexpose.io/incransom-targets-moroccan-pharma-leader-pharma5/) pour la couverture publique de la revendication. Les fichiers bruts restent hors dépôt. **Les correspondances publiques n'établissent pas une compromission.**

- **Traçabilité des fichiers Pharma 5 (SHA-256) :** `12.jpg` = `2edf0dbea43828b081c3df664d40bc598d6bcf283e170145097c92abf52340a7` ; `13.jpg` = `3d531eada1c3a5de9c618cf91edd4c3bf383a306d4758f012d681f1fe3fa8e13` ; `Capture d’écran du 2026-09-28 11-22-02.png` = `66c63a7c0933ab7422853ae4c73aa5c6caa4ed33714cfe17d7e5577cc63e5a74`. Le fichier `1.png` a été exclu et n'est pas utilisé comme élément observé pour Pharma 5. Empreintes des copies transmises, non des fichiers éventuellement détenus par l'acteur.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-28
listing_last_observed_at: 2026-09-28
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-28
-->

### 27 septembre 2026
#### 🇿🇦 Afrique du Sud - First National Bank (FNB)

- **Date de l'incident :** Non établie
- **Date de publication initiale :** 27 septembre 2026 à 00:06 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** Blacknet00
- **Secteur :** Services financiers / Banque
- **Site web :** [fnb.co.za](https://www.fnb.co.za/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Sous-type :** Extorsion et exfiltration revendiquées ; chiffrement non établi
- **Niveau de confiance :** Medium (publication et cohérence visuelle des échantillons ; origine, authenticité et compromission non corroborées)
- **Niveau d'impact :** Level 3

- **Description :** **First National Bank (FNB)** est une banque de détail et d'entreprises sud-africaine opérant en tant que division de **FirstRand Bank Limited**. Elle propose des comptes, paiements, crédits, services bancaires numériques et prestations destinées aux particuliers et entreprises. Cette identité institutionnelle ne démontre pas, à elle seule, que des systèmes bancaires ont été compromis par l'auteur de la publication ([présentation officielle FNB](https://www.fnb.co.za/about-fnb/about-us.html)).

- **Vérification indépendante au 18 octobre 2026 :** Aucune déclaration FNB, notification réglementaire ni enquête indépendante corroborant la revendication Blacknet00 de septembre n’a été identifiée. La panne bancaire observée le 2 septembre est un événement distinct, sans lien causal établi.

  **Incident documenté dans la fiche AFRINTEL :** Blacknet00 a publié une fiche nommant First National Bank en Afrique du Sud et a joint cinq images de documents financiers. Les éléments visibles correspondent à des relevés de comptes professionnels portant la marque FNB et couvrant des périodes en 2023 et 2025. Ils appuient l'existence de la publication et une association documentaire plausible avec FNB, sans établir que les relevés proviennent de l'infrastructure de la banque ni qu'un accès non autorisé a eu lieu.

- **Analyse :**

  **Observed :** La publication est intitulée « Another victim of the BLACKNET-00 ransomware. FIRST NATIONAL BANK in South Africa » et porte l'horodatage affiché du **27 septembre 2026 à 00:06**. Son auteur revendique une infiltration et demande une rançon. Les **cinq** JPEG joints ont été examinés en lecture seule ; ils totalisent **428 994 octets** et présentent trois séries apparentes de relevés de comptes professionnels, dont deux sont partielles. Les périodes documentaires visibles se situent en **2023** et **2025**. Chaque image porte un filigrane BLACKNET-00. La structure visuelle, la dénomination de FNB en tant que division de FirstRand Bank Limited et l'identifiant réglementaire figurant sur les images correspondent aux mentions présentes sur le [site officiel de FNB](https://www.fnb.co.za/). Des identifiants de comptes, coordonnées, transactions, montants et noms sont visibles, mais ne sont pas reproduits.

  **Assumption :** La cohérence entre la marque, la mise en page, les mentions institutionnelles et les trois séries documentaires rend plausible un lien entre les images et des relevés FNB. Elle n'établit pas que FNB était le système source : les relevés peuvent provenir de clients, de partenaires, d'un prestataire, d'un poste utilisateur ou d'un autre dépôt. Le filigrane indique la présentation faite par Blacknet00, non la provenance technique des documents.

  **Unknown :** l'authenticité indépendante des relevés, leur source et leur date de collecte, l'existence de fichiers natifs, le vecteur et la date d'un éventuel accès, les systèmes concernés, le nombre de clients ou comptes touchés, l'étendue de toute exfiltration, l'existence d'un chiffrement, les effets opérationnels, une négociation, un paiement, une revente et toute confirmation par FNB ou une autorité restent inconnus.

- **Périmètre de l'analyse :** les cinq images JPEG fournies ont été examinées dans leur intégralité, avec contrôle de type, de taille, de dimensions et d'empreintes SHA-256. Aucun PDF, relevé natif, fichier source, métadonnée de pièce jointe ni corpus complet n'a été fourni. Aucune valeur financière, donnée personnelle ou identifiant de compte n'a été transcrit, testé ou ajouté au dépôt. Le manifeste minimisé est conservé hors dépôt sous `/tmp/afrintel-evidence/afr-2026-09-fnb-sa/evidence_manifest.json`.

- **Évaluation des risques :** si les documents sont authentiques et issus d'un accès non autorisé, des relevés professionnels peuvent faciliter la fraude au paiement, le BEC, le spear-phishing, l'usurpation et l'ingénierie sociale visant des clients ou partenaires. L'échantillon n'établit ni pertes financières, ni exposition à l'échelle de la banque, ni compromission de comptes FNB.

- **Recommandations :**
1. Préserver les journaux d'accès, d'export et de génération de relevés, ainsi que les traces d'accès aux espaces documentaires et aux services de comptes professionnels.
2. Vérifier, dans un cadre autorisé, si les séries documentaires correspondent à des modèles et canaux de distribution FNB, sans tester les identifiants ou transactions visibles.
3. Rechercher les exports anormaux, les accès privilégiés inhabituels, les modifications de règles de messagerie et les accès de tiers aux documents clients.
4. Renforcer la détection des changements de coordonnées bancaires, des demandes de paiement inhabituelles et des campagnes de phishing ciblant les clients professionnels.
5. Conserver les artefacts dans un espace restreint et suivre toute republication sans ouvrir de lien criminel ni engager de négociation.

- **Sources / Éléments de preuve :** publication Blacknet00 et cinq images d'échantillon fournies à AFRINTEL ; [site officiel de FNB](https://www.fnb.co.za/) pour la correspondance de la marque et des mentions institutionnelles. Aucun lien vers l'infrastructure criminelle, relevé, identifiant, transaction ou donnée personnelle brute n'est publié.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-27T00:06:00
listing_last_observed_at: 2026-10-08
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-10-08
-->

## Incidents antérieurs découverts tardivement et intégrés au corpus de septembre

> Ces fiches concernent des incidents survenus avant septembre 2026. Elles sont intégrées au corpus éditorial de septembre car elles ont été recensées et vérifiées tardivement, avant la publication du rapport mensuel. La date d'incident reste la date réelle ou la meilleure fenêtre documentée ; la date de découverte/intégration AFRINTEL est conservée séparément.

### 03 janvier 2026 - intégré le 01 septembre 2026
#### 🇿🇦 Afrique du Sud - Constantia Pharmacy

- **Date de l'incident :** 03 janvier 2026
- **Date de publication / confirmation :** 05 janvier 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Ransomware `Want_to_cry` observé ; opérateur humain non attribué
- **Secteur :** Santé / Pharmacie
- **Statut :** Corroborated
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 2
- **Description :** **Constantia Pharmacy** est une pharmacie de proximité implantée au **Constantia Village Shopping Centre**, au Cap, en Afrique du Sud. Elle propose des services de dispensation de médicaments, de conseil pharmaceutique et une activité de clinique/soins de proximité. Son activité implique des systèmes métiers pharmaceutiques et des données nécessaires au service des patients ([site officiel](https://constantiapharmacy.co.za/)).

- **Vérification indépendante au 18 octobre 2026 :** **Incident antérieur confirmé par enquête journalistique :** MyBroadband a documenté début janvier 2026 l’intervention d’un tiers face à un logiciel de chiffrement sur un serveur de Constantia Pharmacy. Le piratage concernait janvier, pas septembre ; la découverte AFRINTEL en septembre ne constitue pas une nouvelle attaque.

- **Sources de vérification complémentaires :** [Source 1](https://mybroadband.co.za/news/security/623956-hacker-rescues-south-african-pharmacy-from-cyber-attack.html)

- **Sources / Éléments de preuve :** [MyBroadband, 5 janvier 2026](https://mybroadband.co.za/news/security/623956-hacker-rescues-south-african-pharmacy-from-cyber-attack.html)

Constantia Pharmacy est une pharmacie indépendante située au Cap. Le 3 janvier, un chercheur a observé via Shodan un serveur Windows exposé appartenant à son environnement alors qu'un ransomware était en cours d'exécution. La pharmacie et son fournisseur ProPharm ont été alertés et sont intervenus. L'observation et la réponse coordonnée corroborent l'incident ; l'exfiltration, le volume chiffré et l'identité de l'opérateur restent inconnus.

### 12 janvier 2026 - intégré le 01 septembre 2026
#### 🇿🇦 Afrique du Sud - Land and Agricultural Development Bank of South Africa (Land Bank)

- **Date de l'incident :** 12 janvier 2026
- **Date de confirmation publique détaillée :** 09 mars 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Non attribué publiquement
- **Secteur :** Gouvernement / Banque publique / Finance
- **Statut :** Victim Confirmed
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** La **Land and Agricultural Development Bank of South Africa (Land Bank)** est une institution financière de développement spécialisée dans l'**agriculture sud-africaine**. Elle finance les exploitations, les entreprises agro-industrielles et les nouveaux entrants dans les filières agricoles afin de soutenir la production et la transformation du secteur. Elle constitue une banque publique de développement sectorielle, distincte d'une banque commerciale généraliste ([présentation officielle](https://www.landbank.co.za/About-Us/Pages/Our-Business.aspx)).

- **Vérification indépendante au 18 octobre 2026 :** **Reconnaissance publique corroborée :** ITWeb a rapporté l’attaque ransomware contre Land Bank survenue en janvier 2026 et les mesures de renforcement prises. Cette fiche a été intégrée en septembre, mais l’incident ne date pas de septembre.

- **Sources de vérification complémentaires :** [Source 1](https://www.itweb.co.za/article/land-bank-tightens-security-after-ransomware-attack/raYAyMorlOl7J38N)

- **Sources / Éléments de preuve :** [ITWeb, 9 mars 2026](https://www.itweb.co.za/article/land-bank-tightens-security-after-ransomware-attack/raYAyMorlOl7J38N) ; [ITWeb, 16 janvier 2026](https://www.itweb.co.za/article/land-bank-flags-it-systems-disruption/Kjlyr7wBDRZvk6am)

Le ministre sud-africain des Finances a confirmé une attaque ransomware détectée le 12 janvier après une activité non autorisée. Une partie des serveurs et ordinateurs portables a été chiffrée et des fichiers ont été exfiltrés ; les systèmes ERP, core banking et CRM critiques n'auraient pas été compromis. L'acteur, le volume exact et la durée de présence restent inconnus.

### 23 mars 2026 - intégré le 01 septembre 2026
#### 🇿🇦 Afrique du Sud - Standard Bank South Africa

- **Date de l'incident / première communication :** 23 mars 2026
- **Mises à jour publiques :** 02, 13 et 14 avril 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Non attribué officiellement ; revendication distincte de PrinzEugen non corroborée
- **Secteur :** Finance / Banque
- **Statut :** Victim Confirmed
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** **Standard Bank South Africa** est l'activité bancaire sud-africaine du **Standard Bank Group**, groupe financier proposant notamment des comptes, paiements, financements, services aux entreprises et solutions d'investissement. La **Standard Bank of South Africa Limited** fait partie des entités juridiques identifiées par le groupe dans sa documentation institutionnelle ([déclaration officielle de confidentialité](https://www.standardbank.co.za/southafrica/personal/about-us/legal/privacy-statement)).

- **Vérification indépendante au 18 octobre 2026 :** **Confirmation de première main :** Standard Bank a déclaré le 23 mars 2026 un accès non autorisé à certaines données, tout en précisant que les systèmes transactionnels et les fonds des clients n’étaient pas touchés. L’événement est antérieur à septembre.

- **Sources de vérification complémentaires :** [Source 1](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank)

- **Sources / Éléments de preuve :** [Standard Bank, 23 mars 2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank) ; [Standard Bank, 14 avril 2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-data-incident-update-14-april)

Standard Bank a confirmé un accès non autorisé à des systèmes administratifs et espaces documentaires internes, avec exposition possible de noms, identifiants, coordonnées, adresses et numéros de compte. Les systèmes transactionnels et centraux n'auraient pas été accédés. Le vecteur, le nombre de personnes et le volume copié restent inconnus. Cette fiche est distincte de la revendication Standard Bank Group de mai.

### 18 avril 2026 - intégré le 01 septembre 2026
#### 🇿🇦 Afrique du Sud - Ahmed Al-Kadi Private Hospital

- **Date de l'incident :** 18 avril 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Non attribué publiquement
- **Secteur :** Santé / Hôpital privé
- **Statut :** Victim Confirmed
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** **Ahmed Al-Kadi Private Hospital** est un hôpital privé de **Mayville, à Durban**, en Afrique du Sud. Développé par l'**Islamic Medical Association of South Africa**, l'établissement a ouvert en 2017 et indique disposer de **163 lits**, avec des activités de soins hospitaliers et des spécialités médicales et chirurgicales. Sa mission déclarée est d'accueillir les patients sans distinction d'origine ou de religion ([site officiel](https://ahmedalkadi.com/about-us/)).

- **Vérification indépendante au 18 octobre 2026 :** **Confirmation directe :** l’hôpital annonce un accès non autorisé le 18 avril 2026, suivi du déploiement d’un ransomware ayant chiffré une partie de son environnement ; notification POPIA et signalement au régulateur. L’incident n’est pas daté de septembre.

- **Sources de vérification complémentaires :** [Source 1](https://ahmedalkadi.com/notification-of-data-incident/)

- **Sources / Éléments de preuve :** [Notification officielle de l'hôpital](https://ahmedalkadi.com/notification-of-data-incident/)

L'hôpital a confirmé qu'un tiers avait accédé à son environnement informatique et déployé un ransomware le 18 avril. Une partie de l'environnement a été chiffrée, puis contenue et restaurée avec l'aide de spécialistes externes. Le vecteur, l'étendue du chiffrement et l'exfiltration restent inconnus.

### 28 avril 2026 - intégré le 01 septembre 2026
#### 🇰🇪 Kenya - TikoHUB

- **Date de l'incident :** 28 avril 2026 (date de publication de l'offre d'accès ; compromission initiale non établie)
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Date de publication initiale :** 28 avril 2026 à 23:26 (heure affichée ; fuseau non indiqué)
- **Acteur / Groupe :** DarkMafiaX (compte affiché ; identité et affiliation non vérifiées)
- **Secteur :** Billetterie / Événementiel / Services numériques
- **Site web :** [tikohub.co.ke](https://www.tikohub.co.ke/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Access Sale
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4

- **Description :** **TikoHUB** est une plateforme kényane de **billetterie et de services événementiels** destinée aux organisateurs et aux participants. Son offre est centrée sur la découverte et la gestion d'événements, avec des parcours d'achat ou de participation en ligne. L'existence d'un portail public ne valide toutefois pas les privilèges d'administration prétendument proposés par le vendeur d'accès ([présentation officielle TikoHUB](https://www.tikohub.co.ke/about_us.php)).

- **Vérification indépendante au 18 octobre 2026 :** Aucune preuve publique indépendante d’une vente d’accès à TikoHUB ni communication de la société n’a été identifiée ; la publication suspecte date d’avril 2026 et son intégration au suivi est ultérieure.

  **Incident documenté dans la fiche AFRINTEL :** Une publication attribuée au compte DarkMafiaX propose un accès administrateur présenté comme lié à TikoHUB, une plateforme kényane de billetterie et de gestion d'événements. La publication et les identifiants visibles n'ont pas été testés ; AFRINTEL ne confirme ni leur validité, ni l'accès effectif, ni une compromission de TikoHUB.

- **Analyse :**

  **Observed :** La capture montre une publication intitulée « Admin Access To Tikohub.co.ke | Kenya », datée du 28 avril 2026 à 23:26 selon l'horodatage affiché. Elle contient une URL de ressource d'administration et des champs présentés comme un nom d'utilisateur et un mot de passe. Ces valeurs sont volontairement non reproduites et n'ont pas été testées. La capture a été communiquée à AFRINTEL le 24 septembre 2026.

  **Assumption :** Le domaine `tikohub.co.ke` correspond à une plateforme kényane de billetterie ; cette correspondance rend la cible plausible. La publication peut toutefois être erronée, recyclée, falsifiée ou concerner un accès limité à un composant tiers. La date du 28 avril correspond à la publication observée, pas nécessairement à la compromission initiale.

  **Unknown :** validité actuelle des identifiants, privilèges réels, système concerné, mode d'obtention, durée d'accès, exploitation effective, données consultées ou exfiltrées, confirmation par TikoHUB et éventuelle remédiation restent inconnus.

- **Périmètre de l'échantillon observé :** une capture d'une publication de forum ; aucune connexion, validation d'identifiant, téléchargement, interaction avec l'endpoint ou copie de secret n'a été réalisée.

- **Évaluation des risques :** si l'offre est authentique, un accès administrateur pourrait permettre la modification de contenus, l'accès à des données de clients ou d'organisateurs, la fraude aux billets et la compromission de comptes. Cette fiche ne confirme aucun de ces effets.

- **Recommandations :**
1. Préserver les journaux d'authentification, d'administration, d'API et d'hébergement depuis le 28 avril 2026.
2. Réinitialiser les comptes administrateurs potentiellement concernés et révoquer les sessions selon l'enquête défensive de TikoHUB.
3. Vérifier les changements de privilèges, exports, créations de comptes et modifications de billets ou d'événements.
4. Ne pas tester les identifiants publiés ni ouvrir l'URL sensible depuis la capture.
5. Surveiller l'usurpation, la fraude aux billets et les réutilisations de secrets.

- **Sources / Éléments de preuve :** capture fournie à AFRINTEL le 24 septembre 2026 ; site public [TikoHUB](https://www.tikohub.co.ke/).

### Fin mai 2026 - intégré le 01 septembre 2026
#### 🇿🇦 Afrique du Sud - Centre for High Performance Computing (CHPC) / Supercalculateur Lengau

- **Date de l'incident :** fin mai 2026
- **Date de confirmation publique détaillée :** 24 août 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Non attribué publiquement
- **Secteur :** Recherche / Infrastructure scientifique stratégique
- **Statut :** Victim Confirmed
- **Type d'incident :** System Intrusion
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** Le **Centre for High Performance Computing (CHPC)** est une infrastructure nationale sud-africaine de **calcul intensif**, rattachée à l'écosystème de recherche du **CSIR** et au dispositif NICIS. Il met des ressources de calcul scientifique à la disposition des universités et instituts de recherche ; **Lengau** est l'un des supercalculateurs emblématiques de cette infrastructure. Le CHPC n'est donc pas une entreprise commerciale ordinaire ([présentation officielle du CHPC](https://www.chpc.ac.za/about-the-chpc/)).

- **Vérification indépendante au 18 octobre 2026 :** **Confirmation institutionnelle relayée :** le CSIR et une réponse parlementaire ont fait état de la compromission du cluster Lengau fin mai 2026, liée à des vulnérabilités d’un système ancien, avec perturbation des ressources de calcul. Ne pas assimiler ce cas à un ransomware septembre.

- **Sources de vérification complémentaires :** [Source 1](https://www.itweb.co.za/article/cause-of-breach-on-sas-supercomputer-revealed/KPNG878NLeGq4mwD)

- **Sources / Éléments de preuve :** [ITWeb, 24 août 2026](https://www.itweb.co.za/article/cause-of-breach-on-sas-supercomputer-revealed/KPNG878NLeGq4mwD)

Une réponse parlementaire a confirmé un incident affectant une partie de l'environnement HPC Lengau à la fin mai, en lien avec des vulnérabilités d'un environnement ancien. L'accès, la durée de présence et les données éventuellement consultées restent inconnus.

### Juin 2026 - intégré le 01 septembre 2026
#### 🇿🇦 Afrique du Sud - MIP Holdings

- **Date de l'incident :** juin 2026, date exacte non établie
- **Première notification publique :** 26 juin 2026
- **Confirmation réglementaire complémentaire :** septembre 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Non attribué publiquement
- **Secteur :** Technologie / Logiciels / Prestataire de services
- **Statut :** Victim Confirmed
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** **MIP Holdings** est un éditeur et prestataire sud-africain de solutions **FinTech/InsurTech**. Ses plateformes couvrent notamment la gestion de contrats et de polices, la relation client et des processus métiers pour les assureurs, le secteur de la santé, le crédit et la retraite. Son rôle de fournisseur logiciel auprès de plusieurs organisations peut créer une exposition indirecte de clients lors d'un incident chez le prestataire ([site officiel MIP](https://www.mip.co.za/)).

- **Vérification indépendante au 18 octobre 2026 :** **Incident prestataire confirmé :** LegalWise a déclaré le 26 juin 2026 que MIP Holdings avait identifié un accès non autorisé sur un système historique de développement et d’assistance. Les données de clients de plusieurs assureurs ont ensuite été concernées ; cela ne confirme pas une intrusion chez chacun de leurs clients. Incident initial de juin.

- **Sources de vérification complémentaires :** [Source 1](https://www.legalwise.co.za/media-centre/statement-regarding-third-party-cybersecurity-incident)

- **Sources / Éléments de preuve :** [LegalWise, 26 juin 2026](https://www.legalwise.co.za/media-centre/statement-regarding-third-party-cybersecurity-incident) ; [TechCentral, 25 septembre 2026](https://techcentral.co.za/insurers-mip-breach-regulators/286482/)

MIP Holdings a identifié un accès non autorisé à un ancien environnement de développement et de support. L'Information Regulator sud-africain a confirmé en septembre travailler avec MIP pour établir les circonstances et le nombre de personnes affectées. La compromission et le risque de chaîne d'approvisionnement sont confirmés ; le volume et le vecteur restent inconnus.

### 14-15 juin 2026 - intégré le 01 septembre 2026
#### 🇬🇦 Gabon - Société d'Énergie et d'Eau du Gabon (SEEG)

- **Date de l'incident :** nuit du 14 au 15 juin 2026
- **Date de communication gouvernementale initiale :** 15 juin 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Non attribué publiquement
- **Secteur :** Énergie / Eau / Infrastructure critique
- **Statut :** Victim Confirmed
- **Type d'incident :** System Intrusion
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** La **Société d'Énergie et d'Eau du Gabon (SEEG)** est un opérateur de services publics intervenant dans la **production, le transport et la distribution de l'électricité**, ainsi que dans l'approvisionnement en **eau potable** au Gabon. Son activité repose sur des infrastructures industrielles et des systèmes de gestion indispensables à la continuité de services essentiels pour les ménages et les entreprises ([présentation officielle des activités SEEG](https://www.seeg-gabon.com/activites)).

- **Vérification indépendante au 18 octobre 2026 :** **Incident confirmé, attribution du mode d’action à préciser :** l’indisponibilité d’EDAN dans la nuit du 14 au 15 juin 2026 est documentée par le gouvernement gabonais. La SEEG a ensuite évoqué des actes de sabotage/malveillance informatique. Cela n’établit pas nécessairement une intrusion externe ni une exfiltration. Incident de juin.

- **Sources de vérification complémentaires :** [Source 1](https://gabonofficiel.com/seeg-un-sabotage-informatique-a-paralyse-95-de-son-systeme-la-cybersecurite-desormais-au-coeur-des-enjeux/) ; [Source 2](https://gouvernement.ga/2026/06/15/systeme-edan-retablissement-confirme-et-dispositif-de-protection-renforce-par-letat/)

- **Sources / Éléments de preuve :** [Gouvernement gabonais, 15 juin 2026](https://gouvernement.ga/2026/06/15/systeme-edan-retablissement-confirme-et-dispositif-de-protection-renforce-par-letat/) ; [Gabon Media Time, 5 août 2026](https://gabonmediatime.com/cybersecurite-la-seeg-revele-avoir-perdu-pres-de-95-de-ses-infrastructures-informatiques/)

Un incident majeur a perturbé les systèmes de la SEEG, notamment EDAN. Le gouvernement a évoqué des actes de malveillance et la SEEG a ensuite qualifié l'événement de sabotage, avec une perte annoncée de près de 95 % de ses infrastructures informatiques. Le mécanisme technique, les responsables et l'exfiltration restent inconnus.

### 12 juillet 2026 - intégré le 01 septembre 2026
#### 🇨🇲 Cameroun - Ministère de l'Emploi et de la Formation professionnelle (MINEFOP)

- **Date de l'incident :** 12 juillet 2026
- **Date d'analyse publique :** 27 juillet 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** ANTONKILL
- **Secteur :** Gouvernement / Administration publique
- **Statut :** Corroborated
- **Type d'incident :** Defacement
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 2
- **Description :** Le **Ministère de l'Emploi et de la Formation professionnelle (MINEFOP)** du Cameroun est chargé de concevoir et de mettre en œuvre les politiques publiques relatives à **l'emploi, à la formation et à l'insertion professionnelle**. Il intervient notamment dans l'orientation, la qualification et l'accompagnement vers l'emploi. Il s'agit d'une administration centrale, pas d'un établissement privé de formation ([missions officielles du MINEFOP](https://minefop.gov.cm/fr/missions/)).

- **Vérification indépendante au 18 octobre 2026 :** **Défacement publiquement corroboré :** le CIRT camerounais a publié une alerte sur la campagne ANTONKILL ayant visé le site du MINEFOP en juillet 2026. La portée démontrée concerne le portail web, pas l’ensemble du réseau ministériel. Incident de juillet.

- **Sources de vérification complémentaires :** [Source 1](https://cirt.cm/alerte-de-securite-campagne-antonkill-web-defacement-ciblant-les-institutions-sous-joomla-et-helix3/)

- **Sources / Éléments de preuve :** [OBS-CC, 27 juillet 2026](https://obs-cc.org/defacement-antonkill-minefop/) ; [Base d'incidents OBS-CC](https://obs-cc.org/incidents/)

L'OBS-CC, s'appuyant sur une alerte du CIRT de l'ANTIC, documente le défacement du site du MINEFOP dans une campagne attribuée à ANTONKILL. La profondeur de l'accès, la persistance et l'exposition de données non publiques ne sont pas établies.

### 15 juillet 2026 - intégré le 01 septembre 2026
#### 🇿🇦 Afrique du Sud - Rectron (Pty) Ltd

- **Date de l'incident détecté :** 15 juillet 2026
- **Date de notification SENS :** 22 juillet 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Non attribué officiellement ; DragonForce non confirmé
- **Secteur :** Technologie / Distribution informatique
- **Statut :** Victim Confirmed
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 3
- **Description :** **Rectron (Pty) Ltd** est un distributeur sud-africain de **produits et solutions informatiques**, appartenant au groupe **Mustek**. Son portefeuille comprend notamment logiciels, matériel informatique, réseaux, solutions de stockage, cloud et infrastructures de centres de données, distribués à un réseau de revendeurs et partenaires. L'organisation intervient ainsi dans la chaîne d'approvisionnement technologique ([site officiel Rectron](https://www.rectron.co.za/pages/about)).

- **Vérification indépendante au 18 octobre 2026 :** **Confirmation officielle de marché :** Mustek a publié le 22 juillet 2026 un avis SENS relatif à l’incident de sécurité chez Rectron. Cela établit l’incident, sans confirmer automatiquement le groupe revendiquant la compromission. Incident de juillet.

- **Sources de vérification complémentaires :** [Source 1](https://www2.sharenet.co.za/v3/sens_display.php?scode=MST&seq=33&tdate=20260722130100)

- **Sources / Éléments de preuve :** [Mustek / JSE SENS, 22 juillet 2026](https://www2.sharenet.co.za/v3/sens_display.php?scode=MST&seq=33&tdate=20260722130100)

Mustek a annoncé que Rectron avait subi une compromission affectant certains systèmes et opérations IT, avec accès illégal à certaines données. Rectron a lancé sa réponse à incident et notifié l'Information Regulator. Le vecteur, les catégories de données et le volume exfiltré restent inconnus.

### 18 juillet 2026 - intégré le 01 septembre 2026
#### 🇰🇪 Kenya - Site officiel du Président de la République (`president.go.ke`)

- **Date de l'incident :** 18 juillet 2026
- **Date de confirmation gouvernementale :** 18 juillet 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Non attribué publiquement
- **Secteur :** Gouvernement / Présidence
- **Statut :** Government Confirmed
- **Type d'incident :** Defacement
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 3
- **Description :** Le domaine **`president.go.ke`** correspond au **site institutionnel de la présidence de la République du Kenya**. Il diffuse des informations publiques sur les activités présidentielles, l'administration et la coordination de l'action gouvernementale. La cible de cette fiche est **un portail officiel**, et non nécessairement l'ensemble des services informatiques de la présidence ou du gouvernement kényan ([site institutionnel](https://www.president.go.ke/)).

- **Vérification indépendante au 18 octobre 2026 :** **Confirmation gouvernementale :** le ministère kényan des TIC a reconnu le 18 juillet 2026 le défacement de `president.go.ke` ; il indiquait alors qu’aucun accès à des données sensibles n’était établi. L’événement concerne juillet et un site web précis.

- **Sources de vérification complémentaires :** [Source 1](https://www.aa.com.tr/fr/afrique/kenya-le-site-officiel-de-la-pr%C3%A9sidence-pirat%C3%A9-des-hackers-r%C3%A9clament-une-rancon-en-bitcoin/4002284)

- **Sources / Éléments de preuve :** [ICT Authority / communiqué du ministère, 18 juillet 2026](https://www.linkedin.com/posts/kenya-ict-board_ministry-of-information-communications-activity-7484210613053784065-Fy7R) ; [The Standard, 18 juillet 2026](https://www.standardmedia.co.ke/national/article/2001553147/kabogo-no-sensitive-data-accessed-after-presidents-website-hack)

Le gouvernement kényan a confirmé le défacement du site présidentiel, qui affichait des messages hostiles, une adresse de portefeuille et une demande de 5 BTC. Aucune preuve d'accès à des données sensibles ou d'exfiltration n'a été rapportée. Le vecteur et l'identité de l'attaquant restent inconnus.

### 26 août 2026 - intégré le 01 septembre 2026
#### 🇿🇦 Afrique du Sud - Cartrack South Africa

- **Date de l'incident :** 26 août 2026
- **Date de communication publique :** 28 août 2026
- **Mise à jour :** 10 septembre 2026
- **Date de découverte / intégration AFRINTEL :** 01 septembre 2026
- **Acteur / Groupe :** Non attribué publiquement
- **Secteur :** Télématique / Mobilité / Services automobiles
- **Statut :** Victim Confirmed
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Very High
- **Niveau d'impact :** Level 4
- **Description :** **Cartrack South Africa** est un fournisseur de **télématique automobile**, de géolocalisation, de récupération de véhicules volés et de gestion de flottes. Ses services combinent équipements embarqués, plateformes numériques et services opérationnels pour particuliers et entreprises. L'activité implique la gestion de données de véhicules, d'abonnements et de clients, sans que cela implique leur exposition dans chaque incident ([site officiel Cartrack](https://www.cartrack.co.za/)).

- **Vérification indépendante au 18 octobre 2026 :** **Confirmation directe :** Cartrack indique avoir découvert un ransomware sur certains systèmes le 26 août 2026, et évoque une possible publication d’informations personnelles. La revendication Dire Wolf publiée en septembre ne vaut pas attribution forensique officielle. Incident initial d’août.

- **Sources de vérification complémentaires :** [Source 1](https://cartrack.co.za/platform/resources/news)

- **Sources / Éléments de preuve :** [Cartrack - Data Incident at Cartrack South Africa](https://cartrack.co.za/platform/resources/news)

Cartrack a confirmé un incident ransomware détecté le 26 août. Les serveurs affectés ont été isolés et la plateforme restaurée en cinq heures. Une mise à jour indique que des informations personnelles de certains clients avaient été consultées et pouvaient avoir été publiées sur un site à accès restreint. Le vecteur, l'opérateur et le volume exact restent inconnus.

## Publications ransomware de septembre

> Ces entrées proviennent du classeur local `AFRINTEL_Victimes_Africaines_Septembre_2026.xlsx`. La date indiquée est la date de la publication ou de l'observation dans le corpus source, pas nécessairement la date de compromission. Les listes ou revendications ransomware ne constituent pas à elles seules une confirmation de l'intrusion.

### 01 septembre 2026
#### 🇪🇬 Égypte - Holding Company for Construction and Development (HCCD)
- **Date de publication initiale :** 01 septembre 2026
- **Acteur / Groupe :** krybit
- **Secteur :** Construction
- **Site web :** [hccd-construction.com](https://hccd-construction.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** La **Holding Company for Construction and Development (HCCD)** est une holding égyptienne active dans la **construction, les travaux publics et l'aménagement immobilier**. Son site indique qu'elle supervise des entreprises intervenant dans les travaux de génie civil, les études techniques, l'habitat et les installations électriques. L'entité relève d'une structure de groupe : une revendication visant son nom ne permet pas de déterminer quelle filiale ou quel système serait concerné ([présentation officielle HCCD](https://hccd-construction.com/About_e.aspx)).

- **Vérification indépendante au 18 octobre 2026 :** Seule une inscription dans le suivi des publications attribuées à Krybit est corroborée ; aucune déclaration officielle de HCCD ou enquête vérifiable confirmant une intrusion dans ses systèmes n’a été identifiée.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 35624

Krybit a publié une revendication nommant la Holding Company for Construction and Development. La date correspond à l'observation de la fiche ; la compromission, le volume, le chiffrement et l'exfiltration restent inconnus.

#### 🇪🇬 Égypte - Mecca High Feed Factory
- **Date de publication initiale :** 01 septembre 2026
- **Acteur / Groupe :** krybit
- **Secteur :** Agriculture / Agroalimentaire
- **Site web :** [meccahighfeed.blogspot.com](https://meccahighfeed.blogspot.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **Mecca High Feed Factory** est présentée sur son site historique en arabe comme une activité égyptienne de **fabrication d'aliments pour volailles et bétail**, notamment des formulations végétales. Le blog commercial associe les marques **Mecca** et **High Feed** et publie des informations sur les produits et l'alimentation animale ; cette source autoéditée ne permet pas de vérifier indépendamment la situation juridique ou le périmètre industriel actuel ([blog de l'entreprise](https://meccahighfeed.blogspot.com/)).

- **Vérification indépendante au 18 octobre 2026 :** Les agrégateurs OSINT relaient une revendication Krybit, sans preuve indépendante de compromission ni déclaration de Mecca High Feed Factory identifiée. Certaines bases classent différemment le pays : ne pas modifier l’attribution géographique sans vérification.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 35627

Krybit a publié une revendication visant Mecca High Feed Factory, présentée comme une entreprise égyptienne de fabrication d'aliments pour animaux. Les éléments techniques et l'impact réel ne sont pas établis.

#### 🇪🇬 Égypte - Seashell Hospital
- **Date de publication initiale :** 01 septembre 2026
- **Acteur / Groupe :** krybit
- **Secteur :** Santé / Hôpital
- **Site web :** [seashellhospital.com](https://seashellhospital.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **Seashell Hospital** est un établissement de santé privé situé à **New Cairo**, en Égypte. Son site présente une offre de soins hospitaliers, de diagnostic et de traitement, comprenant notamment un service d'urgences fonctionnant en continu. Cette activité implique des processus cliniques et administratifs sensibles ; aucune fuite de dossiers de patients n'est démontrée par la seule fiche de revendication ([site officiel de l'hôpital](https://www.seashellhospital.com/AboutUs/Index)).

- **Vérification indépendante au 18 octobre 2026 :** La revendication Krybit visant Seashell Hospital figure dans plusieurs index de fuite, mais aucune notification de l’hôpital ni confirmation forensique indépendante n’a été identifiée. Ni une indisponibilité, ni une fuite de patients, ni un chiffrement ne sont établis.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 35637

Krybit a publié une revendication visant Seashell Hospital, établissement hospitalier privé situé en Égypte. Aucun élément public examiné ne confirme l'accès, le chiffrement ou une exfiltration.

### 07 septembre 2026
#### 🇿🇦 Afrique du Sud - VSB Attorneys Inc
- **Date de publication initiale :** 07 septembre 2026
- **Acteur / Groupe :** lockbit5
- **Secteur :** Services juridiques
- **Site web :** [vsbattorneys.co.za](https://vsbattorneys.co.za/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **VSB Attorneys Inc** est un **cabinet d'avocats sud-africain** proposant notamment des prestations en droit immobilier, transfert de propriété (*conveyancing*) et droit commercial. Il intervient auprès de clients particuliers et professionnels dans des opérations juridiques et contractuelles nécessitant des dossiers et justificatifs confidentiels. L'activité du cabinet ne préjuge pas de la nature des documents éventuellement touchés par l'incident revendiqué ([site officiel VSB](https://www.vsbattorneys.co.za/about-vsb-attorneys-law-firm/)).

- **Vérification indépendante au 18 octobre 2026 :** La revendication LockBit5 visant VSB Attorneys est documentée par des index de leak sites, sans réponse publique identifiée du cabinet ni preuve indépendante d’intrusion.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 35798

Lockbit5 a publié une revendication visant VSB Attorneys Inc, cabinet d'avocats sud-africain. La compromission et l'étendue des données ne sont pas confirmées.

#### 🇪🇬 Égypte - Nile Projects Trading
- **Date de publication initiale :** 07 septembre 2026
- **Acteur / Groupe :** TheGentlemen
- **Secteur :** Immobilier / Gestion immobilière
- **Site web :** [nileprojects.com](https://nileprojects.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **Nile Projects & Trading Company** est un groupe commercial égyptien dont l'histoire officielle remonte à **1972**. Initialement entreprise familiale, il s'est diversifié dans la **distribution de marques internationales, les pneumatiques, la mode haut de gamme et les projets immobiliers commerciaux**. Le champ de ses activités dépasse donc l'immobilier seul, mais la publication ne permet pas de savoir quelle branche serait visée ([présentation officielle Nile Projects](https://nileprojects.com/pages/about-us)).

- **Vérification indépendante au 18 octobre 2026 :** Les résultats publics retrouvés reproduisent la revendication The Gentlemen contre Nile Projects Trading ; aucune reconnaissance officielle, notification réglementaire ou vérification forensique ne permet de qualifier l’attaque de confirmée.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 35813

TheGentlemen a publié une revendication visant Nile Projects Trading, groupe égyptien actif notamment dans le commerce, l'immobilier et la distribution. Aucun élément ne confirme l'accès ou l'exfiltration.

#### 🇿🇦 Afrique du Sud - Hollard Insurance Group
- **Date de publication initiale :** 07 septembre 2026
- **Acteur / Groupe :** TheGentlemen
- **Secteur :** Assurance
- **Site web :** [hollard.co.za](https://www.hollard.co.za/)
- **Statut :** Third-Party Exposure Confirmed - Direct Breach Not Established
- **Type d'incident :** Data Leak (third-party exposure) / ransomware claim disputed
- **Description :** **Hollard Insurance Group** est un groupe d'**assurance sud-africain privé** proposant des solutions d'assurance vie, non-vie, de couverture des particuliers et des entreprises, ainsi que des produits liés à l'investissement. Le groupe est présent dans plusieurs marchés africains, directement ou au travers de partenariats. La revendication associée à son nom n'établit pas quelles entités juridiques ou filiales seraient concernées ([présentation officielle Hollard](https://www.hollard.co.za/our-world)).

- **Vérification indépendante au 18 octobre 2026 :** **Exposition via un tiers reconnue, intrusion chez Hollard contestée :** dans ses communiqués des 15 et 18 septembre 2026, Hollard reconnaît que des informations concernant certains assurés « funeral policies » ont été publiées à la suite de l’incident de **juin 2026 chez MIP Holdings**. Hollard a notifié des clients et saisi les autorités compétentes ; ses investigations n’ont trouvé **aucune compromission de son environnement**. La liste The Gentlemen ne doit donc pas être requalifiée en intrusion confirmée chez Hollard.

- **Sources de vérification complémentaires :** [Source 1](https://www.fanews.co.za/article/company-news-results/1/hollard/1301/hollard-statement-regarding-reported-cyber-threat-claims/44724) ; [Source 2](https://mybroadband.co.za/news/security/669576-momentum-group-company-responds-to-data-breach-claims.html)

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 35817

TheGentlemen a publié une revendication visant Hollard Insurance Group. Le corpus source décrit l'assureur et ses activités, mais ne fournit pas de preuve indépendante de compromission.

#### 🇿🇦 Afrique du Sud - RelyComply AML Platform
- **Date de publication initiale :** 09 septembre 2026
- **Acteur / Groupe :** Direwolf (revendication ; attribution technique non confirmée)
- **Secteur :** Fintech / Lutte contre le blanchiment
- **Statut :** Victim Confirmed - Unauthorized Access
- **Type d'incident :** System Intrusion (revendication ransomware non confirmée)
- **Sous-type :** Accès non autorisé confirmé ; lien Direwolf/chiffrement non démontré
- **Description :** **RelyComply** est un éditeur de technologie réglementaire (**RegTech**) proposant une plateforme de conformité **AML/KYC** destinée aux institutions soumises aux obligations de lutte contre le blanchiment. Sa solution vise à centraliser les contrôles d'identité et de connaissance client, la surveillance et les processus de conformité. Le profil public de l'entreprise ne confirme pas à lui seul le périmètre d'une éventuelle intrusion ([plateforme officielle RelyComply](https://relycomply.com/)).

- **Vérification indépendante au 18 octobre 2026 :** **Accès non autorisé confirmé par l’entreprise :** dans sa notification du 16 septembre, RelyComply indique avoir détecté le 8 septembre 2026 un accès à certains de ses systèmes via une vulnérabilité zero-day d’une application tierce. Systèmes concernés reconstruits, identifiants et jetons révoqués/renouvelés, faille corrigée et déclaration au régulateur sud-africain (**référence SC20263150**). Virgin Active et HuntEx documentent l’exposition potentielle de données transactionnelles via Peach Payments. **La responsabilité de Direwolf, le chiffrement et le volume revendiqué ne sont pas confirmés.**

- **Sources de vérification complémentaires :** [Source 1](https://relycomply.com/relycomply-cyber-incident-what-happened-and-what-you-can-do/) ; [Source 2](https://virginactivesa.freshdesk.com/support/solutions/articles/201000132941-cybersecurity-incident-at-relycomply) ; [Source 3](https://www.huntex.net/peach-payments-security-update)

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 35859

**Contexte initial de la revendication :** Direwolf avait inscrit RelyComply sur son site de fuite. La notification de l'entreprise confirme ensuite un accès non autorisé à certains systèmes et documente un vecteur apparent (zero-day d'une application tierce). Le lien opérationnel avec Direwolf, le chiffrement et le volume de données éventuellement extraites restent non démontrés.

### 12 septembre 2026
#### 🇲🇦 Maroc - La Sultana Hotel Group
- **Date de publication initiale :** 12 septembre 2026
- **Acteur / Groupe :** krybit
- **Secteur :** Hôtellerie
- **Site web :** [lasultanahotels.com](https://lasultanahotels.com/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Medium (publication affichée comme publiée et corpus local d'images associé ; provenance technique et exhaustivité non établies)
- **Niveau d'impact :** Level 3
- **Description :** **La Sultana Hotels** est une enseigne marocaine d'**hôtellerie de luxe** regroupant notamment deux établissements : **La Sultana Marrakech**, au cœur de la médina, et **La Sultana Oualidia**, sur la lagune atlantique. Le groupe met en avant une offre d'hébergement, de gastronomie et d'expériences touristiques haut de gamme. La revendication ne permet pas de déterminer quel établissement ou outil de réservation aurait été concerné ([site officiel La Sultana](https://www.lasultanahotels.com/?lang=fr)).

- **Observation de la publication :** Une capture datée du 14 septembre 2026 montre une fiche `lasultanahotels.com` marquée `PUBLISHED`, avec 3 914 vues, 0 image affichée et une taille de données revendiquée de 41 GB. Un compte à rebours affichait une échéance au 15 septembre 2026 à 12:57:51. Ces éléments décrivent l'état visible de la publication et non le résultat d'une négociation ou d'un paiement.

- **Analyse du corpus local associé :** Le répertoire de collecte contient 138 fichiers JPEG de scan, pour environ 54 Mo. L'examen visuel du sous-ensemble disponible montre des images de passeports internationaux et de pages d'identité. Cinq paires de fichiers sont des doublons exacts selon SHA-256, soit 135 empreintes distinctes sur 140 fichiers incluant les deux captures de publication. Le nombre de personnes, la source d'acquisition, le lien technique avec La Sultana, la couverture du corpus et l'exhaustivité restent inconnus.

- **Vérification indépendante au 18 octobre 2026 :** Aucune déclaration du groupe hôtelier ni confirmation publique indépendante de l'intrusion n'a été identifiée. Le corpus d'images renforce l'observation d'une mise à disposition de données associée à la publication, mais ne confirme pas que les passeports proviennent des systèmes de La Sultana ni qu'ils concernent ses clients, employés ou partenaires.

- **Sources / Éléments observés :** publication Krybit capturée le 14 septembre 2026 ; corpus local de 138 scans JPEG associé à la collecte ; classeur local AFRINTEL, entrée ID 35923. Les artefacts bruts restent hors dépôt.

Krybit a publié une revendication visant La Sultana Hotel Group au Maroc. La fiche affichée comme publiée et le corpus local de scans indiquent une mise à disposition de données associée à la publication. Ils ne permettent pas d'établir l'accès initial, la provenance depuis les systèmes de La Sultana, le chiffrement, l'exhaustivité ou le nombre de personnes concernées.

#### 🇪🇬 Égypte - Egyptian Airports Company (EAC)
- **Date de publication initiale :** 12 septembre 2026
- **Acteur / Groupe :** krybit
- **Secteur :** Transport aérien
- **Site web :** [eac-airports.com](https://www.eac-airports.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** L'**Egyptian Airports Company (EAC)** est un opérateur égyptien du secteur **aéroportuaire**, rattaché à l'écosystème public de l'**Egyptian Holding Company for Airports and Air Navigation**. Sa mission porte sur la gestion, l'exploitation, la maintenance et le développement d'aéroports civils. Son rôle est différent de celui d'une compagnie aérienne ou de l'autorité de navigation aérienne ; aucun aéroport précis n'est établi comme compromis par la seule revendication ([ministère égyptien de l'Aviation civile](https://web.civilaviation.gov.eg/Companies/AirportCompany)).

- **Vérification indépendante au 18 octobre 2026 :** Plusieurs outils CTI recensent la déclaration Krybit visant le domaine d’Egyptian Airports Company. Aucune reconnaissance par EAC ou autorité égyptienne, ni preuve d’impact sur des systèmes d’exploitation aéroportuaire, n’a été identifiée.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 35917

Krybit a publié une revendication visant l'Egyptian Airports Company. La publication identifie l'organisation et son secteur ; le résultat technique et l'étendue d'une éventuelle exposition restent inconnus.

### 16 septembre 2026
#### 🇳🇦 Namibie - Namibian Defence Force
- **Date de publication initiale :** 16 septembre 2026
- **Acteur / Groupe :** RansomHouse (association déclarée par NAM-CSIRT)
- **Secteur :** Défense / Forces armées
- **Statut :** Government Confirmed - Unauthorized Access
- **Type d'incident :** System Intrusion (revendication ransomware ; chiffrement non confirmé)
- **Sous-type :** Intrusion ministérielle confirmée ; chiffrement/exfiltration non démontrés
- **Description :** La **Namibian Defence Force (NDF)** constitue les **forces armées nationales de la Namibie**. Sa mission constitutionnelle centrale consiste à défendre l'intégrité territoriale et les intérêts nationaux du pays, sous l'autorité des institutions de défense namibiennes. Une revendication faisant référence à la NDF ne démontre pas à elle seule une compromission de réseaux militaires opérationnels ([ministère namibien de la Défense](https://mod.gov.na/about-ndf)).

- **Vérification indépendante au 18 octobre 2026 :** **Compromission confirmée par l’autorité cyber nationale :** selon la déclaration NAM-CSIRT relayée le 21 septembre 2026, des activités non autorisées ont été détectées dans le réseau du **Ministry of Defence and Veterans Affairs (MODVA)**, et l’enquête a associé l’incident à **RansomHouse**. La revendication nomme « Namibian Defence Force », mais le périmètre officiellement confirmé est le réseau ministériel. **Aucune preuve publiée ne confirme le chiffrement, l’exfiltration, une fuite de secrets militaires ou un paiement.**

- **Sources de vérification complémentaires :** [Source 1](https://www.theregister.com/cyber-crime/2026/09/21/ransomhouse-picks-a-fight-with-namibias-defense-establishment/5297816) ; [Source 2](https://www.namibian.com.na/hackers-hit-ndf-ransomhouse-threatens-state-secrets/)

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 36039

**Contexte initial de la revendication :** RansomHouse a désigné la Namibian Defence Force dans sa publication. Les investigations publiées par NAM-CSIRT confirment ultérieurement une activité non autorisée dans le réseau du ministère de la Défense et une association avec RansomHouse, sans démontrer le chiffrement ni une exfiltration.

### 18 septembre 2026
#### 🇹🇳 Tunisie - Opérations de support PayPal (Transcom WorldWide)
- **Date de publication initiale :** 18 septembre 2026
- **Acteur / Groupe :** N0n
- **Secteur :** Services aux entreprises / Support client
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **Transcom WorldWide** est un groupe de **sous-traitance de la relation client (BPO/CX)** fournissant des services de centres de contact, d'assistance clientèle et de gestion de processus pour des marques internationales, notamment depuis des sites en Tunisie. **PayPal** est une entreprise distincte de services de paiement. La publication les associe à des opérations de support, mais **l'existence et le périmètre d'un contrat PayPal-Transcom concerné ne sont pas corroborés** par ces informations générales ([services officiels Transcom](https://transcom.com/services/customer-experience)).

- **Vérification indépendante au 18 octobre 2026 :** Aucune confirmation indépendante de l’intrusion ni de l’association opérationnelle exacte entre Transcom, PayPal et les sites tunisiens n’a été identifiée. Les cartographies Citrix/AD et 86,7 millions de connexions proviennent uniquement de la revendication N0n.

- **Sources de vérification complémentaires :** [Source 1](https://cypro.co.uk/insights/cyber-bulletins/n0n-ransomware-claim-targets-transcom/)

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 36122

N0n a publié une revendication visant des opérations de support externalisées liées à PayPal et Transcom WorldWide en Tunisie. La publication mentionne des systèmes internes et un délai de règlement, mais ne confirme pas l'accès, l'exactitude des volumes ou l'impact opérationnel.

### 21 septembre 2026
#### 🇪🇹 Éthiopie - Siinqee Bank
- **Date de publication initiale :** 21 septembre 2026
- **Acteur / Groupe :** lockbit5
- **Secteur :** Banque
- **Site web :** [siinqeebank.com](https://siinqeebank.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **Siinqee Bank** est une institution bancaire éthiopienne proposant des **services de banque de détail, de financement et d'inclusion financière**, notamment à destination de communautés et d'entrepreneurs. L'établissement présente une offre associant services bancaires traditionnels, microfinance et canaux numériques. Son nom s'inspire d'un symbole culturel oromo lié à la protection et à la reconnaissance des femmes ([présentation officielle Siinqee Bank](https://siinqeebank.com/about-us/)).

- **Vérification indépendante au 18 octobre 2026 :** La page de prévention contre la fraude publiée par Siinqee Bank le 8 octobre 2026 ne constitue **pas** une confirmation de l’attaque revendiquée par LockBit le 21 septembre. Aucune notification spécifique de cette intrusion ni de fuite n’a été trouvée.

- **Sources de vérification complémentaires :** [Source 1](https://siinqeebank.com/2026/10/08/stay-alert/)

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 36161

Lockbit5 a publié une revendication visant Siinqee Bank, institution financière éthiopienne. Aucun élément indépendant ne confirme l'intrusion ou l'exposition de données.

#### 🇦🇴 Angola - Grupolider
- **Date de publication initiale :** 21 septembre 2026
- **Acteur / Groupe :** TheGentlemen
- **Secteur :** Distribution / Agriculture / Logistique
- **Site web :** [grupolider-ao.com](https://grupolider-ao.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **Grupolider** est un nom associé à des **activités commerciales en Angola**. Des sources publiques relient le domaine `grupolider-ao.com` à des entreprises de distribution/importation et à **Novagrolider**, active dans l'agriculture et l'agro-industrie. Le site du domaine apparaît suspendu lors de cette recherche ; l'appartenance juridique des différentes entités au groupe et l'identité précise de l'entreprise visée **restent à confirmer** ([annuaire commercial argentin](https://exportaciones.cancilleria.gob.ar/sitios/ficha_directorio/89314) ; [fiche Novagrolider](https://icrisco.com/profile.php?id=novagrolider-5238)).

- **Vérification indépendante au 18 octobre 2026 :** Le référencement de Grupolider par The Gentlemen demeure une revendication de leak site ; aucune confirmation officielle ni lien technique certain entre le domaine revendiqué et les entités du groupe n’a été identifié.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 36171

TheGentlemen a publié une revendication visant Grupolider, groupe angolais actif dans l'agriculture, la logistique, la construction et la distribution. La compromission et le volume annoncé restent inconnus.

### 24 septembre 2026
#### 🇹🇿 Tanzanie - Air Tanzania Company Limited (ATCL)
- **Date de publication initiale :** 24 septembre 2026
- **Acteur / Groupe :** krybit
- **Secteur :** Transport aérien
- **Site web :** [airtanzania.co.tz](https://airtanzania.co.tz/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** Medium
- **Description :** **Air Tanzania Company Limited (ATCL)** est la **compagnie aérienne nationale de Tanzanie**, détenue par l'État. Elle assure des services de transport de passagers et de fret et exploite des liaisons nationales et internationales. Son activité repose sur des systèmes de réservation, d'exploitation aérienne et de relation client ; la présence d'images dans un échantillon ne permet pas d'en déduire leur origine dans ces systèmes ([présentation officielle Air Tanzania](https://airtanzania.co.tz/index.php/about-us)).

- **Vérification indépendante au 18 octobre 2026 :** La revendication Krybit visant les domaines d’Air Tanzania figure dans les flux OSINT ; les sources consultées précisent qu’Air Tanzania n’avait pas confirmé l’incident. La présence d’un échantillon revendiqué n’établit pas l’exfiltration depuis les systèmes de réservation ni le chiffrement.

- **Sources de vérification complémentaires :** [Source 1](https://www.galaxywarden.com/blog/breach/airtanzania-co-tz-airtanzania-com-krybit-2026-09)

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 36284

Krybit a publié une revendication visant Air Tanzania Company Limited, compagnie aérienne nationale tanzanienne. Un échantillon local associé à cette publication a été examiné en lecture seule : **114 fichiers** pour **676 972 266 octets**, dont **112 images valides** et **2 fichiers non image malgré l'extension `.jpg`**. Les images valides comprennent **101 fichiers MPO à trois vues** et **11 JPEG simples**, soit **314 vues incorporées** au total. Aucun doublon SHA-256 n'a été détecté.

Cette cohérence structurelle confirme la présence d'un corpus d'images associé à la publication, mais ne confirme pas que les fichiers proviennent de l'infrastructure d'Air Tanzania, ni l'accès initial, l'exfiltration, le chiffrement, le nombre de personnes représentées ou l'exhaustivité de la revendication. Aucun OCR, traitement facial, nom de fichier individuel ou contenu personnel n'a été reproduit. Le manifeste minimisé est conservé hors dépôt sous `/tmp/afrintel-evidence/afr-2026-09-airtanzania/evidence_manifest.json`.

#### 🇺🇬 Ouganda - Armada Credit Bureau
- **Date de publication initiale :** 24 septembre 2026
- **Acteur / Groupe :** Spirals
- **Secteur :** Services financiers / Bureau de crédit
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **Armada Credit Bureau Limited** se présente comme un **bureau ougandais de renseignements sur le crédit et d'analyse financière**, opérant dans le cadre réglementaire de la **Bank of Uganda**. Son activité porte sur les informations de solvabilité et les services d'évaluation du risque de crédit aux organismes habilités. Cette description provient de son site public et ne constitue pas une vérification indépendante de l'agrément ni d'un incident ([site Armada Credit Bureau](https://www.armadacrb.com/)).

- **Vérification indépendante au 18 octobre 2026 :** Seule la présence d’Armada Credit Bureau dans les listings du groupe Spirals est corroborée. Aucune déclaration de la société ou notification officielle ougandaise démontrant une intrusion n’a été identifiée.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 36306

Spirals a publié une revendication visant Armada Credit Bureau Limited, société ougandaise de reporting et d'analyse du crédit. Aucun élément indépendant ne confirme la compromission.

### 25 septembre 2026
#### 🇰🇪 Kenya - Majani Insurance Brokers
- **Date de publication initiale :** 25 septembre 2026
- **Acteur / Groupe :** Vexy Ransomware
- **Secteur :** Assurance
- **Site web :** [majaninsure.com](https://majaninsure.com/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **Majani Insurance Brokers Limited** est un **cabinet de courtage en assurances au Kenya**, proposant des solutions de couverture aux particuliers et aux entreprises. Ses services comprennent l'identification de garanties, la mise en relation avec les assureurs, le renouvellement de contrats et l'assistance lors des déclarations de sinistres. Le courtier se présente comme disposant de plusieurs décennies d'expérience sur le marché ([présentation officielle Majani](https://majaninsure.com/about/)).

- **Vérification indépendante au 18 octobre 2026 :** La revendication de Vexy contre Majani Insurance Brokers apparaît dans les bases de renseignement, sans reconnaissance publique de l’entreprise ni corroboration technique indépendante.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 36310

Vexy Ransomware a publié une revendication visant Majani Insurance Brokers, courtier d'assurance kényan. Le vecteur, les systèmes touchés et toute exfiltration restent inconnus.

### 26 septembre 2026
#### 🇿🇦 Afrique du Sud - Guardrisk
- **Date de publication initiale :** 26 septembre 2026
- **Acteur / Groupe :** TheGentlemen
- **Secteur :** Assurance
- **Site web :** [guardrisk.co.za](https://guardrisk.co.za/)
- **Statut :** Third-Party Exposure Confirmed - Direct Breach Not Established
- **Type d'incident :** Data Leak (third-party exposure) / ransomware claim disputed
- **Description :** **Guardrisk** est un groupe d'assurances sud-africain spécialisé dans les **solutions de transfert et de financement des risques**, notamment les structures d'**assurance captive en cellules** (*cell-captive insurance*). Ses offres concernent l'assurance vie, non-vie et des mécanismes de couverture adaptés aux entreprises et partenaires. L'appellation Guardrisk recouvre plusieurs entités réglementées ; la publication ne précise pas laquelle serait touchée ([site officiel Guardrisk](https://guardrisk.co.za/about/)).

- **Vérification indépendante au 18 octobre 2026 :** **Exposition chez un intermédiaire reconnue, intrusion chez Guardrisk démentie :** le 30 septembre 2026, Guardrisk a indiqué à MyBroadband qu’aucune compromission de ses systèmes ou données client n’était mise en évidence. Le groupe a relié les informations évoquées à une exposition chez **CoverCubed**, titulaire d’un mandat de gestion, concernant environ **6 000 polices obsèques** ; CoverCubed aurait notifié le régulateur et ses clients. **Ne pas attribuer directement ces données à une intrusion de Guardrisk.**

- **Sources de vérification complémentaires :** [Source 1](https://mybroadband.co.za/news/security/669576-momentum-group-company-responds-to-data-breach-claims.html)

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 36351

TheGentlemen a publié une revendication visant Guardrisk, groupe d'assurance sud-africain. La publication fournit un contexte organisationnel, mais ne confirme pas l'accès ni l'étendue de données détenues.

### 29 septembre 2026
#### 🇿🇦 Afrique du Sud - BCX / Business Connexion
- **Date de publication initiale :** 29 septembre 2026
- **Acteur / Groupe :** incransom
- **Secteur :** Technologies de l'information / Conseil
- **Site web :** [bcx.co.za](https://www.bcx.co.za/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Ransomware
- **Description :** **BCX (Business Connexion)** est un fournisseur sud-africain de **services informatiques et d'intégration de systèmes**, filiale du **groupe Telkom**. Il accompagne des entreprises et administrations dans la transformation numérique, la connectivité, les infrastructures, le cloud et les services IT. Ses prestations couvrant plusieurs clients et environnements, la revendication visant BCX ne permet pas d'imputer automatiquement un incident à ses clients ([présentation officielle BCX](https://www.bcx.co.za/contact-us/)).

- **Vérification indépendante au 18 octobre 2026 :** La publication d’INC Ransom visant BCX est reprise par des plateformes CTI ; aucune déclaration de BCX ou du groupe Telkom, dépôt réglementaire ou enquête indépendante confirmant le chiffrement, l’exfiltration ou la compromission de clients n’a été identifiée.

- **Sources / Éléments de preuve :** classeur local AFRINTEL, entrée ID 36421

Incransom a publié une revendication visant BCX / Business Connexion et annonce **500 Go**, 4 224 088 fichiers et 596 613 dossiers, ainsi que du code source et des applications métiers. Ces volumes et catégories sont des revendications de l'acteur ; l'accès, l'exfiltration et l'exhaustivité ne sont pas confirmés.

## Remarque de suivi intermensuel

Cette remarque ne constitue pas une nouvelle fiche ni un nouvel incident comptabilisé en septembre.

La [fiche du Ministry of Education of Libya de juin 2026](../../06-june/victims_FR.md) documente une publication attribuée à **EvaN47**, avec un volume revendiqué de **287 Go**. Un échantillon visuel avait alors été examiné : galerie de documents, certificats de fin d'études, documents scolaires et administratifs, images scannées et fichiers PDF, avec des références à des numéros nationaux, des photographies personnelles et des images de passeports. L'analyse portait sur les éléments visibles ; le volume total revendiqué et l'exhaustivité de la base n'étaient pas validés.

La publication du **10 septembre 2026**, attribuée à **EveN47**, revendique ensuite **800 Go** pour la base de moe.gov.ly et environ **300 Go** de données similaires couvrant plusieurs ministères libyens de l'Éducation. Un échantillon local fourni comme provenant de cette publication a toutefois été analysé en lecture seule : **900 976 395 octets** (environ **901 Mo**), **3 900 fichiers** répartis en quatre répertoires correspondant aux passeports (**1 145** fichiers), numéros nationaux (**467**), photos d'étudiants (**1 146**) et certificats d'étudiants (**1 142**). Les signatures indiquent 3 500 JPEG et 4 PNG valides ; cinq fichiers portant l'extension `.jpg` sont en réalité des PDF et deux autres des documents HTML. L'empreinte SHA-256 arborescente agrégée est `d63371c3d61dd48c87398578d1bdfe4329c7dca1bc73104125e966221591df80`. Le contrôle SHA-256 a relevé **169 groupes de doublons** représentant **213 fichiers excédentaires**, ce qui ne permet pas de déduire un nombre de personnes ou de documents uniques. Aucun OCR massif ni recopie de contenu individuel n'a été réalisé afin de limiter l'exposition des données personnelles ; l'analyse porte sur l'arborescence, les signatures, les métadonnées techniques et les contrôles d'intégrité. Cette structure renforce la corroboration interne de la nature documentaire et éducative du jeu de données, sans valider les revendications de 287 Go, 800 Go ou 300 Go. Aucun lien de téléchargement n'a été ouvert et aucune donnée personnelle brute n'est reproduite ici. Il n'est pas établi s'il s'agit d'une extension, d'une republication, d'un volume révisé ou d'une revendication par un alias différent. Les chiffres de 287 Go, 800 Go et 300 Go ne doivent pas être additionnés ; ils restent des revendications datées et distinctes.
