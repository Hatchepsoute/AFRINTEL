# List of African cyberattack victims in July 2026 (34 records)
👉🏾 [French version](./victims_FR.md)

## July 2026

### July 01, 2026

#### 🇨🇮 Ivory Coast - Hôpital Catholique Saint Joseph Moscati
- **Initial publication date:** July 01, 2026



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

#### 🇨🇮 Côte d'Ivoire - Virtual University of Côte d'Ivoire (UVCI)
- **Initial publication date:** July 01, 2026


- **Author / Publication account:** Sensitive2025
- **Sector:** Higher education / University administration
- **Associated website:** [uvci.edu.ci](https://www.uvci.edu.ci/); displayed service subdomain: `licences3.uvci.online`
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** High for attribution of the supplied corpus to the UVCI ecosystem; Medium for compromise of the production system
- **Impact level:** Level 4
- **Victim description:** The Virtual University of Côte d'Ivoire (UVCI) is an Ivorian digital higher-education institution. The publication associates the organisation and a service subdomain with a university-account database.
- **Analysis:** The observed publication presents a “Fresh Database” attributed to UVCI, associates the `licences3.uvci.online` subdomain with a university service and claims an approximately 8 GB SQL database. AFRINTEL analysed the entire locally supplied SQL dump read-only, not a sample: **8,721,338,295 bytes**, SHA-256 `17e60b953b9196ea6fee65344da4e17b38839c092e4239e49e8662b558736501`. All 10 associated CSV files were also analysed in full; the 11 files total approximately **8.76 GB**. Download links, personal values and secrets are not reproduced.

  **Observed - structure and coverage:** The dump is a MySQL 8.0.42 export of the `licences3` database with **490 tables**, **226 populated tables**, approximately **56,714,959 records** recomputed from SQL tuples and **8,749 INSERT statements**. It includes `mdl_user`, `mdl_user_enrolments`, `mdl_logstore_standard_log`, `mdl_session`, `mdl_files`, `mdl_messages`, `mdl_grade_grades`, `mdl_inscription_pedagogique_uvci`, `mdl_inscription_semestrielle`, `mdl_passerelle_uvci`, cohort, group and role tables.

  Major observed volumes include **16,410,270 Moodle logs**, **17,972,218 question-attempt step-data rows**, **9,481,515 attempt steps**, **3,221,383 question attempts**, **561,444 grade rows**, **605,111 files**, **554,701 Moodle sessions**, **193,269 additional application sessions**, **30,275 messages**, **91,042 user-enrolment associations**, **88,789 role assignments**, **58,299 cohort memberships**, **43,812 pedagogical registrations**, **6,993 users**, **154 external tokens** and **4,635 user private keys**. Session and log schemas contain IP addresses, timestamps, actions, users, courses and session data; no raw value is published.

  **Observed - accounts and academic data:** `mdl_user.csv` contains **6,993 accounts**, all using manual authentication and marked confirmed; **6,891** are not suspended, **102** are suspended and **21** are marked deleted. The 6,993 user IDs, usernames and email addresses are distinct. Each account has a 60-character bcrypt-like password hash. Profile data includes identity, contact, institution, training, location, login dates, last IP, account status and semester fields.

  `mdl_passerelle_uvci.csv` contains **4,398 accounts**, all in Licence 2 / S3, with **3,047** `reinscription=1` values and **1,351** set to `0`. `mdl_inscription_semestrielle.csv` contains **8,559 registrations**, including **8,557** in Licence 2 / S3. The `moyenne_uvci` exports contain **47,553 result rows**, with course, level, speciality, semester, grade, examination-session and academic-status fields. Historical exports contain **21,029** rows for May 2024 and **17,034** for August 2023. `moyenne_uvci(1).csv` is a separate list of **3,802 email addresses**, matching accounts present in the current user and result exports.

  Comparison of `moyenne_uvci.csv` and `moyenne_uvci_25_06_2025_21h-16.csv` shows the same set of **47,553 keys**: **44,683 rows are identical** and **2,870 rows changed**, mainly in examination session 2, status and final-average fields. This is compatible with distinct application states or extracts; it does not date the actor’s access.

  **Observed - secrets and authentication:** `mdl_user.csv` and `mdl_passerelle_uvci.csv` contain **6,993** and **4,398** bcrypt-like password hashes respectively. `mdl_enrol(1).csv` contains **3,824 enrolment configurations**, including **2,972 non-empty four-character password values** and **852 empty fields**; these values do not match a hash format and must be treated as potentially exposed secrets, without reproduction or testing. The presence of **154 external tokens**, **4,635 user private keys**, sessions and session data increases the risk of secondary compromise; their current validity is not described in the available material.

  **Integrity and consistency checks:** All 10 CSV files are readable as UTF-8 or ASCII, with **0 malformed rows** and **0 complete duplicate rows** detected. CSV row counts match the SQL tables where applicable: 6,993 users, 8,559 semester registrations, 4,398 gateway records and 47,553 current results. Hashed email cross-checks between users, registrations, gateway records and grade exports are strong; the `uvci.edu.ci` and `licences3.uvci.online` domains, Moodle/UVCI tables, language settings and course structures form a coherent UVCI environment. Partial repetitions in historical and registration exports are consistent with users appearing across cohorts, semesters or repeated extracts and must not be summed as unique persons.

  **Analytical assessment:** The supplied corpus is highly consistent with a complete application-environment export from `licences3`, used by the UVCI ecosystem. The publication, coherent schemas, domains, accounts, courses, logs and academic data make attribution of the corpus to UVCI highly plausible. The sources consulted do not specify the access vector, acquisition date, initial exfiltration, production-system compromise or completeness of the original database beyond the supplied files.

  **Unknown:** The actor’s access date and method, exact production-system scope, existence of a separate exfiltration, current validity of hashes, tokens, keys and enrolment passwords, globally deduplicated number of unique persons, notifications by UVCI and any official confirmation remain unknown. File dates in June 2026, displayed publication dates and application timestamps must not be merged into a single intrusion date.

  **Attribution and impact conclusion:** The complete analysis of the supplied SQL dump and 10 CSV files confirms a corpus rich in identity, contact, training, registration, academic-result, account, file, message, log, IP-address, session and authentication artefacts, strongly consistent with the UVCI environment. Risks include credential reuse, targeted phishing, student and staff impersonation, academic fraud, privacy harm, exploitation of still-active sessions or tokens and secondary compromise of connected services. No name, email address, telephone number, identifier, IP address, hash, token, key or other raw personal data is reproduced in the repository.
- **Evidence limitations:** The completeness of the supplied SQL file and 10 CSV files was analysed; completeness of the original UVCI system database, access date, intrusion vector, initial exfiltration, current secret validity and production-system compromise are not documented in the public sources. `Data Fully Published` describes the observed publication and supplied corpus; it is not an official incident confirmation or proof that the entire source database was extracted.
- **Classification decision:** Incident assigned to July 2026 according to the initial 1 July 2026 publication.

### July 04, 2026

#### 🇨🇮 Côte d'Ivoire - Université Jean Lorougnon Guédé (UJLoG)
- **Initial publication date:** July 04, 2026


- **Actor / Group:** Sensitive2025 (account displayed in the publication; identity and affiliation not independently verified)
- **Sector:** Higher education / University administration
- **Associated website:** [ujlog.uvci.edu.ci](https://ujlog.uvci.edu.ci/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High for sample attribution to the UJLoG environment; Medium for incident scope
- **Impact level:** Level 3
- **Victim description:** Université Jean Lorougnon Guédé (UJLoG) is an Ivorian university. The publication associates its subdomain with an account database from a university platform.
- **Analysis:** The supplied sample presents a Moodle-type user schema containing account identifiers, usernames, identity fields, email addresses, institution, department, location, language, access timestamps, IP addresses and bcrypt password hashes. Twelve individual records are visible in the supplied extract; the observed accounts and addresses primarily use the `ujlog.uvci.edu.ci` ecosystem, with UJLoG/UVCI institutional references. The `username`, `email`, `institution`, `department`, `city`, `country`, `lastlogin`, `currentlogin` and `lastip` fields indicate an operational account-management database rather than a simple name list.

  Consistency between the `ujlog.uvci.edu.ci` domain, UJLoG institutional labels, the Moodle structure, French-language settings, `CI` country values, profile information and bcrypt hashes strongly supports attribution of the sample to UJLoG's digital environment. The sample can therefore be assessed as highly consistent with that environment. As the remainder of the dump is no longer available, the analysis is strictly limited to the data visible in the supplied sample and cannot verify total volume, duplicates or dataset completeness.

  The exposed data could facilitate targeted phishing, student or administrative account impersonation, credential reuse and analysis of login patterns. No name, email address, telephone number, IP address, hash or other individual data is reproduced in the repository.
- **Evidence limitations:** The sample is strongly consistent with UJLoG, but it does not confirm the access date, intrusion vector, initial exfiltration, production-system compromise or total number of affected individuals. The remainder of the dump is unavailable for analysis; the findings must not be extrapolated to the full claimed dataset.
- **Classification decision:** Counted as a canonical October incident because AFRINTEL first documented it on 25 October 2026 and the July report had already been made public. The 4 July 2026 publication is retained as historical context; it does not create a duplicate in the October tracking set.

### July 06, 2026

#### 🇪🇬 Egypt - EBNY Development
- **Initial publication date:** July 06, 2026



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

#### 🇰🇪 Kenya - East African Gasoil Limited (EAGOL)
- **Initial publication date:** July 06, 2026



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

### July 08, 2026

#### 🇩🇿 Algeria - Directorate-General for Scientific Research and Technological Development (DGRSDT)
- **Initial publication date:** July 08, 2026



- **Incident date:** 8 July 2026 (date supplied for the incident; initial access date not established)
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

### July 10, 2026

#### 🇲🇦 Morocco - Eurodefi
- **Initial publication date:** July 10, 2026



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

### July 11, 2026

#### 🇹🇳 Tunisia - TOPNET
- **Initial publication date:** July 11, 2026



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

#### 🇹🇳 Tunisia - Orange Tunisia
- **Initial publication date:** July 11, 2026



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

#### 🇲🇦 Morocco - Planet Sport
- **Initial publication date:** July 11, 2026



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

#### 🇬🇭 Ghana - Golden Star Resources
- **Initial publication date:** July 11, 2026



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

### July 12, 2026

#### 🇨🇲 Cameroon - Ministry of Employment and Vocational Training (MINEFOP)
- **Initial publication date:** July 12, 2026



- **Incident date:** July 12, 2026
- **Public analysis:** July 27, 2026
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

### July 13, 2026

#### 🇨🇲 Cameroon - TurboSoft
- **Initial publication date:** July 13, 2026



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
- **Initial publication date:** July 14, 2026



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

#### 🇿🇦 South Africa - BE Travel
- **Initial publication date:** July 14, 2026



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
- **Initial publication date:** July 15, 2026



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

#### 🇿🇦 South Africa - Fidelity Services Group
- **Initial publication date:** July 15, 2026



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

#### 🇿🇦 South Africa - Rectron (Pty) Ltd
- **Initial publication date:** July 15, 2026



- **Detected incident date:** July 15, 2026
- **SENS notification:** July 22, 2026
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

### July 16, 2026

#### 🇧🇼 Botswana - North Atlantic Engineering Consultants
- **Initial publication date:** July 16, 2026



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

#### 🇪🇬 Egypt - Sinai Grand Casino
- **Initial publication date:** July 16, 2026



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
- **Initial publication date:** July 18, 2026



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

#### 🇰🇪 Kenya - Official website of the President of the Republic (`president.go.ke`)
- **Initial publication date:** July 18, 2026



- **Incident date:** July 18, 2026
- **Government confirmation:** July 18, 2026
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

### July 19, 2026

#### 🇿🇦 South Africa - CKR Consulting Engineers
- **Initial publication date:** July 19, 2026



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
- **Initial publication date:** July 21, 2026


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
- **Initial publication date:** July 23, 2026



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

#### 🇸🇸 South Sudan - Nile Petroleum Corporation (NILEPET)
- **Initial publication date:** July 23, 2026



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
- **Initial publication date:** July 24, 2026



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

#### 🇲🇦 Morocco - Moroccan Biometric Passport Portal
- **Initial publication date:** July 24, 2026



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

#### 🇳🇬 Nigeria - Unidentified federal university (system access)
- **Initial publication date:** July 24, 2026



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
- **Initial publication date:** July 25, 2026



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
- **Initial publication date:** July 26, 2026



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

#### 🇹🇳 Tunisia - École Nationale d'Administration (ENA) - concours.ena.tn
- **Initial publication date:** July 26, 2026



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

#### 🇳🇬 Nigeria - Zenith Bank Plc
- **Initial publication date:** July 26, 2026



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

#### 🇪🇬 Egypt - Egyptian Football Association (EFA)
- **Initial publication date:** July 26, 2026



* **Incident date:** Not established


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
