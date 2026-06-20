[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Period](https://img.shields.io/badge/Period-May%202026-lightgrey)
![Victims](https://img.shields.io/badge/Victims-54-critical)
![Ransomware](https://img.shields.io/badge/Ransomware-16-red)
![Data Leaks](https://img.shields.io/badge/Data%20Leaks-38-orange)
![Countries](https://img.shields.io/badge/Countries%20Affected-11-blueviolet)
![Intel](https://img.shields.io/badge/Type-CTI%20Statistics-purple)

# AFRINTEL - Africa cyber statistics
## May 2026

👉🏾 [**French version available here**](./README_FR.md)

## Methodology note

These statistics are based on publicly claimed or observed incidents within the AFRINTEL monitoring scope for May 2026. Content originating from cybercriminal forums, leak sites, or underground channels is treated as a **claim** unless independently confirmed by the victim or supported by verifiable technical evidence.

The three multi-country incidents (Resume Docs, DHIS2, Passport Scans) are counted as **1 incident each** in the global total of 54. For regional exposure analysis, they are mapped across affected geographic zones to reflect actual regional exposure.

---

## 1. Statistical summary

| Indicator | Value |
|---|---:|
| Total incidents | 54 |
| Ransomware attacks | 16 |
| Data leaks / access sales | 38 |
| Countries affected | 11 + multi-country |
| Distinct threat actors | 25+ |
| Most affected country | Egypt |
| Main ransomware country | Egypt |
| Main data leak country | South Africa |

### Global breakdown

| Incident type | Count | Percentage |
|---|---:|---:|
| Ransomware | 16 | 29.6% |
| Data leaks / access sales | 38 | 70.4% |
| **Total** | **54** | **100%** |

```mermaid
pie showData
    title Global incident breakdown - May 2026
    "Ransomware" : 16
    "Data leaks and access sales" : 38
```

---

## 2. Victim distribution by country

| Country | Incidents |
|---|---:|
| 🇪🇬 Egypt | 16 |
| 🇿🇦 South Africa | 14 |
| 🇲🇦 Morocco | 5 |
| 🇹🇳 Tunisia | 5 |
| 🇳🇬 Nigeria | 3 |
| 🇩🇿 Algeria | 2 |
| 🇹🇿 Tanzania | 2 |
| 🇬🇭 Ghana | 1 |
| 🇨🇮 Ivory Coast | 1 |
| 🇰🇪 Kenya | 1 |
| 🇸🇳 Senegal | 1 |
| 🌍 Multi-country | 3 |
| **Total** | **54** |

```mermaid
xychart-beta
    title "Victims by country - May 2026"
    x-axis ["Egypt","South Africa","Morocco","Tunisia","Nigeria","Algeria","Tanzania","Ghana","Ivory Coast","Kenya","Senegal","Multi-country"]
    y-axis "Incidents" 0 --> 17
    bar [16,14,5,5,3,2,2,1,1,1,1,3]
```

---

## 3. Ransomware vs data leaks by country

| Country | Ransomware | Data Leaks / Access Sales | Total |
|---|---:|---:|---:|
| 🇪🇬 Egypt | 7 | 9 | 16 |
| 🇿🇦 South Africa | 1 | 13 | 14 |
| 🇲🇦 Morocco | 0 | 5 | 5 |
| 🇹🇳 Tunisia | 2 | 3 | 5 |
| 🇳🇬 Nigeria | 3 | 0 | 3 |
| 🇩🇿 Algeria | 0 | 2 | 2 |
| 🇹🇿 Tanzania | 0 | 2 | 2 |
| 🇬🇭 Ghana | 1 | 0 | 1 |
| 🇨🇮 Ivory Coast | 1 | 0 | 1 |
| 🇰🇪 Kenya | 0 | 1 | 1 |
| 🇸🇳 Senegal | 1 | 0 | 1 |
| 🌍 Multi-country | 0 | 3 | 3 |
| **Total** | **16** | **38** | **54** |

### Ransomware by country

```mermaid
xychart-beta
    title "Ransomware by country - May 2026"
    x-axis ["Egypt","Nigeria","Tunisia","South Africa","Ghana","Senegal","Ivory Coast"]
    y-axis "Ransomware" 0 --> 8
    bar [7,3,2,1,1,1,1]
```

### Data leaks by country

```mermaid
xychart-beta
    title "Data leaks by country - May 2026"
    x-axis ["South Africa","Egypt","Morocco","Tunisia","Multi-country","Algeria","Tanzania","Kenya"]
    y-axis "Data leaks" 0 --> 14
    bar [13,9,5,3,3,2,2,1]
```

---

## 4. Geographic breakdown

| Region | Countries included | Total incidents | Ransomware | Data leaks |
|---|---|---:|---:|---:|
| North Africa | 🇪🇬 Egypt, 🇲🇦 Morocco, 🇹🇳 Tunisia, 🇩🇿 Algeria | 28 (51.9%) | 9 | 19 |
| Southern Africa | 🇿🇦 South Africa | 14 (25.9%) | 1 | 13 |
| West Africa | 🇳🇬 Nigeria, 🇬🇭 Ghana, 🇨🇮 Ivory Coast, 🇸🇳 Senegal | 6 (11.1%) | 5 | 1 |
| East Africa | 🇹🇿 Tanzania, 🇰🇪 Kenya | 3 (5.6%) | 0 | 3 |
| Multi-country | Various | 3 (5.6%) | 0 | 3 |

> Note: Multi-country incidents (Resume Docs, DHIS2, Passport Scans) are counted as one incident each in the global total and assigned to the multi-country category. This view reflects global exposure distribution.

```mermaid
xychart-beta
    title "Regional exposure - May 2026"
    x-axis ["North Africa","Southern Africa","West Africa","East Africa","Multi-country"]
    y-axis "Incidents / exposures" 0 --> 30
    bar [28,14,6,3,3]
```

---

## 5. Sector distribution

| Sector | Incidents | Percentage |
|---|---:|---:|
| Government / Administration | 14 | 25.9% |
| Recruitment / Personal Data | 8 | 14.8% |
| Education / University | 5 | 9.3% |
| Finance / Banking | 4 | 7.4% |
| Food / Beverage / Hospitality | 4 | 7.4% |
| Logistics / Transport | 3 | 5.6% |
| Automotive | 3 | 5.6% |
| E-commerce / Digital | 3 | 5.6% |
| Telecom / ICT | 3 | 5.6% |
| NGO / Charity | 2 | 3.7% |
| Healthcare | 2 | 3.7% |
| Others | 3 | 5.6% |
| **Total** | **54** | **100%** |

```mermaid
xychart-beta
    title "Sector distribution - May 2026"
    x-axis ["Government","Recruitment/Data","Education","Finance","Food/Hospitality","Logistics","Automotive","E-commerce","Telecom","NGO","Healthcare","Others"]
    y-axis "Incidents" 0 --> 15
    bar [14,8,5,4,4,3,3,3,3,2,2,3]
```

---

## 6. Most active threat actors

| Threat actor / Group | Incidents | Dominant type |
|---|---:|---|
| Databasehooligan | 8 | Data leaks |
| TheGentlemen | 4 | Ransomware |
| 404Crew Cyber Team | 4 | Data leaks (coalitions) |
| NightSpire | 3 | Ransomware |
| INT3X | 2 | Data leaks |
| Keymous | 2 | Access sales / data leaks |
| cc5ab | 2 | Data leaks |
| NullSec Nigeria | 2 | Data leaks (coalitions) |
| Other actors | 27 | Mixed |

```mermaid
xychart-beta
    title "Most active threat actors - May 2026"
    x-axis ["Databasehooligan","TheGentlemen","404Crew CT","NightSpire","INT3X","Keymous","cc5ab","NullSec NG","Others"]
    y-axis "Incidents" 0 --> 30
    bar [8,4,4,3,2,2,2,2,27]
```

---

## 7. CTI trend analysis

### 7.1 Egypt as the main ransomware hotspot

Egypt accounts for **7 ransomware incidents**, representing **43.8%** of ransomware activity. NightSpire alone claimed three Egyptian targets in a single month. Targeted sectors include finance, food, chemical industry, logistics, agriculture, and hospitality.

### 7.2 South Africa under coordinated pressure

South Africa recorded **14 incidents** including 13 data leaks driven by the 404Crew Cyber Team coalition (with NullSec Nigeria, NullSec Philippines, and Infernalis) under the "OpSouthAfrica" banner. Targeted institutions include municipalities, correctional services, tax authority, and state IT infrastructure.

### 7.3 Education sector as a strategic target

Egypt's education system faced systemic exposure: Ministry of Education (26.8M student records), Professional Academy for Teachers (1.2M teacher records), Mansoura University (989K records), and a combined Educational & HR database (37 GB). Total exposure exceeds 28 million records.

### 7.4 Databasehooligan dominance in CRM / recruitment platforms

A single data broker targeted eight organizations across four countries (Tunisia, South Africa, Egypt, Algeria), selling structured CRM and consumer databases for $900-$1,400 each. This suggests systematic exploitation of a shared vulnerability or a common SaaS platform.

### 7.5 Government credential exposure

Moroccan government platforms (827K credential lines), the Tanzania Police webmail (10,000+ officer accounts with plaintext passwords), and Stats SA admin access represent high-value targets for social engineering, EDR fraud, and law enforcement impersonation.

### 7.6 Multi-country health system compromise

The DHIS2 admin access sale (seven countries: Mozambique, Liberia, Nigeria, Bhutan, Honduras, Togo, Sierra Leone) poses a critical threat to national public health surveillance infrastructure.

---

## 8. SOC monitoring priorities

| Priority | Monitoring focus |
|---|---|
| Critical | Credential exposure in government and law enforcement systems |
| Critical | Education database access patterns (Egypt: Ministry of Education, PAT, Mansoura) |
| High | CRM / recruitment platform bulk exports (Databasehooligan targets) |
| High | Ransomware early indicators: shadow copy deletion, volume encryption, lateral RDP/SMB |
| High | Government credential reuse from Moroccan government platform leaks |
| Medium | NightSpire / TheGentlemen target profile alignment (finance, food, automotive) |
| Medium | DHIS2 / health system admin panel anomalies |
| Medium | Multi-country EDR fraud account listings |

---

## 9. Conclusion

May 2026 recorded **54 incidents** across **11 countries** plus multi-country events. Egypt and South Africa jointly absorbed 56% of incidents, confirming their status as primary targets on the continent. The systematic targeting of Egypt's education sector, the coordinated OpSouthAfrica campaign, and Databasehooligan's CRM sweep across four countries are the defining patterns of the month.

**AFRINTEL** - [African Cyber Threat Intelligence](https://github.com/Hatchepsoute/AFRINTEL)
