# AFRINTEL CTI Report - Cyber Threats in Africa - January 2025

👉🏾 [Version française](./README_FR.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Period-January%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Executive summary

In January 2025, AFRINTEL documents **19 cyber incidents** affecting organizations and digital services across **8 African countries**.

The landscape is dominated by **Ransomware with 16 records (84.2%)**, followed by **Data Leak with 2 (10.5%)**. Other observed types are Account Takeover 1.

Geographic concentration is significant: **Kenya (4)**, **Egypt (4)**, **Nigeria (3)** together account for **11 records, or 57.9% of the month**. This concentration reflects AFRINTEL corpus visibility rather than an exhaustive national compromise rate.

At sector level, the most represented categories are **Education / University (6)**, **Government / Administration (4)**, **Healthcare / Medical (2)**. The most frequent actor labels are `funksec` (6), `GDLockerSec` (3), `ransomhub` (2). `Unknown`, when present, denotes missing attribution rather than a threat actor.

Evidence maturity remains variable: **17 records** are unverified claims or claims accompanied by samples. AFRINTEL maintains a strict separation between **observed facts, claims, corroboration, official confirmation, and technical unknowns**.

Compared with the final corrected December 2024 baseline, monthly volume **increases by 3 records, from 16 to 19 (+18.8%)**. Ransomware rises from 11 to 16 (+5), while Data Leak falls from 3 to 2, Access Sale from 1 to 0, and Defacement from 1 to 0. Account Takeover appears with 1 record in January.

> **Reading note:** AFRINTEL figures describe documented incidents and the visibility of observed threats. They are not an exhaustive measurement of every cyberattack that actually occurred across Africa.

### 1.1 Month-over-month comparison

| Indicator | Final corrected December 2024 | January 2025 | Change |
|---|---:|---:|---:|
| Total incidents | 16 | 19 | **+3 (+18.8%)** |
| Ransomware | 11 | 16 | **+5 (+45.5%)** |
| Data Leak | 3 | 2 | **-1 (-33.3%)** |
| Access Sale | 1 | 0 | **-1 (-100.0%)** |
| DDoS | 0 | 0 | **Stable** |
| Defacement | 1 | 0 | **-1 (-100.0%)** |
| Account Takeover | 0 | 1 | **+1 (new)** |
| System Intrusion | 0 | 0 | **Stable** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |

> **Comparison basis:** December 2024 uses the final AFRINTEL 2024 baseline after chronology review, reclassification, and integration of validated 2024 cases. All nine incident types are therefore directly comparable with January 2025.

## 2. Methodology

- **Scope:** 54 African countries; reference period: January 2025.
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
| Documented incidents | **19** |
| Countries represented | **8** |
| Regions represented | **4** |
| Leading country | **Kenya (4)** |
| Leading sector | **Education / University (6)** |
| Leading actor label | **funksec (6)** |

| Incident type | Records | Share |
|---|---:|---:|
| Ransomware | 16 | 84.2% |
| Data Leak | 2 | 10.5% |
| Access Sale | 0 | 0.0% |
| DDoS | 0 | 0.0% |
| Defacement | 0 | 0.0% |
| Account Takeover | 1 | 5.3% |
| System Intrusion | 0 | 0.0% |
| Malware | 0 | 0.0% |
| Operational Fraud | 0 | 0.0% |
| **Total** | **19** | **100%** |

```mermaid
pie showData
    title Incident types - January 2025
    "Ransomware" : 16
    "Data Leak" : 2
    "Account Takeover" : 1
```

## 4. Geographic distribution

| Country | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Kenya | **4** | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| Egypt | **4** | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nigeria | **3** | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| South Africa | **2** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Morocco | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Algeria | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Uganda | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zambia | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **19** | **16** | **2** | **0** | **0** | **0** | **1** | **0** | **0** |

> `Operational Fraud = 0` this month; the column is omitted for readability.

## 5. Regional distribution

| Region | Records | Share |
|---|---:|---:|
| North Africa | 8 | 42.1% |
| East Africa | 5 | 26.3% |
| Southern Africa | 3 | 15.8% |
| West Africa | 3 | 15.8% |
| **Total** | **19** | **100%** |

The leading region is **North Africa with 8 records (42.1%)**.

## 6. Sector impact

| Sector | Records | Share | Activity |
|---|---:|---:|---|
| Education / University | 6 | 31.6% | ██████ |
| Government / Administration | 4 | 21.1% | ████ |
| Healthcare / Medical | 2 | 10.5% | ██ |
| Media / Entertainment | 2 | 10.5% | ██ |
| Retail / E-commerce | 1 | 5.3% | █ |
| Technology / IT | 1 | 5.3% | █ |
| Transport / Logistics | 1 | 5.3% | █ |
| Hospitality / Tourism | 1 | 5.3% | █ |
| Professional / Business Services | 1 | 5.3% | █ |
| **Total** | **19** | **100%** | |

## 7. Actors / groups

`Unknown` denotes missing attribution, not a threat actor.

| Actor / Group | Records | Activity |
|---|---:|---|
| funksec | 6 | ██████ |
| GDLockerSec | 3 | ███ |
| ransomhub | 2 | ██ |
| spacebears | 2 | ██ |
| babuk2 | 2 | ██ |
| Unknown | 2 | ██ |
| apt73 | 1 | █ |
| SevenZeroDay404 | 1 | █ |

## 8. Evidence maturity

| Evidence maturity | Records | Share |
|---|---:|---:|
| Claim - Unverified | 8 | 42.1% |
| Claim - Data Sample Published | 9 | 47.4% |
| Victim/Government/Authority Confirmed | 2 | 10.5% |
| **Total** | **19** | **100%** |

Evidence statuses describe the available validation level; they do not change the technical incident type.

## 9. Timeline

```mermaid
timeline
    title AFRINTEL - January 2025
    06 January 2025 : Molars Dental Practice
    09 January 2025 : General Authority for Government Services
    09 January 2025 : Pick n Pay (pnp.co.za)
    11 January 2025 : SEOCOM Marrakech (seocommarrakech.com)
    14 January 2025 : INTELS Nigeria Limited (intelservice.com)
    14 January 2025 : Sharm Reef Hotel
    15 January 2025 : Misr Technology Services (MTS / mts.gov.eg)
    16 January 2025 : North-West University (NWU)
    21 January 2025 : Barika University Center (cu-barika.dz)
    21 January 2025 : Inaya Clinic (inayaclinic.org)
    24 January 2025 : Lower Niger River Basin Development Authority (LNRBDA)
    24 January 2025 : Sidi Mohamed Ben Abdellah University (www.usmba.ac.ma)
    26 January 2025 : Achievers Journal of Scientific Research
    26 January 2025 : FGSE, Cairo University (fgse.cu.edu.eg)
    27 January 2025 : QED (qed.co.ug)
    27 January 2025 : Workers (workers.com.zm)
    27 January 2025 : Zetech University (zetech.ac.ke)
    31 January 2025 - reported date : Business Registration Service (BRS)
    31 January 2025 : Kenya Broadcasting Corporation (KBC)
```

## 10. Monthly CTI analysis

### Ransomware

**16 records** are classified as Ransomware. Leading countries: Egypt (4), Nigeria (3), Kenya (2). A leak-site listing does not itself prove encryption or complete exfiltration.

### Data Leak

**2 records** are classified as Data Leak. Leading countries: South Africa (1), Kenya (1). AFRINTEL distinguishes actually observed data from aggregate volumes claimed by actors.

### Account Takeover

**1 Account Takeover records** are documented. Distribution: Kenya (1). This category keeps institutional-account compromise distinct.

## 11. Notable incidents

| Country | Organization | Type | Status | Impact | Confidence |
|---|---|---|---|---|---|
| Kenya | Business Registration Service (BRS) | Data Leak | Government Confirmed | Level 4 | Very High |
| Nigeria | Lower Niger River Basin Development Authority (LNRBDA) | Ransomware | Claim - Data Sample Published | Level 4 | Very High |
| Uganda | QED (qed.co.ug) | Ransomware | Claim - Data Sample Published | Level 4 | Very High |
| Kenya | Kenya Broadcasting Corporation (KBC) | Account Takeover | Victim Confirmed | Level 3 | High |
| Kenya | Molars Dental Practice | Ransomware | Claim - Data Sample Published | Level 3 | High |

> This table highlights up to five records using structured impact, confirmation, and confidence fields. It is not an absolute severity ranking.

## 12. Key findings and intelligence gaps

- **Geographic concentration:** Kenya accounts for 4 records (21.1%), followed by Egypt (4) and Nigeria (3).
- **Threat structure:** Ransomware is the leading type with 16 records, followed by Data Leak (2).
- **Sectors:** Education / University (6) and Government / Administration (4) have the highest visibility.
- **Actors:** the most frequent labels are funksec (6), GDLockerSec (3), and ransomhub (2).
- **Evidence:** 17 records rely on unverified claims or claims with a published sample; these statuses do not equal complete technical confirmation.

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

**January 2025** contains **19 documented cyber incidents** across **8 African countries**. The monthly CTI value lies not only in volume but in separating **incident type, timeline, evidence level, geography, sector, and actor**.

The report therefore preserves a structured picture of the observable threat environment while keeping claims, corroboration, confirmations, and unknowns at their actual evidence level.

👉🏾 [See monthly victims](./victims.md)

**AFRINTEL** - TLP:CLEAR
