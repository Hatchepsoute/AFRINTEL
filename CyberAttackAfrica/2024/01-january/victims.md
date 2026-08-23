[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%7C%20Data%20Leak%20%7C%20Access%20Sale-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in January 2024 (14 victims)
👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

January 2024 contains **14 documented incident records**: **5 Ransomware**, **8 Data Leak**, **1 Access Sale**, **0 DDoS**, **0 Defacement** and **0 Operational Fraud**, across **10 African countries**.

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

## ✍🏿 Author
*Adama ASSIONGBON*
*SOC & Cyber Threat Intelligence Consultant*
[LinkedIn profile](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)
