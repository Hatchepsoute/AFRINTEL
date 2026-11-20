[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in January 2026 (30 records)
👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

January 2026 includes **30 unique incidents**: **18 ransomware incidents**, **10 data leaks**, **1 access sale**, and **1 coordinated defacement** across **13 African countries**.

### January 03, 2026

#### 🇹🇬 Togo - Government of Togo (gouv.tg)
- **Initial publication date:** January 03, 2026


- **Actor / Group:** Bigbrother (Initial Access Broker)
- **Sector:** Central Public Administration
- **Website:** gouv.tg
- **Status:** Claim - Unverified
- **Incident type:** Access Sale
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Infrastructure of the Togolese government. The actor claims new access to several official platforms.

#### 🇿🇦 South Africa - Constantia Pharmacy
- **Initial publication date:** January 03, 2026



- **Incident date:** January 3, 2026
- **Publication / confirmation date:** January 5, 2026
- **Actor / Group:** `Want_to_cry` ransomware observed; human operator unattributed
- **Sector:** Healthcare / Pharmacy
- **Status:** Corroborated
- **Incident type:** Ransomware
- **Confidence:** High
- **Impact:** Level 2
- **Description:** **Constantia Pharmacy** is a community pharmacy located at **Constantia Village Shopping Centre** in Cape Town, South Africa. It provides prescription dispensing, pharmaceutical advice and clinic/community-care services. Such operations rely on pharmacy information systems and records needed to serve patients ([official website](https://constantiapharmacy.co.za/)).

- **Independent verification as of 18 October 2026:** **Earlier incident corroborated by reporting:** MyBroadband documented a third party’s intervention against file-encrypting malware on a Constantia Pharmacy server in early January 2026. The attack dates to January, not September; AFRINTEL’s September discovery is not a new attack.

- **Additional verification sources:** [Source 1](https://mybroadband.co.za/news/security/623956-hacker-rescues-south-african-pharmacy-from-cyber-attack.html)

- **Sources / Evidence:** [MyBroadband, January 5, 2026](https://mybroadband.co.za/news/security/623956-hacker-rescues-south-african-pharmacy-from-cyber-attack.html)

Constantia Pharmacy is an independent pharmacy in Cape Town. On January 3, a researcher observed via Shodan an exposed Windows server belonging to its environment while ransomware was running. The pharmacy and its ProPharm provider were alerted and intervened. The observation and coordinated response corroborate the incident; exfiltration, encrypted volume and operator identity remain unknown.

### January 04, 2026

#### 🇳🇪 Niger - Government Websites (Massive Defacement)
- **Initial publication date:** January 04, 2026


- **Actor / Group:** Unclaimed
- **Sector:** Public Administration
- **Websites:** erp.ansi.ne, startups.ansi.ne, stagiaires.ansi.ne, magel.gouv.ne, urbanisme.gouv.ne, promotionfemme.gouv.ne, industrie.gouv.ne
- **Incident type:** Defacement
- **Status:** Under Investigation
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Multiple official websites of the Nigerien state were defaced in a coordinated operation. The pages displayed political messages concerning Niger’s geopolitical situation at the time of the incident.

### January 06, 2026

#### 🇿🇦 South Africa - Hytec South Africa
- **Initial publication date:** January 06, 2026


- **Ransomware Group:** vect
- **Sector:** Hydraulic & Mechanical Engineering
- **Website:** hytec.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** South African company specialized in hydraulic and mechanical engineering.

### January 07, 2026

#### 🇬🇭 Ghana - Nerasolgh (nerasolgh.com)
- **Initial publication date:** January 07, 2026



- **Actor / Group:** Solonik, post published on a cybercriminal forum
- **Sector:** Public Utility / Waste Management Services (Government-adjacent)
- **Website:** [nerasolgh.com](https://nerasolgh.com)
- **AFRINTEL status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4

- **Description:**

  Nerasolgh (nerasolgh.com) operates an integrated waste management billing system used to manage customer accounts, collection routes and payments for sanitation/waste-collection services in Ghana, including USSD-based mobile-money bill payment.

- **Analysis:**

  AFRINTEL reviewed a post published on 7 January 2026 by the actor Solonik, titled "NERASOLGH.COM - 26M FULL PII + BANK DATA + GEO + HASHES (SQL DUMP)", and independently obtained and reviewed the underlying database files referenced in the post. The actor claims 26,082,134 total records in SQL format, covering full name, phone number, email address, physical address, GPS coordinates, gender, password hashes and bank details, with a full archive offered for download.

  AFRINTEL's review of three referenced database exports confirms the schema and country markers described by the actor: a 293,232-row customer table (`iwms_new.customers`) containing full name, primary and secondary phone numbers, postal/street address, Ghana Post GPS digital address, GPS coordinates, gender, a bank-details field and bcrypt password hashes; a 2,604-row staff/agent user table (`iwms_new.users`) containing name, email, phone number, role (administrator, waste-collection agent, subscriber), bcrypt password hash, API access token and session token; and a 1,357,156-row USSD mobile-money transaction log recording customer ID, customer name, payment amount, MSISDN, mobile network operator, transaction status and timestamps, consistently tied to Ghanaian (+233) phone numbers. The combined roughly 1.65 million rows reviewed are structurally consistent with the actor's claim but substantially smaller than the 26 million records advertised, indicating the full advertised dump likely includes additional tables not present in the material reviewed.

  The exposure of customer bank details and password hashes alongside administrator API and session tokens creates a risk of account takeover, fraudulent redirection of bill payments, credential-stuffing against reused passwords, and further compromise of the platform's administrative backend if the tokens remain valid. The exact structural and geographic match between the reviewed files and the actor's claim, combined with the scale and sensitivity of the reviewed material, supports a very high confidence assessment of the sample's attribution. It does not validate the advertised 26-million-record volume, the acquisition method or official victim confirmation. AFRINTEL does not reproduce any customer name, phone number, address, password hash, bank detail, transaction record or credential from the reviewed material.

### January 11, 2026

#### 🇪🇬 Egypt - Real Tech
- **Initial publication date:** January 11, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Technology / IT Security
- **Website:** realtech-eg.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Egyptian firm operating in the technology and IT security sector.

### January 12, 2026

#### 🇿🇦 South Africa - Land and Agricultural Development Bank of South Africa (Land Bank)
- **Initial publication date:** January 12, 2026



- **Incident date:** January 12, 2026
- **Detailed public confirmation:** March 9, 2026
- **Actor / Group:** Not publicly attributed
- **Sector:** Government / Public Bank / Finance
- **Status:** Victim Confirmed
- **Incident type:** Ransomware
- **Confidence:** Very High
- **Impact:** Level 4
- **Description:** The **Land and Agricultural Development Bank of South Africa (Land Bank)** is a specialist development-finance institution serving **South African agriculture**. It finances commercial farmers, agribusinesses and new participants in the agricultural value chain to support production and sector development. It is a sector-focused public development bank rather than a general-purpose retail bank ([Land Bank official profile](https://www.landbank.co.za/About-Us/Pages/Our-Business.aspx)).

- **Independent verification as of 18 October 2026:** **Publicly corroborated acknowledgement:** ITWeb reported the Land Bank ransomware incident occurring in January 2026 and the bank’s security improvements. Added to AFRINTEL in September, but not a September attack.

- **Additional verification sources:** [Source 1](https://www.itweb.co.za/article/land-bank-tightens-security-after-ransomware-attack/raYAyMorlOl7J38N)

- **Sources / Evidence:** [ITWeb, March 9, 2026](https://www.itweb.co.za/article/land-bank-tightens-security-after-ransomware-attack/raYAyMorlOl7J38N); [ITWeb, January 16, 2026](https://www.itweb.co.za/article/land-bank-flags-it-systems-disruption/Kjlyr7wBDRZvk6am)

The South African finance minister confirmed a ransomware attack detected on January 12 after unauthorised activity. Some servers and laptops were encrypted and files were exfiltrated; critical ERP, core-banking and CRM systems were reportedly not compromised. The actor, exact volume and dwell time remain unknown.

### January 13, 2026

#### 🇪🇬 Egypt - Tepco-Group
- **Initial publication date:** January 13, 2026


- **Ransomware Group:** direwolf
- **Sector:** Electrical Engineering
- **Website:** tepco-group.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Egyptian group specialized in electrical engineering.

### January 14, 2026

#### 🇲🇺 Mauritius - Rogers Capital
- **Initial publication date:** January 14, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Financial Services & Technology
- **Website:** rogerscapital.mu
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Financial services and technology provider based in Mauritius.

- **Analysis:**
  AFRINTEL reviewed a corpus of approximately 102 files associated with this claim, including PDF, DOC/DOCX, RTF and spreadsheet documents. The material consists of client onboarding and regulatory compliance documentation typical of a global business licence (GBL) and trust administration practice: FATCA and CRS classification reports, certificates of incorporation, GBL licences, trust deeds, audited financial statements, business plans, fund management documents and structure charts. The corpus references several investment funds, trusts and related entities administered or handled by Rogers Capital. It includes corporate, financial, tax-reporting, ownership and beneficiary-related information, as well as professional contact and account-related references. The files primarily concern fund and trust structures rather than individual retail clients, but their disclosure would expose confidential corporate and regulatory information for multiple entities, creating risks of targeted phishing, business email compromise, identity impersonation, payment fraud and reputational pressure on affected fund managers and counterparties. AFRINTEL did not identify a confirmed plaintext password dump, encryption evidence or a technical intrusion vector in the reviewed material; the initial access method remains unknown. The presence of the documents supports the classification as a published data sample, but does not independently confirm the underlying intrusion.

### January 16, 2026

#### 🇸🇳 Senegal - PixPay
- **Initial publication date:** January 16, 2026


- **Actor / Group:** breach3d
- **Sector:** FinTech (Mobile Payment)
- **Website:** pay.pixpay.sn
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Senegalese mobile payment platform.

- **Analysis:**
  AFRINTEL reviewed the forum post and the accompanying sample. The actor breach3d states that the published material covers payment APIs and related data, and lists JWT tokens, API keys, access tokens and database access credentials among the contents. The accessible sample corresponds to a production environment configuration file containing service endpoints, database connection parameters and secret keys for the pay.pixpay.sn platform, rather than a customer records database. If genuine, exposure of this type of material would allow an attacker to interact directly with PixPay's payment backend, with a risk of unauthorized API calls, token or session forgery, and further lateral compromise of connected systems. AFRINTEL cannot confirm whether the credentials were still valid at collection time or have since been rotated.

#### 🇲🇿 Mozambique - CFM Mozambique (Portos e Caminhos de Ferro de Moçambique)
- **Initial publication date:** January 16, 2026


- **Ransomware Group:** qilin
- **Sector:** Transport & Logistics (Rail & Ports)
- **Website:** cfm.co.mz
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Mozambique's national railway and port authority.

#### 🇰🇪 Kenya - Unidentified PAYGO device financing platform (Angaza-based)
- **Initial publication date:** January 16, 2026



- **Incident date:** Not established
- **Actor / Group:** OriginalCrazyOldFart, repost on a cybercriminal forum of an exposed cloud storage bucket
- **Sector:** Financial Services / Consumer Device Financing (PAYGO) / Retail
- **Website:** Not identified with sufficient confidence
- **AFRINTEL status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4

- **Description:**

  The reviewed material describes Kenyan operations of an unidentified pay-as-you-go (PAYGO) consumer device financing platform built on the Angaza SaaS system, used to sell branded smartphones (Tecno Spark and Tecno Pop models observed) on installment plans through local field agents. The same archive reportedly contains data for parallel operations in at least a dozen additional markets across Africa and Asia.

- **Analysis:**

  The reviewed source is a post published on 16 January 2026 by the forum member OriginalCrazyOldFart (long-standing, high-reputation account), titled "Kenya & other countries Phones.7z FREE (has their names & cities too)". The post does not describe a claimed intrusion; it points to a publicly exposed cloud storage bucket indexed by the bucket-scanning service grayhatwarfare.com, and mirrors a 1.28 GB archive on a third-party file host. The poster states the material was not obtained through a breach they claim credit for, and warns that some of the links may already be broken, with no re-upload offered if that occurs.

  The described file alone contains 27,526 rows with a consistent Angaza-platform export schema: customer full name, phone number, city/region, financed product, daily installment price, cumulative amount paid, outstanding balance, account status, registration date, and the name and phone number of the assigned collection agent. A second file referenced in the same post, covering multiple countries beyond Kenya (including Uganda, Nigeria, Tanzania, Togo, Malawi, Zambia, Benin and Myanmar), follows a shorter schema of customer name, phone number and a numeric account/device identifier. The available material does not establish whether all listed countries belong to a single multinational operator or to several distinct organizations sharing the same Angaza-based infrastructure, nor does it identify the specific commercial brand operating the Kenyan portion of the dataset.

  The scale, structural consistency and plausibility of the sample rows support a high confidence assessment that genuine customer and financing records are exposed, independent of the unresolved question of the exact corporate identity. Given the volume, the combination of financial standing (amounts owed, payment history), personal contact details and named collection-agent assignments creates a significant risk of debt-collection-style fraud, impersonation of agents, phishing and harassment targeting financing customers across the affected countries. No customer name, phone number, account identifier, address or financial figure from the reviewed material is reproduced.

#### 🇪🇬 Egypt - BazookaEgy (bazookaegy.com)
- **Initial publication date:** January 16, 2026



- **Chronological qualification:** Publication treated as a new leak and reported in real time in January 2026; the September 2024 publication was identified only later during a retrospective review
- **Earlier publication observed:** September 19, 2024, by MrMeeseeks; its relationship to the January 2026 publication is not established
- **Actor / Group:** MrMeeseeks (original leak); reposted by Sphere on a cybercriminal forum (RaidForums)
- **Sector:** Fast Food / Retail
- **Website:** [bazookaegy.com](https://www.bazookaegy.com)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4

- **Description:**

  Bazooka is an Egyptian fast-food chain, also present in Kuwait, the UAE, Qatar and Bahrain, with an online ordering and registration site.

- **Analysis:**

  The account Sphere reposted, on January 16, 2026, for the second time according to the post title ("[REPOST][REPOST]"), a leak originally attributed to the actor MrMeeseeks and titled "Egypt 1M Costumer information's bazookaegy.com". The sample shown in the post includes a field schema covering the registration channel (mobile_ios, mobile_android, IOS, web_site), an ID, first name, last name, email address and mobile number.

  About thirty complete records are directly visible in the sample, with names (in Latin and Arabic characters), email addresses (including several Apple private-relay addresses) and Egyptian phone numbers. The consistency of the schema with an online ordering platform and the presence of numerous individual records support a high confidence level regarding the authenticity of this leak, although the total claimed volume of one million customers stated in the title could not be independently verified beyond the observed sample. Exposure of this data could facilitate targeted phishing and commercial spam against the chain's customers. AFRINTEL does not reproduce any name, email address or phone number from the reviewed sample.

  **Relationship to the September 2024 publication.** Observed elements: the September 2024 publication attributed to MrMeeseeks claimed more than one million records, more than 752,000 unique emails, names and phone numbers; the January 2026 publication, treated as a new leak when it was disseminated and marked "[REPOST][REPOST]", presents a schema consistent with an ordering platform and a visible sample. Unestablished hypotheses: (1) republication of the same dataset; (2) a second leak from the same system after a new vulnerability or renewed access; (3) incremental extraction or addition of new records; (4) reuse or resale of the corpus by a third party; (5) partial copying with changed metadata or title; (6) data originating from a service provider, ordering platform or separate environment; (7) a fabricated, exaggerated or misattributed sample; (8) negotiation, sharing or transfer between actors. Unknowns: no hash, complete file, overlap comparison, technical timeline, initial-access evidence, transaction, payment or BazookaEgy confirmation is available to distinguish these scenarios. AFRINTEL therefore keeps the 2024 and 2026 publications as separate documentary events without concluding that they represent two independent compromises.

#### 🇩🇿 Algeria - Algiers Regional Football League (LRFA) / Foot’Up [Data Leak]
- **Initial publication date:** January 16, 2026



- **Threat Actor / Group :** dark07x
- **Sector :** Sports / Sports Federation
- **Website :** [lrfa.org.dz](https://lrfa.org.dz)
- **Affected Platform :** Foot’Up
- **Status :** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description :** A cybercriminal forum post claims the compromise of the official management platform of the Algiers Regional Football League (LRFA). The actor claims to have extracted data related to several Algerian football clubs and regional football administrative infrastructures.

- **Clubs Mentioned in the Artifacts :**
  - Omar Ansar Club
  - Wifaq Sour Ghozlane
  - Chabab Amel Kouba

- **Observed Exposed Data :**
  - national identity cards,
  - sports licenses and records,
  - player information,
  - coach and management data,
  - match sheets,
  - administrative documents,
  - internal forms,
  - official signatures and stamps,
  - Foot’Up administrative interfaces,
  - scanned personal documents.

- **CTI Analysis :**
  The published elements suggest access to a centralized sports management platform containing sensitive administrative and personal information related to multiple Algerian football clubs.

  The screenshots also reveal:
  - access to the Foot’Up administration portal,
  - directories containing numerous scanned documents,
  - and files potentially linked to players, managers, and regional sports organizations.

  The exposed information could facilitate:
  - identity theft,
  - document fraud,
  - targeted spear phishing,
  - compromise of sports ecosystems,
  - or abuse of internal administrative information.

- **CTI Note :**
  The threat actor claims to possess broad access to Algeria’s regional football infrastructure. However, the full scope of the compromise and the authenticity of all claimed accesses cannot be independently verified at this stage.

### January 17, 2026

#### 🇹🇿 Tanzania - CCBRT (Comprehensive Community Based Rehabilitation in Tanzania)
- **Initial publication date:** January 17, 2026


- **Ransomware Group:** benzona
- **Sector:** Healthcare / Specialized Care
- **Website:** ccbrt.org
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Tanzanian healthcare NGO providing specialized rehabilitation services.

#### 🇲🇦 Morocco - Nafae Sanitaire
- **Initial publication date:** January 17, 2026


- **Ransomware Group:** tengu
- **Sector:** Construction (Plumbing & Heating)
- **Website:** nafaesanitaire.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Moroccan company operating in the construction and sanitary sector.

- **Analysis:**
  AFRINTEL reviewed the tengu leak site listing for this victim, marked as Encrypted. The group describes a claimed 18.2 GB volume structured into eight categories: daily cash journals covering 2022 to 2026, customer financial positions (debts and receivables), a company bank account number (RIB), Sage 100 accounting and business databases, HR records including staff absence tracking, employment contracts and commercial agreements, supplier and client contact data, and full backups of the accounting systems. This level of detail is consistent with direct access to the company's accounting environment. AFRINTEL did not access the underlying files and cannot independently confirm their integrity, completeness or the exact initial access vector.

#### 🇹🇳 Tunisia - Exscape App [Data Leak]
- **Initial publication date:** January 17, 2026



- **Threat Actor / Group :** forrest
- **Sector :** Mobile Application / Social Network
- **Status :** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Leak Date :** January 17, 2026

- **Description :** A cybercriminal forum post claims the sale of a database allegedly linked to Exscape App containing approximately 5,000 Tunisian user profiles.

- **Observed Data :**
  - usernames
  - full names
  - email addresses
  - phone numbers
  - birth dates
  - gender
  - user biographies
  - GPS coordinates
  - subscription levels
  - age categories

- **CTI Analysis :**
  The exposed data suggests a leak originating from a mobile/social application backend containing precise geolocation information and potentially minor user profiles (“TEEN15”). Risks include doxxing, digital stalking, targeted phishing, and identity correlation through geolocation analysis.

- **CTI Note :**
  The dataset authenticity cannot currently be independently verified, although the observed structure appears consistent with a mobile application backend database.

### January 19, 2026

#### 🇩🇿 Algeria - Inter Partner Assistance Algeria [Data Leak]
- **Initial publication date:** January 19, 2026



- **Threat Actor / Group :** dark07x
- **Sector :** Insurance / Automotive Assistance / Assistance Services
- **Website :** [ipassistance-dz.com](https://ipassistance-dz.com)
- **Status :** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4

- **Description :** A cybercriminal forum post claims the compromise of the official website of Inter Partner Assistance Algeria, a company specialized in automotive, travel, healthcare, and insurance assistance services.

- **Observed Exposed Documents :**
  - automobile accident reports,
  - Algerian national identity cards,
  - vehicle insurance information,
  - automotive expertise reports,
  - CRMA service orders,
  - personal contact information,
  - official signatures and stamps,
  - vehicle registration numbers,
  - driver and vehicle information,
  - internal administrative documents.

- **CTI Analysis :**
  The exposed documents contain sensitive personal and administrative information that could potentially enable:
  - identity theft,
  - insurance fraud,
  - document forgery,
  - targeted spear phishing,
  - or abuse of vehicle and administrative information.

  Several artifacts also reveal the exposure of official document scans and files related to real automobile accident cases.

- **CTI Note :**
  The published screenshots appear to indicate access to internal portals and customer/partner data. However, the full authenticity of all claimed accesses has not yet been independently verified.

### January 20, 2026

#### 🇰🇪 Kenya - CPF Financial Services
- **Initial publication date:** January 20, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Financial Services (Pension Funds)
- **Website:** cpf.or.ke
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Financial services provider in Kenya focused on pension fund management.

#### 🇰🇪 Kenya - NSSF (National Social Security Fund)
- **Initial publication date:** January 20, 2026


- **Ransomware Group:** devman
- **Sector:** Social Security (Retirement)
- **Website:** nssf.or.ke
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Kenya's national social security and retirement fund.

#### 🇿🇦 South Africa - Paltrack
- **Initial publication date:** January 20, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Logistics Software (Agri-food)
- **Website:** paltrack.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Provider of logistical software solutions for the agri-food industry in South Africa.

#### 🇿🇦 South Africa - Rola Motor Group
- **Initial publication date:** January 20, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Automotive Distribution
- **Website:** rola.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** South African automotive dealership and distribution group.

#### 🇿🇦 South Africa - Witzenberg Municipality
- **Initial publication date:** January 20, 2026


- **Ransomware Group:** TheGentlemen
- **Sector:** Public Administration / Local Government
- **Website:** witzenberg.gov.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Local government authority in the Western Cape, South Africa.

### January 26, 2026

#### 🇰🇪 Kenya - namico.go.ke (National Mining Corporation)
- **Initial publication date:** January 26, 2026


- **Ransomware Group:** tengu
- **Sector:** Mining and Mineral Resources
- **Website:** namico.go.ke
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Victim Description:** Kenya's state-owned mining enterprise.

- **Analysis:**
  AFRINTEL reviewed the tengu leak site listing for NAMICO, marked as Encrypted. The group lists a claimed 15 GB volume and displays a file tree including DB, ERP and PORTALS directories, several versions of a compressed staff portal application (CO.STAFFPORTAL), a full database backup file (approximately 4.8 GB) and SQL Server database files exceeding 7 GB. This is consistent with access to NAMICO's internal ERP, staff portal and database infrastructure rather than a single document set. AFRINTEL did not access the underlying database content and cannot confirm what categories of records it contains or the initial access vector.

#### 🇲🇦 Morocco - Moroccan Public Procurement Portal
- **Initial publication date:** January 26, 2026



- **Actor / Group:** B4baYega, post published on a cybercriminal forum
- **Sector:** Government / Public Administration / Public Procurement
- **Website:** [marchespublics.gov.ma](https://marchespublics.gov.ma)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  The Moroccan Public Procurement Portal is the national exchange platform connecting public buyers and suppliers. It supports the publication and consultation of tenders, purchase orders, procurement results, official records and planned public procurement programmes, and is associated with the Kingdom's General Treasury.

- **Analysis:**

  A cybercriminal-forum post attributed to B4baYega, originally published on 26 January 2026 and re-reviewed by AFRINTEL on 02 July 2026, advertises the alleged compromise of the portal's database and offers the material for USD 300. The actor claims approximately 35,000 records, 25,000 documents and a compressed RAR archive of about 16 GB, with structured data in CSV format and documents including PDF and DOCX files. The provided material shows no database structure, column names or document contents. Although the post refers to text and photographic samples, no usable sample is directly visible; authenticity, origin, age, actual document count and archive completeness therefore remain unverified. Given the portal's role, the claimed material could support identification of public buyers, suppliers, procurement procedures and government commercial relationships, as well as targeted phishing, procurement fraud, supplier impersonation and social engineering. The visible material establishes the existence and stated characteristics of a sales offer, but does not independently demonstrate compromise of the portal or possession of the complete database.

### January 27, 2026

#### 🇹🇳 Tunisia - FRUIT-BONTÉ
- **Initial publication date:** January 27, 2026


- **Ransomware Group:** tengu
- **Sector:** Food Industry
- **Website:** fruit-bonte.com.tn
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Tunisian company operating in the agri-food and fruit processing industry.

#### 🇪🇬 Egypt - skyegtours.com
- **Initial publication date:** January 27, 2026


- **Ransomware Group:** tengu
- **Sector:** Tourism / Travel & Transport
- **Website:** skyegtours.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Egyptian travel and tourism agency.

### January 28, 2026

#### 🇩🇿 Algeria - Tahkout Group
- **Initial publication date:** January 28, 2026


- **Ransomware Group:** tengu
- **Sector:** Automotive Industry & Transport
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Major Algerian industrial conglomerate involved in automotive assembly and transport.

- **Analysis:**
  AFRINTEL reviewed the tengu leak site listing for Tahkout Group, marked as Encrypted, with a claimed volume of 83 GB. In addition to the leak site page, AFRINTEL reviewed the group's published proof images, apparently taken from a compromised Windows Server host: a Server Manager console showing Active Directory Domain Services, DHCP and DNS roles configured (consistent with a domain controller), a network share named "Shares" containing folders labelled COMMERCIAL, DLG PAIE, PATRIMOINE, Pointage, POINTAGE FACIAL, Ressources Humaines, RH and Suivi Contrats, and a full-screen ransom notice reading "YOUR SYSTEM HAS BEEN BLOCKED BY TENGU RANSOMWARE". These elements indicate that the group obtained privileged access to core identity infrastructure and to payroll, HR, biometric attendance and contract-related file shares, and that ransomware was executed on at least one host. AFRINTEL did not access the leaked files themselves and cannot confirm the exfiltrated data volume, the full operational impact or the initial access vector.

### January 29, 2026

#### 🇩🇿 Algeria - Algeria Post [Data Leak]
- **Initial publication date:** January 29, 2026



- **Threat Actor / Group :** BlueEx
- **Sector :** Postal Services / Government / Telecommunications
- **Website :** [poste.dz](https://www.poste.dz/)
- **Leak Date :** January 29, 2026
- **Status :** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4

- **Description :** A cybercriminal forum post claims the sale of more than 500,000 records allegedly linked to Algeria Post. The published samples include personal information associated with Algerian citizens as well as photographs of Algerian national identity cards.

- **Observed Data :**
  - full names
  - email addresses
  - phone numbers
  - photographs of national identity cards
  - associated personal information

- **CTI Analysis :**
  The exposed data suggests a leak involving sensitive personal information potentially linked to Algerian postal or administrative services. The simultaneous exposure of:
  - contact information,
  - identity-related data,
  - and official documents

  significantly increases the risks of:
  - identity theft,
  - administrative fraud,
  - targeted phishing,
  - SIM swapping,
  - or fraudulent account and service creation.

- **CTI Note :**
  The full authenticity of the dataset cannot currently be independently verified. However, the presence of structured samples, coherent personal data, and identity document photographs increases the potential credibility of the claimed leak.

### January 30, 2026

#### 🇲🇦 Morocco - AOM Aviation Group (Air Ocean Maroc)
- **Initial publication date:** January 30, 2026


- **Actor / Group:** skra1a
- **Sector:** Air Transport / Civil Aviation
- **Website:** airoceangroup.ma
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Moroccan group providing air transport and civil aviation services.
- **Analysis:** The published sample contains SQL `INSERT INTO` statements targeting a supplier table. The visible records include supplier identifiers, company names, responsible contacts, business addresses, countries, telephone numbers, email addresses, and creation or update dates. The extract links AOM Aviation Group to an aviation-sector supplier management environment and includes Moroccan organizations as well as international partners. The exposure of professional contact data and internal references creates risks of targeted fraud, phishing, and impersonation of business relationships. The analysis is limited to the visible sample; it does not establish the total volume, the full set of affected tables, the initial access vector, or the complete authenticity of the database.
