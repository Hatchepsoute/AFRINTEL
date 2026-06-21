[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Breach-red)
![Period](https://img.shields.io/badge/Period-May%202026-lightgrey)
![Intel Type](https://img.shields.io/badge/Intel%20Type-CTI-purple)

# CTI report - cyberattacks in Africa (May 2026)

👉🏾 [**French version available here**](./README_FR.md)

## 1. Executive summary

May 2026 recorded **54 publicly claimed cyber incidents** across Africa: **16 ransomware attacks** and **38 data leaks / access sales**. The month was marked by a sustained assault on the Egyptian education sector, a coordinated campaign against South African public institutions (OpSouthAfrica), the dominance of the **Databasehooligan** data broker across four countries, and three NightSpire ransomware hits against Egyptian targets in a single month.

Key findings:
- **16 ransomware attacks (29.6%)** and **38 data leaks / access sales (70.4%)**.
- **11 countries** affected, plus 3 multi-country incidents; **Egypt** (16 incidents), **South Africa** (14), **Morocco** (5), and **Tunisia** (5) account for 74% of victims.
- **TheGentlemen** ransomware group hit four countries in one month (Egypt, Tunisia, Ghana, Ivory Coast); **NightSpire** claimed three Egyptian targets.
- **Databasehooligan** dominated data broker activity with 8 victims across Tunisia, South Africa, Egypt, and Algeria.
- Egyptian education sector under systemic attack: Ministry of Education (26.8M student records), Professional Academy for Teachers (1.2M teacher records), Mansoura University (989K records), and a joint Educational & HR database (37 GB).
- Tanzania Police webmail leaked: 10,000+ officer accounts with plaintext passwords offered for sale.
- Trésor Public du Sénégal (national treasury): AuditTeam ransomware with confirmed data exfiltration (~1.66M records across three Oracle databases plus 18 months of SICA payroll files).

### Victim list

👉🏾 [View full victim list](./victims.md)

---

## 2. Methodology

- **Scope**: 54 African countries.
- **Period**: 1-31 May 2026 (incidents disclosed or claimed during this month; actual attack dates may be earlier).
- **Sources**: Dark web, DLS (leak sites), OSINT, Telegram channels, underground forums.
- **Inclusion**: Publicly claimed or attributed incidents with identified victim, country, and sector.
- **Typology**:
  - *Ransomware*: encryption + ransom demand.
  - *Data leak / access sale*: exfiltration without encryption, database sold/published, or access sale to compromised systems.

> All claims from cybercriminal forums, leak sites, and underground channels are treated as **unverified claims** unless independently corroborated.

---

## 3. Global overview

| Indicator | Value |
|---|---|
| Total victims | 54 |
| Countries affected | 18 (11 direct + 7 via multi-country incidents) |
| Distinct actors | 25+ |
| Ransomware incidents | 16 (29.6%) |
| Data leaks / access sales | 38 (70.4%) |

### Country ranking

**All incidents combined (54):**

| Rank | Country | Incidents | Chart |
| :---: | :--- | :---: | :--- |
| **1** | 🇪🇬 Egypt | **16** | ████████████████ |
| **2** | 🇿🇦 South Africa | **14** | ██████████████ |
| **3** | 🇲🇦 Morocco | **5** | █████ |
| **4** | 🇹🇳 Tunisia | **5** | █████ |
| **5** | 🇳🇬 Nigeria | **3** | ███ |
| **6** | 🇩🇿 Algeria | **2** | ██ |
| **7** | 🇹🇿 Tanzania | **2** | ██ |
| **8** | 🇬🇭 Ghana | **1** | █ |
| **9** | 🇨🇮 Ivory Coast | **1** | █ |
| **10** | 🇰🇪 Kenya | **1** | █ |
| **11** | 🇸🇳 Senegal | **1** | █ |
| **–** | 🇰🇪 Kenya / 🇪🇹 Ethiopia / 🇳🇬 Nigeria / 🇿🇼 Zimbabwe (Resume docs) | **1** | █ |
| **–** | 🇲🇿 Mozambique / 🇱🇷 Liberia / 🇳🇬 Nigeria / 🇹🇬 Togo / 🇸🇱 Sierra Leone (DHIS2) | **1** | █ |
| **–** | 🇪🇬 Egypt / 🇱🇾 Libya (Passport scans) | **1** | █ |

```mermaid
pie showData
    title Victims distribution by country - May 2026
    "🇪🇬 Egypt" : 16
    "🇿🇦 South Africa" : 14
    "🇲🇦 Morocco" : 5
    "🇹🇳 Tunisia" : 5
    "🇳🇬 Nigeria" : 3
    "🇩🇿 Algeria" : 2
    "🇹🇿 Tanzania" : 2
    "🇬🇭 Ghana" : 1
    "🇨🇮 Ivory Coast" : 1
    "🇰🇪 Kenya" : 1
    "🇸🇳 Senegal" : 1
    "Resume docs (KE/ET/NG/ZW)" : 1
    "DHIS2 (MZ/LR/NG/TG/SL)" : 1
    "Passport scans (EG/LY)" : 1
```

### Ransomware distribution (Total: 16)

| Rank | Country | Incidents | Chart |
| :---: | :--- | :---: | :--- |
| **1** | 🇪🇬 Egypt | **7** | ███████ |
| **2** | 🇳🇬 Nigeria | **3** | ███ |
| **3** | 🇹🇳 Tunisia | **2** | ██ |
| **4** | 🇿🇦 South Africa | **1** | █ |
| **5** | 🇬🇭 Ghana | **1** | █ |
| **6** | 🇸🇳 Senegal | **1** | █ |
| **7** | 🇨🇮 Ivory Coast | **1** | █ |

### Data leaks / access sales distribution (Total: 38)

| Rank | Country | Incidents | Chart |
| :---: | :--- | :---: | :--- |
| **1** | 🇿🇦 South Africa | **13** | █████████████ |
| **2** | 🇪🇬 Egypt | **9** | █████████ |
| **3** | 🇲🇦 Morocco | **5** | █████ |
| **4** | 🇹🇳 Tunisia | **3** | ███ |
| **5** | 🇩🇿 Algeria | **2** | ██ |
| **6** | 🇹🇿 Tanzania | **2** | ██ |
| **7** | 🇰🇪 Kenya | **1** | █ |
| **–** | 🇰🇪🇪🇹🇳🇬🇿🇼 Resume docs | **1** | █ |
| **–** | 🇲🇿🇱🇷🇳🇬🇹🇬🇸🇱 DHIS2 | **1** | █ |
| **–** | 🇪🇬🇱🇾 Passport scans | **1** | █ |

### Ransomware vs. data leaks comparison by country

| Country | Ransomware | Data Leaks | Side-by-side distribution |
| :--- | :---: | :---: | :--- |
| 🇪🇬 Egypt | **7** | **9** | 🟧🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| 🇿🇦 South Africa | **1** | **13** | 🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| 🇲🇦 Morocco | **0** | **5** | 🟦🟦🟦🟦🟦 |
| 🇹🇳 Tunisia | **2** | **3** | 🟧🟧 🟦🟦🟦 |
| 🇳🇬 Nigeria | **3** | **0** | 🟧🟧🟧 |
| 🇩🇿 Algeria | **0** | **2** | 🟦🟦 |
| 🇹🇿 Tanzania | **0** | **2** | 🟦🟦 |
| 🇬🇭 Ghana | **1** | **0** | 🟧 |
| 🇨🇮 Ivory Coast | **1** | **0** | 🟧 |
| 🇰🇪 Kenya | **0** | **1** | 🟦 |
| 🇸🇳 Senegal | **1** | **0** | 🟧 |
| 🇰🇪🇪🇹🇳🇬🇿🇼 Resume docs | **0** | **1** | 🟦 |
| 🇲🇿🇱🇷🇳🇬🇹🇬🇸🇱 DHIS2 | **0** | **1** | 🟦 |
| 🇪🇬🇱🇾 Passport scans | **0** | **1** | 🟦 |
| **Total (54)** | **16** | **38** | *Legend: 🟧 Ransomware \| 🟦 Data Leaks* |

```mermaid
pie showData
    title Ransomware vs Data Leaks - May 2026
    "Data leaks and access sales" : 38
    "Ransomware" : 16
```

### Geographic breakdown by region

| Region | Total incidents | Ransomware | Leaks | Side-by-side |
| :--- | :---: | :---: | :---: | :--- |
| **North Africa** | **28** (51.9%) | 7 | 21 | 🟧🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| **Southern Africa** | **15** (27.8%) | 1 | 14 | 🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| **West Africa** | **5** (9.3%) | 4 | 1 | 🟧🟧🟧🟧 🟦 |
| **East Africa** | **3** (5.6%) | 0 | 3 | 🟦🟦🟦 |
| 🇰🇪🇪🇹🇳🇬🇿🇼🇲🇿🇱🇷🇹🇬🇸🇱🇱🇾 Multi-country (3 incidents) | **3** (5.6%) | 0 | 3 | 🟦🟦🟦 |

*Legend: 🟧 Ransomware | 🟦 Data Leaks*

### Sector distribution

| Activity sector | Incidents | Share (%) | Chart |
| :--- | :---: | :---: | :--- |
| **Government / Administration** | **14** | 25.9% | ██████████████ |
| **Recruitment / Personal Data** | **8** | 14.8% | ████████ |
| **Education / University** | **5** | 9.3% | █████ |
| **Finance / Banking** | **4** | 7.4% | ████ |
| **Food / Beverage / Hospitality** | **4** | 7.4% | ████ |
| **Logistics / Transport** | **3** | 5.6% | ███ |
| **Automotive** | **3** | 5.6% | ███ |
| **E-commerce / Digital** | **3** | 5.6% | ███ |
| **Telecom / ICT** | **3** | 5.6% | ███ |
| **NGO / Charity** | **2** | 3.7% | ██ |
| **Healthcare** | **2** | 3.7% | ██ |
| **Others** | **3** | 5.6% | ███ |
| **Total** | **54** | **100%** | |

```mermaid
pie showData
    title Sector distribution - May 2026
    "🏛️ Government / Administration" : 14
    "📋 Recruitment / Personal Data" : 8
    "🎓 Education / University" : 5
    "💰 Finance / Banking" : 4
    "🍔 Food / Beverage / Hospitality" : 4
    "🚛 Logistics / Transport" : 3
    "🚗 Automotive" : 3
    "🛒 E-commerce / Digital" : 3
    "📡 Telecom / ICT" : 3
    "❤️ NGO / Charity" : 2
    "🏥 Healthcare" : 2
    "🏭 Others" : 3
```

### Most prolific threat actors and groups

| Threat actor / Group | Incidents | Primary activity | Chart |
| :--- | :---: | :--- | :--- |
| **Databasehooligan** | **8** | Data leaks / sales | 🟦🟦🟦🟦🟦🟦🟦🟦 |
| **TheGentlemen** | **4** | Ransomware | 🟧🟧🟧🟧 |
| **404Crew Cyber Team** | **4** | Data leaks (coalitions) | 🟦🟦🟦🟦 |
| **NightSpire** | **3** | Ransomware | 🟧🟧🟧 |
| **INT3X** | **2** | Data leaks | 🟦🟦 |
| **Keymous** | **2** | Data leaks / access sales | 🟦🟦 |
| **cc5ab** | **2** | Data leaks | 🟦🟦 |
| **NullSec Nigeria** | **2** | Data leaks (coalitions) | 🟦🟦 |

*Legend: 🟧 Ransomware \| 🟦 Data Leaks*

```mermaid
pie showData
    title Most active threat actors - May 2026
    "Databasehooligan (8)" : 8
    "TheGentlemen (4)" : 4
    "404Crew Cyber Team (4)" : 4
    "NightSpire (3)" : 3
    "INT3X (2)" : 2
    "Keymous (2)" : 2
    "cc5ab (2)" : 2
    "NullSec Nigeria (2)" : 2
    "Others (27)" : 27
```

---

## 4. Country-by-country overview

> All entries cover publicly claimed incidents only. Claims remain unverified unless independently confirmed.

### 🇪🇬 Egypt (16 incidents: 7 ransomware, 9 data leaks)

- **Ransomware (7):** NightSpire claimed three targets (Papa John's, Rawaj Consumer Finance, B Investments); TheGentlemen, Qilin, LockBit 5.0, and Lamashtu (Luna Group) each claimed one additional Egyptian victim.
- **Education data leaks (4):** Ministry of Education (26.8M student records, Revesky), Professional Academy for Teachers (1.2M, INT3X), Mansoura University (989K), combined Educational & HR database (37 GB, INT3X). Total exposure exceeds 28M records.
- **Other data leaks (5):** Wuzzuf.net recruitment platform (672K records, Databasehooligan); additional claims by cc5ab, DR-X-LOL, CrowStealer, bigF, and Keymous.
- Also affected by multi-country incident: passport scans (raylie).

### 🇿🇦 South Africa (14 incidents: 1 ransomware, 13 data leaks)

- **OpSouthAfrica campaign:** The 404Crew Cyber Team coalition (NullSec Nigeria, NullSec Philippines, Infernalis) claimed 8 institutions: Ephraim Mogale Municipality, DCS, Bellavista School, SITA, SARS, mevent., CERVI, Sheriff Randburg West.
- **Data broker (3):** Databasehooligan sold Telkom SA (742K records), Wanderers Club (674K), and MIDAS SA databases.
- **Other data leaks (2):** cc5ab and Kazu each claimed one South African target.
- **Ransomware (1):** PrinzEugen claimed Standard Bank (unverified, no sample published).

### 🇲🇦 Morocco (5 data leaks)

- Five data leak claims: Sejjil, superstarkmc, JBT2026 (Watiqa.ma civil registry), fexus, DarkMafiaX.
- Largest exposure: approximately 827K credential lines from government platforms (Massar, Moutamadris, Waliye, Tax.gov.ma, TGR, and other administrative portals).

### 🇹🇳 Tunisia (5 incidents: 2 ransomware, 3 data leaks)

- **Ransomware (2):** TheGentlemen and Titan each claimed one Tunisian victim.
- **Data broker (3):** Databasehooligan sold three Tunisian job platform databases (MyTelnet, OptionCarriere.tn, Keejob).

### 🇳🇬 Nigeria (3 ransomware)

- Three distinct ransomware groups each claimed one Nigerian victim: MedusaLocker, KillSec, 0day Syndicate. No data leaks recorded for direct Nigerian targets.
- Also affected by two multi-country incidents: Resume docs (attackercompany, CV/resume database) and DHIS2 (Keymous). The DHIS2 incident is particularly significant: the published artifacts include URL/username/password pairs for health platform instances, indicating a credible compromise of administrative or operational accounts, not a simple data dump.

### 🇩🇿 Algeria (2 data leaks)

- Databasehooligan sold the OGEBC (Office de Gestion des Biens Culturels) database (425K records).
- kamalsheikhxx claimed one additional Algerian data leak.

### 🇹🇿 Tanzania (2 data leaks)

- Kampuchean offered Tanzania Police webmail access for sale: 10,000+ officer accounts with plaintext passwords, posing immediate law enforcement exposure.
- XOverStm claimed one additional Tanzanian database sale.

### 🇸🇳 Senegal (1 ransomware)

- AuditTeam hit the Trésor Public du Sénégal (national treasury). Confirmed double extortion: approximately 1.66M records exfiltrated across three Oracle databases (national taxpayer registry ~960K, payroll register ~40K, public payment orders ~659K including NINEA identifiers and beneficiary banking coordinates).

### 🇬🇭 Ghana (1 ransomware)

- TheGentlemen claimed one Ghanaian victim.

### 🇨🇮 Ivory Coast (1 ransomware)

- TheGentlemen claimed one victim in Ivory Coast.

### 🇰🇪 Kenya (1 data leak)

- cc5ab claimed one data leak from a Kenyan target. Also affected by the Resume docs multi-country incident (attackercompany).

### 🇲🇿 Mozambique / 🇱🇷 Liberia / 🇹🇬 Togo / 🇸🇱 Sierra Leone (exposure via DHIS2)

These four countries are affected exclusively through the DHIS2 / Ministries of health access sale (Keymous, May 13, 2026).

- The published artifacts include multiple URL / username / password combinations targeting DHIS2 instances operated by government health institutions in each of these countries.
- This suggests a credible compromise of administrative or operational accounts, not a conventional data dump. Unauthorized access, if active, would expose national health surveillance data, epidemiological records, and vaccination tracking systems.
- AFRINTEL did not perform any authentication attempts in order to avoid unauthorized interaction with the affected systems.

### Multi-country incidents (3 data leaks, 11 countries)

Three incidents each affected multiple African countries simultaneously. Each is counted once in the global total of 54.

| Incident | Actor | Evidence type | Countries affected |
|---|---|---|---|
| Resume docs data leak | attackercompany | Database published | 🇰🇪 Kenya, 🇪🇹 Ethiopia, 🇳🇬 Nigeria, 🇿🇼 Zimbabwe |
| DHIS2 / Ministries of health | Keymous | URL/credential pairs published (admin account access) | 🇲🇿 Mozambique, 🇱🇷 Liberia, 🇳🇬 Nigeria, 🇹🇬 Togo, 🇸🇱 Sierra Leone |
| Passport scans | raylie | Document images published | 🇪🇬 Egypt, 🇱🇾 Libya |

---

## 5. Detailed analysis by incident type

### 5.1 Ransomware (16 incidents)

| Rank | Country | Attacks | Main threat actors |
| :---: | :--- | :---: | :--- |
| **1** | 🇪🇬 Egypt | **7** | NightSpire (3), TheGentlemen, Qilin, LockBit 5.0, Lamashtu |
| **2** | 🇳🇬 Nigeria | **3** | MedusaLocker, KillSec, 0day Syndicate |
| **3** | 🇹🇳 Tunisia | **2** | TheGentlemen, Titan |
| **4** | 🇿🇦 South Africa | **1** | PrinzEugen |
| **5** | 🇬🇭 Ghana | **1** | TheGentlemen |
| **6** | 🇸🇳 Senegal | **1** | AuditTeam |
| **7** | 🇨🇮 Ivory Coast | **1** | TheGentlemen |

**Observations:** **NightSpire** claimed three Egyptian targets in the same month (Papa John's, Rawaj Consumer Finance, B Investments), establishing itself as the leading ransomware group on the continent for May. **TheGentlemen** demonstrated notable geographic reach, hitting four countries in a single month. The attack on the **Trésor Public du Sénégal** represents the highest-impact government ransomware incident of the month. Technical analysis confirms double-extortion: data was exfiltrated from two internal servers (Oracle DB + SICA payroll system) approximately 9 days before the ransomware was deployed, yielding approximately 1,659,735 records including a national taxpayer registry (~960K), a payroll register (~40K), and a full public payment order database (~659K) containing NINEA identifiers and beneficiary banking coordinates.

### 5.2 Data leaks & access sales (38 incidents)

| Rank | Country | Incidents | Main actors |
| :---: | :--- | :---: | :--- |
| **1** | 🇿🇦 South Africa | **13** | Databasehooligan, 404Crew CT, NullSec Nigeria, Kazu, cc5ab |
| **2** | 🇪🇬 Egypt | **9** | INT3X, Revesky, cc5ab, DR-X-LOL, CrowStealer, bigF, Keymous, Databasehooligan |
| **3** | 🇲🇦 Morocco | **5** | Sejjil, superstarkmc, JBT2026, fexus, DarkMafiaX |
| **4** | 🇹🇳 Tunisia | **3** | Databasehooligan (3) |
| **5** | 🇩🇿 Algeria | **2** | kamalsheikhxx, Databasehooligan |
| **6** | 🇹🇿 Tanzania | **2** | XOverStm, Kampuchean |
| **–** | 🇰🇪🇪🇹🇳🇬🇿🇼 Resume docs | **1** | attackercompany |
| **–** | 🇲🇿🇱🇷🇳🇬🇹🇬🇸🇱 DHIS2 | **1** | Keymous |
| **–** | 🇪🇬🇱🇾 Passport scans | **1** | raylie |

**Key observations:**
- **Databasehooligan** targeted CRM-structured databases across four countries, selling between $900 and $1,400 per dataset, with victims including Telkom SA (742K records), Wanderers Club SA (674K), Wuzzuf.net Egypt (672K), MyTelnet Tunisia, OptionCarriere.tn, Keejob, MIDAS SA, and OGEBC Algeria.
- The **404Crew Cyber Team** coalition (with NullSec Nigeria, NullSec Philippines, and Infernalis) ran a sustained campaign against South African institutions under the "OpSouthAfrica" banner, targeting Ephraim Mogale Municipality, DCS, Bellavista School, SITA, SARS, mevent., CERVI, and Sheriff Randburg West.
- Egypt's **education sector** faced a systemic breach wave: the Ministry of Education (26.8M student records), Professional Academy for Teachers (1.2M teacher records), Mansoura University (989K students), and a combined Educational & HR database (37 GB).
- **Tanzania Police** webmail was put up for sale with 10,000+ officer accounts and plaintext passwords, posing critical law enforcement exposure.

---

## 6. Sectoral impact

| Activity sector | Incidents | Share (%) | Visual impact |
| :--- | :---: | :---: | :--- |
| **Government / Administration** | **14** | 25.9% | ██████████████ |
| **Recruitment / Personal Data** | **8** | 14.8% | ████████ |
| **Education / University** | **5** | 9.3% | █████ |
| **Finance / Banking** | **4** | 7.4% | ████ |
| **Food / Beverage / Hospitality** | **4** | 7.4% | ████ |
| **Logistics / Transport** | **3** | 5.6% | ███ |
| **Automotive** | **3** | 5.6% | ███ |
| **E-commerce / Digital** | **3** | 5.6% | ███ |
| **Telecom / ICT** | **3** | 5.6% | ███ |
| **NGO / Charity** | **2** | 3.7% | ██ |
| **Healthcare** | **2** | 3.7% | ██ |
| **Others** | **3** | 5.6% | ███ |

**Key observations:**
- **Government dominance:** The public sector (Government + Education) accounts for 35.2% of all May incidents, confirming the persistent targeting of African state infrastructure.
- **Education under systemic assault:** Egypt's education sector alone contributed 4 of the 5 education incidents, with total exposure exceeding 28 million student and teacher records.
- **Recruitment / Personal Data surge:** Databasehooligan's focus on CRM-structured recruitment and consumer platforms (Keejob, MyTelnet, OptionCarriere.tn, Wuzzuf.net, MIDAS, Telkom, Wanderers Club) drove the second-largest sector.
- **Critical infrastructure targeted:** The Trésor Public du Sénégal confirms double-extortion with ~1.66M records exfiltrated (national taxpayer registry, payroll, payment orders with NINEA and banking data). The Tanzania Police webmail sale represents a parallel threat to law enforcement operational security.

---

## 7. Threat actor profile

| Threat actor | Type | Incidents | Primary targets |
| :--- | :--- | :---: | :--- |
| **Databasehooligan** | Data broker | **8** | CRM/recruitment databases (multi-country) |
| **TheGentlemen** | Ransomware | **4** | Industry, automotive, food (4 countries) |
| **404Crew Cyber Team** | Data leak (coalitions) | **4+** | South African public institutions |
| **NightSpire** | Ransomware | **3** | Egyptian finance and food services |
| **INT3X** | Data leak | **2** | Egyptian education institutions |
| **Keymous** | Access sale / data leak | **2** | Health systems, telecom (multi-country) |
| **cc5ab** | Data leak | **2** | Egyptian and Kenyan government |
| **NullSec Nigeria** | Data leak (coalitions) | **2+** | South African government agencies |

**Emerging actors:**
- **PrinzEugen** (Standard Bank claim)
- **Lamashtu** (Luna Group Egypt)
- **Kampuchean** (Tanzania Police webmail)
- **JBT2026** (Watiqa.ma Morocco civil registry)

### 7.1 Risk assessment

| Country | Risk level |
|---|---|
| Egypt | 🔴 Critical |
| South Africa | 🔴 Critical |
| Morocco | 🟠 High |
| Tunisia | 🟠 High |
| Nigeria | 🟠 Medium-High |
| Algeria | 🟡 Medium |
| Tanzania | 🟠 Medium-High |
| Others | 🟡 Low-Medium |

---

## 8. Key trends

- **Education sector as strategic target:** The simultaneous breach of four Egyptian education entities exposing tens of millions of student and teacher records suggests either a coordinated campaign or opportunistic exploitation of shared infrastructure vulnerabilities.
- **"OpSouthAfrica" coalition campaign:** The 404Crew Cyber Team, NullSec Nigeria, and Infernalis targeted at least eight South African institutions in May, combining data leak publication with political messaging around xenophobia grievances.
- **Databasehooligan CRM sweep:** The same data broker sold structured CRM / consumer databases from eight organizations across Tunisia, South Africa, Egypt, and Algeria, suggesting systematic exploitation of a shared vulnerability or common platform.
- **NightSpire concentration on Egypt:** Three Egyptian targets in one month by a single ransomware group suggests a focused campaign against Egyptian business infrastructure, particularly in finance and consumer services.
- **Government email accounts as access vectors:** Moroccan government credential exposure (827K lines), Tanzanian police webmail sale, and multi-country EDR-fraud account offers signal a growing market for law enforcement impersonation.
- **Multi-country health system compromise:** The DHIS2 access sale affecting seven countries (Mozambique, Liberia, Nigeria, Bhutan, Honduras, Togo, Sierra Leone) represents a critical threat to public health data sovereignty.

---

## 9. MITRE ATT&CK mapping (contextual)

| Phase | Technique ID | Technique name | Context |
| :--- | :---: | :--- | :--- |
| **Initial Access** | **T1190** | Exploit Public-Facing Application | FutureShop API, Mansoura University, LSB Kenya |
| **Initial Access** | **T1078** | Valid Accounts | Moroccan gov credentials, Tanzania Police, DHIS2 health platform credentials (URL/password pairs published) |
| **Collection** | **T1005** | Data from Local System | PAT Egypt, SDTM Morocco, SITA SA |
| **Collection** | **T1114.002** | Remote Email Collection | Tanzania Police webmail |
| **Exfiltration** | **T1041** | Exfiltration Over C2 Channel | Wuzzuf.net, Telkom, CGCSA |
| **Impact** | **T1486** | Data Encrypted for Impact | All ransomware incidents |
| **Privilege Escalation** | **T1078.003** | Local Accounts | DHIS2 admin credentials |

> Common cross-campaign techniques:
> - **T1190** – Exploit Public-Facing Application (primary entry vector for data leaks)
> - **T1078** – Valid Accounts (credential theft, IAB listings, infostealer logs)
> - **T1486** – Data Encrypted for Impact (ransomware deployment)
> - **T1041** – Exfiltration Over C2 Channel (bulk database extraction)

---

## 10. Recommendations

- **Governments:** Enforce MFA on all administrative and educational portals; audit credential exposure on underground forums; treat the Moroccan gov credential leak as a systemic identity risk requiring immediate password resets across all affected platforms.
- **Educational institutions:** Isolate student and staff databases from public-facing web infrastructure; encrypt sensitive data at rest; implement audit logging on administrative platforms.
- **Financial sector:** Monitor ransomware DLS for pre-publication indicators; maintain offline backups; review third-party data flows for CRM and e-payment platforms.
- **Law enforcement:** Treat the Tanzania Police webmail compromise as an active operational security risk; rotate all affected credentials; implement DMARC/DKIM on government email domains.
- **Healthcare:** Audit DHIS2 administrative accounts immediately; rotate credentials; restrict admin panel access to internal networks only.

---

## 11. SOC tactical recommendations

- **[T1078] Credential monitoring:** Correlate dark web leak data against internal user directories; flag accounts exposed in Moroccan gov, Tanzania Police, and Stats SA claims.
- **[T1190] API exposure:** Implement authenticated access controls on all public-facing APIs; scan for unauthenticated S3 buckets and exposed admin panels.
- **[T1486] Ransomware detection:** Monitor for unusual volume encryption activity, shadow copy deletion (vssadmin), and lateral movement via SMB/RDP from new admin accounts.
- **[Data broker activity]:** Establish a threat intelligence feed tracking Databasehooligan, 404Crew, and NightSpire for early warning of new African targets.

---

## 12. Conclusion

May 2026 confirmed the continued maturation of threat actor activity targeting Africa, with both volume (54 incidents) and severity (millions of records, critical infrastructure ransomware) remaining high. Egypt and South Africa jointly absorbed 56% of recorded incidents. The systematic exposure of education records in Egypt and the sustained OpSouthAfrica coalition campaign represent the defining threat patterns of the month. The rise of Databasehooligan as a dominant data broker and NightSpire as an emerging ransomware group signals the ongoing evolution of the criminal ecosystem.

**AFRINTEL** – African Cyber Threat Intelligence
🔗 [GitHub AFRINTEL Repository](https://github.com/Hatchepsoute/AFRINTEL)
