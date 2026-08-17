[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-RQL%20export-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel%20Type-CTI-purple)

# List of African cyberattack victims - March 2026 (41 victims)
👉🏾 [**French version available here**](./victims_FR.md)

## Scope and methodology
This list records ransomware and data breach incidents targeting African entities during March 2026. Data is extracted and normalized from monitoring exports of leak sites (DLS) and complementary OSINT sources.

**Quality controls applied:**
- **Integrity:** Each line of the source dataset is kept as a distinct incident.
- **Normalization:** Visual harmonization of group names (e.g., LockBit 5.0, Qilin, APT73/Bashe).
- **Verification:** Validation of institutional URLs and enrichment of technical descriptions.

## Quick overview
- **Victims recorded:** 41
- **Countries affected:** 12 (plus 1 multi-country incident)
- **Actors observed:** 26 attributed actors; 1 incident without public attribution
- **Most affected countries:** South Africa (13), Morocco (8), Egypt (9)

### Incident typology
- **Ransomware claims or publications:** 19 incidents (46.3%)
- **Data breaches / system intrusions:** 22 incidents (53.7%)

### Notable incidents

- **Egypt:** 3.8 million records claimed in an incident attributed to the Ministry of Health.
- **Morocco:** a 300 GB publication attributed to the Ministry of Justice included court-case files.
- **Senegal:** according to ngCERT advisory ngCERT-2026-060005, the UBA Senegal cash-out operation involved 3,421 ATM transactions. Losses were previously reported at 1.143 billion FCFA; ngCERT describes them as exceeding USD 2 million.
- **South Africa:** a 3.8 TB exposure was attributed to the Gauteng provincial government.

> The entries below document observed claims, publications or reported incidents. AFRINTEL does not confirm a compromise without independent evidence.

### Breakdown by country
- 🇿🇦 South Africa: **13** victims
- 🇲🇦 Morocco: **8** victims
- 🇪🇬 Egypt: **9** victims
- 🇳🇬 Nigeria: **2** victims
- 🌍 Multi-country (Africa): **1** victim
- 🇩🇿 Algeria: **1** victim
- 🇸🇳 Senegal: **1** victim
- 🇬🇳 Guinea: **1** victim
- 🇿🇲 Zambia: **1** victim
- 🇲🇬 Madagascar: **1** victim
- 🇹🇳 Tunisia: **1** victim
- 🇳🇦 Namibia: **1** victim
- 🇹🇿 Tanzania: **1** victim

### Breakdown by actor
- **CrowStealer**: 5 victims
- **APT73/BASHE**: 4 victims
- **XP95**: 3 victims
- **xNov**: 3 victims
- **Qilin**: 2 victims
- **The Gentlemen**: 2 victims
- **INC Ransom**: 2 victims
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
- **Al-Sheikh**: 1 victim
- **Grubder (Bridges)**: 1 victim
- **Blackwinter99 (UNISA)**: 1 victim
- **zimablue (Loozap)**: 1 victim
- **Keymous (Guinea Health)**: 1 victim

### Ransomware vs Data Breaches by country
| Country               | Ransomware | Data Breach |
|-----------------------|------------|-------------|
| 🇿🇦 South Africa       | 7          | 6           |
| 🇲🇦 Morocco            | 5          | 3           |
| 🇪🇬 Egypt              | 3          | 6           |
| 🇳🇬 Nigeria            | 0          | 2           |
| 🌍 Multi-country       | 0          | 1           |
| 🇩🇿 Algeria            | 0          | 1           |
| 🇸🇳 Senegal            | 0          | 1           |
| 🇬🇳 Guinea             | 0          | 1           |
| 🇿🇲 Zambia             | 0          | 1           |
| 🇲🇬 Madagascar         | 1          | 0           |
| 🇹🇳 Tunisia            | 1          | 0           |
| 🇳🇦 Namibia            | 1          | 0           |
| 🇹🇿 Tanzania           | 1          | 0           |

## March 2026

