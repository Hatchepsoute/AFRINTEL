[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple) ![Période](https://img.shields.io/badge/Période-2025-blue)

# 🛡️ AFRINTEL | Rapport CTI : Cyberattaques en Afrique
## Période : Septembre 2025 (18 victimes recensées)
👉🏾 [**English version available here**](./README.md)

---

## 1. Introduction
Ce rapport de **Cyber Threat Intelligence (CTI)** présente une analyse détaillée des cyberattaques survenues en Afrique durant le mois de septembre 2025. Les informations sont issues de sources **OSINT** et de sites de fuites de groupes ransomware, compilées dans le cadre du projet **AFRINTEL**. L'objectif est de fournir une vision claire des tendances, des acteurs menaçants et des secteurs ciblés sur le continent.

## 2. Résumé Exécutif
* **Nombre total d'attaques recensées :** 18.
* **Acteurs les plus actifs :** `TheGentlemen` (2 attaques), `killsec` (2 attaques) et `privilege` (2 attaques).
* **Secteurs les plus ciblés :** Administrations publiques, Finance, Assurances, Industrie, Technologies, Télécommunications et Éducation.
* **Volumes de données critiques :** * **Direction Générale des Impôts et des Domaines (Sénégal) :** 1 To de données fiscales exfiltrées.
    * **NSIA Assurances (Côte d'Ivoire) :** 2,5 millions d'enregistrements transactionnels mis en vente.
    * **Université des Frères Mentouri Constantine 1 (Algérie) :** plus de 10 Go de données académiques et personnelles revendiquées exfiltrées.
    * **MobileSub (Nigeria) :** dump SQL de 42 tables couvrant les paiements, la KYC, les transactions et les comptes utilisateurs.
    * **Kolomoni Microfinance Bank (Nigeria) :** fichier CSV de 37 825 lignes contenant des données financières, de contact, démographiques et de connexion.

---

## 3. Statistiques Clés

### 📊 3.1 Répartition par groupe/acteur
| Groupe / Acteur | Nombre d'attaques |
| :--- | :---: |
| **TheGentlemen** | 2 |
| **killsec** | 2 |
| **privilege** | 2 |
| **obscura** | 1 |
| **Tanaka** | 1 |
| **yurei** | 1 |
| **radar** | 1 |
| **qilin** | 1 |
| **warlock** | 1 |
| **arcusmedia** | 1 |
| **blackshrantac** | 1 |
| **KILLUAX** | 1 |
| **Fire Wire** | 1 |
| **Non précisé** | 2 |

### 🏗️ 3.2 Répartition par secteur d'activité
| Secteur | Nombre d'attaques |
| :--- | :---: |
| Administrations publiques | 4 |
| Finance | 4 |
| Assurances | 2 |
| Industrie manufacturière | 2 |
| Technologies | 2 |
| Immobilier / Construction | 1 |
| Restauration / Services alimentaires | 1 |
| Télécommunications | 1 |
| Éducation | 1 |

#### 3.2.1 Top secteurs ciblés
- Finance/Assurances  	[████████████████████] 4
- Administrations     	[████████████████████] 4
- Industrie           	[██████████] 2
- Technologies        	[██████████] 2
- Télécommunications  	[█████] 1
- Éducation           	[█████] 1
- Immobilier / Restauration              	[██████████] 2

```mermaid
pie title Répartition des Secteurs - Septembre 2025
    "Administrations" : 4
    "Finance" : 4
    "Assurances" : 2
    "Industrie" : 2
    "Technologies" : 2
    "Immobilier" : 1
    "Restauration" : 1
    "Télécommunications" : 1
    "Éducation" : 1
```
 
### 🌍 3.3 Répartition par pays
| Pays | Nombre d'attaques |
| :--- | :---: |
| 🇪🇬 Égypte | 3 |
| 🇲🇦 Maroc | 2 |
| 🇳🇬 Nigeria | 4 |
| 🇰🇪 Kenya | 2 |
| 🇩🇿 Algérie | 1 |
| 🇨🇮 Côte d'Ivoire | 1 |
| 🇿🇼 Zimbabwe | 1 |
| 🇳🇦 Namibie | 1 |
| 🇦🇴 Angola | 1 |
| 🇨🇩 RD Congo | 1 |
| 🇸🇳 Sénégal | 1 |
| **Total** | **18** |


```mermaid
graph TD
    subgraph "Répartition des attaques par pays (Septembre 2025)"
    EG[🇪🇬 Égypte: 3] --- Total((Total: 18))
    MA[🇲🇦 Maroc: 2] --- Total
    NG[🇳🇬 Nigeria: 4] --- Total
    KE[🇰🇪 Kenya: 2] --- Total
    DZ[🇩🇿 Algérie: 1] --- Total
    CI[🇨🇮 Côte d'Ivoire: 1] --- Total
    ZW[🇿🇼 Zimbabwe: 1] --- Total
    NA[🇳🇦 Namibie: 1] --- Total
    AO[🇦🇴 Angola: 1] --- Total
    CD[🇨🇩 RD Congo: 1] --- Total
    SN[🇸🇳 Sénégal: 1] --- Total
    end

    style Total fill:#f96,stroke:#333,stroke-width:4px
    style SN fill:#ff9999,stroke:#333
    style CI fill:#ff9999,stroke:#333
```
---


<!-- AFRINTEL_CURRENT_MODEL_START -->
### 3.4 Vue globale standardisée

| Pays | Ransomware | Fuites / accès | Total | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| 🇳🇬 Nigeria | 2 | 2 | 4 | 🟧🟧 🟦🟦 |
| 🇪🇬 Égypte | 2 | 1 | 3 | 🟧🟧 🟦 |
| 🇰🇪 Kenya | 2 | 0 | 2 | 🟧🟧 |
| 🇲🇦 Maroc | 2 | 0 | 2 | 🟧🟧 |
| 🇩🇿 Algérie | 0 | 1 | 1 |  🟦 |
| 🇦🇴 Angola | 0 | 1 | 1 |  🟦 |
| 🇨🇩 RDC | 0 | 1 | 1 |  🟦 |
| 🇨🇮 Côte d’Ivoire | 0 | 1 | 1 |  🟦 |
| 🇳🇦 Namibie | 1 | 0 | 1 | 🟧 |
| 🇸🇳 Sénégal | 1 | 0 | 1 | 🟧 |
| 🇿🇼 Zimbabwe | 1 | 0 | 1 | 🟧 |

```pie
    title Types d’incidents
    "Ransomware" : 11
    "Fuites et accès" : 7
```

### Répartition géographique par région

| Région | Occurrences | Ransomware | Fuites / accès | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| Afrique du Nord | 6 | 4 | 2 | 🟧🟧🟧🟧 🟦🟦 |
| Afrique australe | 2 | 2 | 0 | 🟧🟧 |
| Afrique de l’Ouest et centrale | 8 | 3 | 5 | 🟧🟧🟧 🟦🟦🟦🟦🟦 |
| Afrique de l’Est | 2 | 2 | 0 | 🟧🟧 |

```mermaid
xychart-beta
    title "Occurrences par région"
    x-axis ["1","2","3","4"]
    y-axis "Occurrences" 0 --> 9
    bar [6,2,8,2]
```
Légende : 1 = Afrique du Nord; 2 = Afrique australe; 3 = Afrique de l’Ouest et centrale; 4 = Afrique de l’Est

### Répartition sectorielle

| Secteur | Fiches | Part | Activité |
| :--- | ---: | ---: | :--- |
| Finance / banque | 5 | 27,8% | ██████████ |
| Gouvernement / administration | 5 | 27,8% | ██████████ |
| Technologies / informatique | 4 | 22,2% | ████████ |
| Industrie / fabrication | 2 | 11,1% | ████ |
| Éducation / universités | 1 | 5,6% | ██ |
| Services professionnels | 1 | 5,6% | ██ |

### Acteurs / groupes les plus présents

| Acteur / Groupe | Fiches | Activité |
| :--- | ---: | :--- |
| Not specified | 2 | ██████████ |
| killsec | 2 | ██████████ |
| TheGentlemen | 2 | ██████████ |
| Fire Wire | 1 | █████ |
| KILLUAX | 1 | █████ |
| Tanaka | 1 | █████ |
| arcusmedia | 1 | █████ |
| blackshrantac | 1 | █████ |
| obscura | 1 | █████ |
| privilege | 1 | █████ |
<!-- AFRINTEL_CURRENT_MODEL_END -->
## 4. Détail des attaques par groupe/acteur

#### 4.1 TheGentlemen (2 attaques)
* **09/09/2025 : Dolidol (Maroc)** - Secteur Industrie Manufacturière. Revendication et divulgation des données.
* **09/09/2025 : Proplastics Limited (Zimbabwe)** - Secteur Industrie (Plastiques). Revendication et divulgation des données.
> **Note CTI :** Le groupe a frappé deux cibles industrielles majeures dans deux zones géographiques distinctes le même jour, démontrant une planification coordonnée.

#### 4.2 killsec (2 attaques)
* **10/09/2025 : Princeps Credit Systems Limited (Nigeria)** - Secteur Finance. Revendication et divulgation.
* **22/09/2025 : Fractalite (Maroc)** - Secteur Technologies / Services Numériques. Revendication et divulgation.

#### 4.3 obscura (1 attaque)
* **05/09/2025 : MeamarGroup (Égypte)** - Secteur Immobilier / Construction. Revendication et divulgation.

#### 4.4 Tanaka (1 attaque)
* **06/09/2025 : NSIA Assurances (Côte d'Ivoire)** - Secteur Assurances / Finance. Fuite massive de **2,5 millions d'enregistrements** transactionnels et mise en vente.

#### 4.5 yurei (1 attaque)
* **08/09/2025 : The Promise Nigeria (Nigeria)** - Secteur Restauration / Traiteur. Revendication et divulgation.

#### 4.6 radar (1 attaque)
* **11/09/2025 : Epia Financial Services (Namibie)** - Secteur Services Financiers. Revendication et divulgation.

#### 4.7 qilin (1 attaque)
* **14/09/2025 : Office of the Registrar of Political Parties (Kenya)** - Secteur Administrations Publiques. Revendication et divulgation.

#### 4.8 warlock (1 attaque)
* **16/09/2025 : Jubilee Life Insurance (Kenya)** - Secteur Assurances / Finance. Revendication et divulgation.

#### 4.9 arcusmedia (1 attaque)
* **17/09/2025 : Accflex ERP (Égypte)** - Secteur Technologies / Édition de logiciels. Revendication et divulgation.

#### 4.10 BlackShrantac (1 attaque)
* **29/09/2025 : Direction Générale des Impôts et des Domaines (Sénégal)** - Secteur Administration Fiscale. Exfiltration massive de **1 To de données sensibles** (bases fiscales, registres fonciers, informations bancaires).

#### 4.11 Non attribué (1 attaque)
* **30/09/2025 : Telecom Egypt / TE Data (Égypte)** - Secteur Télécommunications. Claim - Data Sample Published. Échantillon réduit (36 enregistrements) de données de session/comptabilité RADIUS abonnés (identifiants, IP de NAS, adresse MAC, IP attribuée, horodatages de session), aucun acteur revendicateur identifié.

#### 4.12 Fire Wire (1 attaque)
* **02/09/2025 : Université des Frères Mentouri Constantine 1 (Algérie)** - Secteur Éducation / Enseignement supérieur. Claim - Data Sample Published. Plus de 10 Go revendiqués exfiltrés : plannings d'examens de Master 2, plus de 200 dossiers étudiants détaillés (identité + notes), un annuaire de contacts de conformité véhicules et un modèle de contacts de conférence.

#### 4.13 Non précisé (2 attaques)
* **04/09/2025 : MobileSub (Nigeria)** - Fintech / Services de paiement. Claim - Data Sample Published ; dump SQL de 42 tables.
* **24/09/2025 : Kolomoni Microfinance Bank (Nigeria)** - Microfinance / Banque. Claim - Data Sample Published ; CSV de 37 825 lignes.

### 4.14 Acteur → victime → pays

```mermaid
graph LR

A1[TheGentlemen] --> V1[Dolidol]
V1 --> P1[Maroc]

A1 --> V2[Proplastics Limited]
V2 --> P2[Zimbabwe]

A2[killsec] --> V3[Princeps Credit Systems]
V3 --> P3[Nigeria]

A2 --> V4[Fractalite]
V4 --> P1

A3[obscura] --> V5[MeamarGroup]
V5 --> P4[Égypte]

A4[Tanaka] --> V6[NSIA Assurances]
V6 --> P5[Côte d'Ivoire]

A5[yurei] --> V7[The Promise Nigeria]
V7 --> P3

A6[radar] --> V8[Epia Financial Services]
V8 --> P6[Namibie]

A7[qilin] --> V9[Office of the Registrar of Political Parties]
V9 --> P7[Kenya]

A8[warlock] --> V10[Jubilee Life Insurance]
V10 --> P7

A9[arcusmedia] --> V11[Accflex ERP]
V11 --> P4

A10[BlackShrantac] --> V12[DGID Sénégal]
V12 --> P8[Sénégal]

A11[Non attribué] --> V13[Telecom Egypt / TE Data]
V13 --> P4

A12[Fire Wire] --> V14[Université Mentouri Constantine 1]
V14 --> P9[Algérie]

classDef actor fill:#8b0000,color:#fff,stroke:#5c0000,stroke-width:1px;
classDef victim fill:#0b5394,color:#fff,stroke:#073763,stroke-width:1px;
classDef country fill:#38761d,color:#fff,stroke:#274e13,stroke-width:1px;

class A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12 actor;
class V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14 victim;
class P1,P2,P3,P4,P5,P6,P7,P8,P9 country;
```
---

## 5. TTPs Observées (Tactiques, Techniques & Procédures)
* **Exfiltration Massive :** Capacité à collecter et exfiltrer des volumes dépassant le téraoctet (DGID) ou des millions de lignes de données (NSIA).
* **Double Extorsion & Monétisation :** Mise en vente systématique des données sur des forums clandestins pour forcer le paiement (ex: Tanaka).
* **Ciblage d'Infrastructures d'État :** Recrudescence des attaques contre les organismes de régulation et les ministères financiers.
* **Agilité Géo-Opérationnelle :** Capacité de certains groupes à mener des attaques simultanées dans différentes régions du continent (ex: TheGentlemen).

## 6. Recommandations
1.  **Gouvernance des Données :** Pour les administrations publiques, prioriser le chiffrement des bases de données sensibles et les sauvegardes hors ligne.
2.  **Segmentation Réseau :** Isoler les systèmes de gestion de paie et les registres clients des réseaux exposés à Internet.
3.  **Hygiène Cyber :** Généralisation de l'authentification multi-facteurs (MFA) et audits réguliers des accès tiers (VPN/ERP).

---

## 7. Conclusion
Le mois de septembre 2025 confirme que l'Afrique est un terrain d'opération majeur pour les groupes ransomware et les acteurs de fuite de données. La diversité des acteurs (11 groupes nommés et un cas de fuite non attribué) et l'ampleur des exfiltrations (DGID, NSIA, UMC1) appellent à une vigilance accrue et à un partage d'intelligence (CTI) renforcé entre les pays du continent.

---

### ✍🏿 Auteur
**Adama ASSIONGBON**
*Consultant SOC & Cyber Threat Intelligence*
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon/)

---
*Initiative ouverte de veille CTI sur l’Afrique - AFRINTEL*
