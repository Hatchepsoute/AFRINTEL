![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en septembre 2026 (3 fiches)

👉🏾 [**English version available here**](./victims.md)

## Septembre 2026

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

## Remarque de suivi intermensuel

Cette remarque ne constitue pas une nouvelle fiche ni un nouvel incident comptabilisé en septembre.

La [fiche du Ministry of Education of Libya de juin 2026](../../06-june/victims_FR.md) documente une publication attribuée à **EvaN47**, avec un volume revendiqué de **287 Go**. Un échantillon visuel avait alors été examiné : galerie de documents, certificats de fin d'études, documents scolaires et administratifs, images scannées et fichiers PDF, avec des références à des numéros nationaux, des photographies personnelles et des images de passeports. L'analyse portait sur les éléments visibles ; le volume total revendiqué et l'exhaustivité de la base n'étaient pas validés.

La publication du **10 septembre 2026**, attribuée à **EveN47**, revendique ensuite **800 Go** pour la base de moe.gov.ly et environ **300 Go** de données similaires couvrant plusieurs ministères libyens de l'Éducation. Un échantillon local fourni comme provenant de cette publication a toutefois été analysé en lecture seule : **900 976 395 octets** (environ **901 Mo**), **3 900 fichiers** répartis en quatre répertoires correspondant aux passeports (**1 145** fichiers), numéros nationaux (**467**), photos d'étudiants (**1 146**) et certificats d'étudiants (**1 142**). Les signatures indiquent 3 500 JPEG et 4 PNG valides ; cinq fichiers portant l'extension `.jpg` sont en réalité des PDF et deux autres des documents HTML. L'empreinte SHA-256 arborescente agrégée est `d63371c3d61dd48c87398578d1bdfe4329c7dca1bc73104125e966221591df80`. Le contrôle SHA-256 a relevé **169 groupes de doublons** représentant **213 fichiers excédentaires**, ce qui ne permet pas de déduire un nombre de personnes ou de documents uniques. Aucun OCR massif ni recopie de contenu individuel n'a été réalisé afin de limiter l'exposition des données personnelles ; l'analyse porte sur l'arborescence, les signatures, les métadonnées techniques et les contrôles d'intégrité. Cette structure renforce la corroboration interne de la nature documentaire et éducative du jeu de données, sans valider les revendications de 287 Go, 800 Go ou 300 Go. Aucun lien de téléchargement n'a été ouvert et aucune donnée personnelle brute n'est reproduite ici. Il n'est pas établi s'il s'agit d'une extension, d'une republication, d'un volume révisé ou d'une revendication par un alias différent. Les chiffres de 287 Go, 800 Go et 300 Go ne doivent pas être additionnés ; ils restent des revendications datées et distinctes.
