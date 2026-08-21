[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Period](https://img.shields.io/badge/Period-August%202026-lightgrey)
![Incidents](https://img.shields.io/badge/Incidents-9-critical)
![Ransomware](https://img.shields.io/badge/Ransomware-3-red)
![Data Leaks](https://img.shields.io/badge/Data%20Leaks-5-orange)
![Access Sales](https://img.shields.io/badge/Access%20Sales-1-yellow)
![Countries](https://img.shields.io/badge/Countries-5-blueviolet)

# AFRINTEL - Africa cyber statistics
## August 2026

👉🏾 [French version available here](./README_FR.md)

## Methodology note

These statistics derive from [victims.md](../../../CyberAttackAfrica/2026/08-august/victims.md), the English source of truth for August 2026. Each incident is counted once in the global total. No multi-country incident is present this month: the 9 geographic occurrences therefore correspond to the 9 incidents.

Advertised volumes are not treated as confirmed facts. The supplied Afribaba CSV was analyzed, but its geographic attribution remains inconsistent because no Algerian shipping row is visible. Personal data, credentials and sample links are not reproduced.

## 1. Statistical summary

| Indicator | Value |
|---|---:|
| Documented incidents | **9** |
| Ransomware | **3** |
| Data leaks | **5** |
| Access sales | **1** |
| Defacement | **0** |
| Geographic occurrences | **9** |
| Countries represented | **5** |
| Main country | South Africa, 3 |
| Main leak/access country | Algeria, 2 |
| Status profile | 3 unverified; 4 sample published; 2 complete publications claimed |
| Confidence profile | 3 Low; 2 Medium; 3 High; 1 Very High |
| Impact profile | 1 Level 2; 1 Level 3; 7 Level 4 |

### Global breakdown

| Incident type | Count | Percentage |
|---|---:|---:|
| Ransomware | 3 | 33.3% |
| Data leaks | 5 | 55.6% |
| Access sales | 1 | 11.1% |
| **Total** | **9** | **100%** |

~~~mermaid
pie showData
    title Global incident breakdown - August 2026
    "Ransomware" : 3
    "Data leaks" : 5
    "Access sales" : 1
~~~

## 2. Distribution by country

| Country | Occurrences |
|---|---:|
| 🇿🇦 South Africa | 3 |
| 🇩🇿 Algeria | 2 |
| 🇰🇪 Kenya | 2 |
| 🇲🇺 Mauritius | 1 |
| 🇳🇬 Nigeria | 1 |
| **Total** | **9** |

## 3. Ransomware versus leaks and access sales

| Country | Ransomware | Leaks and access sales | Total |
|---|---:|---:|---:|
| South Africa | 1 | 2 | 3 |
| Algeria | 0 | 2 | 2 |
| Kenya | 0 | 2 | 2 |
| Mauritius | 1 | 0 | 1 |
| Nigeria | 1 | 0 | 1 |
| **Total** | **3** | **6** | **9** |

## 4. Regional breakdown

| Region | Occurrences | Ransomware | Leaks and access sales |
|---|---:|---:|---:|
| Southern Africa | 3 | 1 | 2 |
| North Africa | 2 | 0 | 2 |
| East Africa | 2 | 0 | 2 |
| West Africa | 1 | 1 | 0 |
| Indian Ocean | 1 | 1 | 0 |
| **Total** | **9** | **3** | **6** |

## 5. Sector distribution

| Sector | Incidents | Share |
|---|---:|---:|
| Finance / Banking | 3 | 33.3% |
| Government / Administration | 2 | 22.2% |
| Human Resources / Recruitment | 1 | 11.1% |
| Logistics / Courier Services | 1 | 11.1% |
| Media / Publishing | 1 | 11.1% |
| E-commerce / Marketplace | 1 | 11.1% |
| **Total** | **9** | **100%** |

## 6. Most active actors and sources

| Actor or source | Incidents | Main activity |
|---|---:|---|
| exfilar | 2 | Data leaks |
| NullSec Nigeria | 1 | Data leak |
| Florence | 1 | Access sale |
| OriginalCrazyOldFart | 1 | Data leak |
| Panzer | 1 | Ransomware |
| medusalocker | 1 | Ransomware |
| incransom | 1 | Ransomware |
| TelephoneHooliganism | 1 | Data leak |

## 7. CTI trends

- Data leaks account for 5 of the 9 incidents.
- Three incidents concern South Africa and two concern Algeria.
- Reviewed structured samples do not automatically validate advertised volumes.
- The Afribaba case combines a contact claim with an order-history CSV, but observed shipping countries do not include Algeria.
- Cloud environments, recruitment repositories and commerce or payment data remain monitoring priorities.

## 8. SOC monitoring priorities

| Priority | Monitoring focus |
|---|---|
| High | Bulk exports of contacts, orders, HR records and cloud databases |
| High | Anonymous or anomalous access to staging and production environments |
| High | Credential reuse, MFA changes and account creation |
| Medium | Large outbound flows and archive creation before publication |
| Medium | Reposts, misattributed domains and samples with uncertain provenance |

## 9. Conclusion

August 2026 records **9 documented incidents**: 3 ransomware, 5 data leaks and 1 access sale. These statistics describe publications collected by AFRINTEL, not the real frequency of compromises. The Afribaba attribution contradictions should remain explicit in future analysis.

For details, see [victims.md](../../../CyberAttackAfrica/2026/08-august/victims.md).
