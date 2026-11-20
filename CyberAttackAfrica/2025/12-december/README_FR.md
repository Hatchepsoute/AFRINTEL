# Rapport CTI AFRINTEL - Cybermenaces en Afrique - Décembre 2025

👉🏾 [English version](./README.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Période-Décembre%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Synthèse exécutive

En décembre 2025, AFRINTEL documente **21 cyberincidents** affectant des organisations et services numériques dans **11 pays africains**.

Le paysage est dominé par le **Ransomware avec 14 fiches (66,7 %)**, suivi des **Data Leak avec 7 (33,3 %)**.

La concentration géographique est marquée : **Égypte (6)**, **Afrique du Sud (3)** et **Tunisie (4)** représentent ensemble **13 fiches, soit 61,9 % du mois**. Cette concentration reflète la visibilité du corpus AFRINTEL et non un taux national exhaustif de compromission.

Sur le plan sectoriel, les catégories normalisées les plus représentées sont **Finance / Banque (4)**, **Santé / Médical (3)**, **Gouvernement / Administration (2)**, **Éducation / Université (3)** et **Industrie / Fabrication (2)**. Les labels d'acteurs les plus fréquents sont `qilin` (3), `lockbit5` (3), `dragonforce` (2) et `nova` (2).

La maturité des preuves reste variable : **13 fiches sont `Claim - Unverified`, 7 sont `Claim - Data Sample Published` et 1 est `Data Fully Published`**. AFRINTEL conserve une séparation stricte entre faits observés, revendications, corroborations, confirmations officielles et inconnues techniques.

Par rapport à novembre, le volume mensuel **augmente de 5 fiches**. Les variations les plus visibles concernent le Ransomware 10→14 (+4), les Data Leak 5→7 (+2) et le Defacement 1→0 (-1).

> **Note de lecture :** les chiffres AFRINTEL décrivent les incidents documentés et la visibilité des menaces observées. Ils ne constituent pas une mesure exhaustive de toutes les cyberattaques réellement survenues en Afrique.

### 1.1 Comparaison avec le mois précédent

| Indicateur | Novembre 2025 | Décembre 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 16 | 21 | **+5 (+31,3 %)** |
| Ransomware | 10 | 14 | **+4 (+40,0 %)** |
| Data Leak | 5 | 7 | **+2 (+40,0 %)** |
| Access Sale | 0 | 0 | **Stable** |
| DDoS | 0 | 0 | **Stable** |
| Defacement | 1 | 0 | **-1 (-100,0 %)** |
| Account Takeover | 0 | 0 | **Stable** |
| System Intrusion | 0 | 0 | **Stable** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |

## 2. Méthodologie
![Comparaison décembre 2025 avec le mois précédent](assets/comparaison_FR.png)


- **Périmètre :** 54 pays africains ; période de référence : décembre 2025.
- **Source de vérité :** couple validé `victims_FR.md` / `victims.md`.
- **Classification :** Ransomware, Data Leak, Access Sale, DDoS, Defacement, Account Takeover, System Intrusion, Malware et Operational Fraud.
- **Comptage :** une fiche canonique correspond à un cyberincident documenté ; les dossiers en investigation restent hors statistiques.
- **Chronologie :** `Date de l'incident` et `Date de publication initiale` sont séparées.
- **Dates incertaines :** lorsqu'aucun jour de compromission n'est établi, la période de publication soutenue par les preuves est conservée sans inventer de date technique d'intrusion.
- **Preuve :** type d'incident, statut, confiance, impact et provenance restent des dimensions distinctes.
- **Limite :** les fréquences reflètent la visibilité AFRINTEL et non l'ensemble des compromissions réelles sur le continent.

## 3. Vue d'ensemble et types d'incident

| Indicateur | Valeur |
|---|---:|
| Incidents documentés | **21** |
| Pays représentés | **11** |
| Régions représentées | **4** |
| Premier pays | **Égypte (6)** |
| Premier secteur normalisé | **Finance / Banque (4)** |
| Premiers labels acteurs | **qilin (3), lockbit5 (3)** |

| Type d'incident | Fiches | Part |
|---|---:|---:|
| Ransomware | 14 | 66,7 % |
| Data Leak | 7 | 33,3 % |
| Access Sale | 0 | 0,0 % |
| DDoS | 0 | 0,0 % |
| Defacement | 0 | 0,0 % |
| Account Takeover | 0 | 0,0 % |
| System Intrusion | 0 | 0,0 % |
| Malware | 0 | 0,0 % |
| Operational Fraud | 0 | 0,0 % |
| **Total** | **21** | **100 %** |

```mermaid
pie showData
    title Types d'incident - Décembre 2025
    "Ransomware" : 14
    "Data Leak" : 7
```

## 4. Répartition géographique
![Types d’incident](assets/types_FR.png)
![Répartition des types d’incident](assets/types_pie_FR.png)


| Pays | Total | Ransomware | Data Leak |
|---|---:|---:|---:|
| Égypte | **6** | 4 | 2 |
| Afrique du Sud | **3** | 3 | 0 |
| Tunisie | **4** | 3 | 1 |
| Zambie | **1** | 1 | 0 |
| Ghana | **1** | 1 | 0 |
| Nigeria | **1** | 1 | 0 |
| Zimbabwe | **1** | 1 | 0 |
| Algérie | **1** | 0 | 1 |
| Maroc | **1** | 0 | 1 |
| Kenya | **1** | 0 | 1 |
| Côte d'Ivoire | **1** | 0 | 1 |
| **Total** | **21** | **14** | **7** |

## 5. Répartition régionale
![Incidents documentés par pays](assets/pays_FR.png)


| Région | Fiches | Part |
|---|---:|---:|
| Afrique du Nord | 12 | 57,1 % |
| Afrique australe | 5 | 23,8 % |
| Afrique de l'Ouest | 3 | 14,3 % |
| Afrique de l'Est | 1 | 4,8 % |
| **Total** | **21** | **100 %** |

La région la plus représentée est **l'Afrique du Nord avec 12 fiches (57,1 %)**.

## 6. Impact sectoriel
![Répartition régionale](assets/regions_FR.png)
![Parts régionales](assets/regions_pie_FR.png)


| Secteur normalisé | Fiches | Part |
|---|---:|---:|
| Finance / Banque | 4 | 19,0 % |
| Santé / Médical | 3 | 14,3 % |
| Gouvernement / Administration | 2 | 9,5 % |
| Éducation / Université | 3 | 14,3 % |
| Industrie / Fabrication | 2 | 9,5 % |
| Technologie / IT | 1 | 4,8 % |
| Agriculture / Agro-industrie | 2 | 9,5 % |
| Non précisé | 1 | 4,8 % |
| Construction / Immobilier | 1 | 4,8 % |
| Énergie / Services publics | 1 | 4,8 % |
| Commerce / E-commerce | 1 | 4,8 % |
| **Total** | **21** | **100 %** |

## 7. Acteurs / groupes
![Exposition sectorielle](assets/secteurs_FR.png)
![Répartition sectorielle](assets/secteurs_pie_FR.png)


| Acteur / Groupe | Fiches |
|---|---:|
| qilin | 3 |
| lockbit5 | 3 |
| dragonforce | 2 |
| nova | 2 |
| ransomhouse | 1 |
| kazu | 1 |
| devman | 1 |
| direwolf | 1 |
| Habibi | 1 |
| GhostVector | 1 |
| camillabf | 1 |
| KaruHunters | 1 |
| LindaBF | 1 |
| Ahlul Sahara | 1 |

## 8. Maturité des preuves
![Acteurs et labels de publication](assets/acteurs_FR.png)


| Maturité de preuve | Fiches | Part |
|---|---:|---:|
| Claim - Unverified | 13 | 61,9 % |
| Claim - Data Sample Published | 7 | 33,3 % |
| Data Fully Published | 1 | 4,8 % |
| **Total** | **21** | **100 %** |

## 9. Chronologie
![Maturité des preuves](assets/preuves_FR.png)


```mermaid
timeline
    title AFRINTEL - Décembre 2025
    05 Décembre 2025 : 3S Software
    05 Décembre 2025 : National Health Insurance Management Authority
    06 Décembre 2025 : Kasapreko Company Limited
    06 Décembre 2025 : Diesel Electric
    07 Décembre 2025 : incolease.com
    07 Décembre 2025 : elundini.gov.za
    08 Décembre 2025 : Arkan
    11 Décembre 2025 : Leadway Assurance / Leadway Health
    12 Décembre 2025 : Hopital La Rabta
    13 Décembre 2025 : ANADER
    15 Décembre 2025 : Examens.tn
    15 Décembre 2025 : Société Tunisienne de Radiologie
    22 Décembre 2025 : Polaris Parks
    24 Décembre 2025 : National Credit Regulator
    26 Décembre 2025 : Hopital La Rabta - seconde revendication
    26 Décembre 2025 : Proplastics Limited - seconde revendication
    26 Décembre 2025 : Yalla Tager Marketplace
    29 Décembre 2025 : Université d'Oran 1 Ahmed Ben Bella
    29 Décembre 2025 : 100 Watt Plast
    31 Décembre 2025 : Pharmacie.ma
    31 Décembre 2025 : KETRACO
```

## 10. Analyse CTI mensuelle

### Ransomware

**14 fiches** sont classées Ransomware. Les principaux pays sont l'Égypte (4), l'Afrique du Sud (3) et la Tunisie (4). Une publication sur un leak site ne prouve pas à elle seule le chiffrement ou l'exfiltration complète.

### Data Leak

**7 fiches** sont classées Data Leak. L'Égypte en compte 2, tandis que l'Algérie, la Côte d'Ivoire, le Maroc et le Kenya en comptent une chacun. Le dossier ANADER est une **revendication accompagnée d'un échantillon** : la structure SQL/JSON, les rôles administratifs et les rattachements territoriaux sont visibles, mais le dump de 11,4 MB, son origine et son exhaustivité restent non vérifiés.

## 11. Incidents notables

| Pays | Organisation | Type | Statut | Impact | Confiance |
|---|---|---|---|---|---|
| Afrique du Sud | National Credit Regulator (NCR) | Ransomware | Claim - Data Sample Published | Level 4 | High |
| Égypte | Yalla Tager Marketplace | Data Leak | Claim - Data Sample Published | Level 3 | Medium |
| Égypte | 100 Watt Plast | Data Leak | Claim - Data Sample Published | N/A | High |
| Maroc | Pharmacie.ma | Data Leak | Claim - Data Sample Published | N/A | N/A |
| Kenya | KETRACO | Data Leak | Claim - Data Sample Published | N/A | Medium |

## 12. Principaux enseignements et lacunes de renseignement

- **Concentration géographique :** l'Égypte représente 6 fiches (28,6 %), devant l'Afrique du Sud (3) et la Tunisie (4).
- **Structure de menace :** le Ransomware reste le premier type avec 14 fiches, suivi des Data Leak (7).
- **Secteurs :** Finance / Banque (4) et Santé / Médical (3) concentrent la plus forte visibilité ; Commerce / E-commerce gagne une fiche avec Yalla Tager.
- **Preuve :** les 21 fiches restent des revendications ou publications à niveaux de preuve distincts, dont 7 accompagnées d'échantillons publiés et 1 présentée comme entièrement publiée.
- **Yalla Tager :** l'échantillon soutient une revendication d'exposition de données clients/commerçants, sans établir la date ni la méthode de compromission et sans valider le volume annoncé de 20 000 utilisateurs.

### Intelligence gaps

- vecteur d'accès initial souvent non public ;
- date technique exacte de compromission parfois inconnue ;
- volumes revendiqués rarement vérifiables intégralement ;
- attribution technique souvent limitée au pseudonyme ou label de publication ;
- informations publiques sur remédiation, cause racine et conclusions DFIR encore limitées.

## 13. Recommandations

### Organisations

- imposer une MFA résistante au phishing sur les comptes privilégiés, la messagerie, les consoles d'administration et les accès back-office vendeurs/commerçants ;
- appliquer le moindre privilège et surveiller les exports massifs de données clients et commerçants ;
- maintenir des sauvegardes testées et formaliser les procédures de réponse aux violations de données ;
- revoir les interfaces exposées de support client, marketplace, API et administration.

### SOC et détection

- surveiller les authentifications anormales, changements de rôles et créations de comptes privilégiés ;
- détecter les lectures massives de bases, exports CSV inhabituels, créations d'archives et transferts sortants volumineux ;
- corréler IAM, applicatif, WAF, proxy, DNS, cloud et télémétrie EDR ;
- alerter sur les accès anormaux aux jeux de données clients/commerçants depuis de nouveaux appareils, localisations ou comptes de service.

### CTI

- distinguer date de publication, horodatages de compte/client, date d'extraction et date technique de compromission ;
- conserver les volumes revendiqués par l'acteur séparés de la taille de l'échantillon observé ;
- vérifier la parité FR/EN avant toute agrégation statistique.

## 14. Conclusion

**Décembre 2025** compte **21 cyberincidents documentés** dans **11 pays africains** : 14 Ransomware et 7 Data Leak. L'ajout d'ANADER porte la Côte d'Ivoire à une fiche et augmente la composante Data Leak accompagnée d'échantillons, sans modifier l'exigence analytique consistant à séparer les données observées du périmètre revendiqué.

👉🏾 [Voir les victimes du mois](./victims_FR.md)

**AFRINTEL** - TLP:CLEAR
