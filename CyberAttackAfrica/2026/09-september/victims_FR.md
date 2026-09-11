![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en septembre 2026 (1 fiche)

👉🏾 [**English version available here**](./victims.md)

## Septembre 2026

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

## Remarque de suivi intermensuel

Cette remarque ne constitue pas une nouvelle fiche ni un nouvel incident comptabilisé en septembre.

La [fiche du Ministry of Education of Libya de juin 2026](../../06-june/victims_FR.md) documente une publication attribuée à **EvaN47**, avec un volume revendiqué de **287 Go**. Un échantillon visuel avait alors été examiné : galerie de documents, certificats de fin d'études, documents scolaires et administratifs, images scannées et fichiers PDF, avec des références à des numéros nationaux, des photographies personnelles et des images de passeports. L'analyse portait sur les éléments visibles ; le volume total revendiqué et l'exhaustivité de la base n'étaient pas validés.

La publication du **10 septembre 2026**, attribuée à **EveN47**, revendique ensuite **800 Go** pour la base de moe.gov.ly et environ **300 Go** de données similaires couvrant plusieurs ministères libyens de l'Éducation. Un échantillon local fourni comme provenant de cette publication a toutefois été analysé en lecture seule : **900 976 395 octets** (environ **901 Mo**), **3 900 fichiers** répartis en quatre répertoires correspondant aux passeports (**1 145** fichiers), numéros nationaux (**467**), photos d'étudiants (**1 146**) et certificats d'étudiants (**1 142**). Les signatures indiquent 3 500 JPEG et 4 PNG valides ; cinq fichiers portant l'extension `.jpg` sont en réalité des PDF et deux autres des documents HTML. L'empreinte SHA-256 arborescente agrégée est `d63371c3d61dd48c87398578d1bdfe4329c7dca1bc73104125e966221591df80`. Le contrôle SHA-256 a relevé **169 groupes de doublons** représentant **213 fichiers excédentaires**, ce qui ne permet pas de déduire un nombre de personnes ou de documents uniques. Aucun OCR massif ni recopie de contenu individuel n'a été réalisé afin de limiter l'exposition des données personnelles ; l'analyse porte sur l'arborescence, les signatures, les métadonnées techniques et les contrôles d'intégrité. Cette structure renforce la corroboration interne de la nature documentaire et éducative du jeu de données, sans valider les revendications de 287 Go, 800 Go ou 300 Go. Aucun lien de téléchargement n'a été ouvert et aucune donnée personnelle brute n'est reproduite ici. Il n'est pas établi s'il s'agit d'une extension, d'une republication, d'un volume révisé ou d'une revendication par un alias différent. Les chiffres de 287 Go, 800 Go et 300 Go ne doivent pas être additionnés ; ils restent des revendications datées et distinctes.
