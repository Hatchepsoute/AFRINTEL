[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Type de menace](https://img.shields.io/badge/Menace-Vente%20d'accès%20%26%20Fuite-red)
![Période](https://img.shields.io/badge/Période-Août%202026-lightgrey)
![Type de renseignement](https://img.shields.io/badge/Renseignement-CTI-purple)

# Rapport CTI — Cyberattaques en Afrique (août 2026)

👉🏾 [**English version available here**](./README.md)

## 1. Résumé exécutif

AFRINTEL a recensé **3 incidents** concernant des entités africaines en août 2026 : **2 fuites de données** et **1 vente d'accès**. Aucun cas de ransomware ou de défacement n'est identifié dans le fichier source du mois. L'Algérie, le Kenya et l'Afrique du Sud comptent chacun un incident.

- **3 incidents** dans **3 pays** et **3 acteurs/sources observés**.
- **2 fuites de données (66,7 %)** et **1 vente d'accès (33,3 %)**.
- Le secteur Gouvernement / Administration représente **2 incidents (66,7 %)** ; Finance / Banque en représente **1 (33,3 %)**.
- Les observations les plus importantes concernent l'exposition de CV de jeunes et de clés API en Afrique du Sud, ainsi que des données de financement client associées au Kenya.
- La vente d'accès visant le ministère algérien du Commerce reste une revendication de forum non vérifiée.

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
| Total des incidents | 3 |
| Pays concernés | 3 |
| Acteurs / sources observés | 3 |
| Ransomware | 0 (0,0 %) |
| Fuites de données | 2 (66,7 %) |
| Ventes d'accès | 1 (33,3 %) |
| Défacement | 0 (0,0 %) |

### Classement par pays

| Pays | Incidents | Répartition |
|---|---:|---|
| 🇩🇿 Algérie | 1 | ███ 33,3 % |
| 🇰🇪 Kenya | 1 | ███ 33,3 % |
| 🇿🇦 Afrique du Sud | 1 | ███ 33,3 % |

```pie
title Incidents par pays — août 2026
"Algérie" : 1
"Kenya" : 1
"Afrique du Sud" : 1
```

### Type d'incident par pays

| Pays | Ransomware | Fuite de données | Vente d'accès | Défacement |
|---|---:|---:|---:|---:|
| Algérie | 0 | 0 | 1 | 0 |
| Kenya | 0 | 1 | 0 | 0 |
| Afrique du Sud | 0 | 1 | 0 | 0 |
| **Total** | **0** | **2** | **1** | **0** |

🟧 Ransomware | 🟦 Fuites de données | 🟨 Ventes d'accès | 🟥 Défacement

### Répartition régionale

| Région | Incidents |
|---|---:|
| Afrique du Nord | 1 |
| Afrique de l'Est | 1 |
| Afrique australe | 1 |

### Répartition sectorielle

| Secteur | Incidents | Part |
|---|---:|---:|
| Gouvernement / Administration | 2 | 66,7 % |
| Finance / Banque | 1 | 33,3 % |

```pie
title Incidents par secteur — août 2026
"Gouvernement / Administration" : 2
"Finance / Banque" : 1
```

### Acteurs / sources les plus actifs

| Acteur ou source | Type d'incident | Incidents |
|---|---|---:|
| Florence | Vente d'accès | 1 |
| OriginalCrazyOldFart | Fuite de données | 1 |
| exfilar | Fuite de données | 1 |

## 4. Analyse détaillée par type d'incident

### 4.1 Ransomware

Aucun incident ransomware n'est enregistré dans `victims.md` pour août 2026.

### 4.2 Fuites de données et ventes d'accès

Deux fuites de données et une vente d'accès ont été recensées. L'exposition sud-africaine concerne des CV de jeunes, des données de géolocalisation, des comptes utilisateurs et des entrées de clés API dans un environnement Firebase. Le cas kényan concerne des données de financement client associées à une activité PAYGO non identifiée. L'entrée algérienne est une vente d'accès VPN annoncée, sans confirmation indépendante.

## 5. Impact sectoriel

Le secteur Gouvernement / Administration représente **2 des 3 incidents (66,7 %)**, dont la revendication de vente d'accès en Algérie et l'exposition d'un service jeunesse en Afrique du Sud. Finance / Banque représente **1 incident (33,3 %)**, associé aux données de financement client au Kenya.

## 6. Profil des acteurs

Les trois fiches concernent des acteurs ou sources de publication distincts. Les éléments disponibles n'établissent pas de campagne commune entre eux.

### 6.1 Évaluation du risque

| Pays | Risque | Justification |
|---|---|---|
| 🇿🇦 Afrique du Sud | 🔴 Élevé | Des données sensibles de jeunes et des entrées de clés API auraient été exposées dans un environnement Firebase de préproduction. |
| 🇰🇪 Kenya | 🟠 Moyen | Des données clients et de financement auraient été exposées ; l'organisation exacte reste non identifiée. |
| 🇩🇿 Algérie | 🟠 Moyen | Un accès VPN gouvernemental a été annoncé, mais la revendication et sa validité restent non vérifiées. |

## 7. Tendances et lacunes de renseignement

- Les services cloud mal configurés et les environnements Firebase/base de données exposés restent un risque important.
- Les données financières et identitaires combinées créent des risques de fraude, de phishing et d'usurpation ciblée.
- Les lacunes portent notamment sur l'opérateur kényan exact, la validité et les privilèges de l'accès algérien, et l'éventuelle exposition d'environnements de production liés au cas sud-africain.

## 8. Cartographie MITRE ATT&CK (contextuelle)

| Phase | Technique | Nom | Observation associée |
|---|---|---|---|
| Accès initial | T1078 | Valid Accounts | Accès VPN annoncé dans le cas algérien ; validité non confirmée indépendamment. |
| Collecte | T1530 | Data from Cloud Storage | Éléments de stockage cloud exposés décrits dans le cas kényan. |
| Collecte | T1213 | Data from Information Repositories | Des données de financement client et applicatives auraient été accessibles. |

Ces correspondances sont défensives et contextuelles ; elles ne prouvent pas la chaîne complète d'intrusion des acteurs.

## 9. Recommandations

- Administrations : imposer une MFA résistante au phishing pour les VPN, revoir les accès privilégiés et surveiller les connexions VPN anormales.
- Équipes cloud et applicatives : interdire les lectures publiques par défaut, tester continuellement les règles Firebase/base de données et faire tourner immédiatement les clés API exposées.
- Opérateurs financiers et PAYGO : limiter les champs exportés, chiffrer les sauvegardes, surveiller le stockage objet public et préparer les procédures d'information des clients.

## 10. Recommandations SOC et tactiques

- Déclencher des alertes sur les connexions VPN depuis une géographie inhabituelle, un nouvel appareil ou un compte dormant.
- Surveiller les journaux cloud pour les lectures anonymes, exports massifs, énumérations et accès aux environnements de préproduction.
- Détecter l'utilisation de clés API depuis de nouvelles plages IP, des user-agents inattendus ou des services non autorisés.
- Rechercher les accès massifs aux dossiers clients et les volumes de téléchargement inhabituels.

## 11. Recommandations stratégiques

Maintenir un inventaire des actifs et stockages exposés sur Internet, imposer une revue de sécurité des environnements de préproduction et organiser une évaluation externe récurrente pour les plateformes publiques ou financières. Traiter l'exposition de données personnelles et financières comme un incident nécessitant une revue coordonnée juridique, vie privée et protection client.

## 12. Conclusion

Août 2026 présente un nombre limité mais un impact potentiel élevé : deux expositions de données et une revendication de vente d'accès non vérifiée. La sensibilité des données justifie une validation défensive immédiate par les organisations potentiellement concernées.

— **AFRINTEL**  
[Dépôt GitHub](https://github.com/Hatchepsoute/AFRINTEL)
