[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Période](https://img.shields.io/badge/Période-Juillet%202026-lightgrey)
![Incidents](https://img.shields.io/badge/Incidents-42-critical)
![Ransomware](https://img.shields.io/badge/Ransomware-18-red)
![Fuites](https://img.shields.io/badge/Fuites%20de%20données-18-orange)
![Ventes d'accès](https://img.shields.io/badge/Ventes%20d'accès-6-yellow)
![Pays](https://img.shields.io/badge/Pays-12-blueviolet)
![CTI](https://img.shields.io/badge/Type-Rapport%20CTI-purple)

# AFRINTEL - Rapport CTI mensuel
## Cyberattaques en Afrique - juillet 2026

👉🏾 [Version anglaise](./README.md) · [Fiches victimes](./victims_FR.md)

## 1. Synthèse exécutive

AFRINTEL a recensé **42 fiches d’incidents liés à l’Afrique** en juillet 2026, concernant **12 pays** :

- **18 revendications ransomware** ;
- **18 fuites de données** ;
- **6 offres de vente d’accès** ;
- **0 défacement**.

L’Égypte et la Tunisie arrivent en tête avec sept occurrences géographiques chacune, devant le Maroc et l’Afrique du Sud avec six. Le gouvernement et l’administration constituent le premier ensemble sectoriel avec 11 fiches. Aucun acteur ne domine : arcusmedia totalise quatre publications ransomware et dragonforce trois.

La solidité des preuves varie fortement : **21 fiches relèvent de revendications non vérifiées**, **20 comportent un échantillon publié** et **1 correspond à des données entièrement publiées**. Neuf fiches atteignent le niveau d’impact 4. Les cas à la fois sensibles et les mieux étayés comprennent Nerasolgh, Tayara.tn et Distamed, pour lesquels AFRINTEL a examiné des éléments structurés ; les volumes complets annoncés et les vecteurs d’intrusion ne sont pas nécessairement établis.

Les priorités défensives sont la protection des comptes privilégiés et des messageries, la détection des exports massifs de bases et la prise en charge rapide des expositions de données d’identité, de santé, d’éducation et d’administration. Les fiches complètes sont disponibles dans [`victims_FR.md`](./victims_FR.md).

## 2. Périmètre et méthode

Tous les chiffres sont dérivés de [`victims.md`](./victims.md), source unique de vérité du mois. Les fiches françaises constituent une traduction et ne font pas l’objet d’un recomptage séparé.

- **Périmètre géographique :** les 54 pays africains ; seules les victimes, opérations ou données ayant un lien africain explicite sont incluses.
- **Période de collecte :** du 1er au 31 juillet 2026, selon la date de détection AFRINTEL inscrite dans chaque fiche.
- **Sources :** sites de fuite ransomware, forums cybercriminels, OSINT public, captures et échantillons structurés examinés localement.
- **Inclusion :** une fiche par revendication ou incident documenté ; les revendications répétées restent distinctes uniquement si l’acteur, la date ou les preuves diffèrent.
- **Classification :** Ransomware, Data Leak, Access Sale et Defacement restent des types distincts.

La ventilation géographique totalise **43 occurrences** au lieu de 42 : une fiche concernant des photographies de pièces d’identité associe le Nigeria et la Côte d’Ivoire et est donc comptée dans les deux pays. La fiche MTN est attribuée à l'Afrique du Sud sous réserve ; l'entité nationale n'est pas confirmée de manière indépendante.

Les volumes annoncés par les acteurs ne sont pas repris comme des faits établis. Les liens de téléchargement, les identifiants, les données personnelles et les secrets ne sont pas reproduits dans ce rapport.

### Profil des preuves

| Dimension | Répartition | Total |
| :--- | :--- | ---: |
| Statut | 21 Claim - Unverified ; 20 Claim - Data Sample Published ; 1 Data Fully Published | 42 |
| Confiance | 22 Faible ; 8 Moyen ; 9 Élevé ; 3 Très élevé | 42 |
| Impact | 12 Niveau 2 ; 21 Niveau 3 ; 9 Niveau 4 | 42 |

## 3. Vue globale

| Pays | Occurrences | Barre |
| :--- | ---: | :--- |
| 🇪🇬 Égypte | 7 | ███████ |
| 🇹🇳 Tunisie | 7 | ███████ |
| 🇲🇦 Maroc | 6 | ██████ |
| 🇿🇦 Afrique du Sud | 6 | ██████ |
| 🇳🇬 Nigeria | 4 | ████ |
| 🇩🇿 Algérie | 4 | ████ |
| 🇨🇮 Côte d’Ivoire | 3 | ███ |
| 🇬🇭 Ghana | 2 | ██ |
| 🇧🇼 Botswana | 1 | █ |
| 🇨🇲 Cameroun | 1 | █ |
| 🇰🇪 Kenya | 1 | █ |
| 🇸🇸 Soudan du Sud | 1 | █ |
| **Total géographique** | **43** | - |

```mermaid
pie showData
    title Occurrences géographiques - juillet 2026
    "Égypte" : 7
    "Tunisie" : 7
    "Maroc" : 6
    "Afrique du Sud" : 6
    "Nigeria" : 4
    "Algérie" : 4
    "Côte d’Ivoire" : 3
    "Ghana" : 2
    "Botswana" : 1
    "Cameroun" : 1
    "Kenya" : 1
    "Soudan du Sud" : 1
```


```mermaid
xychart-beta
    title "Occurrences géographiques par pays - juillet 2026"
    x-axis ["EG","TN","MA","ZA","NG","DZ","CI","GH","BW","CM","KE","SS"]
    y-axis "Occurrences" 0 --> 8
    bar [7,7,6,6,4,4,3,2,1,1,1,1]
```

Légende : EG = Égypte, TN = Tunisie, MA = Maroc, ZA = Afrique du Sud, NG = Nigeria, DZ = Algérie, CI = Côte d’Ivoire, GH = Ghana, BW = Botswana, CM = Cameroun, KE = Kenya, SS = Soudan du Sud


### Comparaison ransomware et fuites de données par pays

| Pays | Ransomware | Fuites de données / ventes d'accès | Total | Répartition |
|---|---:|---:|---:|---|
| 🇿🇦 Afrique du Sud | 5 | 1 | 6 | 🟧🟧🟧🟧🟧 🟦 |
| 🇪🇬 Égypte | 2 | 5 | 7 | 🟧🟧 🟦🟦🟦🟦🟦 |
| 🇲🇦 Maroc | 2 | 4 | 6 | 🟧🟧 🟦🟦🟦🟦 |
| 🇳🇬 Nigeria | 2 | 2 | 4 | 🟧🟧 🟦🟦 |
| 🇨🇮 Côte d'Ivoire | 2 | 1 | 3 | 🟧🟧 🟦 |
| 🇬🇭 Ghana | 1 | 1 | 2 | 🟧 🟦 |
| 🇨🇲 Cameroun | 1 | 0 | 1 | 🟧 |
| 🇧🇼 Botswana | 1 | 0 | 1 | 🟧 |
| 🇰🇪 Kenya | 1 | 0 | 1 | 🟧 |
| 🇸🇸 Soudan du Sud | 1 | 0 | 1 | 🟧 |
| 🇹🇳 Tunisie | 0 | 7 | 7 | 🟦🟦🟦🟦🟦🟦🟦 |
| 🇩🇿 Algérie | 0 | 4 | 4 | 🟦🟦🟦🟦 |
| **Total** | **18** | **25** | **43** | *🟧 Ransomware \| 🟦 Fuites et ventes d'accès* |

Les 25 occurrences de fuites et de ventes d'accès incluent l'allocation géographique supplémentaire de la fiche relative aux documents d'identité du Nigeria et de la Côte d'Ivoire.

### Ransomware par pays


```mermaid
xychart-beta
    title "Ransomware par pays - juillet 2026"
    x-axis ["ZA","EG","MA","NG","CI","GH","CM","BW","KE","SS"]
    y-axis "Ransomware" 0 --> 6
    bar [5,2,2,2,2,1,1,1,1,1]
```

Légende : ZA = Afrique du Sud, EG = Égypte, MA = Maroc, NG = Nigeria, CI = Côte d’Ivoire, GH = Ghana, CM = Cameroun, BW = Botswana, KE = Kenya, SS = Soudan du Sud


### Répartition géographique des fuites de données et ventes d'accès

| Rang | Pays | Occurrences | Barre |
|---:|---|---:|---|
| 1 | 🇹🇳 Tunisie | **7** | ███████ |
| 2 | 🇪🇬 Égypte | **5** | █████ |
| 3 | 🇲🇦 Maroc | **4** | ████ |
| 3 | 🇩🇿 Algérie | **4** | ████ |
| 5 | 🇳🇬 Nigeria | **2** | ██ |
| 6 | 🇿🇦 Afrique du Sud | **1** | █ |
| 6 | 🇨🇮 Côte d'Ivoire | **1** | █ |
| 6 | 🇬🇭 Ghana | **1** | █ |
| **Total** |  | **25** |  |


```mermaid
xychart-beta
    title "Répartition géographique des fuites et ventes d'accès - juillet 2026"
    x-axis ["TN","EG","MA","DZ","NG","ZA","CI","GH"]
    y-axis "Occurrences" 0 --> 8
    bar [7,5,4,4,2,1,1,1]
```

Légende : TN = Tunisie, EG = Égypte, MA = Maroc, DZ = Algérie, NG = Nigeria, ZA = Afrique du Sud, CI = Côte d’Ivoire, GH = Ghana

### Répartition géographique par région

| Région | Pays inclus | Occurrences | Ransomware | Fuites et ventes d'accès | Répartition |
|---|---|---:|---:|---:|---|
| **Afrique du Nord** | 🇪🇬 Égypte, 🇹🇳 Tunisie, 🇲🇦 Maroc, 🇩🇿 Algérie | **24** | 4 | 20 | 🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| **Afrique australe** | 🇿🇦 Afrique du Sud, 🇧🇼 Botswana | **7** | 6 | 1 | 🟧🟧🟧🟧🟧🟧 🟦 |
| **Afrique de l'Ouest et centrale** | 🇳🇬 Nigeria, 🇨🇮 Côte d'Ivoire, 🇬🇭 Ghana, 🇨🇲 Cameroun | **10** | 6 | 4 | 🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦 |
| **Afrique de l'Est** | 🇰🇪 Kenya, 🇸🇸 Soudan du Sud | **2** | 2 | 0 | 🟧🟧 |
| **Total** | **12 pays** | **43** | **18** | **25** | *🟧 Ransomware \| 🟦 Fuites et ventes d'accès* |

La fiche relative aux documents d'identité du Nigeria et de la Côte d'Ivoire ajoute une occurrence dans chacun de ces deux pays. MTN est attribué à l'Afrique du Sud dans cette vue de travail, mais son entité nationale n'est pas confirmée. Ces allocations ne modifient pas le total global de 42 incidents uniques.


```mermaid
xychart-beta
    title "Occurrences géographiques par région - juillet 2026"
    x-axis ["Afrique du Nord","Afrique australe","Afrique de l'Ouest et centrale","Afrique de l'Est"]
    y-axis "Occurrences" 0 --> 26
    bar [24,7,10,2]
```

## 4. Analyse détaillée par type d'incident

| Type | Fiches | Part |
| :--- | ---: | ---: |
| 🟧 Ransomware | 18 | 42,9 % |
| 🟦 Fuite de données | 18 | 42,9 % |
| 🟪 Vente d’accès | 6 | 14,3 % |
| **Total** | **42** | **100 %** |


```mermaid
pie showData
    title Répartition des types d'incidents - juillet 2026
    "Ransomware" : 18
    "Fuites de données" : 18
    "Ventes d'accès" : 6
```

### 4.1 Ransomware

| Indicateur | Résultat |
| :--- | :--- |
| Fiches | 18 |
| Principaux pays | Afrique du Sud 5 ; Égypte, Maroc, Nigeria et Côte d'Ivoire 2 chacun |
| Groupes les plus représentés | arcusmedia 4 ; dragonforce 3 ; krybit 2 ; TheGentlemen 2 |
| Limite des preuves | La plupart des fiches sont des publications de victimes sans preuve indépendante de chiffrement, d’exfiltration ou d’interruption |

Le total ransomware représente des publications de victimes observées et attribuées à des groupes ransomware. Le rapport ne déduit ni chiffrement ni impact opérationnel de la seule présence d’une victime sur un site de groupe.

### 4.2 Fuites de données et ventes d’accès

| Catégorie | Fiches | Occurrences géographiques | Principales observations |
| :--- | ---: | ---: | :--- |
| Fuite de données | 18 | 19 | Données d’identité, médicales, éducatives, administratives et commerciales |
| Vente d’accès | 6 | 6 | Offres concernant des messageries, Fortinet et des systèmes administratifs |
| **Ensemble** | **24** | **25** | Une fiche de fuite couvre le Nigeria et la Côte d’Ivoire |

La Tunisie domine cette vue avec sept occurrences, devant l’Égypte avec cinq, puis le Maroc et l’Algérie avec quatre chacun. Les preuves vont de simples annonces de vente à des exports structurés et des interfaces administratives visibles.

## 5. Secteurs les plus exposés

| Secteur | Fiches | Part | Barre |
| :--- | ---: | ---: | :--- |
| Gouvernement / Administration | 11 | 26,2 % | ███████████ |
| Télécommunications | 4 | 9,5 % | ████ |
| Santé / Médical | 4 | 9,5 % | ████ |
| Ingénierie / Construction | 3 | 7,1 % | ███ |
| Éducation / Université | 3 | 7,1 % | ███ |
| E-commerce / Distribution | 3 | 7,1 % | ███ |
| Pétrole et énergie | 2 | 4,8 % | ██ |
| Portefeuille d’investissement / Énergie | 1 | 2,4 % | █ |
| Finance / Banque | 1 | 2,4 % | █ |
| Transport / Logistique | 1 | 2,4 % | █ |
| Immobilier | 1 | 2,4 % | █ |
| Mines | 1 | 2,4 % | █ |
| Comptabilité / Audit | 1 | 2,4 % | █ |
| Voyage / Événementiel | 1 | 2,4 % | █ |
| Industrie chimique | 1 | 2,4 % | █ |
| Services de sécurité | 1 | 2,4 % | █ |
| Jeux / Divertissement | 1 | 2,4 % | █ |
| Caoutchouc / Agriculture | 1 | 2,4 % | █ |
| Technologie / Informatique | 1 | 2,4 % | █ |
| **Total** | **42** | **100 %** |  |

```mermaid
xychart-beta
    title "Secteurs les plus représentés - juillet 2026"
    x-axis ["Gouv","Tél","Sant","Ing","Éduc","Commerce","Énergie"]
    y-axis "Fiches" 0 --> 12
    bar [11,4,4,3,3,3,2]
```

Légende : Gouv = Gouvernement / Administration ; Tél = Télécommunications ; Ing = Ingénierie / Construction ; Éduc = Éducation / Université ; Commerce = E-commerce / Distribution.

Les administrations restent le premier ensemble sectoriel. Les fiches concernent notamment des systèmes liés aux marchés publics, à la justice, à l’emploi, à l’identité, au foncier et aux services publics. Cette concentration augmente le risque de fraude documentaire, d’usurpation et d’ingénierie sociale ciblée.

## 6. Acteurs et sources les plus présents

| Acteur / Groupe | Type | Fiches | Pays et principales cibles |
| :--- | :--- | ---: | :--- |
| arcusmedia | Groupe ransomware | 4 | Kenya, Nigeria, Afrique du Sud, Maroc ; énergie, bien-être, voyage, ingénierie |
| dragonforce | Groupe ransomware | 3 | Afrique du Sud, Botswana, Égypte ; chimie, ingénierie, divertissement |
| CrowStealer | Acteur de publication | 2 | Égypte ; comptes universitaires et laboratoires médicaux |
| krybit | Groupe ransomware | 2 | Côte d'Ivoire, Soudan du Sud ; santé et énergie |
| BIGBROTHER | Compte de republication / vente d’accès | 2 | Tunisie ; logistique et administration publique |
| TheGentlemen | Groupe ransomware | 2 | Égypte, Côte d'Ivoire ; immobilier et agriculture |
| Phantom Atlas | Acteur de publication | 2 | Algérie ; université et télécommunications |
| GreYyM3terr | Vendeur d’accès | 2 | Tunisie ; messageries de télécommunications |


```mermaid
xychart-beta
    title "Acteurs et sources les plus présents - juillet 2026"
    x-axis ["arcusmedia","dragonforce","CrowStealer","krybit","BIGBROTHER","TheGentlemen","Phantom Atlas","GreYyM3terr"]
    y-axis "Fiches" 0 --> 5
    bar [4,3,2,2,2,2,2,2]
```

Vingt-trois autres acteurs ou comptes sources nommés apparaissent une fois chacun. Ils ne sont pas agrégés dans le graphique, car une barre résiduelle masquerait le classement comparatif. La fréquence d’un nom ne suffit pas à établir une campagne coordonnée.

### 6.1 Évaluation du risque par pays

Il s’agit d’une **évaluation relative de l’exposition observée en juillet**, et non d’une notation générale du risque cyber national. Elle combine le volume, la solidité des preuves, l’impact et la sensibilité sectorielle.

| Risque | Pays | Justification fondée sur les fiches |
| :--- | :--- | :--- |
| 🔴 Élevé | 🇪🇬 Égypte, 🇹🇳 Tunisie, 🇲🇦 Maroc, 🇿🇦 Afrique du Sud, 🇬🇭 Ghana | Au moins cinq fiches, ou une exposition Niveau 4 à confiance Très élevée |
| 🟠 Moyen | 🇳🇬 Nigeria, 🇩🇿 Algérie, 🇨🇮 Côte d'Ivoire, 🇸🇸 Soudan du Sud | Plusieurs fiches ou un cas Niveau 4 significatif, avec des limites de preuve importantes |
| 🟡 Faible à moyen | 🇧🇼 Botswana, 🇨🇲 Cameroun, 🇰🇪 Kenya | Une publication ransomware à faible confiance par pays |

### 6.2 Dossiers à surveiller

### Ministère égyptien de l’Agriculture

Les éléments examinés comprennent des correspondances, contrats, paiements, inspections, inventaires techniques et captures d’application. L’ensemble est cohérent avec une exposition de documents administratifs et opérationnels. Si l’authenticité est confirmée, les risques incluent la fraude foncière, la falsification documentaire et le phishing contextualisé.

### Nerasolgh - Ghana

Les exports examinés présentent des structures liées aux clients, au personnel, aux paiements USSD, aux transactions et à certains champs bancaires. L’acteur revendique 26 millions d’enregistrements, mais le volume effectivement examiné est beaucoup plus limité. L’écart entre la revendication et l’échantillon demeure une inconnue importante.

### Heliopolis University et HIMS

Ces deux dossiers doivent rester distincts. L’échantillon d’Heliopolis montre des structures de comptes parents et étudiants. La publication HIMS revendique des données concernant les étudiants, le personnel, la finance et les paiements. Les volumes annoncés n’ont pas été confirmés indépendamment.

### Adex - Tunisie

La republication attribuée à BIGBROTHER montre une interface administrative dont le nombre d’enregistrements est proche du volume annoncé. Cela rend l’accès allégué plausible, sans établir l’identité de l’intrus initial ni l’étendue des données.

### 6.3 Revendications multiples et hypothèses

### Planet Sport

Le domaine `planetsport.ma` avait été listé par LockBit 5 en avril 2026. Une publication gratuite attribuée à Mozvo est apparue en juillet. Une republication, une redistribution par un tiers ou un lien avec un affilié sont possibles, mais aucune de ces hypothèses n’est démontrée. Les deux fiches restent donc séparées et liées par une note analytique.

### Zenith Bank

Zenith Bank Plc a été mentionnée dans une revendication de fuite de données publiée le 9 août 2025 par KaruHunters, qui alléguait la mise en vente de plus de 1,8 million de dossiers de clients et d’employés. En juillet 2026, Zenith Bank est réapparue dans une revendication ransomware attribuée à ExfilSquad. Les deux publications sont séparées de près de onze mois et impliquent des acteurs différents. Cette répétition justifie une surveillance renforcée, mais les éléments disponibles ne permettent pas d’établir que les deux publications proviennent de la même compromission.

## 7. Tendances et lacunes de renseignement

### Tendances

- Les ransomware et les fuites de données représentent chacun 18 fiches.
- Six offres concernent des environnements publics, télécoms ou administratifs.
- Des documents d'identité et des éléments liés aux passeports apparaissent dans plusieurs fiches.
- Le gouvernement et l'administration restent le principal groupe sectoriel.
- Planet Sport et Adex illustrent les difficultés d'attribution liées aux republications.
- La qualité des preuves varie des exports structurés aux simples revendications.

### Lacunes de renseignement

- La confirmation par les victimes est généralement absente.
- Le volume complet des données est inconnu dans plusieurs cas.
- Le vecteur d'intrusion initial est rarement visible.
- Les filiales nationales ne sont pas toujours identifiables, notamment pour MTN.
- Une nouvelle compromission et une republication sont parfois difficiles à distinguer.
- La remédiation après publication reste inconnue.

Les niveaux de confiance sont donc évalués fiche par fiche. Le rapport ne transforme pas une revendication en incident confirmé.

## 8. Correspondances MITRE ATT&CK contextuelles

Aucune technique ATT&CK n’est présentée comme directement observée dans une télémétrie endpoint ou réseau. Seules deux hypothèses défensives, étroites et explicitement limitées, sont conservées.

| Phase | ID | Technique | Fiches associées | Limite des preuves |
| :--- | :--- | :--- | :--- | :--- |
| Accès initial / Persistance | T1078 | Valid Accounts | Ventes d’accès webmail TOPNET et Orange Tunisie | Des interfaces de messagerie authentifiées sont visibles, mais le mode d’authentification et l’origine des identifiants restent inconnus. |
| Collecte | T1213 | Data from Information Repositories | Nerasolgh, Université de Chlef, ministère égyptien de l’Agriculture, Distamed | Des contenus structurés issus de référentiels ont été examinés ; les commandes de collecte et le chemin d’intrusion n’ont pas été observés. |

`T1190`, `T1003`, `T1041` et `T1486` ne sont pas retenues pour juillet, car le corpus ne démontre ni exploitation d’une application exposée, ni credential dumping, ni canal C2 d’exfiltration, ni chiffrement ransomware.

## 9. Recommandations

- **Administrations :** imposer une MFA résistante au phishing, auditer les services exposés et surveiller les comptes privilégiés.
- **Télécommunications :** examiner les journaux des accès administrateurs, VPN et messageries, puis renouveler les identifiants exposés.
- **Universités et santé :** segmenter les bases sensibles, limiter les exports massifs et vérifier les comptes de service.
- **Banques et e-commerce :** surveiller les authentifications anormales, les paiements et la récupération de comptes.
- **Toutes les organisations :** préserver les preuves et valider les indicateurs sans redistribuer de données personnelles.

## 10. Recommandations tactiques SOC

| Priorité | Objectif de détection | Télémétrie et corrélation |
| :--- | :--- | :--- |
| Couverture T1078 | Détecter l’usage anormal de comptes valides ou détournés | Journaux IAM, webmail, VPN et SSO ; voyage impossible, nouvel appareil, ASN inhabituel, réinitialisation MFA, création de jeton de session et connexion privilégiée hors profil |
| Couverture T1213 | Détecter les accès inhabituels aux référentiels et la collecte massive | Audit des bases, journaux applicatifs, accès fichiers et DLP ; requêtes volumineuses, lecture de tables complètes, exports massifs, création d’archives et accès hors rôle ou horaire habituel |
| Modification privilégiée | Détecter une préparation de persistance ou d’accès latéral | IAM, Active Directory, Microsoft 365 et EDR ; nouvel administrateur, attribution de rôle, transfert de messagerie, nouveau consentement OAuth et session distante inattendue |
| Réponse à l’exposition | Contenir une divulgation plausible ou confirmée de données sensibles | Révoquer sessions et clés exposées, préserver les preuves, déterminer les jeux affectés, notifier les équipes juridiques et de réponse, surveiller la fraude ciblée |

Maintenir des procédures de triage et de réponse distinctes pour les publications ransomware, les fuites, les ventes d’accès et les republications. Ne pas traiter une publication de victime comme une preuve de chiffrement.

## 11. Recommandations stratégiques

- Mettre en place des canaux régionaux de partage sur les ransomware et les courtiers d'accès.
- Imposer des évaluations des services exposés et des fournisseurs tiers pour les organisations publiques et critiques.
- Maintenir des procédures distinctes pour les ransomware, les fuites, les ventes d'accès et les republications.
- Améliorer les inventaires afin d'identifier rapidement les filiales nationales.
- Organiser des exercices sur l'exposition de données d'identité, les accès privilégiés et la divulgation publique.

## 12. Conclusion

Juillet 2026 présente une menace fragmentée mais large. Le ransomware reste très visible, tandis que les fuites et les ventes d’accès exposent des données d’identité, de santé, d’éducation, d’administration et de paiement. La qualité des preuves varie fortement d’une fiche à l’autre ; cette différence doit rester visible dans toute décision opérationnelle.

### Contrôles de cohérence

- Types : 18 ransomware + 18 fuites de données + 6 ventes d’accès + 0 défacement = 42.
- Statuts : 21 revendications non vérifiées + 20 revendications avec échantillon + 1 jeu entièrement publié = 42.
- Confiance : 22 Faible + 8 Moyen + 9 Élevé + 3 Très élevé = 42.
- Impact : 12 Niveau 2 + 21 Niveau 3 + 9 Niveau 4 = 42.
- Géographie : 42 fiches uniques ; 43 occurrences pays, car une fiche couvre le Nigeria et la Côte d’Ivoire.
- Secteurs : les 19 lignes sectorielles explicites totalisent 42.

**AFRINTEL - Adama ASSIONGBON, Consultant SOC & CTI**
[Repository GitHub](https://github.com/Hatchepsoute/AFRINTEL)
