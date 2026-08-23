[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%7C%20Data%20Leak%20%7C%20Defacement-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Cyber Attacks in Africa: December 2024: List of 14 Victims

👉🏾 [**Version française disponible ici**](./victims_FR.md)

## December 2024

## Monthly snapshot

The corrected December 2024 corpus contains **14 documented incident records**: **11 Ransomware**, **2 Data Leak**, **1 Defacement**, **0 Access Sale**, **0 DDoS** and **0 Operational Fraud**, across **12 African countries**.

The two retrospective additions are **MSEA (Kenya)**, recorded as a high-confidence corroborated Data Leak without direct victim confirmation in the reviewed source set, and **NBS (Nigeria)**, recorded as a victim-confirmed Defacement with documented service disruption and no confirmed backend data theft.

### December 3, 2024

#### 🇸🇩 Sudan - DAL Group
- **Ransomware Group:** ransomhub
- **Sector:** Agriculture / Agribusiness
- **Website:** [dalgroup.com](https://www.dalgroup.com)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Incident type:** Data Leak
- **Analysis:** AFRINTEL reviewed 12 screenshots from the RansomHub evidence set. The material includes financial covenants, bank-account and transaction material, passport-related documents, customer-account records and internal DAL Group documents. The visible evidence suggests exposure across financial operations, identity documentation and business administration rather than a single isolated file. Potential impacts include financial fraud, identity theft, targeted phishing, supplier or customer impersonation, and commercial espionage against a large Sudanese conglomerate. The screenshots do not independently confirm the initial access vector, the completeness of the dataset, the exact number of affected individuals or operational disruption. AFRINTEL does not reproduce personal records, passport details, account numbers or download links.
- **Victim Description:** DAL Group is Sudan's largest private conglomerate, operating across agribusiness, industry, agriculture, distribution, and beverages sectors.

----------------------------

### December 2024 - exact incident date not publicly established

#### 🇰🇪 Kenya - Micro and Small Enterprises Authority (MSEA)
- **Incident date:** December 2024 - exact date not publicly established
- **Initial publication date:** 3 December 2024
- **AFRINTEL correction date:** 23 August 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [msea.go.ke](https://msea.go.ke/)
- **Status:** Corroborated - No Direct Victim Confirmation Located
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** MSEA is a Kenyan public authority responsible for supporting and regulating the micro and small enterprise sector.
- **Analysis:** Public reporting in early December 2024 stated that MSEA had been hacked and that government and organisational information was offered for sale on underground forums. Reported exposed material included employee records, government correspondence, financial statements and business-registration information. The incident was later referenced by INTERPOL's Africa Cyberthreat Assessment and by ENACT, which materially strengthens the assessment that a breach occurred. However, no direct MSEA victim notification was located in the source set used for the retrospective audit. AFRINTEL therefore records the case as a `Data Leak` with `High` confidence and a corroborated status, not as `Victim Confirmed`. The claimed USD 100,000 sale price and technical root-cause statements remain secondary reporting and are not treated as established facts.
- **Evidence qualification:** The breach is strongly corroborated, but direct victim confirmation was not located in the reviewed source set. Reported data categories are retained as reported exposure, not as independently validated file-by-file findings.
- **Public sources:** Techpoint Africa; INTERPOL Africa Cyberthreat Assessment; ENACT references documented in the retrospective correction dataset.

----------------------------

### December 9, 2024

#### 🇲🇷 Mauritania - Bankily
- **Ransomware Group:** apt73/bashe
- **Sector:** Finance / Banking
- **Website:** [bankily.mr](https://www.bankily.mr)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Bankily is a Mauritanian mobile banking platform operated by Banque Populaire de Mauritanie (BPM), providing digital financial services and mobile payment solutions.

----------------------------

### December 10, 2024

#### 🇳🇦 Namibia - Telecom Namibia
- **Ransomware Group:** hunters
- **Sector:** Telecommunications
- **Website:** [telecom.na](https://www.telecom.na)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Telecom Namibia is the national incumbent telecommunications operator providing voice, broadband, data connectivity, and infrastructure services in Namibia.

----------------------------

### December 13, 2024

#### 🇪🇬 Egypt - Kazyon
- **Ransomware Group:** moneymessage
- **Sector:** Retail / E-commerce
- **Website:** [kazyon.com](https://www.kazyon.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Kazyon is a major Egyptian hard-discount supermarket chain offering food, household, and consumer products through a wide store network.

----------------------------

### December 15, 2024

#### 🇿🇲 Zambia - Tumeny Payments Limited
- **Ransomware Group:** killsec
- **Sector:** Finance / Banking
- **Website:** [tumenypay.com](https://www.tumenypay.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Tumeny Payments Limited is a Zambian fintech company providing digital payment services, money transfer, and payment infrastructure solutions.

----------------------------

### December 16, 2024

#### 🇳🇬 Nigeria - Ekiti State Government
- **Ransomware Group:** funksec
- **Sector:** Government / Administration
- **Website:** [ekitistate.gov.ng](https://ekitistate.gov.ng)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** The Ekiti State Government is the executive administration of Ekiti State, in southwestern Nigeria. Its official portal hosts ministries, agencies and public-service information, including recruitment-related content, for state residents and civil servants.
- **Analysis:** AFRINTEL reviewed a local archive consistent with the claim made by the threat actor funksec, comprising a leak notice referencing ekitistate.gov.ng and describing a database exceeding 300MB, alongside a website document library of more than 17,000 individual image files (roughly 530MB) collected from the portal's file repository. The reviewed sample includes personal identification documents (passport-style scans), curriculum vitae bearing personal data fields such as date of birth, address, phone number, email and religion, and a Police Service Commission candidate-screening table listing shortlisted applicants by name, local government area, village and gender for a 2019 recruitment exercise. The volume and structure of the reviewed material, file-naming patterns consistently tied to named individuals, and the presence of an official state-government document template support a very high confidence assessment of a genuine data exposure rather than a superficial claim. Given Ekiti State's role as a subnational public administration and the presence of citizen and civil-servant identity documents, this incident presents a significant risk of identity theft, targeted phishing and impersonation. AFRINTEL does not reproduce any name, passport number, contact detail or other personal identifier from the reviewed material.

----------------------------

- **Evidence qualification:** The reviewed archive strongly supports genuine data exposure associated with the Ekiti State Government. It does not independently establish ransomware encryption, the initial-access vector or operational disruption.
### December 18, 2024

#### 🇳🇬 Nigeria - National Bureau of Statistics (NBS)
- **Incident date:** 18 December 2024
- **Initial publication date:** 18 December 2024
- **AFRINTEL correction date:** 23 August 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [nigerianstat.gov.ng](https://www.nigerianstat.gov.ng/)
- **Status:** Victim Confirmed
- **Incident type:** Defacement
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** Nigeria's National Bureau of Statistics is the national statistical authority and operates a major public repository for economic, demographic and social statistics.
- **Analysis:** On 18 December 2024 NBS confirmed through its official social-media account that its website had been hacked and advised the public to disregard information posted there until recovery. Independent reporting documented a `Page hacked` message. The website remained unavailable for several weeks before restoration in January 2025, materially disrupting public access to national statistical information. No public evidence in the reviewed sources establishes theft of backend datasets, a named attacker or a confirmed data-exfiltration event. AFRINTEL therefore classifies the record as `Defacement`, with service disruption documented as an operational consequence rather than as a separate incident type.
- **Evidence qualification:** Website compromise and defacement are victim-confirmed; service disruption is documented. Backend dataset theft and attacker attribution remain unconfirmed.
- **Public sources:** TheCable and BusinessDay reports documented in the retrospective correction dataset.

----------------------------

### December 20, 2024

#### 🇧🇼 Botswana - Water Utilities Corporation (WUC)
- **Ransomware Group:** killsec
- **Sector:** Water / Utilities
- **Website:** [wuc.bw](https://www.wuc.bw)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Water Utilities Corporation (WUC) is the Botswana public utility responsible for water supply, distribution, and water services management across the country.

----------------------------

### December 21, 2024

#### 🇹🇳 Tunisia - Groupe SETCAR
- **Ransomware Group:** ransomhub
- **Sector:** Manufacturing / Industry
- **Website:** [groupe-setcar.com.tn](https://www.groupe-setcar.com.tn)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Groupe SETCAR is a Tunisian industrial group specialised in buses, coaches, industrial vehicles, automotive activities, and transport solutions.

----------------------------

### December 24, 2024

#### 🇿🇦 South Africa - Baker Tilly Morrison Murray
- **Ransomware Group:** sarcoma
- **Sector:** Professional / Business Services
- **Website:** [bakertillymm.co.za](https://www.bakertillymm.co.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Baker Tilly Morrison Murray is a South African professional services firm providing accounting, audit, tax, and advisory services.
- **Analysis:** AFRINTEL reviewed screenshots stored under the `bakertillymm.co.za` evidence directory and observed South African identity-document material, including a passport, alongside contract and employment-related documents. The sample is consistent with the type of sensitive client, employee or third-party records that may be handled by an accounting and advisory firm, but it does not establish the total scope of the alleged disclosure or the complete set of affected persons. The combination of identity documents and contractual records creates a risk of identity fraud, targeted social engineering, employee impersonation and secondary fraud against clients or business partners. The material supports a medium-confidence assessment that a data sample was published in connection with the Sarcoma claim; AFRINTEL does not reproduce names, document numbers, dates of birth, addresses or other personal data from the screenshots.

----------------------------

### December 24, 2024

#### 🇩🇿 Algeria - ASJP (Algerian Scientific Journal Platform)
- **Ransomware Group:** funksec
- **Sector:** Education / University
- **Website:** [asjp.cerist.dz](https://asjp.cerist.dz)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** ASJP (Algerian Scientific Journal Platform) is a national electronic publishing platform developed and operated by CERIST (Centre de Recherche sur l'Information Scientifique et Technique), an Algerian state research institution. It indexes and hosts full text for more than 700 Algerian scientific journals across all academic disciplines.
- **Analysis:** AFRINTEL reviewed a local archive consistent with the claim made by the threat actor funksec, comprising a server-side filesystem backup (tar archive, file ownership attributed to the www-data web-server account) of the platform's user-avatar directory tree, containing more than 1,700 individual user folders with account-linked profile images dated between 2017 and 2024, and a separate structured list of 499 name and email records. The user folders are predominantly tied to Algerian university email domains (including univ-biskra.dz, univ-tlemcen.dz, univ-batna.dz, univ-tiaret.dz, univ-guelma.dz, univ-alger2.dz, univ-alger3.dz, univ-constantine2.dz, univ-constantine3.dz, univ-msila.dz, univ-mosta.dz, lagh-univ.dz and edu.univ-oran1.dz, among others), consistent with ASJP's role as Algeria's national platform for academic journal publishing, alongside a smaller share of international academic contributors from other countries submitting to Algerian-hosted journals. The presence of a genuine server-side backup with web-server file ownership and multi-year, internally consistent timestamps, corroborated by a separate name/email export, supports a very high confidence assessment of a genuine compromise at the file-system level rather than a superficial claim. Given ASJP's role as a state-operated (CERIST) national research-publishing infrastructure, the scale of the exposed user base and the file-system-level nature of the access, this incident presents a systemic risk to Algeria's academic publishing ecosystem, including large-scale phishing, account takeover and impersonation of researchers and journal staff. AFRINTEL does not reproduce any name, email address or user-account identifier from the reviewed material.

----------------------------

- **Evidence qualification:** The reviewed server-side material strongly supports file-system-level compromise associated with ASJP. It does not independently establish ransomware encryption, service interruption or the original access mechanism.
### December 28, 2024

#### 🇿🇦 South Africa - Cell C
- **Ransomware Group:** ransomhouse
- **Sector:** Telecommunications
- **Website:** [cellc.co.za](https://www.cellc.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Cell C is the fourth-largest mobile network operator in South Africa, serving over 13 million customers (direct and MVNO). The company operates on an asset-light business model, leveraging roaming infrastructure from MTN and Vodacom, and is majority-owned by Blue Label Telecoms.

----------------------------

### December 29, 2024

#### 🇹🇿 Tanzania - WOSAC
- **Ransomware Group:** arcusmedia
- **Sector:** Transport / Logistics
- **Website:** [wosac.co.tz](https://www.wosac.co.tz)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** WOSAC is a Tanzanian maritime transport and shipping agency company providing freight, shipping, and associated logistics services.

----------------------------

## ✍🏿 Author
*Adama ASSIONGBON*
*SOC & Cyber Threat Intelligence Consultant*
[LinkedIn profile](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)
