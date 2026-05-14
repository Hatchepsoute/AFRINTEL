[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# 🛡️ AFRINTEL | CTI Report: Cyberattacks in Africa
## Period: September 2025 (12 documented victims)
👉🏾 [**French version available here**](./README_FR.md)

---

## 1. Introduction
This **Cyber Threat Intelligence (CTI)** report provides a detailed analysis of cyberattacks that occurred across Africa in September 2025. The data is compiled from **OSINT** sources and ransomware group leak sites as part of the **AFRINTEL** project. Our objective is to provide clear insights into trends, threat actors, and targeted sectors on the continent.

## 2. Executive summary
* **Total recorded attacks:** 12.
* **Most active actors:** `thegentlemen` (2 attacks) and `killsec` (2 attacks).
* **Primary targeted sectors:** Finance, Insurance, Manufacturing, Technology, and Public Administration.
* **Critical data volumes:**
    * **General Directorate of Taxes and Domains (Senegal):** 1 TB of tax data exfiltrated.
    * **NSIA Assurances (Ivory Coast):** 2.5 million transactional records put up for sale.

---

## 3. Key statistics

### 📊 3.1 Breakdown by group/actor
| Group / Actor | Number of Attacks |
| :--- | :---: |
| **thegentlemen** | 2 |
| **killsec** | 2 |
| **obscura** | 1 |
| **Tanaka** | 1 |
| **yurei** | 1 |
| **radar** | 1 |
| **qilin** | 1 |
| **warlock** | 1 |
| **arcusmedia** | 1 |
| **BlackShrantac** | 1 |


### 🏗️ 3.2 Breakdown by industry sector
| Sector | Number of Attacks |
| :--- | :---: |
| Finance | 2 |
| Insurance | 2 |
| Manufacturing | 2 |
| Technology | 2 |
| Public Administration | 2 |
| Real Estate / Construction | 1 |
| Catering / Food Services | 1 |

#### 3.2.1 Top Targeted sectors visualization
- Finance/Insurance   	[████████████████████] 4
- Public Admin        	[██████████] 2
- Manufacturing       	[██████████] 2
- Technology          	[██████████] 2
- Others              	[██████████] 2

```mermaid
pie title Sector distribution - September 2025
    "Finance" : 2
    "Insurance" : 2
    "Manufacturing" : 2
    "Technology" : 2
    "Public Admin" : 2
    "Real Estate" : 1
    "Catering" : 1
```

### 🌍 3.3 Geographical distribution
| Country | Number of Attacks |
| :--- | :---: |
| 🇪🇬 Egypt | 2 |
| 🇳🇬 Nigeria | 2 |
| 🇲🇦 Morocco | 2 |
| 🇰🇪 Kenya | 2 |
| 🇨🇮 Ivory Coast | 1 |
| 🇿🇼 Zimbabwe | 1 |
| 🇳🇦 Namibia | 1 |
| 🇸🇳 Senegal | 1 |
| **Total** | **12** |

```mermaid
graph TD
    subgraph "Attack distribution by country (September 2025)"
    EG[🇪🇬 Égypte: 2] --- Total((Total: 12))
    NG[🇳🇬 Nigeria: 2] --- Total
    MA[🇲🇦 Maroc: 2] --- Total
    KE[🇰🇪 Kenya: 2] --- Total
    CI[🇨🇮 Côte d'Ivoire: 1] --- Total
    ZW[🇿🇼 Zimbabwe: 1] --- Total
    NA[🇳🇦 Namibie: 1] --- Total
    SN[🇸🇳 Sénégal: 1] --- Total
    end

    style Total fill:#f96,stroke:#333,stroke-width:4px
    style SN fill:#ff9999,stroke:#333
    style CI fill:#ff9999,stroke:#333
```
---

## 4. Detailed incidents by group/actor

#### 4.1 thegentlemen (2 attacks)
* **09/09/2025: Dolidol (Morocco)** - Manufacturing / Bedding Industry. Claim & data leak.
* **09/09/2025: Proplastics Limited (Zimbabwe)** - Manufacturing Industry (Plastics). Claim & data leak.
> **CTI Note:** The group struck two major industrial targets in distinct geographical zones on the same day, demonstrating coordinated planning.

#### 4.2 killsec (2 attacks)
* **10/09/2025: Princeps Credit Systems Limited (Nigeria)** - Finance sector. Claim & data leak.
* **22/09/2025: Fractalite (Morocco)** - Technology / Digital Services. Claim & data leak.

#### 4.3 obscura (1 attack)
* **05/09/2025: MeamarGroup (Egypt)** - Real Estate / Construction. Claim & data leak.

#### 4.4 Tanaka (1 attack)
* **06/09/2025: NSIA Assurances (Ivory Coast)** - Insurance / Finance sector. Massive leak of **2.5 million transactional records** put up for sale.

#### 4.5 yurei (1 attack)
* **08/09/2025: The Promise Nigeria (Nigeria)** - Catering / Food Services. Claim & data leak.

#### 4.6 radar (1 attack)
* **11/09/2025: Epia Financial Services (Namibia)** - Financial Services. Claim & data leak.

#### 4.7 qilin (1 attack)
* **14/09/2025: Office of the Registrar of Political Parties (Kenya)** - Public Administration. Claim & data leak.

#### 4.8 warlock (1 attack)
* **16/09/2025: Jubilee Life Insurance (Kenya)** - Insurance / Finance. Claim & data leak.

#### 4.9 arcusmedia (1 attack)
* **17/09/2025: Accflex ERP (Egypt)** - Technology / ERP Software Publishing. Claim & data leak.

#### 4.10 BlackShrantac (1 attack)
* **29/09/2025: Direction Générale des Impôts et des Domaines (Senegal)** - Tax Administration. Massive exfiltration of **1 TB of sensitive data** (tax databases, land registries, banking info).
#### 4.11 Actor → victim → country

```mermaid
graph LR

A1[thegentlemen] --> V1[Dolidol]
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

classDef actor fill:#8b0000,color:#fff,stroke:#5c0000,stroke-width:1px;
classDef victim fill:#0b5394,color:#fff,stroke:#073763,stroke-width:1px;
classDef country fill:#38761d,color:#fff,stroke:#274e13,stroke-width:1px;

class A1,A2,A3,A4,A5,A6,A7,A8,A9,A10 actor;
class V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12 victim;
class P1,P2,P3,P4,P5,P6,P7,P8 country;
```
---
## 5. Observed TTPs (Tactics, Techniques & Procedures)
* **Massive Exfiltration:** Ability to collect and exfiltrate volumes exceeding 1 TB (DGID) or millions of rows of data (NSIA).
* **Double Extorsion & Monetization:** Systematic sale of data on underground forums to force payment (e.g., Tanaka).
* **State Infrastructure Targeting:** Increased attacks against regulatory bodies and financial ministries.
* **Geo-Operational Agility:** Ability of certain groups to conduct simultaneous attacks across different regions of the continent (e.g., thegentlemen).

## 6. Recommendations
1.  **Data Governance:** For public administrations, prioritize encryption of sensitive databases and offline backups.
2.  **Network Segmentation:** Isolate payroll systems and customer registries from internet-exposed networks.
3.  **Cyber Hygiene:** Widespread implementation of Multi-Factor Authentication (MFA) and regular audits of third-party access (VPN/ERP).

---

## 7. Conclusion
September 2025 confirms that Africa is a major operational ground for ransomware groups. The diversity of actors (10 different groups) and the scale of exfiltrations (DGID, NSIA) call for increased vigilance and strengthened intelligence sharing (CTI) between the continent's nations.

---

### ✍🏿 Author
**Adama ASSIONGBON**
*SOC & Cyber Threat Intelligence Consultant*
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon/)

---
*Open initiative for CTI monitoring in Africa - AFRINTEL*
