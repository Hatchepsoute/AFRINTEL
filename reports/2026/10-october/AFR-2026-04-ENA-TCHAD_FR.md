# Rapport CTI — AFR-2026-04-ENA-TCHAD

## Synthèse exécutive

AFRINTEL a identifié et documenté en octobre 2026 une publication attribuée au compte `NormalLeVrai`, présentant l'École nationale d'administration du Tchad (ENA Tchad) comme victime et annonçant une base d'e-mails. La publication observée est datée du 29 avril 2026 à 22:55. L'incident est donc rattaché à avril 2026 ; sa découverte et son signalement par AFRINTEL interviennent en octobre 2026.

L'analyse locale du corpus fourni a porté sur l'intégralité des 1 934 fichiers accessibles, représentant 213 937 991 octets. Le corpus contient notamment 1 109 messages, 118 fichiers de type PDF ou extension PDF atypique, 5 651 pages, 4 DOCX, 4 DOC, 85 images et 2 archives ZIP. Ces éléments établissent l'existence d'un corpus cohérent associé à l'organisation revendiquée, mais ne démontrent pas à eux seuls la méthode d'acquisition, l'exhaustivité de la compromission ni une confirmation officielle par la victime.

**Qualification AFRINTEL :** Data Leak · Claim - Data Sample Published · confiance élevée pour l'attribution du corpus fourni, moyenne pour l'étendue de la compromission · impact Level 3.

## 1. Chronologie et périmètre

| Élément | Valeur | Statut |
|---|---|---|
| Incident / publication observée | 29 avril 2026, 22:55 | Observed |
| Période des messages | 21 novembre 2025 — 25 avril 2026 | Observed |
| Découverte et rapport AFRINTEL | Octobre 2026, rapporté le 23 octobre 2026 | Observed |
| Victime revendiquée | École nationale d'administration du Tchad (ENA Tchad) | Observed |
| Pays | Tchad | Observed |
| Domaine organisationnel observé | `ena.td` | Observed |
| Acteur / compte de publication | `NormalLeVrai` | Observed, attribution au compte uniquement |

Le classement d'incident reste **avril 2026**. Le présent rapport est publié dans le paquet d'octobre pour conserver la traçabilité de la découverte tardive, sans modifier les rapports et statistiques d'avril déjà clôturés.

## 2. Preuves conservées

Les preuves originales et les sorties détaillées restent dans un espace local restreint et ne sont pas intégrées au dépôt public. Les identifiants ci-dessous permettent de relier le rapport aux éléments conservés sans publier de données personnelles.

| ID | Élément | Résultat / empreinte SHA-256 | Rôle probatoire |
|---|---|---|---|
| E1 | Capture de la publication de l'acteur | `b4f14cdeb57770465ef86f82627fe75de9a071bb5eca6e1050efbc25b73aa88f` | Date, titre, victime revendiquée et compte de publication |
| E2 | Export JSON des messages | `cc5625a58a621753fe4fb44b714a823521c89f50c3888734b2aecfc8d863b2ca` | Structure et contenu agrégé de 1 109 messages |
| E3 | Export CSV des messages | `8163b813fd5748ee68afe1c6097742f429a38ef3010a570a22b5c46ebe65264d` | Représentation tabulaire concordante |
| E4 | Corpus de fichiers et pièces jointes | Inventaire local de 1 934 fichiers / 213 937 991 octets | Nature, volume et cohérence du corpus fourni |
| E5 | Rapport d'analyse agrégé | `c68ad8062752c4c5da46a7296153e7d73fb292caf327409dc5c2fa04eef6fa02` | Reproductibilité des comptages et contrôles |

La capture E1 est une preuve de publication et de revendication ; elle ne constitue pas une confirmation officielle de l'ENA Tchad. Les exports E2 à E4 sont des artefacts fournis pour analyse et ne prouvent pas, à eux seuls, leur mode d'obtention.

## 3. Analyse du corpus

### 3.1 Structure et couverture

- 1 109 messages analysés ; 87 expéditeurs distincts.
- Dossiers observés : INBOX 439, Trash 649, Sent 18, Drafts 3.
- 131 références de pièces jointes dans les messages, correspondant à 75 noms distincts.
- 65 groupes de messages présentant un même condensat de corps et de sujet.
- 155 groupes de doublons exacts couvrant 487 fichiers ; ces duplications sont cohérentes avec des copies de pièces jointes dans plusieurs dossiers, mais ne doivent pas être additionnées comme des documents uniques.
- Destinataires principalement rattachés à `ena.td`, avec également des domaines de messagerie externes observés. Les valeurs individuelles ne sont pas reproduites.

### 3.2 Documents effectivement observés

