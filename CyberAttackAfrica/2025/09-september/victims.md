[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# List of African cyberattack victims in September 2025 (18 victims)
👉🏾 [**French version available here**](./victims_FR.md)
## September 2025

### 02 September 2025
#### 🇩🇿 Algeria - Université des Frères Mentouri Constantine 1 (UMC1)
- **Incident type:** Data Leak
- **Actor / Group:** Fire Wire
- **Sector:** Education / Higher Education
- **Website:** university-dz.net
- **Status:** Claim - Data Sample Published
- **Victim Description:** Université des Frères Mentouri Constantine 1 (UMC1) is a major Algerian public university. The claiming actor states an exfiltration of over 10 GB, a volume AFRINTEL did not collect or analyze. The reviewed files, exfiltrated via what appears to be a shared academic web platform (university-dz.net), include Master 2 semester 1 (January 2025) exam schedules with dates, modules, rooms and departments; a set of over 200 detailed student records (full name, university enrollment number, TD group and per-subject grades, including exclusion/pass status annotations) from L1 students (2015-2016 cohort); a vehicle compliance directory with phone numbers and emails; and a conference template listing contacts and affiliations for a 2024 academic event (NCME). The combination of academic records, personal contact details and administrative documents creates a significant risk of identity fraud, targeted phishing and vishing against students, staff and affiliated contacts. The claiming actor identifies itself as "Fire Wire".

### 04 September 2025
#### 🇳🇬 Nigeria - MobileSub
- **Actor / Group:** Not specified
- **Sector:** Fintech / Payment Services
- **Website:** [mobilesub.com.ng](https://mobilesub.com.ng)
- **Source file date:** 4 September 2025
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** MobileSub is a Nigerian digital-services platform providing mobile airtime, data, utility, cable-TV, betting and related payment functions.
- **Analysis:** AFRINTEL reviewed a local SQL dump of approximately 14.3 MB containing 42 tables and 306 INSERT blocks. The schema includes user accounts, KYC, API keys, transaction history, transfers, airtime, data, electricity, examination registration, betting, cable-TV and other payment-service modules, as well as user backup tables. The source file timestamp is 4 September 2025; this is treated as the AFRINTEL discovery/source timestamp, not proof of the original compromise date. The dataset may expose customer identity, contact, KYC, transaction and authentication-related information. No personal values, API keys or credentials are reproduced. The authenticity, completeness and publication context remain unverified.
- **Source analysis note:** The dump contains credential- and secret-sensitive table categories; AFRINTEL did not attempt authentication, access or secret recovery.

### 05 September 2025
#### 🇪🇬 Egypt - MeamarGroup
- **Ransomware Group:** obscura
- **Sector:** Real Estate / Construction / Engineering
- **Website:** https://meamargroup.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** MeamarGroup (including Meamar Real Estate Development and Meamar Construction) is a major player in the Egyptian construction sector for over 25 years. Based in Cairo (New Cairo), the group manages over 400 projects ranging from luxury residential complexes to industrial and medical facilities (like the Biogeneric Pharma factory).
- **Analysis:** AFRINTEL reviewed a local server-side filesystem archive (491 files and directories, all owned by the www-data web-server account) consistent with this claim. Directory-level timestamps for this collection cluster around 05 September 2025, matching this entry's claim date, while the bulk of the underlying files carry an earlier timestamp of 27 August 2025, suggesting an initial data-staging event ahead of the public claim. See the fuller analysis under the 13 October 2025 entry ("meamargroup.com (third attack)"), which documents the same archive in detail, including internal accounting ledgers, a large sales call-center/prospect-contact archive, employee CVs, and file copies bearing the ".obscura" ransomware encryption extension. AFRINTEL treats these as related records of the same underlying compromise rather than independent incidents. AFRINTEL does not reproduce any client name, contact number, employee name or financial figure from the reviewed material.

### 06 September 2025
#### 🇨🇮 Ivory Coast - NSIA Assurances
- **Incident type:** Data Leak
- **Actor / Group:** Tanaka
- **Sector:** Insurance / Financial Services
- **Website:** https://www.nsiaassurances.com
- **Status:** Claim - Unverified
- **Victim Description:** Leader in insurance and banking in West and Central Africa, a systemic player based in Abidjan, Ivory Coast. The actor claims to be circulating a database of over 2.5 million transactional and financial records; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 08 September 2025
#### 🇳🇬 Nigeria - The Promise Nigeria
- **Ransomware Group:** yurei
- **Sector:** Catering / Food Services / Industrial Catering
- **Website:** https://www.thepromisenig.com
- **Status:** Claim - Unverified
- **Victim Description:** The Promise is a leading Quick Service Restaurant (QSR) chain and industrial catering service in Nigeria, particularly established in Port Harcourt and the Niger Delta region.

### 09 September 2025
#### 🇲🇦 Morocco - Dolidol
- **Ransomware Group:** thegentlemen
- **Sector:** Manufacturing Industry / Bedding / Furniture
- **Website:** https://www.dolidol.ma
- **Status:** Claim - Unverified
- **Victim Description:** Dolidol (a subsidiary of the Palmeraie Industries et Services group) is the undisputed leader in bedding and polyurethane foam in Morocco.

### 09 September 2025
#### 🇿🇼 Zimbabwe - Proplastics Limited
- **Ransomware Group:** thegentlemen
- **Sector:** Manufacturing Industry (Plastics)
- **Website:** https://www.proplastics.co.zw
- **Status:** Claim - Unverified
- **Victim Description:** Proplastics Limited is the leading manufacturer and supplier of plastic piping systems (PVC, HDPE) in Zimbabwe.
- **Analysis:** The supplied local evidence set contains 63 files associated with Proplastics, including PDFs, spreadsheets, image files and text files. Filenames indicate business records covering invoices and credit memos, account balances, bills of materials, backorders, deliveries, sales analysis and branch reporting. The files carry dates spanning 2023-2024, while the directory metadata places the collection in September 2025; these timestamps are treated as evidence context, not as a confirmed intrusion or publication date. The material supports the plausibility and potential sensitivity of the September 2025 claim, but does not independently establish the access vector, the complete scope of the dataset or the attribution to thegentlemen. AFRINTEL does not reproduce names, account details, financial values, customer records or document contents.

### 10 September 2025
#### 🇳🇬 Nigeria - Princeps Credit Systems Limited
- **Ransomware Group:** killsec
- **Sector:** Finance
- **Website:** https://princepsfinance.com
- **Status:** Claim - Unverified
- **Victim Description:** Financial institution based in Lagos, specializing in consumer credit and SME financing.

### 11 September 2025
#### 🇳🇦 Namibia - Epia Financial Services
- **Ransomware Group:** radar
- **Sector:** Financial Services
- **Website:** https://epiafs.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Financial institution based in Windhoek, offering wealth management, investment advice, and brokerage services in Namibia.
- **Analysis:** Exfiltrated mailbox material attributed to the claim (email correspondence sent to and from EPIA's reception and administration mailboxes with Bank Windhoek/Capricorn Group, First National Bank of Namibia and NamPost regarding client account verifications) is examined, together with the structure of a representative sample of pension fund administration files at the field/column level, without opening or extracting individual member-level rows. The reviewed material corresponds to EPIA's role as administrator for the Namibia Building Workers Pension Fund (NBWPF) and other corporate clients. Membership data workbooks (e.g. a January 2025 extract) contain multiple sheets of several thousand member records each (Actives, Deferred, Unclaimed, Exits) sharing a consistent field schema: member number, surname, first name, other names, company reference, date of birth, national ID number, passport number, contributor status, member status, employer name, gender, employment and fund-membership dates, monthly and annual salary, fund credit amount and date, last contribution date, exit date and payment details. A separate actuarial data extract covers the period September 2022 to April 2024 with a comparable schema and scale. Additional files inspected structurally include multi-year admin and income-allocation reports (aggregate financial transaction summaries per period) and signed client authorization forms, the most recent dated June 2025. AFRINTEL did not open every file in the set; the consistent file-naming pattern and email correspondence indicate the same categories of records recur across the full 2022-2025 period. The combination of national identification numbers, dates of birth, salary and pension fund-credit data for several thousand individuals, together with employer and banking correspondence, represents a high-impact exposure. The breadth, continuity through mid-2025 and organisational specificity of the reviewed material support a high confidence assessment of mailbox and file compromise, independent of the ransomware group's public claim. The local evidence set contains 73 files totaling approximately 79.8 MB, including spreadsheets, reports, presentations, a DOCX employer file and image files. The January 2025 membership workbook contains a summary sheet and member-state worksheets (Actives, Deferred, Unclaimed and Exits), with worksheet dimensions reaching 8,652 summary rows and up to 35 columns; the reviewed field structure includes member, employer, identity, employment, salary, pension-credit, contribution, exit and payment fields. The actuarial extract contains 8,168 rows and 167 columns for a period extending from September 2022 to April 2024. Material timestamped 11 September 2025 is consistent with the September discovery context. No member names, identification numbers, account details, signatures, salary figures or correspondence content are reproduced from the reviewed sample.


### 11 September 2025
#### 🇦🇴 Angola - Angola Government Employees Database (pape.gov.ao)
- **Incident type:** Data Leak
- **Actor / Group:** privilege, post published on a cybercriminal forum
- **Sector:** Government / Public Administration
- **Website:** [pape.gov.ao](https://pape.gov.ao)
- **Status:** Claim - Data Sample Published
- **Victim Description:** The source presents pape.gov.ao as an Angolan government-related platform and claims to offer employee records from different sectors and administrative areas.
- **Analysis:** The publication dated 11 September 2025 claims a database of 245 Angolan government employees and lists fields for employee identifiers, names, dates of birth, administrative area and function. The local TXT file supplied for review contains 244 non-empty comma-separated lines, including one header and approximately 243 data rows, with six fields per row. This supports the existence of a structured employee-data sample but does not independently confirm the advertised total, the exact government body, the dataset's authenticity or its completeness. AFRINTEL does not reproduce any names, identifiers, dates of birth or other personal data from the file.
### 12 September 2025
#### 🇨🇩 Congo (DRC) - Public Administration Reform Fund (FRAP)
- **Incident type:** Data Leak
- **Actor / Group:** privilege
- **Sector:** Government / Administration
- **Website:** [frap.cd](https://frap.cd/)
- **Status:** Data Fully Published
- **Victim description:** Body responsible for modernizing public administration in the DRC.
- **Analysis:** AFRINTEL reviewed the DarkForums listing itself, posted on 12 September 2025 by the threat actor privilege (VIP tier, account created September 2025), titled "FRAP.CD — 1,136 LINES | Full User Data | Gov/Staff Access". The post describes a database of 1,136 records comprising usernames and hashed passwords (multiple hash formats), personal identifiers (first name, last name, gender), contact details (email, phone) where available, internal reference and document-designation fields, and system metadata (creation time, last login, last password update, created/updated by, account status). The actor describes the material as covering administrator and sector-staff accounts on the FRAP.CD portal, consistent with the platform's role in managing administrative profiles and internal staff accounts for the Public Administration Reform Fund. The full dataset is offered through an external hosted link rather than shown directly in the post; AFRINTEL was unable to independently validate the hosted file's authenticity or completeness. Given the account credentials and personal identifiers described, exposure of this material would create a risk of credential-based access to the portal and of targeted phishing against DRC public administration staff. AFRINTEL does not reproduce any usernames, passwords, personal identifiers or contact details from the reviewed post.

### 14 September 2025
#### 🇰🇪 Kenya - Office Of The Registrar Of Political Parties
- **Ransomware Group:** qilin
- **Sector:** Public administrations
- **Website:** https://www.orpp.go.ke
- **Status:** Claim - Unverified
- **Victim Description:** Kenyan state body responsible for the registration, regulation, and supervision of political party funding.

### 16 September 2025
#### 🇰🇪 Kenya - Jubilee Life Insurance
- **Ransomware Group:** warlock
- **Sector:** Insurance / Financial Services
- **Website:** https://jubileelife.com
- **Status:** Claim - Unverified
- **Victim Description:** Major player in life insurance and fund management in Kenya, a subsidiary of Jubilee Holdings Limited.

### 17 September 2025
#### 🇪🇬 Egypt - Accflex ERP
- **Ransomware Group:** arcusmedia
- **Sector:** Technology / ERP Software Publishing
- **Website:** https://www.accflex.com
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian publisher of integrated management solutions (accounting, HR, production) used by numerous companies in the Middle East and Africa.

### 22 September 2025
#### 🇲🇦 Morocco - Fractalite (fractalite.com)
- **Ransomware Group:** killsec
- **Sector:** Technology / Digital Services / Software Development
- **Website:** https://fractalite.com
- **Status:** Claim - Unverified
- **Victim Description:** Fractalite is a Moroccan digital consulting and engineering agency, specializing in software development and digital support for businesses.

### 24 September 2025
#### 🇳🇬 Nigeria - Kolomoni Microfinance Bank
- **Actor / Group:** Not specified
- **Sector:** Microfinance / Banking
- **Website:** [kolomonimfb.com](https://kolomonimfb.com)
- **Source archive date:** 24 September 2025
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Kolomoni Microfinance Bank is a Nigerian financial institution serving account holders through digital and microfinance banking services.
- **Analysis:** AFRINTEL reviewed the supplied RAR extraction and its Kolomoni CSV. The file contains 37,825 data rows and 12 columns covering account name and number, email, phone, gender, date of birth, account status, address, local-government area, state, last login and record date. The combination of financial identifiers, contact details, demographic fields, location and authentication metadata creates risks of phishing, account takeover, identity fraud and targeted financial scams. The archive timestamp is 24 September 2025, while the internal CSV metadata includes an earlier 24 August 2025 file date; neither proves the original compromise date. No personal values are reproduced. The actor, publication venue, authenticity and completeness remain unspecified or unverified.

### 29 September 2025
#### 🇸🇳 Senegal - Direction Générale des Impôts et des Domaines (DGID)
- **Ransomware Group:** blackshrantac
- **Sector:** Public Administration / Finance / Taxation
- **Website:** https://www.impots.gouv.sn
- **Status:** Claim - Unverified
- **Victim Description:** The **DGID** is the central agency of Senegal's Ministry of Finance and Budget, responsible for tax collection, national domain management, and the land registry (cadastre). The ransomware group claims to have leaked 1 terabyte (1 TB) of sensitive data, including structured tax databases, land registries and taxpayer banking information; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 30 September 2025
#### 🇪🇬 Egypt - Telecom Egypt (TE Data)
- **Incident type:** Data Leak
- **Actor / Group:** KILLUAX
- **Sector:** Telecommunications
- **Website:** te.eg
- **Status:** Claim - Data Sample Published
- **Victim Description:** Telecom Egypt operates the TE Data broadband/ISP service. The reviewed sample contains RADIUS-style session accounting records (subscriber usernames in tedata.net.eg format, NAS IP addresses, MAC addresses, assigned IP addresses, session start/stop times and connection type). Only a small number of records (36) were available for review, which limits assessment of the total scope; the exposure could nonetheless support subscriber identification and network reconnaissance.

## ✍🏿 Auteur
*Adama ASSIONGBON*  
*Consultant SOC & Cyber Threat Intelligence*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)
