[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-RQL%20export-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel%20Type-CTI-purple)

# List of African cyberattack victims - March 2026 (36 victims)
👉🏾 [**French version available here**](./victims_FR.md)

## Scope and methodology
This list records ransomware and data breach incidents targeting African entities during March 2026. Data is extracted and normalized from monitoring exports of leak sites (DLS) and complementary OSINT sources.

**Quality controls applied:**
- **Integrity:** Each line of the source dataset is kept as a distinct incident.
- **Normalization:** Visual harmonization of group names (e.g., LockBit 5.0, Qilin, APT73/Bashe).
- **Verification:** Validation of institutional URLs and enrichment of technical descriptions.

## Quick overview
- **Victims recorded:** 36
- **Countries affected:** 11
- **Actors observed:** 23
- **Most affected countries:** South Africa (11), Morocco (8), Egypt (8)

### Incident typology
- **Ransomware (encryption + ransom):** 19 incidents (53%)
- **Data breaches / system intrusions:** 17 incidents (47%)

### Breakdown by country
- 🇿🇦 South Africa: **11** victims
- 🇲🇦 Morocco: **8** victims
- 🇪🇬 Egypt: **8** victims
- 🇳🇬 Nigeria: **2** victims
- 🇸🇳 Senegal: **1** victim
- 🇿🇲 Zambia: **1** victim
- 🇲🇬 Madagascar: **1** victim
- 🇹🇳 Tunisia: **1** victim
- 🇳🇦 Namibia: **1** victim
- 🇹🇿 Tanzania: **1** victim
- 🇨🇩 DRC: **1** victim

### Breakdown by actor
- **CrowStealer**: 5 victims
- **APT73/BASHE**: 4 victims
- **XP95**: 3 victims
- **Qilin**: 2 victims
- **The Gentlemen**: 2 victims
- **INC Ransom**: 2 victims
- **xNov**: 2 victims
- **LockBit 5.0**: 1 victim
- **Crypto24**: 1 victim
- **PEAR**: 1 victim
- **Lynx**: 1 victim
- **Payload**: 1 victim
- **DragonForce**: 1 victim
- **NightSpire**: 1 victim
- **Morpheus**: 1 victim
- **Coinbase Cartel**: 1 victim
- **Spirigatito**: 1 victim
- **TelephoneHooliganism**: 1 victim
- **anisanas2**: 1 victim
- **AshleyWood2022**: 1 victim
- **Bytetobreach**: 1 victim
- **privillege**: 1 victim
- **Coordinated network (UBA Senegal)**: 1 victim

### Ransomware vs Data Breaches by country
| Country               | Ransomware | Data Breach |
|-----------------------|------------|-------------|
| 🇿🇦 South Africa       | 7          | 4           |
| 🇲🇦 Morocco            | 5          | 3           |
| 🇪🇬 Egypt              | 3          | 5           |
| 🇳🇬 Nigeria            | 0          | 2           |
| 🇸🇳 Senegal            | 0          | 1           |
| 🇿🇲 Zambia             | 0          | 1           |
| 🇲🇬 Madagascar         | 1          | 0           |
| 🇹🇳 Tunisia            | 1          | 0           |
| 🇳🇦 Namibia            | 1          | 0           |
| 🇹🇿 Tanzania           | 1          | 0           |
| 🇨🇩 DRC                | 0          | 1           |

## March 2026

