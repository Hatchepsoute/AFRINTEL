# Rapport CTI AFRINTEL - Cybermenaces en Afrique - Novembre 2025

👉🏾 [English version](./README.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Period-November%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Synthèse exécutive

En Novembre 2025, AFRINTEL documente **15 cyberincidents** affectant des organisations et services numériques dans **7 pays africains**.

Le paysage est dominé par **Ransomware avec 10 fiches (66,7 %)**, suivi de **Data Leak avec 4 (26,7 %)**. Les autres types observés sont Defacement 1.

La concentration géographique est marquée : **Maroc (4)**, **Égypte (4)**, **Afrique du Sud (2)** représentent ensemble **10 fiches, soit 66,7 % du mois**. Cette concentration doit être interprétée comme la visibilité du corpus AFRINTEL et non comme un taux national exhaustif de compromission.

Sur le plan sectoriel, les catégories les plus représentées sont **Gouvernement / Administration (3)**, **Transport / Logistique (2)**, **Technologie / IT (2)**. Les labels d'acteurs les plus fréquents sont `clop` (3), `nightspire` (3), `spacebears` (1). `Unknown`, lorsqu'il apparaît, désigne une absence d'attribution et non un groupe cybercriminel.

La maturité des preuves reste variable : **13 fiches** relèvent de claims non vérifiés ou accompagnés d'échantillons. AFRINTEL conserve une séparation stricte entre **faits observés, revendications, corroborations, confirmations officielles et inconnues techniques**.

Par rapport à Octobre, le volume mensuel **diminue de 5 fiches**. Les variations les plus visibles concernent Ransomware 16->10 (-6), Defacement 0->1 (+1), Data Leak 3->4 (+1).

> **Note de lecture :** les chiffres AFRINTEL décrivent les incidents documentés et la visibilité des menaces observées. Ils ne constituent pas une mesure exhaustive de toutes les cyberattaques réellement survenues en Afrique.

### 1.1 Comparaison avec le mois précédent

| Indicateur | Octobre 2025 | Novembre 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 20 | 15 | **-5 (-25,0 %)** |
| Ransomware | 16 | 10 | **-6 (-37,5 %)** |
| Data Leak | 3 | 4 | **+1 (+33,3 %)** |
| Access Sale | 1 | 0 | **-1 (-100,0 %)** |
| DDoS | 0 | 0 | **Stable** |
| Defacement | 0 | 1 | **+1 (nouveau)** |
| Account Takeover | 0 | 0 | **Stable** |
| System Intrusion | 0 | 0 | **Stable** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |




## 2. Méthodologie

- **Périmètre :** 54 pays africains ; période de référence : Novembre 2025.
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
| Incidents documentés | **15** |
| Pays représentés | **7** |
| Régions représentées | **4** |
| Premier pays | **Maroc (4)** |
| Premier secteur | **Gouvernement / Administration (3)** |
| Premier label acteur | **clop (3)** |

| Type d'incident | Fiches | Part |
|---|---:|---:|
| Ransomware | 10 | 66,7 % |
| Data Leak | 4 | 26,7 % |
| Access Sale | 0 | 0,0 % |
| DDoS | 0 | 0,0 % |
| Defacement | 1 | 6,7 % |
| Account Takeover | 0 | 0,0 % |
| System Intrusion | 0 | 0,0 % |
| Malware | 0 | 0,0 % |
| Operational Fraud | 0 | 0,0 % |
| **Total** | **15** | **100 %** |

```mermaid
pie showData
    title Types d'incident - Novembre 2025
    "Ransomware" : 10
    "Data Leak" : 4
    "Defacement" : 1
```

## 4. Répartition géographique

| Pays | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Maroc | **4** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| Égypte | **4** | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Afrique du Sud | **2** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Côte d'Ivoire | **2** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zambie | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nigeria | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kenya | **1** | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| **Total** | **15** | **10** | **4** | **0** | **0** | **1** | **0** | **0** | **0** |

> `Operational Fraud = 0` ce mois-ci ; la colonne est omise pour préserver la lisibilité.

## 5. Répartition régionale

| Région | Fiches | Part |
|---|---:|---:|
| Afrique du Nord | 8 | 53,3 % |
| Afrique australe | 3 | 20,0 % |
| Afrique de l'Ouest | 3 | 20,0 % |
| Afrique de l'Est | 1 | 6,7 % |
| **Total** | **15** | **100 %** |

La région la plus représentée est **Afrique du Nord avec 8 fiches (53,3 %)**.

## 6. Impact sectoriel

| Secteur | Fiches | Part | Activité |
|---|---:|---:|---|
| Gouvernement / Administration | 3 | 20,0 % | ███ |
| Transport / Logistique | 2 | 13,3 % | ██ |
| Technologie / IT | 2 | 13,3 % | ██ |
| Finance / Banque | 2 | 13,3 % | ██ |
| Construction / Immobilier | 2 | 13,3 % | ██ |
| Services professionnels / Business | 1 | 6,7 % | █ |
| Commerce / E-commerce | 1 | 6,7 % | █ |
| Industrie / Fabrication | 1 | 6,7 % | █ |
| Santé / Médical | 1 | 6,7 % | █ |
| **Total** | **15** | **100 %** | |

## 7. Acteurs / groupes

`Unknown` correspond à une absence d'attribution, pas à un acteur.

| Acteur / Groupe | Fiches | Activité |
|---|---:|---|
| clop | 3 | ███ |
| nightspire | 3 | ███ |
| spacebears | 1 | █ |
| Unknown | 1 | █ |
| Spirigatito | 1 | █ |
| stormous | 1 | █ |
| anisanas2 | 1 | █ |
| PCP@Kenya (preliminary government attribution) | 1 | █ |
| qilin | 1 | █ |
| benzona | 1 | █ |
| RL000 | 1 | █ |

## 8. Maturité des preuves

| Maturité de preuve | Fiches | Part |
|---|---:|---:|
| Claim - Unverified | 9 | 60,0 % |
| Claim - Data Sample Published | 4 | 26,7 % |
| Data Fully Published | 1 | 6,7 % |
| Confirmation victime / gouvernement / autorité | 1 | 6,7 % |
| **Total** | **15** | **100 %** |

Les statuts de preuve décrivent le niveau de validation disponible ; ils ne changent pas le type technique de l'incident.

## 9. Chronologie

```mermaid
timeline
    title AFRINTEL - Novembre 2025
    04 Novembre 2025 : DOVERN Import
    04 Novembre 2025 : Wannabees (wannabees.co.za)
    05 Novembre 2025 : Anka (Anka.africa)
    06 Novembre 2025 : ELSEWEDYELECTRIC.COM
    06 Novembre 2025 : ZANACO.CO.ZM
    06 Novembre 2025 : www.marjane.ma
    08 Novembre 2025 : NARSA (Agence Nationale de la Sécurité Routière)
    09 Novembre 2025 : Eastern Cape Department of Human Settlements (ECDHS)
    09 Novembre 2025 : Fidelity Pension Managers, Nigeria
    11 Novembre 2025 : Samcrete Holding
    17 Novembre 2025 : Multiple Government of Kenya websites
    25 Novembre 2025 : LAMAICA, Egypt
    26 Novembre 2025 : Arabia Holding
    26 Novembre 2025 : Santé Espoir Vie Côte d’Ivoire (SEV-CI)
    30 Novembre 2025 : Joutech
```

## 10. Analyse CTI mensuelle

### Ransomware

**10 fiches** sont classées Ransomware. Principaux pays : Égypte (4), Maroc (2), Zambie (1). Une publication sur un leak site ne prouve pas, à elle seule, le chiffrement ou l'exfiltration complète.

### Data Leak

**4 fiches** sont classées Data Leak. Principaux pays : Maroc (2), Afrique du Sud (1), Côte d'Ivoire (1). AFRINTEL distingue les données effectivement observées des volumes globaux revendiqués.

### Defacement

**1 Defacement** sont documentés. Répartition : Kenya (1). Un défacement n'est pas reclassé en fuite de données sans preuve distincte.

## 11. Incidents notables

| Pays | Organisation | Type | Statut | Impact | Confiance |
|---|---|---|---|---|---|
| Kenya | Multiple Government of Kenya websites | Defacement | Government Confirmed + Preliminary Actor Attribution | Level 4 | Very High |
| Maroc | www.marjane.ma | Ransomware | Data Fully Published | Level 4 | High |
| Côte d'Ivoire | Anka (Anka.africa) | Data Leak | Claim - Data Sample Published | Level 3 | Medium |
| Zambie | ZANACO.CO.ZM | Ransomware | Claim - Unverified | Level 3 | Medium |
| Égypte | ELSEWEDYELECTRIC.COM | Ransomware | Claim - Unverified | Level 2 | Medium |

> Ce tableau met en avant jusqu'à cinq fiches selon le niveau d'impact, la confirmation et la confiance structurés. Il ne constitue pas un classement absolu de gravité.

## 12. Principaux enseignements et lacunes de renseignement

- **Concentration géographique :** Maroc représente 4 fiches (26,7 %), devant Égypte (4) et Afrique du Sud (2).
- **Structure de menace :** Ransomware est le premier type avec 10 fiches, suivi de Data Leak (4).
- **Secteurs :** Gouvernement / Administration (3) et Transport / Logistique (2) concentrent la plus forte visibilité.
- **Acteurs :** les labels les plus fréquents sont clop (3), nightspire (3) et spacebears (1).
- **Preuve :** 13 fiches reposent sur des claims non vérifiés ou accompagnés d'un échantillon ; ces statuts ne valent pas confirmation technique complète.

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

Le mois de **Novembre 2025** compte **15 cyberincidents documentés** dans **7 pays africains**. La lecture mensuelle montre que la valeur CTI ne réside pas seulement dans le volume, mais dans la distinction entre **type d'incident, chronologie, niveau de preuve, géographie, secteur et acteur**.

Le rapport conserve ainsi une photographie structurée de la menace observable tout en maintenant les revendications, corroborations, confirmations et inconnues à leur niveau de preuve réel.

👉🏾 [Voir les victimes du mois](./victims_FR.md)

**AFRINTEL** - TLP:CLEAR
