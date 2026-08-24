[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# African victims - January 2025

👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

**19 documented cyber incidents** under AFRINTEL Taxonomy v2: Ransomware 16, Data Leak 2, Account Takeover 1.

> Public-source links are added to supplementary incidents identified through online research to complete the corpus. They are not retroactively imposed on historical AFRINTEL records, including Dark Web observations.

## January 2025

### 06 January 2025
#### 🇰🇪 Kenya - Molars Dental Practice
- **Ransomware Group:** ransomhub
- **Sector:** Healthcare (Dental)
- **Website:** https://molars.co.ke
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Analysis:** AFRINTEL reviewed the supplied workbook and eight additional evidence files. The workbook contains salary-structure material and separate sheets for doctors, accounts, HR, operations, dental officers, credit control, ICT, medical engineers, dental technicians, customer care, nurses, support staff, technical staff, procurement, graphics and marketing. The evidence also includes a bank-payment screenshot and documents consistent with payroll or staff administration. This supports a published sample assessment and indicates potential exposure of employee compensation, departmental structures, internal operations and financial-processing information. The claimed 19 GB volume remains unverified, as does the initial access vector and the completeness of the dataset. AFRINTEL does not reproduce employee names, salaries, bank details or other personal data.
- **Victim Description:** Molars is a leading dental clinic network based in Nairobi, providing specialized care ranging from orthodontics to dental surgery for local and international clientele. The actor claims to have exfiltrated 19 GB of data; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 09 January 2025
#### 🇪🇬 Egypt - General Authority for Government Services
- **Ransomware Group:** funksec
- **Sector:** Public Administrations / Finance / Public Procurement.
- **Website:** gags.gov.eg
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** GAGS is the regulatory authority for government services in Egypt. It oversees tender procedures, state inventory management, and disposal of public assets.
- **Analysis:** AFRINTEL reviewed a local set of screenshots consistent with the claim made by the threat actor funksec, showing authenticated, administrator-level access to two internal modules of the GAGS platform: a complaints and public-tender management interface listing tender and complaint records with reference numbers, dates and subject descriptions, and a state-owned building and property management interface listing entity names, surface areas and financial valuations. One screenshot shows a boolean-based blind SQL injection payload present in an application search field, indicating the technique used to obtain or probe database access. AFRINTEL did not observe a structured data export or bulk sample beyond these interface captures. The combination of an authenticated admin session, internal-only application paths and a visible injection payload supports a high confidence assessment of a genuine intrusion into GAGS's backend systems, though the full scope of data actually exfiltrated remains unconfirmed. Given GAGS's role in Egyptian public procurement and state asset management, this incident presents a risk to the integrity and confidentiality of tender processes and state property records. AFRINTEL does not reproduce any procurement reference, entity name or financial figure from the reviewed material.

### 09 January 2025
#### 🇿🇦 South Africa - Pick n Pay (pnp.co.za)
- **Ransomware Group:** apt73
- **Sector:** Retail / Mass Distribution.
- **Website:** pnp.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** **Pick n Pay Group Ltd** is the second largest food retailer in South Africa.

### 11 January 2025
#### 🇲🇦 Morocco - SEOCOM Marrakech (seocommarrakech.com)
- **Ransomware Group:** funksec
- **Sector:** Technology / Digital Marketing / SEO.
- **Website:** seocommarrakech.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** SEOCOM is a Moroccan agency providing SEO (Search Engine Optimization), advertising campaign management (SEA), and web development services for local and international companies.

### 14 January 2025
#### 🇳🇬 Nigeria - INTELS Nigeria Limited (intelservice.com)
- **Ransomware Group:** ransomhub
- **Sector:** Oil & Gas Logistics / Port Services.
- **Website:** intelservices.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Intels is a pillar of the Nigerian economy, managing 90% of offshore oil exploration support activities. The group claims to have exfiltrated approximately 1.5 TB of sensitive data; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 14 January 2025
#### 🇪🇬 Egypt - Sharm Reef Hotel
- **Ransomware Group:** spacebears
- **Sector:** Hospitality / Tourism.
- **Website:** sharmreefhotel.com / sharmelsheikh.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Sharm Reef Hotel is a 4-star resort located on the Um El Sid plateau in Sharm El Sheikh, Egypt.

### 15 January 2025
#### 🇪🇬 Egypt - Misr Technology Services (MTS / mts.gov.eg)
- **Ransomware Group:** funksec
- **Sector:** Public Administrations
- **Website:** mts.gov.eg
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** Misr Technology Services (MTS) is the Egyptian government entity responsible for developing and managing the national trade facilitation platform, including the Nafeza system.
- **Analysis:** AFRINTEL reviewed a local set of screenshots and system-generated PDF captures consistent with the claim made by the threat actor funksec, produced by internal systems of the Maritime Transport and Logistics Sector, including the Egyptian Maritime Data Bank. The reviewed material includes an individual permit-application record naming an applicant, an affiliated shipping agency and a submission date; a port-traffic comparison report listing vessel-call statistics by port for 2023 and 2024; a list of port investment projects and opportunities; and detailed sector payment-collection reports covering several date ranges between January and April 2024, listing client names, transaction types, reference numbers and payment amounts collected through the sector's point-of-sale channel. Two of the reviewed documents carry a system print timestamp of 14 and 15 January 2025, consistent with the claim's publication date. The presence of internally generated, dated reports bearing named applicants and clients, combined with the platform's own letterhead and print metadata, supports a high confidence assessment of genuine access to MTS's internal reporting systems. Given MTS's role in managing Egypt's national trade-facilitation platform, including the Nafeza system, this incident presents a risk to shipping-agency personnel, client financial records and the confidentiality of national trade-facilitation operations. AFRINTEL does not reproduce any applicant name, client name, financial figure or document reference from the reviewed material.

### 16 January 2025
#### 🇿🇦 South Africa - North-West University (NWU)
- **Actor / Group:** SevenZeroDay404
- **Sector:** Education / University
- **Website:** [nwu.ac.za](https://www.nwu.ac.za/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** North-West University (NWU) is a South African higher education institution. The `nwu.ac.za` domain and the visual identity used in the actor's publication correspond to this university, which is explicitly presented as the victim in the claim.
- **Analysis:** On 16 January 2025, SevenZeroDay404 published an entry titled **"29K NWU Student Database"** on an underground forum, accompanied by the North-West University logo and a dataset presented as a student database. The actor claims approximately **29,000 records**. The provided file contains names, academic results expressed as GPA values, university programmes and study years. Examination of the content identified **2,893 occurrences of structured GPA values**, which cannot automatically be treated as 2,893 distinct students. The claimed volume of 29,000 records therefore cannot be validated from this sample. Attribution of the dataset to `nwu.ac.za` remains uncertain: no explicit marker such as the `nwu.ac.za` domain, a reference to South Africa or a North-West University campus was identified in the provided data. The naming of several academic programmes and the use of a 4.00 grading system also show similarities with another university using the NWU acronym. These elements are not sufficient to reattribute the claim, but they prevent confirmation that the sample actually originates from North-West University's systems in South Africa. The available evidence therefore establishes **North-West University in South Africa as the victim claimed by SevenZeroDay404**, without independently confirming the origin of the dataset, the completeness of the claimed 29,000 records or an actual compromise of the university's systems. If authentic, the exposed data could facilitate targeted phishing and identity impersonation attempts against students or former students.

### 21 January 2025
#### 🇩🇿 Algeria - Barika University Center (cu-barika.dz)
- **Ransomware Group:** funksec
- **Sector:** Education / Higher Education / Research.
- **Website:** cu-barika.dz
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** The Barika University Center (Ahmed Ben Abderrezak El Hamouda) is a higher education hub located in the wilaya of Batna, offering programs in technological sciences, law, and humanities.

### 21 January 2025
#### 🇩🇿 Algeria - Inaya Clinic (inayaclinic.org)
- **Ransomware Group:** spacebears
- **Sector:** Healthcare
- **Website:** inayaclinic.org
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Inaya Clinic is a multidisciplinary medical facility in Algeria, renowned for its centers of excellence in cardiology, cardiovascular surgery, and obstetrics-gynecology.

### 24 January 2025
#### 🇳🇬 Nigeria - Lower Niger River Basin Development Authority (LNRBDA)
- **Ransomware Group:** GDLockerSec
- **Sector:** Public Administrations / Water Resources / Agriculture.
- **Website:** lnrbda.gov.ng
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** LNRBDA is a strategic agency under the supervision of the Nigerian Federal Ministry of Water Resources. It manages dam projects, irrigation, drinking water supply, and rural development.
- **Analysis:** AFRINTEL reviewed a local sample of files consistent with the claim made by the threat actor GDLockerSec, comprising raw database exports from the agency's web application backend together with a session-store database file. The reviewed tables include an applicant-information table (66 records) with full name, date of birth, local government area, phone, email, referee name/email/phone/address, contact address, institution and a free-text "reason for applying" field, consistent with a graduate employment-scheme application form; a user table storing account emails alongside plaintext passwords; an administrative-user table containing hashed admin-level ("AD") account credentials; and a validation table pairing one-time passcodes with phone numbers. A separate news table contains routine public-facing content and is not sensitive. The combination of a genuinely structured, multi-table application backend export, an accompanying session database, and the presence of plaintext user passwords and administrator credentials supports a very high confidence assessment of a genuine, deep compromise of the agency's systems rather than a superficial claim. Given LNRBDA's status as a Nigerian federal government agency, the exposure of plaintext credentials, administrator accounts, applicant personal data and phone-linked one-time passcodes creates a severe risk of account takeover, further lateral compromise of government systems, and identity fraud or targeted phishing against applicants and referees. AFRINTEL does not reproduce any name, date of birth, address, phone number, email, password or passcode from the reviewed sample.

### 24 January 2025
#### 🇲🇦 Morocco - Sidi Mohamed Ben Abdellah University (www.usmba.ac.ma)
- **Ransomware Group:** GDLockerSec
- **Sector:** Education / Higher Education / Research.
- **Website:** usmba.ac.ma
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 2
- **Victim Description:** USMBA is a multidisciplinary university comprising numerous institutions (Faculties of Medicine, Science, Letters, ENCG, ENSA, etc.).
- **Analysis:** AFRINTEL reviewed a local sample of material consistent with the claim made by the threat actor GDLockerSec, consisting of screenshots displaying a structured internal database of research laboratories and teams, rendered through the actor's own CSV-viewer tool. The reviewed records list research units and departments consistent with USMBA's École Normale Supérieure in Fès, alongside their declared research themes and ongoing projects (covering fields such as condensed-matter chemistry, functional ecology, mechanical engineering, artificial intelligence and neural networks, natural-language processing, data warehousing and image processing). Named individuals associated with each research unit are present in the underlying data but were redacted in the material reviewed by AFRINTEL. The consistency between the listed research units, themes and USMBA's known academic structure supports a high confidence assessment that the material reflects a genuine internal research-administration database rather than a fabricated sample. The exposed dataset relates primarily to institutional research organisation and personnel rather than student or financial records, creating a moderate risk of targeted phishing and impersonation against named researchers and laboratory directors. AFRINTEL does not reproduce any name, laboratory identifier or research-project detail beyond what is necessary to characterise the nature of the exposure.

### 26 January 2025
#### 🇳🇬 Nigeria - Achievers Journal of Scientific Research
- **Ransomware Group:** funksec
- **Sector:** Education / Scientific Research / Academic Publishing.
- **Website:** achieverssciencejournal.org
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 2
- **Victim Description:** AJSR is a multidisciplinary peer-reviewed journal that publishes original research in the fields of applied sciences, engineering, and technology.
- **Analysis:** AFRINTEL reviewed a local sample of material consistent with the claim made by the threat actor funksec, including two screenshots of the "Users & Roles" administration panel of the journal's Open Journal Systems (OJS) platform, a CSV export of 64 user records with fields for given name, family name, email, phone, country, mailing address, registration date and assigned roles (Site Admin, editor, author, reviewer and related roles), and a phpinfo() disclosure page (PHP 8.1.31 on a cPanel/CloudLinux server) confirming genuine access to server configuration details. The user records are consistently associated with Nigerian academic institutions (email domains including federalpolyilaro.edu.ng, wellspringuniversity.edu.ng and uniosun.edu.ng), matching the journal's declared academic scope. One user record contains an injected spam link in place of a name field, indicating the platform's input fields were not properly sanitised, consistent with a poorly secured, exploitable web application. The combination of a live administration-panel export, a matching phpinfo() disclosure and Nigerian academic email domains supports a high confidence assessment of a genuine compromise. The exposed dataset consists of academic contributors' names, emails, countries and platform roles rather than financial or health data, creating a risk of targeted phishing and account takeover against journal authors, reviewers and editors. AFRINTEL does not reproduce any name, email address, username or server path from the reviewed sample.

### 26 January 2025
#### 🇪🇬 Egypt - FGSE, Cairo University (fgse.cu.edu.eg)
- **Ransomware Group:** GDLockerSec
- **Sector:** Education / Higher Education / Educational Research.
- **Website:** fgse.cu.edu.eg
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** The FGSE (Faculty of Graduate Studies for Education) is one of the oldest and most respected research institutions in Egypt.

### 27 January 2025
#### 🇺🇬 Uganda - QED (qed.co.ug)
- **Ransomware Group:** funksec
- **Sector:** Consulting Services / Bulk SMS & Broadcast Messaging
- **Website:** qed.co.ug
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** QED is a leading Ugandan firm specializing in Monitoring, Evaluation and Learning (MEL). It supports projects funded by international organizations in the health, education, and governance sectors, and operates a bulk-SMS and broadcast messaging platform used for stakeholder outreach on behalf of client organizations.
- **Analysis:** AFRINTEL reviewed a local set of screenshots consistent with the claim made by the threat actor funksec, showing authenticated administrator access to a bulk-SMS and broadcast messaging platform hosted on a QED subdomain and branded for a client identified in the interface as "d.lightUganda" (a solar and pay-as-you-go energy service provider active in Uganda). One screenshot shows a contacts management module listing 1,847,472 individual records (phone number, first name and last name) used for bulk SMS broadcasts. Another screenshot shows the platform's user-management panel, in which an account named "Funksec" with administrator role and an associated email address had been created, indicating the actor retained persistent administrative access to the application rather than merely viewing it. Separately, AFRINTEL reviewed four exported CSV files consistent with the same platform (delivery and inbound SMS reports) totalling close to 89,000 records, containing sender/recipient MSISDN numbers, message status and timestamps ranging up to 27 January 2025, matching the claim's publication date. The combination of a self-created administrator account left inside the victim's application, a matching contacts volume shown in two independent screenshots, and dated exported delivery logs supports a very high confidence assessment of a genuine, sustained compromise. Given the scale of the exposed contact database and its apparent link to a consumer energy-finance client, this incident presents a significant risk of large-scale smishing, fraud and impersonation campaigns targeting Ugandan mobile subscribers. AFRINTEL does not reproduce any phone number, name, message content or account credential from the reviewed material.

### 27 January 2025
#### 🇿🇲 Zambia - Workers (workers.com.zm)
- **Ransomware Group:** babuk2
- **Sector:** HR Services / Recruitment
- **Website:** workers.com.zm
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** Zambian recruitment and temporary work services company.
- **Analysis:** AFRINTEL reviewed a local MySQL database export consistent with the site's WordPress-based platform, dated 22 October 2024, containing the full schema and data for the site's WordPress core tables (including its user account table), its WooCommerce order tables, and a donation module built on the GiveWP plugin (donor, donation-meta and subscription tables), alongside a custom checkout and orders module. The structure and completeness of the export are consistent with a full backend database backup rather than a partial or superficial sample. AFRINTEL notes as a point of attention that the reviewed file did not carry actor-specific branding confirming attribution; the babuk2 attribution is retained as currently recorded, and manual verification of this attribution, including a possible double-claim check, is recommended. Given the presence of user accounts, order records and donor/payment-related tables, this incident presents a risk of account takeover, payment-related fraud and donor data exposure. AFRINTEL does not reproduce any username, password hash, order record or donor detail from the reviewed material.

### 27 January 2025
#### 🇰🇪 Kenya - Zetech University (zetech.ac.ke)
- **Ransomware Group:** babuk2
- **Sector:** Education / Higher Education
- **Website:** zetech.ac.ke
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Zetech University is a leading higher education institution in Kenya.

### 31 January 2025 - reported date
#### Kenya - Business Registration Service (BRS)
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** https://brs.go.ke/
- **Incident date:** Night of 31 January 2025 - reported date, publicly described as believed/probable
- **Initial publication date:** 2 February 2025
- **Status:** Government Confirmed
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** Kenya's Business Registration Service administers the national register of companies and businesses, including records relating to companies, directors, shareholders and beneficial owners.
- **Analysis:** On 2 February 2025, the Business Registration Service (BRS) said it had opened an investigation after reports of a potential breach affecting the companies registry. Public reporting at that stage placed the attack on the night of 31 January 2025 but described that timing as believed rather than technically established. On 6 February, Kenya's Ministry of Information, Communications and the Digital Economy confirmed that a data breach had occurred and that unauthorized publication of information had been removed. BRS systems and databases were then reported as secured. The access vector, actor and complete scope of affected data remain publicly undetermined.
- **Source type:** Government statements reported by public media
- **Public sources:** [The Star - BRS statement](https://www.the-star.co.ke/news/realtime/2025-02-02-business-registration-service-assures-of-data-security-amid-alleged-breach) | [The Star - ICT Ministry update](https://www.the-star.co.ke/news/2025-02-06-kabogo-weve-addressed-data-breach-at-business-registration-service)

---

### 31 January 2025
#### Kenya - Kenya Broadcasting Corporation (KBC)
- **Actor / Group:** Unknown
- **Sector:** Media / Entertainment
- **Website:** https://www.kbc.co.ke/
- **Incident date:** 31 January 2025 - date reported by Pulse Kenya; KBC confirmed the account compromise
- **Initial publication date:** 1 February 2025
- **Status:** Victim Confirmed
- **Incident type:** Account Takeover
- **Subtype:** Compromised X account / cryptocurrency scam
- **Confidence level:** High
- **Impact level:** Level 3
- **Source type:** Victim Confirmation + Public Media
- **Analysis:** Pulse Kenya reported on 1 February 2025 that attackers had taken control of KBC's official X account on Friday, 31 January. KBC confirmed that the `KBCChannel1` account had been compromised and said it was working to restore access. The account had been renamed "DeepSeek AI" and was used to distribute cryptocurrency-scam content. The public disclosure date is therefore 1 February, while the incident is placed on 31 January based on the reported chronology. The available evidence does not establish a broader compromise of KBC's information systems or the technical identity of the actor.
- **Sources:** [Pulse Kenya - KBC confirms X account compromise](https://www.pulse.co.ke/story/kbcs-x-account-hacked-and-name-changed-to-deepseek-ai-2025020111532480629)
