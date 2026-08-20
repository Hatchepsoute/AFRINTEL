[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Period](https://img.shields.io/badge/Period-July%202024-lightgrey)
![TLP](https://img.shields.io/badge/TLP-CLEAR-brightgreen)

# AFRINTEL CTI Report — July 2024

👉🏾 [Version française](./README_FR.md)

## 1. Executive summary

July 2024 contains **11 incidents**: **7 ransomware claims** and **4 data leaks**. South Africa and Algeria rank first with three incidents each. Algeria's concentration requires caution: all three publications come from a single compilation of older databases being recirculated.

The month spans healthcare, education, defense, transport, finance, and mining. The National War College case contains a material inconsistency: the cited domain belongs to a US institution, while visible documents point to an Ethiopian military school. AFRINTEL retains this limitation instead of silently correcting the attribution.

See [victims.md](./victims.md).

## 2. Methodology

This report covers publications assigned to July 2024. A repost remains a data-circulation incident in the corpus but is not presented as a new intrusion. Confidence reflects the quality of visible evidence, not the age or reputation of the source alone.

Statistics derive from the **11 incidents** in [victims.md](./victims.md), synchronized with [victims_FR.md](./victims_FR.md).

## 3. Global overview

| Indicator | Value |
|---|---:|
| Incidents / Countries | **11 / 7** |
| Ransomware | **7** |
| Data leaks | **4** |
| Access sales / Defacement | **0 / 0** |

### Country ranking

| Country | Total | Ransomware | Data leak |
|---|---:|---:|---:|
| 🇿🇦 South Africa | 3 | 3 | 0 |
| 🇩🇿 Algeria | 3 | 0 | 3 |
| 🇰🇪 Kenya | 1 | 1 | 0 |
| 🇹🇳 Tunisia | 1 | 1 | 0 |
| 🇿🇼 Zimbabwe | 1 | 1 | 0 |
| 🇪🇬 Egypt | 1 | 1 | 0 |
| 🇪🇹 Ethiopia | 1 | 0 | 1 |
| **Total** | **11** | **7** | **4** |

```mermaid
xychart
    title "Incidents by country — July 2024"
    x-axis ["ZA","DZ","KE","TN","ZW","EG","ET"]
    y-axis "Incidents" 0 --> 4
    bar [3,3,1,1,1,1,1]
```

```mermaid
pie showData
    title Incident-type distribution — July 2024
    "Ransomware" : 7
    "Data leaks" : 4
```

### Regional distribution

| Region | Total | Ransomware | Data leak |
|---|---:|---:|---:|
| North Africa | 5 | 2 | 3 |
| Southern Africa | 4 | 4 | 0 |
| East Africa | 2 | 1 | 1 |
| **Total** | **11** | **7** | **4** |

### Normalized sector distribution

| Sector | Incidents | Share |
|---|---:|---:|
| Healthcare / Medical | 2 | 18.2% |
| Professional / Business Services | 2 | 18.2% |
| Transport / Logistics | 2 | 18.2% |
| Defense / Security | 1 | 9.1% |
| Education / University | 1 | 9.1% |
| Media / Entertainment | 1 | 9.1% |
| Finance / Banking | 1 | 9.1% |
| Mining / Extractive Industries | 1 | 9.1% |
| **Total** | **11** | **100%** |

### Most visible actors and sources

| Actor or source | Incidents |
|---|---:|
| Addka72424, repost attributed to FriendlyChemist | 3 |
| Mad Liberator | 2 |
| Six other actors or sources | 1 each |

## 4. Detailed analysis by incident type

### 4.1 Ransomware

The seven publications concern Maxcess Logistics, National Health Laboratory Service, Kenya Urban Roads Authority, ZB Financial Holdings, Cities Network, Assih, and Sibanye-Stillwater. Mad Liberator appears twice on the same day, but public sources do not technically connect the two cases.

### 4.2 Data leaks

The three Algerian entries are reposts from a compilation advertised as dating from 2019 to 2023. They measure renewed data circulation, not three July intrusions. The Ethiopian case remains attributed to the institution identifiable in the documents, with the cited domain retained as inconsistent and unverified.

## 5. Sectoral impact

Healthcare, professional services, and transport each account for two incidents. The greatest sensitivity concerns visible or claimed medical, education, and military data. Mining and transport organizations mainly face continuity risk that cannot be quantified from publications alone.

## 6. Threat actor profile and risk assessment

| Scope | Level | Rationale |
|---|---|---|
| 🇩🇿 Algeria | 🔴 High | Three recirculated leaks, including healthcare and education |
| 🇿🇦 South Africa | 🔴 High | Three ransomware claims |
| 🇪🇹 Ethiopia | 🔴 High | Visible military documents and inconsistent domain attribution |
| Other countries | 🟠 Medium | One publication per country |

## 7. Key trends and intelligence gaps

- **Observed — high confidence:** seven ransomware incidents and four data leaks.
- **Observed — high confidence:** three Algerian leaks originate from one repost rather than established new intrusions.
- **Gap:** no public DFIR report was identified in the sources reviewed for the ransomware claims.
- **Gap:** the exact organization and technical domain in the Ethiopian case remain partly contradictory.
- **Collection need:** provenance of the Algerian compilation, institutional confirmation, and technical indicators for ransomware cases.

## 8. Contextual MITRE ATT&CK mapping

| Status | Technique | Use |
|---|---|---|
| Preventive | T1486 — Data Encrypted for Impact | Encryption detection; not confirmed in the seven claims |
| Preventive | T1567 — Exfiltration Over Web Service | Outbound monitoring; leak-acquisition method unknown |
| Assumption | T1078 — Valid Accounts | Compromise scenario to investigate; no valid credential observed |

## 9. Recommendations

- **Healthcare and education:** identify old datasets, reset exposed accounts, and monitor republication.
- **Defense:** resolve institutional attribution before public response and protect document systems.
- **Transport and mining:** segment operational environments and test continuity.
- **All organizations:** preserve logs and maintain immutable backups.

## 10. SOC and tactical recommendations

| Qualification | Action |
|---|---|
| **Observed** | Search for accounts and applications referenced in samples; no ransomware chain is confirmed. |
| **Assumption** | Review abnormal authentication, database exports, and archive staging before publication. |
| **Preventive** | Detect mass encryption, backup inhibition, and high-volume outbound transfers. |

## 11. Strategic recommendations

| Priority | Qualification | Measure |
|---:|---|---|
| 1 | **Observed** | Treat data republication and new compromise as separate conditions. |
| 2 | **Assumption** | Investigate links between simultaneous publications without declaring a common campaign. |
| 3 | **Preventive** | Strengthen ASM, phishing-resistant MFA, secret management, and isolated backups. |

## 12. Conclusion

July demonstrates why volume and novelty must be separated. Three of four leaks are older data in circulation, while seven ransomware publications provide limited technical depth. Sound assessment depends on provenance, chronology, and explicit attribution limits.

**AFRINTEL — TLP:CLEAR**

[AFRINTEL repository](https://github.com/Hatchepsoute/AFRINTEL)
