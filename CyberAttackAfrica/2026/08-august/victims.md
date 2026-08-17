![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in August 2026 (4 victims)

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

  AFRINTEL reviewed a post published on 1 August 2026 on the DarkForums forum by the account NullsecNg (member since April 2026), titled "[SA] SOUTH AFRICA RESERVE BANK", signed by an individual using the alias "voss" on behalf of a group identifying as "NullSec Nigeria". The post is framed as retaliation for xenophobic violence against Nigerian and other non-South African nationals in South Africa and does not include a ransom demand, distinguishing it from a typical financially motivated extortion post.

  The post claims a "data leak" affecting the South African Reserve Bank and lists the following categories of material said to be included: employee details, access logs, vendor access logs, IT service tickets, and a category rendered as "transactional logo" in the original post (likely a typographical rendering of "transactional logs"). Four links to a third-party file-hosting service are provided; AFRINTEL did not access, download or verify the content behind these links, and no screenshot, data extract or other technical proof of the claimed intrusion is included in the post itself.

  AFRINTEL cannot independently confirm the alleged intrusion, the track record of the "NullSec Nigeria" persona, the authenticity of the linked files, or any connection between this claim and SARB's actual infrastructure. Given the claimed data categories and SARB's role as South Africa's central bank and a systemically important financial institution, a confirmed compromise would carry a high potential impact; at this stage, however, the claim rests on unverified forum assertions and unvalidated download links. AFRINTEL does not reproduce the download links or any other technical indicator from the post.

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

  AFRINTEL reviewed a post published on 16 January 2026 by the forum member OriginalCrazyOldFart (long-standing, high-reputation account), titled "Kenya & other countries Phones.7z FREE (has their names & cities too)". The post does not describe a claimed intrusion; it points to a publicly exposed cloud storage bucket indexed by the bucket-scanning service grayhatwarfare.com, and mirrors a 1.28 GB archive on a third-party file host. The poster states the material was not obtained through a breach they claim credit for, and warns that some of the links may already be broken, with no re-upload offered if that occurs.

  The described file alone contains 27,526 rows with a consistent Angaza-platform export schema: customer full name, phone number, city/region, financed product, daily installment price, cumulative amount paid, outstanding balance, account status, registration date, and the name and phone number of the assigned collection agent. A second file referenced in the same post, covering multiple countries beyond Kenya (including Uganda, Nigeria, Tanzania, Togo, Malawi, Zambia, Benin and Myanmar), follows a shorter schema of customer name, phone number and a numeric account/device identifier. AFRINTEL could not confirm whether all listed countries belong to a single multinational operator or to several distinct organizations sharing the same Angaza-based infrastructure, nor could it identify the specific commercial brand operating the Kenyan portion of the dataset from the material reviewed.

  The scale, structural consistency and plausibility of the sample rows support a high confidence assessment that genuine customer and financing records are exposed, independent of the unresolved question of the exact corporate identity. Given the volume, the combination of financial standing (amounts owed, payment history), personal contact details and named collection-agent assignments creates a significant risk of debt-collection-style fraud, impersonation of agents, phishing and harassment targeting financing customers across the affected countries. AFRINTEL does not reproduce any customer name, phone number, account identifier, address or financial figure from the reviewed material.

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

  AFRINTEL reviewed a post published on 7 August 2026 by the actor exfilar (VIP-tier forum account), titled "mpowa.mobi — 2,585 Youth CVs Exposed via 0day Firebase Scanner", and independently obtained the underlying Firebase Realtime Database export referenced in the post. The actor states the platform's staging Firebase RTDB (staging.mpowa.mobi) was left publicly readable with no authentication, token or referer check, and that a proprietary scanning tool identified it.

  AFRINTEL's review of the exported database confirms the figures stated in the post: 2,585 complete CV/resume records, 26,675 service-delivery geolocation points, 11 service-provider directory records, 19 platform user accounts, and 3 API access-key entries. Each CV record includes a personal-information block (full name, phone, email, date of birth, gender, nationality, marital status, disability status, driver's license code, highest qualification), together with qualification, work-experience, language, skills and personal-reference sections; the reference entries additionally expose the name, employer, position and phone number of third parties named as referees. The 19 user records include full name, date of birth and geolocation coordinates for platform staff. The dataset also contains 3 live-looking API access keys with descriptive labels.

  The combination of disability status, date of birth and full identity data for named minors and young jobseekers constitutes special category personal information under South Africa's POPIA framework, and the exposure of a government-adjacent youth platform's staging database, including active API keys, creates a material risk of credential misuse against related infrastructure, in addition to identity fraud, targeted phishing and physical-safety risks for the affected youth and third-party references. The staging hostname suggests a corresponding production environment may exist and could carry similar or worse exposure. The exact match between the record counts published by the actor and those independently observed in the reviewed export supports a very high confidence assessment. AFRINTEL does not reproduce any candidate name, contact detail, date of birth, disability declaration, reference information, staff record or API key from the reviewed material.

  The full post identifies mpowa.mobi as item "11/25" of an ongoing campaign, describing a proprietary tool ("CredHarvest V6") used to mass-scan and harvest exposed Firebase Realtime Database instances, and states that hundreds of similar databases have already been acquired through the same method. The actor advertises both the sale of this scanning tool and separate paid intrusion/access services on the same forum. This indicates mpowa.mobi is one victim within a broader, systematic campaign targeting misconfigured Firebase deployments, and that comparable exposures likely affect other African organizations using the same backend, independent of any targeting specific to mpowa.mobi.

## Notes (not counted in the monthly victim total)

### 17 August 2026
#### 🇰🇪 Kenya - Kenya Electricity Transmission Company (KETRACO), repost of a previously documented incident

- **Reference:** originally documented as a distinct incident on 31 December 2025, see `CyberAttackAfrica/2025/12-december/victims.md`.
- **Observation:** AFRINTEL observed the same leaked sample (identical fields, same organisational-unit path "nl_KETRACO_Newsletter_Unit", and the same shared password-value anomaly across records) republished on the DarkForums forum under the alias Linda2000, approximately eight months after the original RaidForums post attributed to LindaBF.
- **Assessment:** this is assessed as a repost of the same underlying dataset rather than a new compromise, and is not counted as an additional August 2026 incident. It indicates the data continues to circulate and may still be traded among threat actors. AFRINTEL does not reproduce any username, email address, password value, download link or record from the sample.

