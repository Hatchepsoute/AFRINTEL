[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%7C%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in February 2024 (12 victims)
👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

February 2024 contains **12 documented incident records**: **7 Ransomware**, **5 Data Leak**, **0 Access Sale**, **0 DDoS**, **0 Defacement** and **0 Operational Fraud**, across **7 African countries**.

### February 1, 2024

#### 🇪🇬 Egypt - 8WORX
- **Publication date:** June 30, 2023
- **Discovery date:** February 1, 2024
- **Actor / Group:** Tanaka
- **Sector:** Technology / IT
- **Website:** [8worx.com](https://8worx.com)
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** 8WORX is a technology solutions provider legally established in Delaware, USA, that states a business focus on Egypt and the Middle East, developing web applications and systems for private and public sector clients.
- **Analysis:** The post is published under the Tanaka account, which carries a moderator badge on the forum, so the original intrusion actor is not identified. The forum post advertises a 1.3 GB SQL export dated 2023, with roughly 4 million rows across tables including phone numbers, activity logs and social accounts, structured around a "Leads" module consistent with a CRM or lead-management system. The visible sample shows genuine-looking SQL INSERT statements with detailed contact, activity-tracking and account fields, and a large share of the phone records carry an Egypt (EG) country code, consistent with 8WORX's stated regional focus. The structural consistency of the schema and the plausibility of the sampled records support a high confidence assessment that the sample is authentic, though AFRINTEL has not independently confirmed the intrusion, the full scope of the underlying database, or the completeness of the announced 4-million-row volume. Exposure of this dataset would combine phone numbers, email addresses, lead and account activity, and internal user references for a very large number of individuals, creating a significant risk of targeted phishing, social engineering and fraud. AFRINTEL does not reproduce any phone number, email address, name or internal record from the reviewed sample.

----------------------------

### February 6, 2024

#### 🇪🇬 Egypt - ArpuPlus
- **Ransomware Group:** medusa
- **Sector:** Technology / IT
- **Website:** [arpuplus.com](https://www.arpuplus.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** ArpuPlus, founded in 2003 in Cairo as a subsidiary of A15, is a leading digital venture builder and mobile services provider across the MENA region. Operating from 11 regional offices, it delivers value-added systems including video-on-demand, music distribution, telehealth, and enterprise messaging solutions.

----------------------------

### February 10, 2024

#### 🇹🇳 Tunisia - SOPEM Tunisie
- **Ransomware Group:** hunters
- **Sector:** Manufacturing / Industry
- **Website:** [sopem.com.tn](https://www.sopem.com.tn)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** SOPEM Tunisie (Société Tunisienne de Profilage de Métaux) is an industrial manufacturing company specialized in metal profiling and transformation. Headquartered in Tunisia, the firm supplies metal structures and industrial engineering components for construction and manufacturing sectors.

----------------------------

### February 13, 2024

#### 🇿🇦 South Africa - The Aurum Institute
- **Ransomware Group:** lockbit3
- **Sector:** Healthcare / Medical
- **Website:** [auruminstitute.org](https://www.auruminstitute.org)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Aurum Institute is a prominent African public benefit organization established in 1998 and headquartered in Johannesburg. Specialized in health research and policy implementation, it focuses on global health issues, generating critical scientific evidence and health programs against HIV and Tuberculosis.

----------------------------

### February 16, 2024

#### 🇿🇦 South Africa - Government Pensions Administration Agency (GPAA) / Government Employees Pension Fund (GEPF)
- **Incident date:** February 16, 2024
- **Initial publication date:** March 12, 2024
- **AFRINTEL correction date:** August 23, 2026
- **Ransomware Group:** lockbit3
- **Sector:** Government / Administration
- **Website:** [gepf.co.za](https://www.gepf.co.za/)
- **Status:** Victim Confirmed + Threat Actor Claim
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Evidence note:** The ransomware event and compromise of personal data are victim-confirmed. Threat-actor claims about the completeness or additional scope of published data remain separate from confirmed facts.
- **Victim Description:** GPAA administers pension benefits on behalf of the GEPF, one of Africa's largest pension funds serving government employees, pensioners and beneficiaries.
- **Analysis:** GPAA experienced a cyberattack on February 16, 2024. GEPF later confirmed that criminals launched ransomware against GPAA systems and that approximately **168,000 data-subject records** were accessed. Confirmed affected data categories include identity, pension, employment, salary, marital, banking and tax information. LockBit published data and claimed responsibility. The ransomware event and data compromise are victim-confirmed; AFRINTEL keeps the confirmed 168,000-record impact separate from any broader threat-actor publication claims.
- **Public sources:** [GEPF official breach notification](https://www.gepf.co.za/notice/notification-of-security-compromise-as-per-section-22-of-the-protection-of-personal-information-act-4-of-2013-popia/2/) | [GEPF media release](https://www.gepf.co.za/government-pensions-administration-agency-gpaa-data-breach/)

----------------------------

### February 23, 2024

#### 🇿🇦 South Africa - Companies and Intellectual Property Commission (CIPC)
- **Incident date:** February 23, 2024
- **Initial publication date:** February 29, 2024
- **AFRINTEL correction date:** August 23, 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [cipc.co.za](https://www.cipc.co.za/)
- **Status:** Victim Confirmed - Multi-effect Incident
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Taxonomy note:** `Data Leak` is used as the primary AFRINTEL type because unauthorized access to and exposure of personal information are officially supported. Extortion behaviour and website defacement are retained as secondary effects; ransomware malware deployment is not established.
- **Victim Description:** CIPC is South Africa's corporate and intellectual-property regulator and maintains company, client and employee records.
- **Analysis:** CIPC's official reporting states that a data breach was detected on February 23, 2024 and involved unauthorized access to its systems. Personal information of clients and employees was unlawfully accessed and exposed. CIPC's annual reporting further states that intruders threatened to encrypt and publicly release data in lieu of a ransom, defaced the e-Services website and sent malicious emails to internal staff. Systems were isolated and restored, and law-enforcement and regulatory authorities were notified. The attacker remains publicly unattributed. AFRINTEL therefore records `Data Leak` as the primary controlled type while preserving extortion and defacement as secondary effects.
- **Public sources:** [CIPC POPIA notification](https://www.cipc.co.za/?p=20614) | [CIPC Q4 report](https://www.cipc.co.za/wp-content/uploads/2026/04/CIPC_2023-24_Q4-Report-Narrative_vf_20240430.pdf) | [CIPC annual report](https://www.cipc.co.za/wp-content/uploads/2025/01/CIPC-Annual-Report-2023-2024.pdf)

----------------------------

### February 2024 - exact incident date not publicly established

#### 🇲🇼 Malawi - Department of Immigration and Citizenship Services - Passport Issuance System
- **Incident date:** February 2024 - exact date not publicly established
- **Initial publication date:** February 21, 2024
- **AFRINTEL correction date:** August 23, 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [immigration.gov.mw](https://www.immigration.gov.mw/)
- **Status:** Government Confirmed - Technical Details Contested
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Taxonomy note:** `Ransomware` is a provisional primary AFRINTEL mapping because the government publicly described a cybersecurity breach involving a ransom demand. The exact root cause, attacker identity and technical ransomware deployment remain contested or unresolved.
- **Victim Description:** Malawi's Department of Immigration and Citizenship Services operates the national passport-issuance infrastructure.
- **Analysis:** Malawi's president publicly described the passport-system outage as a serious cybersecurity breach and said attackers had demanded a ransom. The Department of Immigration later confirmed that passport services had been disrupted by a cybersecurity breach and that demographic data lost as a result had been recovered. However, local civil-society and supplier statements disputed aspects of the government's technical narrative and suggested that licensing or system-management issues may also have contributed to the outage. AFRINTEL therefore records the service disruption and official breach declaration as confirmed while keeping the exact technical root cause and ransomware deployment qualified as contested.
- **Public sources:** [Malawi government press release](https://www.malawi.gov.mw/index.php/resources/documents/press-releases?download=145%3Aofficial-passport-press-release-from-the-department-of-immigration-and-citizenship-services) | [Malawi Broadcasting Corporation](https://mbc.mw/?p=10487) | [VOA context](https://www.voanews.com/a/some-question-malawi-president-s-claim-that-cyberattack-caused-passport-problems-/7498879.html)

----------------------------

### February 24, 2024

#### 🇪🇹 Ethiopia - Regional Trade and Integration Ministries of Ethiopia
- **Publication date:** August 24, 2023
- **Discovery date:** February 24, 2024
- **Actor / Group:** ThreatSec
- **Sector:** Government / Administration
- **Websites:** [etrade.gov.et](https://etrade.gov.et) and [eris.efda.gov.et](https://eris.efda.gov.et)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** The Ethiopian government portals identified in the publication support regional trade, integration, importer/exporter registration and related certification processes.
- **Analysis:** The forum post claims that ThreatSec breached the two Ethiopian government portals and collected 43 files, including government documents, PDFs and images containing government identifiers. The screenshot supports the existence of the publication and the claimed scope, but AFRINTEL has not independently verified the compromise, the origin of the files or the completeness and authenticity of the archive. Potential impacts include exposure of official documents, targeted phishing, identity fraud and abuse of trade-registration information. Credentials visible in the source material are not reproduced.

----------------------------

### February 24, 2024

#### 🇬🇭 Ghana - National Teaching Council (tpg.ntc.gov.gh)
- **Publication date:** July 16, 2023
- **Discovery date:** February 24, 2024
- **Actor / Group:** Tanaka
- **Sector:** Government / Administration
- **Website:** [tpg.ntc.gov.gh](https://tpg.ntc.gov.gh/)
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** Ghana's National Teaching Council (NTC) is the statutory body responsible for licensing and regulating the teaching profession. The tpg.ntc.gov.gh portal supports its Teaching Practice Guidelines process for student teachers enrolled in colleges of education across the country.
- **Analysis:** The forum post, attributed to the moderator account Tanaka, advertises a SQL export of the `students` table, dated to 2019 data and announced at roughly 41,000 rows. The visible sample shows genuine-looking `INSERT INTO` statements with a wide field set (student ID, status, names, index number, sex, phone, programme, level, date of birth, nationality, marital status, place of residence, home town, contact address, region, email, credit and grade-point totals, college and year-group, class, disability status, exam status, previous school, certificate dates, and related enrollment fields), populated with individual student-teacher records across multiple colleges of education. The structural consistency of the field set and the plausibility of the college codes and record values support a high confidence assessment that the sample is authentic, though AFRINTEL has not independently confirmed the intrusion, the full scope of the underlying database, or the completeness of the announced 41,000-row volume. Exposure of this dataset would combine full names, contact details, national origin, marital status, home address and academic records for a large number of student teachers, creating a significant risk of identity fraud, targeted phishing and impersonation. AFRINTEL does not reproduce any student name, email address, phone number, address or academic record from the reviewed sample.

### February 24, 2024

#### 🇨🇮 Ivory Coast - Agence Emploi Jeunes
- **Publication date:** July 21, 2023
- **Discovery date:** February 24, 2024
- **Actor / Group:** Tanaka
- **Sector:** Government / Administration
- **Website:** [agenceemploijeunes.ci](https://agenceemploijeunes.ci)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** Agence Emploi Jeunes is a Côte d’Ivoire public employment service focused on supporting young people’s access to employment and professional opportunities.
- **Analysis:** The forum publication advertises a 3.2 GB SQL file associated with agenceemploijeunes.ci, reporting approximately 2,300 rows and 296,000 unique users or email addresses. The visible schema includes applicant, user-account, identity, contact, education, employment and placement-related fields, and the screenshot shows SQL INSERT statements containing personal records. The announced figures are internally inconsistent and the full dataset was not independently verified, so AFRINTEL records this as a medium-confidence data-sample publication rather than a confirmed compromise. If authentic, the material could support identity fraud, targeted phishing, employment-related social engineering and abuse of job-seeker information. AFRINTEL does not reproduce names, email addresses, phone numbers, passwords or other personal data from the sample.

----------------------------


----------------------------

### February 27, 2024

#### 🇨🇮 Ivory Coast - Nouvelle Parfumerie Gandour (NPGCI)
- **Ransomware Group:** lockbit3
- **Sector:** Manufacturing / Industry
- **Website:** [npgandour.com](https://npgandour.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Nouvelle Parfumerie Gandour (NPGCI) is a leading West African cosmetics and consumer goods manufacturing company, based in the Yopougon industrial zone in Abidjan, Ivory Coast. The firm produces a vast portfolio of body care, hair care, oral hygiene, and perfume products distributed continent-wide.

----------------------------

### February 29, 2024

#### 🇿🇦 South Africa - ERWAT (Ekurhuleni Water Care Company)
- **Ransomware Group:** dragonforce
- **Sector:** Water / Utilities
- **Website:** [erwat.co.za](https://erwat.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** ERWAT (Ekurhuleni Water Care Company) is a major South African public utility established in 1992, specializing in bulk wastewater conveyance and treatment. It provides cost-effective and innovative environmental wastewater management solutions to thousands of industries and over 3.5 million residents.

----------------------------

## ✍🏿 Author
*Adama ASSIONGBON*
*SOC & Cyber Threat Intelligence Consultant*
[LinkedIn profile](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)
