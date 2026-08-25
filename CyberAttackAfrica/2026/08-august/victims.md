![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in August 2026 (9 victims)

👉🏾 [**French version available here**](./victims_FR.md)

## August 2026

### 01 August 2026
#### 🇿🇦 South Africa - South African Reserve Bank (SARB)

- **Initial publication date:** 01 August 2026
- **AFRINTEL detection date:** 15 August 2026
- **Actor / Group:** NullSec Nigeria (alias "voss", forum account NullsecNg), post published on the DarkForums cybercriminal forum
- **Sector:** Government / Central Banking / Financial Services
- **Website:** Not specified
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 4

- **Description:**

  The South African Reserve Bank (SARB) is South Africa's central bank, responsible for monetary policy, currency issuance and the stability of the national financial system.

- **Analysis:**

  The reviewed source is a post published on 1 August 2026 on the DarkForums forum by the account NullsecNg (member since April 2026), titled "[SA] SOUTH AFRICA RESERVE BANK", signed by an individual using the alias "voss" on behalf of a group identifying as "NullSec Nigeria". The post is framed as retaliation for xenophobic violence against Nigerian and other non-South African nationals in South Africa and does not include a ransom demand, distinguishing it from a typical financially motivated extortion post.

  The post claims a "data leak" affecting the South African Reserve Bank and lists the following categories of material said to be included: employee details, access logs, vendor access logs, IT service tickets, and a category rendered as "transactional logo" in the original post (likely a typographical rendering of "transactional logs"). Four links to a third-party file-hosting service are provided; the content behind these links was not accessed, downloaded or verified, and no screenshot, data extract or other technical proof of the claimed intrusion is included in the post itself.

  The available material does not independently confirm the alleged intrusion, the track record of the "NullSec Nigeria" persona, the authenticity of the linked files, or any connection between this claim and SARB's actual infrastructure. Given the claimed data categories and SARB's role as South Africa's central bank and a systemically important financial institution, a confirmed compromise would carry a high potential impact; at this stage, however, the claim rests on unverified forum assertions and unvalidated download links. The download links and other technical indicators from the post are not reproduced.


#### 🇪🇬 Egypt - Egyptian Football Association (EFA)

* **Initial publication date:** 26 July 2026 at 18:20 (timezone not shown)

* **AFRINTEL detection date:** 01 August 2026

* **Actor / Group:** Revesky, post published on a cybercriminal forum

* **Sector:** Sports / Federations

* **Website:** [efa.com.eg](https://www.efa.com.eg)

* **Status:** Claim - Data Sample Published

* **Incident type:** Data Leak

* **Confidence level:** High

* **Impact level:** Level 4

* **Description:**
  The Egyptian Football Association (EFA) is Egypt's national governing body responsible for the administration and organisation of football. It is affiliated with FIFA and the Confederation of African Football (CAF).

* **Analysis:**
  **Observed:** On 26 July 2026, the actor using the alias Revesky published a post claiming to have released "all the databases" belonging to the Egyptian Football Association. The publication claims a total dataset of approximately **9.6 GB** concerning around **350,000 players**.

  A collection of documents representing approximately **1.3 GB** was effectively disclosed by the actor. The reviewed material includes structured databases as well as administrative documents associated with players.

  AFRINTEL examined three CSV files originating from the available material. `data.csv` and `simple_famous_player.csv` contain the same set of **82 records across 31 columns**, while `simple_normal_player.csv` contains **802 records across 45 columns**. After removing the duplicated 82-record extract, the reviewed data therefore represents **884 rows from two distinct data extracts**.

  Observed fields include player identity information, national identification numbers, dates and places of birth, nationality, family information, teams, transfers, contracts, sporting seasons and various administrative information. Within the 802-record extract, **798 records contain a 14-digit numeric national identification number**.

  The documentary sample also contains several categories of files directly associated with EFA administrative processes, including EFA-branded player registration forms, copies of identification documents, birth certificates, professional player contracts, insurance certificates and educational documents. Some forms also contain photographs, signatures and fingerprint marks. These elements corroborate several of the data categories announced by Revesky.
  **Assumption:** The consistency between the structured databases, administrative documents and EFA branding supports a **high-confidence** assessment that the reviewed material originates from data associated with the federation. This assessment concerns the structural authenticity and attribution of the samples; it does not confirm how Revesky obtained them.

  **Unknown:** AFRINTEL has not validated the entire claimed **9.6 GB** volume or the figure of approximately **350,000 players**. The corpus effectively identified represents approximately **1.3 GB**, which is insufficient to confirm that all of the databases claimed by the actor were actually made public. The presence of military forms within the complete dataset was also not verified in the reviewed documents. The initial-access vector, extraction method, compromise timeline and any official confirmation by the EFA remain unknown.

  The observed information includes identity data, official documents, contractual information and records that may concern young players or minors, creating a significant risk of document fraud, identity theft, targeted phishing, social engineering and misuse of personal information. AFRINTEL does not reproduce any identity, national identification number, address, signature, photograph or other personal data contained in the reviewed material.


### 05 August 2026
#### 🇩🇿 Algeria - Ministry of Commerce

- **Initial publication date:** 05 August 2026
- **AFRINTEL detection date:** 05 August 2026
- **Actor / Group:** Florence, post published on a cybercriminal forum
- **Sector:** Government / Public administration / Commerce
- **Website:** Not specified
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Access Sale
- **Confidence level:** Low
- **Impact level:** Level 4

- **Description:**

  The Algerian Ministry of Commerce is the public administration responsible for national commerce policy, market regulation and related administrative services.

- **Analysis:**

  A forum post attributed to Florence advertises alleged VPN access to the Algerian Ministry of Commerce for USD 500. The seller describes the credentials as verified and does not provide a revenue figure. The publication does not expose the credentials, the access point, the affected account, the privileges available or technical evidence confirming that the access works.

  The advertised access could enable unauthorised entry into internal government services, follow-on reconnaissance, phishing, data access or lateral movement. The claim remains unverified, and no independent confirmation of the ministry, the VPN access or the credentials is available from the publication.

### 08 August 2026
#### 🇰🇪 Kenya - Unidentified PAYGO device financing platform (Angaza-based)

- **Initial publication date:** 16 January 2026
- **AFRINTEL detection date:** 08 August 2026
- **Actor / Group:** OriginalCrazyOldFart, repost on a cybercriminal forum of an exposed cloud storage bucket
- **Sector:** Financial Services / Consumer Device Financing (PAYGO) / Retail
- **Website:** Not identified with sufficient confidence
- **AFRINTEL status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4

- **Description:**

  The reviewed material describes Kenyan operations of an unidentified pay-as-you-go (PAYGO) consumer device financing platform built on the Angaza SaaS system, used to sell branded smartphones (Tecno Spark and Tecno Pop models observed) on installment plans through local field agents. The same archive reportedly contains data for parallel operations in at least a dozen additional markets across Africa and Asia.

- **Analysis:**

  The reviewed source is a post published on 16 January 2026 by the forum member OriginalCrazyOldFart (long-standing, high-reputation account), titled "Kenya & other countries Phones.7z FREE (has their names & cities too)". The post does not describe a claimed intrusion; it points to a publicly exposed cloud storage bucket indexed by the bucket-scanning service grayhatwarfare.com, and mirrors a 1.28 GB archive on a third-party file host. The poster states the material was not obtained through a breach they claim credit for, and warns that some of the links may already be broken, with no re-upload offered if that occurs.

  The described file alone contains 27,526 rows with a consistent Angaza-platform export schema: customer full name, phone number, city/region, financed product, daily installment price, cumulative amount paid, outstanding balance, account status, registration date, and the name and phone number of the assigned collection agent. A second file referenced in the same post, covering multiple countries beyond Kenya (including Uganda, Nigeria, Tanzania, Togo, Malawi, Zambia, Benin and Myanmar), follows a shorter schema of customer name, phone number and a numeric account/device identifier. The available material does not establish whether all listed countries belong to a single multinational operator or to several distinct organizations sharing the same Angaza-based infrastructure, nor does it identify the specific commercial brand operating the Kenyan portion of the dataset.

  The scale, structural consistency and plausibility of the sample rows support a high confidence assessment that genuine customer and financing records are exposed, independent of the unresolved question of the exact corporate identity. Given the volume, the combination of financial standing (amounts owed, payment history), personal contact details and named collection-agent assignments creates a significant risk of debt-collection-style fraud, impersonation of agents, phishing and harassment targeting financing customers across the affected countries. No customer name, phone number, account identifier, address or financial figure from the reviewed material is reproduced.

### 08 August 2026
#### 🇿🇦 South Africa - mpowa.mobi (Youth Services Platform)

- **Initial publication date:** 07 August 2026
- **AFRINTEL detection date:** 08 August 2026
- **Actor / Group:** exfilar, post published on a cybercriminal forum, operator/seller of a mass Firebase-scanning tool
- **Sector:** Youth Development / Employment Services (Government-adjacent)
- **Website:** [mpowa.mobi](https://mpowa.mobi) (exposed instance: staging.mpowa.mobi)
- **AFRINTEL status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4

- **Description:**

  mpowa.mobi is a South African government-adjacent youth development and employment platform connecting young jobseekers with opportunities and support services, reportedly developed as part of a Code for South Africa-linked initiative.

- **Analysis:**

  The reviewed source is a post published on 7 August 2026 by the actor exfilar (VIP-tier forum account), titled "mpowa.mobi - 2,585 Youth CVs Exposed via 0day Firebase Scanner". The underlying Firebase Realtime Database export referenced in the post was also obtained independently. The actor states the platform's staging Firebase RTDB (staging.mpowa.mobi) was left publicly readable with no authentication, token or referer check, and that a proprietary scanning tool identified it.

  Examination of the exported database confirms the figures stated in the post: 2,585 complete CV/resume records, 26,675 service-delivery geolocation points, 11 service-provider directory records, 19 platform user accounts, and 3 API access-key entries. Each CV record includes a personal-information block (full name, phone, email, date of birth, gender, nationality, marital status, disability status, driver's license code, highest qualification), together with qualification, work-experience, language, skills and personal-reference sections; the reference entries additionally expose the name, employer, position and phone number of third parties named as referees. The 19 user records include full name, date of birth and geolocation coordinates for platform staff. The dataset also contains 3 live-looking API access keys with descriptive labels.

  The combination of disability status, date of birth and full identity data for named minors and young jobseekers constitutes special category personal information under South Africa's POPIA framework, and the exposure of a government-adjacent youth platform's staging database, including active API keys, creates a material risk of credential misuse against related infrastructure, in addition to identity fraud, targeted phishing and physical-safety risks for the affected youth and third-party references. The staging hostname suggests a corresponding production environment may exist and could carry similar or worse exposure. The exact match between the record counts published by the actor and those independently observed in the reviewed export supports a very high confidence assessment. No candidate name, contact detail, date of birth, disability declaration, reference information, staff record or API key from the reviewed material is reproduced.

  The full post identifies mpowa.mobi as item "11/25" of an ongoing campaign, describing a proprietary tool ("CredHarvest V6") used to mass-scan and harvest exposed Firebase Realtime Database instances, and states that hundreds of similar databases have already been acquired through the same method. The actor advertises both the sale of this scanning tool and separate paid intrusion/access services on the same forum. This indicates mpowa.mobi is one victim within a broader, systematic campaign targeting misconfigured Firebase deployments, and that comparable exposures likely affect other African organizations using the same backend, independent of any targeting specific to mpowa.mobi.

### 08 August 2026
#### 🇳🇬 Nigeria - Daily Trust

- **Initial publication date:** 08 August 2026
- **Source detection date:** 08 August 2026, 19:21:01 (timezone not shown)
- **AFRINTEL detection date:** 11 August 2026
- **Actor / Group:** Panzer
- **Sector:** Media / Publishing / Broadcasting
- **Website:** [dailytrust.com](https://dailytrust.com)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4

- **Description:**

  Daily Trust is a Nigerian news and publishing organisation operated by Media Trust Limited. Its services include print and online journalism, Trust TV and Trust Radio.

- **Analysis:**

  **Observed:** An observed source record identifies Daily Trust, the Panzer criminal group, Nigeria and `dailytrust.com`, with a detection timestamp of 8 August 2026 at 19:21:01 and published data marked “N/D”. A separate Panzer listing dated 8 August claims 320 GB, offers a downloadable sample and displayed an active countdown with 17 days, 11 hours, 3 minutes and 44 seconds remaining when captured on 11 August. The exact deadline and timezone are not stated in the supplied material.

  AFRINTEL examined the complete supplied `sample.xlsx` workbook in read-only mode. The 44,996-byte file has SHA-256 `83516d93de48d2e53465071a418e50dd4b678baedef05277ab93ebb6f0034fa6` and contains two worksheets. The primary sheet contains 443 non-empty records under the fields Name, Email Address, New Password, Comments and Status. All 443 email-address cells use the victim's domain and are unique; 438 rows contain a value in the New Password field. The secondary sheet contains 19 target-domain address entries, 18 of which overlap the primary sheet, yielding 444 distinct target-domain addresses across the address fields. Neither sheet contains formulas or duplicate full rows. The workbook also contains 461 external HTTP hyperlinks pointing to the victim's domain; AFRINTEL did not follow them. An embedded `jsaProject.bin` component was identified but not executed. No name, email address, password value, comment, status value or hyperlink target from the sample is reproduced.

  **Assumption:** The structured account-reset schema, exclusive use of the victim's domain in the address fields, consistent cross-sheet relationships and target-domain hyperlinks provide high confidence that the sample is associated with Daily Trust. If the password values remain valid, the material could enable account takeover, business email compromise, impersonation, targeted phishing and access to confidential editorial, source or business communications. This assessment concerns the sample's structural authenticity and attribution; it does not confirm how Panzer obtained it.

  **Unknown:** AFRINTEL has not established whether the password values are current, temporary, previously used or already revoked, nor whether the workbook represents all Daily Trust accounts. The sample contains no reliable record-level date range and does not validate the claimed 320 GB volume. The initial-access method, extraction method, any encryption or operational disruption, the exact disclosure deadline, full-data publication, victim confirmation, negotiation, ransom payment and resale status remain unknown. The observed listing and coherent sample therefore do not constitute official confirmation of a ransomware intrusion or complete exfiltration.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-08T19:21:01
listing_last_observed_at: 2026-08-11T01:56:25+01:00
sample_status: sample-reviewed
deadline_at:
deadline_status: active
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-20T01:35:32+01:00
-->

### 16 August 2026
#### 🇿🇦 South Africa - The Courier Guy

- **Initial publication date:** Not specified
- **Source detection date:** 16 August 2026, 15:19:49 (timezone not shown)
- **AFRINTEL detection date:** 19 August 2026
- **Actor / Group:** medusalocker
- **Sector:** Logistics / Courier Services
- **Website:** [thecourierguy.co.za](https://thecourierguy.co.za)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2

- **Description:**

  The Courier Guy is a South African courier and logistics organisation. An observed source record attributes a ransomware-related entry concerning `thecourierguy.co.za` to medusalocker.

- **Analysis:**

  **Observed:** The supplied source record names “Thecourierguy”, identifies the criminal group as medusalocker, locates the target in South Africa and gives `thecourierguy.co.za` as the target domain. It displays a detection timestamp of 16 August 2026 at 15:19:49, without a visible timezone, lists published data as “N/D”, and claims that 2,018 emails were extracted. The record does not display a sample, publication deadline, ransom price or downloadable release.

  **Assumption:** The matching organisation name and domain support the assessment that the publication is target-specific. If the claim is accurate, a list of corporate or customer email addresses could facilitate phishing, business email compromise, credential attacks and impersonation. The screenshot alone does not establish that medusalocker obtained those addresses.

  **Unknown:** No visible sample corroborates the figure of 2,018 emails or establishes the nature, ownership, uniqueness or current validity of any alleged records. The publication date, initial-access and acquisition methods, encryption or operational disruption, victim confirmation, negotiation, ransom payment, disclosure and resale status remain unknown. This entry is separate from the incransom publication concerning SpearFin Ltd in Mauritius.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-16T15:19:49
listing_last_observed_at: 2026-08-19T05:35:53+01:00
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-19T05:35:53+01:00
-->

### 17 August 2026
#### 🇰🇪 Kenya - SnapStar Talent (snapstartalent.com)

- **Initial publication date:** 17 August 2026
- **AFRINTEL detection date:** 18 August 2026
- **Actor / Group:** exfilar, post published on a cybercriminal forum, operator/seller of a mass Firebase-scanning tool
- **Sector:** Human Resources / Recruitment
- **Website:** [snapstartalent.com](https://snapstartalent.com)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4

- **Description:**

  SnapStar Talent is presented in the observed publication as a Kenyan recruitment platform holding candidate profiles, job applications and employer-tenant records.

- **Analysis:**

  **Observed:** The assessment is based on the two sample files supplied with the publication rather than only on the forum screenshots. The CSV file contains 300 structurally valid application records across 36 columns, with no malformed rows or exact duplicate records; the TXT file contains 300 corresponding detailed blocks. All 300 application identifiers match between the two files in the same order, and every populated scalar field compared between the CSV and TXT representations is consistent. The sample covers 207 distinct candidate profiles and six employer values, with application timestamps ranging from 13 to 16 August 2026. The files contain repeated internal markers for the elevated-talent environment, while the TXT representation also contains repeated SnapStar Talent labels. Their SHA-256 hashes are 8b358e7efcebd5002687f6dab193be24cb7535ce77dec411359bf33ffd42a834 (CSV) and 31cfc806bd28aeab2d79dc23c07cff59c31881a120aa481edfd192b09c403741 (TXT).

  At unique-profile level, all 207 profiles contain an email address, telephone number, date of birth, salary value and CV URL. National identity numbers are present for only 11 profiles (5.3%), video-interview URLs for 50 profiles (24.2%) and profile photographs for 41 profiles (19.8%). Reference data is also present: 87 profiles contain a reference name, 61 a reference email address and 74 a reference telephone number. One date of birth is objectively implausible because it yields an age of zero years. The sample therefore does not support the actor's broad suggestion that every candidate record contains a national identity number or video interview.

  The application-level export contains 299 CV URLs representing 209 distinct links and 78 video URLs representing 57 distinct links. All observed CV and video links use Firebase Storage and contain token-bearing media parameters. These URLs were not queried and the linked documents were not retrieved, so their current validity is not established. Repeated applications belonging to the same profile are internally consistent for email, telephone, date of birth and national identity number; one profile contains a name variation and two profiles contain more than one CV URL, which is compatible with ordinary profile or document updates rather than wholesale inconsistency.

  **Assumption:** The exact CSV-to-TXT correspondence, coherent application/profile relationships, target-specific internal markers, recent timestamps and consistent Firebase Storage structure provide high confidence that the sample is a genuine recruitment-platform dataset linked to the elevated-talent/SnapStar Talent environment. The sample materially supports the claim that candidate identity, contact, employment, compensation, CV, video and third-party reference data were exposed or made available to the actor. It does not validate the advertised full-dataset totals. The verified sample alone creates a high risk of recruitment fraud, targeted phishing, impersonation, identity misuse and privacy harm; token-bearing CV and video links create an additional document-access risk if they remain active.

  **Unknown:** The available material does not independently verify the alleged unauthenticated Firestore access, the actor's extraction method, the claimed totals of 93,462 profiles, 83,237 applications and 176,795 documents, the 249.1 GB file volume, the presence of 83 tenant employers in the full dataset, or any response from SnapStar Talent. The 300 newest applications are a non-random sample and their field-completeness rates cannot be extrapolated to the entire advertised dataset. The incident therefore remains classified as a claim with a published sample, not as confirmation that the complete backend was extracted. Personal records, download URLs, URL tokens, payment instructions and actor contact details are not reproduced.

### 18 August 2026
#### 🇲🇺 Mauritius - SpearFin Ltd

- **Initial publication date:** 18 August 2026
- **AFRINTEL detection date:** 18 August 2026
- **Actor / Group:** incransom
- **Sector:** Financial Services / Fund Administration / Corporate Services
- **Website:** [spearfin.net](https://spearfin.net)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 4

- **Description:**

  SpearFin Ltd is presented in the observed publication as a Mauritius-based provider of fund-administration, corporate, compliance and investor-relations services. The source also claims USD 10 billion in assets under administration and USD 30 million in revenue; those figures have not been independently verified.

- **Analysis:**

  **Observed:** The supplied screenshots show a publication attributed to incransom that names SpearFin Ltd, identifies `spearfin.net` and locates the target in Mauritius. The post is timestamped 18 August 2026 at 09:35, without a visible timezone, and claims that a leak occurred on 26 June 2026, with 416 GB of data obtained. It lists non-disclosure agreements, client correspondence, KYC material, identity documents, certificates, investment and shareholder records, AML audit material, agreements, application forms, bank statements, payroll, loan documents and registers of directors. It also claims USD 10 billion in assets under administration and USD 30 million in revenue. These figures have not been independently verified.

  The publication displays multiple document thumbnails presented as samples, including identity, corporate, administrative and financial material. One enlarged sample is a seven-section contributor confirmation/acknowledgment annex dated in June 2026. The visible text contains a Mauritius registered-office reference, a seven-figure USD capital commitment, and clauses covering unit class, management fees, operating expenses, hurdle rate and performance fees; a corporate seal is partly visible. These structural elements are consistent with fund-administration and investment documentation. Names, addresses, exact financial amounts, identity documents and other confidential values visible in the samples are not reproduced. The publication states that full disclosure is forthcoming. Analysis is limited to the data visible in the provided sample; the original source files were not available, accessed or downloaded.

  **Assumption:** The combination of target-specific publication details, a Mauritius-linked contractual sample, coherent investment-fund terminology, recent contractual dates and multiple document categories supports a medium-confidence assessment that at least part of the visible material is associated with the services attributed to SpearFin. If authentic, the combination of KYC, identity, banking, payroll, corporate-governance and investment records would create a high risk of identity fraud, business email compromise, payment fraud, targeted phishing and compromise of client and investor confidentiality. This assessment does not authenticate each thumbnail, signature or seal and does not establish how the material was obtained.

  **Unknown:** Because the original files are unavailable, AFRINTEL could not examine metadata, signatures, seals, document completeness, duplicate rates, internal consistency across the full sample set or possible manipulation. No independent evidence confirms unauthorised access, data exfiltration, ransomware encryption, operational disruption, the claimed 416 GB volume, the alleged 26 June 2026 leak date, the stated financial figures or publication of a complete archive. No victim statement or independent technical evidence was supplied. The record therefore documents an observed incransom publication with visible samples concerning a distinct Mauritian victim, not a confirmed compromise or confirmed full disclosure.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-18T09:35:00
listing_last_observed_at: 2026-08-18T21:15:30+01:00
sample_status: preview-visible
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-19T06:02:04+01:00
-->

### August 20, 2026
#### 🇩🇿 Algeria - Afribaba (dz.afribaba.com)

- **Initial publication date:** August 20, 2026
- **AFRINTEL detection date:** August 20, 2026
- **Actor / Group:** TelephoneHooliganism, post published on a cybercriminal forum
- **Sector:** E-commerce / Marketplace
- **Website:** [dz.afribaba.com](https://dz.afribaba.com) (observed regional site); actor-cited domain: www.afribaba.dz
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:**

  Afribaba is a classifieds marketplace for individuals and businesses in Algeria. Public sources consulted describe the regional service under dz.afribaba.com; the actor's post instead cites www.afribaba.dz.

- **Analysis:**

  **Observed:** The August 20, 2026 post attributed to TelephoneHooliganism claims to offer approximately 642,000 verified retail contacts, including phone numbers, order history and support tickets, for a negotiable USD 1,400. It describes three export sections and displays several sample links that AFRINTEL did not follow. The local file supplied is only Order_History_Algeria.csv, 5,123 bytes, with 20 data rows and 32 columns. Its SHA-256 is 6c5ecf4641436931b8dd5036a13300ffb04c38f6d2c275cb4c5172d02bffe196.

  Full analysis of the CSV found 20 structurally readable rows, no duplicate full row, but only two distinct order_id values, with 18 repeated order identifiers. Order dates range from March 2022 to September 2024. Observed order statuses are Completed (9), Pending (4), Processing (4), and Canceled (3); payment statuses are Paid (12), Pending (5), and Refunded (3). All monetary fields use USD; observed amounts total USD 4,453.55, without assuming what this small sample represents commercially.

  **Assumption:** The cited domain, post title, and order-export structure are compatible with a claim involving the Afribaba ecosystem. However, the shipping countries are Brazil (13 rows), Bulgaria (2), Cambodia (2), Cameroon (2), and Brunei (1), with no Algerian shipping row. This conflicts with the “Algeria” label and prevents firm attribution of the extract to the Algerian scope or to Afribaba. The sample may represent a multi-country environment, demonstration data, an attribution error, or an excerpt whose context is incomplete.

  **Unknown:** AFRINTEL did not receive the advertised Customer Contacts or Support Tickets tables, nor the approximately 642,000-contact archive. Sample links were not followed; no phone number, name, address, customer identifier or ticket is reproduced; and no Afribaba confirmation is available. The supplied file cannot confirm the claimed volume, technical origin, data validity, access method, exposure of phone numbers or asking price.

### August 22, 2026
#### 🇲🇦 Morocco - RAMED (Régime d’Assistance Médicale)

- **Actor / Group:** JBT2026
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Website:** Not specified in the provided material

- **Description:**
  RAMED, the Medical Assistance Scheme, is Morocco's former public program designed to facilitate access to healthcare for low-income and vulnerable populations. The observed publication concerns a database presented as being associated with beneficiaries of this scheme.

- **Analysis:**
  On August 22, 2026, actor JBT2026 published on an underground forum data presented as originating from the RAMED system. The actor claims to possess more than **17 million entries** and states that approximately **1 million entries** have been released, with the stated intention of publishing the entire database later.

  Analysis of the main provided file identified **1,098,685 records** across **17 columns**, with a size of approximately **183.1 MB**. The data includes administrative identifiers, first and last names in Latin and Arabic characters, sex, dates of birth, CIN national identity numbers when available, and geographic and administrative information.

  Additional material strengthens the consistency of the publication. Four supplementary CSV files contain **10 records**, all of which were found identically in the main dataset. Seven passport-style portrait photographs were also provided; each corresponds, through its filename, to an individual present in the structured data.

  These elements now establish the presence of **identification photographs associated with some records in the analyzed sample**. They strengthen the consistency of the actor's claim regarding the existence of photographs, but do not establish that all of the more than 17 million claimed records include an image.

  Of the **1,098,685 records**, **666,103** contain a value in the CIN field, while **432,582**, approximately **39.4%**, do not. Full-format dates of birth are available for **842,259 records**, while **256,426** contain partial values.

  The combination of structured identity data, CIN numbers and identification photographs significantly increases the potential risk of **identity theft, document fraud, targeted phishing and correlation with other compromised datasets**.

  The structure of the data, its bilingual content, Moroccan administrative references and the correspondence between some records and the photographs strengthen the consistency of the sample with data concerning beneficiaries in Morocco.

  **Evidence limitations:** the analyzed material does not confirm the exact originating technical system, initial access vector, extraction method, actual possession of the more than 17 million claimed entries, or any official confirmation of the incident by a Moroccan institution. The presence of photographs is established only for the provided material and must not be extrapolated to the entire claimed database.
---
### August 24, 2026

#### 🇲🇦 Morocco - General Directorate of National Security (DGSN) / General Directorate for Territorial Surveillance (DGST)

* **Initial publication date:** August 24, 2026

* **AFRINTEL detection date:** August 24, 2026

* **Actor / Group:** JabaR00t, publication relayed by the JBT2026 account on a cybercriminal forum

* **Sector:** Government / Administration / Security and Intelligence

* **Website:** [dgsn.gov.ma](https://dgsn.gov.ma) / `dgst.gov.ma` (domain associated with the DGST, public institutional portal not confirmed)

* **AFRINTEL status:** Data Fully Published

* **Incident type:** Data Leak

* **Confidence level:** High

* **Impact level:** Level 4

* **Description:**

  The General Directorate of National Security (DGSN) is Morocco's national police force. The General Directorate for Territorial Surveillance (DGST) is the Moroccan service responsible for domestic intelligence and territorial security. Both institutions have strategic roles within Morocco's national security apparatus.

* **Analysis:**

  **Observed:** On August 24, 2026, a publication relayed by the JBT2026 account and attributed to JabaR00t presented, under the `#OP_CEUTA` label, a database described as containing approximately **70,000 personnel associated with the DGSN and DGST**. The actor presents this database as having been fully published while also claiming that the released data represents only part of a larger dataset allegedly exfiltrated.

  Analysis of the provided files identifies **70,381 records** in the main dataset. The observed data includes identity information, PPR numbers, CIN/CNI national identity numbers, dates of birth and recruitment years.

  Three additional files contain respectively **8,789**, **1,456** and **21 records**. They include information relating to ranks and RIB bank account details. Several overlaps exist between these datasets; their volumes should therefore not be added to the 70,381 records in the main dataset as if they represented independent populations.

  The correspondence between the **70,381 records** actually observed and the public claim of a database containing approximately 70,000 individuals is an important consistency indicator. The different files also show mutually compatible structures and administrative data consistent with the Moroccan context.

  **Assumption:** The structural consistency of the corpus, the administrative information observed and the overlaps between several files support a **High confidence** assessment that the published data is associated with personnel within the DGSN/DGST ecosystem. This assessment concerns the attribution and consistency of the examined data; it does not confirm the method used by JabaR00t to obtain it.

  The `Data Fully Published` status applies to the database of approximately 70,000 records that the actor presents as having been released in full. It does not mean that all other data JabaR00t claims to have exfiltrated has been made public or verified.

  The combination of identity information, administrative identifiers, professional information, ranks and banking details represents a **critical impact level**. It may facilitate identity theft, financial fraud, spear-phishing, targeted social engineering and personnel mapping. In the context of police and intelligence organizations, the exposure also creates operational security, personnel profiling and counterintelligence concerns.

  **Unknown:** The available evidence does not establish the initial access vector, the affected source systems, the extraction method, the exact date on which the data was acquired or the overall scope of the information the actor claims to have obtained. The analyzed files alone also do not establish that each of the 70,381 records represents an active intelligence officer, nor do they determine the exact distribution of records between the DGSN and DGST.

  No independent public confirmation from the DGSN or DGST regarding the entirety of the claimed compromise is established by the analyzed material. AFRINTEL does not reproduce any names, PPR numbers, CIN/CNI numbers, RIB bank details, dates of birth or other personal data contained in the examined files.

