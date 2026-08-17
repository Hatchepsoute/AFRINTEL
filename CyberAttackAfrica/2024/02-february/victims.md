[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Cyber Attacks in Africa: February 2024: List of 9 Victims

### February 1, 2024

#### 🇪🇬 Egypt - 8WORX
- **Publication date:** June 30, 2023
- **Discovery date:** February 1, 2024
- **Actor / Group:** Tanaka, publication on an underground forum
- **Sector:** Technology / Software Services
- **Website:** [8worx.com](https://8worx.com)
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim description:** 8WORX is a technology solutions provider legally established in Delaware, USA, that states a business focus on Egypt and the Middle East, developing web applications and systems for private and public sector clients.
- **Analysis:** The post is published under the Tanaka account, which carries a moderator badge on the forum, so the original intrusion actor is not identified. The forum post advertises a 1.3 GB SQL export dated 2023, with roughly 4 million rows across tables including phone numbers, activity logs and social accounts, structured around a "Leads" module consistent with a CRM or lead-management system. The visible sample shows genuine-looking SQL INSERT statements with detailed contact, activity-tracking and account fields, and a large share of the phone records carry an Egypt (EG) country code, consistent with 8WORX's stated regional focus. The structural consistency of the schema and the plausibility of the sampled records support a high confidence assessment that the sample is authentic, though AFRINTEL has not independently confirmed the intrusion, the full scope of the underlying database, or the completeness of the announced 4-million-row volume. Exposure of this dataset would combine phone numbers, email addresses, lead and account activity, and internal user references for a very large number of individuals, creating a significant risk of targeted phishing, social engineering and fraud. AFRINTEL does not reproduce any phone number, email address, name or internal record from the reviewed sample.

----------------------------

### February 6, 2024

#### 🇪🇬 Egypt - ArpuPlus
- **Ransomware group:** medusa
- **Sector:** Digital Services & Telecom
- **Website:** [arpuplus.com](https://www.arpuplus.com)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim description:** ArpuPlus, founded in 2003 in Cairo as a subsidiary of A15, is a leading digital venture builder and mobile services provider across the MENA region. Operating from 11 regional offices, it delivers value-added systems including video-on-demand, music distribution, telehealth, and enterprise messaging solutions.

----------------------------

### February 10, 2024

#### 🇹🇳 Tunisia - SOPEM Tunisie
- **Ransomware group:** hunters
- **Sector:** Manufacturing (Metallurgy)
- **Website:** [sopem.com.tn](https://www.sopem.com.tn)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim description:** SOPEM Tunisie (Société Tunisienne de Profilage de Métaux) is an industrial manufacturing company specialized in metal profiling and transformation. Headquartered in Tunisia, the firm supplies metal structures and industrial engineering components for construction and manufacturing sectors.

----------------------------

### February 13, 2024

#### 🇿🇦 South Africa - The Aurum Institute
- **Ransomware group:** lockbit3
- **Sector:** Healthcare & Research
- **Website:** [auruminstitute.org](https://www.auruminstitute.org)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim description:** The Aurum Institute is a prominent African public benefit organization established in 1998 and headquartered in Johannesburg. Specialized in health research and policy implementation, it focuses on global health issues, generating critical scientific evidence and health programs against HIV and Tuberculosis.

----------------------------

### February 24, 2024

#### 🇪🇹 Ethiopia - Regional Trade and Integration Ministries of Ethiopia
- **Publication date:** August 24, 2023
- **Discovery date:** February 24, 2024
- **Actor / Group:** ThreatSec, publication by Tanaka on an underground forum
- **Sector:** Government / Public Administration
- **Website:** [etrade.gov.et](https://etrade.gov.et) and [eris.efda.gov.et](https://eris.efda.gov.et)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim description:** The Ethiopian government portals identified in the publication support regional trade, integration, importer/exporter registration and related certification processes.
- **Analysis:** The forum post claims that ThreatSec breached the two Ethiopian government portals and collected 43 files, including government documents, PDFs and images containing government identifiers. The screenshot supports the existence of the publication and the claimed scope, but AFRINTEL has not independently verified the compromise, the origin of the files or the completeness and authenticity of the archive. Potential impacts include exposure of official documents, targeted phishing, identity fraud and abuse of trade-registration information. Credentials visible in the source material are not reproduced.

----------------------------

### February 24, 2024

#### 🇬🇭 Ghana - National Teaching Council (tpg.ntc.gov.gh)
- **Publication date:** July 16, 2023
- **Discovery date:** February 24, 2024
- **Actor / Group:** Tanaka, publication on an underground forum
- **Sector:** Government / Education (Teacher Training Regulation)
- **Website:** [tpg.ntc.gov.gh](https://tpg.ntc.gov.gh/)
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim description:** Ghana's National Teaching Council (NTC) is the statutory body responsible for licensing and regulating the teaching profession. The tpg.ntc.gov.gh portal supports its Teaching Practice Guidelines process for student teachers enrolled in colleges of education across the country.
- **Analysis:** The forum post, attributed to the moderator account Tanaka, advertises a SQL export of the `students` table, dated to 2019 data and announced at roughly 41,000 rows. The visible sample shows genuine-looking `INSERT INTO` statements with a wide field set (student ID, status, names, index number, sex, phone, programme, level, date of birth, nationality, marital status, place of residence, home town, contact address, region, email, credit and grade-point totals, college and year-group, class, disability status, exam status, previous school, certificate dates, and related enrollment fields), populated with individual student-teacher records across multiple colleges of education. The structural consistency of the field set and the plausibility of the college codes and record values support a high confidence assessment that the sample is authentic, though AFRINTEL has not independently confirmed the intrusion, the full scope of the underlying database, or the completeness of the announced 41,000-row volume. Exposure of this dataset would combine full names, contact details, national origin, marital status, home address and academic records for a large number of student teachers, creating a significant risk of identity fraud, targeted phishing and impersonation. AFRINTEL does not reproduce any student name, email address, phone number, address or academic record from the reviewed sample.

### February 24, 2024

#### 🇨🇮 Ivory Coast - Agence Emploi Jeunes
- **Publication date:** July 21, 2023
- **Discovery date:** February 24, 2024
- **Actor / Group:** Tanaka, publication on an underground forum
- **Sector:** Government / Employment Services
- **Website:** [agenceemploijeunes.ci](https://agenceemploijeunes.ci)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim description:** Agence Emploi Jeunes is a Côte d’Ivoire public employment service focused on supporting young people’s access to employment and professional opportunities.
- **Analysis:** The forum publication advertises a 3.2 GB SQL file associated with agenceemploijeunes.ci, reporting approximately 2,300 rows and 296,000 unique users or email addresses. The visible schema includes applicant, user-account, identity, contact, education, employment and placement-related fields, and the screenshot shows SQL INSERT statements containing personal records. The announced figures are internally inconsistent and the full dataset was not independently verified, so AFRINTEL records this as a medium-confidence data-sample publication rather than a confirmed compromise. If authentic, the material could support identity fraud, targeted phishing, employment-related social engineering and abuse of job-seeker information. AFRINTEL does not reproduce names, email addresses, phone numbers, passwords or other personal data from the sample.

----------------------------


----------------------------

### February 27, 2024

#### 🇨🇮 Ivory Coast - Nouvelle Parfumerie Gandour (NPGCI)
- **Ransomware group:** lockbit3
- **Sector:** Consumer Goods (Cosmetics)
- **Website:** [npgandour.com](https://npgandour.com)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim description:** Nouvelle Parfumerie Gandour (NPGCI) is a leading West African cosmetics and consumer goods manufacturing company, based in the Yopougon industrial zone in Abidjan, Ivory Coast. The firm produces a vast portfolio of body care, hair care, oral hygiene, and perfume products distributed continent-wide.

----------------------------

### February 29, 2024

#### 🇿🇦 South Africa - ERWAT (Ekurhuleni Water Care Company)
- **Ransomware group:** dragonforce
- **Sector:** Utilities (Wastewater Management)
- **Website:** [erwat.co.za](https://erwat.co.za)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim description:** ERWAT (Ekurhuleni Water Care Company) is a major South African public utility established in 1992, specializing in bulk wastewater conveyance and treatment. It provides cost-effective and innovative environmental wastewater management solutions to thousands of industries and over 3.5 million residents.

----------------------------

## ✍🏿 Author
*Adama ASSIONGBON*
*SOC & Cyber Threat Intelligence Consultant*
[LinkedIn profile](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)
