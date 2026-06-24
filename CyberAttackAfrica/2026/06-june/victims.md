
### June 6, 2026
#### 🇲🇦 Morocco - IMT (Institut des Mines de Touissit) [Data Leak]

- **Actor / Group:** anisanas2 (forum [Citizen])
- **Sector:** Education / Vocational Training / Mining
- **Status:** Data Leak
- **Website:** [imt.ac.ma](https://imt.ac.ma)
- **Description:**  
  Data leak from Morocco's Institut des Mines de Touissit (IMT), a public vocational training institution founded in 1954. Exposed data includes:
  - **100+ student records** (ESA and GT programs) with CIN (National ID), Massar IDs, full names, emails, phone numbers
  - **37+ teacher records** with CIN, full names, emails, phone numbers, and status (Active/Non Active)
  - **Grade sheets** for multiple subjects (hygiene & safety, electricity basics, RDM, electrical practical work, automation) containing student grades with personal identifiers
- **Analysis:**  
  Exposure of student and teacher PII (CIN, phone, email) combined with academic records enables identity theft, targeted phishing, and academic fraud. The presence of grade sheets allows employers or competitors to identify student performance. CIN (Moroccan National ID) is a permanent identifier, making this a sensitive breach for national identity security. The 1954-founded institution's reputation and student trust are at risk.
  
#### 🇲🇦 Morocco - Tlog.ma [Data Leak / Sale]

- **Actor / Group:** anisanas2
- **Sector:** Logistics / Express Delivery
- **Status:** Data Leak / Sale
- **Website:** [tlog.ma](https://tlog.ma)
- **Description:**  
  Tlog.ma, Morocco’s largest express delivery and logistics company (173+ vehicles), suffered a data breach. Over **700,000 records** (2019–2026) were extracted. A sample of 1,000 records was released publicly. Exposed data includes:  
  - Client names, phone numbers, full addresses (city, street, building details)  
  - Order amounts, payment method (cash on delivery), supplier names, order dates  
  - Internal tracking IDs (some missing)  
  The actor threatens to leak more if ransom (**$500** for full DB) is not paid within 48 hours.
- **Analysis:**  
  Exposure of detailed client PII (full names, precise addresses, phone numbers) combined with purchase histories enables physical harassment, identity theft, targeted phishing, and residential burglary. The dataset reveals the supply chain and commercial relationships of Moroccan businesses (suppliers like Maison des Parfums, Gurkan cargo, etc.). The actor is the same as the previous IMT Morocco breach, indicating a sustained campaign against Moroccan entities.
  

#### 🇲🇦 Morocco - Mines d'Aouli [Data leak and revelation of strategic assets]

#### 🇲🇦 Morocco - Mines d’Aouli
* **Threat Actor / Group:** anisanas2
* **Sector:** Mining / State / Mineral Extraction
* **Status:** Data leak / Disclosure of strategic assets
* **Website:** Not applicable (company under liquidation)
* **Description:**
  A cybercriminal actor claims to have published internal documents allegedly linked to **Mines d’Aouli**, a Moroccan mining company referenced as being under liquidation in several observed fiscal documents.

  The exposed documents appear to cover a long period, from **2001 to 2025**, and include tax filings, balance sheets, profit and loss statements, tax records, VAT tables, provision statements, accounting balances, bank journals and internal working documents.

  The observed material points to a heavily degraded financial situation, including recurring losses, significant negative retained earnings, apparent absence of meaningful revenue over several recent fiscal years, financing debts, shareholder accounts, old receivables and long-term provisions for risks and charges.

  Sensitive elements observed include a **3 million dirham state advance**, an **8.6 million dirham provision related to M.P. files**, a receivable linked to ONE, and documents referring to mining concessions and an exploitation project led by **HIMVEST** around concessions **C154, C155 and C156**.

* **CTI Analysis:**
  This leak goes beyond a standard document exposure. It reveals financial, fiscal and administrative material that could allow a third party to reconstruct the history of a mining company under liquidation, including its ownership structure, debts, provisions, receivables and certain mining-related assets or rights.

  The main CTI value lies in the strategic nature of the documents. They may be used to understand the entity’s financial structure, institutional links, third-party relationships and the economic stakes associated with specific mining titles or concessions.

  The observed data suggests an atypical situation: a company legally maintained in existence despite limited or absent operational activity in recent documents, while still holding mining or historical assets that may retain economic or strategic value.

  At this stage, the incident can be assessed as an **internal document leak with reputational, institutional and economic impact**. Any conclusion related to legal irregularities, administrative lock-in or asset capture should remain treated as a hypothesis requiring independent verification.


  
#### 🇪🇬 Egypt - Egyptian Pilots Database [Database Leak / Sale]

- **Actor / Group:** Xyphorix 
- **Sector:** Aviation / Government / Military
- **Status:** Database Leak / Sale
- **Website:** Not specified
- **Description:**  
  Sale of a database containing personal information of Egyptian pilots (military, commercial, civilian). Fields include names, phone numbers, occupation, city, and marital status. Samples show pilots from Egypt Air, Qatar Airways, Fly Emirates, Petroleum Air Services, Suez Canal Authority, and the Ministry of Civil Aviation. Price not specified.
- **Analysis:**  
  Exposure of sensitive data on aviation personnel, including military and government-affiliated pilots. Risks include identity theft, targeted phishing, espionage, and impersonation of aviation staff. The presence of military and state-owned enterprise pilots makes this database particularly sensitive for national security.
---
### June 08, 2026

#### 🇿🇦 South Africa - South African Army (SANDF) [Classified document leak – Crowd control preparation]

- **Actor / Group:** mosad 
- **Sector:** Defence / National security / Law enforcement
- **Status:** Restricted document leak
- **Website:** Not applicable (internal military document)
- **Description:**  
  Publication of a classified "Warning Instruction" from the South African Army, dated 6 August 2022, preparing infantry forces for deployment in support of the South African Police Service (SAPS) to address civil unrest. The document, authenticated by Major General P.N. Dube (GOC SA Army Infantry Formation), details operational preparations. Exposed information includes:
  - **Complete operational instructions:** deployment plan, 25-hour standby alert, accommodation for 200 soldiers, crowd control equipment.
  - **Troop numbers and assets:** 100 crowd-control trained soldiers to be deployed, 100 Mamba armoured vehicle drivers.
  - **Command structure:** names, ranks and contact details (phone numbers, emails, SSNs) of senior officers involved, including Major General P.N. Dube, Colonel M.S. Rampai, Colonel H.E. Maleka, Lt Col B.I. Taimane.
  - **Timeline and logistics:** specific preparation dates, troop movements, equipment requirements (mattresses, transport) and personnel list submission procedures.
  - **Legal framework:** references to South African laws (Constitution, Defence Act) and operational directives (Op CORONA).
- **Analysis:**  
  The leak of a classified "RESTRICTED" military document reveals sensitive operational capabilities and civil unrest response protocols. The exposure of personal contact details (phone numbers, emails, SSNs) of senior officers poses a major targeting, harassment or interference risk. The disclosure of troop numbers, deployment timelines and equipment compromises operational security (OPSEC) and could enable hostile actors to anticipate or counter law enforcement operations. The timing of the leak (2022 document published in 2026) raises questions about persistent vulnerabilities within South African military communication systems. The document's presence on Telegram channels and hacker forums indicates active circulation within cybercriminal circles.
---
### June 10, 2026
#### 🇳🇬 Nigeria - Jeroid.co [Database Leak / Sale]
- **Actor / Group:** burti 
- **Sector:** Cryptocurrency / Fintech / Exchange
- **Status:** Database Leak / Sale
- **Website:** [jeroid.co](https://jeroid.co) / [jeroid.ng](https://jeroid.ng)
- **Description:**  
  Sale of a full database from Nigeria's largest crypto-to-Naira exchange platform, Jeroid. Dataset includes:
  - **312,433 users** (100% with email, 98% with phone)
  - **759,900 wallets** (129,423 with balance) – platform TVL: $306M
  - **110,282 BVN** (Bank Verification Numbers)
  - **64,300 NIN** (National ID numbers)
  - **70,956 face verification photos** (stored on public S3 bucket without authentication)
  - **3,872 passports**, **2,106 voter cards**, **1,700 driver licenses**
  - **65,013 users with full Level 3 KYC** (BVN + NIN + face scan + ID document)
  - 89 internal staff accounts (including executives)
  Asking price: **$2,000 USD**.
- **Analysis:**  
  One of the most severe financial data leaks recorded. BVN and NIN are Nigeria's primary banking and national identifiers – their exposure enables complete identity theft, financial fraud, loan scams, and money laundering. The unauthenticated S3 bucket containing face verification selfies compounds the risk with biometric identity theft. This leak threatens Nigeria's entire banking ecosystem and citizen trust in fintech platforms.
  
#### 🇿🇦 South Africa - UNISA (University of South Africa) [Data leak – Technical Support]

- **Actor / Group:** GOD User 
- **Sector:** Education / Technical Support / Higher Education
- **Status:** Data leak
- **Website:** [osprey.unisa.ac.za](https://osprey.unisa.ac.za)
- **Description:**  
  Publication of a complete SQL database from UNISA's technical support system, exposing customer, technician, incident and product registration information. The leak, dated 10 June 2026, contains a full dump of the `tech_support` database. Exposed data includes:
  - **`customers` table:** 52 records with customer IDs, names, complete postal addresses, cities, states, postal codes, countries (mainly US and IN), phone numbers, email addresses and passwords in plain text.
  - **`technicians` table:** 5 technicians with names, emails, phone numbers and passwords in plain text.
  - **`incidents` table:** 37 support tickets with detailed descriptions of technical issues encountered by customers.
  - **`registrations` table:** links between customers and products (sports management software) with registration dates.
  - **`products` and `countries` tables:** product lists and country codes.
  - **`administrators` table:** 2 administrator accounts (admin, joel) with passwords in plain text.
- **Analysis:**  
  The presence of plain-text passwords across all tables constitutes a critical security flaw. The personal data (names, addresses, emails, phone numbers) exposes customers and technicians to identity theft, targeted phishing and brute-force attacks on other accounts using the same credentials. Incident descriptions may reveal internal software vulnerabilities. The compromise of administrator accounts (`admin`, `joel`) allows full system access, threatening the integrity of the university's technical support. Although the database is small (21 KB), it is representative of a real system with authentic data, making it a prime target for further attacks.

---
### June 13 , 2026
#### 🇳🇬 Nigeria - National Institute for Legislative and Democratic Studies (NILDS)
- **Threat Actor / Group:** 404Crew Cyber Team x NullSec Nigeria
- **Sector:** Government / Legislative Research
- **Website:** [nils.gov.ng](https://nils.gov.ng)
- **Status:** Data Leak / Claim
- **Description:**  
  The National Institute for Legislative and Democratic Studies (NILDS) is an institution affiliated with Nigeria’s National Assembly, providing research, training, and technical support for legislative and democratic governance activities.
- **Analysis:**  
  The threat actors claim to have compromised multiple databases associated with NILDS and Nigerian parliamentary platforms. The published samples reveal database structures, administrator accounts, email addresses, usernames, and credentials linked to various systems. Such exposure could enable unauthorized access to internal applications, facilitate targeted phishing campaigns, and increase the risk of further compromise of affected government infrastructure. At this stage, the claim is based solely on information released by the threat actors and has not been independently verified.

### June 17, 2026
#### 🌍 Africa (Multi-country) – Public Institutions & Law Enforcement
- **Actor / Source:** Convince (via the cybercriminal forum) 
- **Sector:** Government / Law Enforcement
- **Status:** Active offer
- **Website:** Not specified
- **Description:**  
  A cybercriminal is offering for sale real and active email addresses from African institutions. These accesses are specifically intended to impersonate official authorities in order to submit fake Emergency Disclosure Requests (EDR) to major digital platforms such as Google, Meta, or Telegram.
  The catalog of African government email addresses put up for sale includes:
  * 🇪🇹 **Ethiopia:** 2 emails ($40)
  * 🇹🇿 **Tanzania:** 13,000 emails ($5)
  * 🇦🇴 **Angola:** 3 emails ($20)
  * 🇰🇪 **Kenya:** 5 emails ($20)
  * 🇿🇲 **Zambia:** 650 emails (make offer)
  * 🇳🇬 **Nigeria:** 2 emails ($50, Police)
  * 🇪🇬 **Egypt:** 1 email ($60, Ministry of Finance)
  * 🇲🇦 **Morocco:** 2 emails ($70)
- **Analysis:**  
  This offer does not constitute a data breach passively suffered by these countries, but rather represents a critical exposure of their official authentication vectors. The commercialization of these addresses, combined with the full EDR tutorial sold by the same actor, allows malicious third parties to unduly obtain personal and user data from online platforms by exploiting the trust placed in these countries' authorities. This significantly increases the risk of administrative identity theft and cross-border fraud at both regional and international levels. This threat is all the more concerning as it involves several institutions already targeted by data leaks in May 2026 (Egypt, Morocco, Nigeria), creating favorable conditions for combined attacks.
---
### June 20, 2026
#### 🌍 Africa (Multi-country) – Public Institutions & Law Enforcement (Portal Access Offer)
- **Actor / Source:** [Citizen] Governor (via cybercriminal forum)
- **Sector:** Government / Law Enforcement / Social Media Platforms
- **Status:** Active offer
- **Website:** Not specified
- **Description:**  
  A cybercriminal is offering for sale active government and police email accounts specifically designed to access **Law Enforcement Portals** of major social media platforms (Meta, Instagram, TikTok, X, etc.). These official portals allow legitimate authorities to:
  - **File Data Subpoena Requests**: Obtain IP addresses, phone numbers, emails, direct messages (DMs), deleted posts, and device information.
  - **File Emergency Data Requests (EDR)**: Obtain less comprehensive data (no direct messages) in cases of immediate danger.
  - **Remove posts or suspend accounts** violating the law.
  The catalog of African accounts offered includes:
  * 🇪🇬 **Egypt (Governmental)**: $120
  * 🇲🇼 **Malawi (Governmental)**: $60
  * 🇹🇿 **Tanzania (Governmental)**: $60
  * 🇩🇿 **Algeria (Governmental)**: $100
  * 🇵🇸 **Palestine (Governmental)**: $130
  * 🇰🇪 **Kenya (Police, Governmental)**: $85
  * 🇿🇲 **Zambia (Police, Governmental)**: $60
  * 🇸🇱 **Sierra Leone (Governmental)**: $80
  * 🇾🇪 **Yemen (Governmental)**: $140
- **Analysis:**  
  This offer follows the same logic as the "Convince" actor's, but with a more dangerous specificity: it sells not just raw email addresses, but **complete accounts that already have access to the official platform portals**. This means the buyer does not even need to draft fake EDR requests; they can directly log into the Meta or X interface using a genuine government agent's credentials. The risk is major: mass identity theft, extraction of personal data (including private messages via subpoenas), and manipulation of online content. The inclusion of countries like Palestine and Yemen in the "African" list (according to the seller) suggests an approximate geographical classification, but does not diminish the threat to legitimate African institutions involved.
---
---
### June 20, 2024
#### 🇹🇿 Tanzania - BRELA (Business Registrations and Licensing Agency) [Data Breach]

- **Actor / Group:** hammer (forum [Citizen])
- **Sector:** Government / Business Registration / Licensing
- **Status:** Data Breach (public)
- **Website:** [brela.go.tz](https://www.brela.go.tz)
- **Description:**  
  Massive data breach affecting Tanzania's Business Registrations and Licensing Agency (BRELA), an executive agency under the Ministry of Industry and Trade. The breach exposes **10.2 million records** affecting **8 million people**, including:
  - **7,390,075 unique TIN records** (Individual TINs) with names, National IDs, phones, emails, dates of birth, gender, NID location data
  - **2,155,179 applicant/owner records** (Peoples) with full names, dates of birth, nationality, role, registration details, addresses
  - **368,761 unique business name registrations** with applicant info, business place, owner and operator details, activities
  - **279,462 unique company registrations** with incorporation numbers, TINs, directors, shareholders, financial documents
- **Analysis:**  
  Catastrophic national data breach. The exposure of TINs (Taxpayer Identification Numbers) combined with National IDs, passport numbers, and biometric data enables complete identity theft, financial fraud, tax fraud, and impersonation of business owners. Foreign nationals (Indian, Chinese, etc.) registered in Tanzania are also affected. The breach compromises the entire business registration ecosystem and threatens Tanzania's tax system and financial sector.
---
---
### June 21, 2026
#### 🇳🇬 Nigeria - Nigerian Military (army.mil.ng) [Credential Leak]

- **Actor / Group:** NulleSecNg (forum [Citizen])
- **Sector:** Government / Military / Defense
- **Status:** Data Leak (public)
- **Website:** [army.mil.ng](https://army.mil.ng)
- **Description:**  
  Public leak of credentials and authentication data from the Nigerian military domain `army.mil.ng`. The dataset includes at least **20+ unique email accounts** belonging to military personnel, with plaintext passwords. Exposed accounts include high-level addresses and various unit/battalion accounts. Credentials were captured from Chrome and Edge browsers and include login URLs for military webmail, DigitalGlobe satellite imagery portals (`securewatch.digitalglobe.com`), and other internal systems. The actor claims the leak is politically motivated, protesting government policies on terrorism.
- **Analysis:**  
  Extremely critical national security breach. Exposed military email accounts with plaintext passwords allow full access to internal communications, operational orders, intelligence sharing platforms, and satellite imagery services. This enables espionage, impersonation of military officers, sabotage of operations, and further compromise of classified systems. The presence of credentials for DigitalGlobe (used for reconnaissance) is particularly alarming. The Nigerian military must immediately revoke all exposed passwords and implement multi-factor authentication.

---



