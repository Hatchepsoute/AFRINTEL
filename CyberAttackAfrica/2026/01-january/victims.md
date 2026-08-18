[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in January 2026 (21 victims)
👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

January 2026 includes **22 unique incidents**: **17 ransomware incidents**, **3 data leaks**, **1 access sale**, and **1 coordinated defacement** across **12 African countries**.

### Notable incidents

- **Niger:** coordinated defacement of more than seven Nigerien state websites displaying political messages about the country’s geopolitical situation.
- **Senegal:** publication of a financial database attributed to PixPay.
- **Morocco:** publication of an aviation database attributed to AOM Aviation Group.
- **Togo:** claimed sale of access to government infrastructure by Bigbrother.

> The entries below document observed claims or publications. AFRINTEL does not confirm a compromise without independent evidence.

## January 2026

### 03 January 2026
#### 🇹🇬 Togo - Government of Togo (gouv.tg)
- **Actor / Group:** Bigbrother (Initial Access Broker)
- **Sector:** Central Public Administration
- **Website:** gouv.tg
- **Status:** Claim - Unverified
- **Incident type:** Access Sale
- **Victim Description:** Infrastructure of the Togolese government. The actor claims new access to several official platforms.

### 04 January 2026
#### 🇳🇪 Niger - Government Websites (Massive Defacement)
- **Actor / Group:** Unclaimed
- **Sector:** Public Administration
- **Websites:** erp.ansi.ne, startups.ansi.ne, stagiaires.ansi.ne, magel.gouv.ne, urbanisme.gouv.ne, promotionfemme.gouv.ne, industrie.gouv.ne
- **Incident type:** Defacement
- **Status:** Under Investigation
- **Victim Description:** Multiple official websites of the Nigerien state were defaced in a coordinated operation. The pages displayed political messages concerning Niger’s geopolitical situation at the time of the incident.

### 06 January 2026
#### 🇿🇦 South Africa - Hytec South Africa
- **Ransomware Group:** vect
- **Sector:** Hydraulic & Mechanical Engineering
- **Website:** hytec.com
- **Status:** Claim - Unverified
- **Victim Description:** South African company specialized in hydraulic and mechanical engineering.

### 08 January 2026
#### 🇰🇪 Kenya - National Water Authority
- **Ransomware Group:** blackshrantac
- **Sector:** Public Services (Water Management)
- **Website:** nwa.go.ke
- **Status:** Claim - Unverified
- **Victim Description:** Kenyan public authority responsible for water resources management.

### 11 January 2026
#### 🇪🇬 Egypt - Real Tech
- **Ransomware Group:** TheGentlemen
- **Sector:** Technology / IT Security
- **Website:** realtech-eg.com
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian firm operating in the technology and IT security sector.

### 13 January 2026
#### 🇪🇬 Egypt - Tepco-Group
- **Ransomware Group:** direwolf
- **Sector:** Electrical Engineering
- **Website:** tepco-group.com
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian group specialized in electrical engineering.

### 14 January 2026
#### 🇲🇺 Mauritius - Rogers Capital
- **Ransomware Group:** TheGentlemen
- **Sector:** Financial Services & Technology
- **Website:** rogerscapital.mu
- **Status:** Claim - Data Sample Published
- **Victim Description:** Financial services and technology provider based in Mauritius.

- **Analysis:**
  AFRINTEL reviewed a corpus of approximately 102 files associated with this claim, including PDF, DOC/DOCX, RTF and spreadsheet documents. The material consists of client onboarding and regulatory compliance documentation typical of a global business licence (GBL) and trust administration practice: FATCA and CRS classification reports, certificates of incorporation, GBL licences, trust deeds, audited financial statements, business plans, fund management documents and structure charts. The corpus references several investment funds, trusts and related entities administered or handled by Rogers Capital. It includes corporate, financial, tax-reporting, ownership and beneficiary-related information, as well as professional contact and account-related references. The files primarily concern fund and trust structures rather than individual retail clients, but their disclosure would expose confidential corporate and regulatory information for multiple entities, creating risks of targeted phishing, business email compromise, identity impersonation, payment fraud and reputational pressure on affected fund managers and counterparties. AFRINTEL did not identify a confirmed plaintext password dump, encryption evidence or a technical intrusion vector in the reviewed material; the initial access method remains unknown. The presence of the documents supports the classification as a published data sample, but does not independently confirm the underlying intrusion.

### 16 January 2026
#### 🇸🇳 Senegal - PixPay
- **Actor / Group:** breach3d
- **Sector:** FinTech (Mobile Payment)
- **Website:** pay.pixpay.sn
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim Description:** Senegalese mobile payment platform.

- **Analysis:**
  AFRINTEL reviewed the forum post and the accompanying sample. The actor breach3d states that the published material covers payment APIs and related data, and lists JWT tokens, API keys, access tokens and database access credentials among the contents. The accessible sample corresponds to a production environment configuration file containing service endpoints, database connection parameters and secret keys for the pay.pixpay.sn platform, rather than a customer records database. If genuine, exposure of this type of material would allow an attacker to interact directly with PixPay's payment backend, with a risk of unauthorized API calls, token or session forgery, and further lateral compromise of connected systems. AFRINTEL cannot confirm whether the credentials were still valid at collection time or have since been rotated.

### 16 January 2026
#### 🇲🇿 Mozambique - CFM Mozambique (Portos e Caminhos de Ferro de Moçambique)
- **Ransomware Group:** qilin
- **Sector:** Transport & Logistics (Rail & Ports)
- **Website:** cfm.co.mz
- **Status:** Claim - Unverified
- **Victim Description:** Mozambique's national railway and port authority.

### 17 January 2026
#### 🇹🇿 Tanzania - CCBRT (Comprehensive Community Based Rehabilitation in Tanzania)
- **Ransomware Group:** benzona
- **Sector:** Healthcare / Specialized Care
- **Website:** ccbrt.org
- **Status:** Claim - Unverified
- **Victim Description:** Tanzanian healthcare NGO providing specialized rehabilitation services.

### 17 January 2026
#### 🇲🇦 Morocco - Nafae Sanitaire
- **Ransomware Group:** tengu
- **Sector:** Construction (Plumbing & Heating)
- **Website:** nafaesanitaire.com
- **Status:** Claim - Data Sample Published
- **Victim Description:** Moroccan company operating in the construction and sanitary sector.

- **Analysis:**
  AFRINTEL reviewed the tengu leak site listing for this victim, marked as Encrypted. The group describes a claimed 18.2 GB volume structured into eight categories: daily cash journals covering 2022 to 2026, customer financial positions (debts and receivables), a company bank account number (RIB), Sage 100 accounting and business databases, HR records including staff absence tracking, employment contracts and commercial agreements, supplier and client contact data, and full backups of the accounting systems. This level of detail is consistent with direct access to the company's accounting environment. AFRINTEL did not access the underlying files and cannot independently confirm their integrity, completeness or the exact initial access vector.

### 20 January 2026
#### 🇰🇪 Kenya - CPF Financial Services
- **Ransomware Group:** TheGentlemen
- **Sector:** Financial Services (Pension Funds)
- **Website:** cpf.or.ke
- **Status:** Claim - Unverified
- **Victim Description:** Financial services provider in Kenya focused on pension fund management.

### 20 January 2026
#### 🇰🇪 Kenya - NSSF (National Social Security Fund)
- **Ransomware Group:** devman
- **Sector:** Social Security (Retirement)
- **Website:** nssf.or.ke
- **Status:** Claim - Unverified
- **Victim Description:** Kenya's national social security and retirement fund.

### 20 January 2026
#### 🇿🇦 South Africa - Paltrack
- **Ransomware Group:** TheGentlemen
- **Sector:** Logistics Software (Agri-food)
- **Website:** paltrack.co.za
- **Status:** Claim - Unverified
- **Victim Description:** Provider of logistical software solutions for the agri-food industry in South Africa.

### 20 January 2026
#### 🇿🇦 South Africa - Rola Motor Group
- **Ransomware Group:** TheGentlemen
- **Sector:** Automotive Distribution
- **Website:** rola.co.za
- **Status:** Claim - Unverified
- **Victim Description:** South African automotive dealership and distribution group.

### 20 January 2026
#### 🇿🇦 South Africa - Witzenberg Municipality
- **Ransomware Group:** TheGentlemen
- **Sector:** Public Administration / Local Government
- **Website:** witzenberg.gov.za
- **Status:** Claim - Unverified
- **Victim Description:** Local government authority in the Western Cape, South Africa.

### 26 January 2026
#### 🇰🇪 Kenya - namico.go.ke (National Mining Corporation)
- **Ransomware Group:** tengu
- **Sector:** Mining and Mineral Resources
- **Website:** namico.go.ke
- **Status:** Claim - Data Sample Published
- **Victim Description:** Kenya's state-owned mining enterprise.

- **Analysis:**
  AFRINTEL reviewed the tengu leak site listing for NAMICO, marked as Encrypted. The group lists a claimed 15 GB volume and displays a file tree including DB, ERP and PORTALS directories, several versions of a compressed staff portal application (CO.STAFFPORTAL), a full database backup file (approximately 4.8 GB) and SQL Server database files exceeding 7 GB. This is consistent with access to NAMICO's internal ERP, staff portal and database infrastructure rather than a single document set. AFRINTEL did not access the underlying database content and cannot confirm what categories of records it contains or the initial access vector.

### 27 January 2026
#### 🇹🇳 Tunisia - FRUIT-BONTÉ
- **Ransomware Group:** tengu
- **Sector:** Food Industry
- **Website:** fruit-bonte.com.tn
- **Status:** Claim - Unverified
- **Victim Description:** Tunisian company operating in the agri-food and fruit processing industry.

### 27 January 2026
#### 🇪🇬 Egypt - skyegtours.com
- **Ransomware Group:** tengu
- **Sector:** Tourism / Travel & Transport
- **Website:** skyegtours.com
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian travel and tourism agency.

### 28 January 2026
#### 🇩🇿 Algeria - Tahkout Group
- **Ransomware Group:** tengu
- **Sector:** Automotive Industry & Transport
- **Status:** Claim - Data Sample Published
- **Victim Description:** Major Algerian industrial conglomerate involved in automotive assembly and transport.

- **Analysis:**
  AFRINTEL reviewed the tengu leak site listing for Tahkout Group, marked as Encrypted, with a claimed volume of 83 GB. In addition to the leak site page, AFRINTEL reviewed the group's published proof images, apparently taken from a compromised Windows Server host: a Server Manager console showing Active Directory Domain Services, DHCP and DNS roles configured (consistent with a domain controller), a network share named "Shares" containing folders labelled COMMERCIAL, DLG PAIE, PATRIMOINE, Pointage, POINTAGE FACIAL, Ressources Humaines, RH and Suivi Contrats, and a full-screen ransom notice reading "YOUR SYSTEM HAS BEEN BLOCKED BY TENGU RANSOMWARE". These elements indicate that the group obtained privileged access to core identity infrastructure and to payroll, HR, biometric attendance and contract-related file shares, and that ransomware was executed on at least one host. AFRINTEL did not access the leaked files themselves and cannot confirm the exfiltrated data volume, the full operational impact or the initial access vector.

### 31 January 2026
#### 🇲🇦 Morocco - AOM Aviation Group (Air Ocean Maroc)
- **Actor / Group:** skra1a
- **Sector:** Air Transport / Civil Aviation
- **Website:** airoceangroup.ma
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim Description:** Moroccan group providing air transport and civil aviation services.
