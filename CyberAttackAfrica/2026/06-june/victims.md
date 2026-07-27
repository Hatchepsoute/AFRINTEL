# African victims - June 2026 (40 incidents)

## Monthly snapshot

June 2026 includes **40 unique incidents**: **20 ransomware incidents** and **20 data leaks or access sales**. The records directly or indirectly concern **20 African countries**, including exposure through two multi-country access-sale listings.

### Notable incidents

- **Morocco:** 7 incidents associated with the anisanas2 actor cluster during the month.
- **Nigeria:** claimed exposure of fintech and biometric data associated with Jeroid.co, and email credentials attributed to the Nigerian Army.
- **Tanzania:** 10.2 million records claimed for BRELA, covering approximately 8 million people.
- **Libya:** two consecutive publications by EvaN47 targeting ministries responsible for education.

> The entries below document observed claims or publications. AFRINTEL does not confirm a compromise without independent evidence.

> **Ransomware reading note:** a ransomware entry is included when AFRINTEL observed the victim listing on the group's leak site. `Claim - Unverified` means that no published data or accessible sample was available for analysis at collection time. It does not mean that the listing itself was not observed. Without analysed data, AFRINTEL does not infer encryption, operational disruption or the initial access vector.

### June 01, 2026
#### 🇬🇦 Gabon - Finam Gabon