- 118 fichiers PDF ou extensions assimilées, totalisant 5 651 pages ; 116 contiennent une couche texte exploitable et 2 sont des PDF image-only.
- 5 fichiers portant une extension atypique ont été vérifiés comme des PDF valides et intégrés au décompte PDF.
- 4 DOCX ont été inspectés par extraction XML locale, sans activation de macros ou de contenu incorporé.
- 4 DOC hérités ont fait l'objet d'une extraction prudente des chaînes lisibles ; leur conversion structurée complète n'est pas garantie.
- 85 images ont été traitées par OCR local ; 63 ont produit du texte non vide.
- 2 archives ZIP identiques ont été inspectées sans exécution ; chacune contient un PDF unique nommé `RedefiningCapitalism.pdf`.

Le contenu observé relève principalement de correspondances administratives, de formation et de scolarité, d'échanges professionnels, de documents d'événements et de pièces jointes associées. Des références à des identités, coordonnées, comptes, documents administratifs et alertes de sécurité sont présentes dans le corpus ; les valeurs brutes ne sont pas reproduites ici.

### 3.3 Sensibilité et impacts possibles

Les catégories observées peuvent faciliter :

- l'hameçonnage ciblé et l'usurpation de correspondants ;
- la fraude documentaire ou administrative ;
- l'ingénierie sociale visant le personnel, les étudiants et les partenaires ;
- la réutilisation de métadonnées pour des prises de contrôle de comptes.

Aucun mot de passe, jeton ou secret n'est publié dans ce rapport. L'analyse n'établit pas que les identifiants observés sont encore valides, ni qu'un accès actif a été obtenu à partir du corpus.

## 4. Évaluation analytique

### Observed

- Une publication publique associe le compte `NormalLeVrai` à une revendication visant l'ENA Tchad.
- Un corpus local cohérent contient des messages et documents rattachables au domaine `ena.td`.
- Les volumes et catégories ci-dessus ont été calculés sur l'ensemble des fichiers accessibles.

### Assumptions / inferences

- Le corpus est probablement une exportation ou une collecte de messagerie, au vu de sa structure, de ses dossiers et des copies de pièces jointes.
- L'association organisationnelle est fortement étayée par les domaines et le contenu institutionnel observés.

### Unknown

- Méthode d'accès initial et identité de l'opérateur technique.
- Exhaustivité par rapport à l'environnement réel de l'ENA Tchad.
- Exfiltration, accès persistant, réutilisation ou vente des données.
- Confirmation officielle, notification réglementaire et impact opérationnel exact.

## 5. Méthode et chaîne de traitement

L'examen a été réalisé localement, en lecture seule, avec empreintes SHA-256, inventaire des fichiers, extraction de texte PDF/DOCX/HTML/TXT/JSON, inspection des archives et OCR des images. Aucun binaire, script, macro, lien incorporé, URL signée ou jeton n'a été exécuté ou suivi. Les résultats publiés sont agrégés et minimisés.

La couverture est complète pour l'inventaire et les empreintes du corpus fourni. La lecture sémantique exhaustive de chaque page et de chaque image n'est pas revendiquée ; les fichiers DOC hérités et les PDF image-only comportent les limites précisées ci-dessus. Le rapport détaillé local est conservé sous la référence `afrintel-evidence-ena-analysis.json`.

## 6. Recommandations défensives

1. Préserver les journaux de messagerie, d'authentification, de transfert et d'administration sur la période novembre 2025 — avril 2026.
2. Réinitialiser les secrets potentiellement exposés après validation du périmètre et imposer la MFA sur les comptes sensibles.
3. Rechercher les règles de transfert, délégations, sessions et applications OAuth inconnues.
4. Mettre en place une surveillance ciblée contre l'usurpation de domaines et les campagnes de phishing contextualisées.
5. Classifier les documents exposés, notifier les parties compétentes selon le cadre applicable et documenter les mesures de remédiation.

## 7. Données structurées OpenCTI

| Champ | Valeur |
|---|---|
| Incident ID | `AFR-2026-04-ENA-TCHAD` |
| Incident type | `Data Leak` |
| Victime | École nationale d'administration du Tchad |
| Pays | Tchad |
| Domaine | `ena.td` |
| Acteur | `NormalLeVrai` (compte de publication) |
| Incident date | `2026-04-29` |
| AFRINTEL reporting date | `2026-10-23` |
| Status | `Claim - Data Sample Published` |
| Confidence | `High` pour l'attribution du corpus ; `Medium` pour l'étendue de la compromission |
| Impact | `Level 3` |

Ce rapport ne transforme pas la revendication en confirmation officielle et ne modifie pas les statistiques historiques d'avril.
