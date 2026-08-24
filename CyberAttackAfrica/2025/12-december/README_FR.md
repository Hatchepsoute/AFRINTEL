# Rapport CTI AFRINTEL - Cybermenaces en Afrique - Décembre 2025

👉🏾 [English version](./README.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Period-December%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Synthèse exécutive

En Décembre 2025, AFRINTEL documente **18 cyberincidents** affectant des organisations et services numériques dans **10 pays africains**.

Le paysage est dominé par **Ransomware avec 14 fiches (77,8 %)**, suivi de **Data Leak avec 4 (22,2 %)**.

La concentration géographique est marquée : **Égypte (5)**, **Afrique du Sud (3)**, **Tunisie (3)** représentent ensemble **11 fiches, soit 61,1 % du mois**. Cette concentration doit être interprétée comme la visibilité du corpus AFRINTEL et non comme un taux national exhaustif de compromission.

Sur le plan sectoriel, les catégories les plus représentées sont **Finance / Banque (4)**, **Santé / Médical (3)**, **Gouvernement / Administration (2)**. Les labels d'acteurs les plus fréquents sont `qilin` (3), `lockbit5` (3), `dragonforce` (2). `Unknown`, lorsqu'il apparaît, désigne une absence d'attribution et non un groupe cybercriminel.

La maturité des preuves reste variable : **18 fiches** relèvent de claims non vérifiés ou accompagnés d'échantillons. AFRINTEL conserve une séparation stricte entre **faits observés, revendications, corroborations, confirmations officielles et inconnues techniques**.

Par rapport à Novembre, le volume mensuel **augmente de 3 fiches**. Les variations les plus visibles concernent Ransomware 10->14 (+4), Defacement 1->0 (-1).

> **Note de lecture :** les chiffres AFRINTEL décrivent les incidents documentés et la visibilité des menaces observées. Ils ne constituent pas une mesure exhaustive de toutes les cyberattaques réellement survenues en Afrique.

### 1.1 Comparaison avec le mois précédent

| Indicateur | Novembre 2025 | Décembre 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 15 | 18 | **+3 (+20,0 %)** |
| Ransomware | 10 | 14 | **+4 (+40,0 %)** |
| Data Leak | 4 | 4 | **Stable** |
| Access Sale | 0 | 0 | **Stable** |
| DDoS | 0 | 0 | **Stable** |
| Defacement | 1 | 0 | **-1 (-100,0 %)** |
| Account Takeover | 0 | 0 | **Stable** |
| System Intrusion | 0 | 0 | **Stable** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |




## 2. Méthodologie

- **Périmètre :** 54 pays africains ; période de référence : Décembre 2025.
- **Source de vérité :** couple validé `victims_FR.md` / `victims.md`.
- **Classification :** Ransomware, Data Leak, Access Sale, DDoS, Defacement, Account Takeover, System Intrusion, Malware et Operational Fraud.
- **Comptage :** une fiche canonique correspond à un cyberincident documenté ; les dossiers en investigation restent hors statistiques.
- **Chronologie :** `Date de l'incident` et `Date de publication initiale` sont séparées. Une publication ultérieure ne déplace pas artificiellement un incident vers un autre mois lorsque la chronologie est suffisamment établie.
- **Dates incertaines :** lorsqu'un jour exact n'est pas connu, le mois ou la fenêtre soutenue par les preuves est conservé.
- **Sources :** les liens publics sont conservés pour les incidents complémentaires identifiés par recherche OSINT/web ; ils ne sont pas imposés rétroactivement aux observations historiques ou Dark Web directes.
- **Preuve :** type d'incident, statut, confiance, impact et provenance restent des dimensions distinctes.
- **Secteurs :** normalisation calculée une seule fois à partir du corpus structuré, puis utilisée à l'identique en FR et EN.
- **Limite :** les fréquences reflètent la visibilité AFRINTEL et non l'ensemble des compromissions réelles sur le continent.

## 3. Vue d'ensemble et types d'incident

| Indicateur | Valeur |
|---|---:|
| Incidents documentés | **18** |
| Pays représentés | **10** |
| Régions représentées | **4** |
| Premier pays | **Égypte (5)** |
| Premier secteur | **Finance / Banque (4)** |
| Premier label acteur | **qilin (3)** |

| Type d'incident | Fiches | Part |
|---|---:|---:|
| Ransomware | 14 | 77,8 % |
| Data Leak | 4 | 22,2 % |
| Access Sale | 0 | 0,0 % |
| DDoS | 0 | 0,0 % |
| Defacement | 0 | 0,0 % |
| Account Takeover | 0 | 0,0 % |
| System Intrusion | 0 | 0,0 % |
| Malware | 0 | 0,0 % |
| Operational Fraud | 0 | 0,0 % |
| **Total** | **18** | **100 %** |

```mermaid
pie showData
    title Types d'incident - Décembre 2025
    "Ransomware" : 14
    "Data Leak" : 4
```

## 4. Répartition géographique

| Pays | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Égypte | **5** | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Afrique du Sud | **3** | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tunisie | **3** | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zambie | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ghana | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nigeria | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zimbabwe | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Algérie | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Maroc | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kenya | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **18** | **14** | **4** | **0** | **0** | **0** | **0** | **0** | **0** |

> `Operational Fraud = 0` ce mois-ci ; la colonne est omise pour préserver la lisibilité.

## 5. Répartition régionale

| Région | Fiches | Part |
|---|---:|---:|
| Afrique du Nord | 10 | 55,6 % |
| Afrique australe | 5 | 27,8 % |
| Afrique de l'Ouest | 2 | 11,1 % |
| Afrique de l'Est | 1 | 5,6 % |
| **Total** | **18** | **100 %** |

La région la plus représentée est **Afrique du Nord avec 10 fiches (55,6 %)**.

## 6. Impact sectoriel

| Secteur | Fiches | Part | Activité |
|---|---:|---:|---|
| Finance / Banque | 4 | 22,2 % | ████ |
| Santé / Médical | 3 | 16,7 % | ███ |
| Gouvernement / Administration | 2 | 11,1 % | ██ |
| Éducation / Université | 2 | 11,1 % | ██ |
| Industrie / Fabrication | 2 | 11,1 % | ██ |
| Technologie / IT | 1 | 5,6 % | █ |
| Agriculture / Agro-industrie | 1 | 5,6 % | █ |
| Non précisé | 1 | 5,6 % | █ |
| Construction / Immobilier | 1 | 5,6 % | █ |
| Énergie / Services publics | 1 | 5,6 % | █ |
| **Total** | **18** | **100 %** | |

## 7. Acteurs / groupes

`Unknown` correspond à une absence d'attribution, pas à un acteur.

| Acteur / Groupe | Fiches | Activité |
|---|---:|---|
| qilin | 3 | ███ |
| lockbit5 | 3 | ███ |
| dragonforce | 2 | ██ |
| nova | 2 | ██ |
| ransomhouse | 1 | █ |
| kazu | 1 | █ |
| devman | 1 | █ |
| direwolf | 1 | █ |
| GhostVector | 1 | █ |
| camillabf | 1 | █ |
| KaruHunters | 1 | █ |
| LindaBF | 1 | █ |

## 8. Maturité des preuves

| Maturité de preuve | Fiches | Part |
|---|---:|---:|
| Claim - Unverified | 13 | 72,2 % |
| Claim - Data Sample Published | 5 | 27,8 % |
| **Total** | **18** | **100 %** |

Les statuts de preuve décrivent le niveau de validation disponible ; ils ne changent pas le type technique de l'incident.

## 9. Chronologie

```mermaid
timeline
    title AFRINTEL - Décembre 2025
    05 Décembre 2025 : 3S Software (Secured Smart Systems Overview Metrics)
    05 Décembre 2025 : National Health Insurance Management Authority
    06 Décembre 2025 : Kasapreko Company Limited
    06 Décembre 2025 : Diesel Electric
    07 Décembre 2025 : incolease.com
    07 Décembre 2025 : elundini.gov.za
    08 Décembre 2025 : Arkan
    11 Décembre 2025 : Leadway Assurance / Leadway Health
    12 Décembre 2025 : Hopital La Rabta (Centre Hospitalier Universitaire)
    15 Décembre 2025 : Société Tunisienne de Radiologie (strtn.org)
    22 Décembre 2025 : Polaris Parks
    24 Décembre 2025 : National Credit Regulator (NCR)
    26 Décembre 2025 : Hopital La Rabta (deuxième revendication ransomware)
    26 Décembre 2025 : Proplastics Limited (deuxième revendication ransomware)
    29 Décembre 2025 : Université d'Oran 1 Ahmed Ben Bella
    29 Décembre 2025 : 100 Watt Plast (100wattplast.com)
    31 Décembre 2025 : Pharmacie.ma
    31 Décembre 2025 : Kenya Electricity Transmission Company (KETRACO)
```

## 10. Analyse CTI mensuelle

### Ransomware

**14 fiches** sont classées Ransomware. Principaux pays : Égypte (4), Afrique du Sud (3), Tunisie (3). Une publication sur un leak site ne prouve pas, à elle seule, le chiffrement ou l'exfiltration complète.

### Data Leak

**4 fiches** sont classées Data Leak. Principaux pays : Algérie (1), Égypte (1), Maroc (1). AFRINTEL distingue les données effectivement observées des volumes globaux revendiqués.

## 11. Incidents notables

| Pays | Organisation | Type | Statut | Impact | Confiance |
|---|---|---|---|---|---|
| Afrique du Sud | National Credit Regulator (NCR) | Ransomware | Claim - Data Sample Published | Level 4 | High |
| Égypte | 3S Software (Secured Smart Systems Overview Metrics) | Ransomware | Claim - Unverified | N/A | N/A |
| Zambie | National Health Insurance Management Authority | Ransomware | Claim - Unverified | N/A | N/A |
| Ghana | Kasapreko Company Limited | Ransomware | Claim - Unverified | N/A | N/A |
| Afrique du Sud | Diesel Electric | Ransomware | Claim - Unverified | N/A | N/A |

> Ce tableau met en avant jusqu'à cinq fiches selon le niveau d'impact, la confirmation et la confiance structurés. Il ne constitue pas un classement absolu de gravité.

## 12. Principaux enseignements et lacunes de renseignement

- **Concentration géographique :** Égypte représente 5 fiches (27,8 %), devant Afrique du Sud (3) et Tunisie (3).
- **Structure de menace :** Ransomware est le premier type avec 14 fiches, suivi de Data Leak (4).
- **Secteurs :** Finance / Banque (4) et Santé / Médical (3) concentrent la plus forte visibilité.
- **Acteurs :** les labels les plus fréquents sont qilin (3), lockbit5 (3) et dragonforce (2).
- **Preuve :** 18 fiches reposent sur des claims non vérifiés ou accompagnés d'un échantillon ; ces statuts ne valent pas confirmation technique complète.

### Intelligence gaps

- vecteur d'accès initial souvent non public ;
- date technique exacte de compromission parfois inconnue ;
- volumes revendiqués rarement vérifiables intégralement ;
- attribution technique souvent limitée au pseudonyme ou label de publication ;
- informations publiques sur remédiation, cause racine et conclusions DFIR encore limitées.

Ces lacunes doivent guider la collecte sans être remplacées par des hypothèses.

## 13. Recommandations

### Organisations

- imposer MFA résistante au phishing sur les comptes privilégiés, VPN, messagerie, réseaux sociaux et consoles d'administration ;
- appliquer PAM, moindre privilège, segmentation et rotation des secrets ;
- maintenir des sauvegardes immuables et tester la restauration ;
- renforcer les applications publiques, API et interfaces administratives ;
- formaliser réponse à incident et notification des violations de données.

### SOC et détection

- surveiller les authentifications anormales, changements MFA, créations de comptes privilégiés et élévations de rôles ;
- détecter lectures massives de bases, exports inhabituels, créations d'archives et transferts sortants volumineux ;
- corréler EDR, IAM, VPN, WAF, proxy, DNS, cloud et journaux applicatifs ;
- distinguer DDoS, intrusion interne, compromission de compte et fuite de données pour éviter les conclusions non étayées.

### CTI

- conserver séparément date d'incident, publication initiale, première observation, échantillon, divulgation et confirmation ;
- suivre republications et reventes sans les compter automatiquement comme nouvelles compromissions ;
- maintenir la hiérarchie de preuve entre claim, corroboration et confirmation ;
- valider la parité FR/EN avant toute génération de statistiques.

## 14. Conclusion

Le mois de **Décembre 2025** compte **18 cyberincidents documentés** dans **10 pays africains**. La lecture mensuelle montre que la valeur CTI ne réside pas seulement dans le volume, mais dans la distinction entre **type d'incident, chronologie, niveau de preuve, géographie, secteur et acteur**.

Le rapport conserve ainsi une photographie structurée de la menace observable tout en maintenant les revendications, corroborations, confirmations et inconnues à leur niveau de preuve réel.

👉🏾 [Voir les victimes du mois](./victims_FR.md)

**AFRINTEL** - TLP:CLEAR
