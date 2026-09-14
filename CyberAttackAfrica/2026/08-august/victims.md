![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Leak-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in August 2026 (29 records)

👉🏾 [**French version available here**](./victims_FR.md)

## August 2026

### 01 August 2026

#### 🇪🇬 Egypt - Egyptian Local Services Portal (probable attribution)

* **Initial publication date:** 5 June 2026
- **AFRINTEL detection date:** 1 August 2026
* **Actor / Group:** R3D3MPTION
* **Sector:** Government / Administration
* **Website:** [lgs.gov.eg](https://www.lgs.gov.eg/)
* **Status:** Claim - Data Sample Published
* **Incident type:** Data Leak
* **Confidence level:** High
* **Impact level:** Level 4
* **Source type:** Underground Forum - Direct AFRINTEL Observation
* **Victim Description:**
  The Egyptian Local Services Portal, `lgs.gov.eg` (بوابة خدمات المحليات), is a government platform providing citizens and businesses with access to various local administrative services online. The portal is part of the digitization of services delivered by governorates, cities and local technology centers across Egypt. Attribution of the incident to this platform is assessed as probable based on the convergence between the analysed data schema, the published documents and the known functions of the portal.

* **Analysis:**
  On 5 June 2026, actor R3D3MPTION published an offer claiming to have compromised an Egyptian government service related to local services. The actor claims possession of more than **70 GB of documents**, more than **5 GB of personal data**, and a `CITIZENS.CSV` file containing **13,117,317 records**. The publication also references datasets related to users, vehicles and companies, as well as approximately **118,000 citizen documents**, described by the actor as identity images, contracts and other administrative documents. These overall volumes remain actor claims and have not been validated.

  The provided and analysed `citizens_sample.csv` contains **9,938 records and 42 columns**, representing **9,933 distinct citizen identifiers**. The analysis identifies structured information including names, national identifiers, passport identifiers, addresses, dates of birth, contact information, nationality and civil-status information, professional data, disability-related information and several administrative identifiers. Of the **9,805 populated national identifier values**, **9,408** contain 14 digits, consistent with the format used for Egyptian national identifiers.

  The analysed dataset also contains recent application timestamps. The `InsertDate` field is populated for **9,435 records**, including **3,544** dated **3 June 2026** and **778** dated **2 June 2026**. These values suggest that some records present in the sample were still being populated shortly before the 5 June publication. They do not, however, establish the date of initial access, exfiltration or compromise.

  Documents visible in the publication include Egyptian identity documents, administrative forms, plans, property-related documents and various records associated with local administrative procedures. The combination of these documents with the citizen-data structure and the announced `Users`, `Cars` and `Companies` datasets is strongly functionally consistent with the Egyptian Local Services Portal ecosystem. This convergence supports a **probable attribution to `lgs.gov.eg` or an associated back-end infrastructure**, but does not constitute official confirmation that the platform was compromised.

  The analysed sample represents approximately **0.076%** of the claimed 13,117,317 records. It therefore cannot validate the completeness of the announced dataset, the claimed **70+ GB of documents**, **5+ GB of PII**, or approximately **118,000 documents**. The initial access vector, systems actually affected, exfiltration method and full scope of the incident remain unknown.

  The sensitivity of the observed data, its administrative nature, the presence of identity documents and the potentially national scope justify an **Impact Level 4** assessment. Primary risks include identity theft, document fraud, highly contextualized spear-phishing and cross-correlation of exposed administrative information.

* **Recommendations:**

  * Review application, IAM, API, database and storage logs for bulk extraction, abnormal queries or unusual access preceding 5 June 2026, with particular attention to 2 and 3 June.
  * Increase monitoring of administrative and technical accounts, reassess access rights to citizen data, and implement detection controls for bulk exports, unusual API activity and outbound transfers of sensitive documents.



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



#### 🇩🇿 Algeria - Directorate-General for Scientific Research and Technological Development (DGRSDT)

- **Incident date:** 8 July 2026 (date supplied for the incident; initial access date not established)
- **Initial publication date:** 8 July 2026 at 18:33 (timezone not shown)
- **AFRINTEL discovery date:** 1 August 2026
- **Actor / Group:** anisanas2
- **Sector:** Government / Scientific research
- **Website:** [dgrsdt.dz](https://www.dgrsdt.dz/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Underground Forum and Messaging Channel - Direct AFRINTEL Observation
- **Public sources:** [Official DGRSDT profile](https://www.dgrsdt.dz/public/index.php/fr/about_dgrsdt)

- **Victim Description:**

  The Directorate-General for Scientific Research and Technological Development (DGRSDT) is an Algerian government directorate operating under the authority of the minister responsible for scientific research. It implements national scientific research and technological development policy, including research programming, evaluation, university research, human resources and programme funding.

- **Analysis:**

  **Observed:** The observed publication, attributed to anisanas2, is dated 8 July 2026 at 18:33 according to the visible timestamp. It claims a compromise of DGRSDT and offers a dataset described as containing government identifiers for doctoral researchers and scientists, personal information, enrolment certificates, selfies and doctoral project files. The advertised price is **USD 800**; the publication claims **6,000 identifiers** and **6,000 profiles**. These figures and the compromise remain actor claims.

  The supplied CSV, analysed in full, contains **1,000 records and 29 columns** with a consistent row width. It includes fields relating to researchers, supervisors, institutions, degrees, situations, contact details and national identifiers. **Sixteen rows are exact duplicates beyond the first occurrence.** Populated national-identifier fields are predominantly 18 digits in both profile blocks; no personal value is reproduced here.

  The profiles archive contains **4,123 files**, representing approximately **2.46 GB** uncompressed. Hash analysis identifies **2,185 unique contents**, with **1,938 exact duplicate files** beyond the first occurrence. File signatures are predominantly images; 3,950 image files were verified by reading, while 172 could not be validated by the image library used. The certificates archive contains **100 files**, comprising 51 PDFs and 49 images across 58 PDF pages; no file is encrypted and no exact duplicate was detected.

  Profile-archive filenames match CSV names or identifiers for **1,042 files and 444 rows**. In the certificates archive, **25 files** match names present in **26 CSV rows**. These matches, the field structure, the documents and the visual elements associated with the publication support a high-confidence assessment of the sample's structural authenticity and attribution to data linked to DGRSDT.

  **Assumption:** The consistency between DGRSDT's official mission, the doctoral CSV schema, the certificates, profile imagery and filename matches makes association of the corpus with the DGRSDT ecosystem plausible. It does not establish the access vector, extraction or official confirmation of the organisation's compromise.

  **Unknown:** The actual number of affected people, completeness of the full dataset, validity of the claimed **6,000 profiles**, access date and method, affected systems, exfiltration, operational impact, victim confirmation and disclosure of the full set remain unknown. The archives were examined locally in read-only mode; no raw personal data is published. Analysis of visual documents is limited by the 172 image files that could not be validated and by the absence of a French or Arabic OCR model in the available environment.


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


### 02 August 2026

#### 🇿🇦 South Africa - Buzz Trading 104

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 02 August 2026 at 13:26:24 (timezone not shown)
- **Actor / Group:** krybit
- **Sector:** Plastics manufacturing / Housewares
- **Website:** [buzztrading104.co.za](https://buzztrading104.co.za/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Public sources:** [Buzz Trading 104 overview](https://buzztrading104.co.za/about-buzz-trading/) | [Official website](https://buzztrading104.co.za/)

- **Description:**

  Buzz Trading 104 is a South African manufacturer of injection-moulded plastic products and related consumer and industrial goods, operating since 2003. Its portfolio includes housewares and storage, outdoor products, industrial wheelie bins, children's furniture, plastic packaging and aluminium ladders.

- **Analysis:**

  **Observed:** The supplied source record associates krybit with Buzz Trading 104, locates the target in South Africa and cites www.buzztrading104.co.za. It is timestamped 2 August 2026 at 13:26:24, with no timezone shown. No sample, volume, disclosure deadline, data category or technical evidence of compromise is provided.

  **Assumption:** The domain matches the company's public website, making the target identification plausible. This does not confirm unauthorised access, exfiltration or encryption.

  **Unknown:** The date and method of initial access, affected systems, any operational impact, the nature of any data obtained, victim confirmation, negotiations, ransom payment and resale remain unknown.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-02T13:26:24
listing_last_observed_at: 2026-08-02T13:26:24
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-02T13:26:24
-->

#### 🇳🇬 Nigeria - ASHA Microfinance Bank Limited (ASA Nigeria)

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 02 August 2026 at 14:24:27 (timezone not shown)
- **Actor / Group:** krybit
- **Sector:** Microfinance / Banking
- **Website:** [nigeria.asa-international.com](https://nigeria.asa-international.com/)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Public sources:** [Institutional overview](https://nigeria.asa-international.com/about-us/) | [At-a-glance profile](https://nigeria.asa-international.com/about-us/at-a-glance/) | [Report on the KRYBIT claim](https://www.dexpose.io/krybit-ransomware-strikes-asha-microfinance-bank-in-nigeria/)

- **Description:**

  ASHA Microfinance Bank Limited, or ASA Nigeria, is a Nigerian deposit-taking microfinance bank and a subsidiary of ASA International. It began operations in 2010 and provides small, socially responsible loans primarily to low-income female entrepreneurs under a nationwide microfinance banking licence.

- **Analysis:**

  **Observed:** The source record associates KRYBIT with ASHA Microfinance Bank and was observed on 2 August 2026 at 14:24:27, with no timezone shown. The supplied corpus is attributed to KRYBIT's data disclosure. According to provenance information supplied with the corpus, the disclosure followed failed negotiations between the two parties; this sequence has not been independently corroborated by a public source. A read-only analysis of the complete directory found 1,498 files (about 7.15 GB): 1,101 contain only null bytes and 397 contain non-null data. Sixteen text tables account for approximately 14.6 million physical lines; 5,164 lines were sampled and eight width irregularities were observed. The corpus also contains spreadsheets, office documents and RTF files; several archives are damaged or unreadable. Readable material contains finance- or transaction-related fields and contact-pattern matches in some files. Structured dates observed range from 27 April 2022 to 16 July 2026.

  **Assumption:** The collection path, associated domain and structured nature of the corpus are consistent with ASHA. However, the readable documents do not all contain an explicit institutional marker. Physical lines do not necessarily represent unique records or distinct customers. If the financial or customer data is authentic, it could support targeted phishing, identity abuse and fraud.

  **Unknown:** The initial access method and date, affected systems, encryption mechanism, completeness of the corpus, number of unique records and operational impact are not established. No official confirmation of the incident has been observed. The negotiation status remains publicly uncorroborated; no payment or transfer to a third party is established.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-02T14:24:27
listing_last_observed_at: 2026-08-02T14:24:27
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: release-reviewed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-13T02:32:51Z
-->

#### 🇿🇦 South Africa - DC Partner

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 02 August 2026 at 14:25:08 (timezone not shown)
- **Actor / Group:** krybit
- **Sector:** Financial services / Payment distribution / Debt counselling support
- **Website:** [dcpartner.co.za](https://www.dcpartner.co.za/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Public sources:** [DC Partner official website](https://www.dcpartner.co.za/)

- **Description:**

  DC Partner (Pty) Ltd is a South African Payment Distribution Agency (PDA) based in George, Western Cape. Its public profile describes it as one of South Africa's four National Credit Regulator-accredited PDAs and says it collects and distributes debt-review funds on behalf of debt counsellors for consumers under review, in line with the National Credit Act. The company also describes DebiCheck services integrated with FNB, its Finwise Debt Management software, reporting and metrics, provider verification and nationwide representative support. Its profile says it serves hundreds of debt counsellors and employs more than 65 people.

- **Analysis:**

  **Observed:** The source record associates krybit with DC Partner, locates the target in South Africa and cites www.dcpartner.co.za. It was recorded on 2 August 2026 at 14:25:08, with no timezone shown. The public profile describes debt-review fund distribution and related payment and management services. Monitoring information reported on 13 September 2026 says the displayed disclosure deadline had passed, but no DC Partner data was publicly accessible at the latest reported check. The exact deadline and the date and time of that check were not provided. No sample, volume, data category or technical evidence is available to substantiate the claim.

  **Assumption:** The domain and public profile make the target identification plausible, but do not confirm a compromise. If debt-review or payment-related data had been exfiltrated, it could create fraud and targeted-phishing risks; no such exposure has been established. The absence of accessible publication after the deadline does not establish its cause. Possible scenarios include a settlement, potentially involving a ransom payment by the victim, or negotiations still ongoing after the deadline; transfer, sharing or resale to another criminal group, a third party or a CTI organisation; delayed or unavailable publication; or an inaccurate or exaggerated claim. None is corroborated by the available evidence.

  **Unknown:** The exact deadline, time of the latest check, potentially affected systems, access vector, unauthorised access, exfiltration, ransomware execution or encryption, operational impact, victim confirmation and the nature or extent of any data remain unknown. Negotiations, payment, private sharing or resale have not been established.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-02T14:25:08
listing_last_observed_at: 2026-08-02T14:25:08
sample_status: none-observed
deadline_at:
deadline_status: expired
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-13
-->

### 04 August 2026


#### 🇿🇦 South Africa - Sure Travel

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 04 August 2026 at 15:50:57 (timezone not shown)
- **Actor / Group:** Orova
- **Sector:** Travel agency / Leisure and corporate travel
- **Secondary source-dataset reference:** emis.com/.../Sure_Travel_Company_Limited (Hong Kong-registered namesake)
- **Website:** [suretravel.co.za](https://www.suretravel.co.za/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 2
- **Public sources:** [Sure Travel overview](https://www.suretravel.co.za/about) | [Institutional profile](https://www.linkedin.com/company/sure-travel-pty-ltd)

- **Description:**

  Sure Travel (Pty) Ltd is a Southern African travel-agency brand providing leisure and corporate travel services. Its website states that the network has operated for more than 30 years and includes more than 80 agencies across South Africa, Namibia and Botswana.

- **Analysis:**


  **Observed:** The victim listing was directly verified on the Orova group's leak site. It identifies Sure Travel as a South African victim, with a timestamp of 4 August 2026 at 15:50:57. The source dataset also contains a secondary URL pointing to a namesake company registered in Hong Kong; this inconsistent reference is not used for geographic attribution. No data sample was available in the supplied material.

  **Assumption:** The publication may correspond to an extortion operation targeting the organisation, but it does not by itself confirm encryption, exfiltration or operational disruption.

  **Unknown:** Initial access, affected systems, any data obtained, whether encryption occurred, operational impact and confirmation by the victim remain unknown.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-04T15:50:57
listing_last_observed_at: 2026-08-04T15:50:57
sample_status: none-observed
deadline_at:
deadline_status: unknown
disclosure_status: unknown
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-04T15:50:57
-->


#### 🇪🇬 Egypt - ADG Healthcare

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 04 August 2026 at 15:55:39 (timezone not shown)
- **Actor / Group:** Orova
- **Sector:** Pharmaceutical manufacturing
- **Domain also cited in the source dataset:** www.adg-healthcare.com
- **Website:** [adghealthcare-eg.com](http://www.adghealthcare-eg.com)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Public sources:** [Institutional profile](https://www.linkedin.com/company/adg-healthcare) | [Business reference](https://www.bizmideast.com/EG/adg-healthcare-02-22571600)

- **Description:**

  Public information about Cairo-based ADG Healthcare associates it with Advocure Pharma Group, an Egyptian pharmaceutical business active in areas including cardiovascular, genito-urinary and anti-infective products. Its public profile points to adghealthcare-eg.com.

- **Analysis:**


  **Observed:** The victim listing was directly verified on the Orova group's leak site. It identifies ADG Healthcare as an Egyptian victim, with a timestamp of 4 August 2026 at 15:55:39. The source dataset cites www.adg-healthcare.com, while the company's public profiles point to adghealthcare-eg.com; this domain discrepancy remains documented. No data sample was available in the supplied material.

  **Assumption:** The publication may correspond to an extortion operation targeting the organisation, but it does not by itself confirm encryption, exfiltration or operational disruption.

  **Unknown:** The technical domain actually targeted, initial access, affected systems, the nature of any data obtained, whether encryption occurred, possible disruption and confirmation by the organisation remain unknown.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-04T15:55:39
listing_last_observed_at: 2026-08-04T15:55:39
sample_status: none-observed
deadline_at:
deadline_status: unknown
disclosure_status: unknown
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-04T15:55:39
-->

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

### 07 August 2026

#### 🇿🇦 South Africa - Serengeti Golf and Wildlife Estate

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 07 August 2026 at 02:25:08 (timezone not shown)
- **Actor / Group:** krybit
- **Sector:** Real estate / Residential estate and golf
- **Website:** [serengeti-estates.co.za](https://serengeti-estates.co.za/)
- **Domain cited by the source dataset:** www.serengetiestates.co.za
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Public sources:** [Official website and contact information](https://serengeti-estates.co.za/contact-us/)

- **Description:**

  Serengeti Golf and Wildlife Estate is a luxury residential and golf estate in Kempton Park, Gauteng, near Johannesburg and OR Tambo International Airport. The estate combines residential property, golf and lifestyle facilities.

- **Analysis:**

  **Observed:** The local dossier associated with the publication contains 21 artefacts: 8 JPG, 5 XLSX, 1 XLS, 3 PDF, 3 DOCX and 1 PPTX. The five XLSX workbooks were opened read-only and contain 54 sheets and 53,927 non-empty cells. They contain 1,643 formula cells, which were not executed, and no external links were detected. The readable contents cover housekeeping schedules and hours, waiter rotations, purchase requisitions and a booking template, spanning periods from 2017 to 2020. The three DOCX files include a service-period procedure, a painting document and a booking template with seven tables. The PDFs are scanned documents; the JPG images and one-slide presentation did not permit complete text qualification. SHA-256 hashes for all 21 artefacts were calculated locally and retained outside the repository.

  **Assumption:** The consistency of schedules, procedures, purchase forms, booking material and visual assets with the activity of a residential and golf estate makes association of the corpus with the victim's environment plausible. The sample is sufficiently structured to increase confidence in its authenticity and attribution, but it does not confirm the access vector, exfiltration, encryption or the exact origin of each file.

  **Unknown:** The number of affected individuals, the exact presence of personal or financial data in the scanned documents and images, source systems, acquisition method, access date, exfiltration scope, operational impact, victim confirmation and any full disclosure remain unknown. The analysis is limited to readable structures and file metadata; formula cells were not recalculated and no raw sensitive content is reproduced.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-07T02:25:08
listing_last_observed_at: 2026-08-07T02:25:08
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-04
-->

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
- **Sector:** Youth Development / Employment Services
- **Historical support domain:** `mpowa.mobi` (cited staging instance: `staging.mpowa.mobi`)
- **AFRINTEL status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4

- **Description:**

  mPowa is a South African youth-development and employment-services platform developed by mLab South Africa, a not-for-profit organisation. It is part of the SA Youth Network. The South African Presidency states that it was developed by mLab in partnership with the Department of Science and Innovation and launched as part of the Presidential Youth Employment Intervention. It is therefore a youth-employment service linked to a public initiative, rather than a government administration.

- **Public verification:**

  The Google Play listing attributes the app to mLab South Africa and uses `app@mpowa.mobi` as its support address, establishing a historical link between the domain and the service. During verification on 14 September 2026, the `mpowa.mobi` root displayed Korean-language casino content unrelated to mPowa. That current content is not attributed to the historical programme, and the domain’s current operator remains unknown.

  Sources: [South African Presidency](https://www.thepresidency.gov.za/virtual-address-president-cyril-ramaphosa-occasion-youth-day-16-june-2021) · [mLab South Africa](https://mlab.co.za/what-we-do/tech-solutions/) · [mPowa Google Play listing](https://play.google.com/store/apps/details?hl=en&id=com.mlab.mpowa)

- **Analysis:**

  The reviewed source is a post published on 7 August 2026 by the actor exfilar (VIP-tier forum account), titled "mpowa.mobi - 2,585 Youth CVs Exposed via 0day Firebase Scanner". The underlying Firebase Realtime Database export referenced in the post was also obtained independently. The actor states the platform's staging Firebase RTDB (staging.mpowa.mobi) was left publicly readable with no authentication, token or referer check, and that a proprietary scanning tool identified it.

  Examination of the exported database confirms the figures stated in the post: 2,585 complete CV/resume records, 26,675 service-delivery geolocation points, 11 service-provider directory records, 19 platform user accounts, and 3 API access-key entries. Each CV record includes a personal-information block (full name, phone, email, date of birth, gender, nationality, marital status, disability status, driver's license code, highest qualification), together with qualification, work-experience, language, skills and personal-reference sections; the reference entries additionally expose the name, employer, position and phone number of third parties named as referees. The 19 user records include full name, date of birth and geolocation coordinates for platform staff. The dataset also contains 3 live-looking API access keys with descriptive labels.

  The combination of disability status, date of birth and full identity data for named minors and young jobseekers constitutes special category personal information under South Africa's POPIA framework, and the exposure of a youth-employment platform linked to a public initiative, including active API keys, creates a material risk of credential misuse against related infrastructure, in addition to identity fraud, targeted phishing and physical-safety risks for the affected youth and third-party references. The staging hostname suggests a corresponding production environment may exist and could carry similar or worse exposure. The exact match between the record counts published by the actor and those independently observed in the reviewed export supports a very high confidence assessment. No candidate name, contact detail, date of birth, disability declaration, reference information, staff record or API key from the reviewed material is reproduced.

  The full post identifies mpowa.mobi as item "11/25" of an ongoing campaign, describing a proprietary tool ("CredHarvest V6") used to mass-scan and harvest exposed Firebase Realtime Database instances, and states that hundreds of similar databases have already been acquired through the same method. The actor advertises both the sale of this scanning tool and separate paid intrusion/access services on the same forum. This indicates mpowa.mobi is one victim within a broader, systematic campaign targeting misconfigured Firebase deployments, and that comparable exposures likely affect other African organizations using the same backend, independent of any targeting specific to mpowa.mobi.

### 08 August 2026
#### 🇳🇬 Nigeria - Daily Trust

- **Incident date:** Not specified
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
- **Public sources:** [Daily Trust overview](https://dailytrust.com/about-us)

- **Description:**

  Daily Trust is a Nigerian news brand published by Media Trust Limited. The group is active in publishing, printing and media services and operates a broader media portfolio that includes Daily Trust titles, Trust TV and Trust Radio, with operations including Abuja.

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

### 14 August 2026

#### 🇲🇦 Morocco - AVANTA Maroc

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 14 August 2026 at 05:55:47 (timezone not shown)
- **Actor / Group:** thegentlemen
- **Sector:** Human resources services
- **Website:** [avanta.ma](https://www.avanta.ma/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Public sources:** [AVANTA Maroc institutional profile](https://www.linkedin.com/company/avanta-maroc-sa)

- **Description:**

  AVANTA Maroc is a Moroccan human-resources services company headquartered in Casablanca. Its institutional profile states that it has operated since 1991 and provides recruitment, temporary staffing, outsourcing, contract management and HR-development services through a network covering several major Moroccan economic centres.

- **Analysis:**

  **Observed:** The supplied source record associates thegentlemen with "Avanta Maroc Ex Adecco", cites avanta.ma and locates the target in Morocco. It is timestamped 14 August 2026 at 05:55:47, with no timezone shown. The current public brand is AVANTA Maroc. The source provides no sample, volume, data category or technical evidence of compromise.

  **Assumption:** The matching name, domain and country make the target identification plausible. HR activities potentially involve candidate, employee or customer data, but no exposure of such information is established.

  **Unknown:** Initial access, affected systems, encryption, exfiltration, operational impact, victim confirmation and publication status remain unknown.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-14T05:55:47
listing_last_observed_at: 2026-08-14T05:55:47
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-14T05:55:47
-->

### 16 August 2026
#### 🇿🇦 South Africa - The Courier Guy

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 16 August 2026, 15:19:49 (timezone not shown)
- **AFRINTEL detection date:** 19 August 2026
- **Actor / Group:** medusalocker
- **Sector:** Courier / Logistics
- **Website:** [thecourierguy.co.za](https://thecourierguy.co.za)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Public sources:** [The Courier Guy overview](https://mail.thecourierguy.co.za/about-us/) | [Official website](https://thecourierguy.co.za/)

- **Description:**

  The Courier Guy is a South African courier and parcel-delivery company serving consumers and businesses through depots, kiosks, lockers and a nationwide driver network. Its public profile states that it has operated for about 25 years and handled more than 21 million deliveries in 2024.

- **Analysis:**

  **Observed:** The local dossier contains 10 artefacts: six CSV files and four XLSX workbooks. The six CSV files were analysed in full read-only mode: 1,269 data rows, four metadata rows per file and 36 columns. Fields include recipient name, recipient bank account, account type, branch code, amount, references and email, fax and SMS notification channels. The set contains 255 distinct recipient names and 236 distinct accounts; no exact duplicate row was observed within the files. The four XLSX workbooks each contain 20 sheets of rental-payment schedules. A total of 3,409 formula cells were detected and none was executed. External-link components are present in three of the four workbooks; no link was followed. Filenames cover July and August 2025 and January, February and April 2026 batches; a sheet named 1 August 2011 also indicates a historical or reused element. SHA-256 hashes for all 10 artefacts were calculated locally and retained outside the repository.

  **Assumption:** The consistent file structure, repeated rental schedules and presence of payment and contact data make association of the corpus with The Courier Guy's operational environment plausible. The sample is sufficiently structured to increase confidence in its authenticity and attribution. It could facilitate payment fraud, recipient or supplier impersonation, targeted phishing and account attacks, but it does not confirm the access vector, exfiltration or medusalocker's actions.

  **Unknown:** The exact number of affected individuals and organisations, the current validity of accounts and contact details, source systems, acquisition method, access date, exfiltration scope, operational impact, victim confirmation and full publication remain unknown. Historical or inherited sheets may no longer reflect the current state. The analysis did not recalculate formulas, follow external links or reproduce raw financial or personal data.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-16T15:19:49
listing_last_observed_at: 2026-08-19T05:35:53+01:00
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-04
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

- **Incident date:** 26 June 2026, date alleged by the actor
- **Initial publication date:** 18 August 2026
- **Source detection date:** 18 August 2026 at 10:27:05 (timezone not shown)
- **AFRINTEL detection date:** 18 August 2026
- **Actor / Group:** incransom
- **Sector:** Financial services / Fund administration
- **Website:** [spearfin.net](https://spearfin.net)
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Public sources:** [SpearFin official website](https://spearfin.net/) | [Fund administration services](https://spearfin.net/fund-administration/)

- **Description:**

  SpearFin Ltd is a Mauritius-based financial-services and management company regulated by the Financial Services Commission of Mauritius. It provides fund-administration, corporate, compliance and investor-support services. Its public information states that it administers more than USD 10 billion in assets.

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

### 19 August 2026

#### 🇿🇦 South Africa - Babcock Africa

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 19 August 2026 at 08:10:32 (timezone not shown)
- **Actor / Group:** thegentlemen
- **Sector:** Engineering / Industrial services / Defence support
- **Website:** [babcock.co.za](https://www.babcock.co.za/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 4
- **Public sources:** [Babcock Africa overview](https://www.babcock.co.za/about/) | [Engineering services](https://www.babcock.co.za/products-and-services/engineered-solutions/6/)

- **Description:**

  Babcock Africa is a division of Babcock International providing critical engineering and industrial-asset services across Africa. Its activities include transport solutions, power-generation support, industrial engineering, equipment for mining and construction, and specialist capabilities in marine and defence-related engineering.

- **Analysis:**

  **Observed:** The supplied source record associates thegentlemen with Babcock, cites babcock.co.za and locates the target in South Africa. It is timestamped 19 August 2026 at 08:10:32, with no timezone shown. The source sector, "defence industry", covers only part of Babcock Africa's public activities. No sample, volume, data category, deadline or technical element is provided.

  **Assumption:** The matching domain and business profile make the target identification plausible. A confirmed compromise could have significant consequences because of the organisation's engineering and critical-sector support services, but no impact is established by the supplied material.

  **Unknown:** Access and acquisition methods, affected environments, encryption, operational disruption, disclosure and any confirmation by Babcock remain unknown.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-19T08:10:32
listing_last_observed_at: 2026-08-19T08:10:32
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-19T08:10:32
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

#### 🇨🇲 Cameroon - CCA Bank
* **Incident date:** Not specified
* **Initial publication date:** 20 August 2026
* **Source detection date:** 20 August 2026 at 13:54:00 (timezone not shown)
* **AFRINTEL detection date:** 20 August 2026
* **Actor / Group:** Everest
* **Sector:** Banking / Financial services
* **Website:** [cca-bank.com](https://www.cca-bank.com/)
* **AFRINTEL status:** Claim - Unverified
* **Incident type:** Ransomware
* **Confidence level:** Medium
* **Impact level:** Level 4
* **Public sources:** [CCA Bank overview](https://www.cca-bank.com/fr) | [Official website](https://www.cca-bank.com/)
* **Description:**
  CCA Bank, or Crédit Communautaire d'Afrique-Bank, is a Cameroonian banking institution headquartered in Douala-Bonanjo. Its public website presents banking and financial services for individuals and businesses, including account, payment and financing solutions.
* **Analysis:**
  **Observed:** On 20 August 2026, AFRINTEL observed an Everest publication targeting `cca-bank.com`. At the time of observation, the victim entry still displayed an active countdown before the announced release of the data, indicating that the extortion phase remained ongoing.

  The available technical inventory identifies **11,837 files totaling 18.92 GB**, together with **17 nested RAR archives totaling 120.31 MB** whose internal files were not included in the file count. The total known volume therefore reaches approximately **19.04 GB**.

  The inventoried material spans several sensitive banking functions, including credit applications and lending analysis, customer portfolios and exposures, financial and treasury information, prudential reporting, regulatory material including COBAC-related documents, AML/KYC and AML/CFT records, identity documentation, legal and recovery material, HR information, internal procedures, IT documentation, access and authorization management, and banking-system migration and reconciliation files.

  Several files described in the inventory correspond to large structured exports. One regulatory workbook contains a **591,799-row customer-base table**, a **489,155-row individual-deposit table**, and a **350,011-row customer-exposure table**. Another credit export contains **250,688 credit rows** involving **67,973 unique client identifiers**. V10/V11 migration and reconciliation datasets also contain hundreds of thousands to several million lines.

  **Assumption:** The functional depth and consistency of the categories described in the inventory are compatible with material originating from the business and technical environments of a banking institution. If authentic, the potential exposure would extend well beyond a conventional document leak and could involve customer, financial, regulatory, KYC, operational and technical information.

  The combination of identity information, credit records, financial data and internal documentation could facilitate **spear-phishing, financial fraud, identity theft, document fraud, account compromise and secondary targeting of customers, employees, suppliers or business partners**.

  IT documentation concerning access management, VPN procedures, account administration and system migrations could also provide other malicious actors with information useful for understanding internal processes and preparing follow-on attacks.

  **Unknown:** AFRINTEL has not directly examined the complete set of **11,837 raw files** claimed by Everest. This assessment is based on the observed Everest publication and the available technical inventory. The initial-access vector, actual compromise date, exact affected systems, exfiltration method, possible encryption activity, precise scope of Everest's access and any official confirmation from CCA Bank remain unknown.

  The observed countdown indicates an announced disclosure but does not establish whether the data will actually be released, whether negotiations are ongoing or whether any agreement has been reached between the victim and the attackers.

  AFRINTEL does not reproduce any personal information, banking data, identity document, credential, access information or other sensitive material described in the dataset.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-20T13:54:00
listing_last_observed_at: 2026-08-20T13:54:00
sample_status: none-observed
deadline_at:
deadline_status: active
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-20T13:54:00
-->

---
### August 22, 2026
#### 🇲🇦 Morocco - RAMED (Régime d’Assistance Médicale)

- **Incident date:** Not specified
- **Initial publication date:** August 22, 2026

- **Actor / Group:** JBT2026
- **Sector:** Government / Administration
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Website:** [sante.gov.ma](https://www.sante.gov.ma)
- **Historical RAMED domain:** `ramed.ma` *(inactive)*

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

#### 🇿🇦 South Africa - Furniture Bargaining Council

- **Incident date:** August 2026, exact date not publicly stated
- **Initial publication date:** Not specified
- **Source detection date:** 24 August 2026 at 21:21:08 (timezone not shown)
- **Actor / Group:** Deadlock, claimant, with no attribution by the victim
- **Sector:** Labour relations / Furniture-sector governance
- **Website:** [fbcweb.furnbed.co.za](https://fbcweb.furnbed.co.za/)
- **AFRINTEL status:** Victim Confirmed
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Public sources:** [Official notification and Council website](https://fbcweb.furnbed.co.za/) | [Council overview](https://fbcweb.furnbed.co.za/what.php)

- **Description:**

  The Furniture Bargaining Council is a South African bargaining council for the furniture manufacturing industry. Its mission includes promoting orderly collective bargaining, labour peace, dispute resolution and sector governance.

- **Analysis:**

  **Observed:** The local corpus associated with the disclosure contains 69 artefacts totalling approximately 94.6 MB: 22 PDFs, 13 XLSX, 31 DOCX, 2 DOCM and 1 DOC. Twelve readable XLSX workbooks contain 134 sheets and 78,605 detected formula cells; no formula was executed. External-link components are present in four workbooks; no link was followed. One additional XLSX workbook is CDFV2-encrypted and could not be opened. The observed documents cover financial packs, cash trackers, e-wallet accounts, bank forms, SARS tax reconciliations, loans, disciplinary warnings, IT audits, security reports, identity documents and personal or administrative material. Separately, the Council's official notification confirms an incident in which certain servers were encrypted.

  Structural and textual examination of the readable documents confirms financial, tax, banking, HR, identity and operational data categories. It establishes that a data corpus was disclosed or made accessible, but cannot determine whether every file came directly from the Council's systems or whether the entire corpus was acquired during the same event. PDFs and documents potentially containing personal information were not reproduced.

  **Assumption:** The official confirmation of server encryption establishes the incident and supports the Victim Confirmed status. The consistency of the documentary corpus with the FBC's administrative and financial activities strongly reinforces attribution to the victim's environment. The presence of financial, tax, banking, identity and personnel data supports a Level 4 impact assessment. It does not confirm the access vector, exfiltration of every file or Deadlock's technical responsibility.

  **Unknown:** The exact number of affected individuals, source systems, acquisition method and date, full disclosure scope, data currency, technical attribution to Deadlock, operational consequences and notifications to affected persons remain unknown. The encrypted workbook, external links and visual or scanned contents were not opened or followed.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-24T21:21:08
listing_last_observed_at: 2026-08-24T21:21:08
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: partial
victim_confirmation: confirmed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-04
-->

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

---
### 26 August 2026

#### 🇪🇬 Egypt - Mima Foods

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 26 August 2026 at 15:29:13 (timezone not shown)
- **Actor / Group:** krybit
- **Sector:** Food manufacturing / Frozen food export
- **Website:** [mimafoods.net](https://mimafoods.net/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Public sources:** [Official website](https://mimafoods.net/) | [Company profile](https://mimafoods.net/company-profile/)

- **Description:**

  Mima Foods is an Egyptian producer and exporter of IQF fruit and vegetables, with a factory in Sadat City and headquarters in Cairo. Its website states that it supplies distributors, food manufacturers and private-label brands in more than 45 countries.

- **Analysis:**

  **Observed:** The supplied source record associates krybit with mimafoods.net and locates the target in Egypt. It is timestamped 26 August 2026 at 15:29:13, with no timezone shown. According to monitoring information reported on 12 September 2026, the displayed deadline had passed and no Mima Foods data or sample was publicly accessible at the latest reported check. The check time and exact deadline are not specified. No technical evidence confirms access, exfiltration or encryption.

  **Assumption:** The domain exactly matches the official website, making the target identification plausible. This does not confirm access, exfiltration or encryption. The lack of accessible data after the deadline could be consistent with an agreement or negotiations, with or without payment; transfer, sharing or resale of data; a delay; listing or link unavailability; or an inaccurate or exaggerated claim. These remain hypotheses. Disclosures attributed to other Krybit victims do not prove Mima Foods' data were transferred.

  **Unknown:** Any affected systems, the access vector, operational scope, nature of any data, victim confirmation, access and exfiltration are not established. The exact deadline, reason for the lack of public disclosure, any private sharing, negotiations, payment or resale remain unknown.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-26T15:29:13
listing_last_observed_at: 2026-08-26T15:29:13
sample_status: none-observed
deadline_at:
deadline_status: expired
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-09-12
-->

#### 🇬🇦 Gabon - Conseil Gabonais des Chargeurs (CGC) [Ransomware]

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 26 August 2026 at 15:56:16 (timezone not specified)
- **Actor / Group:** KRYBIT
- **Sector:** Public administration / Transport and logistics
- **Website:** [cgcgabon.ga](https://cgcgabon.ga/)
- **Domain cited by the source dataset:** cgcgabon.com
- **AFRINTEL status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Associated effect:** Data exposure and disclosure
- **Confidence level:** High
- **Impact level:** Level 4
- **Public sources:** [Conseil Gabonais des Chargeurs official website](https://cgcgabon.ga/)

- **Description:**

  The Conseil Gabonais des Chargeurs (CGC) is a Gabonese public organization involved in supporting, assisting and regulating activities related to shippers, transportation and cargo flows.

- **Data exposed in the analyzed batches:**

  - personally identifiable HR data, including names, employee IDs, CNSS numbers, phone numbers, dates of birth, job titles and professional information;
  - individual performance evaluations and career-management documents;
  - organizational charts, position maps and job descriptions showing internal reporting relationships;
  - information about the IT Operations Directorate, system administrators, databases, IT support and cybersecurity functions;
  - material relating to the internal Active Directory environment, including the `cgc.local` domain, several domain controllers, replication topology, Active Directory roles and administrative data, exposed in part by a PowerShell artifact;
  - business processes related to BIETC/GECOP, importers, exporters, shippers, air-freight operations and infringement databases;
  - documents concerning finance and accounting, communications, public relations, legal affairs and regional offices;
  - internal organizational projects and draft structures.

- **Analysis:**

  Analysis of multiple file batches attributed to the disclosure claimed by KRYBIT indicates a large-scale, cross-department leak of internal documents. The corpus covers Human Resources, information systems, cybersecurity, databases, strategy, air-freight operations, BIETC/GECOP processes, Legal Affairs, Finance, institutional communications and some regional offices. The documents show strong consistency in format, terminology, hierarchy and internal processes, supporting very high confidence that they originated from the CGC.

  **Observed:** Cross-analysis of multiple batches attributed to the disclosure claimed by KRYBIT identifies an internal document corpus spanning Human Resources, the IT Operations Directorate, Strategy and Multimodal Observatory, the Airport Office, Legal Affairs, Communications, Finance/Accounting and a regional office in Port-Gentil. Consistency across templates, job titles, hierarchies, internal references and processes strongly supports association of the documents with the CGC.

  A PowerShell artifact containing `repadmin` and `dcdiag` output, dated 22 February 2026, exposes the `cgc.local` Active Directory domain, three domain controllers, replication topology and AD roles, concentrated on one controller. The replication summary in that snapshot reports zero failures; it describes only the state observed at that time. DOSI job descriptions detail database and system administration, information security, network and support responsibilities. The corpus also describes BIETC/GECOP processes, importers/exporters, manifests, cargo movements and infringements, as well as shipper assistance, air-freight regulation, finance, communications and regional functions.

  The available material strongly corroborates disclosure of internal CGC documents and provides a detailed view of its organization, responsibilities and some technical and business processes. No clear-text credentials were observed in the examined material. The documents describe the functional model of the BIETC/GECOP and infringement databases, but no complete dump of these databases was observed.

  System events containing repeated DCOM authentication-level errors also appear in the artifact. They may result from legitimate administration, maintenance or configuration incompatibility and are not, by themselves, evidence of malicious activity or a link to the ransomware.

  **Assumption:** The breadth and diversity of the corpus are consistent with collection from a shared document repository, network share, document-management system or backup accessible across several departments. This remains a hypothesis: the artifacts do not identify the initial collection point. If exploited after initial access, the organizational and technical information could reduce reconnaissance effort and facilitate targeting of IT, HR, security and finance functions, partners and regional offices.

  **Unknown:** The initial access vector, source system, full extent of exfiltration, existence of a complete BIETC/GECOP dump, ransomware execution, encryption mechanism, operational impact and any official victim confirmation remain unknown. Attribution to KRYBIT is based on the group's claim. The analyzed documents corroborate exfiltration but do not establish the vector, execution or encryption of the ransomware.

  The consistency and diversity of the documents support **very high** confidence in the likely authenticity of the corpus and its association with the CGC. This assessment is not official confirmation of the incident or attribution to KRYBIT.
- **Risks:**
  - targeted spear-phishing against employees and executives;
  - identity theft and social-benefit fraud;
  - targeting or compromise of privileged accounts;
  - social engineering against IT, HR, finance and management personnel;
  - Business Email Compromise and executive impersonation;
  - impersonation of official communications;
  - targeting of importers, exporters, shippers and business partners;
  - secondary exploitation of Active Directory information;
  - economic intelligence based on legal, organizational and strategic documents;
  - follow-on attacks against CGC regional offices and partners.

- **AFRINTEL Assessment:**
  - **Corpus internal consistency:** Very High
  - **Likely authenticity of CGC documents:** Very High
  - **Leak scope:** Multi-department
  - **Organizational exposure:** Critical
  - **Active Directory / infrastructure exposure:** Critical
  - **Business-process exposure:** High to Critical
  - **HR exposure:** High
  - **Economic intelligence value:** High
  - **Clear-text credentials:** Not observed in the material examined
  - **Complete BIETC/GECOP dump:** Not observed at this time
  - **Initial access vector:** Not established
  - **Ransomware encryption:** Not demonstrated by the documents themselves
  - **Official victim confirmation:** Not observed

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-26T15:56:16
listing_last_observed_at: 2026-08-26T15:56:16
sample_status: sample-reviewed
deadline_at:
deadline_status: not-stated
disclosure_status: release-reviewed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-26T15:56:16
-->

### 27 August 2026

#### 🇿🇦 South Africa - Hungry Lion

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 27 August 2026 at 06:27:50 (timezone not shown)
- **Actor / Group:** medusalocker
- **Sector:** Restaurants / Quick-service restaurants
- **Website:** [hungrylion.co.za](https://www.hungrylion.co.za/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Public sources:** [Hungry Lion overview](https://www.hungrylion.co.za/about/) | [Legal information](https://www.hungrylion.co.za/legal/)

- **Description:**

  Hungry Lion is a South African quick-service restaurant chain focused on fried chicken, burgers and related products. The company states that it opened its first restaurant in Stellenbosch in 1997 and later expanded into several African markets. It announced the opening of its 500th restaurant in 2025.

- **Analysis:**

  **Observed:** The supplied source record associates medusalocker with Hungry Lion and locates the target in South Africa. It is timestamped 27 August 2026 at 06:27:50, with no timezone shown. The source description claims 111 locations across seven countries and names three point-of-sale environments, Unity POS, GAAP POS and CoSoft POS, with some operational volumes or frequencies. It ends with the label "Botswana", leaving the exact geographic scope of the publication unclear. No sample or technical evidence is provided.

  **Assumption:** Public information confirms that Hungry Lion is a regional chain headquartered in South Africa, but does not validate the figures or systems described in the claim. If a point-of-sale environment were compromised, operational and fraud risks could result.

  **Unknown:** The exact targeted legal entity or country, initial access, affected terminals or servers, exfiltration, encryption, operational impact, victim confirmation and any disclosure remain unknown.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-27T06:27:50
listing_last_observed_at: 2026-08-27T06:27:50
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-27T06:27:50
-->

#### 🇿🇦 South Africa - Rohloff Group

- **Incident date:** Not specified
- **Initial publication date:** Not specified
- **Source detection date:** 27 August 2026 at 14:31:07 (timezone not shown)
- **Actor / Group:** incransom
- **Sector:** Restaurants / Quick-service restaurants
- **Website:** [Rohloff Group careers site](https://rohloff-group.breezy.hr/)
- **AFRINTEL status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Public sources:** [Institutional profile](https://www.linkedin.com/company/rohloff-group/?originalSubdomain=za) | [Company-managed careers site](https://rohloff-group.breezy.hr/)

- **Description:**

  Rohloff Group is a South African restaurant operator and one of the largest KFC franchise groups in Africa. Founded in 1981 and headquartered in Somerset West, Western Cape, it operates a network of KFC restaurants supported by a restaurant support centre.

- **Analysis:**

  **Observed:** The supplied source record associates incransom with Rohloff Group and locates the target in South Africa. It is timestamped 27 August 2026 at 14:31:07, with no timezone shown. The actor claims 536 GB, 103,196 files and 30,805 folders. It states that the material includes employee personal and banking information, loan applications, identity documents, bank statements, acknowledgements of debt, disciplinary-hearing results, and financial records relating to royalties and food costs. The publication announces a later full disclosure.

  No sample or source file accompanies the supplied material. The volumes and categories therefore remain actor claims.

  **Assumption:** The precise victim name and profile make the publication target-specific, but do not confirm a compromise. If the claimed categories are authentic, the combination of identity, banking, HR and disciplinary information would create a high risk of identity misuse, financial fraud, targeted phishing and employee privacy harm.

  **Unknown:** Initial access, affected systems, exfiltration, encryption, validity of the claimed volumes, availability of any disclosure, victim confirmation, negotiations, ransom payment and resale remain unknown.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at: 2026-08-27T14:31:07
listing_last_observed_at: 2026-08-27T14:31:07
sample_status: none-observed
deadline_at:
deadline_status: not-stated
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-08-27T14:31:07
-->

### August 29, 2026
#### 🇱🇾 Libya - Albarq Media Service / شركة البرق للاتصالات والتقنية

* **Incident period:** June 2026, exact date not established
* **Initial publication date:** June 09, 2026
* **AFRINTEL discovery date:** August 29, 2026
* **Actor / Group:** Richard2002
* **Sector:** Telecommunications / Media Services
* **Website:** [albarq.ly](https://albarq.ly/)
* **Status:** Claim - Data Sample Published
* **Incident type:** Data Leak
* **Confidence level:** Medium
* **Impact level:** Level 3

* **Description:**
  Albarq Media Service is presented as a service associated with شركة البرق للاتصالات والتقنية (Albarq Telecommunications and Technology), a Libyan telecommunications and related-services operator.

* **Analysis:**
  A post attributed to Richard2002 and dated June 09, 2026 presents a sample allegedly originating from the Albarq Media service and claims approximately **330,000 accounts**. The visible sample contains **18 rows** and **24 semicolon-separated fields**. It includes account identifiers, subscription information, dates, general locations and telephone numbers; AFRINTEL does not reproduce raw personal data.

  The visible records contain dates ranging from August 2019 to April 2025, with inconsistent or missing usage values in several rows. The observed material is only a visible extract and cannot validate the claimed **330,000 accounts**, the completeness of the leak, the source system, the access vector or the extraction method. The original source file was not available; the analysis is therefore limited to the data visible in the provided sample.

  **Unknown:** No independent public confirmation of the incident by Albarq or a Libyan authority is established in the examined material. The exact access or exfiltration period remains unknown; June 2026 refers to the date of the observed publication.

* **Recommendations:**
  * Review subscription-platform access logs and data exports around June 09, 2026.
  * Reset sessions and strengthen monitoring of administrative accounts if exposure is confirmed.
