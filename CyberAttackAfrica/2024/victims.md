# AFRINTEL victim records 2024 - corrected annual corpus

[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Period](https://img.shields.io/badge/Period-2024-lightgrey)
![Records](https://img.shields.io/badge/Records-128-critical)
![TLP](https://img.shields.io/badge/TLP-CLEAR-brightgreen)

👉🏾 [French version](./victims_FR.md)

This annual file is rebuilt directly from the twelve harmonized monthly AFRINTEL victim files. It contains **128 documented cyber records across 28 African countries**. Of these, **127 fall inside AFRINTEL's six-type core taxonomy**: 91 Ransomware, 31 Data Leak, 3 Access Sale, 1 Defacement and 1 Operational Fraud. **GTBank is retained separately as one victim-confirmed attempted attack** because the evidence does not support forcing it into an unsupported core category.

The 10 validated retrospective 2024 corrections are fully integrated. Publication date, claimed incident date, correction date and evidential caveats are preserved in the individual cards when available.


## January 2024


### January 1, 2024

#### 🇰🇪 Kenya - Kenya News Broadcasting Company (K24)

- **Actor / Group:** Tanaka
- **Sector:** Media / Entertainment
- **Status:** Claim - Data Sample Published
- **Website:** [24tv.co.ke](https://24tv.co.ke)
- **Confidence level:** Medium
- **Impact level:** Level 2
- **Incident type:** Data Leak
- **Leak date:** 2023 (exact date not specified)
- **Discovery date:** January 2024 (exact day not specified; monthly placement uses January 1)
- **Source publication date:** June 19, 2023

- **Reliability note:**
  The screenshot identifies a K24 database claim attributed to Tanaka, the domain 24tv.co.ke, an announced 28 MB SQL file and approximately 56,000 rows. The local file supplied for review is not readable SQL: it contains 30.1 MB of 0xFF bytes with no line terminators or usable SQL header. The exact compromise date and independent confirmation are unknown.

- **Description:**
  Kenya News Broadcasting Company operates the K24 news broadcasting platform in Kenya. The publication presents a database claim associated with the K24 WordPress site.

- **Analysis:**
  The visible sample references the WordPress wp_options table and website configuration or content-management fields, including cookie-banner settings, category and menu configuration, custom CSS and related site options. The screenshot does not establish whether personal data, credentials or complete user records were included in the claimed SQL file. AFRINTEL does not reproduce any database values from the sample.

- **Recommendations:**
  1. Verify the claim against WordPress, database, web-server and administrator logs, review the wp_options table and active administrator accounts, and rotate credentials if exposure is confirmed.
  2. Audit plugins and themes, restrict database exports, enforce MFA for privileged users and monitor the K24 domain for defacement, phishing or unauthorized content changes.

----------------------------


### January 1, 2024

#### 🇩🇿 Algeria - University of Oran

- **Actor / Group:** zebi
- **Sector:** Education / University
- **Status:** Claim - Data Sample Published
- **Website:** Not identified with sufficient confidence
- **Confidence level:** Medium
- **Impact level:** Level 2
- **Incident type:** Data Leak
- **Leak date:** September 12, 2023
- **Discovery date:** January 1, 2024

- **Reliability note:**
  The publication is explicitly described as a "repost". It contains a data sample attributed to a "University of Oran", but does not identify the exact institution, original compromise date, total database size or initial access method. The original publication is not provided.

- **Description:**
  The threat actor `zebi` reposted a database presented as originating from a university in Oran, Algeria. A sample is directly visible in the forum post, while additional downloadable content is locked behind the forum's access mechanism.

- **Analysis:**
  The visible sample follows a database structure containing the fields `numero`, `nom`, `prenom`, `datenaiss`, `teleph`, `sexe`, `email`, `mot_passe` and `nationalite`.

  The records therefore expose personal and account-related information, including identities, dates of birth, telephone numbers, email addresses, gender and nationality. Values under the `mot_passe` field appear to resemble cryptographic hashes rather than immediately readable passwords; however, the algorithm and security of those values cannot be established from the screenshot alone.

  The presence of multiple consistent records increases confidence that the actor possessed a structured dataset. However, the screenshot does not establish the technical source of the data, the total number of affected individuals or which specific university in Oran was compromised.

  The disclosed information could support targeted phishing, identity impersonation, profiling of affected students or users and credential-reuse attempts against other services.

- **Recommendations:**
  1. Identify the affected institution and application, review authentication logs and reset exposed accounts if the breach is confirmed.
  2. Search for redistribution of the dataset across other leak sources and warn affected users about phishing and account-compromise risks.

----------------------------


### January 1, 2024

#### 🇧🇫 Burkina Faso - BIA-Market

- **Actor / Group:** Tanaka
- **Sector:** Retail / E-commerce
- **Status:** Claim - Data Sample Published
- **Website:** [bia-market.com](https://www.bia-market.com)
- **Confidence level:** Medium
- **Impact level:** Level 2
- **Incident type:** Data Leak
- **Leak date:** 2023 (exact date not specified)
- **Discovery date:** January 2024 (exact day not specified; monthly placement uses January 1)
- **Source publication date:** June 23, 2023

- **Reliability note:**
  The reviewed forum screenshot identifies bia-market.com, Burkina Faso country-code filtering (BF-60) and a SQL sample. The source gives a 2023 date and states that the post was published on June 23, 2023. The exact compromise date, detection day, affected application and independent confirmation are unknown.

- **Description:**
  BIA-Market is an e-commerce platform operating in Burkina Faso. The publication presents a 4.5 GB SQL file containing approximately 5,000 rows and shows records from the site's database structure. AFRINTEL records this case in January 2024 as the detection period requested for this incident.

- **Analysis:**
  The visible sample references the vb_users table and fields including login, email, user URL, registration date, activation key, status and display name. The sample indicates exposure of account and platform metadata, but no raw credentials or personal records are reproduced here. The screenshot does not prove the authenticity or completeness of the dataset, nor does it confirm how or when BIA-Market was accessed.

- **Recommendations:**
  1. Verify the claim against application, database and web-server logs, rotate potentially exposed credentials and invalidate active sessions or activation tokens if the dataset is confirmed.
  2. Review customer and administrator accounts, enforce MFA where available, monitor password-reuse and phishing activity, and preserve evidence for an incident investigation.

----------------------------


### January 1, 2024

#### 🇲🇦 Morocco - Morocco Forum Site

- **Actor / Group:** r57
- **Sector:** Technology / IT
- **Status:** Claim - Data Sample Published
- **Website:** Not specified
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Discovery date:** January 2024 (monthly placement requested)
- **Source publication date:** September 29, 2023

- **Reliability note:**
  A cybercriminal-forum post titled "Morocco Forum Site" advertises a sample from a claimed 180,000-record dataset and displays a price of USD 50. The source sample visibly contains account records with usernames, email addresses, password-related values and IP-address fields. AFRINTEL does not reproduce any raw records, credentials, hashes, IP addresses or access information. The screenshot does not establish the forum's ownership, the dataset's authenticity, the exact affected population or the date of the underlying compromise.

- **Description:**
  Morocco Forum Site is presented in the source as an online forum or community platform associated with Moroccan users. The exact legal entity and domain are not identified in the publication.

- **Analysis:**
  The visible sample suggests exposure of user-account data and authentication-related fields. If authentic, the dataset could support targeted phishing, account takeover attempts, credential-stuffing or password-reset abuse. The advertised volume and price remain actor claims. Because the source publication predates the requested January 2024 placement, AFRINTEL records the source date separately and does not treat January as the incident or publication date.


### January 1, 2024

#### 🇷🇼 Rwanda - Government of Rwanda (multiple domains)

- **Actor / Group:** Milad
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** [cheno.gov.rw](https://cheno.gov.rw), [cnlg.gov.rw](https://cnlg.gov.rw), [nurc.gov.rw](https://nurc.gov.rw), [yego.gov.rw](https://yego.gov.rw)
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Incident type:** Data Leak
- **Discovery date:** January 2024 (monthly placement requested)
- **Source publication date:** June 17, 2023

- **Reliability note:**
  A forum post titled "Government Rwanda Database [ Full Backup ]", published June 17, 2023 by the account Milad, claims a combined 329 MB SQL backup covering four Rwandan government domains (cheno.gov.rw, cnlg.gov.rw, nurc.gov.rw, yego.gov.rw), describing the leak date only as "2023" and rating the data as "Normal" sensitivity in the poster's own classification. The posting account is currently shown as banned on the forum; the stated ban reason is not visible in the reviewed post. The displayed sample shows a raw SQL export of a `be_users` administrative-accounts table containing backend usernames, password hashes (phpass and MD5 formats) and extensive CMS session/configuration data, alongside Kinyarwanda-language content references consistent with Rwandan public-sector communication. AFRINTEL does not reproduce any username, password hash, session token or other credential-related value from the sample.

- **Description:**
  The claim references four Rwandan government web domains. Based on their naming, cnlg.gov.rw corresponds to the National Commission for the Fight against Genocide (Commission Nationale de Lutte contre le Génocide, CNLG) and nurc.gov.rw corresponds to the National Unity and Reconciliation Commission (NURC); the specific institutions behind cheno.gov.rw and yego.gov.rw are not identified in the source and are not assumed here. The visible sample's Kinyarwanda-language content, including genocide-remembrance and commemorative references, is consistent with, but does not independently confirm, an association with one of these bodies.

- **Analysis:**
  The post claims a single 329 MB SQL "full backup" spanning four separate government domains, an unusually broad scope for one export that is not independently corroborated beyond the visible sample. The sample itself displays a coherent backend-administration table (`be_users`) with realistic usernames, hashed credentials in recognised formats, and CMS session metadata, consistent with a genuine database export; however, the poster labels the CMS as "Custom" while the table structure and field names visible in the sample are characteristic of the TYPO3 content-management system, an inconsistency AFRINTEL cannot resolve from the available material. If genuine, compromise of backend administrative credentials across national government and reconciliation-related institutions could enable unauthorised content manipulation, further lateral access to internal systems, and reputational or trust impact on state institutions tied to Rwanda's genocide-memory and national-unity mandate. AFRINTEL treats this as a claim with a published data sample; the authenticity, current validity of the credentials, and the scope of the leak beyond the reviewed table are not independently verified.


### January 2, 2024

#### 🇬🇭 Ghana - Financial Intelligence Centre (FIC)

- **Actor / Group:** DataHoes
- **Sector:** Government / Administration
- **Status:** Data Fully Published
- **Website:** [fic.gov.gh](https://fic.gov.gh)
- **Confidence level:** High
- **Impact level:** Level 4
- **Incident type:** Data Leak
- **Leak date:** December 3, 2023
- **Discovery date:** January 2, 2024

- **Reliability note:**
  The post is attributed to the forum account "DataHoes" (subsequently banned) and states an extraction date, an archive size, a file and folder count, and links to a full directory-tree listing hosted on a separate file-sharing service. AFRINTEL reviewed the forum post and the sampled directory tree but did not download or open the referenced archive or the full tree-list file.

- **Description:**
  The Financial Intelligence Centre (FIC) is Ghana's national agency responsible for receiving and analysing suspicious transaction reports and other information relevant to money laundering, terrorist financing and proliferation financing, and for disseminating actionable intelligence to competent authorities.

- **Analysis:**
  The actor states the data was extracted on December 3, 2023, and describes an archive of 2.0 GiB across 6,025 files and 663 sub-folders, with a full directory listing published separately. The sampled directory tree shows folders labelled "FIC HR DOCS" and "Finance_Scans", containing internal governance and HR material (an accounting manual, an audit manual, a board charter, conditions-of-service and human-resource policy documents, staff-numbers records) and multi-year scanned finance correspondence (bank statement requests, payment authorisations, foreign-exchange requests, monthly payroll notices). One filename explicitly references FIC's response to a GIABA/ICRG nomination process, which is consistent with FIC's known anti-money-laundering mandate and supports the authenticity of the dataset. Several filenames in the sample also reference individually named staff members' academic certificates and payroll documents.

  Given the sensitivity of a national financial-intelligence unit's internal HR, payroll, banking and governance records, exposure of this material could facilitate targeted social engineering or phishing against FIC staff, disclosure of internal banking arrangements, and reputational or operational impact on a body central to Ghana's anti-money-laundering and counter-terrorist-financing framework. AFRINTEL did not access the referenced archive or the linked directory-tree file, and does not reproduce any staff name, financial figure or document content beyond the folder and file names visible in the reviewed forum post.

- **Recommendations:**
  1. FIC should verify whether the described extraction genuinely originates from its own systems, review access logs predating and around December 3, 2023, and assess exposure of the banking, payroll and HR data referenced in the post.
  2. Rotate any credentials or banking correspondence references named in the exposed documents, and monitor for downstream use of the leaked directory in phishing campaigns targeting FIC staff or partner institutions.

----------------------------


### January 2, 2024

#### 🇿🇦 South Africa - International Trade Administration Commission of South Africa (ITAC)
- **Incident date:** January 2, 2024
- **Initial publication date:** April 15, 2024
- **AFRINTEL correction date:** August 23, 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [itac.org.za](https://itac.org.za/)
- **Status:** Victim Confirmed
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Evidence note:** ITAC officially confirmed a ransomware attack. Possible access to and exfiltration of personal information is reported by the victim but remains qualified as possible rather than confirmed.
- **Victim Description:** ITAC is South Africa's statutory trade-administration body and processes information relating to employees, service providers, importers, exporters and other stakeholders.
- **Analysis:** ITAC states that it suffered a ransomware attack on January 2, 2024. Malicious actors encrypted files, locked users out of systems and demanded a ransom. ITAC shut down affected servers, restored backups and initiated forensic work. The official notification also states that the attacker may have accessed and possibly extracted personal information held on ITAC servers. The exact actor, initial access vector, ransom amount and confirmed exfiltration scope were not publicly established in the reviewed source. The ransomware event is therefore victim-confirmed, while data exfiltration remains possible rather than confirmed.
- **Public source:** [ITAC official notification](https://itac.org.za/notification-of-a-personal-information-security-compromise/)

----------------------------


### January 3, 2024

#### 🇳🇬 Nigeria - The Citizens' Watch

- **Actor / Group:** X0Frankenstein
- **Sector:** Civil Society / NGO
- **Status:** Claim - Data Sample Published
- **Website:** [thecitizenswatch.com](https://thecitizenswatch.com/)
- **Confidence level:** High
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Discovery date:** January 3, 2024
- **Claimed leak date:** 2023 (year only, exact date not specified by the source)

- **Reliability note:**
  A forum post titled "SQL Database The Citizens Watch", published January 3, 2024 by the account X0Frankenstein, claims a SQL database leak associated with thecitizenswatch.com, describing over 56,000 lines and stating the leak date only as "2023". The post displays raw SQL record excerpts spanning several distinct table structures, including apparent user/admin accounts with bcrypt-format password hashes, event and training registrant records, applicant/CV submission records, and what appears to be an unrelated geographic reference table included in the same paste. AFRINTEL does not reproduce any of the visible names, email addresses, phone numbers, password hashes, uploaded file paths or other personal data from the sample.

- **Description:**
  The Citizens' Watch (thecitizenswatch.com) is presented as a promise-tracking platform enabling citizens, civil society, journalists, scholars and policy analysts to track government officials' campaign commitments. It is described as an initiative of The Reformers Initiative for Development in Africa ("Reformers of Africa"), a pan-African civic-tech non-profit stated to operate across multiple African countries including Nigeria, South Sudan, Namibia, the Democratic Republic of the Congo, Tunisia, Comoros and South Africa. The organization's precise country of registration or headquarters is not stated in the source; the visible sample shows a strong concentration of Nigerian contact details (Lagos, Ekiti, Oyo, Ogun, Kogi, Anambra), which AFRINTEL uses to place this entry under Nigeria while noting the organization's pan-African scope.

- **Analysis:**
  The visible excerpt mixes several distinct table structures rather than a single coherent schema, consistent with either a genuinely compromised multi-table database export or an assembled paste; AFRINTEL cannot independently confirm the origin of each table segment. Where legible, the sample includes user records with names, email addresses, phone numbers, a bcrypt-format password hash, uploaded CV file references, dates of birth and account-status fields, alongside event/training registration entries and an apparently unrelated geographic reference table. If authentic, exposure of this data could expose citizen and event-registrant personal data (names, contact details, CV documents) to phishing, social-engineering and account-takeover risk, and any exposed password hash could be subject to offline cracking if the hashing scheme is weak or reused elsewhere. AFRINTEL classifies this as a data-sample-published claim given the volume and structure of visible records, while noting that the domain's ownership of each table segment and the full scope of the underlying database are not independently verified.

----------------------------


### January 7, 2024

#### 🇨🇲 Cameroon - University of Buea (UB)

- **Actor / Group:** cnHunter
- **Sector:** Education / University
- **Status:** Claim - Unverified
- **Website:** [ubuea.cm](https://ubuea.cm)
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Access Sale
- **Discovery date:** January 7, 2024

- **Reliability note:**
  A forum post titled "[Admin Access] ubuea.cm", published January 7, 2024 and edited the same day, claims administrative-level access to a REDCap instance hosted at redcap.ubuea.cm, referencing an upload/import handler path and an external file hosted on a file-sharing service as "proof". AFRINTEL did not access the referenced proof file or the claimed target system. The posting account, cnHunter, was subsequently permanently banned from the forum for suspected scamming, which materially reduces confidence in the underlying claim.

- **Description:**
  The University of Buea (UB) is a public university in Cameroon's South-West Region, offering programmes across faculties including science, health sciences, engineering, arts, law, and social and management sciences. REDCap instances deployed by universities are typically used to manage academic, survey and clinical or research data.

- **Analysis:**
  The post asserts administrative access to a REDCap data-collection instance associated with the university's domain and is later marked "Unlocked" in an edit, but provides no visible data sample, no independently verifiable evidence and no listed price. Combined with the subsequent permanent ban of the posting account for suspected scamming, AFRINTEL treats this as a low-confidence, unverified claim. If genuine, unauthorised administrative access to a REDCap instance could expose research, survey or academic records tied to students, staff or study participants; neither the access nor any underlying dataset is confirmed.

----------------------------


### January 10, 2024

#### 🇿🇦 South Africa - TiAuto Investments
- **Ransomware Group:** lockbit3
- **Sector:** Retail / E-commerce
- **Website:** [tiautoinvestments.co.za](https://www.tiautoinvestments.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** TiAuto Investments is a prominent South African holding company specialized in the retail and wholesale distribution of wheels, tires, and automotive accessories. Founded in 2006 and headquartered in Midrand, it controls leading continental brands like Tiger Wheel & Tyre and Tyres & More.

----------------------------


### January 10, 2024

#### 🇿🇦 South Africa - Tiger Wheel & Tyre
- **Ransomware Group:** lockbit3
- **Sector:** Retail / E-commerce
- **Website:** [twt.co.za](https://twt.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Tiger Wheel & Tyre is a flagship subsidiary of TiAuto Investments, boasting over 50 years of operation and managing more than 100 fitment centers across South Africa and Southern Africa. It specializes in wheel alignment, balancing, and premium tire retail services.

----------------------------


### January 26, 2024

#### 🇪🇬 Egypt - Btech.com
- **Actor / Group:** Tanaka
- **Sector:** Retail / E-commerce
- **Website:** [btech.com](https://www.btech.com)
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 2
- **Incident type:** Data Leak
- **Victim Description:** Btech.com is an Egyptian retail chain selling electronics and home appliances.
- **Analysis:** The actor Tanaka, a forum moderator, published a claim on January 26, 2024 concerning Btech.com, described as a 20 MB CSV export dated February 23, 2023 and totaling 203,265 rows. The advertised field header includes: ID, Name, Email, Phone, ZIP, Country, State/Province, Customer Since, Billing Address, Shipping Address, Date of Birth, Gender, Street Address, City, Company.

  The sample shown in the post displays real customer records with names, email addresses, detailed postal addresses in Arabic, dates of birth (mostly unpopulated) and gender. Several sample rows also contain additional values beyond the 15 fields advertised in the header, matching the 14-digit format of Egyptian national identity numbers, along with a name and phone number distinct from the primary account holder, suggesting a richer underlying data structure than described in the post's public header.

  The consistency of the CSV format, the advertised volume and the presence of plausible customer records with detailed addresses support a high confidence level regarding the authenticity of this leak, although the total claimed volume of 203,265 rows could not be independently verified beyond the observed sample. The possible presence of national identity numbers not documented in the header is an aggravating factor, as this data is particularly sensitive in Egypt. Exposure of this data could facilitate identity theft, fraud and targeted phishing against the retailer's customers. AFRINTEL does not reproduce any name, email address, postal address, date of birth or identity number from the reviewed sample.


### January 29, 2024

#### 🇿🇦 South Africa - Crowe Southern Africa
- **Ransomware Group:** lockbit3
- **Sector:** Professional / Business Services
- **Website:** [crowe.com/za](https://www.crowe.com/za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Crowe Southern Africa is a premier professional services firm and an independent member of the global Crowe Global network. With established offices in Johannesburg, Cape Town, and Stellenbosch, it delivers high-quality audit, tax, forensic accounting, and corporate financial advisory.

----------------------------


### January 29, 2024

#### 🇨🇲 Cameroon - Eneo Cameroon
- **Incident date:** January 29, 2024
- **Initial publication date:** February 2, 2024
- **AFRINTEL correction date:** August 23, 2026
- **Actor / Group:** Unknown
- **Sector:** Energy / Utilities
- **Website:** [eneocameroon.cm](https://eneocameroon.cm/)
- **Status:** Victim Confirmed - Ransomware Classification Unverified
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Taxonomy note:** The cyberattack and operational disruption are victim-confirmed. `Ransomware` is retained as a provisional AFRINTEL taxonomy mapping because secondary CTI sources classify the incident as ransomware; victim-facing reporting reviewed here does not independently confirm ransomware deployment.
- **Victim Description:** Eneo Cameroon is the country's principal electricity utility and operates customer billing and prepaid/postpaid electricity services.
- **Analysis:** Eneo confirmed that a cyberattack beginning on January 29, 2024 significantly disrupted its computer systems. Some applications were disabled as a security precaution, and prepaid/postpaid customer operations were affected, including difficulties buying electricity units. Public reporting and later African cybercrime assessments corroborate the attack. Some CTI sources classify the event as ransomware, but the reviewed victim-facing reporting does not provide enough technical detail to independently confirm ransomware deployment. The confirmed facts are therefore the cyberattack and material operational disruption; ransomware remains a qualified secondary assessment.
- **Public sources:** [ITWeb Africa](https://itweb.africa/article/cameroons-power-utility-suffers-a-cyber-attack/8OKdWqDXArbqbznQ) | [OBS-CC](https://obs-cc.org/incident/eneo-cameroon/)

----------------------------


## February 2024


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


## March 2024


### March 1, 2024

#### 🇪🇹 Ethiopia - Federal eTrade and eRIS portals
- **Actor / Group:** ThreatSec
- **Sector:** Government / Administration
- **Website:** [etrade.gov.et](https://etrade.gov.et) ; [eris.efda.gov.et](https://eris.efda.gov.et)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** The publication links the Ethiopian Ministry of Trade and Regional Integration's eTrade portal with the Ethiopian Food and Drug Authority's eRIS system. These are two separate federal services combined in a single claim.

- **Analysis:**
  - **Observed:** the entry is filed under March 1, 2024 at the maintainer's request. The forum publication, relayed by Tanaka and dated August 24, 2023, attributes to ThreatSec a claim of access to both portals and collection of 43 files, including PDFs, images, and government identity documents. One locally provided PDF was examined read-only: 3,023,068 bytes, five scanned pages, SHA-256 `5184bdfc94dfd42e4d78da290ea3860ac074360c684a715354e0447241bfc642`. All five pages contain an Amharic-language administrative and contractual document with official stamps, handwritten signatures, and financial amounts. No raw personal data is reproduced.
  - **Assumption:** the document characteristics are consistent with an Ethiopian administrative record and increase confidence in the sample's structural plausibility, without establishing its technical provenance.
  - **Unknown:** the acquisition method, the PDF's direct link to each portal, the existence and content of the other 42 claimed files, and confirmation by the affected authorities remain unverified. Visual review covered all five pages, but complete Amharic OCR could not be validated.

----------------------------


### March 9, 2024

#### 🇪🇬 Egypt - Go4Kora
- **Ransomware Group:** ransomhub
- **Sector:** Media / Entertainment
- **Website:** [go4kora.tv](https://go4kora.tv)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Go4Kora is a popular sports news and live streaming portal extensively accessed in Egypt and the MENA region for football broadcasting.

----------------------------


### March 11, 2024

#### 🇿🇦 South Africa - Government Printing Works (GPW)
- **Ransomware Group:** lockbit3
- **Sector:** Government / Administration
- **Website:** [gpw.gov.za](https://www.gpw.gov.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Government Printing Works of South Africa is a state-owned entity under the Department of Home Affairs responsible for secure identity documentation, passports, and official gazettes.

----------------------------


### March 15, 2024

#### 🇹🇳 Tunisia - ATL Leasing
- **Ransomware Group:** hunters
- **Sector:** Finance / Banking
- **Website:** [atlleasing.com.tn](https://www.atlleasing.com.tn)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Arab Tunisian Leasing (ATL) is a prominent financial institution listed on the Tunis Stock Exchange, specializing in professional equipment and real estate financing.

----------------------------


### March 15, 2024

#### 🇪🇬 Egypt - El Ezaby Pharmacy
- **Ransomware Group:** lockbit3
- **Sector:** Healthcare / Medical
- **Website:** [elezabypharmacy.com](https://www.elezabypharmacy.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** El Ezaby Pharmacy is one of Egypt's largest pharmaceutical retail networks, operating numerous megastores and a robust nation-wide delivery ecosystem.

----------------------------


### March 16, 2024

#### 🇳🇦 Namibia - Agribank Namibia
- **Ransomware Group:** lockbit3
- **Sector:** Finance / Banking
- **Website:** [agribank.com.na](https://www.agribank.com.na)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Agricultural Bank of Namibia is a state-owned banking institution specialized in financing agricultural expansion, aquaculture, and rural land ownership.

----------------------------


### March 22, 2024

#### 🇪🇬 Egypt - PGESCo
- **Ransomware Group:** ransomhub
- **Sector:** Energy / Utilities
- **Website:** [pgesco.com](https://www.pgesco.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Power Generation Engineering and Services Company (PGESCo) is a major Egyptian engineering firm providing consultancy and project management for large-scale power plants and industrial oil facilities.

----------------------------


### March 26, 2024

#### 🇲🇦 Morocco - Higher School of Commerce and Management (ESGC.MA)
- **Actor / Group:** Unknown
- **Sector:** Education / University
- **Website:** [esgc.ma](https://esgc.ma)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** ESGC.MA is presented as a Moroccan higher-education institution focused on commerce and management.

- **Analysis:** The forum publication dated March 26, 2024 claims that a database from 2021 contained approximately 500 entries with names, email addresses, password hashes, phone numbers and account-creation dates. A sample was displayed, but the complete dataset and the alleged compromise were not independently verified. Personal data and credentials from the sample are not reproduced here.

----------------------------


### March 27, 2024

#### 🇿🇦 South Africa - Nampak
- **Ransomware Group:** lockbit3
- **Sector:** Manufacturing / Industry
- **Website:** [nampak.com](https://www.nampak.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Nampak is Africa's largest packaging manufacturer, based in South Africa, supplying metallic, plastic, paper, and glass packaging solutions across sub-Saharan networks.

----------------------------


## April 2024


### 04 April 2024

#### 🇸🇨 Seychelles - Remitano (Cryptocurrency Exchange)
- **Ransomware Group:** incransom
- **Sector:** Finance / Banking
- **Website:** N/A (Mobile App & Exchange Platform)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Remitano (Cryptocurrency Exchange) is listed on the incransom ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Remitano App is an Escrowed Peer-to-Peer (P2P) Cryptocurrency Exchange platform designed to Buy, Sell, Store, Invest, Deposit, and Withdraw cryptocurrencies using fiat currencies.

- **Analysis:**
  AFRINTEL recorded Remitano (Cryptocurrency Exchange) (Seychelles) as a claimed ransomware victim published by incransom. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. Given the organization's activity in the Banking institutions / Crypto assets sector, a compromise of this type would typically expose customer account, payment or financial information, with associated risks of phishing, fraud or business disruption. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this incransom listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer and payment-data protection and financial-sector incident-response procedures in case evidence of compromise emerges.


### 13 April 2024

#### 🇿🇦 South Africa - Caxton and CTP Publishers and Printers
- **Ransomware Group:** hunters
- **Sector:** Media / Entertainment
- **Website:** https://www.caxton.co.za
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Caxton and CTP Publishers and Printers is listed on the hunters ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Caxton and CTP Publishers and Printers is one of the largest publishers and printers of books, magazines, newspapers, and commercial packaging in South Africa.

- **Analysis:**
  AFRINTEL recorded Caxton and CTP Publishers and Printers (South Africa) as a claimed ransomware victim published by hunters. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. Given the organization's activity in the Medias and audiovisual / Publishing sector, a compromise of this type would typically expose employee, customer or operational information, with associated risks of phishing, fraud or business disruption. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this hunters listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare data protection and incident-response procedures in case evidence of compromise emerges.


### April 19, 2024

#### 🇪🇬 Egypt - Vezeeta Pharmacy (vezeeta.com)

- **Initial publication date:** April 19, 2024
- **AFRINTEL detection date:** August 21, 2026
- **Actor / Group:** EgyptLeaks
- **Sector:** Healthcare / Medical
- **Website:** [vezeeta.com](https://www.vezeeta.com)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak

- **Description:**

  Vezeeta is an Egyptian healthcare-booking and online-pharmacy platform. The post specifically targets Vezeeta Pharmacy and advertises order data.

- **Analysis:**

  **Observed:** A post attributed to EgyptLeaks, dated April 19, 2024, offers approximately 133,000 Vezeeta Pharmacy order records covering 2021, 2022 and 2023. The displayed sample contains order fields for contact, zone, order status, payment, branch, products and delivery addresses. Personal values visible in the sample are not reproduced by AFRINTEL.

  **Assumption:** The match between the Vezeeta Pharmacy name, vezeeta.com domain, branch names and order-export structure is compatible with a customer-data exposure in Egypt. If authentic, the data could enable targeted phishing, delivery fraud, impersonation of staff or pharmacies and indirect exposure of health information inferred from ordered products.

  **Unknown:** AFRINTEL did not receive the complete archive or independently verify the claimed 133,000 orders, acquisition method, completeness, current validity of contact data, presence of protected medical data or any Vezeeta confirmation. The assessment is limited to the visible screenshot and excerpt; no name, phone number, address, person-linked product or order identifier is reproduced.


### 23 April 2024

#### 🇧🇫 Burkina Faso - ONEF (National Observatory for Employment and Training)
- **Actor / Group:** Pedi
- **Sector:** Government / Administration
- **Website:** [onef.gov.bf](https://onef.gov.bf)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Description:** The Observatoire national de l’emploi et de la formation (ONEF) is a Burkinabè public institution focused on employment and vocational-training information.
- **Analysis:** A forum publication presents a database associated with onef.gov.bf as a free SQL release and shows the structure of an application table named `actualite`, containing fields related to news and publication metadata. The screenshot does not establish the database's authenticity, completeness or initial access method. AFRINTEL records the publication as a claim with a data sample and does not reproduce database values.


### 29 April 2024

#### 🇲🇦 Morocco - SM EMBALLAGE
- **Ransomware Group:** spacebears
- **Sector:** Manufacturing / Industry
- **Website:** https://smemballage.com/
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  SM EMBALLAGE is listed on the spacebears ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  SM Emballage specializes in customized industrial packaging solutions designed for protecting, preserving, and simplifying the transport and storage of manufactured and agricultural products in Morocco.

- **Analysis:**
  AFRINTEL recorded SM EMBALLAGE (Morocco) as a claimed ransomware victim published by spacebears. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. Given the organization's activity in the Manufacturing / Industrial Packaging sector, a compromise of this type would typically expose supplier, customer or operational information, with associated risks of phishing, fraud or business disruption. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this spacebears listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare operational-data protection and incident-response procedures in case evidence of compromise emerges.


### 29 April 2024

#### 🇿🇦 South Africa - Thinkadam
- **Ransomware Group:** spacebears
- **Sector:** Technology / IT
- **Website:** https://www.thinkadam.co/
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Thinkadam is listed on the spacebears ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Thinkadam provides advanced remote device-locking solutions tailored for the smartphone-on-credit industry, helping providers mitigate payment defaults.

- **Analysis:**
  AFRINTEL recorded Thinkadam (South Africa) as a claimed ransomware victim published by spacebears. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. Given the organization's activity in the Technologies sector, a compromise of this type would typically expose customer, partner or internal technical information, with associated risks of phishing, fraud or business disruption. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this spacebears listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer-data protection and technology-sector incident-response procedures in case evidence of compromise emerges.


### 30 April 2024

#### 🇱🇾 Libya - Mellitah Oil & Gas (Eni / NOC Joint Venture)
- **Ransomware Group:** ransomhub
- **Sector:** Energy / Utilities
- **Website:** N/A
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Mellitah Oil & Gas (Eni / NOC Joint Venture) is listed on the ransomhub ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Mellitah Oil & Gas is a major operating company and energy consortium in Libya, run as a joint venture between the Libyan National Oil Corporation (NOC) and Eni North Africa.

- **Analysis:**
  AFRINTEL recorded Mellitah Oil & Gas (Eni / NOC Joint Venture) (Libya) as a claimed ransomware victim published by ransomhub. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. Given the organization's activity in the Oil & Gas / Energy sector, a compromise of this type would typically expose operational, partner or employee information, with associated risks of phishing, fraud or business disruption. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this ransomhub listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare operational-data protection and incident-response procedures for energy-sector operators in case evidence of compromise emerges.


## May 2024


### May 6, 2024

#### 🇳🇬 Nigeria - Nestoil
- **Ransomware Group:** blacksuit
- **Sector:** Construction / Real Estate
- **Website:** [nestoilgroup.com](https://www.nestoilgroup.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Nestoil is a major commercial enterprise operating in the construction sector, contributing significantly to the regional economic landscape in Nigeria.

----------------------------


### May 6, 2024

#### 🇪🇬 Egypt - Elarabygroup
- **Ransomware Group:** lockbit3
- **Sector:** Professional / Business Services
- **Website:** [elarabygroup.com](https://www.elarabygroup.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Elarabygroup is a major commercial enterprise operating in the business services sector, contributing significantly to the regional economic landscape in Egypt.

----------------------------


### May 7, 2024

#### 🇿🇦 South Africa - Lenmed
- **Ransomware Group:** lockbit3
- **Sector:** Healthcare / Medical
- **Website:** [lenmed.co.za](https://www.lenmed.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Lenmed is a major commercial enterprise operating in the healthcare services sector, contributing significantly to the regional economic landscape in South Africa.

----------------------------


### May 7, 2024

#### 🇿🇦 South Africa - Kamo jou trading
- **Ransomware Group:** ransomhub
- **Sector:** Finance / Banking
- **Website:** [kamojou.co.za](https://www.kamojou.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Kamo jou trading is a major commercial enterprise operating in the finance sector, contributing significantly to the regional economic landscape in South Africa.

----------------------------


### May 9, 2024

#### 🇳🇦 Namibia - Eif.na
- **Ransomware Group:** lockbit3
- **Sector:** Finance / Banking
- **Website:** [eif.org.na](https://www.eif.org.na)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Eif.na is a major commercial enterprise operating in the financial organizations sector, contributing significantly to the regional economic landscape in Namibia.

----------------------------


### May 13, 2024

#### 🇨🇮 Ivory Coast - Treasury of cote d'ivoire
- **Ransomware Group:** hunters
- **Sector:** Finance / Banking
- **Website:** [tresor.gouv.ci](https://www.tresor.gouv.ci)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Treasury of cote d'ivoire is a major commercial enterprise operating in the finance sector, contributing significantly to the regional economic landscape in Ivory Coast.

----------------------------


### May 16, 2024

#### 🇪🇬 Egypt - Egyptian sudanese
- **Ransomware Group:** arcusmedia
- **Sector:** Professional / Business Services
- **Website:** Not validated from the provided source
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Egyptian sudanese is a major commercial enterprise operating in the services sector, contributing significantly to the regional economic landscape in Egypt.

----------------------------


### May 25, 2024

#### 🇸🇳 Senegal - Sysroad
- **Ransomware Group:** lockbit3
- **Sector:** Technology / IT
- **Website:** [sysroad.com](https://www.sysroad.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Sysroad is a major commercial enterprise operating in the information technologies consulting sector, contributing significantly to the regional economic landscape in Senegal.

----------------------------


### May 2024 - exact incident date not publicly disclosed

#### 🇿🇦 South Africa - Department of Public Works and Infrastructure (DPWI)
- **Incident date:** May 2024 - exact date not publicly disclosed
- **Initial publication date:** 10 July 2024
- **AFRINTEL correction date:** 23 August 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [publicworks.gov.za](https://www.publicworks.gov.za/)
- **Status:** Government Confirmed - Forensic Investigation
- **Incident type:** Operational Fraud
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Taxonomy note:** `Operational Fraud` is used because the confirmed event is cyber-enabled financial theft associated with a system compromise. Public sources do not establish ransomware deployment, a standalone data leak, or the exact technical intrusion path.
- **Victim Description:** South Africa's Department of Public Works and Infrastructure manages public buildings, infrastructure and property-related government functions.
- **Analysis:** The South African government disclosed that cybercriminal activity had siphoned substantial funds from DPWI over a prolonged period and that the latest incident in May 2024 resulted in a further **R24 million** being stolen. The May loss triggered a full forensic investigation involving the Hawks, SAPS, the State Security Agency and cybersecurity specialists. Government officials also raised the possibility of collusion between insiders and criminals. The public source does not establish the exact intrusion path, specific payment-control weakness or identity of the attackers. AFRINTEL therefore records the May event as a government-confirmed Operational Fraud incident involving cyber-enabled financial theft and system compromise, without assigning an unsupported malware family or access technique.
- **Public source:** [SAnews - DPWI investigates theft](https://www.sanews.gov.za/south-africa/dpwi-investigates-theft-r300-million)

----------------------------


## June 2024


### 4 June 2024

#### 🇿🇦 South Africa - Botselo
- **Ransomware Group:** arcusmedia
- **Sector:** Agriculture / Agribusiness
- **Website:** [botselo.com](https://www.botselo.com)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Botselo appears on the arcusmedia leak site. AFRINTEL observed no accessible sample, screenshot or data extract associated with the publication at collection time, and the claim was not independently confirmed by the organization.

- **Description:**
  Botselo is a South African organization classified under Agriculture / Agribusiness in the AFRINTEL corpus.

- **Analysis:**
  AFRINTEL recorded Botselo (South Africa) as a victim claimed by the ransomware group arcusmedia. No leaked file, database extract or screenshot was accessible for analysis, so the potential scope, volume and sensitivity of any affected data cannot be assessed. Without an accessible sample, AFRINTEL cannot determine which data categories may have been involved or whether any operational disruption actually occurred. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset on the basis of this publication alone.

- **Recommendations:**
  1. Review the external attack surface, remote-access services and backup integrity following the arcusmedia publication, and verify the availability of offline or immutable backups.
  2. Monitor for any later publication of data samples associated with the claim and prepare incident-response procedures if evidence of compromise emerges.

----------------------------


### 6 June 2024

#### 🇨🇬 Congo - Burotec.biz
- **Ransomware Group:** eldorado
- **Sector:** Professional / Business Services
- **Website:** [burotec.biz](https://www.burotec.biz)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Burotec.biz appears on the eldorado leak site. AFRINTEL observed no accessible sample, screenshot or data extract associated with the publication at collection time, and the claim was not independently confirmed by the organization.

- **Description:**
  Burotec.biz is an organization based in Congo. The monthly sources do not document its activity more precisely, so AFRINTEL retains the harmonized sector Professional / Business Services.

- **Analysis:**
  AFRINTEL recorded Burotec.biz (Congo) as a victim claimed by the ransomware group eldorado. No leaked file, database extract or screenshot was accessible for analysis, so the potential scope, volume and sensitivity of any affected data cannot be assessed. Without an accessible sample, AFRINTEL cannot determine which data categories may have been involved or whether any operational disruption actually occurred. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset on the basis of this publication alone.

- **Recommendations:**
  1. Review the external attack surface, remote-access services and backup integrity following the eldorado publication, and verify the availability of offline or immutable backups.
  2. Monitor for any later publication of data samples associated with the claim and prepare incident-response procedures if evidence of compromise emerges.

----------------------------


### 23 June 2024

#### 🇿🇦 South Africa - Glyn Marais
- **Ransomware Group:** cactus
- **Sector:** Legal / Justice
- **Website:** [glynmarais.co.za](https://www.glynmarais.co.za)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Glyn Marais appears on the cactus leak site. AFRINTEL observed no accessible sample, screenshot or data extract associated with the publication at collection time, and the claim was not independently confirmed by the organization.

- **Description:**
  Glyn Marais is a South African organization classified under Legal / Justice in the AFRINTEL corpus.

- **Analysis:**
  AFRINTEL recorded Glyn Marais (South Africa) as a victim claimed by the ransomware group cactus. No leaked file, database extract or screenshot was accessible for analysis, so the potential scope, volume and sensitivity of any affected data cannot be assessed. Without an accessible sample, AFRINTEL cannot determine which data categories may have been involved or whether any operational disruption actually occurred. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset on the basis of this publication alone.

- **Recommendations:**
  1. Review the external attack surface, remote-access services and backup integrity following the cactus publication, and verify the availability of offline or immutable backups.
  2. Monitor for any later publication of data samples associated with the claim and prepare incident-response procedures if evidence of compromise emerges.

----------------------------


## July 2024


### July 1, 2024

#### 🇹🇳 Tunisia - Maxcess-logistics
- **Ransomware Group:** killsec
- **Sector:** Transport / Logistics
- **Website:** [maxcess-logistics.com](https://www.maxcess-logistics.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Maxcess-logistics is a Tunisia-based organization classified under Transport / Logistics in the AFRINTEL corpus.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.


### July 2, 2024

#### 🇪🇹 Ethiopia - F.D.R.E Defence War College (cited domain: nwc.ndu.edu)

- **Actor / Group:** TheColorYellow
- **Source context:** Data-sale post published on RaidForums
- **Sector:** Defense / Security
- **Status:** Claim - Data Sample Published
- **Website:** [dwc.edu.et](https://dwc.edu.et/wc/) (organization observed in the samples); actor-cited domain: nwc.ndu.edu
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Incident type:** Data Leak
- **Discovery date:** July 2, 2024

- **Reliability note:**
  TheColorYellow's post presents a victim called the "National War College of Ethiopia" and cites nwc.ndu.edu. That domain corresponds to the National War College of the US National Defense University. However, the five locally provided PNG files display the emblem and Amharic-language header of Ethiopia's "F.D.R.E Defence War College", together with internal documents, a visible inventory of 29 workstations, and a visible table of 17 telephone entries. A domain error in the announcement, a naming confusion, or incorrect technical attribution therefore remains possible. AFRINTEL records the F.D.R.E Defence War College as the organization observed in the samples and retains nwc.ndu.edu as the announced but unverified domain.

- **Description:**
  The visible elements correspond to the F.D.R.E Defence War College, an Ethiopian military-education institution. The official link observed for that organization is [dwc.edu.et](https://dwc.edu.et/wc/). nwc.ndu.edu remains only the domain cited in the actor's announcement.

- **Analysis:**
  TheColorYellow claims to hold 747 MB of confidential emails allegedly stolen directly from the institution's Exchange server, exported as PST mailbox files, and offers the data for $500 through escrow. The local directory contains five PNG files but no PST, EML, MSG, or Exchange export. The images include institutional documents, a Chinese notice for international students, a visible inventory of 29 workstations, and a visible table of 17 telephone entries. These elements are consistent with internal documents from the F.D.R.E Defence War College and strengthen sample attribution, but do not confirm access to the Exchange server, the existence of 747 MB, or the completeness or origin of the data. Amharic and Chinese OCR was not used to transcribe values; no name, hardware identifier, or telephone number is reproduced.


### July 5, 2024

#### 🇿🇦 South Africa - National health laboratory services
- **Ransomware Group:** blacksuit
- **Sector:** Healthcare / Medical
- **Website:** [nhls.ac.za](https://www.nhls.ac.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** National Health Laboratory Service (NHLS) is a South African public laboratory-services organization classified under Healthcare / Medical.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.


### July 11, 2024

#### 🇩🇿 Algeria - Hôpital Chahids Mahmoudi (hcm-dz.com)

- **Actor / Group:** Unknown
- **Source context:** Repost by Addka72424 of material attributed to FriendlyChemist
- **Sector:** Healthcare / Medical
- **Status:** Claim - Data Sample Published
- **Website:** [hcm-dz.com](https://hcm-dz.com)
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Leak date:** September 21, 2023
- **Discovery date:** July 11, 2024

- **Reliability note:**
  The post is explicitly presented as a repost ("REPOST") of a compilation titled "Algerian Databases Collection", itself reposted from an original post attributed to the account FriendlyChemist. The date and content of the original post are not provided, and the initial collection or access method is not specified.

- **Description:**
  Hôpital Chahids Mahmoudi is an Algerian hospital based in Tizi Ouzou, specialized in oncology and nuclear medicine, with an extension in Algiers and a clinic opened in Constantine in 2024. It operates the hcm-dz.com domain for its professional communications.

- **Analysis:**
  The file associated with hcm-dz.com in the compilation reposted on July 11, 2024 is dated September 21, 2023 and presented as covering approximately 1,900 users. The sample reviewed by AFRINTEL corresponds to email filtering logs (an anti-spam gateway type), not an export of medical records or full mailboxes.

  The visible lines indicate, for each message, the sender, recipient, source IP address, subject, size, a filtering score, direction (inbound, outbound or internal) and a message identifier. Several message subjects reference patient names and types of medical examinations (lab results, imaging, cardiology), indicating professional use of the hospital's email system to transmit results, without the message content itself being visible in the sample.

  The consistency of the log format and the observed volume of lines support a medium confidence level regarding the origin of these logs. AFRINTEL could not, however, confirm effective access to the mailboxes themselves, nor the completeness of any compromise beyond the reposted log lines. The presence of message subjects referencing named patients constitutes exposure of sensitive health-related metadata, which could facilitate targeted phishing, impersonation of medical or administrative staff, and partial reconstruction of care pathways. AFRINTEL does not reproduce any patient name, email address, IP address or message subject from the reviewed sample.


### July 11, 2024

#### 🇩🇿 Algeria - University of Tlemcen (univ-tlemcen.dz)

- **Actor / Group:** Unknown
- **Source context:** Repost by Addka72424 of material attributed to FriendlyChemist
- **Sector:** Education / University
- **Status:** Claim - Data Sample Published
- **Website:** [univ-tlemcen.dz](https://www.univ-tlemcen.dz)
- **Confidence level:** High
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Leak date:** June 27, 2022
- **Discovery date:** July 11, 2024

- **Reliability note:**
  As with the other files in the same compilation, the exact origin, initial access method and the date of FriendlyChemist's original post are not specified. The sample, however, shows a complete application table structure and consistent individual records.

- **Description:**
  The University of Tlemcen (Abou Bekr Belkaïd) is an Algerian public higher-education institution. It operates a Moodle e-learning platform accessible via the univ-tlemcen.dz domain.

- **Analysis:**
  The file associated with univ-tlemcen.dz in the compilation reposted on July 11, 2024 is dated June 27, 2022 and presented as covering approximately 80,000 users. The sample reviewed by AFRINTEL shows the structure of the `mdl_user` table, specific to the Moodle learning management system, along with an excerpt of real user records.

  The structural fields include the user ID, username, hashed password, first name, last name, email address, institution, department, country, language, and account creation/last-login dates. The visible records include an administrator account associated with the univ-tlemcen.dz domain, as well as accounts linked to email addresses from other Algerian universities, suggesting a shared authentication federation across several universities via this Moodle system rather than a scope limited to Tlemcen alone. Passwords are hashed using heterogeneous formats, including bcrypt for some recent accounts and older, weaker formats for others, without AFRINTEL being able to confirm their actual strength.

  The consistency of the Moodle table structure with the observed records, combined with the presence of an identifiable administrator account, supports a high confidence level regarding the authenticity of this dataset. A compromise of this scale could facilitate takeover of student and staff accounts, academic identity impersonation, and cascading access to other Algerian institutions potentially sharing the same authentication federation. AFRINTEL does not reproduce any credential, hashed password, email address or individual record from the reviewed sample.


### July 11, 2024

#### 🇩🇿 Algeria - Algeria.com (web portal)

- **Actor / Group:** Unknown
- **Source context:** Repost by Addka72424 of material attributed to FriendlyChemist
- **Sector:** Media / Entertainment
- **Status:** Claim - Data Sample Published
- **Website:** [algeria.com](https://www.algeria.com)
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Data Leak
- **Leak date:** September 2019
- **Discovery date:** July 11, 2024

- **Reliability note:**
  The data in this file is notably older (2019) than the other elements of the compilation. The domain algeria.com is a generic portal dedicated to Algeria rather than a national .dz domain; the exact origin of the leak and the period during which the associated user-account service was active are not specified.

- **Description:**
  Algeria.com is a web portal dedicated to Algeria (travel, news and lifestyle), which in the past offered user accounts and email addresses under its own domain to some of its visitors.

- **Analysis:**
  The file associated with algeria.com in the compilation reposted on July 11, 2024 is dated September 2019 and presented as covering approximately 3,600 user accounts. The sample reviewed by AFRINTEL includes the fields user ID, username, IP address, email address, a token, and a second field labeled "secret".

  The values observed in the token and secret fields do not match any standard cryptographic hash format clearly identifiable by AFRINTEL, and could correspond to an old proprietary mechanism of the portal rather than a directly exploitable password. The age of the data and the generic nature of the domain, distinct from Algerian institutional .dz domains, limit the current operational relevance of this exposure, although the associated email addresses and usernames could still be reused elsewhere by the individuals concerned.

  Given the age of the data, the limited volume and the absence of a clearly identifiable password field, AFRINTEL assesses this claim with a low confidence level and limited impact. AFRINTEL does not reproduce any identifier, email address, IP address or token value from the reviewed sample.


### July 13, 2024

#### 🇰🇪 Kenya - Kenya urban roads authority
- **Ransomware Group:** hunters
- **Sector:** Transport / Logistics
- **Website:** [kura.go.ke](https://www.kura.go.ke)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Kenya Urban Roads Authority (KURA) is a Kenyan public authority responsible for urban road infrastructure and is classified under Transport / Logistics.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.


### July 17, 2024

#### 🇿🇼 Zimbabwe - Zb financial holdings
- **Ransomware Group:** madliberator
- **Sector:** Finance / Banking
- **Website:** [zb.co.zw](https://www.zb.co.zw)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** ZB Financial Holdings is a Zimbabwean financial-services organization classified under Finance / Banking.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.


### July 17, 2024

#### 🇿🇦 South Africa - Cities network
- **Ransomware Group:** madliberator
- **Sector:** Professional / Business Services
- **Website:** [sacities.net](https://www.sacities.net)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** South African Cities Network is classified under Professional / Business Services in the AFRINTEL corpus.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.


### July 17, 2024

#### 🇪🇬 Egypt - Assih
- **Ransomware Group:** lockbit3
- **Sector:** Professional / Business Services
- **Website:** [assih.com](https://www.assih.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Assih is an Egypt-based organization classified under Professional / Business Services in the AFRINTEL corpus.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.


### July 22, 2024

#### 🇿🇦 South Africa - Sibanye-stillwater
- **Ransomware Group:** ransomhouse
- **Sector:** Mining / Extractive Industries
- **Website:** [sibanyestillwater.com](https://www.sibanyestillwater.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Sibanye-Stillwater is a South Africa-based mining organization classified under Mining / Extractive Industries.

---

- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.


## August 2024


### August 1, 2024

#### 🇸🇨 Seychelles - Remitano
- **Ransomware Group:** meow
- **Sector:** Finance / Banking
- **Website:** [remitano.com](https://www.remitano.com)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Remitano is listed on the meow ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Remitano is a major commercial enterprise operating in the finance sector, contributing significantly to the regional economic landscape in Seychelles.

- **Analysis:**
  AFRINTEL recorded Remitano (Seychelles) as a claimed ransomware victim published by meow. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this meow listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer and payment-data protection and financial-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 11, 2024

#### 🇿🇦 South Africa - Acdcexpress
- **Ransomware Group:** lockbit3
- **Sector:** Retail / E-commerce
- **Website:** [acdcexpress.com](https://www.acdcexpress.com)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Acdcexpress is listed on the lockbit3 ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Acdcexpress is a major commercial enterprise operating in the retail (distribution) sector, contributing significantly to the regional economic landscape in South Africa.

- **Analysis:**
  AFRINTEL recorded Acdcexpress (South Africa) as a claimed ransomware victim published by lockbit3. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this lockbit3 listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer-data protection and retail-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 13, 2024

#### 🇿🇼 Zimbabwe - Netone
- **Ransomware Group:** hunters
- **Sector:** Telecommunications
- **Website:** [netone.co.zw](https://www.netone.co.zw)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Netone is listed on the hunters ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Netone is a leading mobile network operator providing telecommunications infrastructure, voice, broadband data, and digital services.

- **Analysis:**
  AFRINTEL recorded Netone (Zimbabwe) as a claimed ransomware victim published by hunters. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this hunters listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare subscriber-data protection and telecom-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 13, 2024

#### 🇿🇦 South Africa - Lenmed
- **Ransomware Group:** darkvault
- **Sector:** Healthcare / Medical
- **Website:** [lenmed.co.za](https://www.lenmed.co.za)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Lenmed is listed on the darkvault ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Double-claim note:**
  Lenmed (lenmed.co.za) was already recorded as claimed by lockbit3 on May 7, 2024 (Claim - Unverified). The actor and the date differ, and no evidence points to a repost of the same material or a resale of the same dataset. AFRINTEL records this darkvault listing as an independent claim pending further evidence.

- **Description:**
  Lenmed is a major commercial enterprise operating in the healthcare services sector, contributing significantly to the regional economic landscape in South Africa.

- **Analysis:**
  AFRINTEL recorded Lenmed (South Africa) as a claimed ransomware victim published by darkvault. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this darkvault listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare patient-data protection and health-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 13, 2024

#### 🇿🇦 South Africa - Gpf.za
- **Ransomware Group:** darkvault
- **Sector:** Finance / Banking
- **Website:** [gpf.org.za](https://www.gpf.org.za)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Gpf.za is listed on the darkvault ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Gpf.za is a major commercial enterprise operating in the finance sector, contributing significantly to the regional economic landscape in South Africa.

- **Analysis:**
  AFRINTEL recorded Gpf.za (South Africa) as a claimed ransomware victim published by darkvault. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this darkvault listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer and payment-data protection and financial-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 14, 2024

#### 🇳🇬 Nigeria - Guaranty Trust Bank (GTBank)
- **Incident date:** 14 August 2024
- **Initial publication date:** 15 August 2024
- **AFRINTEL correction date:** 23 August 2026
- **Actor / Group:** Unknown
- **Sector:** Finance / Banking
- **Website:** [gtbank.com](https://www.gtbank.com/)
- **Status:** Victim Confirmed - Attempted Attack
- **Incident type:** Attempted Attack (taxonomy exception)
- **Confidence level:** High
- **Impact level:** Level 2
- **Taxonomy note:** This record is tracked separately from AFRINTEL's six core incident types. The available evidence does not support classifying the event as Ransomware, Data Leak, Access Sale, DDoS, Defacement or Operational Fraud.
- **Evidence note:** GTBank confirmed an isolated attempt to compromise its website domain. The bank stated that the attempt was unsuccessful, the website was not cloned and no customer-data compromise occurred.
- **Victim Description:** GTBank is a Nigerian commercial bank providing retail, corporate and digital banking services.
- **Analysis:** GTBank confirmed an isolated attempt to compromise its website domain on 14 August 2024. The event coincided with temporary website disruption and public speculation that the site had been cloned. According to the bank, the attempt failed, the website was not cloned and customer information was not stored on the website; no customer-data compromise was therefore confirmed. AFRINTEL records the event because the attempted domain compromise and availability impact were acknowledged by the victim, but does not convert it into a successful breach or assign an unsupported six-type category. The confirmed impact is limited to website/domain availability and incident response; the technical access method and actor remain unknown.
- **Public source:** [Punch - GTBank statement](https://punchng.com/gtb-confirms-attempt-to-hack-banks-website/)

----------------------------


### August 17, 2024

#### 🇿🇦 South Africa - Wwwconfig
- **Ransomware Group:** ransomhub
- **Sector:** Telecommunications
- **Website:** [netconfig.co.za](https://www.netconfig.co.za)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Wwwconfig is listed on the ransomhub ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Wwwconfig is a leading mobile network operator providing telecommunications infrastructure, voice, broadband data, and digital services.

- **Analysis:**
  AFRINTEL recorded Wwwconfig (South Africa) as a claimed ransomware victim published by ransomhub. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this ransomhub listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare subscriber-data protection and telecom-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 19, 2024

#### 🇹🇳 Tunisia - Eventizer
- **Actor / Group:** Bambi
- **Source context:** Publication on a cybercriminal forum
- **Sector:** Professional / Business Services
- **Website:** [eventizer.io](https://www.eventizer.io)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Eventizer is a Tunisian event-management agency and digital platform that centralises event registration, payments, access control, accommodation and dashboards.
- **Analysis:** The publication attributed to Bambi advertises approximately 60,000 records associated with Eventizer and presents a sample structured with user identifiers, names, email addresses, telephone numbers, countries and login-role information. The post title claims coverage involving Tunisia and Nigeria, while the visible sample contains records tagged with several countries. The sample demonstrates exposure of contact and account-context data, but the total volume, completeness, provenance and direct technical connection to Eventizer have not been independently verified. The exposed fields could support targeted phishing, impersonation, account-enumeration and social-engineering campaigns. Raw personal records and contact details are not reproduced.

----------------------------


### August 21, 2024

#### 🇨🇮 Ivory Coast - Codival
- **Ransomware Group:** spacebears
- **Sector:** Retail / E-commerce
- **Website:** [codival.ci](https://www.codival.ci)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Codival is listed on the spacebears ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Codival is a major commercial enterprise operating in the retail (distribution) sector, contributing significantly to the regional economic landscape in Ivory Coast.

- **Analysis:**
  AFRINTEL recorded Codival (Ivory Coast) as a claimed ransomware victim published by spacebears. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this spacebears listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer-data protection and retail-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 22, 2024

#### 🇿🇦 South Africa - Don’t waste group
- **Ransomware Group:** incransom
- **Sector:** Professional / Business Services
- **Website:** Not validated from the supplied source
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Don’t waste group is listed on the incransom ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Don’t waste group is a major commercial enterprise operating in the services sector, contributing significantly to the regional economic landscape in South Africa.

- **Analysis:**
  AFRINTEL recorded Don’t waste group (South Africa) as a claimed ransomware victim published by incransom. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this incransom listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare data protection and incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 22, 2024

#### 🇰🇪 Kenya - Instadriver.co
- **Ransomware Group:** killsec
- **Sector:** Retail / E-commerce
- **Website:** [instadriver.co](https://www.instadriver.co)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Instadriver.co is listed on the killsec ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Instadriver.co is a major commercial enterprise operating in the retail (distribution) sector, contributing significantly to the regional economic landscape in Kenya.

- **Analysis:**
  AFRINTEL recorded Instadriver.co (Kenya) as a claimed ransomware victim published by killsec. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this killsec listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer-data protection and retail-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 24, 2024

#### 🇸🇨 Seychelles - Ingotbrokers
- **Ransomware Group:** darkvault
- **Sector:** Finance / Banking
- **Website:** [ingotbrokers.com](https://www.ingotbrokers.com)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Ingotbrokers is listed on the darkvault ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Ingotbrokers is a major commercial enterprise operating in the financial organizations sector, contributing significantly to the regional economic landscape in Seychelles.

- **Analysis:**
  AFRINTEL recorded Ingotbrokers (Seychelles) as a claimed ransomware victim published by darkvault. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this darkvault listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer and payment-data protection and financial-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 26, 2024

#### 🇿🇦 South Africa - Onedayonly
- **Ransomware Group:** killsec
- **Sector:** Retail / E-commerce
- **Website:** [onedayonly.co.za](https://www.onedayonly.co.za)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Onedayonly is listed on the killsec ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Onedayonly is a major commercial enterprise operating in the shops sector, contributing significantly to the regional economic landscape in South Africa.

- **Analysis:**
  AFRINTEL recorded Onedayonly (South Africa) as a claimed ransomware victim published by killsec. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this killsec listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer-data protection and retail-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 28, 2024

#### 🇩🇯 Djibouti - Dpfza.gov.dj
- **Ransomware Group:** ransomhub
- **Sector:** Government / Administration
- **Website:** [dpfza.gov.dj](https://www.dpfza.gov.dj)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Dpfza.gov.dj is listed on the ransomhub ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Dpfza.gov.dj is a vital state-owned public institution or regulatory authority executing administrative services and citizen management operations.

- **Analysis:**
  AFRINTEL recorded Dpfza.gov.dj (Djibouti) as a claimed ransomware victim published by ransomhub. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this ransomhub listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare citizen-data protection and public-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 28, 2024

#### 🇿🇼 Zimbabwe - Success microfinance bank
- **Ransomware Group:** meow
- **Sector:** Finance / Banking
- **Website:** Not validated from the supplied source
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Ransomware

- **Reliability note:**
  Success microfinance bank is listed on the meow ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Success microfinance bank is a major commercial enterprise operating in the banking institutions sector, contributing significantly to the regional economic landscape in Zimbabwe.

- **Analysis:**
  AFRINTEL recorded Success microfinance bank (Zimbabwe) as a claimed ransomware victim published by meow. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this meow listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer and payment-data protection and financial-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


### August 28, 2024

#### 🇬🇭 Ghana - Ghanare
- **Ransomware Group:** BrainCipher
- **Sector:** Technology / IT
- **Website:** [ghanare.com](https://www.ghanare.com)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Ransomware

- **Reliability note:**
  Ghanare is listed on the BrainCipher ransomware leak site. AFRINTEL did not observe an accessible data sample, screenshot or extract associated with this listing at the time of collection, and the claim has not been independently confirmed by the organization.

- **Description:**
  Ghanare is a major commercial enterprise operating in the technologies sector, contributing significantly to the regional economic landscape in Ghana.

- **Analysis:**
  AFRINTEL recorded Ghanare (Ghana) as a claimed ransomware victim published by BrainCipher. No leaked file, database extract or screenshot was accessible for review, so the scope, volume and sensitivity of any exposed data cannot be assessed. AFRINTEL does not confirm intrusion, data exfiltration or the existence of a complete dataset based on this listing alone.

- **Recommendations:**
  1. Review external attack surface, remote-access services and backup integrity following this BrainCipher listing, and confirm whether offline or immutable backups are available.
  2. Monitor for any subsequent publication of data samples associated with this claim, and prepare customer-data protection and technology-sector incident-response procedures in case evidence of compromise emerges.

----------------------------


## September 2024


### September 6, 2024

#### 🇸🇳 Senegal - Sesam Informatics
- **Ransomware Group:** hunters
- **Sector:** Technology / IT
- **Website:** [sesam-informatics.com](https://www.sesam-informatics.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Sesam Informatics is a Senegalese technology and software services company operating in digital solutions and IT development.
- **Reliability note:** The supplied September corpus documents a ransomware publication but provides no public DFIR report, data sample or independent victim confirmation supporting a successful compromise.
- **Analysis:** AFRINTEL records the publication as a ransomware claim. The supplied evidence does not establish encryption, operational disruption, exfiltration scope, initial access or a confirmed victim response. The record therefore remains `Claim - Unverified`.

----------------------------


### September 7, 2024

#### 🇳🇬 Nigeria - Nigerian Navy (navy.mil.ng)
- **Actor / Group:** Unknown
- **Source context:** NizaarFarah is the source account shown on the September 7 publication; this does not establish intrusion attribution or the account's identity beyond the observed post.
- **Sector:** Defense / Security
- **Website:** https://navy.mil.ng
- **Source publication date:** September 7, 2024
- **Claimed leak date:** November 8, 2020
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Victim Description:** The Nigerian Navy is the naval branch of the Nigerian Armed Forces.
- **Evidence note:** The supplied screenshot claims hundreds of confidential files and 1,200 email logins, with approximately 300 files and a 228.4 MB archive advertised. The screenshot shows document and equipment samples, but AFRINTEL did not collect or reproduce the underlying files or credentials.
- **Analysis:** The source explicitly dates the claimed leak to **8 November 2020**. AFRINTEL therefore treats the September 2024 appearance as renewed observation or recirculation of older material, not evidence of a new September 2024 compromise. The screenshot supports the existence of a publication containing document and equipment samples, but does not establish the authenticity, completeness, current validity or full provenance of the advertised material. The 1,200 email-logins figure, approximately 300 files and 228.4 MB volume remain source claims.

----------------------------


### September 12, 2024

#### 🇨🇲 Cameroon - CNPS Cameroun
- **Ransomware Group:** spacebears
- **Sector:** Government / Administration
- **Website:** [cnps.cm](https://www.cnps.cm)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Caisse Nationale de Prévoyance Sociale (CNPS) of Cameroon is the public body responsible for managing social security and social benefits for workers.
- **Reliability note:** The supplied September corpus documents a ransomware publication but provides no public DFIR report, data sample or independent victim confirmation supporting a successful compromise.
- **Analysis:** AFRINTEL records the publication as a ransomware claim. The supplied evidence does not establish encryption, operational disruption, exfiltration scope, initial access or a confirmed victim response. The record therefore remains `Claim - Unverified`.

----------------------------


### September 15, 2024

#### 🇲🇺 Mauritius - Emtel
- **Ransomware Group:** arcusmedia
- **Sector:** Telecommunications
- **Website:** [emtel.com](https://www.emtel.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Emtel is a Mauritian mobile network operator providing telecommunications infrastructure, voice, broadband data and digital services.
- **Reliability note:** The supplied September corpus documents a ransomware publication but provides no public DFIR report, data sample or independent victim confirmation supporting a successful compromise.
- **Analysis:** AFRINTEL records the publication as a ransomware claim. The supplied evidence does not establish encryption, operational disruption, exfiltration scope, initial access or a confirmed victim response. The record therefore remains `Claim - Unverified`.

----------------------------


### September 16, 2024

#### 🇹🇳 Tunisia - Excelplast Tunisie
- **Ransomware Group:** orca
- **Sector:** Manufacturing / Industry
- **Website:** [excelplastunisie.com](https://www.excelplastunisie.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Excelplast Tunisie is a Tunisian industrial manufacturing company specialised in plastic production, raw-material processing and packaging.
- **Reliability note:** The supplied September corpus documents a ransomware publication but provides no public DFIR report, data sample or independent victim confirmation supporting a successful compromise.
- **Analysis:** AFRINTEL records the publication as a ransomware claim. The supplied evidence does not establish encryption, operational disruption, exfiltration scope, initial access or a confirmed victim response. The record therefore remains `Claim - Unverified`.

----------------------------


## October 2024


### October 3, 2024

#### 🇲🇬 Madagascar - University of Antananarivo (univ-antananarivo.mg)
- **Incident type:** Data Leak
- **Actor / Group:** Unknown
- **Source context:** RainbowBF is the forum account shown as publishing the locked database-access claim.
- **Sector:** Education / University
- **Website:** [univ-antananarivo.mg](https://www.univ-antananarivo.mg)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The University of Antananarivo is Madagascar's oldest and largest public university, comprising multiple faculties and higher-education institutes in the capital region.
- **Analysis:** AFRINTEL reviewed a forum listing on the Breached platform, posted by the account RainbowBF on 3 October 2024, titled "Madagascar univ-antananarivo.mg Database Access" and tagged under the platform's "Breached" content category. The underlying content is paywalled behind the forum's internal credit system and was not unlocked by AFRINTEL; no database export, record screenshot or other verifiable sample was accessible during collection. AFRINTEL treats this as an unconfirmed claim of database access and does not confirm the existence, scope or authenticity of any underlying data. The potential affected data categories and impact cannot currently be assessed because the underlying content was not accessible. AFRINTEL does not reproduce any content from the forum listing beyond its title and metadata.

----------------------------


### October 4, 2024

#### 🇿🇦 South Africa - Enterpriseoutsourcing
- **Ransomware Group:** ransomhub
- **Sector:** Technology / IT
- **Website:** [enterpriseoutsourcing.com](https://www.enterpriseoutsourcing.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Enterpriseoutsourcing is a South African organisation operating in the information technologies consulting sector.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.


### October 5, 2024

#### 🇿🇦 South Africa - Winwinza
- **Ransomware Group:** ransomhub
- **Sector:** Education / University
- **Website:** [winwinza.com](https://www.winwinza.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Winwinza is a South African organisation operating in the education sector.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.


### October 7, 2024

#### 🇩🇿 Algeria - Yassir
- **Ransomware Group:** killsec
- **Sector:** Technology / IT
- **Website:** [yassir.com](https://www.yassir.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Yassir is an Algerian super-app providing ride-hailing, delivery, grocery, and digital services in Algeria and across regional markets.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.


### October 9, 2024

#### 🇳🇬 Nigeria - Unidentified healthcare facilities provider
- **Actor / Group:** grep/cn
- **Source context:** The October 9 forum publication was posted by Tanaka and attributes the leak to grep/cn.
- **Sector:** Healthcare / Medical
- **Website:** Not identified
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** The source describes an unidentified Nigerian healthcare facilities provider operating across multiple facilities. The organization name and the affected facilities could not be established from the source material.
- **Analysis:** A forum publication by Tanaka dated 9 October 2024 claims that approximately 130,000 patient records from multiple Nigerian healthcare facilities were leaked by the actor grep/cn. The local workbook supplied for analysis contains 84 data rows, not 129,825 or 130,000 rows, so the advertised volume cannot be independently confirmed from the available file. The workbook contains patient-related fields including names, identifiers, telephone numbers, age, dates of birth, sex, marital status and facility-related identifiers; raw records were not reproduced. The evidence supports a healthcare data-exposure claim with a high potential impact, but the exact provider, facility scope, acquisition method, completeness and total volume remain unknown.


### October 9, 2024

#### 🇿🇦 South Africa - GMG Mining Supplies
- **Ransomware Group:** sarcoma
- **Sector:** Manufacturing / Industry
- **Website:** [gmgminingsupplies.com](https://gmgminingsupplies.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** GMG Mining Machines and Supplies is a South African company specialised in the supply, reconstruction, and rental of mining equipment, rail-less mobile machines, parts, and associated services.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.


### October 9, 2024

#### 🇿🇦 South Africa - National Edging
- **Ransomware Group:** sarcoma
- **Sector:** Manufacturing / Industry
- **Website:** [nationaledging.com](https://nationaledging.com)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** National Edging is a South African company specialised in the supply of edgebanding, adhesives, finishing materials, and industrial components for the furniture, kitchen, and fitment sectors.
- **Analysis:** AFRINTEL reviewed a local sample of documents consistent with the claim made by the threat actor sarcoma, comprising full passport scans of at least three individuals (two South African nationals and one Indian national holding a UAE residence permit), a signed contract with Freitan Group of Companies (Pty) Ltd bearing a financial director's signature, a corporate travel-booking form referencing the legal entity National Converting Agencies (Pty) Ltd, an email address on the nationaledging.co.za domain and a South African passport and identity number, and a delivery note documenting a shipment of edging and glue products between company branches (Gauteng) with onward collection referenced in Zimbabwe. The direct reference to the nationaledging.co.za domain, together with internally consistent corporate identity (National Converting Agencies/National Edging), signed contractual material and multiple full identity documents, supports a very high confidence assessment of a genuine internal compromise. The exposure of full passport and national identity data for multiple individuals, together with signed contracts and logistics records extending into a cross-border (Zimbabwe) supply chain, creates a significant risk of identity fraud, document forgery and targeted social engineering against employees, business partners and travellers associated with the company. AFRINTEL does not reproduce any name, passport number, identity number, date of birth or contact detail from the reviewed sample.

----------------------------

- **Evidence qualification:** The reviewed sample strongly supports an internal data compromise associated with National Edging. It does not independently establish ransomware encryption, the initial access method or the full exfiltration volume.


### October 11, 2024

#### 🇬🇭 Ghana - Volta River Authority (VRA)
- **Ransomware Group:** blacksuit
- **Sector:** Energy / Utilities
- **Website:** [vra.com](https://www.vra.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Volta River Authority (VRA) is Ghana's main public electricity producer, responsible for hydroelectric and thermal power plants and strategic energy infrastructure.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.


### October 16, 2024

#### 🇱🇾 Libya - Ministry of Interior (moi.gov.ly)
- **Ransomware Group:** killsec
- **Sector:** Government / Administration
- **Website:** [moi.gov.ly](https://www.moi.gov.ly)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Libyan Ministry of Interior is the government institution responsible for internal security, police forces, and the management of the country's administrative and security affairs.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.


### October 17, 2024

#### 🇩🇿 Algeria - Ministry of National Education (education.gov.dz)
- **Actor / Group:** Moroccan Empire
- **Source context:** Reposted by AmeliaBeaumont on a cybercriminal forum; the reviewed post references an older dump.
- **Sector:** Education / University
- **Website:** [education.gov.dz](https://www.education.gov.dz)
- **Claimed initial leak date:** October 6, 2022
- **Date of the reviewed post:** October 17, 2024 (the post directly includes a link to the original dump, first shared on September 18, 2023)
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** The Ministry of National Education is the Algerian administration responsible for the public education system. The post claims the theft of a database containing information on approximately 90,000 students, including administrator accounts and login credentials.
- **Analysis:** The account AmeliaBeaumont published, on October 17, 2024, a claim describing an intrusion attributed to the actor "Moroccan Empire" and dated October 6, 2022. As the original download link (a .onion address on a leak forum) was no longer working, the post directly includes a link to the dump, first shared on September 18, 2023, which displays a SQL/CSV sample with a field schema including: birth certificate number, contract type, institution, commune, last name, first name (in French and Arabic), date of birth, place of birth, insurance number, phone number, diploma, specialty, account credentials (`compte`, `cle`), email address, and a plaintext password field. At least two complete records are visible in the sample, containing names, dates of birth, phone numbers, an email address and a plaintext password tied to identified individuals.

  The presence of a schema consistent with a school administrative management system, including identity, schooling and plaintext login data, supports a high confidence level regarding authentic access to a database of the ministry or an affiliated institution. The total claimed volume of 90,000 students could not be independently verified beyond the observed sample. The fact that the same dump remains shared and referenced more than two years after the initially claimed leak indicates prolonged recirculation of this dataset. The exposure of plaintext passwords, combined with identity and schooling data, creates a high risk of account takeover, identity theft and targeted phishing against students, their families and administrative staff. AFRINTEL does not reproduce any name, date of birth, phone number, email address, password or other personal data from the reviewed sample.

----------------------------


### October 21, 2024

#### 🇲🇦 Morocco - Al Massira University Residences
- **Actor / Group:** bxxxx1
- **Sector:** Education / University
- **Website:** [ruam.ma](https://ruam.ma)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak

- **Description:**
  Al Massira University Residences provide student accommodation in Kenitra. The network includes the Al Massira 1, Al Massira 2 and Al Massira 3 residences near the city’s higher education institutions.

- **Analysis:**
  A cybercriminal-forum post attributed to bxxxx1 presents email addresses associated with people who searched for or applied for accommodation through the Al Massira University Residences platform. The actor claims the data was obtained after logging into the `ruam.ma` control panel, suggesting possible compromise of an administrative account or management interface; however, the screenshot provides no technical evidence identifying the access method. The visible sample contains email addresses only, mostly from public mail services with some university, administrative or professional domains. No passwords, identity numbers, telephone numbers, student documents or financial information are visible. The post states that the data was extracted in October 2024 and includes a text-file download link and an archive or access password, neither of which AFRINTEL reproduces. No total record count, file size, price or deadline is stated, and the screenshot does not establish whether the visible list is complete. The addresses could support targeted phishing impersonating student accommodation services, fraudulent admission or payment notifications, and password-spraying target lists. Since no passwords are visible, direct account compromise cannot be inferred from the sample.

----------------------------


### October 25, 2024

#### 🇪🇬 Egypt - Matouk Bassiouny
- **Ransomware Group:** raworld
- **Sector:** Legal / Justice
- **Website:** [matoukbassiouny.com](https://www.matoukbassiouny.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Matouk Bassiouny is a prominent Egyptian law firm based in Cairo, recognised for corporate law, arbitration, litigation, and legal advisory services.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.


## November 2024


### November 2, 2024

#### 🇿🇦 South Africa - Sumitomo Rubber South Africa
- **Ransomware Group:** killsec
- **Sector:** Manufacturing / Industry
- **Website:** [srigroup.co.za](https://www.srigroup.co.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** Sumitomo Rubber South Africa is a tyre manufacturing company operating in South Africa and affiliated with the Sumitomo Rubber Industries group.
- **Analysis:** AFRINTEL reviewed a local sample of the archive associated with this claim, comprising approximately 239,600 individual PDF files (roughly 23 GB uncompressed), each named with a random UUID rather than an original filename. The files reviewed by AFRINTEL are genuine customer statements of account issued under the letterhead of Sumitomo Rubber South Africa (Pty) Ltd, specifically its "Export DQC - Africa East (USD)" division, listing per-account transaction history (SAP invoice references, dates, credit amounts and running balances) tied to a named account number and a named export sales contact and email address on the srigroup.co.za domain. The consistent company letterhead, real contact names and SAP-linked invoice numbering across the reviewed sample, together with the very large volume and UUID-based naming pattern consistent with a bulk export from a document-management or ERP archive, support a very high confidence assessment of a genuine, large-scale compromise. Given the scale of the archive and its coverage of the company's Africa-wide export accounts-receivable records, this incident presents a risk of large-scale invoice fraud, business email compromise and competitive intelligence exposure extending to Sumitomo Rubber South Africa's export client base across the continent. AFRINTEL does not reproduce any account number, contact name, email address, invoice reference or financial figure from the reviewed material.

----------------------------

- **Evidence qualification:** The reviewed archive strongly supports a genuine large-scale internal-data compromise associated with Sumitomo Rubber South Africa. It does not independently establish the initial-access vector, ransomware encryption behavior or the full scope of any separate exfiltration beyond the reviewed archive.


### November 4, 2024

#### 🇹🇿 Tanzania - College of Business Education (CBE)
- **Ransomware Group:** hellcat
- **Sector:** Education / University
- **Website:** [cbe.ac.tz](https://www.cbe.ac.tz)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The College of Business Education (CBE) is a Tanzanian higher education institution offering programmes in business, management, accounting, and related professional fields.

----------------------------


### November 4, 2024

#### 🇸🇩 Sudan - Kenana Sugar Company
- **Ransomware Group:** ransomhub
- **Sector:** Agriculture / Agribusiness
- **Website:** [kenanasugarcompany.com](https://www.kenanasugarcompany.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Kenana Sugar Company is a major Sudanese agro-industrial complex specialised in sugarcane cultivation, sugar production, and associated agricultural and industrial activities.

----------------------------


### November 12, 2024

#### 🇲🇦 Morocco - Arab Civil Aviation Organization (ACAO)
- **Actor / Group:** Unknown
- **Source context:** Reposted by Hxp7; the November post references an earlier claim.
- **Sector:** Aviation
- **Website:** [acao.org.ma](https://acao.org.ma)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** The Arab Civil Aviation Organization (ACAO) is an intergovernmental body headquartered in Rabat, Morocco, that coordinates civil aviation policy, safety and regulatory cooperation among Arab states.
- **Analysis:** A forum post dated November 12, 2024 reposts an earlier claim that the ACAO database (acao.org.ma) was compromised, referencing approximately 800 files described as database columns and an external download link. No data extract or sample was directly visible in the observed post, so the content, authenticity and scope of the alleged database cannot be assessed. AFRINTEL does not access or reproduce the linked file. This entry is recorded as an unverified claim pending independent confirmation.

----------------------------


### November 14, 2024

#### 🇳🇬 Nigeria - Environmental Design International
- **Ransomware Group:** akira
- **Sector:** Professional / Business Services
- **Website:** [environmentaldesigninternational.com](http://environmentaldesigninternational.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Environmental Design International is a Nigerian engineering and consulting firm; the claim referenced engineering, financial, and personal documents.

----------------------------


### November 17, 2024

#### 🇪🇬 Egypt - Egyptian Tax Authority (ETA)
- **Ransomware Group:** moneymessage
- **Sector:** Government / Administration
- **Website:** [eta.gov.eg](https://www.eta.gov.eg)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Egyptian Tax Authority (ETA) is the Egyptian public tax administration responsible for tax collection, compliance, taxpayer services, and fiscal management.

----------------------------


### November 20-21, 2024 - official sources differ by one day

#### 🇿🇦 South Africa - South African Bureau of Standards (SABS)
- **Incident date:** 20-21 November 2024 - official sources differ by one day
- **Initial publication date:** Retrospective official disclosure; exact first public date not established in reviewed sources
- **AFRINTEL correction date:** 23 August 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [sabs.co.za](https://www.sabs.co.za/)
- **Status:** Government Confirmed
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Date discrepancy note:** An official SABS presentation dates the incident to 20 November 2024, while a later ministerial parliamentary letter states 21 November 2024. AFRINTEL preserves the range instead of silently selecting one date.
- **Victim Description:** SABS is South Africa's national standards body, supporting standards development, testing, certification and related services.
- **Analysis:** Official South African government and parliamentary material confirms that SABS suffered a ransomware attack in November 2024 that encrypted information systems and caused major operational disruption. The encrypted environment prevented access to data required for audit work, delayed financial reporting and required extensive rebuilding of virtual machines and applications. Later audit reporting described a complete shutdown of business applications and prolonged recovery. The attacker was not identified in the official sources reviewed. No monetary loss, affected-record count or confirmed exfiltrated-data volume is established in the reviewed material.
- **Evidence qualification:** Encryption and operational disruption are government-confirmed. The attacker identity, initial-access vector and any data-exfiltration scope remain unestablished.
- **Public sources:** [the dtic / SABS presentation](https://www.thedtic.gov.za/wp-content/uploads/Revised-SABS-Allegations-against-the-SABS.pdf) | [Parliamentary letter](https://www.parliament.gov.za/storage/app/media/Docs/atc/01ls62wgbe2fcfr3dgmfh2s7hbu5b7hej4.pdf)

----------------------------


### November 24, 2024

#### 🇰🇪 Kenya - EFI Sales
- **Ransomware Group:** killsec
- **Sector:** Manufacturing / Industry
- **Website:** [efisales.co.ke](https://www.efisales.co.ke)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** EFI Sales is a Kenyan company in the distribution sector, associated with the supply of industrial equipment and related services.

----------------------------


### November 27, 2024

#### 🇪🇹 Ethiopia - Habesha Cement
- **Ransomware Group:** lockbit3
- **Sector:** Manufacturing / Industry
- **Website:** [habeshacement.com](https://www.habeshacement.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Habesha Cement is an Ethiopian cement company founded in 2008, specialised in cement production and construction materials for infrastructure and real estate sectors.

----------------------------


### November 27, 2024

#### 🇪🇬 Egypt - Contrack Facilities Management
- **Ransomware Group:** raworld
- **Sector:** Professional / Business Services
- **Website:** [contrackfm.com](https://www.contrackfm.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Contrack Facilities Management is an Egyptian facility management company providing maintenance, operations, and support services for corporate buildings and sites.

----------------------------


### November 28, 2024

#### 🇧🇫 Burkina Faso - Burkina Faso Public Health System Portal
- **Actor / Group:** Sentap
- **Sector:** Healthcare / Medical
- **Website:** Not specified
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Access Sale
- **Description:** A forum publication describes a government-run public-health portal in Burkina Faso that may manage health personnel information, health-service reporting, vaccination campaigns, resource planning and internal communications.
- **Analysis:** The publication presents potential portal functions and categories of data, including health personnel and patient-related information, but does not provide a verifiable domain, technical access evidence or a data sample. AFRINTEL records this as an unverified access-sale claim attributed to Sentap. A possible relationship with the COVID-19 data-management system published by the same source later in November remains unconfirmed.

----------------------------


### November 28, 2024

#### 🇧🇫 Burkina Faso - Government COVID-19 Data Management System
- **Actor / Group:** Sentap
- **Sector:** Healthcare / Medical
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Access Sale
- **Description:** A forum publication presents a Burkina Faso government COVID-19 data-management dashboard covering PCR and TDR results, vaccination records and historical reporting.
- **Analysis:** The screenshots show dashboard metrics, vaccination summaries and a historical-results interface, including a claimed total of approximately 3.795 million records. The publication also advertises access for sale, but the domain, provenance, completeness and authenticity of the records are not independently verified. AFRINTEL does not reproduce personal records or contact details. This claim is kept separate from the public-health portal entry because a technical link between the systems is not demonstrated.

----------------------------


### November 28, 2024

#### 🇳🇬 Nigeria - Briatek
- **Ransomware Group:** killsec
- **Sector:** Technology / IT
- **Website:** [briatek.com.ng](https://www.briatek.com.ng)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Briatek is a Nigerian technology company specialised in IT consulting, software integration, and digital solutions for organisations.

----------------------------


### November 28, 2024

#### 🇨🇲 Cameroon - Chanas Assurances S.A.
- **Ransomware Group:** fog
- **Sector:** Finance / Banking
- **Website:** [chanasassurances.com](https://www.chanasassurances.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Chanas Assurances S.A. is a Cameroonian insurance company operating in the insurance services sector.

----------------------------


### November 29, 2024

#### 🇳🇦 Namibia - Namforce Life Insurance
- **Ransomware Group:** spacebears
- **Sector:** Finance / Banking
- **Website:** [namforce.com.na](https://www.namforce.com.na)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Namforce Life Insurance is a Namibian company specialised in life insurance products, financial protection, and risk management solutions for individuals and organisations.

----------------------------


### November 29, 2024

#### 🇿🇦 South Africa - PPOTTS
- **Ransomware Group:** ransomhub
- **Sector:** Technology / IT
- **Website:** [ppotts.com](https://www.ppotts.com)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Analysis:** AFRINTEL reviewed eight screenshots from the RansomHub evidence set. The visible material includes an Uganda National Examinations Board certificate, South African pathology laboratory results and personal-credential disclosure forms containing candidate and company information. The material is sensitive, but the screenshots do not establish whether these records originated from PPOTTS directly, a customer environment, a third-party system or a wider dataset obtained through the claimed intrusion. The evidence supports recording a published sample while keeping the attribution and data provenance under review. AFRINTEL does not reproduce names, identity numbers, medical results or contact details.
- **Victim Description:** PPOTTS is a South African technology company operating in software, digital services, or enterprise technology solutions.

----------------------------


## December 2024


### December 3, 2024

#### 🇸🇩 Sudan - DAL Group
- **Ransomware Group:** ransomhub
- **Sector:** Agriculture / Agribusiness
- **Website:** [dalgroup.com](https://www.dalgroup.com)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Incident type:** Data Leak
- **Analysis:** AFRINTEL reviewed 12 screenshots from the RansomHub evidence set. The material includes financial covenants, bank-account and transaction material, passport-related documents, customer-account records and internal DAL Group documents. The visible evidence suggests exposure across financial operations, identity documentation and business administration rather than a single isolated file. Potential impacts include financial fraud, identity theft, targeted phishing, supplier or customer impersonation, and commercial espionage against a large Sudanese conglomerate. The screenshots do not independently confirm the initial access vector, the completeness of the dataset, the exact number of affected individuals or operational disruption. AFRINTEL does not reproduce personal records, passport details, account numbers or download links.
- **Victim Description:** DAL Group is Sudan's largest private conglomerate, operating across agribusiness, industry, agriculture, distribution, and beverages sectors.

----------------------------


### December 2024 - exact incident date not publicly established

#### 🇰🇪 Kenya - Micro and Small Enterprises Authority (MSEA)
- **Incident date:** December 2024 - exact date not publicly established
- **Initial publication date:** 3 December 2024
- **AFRINTEL correction date:** 23 August 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [msea.go.ke](https://msea.go.ke/)
- **Status:** Corroborated - No Direct Victim Confirmation Located
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** MSEA is a Kenyan public authority responsible for supporting and regulating the micro and small enterprise sector.
- **Analysis:** Public reporting in early December 2024 stated that MSEA had been hacked and that government and organisational information was offered for sale on underground forums. Reported exposed material included employee records, government correspondence, financial statements and business-registration information. The incident was later referenced by INTERPOL's Africa Cyberthreat Assessment and by ENACT, which materially strengthens the assessment that a breach occurred. However, no direct MSEA victim notification was located in the source set used for the retrospective audit. AFRINTEL therefore records the case as a `Data Leak` with `High` confidence and a corroborated status, not as `Victim Confirmed`. The claimed USD 100,000 sale price and technical root-cause statements remain secondary reporting and are not treated as established facts.
- **Evidence qualification:** The breach is strongly corroborated, but direct victim confirmation was not located in the reviewed source set. Reported data categories are retained as reported exposure, not as independently validated file-by-file findings.
- **Public sources:** Techpoint Africa; INTERPOL Africa Cyberthreat Assessment; ENACT references documented in the retrospective correction dataset.

----------------------------


### December 9, 2024

#### 🇲🇷 Mauritania - Bankily
- **Ransomware Group:** apt73/bashe
- **Sector:** Finance / Banking
- **Website:** [bankily.mr](https://www.bankily.mr)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Bankily is a Mauritanian mobile banking platform operated by Banque Populaire de Mauritanie (BPM), providing digital financial services and mobile payment solutions.

----------------------------


### December 10, 2024

#### 🇳🇦 Namibia - Telecom Namibia
- **Ransomware Group:** hunters
- **Sector:** Telecommunications
- **Website:** [telecom.na](https://www.telecom.na)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Telecom Namibia is the national incumbent telecommunications operator providing voice, broadband, data connectivity, and infrastructure services in Namibia.

----------------------------


### December 13, 2024

#### 🇪🇬 Egypt - Kazyon
- **Ransomware Group:** moneymessage
- **Sector:** Retail / E-commerce
- **Website:** [kazyon.com](https://www.kazyon.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Kazyon is a major Egyptian hard-discount supermarket chain offering food, household, and consumer products through a wide store network.

----------------------------


### December 15, 2024

#### 🇿🇲 Zambia - Tumeny Payments Limited
- **Ransomware Group:** killsec
- **Sector:** Finance / Banking
- **Website:** [tumenypay.com](https://www.tumenypay.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Tumeny Payments Limited is a Zambian fintech company providing digital payment services, money transfer, and payment infrastructure solutions.

----------------------------


### December 16, 2024

#### 🇳🇬 Nigeria - Ekiti State Government
- **Ransomware Group:** funksec
- **Sector:** Government / Administration
- **Website:** [ekitistate.gov.ng](https://ekitistate.gov.ng)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** The Ekiti State Government is the executive administration of Ekiti State, in southwestern Nigeria. Its official portal hosts ministries, agencies and public-service information, including recruitment-related content, for state residents and civil servants.
- **Analysis:** AFRINTEL reviewed a local archive consistent with the claim made by the threat actor funksec, comprising a leak notice referencing ekitistate.gov.ng and describing a database exceeding 300MB, alongside a website document library of more than 17,000 individual image files (roughly 530MB) collected from the portal's file repository. The reviewed sample includes personal identification documents (passport-style scans), curriculum vitae bearing personal data fields such as date of birth, address, phone number, email and religion, and a Police Service Commission candidate-screening table listing shortlisted applicants by name, local government area, village and gender for a 2019 recruitment exercise. The volume and structure of the reviewed material, file-naming patterns consistently tied to named individuals, and the presence of an official state-government document template support a very high confidence assessment of a genuine data exposure rather than a superficial claim. Given Ekiti State's role as a subnational public administration and the presence of citizen and civil-servant identity documents, this incident presents a significant risk of identity theft, targeted phishing and impersonation. AFRINTEL does not reproduce any name, passport number, contact detail or other personal identifier from the reviewed material.

----------------------------

- **Evidence qualification:** The reviewed archive strongly supports genuine data exposure associated with the Ekiti State Government. It does not independently establish ransomware encryption, the initial-access vector or operational disruption.


### December 18, 2024

#### 🇳🇬 Nigeria - National Bureau of Statistics (NBS)
- **Incident date:** 18 December 2024
- **Initial publication date:** 18 December 2024
- **AFRINTEL correction date:** 23 August 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [nigerianstat.gov.ng](https://www.nigerianstat.gov.ng/)
- **Status:** Victim Confirmed
- **Incident type:** Defacement
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** Nigeria's National Bureau of Statistics is the national statistical authority and operates a major public repository for economic, demographic and social statistics.
- **Analysis:** On 18 December 2024 NBS confirmed through its official social-media account that its website had been hacked and advised the public to disregard information posted there until recovery. Independent reporting documented a `Page hacked` message. The website remained unavailable for several weeks before restoration in January 2025, materially disrupting public access to national statistical information. No public evidence in the reviewed sources establishes theft of backend datasets, a named attacker or a confirmed data-exfiltration event. AFRINTEL therefore classifies the record as `Defacement`, with service disruption documented as an operational consequence rather than as a separate incident type.
- **Evidence qualification:** Website compromise and defacement are victim-confirmed; service disruption is documented. Backend dataset theft and attacker attribution remain unconfirmed.
- **Public sources:** TheCable and BusinessDay reports documented in the retrospective correction dataset.

----------------------------


### December 20, 2024

#### 🇧🇼 Botswana - Water Utilities Corporation (WUC)
- **Ransomware Group:** killsec
- **Sector:** Water / Utilities
- **Website:** [wuc.bw](https://www.wuc.bw)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Water Utilities Corporation (WUC) is the Botswana public utility responsible for water supply, distribution, and water services management across the country.

----------------------------


### December 21, 2024

#### 🇹🇳 Tunisia - Groupe SETCAR
- **Ransomware Group:** ransomhub
- **Sector:** Manufacturing / Industry
- **Website:** [groupe-setcar.com.tn](https://www.groupe-setcar.com.tn)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Groupe SETCAR is a Tunisian industrial group specialised in buses, coaches, industrial vehicles, automotive activities, and transport solutions.

----------------------------


### December 24, 2024

#### 🇿🇦 South Africa - Baker Tilly Morrison Murray
- **Ransomware Group:** sarcoma
- **Sector:** Professional / Business Services
- **Website:** [bakertillymm.co.za](https://www.bakertillymm.co.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Baker Tilly Morrison Murray is a South African professional services firm providing accounting, audit, tax, and advisory services.
- **Analysis:** AFRINTEL reviewed screenshots stored under the `bakertillymm.co.za` evidence directory and observed South African identity-document material, including a passport, alongside contract and employment-related documents. The sample is consistent with the type of sensitive client, employee or third-party records that may be handled by an accounting and advisory firm, but it does not establish the total scope of the alleged disclosure or the complete set of affected persons. The combination of identity documents and contractual records creates a risk of identity fraud, targeted social engineering, employee impersonation and secondary fraud against clients or business partners. The material supports a medium-confidence assessment that a data sample was published in connection with the Sarcoma claim; AFRINTEL does not reproduce names, document numbers, dates of birth, addresses or other personal data from the screenshots.

----------------------------


### December 24, 2024

#### 🇩🇿 Algeria - ASJP (Algerian Scientific Journal Platform)
- **Ransomware Group:** funksec
- **Sector:** Education / University
- **Website:** [asjp.cerist.dz](https://asjp.cerist.dz)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** ASJP (Algerian Scientific Journal Platform) is a national electronic publishing platform developed and operated by CERIST (Centre de Recherche sur l'Information Scientifique et Technique), an Algerian state research institution. It indexes and hosts full text for more than 700 Algerian scientific journals across all academic disciplines.
- **Analysis:** AFRINTEL reviewed a local archive consistent with the claim made by the threat actor funksec, comprising a server-side filesystem backup (tar archive, file ownership attributed to the www-data web-server account) of the platform's user-avatar directory tree, containing more than 1,700 individual user folders with account-linked profile images dated between 2017 and 2024, and a separate structured list of 499 name and email records. The user folders are predominantly tied to Algerian university email domains (including univ-biskra.dz, univ-tlemcen.dz, univ-batna.dz, univ-tiaret.dz, univ-guelma.dz, univ-alger2.dz, univ-alger3.dz, univ-constantine2.dz, univ-constantine3.dz, univ-msila.dz, univ-mosta.dz, lagh-univ.dz and edu.univ-oran1.dz, among others), consistent with ASJP's role as Algeria's national platform for academic journal publishing, alongside a smaller share of international academic contributors from other countries submitting to Algerian-hosted journals. The presence of a genuine server-side backup with web-server file ownership and multi-year, internally consistent timestamps, corroborated by a separate name/email export, supports a very high confidence assessment of a genuine compromise at the file-system level rather than a superficial claim. Given ASJP's role as a state-operated (CERIST) national research-publishing infrastructure, the scale of the exposed user base and the file-system-level nature of the access, this incident presents a systemic risk to Algeria's academic publishing ecosystem, including large-scale phishing, account takeover and impersonation of researchers and journal staff. AFRINTEL does not reproduce any name, email address or user-account identifier from the reviewed material.

----------------------------

- **Evidence qualification:** The reviewed server-side material strongly supports file-system-level compromise associated with ASJP. It does not independently establish ransomware encryption, service interruption or the original access mechanism.


### December 28, 2024

#### 🇿🇦 South Africa - Cell C
- **Ransomware Group:** ransomhouse
- **Sector:** Telecommunications
- **Website:** [cellc.co.za](https://www.cellc.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Cell C is the fourth-largest mobile network operator in South Africa, serving over 13 million customers (direct and MVNO). The company operates on an asset-light business model, leveraging roaming infrastructure from MTN and Vodacom, and is majority-owned by Blue Label Telecoms.

----------------------------


### December 29, 2024

#### 🇹🇿 Tanzania - WOSAC
- **Ransomware Group:** arcusmedia
- **Sector:** Transport / Logistics
- **Website:** [wosac.co.tz](https://www.wosac.co.tz)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** WOSAC is a Tanzanian maritime transport and shipping agency company providing freight, shipping, and associated logistics services.

----------------------------


## Author
*Adama ASSIONGBON*  
*SOC & Cyber Threat Intelligence Consultant*
