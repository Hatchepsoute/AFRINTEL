[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# African victims - March 2025

👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

**15 documented cyber incidents** under AFRINTEL Taxonomy v2: Ransomware 9, Data Leak 2, Access Sale 1, Account Takeover 2, System Intrusion 1.

> Public-source links are added to supplementary incidents identified through online research to complete the corpus. They are not retroactively imposed on historical AFRINTEL records, including Dark Web observations.

## March 2025

### 02 March 2025
#### 🇧🇼 Botswana - IT-IQ Botswana
- **Ransomware Group:** play
- **Sector:** Technology Consulting
- **Website:** www.itiq.co.bw
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
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
- **Incident type:** Ransomware
- **Victim Description:** LINKGROUP is a South African IT consulting and telecom services company.

### 03 March 2025
#### 🇹🇿 Tanzania - synaptic.co.tz
- **Ransomware Group:** arcusmedia
- **Sector:** Technology Consulting
- **Website:** synaptic.co.tz
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
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

### 07 March 2025
#### South Africa - Pam Golding Properties
- **Actor / Group:** Unknown
- **Sector:** Construction / Real Estate
- **Website:** https://www.pamgolding.co.za/
- **Incident date:** 7 March 2025 - date confirmed in the company's statement
- **Initial publication date:** 11 March 2025
- **Status:** Victim Confirmed
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** Pam Golding Properties is a major South African real-estate group with a large portfolio of clients and properties.
- **Analysis:** Pam Golding stated that on 7 March 2025 an unknown third party gained unauthorized access to its customer-relationship-management system through a user account and viewed some customer personal information. The company stated that banking details, financial information, business information and other documents were not compromised. The access was contained and notifications were made. The available statement supports successful unauthorized access and personal-data exposure, but does not establish how the user account was obtained or identify the actor.
- **Source type:** Victim Statement
- **Public sources:** [Pam Golding media statement](https://propertyflash.co.za/2025/03/11/media-statement-issued-by-pam-golding-properties-re-a-cyber-incident/)

### 11 March 2025
#### 🇪🇬 Egypt - ISEE (International School of Elite Education)
- **Ransomware Group:** funksec
- **Sector:** Education / Private Schooling
- **Website:** isee-eg.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** The International School of Elite Education (ISEE) is a prestigious private school located in Cairo.

### 15 March 2025
#### South Africa - Parliament of South Africa
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** https://www.parliament.gov.za/
- **Incident date:** 15 March 2025 - date Parliament identified and publicly disclosed the breach; exact compromise start not stated
- **Initial publication date:** 15 March 2025
- **Status:** Victim Confirmed
- **Incident type:** Account Takeover
- **Subtype:** Compromised YouTube / streaming service
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Source type:** Official Victim Statement
- **Analysis:** A YouTube/streaming resource connected to Parliament's official channels was compromised and unauthorized content was uploaded. The incident affected a streaming service and does not establish compromise of Parliament's entire information system.
- **Sources:** [Parliament of South Africa - official statement](https://www.parliament.gov.za/press-releases/hacking-incident-parliaments-social-media)

### 16 March 2025
#### South Africa - Astral Foods Limited
- **Actor / Group:** Unknown
- **Sector:** Agriculture / Agribusiness
- **Website:** https://www.astralfoods.com/
- **Incident date:** 16 March 2025 - date confirmed by Astral Foods
- **Initial publication date:** 24 March 2025
- **Status:** Victim Confirmed
- **Incident type:** System Intrusion
- **Subtype:** Operational disruption - technical vector undisclosed
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Source type:** Official Company Disclosure
- **Analysis:** Astral Foods disclosed a cybersecurity incident on 16 March 2025 that disrupted poultry processing and customer deliveries and had an estimated profit impact of about R20 million. The company explicitly stated that no confidential or sensitive stakeholder information was compromised. AFRINTEL preserves the confirmed operational cyber incident without relabelling it as Data Leak or Ransomware.
- **Sources:** [Astral Foods - official SENS announcement](https://www.astralfoods.com/assets/Documents/News/SENS/2025/25.03.24%20Announcement%20-%20Voluntary%20trading%20update.VF.pdf)

### 17 March 2025
#### Ghana - Office of the President - John Dramani Mahama X account
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** https://x.com/JDMahama
- **Incident date:** 17 March 2025 - date the Cyber Security Authority received the report; exact compromise start not established
- **Initial publication date:** 18 March 2025
- **Status:** Authority Confirmed
- **Incident type:** Account Takeover
- **Subtype:** Compromised X account / cryptocurrency scam
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Source type:** National Cyber Authority + Public Media
- **Analysis:** Ghana's Cyber Security Authority confirmed that the President's X account was compromised and used to promote a fraudulent cryptocurrency project called "Solana Africa". The account was restored. The evidence does not establish compromise of Jubilee House networks or other government systems.
- **Sources:** [Ghana News Agency - CSA statement on restoration of the President's X account](https://gna.org.gh/2025/03/president-mahamas-x-account-restored/)

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

### 30 March 2025
#### 🇪🇬 Egypt - INI Investments
- **Ransomware Group:** nightspire
- **Sector:** Finance
- **Website:** iniholdings.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** INI Investments is a diversified Egyptian holding company. It invests in strategic sectors such as real estate, energy, technology, and financial services. The actor claims to have exfiltrated 400 GB of data; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.
- **Double-claim note:** The March and April records are retained separately because the source dates and evidence differ. They involve the same actor, domain and victim name, but AFRINTEL cannot determine from the available material whether the April publication is an update of the March claim or a separate claim. No merger is made pending confirmation.

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

---
