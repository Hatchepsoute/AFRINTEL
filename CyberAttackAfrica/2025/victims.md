# AFRINTEL victim records 2025

[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

The records below are compiled directly from the AFRINTEL monthly files for 2025. Publication dates, discovery dates and uncertainty levels are retained whenever present in the source.

## January 2025

### 06 January 2025
#### 🇰🇪 Kenya - Molars Dental Practice
- **Ransomware Group:** ransomhub
- **Sector:** Healthcare (Dental)
- **Website:** https://molars.co.ke
- **Status:** Claim - Data Sample Published
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
- **Victim Description:** **Pick n Pay Group Ltd** is the second largest food retailer in South Africa.

### 11 January 2025
#### 🇲🇦 Morocco - SEOCOM Marrakech (seocommarrakech.com)
- **Ransomware Group:** funksec
- **Sector:** Technology / Digital Marketing / SEO.
- **Website:** seocommarrakech.com
- **Status:** Claim - Unverified
- **Victim Description:** SEOCOM is a Moroccan agency providing SEO (Search Engine Optimization), advertising campaign management (SEA), and web development services for local and international companies.

### 14 January 2025
#### 🇳🇬 Nigeria - INTELS Nigeria Limited (intelservice.com)
- **Ransomware Group:** ransomhub
- **Sector:** Oil & Gas Logistics / Port Services.
- **Website:** intelservices.com
- **Status:** Claim - Unverified
- **Victim Description:** Intels is a pillar of the Nigerian economy, managing 90% of offshore oil exploration support activities. The group claims to have exfiltrated approximately 1.5 TB of sensitive data; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 14 January 2025
#### 🇪🇬 Egypt - Sharm Reef Hotel
- **Ransomware Group:** spacebears
- **Sector:** Hospitality / Tourism.
- **Website:** sharmreefhotel.com / sharmelsheikh.com
- **Status:** Claim - Unverified
- **Victim Description:** Sharm Reef Hotel is a 4-star resort located on the Um El Sid plateau in Sharm El Sheikh, Egypt.

### 15 January 2025
#### 🇪🇬 Egypt - Misr Technology Services (MTS / mts.gov.eg)
- **Ransomware Group:** funksec
- **Sector:** Public Administrations
- **Website:** mts.gov.eg
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** Misr Technology Services (MTS) is the Egyptian government entity responsible for developing and managing the national trade facilitation platform, including the Nafeza system.
- **Analysis:** AFRINTEL reviewed a local set of screenshots and system-generated PDF captures consistent with the claim made by the threat actor funksec, produced by internal systems of the Maritime Transport and Logistics Sector, including the Egyptian Maritime Data Bank. The reviewed material includes an individual permit-application record naming an applicant, an affiliated shipping agency and a submission date; a port-traffic comparison report listing vessel-call statistics by port for 2023 and 2024; a list of port investment projects and opportunities; and detailed sector payment-collection reports covering several date ranges between January and April 2024, listing client names, transaction types, reference numbers and payment amounts collected through the sector's point-of-sale channel. Two of the reviewed documents carry a system print timestamp of 14 and 15 January 2025, consistent with the claim's publication date. The presence of internally generated, dated reports bearing named applicants and clients, combined with the platform's own letterhead and print metadata, supports a high confidence assessment of genuine access to MTS's internal reporting systems. Given MTS's role in managing Egypt's national trade-facilitation platform, including the Nafeza system, this incident presents a risk to shipping-agency personnel, client financial records and the confidentiality of national trade-facilitation operations. AFRINTEL does not reproduce any applicant name, client name, financial figure or document reference from the reviewed material.

### 21 January 2025
#### 🇩🇿 Algeria - Barika University Center (cu-barika.dz)
- **Ransomware Group:** funksec
- **Sector:** Education / Higher Education / Research.
- **Website:** cu-barika.dz
- **Status:** Claim - Unverified
- **Victim Description:** The Barika University Center (Ahmed Ben Abderrezak El Hamouda) is a higher education hub located in the wilaya of Batna, offering programs in technological sciences, law, and humanities.

### 21 January 2025
#### 🇩🇿 Algeria - Inaya Clinic (inayaclinic.org)
- **Ransomware Group:** spacebears
- **Sector:** Healthcare
- **Website:** inayaclinic.org
- **Status:** Claim - Unverified
- **Victim Description:** Inaya Clinic is a multidisciplinary medical facility in Algeria, renowned for its centers of excellence in cardiology, cardiovascular surgery, and obstetrics-gynecology.

### 24 January 2025
#### 🇳🇬 Nigeria - Lower Niger River Basin Development Authority (LNRBDA)
- **Ransomware Group:** GDLockerSec
- **Sector:** Public Administrations / Water Resources / Agriculture.
- **Website:** lnrbda.gov.ng
- **Status:** Claim - Data Sample Published
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
- **Victim Description:** The FGSE (Faculty of Graduate Studies for Education) is one of the oldest and most respected research institutions in Egypt.

### 27 January 2025
#### 🇺🇬 Uganda - QED (qed.co.ug)
- **Ransomware Group:** funksec
- **Sector:** Consulting Services / Bulk SMS & Broadcast Messaging
- **Website:** qed.co.ug
- **Status:** Claim - Data Sample Published
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
- **Victim Description:** Zetech University is a leading higher education institution in Kenya.

## February 2025

### 03 February 2025
#### 🇪🇬 Egypt - Xlab Group
- **Ransomware Group:** fog
- **Sector:** Business Services / Technology Consulting (IT & Digital Solutions)
- **Website:** https://xlab-group.com/
- **Status:** Claim - Unverified
- **Victim Description:** Xlab Group is an Egyptian company specializing in digital marketing solutions, software development, brand strategy consulting, and digital transformation for Middle Eastern companies.

### 12 February 2025
#### 🇲🇦 Morocco - ASK Gras Savoye (askgs.ma)
- **Ransomware Group:** ransomhub
- **Sector:** Insurance / Brokerage
- **Website:** askgs.ma
- **Status:** Claim - Unverified
- **Victim Description:** ASK Gras Savoye is one of the leading insurance brokers in Morocco.

### 12 February 2025
#### 🇿🇦 South Africa - South African Weather Service (SAWS)
- **Ransomware Group:** ransomhub
- **Sector:** Public Services / Environment (Meteorology)
- **Website:** weathersa.co.za
- **Status:** Claim - Unverified
- **Victim Description:** The South African Weather Service (SAWS) is South Africa's national meteorological service, providing weather forecasts and warnings.

### 19 February 2025
#### 🇿🇲 Zambia - Government Services Portal (services.gov.zm)
- **Ransomware Group:** flocker
- **Sector:** Government / Digital Public Services
- **Website:** http://services.gov.zm/
- **Status:** Claim - Data Sample Published
- **Victim Description:** The services.gov.zm portal is the central platform of the Zambian government (Smart Zambia Institute). It brings together over 322 online services, ranging from visa and permit applications to tax and administrative services for citizens and businesses.
- **Analysis:** AFRINTEL opened and inspected (without reproducing) a large set of files attributed to the claim, corresponding to a full profile export from a Windows host named GSB, harvested under the Administrator account by a collection tool whose output is consistently labelled "_throne_" across three distinct, timestamped collection runs spanning roughly 13 hours (evening of 10 February to mid-morning of 11 February 2025), indicating repeated or persistent tool execution rather than a single pass. The material is packaged into 44 archive parts of 1.7-52 MB each (consistent with exfiltration chunked to a size-capped channel) and totals roughly 1.6 GB. Verified contents include: Chrome and Firefox browser artifacts (autofill databases, session stores, site-security state, the Firefox NSS key database, and a 45 MB browser disk-cache container found on inspection to hold cached Microsoft 365/SharePoint/OneDrive/Akamai CDN HTTP traffic); Windows DPAPI protection blobs and certificate/private-key material tied to the Administrator's Windows security identifier; an RDP connection file whose target field, on inspection, resolves to an internal (RFC1918) address; a Firefox history database whose limited browsing activity, on inspection, includes a second distinct internal address; an empty, unused dial-up/VPN phonebook file; and Visual Studio 2017 project backups. One recovered SQL file contains a query against the `ASPStateTempSessions` table together with an internal support note referencing a system named "ZIGS", indicating an ASP.NET application backed by Microsoft SQL Server and consistent with genuine administrative access to the portal's operating environment rather than a superficial claim; a separate file is the well-known public Ola Hallengren SQL Server maintenance script, confirming SQL Server as the database engine. The set also includes an Office 365 tenant user list: on inspection, all 89 listed accounts are licensed (Microsoft 365 E3), 85 under the domain dotgovsolutions.net, 3 under the tenant's default onmicrosoft.com domain, and 1 under an unrelated external domain (a guest/foreign account within the same tenant) — indicating the portal's Microsoft 365 tenant is operated by a third-party IT services provider, with at least one additional external party granted access. A 10-byte password file was present but not opened by AFRINTEL. No Chrome or Firefox saved-password database was found in the reviewed set. The scale, internal consistency, multiple collection runs, and presence of DPAPI/certificate material, internal-network addresses and RDP artifacts support a high confidence assessment of a genuine administrator-level endpoint compromise, independent of the ransomware group's public claim; this differs materially from the actor's framing as a straightforward "1.2 GB data leak", since the reviewed material is predominantly system, credential-adjacent and internal-network artifacts rather than citizen records. AFRINTEL does not reproduce any credentials, certificates, session data, account names, IP addresses or file content from the reviewed sample.

### 19 February 2025
#### 🇬🇭 Ghana - Brolly
- **Ransomware Group:** killsec
- **Sector:** Insurance / Insurtech
- **Website:** brolly.africa
- **Status:** Claim - Data Sample Published
- **Victim Description:** Brolly is a Ghanaian insurtech startup offering flexible and affordable car insurance solutions (pay-as-you-go model). It allows drivers to spread their insurance payments weekly or monthly via a digital platform.
- **Analysis:** AFRINTEL reviewed the provided KillSec proof without reproducing personal data. The directory contains 4 CSV policy exports with 183 data rows in total, 77 PDF documents and approximately 10.4 MB of material. The CSV structure is consistent with Brolly's vehicle-insurance operations and includes policy/customer fields, coverage type, insurer and vehicle attributes, policy dates, premiums and registration-related fields. The PDFs comprise 50 car-insurance instalment agreements, 25 loan agreements and 2 motor-insurance policy schedules. File names indicate policy-export periods covering August to October 2024, while the documents include agreements generated during October-November 2024; these are evidence dates, not a confirmed intrusion or publication date. The sample contains personal, contact, insurance and vehicle-related information with potential risks of targeted phishing, identity fraud, insurance fraud and social engineering. The observed material supports a medium-to-high confidence assessment that the sample is thematically and structurally consistent with Brolly data, but AFRINTEL has not independently confirmed the intrusion, the full scope of access or the completeness of the dataset. The group KillSec is the claimed actor; no independent attribution beyond the observed ransomware publication is established. AFRINTEL does not reproduce names, phone numbers, registration numbers, chassis numbers, policy identifiers or other raw personal data.

### 21 February 2025
#### 🇳🇦 Namibia - Paratus
- **Ransomware Group:** akira
- **Sector:** Telecommunications
- **Website:** www.paratus.africa
- **Status:** Claim - Unverified
- **Victim Description:** Pan-African telecommunications operator, investing in network infrastructure across Africa.

### 22 February 2025
#### 🇪🇬 Egypt - SPEED Co
- **Ransomware Group:** hunter
- **Sector:** Logistics / Distribution
- **Website:** speed-com.eg
- **Status:** Claim - Unverified
- **Victim Description:** SPEED Co (Speed Ahmed Hassan) is one of the largest logistics and distribution service providers in Egypt. The company manages storage and transportation of Fast-Moving Consumer Goods (FMCG) for major multinationals and local brands, relying on a vast fleet of vehicles and automated distribution centers. The group claims to have extracted a volume of 444.8 GB of data, comprising 285,891 files; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 23 February 2025
#### 🇪🇬 Egypt - Shaghalni
- **Ransomware Group:** killsec
- **Sector:** Services / Recruitment (HR Tech)
- **Website:** shaghalni.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** Shaghalni is one of the leading recruitment platforms in Egypt, specializing in connecting job seekers (notably technical and blue-collar profiles) with companies.
- **Analysis:** The KillSec leak-site listing for Shaghalni offers the data for sale at €5,000, accompanied by a local sample of documents referenced by the listing. The leak-site description matches Shaghalni's publicly known profile as a free Egyptian online job-search platform connecting candidates with employers. The reviewed sample includes an employer-accounts CSV export listing companies registered on the platform (company name, phone number, registration date, country, sector, company size, website and profile text), predominantly Egyptian businesses, and a set of company verification documents uploaded by employers, including Egyptian national ID cards, Egyptian Tax Authority correspondence and registration certificates, an Egyptian Ministry of Tourism company license, and a Saudi Arabia Ministry of Commerce and Investment company registration certificate, indicating the platform's employer base extends beyond Egypt. The documents are internally consistent with Shaghalni's stated activity as an employer-facing recruitment platform. AFRINTEL does not reproduce any national ID numbers, company registration numbers, tax references, phone numbers or names from the reviewed sample. The reviewed material pertains to employer/company accounts and their verification documents; it does not establish whether job-seeker/candidate personal data was also part of the claimed dataset.

## March 2025

### 02 March 2025
#### 🇧🇼 Botswana - IT-IQ Botswana
- **Ransomware Group:** play
- **Sector:** Technology Consulting
- **Website:** www.itiq.co.bw
- **Status:** Claim - Unverified
- **Victim Description:** IT-IQ Botswana is one of the leading providers of IT solutions and certified training (Microsoft, Cisco, VMware) in Botswana.

### 02 March 2025
#### 🇳🇬 Nigeria - Workforce Group
- **Ransomware Group:** killsec
- **Sector:** Education / HR Services
- **Website:** workforcegroup.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Nigerian educational services and human resources management company.
- **Analysis:** AFRINTEL reviewed a local sample of documents and a structured personnel-record export associated with this claim, together with a downloaded but incomplete archive (a single ~26 MB volume of what appears to be a larger split archive; AFRINTEL did not extract or open its contents). The reviewed material includes a large personnel dataset covering staff identifiers, names, contact details, demographic fields, referee information and employer-placement data referencing major Nigerian banks, consistent with Workforce Group's role as an HR-outsourcing and staffing provider. The sample also includes internally branded HR documents (a Workforce Group staff-handbook acknowledgement form, a leave-request form, an employment offer letter with a confidentiality clause) and financial-sector onboarding paperwork, including personal loan application forms containing Bank Verification Numbers (BVN), dates of birth, phone numbers, home addresses and next-of-kin details, plus a guarantor form from a Nigerian commercial bank. The documents are internally consistent with Workforce Group's branding and its outsourcing role across multiple Nigerian financial institutions. Given the scale of the personnel dataset and the presence of BVN and banking-sector staffing records spanning several major banks, potential exposure extends beyond a single organization into the wider outsourced-staffing ecosystem of Nigeria's banking sector, creating a material risk of identity fraud, account takeover and targeted social engineering. AFRINTEL does not reproduce any names, BVNs, contact details, addresses or account information from the reviewed material and has not verified whether the available archive represents the complete claimed dataset.

### 03 March 2025
#### 🇿🇦 South Africa - LINKGROUP
- **Ransomware Group:** arcusmedia
- **Sector:** Technology Consulting
- **Website:** linkgroup.co.za
- **Status:** Claim - Unverified
- **Victim Description:** LINKGROUP is a South African IT consulting and telecom services company.

### 03 March 2025
#### 🇹🇿 Tanzania - synaptic.co.tz
- **Ransomware Group:** arcusmedia
- **Sector:** Technology Consulting
- **Website:** synaptic.co.tz
- **Status:** Claim - Unverified
- **Victim Description:** Tanzanian IT consulting company.

### 05 March 2025
#### 🇳🇬 Nigeria - Medical Rehabilitation Therapists Board (MRTB)
- **Incident type:** Data Leak
- **Actor / Group:** MisterSam
- **Sector:** Government / Healthcare Regulation
- **Website:** Not specified
- **Status:** Claim - Unverified
- **Victim Description:** The Medical Rehabilitation Therapists Board of Nigeria (MRTB) is a Nigerian public regulatory body for medical rehabilitation professions.
- **Analysis:** A forum post claims that backups of several CMS instances associated with the board contain database access and other credentials that could enable broader server access. The hidden content, domain, credentials and a verifiable database sample are not exposed in the available material. This is recorded as an unverified CMS-access and backup-exposure claim; no credentials or personal data are reproduced.

### 07 March 2025
#### 🇿🇦 South Africa - ACDC Express
- **Ransomware Group:** lynx
- **Sector:** Retail (Distribution)
- **Website:** acdcdynamics.co.za
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** ACDC Dynamics is a major South African manufacturer, importer, and distributor of electrical components, tools, and safety equipment.
- **Analysis:** The Lynx leak-site listing for ACDC Express (ACDC Dynamics) categorizes the publication as Encrypted, Proof and AD Dump, and describes a single disclosure titled "Data" covering HR, financial data, contracts and confidential material, with a claimed volume of 800 GB. The listing states a publication date of 7 March 2025 and cites an estimated victim income figure of $123,000,000, a metric self-reported by the actor and not independently verified. The victim description on the leak site matches ACDC Dynamics' publicly known profile (founded 1984, electrical and electronics distributor headquartered in Edenvale, Johannesburg, with branches in Germiston, Cape Town, Pinetown and Riverhorse). The underlying file contents referenced by the "Proof" and "AD Dump" categories were not reviewed and are not reproduced.

### 11 March 2025
#### 🇪🇬 Egypt - ISEE (International School of Elite Education)
- **Ransomware Group:** funksec
- **Sector:** Education / Private Schooling
- **Website:** isee-eg.com
- **Status:** Claim - Unverified
- **Victim Description:** The International School of Elite Education (ISEE) is a prestigious private school located in Cairo.

### 25 March 2025
#### 🇪🇬 Egypt - MISR AL MAHABA HOSPITAL
- **Ransomware Group:** nightspire
- **Sector:** Healthcare / Hospital Sector
- **Website:** misralmahaba.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** Misr Al Mahaba Hospital is a significant private healthcare center in Cairo.
- **Analysis:** The NightSpire leak-site listing for Misr Al Mahaba Hospital, published 24 March 2025, states a countdown/deadline of 27 March 2025 and a claimed volume of 100 GB. A local sample of documents consistent with the claim includes an Egyptian national health-insurance card and a national ID card (each showing a patient photograph and partially visible identifiers), two hospital external-referral forms addressed to the General Authority for Health Insurance bearing the hospital's stamp, and an itemized hospital billing statement for a cardiac-catheterization/CCU admission listing diagnosis-related line items, individual medications administered and total charges, stamped with the hospital's accounts department seal. The documents are internally consistent with Misr Al Mahaba Hospital's branding and billing format. The sample indicates exposure of patient-identifying documents and detailed clinical/billing records, creating a material risk of medical-identity theft, insurance fraud and targeted phishing against affected patients. No patient names, national ID numbers, health-insurance numbers, diagnoses or billing figures are reproduced.

### 30 March 2025
#### 🇪🇬 Egypt - INI Investments
- **Ransomware Group:** nightspire
- **Sector:** Finance
- **Website:** iniholdings.com
- **Status:** Claim - Unverified
- **Victim Description:** INI Investments is a diversified Egyptian holding company. It invests in strategic sectors such as real estate, energy, technology, and financial services. The actor claims to have exfiltrated 400 GB of data; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.
- **Double-claim note:** The March and April records are retained separately because the source dates and evidence differ. They involve the same actor, domain and victim name, but AFRINTEL cannot determine from the available material whether the April publication is an update of the March claim or a separate claim. No merger is made pending confirmation.
### 26 March 2025
#### 🇧🇫 Burkina Faso - Government COVID-19/Vaccination Dashboard
- **Actor / Group:** Ghudra
- **Sector:** Healthcare / Public Health
- **Website:** Not specified
- **Status:** Claim - Unverified
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Access Sale
- **Description:** A forum post advertises administrator access to a Burkina Faso government COVID-19 and vaccination dashboard for a claimed price of $300.
- **Analysis:** The publication displays COVID-19 case metrics, testing figures and vaccination totals, and offers administrator access for sale. The domain, access validity, provenance and relationship to the Sentap claims from November 2024 are unknown. This is recorded as an unverified access-sale claim; no credentials or personal data are reproduced.

### 31 March 2025
#### 🇷🇼 Rwanda - moh.gov.rw
- **Ransomware Group:** babuk2
- **Sector:** Public administrations (Health)
- **Website:** moh.gov.rw
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** Ministry of Health of Rwanda.
- **Analysis:** A set of material and a raw text sample are directly associated with this claim. The most significant evidence is an active PHP web shell deployed on a Linux server hostnamed "covid-mass-testing", running PHP 7.4 as the www-data user with safe mode disabled and a working directory under /var/www; the shell exposes file-manager, console, SQL, PHP-execution and brute-force modules, indicating full remote code-execution capability rather than a passive data claim. A phpMyAdmin database-administration panel lists 23 tables with approximate row counts, including tables consistent with applicants (~110,500 rows), session data (~155,400 rows), clinicians (~29,500 rows), HR data (~9,400 rows), documents (~9,700 rows) and password/authentication records (~4,800 rows), indicating direct database-level access to a health-sector applicant/workforce-management system rather than the ministry's public website alone. Additional material, from what appears to be the same or a related applicant-management portal, shows dashboard statistics of 112,102 total applicants, 7,917 vacant positions, 4,165 employed applicants and 107,937 applicants on a waiting list, consistent with the table row counts observed in the database panel. A raw local text sample of approximately 25 user records from what is labelled a "Student" role is also examined, each containing a sequential ID, an email address and an MD5-format password hash. The combination of an active, fully-featured web shell, direct database administrative access with table-level row counts, and a raw credential-bearing user-record sample supports a very high confidence assessment of a genuine, deep compromise extending beyond a simple website claim to backend systems processing health-sector job applications, clinician records and authentication data for well over 100,000 individuals. Given the scale of exposure and the sensitivity of clinician, HR and authentication data within Rwanda's health sector, the potential impact includes large-scale credential-stuffing and account-takeover risk, targeted phishing against health-sector applicants and staff, and broader compromise of health-workforce management processes. No email address, password hash, individual applicant record or other personal data is reproduced from the reviewed material.

## April 2025

### 04 April 2025
#### 🇸🇳 Senegal - Senegalese Armed Forces (armee.sn)
- **Incident type:** Access Sale
- **Actor / Group:** oblivion666
- **Sector:** Defense / National Security
- **Website:** armee.sn (Army.sn, Sigrh.armee.sn, Srvmail.armee.sn, Spami.armee.sn)
- **Status:** Claim - Unverified
- **Victim Description:** armee.sn is the domain infrastructure of the Senegalese armed forces, covering several administrative and internal-service subdomains (Army.sn, Sigrh.armee.sn, Srvmail.armee.sn, Spami.armee.sn).
- **Analysis:** The actor oblivion666 offers the above domains for sale in a forum post, together with claimed administrator-level access to associated servers and a firewall, timed around the Senegalese independence period. No file, credential or other technical evidence accompanies the post; the listing is a bare access-sale advertisement without an accessible sample. Whether the claimed access is genuine, current or still available cannot be verified. Given the target (national defense infrastructure), a confirmed compromise would carry a high potential impact, but this remains an unverified claim pending independent evidence.

### 06 April 2025
#### 🇪🇬 Egypt - IACC Holdings
- **Ransomware Group:** dragonforce
- **Sector:** Finance / Logistics
- **Website:** www.iacc.holdings
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian private investment holding company focused on maritime transport and logistics. 27.75 GB of data exfiltrated.

### 07 April 2025
#### 🇿🇦 South Africa - Cell C
- **Ransomware Group:** ransomhouse
- **Sector:** Technology (Telecommunications)
- **Website:** cellc.co.za
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 4
- **Analysis:** AFRINTEL reviewed 20 screenshots from the RansomHouse publication. The evidence covers Cell C customer and employee information, passport material, call records, SMS data, international voice activity, customer contracts, franchise records, confidential NDAs, internal documents and a revenue summary. This breadth is consistent with a material telecommunications data exposure. Potential impacts include subscriber privacy loss, targeted phishing and fraud, employee targeting, exposure of call and messaging metadata, commercial espionage and operational reconnaissance. The screenshots do not independently establish the initial access vector, dataset completeness, affected subscriber count or operational impact. AFRINTEL does not reproduce personal records, passport details, phone numbers, contracts or download links.
- **Victim Description:** South African telecommunications operator, one of the country's leading mobile service providers.

### 08 April 2025
#### 🇪🇬 Egypt - International Business Service
- **Ransomware Group:** crypto24
- **Sector:** Business Services / Outsourcing (BPO)
- **Website:** ibsns.com
- **Status:** Claim - Unverified
- **Victim Description:** International Business Service (IBS) is one of the largest outsourcing service providers in Egypt. The company specializes in human resources management, mass recruitment, payroll outsourcing, and maintenance/logistics services for large companies and multinationals operating in Egypt.

### 08 April 2025
#### 🇲🇦 Morocco - CNSS (Caisse Nationale de Sécurité Sociale)
- **Incident type:** Data Leak
- **Actor / Group:** Jabaroot DZ
- **Sector:** Public Administrations (Social Security)
- **Website:** www.cnss.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** National Social Security Fund of Morocco.
- **Analysis:** AFRINTEL reviewed two large structured exports matching CNSS's core databases, dated to the same day as the claim. The first, an employer/affiliate table, contains approximately 1,094,000 records with fields including company name, affiliate number, affiliation dates, employer type, telepayment method, agency and regional office, along with the administrator's first name, last name, national ID number (CIN), email address and phone number, plus banking details (account ID, bank code) linked to the employer. The second, an insured-persons table, contains approximately 1,996,000 records with fields including first name, last name, national ID number (CIN), passport number, residence-permit number, an internal registration/immatriculation number, creation date, application channel and the affiliated employer's name. The scale and structure of both tables are consistent with a genuine, near-complete extract of CNSS's national employer and insured-persons registries. The combination of national ID numbers, contact details and employer affiliations for close to two million individuals and over one million employers represents a very high-impact exposure, creating substantial risk of identity fraud, social-engineering campaigns and targeted phishing at national scale. AFRINTEL does not reproduce any names, national ID numbers, contact details or banking references from the reviewed sample.

### 08 April 2025
#### 🇲🇦 Morocco - Ministry of Industry and Commerce (miepeec.gov.ma)
- **Incident type:** Data Leak
- **Actor / Group:** Jabaroot DZ
- **Sector:** Government / Economy and Industry
- **Website:** miepeec.gov.ma
- **Status:** Claim - Unverified
- **Victim Description:** The MIEPEEC is the Moroccan government body responsible for steering industrial strategy, promoting investment, and regulating trade. It manages critical platforms for interaction between the state and the private sector.

### 08 April 2025
#### 🇩🇿 Algeria - CNAS (Caisse Nationale des Assurances Sociales des Travailleurs Salariés)
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Government / Social Security
- **Website:** [cnas.dz](https://www.cnas.dz)
- **Status:** Claim - Data Sample Published
- **Victim Description:** CNAS is the Algerian public body managing health insurance and in-kind social benefits for salaried workers, through a nationwide network of agencies and payment centers.
- **Analysis:** On April 8, 2025, Phantom Atlas published a claim presented as a direct response to recent cyberattacks targeting the actor, stating it had carried out a full intrusion into CNAS's databases and extracted more than 860,200 documents. The post adds broader accusations of opaque financial and logistical routes involving Algerian companies and Dubai, said to be revealed in a future release; these accusations are not documented in the material reviewed by AFRINTEL and are reported here only as the actor's stated narrative, without validation.

  AFRINTEL reviewed a local sample of 214 image files (approximately 97 MB) associated with this claim. The sample is homogeneous and corresponds to "Attestations d'ouverture des droits aux prestations en nature" (certificates opening entitlement to in-kind benefits) issued by several CNAS agencies (notably Tizi Ouzou/Boghni and Algiers/Belcourt), mostly dated between 2022 and 2024. Each document contains the full identity of the insured member (name, first name, date of birth, address, social security registration number, affiliation center) as well as that of the covered person (insured member, spouse, child or ascendant), the coverage rate, the issuance date, the name of the issuing agent, a stamp and a signature.

  The consistency of the format across the sample, the diversity of agencies and payment centers represented, and the presence of plausible stamps and signatures support a high confidence level regarding authentic access to CNAS systems or archives. The observed volume (214 documents), however, remains far below the 860,200 claimed and does not confirm the total announced scale of the leak. Exposure of these certificates could facilitate identity theft, social-benefit fraud and targeted phishing against insured members and their dependents. AFRINTEL does not reproduce any name, date of birth, address, registration number or other personal data from the reviewed documents.

### 09 April 2025
#### 🇩🇿 Algeria - MGPTT / Mutuelle Générale des Travailleurs de la Poste et des Télécoms
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Social / Health Insurance Fund
- **Website:** mgptt.dz
- **Status:** Claim - Data Sample Published
- **Victim Description:** The MGPTT is a major social institution in Algeria, covering employees in the Postal, Telecommunications, and Information sectors. It manages healthcare reimbursements and social benefits for tens of thousands of civil servants and contractors. The publication claims more than 13 GB of internal MGPTT data, including personal data and strategic documents/databases, and also references sensitive Ministry of Labor files.
- **Analysis:** Phantom Atlas's post is accompanied by a message framing the operation as a direct response to an earlier claimed breach of CNSS, and adopts an explicitly hacktivist tone tied to the Western Sahara territorial dispute between Morocco and Algeria; this political framing is reported by AFRINTEL as stated, without validating or taking a position on the territorial claims or the mutual hacking accusations.

  AFRINTEL reviewed a sample of 4 images (approximately 496 KB in total) associated with this post. The images show photographed or scanned identity and social-protection documents: Algerian social security insured-member cards, an MGPTT retiree membership card, a CNAS affiliation certificate, and a postal payment receipt together with a hospital admission certificate from a private clinic. These documents contain full names, dates of birth, social security registration numbers, addresses and, in some cases, photographs and medical or financial information relating to named individuals.

  The observed volume (four images) is far smaller than the claimed 13 GB and does not corroborate the announced scale of the leak or confirm that this is a representative extract of an internal MGPTT information system. One image also carries the visible watermark of a third-party online document-selling service, suggesting this particular sample may originate, at least in part, from documents already circulating elsewhere rather than from a direct extraction of MGPTT's systems. Taken together, these elements call for a cautious assessment: the presence of real personal and social-insurance data appears established, but the exact origin, completeness and direct link to a compromise of MGPTT's internal systems remain uncertain. AFRINTEL does not reproduce any name, registration number, date of birth, address, photograph or medical/financial detail from the reviewed images.

### 09 April 2025
#### 🇩🇿 Algeria - Ministry of Labor
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Government / Labor Administration
- **Website:** Not specified
- **Source publication date:** April 9, 2025
- **Status:** Claim - Unverified
- **Victim Description:** The supplied publication states that Phantom Atlas accessed sensitive files from Algeria's Ministry of Labor. No ministry-specific sample is provided; this target is therefore recorded separately from MGPTT without independent confirmation of the compromise.
- **Analysis:** The claim appears in the same Phantom Atlas publication as the MGPTT claim and may reflect one operation affecting multiple Algerian public institutions. No ministry-specific dataset was collected or reproduced.

### 13 April 2025
#### 🇲🇷 Mauritania - BMI / SEDAD Mobile Wallet
- **Actor / Group:** Killer_Bee
- **Sector:** Finance / Mobile Payment
- **Website:** [bmi.mr](https://bmi.mr)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Source publication date:** April 13, 2025
- **Observed sample dates:** April 6, 2025

- **Description:**
  The publication claims to expose a database associated with SEDAD, BMI's digital banking and mobile-wallet service in Mauritania. The post claims more than 90,000 records involving wallet complaints and administrative actions.

- **Analysis:**
  The visible sample is a structured JSON record from a customer-complaints workflow. It contains customer identity fields, a national identification number, a phone number, internal user attribution, creation and update timestamps, treatment status and an activation-related complaint type. AFRINTEL does not reproduce the personal values shown in the sample. The sample supports the presence of sensitive structured data, but the claimed database size, completeness, origin and compromise are not independently confirmed. The official BMI website identifies SEDAD as BMI's digital banking and electronic-wallet service.

- **Recommendations:**
  1. Verify the claim against SEDAD application, database, API and administrator audit logs, preserve evidence and determine whether customer identity and phone data were accessed.
  2. Rotate exposed administrative credentials or tokens if required, review privileged actions, enforce MFA, monitor account-takeover and phishing attempts, and notify affected users and authorities according to applicable requirements if the exposure is confirmed.

### 13 April 2025
#### 🇪🇬 Egypt - Tawasol
- **Ransomware Group:** devman
- **Sector:** Information Technology
- **Website:** tawasol-it.com
- **Status:** Claim - Unverified
- **Victim Description:** A technology solutions integrator based in Cairo that installs security and network infrastructure systems for businesses and smart buildings.

### 13 April 2025
#### 🇲🇦 Morocco - Higher Institute of Audiovisual and Cinema Professions (ISMAC)
- **Incident type:** Data Leak
- **Actor / Group:** p4xar
- **Sector:** Education / Higher Education / Audiovisual and Cinema
- **Website:** [ismac.ma](https://ismac.ma)
- **Status:** Claim - Data Sample Published

- **Description:**
  The Higher Institute of Audiovisual and Cinema Professions (ISMAC) is a Moroccan public higher education institution in Rabat. It trains professionals in cinema, audiovisual production, directing, production management, image and sound, under the supervision of the Moroccan Ministry of Youth, Culture and Communication.

- **Analysis:**
  A forum post attributed to p4xar claims that the application hosted at `sul.ismac.ac.ma/app/` was compromised and that a file named `db.sql`, presented as the complete database, was distributed free of charge through a Telegram channel. The visible sample is a substantial SQL export of the `n_etudiants` table, with syntax and structure compatible with MySQL or MariaDB. It contains student personal data, including identity-document fields, birth details, postal addresses, email addresses, telephone numbers, nationality references, student status and user-account identifiers. The combination of these data could facilitate identity fraud, targeted phishing, social engineering, document fraud and abusive account-recovery attempts. Some records contain null or incomplete fields and encoding anomalies. The sample supports the presence of sensitive structured data, but does not establish the total volume, record count, completeness of the distributed file or independent confirmation of the claimed compromise.

### 13 April 2025
#### 🇲🇦 Morocco - Ministry of Housing and Urban Policy (mhpv.gov.ma)
- **Incident type:** Data Leak
- **Actor / Group:** B4baYega
- **Sector:** Government / Housing / Urban Policy
- **Website:** mhpv.gov.ma
- **Status:** Claim - Unverified
- **Victim Description:** The Ministry of Housing and Urban Policy (Ministère de l'Habitat et de la Politique de la Ville) is the Moroccan government body responsible for housing policy and urban development.
- **Analysis:** AFRINTEL identified a password-protected archive bearing an internal archive comment explicitly attributed to the actor B4baYega, referencing a Telegram contact channel for further "fresh and private" databases. The archive's accessible content was limited to a single small image file; AFRINTEL could not access or verify the claimed underlying dataset due to the password protection, and therefore cannot confirm its content, volume or authenticity. This entry is recorded as an unverified claim pending further evidence.

### 17 April 2025
#### 🇪🇬 Egypt - INI Investments
- **Incident type:** Data Leak
- **Actor / Group:** nightspire
- **Sector:** Financial Services / Investment Banking / Project Finance Advisory
- **Website:** Not identified with sufficient confidence
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 2
- **Victim Description:** INI Investments is an Egyptian investment banking and project-finance advisory firm based in Cairo, involved in feasibility studies, financial structuring and closures for industrial and infrastructure projects.
- **Analysis:** AFRINTEL reviewed a local sample of documents consistent with the claim made by the threat actor nightspire, including internal financial feasibility models (multi-year IRR projections ranging from 39% to 58%, capital-structure and financing-source breakdowns) for a UPVC pipe-manufacturing project, a competitor market study comparing production volumes and market share of several named Egyptian UPVC manufacturers, a project-pipeline tracker titled "Pipe line projects for Allweiler Farid Hassanein Pumps co" listing multiple client deals with project values in EGP, USD and EUR, status and bidding dates (referencing clients and projects in Egypt, Russia and Saudi Arabia), a legal study and meeting minutes, a land-assessment report for a named company's UPVC project site, and a document referencing an order extension for Hassan Allam, a major Egyptian construction and engineering group. The file metadata places the evidence between 15 and 17 April 2025; this is treated as an evidence/discovery date, not a confirmed publication date. The internal consistency of the financial models, the naming of real Egyptian industrial counterparts (Allweiler Farid Hassanein Pumps, Hassan Allam) and the coherence between the feasibility study, market study and legal documentation support a high confidence assessment of a genuine compromise of INI Investments' internal project files. The exposed material consists of confidential deal, financing and market-intelligence data rather than personal or consumer records, creating a risk of competitive intelligence exposure, business email compromise and targeted social engineering against INI Investments and its industrial clients and counterparties. AFRINTEL does not reproduce any client name, project value, financial figure or document reference from the reviewed material.
- **Double-claim note:** The March and April records are retained separately because the source dates and evidence differ. They involve the same actor, domain and victim name, but AFRINTEL cannot determine from the available material whether the April publication is an update of the March claim or a separate claim. No merger is made pending confirmation.
### 20 April 2025
#### 🇿🇦 South Africa - Premier Meats South Africa
- **Ransomware Group:** devman
- **Sector:** Agribusiness
- **Website:** premiermeats.co.za
- **Status:** Claim - Unverified
- **Victim Description:** Premier Meats is a South African company specializing in the processing and distribution of quality meats.

### 22 April 2025
#### 🇹🇳 Tunisia - Natilait
- **Ransomware Group:** cicada3301
- **Sector:** Agribusiness / Dairy Industry
- **Website:** natilait.com.tn
- **Status:** Claim - Data Sample Published
- **Victim Description:** Natilait is a major player in the Tunisian agrifood sector, specializing in the production and marketing of milk (UHT), yogurt, and derived products.
- **Analysis:** The 12 supplied JPG/PNG images include at least one structured internal product and stock table with item codes, dairy-product descriptions, quantities and inventory or stock fields; the other images appear related to operational business records, although several are not sufficiently legible for reliable extraction. The material is consistent with a data sample from Natilait manufacturing or distribution operations and could support competitive intelligence, document fraud or supply-chain targeting. The intrusion vector, the complete dataset scope and whether the images were produced by cicada3301 are not independently established. No product records or commercial values are reproduced.

### 23 April 2025
#### 🇪🇬 Egypt - Dar Al Teb
- **Ransomware Group:** gunra
- **Sector:** Healthcare
- **Website:** daralteb.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Dar Al Teb is one of Egypt's most renowned medical centers, specializing in reproductive medicine, in vitro fertilization (IVF), and women's health.
- **Analysis:** The gunra ransomware group claims the compromise of Dar Al Teb (daralteb.com) and displays data samples on its leak-site page. The samples show patient/cycle tracking tables including husband name, wife name, file number, age, two phone numbers, and IVF-specific clinical fields (fresh/frozen semen status, expected oocyte/embryo counts, referring andrologist, referring doctor, and embryology outcome codes). A broader local set includes seven monthly workbooks (December 2022, then March through August 2023) totaling approximately 2,300 rows of patient/cycle records, plus two shorter additional workbooks and an Access database (not opened). The reviewed technical material includes a WLAN profile export containing a cleartext pre-shared key, associated network commands referencing an internal file share, a PowerShell script for deploying an Active Directory forest named "DarAlteb.local", and a preconfigured RDP connection file targeting an internal host with clipboard and smart-card redirection enabled. The combination of individually identifiable clinical data samples, a multi-year patient dataset and internal network/remote-access configuration material supports a high confidence assessment of a genuine, extensive compromise extending beyond a simple leak-site claim. The nature of the observed data, both individually identifiable reproductive-health information covering several thousand patients and internal infrastructure access material, supports a Level 4 impact rating. AFRINTEL does not reproduce any patient name, phone number, file number, Wi-Fi key, IP address or other personal data or secret from the reviewed material.

## May 2025

### 01 May 2025
#### 🇿🇦 South Africa - South African IT firm - iOCO (Subsidiary of EOH)
- **Ransomware Group:** devman
- **Sector:** Technology / Managed Services (MSP) / Cloud
- **Website:** https://www.eoh.co.za / ioco.tech
- **Status:** Claim - Unverified
- **Victim Description:** EOH is one of South Africa's largest technology service and consulting providers, offering digital transformation and infrastructure solutions. The Devman group used a generic description ("South African IT firm") on its leak site, a common tactic to maintain pressure during negotiation phases.

### 01 May 2025
#### 🇿🇦 South Africa - DovesIT
- **Ransomware Group:** devman
- **Sector:** Information Technology (IT) / Managed Services (MSP)
- **Website:** https://dovesit.co.za
- **Status:** Claim - Unverified
- **Victim Description:** DovesIT is a South African Managed Service Provider (MSP). The company offers backup solutions, cloud hosting, network maintenance, and cybersecurity for small and medium-sized enterprises (SMEs) in South Africa.

### 01 May 2025
#### 🇿🇦 South Africa - South African HR company
- **Ransomware Group:** devman
- **Sector:** Business Services / Human Resources
- **Website:** Not identified with sufficient confidence
- **Status:** Claim - Unverified
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
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** South African Airways (SAA) is the national airline and the largest in South Africa, operating domestic and international flights.
- **Analysis:** AFRINTEL reviewed a local sample of documents consistent with the claim made by the threat actor incransom, consisting of internal records from SAA Technical, the airline's aircraft maintenance, repair and overhaul (MRO) division. The material includes EASA/SACAA Part-145 regulatory documents (Maintenance Organisation Exposition, capability list, list of certifying and support staff), a Certificate of Authority for a certifying aircraft mechanic bearing a name, photo, employee and approval number and a multi-country licence scope, commercial quotations and financial records (credit authorisation sheets, debtor codes, cost analyses, component reconciliation exports referencing the AMOS maintenance-management system), and a lease agreement between Dube TradePort Corporation and Air Chefs SOC Limited, an SAA subsidiary. The documents reference multiple third-party MRO customers, including Comair, Air Namibia, Yemenia and the state defence-procurement entity Armscor. The presence of internally consistent, multi-year operational, regulatory and financial records naming specific SAA Technical systems and subsidiaries supports a high confidence assessment of a genuine internal compromise. The exposure of certifying-staff identity and licensing data, together with regulatory approval documentation and third-party client and defence-related commercial records, creates a risk of targeted phishing, aviation-safety oversight disruption and client/supply-chain impact extending beyond SAA itself. AFRINTEL does not reproduce any employee name, photograph, licence number or client financial detail from the reviewed sample.

### 19 May 2025
#### 🇰🇪 Kenya - NSSF (National Social Security Fund) KENYA
- **Ransomware Group:** devman
- **Sector:** Government / Social Services
- **Website:** www.nssf.go.ke
- **Status:** Claim - Data Sample Published
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** National Social Security Fund of Kenya, the statutory body managing mandatory pension and social-security contributions for Kenyan workers. The actor demands $4.5 million USD.
- **Analysis:** Material dated 15-18 May 2025 is consistent with genuine administrative-level access to NSSF's internal Windows environment. The material includes a ransom-note text file opened on a compromised desktop, stating that the "DevMan Cybersecurity Collective" compromised NSSF's systems at 9 PM UTC on 17 May 2025, encrypted critical systems and files, destroyed cloud and network-based backups, and exfiltrated sensitive data including employee personal records, client financial information and pension details; the note references Kenya's Data Protection Act, 2019 and threatens regulatory fines and client lawsuits. Separate material shows Windows Server Manager sessions for at least two domain-joined production servers (a mail/web-facing host and a large-capacity document-management host, both joined to an NSSF domain), dated 15 and 16 May 2025, and a file-explorer view listing drives consistent with an Exchange mail database and virtualization infrastructure, dated 17 May 2025. Additional reviewed material consists of dozens of scanned physical pension-benefit payment forms bearing the NSSF Board of Trustees letterhead, member and employer reference numbers, and payment amounts. The combination of a detailed ransom note matching the actor's typical playbook, evidence of genuine domain-level server access across multiple production systems, and scanned archival pension records supports a very high confidence assessment of a large-scale compromise affecting critical national social-security infrastructure. The full claimed volume of 2.5 TB and the $4.5 million ransom demand are not independently verified beyond what is stated in the actor's own material; no employee or member name, account or reference number, credential, or other individual record is reproduced.

### 20 May 2025
#### 🇧🇼 Botswana - Medswana
- **Ransomware Group:** killsec
- **Sector:** Pharmacy / Healthcare
- **Website:** medswana.co.bw
- **Status:** Claim - Data Sample Published
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

### 21 May 2025
#### 🇿🇦 South Africa - Anglo American plc
- **Ransomware Group:** arkana
- **Sector:** Mining
- **Status:** Claim - Unverified
- **Website:** angloamerican.com
- **Victim Description:** Anglo American plc is a multinational mining company based in Johannesburg and London. It is the world's largest producer of platinum and diamonds, with operations in over 40 countries. It also mines copper, nickel, iron ore, and coal.

### 23 May 2025
#### 🇿🇦 South Africa - netstar
- **Ransomware Group:** devman
- **Sector:** Technology / Telematics / IoT Security
- **Website:** netstar.co.za
- **Status:** Claim - Unverified
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

### 31 May 2025
#### 🇨🇲 Cameroon - ASCOMA Cameroon
- **Ransomware Group:** worldleaks
- **Sector:** Insurance
- **Website:** ascoma.com
- **Status:** Claim - Data Sample Published
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

## June 2025

### 02 June 2025
#### 🇲🇦 Morocco - ANCFCC (Agence Nationale de la Conservation Foncière)
- **Incident type:** Data Leak
- **Actor / Group:** nightspire
- **Sector:** Government / Real Estate and Land Registry.
- **Website:** https://www.ancfcc.gov.ma/
- **Status:** Claim - Data Sample Published
- **Victim Description:** The ANCFCC is the vital body responsible for land registration, cadastre, and cartography in Morocco. NightSpire's original claim cited a 3.1 GB leak comprising over 10,080 property certificates.
  A forum post attributed to vyngrich advertised several collections presented as originating from ANCFCC: more than 10,000 sample property certificates, a claimed underlying set exceeding 10 million certificates, and 20,000 sample documents from a collection allegedly exceeding 4 million documents and 4 TB. The claimed categories included property deeds, civil-status records, identity documents, passports and banking documents, as well as a folder allegedly concerning senior officials and public figures. AFRINTEL does not reproduce identities. AFRINTEL subsequently obtained and reviewed local archive copies of the claimed release, confirming the presence of several thousand individual property-certificate PDF files, sequentially named (e.g. CERTIFICAT_1.pdf through numbers in the thousands), consistent with the claimed sample size, together with a separately labelled folder referencing senior officials and public figures; AFRINTEL did not open or analyse the contents of that folder and does not reproduce any identities from it. The proximity between the more-than-10,000 certificate sample and NightSpire’s 10,080 certificates suggests possible overlap, republication, resale or amplification. The July post is retained as supplementary reporting and is not counted as a separate incident. The authenticity, age, completeness and technical origin of the additional claimed collections remain unknown.

### 02 June 2025
#### 🇲🇦 Morocco - Bar Association Portal (avocatsmaroc.com / mossaada.ma)
- **Incident type:** Data Leak
- **Actor / Group:** B4baYega
- **Sector:** Legal Services / Professional Association
- **Website:** avocatsmaroc.com / mossaada.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** avocatsmaroc.com is a Moroccan legal-profession portal supporting lawyers' case and enforcement-procedure management; mossaada.ma is an associated legal-aid platform.
- **Analysis:** AFRINTEL reviewed application source code and SQL database backups referencing the domains bureau.avocatsmaroc.com and app2.mossaada.ma, distributed by the actor B4baYega alongside a password-protected archive. The application's PHP source files use Arabic-transliterated function and field names consistent with judicial case-management and enforcement terminology (e.g. "Tanfid"/enforcement, "Khazina"/treasury or fund, "Tabligh"/notification, "Diligence", "Tribunal"), together with client-search, client-record-modification and diligence-tracking functions, and multiple dated SQL backup files. This indicates a compromise of a legal case-management application used by or for Moroccan lawyers, rather than a simple static website. AFRINTEL did not extract or review the SQL backups' row-level content and does not reproduce any client names, case references or other personal data from the reviewed sample. The scope and volume of records actually contained in the backups could not be independently confirmed.

### 06 June 2025
#### 🇲🇦 Morocco - MTT EXPERTISES
- **Ransomware Group:** incransom
- **Sector:** Business Services
- **Website:** https://mttexpertises.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** MTT Expertises is a multidisciplinary engineering and expertise firm based in Casablanca (with offices in Agadir and Tangier).
- **Analysis:** AFRINTEL reviewed a small local sample of documents consistent with the claim made by the threat actor incransom, including an unredacted client cheque issued by a Casablanca-based company and made payable through Crédit du Maroc, showing a full bank account number, a banking attestation issued by Crédit du Maroc confirming an account held by MTT Expertise, a client invoice referencing an agri-food company (Quality Tomatos Morocco) with its bank account details, and an industrial-site floor plan ("Plan de masse") bearing the MTT Expertises logo, consistent with an asset-valuation and insurance-loss-assessment engagement. The presence of genuine banking instruments and site-survey documentation tied to distinct third-party clients, together with MTT Expertises' own banking attestation, supports a medium confidence assessment of an actual compromise of the firm's internal files. The exposure of client and firm banking details creates a risk of payment fraud and business email compromise against MTT Expertises and its corporate clients. AFRINTEL does not reproduce any bank account number, cheque number or client name from the reviewed sample.

### 06 June 2025
#### 🇿🇦 South Africa - Ingonyama Trust Board
- **Ransomware Group:** nightspire
- **Sector:** Land Administration / Public Sector.
- **Website:** ingonyamatrust.org.za
- **Status:** Claim - Unverified
- **Victim Description:** The Ingonyama Trust Board (ITB) is a South African administrative authority responsible for managing approximately 2.8 million hectares of communal land in KwaZulu-Natal province.

### 06 June 2025
#### 🇲🇦 Morocco - Best Profil (bestprofil.ma)
- **Ransomware Group:** lynx
- **Sector:** Human Resources / Recruitment / Temporary Work.
- **Website:** https://bestprofil.ma
- **Status:** Data Fully Published
- **Victim Description:** Best Profil is one of the leaders in recruitment and temporary work in Morocco. The Lynx group describes this as a total exfiltration of 26 GB, now freely accessible on its leak site after ransom negotiations reportedly failed.
- **Analysis:** AFRINTEL reviewed a local sample of the leaked material, consisting of internal administrative and operational documents referencing "PEGASE" (an internal system/tool), staff attendance and payroll-tracking spreadsheets, invoice-verification and billing-detail files, and a client-complaint record for an industrial site. The presence of internal system manuals, payroll and timekeeping data and site-level administrative correspondence is consistent with a genuine internal-systems compromise rather than a superficial claim. The exposure of staff attendance, payroll and billing records creates a risk of payroll fraud, business-email compromise and social engineering against Best Profil's staff and corporate clients. AFRINTEL does not reproduce any employee names, client names or financial figures from the reviewed sample.

### 08 June 2025
#### 🇩🇿 Algeria - Crédit Populaire d'Algérie (cpa-bank.dz)
- **Incident type:** Data Leak
- **Actor / Group:** TajineSec / Tajinesec_MA (publication claim)
- **Sector:** Banking / Financial Services.
- **Website:** https://cpa-bank.dz
- **Status:** Claim - Unverified
- **Victim Description:** Crédit Populaire d'Algérie (CPA) is one of the country's main public banks. TajineSec claims to have exfiltrated more than 30 GB, including identity documents, employee and customer information, banking and money-transfer records, and internal administrative documents. A 500 MB sample is announced but is not visible in the supplied evidence.
- **Analysis:** The publication documents a public claim attributed to TajineSec / Tajinesec_MA and describes potentially highly sensitive banking and identity data. The compromise, the claimed volume, the alleged Moroccan attribution, and the publication of the announced sample are not independently verified. The status therefore remains **Claim - Unverified**.

### 09 June 2025
#### 🇩🇿 Algeria - Algérie Télécom (algerietelecom.dz)
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Telecommunications / National Internet Infrastructure
- **Website:** [algerietelecom.dz](https://www.algerietelecom.dz)
- **Status:** Claim - Data Sample Published
- **Victim Description:** Algérie Télécom is the incumbent operator and main provider of fixed internet and fixed telephony access in Algeria, operating the national network infrastructure linking regional access points to international content servers.
- **Analysis:** Phantom Atlas claims full access to Algérie Télécom's internal internet network map for the Tizi Ouzou, Boumerdes and Bouira provinces, stating it holds detailed information on the critical infrastructure connecting access points (BNG) to global content servers (FNA, GGC), as well as core routers, content distribution rings and per-municipality data consumption.

  The reviewed material shows interfaces of a "Network Weathermap"-type network monitoring tool, displaying several distinct topology maps: a diagram of the Tizi Ouzou BNG project with identified routers (PE-01, PE-02, ASBR-01, ASBR-02) and peering links to Google (GGC) and Facebook (FNA) with traffic loads in Gbit/s; a regional metro-loop diagram naming dozens of sites and municipalities across the provinces concerned; and a detailed bandwidth-consumption table by municipality for Tizi Ouzou, Boumerdes and Bouira. A second message states that access had been maintained since at least May 28, 2025 (noting a connection drop during a test on that date) and claims to hold data going beyond simple maps.

  The technical consistency of the observed interfaces (a real network monitoring tool, plausible equipment and site designations, traffic figures consistent across the different views) supports a high confidence level regarding authentic access to an internal Algérie Télécom monitoring system, at least for the provinces mentioned. The disclosure of detailed network maps of a national telecom operator constitutes a critical exposure that could facilitate targeted infrastructure mapping ahead of further intrusions, denial-of-service attacks against identified links, or service disruption in the affected areas. AFRINTEL does not reproduce any topology detail, equipment identifier or additional traffic figure beyond what is necessary to characterize the nature of the exposure.

### 09 June 2025
#### 🇬🇭 Ghana - Priority Insurance Company Limited
- **Incident type:** Data Leak
- **Actor / Group:** 0x0day, post published on the cybercriminal forum DarkForums
- **Sector:** Insurance / Financial Services
- **Website:** priorityinsuranceghana.net
- **Status:** Claim - Data Sample Published
- **Victim Description:** Priority Insurance Company Limited is a Ghanaian non-life insurance company headquartered in Accra, licensed by the National Insurance Commission (NIC) and operating a network of more than 30 branches across the country, including Accra, Kumasi, Tema, Cape Coast and Ho.
- **Analysis:** AFRINTEL identified the originating post, titled "GHANA Inusrance database", published on the cybercriminal forum DarkForums by the account 0x0day on 9 June 2025, superseding an earlier under-investigation record that had provisionally placed this dataset in February 2025 based only on a file-modification timestamp with no located source post. The post displays a JSON sample record consistent with an internal policy-management export, with fields including a customer ID, policy number, branch ID and branch name (Tema), customer type, full name, email, phone number, digital/postal/residential address, tax identification number, company ID and company name (explicitly "Priority Insurance Company Limited"), and a national ID field. This matches the structure and branch network (Accra, Kumasi, Tema, Cape Coast, Ho, Bolga) of the customer-database file previously reviewed by AFRINTEL, which contained 349,288 records including roughly 159,000 with an email address and roughly 159,000 with a national ID number. The combination of a confirmed source account, an explicit publication date and a sample matching the previously reviewed dataset raises the confidence level from under investigation to a dated, attributed claim. Given the volume of records and the combination of national identity numbers, dates of birth, occupation, contact details and insurance policy association, exposure of this dataset would create a significant risk of identity theft, insurance fraud and targeted phishing against policyholders. AFRINTEL does not reproduce any customer name, phone number, address, national ID number or date of birth from the reviewed material.

### 11 June 2025
#### 🇲🇺 Mauritius - Currimjee Jeewanjee & Co
- **Ransomware Group:** warlock
- **Sector:** Conglomerate / Multi-sectoral
- **Website:** https://www.currimjee.com
- **Status:** Claim - Unverified
- **Victim Description:** One of the oldest and most important conglomerates in Mauritius, operating in telecommunications (Emtel), energy, real estate, tourism, and financial services.

### 11 June 2025
#### 🇩🇿 Algeria - Banque Nationale d'Algérie (bna.dz)
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Banking / Financial Services.
- **Website:** https://bna.dz / https://ebanking.bna.dz
- **Status:** Claim - Unverified
- **Victim Description:** The Banque Nationale d'Algérie (BNA) is the primary commercial bank of the Algerian state. The actor claims a massive exfiltration of 90 GB with a partial publication of 7 GB; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.
- **Analysis:** An earlier Phantom Atlas message, posted on June 10, 2025 on the actor's Telegram channel, provides further detail on this claim: the group states it holds more than 90 GB of documents covering the 2016-2025 period, with a staged release plan ("we will start with 2016 ones"), the archive being protected by the password `phantomatlas`. The download link mentioned on DarkForums is no longer accessible at the time of writing this entry; AFRINTEL was therefore unable to collect or review the claimed archive, and cannot confirm either the completeness or the authenticity of the announced content.

### 11 June 2025
#### 🇿🇦 South Africa - carducci
- **Ransomware Group:** warlock
- **Sector:** Retail (Fashion)
- **Website:** http://carducci.co.za/
- **Status:** Claim - Unverified
- **Victim Description:** Carducci is a South African fashion brand based in Cape Town, founded in 1978. It specializes in elegant menswear, including suits, casual wear, and accessories. The brand is renowned for its craftsmanship and refined fabrics. Carducci is part of the Seardel group.

### 14 June 2025
#### 🇪🇬 Egypt - Ministry of Social Solidarity
- **Incident type:** Data Leak
- **Actor / Group:** Keymous
- **Sector:** Government / Public Administration / Social Affairs
- **Website:** [moss.gov.eg](https://www.moss.gov.eg)
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Ministry of Social Solidarity is an Egyptian government administration responsible for policies and services related to social protection and social affairs.
- **Analysis:** A post attributed to the actor Keymous presents data allegedly obtained from the ministry and involving government and institutional representatives from several countries. The publication advertises confidential documents and personal information relating to ministers, government officials and institutional representatives from several African, Arab and Asian countries, specifically mentioning passports or identity documents, names, phone numbers and email addresses; the actor claims a total of 237 elements, described in the post as "Line and file".

  The CSV sample reviewed by AFRINTEL contains 26 records across 8 columns: `Name`, `Phone`, `Email`, `Title / Position`, `Country`, `City`, `Passport / ID` and `Photos`. The records cover Egypt, Djibouti, Benin, Burkina Faso, Senegal, Morocco, Sudan, Türkiye, the United Arab Emirates, Malaysia, Indonesia and Kuwait, as well as OIC-affiliated organisations. All 26 records contain names, phone numbers, email addresses, professional positions and passport or identity document references, and several positions correspond to government, diplomatic or institutional officials. The `Photos` column also contains the value "Back" for 5 records, although no image is directly embedded in the supplied CSV; several location values are missing or represented by a placeholder, and at least one email address is partially masked.

  The combination of identity information, direct contact details and institutional positions creates a significant risk of spear phishing, identity impersonation, document fraud and targeted social engineering, and the exposed professional roles could help an actor identify high-value individuals and build contextualised campaigns against government entities or partner organisations. The forum post includes a download link presented as the "Full file", but the CSV supplied to AFRINTEL contains only 26 records against the 237 elements claimed; the reviewed material should therefore be treated as an observed sample rather than confirmation that the complete claimed dataset was obtained. No asking price is displayed and the data is not presented as being offered for sale. AFRINTEL does not reproduce any name, phone number, email address, passport/ID reference or other personal data from the reviewed sample.

### 14 June 2025
#### 🇩🇿 Algeria - Ministry of Youth and Sports (MJS) / Directorates of Youth and Sports (DJS)
- **Incident type:** Data Leak
- **Actor / Group:** mrdump, post published on a cybercriminal forum (DarkForums)
- **Sector:** Government / Public Administration / Youth and Sports
- **Website:** [mjs.gov.dz](https://www.mjs.gov.dz)
- **Status:** Data Fully Published
- **Victim Description:** The Ministry of Youth and Sports (MJS) is the Algerian government administration in charge of youth and sports policy, supported by a network of Directorates of Youth and Sports (DJS) in each wilaya. The reviewed documents mostly concern the Boumerdes wilaya directorate, along with correspondence from other wilayas (Illizi, El Meghaier, Tlemcen, Bechar) and the central ministry.
- **Analysis:** The actor mrdump posted a claim on a cybercriminal forum (DarkForums) that the ministry's database had been breached, along with a link to an external Telegram channel presented as the source of the full publication. The post states that "all sensitive files and internal data" of the ministry have been published.

  AFRINTEL directly reviewed the full set of files associated with this post, totaling approximately 730 MB across 772 files (610 PDFs, 109 images, 22 unextracted RAR archives, 20 Excel workbooks, plus a few Word documents, videos and text files). The content consists of authentic-looking internal administrative correspondence: budget monitoring and program execution notes (DIEEP notes, draft settlement bills, payment credit requirements), sports infrastructure inventories (stadiums, pools, multi-purpose gyms), youth holiday and camp programs, inter-wilaya twinning agreements, an information databank listing youth institutions, and a circular addressed to youth and sports directors across several wilayas. Document dates range from around 2014 to early June 2025, with the most recent file predating the June 14, 2025 post by only a few days.

  Two Excel workbooks display an abnormally high row count (roughly 1,047,700 rows each) due to a formatting artifact from an accounting-system export; only about a dozen rows actually contain data in each file, corresponding to budget nomenclature fields (program, sub-program, action, category, spending officer) rather than a massive volume of individual records.

  A standalone text file contains an excerpt from an individual career file of a ministry employee (name, original grade, hiring date), confirming exposure of named HR data in addition to the administrative correspondence. The 22 attached RAR archives were not extracted by AFRINTEL, so their exact contents remain unverified beyond their filenames, which reference activity reports, association-funding case files and partnership-related documents.

  The internal consistency of the corpus (official letterheads, a structure consistent with Algerian public administration, a plausible chronology, and a named employee reference) and its volume support a high confidence level regarding authentic access to internal data of the ministry or one of its decentralized directorates. This exposure could facilitate impersonation of civil servants, targeted phishing against the nationwide network of wilaya directorates, reconstruction of the ministry's internal budget organization, and exploitation of HR career data. AFRINTEL does not reproduce any name, HR data, personal contact detail or document from the reviewed corpus.

### 18 June 2025
#### 🇩🇿 Algeria - Ministry of National Defense (MDN)
- **Incident type:** Data Leak
- **Actor / Group:** mrdump, post published on a cybercriminal forum (DarkForums)
- **Sector:** Defense / National Security
- **Website:** Not specified (internal file, no institutional domain visible)
- **Status:** Claim - Unverified
- **Victim Description:** The Ministry of National Defense (MDN) is the Algerian administration responsible for national defense. The post claims to have obtained classified internal documents related to the ministry's logistics and supply chain operations.
- **Analysis:** The actor mrdump, already behind a post targeting the Ministry of Youth and Sports on June 14, 2025, published a new claim on June 18, 2025, this time concerning the Ministry of National Defense, announcing the acquisition of "classified internal documents" related to logistics and supply chain operations.

  An Excel file titled "جدول اللوجستيك لوزارة الدفاع" ("Ministry of Defense logistics table") was shared with AFRINTEL in connection with this post. Given the claimed nature of the document (material presented as classified, related to national defense), AFRINTEL performed a limited, non-content structural review: the workbook is an XLSX file of approximately 15 KB containing one worksheet, 77 rows and 14 columns; roughly 65 populated rows form a repeated structured table, while the remaining rows are document headings or other non-record content. AFRINTEL did not reproduce or extract names, identifiers, locations, quantities, procurement details or other potentially sensitive values.

  The file structure is consistent with a logistics-related administrative table, but the structural review does not establish that the document is authentic, classified, current, complete or sourced from the Ministry of National Defense. The claim therefore remains recorded as unverified. If the claimed provenance were confirmed, exposure of military logistics or supply-chain information could create a high national-security risk; this is a conditional impact assessment, not a confirmation of compromise.

### 18 June 2025
#### 🇲🇦 Morocco - Ministry of National Education (men.gov.ma / massar.men.gov.ma)
- **Incident type:** Data Leak
- **Actor / Group:** RiseAgainLuigi & B4baYega
- **Sector:** Government / Education.
- **Website:** https://men.gov.ma / massar.men.gov.ma
- **Status:** Claim - Unverified
- **Victim Description:** The Ministry of National Education of Morocco. The Massar platform is the ministry's digital backbone, centralizing grades, registrations, and tracking for all students in the Kingdom. The actors claim a data leak and sale listing of over 6 million records; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 19 June 2025
#### 🇩🇿 Algeria - General Directorate of Customs (DGD) / Export and Import Control Service
- **Incident type:** Data Leak
- **Actor / Group:** mrdump (Telegram channel "Server dump")
- **Sector:** Government / Customs and Foreign Trade
- **Website:** [douane.gov.dz](https://www.douane.gov.dz)
- **Status:** Claim - Unverified
- **Victim Description:** The General Directorate of Customs (DGD) is the Algerian administration responsible for customs control, collection of duties and taxes, and regulation of foreign trade, including through its Export and Import Control Service.
- **Analysis:** On June 19, 2025, the Telegram channel "Server dump" (attributed to the same actor, mrdump, behind the June 14 and June 18, 2025 posts) published an image stamped "HACKED" showing a dashboard presented as belonging to the Algerian General Directorate of Customs, along with a message claiming a "takeover of the information system" and "confirmed access to the digital infrastructure and the administration panel." A second message announced that customs documents would be highlighted allegedly showing Algeria exporting goods to Israel, in contradiction with Algeria's official position, and promised the imminent release of detailed PDF files.

  A ZIP archive containing two PDF files was shared with AFRINTEL in connection with this post: a "maritime and commercial shipment record" concerning the vessel "Captain Christos" (IMO 9475410), and a "document retention certificate" presented as issued by the DGD's Export and Import Control Service, both relating to an export from the port of Bejaia to the port of Ashdod (Israel) between April 20 and April 28, 2025.

  AFRINTEL's technical review of both PDFs revealed several converging indicators of fabrication rather than an authentic extraction from a customs system: the metadata of both files show an author named "Yassine," creation via Microsoft Word 2016, and conversion through the online service ilovepdf.com, with creation timestamps matching exactly the day of the post (June 19, 2025) — inconsistent with scanned documents or a direct export from a real information system. The IMO number cited for the vessel, 9475410, fails the standard IMO check-digit calculation (expected check digit: 6; digit given: 0), which is objective technical evidence that this vessel identifier is invalid. The certification document also cites an "executive decree No. 2021-10" dated "June 15, 2010," an internal inconsistency between the decree's number and its stated date. The Israeli importing companies named in the document (ChemImport LTD, Precious Metals Ltd, GasTech Israel, Fashion Importers) could not be verified and appear generic.

  These findings converge on a low-confidence assessment regarding the authenticity of the reviewed documents, which appear to have been drafted to support a pre-existing political narrative rather than extracted from a compromised system. This technical conclusion applies specifically to the two reviewed PDFs; it neither confirms nor independently rules out the separate claim of access to the DGD's administration dashboard, which is visible only via a published image and was not independently verified. Given the fabrication identified in the associated documentary material, the overall claim is assessed with a low confidence level. No named data, complete customs file reference, or other element that could validate or amplify the actor's narrative is reproduced.

### 19 June 2025
#### 🇲🇦 Morocco - Royal Moroccan Football Federation (FRMF)
- **Incident type:** Data Leak
- **Actor / Group:** Keymous
- **Sector:** Sports / Public Administration
- **Website:** https://frmf.ma/
- **Status:** Claim - Data Sample Published
- **Victim Description:** Founded in 1956, the FRMF is the body responsible for organizing, managing, and developing football in Morocco. It oversees national teams, professional and amateur competitions, as well as regional leagues.
- **Analysis:** AFRINTEL identified the source publication as a DarkForums post by the actor Keymous, titled "Football federation morocco Leak," claiming a database of FRMF players and staff covering more than 4,289 named records. AFRINTEL reviewed a local sample of documents consistent with FRMF's official registration and licensing records. The sample includes a FIFA Connect team-official registration record and a CAF Pro coaching-license record, each containing a full name, date of birth, gender, nationality, home address, phone number, a FIFA or license identification number, license validity date and a photograph, together with a club registration request form listing a license holder's full name, date and place of birth, national ID/passport number, nationality and affiliated club. Two small spreadsheet extracts, structured as a football-official/member registry (registration ID, status, name, nationality, date and year of birth, region, city, address, postal code, phone, email, club and badge/authorization code), were also present, covering roughly three dozen records combined, and match the field structure described in Keymous's post. This is consistent with exposure of parts of FRMF's official and licensing database rather than only generic administrative correspondence. At least one reviewed record concerns an individual whose date of birth indicates they were a minor around the time of registration. AFRINTEL does not reproduce any name, address, identification number, contact detail or photograph from the reviewed sample. The total scope, completeness and current validity of the underlying database could not be independently confirmed beyond the limited sample available.

### 20 June 2025
#### 🇲🇦 Morocco - INWI (inwi.ma)
- **Incident type:** Data Leak
- **Actor / Group:** Evil_BYTE_Officiel
- **Sector:** Telecommunications.
- **Website:** https://inwi.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** INWI is one of the three main telecommunications operators in Morocco, providing mobile, fixed-line, and internet services (ADSL/Fiber). The actor published a sample of sensitive data including PII (name, national ID), contact information and password hashes (bcrypt).

### 26 June 2025
#### 🇩🇿 Algeria - Ministry of Transportation
- **Incident type:** Data Leak
- **Actor / Group:** KickingPigs
- **Sector:** Government / Transportation
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Victim Description:** Algeria's Ministry of Transportation is the public administration responsible for national transportation policy and related administrative services.
- **Analysis:** A forum publication dated 26 June 2025, attributed to KickingPigs, presents an alleged leak from the Algerian Ministry of Transportation. The post lists vehicle-registration and transport-administration records, including names, national identification numbers, parent names, company registration numbers, vehicle and registration details, driving-licence documents and internal Excel files. The visible sample contains structured vehicle records and sensitive personal-data fields; AFRINTEL does not reproduce the records or identifiers. The authenticity, completeness and technical origin of the dataset could not be independently confirmed.

### 20 June 2025
#### 🇹🇳 Tunisia - Ministry of National Defense / Armed Forces
- **Incident type:** Data Leak
- **Actor / Group:** mrdump (publication on the Telegram channel \"Server dump\")
- **Sector:** Defense / National Security
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Tunisian Ministry of National Defense is the government administration responsible for national defense and the armed forces.
- **Analysis:** A publication dated 20 June 2025, attributed to mrdump, claims successful access to several systems belonging to Tunisia's Ministry of National Defense, specifically its Armed Forces division. The publication alleges that an underground weapons depot was discovered at Mount Chaambi in Kasserine Governorate and refers to thermal imagery, engineering plans and information concerning stored weapons and ammunition. An associated ZIP archive was provided to AFRINTEL; a non-content structural review identified 10 archive members (six PNG images, one XLSX workbook, one PDF and one JPG), approximately 6.2 MB compressed and 6.3 MB uncompressed. AFRINTEL did not open or reproduce the files because the material is presented as military and potentially operationally sensitive. The archive structure does not independently establish the authenticity, provenance, classification or completeness of the material, and the claimed access remains unverified.

### 29 June 2025
#### 🇩🇯 Djibouti - Embassy of Djibouti in Morocco
- **Incident type:** Data Leak

- **Actor / Group:** MdHackersArmy (post published by Doxeur23azi on a cybercriminal forum, DarkForums)
- **Sector:** Government / Diplomatic
- **Status:** Claim - Unverified
- **Website:** Not specified

- **Description:**
  The Embassy of Djibouti in Morocco is Djibouti's diplomatic mission accredited to the Kingdom of Morocco.

- **Analysis:**
  A post titled "Leak db of the Embassy of Djibouti in Morocco" was published on 29 June 2025 on the cybercriminal forum DarkForums by the account Doxeur23azi, crediting the claim to MdHackersArmy. The post consists solely of an external download link and does not describe the data type, field structure, record volume or sensitivity of the alleged database, and no sample is visible. AFRINTEL did not access the external link. The data at risk, the affected population and the technical origin of the claim remain unknown at this stage.

## July 2025

### 01 July 2025
#### 🇳🇬 Nigeria - Chartered Institute of Bankers of Nigeria (CIBN)
- **Incident type:** Data Leak
- **Actor / Group:** Hepd
- **Sector:** Financial Services / Professional Regulatory Body.
- **Website:** https://cibng.org
- **Status:** Claim - Data Sample Published
- **Victim Description:** The umbrella institution for the banking profession in Nigeria, responsible for the accreditation and ethics of bankers, including members of the Central Bank (CBN). The actor claims to have published a database including sensitive information on the country's banking elite, on the deep web. AFRINTEL reviewed the supplied CIBN archive structurally: 472 files and approximately 18 MB, including member addresses, bank details, employment, qualifications, documents, wallets, login-related tables, staff records, educational and fintech database exports, and access/logging artifacts. The archive also contains files named for member and user records. AFRINTEL did not reproduce any personal record, credential, token or document. The archive supports a substantial data-publication assessment, but its authenticity, completeness and direct provenance from CIBN remain independently unverified.

### 03 July 2025
#### 🇩🇿 Algeria - Algeria Post / ECCP
- **Incident type:** Data Leak
- **Actor / Group:** sanji_shi5 (source account)
- **Sector:** Postal Services / Financial Services
- **Website:** [poste.dz](https://www.poste.dz)
- **Source publication date:** 3 July 2025
- **Status:** Claim - Data Sample Published
- **Victim Description:** Algeria Post operates the ECCP service, which allows Algerian users to check postal-account balances and make online purchases. The supplied forum post displays a sample formatted as account identifiers and password-like values associated with ECCP/Algeria Post. No credential is reproduced or validated, and the underlying dataset was not collected.
- **Analysis:** The observed sample suggests a potential exposure of account-access data affecting a public postal and financial service. If valid, the data could enable account takeover, fraud and targeted phishing. The post identifies sanji_shi5 as the source account, but this does not independently confirm the compromise, the dataset's provenance or the validity of the displayed values.

### 08 July 2025
#### 🇿🇦 South Africa - MAFATE BUSINESS ENTERPRISE
- **Ransomware Group:** d4rk4rmy
- **Sector:** Industrial Supplies / Mining Support Services.
- **Website:** https://mafate.co.za
- **Status:** Claim - Unverified
- **Victim Description:** Mafate Business Enterprise is an industrial service provider established in Middelburg (Mpumalanga), at the heart of the South African mining region.

### 09 July 2025
#### 🇲🇦 Morocco - Fédération Nationale du Bâtiment et des Travaux Publics (FNBTP)
- **Incident type:** Data Leak
- **Actor / Group:** Evil_BYTE_Officiel
- **Sector:** Construction / Public Works / Professional Organisation
- **Website:** [fnbtp.ma](https://www.fnbtp.ma)
- **Status:** Data Fully Published
- **Victim Description:** The Fédération Nationale du Bâtiment et des Travaux Publics (FNBTP) is a professional organisation representing Moroccan companies operating in the construction and public works sector. On 9 July 2025, the actor Evil_BYTE_Officiel published on an underground forum a database attributed to the FNBTP and stated that the data was being released for free.
- **Analysis:** The publication exposes a table named `societe` containing information related to companies operating in the construction and public works sector. The fields listed in the publication are: `Id`, `nb_national`, `nb_regional`, `ENTREPRISE`, `secteur`, `adher`, `MONTANT_COTISATION`, `Responsable`, `Adress`, `Téléphone`, `Fax`, `GSM`, `VILLE` and `E-MAIL`.

  The CSV file analysed by AFRINTEL contains 180 rows and 14 columns. The observed data includes company names, internal references, membership-related information, contact persons, addresses, telephone numbers, fax numbers, mobile numbers, cities and professional email addresses.

  Among the 179 rows structured as company records, 166 contain a city, mainly Rabat, Salé, Temara and Khemisset. 146 contain a contact person, 145 a telephone number, 139 a fax number, 111 a mobile number and 81 at least one email address. Some records contain several contact details for the same company.

  An anomaly is present in the supplied file. The first row contains values that do not match the business structure observed throughout the remaining dataset. Subsequent records, including those visible in the underground forum post, are consistent with the structure described by the actor.

  The exposed information can support the mapping of companies operating in the construction sector and the identification of their representatives and direct contact details. Such information may be used to prepare spear phishing campaigns, impersonation attempts or targeted social engineering against companies and their business contacts.

  The data is published for free by the actor. No asking price or ransom demand is visible. The forum publication directly exposes database records and the analysed file confirms the presence of structured data. The incident therefore involves actual data publication rather than a claim without supporting material. AFRINTEL does not reproduce any company names, contact names or contact details from the reviewed sample.

### 13 July 2025
#### 🇹🇿 Tanzania - Twaweza
- **Ransomware Group:** nightspire
- **Sector:** NGO (Education & Governance)
- **Website:** https://twaweza.org
- **Status:** Claim - Unverified
- **Victim Description:** Twaweza East Africa is a leading pan-African organization, based in Tanzania (with offices in Kenya and Uganda).

### 14 July 2025
#### 🇲🇦 Morocco - IWACLUB (iwaclub.ma)
- **Incident type:** Data Leak
- **Actor / Group:** Keymous
- **Sector:** Telecommunications / Distribution & Retail.
- **Website:** https://iwaclub.ma
- **Status:** Claim - Unverified
- **Victim Description:** IWACLUB is the professional application dedicated to the reseller network of the company IWACO, one of the most important distributors of telecommunications solutions (notably the operator inwi) and technological products in Morocco.

### 14 July 2025
#### 🇩🇿 Algeria - Ministry of Energy, Mines and Renewable Energies / SARL SOPRETA
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Government / Energy and Mining; named third party: chemical industry / building waterproofing
- **Website:** Not specified for the ministry; no official website identified for SOPRETA
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Ministry of Energy, Mines and Renewable Energies is the Algerian authority issuing authorizations for the acquisition of hazardous materials and chemical products. SARL SOPRETA (Société des Produits d'Étanchéité Algériens), based in Ain El Arbaa, Ain Temouchent province, is a company named in the leaked document.
- **Analysis:** On July 14, 2025, Phantom Atlas published an accusation targeting Minister Mohamed Arkab, claiming that the ministry had granted, in March 2025, an import license for more than 10 tons of hazardous chemical substances to a company described as "virtually unknown, not appearing in any known industrial registry," in the absence of any oversight or transparent environmental reporting, insinuating an operation with murky objectives.

  AFRINTEL reviewed the documents attached to the post: authorization No. 1000 dated March 6, 2025, issued by the ministry to SARL SOPRETA; the attached list of authorized materials (anhydrous hydrochloric acid, nonylphenol ethoxylate under the commercial names Indulin W-5 and Indulin AA-83, up to 10 and 8 tons respectively); and a proforma invoice from the Belgian company MBM International SA (Brussels) addressed to SOPRETA for 6,531.60 kg of Indulin W5 and 2,517.30 kg of Indulin AA-83, totaling €43,257.54, with delivery to the port of Oran. The three documents are mutually consistent (same authorization number, same company address, same commercial product names).

  Contrary to Phantom Atlas's insinuation, AFRINTEL identified SARL SOPRETA (Société des Produits d'Étanchéité Algériens) in several public Algerian business directories, at the exact address stated in the authorization; it is an established company specializing in building waterproofing and the manufacture of basic inorganic chemical products, including bitumen-based products. "Indulin" products are lignin-based emulsifiers marketed for producing bitumen emulsions and road waterproofing products, which directly matches SOPRETA's declared line of business rather than suggesting a diverted or unidentified use. The authorization procedure itself (monthly declaration, compliance with hazardous chemicals regulations, oversight by the wilaya's energy and mines directorate, one-year validity) corresponds to an existing regulatory framework, which contradicts the claim of a "complete absence of oversight."

  AFRINTEL therefore assesses that the leaked document is probably authentic and consistent with a legitimate, declared industrial import, but that Phantom Atlas's accusatory framing (an "unknown" company, absence of oversight, opaque objectives) is not corroborated by publicly available information on SOPRETA. This leak nonetheless constitutes an unauthorized disclosure of an internal ministry administrative document as well as commercial data belonging to a third-party company (the Belgian supplier's banking details, contractual specifics). AFRINTEL does not reproduce any banking data or information that could identify individuals associated with this file.

### 14 July 2025
#### 🇰🇪 Kenya - ICT Authority (icta.go.ke)
- **Incident type:** Data Leak
- **Actor / Group:** Unknown
- **Sector:** Government / Digital Infrastructure
- **Website:** [icta.go.ke](http://icta.go.ke)
- **Status:** Claim - Data Sample Published
- **Victim Description:** Kenya's ICT Authority is a public-sector technology institution responsible for coordinating and supporting government information and communication technology infrastructure and services.
- **Analysis:** AFRINTEL reviewed the supplied CSV export without reproducing personal data. The file contains 1,697 data rows and fields for display name, phone, email, identifier, mobile contact, name, address-related fields, user references and website links. The structure is consistent with an organisational contact or directory export containing ICT Authority personnel, public-sector contacts and associated technology-service records. The file metadata places the evidence on 14 July 2025; this is treated as an evidence/discovery date, not a confirmed publication or intrusion date. The available material does not identify the threat actor, publication venue, access method or complete dataset scope. The exposed contact and organisational information could support targeted phishing, impersonation and social engineering against Kenyan public-sector and technology stakeholders. AFRINTEL records this as a data-leak claim with a published sample and does not reproduce names, phone numbers, email addresses, identifiers or addresses.
### 15 July 2025
#### 🇰🇪 Kenya - Adrian Kenya
- **Ransomware Group:** lynx
- **Sector:** Telecommunications / Energy Infrastructure / ICT.
- **Website:** https://adrian.co.ke / www.adriankenya.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Adrian Group (Adrian Kenya) is a Kenyan leader in technological engineering.
- **Analysis:** AFRINTEL reviewed a small local sample of four documents associated with this claim: a vendor invoice for telecom site installation work (antennas, feeder cable and RRU installation) issued to Adrian Kenya, a Kenya Revenue Authority (KRA) VAT payment slip for Adrian Group Limited covering January to March 2025, a fuel-supplier credit note addressed to Adrian Kenya Limited with vehicle, banking and payment-advice details, and an internal email thread between Adrian Kenya and Adrian Group staff (adriankenya.com and adriangroup.tech domains) discussing a telecom site rollout at a warehouse location. The documents are internally consistent, referencing matching company names, domains and project context, and include full personal identifiers, banking details and a tax PIN, none of which AFRINTEL reproduces here. The sample indicates exposure of financial, tax-compliance, vendor and internal-communication records, but its scope is limited to four documents and does not establish the total volume or extent of the underlying compromise. AFRINTEL does not independently confirm the intrusion.

### 15 July 2025
#### 🇪🇬 Egypt - Egyptian Electricity Holding Company (EEHC, eehc.gov.eg)
- **Ransomware Group:** devman
- **Sector:** Government / Energy (Electricity)
- **Website:** https://eehc.gov.eg
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** The Egyptian Electricity Holding Company (EEHC) is the state holding company overseeing electricity generation, transmission and distribution across Egypt, including its regional distribution subsidiaries. The actor demands $2,270,000 USD.
- **Analysis:** AFRINTEL reviewed a directory listing (not the underlying file contents) of an alleged internal file share hosted on a MEGA cloud mount, comprising roughly 8,000 folders and more than 50,000 file entries. The dominant file types are spreadsheets (over 31,000 Excel files) and PDFs (nearly 4,000), alongside Word documents, images and a small number of email exports. The folder structure includes subdirectories named after EEHC's regional distribution companies (matching Egypt's real electricity distribution structure: Alexandria, Canal, Beheira, Middle Egypt, North Delta, South Cairo and South Delta), employee-named personal folders, and material referencing Oracle Utilities Customer Care & Billing (CC&B), Meter Data Management (MDM) and Customer Self Service (CSS) systems, together with technical proposals and meeting records tied to a smart-meter (AMI) rollout programme. The consistency between this folder structure and EEHC's known regional and system architecture supports a high confidence assessment that the listing reflects genuine internal access, though AFRINTEL has not opened or verified the contents of individual files. Given the scale of the listing and EEHC's role as Egypt's national electricity holding company, potential exposure would combine employee personal data, internal operational and billing-system documentation, and technical infrastructure records for a critical national utility. AFRINTEL does not reproduce any employee name, file content or folder path containing personal identifiers from the reviewed listing.

### 15 July 2025
#### 🇳🇦 Namibia - Otjiwarongo Municipality
- **Ransomware Group:** incransom
- **Sector:** Public Administrations / Local Government.
- **Website:** www.otjimun.org.na
- **Status:** Claim - Data Sample Published
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** The municipality of Otjiwarongo is the local government body for the city of Otjiwarongo, capital of the Otjozondjupa region in Namibia.
- **Analysis:** AFRINTEL reviewed a local sample of documents consistent with the claim made by the threat actor incransom, consisting of an unredacted extract from the municipality's VIP Payroll System, a remuneration list for the pay period ending 28 February 2025 listing dozens of employee records with employee code, department, full name, net pay amount in Namibian dollars, bank code and bank account number. The document bears genuine system headers identifying it as an official municipal payroll run ("001 Municipality of Otjiwarongo"), consistent with a real internal HR/payroll system compromise rather than a fabricated sample. The combination of employee identity, remuneration and full banking details for a local government payroll supports a very high confidence assessment. Exposure of this data creates a significant risk of payroll fraud, targeted phishing and identity-related fraud against municipal employees. AFRINTEL does not reproduce any employee name, employee code, salary amount or bank account number from the reviewed sample.

### 15 July 2025
#### 🇲🇷 Mauritania - QCE Portal (qce.gov.mr)
- **Incident type:** Data Leak
- **Actor / Group:** Unknown
- **Sector:** Government / Public Procurement (Enterprise and Personnel Qualification)
- **Website:** qce.gov.mr
- **Status:** Claim - Data Sample Published
- **Victim Description:** qce.gov.mr is a Mauritanian government online platform used to host and process personnel and enterprise qualification dossiers, consistent with contractor/technical-staff vetting for public works and procurement processes; its precise institutional mandate could not be independently confirmed from the reviewed sample.
- **Analysis:** AFRINTEL reviewed a local sample of files consistent with personnel qualification dossiers submitted through the platform, including curricula vitae, national identity cards (CIN), academic diplomas, notarized employment-contract deposits and related supporting documents for individuals employed by several distinct Mauritanian private companies (including construction, drilling and technical-services firms). The documents display genuine official letterheads, notary seals and structured personal-data fields (full name, national identification number, date and place of birth, employer, position, signature, photograph), consistent with a real qualification/procurement dossier repository rather than fabricated content. No claiming actor, publication venue or forum post could be identified for this dataset; the sample was dated from local file metadata (mid-July 2025) in the absence of an explicit publication date. The combination of national ID numbers, diplomas and employment records for numerous private individuals creates a significant risk of identity fraud, document forgery and targeted social engineering against affected candidates and their employers. AFRINTEL does not reproduce any individual's name, national identification number, date of birth, employer contact details or signature from the reviewed sample.

### 18 July 2025
#### 🇲🇦 Morocco - Mohammed VI Polytechnic University (UM6P)
- **Incident type:** Data Leak
- **Actor / Group:** Mercobyte
- **Sector:** Education / Higher Education
- **Website:** https://um6p.ma
- **Status:** Claim - Unverified
- **Victim Description:** An excellence institution (University) based in Benguerir, a strategic hub for research, innovation, and executive training in Morocco. The actor claims a targeted data leak and influence operation, publishing student ID photos accompanied by a political message; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 25 July 2025
#### 🇹🇳 Tunisia - Ministry of Finance (finances.gov.tn)
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Government / Tax Administration.
- **Website:** https://finances.gov.tn
- **Status:** Claim - Unverified
- **Victim Description:** Tunisian Ministry of Finance.
- **Analysis:** AFRINTEL did not directly review technical evidence isolated to finances.gov.tn beyond the actor's "Full Access" claim. However, a credential-store export reviewed alongside this claim, attributed to the same Dark 07x Team campaign on the same date, contained dozens of plaintext username/password pairs for a separate Tunisian institution (the Academy of Banks and Finance, ABF), suggesting the actor pivoted between compromised organizations and reused harvested credentials across targets during this campaign. AFRINTEL does not reproduce any of the exposed credentials.

### 25 July 2025
#### 🇹🇳 Tunisia - Academy of Banks and Finance (abf.tn)
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Professional Training / Banking Sector.
- **Website:** abf.tn
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Academy of Banks and Finance (ABF) is the continuing education body of the Tunisian Professional Association of Banks and Financial Institutions (APTBEF).
- **Analysis:** Material shows an authenticated administrative session on the ABF website under a named staff account, confirming access beyond a simple claim. A separate credential-store export associated with the same campaign contained several dozen plaintext username/password pairs for ABF-linked platforms, including its video-conferencing/webinar system, its e-learning ("formation à distance") portal and a WordPress administration login, alongside a handful of associated email addresses. No exposed credentials or email addresses are reproduced.

### 25 July 2025
#### 🇹🇳 Tunisia - BTK Bank
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Banking / Financial Services.
- **Website:** https://btknet.com
- **Status:** Claim - Data Sample Published
- **Victim Description:** BTK Bank (Banque Tuniso-Koweïtienne) is a Tunisian banking institution resulting from a Tunisian-Kuwaiti joint venture.
- **Analysis:** Material shows a live, authenticated e-banking session on btknet.com, including an account listing, a wire-transfer initiation screen showing a beneficiary list, and a customer bank-identity statement (RIB/IBAN) for a named account holder, confirming an actual account takeover rather than a simple claim. The associated forum post, attributed to a collaboration between the handles Dark 07x, Jokeir 07x and Dr. SHell 08x operating as "Dark Hell 07X", advertised a tiered sale of the stolen data: a full database for $4,000, a bank-account data file for $2,000, and individual bank accounts priced from $100 (one account) to $450 (five accounts). No account numbers, IBANs or customer identities are reproduced from the reviewed sample.

### 25 July 2025
#### 🇹🇳 Tunisia - Banque de Tunisie (bt.com.tn)
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Banking / Financial Services.
- **Website:** https://bt.com.tn
- **Status:** Claim - Data Sample Published
- **Victim Description:** Banque de Tunisie (BT) is one of the oldest and largest private banks in the country.
- **Analysis:** Material shows a live, authenticated customer online-banking dashboard on bt.com.tn with multiple account balances, a foreign-exchange rate module, a securities/portfolio overview and a transaction-history chart, confirming genuine account-level access rather than a simple claim. No account numbers or balances are reproduced from the reviewed sample.

### 27 July 2025
#### 🇪🇷 Eritrea - Embassy of Eritrea in the United States
- **Incident type:** Data Leak

- **Actor / Group:** Gh1nDar
- **Sector:** Government / Diplomatic
- **Status:** Claim - Unverified
- **Website:** [us.eriembassy.org](https://us.eriembassy.org)

- **Description:**
  The Embassy of Eritrea in the United States is the official diplomatic representation of the State of Eritrea on US territory.

- **Analysis:**
  A threat actor using the alias Gh1nDar claims, in a BreachForums post dated July 27, 2025, to have uploaded a leak affecting approximately 5,000 citizens linked to the Embassy of Eritrea in the United States. The allegedly exposed data would include ID card number, full name, mother's name, passport number, email address, phone number, birthdate, religion and current job. No verifiable sample was accessible in the collected source. The account behind the post is recent and has no established reliability history. At this stage, AFRINTEL does not confirm the intrusion or the authenticity of the data.

### 28 July 2025
#### 🇹🇳 Tunisia - BH Bank
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Banking / Financial Services.
- **Website:** https://bhbank.tn/
- **Status:** Claim - Data Sample Published
- **Victim Description:** Historic and systemic banking institution in Tunisia (Banque de l'Habitat), a pillar of real estate financing and the national economy.
- **Analysis:** The actor's forum post, published under the handle Jokeir07x as part of the "Dark Hell 07X" collaboration with Dr. SHell 08x (also behind the BTK Bank claim), states that the group gained full control of the website's infrastructure, emptied and analysed all databases, and confirmed compromise of both back-end and front-end access points; the post separately advertises a list of 200 "Yankee" accounts for sale for 100 USDT. Accompanying material shows live, authenticated online-banking sessions for at least two distinct customer accounts, including a corporate "BH Capital Plus" account, with visible balances, plus a bank-card transaction history including a withdrawal record. No account numbers, card numbers, customer identities or balances are reproduced from the reviewed sample.
### 29 July 2025
#### 🇲🇦 Morocco - Ministry of National Education, Preschool and Sports
- **Incident type:** Data Leak
- **Actor / Group:** Wieko
- **Sector:** Government / Public Administration / Education
- **Website:** [men.gov.ma](https://men.gov.ma)
- **Status:** Claim - Data Sample Published

- **Description:**
  The Ministry of National Education, Preschool and Sports is the Moroccan public administration responsible for government policy concerning preschool, primary and secondary education, as well as school sports. Its official institutional portal uses the `men.gov.ma` domain.

- **Analysis:**
  A cybercriminal-forum post attributed to Wieko advertises a text file containing 223,501 lines in `mail:pass` format. The visible sample includes accounts associated with several Moroccan education-related domains, including universities and training institutions. Individual credentials are not reproduced. A download section is visible but hidden by the forum, preventing verification of the advertised file, its integrity, record uniqueness or the validity of all credential pairs. The material appears to be a combined credential list rather than a structured export from a ministry database. The presence of accounts from several institutions does not demonstrate a direct compromise of the ministry’s central information systems; the credentials’ origin, collection method and technical connection to the central administration remain unknown. The combinations could facilitate credential stuffing, account takeover, unauthorized access to educational platforms, targeted phishing and digital impersonation, particularly where passwords were reused. No price, ransomware group, byte volume, deadline or extortion demand is stated.

- **Double-claim note:**
  AFRINTEL separately recorded a June 18, 2025 claim involving the ministry’s Massar platform. The actors and advertised datasets differ, and available evidence does not establish that both publications derive from the same compromise.

---
[July 2025 Report](./report/README.md)
---

## August 2025

### 06 August 2025
#### 🇹🇳 Tunisia - Yasat (yasat.tn)
- **Incident type:** Data Leak
- **Actor / Group:** RainbowDF
- **Sector:** Technology / Multimedia Distribution
- **Website:** yasat.tn
- **Status:** Claim - Data Sample Published
- **Victim Description:** Tunisian wholesale platform for multimedia services and digital subscriptions, serving as a supplier to many local shop owners and resellers.
- **Analysis:** AFRINTEL reviewed the structured data referenced in the actor's claim, corresponding to production database exports from Yasat's wholesale IPTV/satellite-TV subscription platform, including beIN Sports-branded products and generic IPTV offerings with M3U stream-link fields. The reviewed tables comprise 52,733 invoice line items (products, quantities, pricing, discounts, tax, paid/due amounts), 46,522 general sales records including customer mobile numbers, email addresses and IPTV stream (M3U) links, 8,623 beIN-specific sales records with similar customer contact fields, 211 customer profile records (last/first name, company, address, phone, gender, date of birth) and a 22-record user/account table containing a password field. The combined dataset indicates tens of thousands of exposed customer and transaction records, creating a significant risk of subscription-service fraud, credential reuse and targeted phishing against Yasat's reseller and customer base. AFRINTEL does not reproduce any customer names, contact details, stream links or credentials from the reviewed sample.

### 06 August 2025
#### 🇰🇪 Kenya - KenGen
- **Ransomware Group:** qilin
- **Sector:** Energy / Critical Infrastructure (Electricity Generation)
- **Website:** www.kengen.co.ke
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Kenya Electricity Generating Company PLC (KenGen) is Kenya's main electricity producer, supplying approximately 70% of the country's power.
- **Analysis:** AFRINTEL reviewed a local set of documents associated with this claim. The sample includes internal KenGen contract-management records for a geothermal training centre construction project (a contract implementation team memo, an official purchase order and a bank performance-bond letter from a commercial bank), a detailed CAPEX budget schedule for the Geothermal Development division, a payroll-style financial ledger, an employee roster from the Geothermal Development department listing employee identifiers, names, gender, job titles and grade levels, a signed tender confidentiality declaration tied to an internal ICT procurement, an official letter from Kenya's Ministry of Energy and Petroleum addressed to the CEOs of KenGen and other national energy-sector entities regarding a human-resource and research-and-development framework, and an engineering floor-plan drawing of a plant auxiliary/switch room. The documents share consistent KenGen letterhead, stamps, signatures and cross-referenced contract numbers across independently structured files, which increases confidence that the sample originates from KenGen's internal systems. The dataset combines employee personal data, internal financial and procurement records, engineering documentation and correspondence with national energy-sector institutions, indicating exposure spanning multiple internal systems rather than a single application. AFRINTEL does not reproduce employee names, identifiers, signatures or monetary values from the sample and does not independently confirm the intrusion.

### 06 August 2025
#### 🇲🇦 Morocco - New Era Com
- **Incident type:** Data Leak
- **Actor / Group:** Chucky_BF
- **Sector:** Telecoms / Infrastructure / IT Services
- **Website:** neweracom.ma
- **Status:** Data Fully Published
- **Victim Description:** Moroccan company specializing in telecom engineering, network infrastructure installation, and ERP/CRM solutions. The actor published a 607 MB SQL dump containing over 476,000 records.

### 09 August 2025
#### 🇳🇬 Nigeria - Zenith Bank Plc
- **Actor / Group:** KaruHunters
- **Sector:** Banking / Financial Services
- **Website:** zenithbank.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** One of the largest financial institutions in Nigeria and Anglophone Africa, listed on the Nigerian and London Stock Exchanges. The actor claims exfiltration and sale of over 1.8 million customer records, together with employee data. AFRINTEL reviewed a local CSV sample containing 18 data rows and eight columns covering index, code, identifier, name, amount, address, telephone and email fields. No raw values are reproduced.
- **Correlation note:** The same organization and domain were listed again on 26 July 2026 by ExfilSquad in a ransomware claim. This establishes an identity and temporal correlation, not a confirmed connection between the two events. The 2025 record concerns an alleged sale of 1.8 million records with a reviewed 18-row sample; the 2026 record provides no sample, volume, encryption evidence or victim confirmation. No matching archive, data schema, shared infrastructure or explicit reference links the claims. AFRINTEL therefore tracks them as related records / possible separate claims, with the relationship unresolved.

### 13 August 2025
#### 🇩🇿 Algeria - Cevital
- **Ransomware Group:** akira
- **Sector:** Agribusiness / Industry / Logistics
- **Website:** www.cevital.com
- **Status:** Claim - Unverified
- **Victim Description:** Leader in the agrifood industry in Algeria, active in electronics, steel, glass, and distribution.

### 17 August 2025
#### 🇿🇦 South Africa - SYSPRO
- **Ransomware Group:** warlock
- **Sector:** Technology (Software Publisher)
- **Website:** syspro.com
- **Status:** Claim - Unverified
- **Victim Description:** SYSPRO is a South African ERP (Enterprise Resource Planning) software publisher, providing integrated management solutions for manufacturing and distribution companies.

### 18 August 2025
#### 🇺🇬 Uganda - Uganda Electricity Transmission Company Limited
- **Ransomware Group:** qilin
- **Sector:** Energy (Electricity)
- **Website:** https://www.uetcl.go.ug / www.uetcl.com
- **Status:** Claim - Unverified
- **Victim Description:** Ugandan public company responsible for electricity transmission.

### 11 August 2025
#### 🇿🇦 South Africa - Body Graphics Tattoo Supply
- **Incident type:** Data Leak
- **Actor / Group:** N1KA
- **Sector:** Retail / E-commerce
- **Website:** bodygraphicstattoosupply.co.za
- **Source publication date:** 11 August 2025
- **Status:** Data Fully Published
- **Victim Description:** Major online retailer based in Johannesburg, specializing in the supply of professional tattoo equipment and aftercare products in South Africa.
- **Analysis:** AFRINTEL reviewed two structured export files referenced in a post observed on DarkForums, together totaling 6,501 records, matching the volume claimed by the actor. The dataset corresponds to a WordPress/WooCommerce customer and administrator export, including login names, email addresses, hashed passwords (phpass format), physical addresses, phone numbers, IP addresses, browser user-agent strings and session tokens. The structural consistency between the claimed volume and the reviewed files, together with fields matching the victim's e-commerce platform, supports a high confidence assessment, and the publication identifies the source account as N1KA. AFRINTEL does not reproduce any customer names, contact details, addresses or credentials from the reviewed sample.

### 18 August 2025
#### 🇹🇳 Tunisia - International Freight & Commerce
- **Ransomware Group:** direwolf
- **Sector:** Logistics
- **Website:** ifc-tunisie.com
- **Status:** Claim - Unverified
- **Victim Description:** Tunisian company providing maritime, air, and land transport services, as well as logistics management and customs formalities for importing and exporting companies.

### 20 August 2025
#### 🇿🇦 South Africa - Netstar South Africa (second attack)
- **Ransomware Group:** incransom
- **Sector:** Technology / Telematics / IoT Security
- **Website:** www.netstar.co.za
- **Status:** Claim - Unverified
- **Victim Description:** Netstar, a subsidiary of the Altron group, is the pioneer of the stolen vehicle recovery (SVR) industry in South Africa.
- **Analysis:** AFRINTEL previously recorded a claim against this same company by devman on 23 May 2025. This second claim, published roughly three months later by a different actor, could reflect either a genuine separate intrusion or a republication/resale of the earlier claim; AFRINTEL has not independently confirmed which scenario applies.

### 23 August 2025
#### 🇪🇬 Egypt - TEAM4 Security
- **Incident type:** Data Leak
- **Actor / Group:** GhostCrawl
- **Sector:** Security Services / Defense / Human Resources
- **Website:** team4security.com
- **Status:** Claim - Data Sample Published
- **Victim Description:** Egyptian company specializing in private security services, infrastructure protection, and risk management consulting. TEAM4 Security is a multi-dimensional security company established in 2017, operating out of the UK and Egypt, offering integrated digital and physical security, human guarding and professional K-9 systems, and targeting critical infrastructure, safe cities, government and defense-sector clients.
- **Analysis:** AFRINTEL reviewed the leak batches published by the actor GhostCrawl on DarkForums; the forum thread's own posting timestamps run from 29 to 31 August 2025 (part 1 posted 29 August 2025, 23:55), slightly later than this file's detection date of 23 August. The material corresponds to an exfiltrated administrative/support mailbox (contacts, inbox and sent email in .eml/.mbox format) together with several hundred attached office documents and images across the five batches. Reviewed samples include monthly payroll spreadsheets for security personnel across multiple 2025 pay periods (guards, supervisors and K-9 unit staff), a detailed HR/payroll record listing employee number, full name, national ID number, post/role, birth date, hiring date, social insurance, fixed and variable salary and bonus fields for over twenty staff, internal incident memoranda (including a theft-investigation report dated 3 November 2024), monthly manpower and staff-evaluation forms, an internal phone-extension directory, and individual employee case documents, alongside official company letterhead confirming TEAM4 Security's Egypt head office and branch office addresses. The combination of national ID numbers, birth dates, hiring dates and salary data for security guard personnel creates a significant risk of identity fraud and targeted social engineering against staff, while the internal incident and site-operations records could expose details relevant to protected client sites. AFRINTEL does not reproduce any employee names, national ID numbers, salary figures or other personal data from the reviewed sample.

### 25 August 2025
#### 🇲🇺 Mauritius - SWAN Mauritius
- **Ransomware Group:** qilin
- **Sector:** Insurance / Financial Services
- **Website:** www.swan.mu / swanforlife.com
- **Status:** Claim - Unverified
- **Victim Description:** SWAN (Swan General Ltd and Swan Life Ltd) is the market leader in insurance and financial services in Mauritius.

### 25 August 2025
#### 🇹🇬 Togo - Government Infrastructures
- **Incident type:** Access Sale
- **Actor / Group:** BIGBROTHER
- **Sector:** Government / Critical Infrastructures
- **Website:** gouv.tg
- **Status:** Claim - Data Sample Published
- **Victim Description:** Official portal and digital infrastructures of the Togolese Republic, hosting administrative services and state data.
- **Analysis:** Material corroborates the actor's claim, including the DarkForums listing itself and several elements showing active administrative access across multiple Togolese government digital platforms: the DSNIC identity and civil-status management system (justice.xflow.gouv.tg), a Nextcloud-based government file-sharing and collaboration platform (cloud.numerique.gouv.tg) with shared folders and configuration files, a KoboToolbox data-collection instance (kf.form.gouv.tg) hosting dozens of active government surveys and forms, and an education-statistics reporting system (stateduc.planifeducation.gouv.tg). The material shows genuine administrative-level access to live dashboards rather than a public-facing sample, consistent with the actor's description of the offer as a "0day vulnerability" granting privileged access. This breadth of access across distinct systems and subdomains under the gouv.tg domain supports a high confidence assessment of an active, unremediated compromise affecting multiple government digital services, independent of the actor's Monero-based pricing claim, which AFRINTEL cannot verify. AFRINTEL does not reproduce any credentials, configuration values, citizen data or session details from the reviewed material.
---
[August 2025 report](./report/README.md)

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

## October 2025

### 01 October 2025
#### 🇿🇦 South Africa - Climatron (Pty) Ltd
- **Ransomware Group:** incransom
- **Sector:** Construction / HVAC
- **Website:** https://climatron.co.za
- **Status:** Claim - Unverified
- **Victim Description:** Climatron (Pty) Ltd is a company specializing in industrial and commercial air conditioning solutions, based in Johannesburg.

### 05 October 2025
#### 🇿🇦 South Africa - The Methodist Church of Southern Africa
- **Ransomware Group:** beast
- **Sector:** Religion / Charitable Organization
- **Website:** www.methodist.org.za
- **Status:** Claim - Unverified
- **Victim Description:** The Methodist Church of Southern Africa (MCSA) is one of the most influential Christian denominations in the region. It operates not only in South Africa but also in Botswana, Lesotho, Namibia, Eswatini, and Mozambique.

### 10 October 2025
#### 🇿🇦 South Africa - Momentum Logistics
- **Ransomware Group:** brotherhood
- **Sector:** Transport / Logistics
- **Website:** www.momentumlogistics.co.za
- **Status:** Claim - Unverified
- **Victim Description:** Momentum Logistics is a South African logistics provider based in Johannesburg.

### 13 October 2025
#### 🇲🇦 Morocco - LA VOIE EXPRESS
- **Ransomware Group:** medusa
- **Sector:** Logistics
- **Website:** https://lavoieexpress.ma / https://lavoieexpress.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** Moroccan logistics company based in Casablanca, offering courier, transport, and warehousing services.
- **Analysis:** AFRINTEL reviewed a local sample of multi-sheet spreadsheet exports consistent with the claim made by the threat actor medusa, each watermarked with the group's Tor leak-site address. The reviewed material includes a general accounting ledger (bank and journal entries dated 2020-2021), warehouse and logistics workbooks covering goods reception, dispatch, stock-preparation and internal-transfer movements for major appliance brands (referencing BSH/Bosch-Siemens product lines) tied to named internal staff handling the operations, and a client accounts-receivable ageing report listing several dozen named corporate clients across multiple Moroccan cities (Casablanca, Agadir, Tanger, Marrakech, Fès, Settat and others), including well-known national and multinational accounts (among them Procter & Gamble-affiliated entities, Savola Maroc, Centrale Laitière, Ciment du Maroc, BSH Electroménager and Ecolab), together with named client contacts, phone numbers, outstanding balances, payment terms and collections/dispute status. The internal consistency of the data across accounting, warehouse and commercial modules, the presence of real, identifiable Moroccan and multinational client accounts, and the multi-year date range (2020-2023) spanning multiple branches support a very high confidence assessment of a genuine, broad compromise of La Voie Express's internal ERP and accounting systems. Given the scale of the exposed accounts-receivable and banking-ledger data and its extension into the client base of a major national logistics provider, this incident creates a material risk of invoice fraud, business email compromise and targeted social engineering against La Voie Express and its corporate clients, beyond the company's own operational exposure. AFRINTEL does not reproduce any client name, contact name, phone number, financial figure or staff identifier from the reviewed material.

### 13 October 2025
#### 🇪🇬 Egypt - meamargroup.com (third attack)
- **Ransomware Group:** obscura
- **Sector:** Real Estate / Construction / Engineering
- **Website:** https://meamargroup.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** Egyptian company specializing in real estate development.
- **Analysis:** AFRINTEL reviewed a local server-side filesystem archive (491 files and directories, all owned by the www-data web-server account) consistent with the claim made by the threat actor obscura. File timestamps cluster into two groups: the bulk of the material (484 entries) dated 27 August 2025, and a smaller set of directory entries dated 05 September 2025, matching the group's first public claim date against this victim. The reviewed content includes multi-year internal accounting workbooks (yearly ledgers spanning 2015-2024, a "main data 2024" financial file, project cost-comparison sheets), an extensive sales call-center archive of roughly 249 dated spreadsheets covering missed-call and prospect-contact logs from September 2024 to July 2025, at least 21 employee CVs and resumes, and internal design, brochure and CAD material for named real-estate developments (including the Clove Mall and Prime Mall projects). A nested archive within the collection contains a mix of original files alongside copies bearing the ".obscura" ransomware encryption extension (for example, multiple yearly ledger workbooks and IT-department files), directly evidencing the file-encryption stage of the attack rather than an exfiltration claim alone. A short text file consistent with a Tor negotiation-portal countdown ("240 hours. Not available yet!") was also present. The combination of web-server file ownership, internally consistent multi-year timestamps, and the presence of actor-encrypted file copies supports a very high confidence assessment of a genuine, broad compromise of MeamarGroup's internal file server. Given the scale of the exposed financial ledgers, sales-prospect contact data and employee personal information, this incident creates a risk of invoice fraud, targeted phishing against prospective clients and employees, and competitive exposure of internal project and pricing data. AFRINTEL does not reproduce any client name, contact number, employee name or financial figure from the reviewed material.

### 15 October 2025
#### 🇰🇪 Kenya - Turnkey Africa
- **Ransomware Group:** qilin
- **Sector:** Technology / Fintech (Insurance Solutions)
- **Website:** https://turnkeyafrica.com
- **Status:** Claim - Unverified
- **Victim Description:** Turnkey Africa is a pan-African technology leader. The company develops and provides software management solutions (Core Insurance Systems) for insurance and reinsurance companies in over 10 African countries.

### 17 October 2025
#### 🇲🇬 Madagascar - Madagascar Airlines
- **Ransomware Group:** thegentlemen
- **Sector:** Air transport
- **Website:** www.madagascarairlines.com
- **Status:** Claim - Unverified
- **Victim Description:** Madagascar Airlines is the national airline of the Republic of Madagascar.

### 18 October 2025
#### 🇨🇩 Congo (DRC) - TK HOLDINGS GROUP
- **Ransomware Group:** radar
- **Sector:** Mining / Conglomerate
- **Website:** https://congomineralservices.com
- **Status:** Claim - Data Sample Published
- **Victim Description:** Congolese holding with activities in timber, logistics, and mineral exploration.

- **Confidence level:** Medium
- **Impact level:** Level 4
- **Analysis:** AFRINTEL reviewed the analyst-provided CTI workbook and 32 screenshots associated with the radar publication. The evidence set contains seven document categories: DRC customs and legal texts, public-procurement and governance material, TK Holdings salary and recruitment policies, a geological report from Congo Mineral Services concerning the Mikuba Mining copper exploration project, and an environmental-control decree. The workbook classifies the salary policy and the Mikuba geological report as critical sensitivity. The geological material references drilling campaigns and copper grades, creating a plausible industrial-espionage and strategic-resource risk. The HR policies expose internal salary, bonus, leave, recruitment and confidentiality procedures, creating risks of employee targeting, insider abuse and reputational harm. The legal and regulatory documents could support document fraud, corruption or manipulation of compliance and import processes if their authenticity and currency were established. The evidence confirms that sensitive-looking documents were displayed in the collection, but it does not independently confirm the intrusion path, the completeness of the published dataset, the authenticity of every document, or operational impact. AFRINTEL does not reproduce document contents, personal names, signatures or other sensitive material.

### 18 October 2025
#### 🇿🇦 South Africa - University of the Witwatersrand (WITS)
- **Ransomware Group:** clop
- **Sector:** Education (University)
- **Website:** https://www.wits.ac.za
- **Status:** Data Fully Published
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** The University of the Witwatersrand, located in Johannesburg, is one of Africa's most prestigious research institutions.
- **Analysis:** AFRINTEL reviewed a screenshot of Clop's leak-site listing page for wits.ac.za, using the group's standard victim-profile template (Headquarters, Phone, Website, Revenue and Industry fields). Unlike listing pages reviewed for other African entries on the same leak site, this page includes a dedicated "Torrent Magnet Link" section referencing wits.ac.za, indicating that the actor has made a downloadable dataset available rather than only a claim page. The listed company profile (industry described as Colleges & Universities, Education) is consistent with the University of the Witwatersrand's public profile. AFRINTEL did not download or review the content of the referenced torrent, and the volume, content and sensitivity of the published dataset are therefore not independently assessed. The presence of a functioning magnet-link section, distinct from the claim-only pages seen for other entries, supports a high confidence assessment that data has genuinely been made available for download. Given WITS's status as a major research university, a confirmed dataset could include student, staff or research-related personal data, creating a risk of identity fraud and targeted phishing against the university community. AFRINTEL does not reproduce the magnet link, headquarters address or phone number from the reviewed material.

### 19 October 2025
#### 🇬🇦 Gabon - SANgel
- **Ransomware Group:** qilin
- **Sector:** Agribusiness
- **Website:** https://sangel-gabon.com
- **Status:** Claim - Unverified
- **Victim Description:** Gabonese food production and distribution company based in Libreville, specializing in frozen products.

### 20 October 2025
#### 🇪🇬 Egypt - Al Ahly Leasing & Factoring Company
- **Ransomware Group:** blackshrantac
- **Sector:** Finance
- **Website:** alahlyleasing.com
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian financial institution specializing in leasing and factoring, a subsidiary of the National Bank of Egypt.

### 23 October 2025
#### 🇲🇦 Morocco - STAR LÉGUMES
- **Ransomware Group:** tengu
- **Sector:** Wholesale Trade (Food Products)
- **Website:** https://starlegumes.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** Moroccan wholesaler of fruits, vegetables, spices, and dried seeds based in Casablanca.
- **Analysis:** AFRINTEL reviewed the leak-site listing and a local sample of documents consistent with the claim made by the threat actor tengu. The leak-site page itself was captured (view counter and elapsed-time indicator visible), alongside a Moroccan commercial-registry extract (Tribunal de Commerce de Casablanca) confirming the company's legal identity, registration date, share capital, registered address and manager name; multiple client invoices dated between November 2021 and March 2025 bearing the company's ONSSA food-safety registration number, client names, addresses and transaction amounts; and a system-generated "Journal Factures Clients" accounting-ledger export covering October 2024, printed in February 2025, listing roughly 50 sequential invoice records with client names, invoice numbers and HT/TVA/TTC amounts. A structured analyst summary workbook built from this material further itemises a legal-identity record, a client-contact sample (name, tax ID/ICE, address) and an invoice sample. The combination of an official leak-site listing, a genuine commercial-registry extract, dated system-generated accounting exports and internally consistent branding across documents spanning more than three years supports a very high confidence assessment of a genuine compromise of Star Légumes' invoicing and accounting systems. Given the scale of exposed client contact and transaction data, this incident creates a risk of supplier/customer fraud, business email compromise and resale of the client base. AFRINTEL does not reproduce any client name, address, tax identifier or financial figure from the reviewed material.

### 24 October 2025
#### 🇲🇦 Morocco - Le MULTI LABORATOIRE LC2A
- **Ransomware Group:** tengu
- **Sector:** Pharmaceutical Industry / Laboratory
- **Website:** https://multi-laboratoire-lc2a.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 2
- **Victim Description:** Moroccan laboratory offering a platform for configuring analytical projects for businesses.
- **Analysis:** AFRINTEL reviewed a local sample of internal documents consistent with the claim made by the threat actor tengu, addressed to or generated by LC2A. The reviewed material includes a supplier price quote from a laboratory-equipment vendor (dated May 2022) addressed to LC2A's purchasing department, itemising reagents and analytical equipment with unit and total pricing, and an internal equipment-calibration log ("Carte de contrôle des équipements", quality-management form reference FOR06/PRT06) for a laboratory balance, recording daily calibration checks through October 2021. The company name, internal form references and consistent document branding across both files support a high confidence assessment that the sample originates from LC2A's internal systems rather than a fabricated claim. A separate bulk data package referenced alongside this sample did not complete transfer and could not be reviewed; this analysis is limited to the two documents described above. Given the operational and supplier nature of the reviewed material, this incident presents a moderate risk of supplier impersonation and disclosure of internal quality-control and procurement practices, with no patient or clinical data observed in the reviewed sample. AFRINTEL does not reproduce any supplier name, pricing detail, equipment code or staff identifier from the reviewed material.

### 24 October 2025
#### 🇳🇬 Nigeria - Henrietta Ezeoke Law Firm
- **Ransomware Group:** qilin
- **Sector:** Legal Services
- **Website:** https://houstonwrongfuldeathlawyers.com
- **Status:** Claim - Unverified
- **Victim Description:** Nigerian law firm.

### 28 October 2025
#### 🇹🇿 Tanzania - Alios Finance Group
- **Ransomware Group:** incransom
- **Sector:** Finance
- **Website:** https://aliosfinance.co.tz
- **Status:** Claim - Unverified
- **Victim Description:** Pan-African financial operator present in Tanzania, offering specialized financing solutions. 100 GB of data exfiltrated.

### 28 October 2025
#### 🇹🇳 Tunisia - Alios Finance Group
- **Ransomware Group:** incransom
- **Sector:** Finance
- **Website:** https://aliosfinance.tn
- **Status:** Claim - Unverified
- **Victim Description:** Pan-African financial operator present in Tunisia, specializing in financing for businesses and individuals. During this intrusion, 100 GB of data were exfiltrated by the incransom group.

### 31 October 2025
#### 🇩🇿 Algeria - TMF Logistics
- **Ransomware Group:** incransom
- **Sector:** Logistics
- **Website:** https://tmf-logistics.com
- **Status:** Claim - Data Sample Published
- **Victim Description:** TMF Logistics is an Algerian company specializing in transport and logistics solutions. During this attack, the incransom group claimed the exfiltration of 39 GB of sensitive company data.
- **Analysis:** Internal financial and operational documents reviewed by AFRINTEL corroborate the incransom claim. A November 2024 revenue-by-client spreadsheet lists roughly thirty corporate clients served by TMF Logistics, including major food, beverage and pharmaceutical companies operating in Algeria (e.g. Danone Algérie, Institut Pasteur d'Algérie, GlaxoSmithKline Algérie, Fromagerie Bel Algérie), alongside refrigerated and general freight service categories (frigo, bâché and flatbed trailers). A separate detailed billing export covers invoice-level transport operations across numerous Algerian wilayas (including Béjaïa, Bouira, Batna, Constantine, Djelfa, Ghardaïa, Ouargla and Tindouf), indicating a national delivery network. A delivery discharge document confirms the company's official identity: SPA TMF Logistics, based in the Taharacht industrial zone, Akbou (Béjaïa wilaya), with its registered contact details and business registration references. The combination of a national client portfolio, route network data and business registration details creates a supply-chain risk (client impersonation, invoice fraud, competitive intelligence) extending beyond TMF Logistics' own operational exposure.

### 31 October 2025
#### 🇲🇦 Morocco - Institut Agronomique et Vétérinaire Hassan II (IAV Hassan II)
- **Incident type:** Data Leak
- **Actor / Group:** DBhacker_BF
- **Sector:** Education / Higher Education / Agronomy and Veterinary Sciences
- **Website:** iav.ac.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** IAV Hassan II is a leading Moroccan public institution for agronomic and veterinary higher education, based in Rabat. The reviewed database contains 4,208 applicant/candidate records and covers applicants/candidates and includes full name, date and place of birth, nationality, gender, address, national ID number (CIN), phone number, email address, enrollment status, academic track (filière) and an account password field (largely empty in the reviewed sample). The combination of national ID, contact details and academic data creates a risk of identity fraud, targeted phishing and account-recovery abuse; the completeness and origin of the file have not been independently confirmed.

### 31 October 2025
#### 🇲🇦 Morocco - Ministry of Higher Education, Scientific Research and Innovation (enssup.gov.ma)
- **Incident type:** Data Leak
- **Actor / Group:** EternalRed
- **Sector:** Government / Education / Higher Education
- **Website:** enssup.gov.ma
- **Source publication date:** 25 October 2025
- **Status:** Claim - Data Sample Published
- **Victim Description:** enssup.gov.ma is the Moroccan Ministry of Higher Education, Scientific Research and Innovation. The supplied text file contains exactly 942,930 lines, matching the advertised record count; it is a nationwide student extract covering 942,930 records, with fields including national ID number (CIN), national student identifier (code Massar), full name in Arabic and French, gender, date of birth, nationality, institution code and name, academic program (filière) and education level. The internal file metadata indicates the extract was originally compiled around December 2022, though AFRINTEL reviewed it as part of a 2025 data collection. The scale and structure of the dataset indicate a significant nationwide exposure of higher-education student records, creating risks of identity fraud and targeted phishing against students and institutions; completeness and the exact source of the extraction have not been independently confirmed.

## November 2025

### 04 November 2025
#### 🇲🇦 Morocco - DOVERN Import
- **Ransomware Group:** spacebears
- **Sector:** Logistics
- **Website:** https://dovern-import.com/
- **Status:** Claim - Unverified
- **Victim Description:** Import company based in Morocco, specializing in the distribution of fine wines, spirits, and prestige champagnes.

### 04 November 2025
#### 🇿🇦 South Africa - Wannabees (wannabees.co.za)
- **Incident type:** Data Leak
- **Actor / Group:** Unknown
- **Sector:** Human Resources / Recruitment
- **Website:** wannabees.co.za
- **Status:** Claim - Data Sample Published
- **Victim Description:** Wannabees appears to be a South African recruitment and temporary-employment platform, based on the structure and content of the reviewed applicant database.
- **Analysis:** AFRINTEL reviewed two identical files from the provided evidence set (DB.txt and HoJmS, matching by SHA-256), containing a five-record applicant export. The schema includes applicant identifiers, national identity numbers, names, addresses, phone numbers, email fields, dates of birth, nationality, employment history, current occupation, salary expectations and remuneration-related fields, alongside a password field. The sample is structurally consistent with a recruitment or staffing database and contains highly sensitive personal and employment information. The files are dated 4 November 2025 in the evidence directory; this is treated as the discovery/evidence date, not as a confirmed publication or intrusion date. The available material does not identify a threat actor, forum, access method or complete dataset volume. AFRINTEL records the case as a data-leak claim with a published sample and does not reproduce names, identity numbers, contact details, passwords or other raw personal data.
### 05 November 2025
#### 🇨🇮 Ivory Coast - Anka (Anka.africa)
- **Actor / Group:** Spirigatito, post published on a cybercriminal forum
- **Sector:** Logistics
- **Website:** https://www.anka.africa/
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** Leading Ivorian platform facilitating export, payments, and logistics for African creators and merchants to the global market.
- **Analysis:** The forum post advertises the sale of a database attributed to Anka, claiming 537,877 unique users and a 12.1 GB volume, with a stated field list of id, username, fullname, email, token, avatar, gender, date of birth and phone, among others. AFRINTEL reviewed structured sample extracts derived from the sample published with the post, comprising a small number of individual user records (fewer than 30). The reviewed schema matches the field list advertised in the post, extending it with additional attributes: last sign-in date, account lock and deletion flags, account type, purchase count and amount, wallet balance, and marketplace seller-sales fields. Reviewed records show account-creation timestamps ranging from May 2017 to May 2024, currencies including EUR, USD and GMD, and locales in French and English, consistent with an international user base for an African cross-border e-commerce and payments platform. The structural consistency between the advertised field list and the reviewed sample, and the plausibility of the record values (multi-year timestamps, mixed currencies, mixed locales), support raising this case from an unverified claim to a claim with a published data sample. AFRINTEL has not independently verified the claimed total volume of 537,877 users / 12.1 GB, the origin or method of compromise, or the actor's separate claim of $10 million in platform revenue. Exposure of this dataset would combine full names, contact details, dates of birth, gender, account tokens and wallet/purchase information, creating a significant risk of account takeover, targeted phishing and financial fraud against platform users. AFRINTEL does not reproduce any name, email address, phone number, token, username or other individual record from the reviewed sample.

### 06 November 2025
#### 🇪🇬 Egypt - ELSEWEDYELECTRIC.COM
- **Ransomware Group:** clop
- **Sector:** Technology / Industry
- **Website:** www.elsewedyelectric.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 2
- **Victim Description:** Major Egyptian manufacturer of cables, electrical systems, and engineering products.
- **Analysis:** AFRINTEL reviewed a screenshot of Clop's leak-site listing page for elsewedyelectric.com, using the group's standard victim-profile template (Headquarters, Phone, Website, Revenue and Industry fields, followed by the group's recurring boilerplate warning text). The listed company profile (revenue of approximately $4.9 billion, industry described as manufacturing, wire and cable) is consistent with Elsewedy Electric's publicly known profile as a major Egyptian cable and electrical-systems manufacturer. This listing appeared alongside numerous other multinational organisations on the same Clop leak-site page, consistent with the group's mass-exploitation campaign targeting Oracle E-Business Suite customers disclosed in 2025. The matching company profile supports a medium confidence assessment that the listing is genuine, though AFRINTEL did not review any underlying exfiltrated file, magnet link or data sample beyond the listing page itself, and the scope, volume and sensitivity of any data actually held by the actor remain unverified. AFRINTEL does not reproduce the company's headquarters address or phone number from the reviewed material.

### 06 November 2025
#### 🇿🇲 Zambia - ZANACO.CO.ZM
- **Ransomware Group:** clop
- **Sector:** Financial Services (Banking)
- **Website:** www.zanaco.co.zm
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Zambia National Commercial Bank, one of Zambia's leading commercial banks.
- **Analysis:** AFRINTEL reviewed screenshots of Clop's leak-site listing page for zanaco.co.zm, including the group's navigation bar showing this entry alongside numerous other multinational organisations (among them Logitech, The Washington Post, Trimble and Elsewedy Electric), consistent with Clop's mass-exploitation campaign targeting Oracle E-Business Suite customers disclosed in 2025. The listed company profile (revenue of approximately $337.9 million, industry described as finance/banking) is consistent with Zambia National Commercial Bank's publicly known profile. The listing uses the same standard template and boilerplate warning text observed across other Clop victim pages, supporting a medium confidence assessment that the entry is genuine, though AFRINTEL did not review any underlying exfiltrated file, magnet link or data sample beyond the listing pages, and the scope, volume and sensitivity of any customer or banking data actually held by the actor remain unverified. Given ZANACO's role as a major commercial bank, any confirmed data exposure would carry a significant risk of financial fraud and targeted phishing against its customers. AFRINTEL does not reproduce the bank's headquarters address or phone number from the reviewed material.

### 06 November 2025
#### 🇲🇦 Morocco - www.marjane.ma
- **Ransomware Group:** stormous
- **Sector:** Retail / Mass retail / E-commerce
- **Website:** www.marjane.ma
- **Status:** Data Fully Published
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Groupe Marjane is the largest Moroccan mass retail group, operating hypermarkets and supermarkets.
- **Analysis:** AFRINTEL reviewed a proof screenshot published in connection with the claim made by the threat actor stormous, showing an active session on a Fortinet SSL-VPN portal dated 10 November 2025. The portal's bookmark list references internal infrastructure consistent with Marjane's corporate environment, including a marjane.ma subdomain, a Confluence wiki instance hosted under a confluence.marjane subdomain, a collaboration bookmark labelled "huddle/Store Managers" consistent with the retailer's multi-branch store-management operations, and a direct SSH bookmark to an internal host. The presence of Marjane-specific internal hostnames and a functional SSH access point supports a high confidence assessment that the screenshot reflects genuine internal network access rather than a fabricated proof. Following this initial sample, the actor reportedly published the claimed dataset in full on its leak site; AFRINTEL was unable to collect or review this subsequent publication, and its content, volume and authenticity are therefore not independently assessed. Demonstrated internal VPN and SSH-level access into the network of Morocco's largest mass-retail group creates a risk extending beyond any single data category, including potential disruption or further compromise of point-of-sale, logistics and store-management systems across Marjane's branch network. AFRINTEL does not reproduce any credential, session token, IP address or internal hostname from the reviewed material.

### 08 November 2025
#### 🇲🇦 Morocco - NARSA (Agence Nationale de la Sécurité Routière)
- **Incident type:** Data Leak
- **Actor / Group:** anisanas2
- **Sector:** Government / Transportation / Road Safety
- **Website:** Not identified with sufficient confidence
- **Status:** Claim - Data Sample Published
- **Victim Description:** NARSA is the Moroccan national agency responsible for road safety, vehicle registration and technical inspection.
- **Analysis:** AFRINTEL reviewed a structured CSV export consistent with a vehicle-registration record set, with fields including owner full name, address, national ID number (CIN), vehicle make, category, type, chassis number, engine displacement, registration-centre and circulation dates, purchase price and licence-plate number. The sample size and field structure are consistent with the claimed approximately 150,000-row dataset, though AFRINTEL could not independently confirm the claiming actor's identity or the exact total scope from the reviewed material. The combination of national ID numbers, home addresses and vehicle identification data creates a risk of identity fraud, vehicle-related fraud (including counterfeit registration documents) and physical-security risks from address exposure. AFRINTEL does not reproduce any owner names, addresses, national ID numbers or plate numbers from the reviewed sample.

### 09 November 2025
#### 🇿🇦 South Africa - Eastern Cape Department of Human Settlements (ECDHS)
- **Ransomware Group:** nightspire
- **Sector:** Public administrations / Social Housing
- **Website:** ecdhs.gov.za
- **Status:** Claim - Unverified
- **Victim Description:** The Eastern Cape Department of Human Settlements in South Africa is the provincial body responsible for housing policy, urban planning, and access to property for vulnerable populations in South Africa.

### 09 November 2025
#### 🇳🇬 Nigeria - Fidelity Pension Managers, Nigeria
- **Ransomware Group:** nightspire
- **Sector:** Financial Services (Pension Management)
- **Website:** fidelitypensionmanagers.com
- **Status:** Claim - Unverified
- **Victim Description:** Nigerian pension fund manager.

### 11 November 2025
#### 🇪🇬 Egypt - Samcrete Holding
- **Ransomware Group:** clop
- **Sector:** Construction
- **Website:** www.samcrete.com
- **Status:** Claim - Unverified
- **Victim Description:** Samcrete Holding is a fully integrated engineering, contracting, development, manufacturing, and investment company established in 1963.

### 25 November 2025
#### 🇪🇬 Egypt - LAMAICA, Egypt
- **Ransomware Group:** nightspire
- **Sector:** Wood and Building Materials Manufacturing
- **Website:** lamaica.com
- **Status:** Claim - Unverified
- **Victim Description:** LAMAICA is one of the leaders in the Egyptian market in the production of melamine faced panels, high-pressure laminates (HPL), edge bands, and furniture components.

### 26 November 2025
#### 🇪🇬 Egypt - Arabia Holding
- **Ransomware Group:** qilin
- **Sector:** Real Estate / Investment / Urban Development
- **Website:** arabia-holding.com
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian holding company with interests in various sectors, including real estate and management.

### 26 November 2025
#### 🇨🇮 Ivory Coast - Santé Espoir Vie Côte d'Ivoire (SEV-CI)
- **Ransomware Group:** benzona
- **Sector:** Health / NGO / Humanitarian
- **Website:** sevci.org
- **Status:** Claim - Unverified
- **Victim Description:** Santé Espoir Vie Côte d'Ivoire (SEV-CI) is a leading Ivorian non-governmental organization. It works to improve the health of populations, with a particular focus on the fight against HIV/AIDS, tuberculosis, and the strengthening of community health systems.

### 30 November 2025
#### 🇲🇦 Morocco - Joutech
- **Incident type:** Data Leak
- **Actor / Group:** RL000
- **Sector:** Technology / Digital services (exact business activity not independently confirmed)
- **Website:** joutech.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** Joutech is a Moroccan company operating the joutech.ma domain. The reviewed file is a newsletter/contact-list export of 1,350 records, containing title, first name, last name, email address, company field, sales/marketing flags and registration date. No passwords or financial data were observed in the reviewed sample. The exposure could support targeted phishing and spam campaigns against the listed contacts; the completeness and origin of the file have not been independently confirmed.

## December 2025

### 05 December 2025
#### 🇪🇬 Egypt - 3S Software (Secured Smart Systems Overview Metrics)
- **Ransomware Group:** dragonforce
- **Sector:** Technology
- **Website:** 3s-software.com
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian technology service provider specializing in software development.

### 05 December 2025
#### 🇿🇲 Zambia - National Health Insurance Management Authority
- **Ransomware Group:** nova
- **Sector:** Insurance (Health)
- **Website:** https://nhima.co.zm/
- **Status:** Claim - Unverified
- **Victim Description:** Zambian authority managing the national health insurance scheme.

### 06 December 2025
#### 🇬🇭 Ghana - Kasapreko Company Limited
- **Ransomware Group:** qilin
- **Sector:** Agribusiness / Beverages (Alcoholic and non-alcoholic)
- **Website:** www.kasapreko.com
- **Status:** Claim - Unverified
- **Victim Description:** Kasapreko is one of the largest beverage manufacturers in Ghana and a major exporter throughout the ECOWAS region.

### 06 December 2025
#### 🇿🇦 South Africa - Diesel Electric
- **Ransomware Group:** qilin
- **Sector:** Automotive Distribution / Diagnostic Equipment
- **Website:** diesel-electric.co.za
- **Status:** Claim - Unverified
- **Victim Description:** Diesel-Electric is one of South Africa's largest distributors specializing in automotive components, diesel injection systems, and diagnostic equipment (a major Bosch partner).

### 07 December 2025
#### 🇪🇬 Egypt - incolease.com
- **Ransomware Group:** lockbit5
- **Sector:** Finance
- **Website:** www.incolease.com
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian leasing company.

### 07 December 2025
#### 🇿🇦 South Africa - elundini.gov.za
- **Ransomware Group:** lockbit5
- **Sector:** Public Administration / Local Government
- **Website:** elundini.gov.za
- **Status:** Claim - Unverified
- **Victim Description:** Elundini Local Municipality is a key administrative authority located in the Joe Gqabi District (Eastern Cape), encompassing the towns of Maclear, Ugie, and Mount Fletcher.

### 08 December 2025
#### 🇪🇬 Egypt - Arkan
- **Ransomware Group:** ransomhouse
- **Sector:** Finance / Trade
- **Website:** arkanonline.com
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian conglomerate, Arkan Group, active in industry, agriculture, and wholesale trade.

### 11 December 2025
#### 🇳🇬 Nigeria - Leadway Assurance / Leadway Health
- **Ransomware Group:** kazu
- **Sector:** Insurance
- **Website:** leadwayhealth.com
- **Status:** Claim - Unverified
- **Victim Description:** Leadway Assurance is the largest private insurance company in Nigeria.

### 12 December 2025
#### 🇹🇳 Tunisia - Hopital La Rabta (University Hospital Center)
- **Ransomware Group:** devman
- **Sector:** Healthcare
- **Website:** www.chularabta.tn
- **Status:** Claim - Unverified
- **Victim Description:** La Rabta Hospital is one of the largest hospital complexes in Tunisia.

### 15 December 2025
#### 🇹🇳 Tunisia - Tunisian Society of Radiology (strtn.org)
- **Ransomware Group:** nova
- **Sector:** Health / Medical Association / Education
- **Website:** strtn.org
- **Status:** Claim - Unverified
- **Victim Description:** The Tunisian Society of Radiology (STR) is the reference organization for radiologists in Tunisia.

### 22 December 2025
#### 🇪🇬 Egypt - Polaris Parks
- **Ransomware Group:** direwolf
- **Sector:** Real Estate Development / Management of Industrial and Leisure Parks
- **Website:** polarisparks.com
- **Status:** Claim - Unverified
- **Victim Description:** Polaris Parks is one of Egypt's leading private industrial park developers.

### 24 December 2025
#### 🇿🇦 South Africa - National Credit Regulator (NCR)
- **Ransomware Group:** dragonforce
- **Sector:** Public administrations (Financial Regulation)
- **Website:** www.ncr.org.za
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** South African public body responsible for regulating the consumer credit industry.
- **Analysis:** AFRINTEL reviewed a local sample of documents associated with this claim. The material includes approximately 25 individually named consumer case files consistent with debt-review/debt-counselling matters handled by the NCR, roughly 20 emails referencing named individuals together with partial identifiers resembling South African ID-number date-of-birth prefixes, and an internal enforcement memo dated 24 June 2022 from the NCR's Manager: Complaints Department to the Acting Manager: Investigations and Enforcement, opening an investigation into an entity referred to as "Debt Accord Solutions" for allegedly operating as an unregistered debt counsellor. The sample also includes an internal administrator spreadsheet tracking case-related email volumes on a near-daily to monthly basis from August 2020 through December 2024, NCR-branded logo files, regulatory forms (including a Form 29 and a written-consent document under Regulation 50(5)), a mandate document and a bank-details record. The documents are internally consistent with the NCR's branding, organisational structure (named managers and departments) and regulatory casework format. The sample indicates exposure of consumer debt-review case files, internal investigation and enforcement records, and multi-year operational tracking data, creating a material risk of identity fraud and targeted phishing against named consumers and NCR staff, as well as potential interference with ongoing regulatory investigations. AFRINTEL does not reproduce any consumer name, identifier, case file content, staff name or investigation detail from the reviewed material.

### 26 December 2025
#### 🇹🇳 Tunisia - Hopital La Rabta (second cyberattack)
- **Ransomware Group:** qilin
- **Sector:** Healthcare
- **Website:** www.chularabta.tn
- **Status:** Claim - Unverified
- **Victim Description:** La Rabta Hospital is one of the largest hospital complexes in Tunisia.
- **Analysis:** AFRINTEL previously recorded a claim against this same hospital by devman on 12 December 2025. This second claim, published two weeks later by a different actor, could reflect either a genuine separate intrusion or a republication/resale of the earlier claim; AFRINTEL has not independently confirmed which scenario applies.

### 26 December 2025
#### 🇿🇼 Zimbabwe - Proplastics Limited (second cyberattack)
- **Ransomware Group:** lockbit5
- **Sector:** Manufacturing Industry (Plastics)
- **Website:** proplastics.co.zw
- **Status:** Claim - Unverified
- **Victim Description:** Proplastics Limited is the leading manufacturer and supplier of plastic piping systems (PVC, HDPE) in Zimbabwe.
- **Analysis:** AFRINTEL previously recorded a claim against this same company by thegentlemen on 9 September 2025. This second claim, published roughly three and a half months later by a different actor, could reflect either a genuine separate intrusion or a republication/resale of the earlier claim; AFRINTEL has not independently confirmed which scenario applies.

### 29 December 2025
#### 🇩🇿 Algeria - Oran University 1 Ahmed Ben Bella
- **Incident type:** Data Leak
- **Actor / Group:** GhostVector (source account)
- **Sector:** Education / University
- **Website:** Not specified
- **Source publication date:** 29 December 2025
- **Status:** Claim - Data Sample Published
- **Victim Description:** Oran University 1 Ahmed Ben Bella is a public higher-education institution in Oran, Algeria. The supplied post advertises a database dated 2023 with approximately 58,000 records and fields including names, birth dates, phone numbers, gender, email addresses, password hashes and nationality.
- **Analysis:** The post displays a structured sample associated with the university and identifies GhostVector as the source account. If valid, the dataset could enable identity fraud, phishing and account-targeting against students or staff. No personal record, credential, hash or contact detail is reproduced, and the claim and dataset provenance have not been independently confirmed.

### 29 December 2025
#### 🇪🇬 Egypt - 100 Watt Plast (100wattplast.com)
- **Incident type:** Data Leak
- **Actor / Group:** camillabf, post published on a cybercriminal forum (RaidForums)
- **Sector:** Industrial / Electrical and Plastic Products Manufacturing
- **Website:** [100wattplast.com](https://100wattplast.com)
- **Status:** Claim - Data Sample Published
- **Victim Description:** 100 Watt Plast is an industrial company based in Egypt, with activities also in Lebanon and Saudi Arabia, specializing in the manufacture of electrical and plastic products.
- **Analysis:** The actor camillabf published a claim on December 29, 2025 concerning 100wattplast.com, described as a dataset of 180,000 records in CSV format, comprising first name, last name, email, phone and password. The sample shown in the post displays a field schema including two password values per record: an MD5-type hash (32 hexadecimal characters) and a second, markedly more complex value of variable length, along with three additional undocumented fields (`aa`, `bb`, `already`).

  About twenty complete records are directly visible in the sample, with names, email addresses and Egyptian phone numbers tied to both password values. The consistency of the schema and the number of individual records observed support a high confidence level regarding the authenticity of this leak, although the total claimed volume of 180,000 rows could not be independently verified beyond the observed sample, and the exact nature of the second password field (alternate hash or plaintext value) could not be determined with certainty. Exposure of this data could facilitate account takeover, password reuse across other services and targeted phishing against the company's customers. AFRINTEL does not reproduce any name, email address, phone number or password value from the reviewed sample.

### 31 December 2025
#### 🇲🇦 Morocco - Pharmacie.ma
- **Incident type:** Data Leak
- **Actor / Group:** KaruHunters
- **Sector:** Healthcare / Pharmacy e-commerce
- **Website:** pharmacie.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** Pharmacie.ma is a Moroccan pharmacy directory and e-commerce platform. Two full SQL database backups, dated September 2025, were reviewed, covering the platform's full application schema (clients, addresses, drugs, pharmacists, newsletters, articles and related tables). The `clients` table structure indicates up to approximately 27,900 registered accounts (pharmacists, doctors, pharmacy staff, pharmacy students and other users) with email address, hashed password, name, professional address, city, specialty, phone/mobile numbers, country and date of birth. The volume and structure of the backups support a significant exposure of healthcare-sector professional accounts; the completeness of the extraction and its origin have not been independently confirmed.

### 31 December 2025
#### 🇰🇪 Kenya - Kenya Electricity Transmission Company (KETRACO)
- **Incident type:** Data Leak
- **Actor / Group:** LindaBF, post published on a cybercriminal forum (RaidForums)
- **Sector:** Energy / Electricity Transmission (Critical Infrastructure)
- **Website:** [ketraco.co.ke](https://ketraco.co.ke)
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Kenya Electricity Transmission Company (KETRACO) is a Kenyan state corporation responsible for developing, operating and maintaining the country's high-voltage electricity transmission grid.
- **Analysis:** The actor LindaBF published a post on December 31, 2025 titled "ketraco.co.ke database Kenya", with the download link restricted to forum members who reply to the thread. The visible sample shows a structured user-directory export (fields USER_ID, USER_NAME, USER_PASSWORD, USER_FIRSTNAME, USER_LASTNAME, USER_EMAIL, USER_LASTLOGIN, USER_FLAGS, USER_OU, USER_DATECREATED) tied to an organisational-unit path labelled "nl_KETRACO_Newsletter_Unit", consistent with a newsletter-subscriber or directory-service account list rather than core operational systems. Real-looking Kenyan names, email addresses and account-creation timestamps are visible, but numerous rows in the sample share an identical password value, which is inconsistent with independently generated per-user hashes and may indicate a shared default value, a placeholder, or a partially fabricated sample; this anomaly lowers AFRINTEL's confidence in the sample to a medium level. Given KETRACO's role in national power-transmission infrastructure, any confirmed compromise, even one limited to a newsletter or directory service, would be of concern for a critical-infrastructure operator and could indicate a broader foothold. AFRINTEL does not reproduce any username, email address, password value or record from the sample and has not accessed the linked download.

---

*AFRINTEL compilation — source of truth: monthly files.*
