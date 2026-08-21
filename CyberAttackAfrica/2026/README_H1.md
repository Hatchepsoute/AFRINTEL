[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Period](https://img.shields.io/badge/Period-H1%202026-lightgrey)
![Incidents](https://img.shields.io/badge/Incidents-294-critical)

# AFRINTEL first-half cyber threat report

## January to June 2026

👉🏾 [Version française](./README_H1_FR.md)

TLP:CLEAR, public distribution

## 1. Executive summary

AFRINTEL documented **294 Africa-related cyber incidents** during the first half of 2026: **115 ransomware incidents**, **125 data leaks or access sales**, **52 DDoS claims**, and **2 website defacements**.

Across all 294 records, **data leaks / access sales account for 42.5%**, **ransomware 39.1%**, **DDoS claims 17.7%**, and **website defacement 0.7%**. Considering only ransomware and data leaks / access sales, leaks lead **52.1% to 47.9%**.

The real story is how activity accelerated in the second quarter. April and May alone accounted for **172 incidents**, or **58.5%** of the semester. June eased off from both, but ransomware came back to parity with data leaks, 20 incidents each.

## 2. Methodology and scope

- **Geographic scope:** African victims, institutions, operations or affected datasets.
- **Period:** 1 January to 30 June 2026.
- **Single sources of truth:** the six monthly `victims.md` files.
- **Ransomware:** incidents attributed to a ransomware group, without assuming encryption when no supporting evidence is available.
- **Data leaks and access sales:** published or sampled datasets, database sales, credential sales and access offers.
- **Website defacement:** two incidents, involving Nigerien state websites in January and UBA Senegal in March.
- **Evidence treatment:** each record retains its AFRINTEL status. Victim listings, accessible samples and full data publications are described according to the material documented in the monthly card.

Source files: [January](./01-january/victims.md), [February](./02-february/victims.md), [March](./03-march/victims.md), [April](./04-april/victims.md), [May](./05-may/victims.md), [June](./06-june/victims.md).

## 3. Semester overview

| Indicator | Value |
|---|---:|
| Total documented incidents | 294 |
| Ransomware | 115 |
| Data leaks / access sales | 125 |
| DDoS claims | 52 |
| Website defacement | 2 |
| Highest-volume month | May, 103 incidents |
| Second-highest month | April, 69 incidents |
| Lowest-volume month | February, 20 incidents |

**Visual distribution**

| Incident type | Records | Bar |
|---|---:|:---|
| Ransomware | 115 | 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧 |
| Data leaks and access sales | 125 | 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| DDoS claims | 52 | 🟪🟪🟪🟪 |
| Website defacement | 2 | 🟥 |


<!-- H1_VISUAL_START -->

### Ransomware, leaks, DDoS and defacement by country

| Country | Ransomware | Leaks / access | DDoS | Defacement | Total | Distribution |
| :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| Morocco | 10 | 36 | 43 | 0 | **89** | 🟧×10 🟦×36 🟪×43 |
| Egypt | 28 | 19 | 8 | 0 | **55** | 🟧×28 🟦×19 🟪×8 |
| South Africa | 25 | 23 | 0 | 0 | **48** | 🟧×25 🟦×23 |
| Tunisia | 8 | 8 | 0 | 0 | **16** | 🟧×8 🟦×8 |
| Nigeria | 6 | 9 | 0 | 0 | **15** | 🟧×6 🟦×9 |
| Kenya | 7 | 2 | 0 | 0 | **9** | 🟧×7 🟦×2 |
| Algeria | 1 | 7 | 0 | 0 | **8** | 🟧×1 🟦×7 |
| Senegal | 3 | 2 | 0 | 1 | **6** | 🟧×3 🟦×2 🟥×1 |
| Tanzania | 3 | 3 | 0 | 0 | **6** | 🟧×3 🟦×3 |
| Ghana | 5 | 0 | 0 | 0 | **5** | 🟧×5 |

### Expanded geographic exposure distribution by region

| Region | Ransomware occurrences | Leaks / access occurrences | DDoS occurrences | Defacement occurrences | Total geographic occurrences |
| :--- | ---: | ---: | ---: | ---: | ---: |
| North Africa | 49 | 78 | 52 | 0 | 179 |
| Southern Africa | 32 | 30 | 0 | 0 | 62 |
| West Africa | 16 | 22 | 0 | 2 | 40 |
| Central Africa | 1 | 2 | 0 | 0 | 3 |
| East Africa | 11 | 15 | 0 | 0 | 26 |
| Indian Ocean | 6 | 0 | 0 | 0 | 6 |
| Pan-African / region unspecified | 0 | 1 | 0 | 0 | 1 |
| **Total** | **115** | **148** | **52** | **2** | **317** |

This regional ranking uses **geographic occurrences**, not deduplicated incidents. Six explicitly multi-country incidents expand to 29 country occurrences; one additional pan-African incident has no sufficiently precise regional allocation.

**Bars - Top 10 countries - H1 2026**

| Label | Records | Bar |
|---|---:|:---|
| Morocco | 89 | ██████████████████ |
| Egypt | 55 | ███████████ |
| South Africa | 48 | ██████████ |
| Tunisia | 16 | ███ |
| Nigeria | 15 | ███ |
| Kenya | 9 | ██ |
| Algeria | 8 | ██ |
| Senegal | 6 | █ |
| Tanzania | 6 | █ |
| Ghana | 5 | █ |

### Sector distribution

This sector view covers **239 normalized records**. It should not be read as a decomposition of all 294 incident records.

| Sector | Records | Share | Activity |
| :--- | ---: | ---: | :--- |
| Government / Administration | 70 | 29.3% | ██████████ |
| Industry / Automotive / Manufacturing / Construction / Mining | 25 | 10.5% | ████ |
| Finance / Banking | 25 | 10.5% | ████ |
| Education / University / Academic institutions | 19 | 7.9% | ███ |
| Technology / Digital / Business services / Digital identity | 15 | 6.3% | ███ |
| Healthcare / Medical | 12 | 5.0% | ██ |
| Sports / Federations | 12 | 5.0% | ██ |
| E-commerce / Retail | 12 | 5.0% | ██ |
| Other normalized sectors | 49 | 20.5% | ███████ |
| **Total normalized records** | **239** | **100%** | |

**Bars - Top sectors - H1 2026**

| Label | Records | Bar |
|---|---:|:---|
| Government / Administration | 70 | ██████████ |
| Industry / Automotive / Manufacturing / Construction / Mining | 25 | ████ |
| Finance / Banking | 25 | ████ |
| Education / University / Academic institutions | 19 | ███ |
| Technology / Digital / Business services / Digital identity | 15 | ███ |
| Healthcare / Medical | 12 | ██ |
| Sports / Federations | 12 | ██ |
| E-commerce / Retail | 12 | ██ |

🟧 Ransomware | 🟦 Leaks and access sales | 🟪 DDoS | 🟥 Defacement
<!-- H1_VISUAL_END -->
## 4. Monthly evolution

| Month | Ransomware | Data leaks / access sales | DDoS | Website defacement | Total | Monthly share |
|---|---:|---:|---:|---:|---:|---:|
| January | 17 | 3 | 0 | 1 | 21 | 7.1% |
| February | 20 | 0 | 0 | 0 | 20 | 6.8% |
| March | 21 | 19 | 0 | 1 | 41 | 13.9% |
| April | 20 | 40 | 9 | 0 | 69 | 23.5% |
| May | 17 | 43 | 43 | 0 | 103 | 35.0% |
| June | 20 | 20 | 0 | 0 | 40 | 13.6% |
| **H1 2026** | **115** | **125** | **52** | **2** | **294** | **100%** |

**Bars - Monthly cyber incidents in Africa, H1 2026**

| Label | Records | Bar |
|---|---:|:---|
| Jan | 21 | ████ |
| Feb | 20 | ████ |
| Mar | 41 | ███████ |
| Apr | 69 | ██████████ |
| May | 103 | █████████████████ |
| Jun | 40 | ███████ |

### Ransomware and leak evolution

**Bars - Ransomware activity, H1 2026**

| Label | Records | Bar |
|---|---:|:---|
| Jan | 17 | █████████ |
| Feb | 20 | ██████████ |
| Mar | 21 | ██████████ |
| Apr | 20 | ██████████ |
| May | 17 | █████████ |
| Jun | 20 | ██████████ |

**Bars - Data leaks and access sales, H1 2026**

| Label | Records | Bar |
|---|---:|:---|
| Jan | 3 | █ |
| Feb | 0 |  |
| Mar | 19 | █████ |
| Apr | 40 | ██████████ |
| May | 43 | ██████████ |
| Jun | 20 | █████ |

## 5. Quarter comparison

| Period | Ransomware | Data leaks / access sales | DDoS | Website defacement | Total |
|---|---:|---:|---:|---:|---:|
| First quarter, January to March | 58 | 22 | 0 | 2 | 82 |
| Second quarter, April to June | 57 | 103 | 52 | 0 | 212 |
| **H1 2026** | **115** | **125** | **52** | **2** | **294** |

The second quarter ran **130 incidents ahead of the first**, a **158.5% increase** over Q1. Ransomware decreased slightly, from 58 incidents in Q1 to 57 in Q2. Data leaks and access sales rose from 22 to 103 incidents (**+368.2%**), while **52 DDoS claims** were recorded in Q2 after none in Q1.

## 6. Key CTI findings

1. **Ransomware held steady rather than accelerating.** Monthly volume stayed within the 17-to-21 range.
2. **Data leaks drove the second quarter.** April and May alone produced 83 data leaks or access sales, compared with 22 during the entire first quarter; the same two months also accounted for all 52 DDoS claims recorded in H1.
3. **June shifted the balance without returning to Q1 conditions.** Total volume came down from the April-May peak, but ransomware returned to half of the month's incidents.
4. **The semester was geographically concentrated.** Morocco, Egypt and South Africa account for **192 of 294 incident records (65.3%)** when all incident types are included.
5. **Government and administration led the normalized sector view.** They account for 70 of 239 sector-normalized records (29.3%), with Industry/Automotive/Manufacturing/Construction/Mining and Finance/Banking tied behind at 25 each.
6. **A name repeating across months is not proof of one shared intrusion.** Cross-month activity under the same source account is recorded as continuity of publication unless the source cards establish a common access vector.

## 7. Intelligence limitations

- The total represents 294 incident records, each counted according to its structured AFRINTEL status.
- Cross-month victim deduplication has not been completed.
- A multi-country record counts once in the global total and several times only in the expanded geographic view.
- Actor names were normalized for obvious spelling and version variants. Composite coalition labels were not decomposed into individual actor counts.
- Sector labels were normalized from the explicit sector and organization description in each source card. Each card is counted once.
- Initial access, encryption and operational impact are not documented for many ransomware listings.

## 8. SOC and defensive priorities

### Evidence-backed H1 priorities

| Direct country label | Records | Bar |
|---|---:|:---|
| 🇲🇦 Morocco | 89 | ██████████████████ |
| 🇪🇬 Egypt | 55 | ███████████ |
| 🇿🇦 South Africa | 48 | ██████████ |
| 🇹🇳 Tunisia | 16 | ████ |
| 🇳🇬 Nigeria | 15 | ████ |
| 🇰🇪 Kenya | 9 | ██ |
| 🇩🇿 Algeria | 8 | ██ |
| 🇹🇿 Tanzania | 6 | ██ |
| 🇸🇳 Senegal | 6 | ██ |
| 🇬🇭 Ghana | 5 | ██ |
| 🇲🇺 Mauritius | 3 | █ |
| 🇱🇾 Libya | 3 | █ |
| 🇿🇲 Zambia | 2 | █ |
| 🇳🇦 Namibia | 2 | █ |
| 🇨🇮 Ivory Coast | 2 | █ |
| 🇪🇹 Ethiopia | 2 | █ |
| 🇧🇼 Botswana | 2 | █ |
| 🇸🇩 Sudan | 2 | █ |
| 🇿🇼 Zimbabwe | 1 | █ |
| 🇺🇬 Uganda | 1 | █ |
| 🇹🇬 Togo | 1 | █ |
| 🇸🇴 Somalia | 1 | █ |
| 🇸🇨 Seychelles | 1 | █ |
| 🇳🇪 Niger | 1 | █ |
| 🇲🇿 Mozambique | 1 | █ |
| 🇾🇹 Mayotte | 1 | █ |
| 🇲🇬 Madagascar | 1 | █ |
| 🇬🇳 Guinea | 1 | █ |
| 🇬🇦 Gabon | 1 | █ |
| 🇧🇯 Benin | 1 | █ |
| **Single-country records** | **287** | |

The top three direct country labels account for **192 records (65.3%)**. The corpus also contains six explicitly multi-country incidents and one pan-African incident without a precise country allocation, bringing the incident total to 294.

| Normalized sector | Records | Bar |
|---|---:|:---|
| Government / Administration | 70 | ██████████ |
| Industry / Automotive / Manufacturing / Construction / Mining | 25 | ████ |
| Finance / Banking | 25 | ████ |
| Education / University / Academic institutions | 19 | ███ |
| Technology / Digital / Business services / Digital identity | 15 | ███ |
| Healthcare / Medical | 12 | ██ |
| Sports / Federations | 12 | ██ |
| E-commerce / Retail | 12 | ██ |
| Food / Beverage / Agriculture | 8 | ██ |
| Transport / Logistics / Aviation | 8 | ██ |
| Oil & Energy | 8 | ██ |
| Telecommunications | 5 | █ |
| Human Resources / Recruitment | 5 | █ |
| NGO / Social Welfare | 3 | █ |
| Hospitality / Events / Tourism | 3 | █ |
| Media / Audiovisual | 2 | █ |
| Personal Data Aggregation | 2 | █ |
| Legal Services | 1 | █ |
| Real Estate | 1 | █ |
| Research / Think tank | 1 | █ |
| Political Organizations / Parties | 1 | █ |
| Security Services | 1 | █ |
| **Total normalized records** | **239** | |

This normalized sector view covers **239 records** and is not a full decomposition of the 294 incident records. Nundun Gopee & Co Ltd is classified under Construction / Real Estate.

#### Most represented normalized actor labels

| Actor or group | Records | Bar |
|---|---:|:---|
| anisanas2 | 10 | ██████████ |
| TheGentlemen | 7 | ███████ |
| Databasehooligan | 7 | ███████ |
| 404Crew Cyber Team | 7 | ███████ |
| CrowStealer | 6 | ██████ |
| NightSpire | 6 | ██████ |
| LockBit 5 | 5 | █████ |
| Qilin | 4 | ████ |
| DeadLock | 4 | ████ |
| APT73 / Bashe | 4 | ████ |
| XP95 | 3 | ███ |
| xNov | 3 | ███ |
| Keymous | 3 | ███ |

Actor-name case and version variants are normalized in the counts and charts.

#### Expanded multi-country exposure

| Month | Source card | African countries explicitly listed | Exposures |
|---|---|---|---:|
| April | Government data leak and administrative access sale | Angola, South Africa, Nigeria | 3 |
| May | Resume-document leak | Kenya, Ethiopia, Nigeria, Zimbabwe | 4 |
| May | Regional multi-country listing | Mozambique, Liberia, Nigeria, Togo, Sierra Leone | 5 |
| May | Egypt / Libya listing | Egypt, Libya | 2 |
| June | Government email sale | Ethiopia, Tanzania, Angola, Kenya, Zambia, Nigeria, Egypt, Morocco | 8 |
| June | Law-enforcement portal access sale | Egypt, Malawi, Tanzania, Algeria, Kenya, Zambia, Sierra Leone | 7 |
| **Total** | **6 source cards** | | **29 country exposures** |

The incident total is **294**. Replacing the six explicitly multi-country incidents with their 29 African country occurrences produces **317 geographic exposure occurrences**: **287 single-country incidents**, **29 expanded country occurrences**, and **1 pan-African incident** without a precise regional allocation. The expanded view covers **34 distinct African countries**.

- Prioritize identity, VPN, email, cloud-storage and privileged-account telemetry.
- Track victim listings, encryption evidence and data publication as separate fields.
- Detect unusual bulk exports, database dumps and public-cloud object exposure.
- Enforce MFA for government, education, financial and healthcare portals.
- Establish rapid credential revocation workflows for leaked government and military accounts.
- Normalize actor names across months to avoid duplicate counts.
- Preserve the original claim date, AFRINTEL discovery date and publication date.

## 9. Strategic outlook

### Intelligence gaps

- It is not possible to separate actual activity growth from improved collection coverage using repository data alone.
- The operators behind several unnamed platforms and multi-organization datasets remain unidentified.
- Composite actor labels and coalition publications limit precise actor-level attribution.
- The June return to a 50/50 ransomware versus leak split is one monthly observation, not an established second-half trend.

### Contextual MITRE ATT&CK coverage

| Technique | Name | Defensive use |
|---|---|---|
| T1078 | Valid Accounts | Monitor access-sale and exposed-credential scenarios |
| T1041 | Exfiltration Over C2 Channel | Detection hypothesis for unusual outbound transfers |
| T1537 | Transfer Data to Cloud Account | Monitor cloud data movement |
| T1486 | Data Encrypted for Impact | Apply only when encryption is independently observed |

No technique is attributed to a specific H1 incident without supporting telemetry.

The first half of 2026 shows two risks running in parallel. Ransomware held a stable operational baseline throughout, while data leaks and access sales expanded sharply in the second quarter. Calling the semester a simple ransomware wave would miss the point. The bigger structural shift was the growth of data brokerage, credential exposure and structured-dataset publication.

Going into the second half, AFRINTEL should watch whether June's 50/50 split turns into a sustained ransomware recovery or was just a temporary correction after the April-May leak peak.

## 10. Conclusion

AFRINTEL recorded **294 incidents across H1 2026**: **115 ransomware**, **125 data leaks or access sales**, **52 DDoS claims** and **2 defacements**. The second quarter carried **212 records (72.1%)** of the semester's activity. The Q2 increase was driven by data leaks / access sales and DDoS claims, partly offset by the slight decrease in ransomware and the absence of defacement records in Q2.

The defensive priority runs two tracks at once: keep ransomware readiness up while tightening controls against credential exposure, bulk data extraction, cloud-storage exposure and underground data sales.

### Consistency checks

- Monthly totals: 21 + 20 + 41 + 69 + 103 + 40 = 294.
- Type totals: 115 + 125 + 52 + 2 = 294.
- Direct geography: 287 single-country incidents + 6 explicitly multi-country incidents + 1 pan-African incident = 294.
- Expanded geography: 287 single-country incidents + 29 expanded country occurrences + 1 pan-African occurrence = 317.
- Regional occurrence totals: 115 ransomware + 148 leaks / access occurrences + 52 DDoS + 2 defacements = 317.
- Sector-normalized table: the 22 explicit sector rows sum to 239 records.

---

**AFRINTEL**  
Open African CTI Monitoring Initiative  
[GitHub repository](https://github.com/Hatchepsoute/AFRINTEL)
