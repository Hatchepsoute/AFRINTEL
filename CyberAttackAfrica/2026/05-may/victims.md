# African victims - May 2026

## Monthly snapshot

May 2026 includes **57 unique incidents**: **17 ransomware incidents** and **40 data leaks or access sales**. The records concern **18 African countries**: 12 directly affected countries and 6 additional countries exposed only through three multi-country incidents.

### Notable incidents

- **Egypt:** the education sector was affected by several large claims, including 26.8 million student records attributed to the Ministry of Education.
- **South Africa:** multiple public institutions were targeted during the coordinated OpSouthAfrica campaign.
- **Tanzania:** more than 10,000 police webmail accounts with plaintext passwords were offered for sale.
- **Senegal:** AuditTeam claimed data exfiltration from the Trésor Public, including approximately 1.66 million database records.

> The entries below document observed claims or publications. AFRINTEL does not confirm a compromise without independent evidence.

### May 02, 2026
#### 🇪🇬 Egypt - Ministry of Manpower / Ministry of Labour [Data Leak]
- **Actor / Group:** CrowStealer
- **Sector:** Government / Administration
- **Website :** https://www.manpower.gov.eg/
- **Status:** Claim - Unverified
- **Description :**  Egypt’s Ministry of Labour (formerly Ministry of Manpower) is the governmental authority responsible for employment management, labour affairs, work permits, and workforce administration in Egypt.
- **Sample analysis :**
  The analyzed samples contain full names, national ID numbers, birth dates, addresses, phone numbers, email addresses, professional information, passport numbers, passport expiration dates, and administrative records associated with workers and expatriates.
---
### May 03, 2026
#### 🇹🇿 Tanzania - Personal Database (120,000+ records)

- **Actor / Group:** XOverStm (via the [Citizen] forum)
- **Sector:** Personal Data Aggregation
- **Status:** Claim - Data Sample Published
- **Website:** Not specified

- **Description:**
  A cybercriminal is offering for sale a database containing more than **120,000 records** of Tanzanian citizens. The data includes:
  - full names
  - physical addresses
  - mobile phone numbers
  - cities of residence

  All entries are presented as **active and validated**. The seller claims the data is fresh and operational. The asking price is **$350**, with escrow options available.

- **Analysis:**
  This leak exposes highly precise personally identifiable information (PII), directly exploitable for:
  - **targeted phishing campaigns** against Tanzanian citizens;
  - **telephone scams** (*vishing* or *smishing*) using phone numbers to impersonate contacts;
  - **harassment** or **intimidation** at home, using precise physical addresses;
  - **bank fraud attempts** or **identity theft** to subscribe to financial services.

  The significant volume (120,000+ records) likely covers multiple regions of the country, including Dar es Salaam, Zanzibar, and Kibaha (visible in the sample). The "active" mention suggests the data has recently been verified, increasing its value for cybercriminals and the danger for Tanzanian citizens. The actor XOverStm is also known for other leaks (notably CGCSA in South Africa), which reinforces the credibility of the threat.