### 01 March 2026
#### 🇿🇦 South Africa - Diesel-Electric Group
- **Ransomware group:** LockBit 5.0
- **Sector:** Automotive (Distribution & Services)
- **Website:** [diesel-electric.co.za](https://diesel-electric.co.za)
- **Status:** Claim - Unverified
- **Victim description:** Major automotive component distributor in Southern Africa, including Bosch Service franchises and e-CAR centers.

#### 🇪🇬 Egypt - Canadian International College (CIC)
- **Actor / Group:** CrowStealer
- **Sector:** Education / Higher education
- **Website:** [cic-cairo.edu.eg](https://www.cic-cairo.edu.eg/)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** First Canadian education provider in Egypt, affiliated with Cape Breton University (CBU). The leak (studentsdata.csv) contains 2,925 records: names, majors, levels, GPAs, years.

#### 🇿🇲 Zambia - ZISPIS (Zambia Integrated Social Protection Information System)
- **Threat Actor:** Spirigatito
- **Sector:** Government / Social Protection
- **Website:** [mcdss.gov.zm](https://www.mcdss.gov.zm)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim Description:** The ZISPIS system, a unified national registry used by the Zambian government to manage social protection programs, has been compromised. The breach reportedly affected approximately 15 million individuals and exposed over 34 million records. The leaked data includes full personal information (name, date of birth, gender, national identifiers), detailed socio-economic data (household conditions, education level, living standards), financial data (payments, balances, cycles), and geographic information (GPS coordinates). Published samples also confirm the exposure of system audit logs and user activity, indicating a deep compromise of the application infrastructure. 

- **Analysis:**
  AFRINTEL reviewed a post by the threat actor Spirigatito on a cybercriminal forum, titled "Government of Zambia (ZIPSIS) - 34M", along with an associated data sample. The sample consists of JSON exports from the ZISPIS system, operated by the Ministry of Community Development and Social Services (mcdss.gov.zm) as part of the Social Cash Transfer program. Observed beneficiary records include full name, gender, date of birth, national identifier, household GPS coordinates, district and village of residence, detailed socio-economic status (dwelling type, water and electricity access, food security, disability status) and payment data (amounts, cycles, delivery channel, and the named payment point representative with contact details). The sample also includes application activity logs tied to named government agent accounts (email addresses on the mcdss.gov.zm and cbt.gov.zm domains), with actions such as beneficiary record updates, payment validation, report generation and case closure due to death. These elements are consistent with direct access to the ZISPIS application database and its audit logs, rather than a limited partial export. AFRINTEL does not reproduce any individual name, national identifier, phone number or GPS coordinate from this sample. AFRINTEL did not have access to the full claimed 34 million records and cannot confirm this total volume or the initial access vector.

#### 🇿🇦 South Africa - Eventing South Africa
- **Actor / Group:** xNov
- **Sector:** Sports / Leisure
- **Website:** [eventingsa.co.za](https://www.eventingsa.co.za)
- **Leak Date:** January 16, 2026 (Identified in March 2026)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Eventing South Africa is the national governing body for eventing equestrian sports. xNov leaked a database containing club and member information: names, email addresses, login credentials (passwords), affiliation details, horse and rider records, competition data, and administrative/financial records (payments, invoices).

#### 🇩🇿 Algeria - Bridges (tebridges.dz)
- **Actor / Group:** Grubder
- **Sector:** Technology / Business Services (CRM)
- **Website:** [tebridges.dz](https://www.tebridges.dz)
- **Incident Date:** February 02, 2026
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Bridges is a technology solutions provider in Algeria. Grubder listed a database with ~672,000 active records (PII and CRM) including full names, primary phone numbers, detailed local addresses, postal codes, and account statuses. A data sample (CSV) validated the extraction.

  On the same day (February 02, 2026), a second account, Dripper, posted a separate listing offering the same claimed volume (~672,000 records) for the same domain, priced at 143 dollars with a Telegram/Session contact. AFRINTEL assesses this as most likely a repost or resale of the same database rather than a distinct intrusion. The Dripper account has since been banned by the forum for attempted scamming involving public data, and the sample attached to this repost mixed one record labeled Afghanistan with Algeria-labeled records, which weakens the reliability of this specific repost without calling into question the existence of Grubder's original claim.

#### 🌍 Africa (Multi-country) - Loozap (loozap.com)
- **Actor / Group:** zimablue
- **Sector:** E-commerce / Online classifieds
- **Website:** [loozap.com](http://loozap.com/)
- **Incident Date:** January 28, 2026 (identified in March 2026)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim description:** Loozap is a pan-African online classifieds platform (formerly Listings360) operating country-specific sections across dozens of African markets from a single shared application, rather than a standalone national service. A threat actor published a database containing approximately 34,000 user accounts.
- **Analysis:** AFRINTEL reviewed a structured sample of the published user table. The records are not tied to a single country: reviewed entries list users located in, among others, Egypt, Kenya, Ghana, Ethiopia, Nigeria and Mozambique, consistent with Loozap's role as a single shared platform database serving its country-specific subdomains rather than a per-country deployment. The reviewed fields include full name, email address, an SHA1-format password hash, registration IP address, precise geolocation coordinates, date of birth, gender and social-activity metadata (followers, likes, group memberships). The consistent database schema across records from different countries, together with the volume and internal structure of the sample, supports a high confidence assessment of a genuine, full compromise of the platform's shared user database rather than a claim limited to one national instance. Given the multi-country scope, the presence of precise geolocation data and weak (SHA1) password hashing, this incident creates a risk of large-scale account takeover, credential-stuffing against reused passwords, and targeted phishing affecting users across multiple African countries simultaneously. AFRINTEL does not reproduce any name, email address, password hash, IP address or geolocation coordinate from the reviewed sample.

### 02 March 2026
#### 🇪🇬 Egypt - Waste Management Regulatory Authority (WMRA)
- **Actor / Group:** CrowStealer
- **Sector:** Government / Environment
- **Website:** [garb.gov.eg](https://garb.gov.eg)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Agency under the Ministry of Environment responsible for waste management regulation. Database containing administrative data, internal records, information on partners and staff.

#### 🇪🇬 Egypt - Orascom Construction
- **Actor / Group:** CrowStealer
- **Sector:** Engineering & Construction
- **Website:** [orascom.com](https://orascom.com/)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Leading engineering and construction company operating in the Middle East, North Africa, and the United States. Compromised data: staff_id, full names, professional emails, departments, positions.

#### 🇪🇬 Egypt - Ministry of Health and Population (E-Portal)
- **Actor / Group:** CrowStealer
- **Sector:** Government / Health
- **Website:** [mohp.gov.eg](https://www.mohp.gov.eg)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Database of 3.8 million records (2019-2026) including full names, National ID, phone numbers, addresses, precise medical diagnoses, types of surgeries, treatment facilities.

### 03 March 2026
#### 🇿🇦 South Africa - Walter Sisulu University (WSU)
- **Actor / Group:** TelephoneHooliganism
- **Sector:** Education / University
- **Website:** [wsu.ac.za](https://www.wsu.ac.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Public university in the Eastern Cape. Data structured in three sections (Contacts, Enrollments, Tickets): dates of birth, emails, addresses, GPAs, scholarships, support history.

- **Analysis:**
  AFRINTEL reviewed a data sample corresponding to the Tickets section of this claim: an export of internal IT helpdesk tickets, structured with contact ID, email, phone number, first and last name, ticket status and category, priority, origin channel, assigned agent, opening and closing dates, resolution summary, internal agent notes, an SLA breach flag and region (among them Western Cape, Gauteng, KwaZulu-Natal, Eastern Cape and Northern Cape). Observed ticket categories include student portal access issues, email access, software installations and one case classified as Security involving suspicious account activity. This sample is consistent with the university's support helpdesk ticketing system and confirms, in addition to the Contacts and Enrollments sections already mentioned in the description, exposure of contact details and internal support operational content. AFRINTEL did not have access to the Contacts and Enrollments sections themselves during this review and cannot confirm the total volume of tickets involved or the initial access vector.

#### 🇪🇬 Egypt - Ministry of Education and Technical Education
- **Actor / Group:** CrowStealer
- **Sector:** Government / Education
- **Website:** [moe.gov.eg](https://moe.gov.eg)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Data on students and staff: national IDs, full names, addresses, academic records.

#### 🇲🇦 Morocco - National Office of University, Social and Cultural Works (ONOUSC)
- **Actor / Group:** xNov
- **Sector:** Education / Government
- **Website:** [amo.onousc.ma](https://amo.onousc.ma)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Body responsible for student social services in Morocco (scholarships, university housing, health coverage). Exposure of 3,631 student records related to Mandatory Health Insurance (AMO): names, CINE numbers, university registration numbers, CNE, dates of birth, enrollment statuses.

### 04 March 2026
#### 🇲🇦 Morocco - Outsourcia
- **Ransomware group:** Qilin
- **Sector:** Business Process Outsourcing (BPO)
- **Website:** [outsourcia.com](https://www.outsourcia.com)
- **Status:** Claim - Unverified
- **Victim description:** Major customer relationship operator based in Casablanca, managing business processes for international accounts.

### 05 March 2026
#### 🇪🇬 Egypt - Rowad Modern Engineering
- **Ransomware group:** Crypto24
- **Sector:** Engineering & Construction
- **Website:** [rowad-rme.com](http://www.rowad-rme.com)
- **Status:** Claim - Unverified
- **Victim description:** Egyptian construction company specializing in infrastructure projects and commercial buildings.

### 06 March 2026
#### 🇪🇬 Egypt - INTERACT TECHNOLOGY SOLUTIONS
- **Ransomware group:** PEAR
- **Sector:** IT Consulting
- **Website:** [interactts.com](http://interactts.com)
- **Status:** Claim - Unverified
- **Victim description:** Company providing critical technology and infrastructure solutions in Egypt.

#### 🇲🇬 Madagascar - Orange Madagascar
- **Ransomware group:** Qilin
- **Sector:** Telecommunications
- **Website:** [orange.mg](https://www.orange.mg/)
- **Status:** Claim - Unverified
- **Victim description:** Telecommunications leader in Madagascar, operating internet, mobile, and mobile banking services.

### 09 March 2026
#### 🇹🇳 Tunisia - K.PROPHA (Karray Produits Pharmaceutiques)
- **Ransomware group:** The Gentlemen
- **Sector:** Health / Pharmaceutical
- **Website:** [kpropha.com](http://kpropha.com)
- **Status:** Claim - Unverified
- **Victim description:** Tunisian company specializing in the distribution of pharmaceutical and para-pharmaceutical products.

### 12 March 2026
#### 🇲🇦 Morocco - HACA (High Authority for Audiovisual Communication)
- **Ransomware group:** APT73 / Bashe
- **Sector:** Government / Media
- **Website:** [haca.ma](http://haca.ma)
- **Status:** Claim - Unverified
- **Victim description:** Constitutional body responsible for regulating audiovisual communication in Morocco.

### 13 March 2026
#### 🇿🇦 South Africa - Lion of Africa Insurance
- **Ransomware group:** Lynx
- **Sector:** Insurance services
- **Website:** [lionsureins.com](http://lionsureins.com/)
- **Status:** Claim - Unverified
- **Victim description:** South African insurance company handling large volumes of personal and financial data.

#### 🇿🇦 South Africa - Gauteng Provincial Government
- **Actor / Group:** XP95
- **Sector:** Government / Public administration
- **Website:** [gauteng.gov.za](https://www.gauteng.gov.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Manages the most populous province in South Africa (Johannesburg, Pretoria). 3.8 TB of data (3.6 million files) exfiltrated: health, education, housing, economic development.

### 14 March 2026
#### 🇪🇬 Egypt - Grid Fine Finishes
- **Ransomware group:** Payload
- **Sector:** Fit-out / Construction
- **Website:** [gridff.com](http://gridff.com)
- **Status:** Claim - Unverified
- **Victim description:** Egyptian company specializing in high-end interior fit-out for commercial and residential sectors.

### 17 March 2026
#### 🇿🇦 South Africa - University of South Africa (UNISA)
- **Actor / Group:** Blackwinter99
- **Sector:** Education / Higher Education
- **Website:** [unisa.ac.za](https://www.unisa.ac.za)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** UNISA is Africa's largest distance learning institution. Blackwinter99 publicly disclosed login credentials for the site's administration page on an underground forum, providing direct access to high-level platform privileges, enabling massive student data exfiltration, tampering with academic records, or complete takeover of the web infrastructure.

### 19 March 2026
#### 🇳🇦 Namibia - Namibia Airports Company
- **Ransomware group:** INC Ransom
- **Sector:** Air transport
- **Website:** [airports.com.na](http://airports.com.na)
- **Status:** Claim - Unverified
- **Victim description:** Official manager of national airports in Namibia.

### 20 March 2026
#### 🇿🇦 South Africa - The Unlimited
- **Ransomware group:** DragonForce
- **Sector:** Insurance services
- **Website:** [theunlimited.co.za](http://theunlimited.co.za)
- **Status:** Claim - Unverified
- **Victim description:** Provider of insurance products including health, auto, legal, and life.

#### 🇲🇦 Morocco - Ministry of Justice
- **Actor / Group:** anisanas2
- **Sector:** Government / Justice
- **Website:** [justice.gov.ma](https://www.justice.gov.ma)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Exfiltration of 300 GB including more than 150,000 court case files (2019-2026). Disputes between major Moroccan companies and individuals (12 billion MAD). Documents: IDs, bank statements, court records, invoices.

### 21 March 2026
#### 🇿🇦 South Africa - Elundini Local Municipality
- **Ransomware group:** The Gentlemen
- **Sector:** Local government
- **Website:** [elundini.gov.za](http://elundini.gov.za)
- **Status:** Claim - Unverified
- **Victim description:** Municipal administration dedicated to sustainable development in the Eastern Cape province.

### 22 March 2026
#### 🇿🇦 South Africa - Semenya Furumele Consulting Engineers
- **Ransomware group:** NightSpire
- **Sector:** Engineering consulting
- **Website:** [sfce.co.za](http://www.sfce.co.za)
- **Status:** Claim - Unverified
- **Victim description:** Engineering consulting firm based in South Africa.

### 24 March 2026
#### 🇸🇳 Senegal - United Bank for Africa (UBA Senegal)
- **Actor / Group:** Unattributed
- **Sector:** Finance / Banking
- **Website:** [ubasenegal.com](https://www.ubasenegal.com)
- **Date of attack:** 30-31 January 2026 (disclosed on 24 March 2026)
- **Status:** Under Investigation
- **Reference:** https://cert.gov.ng/advisories/alert-on-cyber-enabled-atm-cash-out-attacks-targeting-african-financial-institutions
- **Taxonomy note:** This incident does not fit AFRINTEL's four incident types (Ransomware, Data Leak, Access Sale, Defacement). It describes a confirmed operational fraud via compromised privileged access to card-authorization infrastructure, not a leak-site claim, a data publication or an advertised access sale. No Incident type is assigned; this entry is excluded from the structured Ransomware/Data Leak/Access Sale/Defacement counters.
- **Victim description:** According to ngCERT, a cyber-enabled ATM cash-out operation affecting UBA Senegal involved 3,421 ATM transactions. Losses were previously reported at 1.143 billion FCFA; the ngCERT advisory describes them as exceeding USD 2 million. The advisory assesses that privileged access to card-authorization infrastructure likely enabled manipulation of transaction controls and coordinated withdrawals. The initial-access vector, exact technical sequence and any insider involvement remain unknown. Phishing, supply-chain weaknesses, insider access and ATM malware are presented by ngCERT as possible scenarios for this attack class, not as confirmed findings for UBA Senegal.

### 26 March 2026
#### 🇿🇦 South Africa - ETFSA
- **Ransomware group:** INC Ransom
- **Sector:** Wealth Management
- **Website:** [etfsa.co.za](http://ETFSA.co.za)
- **Status:** Claim - Data Sample Published
- **Victim description:** South African financial services platform specializing in exchange-traded funds (ETFs).

- **Analysis:**
  AFRINTEL reviewed the extortion post published for this victim, which references a claimed company revenue of approximately USD 8 million and names an individual identified as the platform's managing director. The post states that confidential and personal client data would be published, and displays thumbnail previews of numerous documents. AFRINTEL reviewed one accessible sample: an abridged death certificate issued by the South African Department of Home Affairs, containing an identity number, full name, date of birth and cause of death. This indicates that the exposed material includes client Know Your Customer (KYC) and estate-related identity documents rather than only account or transaction records, consistent with a wealth management and financial advisory client base. AFRINTEL did not access the remaining files and cannot confirm the total number of clients affected or the initial access vector.

#### 🇲🇦 Morocco - Maroc Telecom
- **Ransomware group:** APT73 / Bashe
- **Sector:** Telecommunications
- **Website:** [iam.ma](http://iam.ma)
- **Status:** Claim - Data Sample Published
- **Victim description:** Historic telecommunications operator in Morocco, providing mobile, internet, and fixed-line services.

- **Analysis:**
  AFRINTEL reviewed sample screenshots published in connection with this claim. The material shows internal customer relationship and technical support screens (GRC/complaint-tracking interfaces) referencing client identifiers, contact details, installation addresses and fault-ticket records related to fixed-line and fiber-optic service issues. This is consistent with access to Maroc Telecom's customer support and complaint-management systems rather than a bulk subscriber database export. AFRINTEL did not access the underlying systems and cannot confirm the volume of records involved or the initial access vector.

#### 🇲🇦 Morocco - 2M TV
- **Ransomware group:** APT73 / Bashe
- **Sector:** Media & Audiovisual
- **Website:** [2m.ma](http://2m.ma)
- **Status:** Claim - Data Sample Published
- **Victim description:** Moroccan national television channel.

- **Analysis:**
  AFRINTEL reviewed sample documents published in connection with this claim, consisting of internal human resources material: an employee curriculum vitae for an audiovisual staff member, an internal list of employees holding driving licences, and an employment certificate ("attestation de travail") template bearing the 2M letterhead. This indicates exposure of staff personnel records rather than broadcast systems or customer data. AFRINTEL also reviewed a separate dataset: a full mailbox export in .eml format (1,777 messages), whose associated metadata (message identifiers in Microsoft Exchange/Office 365 format and a last-received timestamp dated November 2025) indicates the compromise of an individual professional mailbox, likely tied to 2M's Rédaction/News department, rather than a static set of documents. The correspondence covers 123 distinct internal 2m.ma addresses and relates notably to editorial planning for an internal show, administrative processes (including a press card request) and HR exchanges; approximately 348 messages carry attachments (images, PDFs, Word documents and Excel spreadsheets). Several message subjects do not correspond to any identifiable editorial activity and are consistent with unsolicited spam or social-engineering attempts received in this mailbox. AFRINTEL does not name the mailbox owner and does not reproduce message content or the identity of third-party correspondents. AFRINTEL did not access further files and cannot confirm the total number of employee records involved, the current access status of this mailbox, or the initial access vector.

#### 🇲🇦 Morocco - Royal Institute for Strategic Studies (IRES)
- **Ransomware group:** APT73 / Bashe
- **Sector:** Research / Think tank
- **Website:** [ires.ma](http://ires.ma)
- **Status:** Claim - Data Sample Published
- **Victim description:** Strategic analysis center attached to the Moroccan Royal Cabinet.

- **Analysis:**
  AFRINTEL reviewed sample documents published in connection with this claim, consisting of curricula vitae of researchers and consultants associated with the institute, covering academic profiles (doctoral and master's-level research in public law and international relations), professional experience references and, in one case, contact details including an email address and phone number. This indicates exposure of staff and researcher personnel records. AFRINTEL did not access further files and cannot confirm the total number of records involved or the initial access vector.

### 29 March 2026
#### 🇿🇦 South Africa - Statistics South Africa (Stats SA)
- **Ransomware group:** XP95
- **Sector:** Government / National Statistics
- **Website:** [statssa.gov.za](https://www.statssa.gov.za)
- **Status:** Claim - Data Sample Published
- **Victim description:** Stats SA is the national statistical agency of South Africa. XP95 exfiltrated 154 GB of data (453,362 files). The breach potentially compromises sensitive socio-economic data, census records, employment information, inflation data, and national administrative records. A $100,000 ransom has been demanded, with a public sale deadline set for April 20, 2026.

#### 🇿🇦 South Africa - Gauteng City Region Academy (GCRA)
- **Ransomware group:** XP95
- **Sector:** Education / Training (Provincial Government)
- **Website:** [gcra.gauteng.gov.za](https://gcra.gauteng.gov.za)
- **Status:** Claim - Data Sample Published
- **Victim description:** The GCRA is the agency responsible for skills development in the Gauteng province. The exfiltration of 147 GB of data potentially compromises student records (bursaries, registrations, PII), training program data, and the academy's administrative documents. XP95 has set a ransom deadline before the public sale of the files.

### 30 March 2026
#### 🇹🇿 Tanzania - SBC Tanzania Limited
- **Ransomware group:** Morpheus
- **Sector:** Food & Beverage
- **Website:** [sbctanzania.co.tz](http://sbctanzania.co.tz)
- **Status:** Claim - Unverified
- **Victim description:** Beverage manufacturer and distributor, official bottler of PepsiCo in Tanzania.

#### 🇿🇦 South Africa - Nashua
- **Ransomware group:** Coinbase Cartel
- **Sector:** IT & Managed Services
- **Website:** [nashua.co.za](http://nashua.co.za)
- **Status:** Claim - Unverified
- **Victim description:** Major provider of integrated technology solutions and managed services for businesses.

#### 🇳🇬 Nigeria - Ahmadu Bello University (ABU Zaria)
- **Actor / Group:** AshleyWood2022
- **Sector:** Education / Higher education
- **Website:** [abu.edu.ng](https://www.abu.edu.ng)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim description:** One of the largest research universities in Nigeria. Database (`tbl_flattened.csv` & `abu.sql`) with over 11,000 records: academic and non-academic staff (names, departments, ranks, qualifications, gender, date of birth, districts of origin).

- **Reliability note:**
  AFRINTEL reviewed the forum post by AshleyWood2022 dated March 30, 2026, together with a posted download link (gofile.io) and a visible data sample. The reviewed sample covers staff attached to the Office of the Vice Chancellor and its sub-units (ABU/FM Radio, ABUCONS, Central Procurement Unit, Academic Planning, University Advancement, Equipment Maintenance and Development Centre, Internal Audit, ITF/SIWES Coordination Centre, Procurement and Security Division), with 237 rows in this section alone, consistent in scale with the broader 11,000-plus record claim.

- **Analysis:**
  The sample follows a consistent schema: local government area and senatorial district of origin, state, geopolitical zone, date of birth, gender, faculty, department, staff category (academic or non-academic), rank and highest qualification. In the reviewed rows, the date-of-birth field is uniformly masked (`0000-00-00`) and no staff names, phone numbers or national identifiers are visible; the actor's post claims that names and other personal fields are present in the full dataset, which AFRINTEL did not download or independently verify. The structural consistency across 237 rows and the presence of a working download link support a stronger assessment than a bare claim, though the completeness, authenticity and full content of the archive remain unconfirmed. If the full claim is accurate, exposure of staff demographic and organisational data could support targeted social engineering, profiling by region, gender or department, and impersonation of university staff. AFRINTEL does not reproduce any record, field value or download link from the reviewed material.

### 31 March 2026
#### 🇳🇬 Nigeria - Remita (SystemSpecs)
- **Actor / Group:** Bytetobreach
- **Sector:** Fintech / Payment services
- **Website:** [remita.net](https://www.remita.net)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Major payment platform in Nigeria used by individuals, businesses, and government. 3 TB breach: 800 GB of KYC documents (IDs, passports, bank statements, invoices), MySQL/Postgres databases, source code, Docker registries, government HSM keys, over 35,000 password hashes.

- **Analysis:**
  AFRINTEL reviewed a set of technical elements associated with this claim. A credentials file lists approximately 35,800 email address / password hash pairs (bcrypt format), covering both internal accounts (agents, operators) and likely platform customer accounts; AFRINTEL did not extract or attempt to crack any hash. Screenshots show a restored instance of the platform's databases in a SQL administration tool, including a business owner table (BVN number, ID type and number, base64-encoded identity document), an interbank transaction table (amounts, beneficiary bank codes, channel, payment reference), an internal admin account table (SystemSpecs agents with role and status) and a customer personal information table (date of birth, email, phone number, KYC status, hashed password). Other screenshots show a source code archive covering several platform microservices, including an SFTP-based encrypted communication module with the Central Bank of Nigeria (CBN) for exchanging payment instructions, an integration with the Pan-African Payment and Settlement System (PAPSS), a virtual wallet system built in partnership with OPay, and OTP verification logic. An additional screenshot shows a directory of key files named after more than twenty Nigerian banks (including GTBank, Zenith, UBA, First Bank, Access, FCMB, Fidelity, Sterling, Stanbic, Ecobank, UBN, Wema, Unity, Providus, Heritage and Citibank), consistent with master encryption keys tied to interbank integration; AFRINTEL did not verify the content or validity of these files. Secret-scanning tool results run against the source code repositories show detection of API keys, cloud access tokens and hardcoded database credentials in several configuration files, associated with SystemSpecs employee email addresses. AFRINTEL also reviewed the structure of a Git backup archive (approximately 34,800 files) covering roughly forty distinct internal repositories with full commit history, corresponding to the entire internal "remitacenta" GitLab organization: interbank and pan-African payment components (including a PAPSS connector and an ISO 20022 payment message builder, a standard used for interbank messaging), a fraud detection engine, a card tokenization SDK, Kubernetes infrastructure-as-code (three separate manifest sets) and a business intelligence module (Superset), the latter alone accounting for over a quarter of the archive's files. The archive contains approximately 200 production configuration files, 354 Helm "values.yaml" files and more than 400 file names explicitly referencing secrets, consistent with potential exposure of numerous additional credentials beyond those already flagged by the scanning tools; AFRINTEL did not open these files individually and does not reproduce any further secret. One additional file, marked as an unfinished download, corresponds to a backup image in Veeam Backup & Replication format (XBSTCK01 signature, tool version 12.1.2) referencing InnoDB log files, consistent with a system-level backup including a MySQL/MariaDB database; as this file is incomplete, AFRINTEL was unable to mount it or review its content. A final screenshot shows access, via cloud credentials extracted from the source code, to a cloud storage bucket dedicated to KYC documents containing approximately 657,000 files for a raw volume of approximately 588 GB, as well as several other buckets tied to the company's internal GitLab infrastructure (backups, artifacts, container registry). AFRINTEL does not reproduce any individual credential, key, token, hash, account name or identity document from these elements. Taken together, these observations are consistent with a deep compromise of Remita's development and production infrastructure, potentially extending to its banking and pan-African integration systems, but AFRINTEL did not verify the authenticity or currency of each individual element and cannot confirm the exact extent of access obtained or the initial access vector.

#### 🇲🇦 Morocco - Smarteez (L'Oréal Morocco Supply Chain Provider)
- **Actor / Group:** xNov
- **Sector:** Digital Marketing / Cosmetics (L'Oréal Supply Chain)
- **Website:** [smarteez.eu](https://smarteez.eu)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Smarteez is a Moroccan digital provider used by L'Oréal Morocco for field operations management. Exposure of critical data: information on 296 pharmacies (GPS, segmentation), 361,000 sales/KPI records, 22 plaintext OAuth2 application secrets, complete administrative logs. A production APK was also disclosed.

#### 🇪🇬 Egypt - Semsar Masr (semsarmasr.com)
- **Actor / Group:** Al-Sheikh
- **Sector:** Real Estate / Online Classifieds
- **Website:** [semsarmasr.com](https://www.semsarmasr.com)
- **Date of breach:** January 2026 (identified in March 2026)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Semsar Masr is an Egyptian real estate classifieds platform, active since 2007, enabling the posting and browsing of listings for apartments, land and other properties for sale or rent in Egypt.
- **Analysis:** AFRINTEL reviewed a post published on January 28, 2026 by the actor Al-Sheikh concerning the `tb_members_Profiles` table of semsarmasr.com, stating it contains 185,024 rows and that user passwords are stored in plaintext. The sample displayed in the post includes a field schema covering user ID, account status, email address, phone number, password, user role, contact name, company name, address, social media handles (WhatsApp, Telegram, LinkedIn, Twitter, Facebook), date of birth, occupation, gender, marital status, email/phone verification flags, and account creation/update dates. Ten complete records are directly visible in the sample, with email addresses, Egyptian and international phone numbers, full names and plaintext passwords tied to accounts created on January 28, 2026. The consistency of the schema with a real-estate classifieds platform and the presence of unhashed passwords in the sample support a high confidence level regarding the authenticity of this leak, although the total claimed volume of 185,024 rows could not be independently verified beyond the observed sample. The exposure of plaintext passwords, combined with user contact details and identity, creates a high risk of account takeover, password reuse across other services and targeted phishing. AFRINTEL does not reproduce any name, email address, phone number or password from the reviewed sample.

#### 🇬🇳 Guinea - Ministry of Health (sante.gov.gn)
- **Actor / Group:** Keymous
- **Sector:** Government / Public Health
- **Website:** [sante.gov.gn](https://sante.gov.gn/)
- **Date of incident:** July 2025 (observed activity, identified in March 2026)
- **Status:** Under Investigation
- **Incident type:** Data Leak
- **Victim description:** The official website of Guinea’s Ministry of Health is directly linked to compromised internal systems, including DHIS2 dashboards exposed by Keymous. The correlation between access to health surveillance tools, leaked government data (emails, staff records), and ministerial infrastructure strongly suggests a broader compromise of the ministry’s digital ecosystem. This exposure may enable targeted attacks, data manipulation, and influence operations.
