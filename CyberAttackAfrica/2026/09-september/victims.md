![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in September 2026 (11 records)

👉🏾 [**Version française disponible ici**](./victims_FR.md)

## September 2026

**Monthly follow-up status: In Progress** — provisional corpus of 11 records; monthly closure and statistics are pending.

### 03 September 2026
#### 🇳🇬 Nigeria - Medical and Dental Council of Nigeria (MDCN)

- **Initial publication date:** 3 September 2026 at 20:19 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 28 September 2026 (screenshot and text excerpt supplied)
- **Actor / Group:** cattier (displayed forum account; identity unverified)
- **Sector:** Healthcare / Medical and dental professional regulation
- **Website:** [mdcn.gov.ng](https://www.mdcn.gov.ng/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium (structured post and excerpt observed; origin and scope uncorroborated)
- **Impact level:** Level 3

- **Description:** An account named cattier posted an offer titled “Medical and Dental Council of Nigeria 65K” and attributes data on **65,580 unique users** to `mdcn.gov.ng`. A sample of healthcare-practitioner records is visible, and **50 rows were supplied as text**. This establishes the existence of the post and the type of data presented; it does not confirm that 65,580 distinct people are affected or that MDCN systems were intruded upon.

- **Analysis:**

  **Observed:** The post dated **3 September 2026** displays `mdcn.gov.ng`, the figure **65,580**, and **24 field labels** covering identity, birth, contact details, professional registration number, origin and practice location, specialisation, medical school, employment and application date. The **50 supplied rows** broadly follow this structure and contain personal and professional information; they are not treated as 50 verified unique individuals. The visible application dates cluster between **28 October and 1 November 2022**; these are record dates, not incident dates. The domain belongs to the [Nigerian medical and dental council](https://www.mdcn.gov.ng/), which manages practitioner registration and licensing.

  **Assumption:** The field labels and row content are consistent with practitioner registration or licensing records. This supports a plausible association with the MDCN ecosystem without demonstrating that the data came directly from a compromised council system: an earlier copy, a service provider, aggregation or another source cannot be ruled out. The age field appears to reflect a later period than the 2022 application dates for some rows; how it was calculated is unknown.

  **Unknown:** the source file, its hash and actual record count, duplicates, accuracy and currency of the data, acquisition method, whether unauthorised access occurred, number of affected people, validation of **65,580 unique users**, confirmation by MDCN or an authority, and any operational effect remain unknown.

- **Analysis scope:** one forum screenshot and 50 text rows supplied in the conversation; no complete archive or database was provided. The 50 rows were not individually verified against the original source file or copied into the repository. A minimised technical manifest for the screenshot is retained outside the repository at `/tmp/afrintel-evidence/AFR-2026-TBD-mdcn/`.

- **Risk assessment:** the observed data categories could facilitate practitioner impersonation, targeted phishing, social engineering and document fraud. The excerpt establishes neither patient medical records nor valid portal access.

- **Sources / Evidence:** forum post and text excerpt supplied to AFRINTEL; [official MDCN website](https://www.mdcn.gov.ng/). No individual's name, telephone number, email address, birth date or professional identifier is published.

### 04 September 2026
#### 🇪🇬 Egypt - Data attributed to Madinaty owners/residents (source organisation unidentified)

- **Incident date:** Not established
- **Initial publication date:** 4 September 2026 at 09:59 (displayed time; timezone not specified)
- **AFRINTEL detection date:** 13 September 2026 (capture supplied)
- **Actor / Group:** sainttrojan (displayed forum account; identity and group affiliation unverified)
- **Sector:** Real estate / Residential community / Property management
- **Data-holding organisation:** Unidentified; the post presents the records as relating to Madinaty owners/residents
- **Source organisation website:** Not identified
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:** Madinaty is a residential urban development in Egypt that Talaat Moustafa Group presents among its projects in the country. This establishes geographic context; it does not identify the organisation that collected or held the data, or confirm that Talaat Moustafa Group was compromised. ([Talaat Moustafa Group overview](https://ecommerce.tmg.com.eg/about))

- **Analysis:**

  A forum post attributed to the **sainttrojan** account, dated 4 September 2026 at 09:59 (timezone not specified), is titled as an offer of data concerning Madinaty owners. The author claims that the excerpt represents **0.5%** of a dataset and seeks a partner to monetise it. The percentage and possession of the complete dataset are the author's claims and have not been verified.

  **Observed:** The capture supplied on 13 September contains the post title and text, together with a structured Arabic-language excerpt. Visible rows include names, alphanumeric residential/property identifiers, roles presented as owner, renter or delegate, and phone-like contact values. The author claims to hold personal phone numbers and full residential addresses; the excerpt does not establish the coverage or accuracy of those addresses. No raw personal values are reproduced here.

  **Assumption:** The post title and visible fields make an association with Madinaty owners or residents plausible. They do not attribute the records to Talaat Moustafa Group, the development's management, a service provider or another organisation. A third-party source or misleading description also remains possible.

  **Unknown:** The source organisation, originating system, acquisition method and date, authenticity and currency of the records, number of unique individuals, dataset completeness, the actual proportion published, any unauthorised access and confirmation by an affected organisation are not established. The original forum URL and data file were not provided; analysis is limited to the supplied capture and excerpt.

- **Data visible in the excerpt, minimised:** names, residential/property identifiers, record roles and phone-like contact values. Full addresses and the claimed scope are asserted by the author but have not been independently validated.

- **Observed sample scope:** partial excerpt visible in a supplied capture and text; original archive, source URL, volume, distinct row count and number of people not established. The **0.5%** claim is unverified. No individual record is reproduced in this entry.

- **Risk assessment:** if authentic, combining identity, residence location and contact details could expose people to doxxing, harassment, physical targeting, phishing and fraud. The claim alone does not confirm exfiltration or identify the responsible organisation.

- **Recommendations:**
1. Preserve the capture and collection metadata in a restricted evidence location; avoid further distribution of the excerpt.
2. Identify the organisation or authorised service provider that may hold this type of data before making a public attribution.
3. If the data custodian is established, compare schemas and identifiers against authorised internal records without testing personal phone numbers or extracting further records.
4. Assess physical-safety and fraud risks for potentially affected people and provide appropriate guidance after validation.
5. Monitor for republication without opening download links or engaging in a transaction with the poster.

- **Sources / Evidence:** forum post visible in a capture supplied on 13 September 2026 (displayed post date: 4 September 2026; original URL not provided); [Talaat Moustafa Group public overview of its Egypt projects](https://ecommerce.tmg.com.eg/about).


### 06 September 2026
#### 🇲🇦 Morocco - Centre Atlantique Formation

- **Incident date:** Not established
- **Initial publication date:** 6 September 2026
- **AFRINTEL discovery date:** 9 September 2026
- **Actor / Group:** xNov
- **Sector:** Education / Vocational and professional training
- **Website:** [atlantique.ma](https://atlantique.ma/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3

- **Description:** Centre Atlantique Formation is a Moroccan vocational and professional training organisation offering practical training in several fields through multiple centres. Observed records reference automotive diagnostics, accounting, graphic design, cooking, pastry, hairdressing, fashion design, office computing, welding, plumbing, medical assistance and other vocational courses.

- **Analysis:**

  On 6 September 2026, the threat actor **xNov** published a claim targeting atlantique.ma and distributed an archive associated with Centre Atlantique Formation. A Telegram relay observed on the same date advertised an archive of approximately **2.49 GB** and stated that the published data represented only **27% of the database**. The **73%** remainder is an arithmetic inference from the claimed 27%, not an independent measurement. During direct contact through the Telegram channel, xNov offered the remainder for **USD 300**; the asking price is therefore directly observed as an offer made by the actor. This observation does not confirm the existence, volume or actual availability of the remaining data, and does not evidence a completed transaction.

  After extraction, the analysed archive occupies approximately **4 GB** and contains **1,155 directories comprising 3,465 items**, exactly three items per directory. The structure consists of registration details, certificate metadata and a PDF certificate.

  The details.json files contain registration ID, honorific/title, full name, CIN where recorded, date and place of birth, address and mobile number where populated, training and centre identifiers and registration date. The certificates.json files contain certificate identifiers linked to registrations, name, CIN where recorded, certificate date, year and creation timestamp. One registration may have multiple certificates.

  PDF certificates from distinct directories reproduce information consistent with the JSON records: identity, CIN, birth data, training, year, duration, issue date, certificate number and verification QR code. This correlation provides **strong internal corroboration** that a substantial portion of the published data originated from an operational environment associated with Centre Atlantique Formation.

  The **1,155 directories are learner or registration folders, not automatically 1,155 unique individuals**. CIN-first deduplication, followed by name and date of birth where CIN is absent, is required. Dates of birth indicate adults and apparently minors. Initial access, compromised system, access duration, extent of compromise, complete exfiltration and total volume remain unknown.

- **Observed exposed data:** names, honorifics/titles, CIN numbers, dates and places of birth, addresses and mobile numbers, registration identifiers, training and centre identifiers, registration dates, certificate identifiers and dates, training years, creation timestamps, PDF certificates, certificate numbers and verification QR codes where present.

- **Observed dataset scope:** advertised archive 2.49 GB; extracted volume approximately 4 GB; 1,155 directories; 3,465 items; exactly 3 items per directory; unique-person count not established; 27% claimed as published; remainder estimated at approximately 73% according to the actor, with existence and volume unverified; USD 300 asking price directly observed during contact with xNov.

- **Risk assessment:** the combination of identity data, CIN, birth data, contact information, training records and certificates creates significant risks of identity theft, targeted phishing, document fraud and social engineering. The apparent presence of minors increases safeguarding implications. No reviewed element establishes ransomware, destruction or operational interruption.

- **Recommendations:**
1. Identify the source application, database, storage or backup and preserve logs.
2. Review authentication, privileged accounts, exposed administration, APIs, database credentials and third-party access.
3. Rotate potentially exposed passwords, API keys and secrets.
4. Deduplicate affected persons using CIN and secondary attributes.
5. Identify potentially affected minors separately and apply protective measures.
6. Monitor xNov and related underground channels for the claimed remainder.
7. Monitor phishing, impersonation, document fraud and fraudulent certificate use.
8. Audit certificate validation for enumeration through QR codes or identifiers.

- **Sources / Evidence:** xNov underground forum publication (6 September 2026); supplied Telegram relay and capture (6 September 2026); direct contact with xNov through the Telegram channel regarding the asking price; AFRINTEL analysis of the published archive and extracted learner/certificate folders.


### 09 September 2026
#### 🇪🇬 Egypt - Badr University in Cairo (BUC)

- **Incident date:** Not established
- **Initial publication date:** 9 September 2026 at 16:50 (timezone not specified)
- **AFRINTEL discovery date:** 12 September 2026
- **Actor / Group:** Unknown
- **Displayed author account:** elmo7areb (identity and role unverified)
- **Sector:** Education / Higher education
- **Website:** [buc.edu.eg](https://buc.edu.eg/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:** Badr University in Cairo (BUC) is an Egyptian higher education institution located in Badr City. Its official website presents its programmes and services, including admissions processes and a student portal.

- **Analysis:**

  A post attributed to the **elmo7areb** account, dated 9 September 2026 at 16:50 (timezone not specified), claims a full extraction of BUC's database. The author says the data concerns students and their families, citing national identifiers, addresses and phone numbers. A visible excerpt contains values presented as email-like identifiers, but these fields are incomplete: segments, including the part after the '@' sign, are replaced with `****`. The associated strings presented as passwords are also partially obscured with `****`. No values are reproduced or tested. The original sample file was unavailable; analysis is limited to material visible in the supplied screenshot.

  **Observed:** the existence of a post claiming an extraction, its displayed timestamp, the data categories mentioned by the author, and an excerpt of login rows in which email-like identifiers are incomplete, with the domain obscured by `****`, and strings presented as passwords also contain segments replaced by `****`.

  **Assumption:** BUC's identity and the subdomain's consistency with its admissions services make the target plausible. They do not validate the data's authenticity or provenance, successful extraction, or database completeness. The post describes the sample as encrypted administrative logs, while the visible portion resembles login identifier and password pairs; this inconsistency cannot be resolved from the screenshot.

  **Unknown:** number of records or people affected, validity or currency of the credentials, contents and completeness of the dataset, initial access vector, affected systems, incident scope, operational impact, and confirmation by BUC or an authority.

- **Data visible in the excerpt:** rows presented as login entries, with incomplete email-like identifiers (the domain is replaced by `****`) and strings presented as passwords that are also partially obscured with `****`, plus an admissions portal URL. The full original values are not visible; their authenticity, currency and uniqueness cannot be established.

- **Observed sample scope:** a screenshot of a post and part of a text excerpt; original source file unavailable; total volume, row count and number of people not established. No individual data or secret is reproduced in this record.

- **Risk assessment:** if authentic, the claimed exposure of credentials, identity data and contact details could enable account takeover, targeted phishing, identity fraud and social engineering against students or their families. The excerpt does not demonstrate that the credentials work or that any account was compromised.

- **Recommendations:**
1. Preserve admissions portal, authentication, database and administrative-system logs covering the relevant period.
2. Investigate unusual access, bulk queries or exports, compromised privileged accounts and configuration changes.
3. Assess potentially affected accounts; reset exposed credentials and revoke sessions where justified by the investigation.
4. Establish the actual data scope and follow applicable notification and protection procedures.
5. Do not test the disclosed credentials; monitor for login attempts and phishing targeting students and their families.

- **Sources / Evidence:** forum post visible in a screenshot supplied on 12 September 2026 (original URL not provided); [BUC official website](https://buc.edu.eg/); [BUC official admissions page](https://buc.edu.eg/buc-admission-application-form/).

### 12 September 2026
#### 🇦🇴 Angola - SEPE: Angola's E-Government Platform

- **Incident date:** Not established
- **Initial publication date:** 12 September 2026 at 18:23 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 22 September 2026 (supplied screenshot and local sample)
- **Actor / Group:** Kazu (displayed account; identity and affiliation unverified)
- **Sector:** Government / Digital public services
- **Website:** [sepe.gov.ao](https://www.sepe.gov.ao/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4

- **Description:** A post attributed to the Kazu account targets SEPE, Angola's official electronic public-services platform, and claims a data exposure in a ransomware-extortion context. AFRINTEL examined a local sample derived from the publication; this strengthens structural consistency and association with Angolan administrative data, but does not confirm initial access, complete exfiltration, the claimed overall volume or official confirmation by SEPE.

- **Analysis:**

  **Observed:** The post displayed on 12 September 2026 claims **364,841 files**, **110,021 users with personal data**, a claimed size of **179 GB**, a **USD 100,000** demand and a deadline displayed as **27 September 2026**. These figures remain actor claims. The supplied local sample contains **1,189 files** totalling **544,921,521 bytes**: 1,030 PDFs, 111 JSON files, 26 JPGs, 8 JPEGs, 7 PNGs, 4 DOCX files, 2 PPTX files and 1 file without an extension; 15 files are empty. All 111 JSON files expose a `formData` structure with identity, national-document, name, email, phone, address, birth, nationality, residence, municipality, province, employment and training-type fields. No individual content is reproduced in this record.

  **Assumption:** The `sepe.gov.ao` domain, logo and platform description make an Angolan public-service target plausible. The consistency between documentary filenames and the JSON schema is compatible with administrative or application records. It does not prove that SEPE held all files, that the actor gained access through an intrusion, or that 179 GB or 110,021 users are real.

  **Unknown:** initial access vector, affected systems, compromise date, number of unique individuals, actual coverage, completeness, current document validity, full disclosure, ransom payment, confirmation by SEPE or an authority, and the deadline state after the last check remain unknown.

- **Observed sample scope:** 1,189 local files; 544,921,521 bytes; 111 JSON structures inspected; documents and personal data not transcribed. The sample manifest fingerprint is retained locally at `/tmp/afrintel-evidence/afr-2026-09-sepe/evidence_manifest.json`. The sample is not the full dump and cannot establish a unique-person count.

- **Risk assessment:** if the claims are accurate, exposure of identity documents, contact details, education records and other administrative documents could facilitate identity fraud, targeted phishing, document fraud and harm to public-service users. AFRINTEL publishes no secret, identifier or individual document.

- **Recommendations:**
1. Preserve SEPE, IAM, API, document-storage and database logs covering the relevant period.
2. Investigate bulk exports, privileged accounts, anomalous access and configuration changes.
3. Revoke sessions and rotate secrets only as justified by the investigation; do not test sample data.
4. Identify affected data categories and prepare appropriate notification and protection measures.
5. Verify public-service integrity and monitor phishing, impersonation and document fraud.
6. Track the deadline and any later publication without opening criminal links or negotiating with the actor.

- **Sources / Evidence:** Kazu post screenshot supplied on 22 September 2026; local sample supplied and analysed read-only; [SEPE portal](https://www.sepe.gov.ao/).

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-12T18:23:00
listing_last_observed_at: 2026-09-22T18:23:00
sample_status: sample-reviewed
deadline_at: 2026-09-27
deadline_status: active
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-22T18:23:00
-->

### 19 September 2026
#### 🇿🇦 South Africa - Apollo 21

- **Initial publication date:** 19 September 2026 (date displayed in the BLACKLOCKS list; time and timezone not specified)
- **AFRINTEL discovery date:** 28 September 2026 (local screenshots and images reviewed)
- **Actor / Group:** BLACKLOCKS
- **Sector:** Spare-parts distribution / Road transport
- **Website:** [apollo21.co.za](https://apollo21.co.za/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Subtype:** Data exfiltration claimed; encryption unestablished
- **Confidence level:** High (listing and documentary link to Apollo 21; compromise and total volume unconfirmed)
- **Impact level:** Level 3

- **Description:** The Apollo 21 entry appears in a BLACKLOCKS victim list with the date **19 September 2026**. Another view of the entry associates `apollo21.co.za` with South Africa and claims **400 GB** of data. The reviewed sample images include commercial and financial tables and identity documents. They support a documentary link to Apollo 21 without confirming the acquisition method, encryption, or possession of 400 GB.

- **Analysis:**

  **Observed:** The supplied list has three visible entries: a South Korean organisation dated **1 September**, Apollo 21 dated **19 September**, and ARCA Unlimited Architects in South Africa dated **22 September 2026**. These are displayed publication dates; they establish neither the group's definitive start date nor the dates of intrusion. The detailed Apollo 21 entry claims **400 GB** without providing the corresponding corpus. AFRINTEL reviewed **14 local images** totalling **3,518,628 bytes**: two views of the listing and **12 sample images**. The samples show debtor-account and deposit lists, a credit application, sales, stock, supply and shipment tables, and **three images of identity documents**. Several documents name Apollo 21 or its trading name and carry a BLACKLOCKS watermark. Contact details, amounts and personal identifiers are visible but are not reproduced.

  **Assumption:** Consistency between the posted domain, the business described on the [official Apollo 21 website](https://apollo21.co.za/about-apollo21/) and the commercial documents supports high confidence in the sample's association with the company. The watermark establishes how the actor presents the material, not its technical provenance. The identity documents alone cannot establish the individuals' roles or the total number of people exposed.

  **Unknown:** the date and vector of access, affected systems, exact origin of each document, actual possession and publication of the claimed **400 GB**, number of people affected, encryption, operational effects, confirmation by Apollo 21 or an authority, any negotiation, payment or resale remain unknown.

- **Analysis scope:** all 14 images were reviewed read-only; no native spreadsheet or document files and no 400 GB corpus were provided. The analysis establishes visible categories, not completeness or independent authenticity of every item. Hashes and file sizes are recorded in a local manifest outside the repository at `/tmp/afrintel-evidence/AFR-2026-TBD-apollo21/`.

- **Risk assessment:** the visible identity documents and contact data present risks of identity misuse and document fraud; commercial, financial and partner information could facilitate targeted phishing, payment fraud and social engineering. These images do not establish any operational effects.

- **Sources / Evidence:** BLACKLOCKS list and entry supplied as screenshots; twelve sample images supplied locally; [official Apollo 21 website](https://apollo21.co.za/). No individual document, personal identifier or criminal-site link is published.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-28
listing_last_observed_at: 2026-09-28
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-28
-->

### 21 September 2026
#### 🇳🇬 Nigeria - Federal Capital Territory Internal Revenue Service (FCT-IRS)

- **Initial publication date:** 21 September 2026 at 13:03 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 28 September 2026 (screenshot and PDF supplied)
- **Actor / Group:** individual (displayed account; identity unverified)
- **Sector:** Government / Tax administration
- **Website:** [fctirs.gov.ng](https://fctirs.gov.ng/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High (post and sample association with FCT-IRS; technical origin unestablished)
- **Impact level:** Level 3

- **Description:** A post titled “Nigerian Tax Authority | Full Breach” displays the **Federal Capital Territory Internal Revenue Service (FCT-IRS)** logo and references images of people and signatures. The supplied PDF, exported from JustPaste.it, contains **314 pages** of text and personal data. “Full Breach” is the author's claim in the post title; data completeness and a compromise of FCT-IRS systems are not established.

- **Analysis:**

  **Observed:** The screenshot shows a post attributed to the **individual** account, dated **21 September 2026 at 13:03** according to the displayed timestamp. Its visual content identifies FCT-IRS. The **1,284,983-byte** PDF was processed read-only; metadata reports 314 pages and creation by HeadlessChrome on 28 September 2026, which dates the local PDF export, not the post or incident. Full text extraction yielded **742,955 characters** across **12,541 lines**. Automated detection found **2,541 email-format occurrences**, including **2,540 distinct values**, and **61 occurrences** matching the Nigerian phone-number pattern used. These occurrences are not validated records or unique people. The screenshot also shows thumbnails of portraits and signatures. No individual value is reproduced.

  **Assumption:** The FCT-IRS logo, tax context and consistency with the official [Federal Capital Territory Internal Revenue Service website](https://fctirs.gov.ng/) make an association with FCT-IRS plausible. The generic “Nigerian Tax Authority” title is insufficient to attribute the case to the national Nigeria Revenue Service; this record identifies the tax service for the Federal Capital Territory.

  **Unknown:** the pre-export source file, exact record structure and deduplication, provenance of the images and contact data, originating organisation or system, vector and date of any access, full data scope, data validity, official confirmation and operational effects remain unknown. The claim of a complete breach is not corroborated.

- **Analysis scope:** text extraction covered all 314 pages, with visual review of the screenshot; analysis is limited to this PDF and the displayed post. Reflowed layout prevents a reliable count of records or people. No extracted text or raw personal data is retained in the repository. Metadata and aggregate statistics are kept outside the repository at `/tmp/afrintel-evidence/AFR-2026-TBD-fctirs/`.

- **Risk assessment:** exposure of contact and identifying information could facilitate targeted phishing, identity misuse, fraud and social engineering. The reviewed sample does not establish exposure of detailed tax or financial data.

- **Sources / Evidence:** forum-post screenshot supplied on 28 September 2026; local JustPaste.it PDF reviewed read-only; [official FCT-IRS website](https://fctirs.gov.ng/). No personal data or criminal-site link is published.

### 22 September 2026
#### 🇿🇦 South Africa - ARCA Unlimited Architects

- **Initial publication date:** 22 September 2026 (date displayed in the BLACKLOCKS list; time and timezone not specified)
- **AFRINTEL discovery date:** 28 September 2026 (local screenshots and samples reviewed)
- **Actor / Group:** BLACKLOCKS
- **Sector:** Architecture / Design and project management
- **Website:** [arcaunlimited.com](https://arcaunlimited.com/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Subtype:** Data exfiltration claimed; encryption unestablished
- **Confidence level:** High (listing and documentary link to ARCA; acquisition and total volume unconfirmed)
- **Impact level:** Level 3

- **Description:** BLACKLOCKS lists ARCA Unlimited Architects as a South African victim and displays a volume of **400G** without defining the unit. Sample images include architectural drawings, project documents and cost tables. Several items carry ARCA's name or branding and are consistent with its business. The review confirms neither the acquisition method, encryption, nor possession of the claimed volume.

- **Analysis:**

  **Observed:** The previously supplied BLACKLOCKS list dates the ARCA entry to **22 September 2026**; the detailed entry associates `arcaunlimited.com` with South Africa and states **“DATA SIZE: 400G”**. AFRINTEL reviewed **18 local images** read-only, totalling **3,737,321 bytes**: the detailed listing and **17 sample images**. These show plans, sections and elevations, a design report dated September 2026, a building-plan approval application, an energy-compliance worksheet, project-cost tables and an identity document. Some recent documents bear ARCA branding and its domain; other plans concern third parties or historical projects. Names, identifiers, contact details and building details are visible but are not reproduced.

  **Assumption:** Consistency between the posted domain, [ARCA's official website](https://arcaunlimited.com/who-are-we.asp), the design documents and ARCA branding supports high confidence in the documentary link to the company. The presence of plans relating to clients, including an electricity-sector operator, does not establish a separate incident at those clients. The BLACKLOCKS watermark does not demonstrate the files' technical provenance.

  **Unknown:** the date and vector of access, affected systems, provenance of each drawing, any prior distribution rights, actual amount of data held or published, exact unit of “400G”, number of people affected, any encryption or operational impact, confirmation by ARCA or an authority, any negotiation, payment or resale remain unknown.

- **Analysis scope:** 18 images reviewed; no native CAD, document or spreadsheet source files and no corpus matching the claimed volume were supplied. The sample demonstrates the range of visible material, not its completeness or the independent authenticity of every document. An aggregate SHA-256 manifest is retained outside the repository at `/tmp/afrintel-evidence/AFR-2026-TBD-arcaunlimited/`.

- **Risk assessment:** possible exposure of detailed drawings, project documents, cost information and an identity document could facilitate document fraud, targeted phishing, social engineering and disclosure of client-site details. The sensitivity of some plans warrants particular attention without concluding that any named third-party organisation was compromised.

- **Sources / Evidence:** BLACKLOCKS list and ARCA entry supplied as screenshots; 17 local sample images; [official ARCA Unlimited website](https://arcaunlimited.com/). No drawing, site detail, personal identifier or criminal-site link is published.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-28
listing_last_observed_at: 2026-09-28
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-28
-->

#### 🇲🇱 Mali - AFRICA-TECH

- **Initial publication date:** 22 September 2026 (reported date; time not specified)
- **Data disclosure date:** 25 September 2026 at 16:00 GMT (UTC), according to the supplied collection information
- **Actor / Group:** N0n
- **Sector:** Technology / IT services / Document processing
- **Website:** Not identified
- **Proposed domain:** [africatech-mali.com](https://www.africatech-mali.com/) (attribution to the victim not established)
- **Status:** Data Fully Published
- **Incident type:** Ransomware
- **Subtype:** Claimed double extortion; released data reviewed
- **Confidence level:** High
- **Impact level:** Level 3

- **Description:** AFRICA-TECH is presented in N0n's publication as a Malian IT-services and document-processing company. All files released by the group were supplied for analysis. A Word complaint names AFRICA-TECH and contains references to Mali and Bamako, supporting a documentary link to the organisation. The proposed domain, https://www.africatech-mali.com/, advertises solar and electrical activities in Bamako. Comparison with the documents established no shared contact details; attribution to the victim remains unestablished.

- **Analysis:**

  **Observed:** N0n's victim listing displayed a deadline of **25 September 2026 at 16:00 UTC**. According to the supplied collection information, the group released all files at **16:00 GMT**, meeting that deadline, and the supplied directory corresponds to the entire publication. The local review of **26 September 2026** covers **10 files with distinct SHA-256 hashes**, totalling **2,413,673 bytes**: **6 PDFs containing 39 pages**, **2 Word documents**, **1 text file** and **1 temporary Word file of 162 bytes**, unusable as a document. The bank statement accounts for **31 pages**. Document texts were extracted and all **39 PDF pages** and the **4 embedded images** in the Word document were processed through OCR. Contents include banking documents, a complaint involving money-transfer services, a service offer, a travel ticket, a document related to a visa process and travel insurance. The complaint contains **2 occurrences** of AFRICA-TECH. References to Ecobank and Sanlam describe the documents; they do not constitute separate incidents affecting those organisations.

  **Assumption:** The range of documents, references to Mali and Bamako and AFRICA-TECH's name are consistent with document retention in a document-services business. These elements support high confidence in the documentary link to AFRICA-TECH. They do not prove how the files were acquired. The README repeats claims of client-document encryption and destruction of backups and shadow copies; the reviewed batch contains no technical evidence of those actions.

  **Unknown:** the compromise date and vector, affected systems, business authenticity of every document, total volume potentially extracted before publication, operational effects, actual encryption, access to backups, negotiation, ransom payment or resale, and confirmation by AFRICA-TECH or an authority remain unknown. Completeness of the published batch, as reported during collection, does not establish completeness of all data potentially held by the group.

- **Data observed in the publication:** identity, birth, passport, contact and travel information; banking information and financial transactions; insurance documents and professional correspondence. Documentary year markers include **2021, 2023, 2025 and 2026**; they do not date the intrusion. No count of distinct people or transactions is established.

- **Analysis limitations:** OCR uses the English model and may misread French text, tables and graphical elements. All 4 Word images were processed, but only 2 yielded nonempty, very short text. Every field was not visually validated. Format and content consistency is neither authentication of every document nor official confirmation of the incident. Published findings are aggregated; no raw personal data is reproduced.

- **Risk assessment:** the released data categories could facilitate targeted phishing, identity theft, document fraud and payment pretexts. Impact is assessed at Level 3 given the observed personal and financial information. Service interruption or restoration difficulties are not established by the reviewed files.

- **Sources / Evidence:** N0n victim listing and deadline supplied for 22 September 2026; local directory supplied as all files released by N0n on 25 September 2026 at 16:00 GMT; local review of 26 September 2026 and SHA-256 manifest retained outside the repository. Provenance and disclosure time are documented through the supplied collection information; no independent visit to the group's site was performed for this update.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-22
listing_last_observed_at: 2026-09-22
sample_status: sample-reviewed
deadline_at: 2026-09-25T16:00:00Z
deadline_status: expired
disclosure_status: release-reviewed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-27
-->

### 24 September 2026
#### 🇰🇪 Kenya - TikoHUB

- **Incident date:** 28 April 2026 (date of the access-offer post; initial compromise not established)
- **Initial publication date:** 28 April 2026 at 23:26 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 24 September 2026 (supplied screenshot)
- **Actor / Group:** DarkMafiaX (displayed account; identity and affiliation unverified)
- **Sector:** Ticketing / Events / Digital services
- **Website:** [tikohub.co.ke](https://www.tikohub.co.ke/)
- **Status:** Claim - Unverified
- **Incident type:** Access Sale
- **Confidence level:** Medium
- **Impact level:** Level 4

- **Description:** A post attributed to the DarkMafiaX account offers administrator access presented as related to TikoHUB, a Kenyan ticketing and event-management platform. The post and displayed credentials were not tested; AFRINTEL does not confirm their validity, effective access or a compromise of TikoHUB.

- **Analysis:**

  **Observed:** The screenshot shows a post titled “Admin Access To Tikohub.co.ke | Kenya”, dated 28 April 2026 at 23:26 according to the displayed timestamp. It contains an administrative-resource URL and fields presented as a username and password. These values are deliberately not reproduced and were not tested. The screenshot was supplied to AFRINTEL on 24 September 2026.

  **Assumption:** The `tikohub.co.ke` domain corresponds to a Kenyan ticketing platform, making the target plausible. The post could nevertheless be inaccurate, recycled, falsified or related to limited access to a third-party component. 28 April is the observed post date, not necessarily the initial compromise date.

  **Unknown:** current credential validity, actual privileges, affected system, acquisition method, access duration, effective exploitation, accessed or exfiltrated data, confirmation by TikoHUB and remediation status remain unknown.

- **Observed sample scope:** one screenshot of a forum post; no login, credential validation, download, endpoint interaction or secret copying was performed.

- **Risk assessment:** if authentic, administrator access could enable content modification, access to customer or organiser data, ticket fraud and account compromise. This record does not confirm any of these effects.

- **Recommendations:**
1. Preserve authentication, administration, API and hosting logs from 28 April 2026 onward.
2. Reset potentially affected administrator accounts and revoke sessions as justified by TikoHUB's defensive investigation.
3. Review privilege changes, exports, account creation and ticket or event modifications.
4. Do not test the disclosed credentials or open the sensitive URL shown in the screenshot.
5. Monitor impersonation, ticket fraud and secret reuse.

- **Sources / Evidence:** screenshot supplied to AFRINTEL on 24 September 2026; public [TikoHUB website](https://www.tikohub.co.ke/).

### 25 September 2026
#### 🇲🇦 Morocco - Pharma 5

- **Initial publication date:** 25 September 2026 at 08:27 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 28 September 2026 (local images reviewed)
- **Actor / Group:** INC Ransom
- **Sector:** Healthcare / Pharmaceutical industry
- **Website:** [pharma5.ma](https://www.pharma5.ma/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Subtype:** Data exfiltration claimed
- **Confidence level:** High (existence of the listing and consistency of the visible sample; scope and acquisition unestablished)
- **Impact level:** Level 3

- **Description:** INC Ransom published a listing naming Pharma 5 and claims to hold **50 GB** of data. The listing includes a gallery of document previews; one quality-management page was also provided at readable size. The visible material is consistent with pharmaceutical activities and a supply chain. This consistency does not confirm an intrusion, the acquisition method, or the claimed 50 GB.

- **Analysis:**

  **Observed:** The publication dated **25 September 2026** associates `pharma5.ma` with INC Ransom and displays **50 Gb** (recorded here as **approximately 50 GB claimed**). It claims corporate and financial information, product and supply-chain data, quality control and certification material, drug-testing information, and employee and partner data. The gallery contains several document and table previews, including material related to products and activity tracking; their detailed content is not readable enough to confirm every claimed category. One **distinct, readable page** of a Pharma 5 quality-department specifications document concerns **salicylamide**. It identifies client, supplier and manufacturer roles, as well as contact fields. Two images depict the same page, one partly redacted; they are not two independent documents. The document indicates “page 1/5”; the other four pages and the source files were not provided.

  **Assumption:** The document structure and references to Pharma 5, salicylamide and supply-chain roles strengthen its documentary link to the organisation. The other previews suggest varied documents, without allowing verification of the underlying files or the claimed volumes.

  **Unknown:** the date and vector of access, affected systems, independent authenticity of the document, acquisition method, volume actually obtained or published, number of people affected, encryption, any business interruption, confirmation by Pharma 5 or an authority, any negotiation, payment or resale remain unknown.

- **Analysis scope:** four local images reviewed in read-only mode: two versions of the same listing with a preview gallery, and two versions of the same document page. Thumbnails are not treated as complete reviewed files. Analysis was limited to visible data; neither the complete source document nor the claimed dataset was available. Individual names and contact details are not reproduced.

- **Risk assessment:** if the other claimed data was indeed exposed, personal and professional information could facilitate spear-phishing, payment fraud or BEC, social engineering and targeting of supply-chain partners. The impact level reflects the sensitivity of the pharmaceutical context and visible contact fields without validating the extent of the leak.

- **Sources / Evidence:** INC Ransom listing and sample images supplied locally; visual review and SHA-256 manifest retained outside the repository at `/tmp/afrintel-evidence/AFR-2026-TBD-pharma5/`; [public Pharma 5 document](https://www.pharma5.ma/wp-content/uploads/presse/communique/CP-PHARMA5-VF-17-NOVEMBRE-2020.pdf) linking the domain to the organisation. No raw personal data or criminal-site address is published.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-28
listing_last_observed_at: 2026-09-28
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-28
-->

## Inter-month follow-up note

This note is not a new record and is excluded from the September incident count.

The [June 2026 Ministry of Education of Libya record](../../06-june/victims.md) documents a publication attributed to **EvaN47**, with a claimed volume of **287 GB**. A visual sample was examined at that time: a document gallery, secondary-education certificates, school and administrative documents, scanned images and PDFs, with references to national numbers, personal photographs and passport images. The analysis covered visible material; the claimed total volume and database completeness were not validated.

The **10 September 2026** publication, attributed to **EveN47**, subsequently claims **800 GB** for the moe.gov.ly database and approximately **300 GB** of similar data covering several Libyan education ministries. A local sample supplied as originating from this publication was nevertheless analysed in read-only mode: **900,976,395 bytes** (approximately **901 MB**), comprising **3,900 files** across four directories corresponding to passports (**1,145** files), national numbers (**467**), student photographs (**1,146**) and student certificates (**1,142**). Signatures identify 3,500 valid JPEGs and 4 valid PNGs; five files carrying a `.jpg` extension are actually PDFs and two others are HTML documents. The aggregate tree SHA-256 fingerprint is `d63371c3d61dd48c87398578d1bdfe4329c7dca1bc73104125e966221591df80`. SHA-256 checking found **169 duplicate groups** representing **213 excess files**, so the sample cannot be used to infer a unique count of people or documents. No bulk OCR or transcription of individual content was performed to limit exposure of personal data; the analysis covers the directory structure, signatures, technical metadata and integrity checks. This structure strengthens internal corroboration of the dataset's documentary and education-related nature, without validating the 287 GB, 800 GB or 300 GB claims. No download link was opened and no raw personal data is reproduced here. It is not established whether this represents an extension, republication, revised volume claim or a publication by a different alias. The 287 GB, 800 GB and 300 GB figures must not be added together; they remain separate dated threat-actor claims.
