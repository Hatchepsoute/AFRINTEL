# AFRINTEL CTI Report - Cyber Threats in Africa - December 2025

👉🏾 [Version française](./README_FR.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Period-December%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Executive summary

In December 2025, AFRINTEL documents **18 cyber incidents** affecting organizations and digital services across **10 African countries**.

The landscape is dominated by **Ransomware with 14 records (77.8%)**, followed by **Data Leak with 4 (22.2%)**.

Geographic concentration is significant: **Egypt (5)**, **South Africa (3)**, **Tunisia (3)** together account for **11 records, or 61.1% of the month**. This concentration reflects AFRINTEL corpus visibility rather than an exhaustive national compromise rate.

At sector level, the most represented categories are **Finance / Banking (4)**, **Healthcare / Medical (3)**, **Government / Administration (2)**. The most frequent actor labels are `qilin` (3), `lockbit5` (3), `dragonforce` (2). `Unknown`, when present, denotes missing attribution rather than a threat actor.

Evidence maturity remains variable: **18 records** are unverified claims or claims accompanied by samples. AFRINTEL maintains a strict separation between **observed facts, claims, corroboration, official confirmation, and technical unknowns**.

Compared with November, monthly volume **increases by 3 records**. The most visible changes are Ransomware 10->14 (+4), Defacement 1->0 (-1).

> **Reading note:** AFRINTEL figures describe documented incidents and the visibility of observed threats. They are not an exhaustive measurement of every cyberattack that actually occurred across Africa.

### 1.1 Month-over-month comparison

| Indicator | November 2025 | December 2025 | Change |
|---|---:|---:|---:|
| Total incidents | 15 | 18 | **+3 (+20.0%)** |
| Ransomware | 10 | 14 | **+4 (+40.0%)** |
| Data Leak | 4 | 4 | **Stable** |
| Access Sale | 0 | 0 | **Stable** |
| DDoS | 0 | 0 | **Stable** |
| Defacement | 1 | 0 | **-1 (-100.0%)** |
| Account Takeover | 0 | 0 | **Stable** |
| System Intrusion | 0 | 0 | **Stable** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |




## 2. Methodology

- **Scope:** 54 African countries; reference period: December 2025.
- **Source of truth:** validated `victims_FR.md` / `victims.md` pair.
- **Classification:** Ransomware, Data Leak, Access Sale, DDoS, Defacement, Account Takeover, System Intrusion, Malware, and Operational Fraud.
- **Counting:** one canonical record equals one documented cyber incident; cases under investigation remain outside statistics.
- **Timeline:** `Incident date` and `Initial publication date` remain separate. A later disclosure does not artificially move an incident into another month when chronology is sufficiently supported.
- **Uncertain dates:** when no exact day is known, the evidence-supported month or time window is retained.
- **Sources:** public links are retained for supplementary incidents found through OSINT/web research; they are not retroactively imposed on historical or direct Dark Web observations.
- **Evidence:** incident type, status, confidence, impact, and provenance remain separate dimensions.
- **Sectors:** normalization is calculated once from the structured corpus and used identically in FR and EN.
- **Limitation:** frequencies reflect AFRINTEL visibility rather than every real compromise on the continent.

## 3. Overview and incident types

| Indicator | Value |
|---|---:|
| Documented incidents | **18** |
| Countries represented | **10** |
| Regions represented | **4** |
| Leading country | **Egypt (5)** |
| Leading sector | **Finance / Banking (4)** |
| Leading actor label | **qilin (3)** |

| Incident type | Records | Share |
|---|---:|---:|
| Ransomware | 14 | 77.8% |
| Data Leak | 4 | 22.2% |
| Access Sale | 0 | 0.0% |
| DDoS | 0 | 0.0% |
| Defacement | 0 | 0.0% |
| Account Takeover | 0 | 0.0% |
| System Intrusion | 0 | 0.0% |
| Malware | 0 | 0.0% |
| Operational Fraud | 0 | 0.0% |
| **Total** | **18** | **100%** |

```mermaid
pie showData
    title Incident types - December 2025
    "Ransomware" : 14
    "Data Leak" : 4
```

## 4. Geographic distribution

| Country | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Egypt | **5** | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| South Africa | **3** | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tunisia | **3** | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zambia | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ghana | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nigeria | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zimbabwe | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Algeria | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Morocco | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kenya | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **18** | **14** | **4** | **0** | **0** | **0** | **0** | **0** | **0** |

> `Operational Fraud = 0` this month; the column is omitted for readability.

## 5. Regional distribution

| Region | Records | Share |
|---|---:|---:|
| North Africa | 10 | 55.6% |
| Southern Africa | 5 | 27.8% |
| West Africa | 2 | 11.1% |
| East Africa | 1 | 5.6% |
| **Total** | **18** | **100%** |

The leading region is **North Africa with 10 records (55.6%)**.

## 6. Sector impact

| Sector | Records | Share | Activity |
|---|---:|---:|---|
| Finance / Banking | 4 | 22.2% | ████ |
| Healthcare / Medical | 3 | 16.7% | ███ |
| Government / Administration | 2 | 11.1% | ██ |
| Education / University | 2 | 11.1% | ██ |
| Manufacturing / Industry | 2 | 11.1% | ██ |
| Technology / IT | 1 | 5.6% | █ |
| Agriculture / Agribusiness | 1 | 5.6% | █ |
| Not specified | 1 | 5.6% | █ |
| Construction / Real Estate | 1 | 5.6% | █ |
| Energy / Utilities | 1 | 5.6% | █ |
| **Total** | **18** | **100%** | |

## 7. Actors / groups

`Unknown` denotes missing attribution, not a threat actor.

| Actor / Group | Records | Activity |
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

## 8. Evidence maturity

| Evidence maturity | Records | Share |
|---|---:|---:|
| Claim - Unverified | 13 | 72.2% |
| Claim - Data Sample Published | 5 | 27.8% |
| **Total** | **18** | **100%** |

Evidence statuses describe the available validation level; they do not change the technical incident type.

## 9. Timeline

```mermaid
timeline
    title AFRINTEL - December 2025
    05 December 2025 : 3S Software (Secured Smart Systems Overview Metrics)
    05 December 2025 : National Health Insurance Management Authority
    06 December 2025 : Kasapreko Company Limited
    06 December 2025 : Diesel Electric
    07 December 2025 : incolease.com
    07 December 2025 : elundini.gov.za
    08 December 2025 : Arkan
    11 December 2025 : Leadway Assurance / Leadway Health
    12 December 2025 : Hopital La Rabta (University Hospital Center)
    15 December 2025 : Tunisian Society of Radiology (strtn.org)
    22 December 2025 : Polaris Parks
    24 December 2025 : National Credit Regulator (NCR)
    26 December 2025 : Hopital La Rabta (second ransomware claim)
    26 December 2025 : Proplastics Limited (second ransomware claim)
    29 December 2025 : Oran University 1 Ahmed Ben Bella
    29 December 2025 : 100 Watt Plast (100wattplast.com)
    31 December 2025 : Pharmacie.ma
    31 December 2025 : Kenya Electricity Transmission Company (KETRACO)
```

## 10. Monthly CTI analysis

### Ransomware

**14 records** are classified as Ransomware. Leading countries: Egypt (4), South Africa (3), Tunisia (3). A leak-site listing does not itself prove encryption or complete exfiltration.

### Data Leak

**4 records** are classified as Data Leak. Leading countries: Algeria (1), Egypt (1), Morocco (1). AFRINTEL distinguishes actually observed data from aggregate volumes claimed by actors.

## 11. Notable incidents

| Country | Organization | Type | Status | Impact | Confidence |
|---|---|---|---|---|---|
| South Africa | National Credit Regulator (NCR) | Ransomware | Claim - Data Sample Published | Level 4 | High |
| Egypt | 3S Software (Secured Smart Systems Overview Metrics) | Ransomware | Claim - Unverified | N/A | N/A |
| Zambia | National Health Insurance Management Authority | Ransomware | Claim - Unverified | N/A | N/A |
| Ghana | Kasapreko Company Limited | Ransomware | Claim - Unverified | N/A | N/A |
| South Africa | Diesel Electric | Ransomware | Claim - Unverified | N/A | N/A |

> This table highlights up to five records using structured impact, confirmation, and confidence fields. It is not an absolute severity ranking.

## 12. Key findings and intelligence gaps

- **Geographic concentration:** Egypt accounts for 5 records (27.8%), followed by South Africa (3) and Tunisia (3).
- **Threat structure:** Ransomware is the leading type with 14 records, followed by Data Leak (4).
- **Sectors:** Finance / Banking (4) and Healthcare / Medical (3) have the highest visibility.
- **Actors:** the most frequent labels are qilin (3), lockbit5 (3), and dragonforce (2).
- **Evidence:** 18 records rely on unverified claims or claims with a published sample; these statuses do not equal complete technical confirmation.

### Intelligence gaps

- initial-access vector often not public;
- exact technical compromise date sometimes unknown;
- claimed volumes rarely fully verifiable;
- technical attribution often limited to a publication handle or label;
- public remediation, root-cause, and DFIR conclusions remain limited.

These gaps should guide collection rather than be replaced with assumptions.

## 13. Recommendations

### Organizations

- enforce phishing-resistant MFA on privileged accounts, VPN, email, social media, and administration consoles;
- apply PAM, least privilege, segmentation, and secret rotation;
- maintain immutable backups and test restoration;
- strengthen public applications, APIs, and administration interfaces;
- formalize incident response and data-breach notification.

### SOC and detection

- monitor abnormal authentication, MFA changes, privileged-account creation, and role elevation;
- detect mass database reads, unusual exports, archive creation, and large outbound transfers;
- correlate EDR, IAM, VPN, WAF, proxy, DNS, cloud, and application logs;
- distinguish DDoS, internal intrusion, account compromise, and data exposure to avoid unsupported conclusions.

### CTI

- keep incident date, initial publication, first observation, sample, disclosure, and confirmation separate;
- track republication and resale without automatically counting them as new compromise;
- preserve the evidence hierarchy between claim, corroboration, and confirmation;
- validate FR/EN parity before generating statistics.

## 14. Conclusion

**December 2025** contains **18 documented cyber incidents** across **10 African countries**. The monthly CTI value lies not only in volume but in separating **incident type, timeline, evidence level, geography, sector, and actor**.

The report therefore preserves a structured picture of the observable threat environment while keeping claims, corroboration, confirmations, and unknowns at their actual evidence level.

👉🏾 [See monthly victims](./victims.md)

**AFRINTEL** - TLP:CLEAR
