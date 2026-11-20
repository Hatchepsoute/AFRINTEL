# AFRINTEL CTI Report - Cyber Threats in Africa - December 2025

👉🏾 [Version française](./README_FR.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Period](https://img.shields.io/badge/Period-December%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Executive summary

In December 2025, AFRINTEL documents **21 cyber incidents** affecting organizations and digital services across **11 African countries**.

The landscape is dominated by **Ransomware with 14 records (66.7%)**, followed by **Data Leak with 7 (33.3%)**.

Geographic concentration is significant: **Egypt (6)**, **South Africa (3)**, and **Tunisia (4)** together account for **13 records, or 61.9% of the month**. This concentration reflects AFRINTEL corpus visibility rather than an exhaustive national compromise rate.

At sector level, the most represented normalized categories are **Finance / Banking (4)**, **Healthcare / Medical (3)**, **Government / Administration (2)**, **Education / University (3)** and **Manufacturing / Industry (2)**. The most frequent actor labels are `qilin` (3), `lockbit5` (3), `dragonforce` (2) and `nova` (2).

Evidence maturity remains variable: **13 records are `Claim - Unverified`, 7 are `Claim - Data Sample Published`, and 1 is `Data Fully Published`**. AFRINTEL maintains a strict separation between observed facts, claims, corroboration, official confirmation, and technical unknowns.

Compared with November, monthly volume **increases by 5 records**. The most visible changes are Ransomware 10→14 (+4), Data Leak 5→7 (+2), and Defacement 1→0 (-1).

> **Reading note:** AFRINTEL figures describe documented incidents and the visibility of observed threats. They are not an exhaustive measurement of every cyberattack that actually occurred across Africa.

### 1.1 Month-over-month comparison

| Indicator | November 2025 | December 2025 | Change |
|---|---:|---:|---:|
| Total incidents | 16 | 21 | **+5 (+31.3%)** |
| Ransomware | 10 | 14 | **+4 (+40.0%)** |
| Data Leak | 5 | 7 | **+2 (+40.0%)** |
| Access Sale | 0 | 0 | **Stable** |
| DDoS | 0 | 0 | **Stable** |
| Defacement | 1 | 0 | **-1 (-100.0%)** |
| Account Takeover | 0 | 0 | **Stable** |
| System Intrusion | 0 | 0 | **Stable** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |

## 2. Methodology
![December 2025 comparison with previous month](assets/comparaison_EN.png)


- **Scope:** 54 African countries; reference period: December 2025.
- **Source of truth:** validated `victims_FR.md` / `victims.md` pair.
- **Classification:** Ransomware, Data Leak, Access Sale, DDoS, Defacement, Account Takeover, System Intrusion, Malware, and Operational Fraud.
- **Counting:** one canonical record equals one documented cyber incident; cases under investigation remain outside statistics.
- **Timeline:** `Incident date` and `Initial publication date` remain separate.
- **Uncertain dates:** when no exact compromise day is known, the evidence-supported publication period is retained without inventing a technical intrusion date.
- **Evidence:** incident type, status, confidence, impact, and provenance remain separate dimensions.
- **Limitation:** frequencies reflect AFRINTEL visibility rather than every real compromise on the continent.

## 3. Overview and incident types

| Indicator | Value |
|---|---:|
| Documented incidents | **21** |
| Countries represented | **11** |
| Regions represented | **4** |
| Leading country | **Egypt (6)** |
| Leading normalized sector | **Finance / Banking (4)** |
| Leading actor labels | **qilin (3), lockbit5 (3)** |

| Incident type | Records | Share |
|---|---:|---:|
| Ransomware | 14 | 66.7% |
| Data Leak | 7 | 33.3% |
| Access Sale | 0 | 0.0% |
| DDoS | 0 | 0.0% |
| Defacement | 0 | 0.0% |
| Account Takeover | 0 | 0.0% |
| System Intrusion | 0 | 0.0% |
| Malware | 0 | 0.0% |
| Operational Fraud | 0 | 0.0% |
| **Total** | **21** | **100%** |

```mermaid
pie showData
    title Incident types - December 2025
    "Ransomware" : 14
    "Data Leak" : 7
```

## 4. Geographic distribution
![Incident types](assets/types_EN.png)
![Incident distribution](assets/types_pie_EN.png)


| Country | Total | Ransomware | Data Leak |
|---|---:|---:|---:|
| Egypt | **6** | 4 | 2 |
| South Africa | **3** | 3 | 0 |
| Tunisia | **4** | 3 | 1 |
| Zambia | **1** | 1 | 0 |
| Ghana | **1** | 1 | 0 |
| Nigeria | **1** | 1 | 0 |
| Zimbabwe | **1** | 1 | 0 |
| Algeria | **1** | 0 | 1 |
| Morocco | **1** | 0 | 1 |
| Kenya | **1** | 0 | 1 |
| Ivory Coast | **1** | 0 | 1 |
| **Total** | **21** | **14** | **7** |

## 5. Regional distribution
![Documented incidents by country](assets/pays_EN.png)


| Region | Records | Share |
|---|---:|---:|
| North Africa | 12 | 57.1% |
| Southern Africa | 5 | 23.8% |
| West Africa | 3 | 14.3% |
| East Africa | 1 | 4.8% |
| **Total** | **21** | **100%** |

The leading region is **North Africa with 11 records (57.9%)**.

## 6. Sector impact
![Regional distribution](assets/regions_EN.png)
![Regional shares](assets/regions_pie_EN.png)


| Normalized sector | Records | Share |
|---|---:|---:|
| Finance / Banking | 4 | 19.0% |
| Healthcare / Medical | 3 | 14.3% |
| Government / Administration | 2 | 9.5% |
| Education / University | 3 | 14.3% |
| Manufacturing / Industry | 2 | 9.5% |
| Technology / IT | 1 | 4.8% |
| Agriculture / Agribusiness | 2 | 9.5% |
| Not specified | 1 | 4.8% |
| Construction / Real Estate | 1 | 4.8% |
| Energy / Utilities | 1 | 4.8% |
| Retail / E-commerce | 1 | 4.8% |
| **Total** | **21** | **100%** |

## 7. Actors / groups
![Sector exposure](assets/secteurs_EN.png)
![Sector distribution](assets/secteurs_pie_EN.png)


| Actor / Group | Records |
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

## 8. Evidence maturity
![Actors and publication labels](assets/acteurs_EN.png)


| Evidence maturity | Records | Share |
|---|---:|---:|
| Claim - Unverified | 13 | 61.9% |
| Claim - Data Sample Published | 7 | 33.3% |
| Data Fully Published | 1 | 4.8% |
| **Total** | **21** | **100%** |

## 9. Timeline
![Evidence maturity](assets/preuves_EN.png)


```mermaid
timeline
    title AFRINTEL - December 2025
    05 December 2025 : 3S Software
    05 December 2025 : National Health Insurance Management Authority
    06 December 2025 : Kasapreko Company Limited
    06 December 2025 : Diesel Electric
    07 December 2025 : incolease.com
    07 December 2025 : elundini.gov.za
    08 December 2025 : Arkan
    11 December 2025 : Leadway Assurance / Leadway Health
    12 December 2025 : Hopital La Rabta
    13 December 2025 : ANADER
    15 December 2025 : Examens.tn
    15 December 2025 : Tunisian Society of Radiology
    22 December 2025 : Polaris Parks
    24 December 2025 : National Credit Regulator
    26 December 2025 : Hopital La Rabta - second claim
    26 December 2025 : Proplastics Limited - second claim
    26 December 2025 : Yalla Tager Marketplace
    29 December 2025 : Oran University 1 Ahmed Ben Bella
    29 December 2025 : 100 Watt Plast
    31 December 2025 : Pharmacie.ma
    31 December 2025 : KETRACO
```

## 10. Monthly CTI analysis

### Ransomware

**14 records** are classified as Ransomware. Leading countries are Egypt (4), South Africa (3), and Tunisia (4). A leak-site listing does not itself prove encryption or complete exfiltration.

### Data Leak

**7 records** are classified as Data Leak. Egypt has 2, while Algeria, Ivory Coast, Morocco, and Kenya have one each. The ANADER record is a **sample-backed claim**: the visible SQL/JSON structure, administrative roles and territorial mappings are coherent, but the claimed 11.4 MB dump, origin and completeness remain unverified.

## 11. Notable incidents

| Country | Organization | Type | Status | Impact | Confidence |
|---|---|---|---|---|---|
| South Africa | National Credit Regulator (NCR) | Ransomware | Claim - Data Sample Published | Level 4 | High |
| Egypt | Yalla Tager Marketplace | Data Leak | Claim - Data Sample Published | Level 3 | Medium |
| Egypt | 100 Watt Plast | Data Leak | Claim - Data Sample Published | N/A | High |
| Morocco | Pharmacie.ma | Data Leak | Claim - Data Sample Published | N/A | N/A |
| Kenya | KETRACO | Data Leak | Claim - Data Sample Published | N/A | Medium |

## 12. Key findings and intelligence gaps

- **Geographic concentration:** Egypt accounts for 6 records (28.6%), followed by South Africa (3) and Tunisia (4).
- **Threat structure:** Ransomware remains the leading type with 14 records, followed by Data Leak (7).
- **Sectors:** Finance / Banking (4) and Healthcare / Medical (3) have the highest visibility; Retail / E-commerce gains one record through Yalla Tager.
- **Evidence:** 21 records remain claims or publications with distinct evidence levels, including 7 accompanied by published samples and 1 presented as fully published.
- **Yalla Tager:** the sample supports a customer/merchant-data exposure claim, but does not establish the date or method of compromise and does not validate the advertised 20,000-user total.

### Intelligence gaps

- initial-access vector often not public;
- exact technical compromise date sometimes unknown;
- claimed volumes rarely fully verifiable;
- technical attribution often limited to a publication handle or label;
- public remediation, root-cause, and DFIR conclusions remain limited.

## 13. Recommendations

### Organizations

- enforce phishing-resistant MFA on privileged accounts, email, administration consoles and seller/merchant back-office access;
- apply least privilege and monitor bulk exports of customer and merchant data;
- maintain tested backups and formalize data-breach response procedures;
- review exposed customer-support, marketplace, API and administrative interfaces.

### SOC and detection

- monitor abnormal authentication, role changes and privileged-account creation;
- detect mass database reads, unusual CSV exports, archive creation and large outbound transfers;
- correlate IAM, application, WAF, proxy, DNS, cloud and EDR telemetry;
- alert on abnormal access to customer/merchant datasets from new devices, locations or service accounts.

### CTI

- separate publication date, account/customer timestamps, extraction date and technical compromise date;
- keep actor-claimed volumes distinct from observed sample size;
- preserve FR/EN parity before deriving aggregate statistics.

## 14. Conclusion

**December 2025** contains **21 documented cyber incidents** across **11 African countries**: 14 Ransomware and 7 Data Leak. The addition of ANADER adds Ivory Coast to the month and raises the sample-backed Data Leak component without changing the evidential requirement to distinguish observed data from claimed scope.

👉🏾 [See monthly victims](./victims.md)

**AFRINTEL** - TLP:CLEAR
