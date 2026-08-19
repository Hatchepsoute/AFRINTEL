[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Type de menace](https://img.shields.io/badge/Menace-Ransomware%20%26%20Fuite-red)
![Période](https://img.shields.io/badge/Période-Août%202026-lightgrey)
![Type de renseignement](https://img.shields.io/badge/Renseignement-CTI-purple)

# Rapport CTI — Cyberattaques en Afrique (août 2026)

👉🏾 [**English version available here**](./README.md)

## 1. Résumé exécutif

AFRINTEL a recensé **6 incidents** concernant des entités africaines en août 2026 : **1 publication ransomware**, **4 fuites de données** et **1 vente d'accès**. Le Kenya et l'Afrique du Sud comptent chacun deux incidents ; l'Algérie et Maurice en comptent un chacun. Aucun défacement n'est recensé.

- **6 incidents** dans **4 pays** et **5 acteurs / sources observés**.
- **1 ransomware (16,7 %)**, **4 fuites de données (66,7 %)** et **1 vente d'accès (16,7 %)**.
- Finance / Banque représente **3 incidents (50,0 %)**, Gouvernement / Administration **2 (33,3 %)** et Ressources humaines / Recrutement **1 (16,7 %)**.
- Les observations les plus importantes concernent les échantillons visibles de documents d'identité, KYC, d'entreprise et financiers dans la publication ransomware SpearFin, l'exposition alléguée à grande échelle de dossiers de recrutement kényans, ainsi que des CV de jeunes et des entrées de clés API en Afrique du Sud.
- La vente d'accès visant le ministère du Commerce et la publication concernant la South African Reserve Bank restent des revendications sans confirmation indépendante.

### Liste des victimes

👉🏾 [Voir la liste complète des victimes](./victims_FR.md)

## 2. Méthodologie

- **Périmètre :** 54 pays africains.
- **Période :** 1er–31 août 2026, selon les dates de détection/publication du fichier `victims.md`.
- **Sources :** OSINT, forums clandestins et éléments de stockage cloud/base de données exposés décrits dans le fichier source.
- **Inclusion :** victime, activité ou exposition liée à l'Afrique avec pays et organisation/contexte identifiables.
- **Typologie :** Ransomware, Fuite de données, Vente d'accès et Défacement. Une publication n'est pas traitée comme une confirmation sans éléments suffisants.
- `victims.md` est la source unique de vérité pour tous les comptages de ce rapport.

## 3. Vue d'ensemble

| Indicateur | Valeur |
|---|---:|
| Total des incidents | 6 |
| Pays concernés | 4 |
| Acteurs / sources observés | 5 |
| Ransomware | 1 (16,7 %) |
| Fuites de données | 4 (66,7 %) |
| Ventes d'accès | 1 (16,7 %) |
| Défacement | 0 (0,0 %) |

### Classement par pays

| Pays | Incidents | Répartition |
|---|---:|---|
| 🇰🇪 Kenya | 2 | ███ 33,3 % |
| 🇿🇦 Afrique du Sud | 2 | ███ 33,3 % |
| 🇩🇿 Algérie | 1 | ██ 16,7 % |
| 🇲🇺 Maurice | 1 | ██ 16,7 % |

```pie
title Incidents par pays — août 2026
"Kenya" : 2
"Afrique du Sud" : 2
"Algérie" : 1
"Maurice" : 1
```

### Type d'incident par pays

| Pays | Ransomware | Fuite de données | Vente d'accès | Défacement |
|---|---:|---:|---:|---:|
| Algérie | 0 | 0 | 1 | 0 |
| Kenya | 0 | 2 | 0 | 0 |
| Maurice | 1 | 0 | 0 | 0 |
| Afrique du Sud | 0 | 2 | 0 | 0 |
| **Total** | **1** | **4** | **1** | **0** |

🟧 Ransomware | 🟦 Fuites de données | 🟨 Ventes d'accès | 🟥 Défacement

### Répartition régionale

| Région | Incidents |
|---|---:|
| Afrique de l'Est | 3 |
| Afrique australe | 2 |
| Afrique du Nord | 1 |

### Répartition sectorielle

| Secteur | Incidents | Part |
|---|---:|---:|
| Finance / Banque | 3 | 50,0 % |
| Gouvernement / Administration | 2 | 33,3 % |
| Ressources humaines / Recrutement | 1 | 16,7 % |

```pie
title Incidents par secteur — août 2026
"Finance / Banque" : 3
"Gouvernement / Administration" : 2
"Ressources humaines / Recrutement" : 1
```

### Acteurs / sources les plus actifs

| Acteur ou source | Type d'incident | Incidents | Cibles |
|---|---|---:|---|
| exfilar | Fuite de données | 2 | SnapStar Talent ; mpowa.mobi |
| Florence | Vente d'accès | 1 | Ministère du Commerce (Algérie) |
| incransom | Ransomware | 1 | SpearFin Ltd |
| NullSec Nigeria | Fuite de données | 1 | South African Reserve Bank |
| OriginalCrazyOldFart | Fuite de données | 1 | Plateforme PAYGO kényane non identifiée |

## 4. Analyse détaillée par type d'incident

### 4.1 Ransomware

Une publication ransomware est recensée. SpearFin Ltd a été publiée par incransom avec une archive revendiquée de 416 Go et une date de fuite alléguée au 26 juin 2026. Les captures fournies affichent des miniatures présentées comme des échantillons et indiquent que la publication intégrale était encore annoncée comme à venir. AFRINTEL n'a pas examiné les fichiers sous-jacents et ne dispose d'aucun élément établissant un chiffrement, une perturbation opérationnelle, le volume annoncé ou une confirmation indépendante de la victime.

### 4.2 Fuites de données et ventes d'accès

Quatre fuites de données et une vente d'accès ont été recensées. Les entrées sud-africaines concernent une publication non vérifiée visant la banque centrale et une exposition distincte analysée portant sur des CV de jeunes, des données de géolocalisation, des comptes utilisateurs et des entrées de clés API. Les entrées kényanes concernent des données de financement client associées à une activité PAYGO non identifiée et une revendication proposant un important jeu de données de recrutement comprenant des identités, candidatures, CV et entretiens vidéo. L'entrée algérienne est une vente d'accès VPN annoncée sans confirmation indépendante.

## 5. Impact sectoriel

Finance / Banque représente **3 des 6 incidents (50,0 %)**, associés aux dossiers PAYGO kényans, à la revendication visant la banque centrale sud-africaine et à la publication ransomware SpearFin. Gouvernement / Administration représente **2 incidents (33,3 %)**, avec la revendication de vente d'accès en Algérie et l'exposition d'un service jeunesse en Afrique du Sud. Ressources humaines / Recrutement représente **1 incident (16,7 %)**, la revendication de vente de données concernant SnapStar Talent.

## 6. Profil des acteurs

Cinq acteurs ou sources de publication distincts sont recensés. exfilar apparaît dans deux entrées de fuite de données au Kenya et en Afrique du Sud impliquant des données applicatives prétendument exposées dans le cloud. incransom est associé à l'unique publication ransomware. Ces observations ne permettent pas d'établir une chaîne d'intrusion commune ni une relation de campagne plus large.

### 6.1 Évaluation du risque

| Pays | Risque | Justification |
|---|---|---|
| 🇰🇪 Kenya | 🔴 Élevé | Deux entrées concernent des données sensibles de financement et un important jeu de données de recrutement allégué comprenant des identités, CV et entretiens vidéo. |
| 🇿🇦 Afrique du Sud | 🔴 Élevé | Le mois comprend des dossiers sensibles de jeunes et des entrées de clés API exposés, ainsi qu'une revendication distincte non vérifiée visant la banque centrale. |
| 🇲🇺 Maurice | 🔴 Élevé | La publication SpearFin affiche des échantillons présentés comme des documents sensibles d'identité, KYC, d'entreprise et financiers ; l'authenticité, l'exhaustivité et le volume revendiqué restent non confirmés. |
| 🇩🇿 Algérie | 🟠 Moyen | Un accès VPN gouvernemental a été annoncé, mais la revendication et sa validité restent non vérifiées. |

## 7. Tendances et lacunes de renseignement

- Les bases de données et services de stockage cloud mal configurés restent une voie d'exposition importante.
- Les données de recrutement combinent identité, emploi, rémunération et images enregistrées, ce qui accroît les risques de fraude, d'usurpation et d'atteinte à la vie privée.
- La publication SpearFin illustre le risque de concentration chez les administrateurs de fonds : une seule archive alléguée peut contenir des dossiers concernant plusieurs entités gérées et investisseurs.
- exfilar apparaît dans deux publications observées impliquant des données applicatives hébergées dans le cloud ; les éléments disponibles ne prouvent pas une chaîne d'intrusion commune.
- Les lacunes portent sur l'opérateur PAYGO kényan exact, la validité et les privilèges de l'accès algérien, l'authenticité et l'exhaustivité des éléments SnapStar Talent et SpearFin, la revendication visant la banque centrale et l'éventuelle persistance d'expositions dans les environnements associés.

## 8. Cartographie MITRE ATT&CK (contextuelle)

| Phase | Technique | Nom | Observation associée |
|---|---|---|---|
| Accès initial | T1078 | Valid Accounts | Accès VPN annoncé dans le cas algérien ; validité non confirmée indépendamment. |
| Collecte | T1530 | Data from Cloud Storage | Des fichiers cloud sont décrits dans le dossier PAYGO kényan et la revendication SnapStar Talent. |
| Collecte | T1213.006 | Databases | Des dossiers clients, applicatifs et candidats auraient été accessibles dans des bases de données. |

Ces correspondances sont défensives et contextuelles ; elles ne prouvent pas la chaîne complète d'intrusion des acteurs. Aucune technique ATT&CK n'est attribuée à SpearFin, car les captures n'établissent ni la méthode d'accès initial, ni la collecte, ni l'exfiltration, ni le chiffrement.

## 9. Recommandations

- Administrations : imposer une MFA résistante au phishing pour les VPN, revoir les accès privilégiés et surveiller les connexions VPN anormales.
- Équipes cloud et applicatives : interdire les lectures publiques par défaut, tester continuellement les règles Firestore/Firebase/base de données et faire tourner immédiatement les clés API exposées.
- Opérateurs financiers et PAYGO : limiter les champs exportés, chiffrer les sauvegardes, surveiller le stockage objet public et préparer les procédures d'information des clients.
- Administrateurs de fonds et prestataires de services aux entreprises : isoler les référentiels KYC, appliquer le moindre privilège, revoir les accès tiers et préparer des procédures coordonnées de notification aux entités gérées concernées.
- Plateformes RH et de recrutement : séparer les documents d'identité et entretiens enregistrés, raccourcir la durée des URL signées, restreindre les exports massifs et appliquer des durées de conservation respectueuses de la vie privée.

## 10. Recommandations SOC et tactiques

- Déclencher des alertes sur les connexions VPN depuis une géographie inhabituelle, un nouvel appareil ou un compte dormant.
- Surveiller les journaux cloud pour les lectures anonymes, exports massifs, énumérations et accès aux bases de préproduction ou de production.
- Détecter l'utilisation de clés API depuis de nouvelles plages IP, des user-agents inattendus ou des services non autorisés.
- Rechercher les accès massifs aux dossiers candidats et clients, CV, photographies et entretiens vidéo, notamment la génération inhabituelle d'URL signées ou des volumes anormaux de téléchargement.
- Surveiller les référentiels KYC, la gestion documentaire et les partages de fichiers pour détecter des lectures massives, créations d'archives et transferts sortants inhabituels, sans considérer ces seuls signaux comme une preuve d'activité ransomware.

## 11. Recommandations stratégiques

Maintenir un inventaire des actifs et stockages exposés sur Internet, imposer une revue de sécurité des environnements de préproduction et de production, et organiser des évaluations externes récurrentes pour les plateformes publiques, financières, d'administration de fonds et de recrutement. Traiter l'exposition de données personnelles, financières et professionnelles comme un incident nécessitant une revue coordonnée juridique, vie privée et protection des clients ou candidats.

## 12. Conclusion

Août 2026 comprend **6 incidents recensés** : une publication ransomware, quatre entrées de fuite de données et une revendication de vente d'accès. Bien que plusieurs publications restent non confirmées, la sensibilité et l'ampleur des données identitaires, professionnelles, financières et gouvernementales revendiquées justifient une validation défensive immédiate par les organisations potentiellement concernées.

— **AFRINTEL**  
[Dépôt GitHub](https://github.com/Hatchepsoute/AFRINTEL)
