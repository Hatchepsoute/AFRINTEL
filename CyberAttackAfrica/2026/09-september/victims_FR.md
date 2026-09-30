![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en septembre 2026 (11 fiches)

👉🏾 [**English version available here**](./victims.md)

## Septembre 2026

**Statut du suivi mensuel : In Progress / En cours** — corpus provisoire de 11 fiches ; la clôture et les statistiques mensuelles restent à venir.

### 03 septembre 2026
#### 🇳🇬 Nigéria - Medical and Dental Council of Nigeria (MDCN)

- **Date de publication initiale :** 3 septembre 2026 à 20:19 (heure affichée ; fuseau non indiqué)
- **Date de découverte AFRINTEL :** 28 septembre 2026 (capture et extrait textuel fournis)
- **Acteur / Groupe :** cattier (compte de forum affiché ; identité non vérifiée)
- **Secteur :** Santé / Régulation des professions médicales et dentaires
- **Site web :** [mdcn.gov.ng](https://www.mdcn.gov.ng/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Medium (publication et extrait structurés observés ; origine et étendue non corroborées)
- **Niveau d'impact :** Level 3

- **Description :** Un compte nommé cattier a publié une offre intitulée « Medical and Dental Council of Nigeria 65K » et attribue au domaine `mdcn.gov.ng` des données concernant **65 580 utilisateurs uniques**. Un extrait de dossiers de professionnels de santé est visible et **50 lignes ont été communiquées en texte**. Ces éléments établissent l'existence de la publication et la nature des données présentées ; ils ne confirment ni que 65 580 personnes distinctes sont concernées, ni une intrusion dans les systèmes du MDCN.

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

- **Description :** Madinaty est un projet urbain résidentiel en Égypte que le groupe Talaat Moustafa présente parmi ses projets dans le pays. Cette information situe le contexte géographique ; elle ne permet pas d'identifier l'organisation ayant collecté ou détenu les données ni de confirmer que le groupe Talaat Moustafa a été compromis. ([Présentation du groupe Talaat Moustafa](https://ecommerce.tmg.com.eg/about))

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
- **Date de découverte AFRINTEL :** 9 septembre 2026
- **Acteur / Groupe :** xNov
- **Secteur :** Éducation / Formation professionnelle
- **Site web :** [atlantique.ma](https://atlantique.ma/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 3

- **Description :** Centre Atlantique Formation est un organisme marocain de formation professionnelle proposant des formations pratiques dans plusieurs domaines et au sein de différents centres. Les enregistrements observés font notamment référence au diagnostic automobile, à la comptabilité, l'infographie, la cuisine, la pâtisserie, la coiffure, au stylisme et modélisme, à l'informatique bureautique, la soudure, la plomberie et l'assistance médicale.

- **Analyse :**

  Le 6 septembre 2026, l'acteur **xNov** a publié une revendication visant atlantique.ma et diffusé une archive associée à Centre Atlantique Formation. Un relais Telegram observé le même jour annonçait une archive d'environ **2,49 Go** et affirmait que les données publiées ne représentaient que **27 % de la base**. Les **73 %** correspondent à une déduction arithmétique à partir des 27 % revendiqués et non à une mesure indépendante. Lors d'un contact direct via le canal Telegram, xNov a proposé le reste pour **300 USD** : le prix demandé est donc directement observé comme une offre de l'acteur. Cette observation ne confirme ni l'existence, ni le volume, ni la disponibilité effective des données restantes, et ne constitue pas la preuve d'une transaction.

  Après extraction, l'archive analysée occupe environ **4 Go** et contient **1 155 dossiers regroupant 3 465 éléments**, soit exactement trois éléments par dossier. La structure repose sur les informations d'inscription, les métadonnées de certificats et une attestation PDF.

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

- **Sources / Éléments de preuve :** publication xNov sur un forum underground (6 septembre 2026), relais et capture Telegram fournis (6 septembre 2026), contact direct avec xNov via son canal Telegram concernant le prix demandé, analyse AFRINTEL de l'archive et des dossiers extraits.


### 09 septembre 2026
#### 🇪🇬 Égypte - Badr University in Cairo (BUC)

- **Date de l'incident :** Non établie
- **Date de publication initiale :** 9 septembre 2026 à 16:50 (fuseau horaire non indiqué)
- **Date de découverte AFRINTEL :** 12 septembre 2026
- **Acteur / Groupe :** Unknown
- **Compte auteur affiché :** elmo7areb (identité et rôle non vérifiés)
- **Secteur :** Éducation / Enseignement supérieur
- **Site web :** [buc.edu.eg](https://buc.edu.eg/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3

- **Description :** Badr University in Cairo (BUC) est un établissement d'enseignement supérieur égyptien situé à Badr City. Son site officiel présente ses programmes et services, notamment des démarches d'admission et un portail étudiant.

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
- **Date de découverte AFRINTEL :** 22 septembre 2026 (capture et échantillon local fournis)
- **Acteur / Groupe :** Kazu (compte affiché ; identité et affiliation non vérifiées)
- **Secteur :** Gouvernement / Services publics numériques
- **Site web :** [sepe.gov.ao](https://www.sepe.gov.ao/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Niveau de confiance :** High
- **Niveau d'impact :** Level 4

- **Description :** Une publication attribuée au compte Kazu vise SEPE, la plateforme officielle de services publics électroniques de l'Angola, et revendique une exposition de données dans un contexte d'extorsion ransomware. AFRINTEL a examiné un échantillon local dérivé de la publication ; cette analyse renforce la cohérence structurelle et l'association avec des données administratives angolaises, sans confirmer l'accès initial, l'exfiltration complète, le volume global revendiqué ou la compromission officielle de SEPE.

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
- **Date de découverte AFRINTEL :** 28 septembre 2026 (captures et images locales examinées)
- **Acteur / Groupe :** BLACKLOCKS
- **Secteur :** Distribution de pièces détachées / Transport routier
- **Site web :** [apollo21.co.za](https://apollo21.co.za/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Sous-type :** Exfiltration de données revendiquée ; chiffrement non établi
- **Niveau de confiance :** High (publication et lien documentaire avec Apollo 21 ; compromission et volume global non confirmés)
- **Niveau d'impact :** Level 3

- **Description :** La fiche Apollo 21 apparaît dans une liste de victimes de BLACKLOCKS avec la date du **19 septembre 2026**. Une autre vue de cette fiche associe `apollo21.co.za` à l'Afrique du Sud et revendique **400 GB** de données. Les images d'échantillon examinées comprennent des tableaux commerciaux et financiers ainsi que des pièces d'identité. Elles étayent le lien documentaire avec Apollo 21, sans confirmer la méthode d'acquisition, le chiffrement ou la possession de 400 Go.

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
- **Date de découverte AFRINTEL :** 28 septembre 2026 (capture et PDF fournis)
- **Acteur / Groupe :** individual (compte affiché ; identité non vérifiée)
- **Secteur :** Gouvernement / Administration fiscale
- **Site web :** [fctirs.gov.ng](https://fctirs.gov.ng/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** High (publication et association de l'échantillon au FCT-IRS ; origine technique non établie)
- **Niveau d'impact :** Level 3

- **Description :** Une publication intitulée « Nigerian Tax Authority | Full Breach » affiche le logo du **Federal Capital Territory Internal Revenue Service (FCT-IRS)** et fait référence à des images de personnes et de signatures. Le PDF fourni, exporté depuis JustPaste.it, contient **314 pages** de texte et présente des données personnelles. L'expression « Full Breach » est le titre revendiqué par l'auteur ; l'exhaustivité des données et une compromission du système du FCT-IRS ne sont pas établies.

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
- **Date de découverte AFRINTEL :** 28 septembre 2026 (captures et échantillons locaux examinés)
- **Acteur / Groupe :** BLACKLOCKS
- **Secteur :** Architecture / Conception et gestion de projets
- **Site web :** [arcaunlimited.com](https://arcaunlimited.com/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Sous-type :** Exfiltration de données revendiquée ; chiffrement non établi
- **Niveau de confiance :** High (publication et lien documentaire avec ARCA ; acquisition et volume global non confirmés)
- **Niveau d'impact :** Level 3

- **Description :** BLACKLOCKS présente ARCA Unlimited Architects comme victime sud-africaine et affiche un volume de **400G** sans préciser l'unité. Les images d'échantillon comprennent des plans architecturaux, des documents de projet et des tableaux de coûts. Plusieurs éléments portent le nom ou la marque ARCA et sont cohérents avec son activité. L'examen ne confirme ni la méthode d'acquisition, ni un chiffrement, ni la possession du volume revendiqué.

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

- **Description :** AFRICA-TECH est présentée dans la publication de N0n comme une entreprise malienne de services IT et de traitement documentaire. L'ensemble des fichiers divulgués par le groupe a été fourni pour analyse. Une réclamation Word mentionne AFRICA-TECH et des références au Mali et à Bamako, ce qui étaye le lien documentaire avec l'organisation. Le domaine proposé, https://www.africatech-mali.com/, présente des activités solaires et électriques à Bamako. La comparaison avec les documents n'a pas établi de coordonnées communes ; son attribution à la victime reste non établie.

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

### 24 septembre 2026
#### 🇰🇪 Kenya - TikoHUB

- **Date de l'incident :** 28 avril 2026 (date de publication de l'offre d'accès ; compromission initiale non établie)
- **Date de publication initiale :** 28 avril 2026 à 23:26 (heure affichée ; fuseau non indiqué)
- **Date de découverte AFRINTEL :** 24 septembre 2026 (capture fournie)
- **Acteur / Groupe :** DarkMafiaX (compte affiché ; identité et affiliation non vérifiées)
- **Secteur :** Billetterie / Événementiel / Services numériques
- **Site web :** [tikohub.co.ke](https://www.tikohub.co.ke/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Access Sale
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 4

- **Description :** Une publication attribuée au compte DarkMafiaX propose un accès administrateur présenté comme lié à TikoHUB, une plateforme kényane de billetterie et de gestion d'événements. La publication et les identifiants visibles n'ont pas été testés ; AFRINTEL ne confirme ni leur validité, ni l'accès effectif, ni une compromission de TikoHUB.

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

### 25 septembre 2026
#### 🇲🇦 Maroc - Pharma 5

- **Date de publication initiale :** 25 septembre 2026 à 08:27 (heure affichée ; fuseau non indiqué)
- **Date de découverte AFRINTEL :** 28 septembre 2026 (images locales examinées)
- **Acteur / Groupe :** INC Ransom
- **Secteur :** Santé / Industrie pharmaceutique
- **Site web :** [pharma5.ma](https://www.pharma5.ma/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Ransomware
- **Sous-type :** Exfiltration de données revendiquée
- **Niveau de confiance :** High (existence de la publication et cohérence de l'échantillon visible ; périmètre et acquisition non établis)
- **Niveau d'impact :** Level 3

- **Description :** INC Ransom a publié une fiche visant Pharma 5 et revendique **50 Go** de données. La publication présente une galerie d'aperçus documentaires ; une page de gestion qualité a aussi été fournie en taille lisible. Les éléments visibles sont cohérents avec des activités pharmaceutiques et une chaîne d'approvisionnement. Cette cohérence ne confirme ni l'intrusion, ni la méthode d'acquisition, ni les 50 Go annoncés.

- **Analyse :**

  **Observed :** La publication datée du **25 septembre 2026** associe `pharma5.ma` à INC Ransom et affiche **50 Gb** (repris ici comme **environ 50 Go revendiqués**). Elle revendique des informations d'entreprise et financières, des données sur les produits et l'approvisionnement, le contrôle qualité et les certifications, des informations relatives aux tests de médicaments, ainsi que des données d'employés et de partenaires. La galerie présente plusieurs aperçus de documents et de tableaux, notamment des supports liés aux produits et au suivi d'activité ; leur contenu détaillé n'est pas suffisamment lisible pour confirmer toutes les catégories annoncées. Une **page distincte, lisible**, d'un document de spécifications du service qualité de Pharma 5 concerne le **salicylamide**. Elle identifie les rôles de client, fournisseur et fabricant ainsi que des champs de contact. Deux images représentent cette même page, dont une version partiellement masquée ; elles ne constituent pas deux documents indépendants. Le document indique « page 1/5 » ; les quatre autres pages et les fichiers sources n'ont pas été fournis.

  **Assumption :** La structure du document, les références à Pharma 5, au salicylamide et aux rôles de la chaîne d'approvisionnement renforcent le lien documentaire avec l'organisation. Les autres aperçus suggèrent une diversité documentaire, sans permettre de vérifier le contenu des fichiers sous-jacents ni les volumes revendiqués.

  **Unknown :** la date et le vecteur d'accès, les systèmes concernés, l'authenticité indépendante du document, la méthode d'acquisition, le volume effectivement obtenu ou publié, le nombre de personnes touchées, le chiffrement, l'éventuelle interruption d'activité, une confirmation de Pharma 5 ou d'une autorité, toute négociation, tout paiement et toute revente restent inconnus.

- **Périmètre de l'analyse :** quatre images locales examinées en lecture seule : deux versions de la même publication avec galerie d'aperçus, et deux versions de la même page documentaire. Les vignettes ne sont pas assimilées à des fichiers complets analysés. Analyse limitée aux données visibles ; ni le document source complet ni le jeu de données revendiqué n'étaient disponibles. Les noms et coordonnées individuels ne sont pas reproduits.

- **Évaluation des risques :** si les autres données revendiquées ont effectivement été exposées, des informations personnelles et professionnelles pourraient faciliter le spear-phishing, la fraude au paiement ou BEC, l'ingénierie sociale et le ciblage de partenaires de la chaîne d'approvisionnement. Le niveau d'impact repose sur la sensibilité du contexte pharmaceutique et des champs de contact visibles, sans valider l'étendue de la fuite.

- **Sources / Éléments de preuve :** publication INC Ransom et images d'échantillon fournies localement ; examen visuel et manifeste SHA-256 conservé hors dépôt sous `/tmp/afrintel-evidence/AFR-2026-TBD-pharma5/` ; [document public Pharma 5](https://www.pharma5.ma/wp-content/uploads/presse/communique/CP-PHARMA5-VF-17-NOVEMBRE-2020.pdf) pour la correspondance du domaine avec l'organisation. Aucune donnée personnelle brute ni adresse du site criminel n'est publiée.

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

## Remarque de suivi intermensuel

Cette remarque ne constitue pas une nouvelle fiche ni un nouvel incident comptabilisé en septembre.

La [fiche du Ministry of Education of Libya de juin 2026](../../06-june/victims_FR.md) documente une publication attribuée à **EvaN47**, avec un volume revendiqué de **287 Go**. Un échantillon visuel avait alors été examiné : galerie de documents, certificats de fin d'études, documents scolaires et administratifs, images scannées et fichiers PDF, avec des références à des numéros nationaux, des photographies personnelles et des images de passeports. L'analyse portait sur les éléments visibles ; le volume total revendiqué et l'exhaustivité de la base n'étaient pas validés.

La publication du **10 septembre 2026**, attribuée à **EveN47**, revendique ensuite **800 Go** pour la base de moe.gov.ly et environ **300 Go** de données similaires couvrant plusieurs ministères libyens de l'Éducation. Un échantillon local fourni comme provenant de cette publication a toutefois été analysé en lecture seule : **900 976 395 octets** (environ **901 Mo**), **3 900 fichiers** répartis en quatre répertoires correspondant aux passeports (**1 145** fichiers), numéros nationaux (**467**), photos d'étudiants (**1 146**) et certificats d'étudiants (**1 142**). Les signatures indiquent 3 500 JPEG et 4 PNG valides ; cinq fichiers portant l'extension `.jpg` sont en réalité des PDF et deux autres des documents HTML. L'empreinte SHA-256 arborescente agrégée est `d63371c3d61dd48c87398578d1bdfe4329c7dca1bc73104125e966221591df80`. Le contrôle SHA-256 a relevé **169 groupes de doublons** représentant **213 fichiers excédentaires**, ce qui ne permet pas de déduire un nombre de personnes ou de documents uniques. Aucun OCR massif ni recopie de contenu individuel n'a été réalisé afin de limiter l'exposition des données personnelles ; l'analyse porte sur l'arborescence, les signatures, les métadonnées techniques et les contrôles d'intégrité. Cette structure renforce la corroboration interne de la nature documentaire et éducative du jeu de données, sans valider les revendications de 287 Go, 800 Go ou 300 Go. Aucun lien de téléchargement n'a été ouvert et aucune donnée personnelle brute n'est reproduite ici. Il n'est pas établi s'il s'agit d'une extension, d'une republication, d'un volume révisé ou d'une revendication par un alias différent. Les chiffres de 287 Go, 800 Go et 300 Go ne doivent pas être additionnés ; ils restent des revendications datées et distinctes.
