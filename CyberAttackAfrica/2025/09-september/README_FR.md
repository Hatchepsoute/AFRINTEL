# Rapport CTI AFRINTEL - Cybermenaces en Afrique - Septembre 2025

👉🏾 [English version](./README.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Period-September%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Synthèse exécutive

En Septembre 2025, AFRINTEL documente **19 cyberincidents** affectant des organisations et services numériques dans **11 pays africains**.

Le paysage est dominé par **Ransomware avec 11 fiches (57,9 %)**, suivi de **Data Leak avec 7 (36,8 %)**. Les autres types observés sont DDoS 1.

La concentration géographique est marquée : **Nigeria (4)**, **Maroc (3)**, **Égypte (3)** représentent ensemble **10 fiches, soit 52,6 % du mois**. Cette concentration doit être interprétée comme la visibilité du corpus AFRINTEL et non comme un taux national exhaustif de compromission.

Sur le plan sectoriel, les catégories les plus représentées sont **Gouvernement / Administration (5)**, **Finance / Banque (5)**, **Non précisé (2)**. Les labels d'acteurs les plus fréquents sont `Not specified` (2), `TheGentlemen` (2), `killsec` (2). `Unknown`, lorsqu'il apparaît, désigne une absence d'attribution et non un groupe cybercriminel.

La maturité des preuves reste variable : **17 fiches** relèvent de claims non vérifiés ou accompagnés d'échantillons. AFRINTEL conserve une séparation stricte entre **faits observés, revendications, corroborations, confirmations officielles et inconnues techniques**.

Par rapport à Août, le volume mensuel **augmente de 3 fiches**. Les variations les plus visibles concernent Ransomware 7->11 (+4), Data Leak 5->7 (+2), Access Sale 2->0 (-2).

> **Note de lecture :** les chiffres AFRINTEL décrivent les incidents documentés et la visibilité des menaces observées. Ils ne constituent pas une mesure exhaustive de toutes les cyberattaques réellement survenues en Afrique.

### 1.1 Comparaison avec le mois précédent

| Indicateur | Août 2025 | Septembre 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 16 | 19 | **+3 (+18,8 %)** |
| Ransomware | 7 | 11 | **+4 (+57,1 %)** |
| Data Leak | 5 | 7 | **+2 (+40,0 %)** |
| Access Sale | 2 | 0 | **-2 (-100,0 %)** |
| DDoS | 1 | 1 | **Stable** |
| Defacement | 1 | 0 | **-1 (-100,0 %)** |
| Account Takeover | 0 | 0 | **Stable** |
| System Intrusion | 0 | 0 | **Stable** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |




## 2. Méthodologie

- **Périmètre :** 54 pays africains ; période de référence : Septembre 2025.
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
| Incidents documentés | **19** |
| Pays représentés | **11** |
| Régions représentées | **5** |
| Premier pays | **Nigeria (4)** |
| Premier secteur | **Gouvernement / Administration (5)** |
| Premier label acteur | **Not specified (2)** |

| Type d'incident | Fiches | Part |
|---|---:|---:|
| Ransomware | 11 | 57,9 % |
| Data Leak | 7 | 36,8 % |
| Access Sale | 0 | 0,0 % |
| DDoS | 1 | 5,3 % |
| Defacement | 0 | 0,0 % |
| Account Takeover | 0 | 0,0 % |
| System Intrusion | 0 | 0,0 % |
| Malware | 0 | 0,0 % |
| Operational Fraud | 0 | 0,0 % |
| **Total** | **19** | **100 %** |

```mermaid
pie showData
    title Types d'incident - Septembre 2025
    "Ransomware" : 11
    "Data Leak" : 7
    "DDoS" : 1
```

## 4. Répartition géographique

| Pays | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Nigeria | **4** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| Maroc | **3** | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Égypte | **3** | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kenya | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Algérie | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Côte d'Ivoire | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zimbabwe | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Namibie | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Angola | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Congo (RDC) | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Sénégal | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **19** | **11** | **7** | **0** | **1** | **0** | **0** | **0** | **0** |

> `Operational Fraud = 0` ce mois-ci ; la colonne est omise pour préserver la lisibilité.

## 5. Répartition régionale

| Région | Fiches | Part |
|---|---:|---:|
| Afrique du Nord | 7 | 36,8 % |
| Afrique de l'Ouest | 6 | 31,6 % |
| Afrique australe | 3 | 15,8 % |
| Afrique de l'Est | 2 | 10,5 % |
| Afrique centrale | 1 | 5,3 % |
| **Total** | **19** | **100 %** |

La région la plus représentée est **Afrique du Nord avec 7 fiches (36,8 %)**.

## 6. Impact sectoriel

| Secteur | Fiches | Part | Activité |
|---|---:|---:|---|
| Gouvernement / Administration | 5 | 26,3 % | █████ |
| Finance / Banque | 5 | 26,3 % | █████ |
| Non précisé | 2 | 10,5 % | ██ |
| Industrie / Fabrication | 2 | 10,5 % | ██ |
| Technologie / IT | 2 | 10,5 % | ██ |
| Éducation / Université | 1 | 5,3 % | █ |
| Construction / Immobilier | 1 | 5,3 % | █ |
| Télécommunications | 1 | 5,3 % | █ |
| **Total** | **19** | **100 %** | |

## 7. Acteurs / groupes

`Unknown` correspond à une absence d'attribution, pas à un acteur.

| Acteur / Groupe | Fiches | Activité |
|---|---:|---|
| Not specified | 2 | ██ |
| TheGentlemen | 2 | ██ |
| killsec | 2 | ██ |
| privilege | 2 | ██ |
| Fire Wire | 1 | █ |
| Keymous (claim) | 1 | █ |
| obscura | 1 | █ |
| Tanaka | 1 | █ |
| yurei | 1 | █ |
| radar | 1 | █ |
| qilin | 1 | █ |
| warlock | 1 | █ |
| arcusmedia | 1 | █ |
| BlackShrantac | 1 | █ |
| KILLUAX | 1 | █ |

## 8. Maturité des preuves

| Maturité de preuve | Fiches | Part |
|---|---:|---:|
| Claim - Unverified | 10 | 52,6 % |
| Claim - Data Sample Published | 7 | 36,8 % |
| Data Fully Published | 1 | 5,3 % |
| Corroboré / preuve secondaire | 1 | 5,3 % |
| **Total** | **19** | **100 %** |

Les statuts de preuve décrivent le niveau de validation disponible ; ils ne changent pas le type technique de l'incident.

## 9. Chronologie

```mermaid
timeline
    title AFRINTEL - Septembre 2025
    02 Septembre 2025 : Université des Frères Mentouri Constantine 1 (UMC1)
    03 Septembre 2025 : Government portals + Maroc Telecom (campaign)
    04 Septembre 2025 : MobileSub
    05 Septembre 2025 : MeamarGroup
    06 Septembre 2025 : NSIA Assurances
    08 Septembre 2025 : The Promise Nigeria
    09 Septembre 2025 : Dolidol
    09 Septembre 2025 : Proplastics Limited
    10 Septembre 2025 : Princeps Credit Systems Limited
    11 Septembre 2025 : Epia Financial Services
    11 Septembre 2025 : Base de données des employés du gouvernement angolais (pape.gov.ao)
    12 Septembre 2025 : Fonds pour la Réforme de l'Administration Publique (FRAP)
    14 Septembre 2025 : Office Of The Registrar Of Political Parties
    16 Septembre 2025 : Jubilee Life Insurance
    17 Septembre 2025 : Accflex ERP
    22 Septembre 2025 : Fractalite (fractalite.com)
    24 Septembre 2025 : Kolomoni Microfinance Bank
    29 Septembre 2025 : Direction Générale des Impôts et des Domaines (DGID)
    30 Septembre 2025 : Telecom Egypt (TE Data)
```

## 10. Analyse CTI mensuelle

### Ransomware

**11 fiches** sont classées Ransomware. Principaux pays : Égypte (2), Nigeria (2), Maroc (2). Une publication sur un leak site ne prouve pas, à elle seule, le chiffrement ou l'exfiltration complète.

### Data Leak

**7 fiches** sont classées Data Leak. Principaux pays : Nigeria (2), Algérie (1), Côte d'Ivoire (1). AFRINTEL distingue les données effectivement observées des volumes globaux revendiqués.

### DDoS

**1 campagne(s)** DDoS sont documentées. Répartition : Maroc (1). Le comptage porte sur les campagnes et non nécessairement sur chaque domaine ciblé.

## 11. Incidents notables

| Pays | Organisation | Type | Statut | Impact | Confiance |
|---|---|---|---|---|---|
| Namibie | Epia Financial Services | Ransomware | Claim - Data Sample Published | Level 4 | High |
| Maroc | Government portals + Maroc Telecom (campaign) | DDoS | Claim - OSINT Availability Evidence | Level 4 | Medium |
| Égypte | MeamarGroup | Ransomware | Claim - Data Sample Published | Level 3 | Very High |
| Nigeria | MobileSub | Data Leak | Claim - Data Sample Published | Level 3 | Medium |
| Nigeria | Kolomoni Microfinance Bank | Data Leak | Claim - Data Sample Published | Level 3 | Medium |

> Ce tableau met en avant jusqu'à cinq fiches selon le niveau d'impact, la confirmation et la confiance structurés. Il ne constitue pas un classement absolu de gravité.

## 12. Principaux enseignements et lacunes de renseignement

- **Concentration géographique :** Nigeria représente 4 fiches (21,1 %), devant Maroc (3) et Égypte (3).
- **Structure de menace :** Ransomware est le premier type avec 11 fiches, suivi de Data Leak (7).
- **Secteurs :** Gouvernement / Administration (5) et Finance / Banque (5) concentrent la plus forte visibilité.
- **Acteurs :** les labels les plus fréquents sont Not specified (2), TheGentlemen (2) et killsec (2).
- **Preuve :** 17 fiches reposent sur des claims non vérifiés ou accompagnés d'un échantillon ; ces statuts ne valent pas confirmation technique complète.

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

Le mois de **Septembre 2025** compte **19 cyberincidents documentés** dans **11 pays africains**. La lecture mensuelle montre que la valeur CTI ne réside pas seulement dans le volume, mais dans la distinction entre **type d'incident, chronologie, niveau de preuve, géographie, secteur et acteur**.

Le rapport conserve ainsi une photographie structurée de la menace observable tout en maintenant les revendications, corroborations, confirmations et inconnues à leur niveau de preuve réel.

👉🏾 [Voir les victimes du mois](./victims_FR.md)

**AFRINTEL** - TLP:CLEAR
