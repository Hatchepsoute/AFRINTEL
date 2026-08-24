# AFRINTEL CTI Report - Cyber Threats in Africa - November 2025

👉🏾 [Version française](./README_FR.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Period-November%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Executive summary

In November 2025, AFRINTEL documents **15 cyber incidents** affecting organizations and digital services across **7 African countries**.

The landscape is dominated by **Ransomware with 10 records (66.7%)**, followed by **Data Leak with 4 (26.7%)**. Other observed types are Defacement 1.

Geographic concentration is significant: **Morocco (4)**, **Egypt (4)**, **South Africa (2)** together account for **10 records, or 66.7% of the month**. This concentration reflects AFRINTEL corpus visibility rather than an exhaustive national compromise rate.

At sector level, the most represented categories are **Government / Administration (3)**, **Transport / Logistics (2)**, **Technology / IT (2)**. The most frequent actor labels are `clop` (3), `nightspire` (3), `spacebears` (1). `Unknown`, when present, denotes missing attribution rather than a threat actor.

Evidence maturity remains variable: **13 records** are unverified claims or claims accompanied by samples. AFRINTEL maintains a strict separation between **observed facts, claims, corroboration, official confirmation, and technical unknowns**.

Compared with October, monthly volume **decreases by 5 records**. The most visible changes are Ransomware 16->10 (-6), Defacement 0->1 (+1), Data Leak 3->4 (+1).

> **Reading note:** AFRINTEL figures describe documented incidents and the visibility of observed threats. They are not an exhaustive measurement of every cyberattack that actually occurred across Africa.

### 1.1 Month-over-month comparison

| Indicator | October 2025 | November 2025 | Change |
|---|---:|---:|---:|
| Total incidents | 20 | 15 | **-5 (-25.0%)** |
| Ransomware | 16 | 10 | **-6 (-37.5%)** |
| Data Leak | 3 | 4 | **+1 (+33.3%)** |
| Access Sale | 1 | 0 | **-1 (-100.0%)** |
| DDoS | 0 | 0 | **Stable** |
| Defacement | 0 | 1 | **+1 (new)** |
| Account Takeover | 0 | 0 | **Stable** |
| System Intrusion | 0 | 0 | **Stable** |
| Malware | 0 | 0 | **Stable** |
| Operational Fraud | 0 | 0 | **Stable** |




## 2. Methodology

- **Scope:** 54 African countries; reference period: November 2025.
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
| Documented incidents | **15** |
| Countries represented | **7** |
| Regions represented | **4** |
| Leading country | **Morocco (4)** |
| Leading sector | **Government / Administration (3)** |
| Leading actor label | **clop (3)** |

| Incident type | Records | Share |
|---|---:|---:|
| Ransomware | 10 | 66.7% |
| Data Leak | 4 | 26.7% |
| Access Sale | 0 | 0.0% |
| DDoS | 0 | 0.0% |
| Defacement | 1 | 6.7% |
| Account Takeover | 0 | 0.0% |
| System Intrusion | 0 | 0.0% |
| Malware | 0 | 0.0% |
| Operational Fraud | 0 | 0.0% |
| **Total** | **15** | **100%** |

```mermaid
pie showData
    title Incident types - November 2025
    "Ransomware" : 10
    "Data Leak" : 4
    "Defacement" : 1
```

## 4. Geographic distribution

| Country | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Morocco | **4** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| Egypt | **4** | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| South Africa | **2** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ivory Coast | **2** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zambia | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nigeria | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kenya | **1** | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| **Total** | **15** | **10** | **4** | **0** | **0** | **1** | **0** | **0** | **0** |

> `Operational Fraud = 0` this month; the column is omitted for readability.

## 5. Regional distribution

| Region | Records | Share |
|---|---:|---:|
| North Africa | 8 | 53.3% |
| Southern Africa | 3 | 20.0% |
| West Africa | 3 | 20.0% |
| East Africa | 1 | 6.7% |
| **Total** | **15** | **100%** |

The leading region is **North Africa with 8 records (53.3%)**.

## 6. Sector impact

| Sector | Records | Share | Activity |
|---|---:|---:|---|
| Government / Administration | 3 | 20.0% | ███ |
| Transport / Logistics | 2 | 13.3% | ██ |
| Technology / IT | 2 | 13.3% | ██ |
| Finance / Banking | 2 | 13.3% | ██ |
| Construction / Real Estate | 2 | 13.3% | ██ |
| Professional / Business Services | 1 | 6.7% | █ |
| Retail / E-commerce | 1 | 6.7% | █ |
| Manufacturing / Industry | 1 | 6.7% | █ |
| Healthcare / Medical | 1 | 6.7% | █ |
| **Total** | **15** | **100%** | |

## 7. Actors / groups

`Unknown` denotes missing attribution, not a threat actor.

| Actor / Group | Records | Activity |
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

## 8. Evidence maturity

| Evidence maturity | Records | Share |
|---|---:|---:|
| Claim - Unverified | 9 | 60.0% |
| Claim - Data Sample Published | 4 | 26.7% |
| Data Fully Published | 1 | 6.7% |
| Victim/Government/Authority Confirmed | 1 | 6.7% |
| **Total** | **15** | **100%** |

Evidence statuses describe the available validation level; they do not change the technical incident type.

## 9. Timeline

```mermaid
timeline
    title AFRINTEL - November 2025
    04 November 2025 : DOVERN Import
    04 November 2025 : Wannabees (wannabees.co.za)
    05 November 2025 : Anka (Anka.africa)
    06 November 2025 : ELSEWEDYELECTRIC.COM
    06 November 2025 : ZANACO.CO.ZM
    06 November 2025 : www.marjane.ma
    08 November 2025 : NARSA (Agence Nationale de la Sécurité Routière)
    09 November 2025 : Eastern Cape Department of Human Settlements (ECDHS)
    09 November 2025 : Fidelity Pension Managers, Nigeria
    11 November 2025 : Samcrete Holding
    17 November 2025 : Multiple Government of Kenya websites
    25 November 2025 : LAMAICA, Egypt
    26 November 2025 : Arabia Holding
    26 November 2025 : Santé Espoir Vie Côte d'Ivoire (SEV-CI)
    30 November 2025 : Joutech
```

## 10. Monthly CTI analysis

### Ransomware

**10 records** are classified as Ransomware. Leading countries: Egypt (4), Morocco (2), Zambia (1). A leak-site listing does not itself prove encryption or complete exfiltration.

### Data Leak

**4 records** are classified as Data Leak. Leading countries: Morocco (2), South Africa (1), Ivory Coast (1). AFRINTEL distinguishes actually observed data from aggregate volumes claimed by actors.

### Defacement

**1 Defacement records** are documented. Distribution: Kenya (1). Defacement is not reclassified as Data Leak without separate evidence.

## 11. Notable incidents

| Country | Organization | Type | Status | Impact | Confidence |
|---|---|---|---|---|---|
| Kenya | Multiple Government of Kenya websites | Defacement | Government Confirmed + Preliminary Actor Attribution | Level 4 | Very High |
| Morocco | www.marjane.ma | Ransomware | Data Fully Published | Level 4 | High |
| Ivory Coast | Anka (Anka.africa) | Data Leak | Claim - Data Sample Published | Level 3 | Medium |
| Zambia | ZANACO.CO.ZM | Ransomware | Claim - Unverified | Level 3 | Medium |
| Egypt | ELSEWEDYELECTRIC.COM | Ransomware | Claim - Unverified | Level 2 | Medium |

> This table highlights up to five records using structured impact, confirmation, and confidence fields. It is not an absolute severity ranking.

## 12. Key findings and intelligence gaps

- **Geographic concentration:** Morocco accounts for 4 records (26.7%), followed by Egypt (4) and South Africa (2).
- **Threat structure:** Ransomware is the leading type with 10 records, followed by Data Leak (4).
- **Sectors:** Government / Administration (3) and Transport / Logistics (2) have the highest visibility.
- **Actors:** the most frequent labels are clop (3), nightspire (3), and spacebears (1).
- **Evidence:** 13 records rely on unverified claims or claims with a published sample; these statuses do not equal complete technical confirmation.

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

**November 2025** contains **15 documented cyber incidents** across **7 African countries**. The monthly CTI value lies not only in volume but in separating **incident type, timeline, evidence level, geography, sector, and actor**.

The report therefore preserves a structured picture of the observable threat environment while keeping claims, corroboration, confirmations, and unknowns at their actual evidence level.

👉🏾 [See monthly victims](./victims.md)

**AFRINTEL** - TLP:CLEAR
