# Rapport CTI AFRINTEL - Cybermenaces en Afrique - Avril 2025

👉🏾 [English version](./README.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Period-April%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Synthèse exécutive

En Avril 2025, AFRINTEL documente **20 cyberincidents** affectant des organisations et services numériques dans **8 pays africains**.

Le paysage est dominé par **Data Leak avec 10 fiches (50,0 %)**, suivi de **Ransomware avec 7 (35,0 %)**. Les autres types observés sont Access Sale 2, DDoS 1.

La concentration géographique est marquée : **Maroc (6)**, **Égypte (5)**, **Algérie (3)** représentent ensemble **14 fiches, soit 70,0 % du mois**. Cette concentration doit être interprétée comme la visibilité du corpus AFRINTEL et non comme un taux national exhaustif de compromission.

Sur le plan sectoriel, les catégories les plus représentées sont **Gouvernement / Administration (6)**, **Finance / Banque (4)**, **Technologie / IT (2)**. Les labels d'acteurs les plus fréquents sont `Phantom Atlas` (3), `Jabaroot DZ` (2), `Unknown` (2). `Unknown`, lorsqu'il apparaît, désigne une absence d'attribution et non un groupe cybercriminel.

La maturité des preuves reste variable : **18 fiches** relèvent de claims non vérifiés ou accompagnés d'échantillons. AFRINTEL conserve une séparation stricte entre **faits observés, revendications, corroborations, confirmations officielles et inconnues techniques**.

Par rapport à Mars, le volume mensuel **augmente de 5 fiches**. Les variations les plus visibles concernent Data Leak 2->10 (+8), Ransomware 9->7 (-2), Account Takeover 2->0 (-2).

> **Note de lecture :** les chiffres AFRINTEL décrivent les incidents documentés et la visibilité des menaces observées. Ils ne constituent pas une mesure exhaustive de toutes les cyberattaques réellement survenues en Afrique.

### 1.1 Comparaison avec le mois précédent

| Indicateur | Mars 2025 | Avril 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 15 | 20 | **+5 (+33,3 %)** |
| Ransomware | 9 | 7 | **-2 (-22,2 %)** |
| Data Leak | 2 | 10 | **+8 (+400,0 %)** |
| Access Sale | 1 | 2 | **+1 (+100,0 %)** |
| DDoS | 0 | 1 | **+1 (nouveau)** |
| Defacement | 0 | 0 | **Stable** |
| Account Takeover | 2 | 0 | **-2 (-100,0 %)** |
| System Intrusion | 1 | 0 | **-1 (-100,0 %)** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |




## 2. Méthodologie

- **Périmètre :** 54 pays africains ; période de référence : Avril 2025.
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
| Incidents documentés | **20** |
| Pays représentés | **8** |
| Régions représentées | **3** |
| Premier pays | **Maroc (6)** |
| Premier secteur | **Gouvernement / Administration (6)** |
| Premier label acteur | **Phantom Atlas (3)** |

| Type d'incident | Fiches | Part |
|---|---:|---:|
| Ransomware | 7 | 35,0 % |
| Data Leak | 10 | 50,0 % |
| Access Sale | 2 | 10,0 % |
| DDoS | 1 | 5,0 % |
| Defacement | 0 | 0,0 % |
| Account Takeover | 0 | 0,0 % |
| System Intrusion | 0 | 0,0 % |
| Malware | 0 | 0,0 % |
| Operational Fraud | 0 | 0,0 % |
| **Total** | **20** | **100 %** |

```mermaid
pie showData
    title Types d'incident - Avril 2025
    "Ransomware" : 7
    "Data Leak" : 10
    "Access Sale" : 2
    "DDoS" : 1
```

## 4. Répartition géographique

| Pays | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Maroc | **6** | 0 | 4 | 1 | 1 | 0 | 0 | 0 | 0 |
| Égypte | **5** | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Algérie | **3** | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| Afrique du Sud | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Sénégal | **1** | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Mauritanie | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tunisie | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ghana | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **20** | **7** | **10** | **2** | **1** | **0** | **0** | **0** | **0** |

> `Operational Fraud = 0` ce mois-ci ; la colonne est omise pour préserver la lisibilité.

## 5. Répartition régionale

| Région | Fiches | Part |
|---|---:|---:|
| Afrique du Nord | 15 | 75,0 % |
| Afrique de l'Ouest | 3 | 15,0 % |
| Afrique australe | 2 | 10,0 % |
| **Total** | **20** | **100 %** |

La région la plus représentée est **Afrique du Nord avec 15 fiches (75,0 %)**.

## 6. Impact sectoriel

| Secteur | Fiches | Part | Activité |
|---|---:|---:|---|
| Gouvernement / Administration | 6 | 30,0 % | ██████ |
| Finance / Banque | 4 | 20,0 % | ████ |
| Technologie / IT | 2 | 10,0 % | ██ |
| Télécommunications | 2 | 10,0 % | ██ |
| Défense / Sécurité | 1 | 5,0 % | █ |
| Services professionnels / Business | 1 | 5,0 % | █ |
| Éducation / Université | 1 | 5,0 % | █ |
| Agriculture / Agro-industrie | 1 | 5,0 % | █ |
| Industrie / Fabrication | 1 | 5,0 % | █ |
| Santé / Médical | 1 | 5,0 % | █ |
| **Total** | **20** | **100 %** | |

## 7. Acteurs / groupes

`Unknown` correspond à une absence d'attribution, pas à un acteur.

| Acteur / Groupe | Fiches | Activité |
|---|---:|---|
| Phantom Atlas | 3 | ███ |
| Jabaroot DZ | 2 | ██ |
| Unknown | 2 | ██ |
| devman | 2 | ██ |
| oblivion666 | 1 | █ |
| dragonforce | 1 | █ |
| ransomhouse | 1 | █ |
| crypto24 | 1 | █ |
| yn0x1 | 1 | █ |
| Killer_Bee | 1 | █ |
| p4xar | 1 | █ |
| B4baYega | 1 | █ |
| nightspire | 1 | █ |
| cicada3301 | 1 | █ |
| gunra | 1 | █ |

## 8. Maturité des preuves

| Maturité de preuve | Fiches | Part |
|---|---:|---:|
| Claim - Unverified | 9 | 45,0 % |
| Claim - Data Sample Published | 9 | 45,0 % |
| Confirmation victime / gouvernement / autorité | 1 | 5,0 % |
| Corroboré / preuve secondaire | 1 | 5,0 % |
| **Total** | **20** | **100 %** |

Les statuts de preuve décrivent le niveau de validation disponible ; ils ne changent pas le type technique de l'incident.

## 9. Chronologie

```mermaid
timeline
    title AFRINTEL - Avril 2025
    04 Avril 2025 : Forces Armées Sénégalaises (armee.sn)
    06 Avril 2025 : IACC Holdings
    07 Avril 2025 : Cell C
    08 Avril 2025 : International Busines Service
    08 Avril 2025 : CNSS (Caisse Nationale de Sécurité Sociale)
    08 Avril 2025 : Ministère de l'Industrie et du Commerce (miepeec.gov.ma)
    08 Avril 2025 : CNAS (Caisse Nationale des Assurances Sociales des Travailleurs Salariés)
    08 Avril 2025 : Maroc Telecom
    09 Avril 2025 : MGPTT / Mutuelle Générale des Travailleurs de la Poste et des Télécoms
    09 Avril 2025 : Ministère du Travail
    12 Avril 2025 : Moroccan government portals (coordinated campaign)
    13 Avril 2025 : BMI / SEDAD Mobile Wallet
    13 Avril 2025 : Tawasol
    13 Avril 2025 : Institut Supérieur des Métiers de l’Audiovisuel et du Cinéma (ISMAC)
    13 Avril 2025 : Ministère de l'Habitat et de la Politique de la Ville (mhpv.gov.ma)
    17 Avril 2025 : INI Investments
    20 Avril 2025 : Premier Meats South Africa
    22 Avril 2025 : Natilait
    23 Avril 2025 : Dar Al Teb
    Avril 2025 - date exacte de compromission non communiquée publiquement : MTN Group / MTN Ghana
```

## 10. Analyse CTI mensuelle

### Ransomware

**7 fiches** sont classées Ransomware. Principaux pays : Égypte (4), Afrique du Sud (2), Tunisie (1). Une publication sur un leak site ne prouve pas, à elle seule, le chiffrement ou l'exfiltration complète.

### Data Leak

**10 fiches** sont classées Data Leak. Principaux pays : Maroc (4), Algérie (3), Mauritanie (1). AFRINTEL distingue les données effectivement observées des volumes globaux revendiqués.

### Access Sale

**2 fiche(s)** relèvent d'Access Sale. Répartition : Sénégal (1), Maroc (1). Une offre d'accès ne prouve pas automatiquement une exfiltration ou une compromission de l'ensemble de l'infrastructure.

### DDoS

**1 campagne(s)** DDoS sont documentées. Répartition : Maroc (1). Le comptage porte sur les campagnes et non nécessairement sur chaque domaine ciblé.

## 11. Incidents notables

| Pays | Organisation | Type | Statut | Impact | Confiance |
|---|---|---|---|---|---|
| Ghana | MTN Group / MTN Ghana | Data Leak | Victim Confirmed | Level 4 | Very High |
| Maroc | Moroccan government portals (coordinated campaign) | DDoS | Incident Corroborated - Attribution Unconfirmed | Level 4 | High |
| Afrique du Sud | Cell C | Ransomware | Claim - Data Sample Published | Level 4 | High |
| Égypte | Dar Al Teb | Ransomware | Claim - Data Sample Published | Level 4 | High |
| Maroc | Maroc Telecom | Access Sale | Claim - Unverified | Level 3 | Medium |

> Ce tableau met en avant jusqu'à cinq fiches selon le niveau d'impact, la confirmation et la confiance structurés. Il ne constitue pas un classement absolu de gravité.

## 12. Principaux enseignements et lacunes de renseignement

- **Concentration géographique :** Maroc représente 6 fiches (30,0 %), devant Égypte (5) et Algérie (3).
- **Structure de menace :** Data Leak est le premier type avec 10 fiches, suivi de Ransomware (7).
- **Secteurs :** Gouvernement / Administration (6) et Finance / Banque (4) concentrent la plus forte visibilité.
- **Acteurs :** les labels les plus fréquents sont Phantom Atlas (3), Jabaroot DZ (2) et Unknown (2).
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

Le mois de **Avril 2025** compte **20 cyberincidents documentés** dans **8 pays africains**. La lecture mensuelle montre que la valeur CTI ne réside pas seulement dans le volume, mais dans la distinction entre **type d'incident, chronologie, niveau de preuve, géographie, secteur et acteur**.

Le rapport conserve ainsi une photographie structurée de la menace observable tout en maintenant les revendications, corroborations, confirmations et inconnues à leur niveau de preuve réel.

👉🏾 [Voir les victimes du mois](./victims_FR.md)

**AFRINTEL** - TLP:CLEAR
