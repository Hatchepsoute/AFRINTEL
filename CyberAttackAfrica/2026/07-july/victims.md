# List of African cyberattack victims in July 2026 (42 victims)
👉🏾 [French version](./victims_FR.md)

## July 2026

### July 01, 2026
#### 🇳🇬 Nigeria / 🇨🇮 Côte d’Ivoire - Citizen ID Photo Dataset

- **Initial publication date:** 02 February 2026
- **AFRINTEL detection date:** 01 July 2026
- **Actor / Group:** azrekx
- **Sector:** Government / Public administration / Identity documents
- **Website:** Not specified
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  A forum post claims access to 10,669 current Nigerian and Ivorian citizen ID photos, including front-and-back images, with 1,500 images allegedly shared and an additional dataset offered for sale.

- **Analysis:**

  The publication is recorded as one multi-country data-leak claim affecting Nigeria and Côte d’Ivoire. The supplied evidence shows the actor’s statement but does not independently verify the dataset, the claimed volumes, the countries represented in the full collection, or the alleged sharing of 1,500 images. AFRINTEL does not collect or reproduce identity photos or personal data from the listing.


### July 01, 2026
#### 🇪🇬 Egypt - Ministry of Agriculture and Land Reclamation

- **Initial publication date:** 11 June 2026
- **AFRINTEL detection date:** 01 July 2026
- **Actor / Group:** V0idix, post published on a cybercriminal forum
- **Sector:** Government / Public administration / Agriculture
- **Website:** [moa.gov.eg](https://moa.gov.eg)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3

- **Reliability note:**

V0idix advertised the publication of more than 700 MB of data attributed to the Egyptian Ministry of Agriculture and Land Reclamation. The reviewed files establish that the provided corpus contains a coherent collection of internal administrative documents mainly associated with the General Authority for Rehabilitation Projects and Agricultural Development. This finding does not independently establish the acquisition method, the completeness of the advertised archive or official victim confirmation.

- **Description:**

V0idix released PDF, XLS, XLSX, ODS, ODT and image files presented as originating from the ministry and several related administrative entities. The material covers land management, agricultural associations, financial recovery, development projects, archiving, information systems and the processing of state-owned land requests.

- **CTI analysis:**

The observed documents include official correspondence, land contracts, administrative decisions, payment notices, regularisation records, inspection reports, agricultural association accounts and payment histories. Several files contain institutional letterheads, internal references, official stamps, signatures and handwritten annotations, increasing confidence in their administrative origin.

The archives also expose information relating to beneficiaries, agricultural association representatives and government officials, together with plot references, land areas, outstanding amounts, payment schedules, disputes, termination or regularisation decisions and debt-recovery proceedings. Some records cover unauthorised occupation, eviction requests and exchanges between multiple government bodies.

Precise geospatial data was also disclosed. Two documents provide the boundaries and geographic coordinates of plots covering **953 feddans** and **3,836 feddans**, enabling the affected land to be located and its perimeter reconstructed.

The technical material includes a named organisational chart covering network, technical support, GIS, statistics, archiving and documentation teams. An equipment inventory lists **389 computers, 87 scanners and 214 printers**, representing **690 devices**, together with their models and departmental distribution.
The data visible in a government application interface used to process state-owned land recovery requests shows **30,456 requests** and fields relating to the applicant, national identity number, public authority, location, land area and case status.

A software manual found in the corpus contains initial accounts associated with several privilege levels. Their current use by the ministry has not been demonstrated, but they may create additional exposure if default credentials or configurations were retained.

The material may support targeted phishing against government employees and agricultural associations, identity fraud, land-related fraud, document forgery and manipulation of administrative procedures. Organisational charts, technical inventories and visible application details also provide useful intelligence for reconnaissance and targeted attacks against internal systems.

- **Recommendations:**

1. Identify affected systems and accounts, reset sensitive access, remove default credentials and review authentication, administrative and land-record access logs.

2. Identify exposed individuals and records, monitor phishing and document-fraud attempts, and investigate unusual changes to land, financial or administrative case files.
---

### July 01, 2026
#### 🇪🇬 Egypt - Heliopolis University

- **Initial publication date:** 02 February 2026
- **AFRINTEL detection date:** 01 July 2026
- **Actor / Group:** CrowStealer, post published on a cybercriminal forum
- **Sector:** Education / Higher Education
- **Website:** Not specified
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3

- **Description:**

  Heliopolis University is a private Egyptian university established near Cairo, with programmes in engineering, pharmacy, business and economics, physical therapy and organic agriculture.

- **Analysis:**

  A forum publication by CrowStealer dated 02 February 2026 advertises a database associated with Heliopolis University containing 19,790 records. The local workbook supplied for analysis contains 62 structured account records, including 38 Parent accounts and 24 Student accounts; the complete advertised volume was not independently verified from the available file.

  The reviewed schema includes usernames, names, email addresses where present, telephone fields, institution type, last-IP fields, account creation timestamps and suspension status. All 62 records contain a stored password value classified in the workbook as either a 32-character hexadecimal hash or bcrypt (`$2y$`); AFRINTEL did not attempt to crack, reproduce or publish any password value. Only 24 email addresses and 8 last-IP values are populated in the reviewed file.

  The combination of student/parent account data, contact details and password hashes could facilitate phishing, credential stuffing and account takeover if passwords were reused elsewhere. The exact acquisition method, completeness of the 19,790-record claim and independent confirmation by the university remain unknown.

### July 01, 2026
#### 🇪🇬 Egypt - HIMS University

- **Initial publication date:** 02 February 2026
- **AFRINTEL detection date:** 01 July 2026
- **Actor / Group:** leakdealer, post published on a cybercriminal forum
- **Sector:** Education / Higher Education
- **Website:** [hims.edu.eg](https://hims.edu.eg)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4

- **Description:**

  HIMS University is presented in the source as an Egyptian higher-education institution. The domain `hims.edu.eg` is observed in the supplied sample, but the institution's official identity and the completeness of the advertised archive were not independently verified.

- **Analysis:**

  A forum post dated 02 February 2026 advertises a database allegedly associated with HIMS University, with a claimed total of 28,124 records and student/staff personal data, financial records and payment-gateway information. The publication lists CSV files covering student accounts, payment records, privilege mappings, balances, bank-related transaction logs, staff details and system metadata. The actor also claims exposure of plaintext credentials and payment-gateway API material; these claims were not independently verified from the visible material supplied.

  The file counts displayed in the source add up to 28,004 records, which is 120 fewer than the advertised total of 28,124. This discrepancy, together with the absence of a reviewed archive, prevents confirmation of the complete volume and scope. If genuine, the combination of student and staff PII, account credentials, financial information and payment-system material could create significant risks of phishing, account takeover, payment fraud and further unauthorized access. AFRINTEL does not reproduce any personal data, credential, API key, national identifier or financial record from the sample.



### July 01, 2026
#### 🇩🇿 Algeria - Unidentified government entity (Fortinet access)

- **Initial publication date:** 08 April 2026
- **AFRINTEL detection date:** 01 July 2026
- **Actor / Group:** AckLine, post published on a cybercriminal forum
- **Sector:** Government / Public administration
- **Website:** Not identified with sufficient confidence
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Access Sale
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

The post advertises the sale of alleged Fortinet-related access to an unidentified Algerian government entity, with contact details provided via qTox. No specific organization, domain, price or technical evidence is disclosed.

- **Analysis:**

The actor AckLine published a short listing offering access described only as "Fortinet" and associated with "Algeria gov", without naming a specific ministry, agency or domain. The listing gives no price figure ("$$$ offer price"), no data sample, and no technical proof of access such as a screenshot of a management console, VPN portal or configuration. Negotiation is directed to an external qTox contact, which is consistent with typical access-broker listings but does not itself confirm that the offered access is genuine.

Given the absence of a named victim, verifiable evidence or pricing detail, this claim is assessed with low confidence. If genuine, unauthorized access to a Fortinet appliance (firewall/VPN) belonging to an Algerian government entity could enable network intrusion, lateral movement and further compromise of connected systems.

- **Recommendations:**

1. Algerian government entities should audit exposed Fortinet devices, apply available security patches, and review VPN/firewall access logs for anomalous activity.
2. Monitor cybercriminal forums and access-broker listings referencing Algerian government infrastructure for follow-up claims that could confirm or clarify the target.
---


### July 01, 2026
#### 🇬🇭 Ghana - Nerasolgh (nerasolgh.com)

- **Initial publication date:** 07 January 2026
- **AFRINTEL detection date:** 01 July 2026
- **Actor / Group:** Solonik, post published on a cybercriminal forum
- **Sector:** Public Utility / Waste Management Services (Government-adjacent)
- **Website:** [nerasolgh.com](https://nerasolgh.com)
- **AFRINTEL status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4

- **Description:**

  Nerasolgh (nerasolgh.com) operates an integrated waste management billing system used to manage customer accounts, collection routes and payments for sanitation/waste-collection services in Ghana, including USSD-based mobile-money bill payment.

- **Analysis:**

  AFRINTEL reviewed a post published on 7 January 2026 by the actor Solonik, titled "NERASOLGH.COM — 26M FULL PII + BANK DATA + GEO + HASHES (SQL DUMP)", and independently obtained and reviewed the underlying database files referenced in the post. The actor claims 26,082,134 total records in SQL format, covering full name, phone number, email address, physical address, GPS coordinates, gender, password hashes and bank details, with a full archive offered for download.

  AFRINTEL's review of three referenced database exports confirms the schema and country markers described by the actor: a 293,232-row customer table (`iwms_new.customers`) containing full name, primary and secondary phone numbers, postal/street address, Ghana Post GPS digital address, GPS coordinates, gender, a bank-details field and bcrypt password hashes; a 2,604-row staff/agent user table (`iwms_new.users`) containing name, email, phone number, role (administrator, waste-collection agent, subscriber), bcrypt password hash, API access token and session token; and a 1,357,156-row USSD mobile-money transaction log recording customer ID, customer name, payment amount, MSISDN, mobile network operator, transaction status and timestamps, consistently tied to Ghanaian (+233) phone numbers. The combined roughly 1.65 million rows reviewed are structurally consistent with the actor's claim but substantially smaller than the 26 million records advertised, indicating the full advertised dump likely includes additional tables not present in the material reviewed.

  The exposure of customer bank details and password hashes alongside administrator API and session tokens creates a risk of account takeover, fraudulent redirection of bill payments, credential-stuffing against reused passwords, and further compromise of the platform's administrative backend if the tokens remain valid. The exact structural and geographic match between the reviewed files and the actor's claim, combined with the scale and sensitivity of the reviewed material, supports a very high confidence assessment of the sample's attribution. It does not validate the advertised 26-million-record volume, the acquisition method or official victim confirmation. AFRINTEL does not reproduce any customer name, phone number, address, password hash, bank detail, transaction record or credential from the reviewed material.


### July 01, 2026
#### 🇨🇮 Ivory Coast - Hôpital Catholique Saint Joseph Moscati

- **Initial publication date:** 01 July 2026
- **AFRINTEL detection date:** 01 July 2026
- **Ransomware group:** krybit
- **Sector:** Healthcare, hospital
- **Website:** [moscati.org](https://moscati.org/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  Saint Joseph Moscati Catholic Hospital is a charitable non-profit healthcare facility located in Yamoussoukro, Côte d'Ivoire. It provides healthcare services and operates with a mission focused on patient care.

- **Analysis:**

  The July 2026 ransomware dataset lists Hôpital Catholique Saint Joseph Moscati as a victim attributed to krybit. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect patient and administrative health-related information and may support phishing, identity fraud and targeted extortion against a non-profit healthcare provider.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-01
listing_last_observed_at: 2026-07-01
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-01
-->

### July 01, 2026
#### 🇪🇬 Egypt - Egyptian Medical Laboratories (multi-organisation claim)

- **Initial publication date:** February 1, 2026
- **AFRINTEL detection date:** July 1, 2026
- **Actor / Group:** CrowStealer
- **Sector:** Healthcare / Medical Laboratories
- **Website:** results.u-carelabs.com; marzouk-labs.com; hassablabsresults.com; mabaralabs-results.com
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:**

  The publication advertises patient-result data allegedly associated with four Egyptian medical-laboratory platforms.

- **Analysis:**

  The post claims 5,529 records in a CSV file named `egy_labs.csv`, covering December 2025 to January 2026. The displayed schema includes laboratory name, patient name, mobile number, accession number, visit date, test type and result-drive reference. The sample shows structured medical-laboratory records, but the authenticity, completeness, exact ownership and independent relationship between the four domains are not confirmed. AFRINTEL records this as one multi-organisation data-leak claim and does not reproduce patient names, contact details or individual file links.



### July 02, 2026
#### 🇹🇳 Tunisia - Adex.tn

- **Initial publication date:** 20 June 2026
- **AFRINTEL detection date:** 02 July 2026
- **Actor / Group:** BIGBROTHER, repost on a cybercriminal forum
- **Sector:** Transportation / Logistics / Courier and Parcel Delivery
- **Website:** [adex.tn](https://adex.tn)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Access Sale
- **Confidence level:** High
- **Impact level:** Level 2

- **Description:**

  Adex.tn is a Tunisian shipping and parcel-delivery company operating through a network of local agencies across the country, providing order and package tracking services for its clients.

- **Analysis:**

  AFRINTEL reviewed a forum post published on 20 June 2026 by the actor BIGBROTHER, titled "{REPOST} [Tunisia] Data Leak from Adex.tn" and tagged as a sale listing, describing "15k personal Data from shipping and transporting company of Tunisia 'Adex.tn'" and linking to an externally hosted proof image, with a Session messenger identifier provided for direct contact. The post is explicitly marked as a repost, indicating the material originates from an earlier, unidentified source rather than an intrusion claimed first-hand by BIGBROTHER.

  Analysis of the data visible in the provided material identified an Adex order-management interface listing individual shipment records across multiple Tunisian agencies, including Sfax, Siliana, Ben Arous, Tunis, Nabeul and Sousse. The interface displays a pagination count of 15,301 records, consistent with the advertised "15k" figure. No exported data file, database dump or downloadable archive was available; analysis was limited to the visible administrative interface rather than an extracted source dataset.

  The match between the claimed record count and the visible total supports a high-confidence assessment that the published material plausibly depicts administrative access. It does not independently establish the original intruder, whether the access remained active or the scope of fields available beyond client names and shipment metadata. If genuine, access to a logistics back office of this kind could expose customer contact details, delivery addresses and shipment patterns and support fraud, parcel interception or social engineering. AFRINTEL does not reproduce any client name, order reference or account detail from the reviewed material.


### July 02, 2026
#### 🇹🇳 Tunisia - Ministry of Vocational Training and Employment (mfpe.gov.tn)

- **Initial publication date:** 20 June 2026
- **AFRINTEL detection date:** 02 July 2026
- **Actor / Group:** BIGBROTHER, repost on a cybercriminal forum
- **Sector:** Government / Public Administration / Vocational Training and Employment
- **Website:** [mfpe.gov.tn](https://mfpe.gov.tn)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Access Sale
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:**

  The Ministry of Vocational Training and Employment (Ministère de la Formation Professionnelle et de l'Emploi, mfpe.gov.tn) is the Tunisian government body responsible for vocational training policy and employment services, including the processing of citizen applications and requests related to training programs and job placement.

- **Analysis:**

  AFRINTEL reviewed a forum post published on 20 June 2026 by the actor BIGBROTHER, one minute before the same actor's repost concerning Adex.tn and using an identical Session contact identifier, titled "{REPOST} [Tunisia] Data Leak from mfpe.gov.tn" and tagged as a sale listing, describing "4,000 personal Data from Ministry of Vocational Training and Employment of Tunisia 'mfpe.gov.tn'" and linking to an externally hosted proof image. As with the related Adex.tn post, this listing is explicitly marked as a repost of material from an earlier, unidentified source.

  Analysis of the visible data identified an Arabic-language ministry request-management interface listing individual citizen requests with full name, national ID/passport number, date of birth, governorate, phone number, request number, submission date, processing status and field of specialty. No total record count is visible, so the advertised "4,000" figure could not be independently corroborated from the provided material.

  The structure and content are consistent with a plausible government case-management interface, but the visible material does not independently establish the access method, its current validity or the original intruder. The combination of national identity numbers, dates of birth and phone numbers for named citizens interacting with a ministry constitutes sensitive administrative personal data. If genuine, such access could support identity fraud, impersonation in administrative procedures and targeted phishing. In the absence of a verifiable record count or an independently reviewed data export, AFRINTEL assesses this claim with medium confidence and does not reproduce any citizen name, national ID/passport number, date of birth, phone number or request detail.


### July 02, 2026
#### 🇹🇳 Tunisia - Tayara.tn

- **Initial publication date:** 08 June 2026
- **AFRINTEL detection date:** 02 July 2026
- **Actor / Group:** KLINZO007, post published on a cybercriminal forum
- **Sector:** E-commerce / Online Classifieds Marketplace
- **Website:** [tayara.tn](https://tayara.tn)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4

- **Description:**

  Tayara.tn is Tunisia's largest online classifieds marketplace, part of the international Adevinta classifieds group, covering categories such as vehicles, real estate and jobs and connecting individual and business sellers with buyers across the country.

- **Analysis:**

  AFRINTEL reviewed a post published on 8 June 2026 by the newly registered actor KLINZO007 (account created June 2026, low reputation), titled "[MASSIVE LEAK] Tunisia Tayara.tn Database - 2 Million Lines | [4GB Full Dump]". The actor claims to hold the complete Tayara.tn user database: over 2,000,000 lines, a 4 GB raw dump, containing full names, active users' mobile phone numbers, email addresses, hashed passwords, ad titles and descriptions (vehicles, real estate, jobs), verified listing prices and full nationwide category/location coverage. Rather than a public download link, the post states the dump is "ready to send" on request via Telegram and TOX contact, and includes a short raw data sample directly in the thread.

  AFRINTEL independently reviewed the published sample. It consists of structured user records including internal platform and group-wide identifiers (linking each account to Adevinta's shared user-identity system), account creation timestamps, a retained history of prior state changes per account (previous display names, emails and phone numbers), avatar URLs, phone numbers, and salted password hashes (pbkdf2-sha256). Notably, a subset of the reviewed records additionally contain full RSA-style private and public key material embedded directly in the user record, associated with per-account cryptographic functionality; exposure of this key material is a significant risk in its own right, independent of password strength, as it could enable impersonation or decryption of anything secured with the affected keys. One reviewed record also contained a stored cross-site-scripting payload in place of a display name, indicating either a persisted historical attack against the platform or contamination from automated scanning.

  The exact structural match between the actor's description and the independently reviewed sample, together with the plausibility and internal consistency of the records, supports a very high confidence assessment. Given the combination of full identity data, password hashes and per-account private key material at national platform scale, AFRINTEL rates this incident's impact as Level 4. AFRINTEL does not reproduce any user name, phone number, email address, password hash, cryptographic key or record from the reviewed material.


### July 02, 2026
#### 🇲🇦 Morocco - Moroccan Public Procurement Portal

- **Initial publication date:** 26 January 2026
- **AFRINTEL detection date:** 02 July 2026
- **Actor / Group:** B4baYega, post published on a cybercriminal forum
- **Sector:** Government / Public Administration / Public Procurement
- **Website:** [marchespublics.gov.ma](https://marchespublics.gov.ma)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  The Moroccan Public Procurement Portal is the national exchange platform connecting public buyers and suppliers. It supports the publication and consultation of tenders, purchase orders, procurement results, official records and planned public procurement programmes, and is associated with the Kingdom's General Treasury.

- **Analysis:**

  A cybercriminal-forum post attributed to B4baYega, originally published on 26 January 2026 and re-reviewed by AFRINTEL on 02 July 2026, advertises the alleged compromise of the portal's database and offers the material for USD 300. The actor claims approximately 35,000 records, 25,000 documents and a compressed RAR archive of about 16 GB, with structured data in CSV format and documents including PDF and DOCX files. The provided material shows no database structure, column names or document contents. Although the post refers to text and photographic samples, no usable sample is directly visible; authenticity, origin, age, actual document count and archive completeness therefore remain unverified. Given the portal's role, the claimed material could support identification of public buyers, suppliers, procurement procedures and government commercial relationships, as well as targeted phishing, procurement fraud, supplier impersonation and social engineering. The visible material establishes the existence and stated characteristics of a sales offer, but does not independently demonstrate compromise of the portal or possession of the complete database.


### July 06, 2026
#### 🇪🇬 Egypt - EBNY Development

- **Initial publication date:** 06 July 2026
- **AFRINTEL detection date:** 06 July 2026
- **Ransomware group:** TheGentlemen
- **Sector:** Real estate development
- **Website:** [ebny.com.eg](https://ebny.com.eg/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  EBNY Development is an Egyptian real estate developer founded in 2012. The company develops residential and urban real estate projects in Egypt and positions its activities around the design, development and delivery of property projects.

- **Analysis:**

  The July 2026 ransomware dataset lists EBNY Development as a victim attributed to TheGentlemen. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect client, contract and property-related information and may support phishing, identity fraud and targeted extortion against property buyers and business partners.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-06
listing_last_observed_at: 2026-07-06
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-06
-->

### July 06, 2026
#### 🇰🇪 Kenya - East African Gasoil Limited (EAGOL)

- **Initial publication date:** 06 July 2026
- **AFRINTEL detection date:** 06 July 2026
- **Ransomware group:** arcusmedia
- **Sector:** Fuel distribution, oil and gas
- **Website:** [eastafricangasoil.com](https://www.eastafricangasoil.com/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  East African Gasoil Limited (EAGOL) is a Kenyan company established in 2009 and active in petroleum product marketing. Headquartered in Nairobi, it supplies fuel products and energy services in Kenya and has developed a regional East African presence.

- **Analysis:**

  The July 2026 ransomware dataset lists East African Gasoil Limited (EAGOL) as a victim attributed to arcusmedia. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect operational, supplier and customer information related to fuel distribution and may support phishing, supply-chain disruption, invoice fraud and extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-06
listing_last_observed_at: 2026-07-06
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-06
-->

### July 10, 2026
#### 🇲🇦 Morocco - Eurodefi

- **Initial publication date:** 10 July 2026
- **AFRINTEL detection date:** 10 July 2026
- **Ransomware group:** qilin
- **Sector:** Professional services / Accounting and audit
- **Website:** [eurodefis.com](https://www.eurodefis.com)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  Eurodefi is a Moroccan limited-liability company based in Casablanca. Public company information describes it as an accounting and audit firm providing accounting expertise, legal and tax advice, audit and statutory-audit services.

- **Analysis:**

  The July 2026 ransomware dataset lists Eurodefi as a victim attributed to qilin. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect financial, accounting and client-related information and may support phishing, invoice fraud, supplier impersonation and targeted extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-10
listing_last_observed_at: 2026-07-10
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-10
-->

### July 10, 2026
#### 🇩🇿 Algeria - Hassiba Ben Bouali University of Chlef (univ-chlef.dz)

- **Initial publication date:** April 10, 2026
- **AFRINTEL detection date:** July 10, 2026
- **Actor / Group:** Phantom Atlas
- **Sector:** Education / Higher education
- **Website:** [univ-chlef.dz](https://www.univ-chlef.dz)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3

- **Description:**

  Hassiba Ben Bouali University of Chlef is an Algerian public higher-education institution comprising nine faculties and two institutes.

- **Analysis:**

  Phantom Atlas published, on April 10, 2026, a claim of access to the university server's phpMyAdmin interface, addressed directly to the institution's director and framed as exposing "internal governance failures" rather than a mere technical exploit. The post's own text refers to access obtained and maintained since November 8, 2025. The post claims full access to administration panels and student databases, while explicitly stating it does not intend to leak student data. A follow-up message, posted after the site was taken down for maintenance, reiterates the claimed extended access and threatens further disclosures.

  Analysis of the visible data identified two distinct databases presented through phpMyAdmin on univ-chlef.dz. The first corresponds to a CMS-type website database (table prefix `refx_`, including post, comment, user and SEO metadata tables), totaling 15 tables for approximately 152.5 MiB. The second corresponds to a staff administrative-management database (19 tables, including `ats`, `att_travail`, `fiche_paie`, `personne`, `grade`, `print_badge`), totaling approximately 13,630 rows for 1.7 MiB. A visible excerpt of the `ats` table displays named staff records including first and last name in French and Arabic, gender, professional grade, date and place of birth, a photo reference, an appointment date, a faculty assignment code and a password stored as a 40-character hexadecimal hash.

  The consistency of the visible interface, table names and fields, together with the site's maintenance shortly after the post, supports a high-confidence assessment that the published material plausibly depicts a university database environment. It does not independently establish how access was obtained, whether it remained active or whether all claimed databases were accessible. The visible staff data, including dates of birth and hashed passwords, creates a risk of identity theft, account compromise in case of password reuse, and targeted phishing against university staff. Analysis was limited to the visible material because the original database exports were not available; AFRINTEL does not reproduce any name, date of birth, place of birth, photo reference or hash value.


### July 11, 2026
#### 🇹🇳 Tunisia - TOPNET

- **AFRINTEL detection date:** 11 July 2026
- **Actor / Group:** GreYyM3terr
- **Sector:** Telecommunications / Internet Service Provider
- **Website:** [topnet.tn](https://www.topnet.tn)
- **Status:** Claim - Data Sample Published
- **Incident type:** Access Sale
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:**

TOPNET is a Tunisian Internet Service Provider. A post published on an underground forum by the actor GreYyM3terr advertises the sale of webmail access associated with the `@topnet.tn` domain.

- **Analysis:**

The post identifies `@topnet.tn` as one of two Tunisian email domains to which the actor claims to have access. No price, number of compromised accounts, access method or validity period is provided.

The data visible in the provided material depicts a TOPNET Webmail interface with an inbox containing **273 messages**. Visible elements correspond to professional communications involving team schedules, attendance records, human resources, a salary transfer, meal vouchers, training activities and B2C customer retention campaigns.

The visible material supports the existence of at least one mailbox interface presented as associated with TOPNET. It does not independently establish that the actor controlled the mailbox, demonstrate a domain-wide compromise of `topnet.tn` or establish how many accounts were accessible.

Access to a professional mailbox has significant operational value for a threat actor. It can provide internal information, employee relationships and business processes that may support spear phishing, impersonation, conversation hijacking and business email fraud.

No mailbox dump, downloadable archive or complete database is visible. The underground offer concerns the **sale of webmail access**, rather than the publication of an exfiltrated dataset.


### July 11, 2026
#### 🇹🇳 Tunisia - Orange Tunisia

- **AFRINTEL detection date:** 11 July 2026
- **Actor / Group:** GreYyM3terr
- **Sector:** Telecommunications / Telecom operator
- **Website:** [orange.tn](https://www.orange.tn)
- **Status:** Claim - Data Sample Published
- **Incident type:** Access Sale
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:**

Orange Tunisia is a Tunisian telecommunications operator. In the same post published on an underground forum, GreYyM3terr advertises the sale of webmail access that the actor associates with the `@orange.tn` domain.

- **Analysis:**

The actor identifies `@orange.tn` as the second domain included in the offer. No asking price, affected account identifier, number of accessible mailboxes, compromise method or access validity period is disclosed.

The provided material depicts an Orange-branded webmail interface containing professional communications. Visible message subjects relate to debt recovery activities, international cooperation projects, administrative procedures, technical requests, agreements and quotations.

The exact address of the authenticated mailbox is not visible. The observed evidence therefore provides visual support for access to a webmail environment presented as related to Orange, but does not establish the overall scope of compromise affecting the `orange.tn` domain.

Access to a professional mailbox could allow a threat actor to map trusted relationships, identify partners and correspondents, understand ongoing business activities and prepare highly contextualised phishing campaigns. Existing email conversations may also facilitate impersonation and business email fraud.

No mailbox archive, database dump or complete email extraction is visible. The actor is primarily selling **webmail access**, with the visible interface used to support the offer.
---

### July 11, 2026
#### 🇲🇦 Morocco - Planet Sport

- **Initial publication date:** 11 July 2026
- **AFRINTEL detection date:** 11 July 2026
- **Actor / Group:** Mozvo, post published on a cybercriminal forum
- **Sector:** E-commerce / Retail / Sporting goods
- **Website:** [planetsport.ma](https://planetsport.ma)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3

- **Description:**

  Planet Sport is a Moroccan sporting-goods retailer and e-commerce operator. Its activities include the sale and distribution of sports equipment, apparel and related products.

- **Analysis:**

  A forum publication attributed to Mozvo advertises a “full leak” of Planet Sport data. The post is dated 11 July 2026 and points to a compressed archive. Local analysis of the supplied unpacked directory identified approximately 2.1 GB of material across 1,100 files: 660 XLSX spreadsheets, 34 XLS spreadsheets, 375 PDF documents, 28 DOCX documents and three CSV files.

  The corpus covers product catalogues and commercial packs, stock and warehouse records, purchase orders, invoices, import and customs documentation, distributor and brand operations, product interfaces, payments and accounting material. The main e-commerce export contains 12,001 data rows across 65 columns. Its field structure includes personal or account-related fields alongside order, product, stock and transaction fields; no raw values are reproduced.

  The archive is operationally significant because it may expose commercial relationships, inventory and pricing information, supply-chain documentation, financial records and personal or account-related data. Potential impacts include targeted phishing, invoice and payment fraud, supplier impersonation, competitive intelligence and abuse of customer or staff information. The available corpus demonstrates a substantial publication, but its completeness, origin and direct technical connection to Planet Sport have not been independently verified.

  **Relationship hypothesis:** the same domain, `planetsport.ma`, was previously listed by LockBit 5 on 29 April 2026 as an unverified ransomware claim. It is plausible that the July material was downloaded and freely republished or redistributed by a third party after an earlier LockBit-related exfiltration, or that Mozvo was an affiliate or associated operator. AFRINTEL found no evidence proving a relationship between Mozvo and LockBit 5, such as matching archive hashes, shared infrastructure, identical leak-site references or an explicit attribution. The July and April records are therefore retained as a possible free republication/redistribution or related double claim, with the relationship unresolved.


### July 11, 2026
#### 🇬🇭 Ghana - Golden Star Resources

- **Initial publication date:** 11 July 2026
- **AFRINTEL detection date:** 11 July 2026
- **Ransomware group:** cmdorganization
- **Sector:** Gold mining
- **Website:** [gsr.com](https://www.gsr.com/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 4

- **Description:**

  Golden Star Resources is a gold mining operator active in Ghana and operating the Wassa Gold Mine. Its official website identifies the company as a subsidiary of Chifeng Gold Group, with the Government of Ghana holding an interest in the mining operation.

- **Analysis:**

  The July 2026 ransomware dataset lists Golden Star Resources as a victim attributed to cmdorganization. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect operational, financial and state-related mining-sector information and may support espionage, supply-chain disruption, phishing and targeted extortion against a strategic mineral-resource asset.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-11
listing_last_observed_at: 2026-07-11
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-11
-->

### July 13, 2026
#### 🇨🇲 Cameroon - TurboSoft

- **Initial publication date:** 13 July 2026
- **AFRINTEL detection date:** 13 July 2026
- **Ransomware group:** spacebears
- **Sector:** Business software and IT services
- **Website:** [turbosoft.cm](https://turbosoft.cm/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  TurboSoft is a Cameroonian business software provider based in Yaoundé. Its portfolio includes payroll and personnel management, accounting, banking management and school management software.

- **Analysis:**

  The July 2026 ransomware dataset lists TurboSoft as a victim attributed to spacebears. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect client organisations' payroll, accounting and banking-related data hosted or processed through TurboSoft's software and may support supply-chain phishing, financial fraud and extortion against TurboSoft's business clients.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-13
listing_last_observed_at: 2026-07-13
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-13
-->

### July 14, 2026
#### 🇳🇬 Nigeria - i-Fitness Gym & Wellness Centre

- **Initial publication date:** 14 July 2026
- **AFRINTEL detection date:** 14 July 2026
- **Ransomware group:** arcusmedia
- **Sector:** Fitness, health and wellness
- **Website:** [ifitness.ng](https://ifitness.ng/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  i-Fitness is a Nigerian health, fitness and wellness company operating a network of gyms. It provides fitness facilities, professional trainers, group classes and related services supporting members' fitness and wellness.

- **Analysis:**

  The July 2026 ransomware dataset lists i-Fitness Gym & Wellness Centre as a victim attributed to arcusmedia. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect member and payment-related information and may support phishing, payment fraud and targeted extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-14
listing_last_observed_at: 2026-07-14
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-14
-->

### July 14, 2026
#### 🇿🇦 South Africa - BE Travel

- **Initial publication date:** 14 July 2026
- **AFRINTEL detection date:** 14 July 2026
- **Ransomware group:** arcusmedia
- **Sector:** Corporate travel and events management
- **Website:** [betravel.co.za](https://betravel.co.za/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  BE Travel is a South African travel and events management company. It focuses on corporate travel management and supports travel across South Africa, the region and international destinations.

- **Analysis:**

  The July 2026 ransomware dataset lists BE Travel as a victim attributed to arcusmedia. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect traveller, booking and corporate-client information and may support phishing, identity fraud and targeted extortion against corporate clients and travellers.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-14
listing_last_observed_at: 2026-07-14
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-14
-->

### July 15, 2026
#### 🇿🇦 South Africa - ISEGEN South Africa (Pty) Ltd

- **Initial publication date:** 15 July 2026
- **AFRINTEL detection date:** 15 July 2026
- **Ransomware group:** dragonforce
- **Sector:** Chemical manufacturing
- **Website:** [isegen.co.za](https://isegen.co.za/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  ISEGEN South Africa (Pty) Ltd is a South African chemical manufacturer. Its products include food acidulants, phthalic and maleic anhydrides, and plasticisers, with production facilities in South Africa.

- **Analysis:**

  The July 2026 ransomware dataset lists ISEGEN South Africa (Pty) Ltd as a victim attributed to dragonforce. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect operational, supplier and commercial information and may support phishing, supplier impersonation, invoice fraud and extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-15
listing_last_observed_at: 2026-07-15
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-15
-->

### July 15, 2026
#### 🇿🇦 South Africa - Fidelity Services Group

- **Initial publication date:** 15 July 2026
- **AFRINTEL detection date:** 15 July 2026
- **Ransomware group:** ransomhouse
- **Sector:** Integrated security and risk services
- **Website:** [fidelity-services.com](https://fidelity-services.com/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  Fidelity Services Group is a South African provider of integrated security and risk solutions. Its activities include guarding, technology-enabled security, cash management, fire security and other services for residential and corporate customers.

- **Analysis:**

  The July 2026 ransomware dataset lists Fidelity Services Group as a victim attributed to ransomhouse. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect client, site-security and cash-management operational information and may support phishing, physical-security reconnaissance, targeted extortion and fraud against corporate and residential customers.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-15
listing_last_observed_at: 2026-07-15
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-15
-->

### July 16, 2026
#### 🇧🇼 Botswana - North Atlantic Engineering Consultants

- **Initial publication date:** 16 July 2026
- **AFRINTEL detection date:** 16 July 2026
- **Ransomware group:** dragonforce
- **Sector:** Mechanical and electrical engineering consulting
- **Website:** [northatlantic.bw](https://www.northatlantic.bw/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  North Atlantic Engineering Consultants is an engineering consultancy based in Gaborone, Botswana. It provides mechanical and electrical engineering services covering electrical installations, HVAC, fire protection, wet services, lighting design, thermal analysis and information technology.

- **Analysis:**

  The July 2026 ransomware dataset lists North Atlantic Engineering Consultants as a victim attributed to dragonforce. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect project, client and technical design information and may support phishing, client impersonation, competitive intelligence gathering and extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-16
listing_last_observed_at: 2026-07-16
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-16
-->

### July 16, 2026
#### 🇩🇿 Algeria - ATS (Algérie Télécom Satellite)

- **Initial publication date:** April 16, 2026
- **AFRINTEL detection date:** July 16, 2026
- **Actor / Group:** Phantom Atlas
- **Sector:** Telecommunications / Satellite Operator
- **Website:** [ats.dz](https://www.ats.dz)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3

- **Description:**

  ATS (Algérie Télécom Satellite) is the Algerian satellite operator, a subsidiary of the Algérie Télécom group, providing nationwide satellite telecommunications services.

- **Analysis:**

  Phantom Atlas published, on April 16, 2026, a claim of a full compromise of ATS's digital systems, stating it held the payroll slips of all of the company's employees. The message carries an explicitly pro-Moroccan hacktivist tone (quoting Morocco's royal motto "Allah, Al Watan, Al Malik"), framing the operation as a direct response to earlier cyberattacks targeting Morocco, and announces the upcoming release of a payroll sample along with staff names and positions.

  AFRINTEL reviewed a local sample of 88 files (approximately 29 MB), mostly individual payroll slips in image format, dated from July 2023 to November 2024, along with a few more recent screenshots. The reviewed slips concern employees from different ATS regional directorates (Regional Directorate East-Constantine, South-East Directorate, among others) and display a consistent structure: employer number, staff ID, first and last name, hiring date, marital status, social security number, job title and category/grade, along with a full breakdown of salary items (earnings and deductions), the social-contribution base, taxable salary, bank account number and net amount payable. Several documents carry authentic-looking stamps from ATS's Human Resources Department or regional directorates.

  The consistency of the format across the sample, the diversity of employees, directorates and time periods represented, and the presence of plausible official stamps support a high confidence level regarding the authenticity of this leak. Exposure of named payroll slips, including social security numbers and banking details, creates a high risk of financial fraud, identity theft and targeted phishing against ATS staff. AFRINTEL does not reproduce any name, staff ID, social security number, account number or salary figure from the reviewed sample.


### July 16, 2026
#### 🇪🇬 Egypt - BazookaEgy (bazookaegy.com)

- **Initial publication date:** January 16, 2026
- **AFRINTEL detection date:** July 16, 2026
- **Actor / Group:** MrMeeseeks (original leak); reposted by Sphere on a cybercriminal forum (RaidForums)
- **Sector:** Fast Food / Retail
- **Website:** [bazookaegy.com](https://www.bazookaegy.com)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 2

- **Description:**

  Bazooka is an Egyptian fast-food chain, also present in Kuwait, the UAE, Qatar and Bahrain, with an online ordering and registration site.

- **Analysis:**

  The account Sphere reposted, on January 16, 2026, for the second time according to the post title ("[REPOST][REPOST]"), a leak originally attributed to the actor MrMeeseeks and titled "Egypt 1M Costumer information's bazookaegy.com". The sample shown in the post includes a field schema covering the registration channel (mobile_ios, mobile_android, IOS, web_site), an ID, first name, last name, email address and mobile number.

  About thirty complete records are directly visible in the sample, with names (in Latin and Arabic characters), email addresses (including several Apple private-relay addresses) and Egyptian phone numbers. The consistency of the schema with an online ordering platform and the presence of numerous individual records support a high confidence level regarding the authenticity of this leak, although the total claimed volume of one million customers stated in the title could not be independently verified beyond the observed sample. Exposure of this data could facilitate targeted phishing and commercial spam against the chain's customers. AFRINTEL does not reproduce any name, email address or phone number from the reviewed sample.


### July 16, 2026
#### 🇪🇬 Egypt - Sinai Grand Casino

- **Initial publication date:** 16 July 2026
- **AFRINTEL detection date:** 16 July 2026
- **Ransomware group:** dragonforce
- **Sector:** Casino, gaming and entertainment
- **Website:** [sinaigrandcasino.com](https://sinaigrandcasino.com/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  Sinai Grand Casino is a gaming and entertainment venue located in Naama Bay, Sharm El Sheikh, Egypt. It offers roulette, blackjack, poker, slot machines, as well as dining and entertainment services.

- **Analysis:**

  The July 2026 ransomware dataset lists Sinai Grand Casino as a victim attributed to dragonforce. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect customer and payment-related information and may support phishing, payment fraud and targeted extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-16
listing_last_observed_at: 2026-07-16
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-16
-->

### July 18, 2026
#### 🇿🇦 South Africa - Reatile Group

- **Initial publication date:** 18 July 2026
- **AFRINTEL detection date:** 18 July 2026
- **Ransomware group:** incransom
- **Sector:** Investment holding, energy and industry
- **Website:** [reatile.co.za](https://www.reatile.co.za/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  Reatile Group is a South African investment holding company established in 2003. Its strategic focus is on the energy, petrochemical and industrial sectors, where it owns and develops portfolio investments.

- **Analysis:**

  The July 2026 ransomware dataset lists Reatile Group as a victim attributed to incransom. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect corporate, financial and investment-related information and may support phishing, business email compromise, invoice fraud and extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-18
listing_last_observed_at: 2026-07-18
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-18
-->

### July 19, 2026
#### 🇿🇦 South Africa - CKR Consulting Engineers

- **Initial publication date:** 19 July 2026
- **AFRINTEL detection date:** 19 July 2026
- **Ransomware group:** payload
- **Sector:** Multidisciplinary engineering consulting
- **Website:** [ckr.co.za](https://ckr.co.za/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  CKR Consulting Engineers is a South African multidisciplinary engineering consultancy. It provides built-environment engineering services including electrical, mechanical, civil, structural, ICT and other technical systems, with projects across Africa, the Middle East and Asia.

- **Analysis:**

  The July 2026 ransomware dataset lists CKR Consulting Engineers as a victim attributed to payload. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect project, client and technical design information and may support phishing, client impersonation, competitive intelligence gathering and extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-19
listing_last_observed_at: 2026-07-19
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-19
-->

### July 21, 2026
#### 🇹🇳 Tunisia - Ministry of Justice
- **AFRINTEL detection date:** 21 July 2026
- **Actor / Group:** R3V4ULT
- **Sector:** Government / Justice / Public administration
- **Website:** justice.gov.tn
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3
- **Description:**

The Tunisian Ministry of Justice is the public administration responsible for the judicial sector in Tunisia. Its activities include the administration of courts, correctional facilities and judicial services.

- **Analysis:**

The actor R3V4ULT published an initial dataset on a cybercriminal forum, presenting it as originating from the Tunisian Ministry of Justice. The post uses a hacktivist narrative related to water and electricity disruptions in Tunisia, contains two download links and announces possible additional disclosures.

The analysed CSV file contains 6,599 unique contact records, structured into four fields: first name, surname, email address and domain. Of these records, 6,593 addresses use the institutional domains justice.gov.tn, mail.justice.gov.tn, e-justice.tn or mail.e-justice.tn. No passwords, hashes, authentication tokens or email content were identified.

The sample also includes a three-page scanned administrative document dated 23 October 2024, containing internal references, budget lines, financial amounts, stamps and signatures. The visible expenses relate to water, electricity, gas, telecommunications, rent, transportation, maintenance, administrative supplies and certain medical expenses associated with detainees. A fuel supply request is also visible in the forum publication.

The observed files represent an initial sample, not a complete release. They do not confirm access to email accounts, compromised credentials or the intrusion vector. The exposed information could nevertheless support targeted phishing, impersonation of public officials, mapping of judicial departments and fraud using credible administrative references.

As an Ethiopian proverb states, “When spider webs unite, they can tie up a lion.” The Ministry should strengthen multifactor authentication, monitor abnormal use of institutional accounts and investigate the source of the exposure.

As the government sector remains particularly exposed to data leaks in Africa, other public institutions should treat this publication as a sector-wide warning, review exposed directories, notify their SOC teams and prepare employees for phishing campaigns that may reuse the leaked information.

---

### July 23, 2026
#### 🇨🇮 Ivory Coast - Compagnie des Caoutchoucs du Pakidié (CCP)

- **Initial publication date:** 23 July 2026
- **AFRINTEL detection date:** 23 July 2026
- **Ransomware group:** TheGentlemen
- **Sector:** Rubber farming and natural rubber processing
- **Website:** [pakidie.com](https://www.pakidie.com/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  Compagnie des Caoutchoucs du Pakidié (CCP) is an Ivorian company established in 1960 and a pioneer of rubber farming in the country. It operates rubber plantations, processes and sells natural rubber, and also manufactures latex-based products.

- **Analysis:**

  The July 2026 ransomware dataset lists Compagnie des Caoutchoucs du Pakidié (CCP) as a victim attributed to TheGentlemen. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect operational, supplier and commercial information and may support phishing, supplier impersonation, invoice fraud and extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-23
listing_last_observed_at: 2026-07-23
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-23
-->

### July 23, 2026
#### 🇸🇸 South Sudan - Nile Petroleum Corporation (NILEPET)

- **Initial publication date:** 23 July 2026
- **AFRINTEL detection date:** 23 July 2026
- **Ransomware group:** krybit
- **Sector:** Oil and gas
- **Website:** [nilepet.com](https://nilepet.com/)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 4

- **Description:**

  Nile Petroleum Corporation (NILEPET) is South Sudan's state-owned national oil and gas company, headquartered in Juba. It represents the state's interests in the petroleum sector and operates across hydrocarbon-related activities.

- **Analysis:**

  The July 2026 ransomware dataset lists Nile Petroleum Corporation (NILEPET) as a victim attributed to krybit. AFRINTEL reviewed a local corpus of 71 files associated with the domain, including 34 PDFs, 25 DOCX documents, one XLSX workbook, 9 TXT files and supporting image files.

  The corpus contains fuel-ordering and fuel-receipt procedures, station asset and equipment management, workforce and agent-management documents, sales and reporting procedures, financial and cash-management material, contracts and partnerships, governance, risk-management and technical-support procedures. It also includes accounting and operational reports covering fuel inventories, receivables, payables, bank reconciliations, assets and customer prepayments, with most dated material referring to 2022 and 2023 and some later references. The available files therefore provide a structured sample of operational, financial, workforce and supply-chain documentation associated with NILEPET.

  The local corpus supports the existence of a substantial disclosed document set, but it does not independently establish the intrusion method, complete archive size, ransomware encryption or victim confirmation. No disclosure deadline was stated in the available record. AFRINTEL does not reproduce names, account details, financial figures, credentials or other raw sensitive content.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-23
listing_last_observed_at: 2026-07-23
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: release-reviewed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-23
-->

### July 24, 2026
#### 🇲🇦 Morocco - Distamed

- **AFRINTEL detection date:** 24 July 2026
- **Actor / Group:** anisanas2
- **Sector:** Healthcare / Medical equipment
- **Website:** [distamed.ma](https://distamed.ma)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4

- **Description:**

Distamed is a Moroccan company specialising in medical equipment and digital healthcare solutions. Its activities include cardiology, pulmonology, neurology, sleep diagnostics, rehabilitation and medical imaging.

- **Analysis:**

The actor anisanas2 claims to have extracted Distamed’s data and is offering the company’s internal archives for sale for **USD 5,000**. The publication also announces the future release of the complete dataset.

The reviewed files contain **8,823 patient rows**, including 8,776 distinct rows, with names, dates of birth, ages, national identity numbers, telephone numbers, cities, insurance details and visit dates. They also include **8,147 client entries**, **1,195 entries presented as a doctor list**, **1,550 contracts**, **1,455 invoices** and **3,251 payments**.

The observed documents also include medical reports containing pathologies, examination results and clinical conclusions. Some entries refer to Moroccan public and military hospitals.

The consistency between the administrative, medical and financial data supports the assessment that the reviewed material contains a significant exposure. It does not independently establish the acquisition method, archive completeness or official victim confirmation. The claim that the complete archive dates back to 2013 is not demonstrated by the reviewed material, whose observed dates mainly cover **2018 to 2026**.

This exposure creates high risks of medical confidentiality breaches, identity theft, document fraud, invoice fraud and targeted phishing against patients, doctors and partner institutions.

- **Recommendations:**

1. Investigate unusual access, exports and download activity, then immediately revoke potentially compromised accounts, sessions and keys.
2. Notify affected individuals and institutions, then strengthen monitoring for identity fraud, invoice fraud and fraudulent changes to banking details.

### July 24, 2026
#### 🇲🇦 Morocco - Moroccan Biometric Passport Portal

- **AFRINTEL detection date:** 24 July 2026
- **Actor / Group:** Magherbi, post published on a cybercriminal forum
- **Sector:** Government / Public administration / Identity documents
- **Website:** [passeport.ma](https://www.passeport.ma)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4

- **Description:**

The publication targets the Moroccan portal associated with passport application and issuance services. The actor also claims to have compromised several other Moroccan government platforms related to consular services, civil status records and identity documents.

- **Analysis:**

The actor Magherbi claims to have compromised `passeport.ma` following a personal dispute related to a delay in the issuance of a passport. The actor threatens to publish the claimed databases free of charge unless the request is processed within **72 hours**, excluding Saturdays and Sundays.

The publication also names four additional platforms:

- `consulat.ma`
- `watiqa.ma`
- `alhalalmadania.ma`
- `cnie.ma`

A sample of personal data is directly visible. Observed fields include:

`NUM_COMMANDE`, `NOM`, `PRENOM`, `NOM_AR`, `PRENOM_AR`, `CIN`, `DATE_NAISSANCE`, `ADRESSE`, `TEL`, `EMAIL`, `NBR_ENFANTS` and `SITUATION_FAMILIALE`.

The displayed records contain administrative order references, identities in Latin and Arabic characters, national identity card numbers, dates of birth, residential addresses, telephone numbers, email addresses and family-related information.

The exposed data creates a high risk of identity theft, document fraud, targeted phishing and social engineering. Combining national identity numbers, dates of birth, addresses and contact details allows threat actors to build detailed profiles of the affected individuals.

The visible sample supports the assessment that the publication contains personal data, but it does not by itself establish the actor's control of the complete source datasets. Its exact origin cannot be conclusively attributed to `passeport.ma` or to any of the four additional platforms named in the post. No separate sample or technical evidence is provided for each domain.

No total file size, record count, price or download link is visible. The provided material contains a disclosure threat associated with a deadline, but it does not establish that the complete databases of all five platforms were extracted.

For AFRINTEL, the publication should be recorded as **one primary incident targeting `passeport.ma`**, with the four additional domains listed as further claimed platforms. Separate incidents should not be created without distinct evidence for each platform.

### July 24, 2026
#### 🇳🇬 Nigeria - Unidentified federal university (system access)

- **Initial publication date:** July 24, 2026
- **AFRINTEL detection date:** 24 July 2026
- **Actor / Group:** nowornever, post published on a cybercriminal forum (RaidForums)
- **Sector:** Government / Higher education (federal university)
- **Website:** Not identified with certainty
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Access Sale
- **Confidence level:** Low
- **Impact level:** Level 4

- **Description:**

  The post targets an unidentified server belonging to a Nigerian federal university (national .ng domain), without naming the specific institution or providing its domain.

- **Analysis:**

  The actor nowornever, whose account had just been created (July 2026, a single post published, no reputation), claims to have obtained, while exploring .ng domains, SYSTEM-level access to a domain-joined Windows Server 2019 (IIS) machine, with full access to every file on the machine and to a PostgreSQL database described as more than 200 tables deep. The actor also claims SYSTEM-level RDP access, a mapped internal subnet, enumeration of the Active Directory domain and the possibility of lateral movement, as well as access to a Microsoft 365 tenant with Azure AD authentication and full user enumeration. Finally, the actor claims superadmin rights across multiple target servers and refers to a portal-style dashboard, without providing visible technical evidence.

  The actor also claims to have found, on the same server, personal material attributed to an employee (likely an IT staff member): more than 160 saved passwords, accounts on several cryptocurrency and fintech platforms, and banking details and a payment method linked to a personal email address stored on the server.

  The post shows no screenshot or technical evidence (administration console, RDP session, Azure AD or PostgreSQL dashboard) independently corroborating these claims; the text asserts their existence without demonstrating it. The account's newness, lack of reputation and absence of visible proof support a low confidence level. If confirmed, however, these claims would describe a critical compromise of a Nigerian public university's core infrastructure (full domain access, Microsoft 365 cloud tenant, possible lateral movement), which justifies a high impact level as a precaution. No fixed price is stated; the actor asks potential buyers to submit an offer along with fresh proof. AFRINTEL does not reproduce any credential, password, banking detail or information relating to the mentioned employee.

- **Recommendations:**

  1. Nigerian federal universities exposing Windows Server, RDP or Microsoft 365 tenant services should review authentication and administrator access logs for the relevant period, and look for abnormal account creation or privilege escalation activity.
  2. Audit service and administrator accounts for reuse of personal passwords, and raise awareness among IT staff about storing personal or financial data on professional servers.


### July 25, 2026
#### 🇿🇦 South Africa - MTN (attributed with reservation)

- **Initial publication date:** 25 July 2026
- **AFRINTEL detection date:** 25 July 2026
- **Actor / Group:** ki4tane; publication claims association with NullSec Nigeria
- **Sector:** Telecommunications
- **Website:** [mtn.com](https://www.mtn.com/)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:**

  MTN is a telecommunications group operating across several African markets. The supplied evidence does not identify which national MTN entity is allegedly affected.

- **Analysis:**

  A forum post dated 25 July 2026 claims that customer and employee credentials linked to MTN were disclosed. The post refers to customer email/password material, approximately 2,000 employee credentials and downloadable files. AFRINTEL reviewed the evidence directory without reproducing records: client.emails.txt contains 130 lines, while the employee archive contains separate email, credential and password files with 381, 814 and 549 lines respectively. The employee email sample uses the mtn.com domain, supporting an apparent MTN corporate context but not the affected country or subsidiary with certainty. AFRINTEL attributes this record to South Africa with reservation: the actor frames the attack around tensions between South Africa and Nigerian nationals, and one fragment in the domain sample references "MTNGroupsa", which supports this attribution. MTN Group Limited is headquartered in Johannesburg, South Africa, so this fragment plausibly refers to the group's parent entity, whose email and IT infrastructure is often managed centrally; this does not establish that the affected customers or employees belong to the South African subsidiary specifically rather than another national operation. A Nigeria-linked fragment ("clientsupport.ng") also appears in the same sample, and the actor identifies as NullSec Nigeria, so the country attribution is treated as low-confidence and subject to revision. The data, access path and claimed complete volume have not been independently verified. AFRINTEL records one data-leak incident and does not reproduce credentials, passwords, download links or personal data.
### July 26, 2026
#### 🇲🇦 Morocco - Brazer Ingenierie

- **Initial publication date:** 26 July 2026
- **AFRINTEL detection date:** 26 July 2026
- **Ransomware group:** arcusmedia
- **Sector:** Engineering / Telecommunications / Construction
- **Website:** [brazeringenierie.com](https://www.brazeringenierie.com)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  Brazer Ingenierie is a Moroccan limited-liability company based in the Rabat-Témara area. Public business listings describe activities covering telecommunications works, electrical works and construction, while its public website presents low- and medium-voltage electrical services.

- **Analysis:**

  The July 2026 ransomware dataset lists Brazer Ingenierie as a victim attributed to arcusmedia. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect project, supplier, operational and commercial information and may support phishing, supplier impersonation, invoice fraud and extortion.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-26
listing_last_observed_at: 2026-07-26
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-26
-->

### July 26, 2026
#### 🇹🇳 Tunisia - École Nationale d'Administration (ENA) - concours.ena.tn

- **Initial publication date:** 26 July 2026
- **AFRINTEL detection date:** 26 July 2026
- **Actor / Group:** N0ull_0X, post published on a cybercriminal forum
- **Sector:** Government / Public Administration / Education (Civil Service Entrance Examinations)
- **Website:** [concours.ena.tn](https://concours.ena.tn) / [www.ena.tn](https://www.ena.tn)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4

- **Description:**

  ENA (École Nationale d'Administration) is Tunisia's national school for training civil servants. Concours.ena.tn is the platform it operates to manage competitive entrance examinations for candidates seeking admission to the civil service.

- **Analysis:**

  AFRINTEL reviewed a DarkForums post titled "Tunisia Database www.ena.tn / concours.ena.tn", published on 26 July 2026 by the newly registered actor N0ull_0X (account created July 2026). The post directly displays a plaintext sample of candidate records rather than a mere description, comprising at least seventeen rows following a consistent database schema: candidate full name, email address, gender, individual exam-module grades, an overall average and a baccalaureate average, physical home address, place of national ID (CIN) issuance, national ID (CIN) number, a fingerprint/biometric reference field tied to the CIN, phone number, date of birth, prior diploma years, competition code, specialty code and establishment code. The combination of a national identity number, a biometric reference field, contact details, home addresses and academic records for named individuals constitutes highly sensitive exposure of Tunisian citizens applying to a state civil-service examination. The structural consistency and volume of the displayed sample support a high confidence assessment, although AFRINTEL could not independently verify the total size of the underlying database or the currency of the data beyond the sample shown. AFRINTEL does not reproduce any candidate name, email, national ID number, phone number, address or exam result from the reviewed post.


### July 26, 2026
#### 🇳🇬 Nigeria - Zenith Bank Plc

- **Initial publication date:** 26 July 2026
- **AFRINTEL detection date:** 26 July 2026
- **Ransomware group:** ExfilSquad
- **Sector:** Banking and financial services
- **Website:** [zenithbank.com](https://www.zenithbank.com/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  Zenith Bank Plc is a commercial bank and financial services group headquartered in Lagos, Nigeria. It provides retail and corporate banking services, electronic banking, payments and other financial services.

- **Analysis:**

  The July 2026 ransomware dataset lists Zenith Bank Plc as a victim attributed to ExfilSquad. The available record does not provide a disclosed sample, ransom amount, data volume, displayed disclosure deadline, encryption evidence or independent victim confirmation. The claimed exposure could affect customer banking, payment and account information and may support phishing, account takeover, payment fraud and targeted extortion.

**Correlation assessment:** Zenith Bank Plc and zenithbank.com were previously listed on 9 August 2025 by KaruHunters in an unverified claim alleging the sale of more than 1.8 million customer and employee records. The 2025 claim and the July 2026 ransomware claim are separated by nearly eleven months and are attributed to different actors. AFRINTEL found no matching sample, archive fingerprint, data schema, shared infrastructure, explicit cross-reference or independent victim confirmation connecting them. The strongest current assessment is a related-victim / possible double-claim relationship, not a confirmed single compromise. The July record remains a separate Claim - Unverified ransomware entry.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-07-26
listing_last_observed_at: 2026-07-26
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-07-26
-->

### July 31, 2026
#### 🇩🇿 Algeria - Ministry of Finance

- **Initial publication date:** 12 January 2026
- **AFRINTEL detection date:** 31 July 2026
- **Actor / Group:** jrintel (source account)
- **Sector:** Government / Finance
- **Website:** Not specified
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 3

- **Description:**

  The Algerian Ministry of Finance is the government institution responsible for national fiscal and financial administration. A forum publication titled "Fresh Confidential Ministry of Finance Documents Leaked DEC 2025" advertises two PDF documents and displays samples of official administrative and financial correspondence, with a claimed document period of December 2025.

- **Analysis:**

  The provided material contains official-looking ministry documents and a publication attributed to the source account jrintel. It may expose sensitive administrative information, but AFRINTEL has not independently verified the documents, their provenance or the full dataset. Download links, session identifiers and personal information are not reproduced.