---
### May 04, 2026
#### 🇩🇿 Algeria - Ministry of Pharmaceutical Industry [Data Leak]
- **Threat Actor / Group :** kamalsheikhxx
- **Sector:** Government / Administration
- **Status:** Data Fully Published
- **Website :** [miph.gov.dz/](https://miph.gov.dz/)
- **Description :** A cybercriminal forum post claims the leak of approximately 34.3GB of data allegedly linked to the Algerian Ministry of Pharmaceutical Industry, including more than 52,000 files and 17,800 folders covering the 2019-2025 period.
- **Observed data :**
  - drug import reports
  - invoices and customs declarations
  - pharmaceutical commercial registers
  - personal data of company officials
  - official authorizations
  - pharmaceutical inventories
  - psychotropic substance lists
  - PDF, Excel, Word, and ZIP files

#### 🇪🇬 Egypt - Educational & HR Databases
- **Actor / Group:** bigF
- **Sector:** Education / University
- **Status:** Claim - Unverified
- **Website:** [mans.edu.eg](https://www.mans.edu.eg) ; [gu.edu.eg](https://gu.edu.eg)
- **Description:**
  A threat actor claims to possess approximately **37 GB** of databases linked to Egyptian educational institutions and HR systems.
- **Analysis:**
  The published samples reference more than **1.5 million student records** and nearly **60 million records** containing sensitive personal, academic and administrative information:
  ▫️ full names
  ▫️ Egyptian national ID numbers
  ▫️ addresses and contact details
  ▫️ academic information
  ▫️ scanned IDs and passports
  ▫️ HR and payroll data

#### 🇿🇦 South Africa - Standard Bank Group
- **Ransomware group:** PrinzEugen
- **Sector:** Finance / Banking
- **Website:** [www.standardbank.com](https://www.standardbank.com)
- **Status:** Claim - Unverified
- **Description:** Standard Bank Group is one of the largest financial institutions and banking groups on the African continent. On May 4, 2026, the threat actor **PrinzEugen** claimed to hold and leak data associated with the organization.

#### 🇪🇬 Egypt - Luna Group
- **Ransomware group:** Lamashtu
- **Sector:** Industry / Automotive / Manufacturing
- **Website:** [lunagroupeg.com](https://lunagroupeg.com)
- **Status:** Claim - Unverified
- **Description:** Luna Group is a major Egyptian conglomerate primarily engaged in food processing, packaging manufacturing, as well as personal and household care production. On May 4, 2026, the **Lamashtu** ransomware group claimed a compromise of the organization.

---
### May 05, 2026
#### 🇳🇬 Nigeria - ActionAid / TACOSA
- **Ransomware group:** MedusaLocker
- **Sector:** NGO / Social Welfare
- **Website:** [www.actionaid.org](https://www.actionaid.org)
- **Status:** Claim - Unverified
- **Description:** ActionAid is an international non-governmental organization focused on combating poverty and social injustice, operating locally in collaboration with entities such as TACOSA (The ActionAid Community and Social Action). The MedusaLocker ransomware group claimed a compromise of the organization's digital infrastructure, threatening the exposure of sensitive data tied to community development programs and beneficiary information.

---
### May 03, 2026
#### 🇿🇦 South Africa - Consumer Goods Council of South Africa (CGCSA)
- **Ransomware group:** Stormous (XOverStm)
- **Sector:** E-commerce / Retail
- **Website:** [cgcsa.co.za](https://www.cgcsa.co.za)
- **Status:** Claim - Data Sample Published
- **Description :**
  The Stormous group published what it claims to be a data leak originating from the Consumer Goods Council of South Africa (CGCSA), an organization representing the retail, wholesale, and consumer goods sectors in South Africa.
- **Analysis :**
  According to the threat actor, approximately **20 GB of data** was released following the alleged failure of negotiations with the organization.
  The leaked data reportedly includes:
        ▫️ full internal reports
        ▫️ customer databases containing thousands of records
        ▫️ scripts and technical documents
        ▫️ invoices
        ▫️ CEO reports
        ▫️ accounting and financial backups
        ▫️ a full Sage 200 Evolution database (SAGE200EVOSQL)
  The reviewed samples indicate the presence of financial records, accounting information, customer account data, invoices, financial reports, and IT asset inventories linked to CGCSA.
  Exposure of such information could provide threat actors with detailed insight into the organization's financial operations, business relationships, member companies, suppliers, and internal IT environment.
  The leak also appears to contain backups of business and accounting systems that may include sensitive financial information and data related to CGCSA member organizations.

---
### May 05, 2026
#### 🇰🇪 Kenya / 🇪🇹 Ethiopia / 🇳🇬 Nigeria / 🇿🇼 Zimbabwe - Resume docs data leak
- **Actor / Group:** attackercompany (via the [Citizen] forum)
- **Sector:** Human Resources / Recruitment
- **Status:** Claim - Unverified
- **Website:** Not specified (seller contact details intentionally omitted)
- **Description:**
  A cybercriminal claims a massive leak of resume documents (*resume docs*) on a global scale. The data allegedly involves hundreds of thousands of individuals across more than 200 countries.
  African countries explicitly listed in the published count include:
  * 🇰🇪 **Kenya**: 435 records
  * 🇪🇹 **Ethiopia**: 335 records
  * 🇳🇬 **Nigeria**: 332 records
  * 🇿🇼 **Zimbabwe**: 328 records
  The published data sample contains sensitive fields such as:
  - first and last names
  - full postal addresses, cities, and postal codes
  - phone numbers
  - customer IDs and subscription IDs
  - account creation and update timestamps
  - a `country` field (in the sample, `FR` is systematically displayed, suggesting the data may concern African nationals residing in France, or this may be a default value in the database)
- **Analysis:**
- **Analysis:**
  The sample contains detailed personal information, but its African scope relies on the seller’s country attribution while the observed country field displays `FR`.

  **Observed:** structured records with contact and address fields; the sample country field displays `FR`.

  **Assumption:** some records may concern nationals or residents of Kenya, Ethiopia, Nigeria and Zimbabwe, based on the seller’s listing.

  **Unknown:** nationality, residence, collection source and whether the sample belongs to a larger dataset.
---

### May 06, 2026
#### 🇬🇭 Ghana - Kasapreko
- **Ransomware group:** TheGentlemen
- **Sector:** Food / Beverage / Restaurants
- **Website:** [kasapreko.com](https://kasapreko.com)
- **Status:** Claim - Unverified
- **Description:** Kasapreko is one of the leading beverage manufacturers and distributors in Ghana. **TheGentlemen** ransomware group claimed a cyberattack against the company on May 6, 2026.
---
### May 07, 2026
#### 🇪🇬 Egypt - Rhactus Hotel
- **Ransomware group:** LockBit 5.0
- **Sector:** Hospitality / Events
- **Website:** [rhactushotel.com](https://rhactushotel.com)
- **Status:** Claim - Unverified
- **Description:** Rhactus Hotel is a hospitality establishment operating in Egypt. The **LockBit 5.0** ransomware group claimed a compromise of the organization on May 7, 2026.
---
### May 08, 2026
#### 🇪🇬 Egypt - Imex International
- **Ransomware group:** Qilin
- **Sector:** Transport / Logistics
- **Website:** [imex-logistics.com](https://www.imex-logistics.com)
- **Status:** Claim - Unverified
- **Description:** Imex International is an Egyptian firm specializing in international logistics and freight forwarding services. The **Qilin** ransomware group claimed a cyberattack against the organization on May 8, 2026.
---
### May 09, 2026
#### 🇪🇬 Egypt - Misr Chemical Industries (MCI)
- **Ransomware group:** TheGentlemen
- **Sector:** Industry / Automotive / Manufacturing
- **Website:** [mci.com.eg](http://mci.com.eg)
- **Status:** Claim - Unverified
- **Description:** Misr Chemical Industries (MCI) is a major Egyptian industrial player specializing in the manufacture of chemical products. **TheGentlemen** ransomware group claimed a compromise of the company on May 9, 2026.

#### 🇳🇬 Nigeria - MRS Holdings
- **Ransomware group:** KillSec
- **Sector:** Oil & Energy
- **Website:** [www.mrsholdings.com](https://www.mrsholdings.com)
- **Status:** Claim - Unverified
- **Description:** MRS Holdings is a major Nigerian energy conglomerate operating in the oil, gas, and power sectors. The **KillSec** threat group claims possession and publication of exfiltrated data belonging to the organization.

---
### May 10, 2026
#### 🇪🇬 Egypt - Mansoura University
- **Actor / Group:** INT3X
- **Sector:** Education / University
- **Website:** [mans.edu.eg](https://www.mans.edu.eg)
- **Status:** Claim - Unverified
- **Description:**
  Mansoura University is one of the largest and oldest universities in Egypt, hosting a significant volume of student and academic data.
- **Analysis:**
  The threat actor claims to possess more than **10 GB** of leaked data, including approximately **989,000 student records** covering the period from 2012 to 2026, along with internal documents, research materials and student images.
  The exposed data allegedly includes usernames, names, national ID numbers, email addresses, passwords, academic information and internal institutional documents.
  Such exposure could facilitate identity theft, unauthorized access to university accounts, targeted phishing campaigns and password reuse attacks against other institutional services.
  At this stage, this remains a claim published on a cybercriminal forum, and the full authenticity of the leaked dataset has not yet been independently verified.
---
### May 12, 2026
#### 🇲🇦 Morocco - SDTM / Groupe Barid Al-Maghrib
- **Threat Actor / Group :** Sejjil
- **Sector:** Transport / Logistics
- **Targeted Organization :** SDTM - Groupe Barid Al-Maghrib
- **Website :** [groupesdtm.com](https://www.groupesdtm.com/)
- **Status:** Claim - Unverified
- **Description :**  *SDTM* is a logistics subsidiary of Groupe Barid Al-Maghrib specializing in transportation, distribution, fleet management, and operational services supporting postal and financial activities in Morocco.
- **Leak description :**
  On May 12, 2026, the threat actor Sejjil claimed the complete exposure of SDTM’s ERP and financial infrastructure. According to the post, the exposed dataset includes 129 structured CSV files originating from SAGE ERP systems, SMS gateways, banking data, and internal platforms linked to logistics and financial operations.
- **Sample analysis :**
  The analyzed samples contain administrative metadata, ERP user accounts, MD5 password hashes, active session tokens, corporate email addresses, agency-related information, phone numbers, internal financial data, bank account identifiers (RIB), account designations, and customer-related information including national ID references and physical addresses.

#### 🇹🇳 Tunisia - SETCAR
- **Ransomware group:** TheGentlemen
- **Sector:** Industry / Automotive / Manufacturing
- **Website:** [www.setcar.com.tn](https://www.setcar.com.tn)
- **Status:** Claim - Unverified
- **Description:** SETCAR is a Tunisian company specializing in automotive manufacturing, equipment, and services. On May 12, 2026, **TheGentlemen** ransomware group claimed a cyberattack against the organization.

#### 🇪🇬 Egypt - FutureShop [Data Breach / API Exposure]

- **Actor / Group:** cc5ab (forum [Citizen])
- **Sector:** E-commerce / Retail
- **Status:** Claim - Data Sample Published
- **Website:** [futureshop.eg](https://futureshop.eg)
- **Description:**
  Full API exposure without authentication. Total exposed:
  - 3,893 customer records (names, phones, emails, creation dates)
  - 5,181 orders (prices, notes, statuses, timestamps)
  - 2,438 delivery addresses (GPS, landmarks, formatted addresses)
  - 643 store orders (admin panel data)
  - 60 store profiles (business info, contracts, commercial registration documents)
  Exposed S3 bucket: futureshopbucket.s3.eu-west-1.amazonaws.com
- **Analysis:**
  Critical API misconfiguration exposing PII, delivery addresses with GPS, and internal commercial contracts. Enables stalking, physical theft, competitor intelligence, and fraud. The exposed S3 bucket with signed contracts and commercial registrations facilitates corporate espionage and document fraud.
---
### May 13, 2026
#### 🇪🇬 Egypt - Ministry of Education
- **Threat Actor / Group :** Revesky
- **Sector:** Government / Administration
- **Website :** [moe.gov.eg](https://moe.gov.eg/)
- **Status:** Claim - Data Sample Published
- **Victim description :**
  The Egyptian Ministry of Education is the governmental institution responsible for managing the national education system, including schools, student records, teachers, and digital educational platforms. On May 13, 2026, the threat actor *Revesky* claimed the leak of multiple databases totaling approximately 22.6 GB of data related to students, teachers, and administrators.
- **Sample analysis :**
  The published information mentions approximately 26.8 million student records and 3.8 million teacher and administrator records. The actor also claims to possess full administrative privileges allowing management of teacher and student accounts, password resets, modification of administrative information, and access to sensitive educational platform functions.


#### 🇲🇿 Mozambique / 🇱🇷 Liberia / 🇳🇬 Nigeria / 🇹🇬 Togo / 🇸🇱 Sierra Leone - DHIS2 / Ministries of Health

- **Actor / Group:** Keymous
- **Sector:** Government / Administration
- **Targeted Platforms:** DHIS2 (District Health Information System)
- **Website:** Not specified
- **Status:** Claim - Unverified
- **Description:**
  DHIS2 is a widely used open-source platform deployed by Ministries of Health for health data management, epidemic surveillance and vaccination program monitoring.
- **Analysis:**
  The threat actor claims to possess access to multiple DHIS2 instances used by healthcare institutions and Ministries of Health across several African and international countries.
  The published artifacts include multiple **URL / username / password** combinations associated with government health platforms, suggesting a credible compromise of administrative or operational accounts.  The claimed accesses notably involve infrastructures in:
  ▫️🇲🇿 Mozambique
  ▫️🇱🇷 Liberia
  ▫️🇳🇬 Nigeria
  ▫️🇧🇹 Bhutan
  ▫️🇭🇳 Honduras
  ▫️🇹🇬 Togo
  ▫️🇸🇱 Sierra Leone
AFRINTEL geographic scope: Mozambique, Liberia, Nigeria, Togo and Sierra Leone are included in African statistics. Bhutan and Honduras are retained as source context but excluded from AFRINTEL country counts.

Such a compromise could potentially allow:
  ▫️ unauthorized access to national health data
  ▫️ manipulation or deletion of epidemiological information
  ▫️ compromise of vaccination tracking systems
  ▫️ exfiltration of medical and administrative data
  ▫️ disruption of public health operations
  AFRINTEL did not perform any authentication attempts in order to avoid unauthorized interaction with the affected systems.
---
### May 15, 2026

#### 🇪🇹 Ethiopia - NGO Registration Database [Data Leak / Sale]
- **Actor / Group:** 404Crew Cyber Team (forum [Citizen])
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** [csogov.et] (government agency for NGO registration and audit)
- **Description:**
  Sale of a full database from Ethiopia’s official NGO registration and auditing agency. The dataset contains **3,668 records** of registered civil society organizations. Each record includes the organization’s English and Amharic names, registration date, certificate number, category (Local Organization), type (Charitable Association, Professional Association, etc.), head office address, and contact email.
- **Analysis:**
  Exposure of the entire civil society registry compromises sensitive operational data of NGOs, including their leadership contacts and locations. This enables targeted phishing, physical harassment, and espionage against humanitarian organizations. The data also reveals government oversight structures, potentially facilitating attacks on regulatory bodies.

#### 🇿🇦 South Africa - Ephraim Mogale Local Municipality
- **Actor / Group:** NullSec Nigeria x 404Crew Cyber Team x Infernalis
- **Sector:** Government / Administration
- **Website:** [ephraimmogalelm.gov.za](https://www.ephraimmogalelm.gov.za)
- **Status:** Claim - Unverified
- **Description:**
  Ephraim Mogale Local Municipality is a South African local government authority responsible for public administration, municipal services management, and local development within Limpopo Province.
- **Analysis:**
  The threat actors claim to have compromised the municipality’s website and related systems. The published samples contain internal administrative documents, official correspondence, and records associated with municipal operations. The attackers allege possession of approximately **111 GB** of data and released a limited sample to support their claim. Such exposure could lead to the disclosure of sensitive administrative information, facilitate social engineering activities, and provide valuable intelligence regarding the municipality’s internal operations. At this stage, the full scope and authenticity of the alleged compromise have not been independently verified.


#### 🇿🇦 South Africa - Bellavista School
- **Actor / Group:** 404Crew Cyber Team
- **Sector:** Education / University
- **Website:** [bellavista.org.za](https://www.bellavista.org.za)
- **Status:** Claim - Data Sample Published
- **Description:**
  Bellavista School is a South African educational institution specializing in learning support and educational assistance for students with specific learning needs.
- **Analysis:**
  A threat actor published a dataset sample allegedly originating from Bellavista School's website.
  The exposed sample contains personal information associated with registered users of the school's online platform. Visible records include usernames or identifiers, first names, surnames, email addresses, registration timestamps, phone numbers, and various account-related administrative fields.
  Several email addresses belong to educational, school-related, and personal domains, suggesting the presence of students, parents, teachers, and administrative staff within the dataset.
  The registration dates visible in the sample span multiple years, indicating that historical user records may have been exposed.
  Such information could be leveraged for targeted phishing campaigns against families and educational staff, identity impersonation attempts, or social engineering operations aimed at educational institutions.
  The published sample demonstrates the exposure of personal information and provides a credible indication of unauthorized access to a database associated with the school.

#### 🇪🇬 Egypt - Baitzakat.org.eg [Data Leak]
- **Actor / Group:** DR-X-LOL (forum [Citizen])
- **Sector:** NGO / Social Welfare
- **Status:** Claim - Data Sample Published
- **Website:** [baitzakat.org.eg](https://baitzakat.org.eg)
- **Description:**
  Leak of over **300,000 Egyptian citizen records** from a zakat (charity) organization. Exposed data includes National ID, phone numbers, government affiliation, full names, and email addresses. No asking price mentioned; likely a public dump.
- **Analysis:**
  Extremely sensitive exposure: National IDs are irreversible identifiers enabling identity theft, government impersonation, KYC bypass, and financial fraud. The inclusion of "Government" affiliation suggests many victims are public servants or officials, amplifying national security risks. The charity sector's trust is severely damaged.
---
### May 16, 2026
#### 🇪🇬 Egypt - Professional Academy for Teachers (PAT)
- **Threat Actor / Group :** INT3X
- **Sector:** Government / Administration
- **Targeted Organization :** Professional Academy for Teachers (PAT)
- **Website :** [pat.edu.eg](https://pat.edu.eg)
- **Status:** Claim - Data Sample Published
- **Victim description :**
  The Professional Academy for Teachers (PAT), an Egyptian institution linked to the Ministry of Education responsible for teacher accreditation, training, and educational management, was claimed by the threat actor INT3X.
  The actor claims to possess between 8 and 10 GB of compressed data and more than 80 GB of uncompressed files, including information related to approximately 1.2 million teachers, STEM students, academic content, MSSQL backups, Microsoft Access databases, identity photographs, and administrative records.
- **Sample analysis :**
  The exposed samples contain structured datasets including full names, phone numbers, email addresses, national identification numbers, teacher codes, job positions, teaching subjects, schools, regional education offices, grade levels, and internal administrative information.


#### 🇿🇦 South Africa - Department of Correctional Services (DCS)
- **Actor / Group:** NullSec Nigeria x 404Crew Cyber Team x Infernalis
- **Sector:** Government / Administration
- **Website:** [dcs.gov.za](https://www.dcs.gov.za)
- **Status:** Claim - Unverified
- **Description:**
  The Department of Correctional Services (DCS) is the South African government agency responsible for correctional facilities, inmate rehabilitation, and prison administration nationwide.
- **Analysis:**
  The group claims to have compromised the Department of Correctional Services as part of its "OpSouthAfrica" campaign.
  The published samples appear to contain authentic DCS administrative documents, including procurement-related communications and an official media statement issued by the National Commissioner regarding educational examinations conducted within correctional facilities.
  The disclosed documents contain administrative contact details, institutional information, and internal operational content related to the department's activities.
  Based on the available evidence, the incident currently appears to involve the disclosure of internal documents rather than a large-scale compromise of information systems or a significant exposure of personal data.
  The publication is presented as part of a politically motivated campaign linked by the threat actors to xenophobia-related grievances.

#### 🇰🇪 Kenya - Land Surveyors Board of Kenya (LSB)
- **Actor / Group:** cc5ab
- **Sector:** Government / Administration
- **Status:** Claim - Unverified
- **Website:** [lsb.go.ke](https://www.lsb.go.ke)
- **Description:**
  A threat actor claims to have compromised the Land Surveyors Board of Kenya (LSB), the Kenyan government body responsible for regulating and licensing land surveyors.
- **Analysis:**
  According to the published claim, multiple categories of personal and technical data were allegedly exposed.
  The reported exposure includes:
         -▫️175 licensed surveyors containing full names, personal email addresses, postal addresses, company affiliations, license numbers and licensing status
         -▫️730 approved survey assistants including full names, national ID numbers, registration numbers and supervising surveyor information
         -▫️ additional personally identifiable information exposed through verification endpoints, including phone numbers and identification records
        -▫️complete API documentation detailing endpoints, request parameters and authentication mechanisms
        -▫️ access to a Django administration login panel
        -▫️ disclosure of sensitive configuration information including PostgreSQL settings, application accounts, email configuration and JWT-related settings
        -▫️ complete application URL routing structure exposing the platform architecture
        -▫️ more than 45 official government documents related to land legislation, cadastral regulations and surveying procedures
  This claim is significant because it allegedly involves not only personal information but also technical infrastructure details that could facilitate future attacks against the organization.
  The exposure of national identification data combined with professional records could increase the risk of identity theft, document fraud and targeted social engineering campaigns.

 ---
### May 17, 2026
#### 🇿🇦 South Africa - Statistics South Africa (Stats SA)
- **Actor / Group:** Kazu
- **Sector:** Government / Administration
- **Website:** [statssa.gov.za](https://www.statssa.gov.za/)
- **Status:** Claim - Data Sample Published
- **Description:** Statistics South Africa (Stats SA) is the official South African government agency responsible for collecting, processing and publishing national demographic, economic and social statistics.
- **Analysis:**  The threat actor claims to possess approximately **154 GB** of data containing more than **453,000 files** allegedly linked to Stats SA. Shared samples include:
  - South African identity cards
  - Academic transcripts and certificates
  - CVs containing personal information
  - Census and fieldworker-related documents
  - Administrative and educational records

#### 🇲🇦 Morocco - Multiple Moroccan Government Platforms
- **Threat Actor / Group :** superstarkmc
- **Sector:** Government / Administration
- **Websites :**  [men.gov.ma](https://www.men.gov.ma) ; [tax.gov.ma](https://www.tax.gov.ma) ; [tgr.gov.ma](https://www.tgr.gov.ma)
- **Status:** Claim - Data Sample Published
- **Victim description :**  Multiple Moroccan government platforms related to education, taxation, treasury services, culture, justice, transport, and administrative services were referenced in a post claiming a large-scale credential leak. Mentioned domains include Massar, Moutamadris, Waliye, Tax.gov.ma, TGR, and several Moroccan administrative platforms.
  The threat actor claims to possess approximately 827,000 lines of data (~16 MB) and offers the access for sale.
- **Sample analysis :**  The exposed data contains hundreds of credentials linked to Moroccan government services, including *@taalim.ma* email accounts, usernames, plaintext passwords, tax portals, educational administrative systems, HR services, recruitment platforms, school management portals, treasury services, and road infraction systems. Several entries appear to expose access to sensitive financial, educational, and administrative services.
---
### May 18, 2026
#### 🇹🇳 Tunisia - CRIT Tunisie
- **Ransomware group:** Titan
- **Sector:** Human Resources / Recruitment
- **Website:** [www.crit-tunisie.net](https://www.crit-tunisie.net)
- **Status:** Claim - Unverified
- **Description:** CRIT Tunisie is a subsidiary of the French CRIT Group, specializing in human resources, permanent and temporary employment (CDI/CDD), and workforce placement. Operating in Tunisia to support local and international businesses, the company manages sourcing, selection, and staffing solutions across key industry sectors including manufacturing, logistics, services, and customer relations. The **Titan** ransomware group claimed a compromise of the organization on May 18, 2026.

#### 🇸🇳 Senegal - Trésor Public du Sénégal
- **Ransomware group:** AuditTeam
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** [www.tresor.sn](https://www.tresor.sn)
- **Description:**
  The Trésor Public du Sénégal is the state institution responsible for managing public finances, executing the national budget, and overseeing tax collection and government expenditure. The **AuditTeam** ransomware group claimed the compromise of the institution on May 17-18, 2026. The analysed files were presented as originating from two internal systems and contain dates preceding the public claim. The duration and method of access remain unknown.
- **Analysis:**
  The analysed files were presented as data extracted from two internal systems. They do not independently establish the complete intrusion sequence or ransomware deployment.
  **Analysed database material:** Three database dumps were extracted on May 9, 2026:
  - personnel and payroll dataset (~40,394 records): government personnel and payroll registry. Fields include employee identifiers, names, phone numbers, bank details (bank code, branch, account number, RIB), service codes, management year, and salary amounts.
  - taxpayer and debtor dataset (~960,146 records): national taxpayer and debtor registry. Fields include taxpayer ID (N_C_CONTRIB), full name or business denomination, address, phone number, and business registration number. Data spans from 2017 onwards.
  - public payment-order dataset (~659,195 records): complete public payment order database. Fields include mandate number, date, transaction purpose, amount (with and without VAT), beneficiary bank details (bank code, branch, account number, RIB), beneficiary name, NINEA (Numéro d'Identification Nationale des Entreprises et Associations), and operation description. Data covers at least April 2024 through extraction date.
  **Analysed payroll and salary-management material:** Operational files spanning January 2, 2025 to May 8, 2026 (18 months of financial operations) were extracted, including:
  - Government salary batch files for March 2026 by geographic region.
  - Wire transfer files (virement) dated May 8, 2026 in bank-standard CSV format (bank code, branch, account number, RIB, amount, beneficiary name, operation label). Types observed include salary payments, exam correction allowances, and supply purchases. The dates show that the files contain recent operational information, but do not independently confirm live system access on that date.
  - Payment mandate files (MD26-XXXXXX series) documenting individual payroll authorizations.
  - Exam allowance transfers (CFEE 2025) linking the Trésor system to national primary education examination payment flows.
  Total records represented in the analysed material: approximately **1,659,735 database entries** across three tables, plus 323 days of SICA financial operation files.
  **CTI observations:**
  - The dates visible in the databases and SICA activity files precede the AuditTeam public claim by approximately nine days. This indicates that the material presented as exfiltrated predates the publication, but does not confirm the duration of access, encryption or the complete incident sequence.
  - The taxpayer and debtor dataset (~960,146 records) presents a high-sensitivity exposure involving a public financial institution in West Africa.
  - The public payment-order dataset exposes NINEA identifiers and banking coordinates of all government suppliers and contractors, creating significant risk of supplier fraud, BEC (Business Email Compromise), and targeted financial social engineering against the public sector supply chain.
  - Salary and wire transfer data (employee bank accounts, amounts, identities) enables direct financial fraud targeting public sector employees.
  - The presence of CFEE exam allowance transfers in the SICA material indicates an inter-institutional dependency involving Ministry of Education payment flows.
  - **Confidence level: High. Impact level: Level 4** (critical national financial infrastructure and large-scale exposure of sensitive financial and identity data).

#### 🇪🇬 Egypt / 🇱🇾 Libya - Passport Scans [Data Leak]
- **Actor / Group:** raylie (forum [Citizen])
- **Sector:** Government / Administration
- **Status:** Data Fully Published
- **Website:** Not applicable (download link omitted)
- **Description:**
  Public leak of scanned passport pages from over 20 countries. African countries affected: **Egypt** and **Libya**. Other countries include Azerbaijan, Australia, Bosnia, China, Colombia, Iran, Iraq, Israel, Japan, Jordan, Kuwait, Norway, Saudi Arabia, South Korea, Sweden, Tajikistan, USA, Venezuela.
- **Analysis:**
  The observed passport scans present a high risk of identity theft, document fraud and targeted impersonation. AFRINTEL does not reproduce the documents or personal identifiers. The source and date of collection remain unknown.
---
### May 19, 2026
#### 🇩🇿 Algeria - OGEBC (National Cultural Asset Management) [Database Leak / Sale]
- **Actor / Group:** Databasehooligan (via the [Citizen] forum)
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** [www.ogebc.com](https://www.ogebc.com)
- **Description:**
  A cybercriminal is offering for sale a complete database originating from the official website of Algeria's **Office de Gestion des Biens Culturels (OGEBC)**. The dataset allegedly contains **425,000 records** structured into three main sections:
  1. **Customers**: contact and account information (names, emails, phones, fax, postal addresses, country, account status, customer segment, revenue, credit limits, etc.)
  2. **Order History**: purchase details, shipping tracking, amounts, payment methods, invoices, discounts, follow-up notes
  3. **Support Tickets**: interaction history, customer cases, priorities, descriptions, assigned agents, satisfaction ratings

  The data is presented as fresh and well-organized. The asking price is **$900**, with escrow options available.

- **Analysis:**
  This leak is particularly sensitive as it concerns a public institution responsible for managing Algeria's **cultural heritage**. The exposure of 425,000 records containing detailed personal data (identities, contact details, purchase and support histories) presents major risks:
  - **Identity theft** and **administrative fraud** using the personal information of citizens and cultural sector professionals;
  - **Targeted social engineering** against managers, artists, curators, or suppliers of the Ministry of Culture;
  - **Economic espionage** on financial flows, orders, and business relationships of the institution;
  - **Phishing** campaigns targeting registered contacts (clients, suppliers, partners) by exploiting the institution's legitimacy.

  The highly structured nature of the data (including internal notes and support tickets) suggests deep access to the organization's internal systems. The sale of this data could compromise not only citizens' privacy but also the security of the Office's operations and public trust in Algeria's cultural institutions.
---
### May 20, 2026
#### 🇲🇦 Morocco - Watiqa.ma
- **Actor / Group:** JBT2026
- **Sector:** Government / Administration
- **Website:** [watiqa.ma](https://www.watiqa.ma)
- **Status:** Claim - Unverified
- **Description:**  Watiqa.ma is the official Moroccan platform allowing citizens to request civil registry and administrative documents online.
- **Analysis:**   The threat actor claims to possess approximately **695,400 records** containing sensitive personal and family-related information, including names, birth dates, addresses, phone numbers and civil registry details.
  The exposed data could potentially be used for identity theft, administrative fraud, targeted phishing campaigns and social engineering operations targeting Moroccan citizens.
---
### May 21, 2026
#### 🇲🇦 Morocco - Avito.ma
- **Actor / Group:** fexus
- **Sector:** E-commerce / Retail
- **Website:** [avito.ma](https://www.avito.ma)
- **Status:** Claim - Data Sample Published
- **Description:**  Avito.ma is one of Morocco’s leading online marketplace and classified advertisement platforms, widely used by individuals and businesses.
- **Analysis:**
  The threat actor claims to possess leaked Avito.ma user data, including email addresses, phone numbers, cities and passwords.
  The published samples contain several profiles linked to the real estate sector (“Crédit Immobilier”) with Moroccan personal data associated with cities such as Casablanca, Khouribga, Kénitra, Guelmim and Oued Zem.
  The exposed passwords appear to be stored in plaintext or reused credentials, significantly increasing the risks of:
  ▫️ account compromise
  ▫️ credential stuffing attacks
  ▫️ targeted phishing campaigns
  ▫️ fraud and identity theft
  ▫️ attacks against other services using the same credentials
AFRINTEL did not conduct any authentication attempts or interaction with the affected systems.
---
### May 22, 2026
#### 🇲🇦 Morocco - Spacex.ma
- **Actor / Group:** DarkMafiaX
- **Sector:** E-commerce / Retail
- **Website:** [spacex.ma](https://spacex.ma)
- **Status:** Claim - Data Sample Published
- **Description:**
  Spacex.ma is presented as a Moroccan online store platform.
- **Analysis:**
  The threat actor publicly shared a suspected administrative access to the website, including an admin panel URL along with a username and password associated with an “admin” account.
  Such exposure could potentially allow:
  ▫️ takeover of the administration panel
  ▫️ website content modification
  ▫️ access to customer and order data
  ▫️ deployment of malicious content or phishing pages
  ▫️ compromise of the underlying web infrastructure
AFRINTEL did not perform any authentication attempts in order to avoid unauthorized interaction with the affected systems.

#### 🇹🇿 Tanzania - Police (Webmail) [Database Leak / Sale]

- **Actor / Group:** [Citizen] Kampuchean
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** [tpf.go.tz](https://tpf.go.tz)

- **Description:**
  A cybercriminal is offering for sale the complete webmail database of the Tanzanian police, corresponding to the `tpf.go.tz` domain. The dataset contains over **10,000 full police email accounts**, including plaintext (dehashed) passwords and their hashes. The asking price is **$550**, with negotiation and escrow options available.

- **Analysis:**
- **Analysis:**
  If the advertised credentials were valid at the time of observation, they could support impersonation, phishing and unauthorized access attempts. AFRINTEL did not test the credentials. Their validity, origin, reuse and remediation status remain unknown.
---

---
#### 🇲🇦 Morocco - RADEM Meknès [Massive data leak - Critical infrastructure]
- **Actor / Group:** anisanas2
- **Sector:** Oil & Energy
- **Status:** Claim - Data Sample Published
- **Website:** [www.radem.ma](http://www.radem.ma)
- **Description:**
  The actor claims to have extracted nearly **1.1 million documents** attributed to RADEM, the public water and electricity utility serving Meknès and surrounding municipalities. An initial batch of approximately **18,000 PDF documents** was published. The observed material includes customer information and operational records related to utility services.
- **Analysis:**
  The observed publication creates risks of phishing, identity fraud and exposure of operational information.

  **Observed:** an initial document batch attributed to RADEM, including customer and operational information.

  **Assumption:** the publication may form part of a pressure or monetisation strategy.

  **Unknown:** initial access vector, operational impact, complete claimed volume, remediation status and institutional response.
---
### May 23, 2026
#### 🇿🇦 South Africa - SITA (State Information Technology Agency)
- **Actor / Group:** NullSec Nigeria x NullSec Philippines
- **Sector:** Government / Administration
- **Website:** [sita.co.za](https://www.sita.co.za)
- **Status:** Claim - Unverified
- **Description:**
  The State Information Technology Agency (SITA) is South Africa’s government IT agency responsible for delivering information technology services and digital infrastructure to public sector institutions.
- **Analysis:**
  The threat actors claim to have compromised SITA and published a sample of data allegedly originating from the organization. According to the post, the exposed information includes usernames, Gmail addresses, passwords (both hashed and potentially plaintext), and platform access-related information.
  If authentic, such exposure could facilitate account compromise attempts, targeted phishing campaigns, credential reuse attacks, and unauthorized access to government-related systems.


#### 🇿🇦 South Africa - South African Revenue Service (SARS)

- **Actor / Group:** NullSec Nigeria x NullSec Philippines
- **Sector:** Government / Administration
- **Website:** [sars.gov.za](https://www.sars.gov.za)
- **Status:** Claim - Unverified
- **Description:**
  The South African Revenue Service (SARS) is South Africa's national tax authority, responsible for tax collection, customs administration, and fiscal services.
- **Analysis:**
  The threat actors claim to have compromised SARS and obtained data containing email addresses, passwords, and credentials allegedly associated with SARS-related portals.
  The shared sample contains multiple **email/password combinations** linked to SARS login URLs. However, the observed email addresses primarily belong to third-party international organizations and do not, by themselves, demonstrate a direct compromise of SARS systems.
  At this stage, the dataset could originate from credential-stuffing collections, infostealer logs, or other previously compromised credential sources that have been contextualized as SARS-related data. Additional technical validation would be required to verify the true origin of the records.
  The publication remains a claim posted on a cybercriminal forum, and the authenticity, scope, and actual impact of the alleged compromise have not been independently confirmed.
---
### May 24, 2026
#### 🇪🇬 Egypt - Papa John's Egypt
- **Ransomware group:** NightSpire
- **Sector:** Food / Beverage / Restaurants
- **Website:** [www.papajohnsegypt.com](https://www.papajohnsegypt.com)
- **Status:** Claim - Unverified
- **Description:** Papa John's Egypt operates the local franchise of the international fast-food restaurant chain. On May 24, 2026, the **NightSpire** ransomware group claimed a compromise of the organization's systems.

#### 🇪🇬 Egypt - Rawaj Consumer Finance
- **Ransomware group:** NightSpire
- **Sector:** Finance / Banking
- **Website:** [www.rawaj-finance.com](https://www.rawaj-finance.com)
- **Status:** Claim - Unverified
- **Description:** Rawaj Consumer Finance is an established financial institution specializing in consumer credit and financing in Egypt. The **NightSpire** ransomware group claimed a cyberattack against the company on May 24, 2026.


#### 🇿🇦 South Africa - CERVI My Private Care

- **Actor / Group:** 404Crew Cyber Team
- **Sector:** Healthcare / Medical
- **Website:** [cervi.co.za](https://www.cervi.co.za)
- **Status:** Claim - Data Sample Published
- **Description:**
  CERVI My Private Care is a South African digital healthcare platform used to manage and coordinate healthcare professionals, pharmacies, clinics, and other medical service providers.
- **Analysis:**
  A threat actor published a dataset sample allegedly originating from the CERVI platform.
  The exposed sample contains detailed information relating to healthcare professionals and medical facilities across multiple South African provinces.
  The leaked records appear to include names, Board of Healthcare Funders (BHF) practice numbers, business addresses, phone numbers, email addresses, tax-related information, and banking details associated with healthcare organizations.
  The available evidence suggests the exposure of a centralized database containing information about healthcare providers connected to the platform.
  Such a leak could facilitate financial fraud, healthcare provider impersonation, Business Email Compromise (BEC) attacks, payment diversion schemes involving bank account manipulation, and targeted phishing campaigns against organizations operating within the healthcare sector.
  The exposed information is consistent with the platform's business model and indicates the disclosure of sensitive operational data belonging to South Africa's healthcare ecosystem.


#### 🇿🇦 South Africa - mevent.
- **Actor / Group:** 404Crew Cyber Team
- **Sector:** Hospitality / Events
- **Website:** [mevent.co.za](https://www.mevent.co.za)
- **Status:** Claim - Data Sample Published
- **Description:**
  mevent. is a South African company specializing in event management, business travel, conferences, and MICE (Meetings, Incentives, Conferences & Events) services.
- **Analysis:**
  A threat actor published a dataset sample allegedly originating from the organization.
  The exposed records contain names, phone numbers, locations, and multiple references to healthcare professionals identified as "Clinic Nurse Practitioner".
  Observed locations include healthcare-related sites across South Africa, including Sandton, Ballito, Bedford Square, Athol Oaklands, and Baywest Mall.
  The available sample appears more consistent with a professional contact database, healthcare staffing platform, or appointment-management system than with a traditional event management database.
  Such exposure could facilitate targeted phishing campaigns, professional impersonation attempts, and the collection of information related to healthcare personnel and their contact details.


#### 🇿🇦 South Africa - Sheriff Randburg West
- **Actor / Group:** 404Crew Cyber Team
- **Sector:** Government / Administration
- **Website:** [sheriffrandburgwest.co.za](https://www.sheriffrandburgwest.co.za)
- **Status:** Claim - Data Sample Published
- **Description:**
  Sheriff Randburg West is an official South African sheriff's office responsible for the enforcement of court orders, service of legal documents, and other judicial procedures.
- **Analysis:**
  A threat actor published a dataset sample allegedly originating from the Sheriff Randburg West website.
  The exposed sample contains personal information relating to individuals who interacted with the organization's website or services. The leaked records include full names, email addresses, and mobile phone numbers.
  Several dozen records are visible in the published sample, including Gmail, Outlook, iCloud, and corporate email addresses belonging to various South African organizations.
  The consistency and structure of the exposed information suggest the compromise of a contact database or online submission system used by citizens, clients, or business partners.
  Such information could be leveraged for targeted phishing campaigns, identity impersonation attempts, telephone fraud (vishing), or social engineering operations abusing the trust associated with judicial institutions.
  The published records show personal information attributed to Sheriff Randburg West; the acquisition method and full scope remain unknown.

#### 🇪🇬 Egypt - Wuzzuf.net [Database Leak / Sale]
- **Actor / Group:** Databasehooligan (forum [Citizen])
- **Sector:** Human Resources / Recruitment
- **Status:** Claim - Data Sample Published
- **Website:** [www.wuzzuf.net](https://www.wuzzuf.net)
- **Description:**
  Sale of a database from Egypt's leading job platform Wuzzuf.net, containing approximately **672,000 records** structured into three sections:
  - **Contacts**: job seekers' personal data (names, emails, phones, addresses, birth dates, gender, LinkedIn, Twitter, etc.).
  - **Job Applications**: application history, job titles, universities, graduation years, interview schedules, recruiter notes, etc.
  - **Authentication Records**: identity verification data (ID numbers, document images, verification videos, risk scores, device info, etc.).
  Asking price: **$1,100**.
- **Analysis:**
  The identity-verification fields described in the sample create a high risk of identity theft, document fraud and targeted social engineering. AFRINTEL does not confirm the complete dataset, its acquisition method or the validity of every record.
---
### May 26, 2026
#### 🇪🇬 Egypt - B Investments (Basata / Basatamfi)
- **Ransomware group:** NightSpire
- **Sector:** Finance / Banking
- **Website:** [www.binvestmentsegypt.com](https://www.binvestmentsegypt.com)
- **Status:** Claim - Unverified
- **Description:**  **B Investments Holding** is a prominent Egyptian private equity and venture capital firm listed on the Egyptian Exchange (EGX), managing a diversified portfolio that includes *Basata Financial Holding* (fintech and e-payment services). The organization's digital infrastructure (associated with the `binvestmentsegypt.com` domain) was targeted by the **NightSpire** ransomware group, which officially listed the entity on its data leak site.

---
### May 27, 2026
#### 🇹🇳 Tunisia - Keejob

- **Actor / Group:** Databasehooligan
- **Sector:** Human Resources / Recruitment
- **Status:** Claim - Data Sample Published
- **Website:** [keejob.com](https://www.keejob.com)
- **Description:**
  A threat actor is offering for sale, for **$ 1,400**, a database allegedly associated with the Tunisian recruitment platform Keejob. According to the advertisement, the dataset contains approximately **137,000 records** related to contacts, email campaigns, and job applications.

- **Analysis:**
  The published samples contain personal and professional information including names, email addresses, phone numbers, job application details, cover letters, positions applied for, salary expectations, recruitment-related records, as well as email campaign and tracking information. The actor further claims that the complete dataset contains direct contact details, project descriptions, and financial information.


#### 🇹🇳 Tunisia - MyTelnet
- **Actor / Group:** Databasehooligan
- **Sector:** Telecommunications
- **Status:** Claim - Data Sample Published
- **Website:** [mytelnet.tn](https://www.mytelnet.tn)
- **Description:**  A cybercriminal is offering for sale a database allegedly originating from Tunisian ISP MyTelnet for **USD 1,100**. According to the advertisement, the dataset contains customer information, product usage profiles, and detailed demographic records related to subscribers.
- **Analysis:**
  The published samples indicate the presence of personal and marketing-related information including names, email addresses, phone numbers, physical addresses, ages, genders, usernames, login-related information, subscribed products, usage history, access levels, loyalty points, customer preferences, and demographic data such as marital status, number of children, education level, employment status, and income categories. The threat actor further claims that the full database includes CRM-related information and detailed customer profiles used for marketing and commercial activities.

---
### May 27, 2026
#### 🇿🇦 South Africa - MIDAS

- **Actor / Group:** Databasehooligan
- **Sector:** Industry / Automotive / Manufacturing
- **Website:** [midas.co.za](https://www.midas.co.za)
- **Status:** Claim - Data Sample Published
- **Description:**
  MIDAS is a South African company specializing in automotive parts distribution, accessories, and logistics solutions for businesses and consumers.
- **Analysis:**
  The threat actor claims to be selling a database containing approximately **463,000 records** originating from MIDAS customer relationship management and business operation systems.

  According to the advertisement, the dataset is structured around three main categories: **CustomerContact**, **DeliveryAddress**, and **SalesOrder**. The exposed information allegedly includes customer contact details, delivery addresses, phone numbers, email addresses, VAT numbers, business information, account status data, orders, payments, invoices, and logistics records.

  Such exposure could facilitate targeted phishing campaigns, business fraud, customer impersonation, and intelligence gathering on the organization's operations and supply chain activities.
  The dataset is offered for sale for **USD 1,100** on a cybercriminal forum. At this stage, the authenticity and full scope of the leaked data have not been independently verified.

### May 27, 2026
#### 🇿🇦 South Africa - Wanderers Club

- **Actor / Group:** Databasehooligan
- **Sector:** Sports / Federations
- **Website:** [wanderers.co.za](https://www.wanderers.co.za)
- **Status:** Claim - Data Sample Published

- **Description:**
  The Wanderers Club is one of South Africa’s leading sports and recreational clubs, offering a wide range of sporting activities, memberships, and events for its members.

- **Analysis:**
  The threat actor claims to be selling a database containing approximately **674,000 records** originating from the club’s membership and event management systems.

  According to the advertisement, the dataset is organized into three main categories: **Contacts**, **Sports Memberships**, and **Event Bookings**. The exposed information allegedly includes member contact details, phone numbers, email addresses, membership categories, membership status information, sports activity history, payment-related data, and event booking records.

  Such exposure could facilitate targeted phishing campaigns, member impersonation, payment fraud, and intelligence gathering on member activities and participation patterns.

  The dataset is offered for sale for **USD 1,400** on a cybercriminal forum. At this stage, the authenticity and full scope of the leaked data have not been independently verified.


#### 🇿🇦 South Africa - Telkom

- **Actor / Group:** Databasehooligan
- **Sector:** Telecommunications
- **Website:** [telkom.co.za](https://www.telkom.co.za)
- **Status:** Claim - Data Sample Published
- **Description:**
  Telkom is one of South Africa’s leading telecommunications operators, providing fixed-line, mobile, broadband, fiber, and digital services to both residential and business customers.
- **Analysis:**
  The threat actor claims to be selling a database containing approximately **742,000 records** associated with Telkom customers.

  According to the advertisement, the dataset is structured around three main categories: **Contacts**, **Subscription Contracts**, and **Support Tickets**. The exposed information allegedly includes customer personal data (names, email addresses, phone numbers, dates of birth, national identification numbers), contract details, billing information, account balances, and customer support interaction records.

  Such exposure could facilitate targeted phishing campaigns, identity theft, subscription fraud, technical-support scams, and intelligence gathering on customers and their subscribed services.

  The database is being offered for sale for **USD 900** on a cybercriminal forum. At this stage, the authenticity and full scope of the claimed dataset have not been independently verified.
---
### May 28, 2026
#### 🇪🇬 Egypt - Citex Systems
- **Actor / Group:** Keymous
- **Sector:** Telecommunications
- **Website:** [citexltd.com](https://www.citexltd.com)
- **Status:** Claim - Unverified
- **Description:**  Citex Systems is an Egyptian telecommunications and ICT company providing network infrastructure, fintech solutions and technology services.
- **Analysis:**
  The threat actor claims to have obtained access to multiple internal company databases, including employee records, project management information and corporate mailing data.
  Published samples reportedly contain:
  ▫️ employee names and business contact information
  ▫️ corporate email addresses
  ▫️ internal roles and job positions
  ▫️ HR-related employee data
  ▫️ project management and operational records
  Such exposure could facilitate social engineering, targeted phishing, corporate impersonation and intelligence gathering on the company's internal operations.

#### 🇨🇮 Ivory Coast - Mayelia Automotive
- **Ransomware group:** TheGentlemen
- **Sector:** Industry / Automotive / Manufacturing
- **Website:** [www.mayelia.com](https://www.mayelia.com)
- **Status:** Claim - Unverified
- **Description:** Mayelia Automotive is an Ivorian company specializing in vehicle inspections and automotive-related services. On May 28, 2026, **TheGentlemen** ransomware group claimed a cyberattack against the organization, publishing exfiltrated data on its leak site.

#### 🇳🇬 Nigeria - XL Africa Group
- **Ransomware group:** 0day Syndicate
- **Sector:** Business Services
- **Website:** [xlafricagroup.com](https://www.xlafricagroup.com)
- **Status:** Claim - Unverified
- **Description:** XL Africa Group is a Nigerian diversified services conglomerate founded by Charles Nwodo Jr., specializing in B2B outsourcing services including human resources management, security, logistics and transport, facility management, and treasury services. The group operates beyond Nigeria, with a presence in Ghana, Liberia, Sierra Leone, and the United States. On May 28, 2026, the **0day Syndicate** group claimed a compromise of the organization's infrastructure on its dedicated leak platform.
---
### May 31, 2026
#### 🇹🇳 Tunisia - OptionCarriere.tn [Database Leak / Sale]
- **Actor /Group:** Databasehooligan (forum [Citizen])
- **Sector:** Human Resources / Recruitment
- **Status:** Claim - Data Sample Published
- **Website:** [www.optioncarriere.tn](https://www.optioncarriere.tn)
- **Description:**
  Sale of a database from the Tunisian platform OptionCarriere.tn, containing approximately **274,000 records** structured into three sections:
  - **Contacts** (job seekers): names, emails, phones, addresses, date of birth, gender, LinkedIn profiles, etc.
  - **Job Applications**: history, dates, cover letters.
  - **Employers**: information on recruiting companies.
  Asking price: **$1,300**.
- **Analysis:**
  Massive exposure of sensitive personal data. Key risks: identity theft, employment fraud, targeted phishing, and social engineering against companies. The presence of fields such as LinkedIn, date of birth, and emergency contact makes this database particularly dangerous. The platform risks loss of trust and potential legal consequences.

#### 🇲🇦 Morocco - Massive sale of Moroccan databases [Data leak / Put up for sale]

- **Actor / Group:** anisanas2 (BreachForums / Telegram)
- **Sector:** Government / Administration
- **Status:** Claim - Unverified
- **Website:** Multiple entities (see description)
- **Description:**
  An actor offering for sale a collection of stolen Moroccan databases, representing a combined total of over **12 million lines and documents**. The data, attributed to anisanas2, covers several sensitive sectors. Global offer at **5,500 USD** or sold individually:

  **Government entities:**
  - **Ministry of Justice:** 2 million documents / 150,000 court files - 3,000 USD.
  - **NARSA** (National Road Safety Agency): 2 million lines - 800 USD.
  - **RADEM Meknès** (Water and electricity utility): 1.1 million documents - 600 USD.
  - **OFPPT** (Vocational Training Office): 400,000 lines - 300 USD.
  - **LNM6** (unidentified institution): 95,000 documents - 500 USD.

  **Private companies:**
  - **Delivery companies:** 8 million lines - 1,800 USD.
  - **Insurance company:** initial access - 600 USD.
  - **Other companies:** 500,000 lines - 350 USD.

- **Analysis:**
  This sale concerns both government institutions and private companies in Morocco. The claimed judicial, road-safety and vocational-training data could create risks of fraud, identity theft, phishing and blackmail. The same actor also published claims concerning Moroccan institutions in April 2026, indicating repeated activity that warrants continued monitoring. The source material does not establish the initial access vector, the remediation status or any institutional response.