### 01 March 2026
#### 🇿🇦 South Africa - Diesel-Electric Group
- **Ransomware group:** LockBit 5.0
- **Sector:** Automotive (Distribution & Services)
- **Website:** [diesel-electric.co.za](https://diesel-electric.co.za)
- **Status:** Claim
- **Victim description:** Major automotive component distributor in Southern Africa, including Bosch Service franchises and e-CAR centers.

#### 🇪🇬 Egypt - Canadian International College (CIC)
- **Actor / Group:** CrowStealer
- **Sector:** Education / Higher education
- **Website:** [cic-cairo.edu.eg](https://www.cic-cairo.edu.eg/)
- **Status:** Database leak
- **Victim description:** First Canadian education provider in Egypt, affiliated with Cape Breton University (CBU). The leak (studentsdata.csv) contains 2,925 records: names, majors, levels, GPAs, years.

#### 🇿🇲 Zambia - Ministry of Community Development and Social Services
- **Actor / Group:** Spirigatito
- **Sector:** Government / Social services
- **Website:** [mcdss.gov.zm](https://www.mcdss.gov.zm)
- **Status:** Massive database leak
- **Victim description:** Institution responsible for social protection and empowerment. Leak of the "Social Cash Transfer" (SCT) system: full identities (names, NRC numbers, dates of birth), contact details, benefit amounts.

### 02 March 2026
#### 🇪🇬 Egypt - Waste Management Regulatory Authority (WMRA)
- **Actor / Group:** CrowStealer
- **Sector:** Government / Environment
- **Website:** [garb.gov.eg](https://garb.gov.eg)
- **Status:** Database leak
- **Victim description:** Agency under the Ministry of Environment responsible for waste management regulation. Database containing administrative data, internal records, information on partners and staff.

#### 🇪🇬 Egypt - Orascom Construction
- **Actor / Group:** CrowStealer
- **Sector:** Engineering & Construction
- **Website:** [orascom.com](https://orascom.com/)
- **Status:** Database leak
- **Victim description:** Leading engineering and construction company operating in the Middle East, North Africa, and the United States. Compromised data: staff_id, full names, professional emails, departments, positions.

#### 🇪🇬 Egypt - Ministry of Health and Population (E-Portal)
- **Actor / Group:** CrowStealer
- **Sector:** Government / Health
- **Website:** [mohp.gov.eg](https://www.mohp.gov.eg)
- **Status:** Massive leak (sold for $2,500)
- **Victim description:** Database of 3.8 million records (2019-2026) including full names, National ID, phone numbers, addresses, precise medical diagnoses, types of surgeries, treatment facilities.

### 03 March 2026
#### 🇿🇦 South Africa - Walter Sisulu University (WSU)
- **Actor / Group:** TelephoneHooliganism
- **Sector:** Education / University
- **Website:** [wsu.ac.za](https://www.wsu.ac.za)
- **Status:** Database leak (sold for $1,150)
- **Victim description:** Public university in the Eastern Cape. Data structured in three sections (Contacts, Enrollments, Tickets): dates of birth, emails, addresses, GPAs, scholarships, support history.

#### 🇪🇬 Egypt - Ministry of Education and Technical Education
- **Actor / Group:** CrowStealer
- **Sector:** Government / Education
- **Website:** [moe.gov.eg](https://moe.gov.eg)
- **Status:** Database leak
- **Victim description:** Data on students and staff: national IDs, full names, addresses, academic records.

#### 🇲🇦 Morocco - National Office of University, Social and Cultural Works (ONOUSC)
- **Actor / Group:** xNov
- **Sector:** Education / Government
- **Website:** [amo.onousc.ma](https://amo.onousc.ma)
- **Status:** Data leak
- **Victim description:** Body responsible for student social services in Morocco (scholarships, university housing, health coverage). Exposure of 3,631 student records related to Mandatory Health Insurance (AMO): names, CINE numbers, university registration numbers, CNE, dates of birth, enrollment statuses (approved/rejected with reasons).

### 04 March 2026
#### 🇲🇦 Morocco - Outsourcia
- **Ransomware group:** Qilin
- **Sector:** Business Process Outsourcing (BPO)
- **Website:** [outsourcia.com](https://www.outsourcia.com)
- **Status:** Claim
- **Victim description:** Major customer relationship operator based in Casablanca, managing business processes for international accounts.

### 05 March 2026
#### 🇪🇬 Egypt - Rowad Modern Engineering
- **Ransomware group:** Crypto24
- **Sector:** Engineering & Construction
- **Website:** [rowad-rme.com](http://www.rowad-rme.com)
- **Status:** Claim
- **Victim description:** Egyptian construction company specializing in infrastructure projects and commercial buildings.

### 06 March 2026
#### 🇪🇬 Egypt - INTERACT TECHNOLOGY SOLUTIONS
- **Ransomware group:** PEAR
- **Sector:** IT Consulting
- **Website:** [interactts.com](http://interactts.com)
- **Status:** Claim
- **Victim description:** Company providing critical technology and infrastructure solutions in Egypt.

#### 🇲🇬 Madagascar - Orange Madagascar
- **Ransomware group:** Qilin
- **Sector:** Telecommunications
- **Website:** [orange.mg](https://www.orange.mg/)
- **Status:** Claim
- **Victim description:** Telecommunications leader in Madagascar, operating internet, mobile, and mobile banking services.

### 09 March 2026
#### 🇹🇳 Tunisia - K.PROPHA (Karray Produits Pharmaceutiques)
- **Ransomware group:** The Gentlemen
- **Sector:** Health / Pharmaceutical
- **Website:** [kpropha.com](http://kpropha.com)
- **Status:** Claim
- **Victim description:** Tunisian company specializing in the distribution of pharmaceutical and para-pharmaceutical products.

### 12 March 2026
#### 🇲🇦 Morocco - HACA (High Authority for Audiovisual Communication)
- **Ransomware group:** APT73 / Bashe
- **Sector:** Government / Media
- **Website:** [haca.ma](http://haca.ma)
- **Status:** Claim
- **Victim description:** Constitutional body responsible for regulating audiovisual communication in Morocco.

### 13 March 2026
#### 🇿🇦 South Africa - Lion of Africa Insurance
- **Ransomware group:** Lynx
- **Sector:** Insurance services
- **Website:** [lionsureins.com](http://lionsureins.com/)
- **Status:** Claim
- **Victim description:** South African insurance company handling large volumes of personal and financial data.

#### 🇿🇦 South Africa - Gauteng Provincial Government
- **Actor / Group:** XP95
- **Sector:** Government / Public administration
- **Website:** [gauteng.gov.za](https://www.gauteng.gov.za)
- **Status:** Massive leak (sold for $25,000)
- **Victim description:** Manages the most populous province in South Africa (Johannesburg, Pretoria). 3.8 TB of data (3.6 million files) exfiltrated: health, education, housing, economic development.

### 14 March 2026
#### 🇪🇬 Egypt - Grid Fine Finishes
- **Ransomware group:** Payload
- **Sector:** Fit-out / Construction
- **Website:** [gridff.com](http://gridff.com)
- **Status:** Claim
- **Victim description:** Egyptian company specializing in high-end interior fit-out for commercial and residential sectors.

### 19 March 2026
#### 🇳🇦 Namibia - Namibia Airports Company
- **Ransomware group:** INC Ransom
- **Sector:** Air transport
- **Website:** [airports.com.na](http://airports.com.na)
- **Status:** Claim
- **Victim description:** Official manager of national airports in Namibia.

### 20 March 2026
#### 🇿🇦 South Africa - The Unlimited
- **Ransomware group:** DragonForce
- **Sector:** Insurance services
- **Website:** [theunlimited.co.za](http://theunlimited.co.za)
- **Status:** Claim (137 GB exfiltrated)
- **Victim description:** Provider of insurance products including health, auto, legal, and life.

#### 🇲🇦 Morocco - Ministry of Justice
- **Actor / Group:** anisanas2
- **Sector:** Government / Justice
- **Website:** [justice.gov.ma](https://www.justice.gov.ma)
- **Status:** Massive leak (300 GB)
- **Victim description:** Exfiltration of 300 GB including more than 150,000 court case files (2019-2026). Disputes between major Moroccan companies and individuals (12 billion MAD). Documents: IDs, bank statements, court records, invoices.

### 21 March 2026
#### 🇿🇦 South Africa - Elundini Local Municipality
- **Ransomware group:** The Gentlemen
- **Sector:** Local government
- **Website:** [elundini.gov.za](http://elundini.gov.za)
- **Status:** Claim
- **Victim description:** Municipal administration dedicated to sustainable development in the Eastern Cape province.

### 22 March 2026
#### 🇿🇦 South Africa - Semenya Furumele Consulting Engineers
- **Ransomware group:** NightSpire
- **Sector:** Engineering consulting
- **Website:** [sfce.co.za](http://www.sfce.co.za)
- **Status:** Claim
- **Victim description:** Engineering consulting firm based in South Africa.

### 24 March 2026
#### 🇸🇳 Senegal - United Bank for Africa (UBA Senegal)
- **Actor / Group:** Coordinated network (suspected internal complicity)
- **Sector:** Finance / Banking
- **Website:** [ubasenegal.com](https://www.ubasenegal.com)
- **Date of attack:** 30-31 January 2026 (disclosed on 24 March 2026)
- **Status:** System intrusion & massive fraud (1.143 billion FCFA ~ $1.9 million USD)
- **Victim description:** UBA Senegal suffered an exceptional cyberattack. Over a few hours, more than 3,400 fraudulent withdrawals were executed across ATMs in multiple cities (Dakar, Thiès, Kaolack). Attackers compromised the internal information system, manipulated databases (creating/modifying accounts, increasing withdrawal limits, transferring funds from legitimate clients), then coordinated simultaneous withdrawals to empty ATMs before detection. Potential exploited vulnerabilities: lack of real-time SOC monitoring, insufficient anti‑fraud procedures on mass withdrawals, possible internal complicity, and weak security configurations. This incident is a major wake‑up call for West African financial institutions.

### 26 March 2026
#### 🇿🇦 South Africa - ETFSA
- **Ransomware group:** INC Ransom
- **Sector:** Wealth Management
- **Website:** [etfsa.co.za](http://ETFSA.co.za)
- **Status:** Claim (client data exfiltrated)
- **Victim description:** South African financial services platform specializing in exchange-traded funds (ETFs).

#### 🇲🇦 Morocco - Maroc Telecom
- **Ransomware group:** APT73 / Bashe
- **Sector:** Telecommunications
- **Website:** [iam.ma](http://iam.ma)
- **Status:** Claim
- **Victim description:** Historic telecommunications operator in Morocco, providing mobile, internet, and fixed-line services.

#### 🇲🇦 Morocco - 2M TV
- **Ransomware group:** APT73 / Bashe
- **Sector:** Media & Audiovisual
- **Website:** [2m.ma](http://2m.ma)
- **Status:** Claim
- **Victim description:** Moroccan national television channel.

#### 🇲🇦 Morocco - Royal Institute for Strategic Studies (IRES)
- **Ransomware group:** APT73 / Bashe
- **Sector:** Research / Think tank
- **Website:** [ires.ma](http://ires.ma)
- **Status:** Claim
- **Victim description:** Strategic analysis center attached to the Moroccan Royal Cabinet.

### 29 March 2026
#### 🇿🇦 South Africa - Statistics South Africa (Stats SA)
- **Ransomware group:** XP95
- **Sector:** Government / National Statistics
- **Website:** [statssa.gov.za](https://www.statssa.gov.za)
- **Status:** Ransomware / Database for Sale ($100,000)
- **Victim description:** Stats SA is the national statistical agency of South Africa. Threat actor XP95 exfiltrated 154 GB of data (453,362 files). The breach potentially compromises sensitive socio-economic data, census records, employment information, inflation data, and national administrative records. A $100,000 ransom has been demanded, with a public sale deadline set for April 20, 2026.

#### 🇿🇦 South Africa - Gauteng City Region Academy (GCRA)
- **Ransomware group:** XP95
- **Sector:** Education / Training (Provincial Government)
- **Website:** [gcra.gauteng.gov.za](https://gcra.gauteng.gov.za)
- **Status:** Ransomware / Database for Sale
- **Victim description:** The GCRA is the agency responsible for skills development in the Gauteng province. The exfiltration of 147 GB of data potentially compromises student records (bursaries, registrations, PII), training program data, and the academy's administrative documents. Threat actor XP95 has set a ransom deadline before the public sale of the files.

### 30 March 2026
#### 🇹🇿 Tanzania - SBC Tanzania Limited
- **Ransomware group:** Morpheus
- **Sector:** Food & Beverage
- **Website:** [sbctanzania.co.tz](http://sbctanzania.co.tz)
- **Status:** Claim
- **Victim description:** Beverage manufacturer and distributor, official bottler of PepsiCo in Tanzania.

#### 🇿🇦 South Africa - Nashua
- **Ransomware group:** Coinbase Cartel
- **Sector:** IT & Managed Services
- **Website:** [nashua.co.za](http://nashua.co.za)
- **Status:** Claim
- **Victim description:** Major provider of integrated technology solutions and managed services for businesses.

#### 🇳🇬 Nigeria - Ahmadu Bello University (ABU Zaria)
- **Actor / Group:** AshleyWood2022
- **Sector:** Education / Higher education
- **Website:** [abu.edu.ng](https://www.abu.edu.ng)
- **Status:** Database leak
- **Victim description:** One of the largest research universities in Nigeria. Database (`tbl_flattened.csv` & `abu.sql`) with over 11,000 records: academic and non-academic staff (names, departments, ranks, qualifications, gender, date of birth, districts of origin).

### 31 March 2026
#### 🇳🇬 Nigeria - Remita (SystemSpecs)
- **Actor / Group:** Bytetobreach
- **Sector:** Fintech / Payment services
- **Website:** [remita.net](https://www.remita.net)
- **Status:** Massive leak (3 TB)
- **Victim description:** Major payment platform in Nigeria used by individuals, businesses, and government. 3 TB breach: 800 GB of KYC documents (IDs, passports, bank statements, invoices), MySQL/Postgres databases, source code, Docker registries, government HSM keys, over 35,000 password hashes.

#### 🇲🇦 Morocco - Smarteez (L'Oréal Morocco Supply Chain Provider)
- **Actor / Group:** xNov
- **Sector:** Digital Marketing / Cosmetics (L'Oréal Supply Chain)
- **Website:** [smarteez.eu](https://smarteez.eu)
- **Status:** Supply chain compromise / Database leak
- **Victim description:** Smarteez is a Moroccan digital provider used by L'Oréal Morocco for field operations management. Exposure of critical data: information on 296 pharmacies (GPS, segmentation), 361,000 sales/KPI records, 22 plaintext OAuth2 application secrets, complete administrative logs. A production APK was also disclosed.

#### 🇨🇩 DRC - Public Administration Reform Fund (FRAP)
- **Actor / Group:** privillege
- **Sector:** Government / Administration
- **Website:** [frap.cd](https://frap.cd/)
- **Date of breach:** September 2025 (identified in March 2026)
- **Status:** Database leak (historical archive)
- **Victim description:** Body responsible for modernizing public administration in the DRC. Data exfiltrated in September 2025: administrative records and information on state employees.