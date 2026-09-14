![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in September 2026 (3 records)

👉🏾 [**Version française disponible ici**](./victims_FR.md)

## September 2026

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

## Inter-month follow-up note

This note is not a new record and is excluded from the September incident count.

The [June 2026 Ministry of Education of Libya record](../../06-june/victims.md) documents a publication attributed to **EvaN47**, with a claimed volume of **287 GB**. A visual sample was examined at that time: a document gallery, secondary-education certificates, school and administrative documents, scanned images and PDFs, with references to national numbers, personal photographs and passport images. The analysis covered visible material; the claimed total volume and database completeness were not validated.

The **10 September 2026** publication, attributed to **EveN47**, subsequently claims **800 GB** for the moe.gov.ly database and approximately **300 GB** of similar data covering several Libyan education ministries. A local sample supplied as originating from this publication was nevertheless analysed in read-only mode: **900,976,395 bytes** (approximately **901 MB**), comprising **3,900 files** across four directories corresponding to passports (**1,145** files), national numbers (**467**), student photographs (**1,146**) and student certificates (**1,142**). Signatures identify 3,500 valid JPEGs and 4 valid PNGs; five files carrying a `.jpg` extension are actually PDFs and two others are HTML documents. The aggregate tree SHA-256 fingerprint is `d63371c3d61dd48c87398578d1bdfe4329c7dca1bc73104125e966221591df80`. SHA-256 checking found **169 duplicate groups** representing **213 excess files**, so the sample cannot be used to infer a unique count of people or documents. No bulk OCR or transcription of individual content was performed to limit exposure of personal data; the analysis covers the directory structure, signatures, technical metadata and integrity checks. This structure strengthens internal corroboration of the dataset's documentary and education-related nature, without validating the 287 GB, 800 GB or 300 GB claims. No download link was opened and no raw personal data is reproduced here. It is not established whether this represents an extension, republication, revised volume claim or a publication by a different alias. The 287 GB, 800 GB and 300 GB figures must not be added together; they remain separate dated threat-actor claims.
