# Rapport CTI AFRINTEL - Cybermenaces en Afrique - Février 2025

👉🏾 [English version](./README.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Period-February%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Synthèse exécutive

En Février 2025, AFRINTEL documente **10 cyberincidents** affectant des organisations et services numériques dans **7 pays africains**.

Le paysage est dominé par **Ransomware avec 8 fiches (80,0 %)**, suivi de **Account Takeover avec 2 (20,0 %)**.

La concentration géographique est marquée : **Égypte (3)**, **Kenya (2)**, **Maroc (1)** représentent ensemble **6 fiches, soit 60,0 % du mois**. Cette concentration doit être interprétée comme la visibilité du corpus AFRINTEL et non comme un taux national exhaustif de compromission.

Sur le plan sectoriel, les catégories les plus représentées sont **Gouvernement / Administration (2)**, **Finance / Banque (2)**, **Technologie / IT (1)**. Les labels d'acteurs les plus fréquents sont `Unknown` (2), `ransomhub` (2), `killsec` (2). `Unknown`, lorsqu'il apparaît, désigne une absence d'attribution et non un groupe cybercriminel.

La maturité des preuves reste variable : **8 fiches** relèvent de claims non vérifiés ou accompagnés d'échantillons. AFRINTEL conserve une séparation stricte entre **faits observés, revendications, corroborations, confirmations officielles et inconnues techniques**.

Par rapport à Janvier, le volume mensuel **diminue de 9 fiches**. Les variations les plus visibles concernent Ransomware 16->8 (-8), Data Leak 2->0 (-2), Account Takeover 1->2 (+1).

> **Note de lecture :** les chiffres AFRINTEL décrivent les incidents documentés et la visibilité des menaces observées. Ils ne constituent pas une mesure exhaustive de toutes les cyberattaques réellement survenues en Afrique.

### 1.1 Comparaison avec le mois précédent

| Indicateur | Janvier 2025 | Février 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 19 | 10 | **-9 (-47,4 %)** |
| Ransomware | 16 | 8 | **-8 (-50,0 %)** |
| Data Leak | 2 | 0 | **-2 (-100,0 %)** |
| Access Sale | 0 | 0 | **Stable** |
| DDoS | 0 | 0 | **Stable** |
| Defacement | 0 | 0 | **Stable** |
| Account Takeover | 1 | 2 | **+1 (+100,0 %)** |
| System Intrusion | 0 | 0 | **Stable** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |




## 2. Méthodologie

- **Périmètre :** 54 pays africains ; période de référence : Février 2025.
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
| Incidents documentés | **10** |
| Pays représentés | **7** |
| Régions représentées | **4** |
| Premier pays | **Égypte (3)** |
| Premier secteur | **Gouvernement / Administration (2)** |
| Premier label acteur | **Unknown (2)** |

| Type d'incident | Fiches | Part |
|---|---:|---:|
| Ransomware | 8 | 80,0 % |
| Data Leak | 0 | 0,0 % |
| Access Sale | 0 | 0,0 % |
| DDoS | 0 | 0,0 % |
| Defacement | 0 | 0,0 % |
| Account Takeover | 2 | 20,0 % |
| System Intrusion | 0 | 0,0 % |
| Malware | 0 | 0,0 % |
| Operational Fraud | 0 | 0,0 % |
| **Total** | **10** | **100 %** |

```mermaid
pie showData
    title Types d'incident - Février 2025
    "Ransomware" : 8
    "Account Takeover" : 2
```

## 4. Répartition géographique

| Pays | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Égypte | **3** | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kenya | **2** | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| Maroc | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Afrique du Sud | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zambie | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ghana | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Namibie | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **10** | **8** | **0** | **0** | **0** | **0** | **2** | **0** | **0** |

> `Operational Fraud = 0` ce mois-ci ; la colonne est omise pour préserver la lisibilité.

## 5. Répartition régionale

| Région | Fiches | Part |
|---|---:|---:|
| Afrique du Nord | 4 | 40,0 % |
| Afrique australe | 3 | 30,0 % |
| Afrique de l'Est | 2 | 20,0 % |
| Afrique de l'Ouest | 1 | 10,0 % |
| **Total** | **10** | **100 %** |

La région la plus représentée est **Afrique du Nord avec 4 fiches (40,0 %)**.

## 6. Impact sectoriel

| Secteur | Fiches | Part | Activité |
|---|---:|---:|---|
| Gouvernement / Administration | 2 | 20,0 % | ██ |
| Finance / Banque | 2 | 20,0 % | ██ |
| Technologie / IT | 1 | 10,0 % | █ |
| Médias / Divertissement | 1 | 10,0 % | █ |
| Non précisé | 1 | 10,0 % | █ |
| Télécommunications | 1 | 10,0 % | █ |
| Transport / Logistique | 1 | 10,0 % | █ |
| Services professionnels / Business | 1 | 10,0 % | █ |
| **Total** | **10** | **100 %** | |

## 7. Acteurs / groupes

`Unknown` correspond à une absence d'attribution, pas à un acteur.

| Acteur / Groupe | Fiches | Activité |
|---|---:|---|
| Unknown | 2 | ██ |
| ransomhub | 2 | ██ |
| killsec | 2 | ██ |
| fog | 1 | █ |
| flocker | 1 | █ |
| akira | 1 | █ |
| hunter | 1 | █ |

## 8. Maturité des preuves

| Maturité de preuve | Fiches | Part |
|---|---:|---:|
| Claim - Unverified | 5 | 50,0 % |
| Claim - Data Sample Published | 3 | 30,0 % |
| Confirmation victime / gouvernement / autorité | 2 | 20,0 % |
| **Total** | **10** | **100 %** |

Les statuts de preuve décrivent le niveau de validation disponible ; ils ne changent pas le type technique de l'incident.

## 9. Chronologie

```mermaid
timeline
    title AFRINTEL - Février 2025
    03 Février 2025 : Xlab Group
    06 Février 2025 : K24 TV
    09 Février 2025 : Directorate of Criminal Investigations (DCI)
    12 Février 2025 : ASK Gras Savoye (askgs.ma)
    12 Février 2025 : South African Weather Service (SAWS)
    19 Février 2025 : Government Services Portal (services.gov.zm)
    19 Février 2025 : Brolly
    21 Février 2025 : Paratus
    22 Février 2025 : SPEED Co
    23 Février 2025 : Shaghalni
```

## 10. Analyse CTI mensuelle

### Ransomware

**8 fiches** sont classées Ransomware. Principaux pays : Égypte (3), Maroc (1), Afrique du Sud (1). Une publication sur un leak site ne prouve pas, à elle seule, le chiffrement ou l'exfiltration complète.

### Account Takeover

**2 Account Takeover** sont documentés. Répartition : Kenya (2). Cette catégorie conserve séparément les compromissions de comptes institutionnels.

## 11. Incidents notables

| Pays | Organisation | Type | Statut | Impact | Confiance |
|---|---|---|---|---|---|
| Kenya | Directorate of Criminal Investigations (DCI) | Account Takeover | Victim Confirmed | Level 4 | Very High |
| Kenya | K24 TV | Account Takeover | Victim Confirmed | Level 3 | High |
| Égypte | Shaghalni | Ransomware | Claim - Data Sample Published | Level 3 | High |
| Égypte | Xlab Group | Ransomware | Claim - Unverified | N/A | N/A |
| Maroc | ASK Gras Savoye (askgs.ma) | Ransomware | Claim - Unverified | N/A | N/A |

> Ce tableau met en avant jusqu'à cinq fiches selon le niveau d'impact, la confirmation et la confiance structurés. Il ne constitue pas un classement absolu de gravité.

## 12. Principaux enseignements et lacunes de renseignement

- **Concentration géographique :** Égypte représente 3 fiches (30,0 %), devant Kenya (2) et Maroc (1).
- **Structure de menace :** Ransomware est le premier type avec 8 fiches, suivi de Account Takeover (2).
- **Secteurs :** Gouvernement / Administration (2) et Finance / Banque (2) concentrent la plus forte visibilité.
- **Acteurs :** les labels les plus fréquents sont Unknown (2), ransomhub (2) et killsec (2).
- **Preuve :** 8 fiches reposent sur des claims non vérifiés ou accompagnés d'un échantillon ; ces statuts ne valent pas confirmation technique complète.

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

Le mois de **Février 2025** compte **10 cyberincidents documentés** dans **7 pays africains**. La lecture mensuelle montre que la valeur CTI ne réside pas seulement dans le volume, mais dans la distinction entre **type d'incident, chronologie, niveau de preuve, géographie, secteur et acteur**.

Le rapport conserve ainsi une photographie structurée de la menace observable tout en maintenant les revendications, corroborations, confirmations et inconnues à leur niveau de preuve réel.

👉🏾 [Voir les victimes du mois](./victims_FR.md)

**AFRINTEL** - TLP:CLEAR
