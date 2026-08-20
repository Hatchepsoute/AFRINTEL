[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Period](https://img.shields.io/badge/Period-July%202026-lightgrey)
![Incidents](https://img.shields.io/badge/Incidents-42-critical)
![Ransomware](https://img.shields.io/badge/Ransomware-18-red)
![Data Leaks](https://img.shields.io/badge/Data%20Leaks-18-orange)
![Access Sales](https://img.shields.io/badge/Access%20Sales-6-yellow)
![Countries](https://img.shields.io/badge/Countries-12-blueviolet)

# AFRINTEL - Africa cyber statistics
## July 2026

👉🏾 [French version available here](./README_FR.md)

## Methodology note

These English statistics derive from [`victims.md`](../../../CyberAttackAfrica/2026/07-july/victims.md), the source of truth for the English version for July 2026. Each card is counted once in the global total. One identity-document card concerns both Nigeria and Côte d’Ivoire, so the geographic view contains 43 occurrences for 42 incident records. The MTN record is allocated to South Africa for the working geographic view, although the national entity is not confirmed.

Claimed volumes are not treated as confirmed facts. Personal data, credentials and download links are not reproduced.

## 1. Statistical summary

| Indicator | Value |
|---|---:|
| Total incidents | **42** |
| Ransomware | **18** |
| Data leaks | **18** |
| Access sales | **6** |
| Defacements | **0** |
| Geographic occurrences | **43** |
| Countries represented | **12** |
| Most represented countries | Egypt and Tunisia, 7 each |
| Main ransomware country | South Africa, 5 |
| Main leak and access country | Tunisia, 7 |
| Status profile | 21 unverified; 20 sample published; 1 complete publication claimed (`Data Fully Published`) |
| Confidence profile | 22 Low; 8 Medium; 9 High; 3 Very High |
| Impact profile | 12 Level 2; 21 Level 3; 9 Level 4 |

### Global breakdown

| Incident type | Count | Percentage |
|---|---:|---:|
| Ransomware | 18 | 42.9% |
| Data leaks | 18 | 42.9% |
| Access sales | 6 | 14.3% |
| **Total** | **42** | **100%** |

~~~mermaid
pie showData
    title Global incident breakdown - July 2026
    "Ransomware" : 18
    "Data leaks" : 18
    "Access sales" : 6
~~~

## 2. Victim distribution by country

| Country | Geographic occurrences |
|---|---:|
| 🇪🇬 Egypt | 7 |
| 🇹🇳 Tunisia | 7 |
| 🇲🇦 Morocco | 6 |
| 🇿🇦 South Africa | 6 |
| 🇳🇬 Nigeria | 4 |
| 🇩🇿 Algeria | 4 |
| 🇨🇮 Côte d’Ivoire | 3 |
| 🇬🇭 Ghana | 2 |
| 🇧🇼 Botswana | 1 |
| 🇨🇲 Cameroon | 1 |
| 🇰🇪 Kenya | 1 |
| 🇸🇸 South Sudan | 1 |
| **Total** | **43** |

~~~mermaid
xychart-beta
    title "Geographic occurrences by country - July 2026"
    x-axis ["Egypt","Tunisia","Morocco","South Africa","Nigeria","Algeria","Côte d’Ivoire","Ghana","Botswana","Cameroon","Kenya","South Sudan"]
    y-axis "Occurrences" 0 --> 8
    bar [7,7,6,6,4,4,3,2,1,1,1,1]
~~~

## 3. Ransomware versus leaks and access sales

| Country | Ransomware | Leaks and access sales | Total occurrences |
|---|---:|---:|---:|
| Egypt | 2 | 5 | 7 |
| Tunisia | 0 | 7 | 7 |
| Morocco | 2 | 4 | 6 |
| South Africa | 5 | 1 | 6 |
| Nigeria | 2 | 2 | 4 |
| Algeria | 0 | 4 | 4 |
| Côte d’Ivoire | 2 | 1 | 3 |
| Ghana | 1 | 1 | 2 |
| Cameroon | 1 | 0 | 1 |
| Botswana | 1 | 0 | 1 |
| Kenya | 1 | 0 | 1 |
| South Sudan | 1 | 0 | 1 |
| **Total** | **18** | **25** | **43** |

The 25 leak and access occurrences include the additional country allocation for the Nigeria and Côte d’Ivoire identity-document card.

## 4. Geographic breakdown

| Region | Countries included | Occurrences | Ransomware | Leaks and access sales | Distribution |
|---|---|---:|---:|---:|---|
| North Africa | Egypt, Tunisia, Morocco, Algeria | **24** | 4 | 20 | 🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Southern Africa | South Africa, Botswana | **7** | 6 | 1 | 🟧🟧🟧🟧🟧🟧 🟦 |
| West and Central Africa | Nigeria, Côte d’Ivoire, Ghana, Cameroon | **10** | 6 | 4 | 🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦 |
| East Africa | Kenya, South Sudan | **2** | 2 | 0 | 🟧🟧 |
| **Total** | **12 countries** | **43** | **18** | **25** | *🟧 Ransomware \| 🟦 Leaks and access sales* |

~~~mermaid
xychart-beta
    title "Geographic occurrences by region - July 2026"
    x-axis ["North Africa","Southern Africa","West and Central Africa","East Africa"]
    y-axis "Occurrences" 0 --> 26
    bar [24,7,10,2]
~~~

## 5. Sector distribution

| Sector | Records | Share | Chart |
|---|---:|---:|---:|
| Government / Administration | 11 | 26.2% | ███████████ |
| Telecommunications | 4 | 9.5% | ████ |
| Healthcare / Medical | 4 | 9.5% | ████ |
| Engineering / Construction | 3 | 7.1% | ███ |
| Education / University | 3 | 7.1% | ███ |
| E-commerce / Retail | 3 | 7.1% | ███ |
| Oil and Energy | 2 | 4.8% | ██ |
| Investment Holding / Energy | 1 | 2.4% | █ |
| Finance / Banking | 1 | 2.4% | █ |
| Transport / Logistics | 1 | 2.4% | █ |
| Real Estate | 1 | 2.4% | █ |
| Mining | 1 | 2.4% | █ |
| Accounting / Audit | 1 | 2.4% | █ |
| Travel / Events | 1 | 2.4% | █ |
| Chemical Industry | 1 | 2.4% | █ |
| Security Services | 1 | 2.4% | █ |
| Gaming / Entertainment | 1 | 2.4% | █ |
| Rubber / Agriculture | 1 | 2.4% | █ |
| Technology / IT | 1 | 2.4% | █ |
| **Total** | **42** | **100%** |  |
~~~mermaid
xychart-beta
    title "Top represented sectors - July 2026"
    x-axis ["Government","Telecommunications","Healthcare","Engineering","Education","Retail","Energy"]
    y-axis "Records" 0 --> 12
    bar [11,4,4,3,3,3,2]
~~~

## 6. Most active threat actors and sources

| Actor or source | Records | Main activity |
|---|---:|---|
| arcusmedia | 4 | Ransomware |
| dragonforce | 3 | Ransomware |
| CrowStealer | 2 | Data leaks |
| krybit | 2 | Ransomware |
| BIGBROTHER | 2 | Access sales and reposts |
| TheGentlemen | 2 | Ransomware |
| Phantom Atlas | 2 | Data leaks |
| GreYyM3terr | 2 | Access sales |

Twenty-three other named actors or source accounts occur once each and are excluded from the ranking rather than grouped into a residual category.

## 7. CTI trend analysis

- Ransomware and data leaks each represent 18 records.
- Six access offers concern public, telecom or administrative environments.
- Identity and passport-related material appears in several records.
- Government and administration remain the largest sector group.
- Planet Sport and Adex illustrate the difficulty of separating new compromises from reposts.
- Evidence quality ranges from structured exports to unsupported claims.

## 8. SOC monitoring priorities

| Priority | Monitoring focus |
|---|---|
| High | Privileged access, VPN, webmail and exposed administrative portals |
| High | Bulk exports from identity, healthcare, education and payment repositories |
| High | New administrator accounts, privilege escalation and unusual sessions |
| Medium | Credential reuse, account recovery abuse and abnormal payment activity |
| Medium | Reposted leak material and access-sale listings involving national subsidiaries |

## 9. Conclusion

July 2026 recorded **42 incident records** and **43 geographic occurrences**. Ransomware and data leaks were evenly represented, while six access-sale offers added a separate access-brokerage risk. North Africa concentrated leak and access activity; South Africa and West and Central Africa showed stronger ransomware pressure.

For details, consult the monthly victim cards in [CyberAttackAfrica/2026/07-july/victims.md](../../../CyberAttackAfrica/2026/07-july/victims.md).
