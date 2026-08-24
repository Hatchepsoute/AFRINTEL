[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# African victims - May 2025

👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

**26 documented cyber incidents** under AFRINTEL Taxonomy v2: Ransomware 13, Data Leak 9, Defacement 2, Account Takeover 1, System Intrusion 1.

> Public-source links are added to supplementary incidents identified through online research to complete the corpus. They are not retroactively imposed on historical AFRINTEL records, including Dark Web observations.

## May 2025

### 01 May 2025
#### 🇿🇦 South Africa - South African IT firm - iOCO (Subsidiary of EOH)
- **Ransomware Group:** devman
- **Sector:** Technology / Managed Services (MSP) / Cloud
- **Website:** https://www.eoh.co.za / ioco.tech
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** EOH is one of South Africa's largest technology service and consulting providers, offering digital transformation and infrastructure solutions. The Devman group used a generic description ("South African IT firm") on its leak site, a common tactic to maintain pressure during negotiation phases.

### 01 May 2025
#### 🇿🇦 South Africa - DovesIT
- **Ransomware Group:** devman
- **Sector:** Information Technology (IT) / Managed Services (MSP)
- **Website:** https://dovesit.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** DovesIT is a South African Managed Service Provider (MSP). The company offers backup solutions, cloud hosting, network maintenance, and cybersecurity for small and medium-sized enterprises (SMEs) in South Africa.

### 01 May 2025
#### 🇿🇦 South Africa - South African HR company
- **Ransomware Group:** devman
- **Sector:** Business Services / Human Resources
- **Website:** Not identified with sufficient confidence
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** This is a human resources firm or service provider based in South Africa, managing contractual, payroll, and personal data of numerous employees on behalf of third parties (HR outsourcing).

### 05 May 2025
#### 🇪🇬 Egypt - Future Association for Microfinance
- **Ransomware Group:** nightspire
- **Sector:** Finance / Association
- **Website:** https://fam-eg.org
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** Egyptian NGO specializing in providing microcredit to micro-entrepreneurs and rural populations.
- **Analysis:** Material evidence-dated 6-7 May 2025 includes interface views and structured export files. A live, HTTP-only ("Not secure") web administration panel at an IP-based address is used to manage loan/payment invoices; in one view, the "Customer Name" field of at least a dozen consecutive invoice records has been altered to read "NightSpire", a proof-of-access technique demonstrating write access to the production application rather than a passive claim. A paginated loan-servicing list (client names, national-ID-style reference numbers, dates, amounts) spans dozens of pages, and an internal shared-drive folder tree is organized by department (Audit, Financial, HR, IT, Legal, MIS, Operation, Risks and their cross-combinations, plus Backup and Meeting Room folders), consistent with the internal structure of a mid-sized financial institution. The reviewed structured exports (fields including REFERENCE_NUMBER, DUE_AMOUNT, MIN/MAX_AMOUNT, DUE_DATE, EXPIRY_DATE, CUSTOMER_NAME, STATUS, PAID_AMOUNT, BRANCH_CODE, CLIENT_NUMBER and LOAN_NUMBER) comprise several files ranging from roughly 470 to just over 2,000 rows each, covering loan and payment data dated April 2024 and April 2025 across multiple branch codes, indicating recurring or bulk extraction rather than a single limited sample. The combination of demonstrated write access to a live administration panel and multiple large, structurally consistent loan/payment exports supports a very high confidence assessment of a genuine, ongoing compromise of the association's loan-management system. Given the scale of exposed loan and payment records (client names, national identifiers, loan amounts and branch-level data) at a microfinance institution serving individual borrowers, the potential impact includes large-scale identity fraud, loan fraud and targeted social engineering against a financially vulnerable client base. No client name, national identifier, loan or payment amount, branch code or reference number is reproduced.

### 10 May 2025
#### 🇿🇦 South Africa - Pienaar Brothers
- **Ransomware Group:** devman
- **Sector:** Personal Protective Equipment (PPE) / Industry
- **Website:** pienaarbrothers.co.za
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** South African leader in the supply and distribution of Personal Protective Equipment (PPE) and safety solutions for the mining, industrial, and manufacturing sectors.
- **Analysis:** Material dated 9-10 May 2025 is consistent with an active intrusion against Pienaar Bros' infrastructure. A server-side archive utility compresses an approximately 2.75 GB, 3,274-file archive of catalogue and pricing data (including branded PPE-glove pricelists) for upload to a cloud storage service, alongside a separately completed upload of a contracts archive. Command-line evidence shows a compromised backup-related service account being used to browse a Windows domain listing multiple named servers and workstations, and a server backup share containing a ransom-note file dated 10 May 2025. A company delivery/route sheet bearing the letterhead of a regional Pienaar Bros trading entity lists third-party business customer accounts, invoice numbers and delivery addresses. The combination of an exfiltration in progress, domain lateral-movement evidence and a ransom note deployed on internal infrastructure supports a high confidence assessment of a genuine compromise. No exposed service-account credential, business customer name, address, invoice number or other individual record is reproduced.

### 15 May 2025
#### 🇲🇷 Mauritania - Banque Al-Wava Mauritanienne Islamique (BAMIS)
- **Incident type:** Data Leak
- **Actor / Group:** kill9
- **Sector:** Banking / Financial Services
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Victim Description:** BAMIS is a Mauritanian Islamic bank offering Sharia-compliant retail and corporate banking services.
- **Analysis:** AFRINTEL reviewed a DarkForums post published on 15 May 2025 by the actor kill9, titled "Mauritanian Banks Data Leak", claiming a coordinated intrusion into the internal networks of six Mauritanian financial institutions, including BAMIS. The post displays unattributed customer records (name, negative account balance in MRU, partially masked client ID and password) that could not be linked to a specific bank, alongside a table of six partially masked payment card samples (BIN 471360, Platinum tier, expiry dates ranging 2025-2027) explicitly labeled as issued by BAMIS. The actor states the full dataset will be sold 48 hours after posting, with contact via Telegram. The post also includes one additional card sample attributed to a separate institution, Banque El Amana, which is not part of the actor's list of six claimed targets; AFRINTEL cannot explain this discrepancy. The presence of bank-specific card samples supports a medium confidence assessment for BAMIS specifically, while the overall scope, volume and authenticity of the claimed network intrusion remain unverified. AFRINTEL does not reproduce any customer names, account identifiers, passwords or card numbers from the reviewed post.

### 15 May 2025
#### 🇲🇷 Mauritania - Banque Mauritanienne pour le Commerce International
- **Incident type:** Data Leak
- **Actor / Group:** kill9
- **Sector:** Banking / Financial Services
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Victim Description:** Banque Mauritanienne pour le Commerce International is a commercial bank operating in Mauritania, providing retail and corporate banking services.
- **Analysis:** AFRINTEL reviewed the same DarkForums post published on 15 May 2025 by the actor kill9 ("Mauritanian Banks Data Leak"), which names Banque Mauritanienne pour le Commerce International among six Mauritanian financial institutions claimed to be compromised. The post includes a table of six partially masked payment card samples (BIN 488985, Platinum tier, expiry dates ranging 2025-2028) explicitly labeled as issued by this bank, alongside unattributed customer records (name, negative account balance, partially masked client ID and password) that could not be linked to a specific institution. The full dataset is offered for sale 48 hours after posting, via Telegram contact. The presence of bank-specific card samples supports a medium confidence assessment, while the overall scope, volume and authenticity of the claimed intrusion remain unverified. AFRINTEL does not reproduce any customer names, account identifiers, passwords or card numbers from the reviewed post.

### 15 May 2025
#### 🇲🇷 Mauritania - Banque pour le Commerce et l'Industrie (BCI)
- **Incident type:** Data Leak
- **Actor / Group:** kill9
- **Sector:** Banking / Financial Services
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Victim Description:** BCI is a commercial bank operating in Mauritania, serving retail and corporate/industrial clients.
- **Analysis:** AFRINTEL reviewed the same DarkForums post published on 15 May 2025 by the actor kill9 ("Mauritanian Banks Data Leak"), which names BCI among six Mauritanian financial institutions claimed to be compromised. The post includes a table of six partially masked payment card samples (BIN 411697, Platinum tier, expiry dates ranging 2025-2029) explicitly labeled as issued by BCI, alongside unattributed customer records (name, negative account balance, partially masked client ID and password) that could not be linked to a specific institution. The full dataset is offered for sale 48 hours after posting, via Telegram contact. The presence of bank-specific card samples supports a medium confidence assessment, while the overall scope, volume and authenticity of the claimed intrusion remain unverified. AFRINTEL does not reproduce any customer names, account identifiers, passwords or card numbers from the reviewed post.

### 15 May 2025
#### 🇲🇷 Mauritania - Orabank Mauritanie-SA
- **Incident type:** Data Leak
- **Actor / Group:** kill9
- **Sector:** Banking / Financial Services
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Victim Description:** Orabank Mauritanie-SA is the Mauritanian subsidiary of the pan-African Oragroup/Orabank network, offering retail and corporate banking services.
- **Analysis:** AFRINTEL reviewed the same DarkForums post published on 15 May 2025 by the actor kill9 ("Mauritanian Banks Data Leak"), which names Orabank Mauritanie-SA among six Mauritanian financial institutions claimed to be compromised. The post includes a table of six partially masked payment card samples (BIN 455143, Platinum tier, expiry dates ranging 2025-2028) explicitly labeled as issued by Orabank, alongside unattributed customer records (name, negative account balance, partially masked client ID and password) that could not be linked to a specific institution. The full dataset is offered for sale 48 hours after posting, via Telegram contact. The presence of bank-specific card samples supports a medium confidence assessment, while the overall scope, volume and authenticity of the claimed intrusion remain unverified. AFRINTEL does not reproduce any customer names, account identifiers, passwords or card numbers from the reviewed post.

### 15 May 2025
#### 🇲🇷 Mauritania - Banque Islamique de Mauritanie (BIM Bank)
- **Incident type:** Data Leak
- **Actor / Group:** kill9
- **Sector:** Banking / Financial Services
- **Website:** Not specified
- **Status:** Claim - Unverified
- **Victim Description:** BIM Bank is a Mauritanian Islamic bank offering Sharia-compliant banking services.
- **Analysis:** AFRINTEL reviewed the same DarkForums post published on 15 May 2025 by the actor kill9 ("Mauritanian Banks Data Leak"), which names BIM Bank among six Mauritanian financial institutions claimed to be compromised. Unlike four of the other named banks, the post does not include a payment-card sample or other data specifically attributed to BIM Bank; the unattributed customer records shown in the post (name, negative account balance, partially masked client ID and password) could not be linked to this or any specific institution. In the absence of bank-specific evidence, AFRINTEL assesses this claim with low confidence, pending independent verification.

### 15 May 2025
#### 🇲🇷 Mauritania - General Bank of Mauritania (GBM)
- **Incident type:** Data Leak
- **Actor / Group:** kill9
- **Sector:** Banking / Financial Services
- **Website:** Not specified
- **Status:** Claim - Unverified
- **Victim Description:** General Bank of Mauritania (GBM) is a commercial bank operating in Mauritania, providing retail and corporate banking services.
- **Analysis:** AFRINTEL reviewed the same DarkForums post published on 15 May 2025 by the actor kill9 ("Mauritanian Banks Data Leak"), which names General Bank of Mauritania among six Mauritanian financial institutions claimed to be compromised. Unlike four of the other named banks, the post does not include a payment-card sample or other data specifically attributed to GBM; the unattributed customer records shown in the post (name, negative account balance, partially masked client ID and password) could not be linked to this or any specific institution. In the absence of bank-specific evidence, AFRINTEL assesses this claim with low confidence, pending independent verification.

### 16 May 2025
#### 🇿🇦 South Africa - south african airways (SAA)
- **Ransomware Group:** incransom
- **Sector:** Air transport
- **Website:** www.flysaa.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** South African Airways (SAA) is the national airline and the largest in South Africa, operating domestic and international flights.
- **Analysis:** AFRINTEL reviewed a local sample of documents consistent with the claim made by the threat actor incransom, consisting of internal records from SAA Technical, the airline's aircraft maintenance, repair and overhaul (MRO) division. The material includes EASA/SACAA Part-145 regulatory documents (Maintenance Organisation Exposition, capability list, list of certifying and support staff), a Certificate of Authority for a certifying aircraft mechanic bearing a name, photo, employee and approval number and a multi-country licence scope, commercial quotations and financial records (credit authorisation sheets, debtor codes, cost analyses, component reconciliation exports referencing the AMOS maintenance-management system), and a lease agreement between Dube TradePort Corporation and Air Chefs SOC Limited, an SAA subsidiary. The documents reference multiple third-party MRO customers, including Comair, Air Namibia, Yemenia and the state defence-procurement entity Armscor. The presence of internally consistent, multi-year operational, regulatory and financial records naming specific SAA Technical systems and subsidiaries supports a high confidence assessment of a genuine internal compromise. The exposure of certifying-staff identity and licensing data, together with regulatory approval documentation and third-party client and defence-related commercial records, creates a risk of targeted phishing, aviation-safety oversight disruption and client/supply-chain impact extending beyond SAA itself. AFRINTEL does not reproduce any employee name, photograph, licence number or client financial detail from the reviewed sample.

### 17 May 2025
#### 🇿🇦 South Africa - vOffice.co.za
- **Incident date:** 17 May 2025 - date reported by the secondary CTI source
- **Initial publication date:** 17 May 2025
- **Actor / Group:** Unknown
- **Sector:** Technology / IT
- **Website:** voffice.co.za
- **Status:** Reported - Secondary CTI
- **Incident type:** Defacement
- **Confidence level:** Medium
- **Impact level:** Level 2
- **Victim Description:** The source describes voffice.co.za as the official website of a South African technology company.
- **Analysis:** CyHawk Africa reported on 17 May 2025 that the official `voffice.co.za` website had been defaced by an unknown threat actor. The source does not provide technical attribution, an access vector, outage duration or victim confirmation. AFRINTEL therefore records the event as a Defacement reported by a secondary CTI source, with medium confidence and without inferring a broader information-system compromise.
- **Source type:** Public CTI Source
- **Public sources:** [CyHawk Africa - Unknown Threat Actor Defaces South African Tech Site](https://cyhawk-africa.com/defacement/unknown-threat-actor-defaces-south-african-tech-site-voffice-co-za-breach-signals-web-vulnerabilities/)

### 19 May 2025
#### 🇰🇪 Kenya - NSSF (National Social Security Fund) KENYA
- **Ransomware Group:** devman
- **Sector:** Government / Social Services
- **Website:** www.nssf.go.ke
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** National Social Security Fund of Kenya, the statutory body managing mandatory pension and social-security contributions for Kenyan workers. The actor demands $4.5 million USD.
- **Analysis:** Material dated 15-18 May 2025 is consistent with genuine administrative-level access to NSSF's internal Windows environment. The material includes a ransom-note text file opened on a compromised desktop, stating that the "DevMan Cybersecurity Collective" compromised NSSF's systems at 9 PM UTC on 17 May 2025, encrypted critical systems and files, destroyed cloud and network-based backups, and exfiltrated sensitive data including employee personal records, client financial information and pension details; the note references Kenya's Data Protection Act, 2019 and threatens regulatory fines and client lawsuits. Separate material shows Windows Server Manager sessions for at least two domain-joined production servers (a mail/web-facing host and a large-capacity document-management host, both joined to an NSSF domain), dated 15 and 16 May 2025, and a file-explorer view listing drives consistent with an Exchange mail database and virtualization infrastructure, dated 17 May 2025. Additional reviewed material consists of dozens of scanned physical pension-benefit payment forms bearing the NSSF Board of Trustees letterhead, member and employer reference numbers, and payment amounts. The combination of a detailed ransom note matching the actor's typical playbook, evidence of genuine domain-level server access across multiple production systems, and scanned archival pension records supports a very high confidence assessment of a large-scale compromise affecting critical national social-security infrastructure. The full claimed volume of 2.5 TB and the $4.5 million ransom demand are not independently verified beyond what is stated in the actor's own material; no employee or member name, account or reference number, credential, or other individual record is reproduced.

### 19 May 2025
#### Ivory Coast - igp.ci
- **Actor / Group:** Team 1722 (claim)
- **Sector:** Not specified
- **Website:** https://igp.ci/
- **Incident date:** 19 May 2025 - date reported by the secondary CTI source
- **Initial publication date:** 19 May 2025
- **Status:** Claim - Secondary OSINT Evidence
- **Incident type:** Defacement
- **Confidence level:** Medium
- **Impact level:** Level 2
- **Victim Description:** The affected asset is the Ivorian domain igp.ci. The exact organizational scope was not established in the reviewed material.
- **Analysis:** A secondary CTI report states that the igp.ci website was defaced with propaganda content and Telegram references attributed to Team 1722. No official confirmation was identified in the supplied audit. AFRINTEL therefore records the event with medium confidence and keeps Team 1722 as a claim rather than a technical attribution.
- **Source type:** Secondary CTI
- **Public sources:** [CyHawk Africa](https://cyhawk-africa.com/defacement/hacktivist-group-deface-one-website-in-cote-divoire/)

### 20 May 2025
#### 🇧🇼 Botswana - Medswana
- **Ransomware Group:** killsec
- **Sector:** Pharmacy / Healthcare
- **Website:** medswana.co.bw
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence Level:** Medium
- **Impact Level:** Level 3
- **Victim Description:** Medswana (Pty) Ltd is one of Botswana's leading pharmaceutical distributors.
- **Analysis:** The killsec ransomware group claims the compromise of Medswana (medswana.co.bw) and displays data samples on its leak-site page, dated 22 and 23 May 2025. The samples cover three distinct categories of data. Customer/debtor accounts tied to a network of pharmacy branches operating under the "Pharma" brand (Pharma Acacia, Pharma North, Pharma West, Pharma South, Pharma Africa, Pharma Kweneng, among others) across several Botswana towns (Gaborone, Kasane, Maun, Francistown), including name, postal address, landline and mobile phone numbers, and e-mail address. Dependant records tied to medical aid schemes, including name, date of birth, sex, member number, relationship, treating doctor's contact details, and allergy fields. Pharmaceutical stock and dispensing data (product codes, drug descriptions, quantities, purchase and retail prices, prescription numbers), with timestamps spanning several years of activity, from 2021 to 2025. The leak-site page displays a countdown to a disclosure deadline, an unspecified ransom price, and a disclosure counter at 0/1, indicating that no full publication has occurred yet at this stage. The consistency between the retail brands visible in the samples and Medswana's profile as a pharmaceutical distributor supports a medium confidence level. The nature of the observed data, both patient health information and customer contact details, supports a Level 3 impact rating. No patient name, customer name, or raw personal data is reproduced in this entry.

### 20 May 2025
#### 🇩🇿 Algeria - University Setif 1 - Ferhat Abbas (univ-setif.dz)
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Education / Higher education
- **Website:** [univ-setif.dz](https://www.univ-setif.dz)
- **Status:** Claim - Unverified
- **Victim Description:** Setif 1 University - Ferhat Abbas is an Algerian public higher-education institution.
- **Analysis:** The actor Phantom Atlas claims an intrusion into the university's website and announces the upcoming publication of files described as important, for a claimed volume of 3.5 GB. No sample or technical evidence accompanies the post; AFRINTEL did not collect or analyze any underlying data and therefore cannot confirm the compromise.

### 20 May 2025
#### Tanzania - Tanzania Police Force / Tanzania Revenue Authority official social-media accounts
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** Official X and YouTube accounts
- **Incident date:** 19-20 May 2025 - reported window for compromise of the official accounts
- **Initial publication date:** 20 May 2025
- **Status:** Government / Institution Confirmed
- **Incident type:** Account Takeover
- **Subtype:** Compromised official social-media accounts / disinformation
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Source type:** Institutional Confirmation + Public Media
- **Analysis:** The Tanzania Police Force confirmed that its official X account had been hacked and used to spread false information. The Tanzania Revenue Authority's YouTube channel was also reported and publicly acknowledged as compromised. AFRINTEL keeps the scope to the confirmed public accounts and does not infer compromise of central national cyber infrastructure.
- **Sources:** [The Citizen - Police X account compromise](https://www.thecitizen.co.tz/tanzania/news/national/police-launch-hunt-after-official-x-account-hacked-warns-public-against-sharing-fake-news-5049060) | [The Citizen - Police and TRA account compromises](https://www.thecitizen.co.tz/tanzania/news/national/hackers-target-tanzanian-government-institutions-spread-falsehoods-5049088)

### 21 May 2025
#### 🇿🇦 South Africa - Anglo American plc
- **Ransomware Group:** arkana
- **Sector:** Mining
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Website:** angloamerican.com
- **Victim Description:** Anglo American plc is a multinational mining company based in Johannesburg and London. It is the world's largest producer of platinum and diamonds, with operations in over 40 countries. It also mines copper, nickel, iron ore, and coal.

### 23 May 2025
#### 🇿🇦 South Africa - netstar
- **Ransomware Group:** devman
- **Sector:** Technology / Telematics / IoT Security
- **Website:** netstar.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Netstar, a subsidiary of the Altron group, is the pioneer of the stolen vehicle recovery (SVR) industry in South Africa.

### 26 May 2025
#### 🇿🇦 South Africa - Mediclinic Group
- **Ransomware Group:** everest
- **Sector:** Healthcare
- **Website:** https://www.mediclinic.co.za / www.mediclinic.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** Mediclinic International (Mediclinic Group) is one of the three largest private hospital operators in South Africa. The group manages dozens of multidisciplinary hospitals and day clinics across the country (and internationally, notably in the United Arab Emirates and Switzerland via Hirslanden).
- **Analysis:** A local set of material is associated with this claim. The material includes two views of a SAP SuccessFactors "People Profile" self-service HR interface for a profile named Gregory van Wyk, shown with the title Chief Executive Officer, Office of the CEO, Mediclinic Southern Africa Corporate Office (Johannesburg); the associated email address follows an "sftest@mediclinic.com" pattern, consistent with a test/sandbox account rather than confirmed production data, though this does not rule out that it reflects a real user record. The visible modules include Payroll Information (self-service payslip access and Admin Services links for Social Insurance, External Transfers, Loans, Taxes, Employee Remuneration Info, Cost Distribution and Company Car), Compensation Information (a monthly basic-salary figure under the "MEDICLINIC Salaries - Management (M1)" pay group), and employment/organisational metadata referencing the legal entities Mediclinic (Pty) Ltd and Mediclinic Southern Africa (Pty) Ltd, GL account codes and job classification fields. A separate project-folder directory (Requirements, Change Request, LMS Handover, Meetings & Trackers, Configuration, Integrations, Documentation, Migration, and a "Mediclinic JAM Walkthrough" video file) shows folder sizes ranging from under 1 MB up to roughly 1.6 GB for the Migration folder, consistent with a SuccessFactors implementation or project workspace rather than a simple document leak. The consistent Mediclinic branding, legal-entity names and SuccessFactors module structure across the reviewed material support a high-confidence assessment of genuine access to Mediclinic's HR information-system environment, though the scope, production status and total volume of the underlying compromise are not established from this limited sample. No salary figures, phone numbers, employee IDs or other personal data are reproduced.

### 26 May 2025
#### 🇿🇦 South Africa - FrontierCo
- **Ransomware Group:** Datacarry
- **Sector:** Retail / Distribution (Clothing and footwear)
- **Website:** http://frontierco.co.za/
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** FrontierCo is a major player in South African distribution. The company holds exclusive distribution licenses and sales rights for several renowned international brands (clothing, footwear, and accessories) through a wide network of physical stores and e-commerce platforms.
- **Analysis:** AFRINTEL reviewed structured customer-data exports and network-reconnaissance evidence associated with this claim. Six CSV files, matching a Microsoft Dynamics 365 Business Central "Customer" table schema (fields including company/contact name, address, city, phone, mobile phone, email, VAT registration number, credit limit, payment terms and related commercial metadata), together total approximately 120,000 customer records. A separate file consistent with a further database export (roughly 99 MB uncompressed) was also present but not opened by AFRINTEL. A network-reconnaissance log shows an SMB enumeration sweep against 256 internal targets on an internal /24 range, in which a Windows "Administrator" credential (not reproduced) is shown successfully authenticating against more than a dozen servers, including hosts named consistently with a SQL database server, two backup/Veeam servers, an HR-related server, a UAT server and multiple Hyper-V hosts, alongside failed attempts against other hosts. This indicates domain-wide administrative access achieved through credential reuse rather than a single-system compromise. The combination of a large, structurally consistent customer-database export and demonstrated domain-wide lateral movement with a working administrator credential supports a very high confidence assessment of a genuine, extensive compromise of FrontierCo's IT environment. Given the scale of exposed customer records (contact details, VAT numbers, commercial terms) combined with confirmed domain administrator-level access spanning database, backup and HR-related infrastructure, the potential impact includes large-scale business-customer fraud, targeted phishing and further compromise of backup and financial systems. AFRINTEL does not reproduce any customer name, contact detail, VAT number, credential hash or IP-to-hostname mapping from the reviewed material.

### 27 May 2025
#### South Africa - Eastern Platinum Limited (Eastplats)
- **Actor / Group:** Unknown
- **Sector:** Mining
- **Website:** https://www.eastplats.com/
- **Incident date:** 27 May 2025 - detection date confirmed by Eastplats
- **Initial publication date:** 16 June 2025
- **Status:** Victim Confirmed
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** Eastern Platinum Limited owns and operates platinum-group-metal and chrome assets in South Africa.
- **Analysis:** Eastplats announced that it detected a cybersecurity incident on 27 May 2025 affecting internal IT systems. The company confirmed that some files relating to its internal affairs had been disclosed without authorization by third parties on a restricted part of the Internet. Business operations continued. No attacker or initial-access vector was publicly identified. AFRINTEL records the confirmed internal-system compromise and unauthorized file disclosure without inferring ransomware.
- **Source type:** Victim / Regulatory Disclosure
- **Public sources:** [Eastplats - official cybersecurity incident release](https://www.eastplats.com/investors/news-releases/2025/eastern-platinum-limited-announces-cybersecurity-incident/) | [JSE SENS filing](https://senspdf.jse.co.za/documents/SENS_20250617_S506288.pdf)

### 31 May 2025
#### 🇨🇲 Cameroon - ASCOMA Cameroon
- **Ransomware Group:** worldleaks
- **Sector:** Insurance
- **Website:** ascoma.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** ASCOMA Cameroon is the Cameroonian branch of the Ascoma group, the leading independent insurance brokerage network in sub-Saharan Africa.
- **Analysis:** AFRINTEL reviewed a local sample of files consistent with the claim made by the threat actor worldleaks, retrieved from an internal file share (host 192.168.1.20) with folders named "Automobile_Transport" and "Sinistre_Sante" (health claims). The sample includes a network configuration page for an internal HP OfficeJet Pro printer, confirming the internal domain "ascoma.local", an internal IP addressing scheme (192.168.1.0/24) and a weak, unchanged Wi-Fi Direct password, as well as internal scanner/fax routing logs listing document destinations tied to the company's claims and medical departments ("Sinistre IARD", "Sinistre Santé", "Indemnisation IARDT", "Medical", "Production Santé"). The consistency between the internal domain name, the network configuration and the named file-share folders supports a high confidence assessment of genuine internal network access. Given ASCOMA's role as an insurance broker processing health and property/casualty claims, and the confirmed presence of a dedicated health-claims share, this incident presents a risk of exposure of policyholder health and personal data, in addition to internal network reconnaissance value for further compromise. AFRINTEL does not reproduce any internal IP-to-hostname mapping, network credential or claims-department document content from the reviewed material.

### 31 May 2025
#### 🇹🇬 Togo - Netmaster (netmaster.tg)
- **Incident type:** Data Leak
- **Actor / Group:** cache
- **Sector:** Technology / Digital Services (Hosting & Domains)
- **Website:** netmaster.tg
- **Status:** Data Fully Published
- **Victim Description:** Netmaster is a leading digital service provider in Togo. It acts as the registrar for the national .tg domain and provides web hosting, professional email, and SSL certificate solutions to many Togolese companies and institutions.
- **Analysis:** AFRINTEL reviewed the DarkForums listing and the referenced database export, which corresponds to a full WHMCS billing and hosting-management database, including client, billing, invoicing, hosting, domain, support-ticket, administrator and payment-gateway tables. Alongside the database, a companion file lists EPP transfer codes for several hundred `.tg` domains, consistent with Netmaster's role as registrar for Togo's national domain; exposure of these codes creates a risk of unauthorized domain transfers affecting Togolese businesses and institutions relying on Netmaster, in addition to the billing and support data covering Netmaster's own customer base. The reviewed export's structure and scale are consistent with the claim made by the threat actor cache of a full database leak. AFRINTEL does not reproduce any client records, invoices, credentials or EPP codes from the reviewed material.

---

### May 2025 - exact attempt date not publicly disclosed
#### Nigeria - PremiumTrust Bank
- **Actor / Group:** Criminal syndicate - identities not attributed
- **Sector:** Finance / Banking
- **Website:** https://premiumtrustbank.com/
- **Incident date:** April-May 2025 - period cited by the EFCC; exact attempt date not publicly disclosed
- **Initial publication date:** 21 May 2025 - EFCC/public reporting; victim statement followed on 22 May
- **Status:** Attempted - Blocked
- **Incident type:** System Intrusion
- **Subtype:** Attempted unauthorized database / infrastructure access
- **Confidence level:** Very High
- **Impact level:** Level 2
- **Source type:** Victim Statement + Law-Enforcement Follow-up
- **Analysis:** PremiumTrust Bank stated that an attempt to gain unauthorized access to its database and infrastructure was detected and neutralized. The matter was referred to law enforcement and suspects were arrested and prosecuted. The bank stated that customer data was not compromised. AFRINTEL therefore tracks this as a confirmed attempted attack, not as a successful breach or Data Leak.
- **Sources:** [Source](https://www.thisdaylive.com/2025/05/22/premiumtrust-bank-reassures-customers-our-security-architecture-remains-resilient-2/)
