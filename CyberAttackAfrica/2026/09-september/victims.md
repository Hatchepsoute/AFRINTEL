![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in September 2026 (41 records)

👉🏾 [**Version française disponible ici**](./victims_FR.md)

## September 2026

**Monthly follow-up status: In Progress** - corpus of 41 records; additional late discoveries may still be added.

> **OSINT verification update — 18 October 2026.** These 41 entries form a **September tracking/intake corpus**, not 41 cyberattacks occurring in September. **13 entries** document incidents confirmed or corroborated at the named organisation (including RelyComply and Namibia’s defence ministry), **2 entries** concern acknowledged indirect third-party data exposure (Hollard and Guardrisk: direct victim-system intrusion unestablished), and **26** remain claims or samples without independent confirmation. Statuses distinguish incident confirmation, group attribution, claimed volume, encryption and exfiltration. Absence of public confirmation means none was found in the reviewed sources as of this date; it is not proof no incident occurred.


### 03 September 2026
#### 🇳🇬 Nigeria - Medical and Dental Council of Nigeria (MDCN)

- **Initial publication date:** 3 September 2026 at 20:19 (displayed time; timezone not specified)
- **Actor / Group:** cattier (displayed forum account; identity unverified)
- **Sector:** Healthcare / Medical and dental professional regulation
- **Website:** [mdcn.gov.ng](https://www.mdcn.gov.ng/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium (structured post and excerpt observed; origin and scope uncorroborated)
- **Impact level:** Level 3

- **Description:** The **Medical and Dental Council of Nigeria (MDCN)** is Nigeria's statutory regulator for medical and dental practice. Its responsibilities include setting professional standards, maintaining registers of practitioners, and managing registration and licensing. Its services therefore handle practitioners' identity, qualifications and professional registration information ([MDCN official responsibilities](https://mdcn.gov.ng/page/about-us/our-role)).

- **Independent verification as of 18 October 2026:** No MDCN statement or regulatory notice corroborating unauthorised access or the claimed 65,580 affected individuals was found. AFRINTEL’s screenshot and 50-row review substantiate the presentation of data, not a technical compromise of MDCN.

  **Incident context already documented in AFRINTEL :** An account named cattier posted an offer titled “Medical and Dental Council of Nigeria 65K” and attributes data on **65,580 unique users** to `mdcn.gov.ng`. A sample of healthcare-practitioner records is visible, and **50 rows were supplied as text**. This establishes the existence of the post and the type of data presented; it does not confirm that 65,580 distinct people are affected or that MDCN systems were intruded upon.

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

- **Description:** **Madinaty** is a large planned residential community east of Cairo, developed by **Talaat Moustafa Group (TMG)**, with housing, infrastructure and local amenities. This entry concerns a **residential community**, not a confirmed breached legal entity: the post does not establish whether the developer, a property manager or a third-party supplier held the alleged data ([TMG project overview](https://ecommerce.tmg.com.eg/about)).

- **Independent verification as of 18 October 2026:** No independently verified intrusion or reliable identification of the original data controller was found. The claimed Madinaty link does not establish a breach of Talaat Moustafa Group.

  **Incident context already documented in AFRINTEL :** Madinaty is a residential urban development in Egypt that Talaat Moustafa Group presents among its projects in the country. This establishes geographic context; it does not identify the organisation that collected or held the data, or confirm that Talaat Moustafa Group was compromised. ([Talaat Moustafa Group overview](https://ecommerce.tmg.com.eg/about))

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
- **Actor / Group:** xNov
- **Sector:** Education / Vocational and professional training
- **Website:** [atlantique.ma](https://atlantique.ma/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3

- **Description:** **Centre Atlantique Formation** is a Moroccan network of private, practical vocational-training centres serving learners, jobseekers and professionals. Its courses cover technical trades, services, administration and other practical specialisms across multiple Moroccan cities. Such operations involve enrolment workflows and the issuance of training certificates ([official website](https://atlantique.ma/)).

- **Independent verification as of 18 October 2026:** No public Centre Atlantique Formation statement or regulatory notice confirming an attack vector was found. AFRINTEL’s internal documentary analysis of the archive (1,155 folders) remains available corroboration, separate from official acknowledgement.

  **Incident context already documented in AFRINTEL :** Centre Atlantique Formation is a Moroccan vocational and professional training organisation offering practical training in several fields through multiple centres. Observed records reference automotive diagnostics, accounting, graphic design, cooking, pastry, hairdressing, fashion design, office computing, welding, plumbing, medical assistance and other vocational courses.

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
- **Actor / Group:** Unknown
- **Displayed author account:** elmo7areb (identity and role unverified)
- **Sector:** Education / Higher education
- **Website:** [buc.edu.eg](https://buc.edu.eg/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:** **Badr University in Cairo (BUC)** is an Egyptian university based in Badr City within Greater Cairo. It offers degree programmes across scientific, creative and humanities disciplines and operates digital admissions and student services. This provides organisational context for possible student and administrative records, without establishing any system breach ([BUC official website](https://buc.edu.eg/new-undergraduate/)).

- **Independent verification as of 18 October 2026:** Secondary OSINT articles repeat the claim but no public Badr University in Cairo acknowledgement or external proof of a full database extraction was found. Partially redacted credentials in the screenshot do not establish valid access.

- **Additional verification sources:** [Source 1](https://undercodenews.com/badr-university-in-cairo-reportedly-targeted-in-a-dark-web-data-leak-claim-video/)

  **Incident context already documented in AFRINTEL :** Badr University in Cairo (BUC) is an Egyptian higher education institution located in Badr City. Its official website presents its programmes and services, including admissions processes and a student portal.

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
- **Actor / Group:** Kazu (displayed account; identity and affiliation unverified)
- **Sector:** Government / Digital public services
- **Website:** [sepe.gov.ao](https://www.sepe.gov.ao/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4

- **Description:** **SEPE** (*Serviços Públicos Electrónicos*) is Angola's government gateway to online public services. Its catalogue spans identity, family, business, tax and other administrative procedures that may require personal supporting documents. As a service gateway, SEPE is not necessarily the direct host of every record described in a criminal claim ([official SEPE portal](https://sepe.gov.ao/)).

- **Independent verification as of 18 October 2026:** Angolan media revisited Kazu’s allegation in October, finding no independent confirmation and reporting that the SEPE portal remained reachable. Availability alone cannot rule out exfiltration. Neither the claimed 179 GB nor an intrusion, encryption or direct SEPE compromise has been independently established; AFRINTEL’s sample review remains partial documentary evidence.

- **Additional verification sources:** [Source 1](https://pti.ao/sepe-falta-de-evidencias-coloca-em-causa-suposto-ataque-cibernetico/) ; [Source 2](https://pti.ao/sepe-mantem-servicos-online-e-acessiveis-ao-publico/)

  **Incident context already documented in AFRINTEL :** A post attributed to the Kazu account targets SEPE, Angola's official electronic public-services platform, and claims a data exposure in a ransomware-extortion context. AFRINTEL examined a local sample derived from the publication; this strengthens structural consistency and association with Angolan administrative data, but does not confirm initial access, complete exfiltration, the claimed overall volume or official confirmation by SEPE.

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
- **Actor / Group:** BLACKLOCKS
- **Sector:** Spare-parts distribution / Road transport
- **Website:** [apollo21.co.za](https://apollo21.co.za/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Subtype:** Data exfiltration claimed; encryption unestablished
- **Confidence level:** High (listing and documentary link to Apollo 21; compromise and total volume unconfirmed)
- **Impact level:** Level 3

- **Description:** **Apollo 21** is a South African business established in 1972 specialising in importing and distributing replacement parts for trucks, buses and trailers. It supplies mechanical, electrical and body components to transport operators and commercial-vehicle maintenance businesses. Its operations depend on supplier relationships, inventory and commercial records ([Apollo 21 official website](https://apollo21.co.za/home/)).

- **Independent verification as of 18 October 2026:** The BLACKLOCKS listing and sample images were observed, but no public Apollo 21 acknowledgement or independent source establishing unauthorised access, encryption or 400 GB exfiltration was found.

  **Incident context already documented in AFRINTEL :** The Apollo 21 entry appears in a BLACKLOCKS victim list with the date **19 September 2026**. Another view of the entry associates `apollo21.co.za` with South Africa and claims **400 GB** of data. The reviewed sample images include commercial and financial tables and identity documents. They support a documentary link to Apollo 21 without confirming the acquisition method, encryption, or possession of 400 GB.

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
- **Actor / Group:** individual (displayed account; identity unverified)
- **Sector:** Government / Tax administration
- **Website:** [fctirs.gov.ng](https://fctirs.gov.ng/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High (post and sample association with FCT-IRS; technical origin unestablished)
- **Impact level:** Level 3

- **Description:** The **Federal Capital Territory Internal Revenue Service (FCT-IRS)** administers internally generated tax revenue in Nigeria's **Federal Capital Territory, Abuja**. Established by legislation in 2015, it assesses, collects and accounts for local taxes and levies, including personal income tax within its jurisdiction. It should not be confused with the nationwide federal revenue authority ([FCT-IRS official overview](https://fctirs.gov.ng/about-us/)).

- **Independent verification as of 18 October 2026:** No FCT-IRS statement, regulator filing or independent investigation confirming an intrusion was located. The analysed PDF establishes published content under this attribution, not the technical source of the data.

  **Incident context already documented in AFRINTEL :** A post titled “Nigerian Tax Authority | Full Breach” displays the **Federal Capital Territory Internal Revenue Service (FCT-IRS)** logo and references images of people and signatures. The supplied PDF, exported from JustPaste.it, contains **314 pages** of text and personal data. “Full Breach” is the author's claim in the post title; data completeness and a compromise of FCT-IRS systems are not established.

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
- **Actor / Group:** BLACKLOCKS
- **Sector:** Architecture / Design and project management
- **Website:** [arcaunlimited.com](https://arcaunlimited.com/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Subtype:** Data exfiltration claimed; encryption unestablished
- **Confidence level:** High (listing and documentary link to ARCA; acquisition and total volume unconfirmed)
- **Impact level:** Level 3

- **Description:** **ARCA Unlimited Architects** is a multidisciplinary South African design practice based in Pretoria. Its services include architecture, interior and spatial design, project management, procurement and consulting; the firm says it has delivered work across Africa since 1995. These activities involve architectural drawings, project files and cost documentation for clients ([ARCA official profile](https://arcaunlimited.com/who-are-we.asp)).

- **Independent verification as of 18 October 2026:** The BLACKLOCKS listing and architectural plans consistent with ARCA corroborate the presence of samples, not a compromise of ARCA infrastructure. No company acknowledgement was found.

  **Incident context already documented in AFRINTEL :** BLACKLOCKS lists ARCA Unlimited Architects as a South African victim and displays a volume of **400G** without defining the unit. Sample images include architectural drawings, project documents and cost tables. Several items carry ARCA's name or branding and are consistent with its business. The review confirms neither the acquisition method, encryption, nor possession of the claimed volume.

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

- **Description:** **AFRICA-TECH** is described in the reviewed publication as a Malian organisation engaged in **IT services and document processing**. Documents examined by AFRINTEL refer to the organisation and to Mali, but available public information does not independently establish its registered legal identity, service portfolio or official website. The domain `africatech-mali.com` advertises different activities and **must not be automatically linked** to this record.

- **Independent verification as of 18 October 2026:** AFRINTEL observed and analysed the complete released batch attributed to AFRICA-TECH; external OSINT mostly repeats N0n’s statement. No acknowledgement by the entity, public proof of encryption, or sufficiently certain organisation identification was found.

  **Incident context already documented in AFRINTEL :** AFRICA-TECH is presented in N0n's publication as a Malian IT-services and document-processing company. All files released by the group were supplied for analysis. A Word complaint names AFRICA-TECH and contains references to Mali and Bamako, supporting a documentary link to the organisation. The proposed domain, https://www.africatech-mali.com/, advertises solar and electrical activities in Bamako. Comparison with the documents established no shared contact details; attribution to the victim remains unestablished.

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

### 25 September 2026
#### 🇲🇦 Morocco - Pharma 5

- **Initial publication date:** 25 September 2026 at 08:27 (displayed time; timezone not specified)
- **Actor / Group:** INC Ransom
- **Sector:** Healthcare / Pharmaceutical industry
- **Website:** [pharma5.ma](https://www.pharma5.ma/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Subtype:** Data exfiltration claimed
- **Confidence level:** High (existence of the listing and consistency of the visible sample; scope and acquisition unestablished)
- **Impact level:** Level 3

- **Description:** **Pharma 5** is a Moroccan pharmaceutical laboratory specialising in the development, manufacture and marketing of **generic medicines**. It operates in a regulated supply chain involving production, quality control and distribution in Morocco and African markets. Products associated with Pharma 5 appear in Morocco's public generic-medicines register ([Moroccan medicines authority, AMMPS](https://ammps.gov.ma/repertoire-medicaments-generiques)).

- **Independent verification as of 18 October 2026:** INC Ransom's claim was reported by [Le1.ma (27 September 2026)](https://le1.ma/pharma-5-frappe-par-une-cyberattaque/) and [DeXpose (26 September 2026)](https://www.dexpose.io/incransom-targets-moroccan-pharma-leader-pharma5/). These reports confirm the **existence and circulation of the claim**, not a verified breach. Le1.ma reported that Pharma 5 had neither confirmed nor denied the claim as of 27 September. No later official or independently technical confirmation of an intrusion, encryption or the claimed **50 GB** was identified in the sources examined through 18 October. The newly supplied images do, however, **corroborate the document's consistency with Pharma 5 and a plausible pharmaceutical supply chain**, without establishing technical provenance.

- **Sample OSINT corroboration (18 October 2026):**
  1. The readable page shows **“Pharma5 Quality Management Department”**, **“Specifications”**, document reference **`DE01 / PG / MQ / 036`**, **revision 01** and **“Page: 1/5”**. It concerns **salicylamide**, naming **Pharma 5 as client**, **MEDILIFE as supplier** and **JQC-CHINE as manufacturer**. Professional contact fields are present; personal names and contact details are deliberately omitted from AFRINTEL.
  2. The professional address for **MEDILIFE S.R.L.**, **Via San Vincenzo 8, 20123 Milan**, matches a [public Italian company record](https://www.ufficiocamerale.it/9842/medilife-srl). **JQC (Huayin) Pharmaceutical Co., Ltd.** lists **salicylamide** in its [official product catalogue](https://www.jqcpharm.com/en/index.php/Product). Pharma 5 publicly describes quality-control processes covering raw materials and manufacture in a [2020 company statement](https://www.pharma5.ma/wp-content/uploads/presse/communique/CP-PHARMA5-VF-17-NOVEMBRE-2020.pdf).
  3. These matches provide **contextual corroboration** of supplier identity and the pharmaceutical activity, **not** independent validation of a contractual relationship, the source document's authenticity, or a compromise of Pharma 5, MEDILIFE or JQC. The document's creation date is not established; 25 September 2026 is the threat actor's posting date.

- **Additional verification sources:** [Le1.ma](https://le1.ma/pharma-5-frappe-par-une-cyberattaque/) ; [DeXpose](https://www.dexpose.io/incransom-targets-moroccan-pharma-leader-pharma5/) ; [public MEDILIFE listing](https://www.ufficiocamerale.it/9842/medilife-srl) ; [JQC manufacturer catalogue](https://www.jqcpharm.com/en/index.php/Product) ; [official Pharma 5 quality statement](https://www.pharma5.ma/wp-content/uploads/presse/communique/CP-PHARMA5-VF-17-NOVEMBRE-2020.pdf).

- **Analysis:**

  **Observed:** The INC Ransom listing is dated **25 September 2026 at 08:27** (timezone unspecified), names `pharma5.ma` and displays **“Leaked data: 50Gb”** and a **“Revenue: 500M$”** figure (both attacker assertions, unverified). It claims corporate and financial records, product and supply data, quality-control and certification information, drug-testing material, employee data and counterparties' information. The gallery features document and spreadsheet thumbnails whose resolution does not establish all claimed categories. The second supplied image shows **one readable quality-management specifications page** naming salicylamide, reference `DE01 / PG / MQ / 036`, revision `01`, `1/5`, Pharma 5 as client, MEDILIFE (Italy) as supplier and JQC-CHINE as manufacturer. The page contains professional fields and personal contact details which are not reproduced. **Only page 1** was provided, not the four remaining pages or the native file.

  **Assumption:** The Pharma 5 header, pharmaceutical quality/sourcing context, independently locatable Italian supplier and the Chinese manufacturer's official catalogue together support a **strong documentary association** with Pharma 5's ecosystem. This does not demonstrate an intrusion into Pharma 5 systems: legitimate earlier document sharing, a third party, a pre-existing disclosure, a repost or fabrication cannot be excluded. No breach at MEDILIFE or JQC is established.

  **Unknown:** origin, creation date, non-public status and independently verified authenticity of the document; actual source organisation or system; timing and vector of any unauthorised access; existence and volume of the files claimed; exposed categories beyond the readable page; unique affected-person count; encryption or service disruption; official confirmation; negotiation, ransom payment or resale.

- **Analysis scope:** **two images supplied for this review**: (1) an INC Ransom victim listing with document thumbnails and (2) one readable Pharma 5 specifications page marked `1/5`. Thumbnails are not independently validated original files; the other pages were not supplied. SHA-256 hashes below identify **the two received images**, not any purported exfiltrated originals. No person's name, email address, telephone number or raw document is republished in this record.

- **Risk assessment:** A visible business contact and supplier/manufacturer relationship could be misused for **targeted phishing**, supplier payment diversion/BEC or social engineering. If additional claimed categories are genuine, confidentiality risks could extend to commercial and quality-assurance information and partners. **The two images do not substantiate patient health records, trade-secret theft or medication tampering.**

- **SOC/CTI recommendations:** preserve received image originals and acquisition metadata; check the specifications reference, date and hash against authorised internal quality/procurement systems offline; review unusual access to quality, purchasing and supplier-sharing repositories; verify any bank-details changes out-of-band; alert relevant business contacts as appropriate; monitor for further disclosure without purchasing or redistributing the data.

- **Sources / Evidence:** two October 2026 images supplied to AFRINTEL (actor listing displayed as dated 25 September); public cross-checks from [Pharma 5](https://www.pharma5.ma/wp-content/uploads/presse/communique/CP-PHARMA5-VF-17-NOVEMBRE-2020.pdf), [MEDILIFE S.R.L.](https://www.ufficiocamerale.it/9842/medilife-srl) and [JQC Pharmaceutical](https://www.jqcpharm.com/en/index.php/Product); [Le1.ma](https://le1.ma/pharma-5-frappe-par-une-cyberattaque/) and [DeXpose](https://www.dexpose.io/incransom-targets-moroccan-pharma-leader-pharma5/) for reporting on the claim. **Public business matches do not establish an intrusion.**

- **Screenshot traceability (SHA-256):** `1.png` = `27d9e3d2da239eb4d77495fa37482cab0c665b4447589efa1967c9e4e542b078` ; `Capture d’écran du 2026-09-28 11-22-02.png` = `66c63a7c0933ab7422853ae4c73aa5c6caa4ed33714cfe17d7e5577cc63e5a74`. Hashes of supplied copies only, not the actor's purported original files.

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

### 27 September 2026
#### 🇿🇦 South Africa - First National Bank (FNB)

- **Incident date:** Not established
- **Initial publication date:** 27 September 2026 at 00:06 (displayed time; timezone not specified)
- **Actor / Group:** Blacknet00
- **Sector:** Financial services / Banking
- **Website:** [fnb.co.za](https://www.fnb.co.za/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Subtype:** Extortion and data exfiltration claimed; encryption unestablished
- **Confidence level:** Medium (listing and visual consistency of the samples; origin, authenticity and compromise uncorroborated)
- **Impact level:** Level 3

- **Description:** **First National Bank (FNB)** is a South African retail and business banking brand operating as a division of **FirstRand Bank Limited**. It offers accounts, payments, credit, digital banking and services for individuals and businesses. Identifying the bank does not by itself demonstrate that its systems were compromised by the poster ([FNB official overview](https://www.fnb.co.za/about-fnb/about-us.html)).

- **Independent verification as of 18 October 2026:** No FNB statement, regulator notification or independent investigation corroborating the September Blacknet00 allegation was found. The banking outage observed on 2 September was a separate event with no established causal link.

  **Incident context already documented in AFRINTEL :** Blacknet00 published a listing naming First National Bank in South Africa and attached five images of financial documents. The visible material consists of FNB-branded business-account statements covering periods in 2023 and 2025. It supports the existence of the listing and a plausible documentary association with FNB, without establishing that the statements came from the bank's infrastructure or that unauthorised access occurred.

- **Analysis:**

  **Observed:** The listing is titled “Another victim of the BLACKNET-00 ransomware. FIRST NATIONAL BANK in South Africa” and carries the displayed timestamp **27 September 2026 at 00:06**. Its author claims an intrusion and demands a ransom. All **five** attached JPEGs were reviewed read-only; they total **428,994 bytes** and depict three apparent series of business-account statements, two of which are partial. Visible documentary periods fall in **2023** and **2025**. Every image carries a BLACKNET-00 watermark. The visual layout, FNB's wording as a division of FirstRand Bank Limited and the regulatory identifier visible in the images align with statements on the [official FNB website](https://www.fnb.co.za/). Account identifiers, contact information, transactions, amounts and names are visible but are not reproduced.

  **Assumption:** Consistency between the brand, layout, institutional wording and the three document series makes a link between the images and FNB statements plausible. It does not establish FNB as the source system: the statements could originate from customers, partners, a service provider, an endpoint or another repository. The watermark indicates how Blacknet00 presents the material, not the documents' technical provenance.

  **Unknown:** independent authenticity of the statements, their source and collection date, the existence of native files, any access vector and date, affected systems, the number of customers or accounts affected, any exfiltration scope, encryption, operational effects, negotiation, payment, resale, and confirmation by FNB or an authority remain unknown.

- **Analysis scope:** all five supplied JPEGs were reviewed in full, with file-type, size, dimension and SHA-256 checks. No PDF, native statement, source file, attachment metadata or complete corpus was supplied. No financial value, personal data or account identifier was transcribed, tested or added to the repository. A minimised manifest is retained outside the repository at `/tmp/afrintel-evidence/afr-2026-09-fnb-sa/evidence_manifest.json`.

- **Risk assessment:** if the documents are authentic and originate from unauthorised access, business statements could enable payment fraud, BEC, spear-phishing, impersonation and social engineering against customers or partners. The sample does not establish financial loss, bank-wide exposure or compromise of FNB accounts.

- **Recommendations:**
1. Preserve access, export and statement-generation logs, along with traces for document repositories and business-account services.
2. Within an authorised process, verify whether the document series match FNB templates and distribution channels, without testing visible identifiers or transactions.
3. Investigate unusual exports, privileged access, email-rule changes and third-party access to customer documents.
4. Strengthen detection of bank-detail changes, unusual payment requests and phishing campaigns targeting business customers.
5. Retain artefacts in restricted storage and monitor republication without opening criminal links or entering negotiations.

- **Sources / Evidence:** Blacknet00 listing and five sample images supplied to AFRINTEL; [official FNB website](https://www.fnb.co.za/) for correspondence of the brand and institutional wording. No criminal-infrastructure link, statement, identifier, transaction or raw personal data is published.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-09-27T00:06:00
listing_last_observed_at: 2026-10-08
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-10-08
-->

## Earlier incidents discovered late and integrated into the September corpus

> These records concern incidents that occurred before September 2026. They are integrated into the September editorial corpus because they were identified and verified late, before publication of the monthly report. The incident date remains the actual date or the best-supported documented window; the AFRINTEL discovery/integration date is recorded separately.

### January 3, 2026 - integrated September 1, 2026
#### 🇿🇦 South Africa - Constantia Pharmacy

- **Incident date:** January 3, 2026
- **Publication / confirmation date:** January 5, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** `Want_to_cry` ransomware observed; human operator unattributed
- **Sector:** Healthcare / Pharmacy
- **Status:** Corroborated
- **Incident type:** Ransomware
- **Confidence:** High
- **Impact:** Level 2
- **Description:** **Constantia Pharmacy** is a community pharmacy located at **Constantia Village Shopping Centre** in Cape Town, South Africa. It provides prescription dispensing, pharmaceutical advice and clinic/community-care services. Such operations rely on pharmacy information systems and records needed to serve patients ([official website](https://constantiapharmacy.co.za/)).

- **Independent verification as of 18 October 2026:** **Earlier incident corroborated by reporting:** MyBroadband documented a third party’s intervention against file-encrypting malware on a Constantia Pharmacy server in early January 2026. The attack dates to January, not September; AFRINTEL’s September discovery is not a new attack.

- **Additional verification sources:** [Source 1](https://mybroadband.co.za/news/security/623956-hacker-rescues-south-african-pharmacy-from-cyber-attack.html)

- **Sources / Evidence:** [MyBroadband, January 5, 2026](https://mybroadband.co.za/news/security/623956-hacker-rescues-south-african-pharmacy-from-cyber-attack.html)

Constantia Pharmacy is an independent pharmacy in Cape Town. On January 3, a researcher observed via Shodan an exposed Windows server belonging to its environment while ransomware was running. The pharmacy and its ProPharm provider were alerted and intervened. The observation and coordinated response corroborate the incident; exfiltration, encrypted volume and operator identity remain unknown.

### January 12, 2026 - integrated September 1, 2026
#### 🇿🇦 South Africa - Land and Agricultural Development Bank of South Africa (Land Bank)

- **Incident date:** January 12, 2026
- **Detailed public confirmation:** March 9, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** Not publicly attributed
- **Sector:** Government / Public Bank / Finance
- **Status:** Victim Confirmed
- **Incident type:** Ransomware
- **Confidence:** Very High
- **Impact:** Level 4
- **Description:** The **Land and Agricultural Development Bank of South Africa (Land Bank)** is a specialist development-finance institution serving **South African agriculture**. It finances commercial farmers, agribusinesses and new participants in the agricultural value chain to support production and sector development. It is a sector-focused public development bank rather than a general-purpose retail bank ([Land Bank official profile](https://www.landbank.co.za/About-Us/Pages/Our-Business.aspx)).

- **Independent verification as of 18 October 2026:** **Publicly corroborated acknowledgement:** ITWeb reported the Land Bank ransomware incident occurring in January 2026 and the bank’s security improvements. Added to AFRINTEL in September, but not a September attack.

- **Additional verification sources:** [Source 1](https://www.itweb.co.za/article/land-bank-tightens-security-after-ransomware-attack/raYAyMorlOl7J38N)

- **Sources / Evidence:** [ITWeb, March 9, 2026](https://www.itweb.co.za/article/land-bank-tightens-security-after-ransomware-attack/raYAyMorlOl7J38N); [ITWeb, January 16, 2026](https://www.itweb.co.za/article/land-bank-flags-it-systems-disruption/Kjlyr7wBDRZvk6am)

The South African finance minister confirmed a ransomware attack detected on January 12 after unauthorised activity. Some servers and laptops were encrypted and files were exfiltrated; critical ERP, core-banking and CRM systems were reportedly not compromised. The actor, exact volume and dwell time remain unknown.

### March 23, 2026 - integrated September 1, 2026
#### 🇿🇦 South Africa - Standard Bank South Africa

- **Incident / first communication date:** March 23, 2026
- **Public updates:** April 2, 13 and 14, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** Not officially attributed; separate PrinzEugen claim uncorroborated
- **Sector:** Finance / Banking
- **Status:** Victim Confirmed
- **Incident type:** Data Leak
- **Confidence:** Very High
- **Impact:** Level 4
- **Description:** **Standard Bank South Africa** represents the South African banking operations of **Standard Bank Group**, offering accounts, payments, financing, business banking and investment-related services. **The Standard Bank of South Africa Limited** is identified among the group's South African legal entities in its institutional documentation ([official privacy statement](https://www.standardbank.co.za/southafrica/personal/about-us/legal/privacy-statement)).

- **Independent verification as of 18 October 2026:** **First-party confirmation:** on 23 March 2026, Standard Bank disclosed unauthorised access to a limited set of data and said transactional systems and customer funds were unaffected. This predates September.

- **Additional verification sources:** [Source 1](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank)

- **Sources / Evidence:** [Standard Bank, March 23, 2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank); [Standard Bank, April 14, 2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-data-incident-update-14-april)

Standard Bank confirmed unauthorised access to internal administrative systems and document repositories, potentially exposing names, identifiers, contact details, addresses and account numbers. Transactional and core systems were reportedly not accessed. The vector, number of people and copied volume remain unknown. This record is distinct from the May Standard Bank Group claim.

### April 18, 2026 - integrated September 1, 2026
#### 🇿🇦 South Africa - Ahmed Al-Kadi Private Hospital

- **Incident date:** April 18, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** Not publicly attributed
- **Sector:** Healthcare / Private Hospital
- **Status:** Victim Confirmed
- **Incident type:** Ransomware
- **Confidence:** Very High
- **Impact:** Level 4
- **Description:** **Ahmed Al-Kadi Private Hospital** is a private hospital in **Mayville, Durban**, South Africa. Developed by the **Islamic Medical Association of South Africa**, it opened in 2017 and reports **163 beds**, providing inpatient and specialist medical and surgical care. It states that its services are available regardless of ethnicity or religion ([official hospital profile](https://ahmedalkadi.com/about-us/)).

- **Independent verification as of 18 October 2026:** **Direct confirmation:** the hospital reported unauthorised access on 18 April 2026 followed by ransomware deployment encrypting part of its environment; it issued a POPIA notice and notified the regulator. Not a September occurrence.

- **Additional verification sources:** [Source 1](https://ahmedalkadi.com/notification-of-data-incident/)

- **Sources / Evidence:** [Hospital official notice](https://ahmedalkadi.com/notification-of-data-incident/)

The hospital confirmed that an unauthorised party accessed its IT environment and deployed ransomware on April 18. Part of the environment was encrypted, contained and restored with external specialists. The vector, encryption scope and exfiltration remain unknown.

### April 28, 2026 - integrated September 1, 2026
#### 🇰🇪 Kenya - TikoHUB

- **Incident date:** 28 April 2026 (date of the access-offer post; initial compromise not established)
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Initial publication date:** 28 April 2026 at 23:26 (displayed time; timezone not specified)
- **Actor / Group:** DarkMafiaX (displayed account; identity and affiliation unverified)
- **Sector:** Ticketing / Events / Digital services
- **Website:** [tikohub.co.ke](https://www.tikohub.co.ke/)
- **Status:** Claim - Unverified
- **Incident type:** Access Sale
- **Confidence level:** Medium
- **Impact level:** Level 4

- **Description:** **TikoHUB** is a Kenyan **ticketing and events-services platform** serving event organisers and attendees. Its public offering focuses on event discovery and management and online ticketing or participation workflows. The existence of the service does not validate any claimed administrator privileges offered for sale ([TikoHUB official overview](https://www.tikohub.co.ke/about_us.php)).

- **Independent verification as of 18 October 2026:** No independent public evidence of access being offered for TikoHUB, or company acknowledgement, was found. The suspect posting is dated April 2026 and the tracker’s inclusion came later.

  **Incident context already documented in AFRINTEL :** A post attributed to the DarkMafiaX account offers administrator access presented as related to TikoHUB, a Kenyan ticketing and event-management platform. The post and displayed credentials were not tested; AFRINTEL does not confirm their validity, effective access or a compromise of TikoHUB.

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

### Late May 2026 - integrated September 1, 2026
#### 🇿🇦 South Africa - Centre for High Performance Computing (CHPC) / Lengau Supercomputer

- **Incident date:** late May 2026
- **Detailed public confirmation:** August 24, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** Not publicly attributed
- **Sector:** Research / Strategic Scientific Infrastructure
- **Status:** Victim Confirmed
- **Incident type:** System Intrusion
- **Confidence:** Very High
- **Impact:** Level 4
- **Description:** The **Centre for High Performance Computing (CHPC)** is South Africa's national **high-performance computing** facility within the **CSIR** research ecosystem and the NICIS infrastructure programme. It provides scientific computing resources to universities and research organisations; **Lengau** is a flagship supercomputer associated with the facility. CHPC is therefore a research infrastructure rather than an ordinary commercial company ([CHPC official profile](https://www.chpc.ac.za/about-the-chpc/)).

- **Independent verification as of 18 October 2026:** **Institutionally corroborated:** the CSIR and a parliamentary answer described compromise of the Lengau cluster in late May 2026, associated with vulnerabilities in aging systems and service disruption. Do not categorise this as a September ransomware event.

- **Additional verification sources:** [Source 1](https://www.itweb.co.za/article/cause-of-breach-on-sas-supercomputer-revealed/KPNG878NLeGq4mwD)

- **Sources / Evidence:** [ITWeb, August 24, 2026](https://www.itweb.co.za/article/cause-of-breach-on-sas-supercomputer-revealed/KPNG878NLeGq4mwD)

A parliamentary response confirmed an incident affecting part of the Lengau HPC environment in late May, linked to vulnerabilities in an ageing environment. Access depth, dwell time and any data viewed remain unknown.

### June 2026 - integrated September 1, 2026
#### 🇿🇦 South Africa - MIP Holdings

- **Incident date:** June 2026, exact date not established
- **First public notice:** June 26, 2026
- **Additional regulatory confirmation:** September 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** Not publicly attributed
- **Sector:** Technology / Software / Service Provider
- **Status:** Victim Confirmed
- **Incident type:** Data Leak
- **Confidence:** Very High
- **Impact:** Level 4
- **Description:** **MIP Holdings** is a South African **FinTech/InsurTech** software and technology provider. Its platforms support policy and contract administration, customer relationship management and workflows for insurers, healthcare operators, lenders and retirement administrators. As a software supplier to multiple organisations, an incident affecting MIP can have potential downstream implications for customers ([MIP official website](https://www.mip.co.za/)).

- **Independent verification as of 18 October 2026:** **Confirmed service-provider incident:** on 26 June 2026 LegalWise reported that MIP Holdings had detected unauthorised access to a legacy development/support system. Data belonging to customers of multiple insurers was subsequently implicated; this does not establish intrusion at each client. Initial incident in June.

- **Additional verification sources:** [Source 1](https://www.legalwise.co.za/media-centre/statement-regarding-third-party-cybersecurity-incident)

- **Sources / Evidence:** [LegalWise, June 26, 2026](https://www.legalwise.co.za/media-centre/statement-regarding-third-party-cybersecurity-incident); [TechCentral, September 25, 2026](https://techcentral.co.za/insurers-mip-breach-regulators/286482/)

MIP Holdings identified unauthorised access to a former development and support environment. South Africa's Information Regulator confirmed in September that it was working with MIP to establish the circumstances and number of affected people. The compromise and supply-chain risk are confirmed; volume and vector remain unknown.

### June 14-15, 2026 - integrated September 1, 2026
#### 🇬🇦 Gabon - Société d'Énergie et d'Eau du Gabon (SEEG)

- **Incident date:** night of June 14-15, 2026
- **Initial government communication:** June 15, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** Not publicly attributed
- **Sector:** Energy / Water / Critical Infrastructure
- **Status:** Victim Confirmed
- **Incident type:** System Intrusion
- **Confidence:** Very High
- **Impact:** Level 4
- **Description:** The **Société d'Énergie et d'Eau du Gabon (SEEG)** is a Gabonese utility operator involved in **electricity generation, transmission and distribution**, as well as the supply of **drinking water**. Its work relies on industrial infrastructure and management systems essential to continued delivery of services to households and businesses ([SEEG official activities overview](https://www.seeg-gabon.com/activites)).

- **Independent verification as of 18 October 2026:** **Confirmed incident, mechanism requires precision:** the Gabonese government documented the EDAN outage overnight on 14–15 June 2026. SEEG later cited alleged sabotage or malicious IT actions. This does not necessarily establish an external intrusion or exfiltration. June incident.

- **Additional verification sources:** [Source 1](https://gabonofficiel.com/seeg-un-sabotage-informatique-a-paralyse-95-de-son-systeme-la-cybersecurite-desormais-au-coeur-des-enjeux/) ; [Source 2](https://gouvernement.ga/2026/06/15/systeme-edan-retablissement-confirme-et-dispositif-de-protection-renforce-par-letat/)

- **Sources / Evidence:** [Gabonese Government, June 15, 2026](https://gouvernement.ga/2026/06/15/systeme-edan-retablissement-confirme-et-dispositif-de-protection-renforce-par-letat/); [Gabon Media Time, August 5, 2026](https://gabonmediatime.com/cybersecurite-la-seeg-revele-avoir-perdu-pres-de-95-de-ses-infrastructures-informatiques/)

A major incident disrupted SEEG systems, including EDAN. The government cited malicious activity and SEEG later described the event as sabotage, with nearly 95% of its IT infrastructure reportedly lost. The technical mechanism, responsible parties and exfiltration remain unknown.

### July 12, 2026 - integrated September 1, 2026
#### 🇨🇲 Cameroon - Ministry of Employment and Vocational Training (MINEFOP)

- **Incident date:** July 12, 2026
- **Public analysis:** July 27, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** ANTONKILL
- **Sector:** Government / Public Administration
- **Status:** Corroborated
- **Incident type:** Defacement
- **Confidence:** High
- **Impact:** Level 2
- **Description:** Cameroon's **Ministry of Employment and Vocational Training (MINEFOP)** develops and implements public policy on **employment, vocational training and professional integration**. Its responsibilities include career guidance, skills development and support for access to work. It is a national government ministry, not a private training college ([MINEFOP official mandate](https://minefop.gov.cm/fr/missions/)).

- **Independent verification as of 18 October 2026:** **Publicly corroborated defacement:** Cameroon’s CIRT issued an advisory on the ANTONKILL campaign targeting the MINEFOP website in July 2026. The demonstrated scope is a web portal, not the entire ministry network. July incident.

- **Additional verification sources:** [Source 1](https://cirt.cm/alerte-de-securite-campagne-antonkill-web-defacement-ciblant-les-institutions-sous-joomla-et-helix3/)

- **Sources / Evidence:** [OBS-CC, July 27, 2026](https://obs-cc.org/defacement-antonkill-minefop/); [OBS-CC incident database](https://obs-cc.org/incidents/)

OBS-CC, relying on an ANTIC CIRT alert, documented the defacement of the MINEFOP website in a campaign attributed to ANTONKILL. The depth of access, persistence and exposure of non-public data are not established.

### July 15, 2026 - integrated September 1, 2026
#### 🇿🇦 South Africa - Rectron (Pty) Ltd

- **Detected incident date:** July 15, 2026
- **SENS notification:** July 22, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** Not officially attributed; DragonForce unconfirmed
- **Sector:** Technology / IT Distribution
- **Status:** Victim Confirmed
- **Incident type:** Data Leak
- **Confidence:** Very High
- **Impact:** Level 3
- **Description:** **Rectron (Pty) Ltd** is a South African **ICT products and solutions distributor** within the **Mustek** group. Its portfolio includes software, hardware, networking, data storage, cloud and data-centre solutions sold through resellers and technology partners. The company therefore operates within the technology supply chain ([Rectron official profile](https://www.rectron.co.za/pages/about)).

- **Independent verification as of 18 October 2026:** **Official market disclosure:** on 22 July 2026 Mustek released a SENS notice concerning a cyber incident at Rectron. This establishes the incident but not necessarily the responsibility of a claiming group. July incident.

- **Additional verification sources:** [Source 1](https://www2.sharenet.co.za/v3/sens_display.php?scode=MST&seq=33&tdate=20260722130100)

- **Sources / Evidence:** [Mustek / JSE SENS, July 22, 2026](https://www2.sharenet.co.za/v3/sens_display.php?scode=MST&seq=33&tdate=20260722130100)

Mustek announced that Rectron suffered a compromise affecting some IT systems and operations, with unlawful access to some data. Rectron launched incident response and notified the Information Regulator. The vector, data categories and exfiltrated volume remain unknown.

### July 18, 2026 - integrated September 1, 2026
#### 🇰🇪 Kenya - Official website of the President of the Republic (`president.go.ke`)

- **Incident date:** July 18, 2026
- **Government confirmation:** July 18, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** Not publicly attributed
- **Sector:** Government / Presidency
- **Status:** Government Confirmed
- **Incident type:** Defacement
- **Confidence:** Very High
- **Impact:** Level 3
- **Description:** The domain **`president.go.ke`** hosts the **official website of the Presidency of the Republic of Kenya**. It publishes public information about presidential activities, the administration and coordination of government business. This record concerns **an official web portal**, not necessarily the Presidency's or Kenyan government's entire IT environment ([official portal](https://www.president.go.ke/)).

- **Independent verification as of 18 October 2026:** **Government-confirmed:** Kenya’s ICT ministry acknowledged the defacement of `president.go.ke` on 18 July 2026 and said no sensitive-data compromise had been established. The event concerns a specific website in July.

- **Additional verification sources:** [Source 1](https://www.aa.com.tr/fr/afrique/kenya-le-site-officiel-de-la-pr%C3%A9sidence-pirat%C3%A9-des-hackers-r%C3%A9clament-une-rancon-en-bitcoin/4002284)

- **Sources / Evidence:** [ICT Authority / ministry statement, July 18, 2026](https://www.linkedin.com/posts/kenya-ict-board_ministry-of-information-communications-activity-7484210613053784065-Fy7R); [The Standard, July 18, 2026](https://www.standardmedia.co.ke/national/article/2001553147/kabogo-no-sensitive-data-accessed-after-presidents-website-hack)

The Kenyan government confirmed the defacement of the presidential website, which displayed hostile messages, a wallet address and a demand for 5 BTC. No evidence of access to sensitive data or exfiltration was reported. The vector and attacker identity remain unknown.

### August 26, 2026 - integrated September 1, 2026
#### 🇿🇦 South Africa - Cartrack South Africa

- **Incident date:** August 26, 2026
- **Public communication:** August 28, 2026
- **Update:** September 10, 2026
- **AFRINTEL discovery / integration date:** September 1, 2026
- **Actor / Group:** Not publicly attributed
- **Sector:** Telematics / Mobility / Automotive Services
- **Status:** Victim Confirmed
- **Incident type:** Ransomware
- **Confidence:** Very High
- **Impact:** Level 4
- **Description:** **Cartrack South Africa** provides **vehicle telematics**, tracking, stolen-vehicle recovery and fleet-management services. Its offering combines vehicle-installed equipment, digital platforms and operational services for consumers and businesses. This business model involves vehicle, subscription and customer information, without implying that all such data was exposed in a particular incident ([Cartrack official website](https://www.cartrack.co.za/)).

- **Independent verification as of 18 October 2026:** **Direct confirmation:** Cartrack disclosed finding ransomware on certain systems on 26 August 2026 and warned that personal information might have been posted. The September Dire Wolf claim is not an official forensic attribution. Initial event in August.

- **Additional verification sources:** [Source 1](https://cartrack.co.za/platform/resources/news)

- **Sources / Evidence:** [Cartrack - Data Incident at Cartrack South Africa](https://cartrack.co.za/platform/resources/news)

Cartrack confirmed a ransomware incident detected on August 26. Affected servers were isolated and the platform restored within five hours. An update states that personal information relating to some customers was accessed and may have been published on a restricted-access site. The vector, operator and exact volume remain unknown.

## September ransomware publications

> These records originate from the local `AFRINTEL_Victimes_Africaines_Septembre_2026.xlsx` workbook. The date shown is the publication or observation date in the source corpus, not necessarily the compromise date. Ransomware listings or claims do not by themselves confirm an intrusion.

### September 1, 2026
#### 🇪🇬 Egypt - Holding Company for Construction and Development (HCCD)
- **Initial publication date:** September 1, 2026
- **Actor / Group:** krybit
- **Sector:** Construction
- **Website:** [hccd-construction.com](https://hccd-construction.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** The **Holding Company for Construction and Development (HCCD)** is an Egyptian holding company active in **construction, civil works and property development**. Its website describes subsidiaries involved in contracting, engineering consulting, housing and electrical works. As a corporate group, a claim naming HCCD does not establish which subsidiary or information system may be affected ([HCCD official overview](https://hccd-construction.com/About_e.aspx)).

- **Independent verification as of 18 October 2026:** Only the listing in Krybit claim trackers is corroborated; no HCCD statement or verifiable investigation proving an intrusion into its systems was found.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 35624

Krybit published a claim naming the Holding Company for Construction and Development. The date reflects the listing observation; compromise, volume, encryption and exfiltration remain unknown.

#### 🇪🇬 Egypt - Mecca High Feed Factory
- **Initial publication date:** September 1, 2026
- **Actor / Group:** krybit
- **Sector:** Agriculture / Agribusiness
- **Website:** [meccahighfeed.blogspot.com](https://meccahighfeed.blogspot.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **Mecca High Feed Factory** is described on its Arabic-language business blog as an Egyptian producer of **poultry and livestock feed**, including plant-based feed formulations. The business blog associates the **Mecca** and **High Feed** names and discusses animal nutrition products; as a self-published source, it does not independently verify the company's current legal structure or industrial footprint ([company blog](https://meccahighfeed.blogspot.com/)).

- **Independent verification as of 18 October 2026:** OSINT aggregators relay a Krybit claim without independent evidence of compromise or an identified Mecca High Feed Factory statement. Some databases disagree on country: do not revise geographical attribution without checking.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 35627

Krybit published a claim targeting Mecca High Feed Factory, described as an Egyptian animal-feed manufacturer. Technical evidence and actual impact are not established.

#### 🇪🇬 Egypt - Seashell Hospital
- **Initial publication date:** September 1, 2026
- **Actor / Group:** krybit
- **Sector:** Healthcare / Hospital
- **Website:** [seashellhospital.com](https://seashellhospital.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **Seashell Hospital** is a private healthcare facility in **New Cairo**, Egypt. Its website describes inpatient healthcare, diagnosis and treatment services, including a round-the-clock emergency department. Its operations involve sensitive clinical and administrative workflows, although the claim alone does not demonstrate exposure of patient records ([hospital official website](https://www.seashellhospital.com/AboutUs/Index)).

- **Independent verification as of 18 October 2026:** Multiple leak-site indices reproduce a Krybit claim naming Seashell Hospital, but no hospital notification or independent forensic confirmation was found. Disruption, patient-data exposure and encryption remain unestablished.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 35637

Krybit published a claim targeting Seashell Hospital, a private Egyptian hospital. No reviewed public element confirms access, encryption or exfiltration.

### September 7, 2026
#### 🇿🇦 South Africa - VSB Attorneys Inc
- **Initial publication date:** September 7, 2026
- **Actor / Group:** lockbit5
- **Sector:** Legal Services
- **Website:** [vsbattorneys.co.za](https://vsbattorneys.co.za/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **VSB Attorneys Inc** is a **South African law firm** offering property law, conveyancing and corporate/commercial legal services. It assists individuals and businesses with legal and contractual matters that can involve confidential files and supporting documents. The nature of its legal work does not establish which records, if any, were affected by the claim ([VSB official profile](https://www.vsbattorneys.co.za/about-vsb-attorneys-law-firm/)).

- **Independent verification as of 18 October 2026:** The LockBit5 claim naming VSB Attorneys is recorded by leak-site monitors, without an identified company response or independent proof of intrusion.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 35798

Lockbit5 published a claim targeting VSB Attorneys Inc, a South African law firm. Compromise and data scope are unconfirmed.

#### 🇪🇬 Egypt - Nile Projects Trading
- **Initial publication date:** September 7, 2026
- **Actor / Group:** TheGentlemen
- **Sector:** Real Estate / Property Management
- **Website:** [nileprojects.com](https://nileprojects.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **Nile Projects & Trading Company** is an Egyptian trading group that traces its origins to **1972**. Initially a family business, it expanded into **international brand distribution, tyres, luxury fashion and commercial real estate**. Its operations extend beyond real estate, but the listing does not identify which business unit, if any, was targeted ([Nile Projects official profile](https://nileprojects.com/pages/about-us)).

- **Independent verification as of 18 October 2026:** Public search results reproduce The Gentlemen’s claim against Nile Projects Trading; no official acknowledgement, regulatory notice or forensic verification establishes a confirmed incident.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 35813

TheGentlemen published a claim targeting Nile Projects Trading, an Egyptian group active in retail, real estate and distribution. No evidence confirms access or exfiltration.

#### 🇿🇦 South Africa - Hollard Insurance Group
- **Initial publication date:** September 7, 2026
- **Actor / Group:** TheGentlemen
- **Sector:** Insurance
- **Website:** [hollard.co.za](https://www.hollard.co.za/)
- **Status:** Third-Party Exposure Confirmed - Direct Breach Not Established
- **Incident type:** Data Leak (third-party exposure) / ransomware claim disputed
- **Description:** **Hollard Insurance Group** is a **privately owned South African insurance group** providing life and non-life coverage, personal and commercial insurance and investment-related products. It has a footprint across several African markets through operations and partnerships. The claim naming Hollard does not establish which legal entity or subsidiary, if any, was affected ([Hollard official overview](https://www.hollard.co.za/our-world)).

- **Independent verification as of 18 October 2026:** **Third-party exposure acknowledged; direct Hollard breach disputed:** in statements dated 15 and 18 September 2026 Hollard reported that information relating to some funeral policyholders was published following the **June 2026 incident at MIP Holdings**. It has notified affected customers and engaged regulators; its investigations found **no compromise of Hollard’s own environment**. The Gentlemen’s listing must not be treated as a confirmed intrusion at Hollard.

- **Additional verification sources:** [Source 1](https://www.fanews.co.za/article/company-news-results/1/hollard/1301/hollard-statement-regarding-reported-cyber-threat-claims/44724) ; [Source 2](https://mybroadband.co.za/news/security/669576-momentum-group-company-responds-to-data-breach-claims.html)

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 35817

TheGentlemen published a claim targeting Hollard Insurance Group. The source corpus describes the insurer and its activities but provides no independent compromise evidence.

#### 🇿🇦 South Africa - RelyComply AML Platform
- **Initial publication date:** September 9, 2026
- **Actor / Group:** Direwolf (claim; technical attribution unconfirmed)
- **Sector:** Fintech / Anti-Money Laundering
- **Status:** Victim Confirmed - Unauthorized Access
- **Incident type:** System Intrusion (ransomware claim unconfirmed)
- **Subtype:** Unauthorised access confirmed; Direwolf link/encryption unproven
- **Description:** **RelyComply** is a regulatory-technology (**RegTech**) provider offering an **AML/KYC** compliance platform for organisations subject to anti-money-laundering requirements. Its software centralises customer due-diligence, identity-checking, monitoring and compliance workflows. The company's public profile does not, by itself, confirm the scope of any intrusion ([RelyComply official platform](https://relycomply.com/)).

- **Independent verification as of 18 October 2026:** **Company-confirmed unauthorised access:** in its 16 September notice, RelyComply said it detected access to certain systems on 8 September 2026 after exploitation of a third-party application zero-day. The company rebuilt affected systems, rotated credentials/tokens, patched the flaw and notified South Africa’s Information Regulator (**reference SC20263150**). Virgin Active and HuntEx describe potential transaction-data exposure via Peach Payments. **Direwolf attribution, encryption and the claimed data volume are not confirmed.**

- **Additional verification sources:** [Source 1](https://relycomply.com/relycomply-cyber-incident-what-happened-and-what-you-can-do/) ; [Source 2](https://virginactivesa.freshdesk.com/support/solutions/articles/201000132941-cybersecurity-incident-at-relycomply) ; [Source 3](https://www.huntex.net/peach-payments-security-update)

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 35859

**Original claim context:** Direwolf named RelyComply in a leak-site listing. The company later confirmed unauthorised access to some systems and identified an apparent third-party zero-day exploitation path. Direwolf involvement, encryption and the volume of any extracted data remain unproven.

### September 12, 2026
#### 🇲🇦 Morocco - La Sultana Hotel Group
- **Initial publication date:** September 12, 2026
- **Actor / Group:** krybit
- **Sector:** Hospitality
- **Website:** [lasultanahotels.com](https://lasultanahotels.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **La Sultana Hotels** is a Moroccan **luxury hospitality** brand comprising **La Sultana Marrakech** in the historic medina and **La Sultana Oualidia** by the Atlantic lagoon. Its offering includes premium accommodation, dining and visitor experiences. The claim does not establish which property or reservation-related system, if any, was affected ([La Sultana official website](https://www.lasultanahotels.com/)).

- **Independent verification as of 18 October 2026:** The Krybit claim naming La Sultana hotels appears in OSINT indices, but no hotel-group statement or independent proof of intrusion was located.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 35923

Krybit published a claim targeting La Sultana Hotel Group in Morocco. No reviewed element confirms access, encryption or data disclosure.

#### 🇪🇬 Egypt - Egyptian Airports Company (EAC)
- **Initial publication date:** September 12, 2026
- **Actor / Group:** krybit
- **Sector:** Air Transport
- **Website:** [eac-airports.com](https://www.eac-airports.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** The **Egyptian Airports Company (EAC)** is an Egyptian **airport operator** within the state-owned **Egyptian Holding Company for Airports and Air Navigation** ecosystem. Its role involves managing, operating, maintaining and developing civil airports. It is distinct from an airline or air-navigation service provider; the claim does not identify any specific compromised airport ([Egyptian Ministry of Civil Aviation](https://web.civilaviation.gov.eg/Companies/AirportCompany)).

- **Independent verification as of 18 October 2026:** Several CTI feeds list Krybit’s claim against the Egyptian Airports Company domain. No acknowledgement by EAC or an Egyptian authority, or evidence of impact on operational airport systems, was found.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 35917

Krybit published a claim targeting the Egyptian Airports Company. The publication identifies the organisation and sector; technical outcome and any exposure remain unknown.

### September 16, 2026
#### 🇳🇦 Namibia - Namibian Defence Force
- **Initial publication date:** September 16, 2026
- **Actor / Group:** RansomHouse (association publicly reported by NAM-CSIRT)
- **Sector:** Defence / Armed Forces
- **Status:** Government Confirmed - Unauthorized Access
- **Incident type:** System Intrusion (ransomware claim; encryption unconfirmed)
- **Subtype:** Ministry network intrusion confirmed; encryption/exfiltration unproven
- **Description:** The **Namibian Defence Force (NDF)** is **Namibia's national armed forces**. Its core constitutional mission is to defend the country's territorial integrity and national interests under Namibia's defence institutions. A claim naming the NDF does not, by itself, demonstrate a compromise of operational military networks ([Namibian Ministry of Defence](https://mod.gov.na/about-ndf)).

- **Independent verification as of 18 October 2026:** **Compromise confirmed by the national cyber authority:** according to a NAM-CSIRT statement reported on 21 September 2026, unauthorised activity was found on the **Ministry of Defence and Veterans Affairs (MODVA)** network, and the investigation linked the incident to **RansomHouse**. The claim names the “Namibian Defence Force”, but the officially confirmed scope is the ministry network. **No released evidence confirms encryption, exfiltration, military-secret leakage or payment.**

- **Additional verification sources:** [Source 1](https://www.theregister.com/cyber-crime/2026/09/21/ransomhouse-picks-a-fight-with-namibias-defense-establishment/5297816) ; [Source 2](https://www.namibian.com.na/hackers-hit-ndf-ransomhouse-threatens-state-secrets/)

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 36039

**Original claim context:** RansomHouse named the Namibian Defence Force in its listing. NAM-CSIRT subsequently confirmed unauthorised activity on the Ministry of Defence network and associated it with RansomHouse, while neither encryption nor data exfiltration was publicly demonstrated.

### September 18, 2026
#### 🇹🇳 Tunisia - PayPal Support Operations (Transcom WorldWide)
- **Initial publication date:** September 18, 2026
- **Actor / Group:** N0n
- **Sector:** Business Services / Customer Support
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **Transcom WorldWide** is a **business-process outsourcing and customer-experience (BPO/CX)** provider offering contact-centre, customer-support and business-process services to international brands, including from Tunisia. **PayPal** is a separate payments-services company. The claim links them to support operations, but **the existence and scope of an affected PayPal–Transcom contract is not independently corroborated** by these public company descriptions ([Transcom official services](https://transcom.com/services/customer-experience)).

- **Independent verification as of 18 October 2026:** No independent confirmation of an intrusion or of the precise operational relationship between Transcom, PayPal and Tunisian sites was found. Citrix/AD infrastructure maps and 86.7 million connection records are solely N0n claims.

- **Additional verification sources:** [Source 1](https://cypro.co.uk/insights/cyber-bulletins/n0n-ransomware-claim-targets-transcom/)

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 36122

N0n published a claim targeting outsourced support operations linked to PayPal and Transcom WorldWide in Tunisia. The post mentions internal systems and a settlement deadline, but does not confirm access, the stated volumes or operational impact.

### September 21, 2026
#### 🇪🇹 Ethiopia - Siinqee Bank
- **Initial publication date:** September 21, 2026
- **Actor / Group:** lockbit5
- **Sector:** Banking
- **Website:** [siinqeebank.com](https://siinqeebank.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **Siinqee Bank** is an Ethiopian financial institution providing **retail banking, finance and financial-inclusion services**, including for communities and entrepreneurs. It describes offerings combining mainstream banking, microfinance and digital channels. Its name refers to an Oromo cultural symbol associated with women's rights and protection ([Siinqee Bank official overview](https://siinqeebank.com/about-us/)).

- **Independent verification as of 18 October 2026:** Siinqee Bank’s 8 October 2026 fraud-awareness post is **not** confirmation of the LockBit incident claimed on 21 September. No incident-specific breach notice was located.

- **Additional verification sources:** [Source 1](https://siinqeebank.com/2026/10/08/stay-alert/)

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 36161

Lockbit5 published a claim targeting Siinqee Bank, an Ethiopian financial institution. No independent element confirms intrusion or data exposure.

#### 🇦🇴 Angola - Grupolider
- **Initial publication date:** September 21, 2026
- **Actor / Group:** TheGentlemen
- **Sector:** Distribution / Agriculture / Logistics
- **Website:** [grupolider-ao.com](https://grupolider-ao.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **Grupolider** is a name associated with **commercial activity in Angola**. Public sources link `grupolider-ao.com` to distribution/import businesses and **Novagrolider**, which is active in agriculture and agro-industry. The domain's website was suspended when checked; the precise corporate relationships and the identity of the entity named in the claim **remain unverified** ([Argentine trade directory](https://exportaciones.cancilleria.gob.ar/sitios/ficha_directorio/89314); [Novagrolider profile](https://icrisco.com/profile.php?id=novagrolider-5238)).

- **Independent verification as of 18 October 2026:** Grupolider’s entry on The Gentlemen’s leak site remains an allegation; no official confirmation or technically verified link between the claimed domain and group entities was found.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 36171

TheGentlemen published a claim targeting Grupolider, an Angolan group active in agriculture, logistics, construction and distribution. Compromise and claimed volume remain unknown.

### September 24, 2026
#### 🇹🇿 Tanzania - Air Tanzania Company Limited (ATCL)
- **Initial publication date:** September 24, 2026
- **Actor / Group:** krybit
- **Sector:** Air Transport
- **Website:** [airtanzania.co.tz](https://airtanzania.co.tz/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Description:** **Air Tanzania Company Limited (ATCL)** is **Tanzania's state-owned national airline**. It provides passenger and cargo air transport on domestic and international routes. Its operations rely on booking, airline-operation and customer-service systems; the presence of images in a sample does not establish that they originated from these systems ([Air Tanzania official profile](https://airtanzania.co.tz/index.php/about-us)).

- **Independent verification as of 18 October 2026:** Krybit’s Air Tanzania domain claim appears in OSINT feeds; reviewed sources state that the airline had not confirmed it. A purported sample does not establish exfiltration from booking systems or encryption.

- **Additional verification sources:** [Source 1](https://www.galaxywarden.com/blog/breach/airtanzania-co-tz-airtanzania-com-krybit-2026-09)

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 36284

Krybit published a claim targeting Air Tanzania Company Limited, Tanzania's national airline. A local sample associated with the publication was reviewed read-only: **114 files** totalling **676,972,266 bytes**, including **112 valid images** and **2 non-image files despite the `.jpg` extension**. The valid images comprise **101 three-frame MPO files** and **11 single-frame JPEGs**, for **314 embedded views** in total. No SHA-256 duplicates were detected.

This structural consistency supports the presence of an image corpus associated with the publication, but does not confirm that the files originated from Air Tanzania's infrastructure, or establish initial access, exfiltration, encryption, the number of people represented or completeness of the claim. No OCR, facial processing, individual filename or personal content was reproduced. A minimised manifest is retained outside the repository at `/tmp/afrintel-evidence/afr-2026-09-airtanzania/evidence_manifest.json`.

#### 🇺🇬 Uganda - Armada Credit Bureau
- **Initial publication date:** September 24, 2026
- **Actor / Group:** Spirals
- **Sector:** Financial Services / Credit Bureau
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **Armada Credit Bureau Limited** describes itself as a Ugandan **credit-reporting and financial-analytics bureau** operating under the **Bank of Uganda** regulatory framework. Its business relates to creditworthiness information and credit-risk assessment services for authorised organisations. This description is based on its public website and is not independent verification of licensing or an incident ([Armada Credit Bureau website](https://www.armadacrb.com/)).

- **Independent verification as of 18 October 2026:** Only Armada Credit Bureau’s appearance on a Spirals leak-site listing is corroborated. No company statement or official Ugandan notice demonstrating intrusion was found.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 36306

Spirals published a claim targeting Armada Credit Bureau Limited, a Ugandan credit-reporting and analytics company. No independent evidence confirms compromise.

### September 25, 2026
#### 🇰🇪 Kenya - Majani Insurance Brokers
- **Initial publication date:** September 25, 2026
- **Actor / Group:** Vexy Ransomware
- **Sector:** Insurance
- **Website:** [majaninsure.com](https://majaninsure.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **Majani Insurance Brokers Limited** is a **Kenyan insurance brokerage** serving individuals and businesses. Its services include sourcing insurance cover, placing business with insurers, renewals and claims assistance. The broker reports several decades of experience in the market ([Majani official profile](https://majaninsure.com/about/)).

- **Independent verification as of 18 October 2026:** The Vexy claim against Majani Insurance Brokers is indexed in threat-intelligence databases without a public company acknowledgement or independent technical corroboration.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 36310

Vexy Ransomware published a claim targeting Majani Insurance Brokers, a Kenyan insurance broker. The vector, affected systems and any exfiltration remain unknown.

### September 26, 2026
#### 🇿🇦 South Africa - Guardrisk
- **Initial publication date:** September 26, 2026
- **Actor / Group:** TheGentlemen
- **Sector:** Insurance
- **Website:** [guardrisk.co.za](https://guardrisk.co.za/)
- **Status:** Third-Party Exposure Confirmed - Direct Breach Not Established
- **Incident type:** Data Leak (third-party exposure) / ransomware claim disputed
- **Description:** **Guardrisk** is a South African insurance group specialising in **risk-transfer and risk-financing solutions**, notably **cell-captive insurance** structures. It operates across life, non-life and customised commercial insurance arrangements. The Guardrisk name encompasses several regulated entities; the listing does not establish which one, if any, was affected ([Guardrisk official overview](https://guardrisk.co.za/about/)).

- **Independent verification as of 18 October 2026:** **Intermediary exposure acknowledged; direct Guardrisk breach denied:** on 30 September 2026 Guardrisk told MyBroadband that there was no indication of its systems or customer data being compromised. It linked the matter to exposure at binder holder **CoverCubed** affecting around **6,000 funeral policies**, stating that CoverCubed had notified clients and the regulator. **Do not attribute the data to a confirmed intrusion at Guardrisk.**

- **Additional verification sources:** [Source 1](https://mybroadband.co.za/news/security/669576-momentum-group-company-responds-to-data-breach-claims.html)

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 36351

TheGentlemen published a claim targeting Guardrisk, a South African insurance group. The publication provides organisational context but does not confirm access or the scope of held data.

### September 29, 2026
#### 🇿🇦 South Africa - BCX / Business Connexion
- **Initial publication date:** September 29, 2026
- **Actor / Group:** incransom
- **Sector:** Information Technology / Consulting
- **Website:** [bcx.co.za](https://www.bcx.co.za/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Description:** **BCX (Business Connexion)** is a South African **ICT services and systems-integration provider** within the **Telkom group**. It supports companies and public-sector clients with digital transformation, connectivity, infrastructure, cloud and IT services. Given its multi-client activities, a claim against BCX must not automatically be interpreted as a separate compromise of its customers ([BCX official profile](https://www.bcx.co.za/contact-us/)).

- **Independent verification as of 18 October 2026:** The INC Ransom listing naming BCX is reproduced by CTI platforms; no BCX or Telkom statement, regulatory filing or independent investigation confirming encryption, exfiltration or client compromise was found.

- **Sources / Evidence:** local AFRINTEL workbook, entry ID 36421

Incransom published a claim targeting BCX / Business Connexion and stated **500 GB**, 4,224,088 files and 596,613 folders, along with source code and business applications. These volumes and categories are actor claims; access, exfiltration and completeness are unconfirmed.

## Inter-month follow-up note

This note is not a new record and is excluded from the September incident count.

The [June 2026 Ministry of Education of Libya record](../../06-june/victims.md) documents a publication attributed to **EvaN47**, with a claimed volume of **287 GB**. A visual sample was examined at that time: a document gallery, secondary-education certificates, school and administrative documents, scanned images and PDFs, with references to national numbers, personal photographs and passport images. The analysis covered visible material; the claimed total volume and database completeness were not validated.

The **10 September 2026** publication, attributed to **EveN47**, subsequently claims **800 GB** for the moe.gov.ly database and approximately **300 GB** of similar data covering several Libyan education ministries. A local sample supplied as originating from this publication was nevertheless analysed in read-only mode: **900,976,395 bytes** (approximately **901 MB**), comprising **3,900 files** across four directories corresponding to passports (**1,145** files), national numbers (**467**), student photographs (**1,146**) and student certificates (**1,142**). Signatures identify 3,500 valid JPEGs and 4 valid PNGs; five files carrying a `.jpg` extension are actually PDFs and two others are HTML documents. The aggregate tree SHA-256 fingerprint is `d63371c3d61dd48c87398578d1bdfe4329c7dca1bc73104125e966221591df80`. SHA-256 checking found **169 duplicate groups** representing **213 excess files**, so the sample cannot be used to infer a unique count of people or documents. No bulk OCR or transcription of individual content was performed to limit exposure of personal data; the analysis covers the directory structure, signatures, technical metadata and integrity checks. This structure strengthens internal corroboration of the dataset's documentary and education-related nature, without validating the 287 GB, 800 GB or 300 GB claims. No download link was opened and no raw personal data is reproduced here. It is not established whether this represents an extension, republication, revised volume claim or a publication by a different alias. The 287 GB, 800 GB and 300 GB figures must not be added together; they remain separate dated threat-actor claims.