- **Ransomware group:** DeadLock
- **Sector:** Finance / Banking
- **Status:** Claim - Unverified
- **Website:** [finamgabon.com](https://finamgabon.com/)
- **Initial claim date:** May 5, 2026
- **Announced disclosure date:** May 15, 2026
- **AFRINTEL monitoring date:** June 2026
- **Monthly inclusion basis:** First identified and assessed by AFRINTEL in June 2026
- **Published data:** No publicly accessible data observed
- **Claimed volume:** Not disclosed

- **Description:**
  The DeadLock ransomware group claimed responsibility for a cyberattack against Finam Gabon, a Gabonese microfinance institution providing savings, lending and mobile banking services.

  In its leak site post, the group announced that the allegedly stolen files would become available for download on May 15, 2026.

  During AFRINTEL monitoring in June 2026, no files or data samples attributed to Finam Gabon were publicly accessible on DeadLock's leak site. The download subdomain associated with the victim returned an HTTP 403 response.

---
### June 01, 2026
#### 🇳🇬 Nigeria - Fidelity Pension Managers

- **Ransomware group:** DeadLock
- **Sector:** Finance / Banking
- **Status:** Claim - Unverified
- **Website:** [fidelitypensionmanagers.com](https://www.fidelitypensionmanagers.com/)

- **Description:**
  Fidelity Pension Managers is a licensed pension fund administrator in Nigeria, with digital services for retirement accounts. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.
---
### June 02, 2026
#### 🇿🇦 South Africa - African National Congress (ANC)

- **Ransomware group:** Black X
- **Sector:** Others
- **Website:** [anc1912.org.za](https://www.anc1912.org.za/)
- **Status:** Data Fully Published

- **Description:**

The African National Congress is a South African political party that also describes itself as a national liberation movement. Black X published files presented as originating from its membership management system.

- **Analysis:**

The main analysed file contains 2,310,865 records across 17 columns. The exposed information includes South African identity numbers, names, dates of birth, contact details, residential addresses, languages and membership information. A second file containing 98,026 rows is almost entirely a subset of the main dataset. Fifteen portrait photographs are also included, but no confirmed link to specific records was identified.

The consistency and volume of the files strengthen the credibility of a data exfiltration. However, they do not confirm that the complete database was published, that systems were encrypted, that operations were disrupted or how initial access was obtained. The combination of identity data, residential addresses and possible political affiliation creates a high risk of identity fraud, targeted phishing, smishing, harassment and political profiling.
---
### June 04, 2026
#### 🇪🇬 Egypt - Bouri Group

- **Ransomware group:** TheGentlemen
- **Sector:** E-commerce / Retail
- **Status:** Claim - Unverified
- **Website:** [bouri.net](https://bouri.net/)

- **Description:**
  Bouri Group is an Egyptian group active in the manufacturing, import and distribution of household goods and home appliances. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.
---
### June 05, 2026
#### 🇿🇦 South Africa - Access Dental

- **Ransomware group:** WorldLeaks
- **Sector:** Healthcare / Medical
- **Status:** Claim - Unverified
- **Website:** [accessdental.co.za](https://www.accessdental.co.za/)

- **Description:**
  Access Dental is a South African organization operating in the dental sector. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.
---
### June 05, 2026
#### 🇿🇼 Zimbabwe - First Mutual Holdings

- **Ransomware group:** Nightspire
- **Sector:** Finance / Banking
- **Status:** Claim - Unverified
- **Website:** [firstmutual.co.zw](https://www.firstmutual.co.zw/)

- **Description:**
  First Mutual Holdings is a Zimbabwean financial services group. AFRINTEL observed its listing on Nightspire's leak site, where the group referred to an internal database. No published data or accessible sample was available for analysis at collection time, so the database content, encryption status, operational impact and initial access vector remain unknown.
---
### June 06, 2026
#### 🇲🇦 Morocco - IMT (Institut des Mines de Touissit) [Data Leak]

- **Actor / Group:** anisanas2
- **Sector:** Education / University
- **Status:** Data Fully Published
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
- **Sector:** Others
- **Status:** Claim - Data Sample Published
- **Website:** [tlog.ma](https://tlog.ma)

- **Description:**
  The actor claims to have obtained more than **700,000 records** (2019-2026) linked to Tlog.ma. A sample of 1,000 records was released publicly and analysed. Exposed data includes:
  - Client names, phone numbers, full addresses (city, street, building details)
  - Order amounts, payment method (cash on delivery), supplier names, order dates
  - Internal tracking IDs (some missing)

  The actor threatens to leak more if ransom (**$500** for full DB) is not paid within 48 hours.

- **Analysis:**
  Exposure of detailed client PII (full names, precise addresses, phone numbers) combined with purchase histories enables physical harassment, identity theft, targeted phishing, and residential burglary. The dataset reveals the supply chain and commercial relationships of Moroccan businesses (suppliers like Maison des Parfums, Gurkan cargo, etc.). The actor is the same as the previous IMT Morocco breach, indicating a sustained campaign against Moroccan entities.

#### 🇲🇦 Morocco - Mines d'Aouli

- **Actor / Group:** anisanas2
- **Sector:** Others
- **Status:** Data Fully Published
- **Website:** Not applicable (company under liquidation)

- **Description:**
  A cybercriminal actor claims to have published internal documents allegedly linked to **Mines d'Aouli**, a Moroccan mining company referenced as being under liquidation in several observed fiscal documents.

  The exposed documents appear to cover a long period, from **2001 to 2025**, and include tax filings, balance sheets, profit and loss statements, tax records, VAT tables, provision statements, accounting balances, bank journals and internal working documents.

  The observed material points to a heavily degraded financial situation, including recurring losses, significant negative retained earnings, apparent absence of meaningful revenue over several recent fiscal years, financing debts, shareholder accounts, old receivables and long-term provisions for risks and charges.

  Sensitive elements observed include a **3 million dirham state advance**, an **8.6 million dirham provision related to M.P. files**, a receivable linked to ONE, and documents referring to mining concessions and an exploitation project led by **HIMVEST** around concessions **C154, C155 and C156**.

- **Analysis:**
  This leak goes beyond a standard document exposure. It reveals financial, fiscal and administrative material that could allow a third party to reconstruct the history of a mining company under liquidation, including its ownership structure, debts, provisions, receivables and certain mining-related assets or rights.

  The main CTI value lies in the strategic nature of the documents. They may be used to understand the entity's financial structure, institutional links, third-party relationships and the economic stakes associated with specific mining titles or concessions.

  The observed data suggests an atypical situation: a company legally maintained in existence despite limited or absent operational activity in recent documents, while still holding mining or historical assets that may retain economic or strategic value.

  At this stage, the incident can be assessed as an **internal document leak with reputational, institutional and economic impact**. Any conclusion related to legal irregularities, administrative lock-in or asset capture should remain treated as a hypothesis requiring independent verification.

#### 🇪🇬 Egypt - Egyptian Pilots Database [Database Leak / Sale]

- **Actor / Group:** Xyphorix
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** Not specified

- **Description:**
  Sale of a database containing personal information of Egyptian pilots (military, commercial, civilian). Fields include names, phone numbers, occupation, city, and marital status. Samples show pilots from Egypt Air, Qatar Airways, Fly Emirates, Petroleum Air Services, Suez Canal Authority, and the Ministry of Civil Aviation. Price not specified.

- **Analysis:**
  Exposure of sensitive data on aviation personnel, including military and government-affiliated pilots. Risks include identity theft, targeted phishing, espionage, and impersonation of aviation staff. The presence of military and state-owned enterprise pilots makes this database particularly sensitive for national security.
---
### June 08, 2026
#### 🇿🇦 South Africa - South African Army (SANDF) [Classified document leak - Crowd control preparation]

- **Actor / Group:** mosad
- **Sector:** Government / Administration
- **Status:** Data Fully Published
- **Website:** Not applicable (internal military document)

- **Description:**
  Publication of a classified "Warning Instruction" attributed to the South African Army, dated 6 August 2022, preparing infantry forces for deployment in support of the South African Police Service (SAPS) to address civil unrest. The document identifies senior military personnel and details operational preparations. Exposed information includes:
  - **Complete operational instructions:** deployment plan, 25-hour standby alert, accommodation for 200 soldiers, crowd control equipment.
  - **Troop numbers and assets:** 100 crowd-control trained soldiers to be deployed, 100 Mamba armoured vehicle drivers.
  - **Command structure:** names, ranks and contact details of identifiable senior officers. Individual names and contact details are intentionally omitted by AFRINTEL.
  - **Timeline and logistics:** specific preparation dates, troop movements, equipment requirements (mattresses, transport) and personnel list submission procedures.
  - **Legal framework:** references to South African laws (Constitution, Defence Act) and operational directives (Op CORONA).

- **Analysis:**
  The leak of a classified "RESTRICTED" military document reveals sensitive operational capabilities and civil unrest response protocols. The exposure of personal contact details (phone numbers, emails, SSNs) of senior officers poses a major targeting, harassment or interference risk. The disclosure of troop numbers, deployment timelines and equipment compromises operational security (OPSEC) and could enable hostile actors to anticipate or counter law enforcement operations. The timing of the leak (2022 document published in 2026) raises questions about persistent vulnerabilities within South African military communication systems. The document's presence on Telegram channels and hacker forums indicates active circulation within cybercriminal circles.
---
### June 10, 2026
#### 🇳🇬 Nigeria - Jeroid.co [Database Leak / Sale]

- **Actor / Group:** burti
- **Sector:** Finance / Banking
- **Status:** Claim - Data Sample Published
- **Website:** [jeroid.co](https://jeroid.co) / [jeroid.ng](https://jeroid.ng)

- **Description:**
  Sale of a full database from Nigeria's largest crypto-to-Naira exchange platform, Jeroid. Dataset includes:
  - **312,433 users** (100% with email, 98% with phone)
  - **759,900 wallets** (129,423 with balance), platform TVL: $306M
  - **110,282 BVN** (Bank Verification Numbers)
  - **64,300 NIN** (National ID numbers)
  - **70,956 face verification photos** (stored on public S3 bucket without authentication)
  - **3,872 passports**, **2,106 voter cards**, **1,700 driver licenses**
  - **65,013 users with full Level 3 KYC** (BVN + NIN + face scan + ID document)
  - 89 internal staff accounts (including executives)

  Asking price: **$2,000 USD**.

- **Analysis:**
  One of the most severe financial data leaks recorded. BVN and NIN are Nigeria's primary banking and national identifiers, their exposure enables complete identity theft, financial fraud, loan scams, and money laundering. The unauthenticated S3 bucket containing face verification selfies compounds the risk with biometric identity theft. This leak threatens Nigeria's entire banking ecosystem and citizen trust in fintech platforms.

#### 🇿🇦 South Africa - UNISA (University of South Africa) [Data leak - Technical Support]

- **Actor / Group:** GOD User
- **Sector:** Education / University
- **Status:** Data Fully Published
- **Website:** [osprey.unisa.ac.za](https://osprey.unisa.ac.za)

- **Description:**
  Publication of a complete SQL database from UNISA's technical support system, exposing customer, technician, incident and product registration information. The leak, dated 10 June 2026, contains a full dump of the `tech_support` database. Exposed data includes:
  - **`customers` table:** 52 records with customer IDs, names, complete postal addresses, cities, states, postal codes, countries (mainly US and IN), phone numbers, email addresses and passwords in plain text.
  - **`technicians` table:** 5 technicians with names, emails, phone numbers and passwords in plain text.
  - **`incidents` table:** 37 support tickets with detailed descriptions of technical issues encountered by customers.
  - **`registrations` table:** links between customers and products (sports management software) with registration dates.
  - **`products` and `countries` tables:** product lists and country codes.
  - **`administrators` table:** 2 named administrator accounts with passwords in plain text. Account names are intentionally omitted by AFRINTEL.

- **Analysis:**
  The presence of plain-text passwords across all tables constitutes a critical security flaw. The personal data (names, addresses, emails, phone numbers) exposes customers and technicians to identity theft, targeted phishing and credential-reuse attacks. Incident descriptions may reveal internal software weaknesses. If the published administrator credentials were valid at the time of exposure, they could have enabled unauthorized access to the technical support system. Although the database is small (21 KB), the observed structure and records warrant remediation without requiring AFRINTEL to reproduce account identifiers.
---
### June 13, 2026
#### 🇳🇬 Nigeria - National Institute for Legislative and Democratic Studies (NILDS) / National Assembly of Nigeria

- **Actor / Group:** 404Crew Cyber Team
- **Coalition:** NullSec Nigeria
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** [nilds.gov.ng](https://nilds.gov.ng/) / [nass.gov.ng](https://nass.gov.ng/)

- **Description:**
  NILDS is an organ of the National Assembly of Nigeria responsible for parliamentary research, training and legislative support.

- **Analysis:**
  The actors claim to have compromised a NILDS database and published an unverified download link. The evidence shows six databases, including several associated with the National Assembly. The `nass_nassdb` database contains 29 tables covering administrative accounts, bills, committees, petitions, sittings, votes and parliamentary documents.

  The samples include a document marked confidential, a register of 24 international agreements and an old NILS logo. No personal data, authentication information or complete database records are visible. A direct compromise of the Nigerian Presidency is not demonstrated.

  The political message associated with `#OpNigeria`, without a financial demand, suggests a likely hacktivist motivation. The main risks include institutional document exposure, targeted phishing, impersonation of public officials and potential access to administrative accounts.

  **Confidence level: Medium.**
---
### June 15, 2026
#### 🇪🇬 Egypt - Sheraton Miramar Resort El Gouna

- **Ransomware group:** Nightspire
- **Sector:** Others
- **Status:** Claim - Unverified
- **Website:** [elgouna.com](https://www.elgouna.com/hotels/sheraton-miramar-resort-el-gouna)

- **Description:**
  Sheraton Miramar Resort El Gouna is a hotel located in El Gouna, Egypt. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.
---
### June 16, 2026
#### 🇹🇳 Tunisia - Sumitomo Electric Bordnetze, SEBN Tunisia / Fejja site

- **Ransomware group:** Aurora
- **Sector:** Others
- **Status:** Claim - Unverified
- **Website:** [sebn.com](https://www.sebn.com/en/locations/sebn-tn/)

- **Description:**
  Sumitomo Electric Bordnetze is an automotive supplier with an operation at the SEBN Tunisia / Fejja site. AFRINTEL observed this Tunisian site in Aurora's ransomware listing, together with a claimed data volume. No published data or accessible sample was available for analysis at collection time; the content, encryption status, operational impact and initial access vector remain unknown.
---
### June 17, 2026
#### 🌍 Africa (Multi-country) - Public Institutions & Law Enforcement

- **Actor / Group:** Convince (via a cybercriminal forum)
- **Sector:** Government / Administration
- **Status:** Claim - Unverified
- **Website:** Not specified

- **Description:**
  A cybercriminal is offering for sale real and active email addresses from African institutions. These accesses are specifically intended to impersonate official authorities in order to submit fake Emergency Disclosure Requests (EDR) to major digital platforms such as Google, Meta, or Telegram.

  The catalog of African government email addresses put up for sale includes:
  - 🇪🇹 **Ethiopia:** 2 emails ($40)
  - 🇹🇿 **Tanzania:** 13,000 emails ($5)
  - 🇦🇴 **Angola:** 3 emails ($20)
  - 🇰🇪 **Kenya:** 5 emails ($20)
  - 🇿🇲 **Zambia:** 650 emails (make offer)
  - 🇳🇬 **Nigeria:** 2 emails ($50, Police)
  - 🇪🇬 **Egypt:** 1 email ($60, Ministry of Finance)
  - 🇲🇦 **Morocco:** 2 emails ($70)

- **Analysis:**
  This offer does not constitute a data breach passively suffered by these countries, but rather represents a critical exposure of their official authentication vectors. The commercialization of these addresses, combined with the full EDR tutorial sold by the same actor, allows malicious third parties to unduly obtain personal and user data from online platforms by exploiting the trust placed in these countries' authorities. This significantly increases the risk of administrative identity theft and cross-border fraud at both regional and international levels. This threat is all the more concerning as it involves several institutions already targeted by data leaks in May 2026 (Egypt, Morocco, Nigeria), creating favorable conditions for combined attacks.

#### 🇪🇬 Egypt - Great Foods

- **Ransomware group:** Lamashtu
- **Sector:** E-commerce / Retail
- **Status:** Claim - Unverified
- **Website:** [greatfoods.com.eg](https://greatfoods.com.eg/)

- **Description:**
  Great Foods is an Egyptian food manufacturing and distribution company, part of El Naggar Group. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.

#### 🇸🇳 Senegal - Cour des Comptes du Sénégal

- **Ransomware group:** Krybit
- **Sector:** Government / Administration
- **Status:** Data Fully Published
- **Website:** [courdescomptes.sn](https://www.courdescomptes.sn/)
- **Claimed volume:** 19.73 GB

- **Description:**
  The Court of Auditors of Senegal is a supreme audit institution responsible for overseeing public finances, verifying the regularity of public revenues and expenditures, and reviewing the management of public bodies.

- **Analysis:**
  The KRYBIT ransomware group claimed an attack against the Court of Auditors of Senegal and later published files attributed to the institution after the countdown deadline expired. The first observed files mostly appeared to be public or academic documents, but subsequent batches included several files directly linked to the Court of Auditors, particularly the Chamber of Budgetary and Financial Affairs. The observed material includes internal meeting notices, deliberation agendas, documents related to the clearance plan for State accounts, notification letters, internal notes, working materials, HR-related documents, and reports linked to sensitive audits, including mining sector revenues, medical coverage for State employees, and public accounting offices. No technical credentials, passwords, or system configuration files were observed at this stage in the reviewed files. However, the institutional nature of the documents increases the credibility of the leak and exposes the organization to risks of social engineering, administrative impersonation, reputational pressure, and manipulation of information related to public finance oversight.
---
### June 18, 2026
#### 🇧🇼 Botswana - Botswana Vaccine Institute (BVI)

- **Ransomware group:** LockBit 5
- **Sector:** Healthcare / Medical
- **Status:** Claim - Unverified
- **Website:** [bvi.co.bw](https://bvi.co.bw/)

- **Description:**
  Botswana Vaccine Institute is a Botswana-based animal-health organization producing veterinary vaccines. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.

#### 🇿🇦 South Africa - Grey High School

- **Ransomware group:** LockBit 5
- **Sector:** Education / University
- **Status:** Claim - Unverified
- **Website:** [greyhighschool.com](https://www.greyhighschool.com/)

- **Description:**
  Grey High School is a secondary school in South Africa. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.

#### 🇲🇺 Mauritius - Nundun Gopee & Co Ltd

- **Ransomware group:** LockBit 5
- **Sector:** Others
- **Status:** Claim - Unverified
- **Website:** [nundungopee.mu](http://www.nundungopee.mu)

- **Description:**
  Nundun Gopee & Co Ltd is a Mauritian organization associated with the domain nundungopee.mu. AFRINTEL observed its listing on LockBit 5's leak site. No published data or accessible sample was available for analysis at collection time; encryption, operational disruption and the initial access vector remain unknown.
---
### June 19, 2026
#### 🇲🇦 Morocco - MUPRAS RAM

- **Ransomware group:** Krybit
- **Sector:** Finance / Banking
- **Status:** Data Fully Published
- **Website:** [mupras.com](https://mupras.com/)

- **Description:**
  MUPRAS RAM is a Moroccan mutual provident and social action organization dedicated to Royal Air Maroc employees, affiliates and beneficiaries. It covers medical care, healthcare reimbursements, social benefits, contributions and relationships with healthcare, banking and IT partners.

- **Analysis:**
  The analysis of the leaked data attributed to MUPRAS indicates a high-criticality exposure. The observed documents do not appear to be limited to isolated administrative files. They cover several sensitive areas of the organization: member management, contributions, medical reimbursements, social benefits, banking flows, accounting records, internal documents, IT maintenance contracts, information system-related elements, and relationships with healthcare providers, banks and IT suppliers.

  The main sensitivity of this leak comes from the combination of exposed data. The files appear to link members and beneficiaries to contributions, reimbursements, medical files, amounts, internal references, healthcare providers, transfers, direct debits, bank details and administrative documents. This significantly increases the risk of secondary exploitation: targeted phishing, reimbursement fraud, fraudulent bank detail changes, identity theft, fake provider disputes, manipulation of financial services and social engineering.

  From a CTI perspective, the leak also provides strong visibility into the operational ecosystem of MUPRAS. The documents may help identify relationships with clinics, hospitals, pharmacies, laboratories, banks, insurers, suppliers and IT service providers. For a threat actor, this type of information can be used to build highly credible social engineering scenarios, using real references, real amounts, real provider names or real internal processes.

  This disclosure poses a high risk for members, healthcare providers, banks, suppliers and internal staff. No public confirmation from the victim is included in this analysis.
---
### June 20, 2026
#### 🌍 Africa (Multi-country) - Public Institutions & Law Enforcement (Portal Access Offer)

- **Actor / Group:** Governor
- **Sector:** Government / Administration
- **Status:** Claim - Unverified
- **Website:** Not specified

- **Description:**
  A cybercriminal is offering for sale active government and police email accounts specifically designed to access **Law Enforcement Portals** of major social media platforms (Meta, Instagram, TikTok, X, etc.). These official portals allow legitimate authorities to:
  - **File Data Subpoena Requests:** Obtain IP addresses, phone numbers, emails, direct messages (DMs), deleted posts, and device information.
  - **File Emergency Data Requests (EDR):** Obtain less comprehensive data (no direct messages) in cases of immediate danger.
  - **Remove posts or suspend accounts** violating the law.

  The catalog of African accounts offered includes:
  - 🇪🇬 **Egypt (Governmental):** $120
  - 🇲🇼 **Malawi (Governmental):** $60
  - 🇹🇿 **Tanzania (Governmental):** $60
  - 🇩🇿 **Algeria (Governmental):** $100
  - 🇵🇸 **Palestine (Governmental):** $130
  - 🇰🇪 **Kenya (Police, Governmental):** $85
  - 🇿🇲 **Zambia (Police, Governmental):** $60
  - 🇸🇱 **Sierra Leone (Governmental):** $80
  - 🇾🇪 **Yemen (Governmental):** $140

- **Analysis:**
  This offer follows the same logic as the "Convince" actor's, but with a more dangerous specificity: it sells not just raw email addresses, but **complete accounts that already have access to the official platform portals**. This means the buyer does not even need to draft fake EDR requests; they can directly log into the Meta or X interface using a genuine government agent's credentials. The risk is major: mass identity theft, extraction of personal data (including private messages via subpoenas), and manipulation of online content. The inclusion of countries like Palestine and Yemen in the "African" list (according to the seller) suggests an approximate geographical classification, but does not diminish the threat to legitimate African institutions involved.

#### 🇹🇿 Tanzania - BRELA (Business Registrations and Licensing Agency) [Data Breach]

- **Actor / Group:** hammer (forum [Citizen])
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** [brela.go.tz](https://www.brela.go.tz)

- **Description:**
  Massive data breach affecting Tanzania's Business Registrations and Licensing Agency (BRELA), an executive agency under the Ministry of Industry and Trade. The breach exposes **10.2 million records** affecting **8 million people**, including:
  - **7,390,075 unique TIN records** (Individual TINs) with names, National IDs, phones, emails, dates of birth, gender, NID location data
  - **2,155,179 applicant/owner records** (Peoples) with full names, dates of birth, nationality, role, registration details, addresses
  - **368,761 unique business name registrations** with applicant info, business place, owner and operator details, activities
  - **279,462 unique company registrations** with incorporation numbers, TINs, directors, shareholders, financial documents

- **Analysis:**
  High-impact national data exposure. The exposure of TINs (Taxpayer Identification Numbers) combined with National IDs, passport numbers, and biometric data enables complete identity theft, financial fraud, tax fraud, and impersonation of business owners. Foreign nationals (Indian, Chinese, etc.) registered in Tanzania are also affected. The exposure creates risks across the business registration ecosystem and threatens Tanzania's tax system and financial sector.
---
### June 21, 2026
#### 🇳🇬 Nigeria - Nigerian Military (army.mil.ng) [Credential Leak]

- **Actor / Group:** NulleSecNg
- **Sector:** Government / Administration
- **Status:** Data Fully Published
- **Website:** [army.mil.ng](https://army.mil.ng)

- **Description:**
  Public leak of credentials and authentication data from the Nigerian military domain `army.mil.ng`. The dataset includes at least **20+ unique email accounts** belonging to military personnel, with plaintext passwords. Exposed accounts include high-level addresses and various unit/battalion accounts. Credentials were captured from Chrome and Edge browsers and include login URLs for military webmail, DigitalGlobe satellite imagery portals (`securewatch.digitalglobe.com`), and other internal systems. The actor claims the leak is politically motivated, protesting government policies on terrorism.

- **Analysis:**
  High-impact national security exposure. If valid at the time of observation, the exposed military email accounts and plaintext passwords could enable unauthorized access to internal communications, operational orders, intelligence sharing platforms, and satellite imagery services. Potential consequences include espionage, impersonation of military personnel and secondary compromise of connected systems. The presence of credentials for DigitalGlobe (used for reconnaissance) is particularly alarming. The Nigerian military must immediately revoke all exposed passwords and implement multi-factor authentication.


#### 🇾🇹 Mayotte - Municipality of Ouangani
- **Ransomware group:** DeadLock
- **Sector:** Government / Administration
- **Website:** [ville-ouangani.yt](https://ville-ouangani.yt/)
- **Status:** Data Fully Published
- **AFRINTEL classification:** Data Fully Published

- **Description:**

Ouangani is a municipality located in Mayotte. The municipality provides local administrative services and manages public finances, facilities and development projects.

- **Analysis:**

DeadLock published approximately **138 MB of data** attributed to the Municipality of Ouangani.

The observed documents include financing agreements, payment spreadsheets, municipal workforce records, a list of secondary school graduates, payroll documents, civil registry records, a driving licence application, a training offer and internal meeting reports.

The workforce file exposes employee identities, birth years, hiring dates, grades, categories, departments, positions and employment status. The graduate list contains identities, villages, telephone numbers, educational institutions, courses and academic results.

Individual documents also reveal postal addresses, photographs, signatures, family relationships, civil registry references, social security information, salary data and banking details. Financial records contain suppliers, expenditure descriptions, budget codes, dates, amounts, mandate numbers and payment slip references. Several worksheets are duplicated across different workbooks and should not be counted more than once.

The financing agreements and internal documents also expose banking details, a SEPA mandate, signature-related elements, budgets, municipal projects and internal approval procedures.

This information could facilitate identity theft, targeted phishing, bank account change fraud, fraudulent invoicing, payroll diversion and the impersonation of suppliers or municipal officials.

No passwords, access tokens, API keys or technical indicators of compromise were identified in the observed documents. The files do not establish the initial access vector, the exact compromise date or the exfiltration method. The association with DeadLock is based on the group’s publication.
---
### June 22, 2026
#### 🇱🇾 Libya - Central Bank of Libya

- **Ransomware group:** Qilin
- **Sector:** Finance / Banking
- **Status:** Claim - Unverified
- **Website:** [cbl.gov.ly](https://cbl.gov.ly/en/)

- **Description:**
  The Central Bank of Libya is Libya's central banking institution. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.
---
### June 23, 2026
#### 🇰🇪 Kenya - Kenya National Highways Authority (KeNHA)

- **Ransomware group:** DeadLock
- **Sector:** Government / Administration
- **Status:** Claim - Unverified
- **Website:** [kenha.co.ke](https://kenha.co.ke/)

- **Description:**
  Kenya National Highways Authority is the Kenyan public authority responsible for the construction, management and maintenance of national roads. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.



#### 🇹🇳 Tunisia – Examens.tn

- **Actor / Group:** AshleyWood2022
- **Sector:** Education / University
- **Status:** Data Fully Published
- **Website:** [examens.tn](https://examens.tn/)

- **Description:**

Examens.tn is a Tunisian educational platform providing courses, exercises and exam-preparation resources for students and teachers.

- **Analysis:**

The actor `AshleyWood2022` published the platform’s complete database. The disclosure includes the approximately **717 MB** `examens.sql` dump, together with the `wp_users` and `wp_usermeta` exports.

Analysis of the CSV files confirms the exposure of **3,697 user accounts** and **74,891 metadata records**. The leaked data includes usernames, email addresses, display names, WordPress password hashes, account statuses, payment-related information and user roles, including one administrator account.

The metadata also contains session tokens, password-reset tokens, Google Site Kit OAuth data and an application password. This exposure increases the risk of targeted phishing, credential stuffing and account compromise.

- **Recommendations:**

1. Reset passwords, revoke exposed sessions, recovery tokens, OAuth access and application passwords, and enforce multi-factor authentication for privileged accounts.
2. Identify and remediate the initial compromise vector, review WordPress and server logs, monitor abnormal authentication attempts and notify affected users.
---
### June 25, 2026
#### 🇲🇦 Morocco - MG Maroc

- **Actor / Group:** 404Crew Cyber Team
- **Sector:** Healthcare / Medical
- **Status:** Claim - Data Sample Published
- **Website:** [mgmaroc.com](https://mgmaroc.com)

- **Description:**
  MG Maroc is a Moroccan association representing general practitioners and providing continuing medical education, professional resources, and training services for healthcare professionals across Morocco.

- **Analysis:**
  A threat actor operating under the name **404Crew Cyber Team** claims to have compromised MG Maroc and to possess data covering the **2025-2026** period. The published samples include administrative documents containing employee social security declaration records. The exposed information appears to include employees' full names, registration numbers, declared salaries (in Moroccan dirhams), number of working days, social security affiliation numbers, and administrative certificates. The screenshots display hundreds of employee records, suggesting the exposure of HR and payroll-related information. If authentic, this information could facilitate identity theft, payroll fraud, targeted phishing campaigns, and social engineering attacks against employees by leveraging sensitive employment and salary data. Based on the available evidence, the published material appears to be a sample intended to support the actor's claim of compromise.
---
### June 26, 2026
#### 🇹🇳 Tunisia - Centrale Laitière du Cap-Bon (CLC)

- **Ransomware group:** SETTRA
- **Sector:** Others
- **Status:** Claim - Unverified
- **Website:** [clc-tn.com](https://clc-tn.com/)

- **Description:**
  Centrale Laitière du Cap-Bon is a Tunisian dairy company and a subsidiary of Delice Holding, specializing in milk collection, processing, UHT packaging and distribution. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.

#### 🇲🇦 Morocco - Avito.ma

- **Actor / Group:** anisanas2
- **Sector:** E-commerce / Retail
- **Status:** Claim - Data Sample Published
- **Website:** [avito.ma](https://www.avito.ma)

- **Description:**
  Avito.ma is a Moroccan classified advertising platform used by individuals and businesses to sell vehicles, real estate, electronic devices and other products.

- **Analysis:**
  PKA291 claims to have collected the complete Avito.ma archive and is offering the full database for USD 800. The shared document is a sample containing 200,000 listings and 17 fields, including seller information, phone numbers, listing identifiers, titles, prices, locations and publication dates. The sample contains approximately 47,695 distinct phone numbers and data collected between 24 and 25 June 2026. Its structure mainly indicates automated scraping of publicly available listings, with no visible evidence of access to Avito.ma's internal systems. No passwords, session tokens or authentication credentials were observed. The information could nevertheless support spam, smishing, targeted fraud and seller profiling. The sample appears structurally consistent, but it does not confirm the existence or completeness of the full database offered for sale. Avito.ma had already been the subject of a publication in May 2026, but the sample released at that time contained only around ten records attributed to customers or sellers.

#### 🇲🇦 Morocco - Startup management platform, operator unidentified

- **Actor / Group:** anisanas2
- **Sector:** Others
- **Status:** Data Fully Published
- **Website:** Platform operator unidentified

- **Description:**
  anisanas2 describes the source of the exposed data as a "Moroccan Startups Management System". The affected system appears to have been used to collect or manage administrative, legal and professional records belonging to Moroccan startups.

  The platform's name is concealed in the publication. No domain, logo or other verifiable information formally identifies its operator.

  Four Moroccan companies are represented in the published archives:

  | Affected organisation | Identified activity | Official website |
  |---|---|---|
  | ARSYS INFO SARL AU | IT integration, networks, systems, cybersecurity, information systems auditing and consulting | Unidentified |
  | AUDD | Digital agency, according to a public presence associated with the name "Audd Agency". The connection with the company represented in the leak has not been formally confirmed | Unidentified |
  | Black Service Solution SARL / BFRET | Transport, logistics and a platform connecting shippers with carriers | [bfreteurope.com](https://www.bfreteurope.com) |
  | Media Triangle SARL AU | Computer programming, systems analysis and design, and online sales | Unidentified |

  The bfreteurope.com domain belongs to the BFRET platform operated by Black Service Solution. No verifiable official domain was found for ARSYS INFO, AUDD or Media Triangle.

- **Analysis:**
  The publication contains four RAR archives representing approximately 21.5 MB and at least 47 documents:

  | Archive | Announced size | Observed content |
  |---|---:|---|
  | ARSYS COMPANY | 8.1 MB | Identity cards, CVs, professional certificates, articles of association, commercial registry records, tax documents and CNSS records |
  | AUDD company | 5.9 MB | Identity cards, CVs, articles of association, Model J extract, commercial registry records, tax identifiers and professional tax documents |
  | BLACKSERVICESOLUTION | 4.3 MB | Identity cards, passport, CVs, articles of association, signatures, tax documents, commercial registry records, and accounting and tax statements |
  | MEDIA TRIANGLE DOCS | 3.2 MB | Identity card, CV, articles of association, commercial registry records, CNSS affiliation bulletin, tax bulletin and Model J extract |

  The documents concern four legally separate companies. The homogeneous structure of the folders, including the recurring presence of identity documents, CVs, articles of association and registration records, suggests that they originated from a shared application, incubation, support or administrative management system.

  This similarity does not identify the organisation operating the platform or confirm how the documents were collected. No public connection between all four companies and a specific incubator, accelerator or funding programme was established.

  The primary victim should therefore remain recorded as an unidentified operator. ARSYS INFO, AUDD, Black Service Solution and Media Triangle are four downstream affected organisations. ARSYS INFO should not be considered the primary victim solely because its archive is the largest.

  The observed data includes:
  - national identity cards and a passport;
  - identity photographs, signatures and MRZ information;
  - personal and professional addresses;
  - CVs describing the backgrounds of founders and executives;
  - articles of association and company formation documents;
  - management powers and shareholding structures;
  - commercial registry records and Model J extracts;
  - tax identifiers and tax documents;
  - CNSS affiliation records;
  - professional certificates and training documents;
  - accounting information covering assets, liabilities, expenses, cash holdings and financial results.

  Black Service Solution has the most financially sensitive folder because it contains accounting and tax statements. This does not establish the company as the primary victim of the affected system.

  No passwords, access tokens, API secrets or login credentials were observed in the files that could be analysed. The initial access vector, the actual compromise date and the total volume of accessible documents remain unknown.

  The "Price: Not For Sale" statement indicates that the data was not offered for sale in this publication. The four archives were directly available for download. It is not possible to confirm whether they represent all accessible data or only a selection of folders extracted from the system.

  The exposure of identity documents, signatures, corporate records and financial information creates significant risks of identity theft, document forgery, banking fraud, fraudulent bank detail changes, business email compromise and targeted social engineering.

  The information could be used to create credible fraudulent requests directed at banks, government agencies, investors, customers or business partners.

  For AFRINTEL accounting, this publication can be recorded as a multi-organisation incident affecting at least four Moroccan companies. The primary victim should remain unidentified until the operator or domain of the shared system has been formally established.

#### 🇲🇦 Morocco - Unidentified Moroccan delivery company

- **Actor / Group:** anisanas2
- **Sector:** Others
- **Status:** Data Fully Published
- **Website:** Not identified

- **Description:**
  The affected organisation reportedly operates a delivery management system used in Morocco since 2019. Its identity is masked in the publication. The observed data shows nationwide operations covering order preparation, courier assignment, transportation, delivery, cash collection and return management.

- **Analysis:**
  The actor anisanas2 presents the file as the full database and claims that it contains nearly 500,000 records. The analysed CSV file is approximately 344.5 MiB and contains exactly 486,024 delivery records across 16 columns. This volume matches the forum publication and confirms that the file is not a small sample.

  The records cover the period from 4 July 2019 to 20 June 2026, representing almost seven years of activity. Each record contains a unique 11-character tracking code using the format `MP#########`. This prefix alone is insufficient to identify the affected company.

  The exposed fields include:
  - tracking codes and internal references;
  - recipient names;
  - delivery addresses;
  - cities;
  - telephone numbers;
  - cash-on-delivery amounts;
  - parcel exchange and opening options;
  - order creation dates;
  - ordered products;
  - complete delivery status histories;
  - product preparation, storage and return statuses;
  - cash-on-delivery payment statuses.

  The analysis identified approximately 407,315 distinct telephone values, 290,358 distinct addresses and 248,215 distinct recipient labels. These figures do not necessarily represent the same number of unique individuals because customers may appear several times and telephone numbers use different formats.

  The database contains 374 city labels. The largest volumes concern Casablanca, Marrakech, Tangier, Rabat, Fez, Agadir, Kenitra, Sale, Meknes and Oujda, confirming nationwide coverage.

  More than 208,000 records also contain product descriptions and preparation information. The observed histories cover delivery requests, packaging, courier assignment, sorting centre reception, transportation, delivery, payment, postponement, refusal, cancellation and return to stock.

  No passwords, user accounts, email addresses, API keys, access tokens or banking details were observed. Some rows contain missing or incorrectly positioned values, indicating minor export and data-quality issues.

  The combination of recipient names, telephone numbers, addresses, ordered products, payment amounts and real delivery statuses could support highly credible smishing, vishing and delivery fraud campaigns. Attackers could impersonate the carrier, request fraudulent fees, modify delivery details, organise fake redeliveries or target customers according to the nature and value of their orders.

  The exact identity of the company remains unknown. The file confirms the large-scale exposure of a Moroccan delivery management system, but no domain, logo or legal name supports a reliable attribution.
---
### June 27, 2026
#### 🇲🇦 Morocco - Stellantis Morocco

- **Actor / Group:** anisanas2
- **Sector:** Others
- **Status:** Claim - Data Sample Published
- **Website:** [stellantis.com](https://www.stellantis.com)

- **Description:**
  Stellantis is a global automotive group formed through the merger of Fiat Chrysler Automobiles and PSA Group. Its portfolio includes 14 automotive brands, including Abarth, Alfa Romeo, Citroën, Dodge, Fiat, Jeep, Maserati, Opel and Peugeot. The group also maintains industrial and commercial operations in Morocco.

- **Analysis:**
  The actor published a downloadable file named `stellantis_1000_sample.csv` and claims to have compromised Stellantis operations in Morocco and extracted a complete database.

  The analysed file is 84,397 bytes, approximately 82.4 KiB. Despite the reference to 1,000 entries in its filename, it contains exactly 992 logical records across 10 columns: brand, model, name, phone number, email address, city, date, campaign, reseller comment and customer comment.

  The sample contains 978 populated names, 992 phone numbers, 562 email addresses, 64 location values, 23 brand values and 67 vehicle models. The records cover the period from 9 October 2022 to 22 March 2026. Casablanca accounts for 443 entries, followed by Rabat, Marrakech, Agadir and Tangier.

  The most represented brands are Fiat, Jeep, Renault, Alfa Romeo and Peugeot. The presence of brands competing with Stellantis suggests that the file may originate from an automotive lead-management platform, a sales CRM or a multi-brand source. This does not establish that the file was technically extracted from an internal Stellantis Morocco system.

  The `campagne` and `commentaire reseller` fields are empty across all 992 records. The `commentaire client` field is populated in 26 records and mainly contains sales follow-up information, such as assignment to a sales agent, customer unavailability or the result of a contact attempt.

  No passwords, authentication credentials, identity document numbers, banking details or payment information were observed in the sample. However, the combination of contact details, city, vehicle interest and request date could support targeted phishing, smishing and vishing campaigns, dealership impersonation, fraudulent financing offers and commercial lead theft.

  The sample confirms the publication of structured personal data related to the Moroccan automotive sector. It does not verify the claimed extraction of a complete database or independently confirm a direct compromise of Stellantis Morocco.
---
### June 28, 2026
#### 🇹🇳 Tunisia - monoprix.tn

- **Ransomware group:** Stormous
- **Sector:** E-commerce / Retail
- **Status:** Claim - Unverified
- **Website:** [monoprix.tn](https://www.monoprix.tn)

- **Description:**
  monoprix.tn is a Tunisian retail platform. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.

#### 🇿🇦 South Africa - Fidelity Security Group

- **Ransomware group:** CMD Organization
- **Sector:** Others
- **Status:** Claim - Unverified
- **Website:** [fidelity-services.com](https://fidelity-services.com/)

- **Description:**
  Fidelity Security Group is a South African provider of security services and solutions. AFRINTEL observed the victim listing on the ransomware group's leak site. At collection time, no published data or accessible sample was available for analysis. The listing is therefore documented as an observed ransomware claim; encryption, operational disruption and the initial access vector remain unknown.
---
### June 29, 2026
#### 🇱🇾 Libya - Ministry of Technical and Vocational Education

- **Actor / Group:** [Citizen] EvaN47
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** [tve.gov.ly](https://tve.gov.ly)

- **Description:**
  The Ministry of Technical and Vocational Education, وزارة التعليم التقني والفني, is a Libyan government entity linked to technical education and vocational training. Its scope includes institutes, technical colleges, training programs, academic registrations and administrative systems associated with students.

- **Analysis:**
  The publication exposes a database attributed to the Libya Ministry of Technical and Vocational Education, with a claimed volume of 900,000 students.

  The visible samples show structured student records, including national numbers, names in Arabic and English, phone numbers, institutions, academic registration numbers, departments, specializations, academic years, semesters, gender and nationality.

  A second screenshot shows a user account table containing official @tve.gov.ly emails, names, phone numbers and a password-related field. Sensitive values are not reproduced here.

  The observed data appears to come from an application or relational database linked to an academic management system. The visible structure shows at least two data categories: a student records table and a user or administrator account table.

  The main risks are identity theft, targeted phishing, document fraud, mapping of educational institutions and secondary compromise of institutional accounts.

  The operational value for an attacker is high, as the data can help identify students, institutions, internal accounts and users linked to the government domain. No price, deadline or direct download link is visible in the provided screenshots.
---
### June 30, 2026
#### 🇱🇾 Libya - Ministry of Education of Libya

- **Actor / Group:** EvaN47
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** [moe.gov.ly](https://moe.gov.ly)

- **Description:**
  The Ministry of Education of Libya, وزارة التربية والتعليم, is the Libyan government entity responsible for the education sector. Its scope includes national education services, examinations, school records, certificates and administrative systems linked to pupils and students.

- **Analysis:**
  The publication exposes a database attributed to the Ministry of Education of Libya, with a claimed volume of **287 GB** of personal and sensitive data linked to citizens and the ministry's systems.

  The data listed in the publication includes secondary education completion certificates for students across Libya, student national ID numbers, personal photos, passport photos, other sensitive official documents, and personal or administrative files linked to the ministry's systems.

  The screenshots show a visible sample made of many document thumbnails. The observed files mainly include certificates, school documents, administrative papers, scanned images and PDF files. Several documents appear to contain identity photos, official stamps and school-related information. Visible personal data is not reproduced here.

  The publication contains an explicit threat to publish the data if no contact is made. No price, no precise deadline and no direct download link are visible in the provided screenshots.

  The operational value of the data is significant. Certificates, national ID numbers, photos, passports and administrative documents can support identity theft, document fraud, targeted phishing, pressure against individuals, or the creation of exploitable profiles against students and families.

  For an attacker, these documents can also help map education processes, official document formats and internal administrative workflows.

  The main risk concerns the large-scale exposure of government and school-related documents, with potential impact on student privacy, academic record integrity and trust in the ministry's digital systems.

- **Sample analysis:**

| Element | Observation |
|---|---|
| Visible storage type | File gallery, scanned images and PDFs |
| Database type | Not determinable from the screenshot |
| Visible technologies | No server or application technology identifiable |
| Visible structure | Numbered document series, image thumbnails and PDF files |
| Sensitive data | Yes, identity documents, certificates, photos, national ID numbers according to the publication |
| Business data | Yes, school and administrative documents linked to the ministry |
| Financial data | Not visible |
| HR data | Not visible |
| Customer data | Not applicable |
| Health data | Not visible |
| Government data | Yes |
| Critical data | Yes, official documents and personal student data |
