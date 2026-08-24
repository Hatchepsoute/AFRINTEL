# Rapport CTI AFRINTEL - Cybermenaces en Afrique - Mars 2025

👉🏾 [English version](./README.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Period-March%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Synthèse exécutive

En Mars 2025, AFRINTEL documente **15 cyberincidents** affectant des organisations et services numériques dans **8 pays africains**.

Le paysage est dominé par **Ransomware avec 9 fiches (60,0 %)**, suivi de **Data Leak avec 2 (13,3 %)**. Les autres types observés sont Account Takeover 2, System Intrusion 1, Access Sale 1.

La concentration géographique est marquée : **Afrique du Sud (5)**, **Égypte (3)**, **Nigeria (2)** représentent ensemble **10 fiches, soit 66,7 % du mois**. Cette concentration doit être interprétée comme la visibilité du corpus AFRINTEL et non comme un taux national exhaustif de compromission.

Sur le plan sectoriel, les catégories les plus représentées sont **Gouvernement / Administration (4)**, **Technologie / IT (3)**, **Éducation / Université (2)**. Les labels d'acteurs les plus fréquents sont `Unknown` (4), `arcusmedia` (2), `nightspire` (2). `Unknown`, lorsqu'il apparaît, désigne une absence d'attribution et non un groupe cybercriminel.

La maturité des preuves reste variable : **11 fiches** relèvent de claims non vérifiés ou accompagnés d'échantillons. AFRINTEL conserve une séparation stricte entre **faits observés, revendications, corroborations, confirmations officielles et inconnues techniques**.

Par rapport à Février, le volume mensuel **augmente de 5 fiches**. Les variations les plus visibles concernent Data Leak 0->2 (+2), System Intrusion 0->1 (+1), Ransomware 8->9 (+1).

> **Note de lecture :** les chiffres AFRINTEL décrivent les incidents documentés et la visibilité des menaces observées. Ils ne constituent pas une mesure exhaustive de toutes les cyberattaques réellement survenues en Afrique.

### 1.1 Comparaison avec le mois précédent

| Indicateur | Février 2025 | Mars 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 10 | 15 | **+5 (+50,0 %)** |
| Ransomware | 8 | 9 | **+1 (+12,5 %)** |
| Data Leak | 0 | 2 | **+2 (nouveau)** |
| Access Sale | 0 | 1 | **+1 (nouveau)** |
| DDoS | 0 | 0 | **Stable** |
| Defacement | 0 | 0 | **Stable** |
| Account Takeover | 2 | 2 | **Stable** |
| System Intrusion | 0 | 1 | **+1 (nouveau)** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |




## 2. Méthodologie

- **Périmètre :** 54 pays africains ; période de référence : Mars 2025.
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
| Pays représentés | **8** |
| Régions représentées | **4** |
| Premier pays | **Afrique du Sud (5)** |
| Premier secteur | **Gouvernement / Administration (4)** |
| Premier label acteur | **Unknown (4)** |

| Type d'incident | Fiches | Part |
|---|---:|---:|
| Ransomware | 9 | 60,0 % |
| Data Leak | 2 | 13,3 % |
| Access Sale | 1 | 6,7 % |
| DDoS | 0 | 0,0 % |
| Defacement | 0 | 0,0 % |
| Account Takeover | 2 | 13,3 % |
| System Intrusion | 1 | 6,7 % |
| Malware | 0 | 0,0 % |
| Operational Fraud | 0 | 0,0 % |
| **Total** | **15** | **100 %** |

```mermaid
pie showData
    title Types d'incident - Mars 2025
    "Ransomware" : 9
    "Data Leak" : 2
    "Access Sale" : 1
    "Account Takeover" : 2
    "System Intrusion" : 1
```

## 4. Répartition géographique

| Pays | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Afrique du Sud | **5** | 2 | 1 | 0 | 0 | 0 | 1 | 1 | 0 |
| Égypte | **3** | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nigeria | **2** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Botswana | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tanzanie | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ghana | **1** | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Burkina Faso | **1** | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Rwanda | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **15** | **9** | **2** | **1** | **0** | **0** | **2** | **1** | **0** |

> `Operational Fraud = 0` ce mois-ci ; la colonne est omise pour préserver la lisibilité.

## 5. Répartition régionale

| Région | Fiches | Part |
|---|---:|---:|
| Afrique australe | 6 | 40,0 % |
| Afrique de l'Ouest | 4 | 26,7 % |
| Afrique du Nord | 3 | 20,0 % |
| Afrique de l'Est | 2 | 13,3 % |
| **Total** | **15** | **100 %** |

La région la plus représentée est **Afrique australe avec 6 fiches (40,0 %)**.

## 6. Impact sectoriel

| Secteur | Fiches | Part | Activité |
|---|---:|---:|---|
| Gouvernement / Administration | 4 | 26,7 % | ████ |
| Technologie / IT | 3 | 20,0 % | ███ |
| Éducation / Université | 2 | 13,3 % | ██ |
| Santé / Médical | 2 | 13,3 % | ██ |
| Commerce / E-commerce | 1 | 6,7 % | █ |
| Construction / Immobilier | 1 | 6,7 % | █ |
| Agriculture / Agro-industrie | 1 | 6,7 % | █ |
| Finance / Banque | 1 | 6,7 % | █ |
| **Total** | **15** | **100 %** | |

## 7. Acteurs / groupes

`Unknown` correspond à une absence d'attribution, pas à un acteur.

| Acteur / Groupe | Fiches | Activité |
|---|---:|---|
| Unknown | 4 | ████ |
| arcusmedia | 2 | ██ |
| nightspire | 2 | ██ |
| play | 1 | █ |
| killsec | 1 | █ |
| MisterSam | 1 | █ |
| lynx | 1 | █ |
| funksec | 1 | █ |
| Ghudra | 1 | █ |
| babuk2 | 1 | █ |

## 8. Maturité des preuves

| Maturité de preuve | Fiches | Part |
|---|---:|---:|
| Claim - Unverified | 7 | 46,7 % |
| Claim - Data Sample Published | 4 | 26,7 % |
| Confirmation victime / gouvernement / autorité | 4 | 26,7 % |
| **Total** | **15** | **100 %** |

Les statuts de preuve décrivent le niveau de validation disponible ; ils ne changent pas le type technique de l'incident.

## 9. Chronologie

```mermaid
timeline
    title AFRINTEL - Mars 2025
    02 Mars 2025 : IT-IQ Botswana
    02 Mars 2025 : Workforce Group
    03 Mars 2025 : LINKGROUP
    03 Mars 2025 : synaptic.co.tz
    05 Mars 2025 : Medical Rehabilitation Therapists Board (MRTB)
    07 Mars 2025 : ACDC Express
    07 Mars 2025 : Pam Golding Properties
    11 Mars 2025 : ISEE (International School of Elite Education)
    15 Mars 2025 : Parliament of South Africa
    16 Mars 2025 : Astral Foods Limited
    17 Mars 2025 : Office of the President - John Dramani Mahama X account
    25 Mars 2025 : MISR AL MAHABA HOSPITAL
    26 Mars 2025 : Tableau de bord gouvernemental COVID-19/vaccination
    30 Mars 2025 : INI Investments
    31 Mars 2025 : moh.gov.rw
```

## 10. Analyse CTI mensuelle

### Ransomware

**9 fiches** sont classées Ransomware. Principaux pays : Égypte (3), Afrique du Sud (2), Botswana (1). Une publication sur un leak site ne prouve pas, à elle seule, le chiffrement ou l'exfiltration complète.

### Data Leak

**2 fiches** sont classées Data Leak. Principaux pays : Nigeria (1), Afrique du Sud (1). AFRINTEL distingue les données effectivement observées des volumes globaux revendiqués.

### Access Sale

**1 fiche(s)** relèvent d'Access Sale. Répartition : Burkina Faso (1). Une offre d'accès ne prouve pas automatiquement une exfiltration ou une compromission de l'ensemble de l'infrastructure.

### Account Takeover

**2 Account Takeover** sont documentés. Répartition : Afrique du Sud (1), Ghana (1). Cette catégorie conserve séparément les compromissions de comptes institutionnels.

### System Intrusion

**1 System Intrusion** sont documentées. Répartition : Afrique du Sud (1). Ce type est utilisé lorsqu'un accès ou une tentative d'accès système est établi sans preuve suffisante pour une catégorie plus spécifique.

## 11. Incidents notables

| Pays | Organisation | Type | Statut | Impact | Confiance |
|---|---|---|---|---|---|
| Afrique du Sud | Parliament of South Africa | Account Takeover | Victim Confirmed | Level 4 | Very High |
| Rwanda | moh.gov.rw | Ransomware | Claim - Data Sample Published | Level 4 | Very High |
| Nigeria | Workforce Group | Ransomware | Claim - Data Sample Published | Level 4 | High |
| Afrique du Sud | Pam Golding Properties | Data Leak | Victim Confirmed | Level 3 | Very High |
| Afrique du Sud | Astral Foods Limited | System Intrusion | Victim Confirmed | Level 3 | Very High |

> Ce tableau met en avant jusqu'à cinq fiches selon le niveau d'impact, la confirmation et la confiance structurés. Il ne constitue pas un classement absolu de gravité.

## 12. Principaux enseignements et lacunes de renseignement

- **Concentration géographique :** Afrique du Sud représente 5 fiches (33,3 %), devant Égypte (3) et Nigeria (2).
- **Structure de menace :** Ransomware est le premier type avec 9 fiches, suivi de Data Leak (2).
- **Secteurs :** Gouvernement / Administration (4) et Technologie / IT (3) concentrent la plus forte visibilité.
- **Acteurs :** les labels les plus fréquents sont Unknown (4), arcusmedia (2) et nightspire (2).
- **Preuve :** 11 fiches reposent sur des claims non vérifiés ou accompagnés d'un échantillon ; ces statuts ne valent pas confirmation technique complète.

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

Le mois de **Mars 2025** compte **15 cyberincidents documentés** dans **8 pays africains**. La lecture mensuelle montre que la valeur CTI ne réside pas seulement dans le volume, mais dans la distinction entre **type d'incident, chronologie, niveau de preuve, géographie, secteur et acteur**.

Le rapport conserve ainsi une photographie structurée de la menace observable tout en maintenant les revendications, corroborations, confirmations et inconnues à leur niveau de preuve réel.

👉🏾 [Voir les victimes du mois](./victims_FR.md)

**AFRINTEL** - TLP:CLEAR
