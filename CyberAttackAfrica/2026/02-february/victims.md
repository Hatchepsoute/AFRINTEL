[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in February 2026 (27 records)
👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

February 2026 includes **27 documented records**: **20 Ransomware**, **7 Data Leak**, **0 Access Sale**, **0 DDoS**, **0 Defacement** and **0 Operational Fraud**, involving **14 African countries**. These are documented reports, not necessarily independently confirmed intrusions.

### February 01, 2026

#### 🇸🇴 Somalia - BlueSky Aviation
- **Initial publication date:** February 01, 2026


- **Ransomware Group:** 0APT
- **Sector:** Aviation
- **Website:** bluesky-air.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Somali aviation company providing air transport services.

#### 🇪🇬 Egypt - Egyptian Medical Laboratories (multi-organisation claim)
- **Initial publication date:** February 01, 2026



- **Actor / Group:** CrowStealer
- **Sector:** Healthcare / Medical Laboratories
- **Website:** results.u-carelabs.com; marzouk-labs.com; hassablabsresults.com; mabaralabs-results.com
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:**

  The publication advertises patient-result data allegedly associated with four Egyptian medical-laboratory platforms.

- **Analysis:**

  The post claims 5,529 records in a CSV file named `egy_labs.csv`, covering December 2025 to January 2026. The displayed schema includes laboratory name, patient name, mobile number, accession number, visit date, test type and result-drive reference. The sample shows structured medical-laboratory records, but the authenticity, completeness, exact ownership and independent relationship between the four domains are not confirmed. AFRINTEL records this as one multi-organisation data-leak claim and does not reproduce patient names, contact details or individual file links.

### February 02, 2026

#### 🇪🇬 Egypt - Canadian International College (CIC)
- **Initial publication date:** February 02, 2026


- **Actor / Group:** CrowStealer
- **Sector:** Education / Higher education
- **Website:** [cic-cairo.edu.eg](https://www.cic-cairo.edu.eg/)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim Description:** First Canadian education provider in Egypt, affiliated with Cape Breton University (CBU). The leak (studentsdata.csv) contains 2,925 records: names, majors, levels, GPAs and years.

#### 🇳🇬 Nigeria / 🇨🇮 Côte d’Ivoire - Citizen ID Photo Dataset
- **Initial publication date:** February 02, 2026



- **Actor / Group:** azrekx
- **Sector:** Government / Public administration / Identity documents
- **Website:** Not specified
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  A forum post claims access to 10,669 current Nigerian and Ivorian citizen ID photos, including front-and-back images, with 1,500 images allegedly shared and an additional dataset offered for sale.

- **Analysis:**

  The publication is recorded as one multi-country data-leak claim affecting Nigeria and Côte d’Ivoire. The supplied evidence shows the actor’s statement but does not independently verify the dataset, the claimed volumes, the countries represented in the full collection, or the alleged sharing of 1,500 images. AFRINTEL does not collect or reproduce identity photos or personal data from the listing.

#### 🇪🇬 Egypt - Heliopolis University
- **Initial publication date:** February 02, 2026



- **Actor / Group:** CrowStealer, post published on a cybercriminal forum
- **Sector:** Education / Higher Education
- **Website:** Not specified
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3

- **Description:**

  Heliopolis University is a private Egyptian university established near Cairo, with programmes in engineering, pharmacy, business and economics, physical therapy and organic agriculture.

- **Analysis:**

  A forum publication by CrowStealer dated 02 February 2026 advertises a database associated with Heliopolis University containing 19,790 records. The local workbook supplied for analysis contains 62 structured account records, including 38 Parent accounts and 24 Student accounts; the complete advertised volume was not independently verified from the available file.

  The reviewed schema includes usernames, names, email addresses where present, telephone fields, institution type, last-IP fields, account creation timestamps and suspension status. All 62 records contain a stored password value classified in the workbook as either a 32-character hexadecimal hash or bcrypt (`$2y$`); AFRINTEL did not attempt to crack, reproduce or publish any password value. Only 24 email addresses and 8 last-IP values are populated in the reviewed file.

  The combination of student/parent account data, contact details and password hashes could facilitate phishing, credential stuffing and account takeover if passwords were reused elsewhere. The exact acquisition method, completeness of the 19,790-record claim and independent confirmation by the university remain unknown.

#### 🇪🇬 Egypt - HIMS University
- **Initial publication date:** February 02, 2026



- **Actor / Group:** leakdealer, post published on a cybercriminal forum
- **Sector:** Education / Higher Education
- **Website:** [hims.edu.eg](https://hims.edu.eg)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4

- **Description:**

  HIMS University is presented in the source as an Egyptian higher-education institution. The domain `hims.edu.eg` is observed in the supplied sample, but the institution's official identity and the completeness of the advertised archive were not independently verified.

- **Analysis:**

  A forum post dated 02 February 2026 advertises a database allegedly associated with HIMS University, with a claimed total of 28,124 records and student/staff personal data, financial records and payment-gateway information. The publication lists CSV files covering student accounts, payment records, privilege mappings, balances, bank-related transaction logs, staff details and system metadata. The actor also claims exposure of plaintext credentials and payment-gateway API material; these claims were not independently verified from the visible material supplied.

  The file counts displayed in the source add up to 28,004 records, which is 120 fewer than the advertised total of 28,124. This discrepancy, together with the absence of a reviewed archive, prevents confirmation of the complete volume and scope. If genuine, the combination of student and staff PII, account credentials, financial information and payment-system material could create significant risks of phishing, account takeover, payment fraud and further unauthorized access. AFRINTEL does not reproduce any personal data, credential, API key, national identifier or financial record from the sample.

### February 05, 2026

#### 🇸🇳 Senegal - DAF SENEGAL (Direction de l'Administration Générale et de l'Équipement)
- **Initial publication date:** February 05, 2026


- **Ransomware Group:** The Green Blood Group
- **Sector:** Government
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Senegalese government administration. Major data breach involving citizen databases and biometric records.

#### 🇬🇭 Ghana - Global Media Alliance
- **Initial publication date:** February 05, 2026


- **Ransomware Group:** 0APT
- **Sector:** Media
- **Website:** gmaworld.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Integrated media and communications company based in Ghana.

### February 06, 2026

#### 🇹🇿 Tanzania - Vertex Law Chambers
- **Initial publication date:** February 06, 2026


- **Ransomware Group:** 0APT
- **Sector:** Legal
- **Website:** vertexlaw.co.tz
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Law firm providing legal services in Tanzania.

#### 🇰🇪 Kenya - Wells Fargo
- **Initial publication date:** February 06, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Banking
- **Website:** fargo.co.ke
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Security and logistics provider, also involved in banking/financial services in Kenya.

### February 08, 2026

#### 🇲🇦 Morocco - Al Akhawayn University (AUI) [Data Leak]
- **Initial publication date:** February 08, 2026



- **Threat Actor / Group :** anisanas2
- **Sector :** Education / University
- **Website :** [Al Akhawayn University (AUI)](https://aui.ma/)
- **Status :** Claim - Unverified
- **Incident type:** Data Leak

- **Description :** A cybercriminal forum post claims the leak of a database allegedly linked to Al Akhawayn University (AUI), a Moroccan university located in Ifrane and considered one of the country’s leading academic institutions.

- **CTI Analysis :**
  The threat actor claims that a previously reported AUI breach was “fabricated” and presents this new dataset as “verified and authentic”.

  The observed elements suggest a potential compromise involving academic or administrative systems related to:
  - students,
  - user accounts,
  - administrative databases,
  - or internal university platforms.

  Such leaks may expose:
  - student personal data,
  - institutional email addresses,
  - academic information,
  - internal access data,
  - or reusable credentials across other systems.

- **CTI Note :**
  The full authenticity of the dataset has not been independently verified at this stage. However, the targeted institution is considered strategically important within Morocco’s academic ecosystem, increasing risks related to spear phishing, university account compromise, and BEC-style attacks targeting students, faculty members, or administrative staff.
---

### February 09, 2026

#### 🇳🇬 Nigeria - Getly
- **Initial publication date:** February 09, 2026


- **Ransomware Group:** killsec
- **Sector:** Fintech
- **Website:** getly.app
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim Description:** Nigerian financial technology application.

- **Analysis:**
  AFRINTEL reviewed a set of sample documents associated with this claim. The accessible material consists of Nigerian National Identification Number (NIN) slips and digital NIN cards for multiple individuals, including full names, NIN numbers, dates of birth, photographs and, in some cases, residential addresses. This is consistent with Know Your Customer (KYC) identity verification data collected by a fintech application during customer onboarding. Exposure of this type of document creates a significant risk of identity theft, account takeover and fraudulent use of national identification numbers. AFRINTEL did not access the platform's backend systems and cannot confirm the total volume of records affected or the initial access vector.

### February 11, 2026

#### 🇬🇭 Ghana - Ghana Bauxite
- **Initial publication date:** February 11, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Public Service
- **Website:** ghanabauxite.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Ghanaian enterprise involved in the bauxite mining and production sector.

### February 12, 2026

#### 🇳🇬 Nigeria - Midwestern Oil & Gas
- **Initial publication date:** February 12, 2026


- **Ransomware Group:** incransom
- **Sector:** Energy
- **Website:** midwesternog.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim Description:** Nigerian upstream oil and gas company.

- **Analysis:**
  AFRINTEL reviewed the incransom leak site listing for Midwestern Oil & Gas, which states a company revenue of approximately USD 27.6 million. The listing displays a large set of sample document previews spanning multiple categories: internal financial and audit reports, community affairs and stakeholder engagement reports, HSE and pipeline maintenance records, technical and engineering documentation, procurement and inventory materials, and photographs of personnel and field operations. The breadth of categories suggests broad access to the company's shared file infrastructure rather than to a single system. AFRINTEL did not access the full files and cannot confirm the exact data volume, exfiltration scope or initial access vector.

### February 13, 2026

#### 🇪🇬 Egypt - Nile Air
- **Initial publication date:** February 13, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Airlines
- **Website:** nileair.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Private Egyptian airline based at Cairo International Airport.

### February 14, 2026

#### 🇲🇺 Mauritius - Sands Suites
- **Initial publication date:** February 14, 2026


- **Ransomware Group:** LockBit 5.0.0
- **Sector:** Hospitality
- **Website:** sands.mu
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Luxury resort located in Mauritius.

### February 15, 2026

#### 🇿🇦 South Africa - Intsika Yethu Municipality
- **Initial publication date:** February 15, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Local Government
- **Website:** intsikayethu.gov.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Local municipality in the Eastern Cape province of South Africa.

#### 🇹🇳 Tunisia - BITS
- **Initial publication date:** February 15, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** IT Consulting
- **Website:** bits.com.tn
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Tunisian IT services and consulting firm.

### February 17, 2026

#### 🇪🇬 Egypt - sodic.com
- **Initial publication date:** February 17, 2026


- **Ransomware Group:** payload
- **Sector:** Real Estate
- **Website:** sodic.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** One of Egypt's leading real estate development companies.

### February 18, 2026

#### 🇸🇩 Sudan - Amtaar Investment
- **Initial publication date:** February 18, 2026


- **Ransomware Group:** apt73/bashe
- **Sector:** Agriculture / Agribusiness
- **Website:** amtaar.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim Description:** A major agricultural investment and consulting firm operating in Sudan, managing 6,000 hectares of irrigated land and serving as a key player in national food security..

### February 19, 2026

#### 🇨🇮 Ivory Coast - aircotedivoire.com
- **Initial publication date:** February 19, 2026


- **Ransomware Group:** incransom
- **Sector:** Airlines
- **Website:** aircotedivoire.com
- **Status:** Data Fully Published
- **Incident type:** Ransomware
- **Victim Description:** National airline of Ivory Coast.

- **Analysis:**
  AFRINTEL reviewed the incransom (INC Ransom) leak site entry for this victim, listed under the group's Disclosures section. The listing states an estimated annual revenue of USD 40.5 million, approximately 1,000 employees and a headquarters in Abidjan, and confirms a data disclosure of approximately 208 GB (208,351,284,086 bytes) following a ransomware attack against the airline. AFRINTEL also reviewed a data sample distinct from the leak site listing: a PDF document generated by Microsoft Access, titled "État d'opération", corresponding to a payroll bank transfer order dated 21 June 2022 and covering 529 Air Côte d'Ivoire employees, for a cumulative total amount of 676,139,136 (currency not specified in the document, consistent with FCFA). Each line lists a full name, an internal staff number, the beneficiary bank and a complete bank account identifier (RIB), along with the individual transfer amount. The source file name referenced in the document ("E:\VIREMENTS SALAIRES JUIN 2022.txt") is consistent with an export from the airline's payroll management or bulk transfer environment. AFRINTEL does not reproduce any individual name, staff number or bank account detail from this sample. This element, dated 2022, confirms exposure of internal financial and HR data distinct from the leak site listing alone, but it does not establish whether the full claimed volume (208 GB) consists of the same type of content, nor does it confirm the initial access vector.

### February 20, 2026

#### 🇲🇦 Morocco - Shora Advisory
- **Initial publication date:** February 20, 2026


- **Ransomware Group:** tengu
- **Sector:** Accounting
- **Website:** shora.ma
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim Description:** Moroccan accounting and financial advisory firm.

- **Analysis:**
  AFRINTEL reviewed the tengu leak site listing and accompanying sample documents for this victim. The material includes an internal folder structure covering client accounting files organized by fiscal year (folders labelled "ARRETE DES COMPTES" for 2018 to 2020) and grouped by client type (associations, public establishments, individuals and companies), alongside marketing, HR and administrative folders, for a combined archive described as approximately 23.5 GB across roughly 16,000 files and 2,000 folders. Individual sample documents include a CNSS social security payment slip issued to Shora Auditing SARL and internal client correspondence. Because Shora operates as an accounting and audit firm, this exposure risks affecting the confidentiality of financial records belonging to numerous third-party client organizations, not only Shora itself. AFRINTEL did not access the full archive and cannot confirm the exact scope of client data involved or the initial access vector.

#### 🇪🇬 Egypt - moa.gov.eg (Ministry of Agriculture)
- **Initial publication date:** February 20, 2026


- **Ransomware Group:** LockBit 5.0.0
- **Sector:** Government
- **Website:** moa.gov.eg
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Egyptian Ministry of Agriculture and Land Reclamation.

### February 22, 2026

#### 🇳🇦 Namibia - CYMOT
- **Initial publication date:** February 22, 2026


- **Ransomware Group:** qilin
- **Sector:** Retail
- **Website:** cymot.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Namibian supplier of spares, tools, and equipment.

### February 23, 2026

#### 🇲🇦 Morocco - Chezpara.ma [Data Leak]
- **Initial publication date:** February 23, 2026


- **Threat Actor / Group :** Richard2002
- **Sector :** Online Pharmacy / Healthcare E‑commerce
- **Website :** [chezpara.ma](https://chezpara.ma/)
- **Status :** Claim - Unverified
- **Incident type:** Data Leak
- **Description :** ~400,000 customer records including names, phone numbers, detailed addresses, delivery info, and order comments.
---

### February 24, 2026

#### 🇿🇦 South Africa - EnerTec
- **Initial publication date:** February 24, 2026


- **Ransomware Group:** vect
- **Sector:** Energy
- **Website:** enertec.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** South African energy solutions and battery distribution company.

### February 27, 2026

#### 🇿🇦 South Africa - Diesel-Electric
- **Initial publication date:** February 27, 2026


- **Ransomware Group:** LockBit 5.0.0
- **Sector:** Automotive
- **Website:** diesel-electric.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Major distributor in South Africa specialized in automotive components.
