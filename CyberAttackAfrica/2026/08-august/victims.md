![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in August 2026 (6 victims)

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

  The reviewed source is a post published on 7 August 2026 by the actor exfilar (VIP-tier forum account), titled "mpowa.mobi — 2,585 Youth CVs Exposed via 0day Firebase Scanner". The underlying Firebase Realtime Database export referenced in the post was also obtained independently. The actor states the platform's staging Firebase RTDB (staging.mpowa.mobi) was left publicly readable with no authentication, token or referer check, and that a proprietary scanning tool identified it.

  Examination of the exported database confirms the figures stated in the post: 2,585 complete CV/resume records, 26,675 service-delivery geolocation points, 11 service-provider directory records, 19 platform user accounts, and 3 API access-key entries. Each CV record includes a personal-information block (full name, phone, email, date of birth, gender, nationality, marital status, disability status, driver's license code, highest qualification), together with qualification, work-experience, language, skills and personal-reference sections; the reference entries additionally expose the name, employer, position and phone number of third parties named as referees. The 19 user records include full name, date of birth and geolocation coordinates for platform staff. The dataset also contains 3 live-looking API access keys with descriptive labels.

  The combination of disability status, date of birth and full identity data for named minors and young jobseekers constitutes special category personal information under South Africa's POPIA framework, and the exposure of a government-adjacent youth platform's staging database, including active API keys, creates a material risk of credential misuse against related infrastructure, in addition to identity fraud, targeted phishing and physical-safety risks for the affected youth and third-party references. The staging hostname suggests a corresponding production environment may exist and could carry similar or worse exposure. The exact match between the record counts published by the actor and those independently observed in the reviewed export supports a very high confidence assessment. No candidate name, contact detail, date of birth, disability declaration, reference information, staff record or API key from the reviewed material is reproduced.

  The full post identifies mpowa.mobi as item "11/25" of an ongoing campaign, describing a proprietary tool ("CredHarvest V6") used to mass-scan and harvest exposed Firebase Realtime Database instances, and states that hundreds of similar databases have already been acquired through the same method. The actor advertises both the sale of this scanning tool and separate paid intrusion/access services on the same forum. This indicates mpowa.mobi is one victim within a broader, systematic campaign targeting misconfigured Firebase deployments, and that comparable exposures likely affect other African organizations using the same backend, independent of any targeting specific to mpowa.mobi.

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

  **Observed:** The supplied screenshots show a publication attributed to incransom that names SpearFin Ltd, identifies `spearfin.net` and locates the target in Mauritius. The post is dated 18 August 2026 and claims that a leak occurred on 26 June 2026, with 416 GB of data obtained. It lists non-disclosure agreements, client correspondence, KYC material, identity documents, certificates, investment and shareholder records, AML audit material, agreements, application forms, bank statements, payroll, loan documents and registers of directors. The publication displays multiple document thumbnails presented as samples, including identity, corporate, administrative and financial material, and states that full publication is forthcoming. The assessment is limited to the supplied screenshots; the underlying documents were not accessed or downloaded.

  **Assumption:** The visible document set is broadly consistent with the activities attributed to a fund-administration and corporate-services provider, which supports a medium-confidence assessment that the claim is target-specific. If authentic, the combination of KYC, banking, payroll, corporate-governance and investment records would create a high risk of identity fraud, business email compromise, payment fraud, targeted phishing and compromise of third-party confidentiality. This assessment does not authenticate every thumbnail or establish the completeness of the claimed archive.

  **Unknown:** No independent evidence confirms unauthorised access, data exfiltration, ransomware encryption, operational disruption, the claimed 416 GB volume, the alleged 26 June 2026 leak date, the stated financial figures, or publication of a complete archive. No victim statement or independent technical evidence was supplied. The record therefore documents an observed ransomware-site publication with visible samples, not a confirmed compromise or confirmed full disclosure. Client names, identity documents, banking details and other personal or confidential data visible in the source are not reproduced.

## Notes (not counted in the monthly victim total)

### 17 August 2026
#### 🇰🇪 Kenya - Kenya Electricity Transmission Company (KETRACO), repost of a previously documented incident

- **Reference:** originally documented as a distinct incident on 31 December 2025, see `CyberAttackAfrica/2025/12-december/victims.md`.
- **Observation:** The same leaked sample (identical fields, same organisational-unit path "nl_KETRACO_Newsletter_Unit", and the same shared password-value anomaly across records) was observed republished on the DarkForums forum under the alias Linda2000, approximately eight months after the original RaidForums post attributed to LindaBF.
- **Assessment:** this is assessed as a repost of the same underlying dataset rather than a new compromise, and is not counted as an additional August 2026 incident. It indicates the data continues to circulate and may still be traded among threat actors. No username, email address, password value, download link or record from the sample is reproduced.
