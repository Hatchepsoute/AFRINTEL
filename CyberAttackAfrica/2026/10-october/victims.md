![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in October 2026 (48 records)

👉🏾 [**French version available here**](./victims_FR.md)

## October 2026

**Monthly tracking status: Published / Publié**  -  corpus of 48 records published or first observed in October 2026. Monthly closure and statistics are published in the accompanying report.

### October 1, 2026

#### 🇨🇩 Democratic Republic of the Congo - ServerUnlockApp (`serverunlockapp.com`) [Data Leak]

- **Initial publication date:** 1 October 2026 at 13:32 (displayed timestamp; timezone not specified)
- **Actor / Group:** SensitiveDarkForum (displayed forum/account; identity and affiliation unverified)
- **Sector:** Digital services / Phone unlocking, activation and related services
- **Website:** [serverunlockapp.com](https://serverunlockapp.com/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Claimed effect:** Disclosure of website backup files and application data
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Underground forum post and local backup provided to AFRINTEL

- **Victim description:** ServerUnlockApp is an online service associated with the Democratic Republic of the Congo, offering phone-unlocking, IMEI-processing, tool-activation and related services. The public website associates the activity with Kinshasa and displays payment and contact methods intended for customers and resellers.

- **Analysis:**

  **Observed:** A SensitiveDarkForum post timestamped **1 October 2026 at 13:32** according to the displayed time presents “Website Backup Files” associated with `serverunlockapp.com` and the DRC. The local sample is an application-backup tree containing **7,329 files** with an aggregate file size of **158,750,705 bytes**. It includes **3,467 PHP files**, **708 JavaScript files**, **504 JSON files**, **473 templates**, **249 CSS files**, graphical resources and configuration files.

  The corpus contains an `unlockapp` application and scripts for client, service, order, payment, messaging and administration functions. `config.php`, a temporary configuration file, certificates, PEM files and a key are present; their values were not reproduced, tested or published. Their presence shows that they were included in the supplied backup; the sources do not specify whether they remain valid or provide access to the service.

  `unlockapp/tmp/export.csv` contains **719 data rows** and fields relating to username, email address, registration date, available balance and amounts due. Full CSV analysis identifies **130 non-zero balances**, totalling **USD 1,493.672**, with a maximum balance of **USD 334.649**. Four rows contain a non-zero amount due, totalling **USD 39.900**. Registration dates range from **13 November 2024** to **25 April 2025**; flag fields are empty across all **719 rows**. Usernames and email addresses are distinct within this file, but the sources consulted do not specify the identity or actual number of affected individuals. Two working JSON files contain **365** and **173** structured items respectively, centred on services or groups. These files indicate application and commercial data, while the sources consulted do not specify the total number of users or transactions.

  **Analytical assessment:** The correspondence between the published domain, the `unlockapp` tree, unlocking and IMEI functions, account data and commercial elements makes association of the backup with ServerUnlockApp highly plausible. The structure is consistent with a website or application-server copy. The sources consulted do not specify the access vector, the actor's real identity, acquisition date or effective use of any potential secrets.

  **Information not specified in the sources:** The exact systems copied, technical access timeline, technical origin of the backup, data completeness, unique persons, duplicates, account validity, certificate and key validity, transactions actually affected, operational impact and any confirmation by ServerUnlockApp. The publication does not describe a real-time compromise of the website.

- **Analysis scope and limitations:** The local tree was inventoried read-only. PHP, JavaScript and other scripts were not executed. Configuration values, keys, certificates, identifiers, emails and financial data were not reproduced. The analysis covers backup structure and CSV/JSON aggregates; it does not validate the completeness of the alleged backup or current access to the application.
- **Risks:** Reuse of customer accounts, balance or payment fraud, targeted phishing, reseller impersonation, exposure of commercial data, potential reuse of secrets and secondary compromise of payment or messaging integrations.
- **SOC / CTI recommendations:** Revoke and rotate potentially exposed secrets, keys, certificates and sessions; review administration, download and export logs; verify customer and reseller accounts; audit payment and messaging integrations; search for code changes and scheduled tasks; preserve original backups and do not execute disclosed scripts.
- **AFRINTEL assessment:** Publication observed; application backup provided and analysed; ServerUnlockApp attribution highly plausible; account and commercial data observed; potential secrets present but not tested; unauthorised access, complete exfiltration and current secret validity unconfirmed.

#### 🇲🇦 Morocco - Midipcom

- **Initial publication date:** 1 October 2026 at 21:25 (displayed time; timezone not specified)
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Technology / IT equipment distribution
- **Website:** [midipcom.ma](https://midipcom.ma/); `pro.midipcom.ma` cited in the publication
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3
- **Source type:** Underground Forum - Publication provided to AFRINTEL + local samples analysed read-only

- **Victim Description:** Midipcom is a Moroccan distributor of IT equipment, refurbished devices, peripherals and printing solutions. Its website presents computers, components, accessories, monitors, printers and toner products.

- **Analysis:**

  **Observed:** A forum post attributed to the **Nameless511** account, timestamped **1 October 2026 at 21:25** according to the displayed time, advertises a “Midipcom database” associated with `midipcom.ma` and `pro.midipcom.ma`. The author claims an Odoo export covering January 2023 to September 2026, **146 CSV files** totalling **158 MB**, and per-file row counts. These volumes and counts remain unverified actor claims. AFRINTEL analysed all **six locally supplied CSV files** read-only, totalling **335,319 bytes**: bank transfers, customers, invoices, mail, purchase orders and sales orders. The files contain recurring Midipcom and Odoo markers, accounting and commercial metadata, and visible dates spanning **May 2023** to **September 2026**. Observable categories cover accounting, stock movements, invoices, orders, business partners and mail. Potentially sensitive fields, including one named `access_token`, are present in the schema; no value was reproduced or tested.

  **Assumption:** Consistency across the six files, the Midipcom references, Odoo structures and the business activity described on the official site strongly supports association of the sample with Midipcom’s operational environment. It does not confirm the exact source system, access vector, complete extraction or the current validity of any possible token or account.

  **Unknown:** The actual number of files and records, the claimed **146 files** and **158 MB**, integrity of the original exports, unique people or organisations affected, duplicates, affected systems, acquisition date and method, any unauthorised access, full exfiltration, operational effect and confirmation by Midipcom or an authority all remain unknown.

- **Analysis scope and limitations:** All six local files were examined in full, including SHA-256 calculation, size, encoding and structural-marker checks. However, each file contains only one line separator: records are concatenated into one continuous line. This anomaly prevents reliable row reconstruction, deduplication or independent validation of the claimed totals. No additional file, 158 MB archive or 146-CSV corpus was provided. The samples remain outside the repository; no personal data, financial value, partner name, payment reference or token is published.

- **Risk assessment:** If authentic, the combination of commercial, invoicing, order, stock, partner and mail information could facilitate invoice fraud, supplier or customer impersonation, targeted phishing and commercial espionage. Fields that may hold tokens require controlled verification and rotation, without assuming that an exploitable secret is present or active.

- **Recommendations:**
  1. Preserve Odoo, database, backup, web-application, mail and administrative-account logs covering at least the period documented by the exports.
  2. Investigate bulk exports, administrator access, provider accounts, unusual logins, scheduled tasks and outbound transfers.
  3. Inventory and controlledly revoke potentially exposed tokens, API keys, sessions and access links, then monitor for reuse.
  4. Validate the scope of customer, supplier and financial data before initiating appropriate notification procedures.
  5. Strengthen detection for bank-detail-change fraud, fraudulent purchase orders and payment requests targeting partners.

- **Sources / Evidence:** forum publication and image supplied on 8 October 2026; six locally supplied CSV files analysed read-only; [Midipcom official website](https://midipcom.ma/). No forum link, data excerpt, identifier, contact, financial reference or secret is published.

### October 2, 2026

#### 🇲🇦 Morocco - Ministry of National Territory Planning, Land Planning, Housing and City Policy

- **Initial publication date:** 2 October 2026 at 15:20 (displayed time; timezone not specified)
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Government / Administration / Housing and urban planning
- **Associated website:** [matnuhpv.gov.ma](https://matnuhpv.gov.ma/) (domain displayed by the actor in the publication; connection to the affected system unconfirmed)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication provided to AFRINTEL

- **Victim Description:** The Moroccan ministry is responsible for public policies relating to national territory planning, urban planning, housing and city policy. Its institutional identity and remit are documented in an organisational decree published by the Moroccan administration.

- **Analysis:**

  **Observed:** A forum post attributed to the **Nameless511** account, timestamped **2 October 2026 at 15:20** according to the displayed time, offers for sale data attributed to the ministry. Its presentation page displays the `matnuhpv.gov.ma` domain. Its title mentions **26,452 candidate records**, while the body claims that more than **2,772 records** were compromised and describes **2,772 full candidate profiles** as the material held and offered for sale. These figures remain contradictory and unverified actor claims. The “Samples” section is distinct: the visible rows that follow are the sample supplied in the exchange. This sample is structured as recruitment-application lists, including third-grade technician and first-grade state-engineer competitions. Visible categories include identity, national identity number, date and place of birth, contact details, address, application status, diplomas, specialisations, degree-awarding institution, examination centre and supporting-document references. No individual value, application-document filename or identifier is reproduced in this record.

  **Analytical assessment:** The institutional logo, the administration’s name, the displayed domain and the data schema are consistent with candidate or recruitment processes connected to the ministry. The sources consulted do not specify whether `matnuhpv.gov.ma` or another ministerial system was compromised; a historical copy, contractor, data aggregator, third-party source or misleading presentation remain possible.

  **Unknown:** The source file, its hash, the actual number of rows and unique people, the records’ authenticity, currency and completeness, originating system, acquisition date and method, any unauthorised access, exfiltration, operational effect and official confirmation by the ministry or an authority all remain unknown.

- **Analysis scope:** Preliminary analysis based on the supplied publication and data visible in the sample provided after the “Samples” section; the original source file was unavailable. This sample cannot validate the claimed volumes, deduplicate affected individuals or establish the data’s technical provenance.

- **Risk assessment:** If authentic, the observed data categories could facilitate identity fraud, targeted phishing, document fraud, social engineering and abuse of recruitment processes. The alleged references to supporting documents could increase risk to candidates; the sources consulted do not specify whether the documents themselves are accessible.

- **Recommendations:**
  1. Preserve logs for application portals, recruitment tools, document repositories and relevant administrative accounts.
  2. Investigate bulk exports, anomalous queries, unusual privileged access and third-party access around the period to be established by the investigation.
  3. Use authorised means to determine whether the field schema and application references correspond to ministerial applications or service providers.
  4. Assess the potential population affected before any notification, and strengthen detection for phishing or fraud targeting applicants.
  5. Do not download the offer, contact the seller or test disclosed individual data.

- **Sources / Evidence:** forum publication and visible sample supplied on 8 October 2026; [Moroccan decree on the ministry’s remit and organisation](https://bdj.mmsp.gov.ma/Fr/Document/10596-D%C3%A9cret-n-2-23-751-du-7-joumada-II-1445-21-d%C3%A9cemb.aspx?KeyPath=594%2F681%2F697%2F10596). No forum link or personal data is published.

#### 🇲🇦 Morocco - Karamtech

- **Initial publication date:** 2 October 2026 at 00:51 (displayed time; timezone not specified)
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Technology / IT and security equipment retail and distribution
- **Website:** [karamtech.ma](https://karamtech.ma/); `kmt.codebarre.ma` cited in the publication
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication provided to AFRINTEL + local samples analysed read-only

- **Victim Description:** Karamtech is a Moroccan e-commerce site presenting IT equipment, accessories, network equipment, printing solutions, access-control and security equipment.

- **Analysis:**

  **Observed:** A post attributed to **Nameless511**, timestamped **2 October 2026 at 00:51** according to the displayed time, announces an Odoo export associated with `karamtech.ma` and `kmt.codebarre.ma`. Its presentation page claims that a raw Odoo database containing more than **2 million** financial journal entries, tax identifiers, plaintext credentials and all employee personal data was compromised. It also claims that the organisation did not reach an agreement with the author. These statements remain unverified actor claims. The detailed message further claims possession of **441 CSV files** covering the entire instance, around **18 GB** of data, approximately **2.08 million** journal entries, **492,900** authentication events, **207,400** orders and **39,100** customer records. It also cites, without testing the stated material, alleged exposure of a database secret and shared session tokens.

  Five locally supplied CSV files, presented as samples, were examined in full read-only: customer, employee, employee identity-and-bank-detail, sales/profit and messaging samples. They total **31,415 bytes** and contain categories consistent with the stated labels: identity and contact data, HR data, financial information, commercial data and messaging. The structures also contain authentication-related fields. No personal, bank, authentication or secret value was reproduced, verified or tested.

  **Analytical assessment:** The displayed logo and domains, Karamtech’s public activity and thematic consistency of the five samples support a plausible association with Karamtech’s commercial environment. The sources consulted do not specify whether the **441 CSV files**, **18 GB**, claimed volumes or alleged secrets originate from a compromised organisational system.

  **Unknown:** The source corpus, its integrity, actual number of files and records, unique people affected, current validity of any secret, password or token, originating system, access vector and date, complete exfiltration, operational impact and confirmation by Karamtech or an authority all remain unknown.

- **Analysis scope and limitations:** The five samples were examined in full, including SHA-256 calculation, size and structural checks. However, each file contains only one line separator: records are concatenated into one continuous line. This anomaly prevents reliable row reconstruction, deduplication and validation of the claimed volumes. No 441-CSV corpus or 18-GB archive was supplied. The samples contain sensitive data and remain outside the repository.

- **Risk assessment:** If the claimed material is authentic, combining customer, commercial, HR, banking and messaging data could enable targeted phishing, supplier fraud, identity abuse and payment fraud. Potential exposure of secrets, passwords or tokens could increase the risk of unauthorised access and warrants precautionary rotation, without assuming that they are genuine or active.

- **Recommendations:**
  1. Preserve Odoo, IAM, database, e-commerce, mail and integration logs to establish the timeline of any incident.
  2. Controlledly rotate application secrets, API keys, service-account passwords, tokens and sessions; do not test values published by the actor.
  3. Investigate bulk exports, unusual privileged access, logins from new addresses, configuration changes and outbound transfers.
  4. Verify data held on customers, suppliers and employees, then prepare appropriate protection and notification measures once scope is established.
  5. Strengthen payment-fraud controls, bank-detail-change procedures and checks for unusual procurement or delivery requests.

- **Sources / Evidence:** forum publication supplied on 8 October 2026; five locally supplied CSV files analysed read-only; [Karamtech official website](https://karamtech.ma/). No secret, password, token, bank value or individual data is published.

#### 🇲🇦 Morocco - Ministry of Investment, Convergence and Evaluation of Public Policies (MICEPP)

- **Initial publication date:** 2 October 2026 at 23:55 (displayed forum timestamp; timezone not specified)
- **Actor / Group:** anisanas2 (displayed forum account; identity and affiliation unverified)
- **Sector:** Government / Administration / Investment and public-policy evaluation
- **Website:** [micepp.gov.ma](https://micepp.gov.ma/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Source type:** Underground Forum and Telegram posts provided to AFRINTEL

- **Victim Description:** MICEPP is the acronym used in the available material for Morocco’s Ministry of Investment, Convergence and Evaluation of Public Policies. Its precise institutional role and any potentially affected systems are not specified in the sources consulted by the observed publications.

- **Analysis:**

  **Observed:** A forum post attributed to the account **anisanas2**, timestamped **2 October 2026 at 23:55** according to the displayed time, advertises “sample documents” and a “database” associated with MICEPP. Supplied Telegram posts, dated **2 October** without a visible year or timezone, repeat this attribution. They claim that more than **150,000 folders** and more than **50,000 investors** are affected, that the corpus exceeds **400 GB**, and that it is offered for sale in parts. These volumes, the acquisition method and the existence of a compromise remain author claims. The posts display a **1.6 GB** file named `part_1_sample.rar` and a **26 KB** file named `investors_sample_300.csv`. Neither the archive nor the CSV was supplied locally or examined. The visible column categories describe identity and contact data, identity-document references, nationality, address, territorial administrative data, and company information, including the Common Enterprise Identifier (ICE). No individual content is reproduced.

  **Analytical assessment:** The name, institutional logo and displayed data categories are consistent with administrative procedures or investment-related schemes. The sources consulted do not specify whether the files came from a system operated by MICEPP; a historical copy, provider, other administration, aggregator or misleading presentation remain possible.

  **Unknown:** Actual access to the advertised files, their hashes, structure, authenticity, currency, number of folders and unique people or organisations, source system, acquisition method and date, scope of any exposure, operational impact, and confirmation by MICEPP or an authority all remain unknown.

- **Analysis scope:** Preliminary analysis based on the publication and supplied material; the advertised source files were not available. The visible material cannot validate the claimed volumes, confirm the technical attribution of the data or establish a compromise.

- **Risk assessment:** If the advertised data is authentic, combining identity, contact, administrative and company data could facilitate targeted phishing, identity abuse, document fraud, social engineering and fraud targeting investors or administrative procedures. The alleged presence of company identifiers and identity-document references warrants prioritised scoping, without assuming that the files are actually available.

- **Recommendations:**
  1. Preserve logs from portals, case-management systems, document repositories, integrations and administrative accounts that may process investment files.
  2. Investigate bulk exports, unusual privileged access, anomalous queries, provider accounts and outbound transfers around the period to be established through investigation.
  3. Verify through authorised means whether the observed field categories correspond to internal systems or providers, without downloading or handling files offered by the author.
  4. Assess the potential scope for affected investors, companies and staff before notification, then strengthen detection of targeted phishing and document fraud.
  5. Establish out-of-band verification for unusual requests involving investments, company details or administrative procedures.

- **Sources / Evidence:** forum and Telegram posts supplied on 9 October 2026. No download link, individual data, identifier, secret or archive is published.

#### 🇿🇦 South Africa - Ampath Laboratories [Data Leak]
- **Public publication / notification date:** 2 October 2026
- **Domain:** `ampath.co.za`
- **Actor / Group:** bytetobreach (displayed publication account)
- **Sector:** Healthcare / Medical laboratories
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim description:** Ampath Laboratories is a South African network of medical laboratories and diagnostic services.
- **Analysis:** The bytetobreach publication claims that 10 of approximately 375 databases were copied and that the overall corpus would exceed 80 million records. It describes HR and employee data, multiple patient databases, financial data, system configurations and application components. The supplied local folder contains structured samples examined read-only: 4,000 employee rows, 5,000 patient rows, 1,000 Medicaid records, 1,000 patient registration records and 997 card-payment records, together with an XML file containing 278,401 structural lines. The schemas contain identity, contact, health, employment, insurance and payment categories. This structural consistency supports the existence of a sample associated with Ampath, but does not validate the 375 databases, the claimed 80 million records, corpus completeness, access method or the real identity of the actor.
- **Analysis scope and limitations:** The five available CSV files and the XML file were examined read-only, including type, size, hash, column and row-volume checks. The file inventory and application components were treated as contextual evidence; no binary, script, link or secret was executed, tested or published. Accounts, identifiers, addresses, medical data, financial data and secrets remain outside the repository.
- **Risk assessment:** Potential exposure concerns health, identity, contact, employment, insurance and payment data. It could facilitate identity theft, targeted phishing, document fraud, financial fraud and targeting of patients or employees. No individual record is reproduced.
- **Sources / Evidence:** supplied publication and visual material; local Ampath samples examined read-only. The bytetobreach account is retained as a publication identifier; its identity and technical affiliation are not established.

#### 🇪🇬 Egypt - Dar Al-Tib (`daralteb.com`) [Ransomware]
- **Initial publication date:** 4 October 2026; some sources indicate 2 October 2026
- **Domain:** [daralteb.com](https://daralteb.com/)
- **Actor / Group:** Krybit
- **Sector:** Healthcare / Fertility and assisted reproduction
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 4 (potential)
- **Victim description:** Dar Al-Tib is an Egyptian medical centre specialising in infertility treatment, in-vitro fertilisation and assisted reproduction.
- **Analysis:** `daralteb.com` appears in a Krybit-associated claim in October 2026. No sample, volume, victim statement, proof of encryption or technical proof of exfiltration was identified. The official website remains accessible, which neither confirms nor invalidates the claim.
- **Risk assessment:** If authentic, potential risks could concern medical data, patient files, administrative information and service continuity. These impacts remain unestablished.
- **Sources / Evidence:** [Dar Al-Tib official website](https://daralteb.com/); [SOCRadar](https://socradar.io/free-tools/ransomware-intelligence/victims/daralteb-com-krybit-76ff21cf); [Yazoul Security](https://www.yazoul.net/intel/claim/2026-10-04-dar-al-tib-ransomware-claim-by-krybit-oct-2026/). Secondary sources describe the case as an publication attributed to the actor.


#### 🇨🇬 Republic of the Congo - e-Solde (`e-solde.cg`) [Access Sale]

- **Initial publication date:** October 2, 2026 at 12:28 (displayed timestamp; timezone not specified)
- **Earlier publication identified retrospectively:** June 28, 2026 at 13:17 by the displayed account Sensitive2025 (timestamp and timezone as displayed)
- **Actor / Group:** SensitiveDarkForum (displayed account; identity and affiliation unverified)
- **Sector:** Public administration / Payroll management
- **Associated website:** [e-solde.cg](https://e-solde.cg/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Access Sale
- **Confidence level:** High
- **Impact level:** Level 4
- **Claimed price:** USD 110,000 (currency inferred from market context; not explicitly displayed)
- **Source type:** Underground forum post and data sample provided to AFRINTEL
- **Public source:** [Circular note on the e-Solde platform](https://lasemaineafricaine.info/wp-content/uploads/2024/04/4227.pdf)

- **Victim Description:** e-Solde is a Congolese platform presented as a government service for consulting payroll statements and managing information relating to public employees. A circular note published in 2024 states that the platform entered production on November 30, 2023. The October 2026 post offers a “government system” associated with the `e-solde.cg` domain for sale.

- **Analysis of provided samples:**

  **Observed:** The tracked post, dated **October 2, 2026**, presents e-Solde as a government system of the Republic of the Congo and displays a claimed price of **110K**. An earlier post with the same domain, price and concordant samples was identified retrospectively on **June 28, 2026** on another forum under the displayed account Sensitive2025. The two posts are treated as one tracked claim or exposure, without double counting. The currency is not explicitly stated; the amount is interpreted as **USD 110,000** only as an assumption based on the convention frequently used in underground markets. The seller invites interested parties to begin a private transaction. Two data samples are visible in the tracked post and in the excerpt provided to AFRINTEL: one sample of accounts and administrative requests, followed by one sample of payroll data. The analysis covers the visible fields and records; it does not cover the entire claimed database.

  **Main observed elements in the sample:**

  - user accounts with identifiers, names, email addresses, telephone numbers, application roles and validation states;
  - password fields present as **bcrypt hashes** beginning with `$2y$10$`; no plaintext password is reproduced;
  - references to profile or supporting-document files;
  - payroll data containing personnel numbers, names, dates of birth, position, sex, agent category and net amount;
  - data relating to civil servants, contractors, police personnel and public-force members;
  - application or registration records containing contacts, identity-document references, associated files and rejection reasons;
  - timestamps mainly falling between **January 26 and February 4, 2026**, together with a `202601` payroll period;
  - the visible structures are consistent with several tables from an employee and payroll-management application.

  **Account and request-sample analysis:** The records present an application structure with an identifier, name, personnel number, contact details, status, role or validating agent, file reference and creation or update dates. Some records contain references to identity documents and administrative rejection reasons. Password fields are populated with bcrypt hashes, showing authentication material in the sample, but not establishing whether the accounts remain active or whether the hashes are exploitable.

  **Payroll-sample analysis:** The second excerpt contains fields corresponding to a row identifier, personnel number, employee identity, date of birth, administrative position, sex, agent type, net amount, payroll period and timestamps. The `202601` period and February 2026 creation dates show that the sample contains data later than 2025. Categories such as civil servant, contractor, police and public force strengthen consistency with a Congolese public-sector payroll-management database.

  **Content qualification:** The samples are not merely interface elements or metadata; they contain structured records with identity data, contact details, professional information, payroll elements, supporting-document references and hashed authentication material. They demonstrate exposure of sensitive data in the provided sample, without demonstrating dataset completeness, the total number of affected people or interactive access to the system.

  **Analytical assessment:** The combination of the `e-solde.cg` domain, Congolese government context, payroll fields and agent categories makes association of the sample with the e-Solde service or a related administrative system plausible. The sale offer and the presence of a sample support an **Access Sale** classification with secondary data exposure. The sources consulted do not specify whether a buyer obtained functional access, whether the actor still controls the system or whether the entire database came directly from official infrastructure.

  **Unknown:** Initial access vector, technical access timeline, total volume, number of affected individuals, existence of interactive access, validity of accounts or hashes, confirmation that the price is denominated in USD, real seller identity and any official confirmation by the Congolese administration remain unknown. The “110K” figure is a commercial claim and is not a confirmed record count.

- **Analysis scope and limitations:** Analysis is limited to the publication and data excerpt provided in the exchange; the complete source file was not provided. Personal values, personnel numbers, contact details, file references and hashes are not reproduced. No access was tested, no contact link was followed and no hash cracking or reuse attempt was performed.
- **Risk assessment:** Potential exposure of public-employee, payroll, identity and administrative-validation data creates risks of payroll fraud, identity theft, targeted phishing, extortion and secondary account compromise. Level 4 reflects the governmental and financial nature of the service and the presence of authentication-related elements.
- **SOC/CTI recommendations:** Reset potentially exposed access and invalidate sessions; rotate application secrets and review password hashes; search for bulk exports and unusual administrative access; review application and database logs; control associated files and documents; audit validation roles and accounts; preserve evidence; do not buy, test or download the claimed access.
- **Counting decision:** The incident is retained in the October corpus and assigned to October tracking because the October 2 post was AFRINTEL's first observation. The June 28 post is documented as a retrospective discovery of the same corpus. The event remains counted as **one incident**. The primary type remains `Access Sale`; data exposure is a secondary effect observed in the sample.



### October 5, 2026

#### 🇲🇦 Morocco - Tera.ma / Sté Tera.ma SARL

- **Initial publication date:** 5 October 2026 at 19:41 (displayed time; timezone not specified)
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Technology / IT equipment distribution and retail
- **Website:** [tera.ma](https://www.tera.ma/) (domain displayed in the publication; identified as a Moroccan IT-commerce website)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication provided to AFRINTEL + local corpus analysed read-only

- **Victim Description:** Tera.ma is a Moroccan IT-equipment distribution and retail company associated with Témara / Rabat. The available material is consistent with sales, inventory, e-commerce, accounting and partner-management operations.

- **Analysis:**

  **Observed:** A post attributed to **Nameless511**, dated **5 October 2026 at 19:41** according to the displayed timestamp, announces a “final release” of an Odoo export associated with Tera.ma. The author claims that the corpus was extracted on **27 September 2025** and comprises **2.3 GB**, **282 CSV files**, **19,595 customers**, **69,197 orders**, **124,088 accounting entries** and **124 internal accounts**. The claimed extraction date and statements concerning negotiation remain actor assertions. The supplied local corpus contains **8,140 files** totalling **2,389,358,436 bytes**, including **282 CSV files** totalling **1,392,426,551 bytes**, **3,693 PDFs**, **3,152 JPEG/JFIF/JPG images**, **413 PNG images**, audio files and a video. Line counts, excluding headers, match the advertised figures for `account_move.csv` (**124,088**), `res_partner.csv` (**19,595**) and `sale_order.csv` (**69,197**). The CSV files contain roughly **21.7 million lines** in total, including headers.

  The reviewed structures cover accounting entries and invoices, orders, partners, inventory, stock movements, mail and application logs. The corpus also includes attachments presented as invoices, scans, contracts, delivery proofs and identity-document images. Filenames, Odoo structures and references to commerce and logistics integrations are mutually consistent. No individual data, bank reference, document, audio file or download link is reproduced here.

  **Assumption:** The match between the published figures and the three key exports, corpus composition, Odoo structures and associated documents provides very strong structural evidence of an operational dataset linked to Tera.ma. It does not, by itself, establish the access vector, the author’s identity, actual extraction date, scope beyond the corpus or official confirmation of the incident.

  **Unknown:** The source and affected systems, access method and duration, production-database completeness, number of unique people and organisations, current validity of accounts or integrations, encryption, operational disruption, existence or outcome of negotiation, and confirmation by Tera.ma or an authority all remain unknown.

- **Analysis scope:** All **8,140 supplied files** were inventoried read-only. The **282 CSV files** were counted, and full structural checks were completed for the principal advertised exports. The corpus contains sensitive personal and commercial data: it remains outside the repository, with no extraction or reproduction of its content. The sources consulted do not specify duplicate counts or the number of unique people.

- **Risk assessment:** Based on the reviewed corpus, the release includes customer, supplier and employee information; invoices and orders; bank or payment information; application logs; commercial documents; and identity documents. If exploited, this material could enable identity abuse, bank-detail-change fraud, fraudulent payment requests, targeted phishing, privacy harm and commercial espionage. The risk is heightened by the presence of documents and third-party integration material.

- **Recommendations:**
  1. Isolate and preserve evidence across Odoo, database, e-commerce, mail, integration and backup environments; retain logs required for forensic investigation.
  2. Controlledly revoke potentially exposed sessions, API keys, tokens, technical accounts and provider access, then investigate anomalous reuse.
  3. Review bulk exports, administrator access, unusual queries, scheduled tasks and outbound transfers before and after 27 September 2025, without treating that date as confirmed.
  4. Prioritise protection for potentially affected customers, partners and employees; prepare applicable notification requirements once scope is established.
  5. Immediately strengthen payment-fraud, bank-detail-change and supplier-impersonation controls; require out-of-band verification for unusual financial requests.

- **Sources / Evidence:** forum post supplied on 8 October 2026; local Tera.ma corpus supplied and analysed read-only. Criminal download links were neither followed nor published.

#### 🇲🇦 Morocco - Cadi Ayyad University (UCA)

- **Initial publication date:** 5 October 2026 at 02:25 (displayed time; timezone not specified)
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Education / Public higher education
- **Website:** [uca.ma](https://www.uca.ma/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication and sample provided to AFRINTEL

- **Victim Description:** Cadi Ayyad University is a Moroccan public university established in Marrakech and active through several disciplines and institutions in the Marrakech-Safi region.

- **Analysis:**

  **Observed:** A post attributed to **Nameless511**, timestamped **5 October 2026 at 02:25** according to the displayed time, is titled as a Cadi Ayyad University leak and advertises **270 free records**. The post describes categories including French and Arabic names, CIN, CNE, APOGÉE identifier, email address, telephone number, date and place of birth, gender, academic programme, enrolment status and photographs. The supplied structured sample contains these categories and references to institutional `@uca.ac.ma` addresses, APOGÉE identifiers, academic programmes and encoded images. Individual data, photographs and file metadata are not reproduced.

  **Assumption:** Consistency among the university’s identity, its official domain, APOGÉE identifiers, institutional addresses and academic information strongly supports attribution of the sample to the UCA ecosystem. It does not document that the data came directly from a system administered by the university: a historical copy, provider or another source remain possible.

  **Unknown:** The complete source file, its hash, actual number of records and unique people, authenticity and currency of the records, originating system, acquisition method and date, scope beyond the claimed **270** records, complete exfiltration, operational impact and confirmation by UCA or an authority all remain unknown.

- **Analysis scope:** Analysis is limited to the supplied publication, material and structured sample content; no source archive or download link was opened. The content contains highly sensitive personal data and photographs, so it was neither reconstructed nor retained in the repository. The sample cannot validate the claimed **270** records or assess duplicates.

- **Risk assessment:** If authentic, the observed data could facilitate identity abuse, document fraud, targeted phishing against students and staff, targeting of university accounts and abuse of administrative processes. Photographs combined with civil and academic identifiers heighten fraud and privacy risks.

- **Recommendations:**
  1. Preserve logs across APOGÉE, admissions, identity, directory, photo-storage and administrative-account systems.
  2. Investigate bulk exports, unusual privileged access, provider accounts and outbound transfers of student data.
  3. Assess the scope of potentially affected students, alumni and staff without reusing published values.
  4. Strengthen university-account protections and monitor phishing, document fraud and impersonation attempts targeting the UCA community.
  5. Apply appropriate notification and protection procedures after the actual scope is established.

- **Sources / Evidence:** forum publication and structured sample supplied on 8 October 2026; [UCA official website](https://www.uca.ma/). No criminal link, national identifier, email address, telephone number, photograph or other individual data is published.

#### 🇿🇦 South Africa - TechExchange (`techexchange.co.za`)

- **Initial publication date:** 5 October 2026 at 15:34 (displayed timestamp; timezone not specified)
- **Actor / Group:** Sensitive2025 (displayed forum account; identity not established)
- **Sector:** Retail / E-commerce / Mobile phones
- **Website:** [techexchange.co.za](https://techexchange.co.za/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High for the existence of the publication and domain consistency; Medium for attribution of the full corpus to TechExchange
- **Impact level:** Level 4 (potential)
- **Source type:** Forum publication with visible CSV sample and structured extract supplied to AFRINTEL

- **Victim description:** TechExchange is presented as a South African company specialising in new, pre-owned, refurbished and demo mobile phones.
- **Analysis:** The publication offers website backup files described as approximately **6,000 CSV files totalling 1 GB**, covering **2014-2022**. The visible header and structured extract correspond to an e-commerce order export containing order identifiers, order and payment dates, statuses, amounts, currency, payment methods, transaction identifiers, customer accounts, email addresses, telephone numbers, billing and shipping addresses, geographic fields, IP addresses, user agents, ordered items, taxes, discounts and order notes. The visible fields are consistent with an online-commerce platform, and several elements refer to South Africa and the ZAR currency. Individual data, contact details, transaction identifiers, IP addresses and order references are not reproduced.
- **Observed:** The publication is dated 5 October 2026 at 15:34 according to the displayed timestamp; the `techexchange.co.za` domain, business description, CSV header and structured records are visible in the supplied material.
- **Assumption:** If authentic and sourced from TechExchange systems, the sample could affect customers, orders, payments and deliveries, creating risks of payment fraud, phishing and impersonation. Structural consistency alone does not validate the technical origin or completeness of the corpus.
- **Unknown:** Initial access vector, extraction date, actual number of files and records, backup completeness, source systems, current data validity, exposure of passwords or tokens, real actor identity and any official confirmation remain unknown.
- **Analysis scope and limitations:** Detailed analysis of the supplied publication, visual material and structured extract; the complete source file, its hash and the advertised 6,000 files were not available. No download link or criminal contact was followed, and no raw personal data is retained in the repository.
- **Risk assessment:** Potential exposure of order, contact, delivery and payment data could facilitate transaction fraud, fake refunds, targeted phishing, customer or supplier impersonation and privacy harm.
- **Sources / Evidence:** visual material and structured extract supplied to AFRINTEL; forum publication attributed to the Sensitive2025 account. Raw data and download links remain outside the repository.

#### 🇿🇦 South Africa - Thrive Online Group (`thriveonlinegroup.com`)

- **Initial publication date:** 5 October 2026 at 19:46 (displayed timestamp; timezone not specified)
- **Actor / Group:** Sorb (displayed forum account; identity and affiliation not established)
- **Sector:** Technology / Digital marketing
- **Associated website:** `thriveonlinegroup.com`
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High for the existence of the publication and visible extracts; Medium for attribution of the full dataset to Thrive Online Group
- **Impact level:** Level 4 (potential)
- **Source type:** Forum publication and visible CSV extracts supplied to AFRINTEL

- **Victim description:** Thrive Online Group is presented as a South African organisation active in targeted digital marketing.
- **Analysis:** The post attributed to the **Sorb** account claims approximately **17 million lines**, more than **10 million unique personal-data records** and a price of **USD 1,000**. These volumes and the commercial offer remain the author's claims. The two visible CSV extracts contain fields consistent with South African personal data: user or SMS identifiers, names, telephone numbers, South African identifiers, email addresses, province, postal code, opt-out indicator and campaign code. The second extract includes mobile numbers and RSA identifiers. No individual value is reproduced in the repository.
- **Observed:** Publication visibly dated **5 October 2026 at 19:46** according to the displayed timestamp; domain `thriveonlinegroup.com`; structured extracts showing identity, contact and South African identification fields; displayed price of **USD 1,000**.
- **Assumption:** If authentic and sourced from Thrive Online Group or an associated provider, the exposure could facilitate phishing, identity abuse, telephone fraud and targeting of SMS campaigns. Field consistency does not validate technical origin or the claimed volumes.
- **Unknown:** Access vector and date, source system, actual number of unique people, corpus completeness, current data validity, existence of exfiltration, real seller identity and any confirmation by Thrive Online Group or an authority remain unknown.
- **Analysis scope and limitations:** Analysis is limited to the supplied publication, visual material and visible CSV extracts; the complete source files, their hashes and the claimed **17 million lines** were not available. No download link or criminal contact was followed. Raw personal data remains outside the repository.
- **Risk assessment:** If authentic, the combination of contact data, South African identifiers and campaign data could support targeted phishing, impersonation, telephone or SMS fraud and identity correlation.
- **SOC/CTI recommendations:** Preserve logs from marketing applications, CRM, databases, service accounts and SMS integrations; investigate bulk exports and unusual privileged access; review associated providers and campaigns; monitor for domains, numbers and messages impersonating the organisation; do not buy, download or test the offered data.
- **Sources / Evidence:** visual material and structured extracts supplied to AFRINTEL; forum publication attributed to the Sorb account. No identifier, telephone number, email address or criminal-market link is published.


#### 🇿🇦 South Africa - Lawyers for Human Rights [System Intrusion]
- **Security notice publication date:** 15 October 2026
- **Official domain:** [lhr.org.za](https://www.lhr.org.za/)
- **Actor / Group:** Non établi
- **Sector:** NGO / Human rights / Legal services
- **Status:** Incident Confirmed by Victim
- **Incident type:** System Intrusion
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim description:** Lawyers for Human Rights is a South African organisation providing human-rights legal services and assistance.
- **Analysis:** In its 15 October 2026 security notice, LHR stated that a database hosted by a third-party service provider was subject to unauthorised access on 5 October. LHR's investigation concluded that an unauthorised third party accessed and downloaded information. The environment was secured, an investigation opened, and authorities and potentially affected individuals were notified.
- **Potentially affected data:** names, South African identity numbers, passport or refugee/asylum-seeker permit numbers, addresses, telephone numbers, email addresses, dates of birth, gender, nationality, employment and contractor information, tenant and lease information, client and beneficiary records, organisation information, legal-case documents and correspondence, and data relating to partners, donors, employees, service providers and tenants.
- **Number of people and volume:** Not established.
- **Risk assessment:** Legal, identity, contact and vulnerable-person data may create significant risks of identity theft, phishing, document fraud, targeting and intimidation. No ransomware, encryption or leak-site publication has been established.
- **SOC/CTI action:** Preserve and correlate third-party, database, administrative-account and outbound-gateway logs around 5 October; revoke access and secrets shared with the provider; review other environments using the same identities; monitor fake legal correspondence and document requests; use out-of-band validation with LHR.
- **Sources / Evidence:** [LHR official notice dated 15 October 2026](https://www.lhr.org.za/lhr-news/important-notice-regarding-a-security-incident/); [LHR news index](https://www.lhr.org.za/lhr-news/). The exact corpus scope and number of affected people remain under assessment.

#### 🇪🇬 Egypt - Millensys (`millensys.com`) [Ransomware]
- **Initial publication date:** 5 October 2026
- **Domain:** [millensys.com](https://www.millensys.com/)
- **Actor / Group:** MedUSlocker
- **Sector:** Healthcare software / Information technology
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3 (potential)
- **Victim description:** MILLENSYS is an Egyptian company providing software and IT solutions for healthcare providers, including imaging, medical-record and telemedicine systems.
- **Analysis:** The victim appears in a claim associated with MedUSlocker. No sample, volume, proof of encryption, exfiltration or statement from MILLENSYS was identified.
- **Risk assessment:** An authentic claim could concern software, healthcare environments, customer data or imaging systems. None of these impacts is established.
- **Sources / Evidence:** [MILLENSYS official website](https://www.millensys.com/about); ransomware publication extracted from the corpus provided to AFRINTEL.

### October 6, 2026

#### 🇪🇬 Egypt - Beni Suef Technological University [Ransomware]
- **Initial publication date:** 6 October 2026
- **Institutional domain in the source:** `bsut.edu.eg`
- **Actor / Group:** UmBra
- **Sector:** Higher education / Technology
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3 (potential)
- **Victim description:** Beni Suef Technological University is an Egyptian public technological university offering programmes in industrial technology, information technology, mechatronics and energy.
- **Analysis:** The victim appears in a claim associated with UmBra. No sample, volume, proof of encryption, exfiltration or statement from the university was identified.
- **Risk assessment:** Potential risks concern administrative systems, student accounts, learning platforms and personal data. No affected scope is established.
- **Sources / Evidence:** [Beni Suef Technological University official website](https://btu.edu.eg/en/home/); [Egyptian institutional portal](https://bani-suef-tu.mohesr.gov.eg/); ransomware publication extracted from the corpus provided to AFRINTEL.

### October 3, 2026

#### 🇲🇦 Morocco - NextLevel PC

- **Initial publication date:** 3 October 2026 at 12:00 (displayed time; timezone not specified)
- **Later publication:** 7 October 2026 at 01:41, announcing free release of the full database (displayed time; timezone not specified)
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** E-commerce / IT equipment and gaming
- **Website:** [nextlevelpc.ma](https://nextlevelpc.ma/) (domain displayed in the publication; identified as a Moroccan computer-equipment retailer)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication and sample provided to AFRINTEL

- **Victim Description:** NextLevel PC is a Moroccan e-commerce site described in the available material as specialising in IT equipment and gaming. The domain and its technical connection to a compromised system have not been independently confirmed.

- **Analysis:**

  **Observed:** An initial post attributed to **Nameless511**, dated **3 October 2026 at 12:00** according to the displayed timestamp, presents the NextLevel PC database and describes the company, its commercial volumes and the affected data categories. A later post dated **7 October 2026 at 01:41** announces free release of the “full database” after a period the author describes as **72 hours without response**. The author claims **52,545 customer accounts**, **60,262 shipping addresses**, **47,653 orders**, **11 internal accounts**, **14,160 cart/discount rules**, and transaction history worth **MAD 122.9 million**. The complete supplied and analysed local corpus contains **eight CSV files** totalling **30,556,090 bytes**, and exactly confirms the first five counts: `customers.csv` (**52,545** rows), `addresses.csv` (**60,262**), `orders.csv` (**47,653**), `employees.csv` (**11**) and `cart_rules.csv` (**14,160**). The **47,653 orders** total **122,865,604.60** in the payment field, consistent with the author’s claimed **MAD 122.9 million**. The currency is attributed to the publication; it is not independently established by that calculation.

  The corpus covers customer accounts, shipping addresses, orders, order details, products, discount rules, messages and internal accounts. It contains **69,957** order-detail rows and **4,168** messages. Observed dates span **May 2021** to **November 2026**, with the latter bound including discount-rule end dates. Customer files contain contact, preference, password and session-key fields. All **52,545** password values are populated; **42,743** follow a format beginning with `$2`, while the remainder use an unidentified format. These values were neither reproduced, tested nor subjected to password-cracking. No individual value, email address, telephone number, authentication string or order data is published.

  **Assumption:** The exact match between published figures and the eight exports, consistent e-commerce table structure and displayed logo/domain provide very strong structural evidence of an operational corpus linked to NextLevel PC. It does not, by itself, establish the access vector, extraction date, official compromise or completeness of systems not included in the supplied files.

  **Unknown:** The algorithm and validity of all authentication values, number of unique people  -  distinct from accounts, addresses or orders  -  currentness of contact information, technical source, acquisition method and date, scope beyond the corpus, operational impact, any negotiation and confirmation by the organisation or an authority all remain unknown.

- **Analysis scope:** All eight local CSV files were examined in full read-only, including SHA-256 calculation, schema, row-width, exact-duplicate and date-range checks. Every file has a consistent row width, and no exact row duplicate was observed. These checks do not validate the absence of business-level duplicates, each person’s identity or completeness of the production database. No criminal link was opened, and no personal data or authentication string is retained in the repository.

- **Risk assessment:** If authentic, the combination of contact details, shipping addresses, order histories and authentication values could facilitate targeted phishing, credential-reuse attempts, customer impersonation, delivery fraud and social engineering. The alleged transaction information could also support targeted commercial fraud.

- **Recommendations:**
  1. Preserve store, database, authentication, payment, logistics-integration and administrative-account logs.
  2. Identify potentially affected accounts, reset passwords where justified by the investigation, and invalidate potentially exposed sessions and application keys.
  3. Review password-hashing settings, rate limits, administrator MFA and API access.
  4. Increase monitoring for shipping-address changes, refund requests, account-takeover attempts and phishing targeting customers.
  5. Establish the scope before notification, without using published data to contact or authenticate individuals.

- **Sources / Evidence:** forum publication and visible sample supplied on 8 October 2026. No criminal link, identifier, password hash, session key or individual data is published.

#### 🇪🇹 Ethiopia - Ministry of Health (`moh.gov.et`) [Data Leak]

- **Initial publication date:** October 7, 2026 at 16:51 (displayed timestamp; timezone not stated)
- **Actor / Group:** Individual (displayed account; identity and affiliation unverified)
- **Sector:** Public health / Government administration
- **Website:** [moh.gov.et](https://moh.gov.et/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Forum publication, supplied material and local sample supplied to AFRINTEL

- **Victim Description:** Ethiopia’s Ministry of Health is the national administration responsible for health policy, coordination of health programmes and oversight of health facilities and professionals in Ethiopia.

- **Analysis:**

  **Observed:** A post attributed to the **Individual** account, timestamped **October 7, 2026 at 16:51** according to the displayed time, presents `moh.gov.et` under a “Master Facilities” title and claims **4 million records** and **13 GB**, described as “PART2”. The supplied material presents Ethiopian digital identity cards, an Addis Ababa resident card and a card associated with the Oromia Health Bureau. Visible categories include highly sensitive identity and health-related information, including photograph, full name, date of birth, nationality, sex, registration number and blood group. No individual value is reproduced here.

  The local `facility 83463 clean csv.txt` sample was examined in full read-only. It is an ASCII file of **13,269 bytes**, with **one physical line** and **1,442 comma-separated fields**; it has no usable header row. Aggregate markers include **67 email-like strings**, **111 phone-like values**, **61 UUIDs**, **77 dates**, **3 URLs** and Ethiopian-domain references including `orhb.gov.et`. The content also contains markers related to facilities, hospitals, clinics and doctors. These occurrences are not unique-person counts and do not allow reliable reconstruction of the original schema.

  The supplied material and local text also present structures related to user accounts, roles, identities, facilities, health professionals and authentication fields. Sensitive values were not tested, published or used to attempt access. The supplied unmasked identity documents are treated as local evidence and no facial or identifying data is added to the repository.

  **Analytical assessment:** The consistency between `moh.gov.et`, Ethiopian health-structure references, visible official-looking cards and a health-platform data structure strongly supports association with a Ministry-related or health-sector environment. The sources consulted do not specify whether the Ministry’s own system was directly compromised or whether all data originated from one environment.

  **Unknown:** The claimed 4 million records and 13 GB, the existence and contents of Part 1, corpus completeness, unique-person count, extraction date, access vector, authenticity of each document, current validity of identifiers or secrets, operational impact and any confirmation by the Ministry or an authority remain unknown.

- **Analysis scope and limitations:** The local text sample was examined in full, including SHA-256, size, physical-line count, apparent field width and aggregate marker counts. The supplied material was reviewed without transcribing personal data. The file is not a normalized CSV export: fields cannot be reliably mapped to columns, and motif counts are not individual counts. The complete claimed corpus was not available.
- **Risks:** Identity theft, document fraud, targeted phishing, account compromise, medical-privacy harm, targeting of health professionals and exploitation of health-facility information.
- **SOC / CTI recommendations:** Preserve IAM, API, database, export and download logs; revoke potentially exposed secrets or sessions after validation; strengthen MFA and privileged-account controls; review identity and health-system access; search for mass exports and outbound transfers; protect identity-document copies and apply applicable notification procedures.
- **AFRINTEL assessment:** Publication observed and sensitive sample analysed; attribution to an Ethiopian health-sector environment highly plausible; direct Ministry compromise, global volume and acquisition method unconfirmed.
- **Sources / Evidence:** Forum post and supplied material provided on October 30, 2026; local sample examined read-only. No national identifier, name, email address, phone number, photograph or secret is published in this record.

### October 7, 2026

#### 🇪🇬 Egypt - SANAtech Global Solutions [Ransomware]
- **Publication date:** 7 October 2026
- **Actor / Group:** UmBra (claimed attribution only)
- **Sector:** Technology / Digital services
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim description:** SANAtech Global Solutions is presented as an Egyptian technology and digital-services company.
- **Analysis:** The victim appears on a source associated with UmBra. No exploitable sample or victim statement was identified. Intrusion, exfiltration, encryption and service disruption are not specified in the sources consulted.

### October 8, 2026

#### 🇪🇬 Egypt - FSE, Cairo University [Ransomware]
- **Initial publication date:** 8 October 2026
- **Institutional domain:** [cu.edu.eg](https://cu.edu.eg/)
- **Actor / Group:** UmBra
- **Sector:** Higher education / University
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3 (potential)
- **Victim description:** FSE is presented in the source corpus as an entity of Cairo University associated with higher education and training.
- **Analysis:** The victim appears in a claim associated with UmBra. No sample, volume, affected system, proof of encryption, exfiltration or statement from Cairo University was identified.
- **Risk assessment:** Potential risks concern university platforms, student data and administrative documents. The sources consulted do not describe the resulting exposure scope.
- **Sources / Evidence:** [Cairo University official website](https://cu.edu.eg/); ransomware publication extracted from the corpus provided to AFRINTEL.

### October 9, 2026

#### 🇲🇦 Morocco - National Press Council (CNP)

- **Initial publication date:** 9 October 2026 at 03:20 (displayed timestamp; timezone not specified)
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Independent public institution / Press regulation
- **Website:** [cnp.press.ma](https://cnp.press.ma/fr/home-fr/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication provided to AFRINTEL

- **Victim Description:** The National Press Council is an independent national institution responsible, among other duties, for self-regulation of the press and publishing sector and for issuing professional press cards in Morocco.

- **Analysis:**

  **Observed:** A forum post attributed to the account **Nameless511**, timestamped **9 October 2026 at 03:20** according to the displayed time, identifies the National Press Council (CNP) as a target in Morocco. The author claims to hold **39,000 records** and offers a “full database” for sale. The post advertises a sample of **30 PDFs**, presented as containing real documents. Listed data categories include full names, CIN numbers, home addresses, telephone numbers, email addresses, workplaces, academic qualifications, press-card numbers and renewal dates. The advertised files and associated links were not opened, downloaded or examined. The volumes, the exact nature of the documents, their source and any compromise remain author claims. No individual data is reproduced.

  **Analytical assessment:** The institution’s name, displayed logo and cited data categories are consistent with CNP functions, including processes related to professional press cards. The sources consulted do not specify whether the data came from a CNP-operated system; a historical copy, provider, other source or misleading presentation remain possible.

  **Unknown:** Actual access to the advertised sample or database, file hashes and structure, their authenticity and currency, actual number of unique people affected, source system, acquisition method and date, exposure scope, operational impact, and confirmation by the CNP or an authority all remain unknown.

- **Analysis scope:** Preliminary analysis based on the supplied post; the advertised PDFs and database were not locally available or examined. This analysis cannot validate the claimed **39,000 records**, the documents’ authenticity or the existence of an intrusion.

- **Risk assessment:** If the advertised material is authentic, combining contact details, identity documents, professional information and press-card data could expose journalists and other professionals to identity abuse, targeted phishing, social engineering, doxxing and document fraud. Potential exposure of people working in the press may also increase risks of targeting and harassment.

- **Recommendations:**
  1. Preserve logs from press-card management applications, submission portals, document systems, directories and administrative accounts.
  2. Investigate bulk exports, unusual file access, anomalous privileged access, provider accounts and outbound transfers.
  3. Assess through authorised means whether the published data categories correspond to CNP systems, without opening or downloading files offered by the author.
  4. Prepare protection and communication measures for potentially affected people once the actual scope is established.
  5. Strengthen detection of phishing, impersonation, document fraud and harassment targeting press-card holders or applicants.

- **Sources / Evidence:** forum post supplied on 9 October 2026; [CNP duties and powers](https://cnp.press.ma/fr/2020/05/06/missions-et-pouvoirs-du-conseil-national-de-la-presse/). No download link, document, individual data or author contact is published.

#### 🇲🇦 Morocco - Ministry of Endowments and Islamic Affairs

- **Initial publication date:** 9 October 2026 at 03:44 (displayed time; timezone not specified)
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Government / Administration / Religious affairs
- **Official website:** [habous.gov.ma](https://www.habous.gov.ma/fr/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication, supplied material and local corpus provided to AFRINTEL

- **Victim Description:** The Ministry of Endowments and Islamic Affairs is a Moroccan public institution responsible, among other functions, for religious affairs and the administration of endowment assets. Its official website is [habous.gov.ma](https://www.habous.gov.ma/fr/).

- **Analysis:**

  **Observed:** A post attributed to **Nameless511**, timestamped **9 October 2026 at 03:44** according to the displayed time, advertises a “full candidate database” associated with a first-grade state engineer recruitment examination. The author claims approximately **109,000 rows** in CSV, XLSX and PDF-attachment formats. Displayed categories include Arabic and Latin-script names, national identity number, date and place of birth, gender, address, contact information, diplomas, specialities, issuing institutions, application status, rejection reason, examination centre and uploaded documents. The supplied local corpus includes **33 XLSX files** and one CSV, totaling approximately **44.2 MB**. XML-structure analysis of all XLSX files identified **109,673 rows**, including **109,640 data rows** assuming one header row per file: a volume consistent with the claim. The visible sample has a structure consistent with candidate application files. No individual data, identity document or attachment is reproduced.

  **Assumption:** Consistency between the examination title, administrative fields and file structure supports a link to a Moroccan public-recruitment process attributed to the ministry. It does not document the files came directly from a ministry-administered system or that the claimed full volume was exfiltrated.

  **Unknown:** The actual number of candidates and unique people, the corpus’s precise coverage, originating system, acquisition method and date, authenticity and currency of the files, actual presence of every claimed attachment, operational impact and any official confirmation remain unknown.

- **Analysis scope:** Analysis is limited to the publication, supplied material and a supplied local corpus. The author’s approximately **109,000**-row claim is consistent with AFRINTEL’s structural count of the XLSX files, but this does not confirm the number of unique people or completeness of the corpus. The highly sensitive observed data was neither reconstructed nor retained in the repository.

- **Risk assessment:** If authentic, the data could enable identity abuse, targeted phishing against candidates, document fraud, misuse of application information and large-scale privacy harm.

- **Recommendations:**
  1. Preserve logs for recruitment, application-submission, document-storage and administrative-account systems.
  2. Investigate bulk exports, unusual privileged access and outbound transfers related to the relevant recruitment processes.
  3. Establish the actual scope of potentially affected candidates without using published values.
  4. Strengthen account security, document-access controls and detection of phishing targeting candidates.
  5. Apply appropriate notification and protection procedures after validating the incident and its scope.

- **Sources / Evidence:** forum publication, sample and local corpus supplied on 9 October 2026. No criminal link, national identifier, address, telephone number, email, document or other individual data is published.
- **Institutional source:** [official website of the Ministry of Endowments and Islamic Affairs](https://www.habous.gov.ma/fr/)

### October 10, 2026

#### 🇪🇬 Egypt - Helwan University (HITU) [Ransomware]
- **Initial publication date:** 10 October 2026
- **Domain:** [helwan.edu.eg](https://www.helwan.edu.eg/)
- **Actor / Group:** UmBra
- **Sector:** Higher education / University
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3 (potential)
- **Victim description:** Helwan University is an Egyptian public university located in Cairo and the Greater Cairo area.
- **Analysis:** The victim appears in a claim associated with UmBra. No sample, volume, proof of encryption, exfiltration or statement from the university was identified.
- **Risk assessment:** Potential risks concern administrative systems, student accounts, learning platforms and personal data. No affected system is established.
- **Sources / Evidence:** [Helwan University official website](https://www.helwan.edu.eg/); ransomware publication extracted from the corpus provided to AFRINTEL.

### October 11, 2026

#### 🇲🇦 Morocco - Decathlon Morocco

- **Sector:** Retail / Sporting Goods / E-commerce
- **Victim:** Decathlon Morocco
- **Website:** https://www.decathlon.ma/
- **Initial publication date:** October 11, 2026
- **AFRINTEL detection date:** October 11, 2026
- **Incident Type:** Data Leak / Alleged Personal Data Exposure
- **Threat Actor / Group:** Nameless511
- **Claimed Volume:** More than 24,438 customer orders
- **Status:** Claim - Data Sample Published
- **Confidence Level:** Medium


##### Incident Description

A threat actor operating under the alias Nameless511 published a data leak claim on the DarkForums cybercrime forum targeting Decathlon Morocco, a sporting goods retailer.

The actor claims to have released a database containing more than 24,438 customer orders associated with several Decathlon stores and distribution channels in Morocco.

The locations and entities mentioned in the claim include:

- Decathlon Kenitra
- Decathlon Corniche
- Decathlon Rabat
- Decathlon Ecom
- Decathlon Marina
- Decathlon Derb Ghallef

According to the threat actor, the exposed information includes:

- Customer first and last names
- Moroccan telephone numbers
- Delivery addresses
- GPS coordinates (latitude and longitude)
- Order identifiers and references
- Order amounts and delivery dates
- Payment methods
- Delivery instructions
- Operational comments and employee notes
- Assembly, return and repair information

##### Observed Evidence

A data sample displayed in the threat actor's publication was examined as part of the CTI investigation.

The reconstructed sample contains 522 records and 30 columns with structured order and delivery information.

Observed fields include:

- Order references
- Store and depot identifiers
- Delivery statuses
- Customer information
- Addresses and GPS coordinates
- Order amounts
- Payment information
- Logistics-related comments

The observed records cover the period from September 29, 2021, to January 5, 2022.

Additional Excel files were also provided through a download link shared in the threat actor's publication.

Their relationship to the same dataset and their exact connection to Decathlon Morocco remain unverified.

##### CTI Assessment

The sample structure is consistent with an export from an order management, route planning or delivery management application.

These characteristics support the possibility that the published records are associated with Decathlon Morocco's commercial and logistics operations.

However, the available sources do not specify whether the exposure resulted from:

- A direct compromise of Decathlon Morocco;
- A compromise of a logistics service provider;
- Unauthorized access to a third-party platform;
- The subsequent disclosure of a historical data export.

The claimed volume of 24,438 customer orders has not been independently verified.

The publication date should not be interpreted as the date of the original compromise.

##### Potential Risks

- Targeted phishing and smishing
- Voice phishing and identity impersonation
- Delivery-related fraud
- Social engineering
- Misuse of customer order histories
- Privacy risks involving precise GPS coordinates
- Geographic targeting of affected individuals

##### SOC/CTI Recommendations

- Verify the authenticity and origin of the published data.
- Identify systems and third parties with access
  to customer order and delivery records.
- Investigate suspicious access and bulk data exports.
- Review logistics platform access logs.
- Audit internal and third-party account permissions.
- Assess applicable data breach notification obligations.
- Notify affected individuals where legally required.
- Raise customer awareness of delivery-related scams
  and social engineering attempts.

##### Conclusion

Nameless511's publication represents a credible data exposure claim requiring further investigation.

The available sample contains structured records consistent with commercial and logistics operations associated with Decathlon Morocco.

The authenticity of the complete dataset, the actual scope of the exposure and the source of the extracted information remain unconfirmed.

There is currently insufficient evidence to establish a direct compromise of Decathlon Morocco's infrastructure.

#### 🇲🇦 Morocco - CNESTEN [Ransomware]
- **Initial publication date:** 11 October 2026
- **Institutional domain:** [cnesten.org.ma](https://www.cnesten.org.ma/)
- **Actor / Group:** Qilin
- **Sector:** Nuclear research / Science and technology
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 4 (potential)
- **Victim description:** CNESTEN is a Moroccan public institution responsible for research and applications in energy, nuclear science and nuclear technology.
- **Analysis:** CNESTEN appears in a claim associated with Qilin. The source row provides no data description or technical proof. No sample, volume, encryption, exfiltration or statement from CNESTEN was identified.
- **Risk assessment:** If authentic, a claim could concern sensitive scientific, administrative or operational data. No impact to a nuclear facility or safety has been established.
- **Sources / Evidence:** [CNESTEN](https://www.cnesten.org.ma/storage/2023/06/Brochure-CNESTEN-Eng.pdf); ransomware publication extracted from the corpus provided to AFRINTEL.

### October 12, 2026

#### 🇲🇦 Morocco - Eurogate Tanger (`eurogate-tanger.com`)

- **Initial publication date:** 12 October 2026 at 13:55:54 (displayed timestamp; timezone not specified)
- **Observed disclosure date:** 19 October 2026 at 13:27 UTC (announced first batch)
- **Actor / Group:** N0n (name displayed by the source; identity and affiliation unverified)
- **Sector:** Maritime transport / container-terminal operations
- **Website:** [eurogate-tanger.com](https://www.eurogate-tanger.com/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4 (potential)
- **Source type:** Ransomware tracker and actor-published archive

- **Victim Description:** Eurogate Tanger is a container-terminal operator in Morocco. Systems associated with `eurogate-tanger.com` are described in the post as containing commercial correspondence, operational documents and internal working files.

- **Analysis:**

  **Observed:** The observed record identifies Eurogate Tanger, Morocco, the maritime-transport sector, the N0n group and a `NOT PAID – EXPOSED` statement. “Published data” is listed as `N/D`. The supplied local archive, `eurogate_tanger.com-leak.zip`, passed a read-only integrity test and contains **355 files**, **373,065,003 uncompressed bytes**, **373,150,373 archive bytes**, with no ZIP encryption. Files are grouped under `eurogate-tanger.com` and include DOCX, XLS/XLSX, PDF, MSG, PPTX, ODS, EDI, XML, log/trace, SQL, archive and technical files. The included README explicitly describes a **first publication batch** and announces possible additional batches.

  A read-only static analysis covered all **354 files extracted under the domain**: hashes, actual file types, structure and textual/XML content where extractable. It included **98 DOCX, 86 XLSX, 11 XLS, 5 PPTX, 2 ODS, 22 PDF, 10 MSG, 32 TRC files, 32 TRM files, 19 RAR, 5 ZIP, 1 JAR, 1 Java class, and EDI/XML/WSDL/SQL and log files**. XML analysis of the XLSX files represents approximately **652,708 row elements** and **13,686,923 cell elements**; these are structural indicators and do not directly represent unique people or operations.

  Text and XML content repeatedly contains references consistent with **EGT, Eurogate, Tanger, OPUS Terminal, terminal, port, containers, vessels, cargo, reefers, gates, cranes, yard, voyages, trucks and operational movements**. DOCX and XLSX files also contain references to release notes, hotfixes, SQL scripts, traces and technical exchanges associated with this environment. The RAR archives, ZIP archives and JAR were inventoried without execution; their members and sizes were checked.

  No file was executed. No VBA macro marker was detected in the inspected Office containers. PDFs and MSG files received static string and metadata analysis, without rendering or full interpretation of embedded objects. Email-address markers are present in several text-like files; no individual data is reproduced in this report.

  **Assumption:** The domain name in the archive tree, the organization name, the stated sector and the announced file categories are consistent with an exposure of Eurogate Tanger internal data. This supports archive-to-victim attribution, but does not document the access method, initial compromise, data completeness or the absence of a provider or third-party environment.

  **Unknown:** The technical access timeline and vector, the total volume actually exfiltrated, N0n’s real identity and capabilities, completeness of the first batch, operational impact, any confirmation by Eurogate Tanger or an authority, and the exact content of the documents remain unknown.

- **Analyzed archive hash:** SHA-256 `87bb4495b774c21919af26daf9b3ab807e57f78d7fad5879d0176bd9df28c891`.
- **Analysis scope and limitations:** All 354 files extracted under the domain were covered by static analysis of actual type, hashes, structure and textual/XML content where extractable. This method does not decrypt protected files, visually render every page or validate every embedded object. It is not official confirmation of the incident. The archive remains outside the AFRINTEL repository.
- **Risk assessment:** Potential exposure of operational documents, vessel and container data, configurations or release notes, scripts and technical traces could facilitate social engineering, document fraud, employee targeting, preparation of port-operation disruption or identification of application dependencies. Level 4 reflects the potentially critical nature of this environment; actual disruption or access to control systems is not specified in the sources consulted.
- **Sources / Evidence:** public record observed on 20 October 2026; local archive supplied for analysis; no onion address, raw personal data or individual value is published.

### October 12, 2026

#### 🇿🇦 South Africa - Aeroklas Duys / Duys Engineering Group (`aeroklasduys.co.za`) [Ransomware]
- **Initial publication date:** 12 October 2026
- **Domain:** [aeroklasduys.co.za](https://aeroklasduys.co.za/)
- **Actor / Group:** Deadlock
- **Sector:** Automotive manufacturing / Engineering and fabrication
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3 (potential)
- **Victim description:** Aeroklas Duys is a South African company associated with Duys Engineering, active in automotive manufacturing, mechanical engineering and industrial services.
- **Analysis:** Aeroklas Duys / Duys Engineering Group appears in a claim associated with Deadlock. The organisation’s identity and South African location are corroborated, but no sample, volume, proof of encryption, exfiltration or victim statement was identified.
- **Risk assessment:** Potential risks concern industrial data, manufacturing operations, suppliers and production systems. No operational impact is established.
- **Sources / Evidence:** [Duys Engineering Group](https://duysgroup.com/); [Aeroklas Duys supplier registry](https://cloud.procureactiv.co.za/procurement/suppliers/view/aeroklas); [DeXpose](https://www.dexpose.io/deadlock-ransomware-strikes-aeroklas-duys-in-south-africa/).

### October 14, 2026

#### 🇿🇦 South Africa - Europ Assistance South Africa / AZOZA [Ransomware]
- **Publication date:** 14 October 2026
- **Domains:** `azoza.co.za`; former domain `europassistance.co.za`
- **Actor / Group:** The Gentlemen
- **Sector:** Assistance and insurance-benefit administration
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim description:** AZOZA is associated with the former South African Europ Assistance activity and provides assistance and benefit-management services.
- **Analysis:** The former Europ Assistance South Africa identity appeared on a leak site associated with The Gentlemen. No sample was analysed; intrusion, exfiltration, encryption and impact are unconfirmed.

### October 15, 2026

#### 🇪🇬 Egypt - Luxor Company for Drinking Water and Sanitation [Ransomware]
- **Publication date:** 15 October 2026
- **Domain:** `lcww.com.eg`
- **Actor / Group:** LockBit 5.0
- **Sector:** Water supply and sanitation
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 4 (potential)
- **Victim description:** Luxor Company for Drinking Water and Sanitation is an Egyptian provider responsible for drinking-water and sanitation services.
- **Analysis:** The victim was published on a source attributed to LockBit 5.0. No sample, volume or official statement was examined. The publication is not documented as a compromise, exfiltration, encryption or impact to water services.

### October 18, 2026

#### 🇷🇼 Rwanda - Ministry of Health [Data Leak]

- **Initial publication date:** October 18, 2026 at 22:07 (displayed timestamp; timezone not specified)
- **Actor / Group:** Lenken (displayed account; identity and affiliation unverified)
- **Sector:** Public health / Government administration
- **Associated website:** [moh.gov.rw](https://moh.gov.rw/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Forum publication and associated local CSV corpus
- **Public sources:** [Government of Rwanda - Ministry of Health](https://www.gov.rw/government/institutions/ministries) | [Ministry of Health Rwanda](https://moh.gov.rw/about/overview)

- **Victim Description:** Rwanda's Ministry of Health is a government institution responsible for health-sector policy and coordination in Rwanda. The post attributed to the Lenken account presents a database as leaked and available for download. The ministry is identified as an official institution by the Government of Rwanda portal.

- **In-depth corpus analysis:**

  **Observed:** The publication claims **5.7 GB compressed** and **375 tables**. The associated local corpus contains **375 CSV files** totalling **6,050,914,271 bytes** and **42,509,228 physical lines including headers**. This total is a newline inventory: some fields contain embedded line breaks, so the physical-line count must not be interpreted as a count of people or logical records. For example, `userinfo.csv` contains **9,776 physical lines** but **9,509 parsed CSV records** with no malformed rows. The agreement between the table count, claimed volume and local corpus is a significant structural corroboration element. The archive advertised by the post was not retrieved directly; exact cryptographic identity between the advertised archive and the local corpus is therefore not specified in the sources consulted.

  **Main observed elements:**

  - `userinfo.csv` contains **9,509 user accounts**; **9,106** rows have a populated password field, **27** have a populated `secret` field and **8,072** contain an email address;
  - `api_token.csv` contains **40 entries**; `userkeyjsonvalue.csv` contains **23,812 records** related to user-key values;
  - identity data also includes phone numbers, birth dates, nationalities, employers, education, last-login information and account status fields;
  - `trackedentityattributevalueaudit.csv` contains **4,503,344 audit rows** and `datavalueaudit.csv` contains **3,211,053 audit rows**;
  - `trackedentityprogramowner.csv` contains **10,202,305 relationships** between tracked entities and programmes;
  - `programmessage.csv` contains **4,452,109 messages**; message and channel tables indicate substantial notification and communication capability;
  - event and analytics exports contain structures compatible with health, facility, programme and measurement data;
  - analysed fields and values contain markers relating to patients, health, diseases, vaccination, facilities, administrative units, audits and accounts;
  - **33 CSV files are empty** and no null byte was detected during the global corpus scan.

  Content indicators were calculated across all files through sequential read-only scanning: approximately **4.6 million lines** contain health markers, **218,336** contain identity markers, **46,427** contain audit markers, **38,816** contain financial markers and **796,202** contain administrative markers. These are aggregate presence indicators and do not represent unique individuals or unique medical records.

  Observed password fields are populated with hashed values in the visible records; no cracking, authentication or reuse attempt was performed. Secrets, tokens, contact details, identifiers and health records were not reproduced.

  **Assumption:** The consistency between the post, table count, claimed volume and local structures makes association of the corpus with the ministry's information system or an affiliated health service plausible. The observed table names and relationships are compatible with a health-data management platform. This compatibility alone does not document initial access, exfiltration by Lenken, corpus completeness or the absence of a provider.

  **Information not specified in the sources:** Initial access vector, technical access timeline, real actor identity, accounts actually used, data completeness, presence of complete medical records, operational impact and any official confirmation by the ministry. The sources do not specify whether hashes, secrets or tokens in the copy remain valid.

- **Analysis scope and limitations:** All **375 files** were read sequentially and read-only for inventory, physical-line counting and aggregate content-marker scanning. The highest-impact tables received detailed CSV parsing with physical-line and logical-record counts kept separate. Text indicators are triage signals rather than semantic classification of every cell. No file was executed, no download link was followed and no secret, hash, token or individual record is published. This analysis is not official confirmation of the incident.
- **Risk assessment:** Potential exposure of administrative accounts, identity data, health data, audit histories and notification mechanisms could facilitate fraud, targeted phishing, account impersonation, extortion, targeting of health personnel and violations of patient confidentiality. Level 4 reflects the combination of a government health victim, potentially sensitive data and access-related elements; actual operational disruption is not specified in the sources consulted.
- **SOC/CTI recommendations:** Revoke and rotate potentially exposed tokens, secrets and sessions; enforce password rotation and MFA; search for bulk exports, unusual administrative access and outbound transfers; verify backup and configuration integrity; audit roles and privileges; preserve logs; rapidly assess affected health-data categories; coordinate response with the competent Rwandan authority; do not download or redistribute the public archive.
- **Counting decision:** The incident is added to the October corpus and counted as a **new October incident**, subject to monthly closure and final statistical validation.
- **Local manifest:** `/tmp/afrintel-evidence/afr-2026-10-rwanda-moh/evidence_manifest.json`; raw data remains outside the repository.

#### 🇪🇬 Egypt - WE Academy / Telecom Egypt [Data Leak]
- **Publication date:** 18 October 2026
- **Domain:** `te.eg`
- **Actor / Group:** N0n
- **Sector:** Vocational training / Telecommunications
- **Status:** Claim - Unverified
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim description:** WE Academy is a training entity associated with Telecom Egypt, an Egyptian telecommunications operator.
- **Analysis:** The actor claims learner records, training material, projects, exams and a training database. No sample was analysed. The institutional link is plausible, but no access to the telecom core network or billing systems is established.

### October 20, 2026

#### 🇲🇿 Mozambique - Procuradoria-Geral da República (PGR) [Data Leak]

- **Initial publication date:** 20 October 2026 at 04:29 (displayed timestamp; timezone not specified)
- **Actor / Group:** Kazu (displayed account; identity and affiliation unverified)
- **Sector:** Public administration / Justice and public prosecution
- **Website:** [pgr.gov.mz](https://www.pgr.gov.mz/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Claimed effect:** Alleged exposure and sale of a backup of the public justice system
- **Claimed volume:** 22 GB and 158,511 files; figures unverified
- **Claimed price:** Make an offer
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Underground forum post and local samples provided to AFRINTEL

- **Victim description:** The Procuradoria-Geral da República (PGR) is Mozambique's public prosecution service. It performs functions relating to legality, prosecution of offences and the administration of justice. The official PGR portal publishes institutional, legal, administrative and judicial information.

- **Analysis:**

  **Observed:** A post attributed to the **Kazu** account, timestamped **20 October 2026 at 04:29** according to the displayed time, offers for sale a “Public Justice System” associated with PGR Mozambique and the `pgr.gov.mz` domain. The author claims **22 GB** and **158,511 files**. The local corpus provided contains **262 files** totalling **75,941,802 bytes**: **180 JSON**, **71 PDFs**, **9 EML email files**, one DOC file and one JPG image.

  The 180 JSON files are readable and all present an object structure containing **22 keys**; individual values are not published. The 71 PDFs were checked read-only and total **117 pages**. Each of the 9 EML messages contains sender, recipient, date and subject metadata. The combination of structured data, PDF documents and email messages is compatible with an administrative or judicial document environment backup. These 262 files do not validate the claimed 22 GB volume or 158,511-file total.

  **Assumption:** The consistency between the PGR name, the Mozambican official domain, institutional identity and corpus structure makes attribution to the PGR scope plausible. The file categories are compatible with administrative, legal or public-prosecution records. This consistency does not document that the actor compromised PGR infrastructure or that the sample represents the entire system.

  **Unknown:** The access vector, affected systems, technical access timeline, technical origin of the files, number of cases and unique people, duplicates, completeness, exact legal sensitivity of the documents, operational impact and any official confirmation remain unknown.

- **Analysis scope and limitations:** All 262 files were inventoried read-only. JSON, PDF and EML files received structural checks; no individual document, message, name, address or procedural element is reproduced. No script, criminal link or remote content was executed or followed. The analysis confirms the composition of the supplied sample, not initial access, complete exfiltration or official victim confirmation.
- **Risks:** Exposure of judicial or administrative records, privacy violations affecting people involved in proceedings, targeted phishing, document fraud, intimidation of witnesses or personnel and exploitation of sensitive justice-administration information.
- **SOC / CTI recommendations:** Preserve portal, document-system, email and administrative-account logs; search for bulk exports and unusual downloads; review access to judicial files; revoke potentially exposed sessions and secrets; verify backup integrity; coordinate response with competent Mozambican authorities; do not download or redistribute additional data.
- **AFRINTEL assessment:** Publication observed; local sample provided and analysed; PGR attribution plausible; document structure consistent; overall volume and completeness unverified; unauthorised access and exfiltration unconfirmed; official confirmation not observed.

#### 🇲🇬 Madagascar - `staging.sso.gov.mg` (claimed attribution)

- **Initial publication date:** 20 October 2026 at 05:14 (displayed timestamp; timezone not specified)
- **Exchange start date:** Monday, 19 October 2026, according to the supplied chronology; time not specified
- **Actor / Group:** List1 (account displayed in the post; identity and affiliation unverified)
- **Sector:** Government / Digital identity and authentication
- **Claimed web service:** `staging.sso.gov.mg`
- **Status:** Claim - Unverified
- **Incident type:** Access Sale
- **Confidence level:** Medium
- **Impact level:** Level 4 (potential)
- **Source type:** Underground forum, direct exchanges and supplied material provided to AFRINTEL

- **Victim Description:** `staging.sso.gov.mg` is presented as a staging environment linked to a Malagasy digital-identity service. Its exact operational relationship with the relevant administration has not been independently established.
- **Analysis:** The post displayed on **20 October 2026 at 05:14** announces the sale of “admin access” to `staging.sso.gov.mg`. The supplied exchanges state an advertised price of **USD 450** and an assertion of administrative access. The material shows a Keycloak-like interface with several realms and a partially masked user list. No username, password or secret is reproduced; no access was tested. During the same exchange, the seller separately offered access to `e-koragna.gov.mg`, which is treated in a separate record.
- **Analytical assessment:** The Malagasy domain, presented interface and consistency between the post and supplied material support an apparent access offer targeting an administrative environment. Whether the access is real, unauthorised, valid or within the seller’s control remains undetermined.
- **Unknown:** Acquisition method, technical timeline, privilege scope, persistence, possible data exposure, transaction and confirmation by the service owner or an authority.
- **Analysis scope and limitations:** Analysis based on the post, supplied exchanges and material; systems, accounts and credentials were not tested. Personal data and session identifiers remain outside the repository.
- **Risk assessment:** If valid, an administrator account could allow modification of realms, clients, roles or accounts and facilitate takeover of dependent services.
- **Counting decision:** Counted as one distinct `Access Sale` covering only `staging.sso.gov.mg`.
- **Sources / Evidence:** Forum post supplied on 23 October 2026 and timestamped 20 October 2026; exchanges and Keycloak-related material supplied to AFRINTEL. Contact details, session identifiers, secrets and personal data are not published.

#### 🇲🇬 Madagascar - `e-koragna.gov.mg` (claimed attribution)

- **Initial publication date:** 20 October 2026 at 05:14; separate offer visible in the later exchange at 14:08 (displayed timestamps; timezones not specified)
- **Actor / Group:** List1 (account displayed in the post; identity and affiliation unverified)
- **Sector:** Government / Digital identity and public services
- **Claimed web service:** `e-koragna.gov.mg`
- **Status:** Claim - Unverified
- **Incident type:** Access Sale
- **Confidence level:** Medium
- **Impact level:** Level 4 (potential)
- **Source type:** Direct exchange associated with a forum post and supplied material provided to AFRINTEL

- **Victim Description:** **e-Koragna** is a complaints-management platform linked to Madagascar’s PRODIGY digital-governance and identity-management project. Public information associates it with the **Digital Governance Unit (UGD)** ([public e-Koragna description](https://torolalana.gov.mg/fr/services/e-koragna-mecanisme-de-gestion-de-plaintes/) ; [UGD website](https://digital.gov.mg/)).
- **Analysis:** After advertising administrator access to `staging.sso.gov.mg`, the seller offered `e-koragna.gov.mg` as an additional access during the supplied exchange. The advertised offer price was **USD 450**. The associated material shows a Keycloak-like interface; no username, password or secret is reproduced and no access was tested.
- **Analytical assessment:** Public links between e-Koragna, UGD and PRODIGY, the Malagasy domain and the exchange support an apparent access offer targeting this service. Whether the access is real, unauthorised, valid or within the seller’s control remains undetermined.
- **Unknown:** Acquisition method, technical timeline, privilege scope, persistence, possible data exposure, transaction and confirmation by the service owner or an authority.
- **Analysis scope and limitations:** Analysis based on the post, supplied exchange and material; systems, accounts and credentials were not tested. Personal data and session identifiers remain outside the repository.
- **Risk assessment:** If valid, the access could allow modification of accounts, roles or service settings and facilitate takeover of dependent functions.
- **Counting decision:** Counted as one distinct `Access Sale` covering only `e-koragna.gov.mg`.
- **Sources / Evidence:** Forum post supplied on 23 October 2026, associated exchanges and Keycloak-related material supplied to AFRINTEL. Contact details, session identifiers, secrets and personal data are not published.

#### 🇨🇩 Democratic Republic of the Congo - MINESURSI Teacher Registration Platform [Data Leak]

- **Initial publication date:** 20 October 2026 at 06:27 (displayed timestamp; timezone not specified)
- **Actor / Group:** Kazu (displayed account; identity and affiliation unverified)
- **Sector:** Public administration / Higher education / Scientific research
- **Associated website:** [minesursi.gouv.cd](https://minesursi.gouv.cd/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Claimed effect:** Alleged exposure and sale of a corpus associated with a teacher-registration platform
- **Claimed volume:** 136 GB and 125,823 files; figures unverified
- **Claimed price:** Make an offer
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Underground forum post and sample archive provided to AFRINTEL

- **Victim description:** MINESURSI is the Congolese ministry responsible for higher and university education, scientific research and innovations. The domain associated with the publication corresponds to the ministry's institutional domain. Public services associated with the domain include digital platforms for higher-education institutions, students and personnel.

- **Analysis:**

  **Observed:** A post attributed to the **Kazu** account, dated **20 October 2026 at 06:27** according to the displayed timestamp, offers for sale a corpus presented as originating from a MINESURSI “Teacher Registration Platform”. The post claims **136 GB**, **125,823 files** and a **2026** dump date. It associates the corpus with `minesursi.gouv.cd` and describes a registration and login platform for identifying and managing information about higher-education teachers.

  The local archive provided to AFRINTEL was checked read-only. It has SHA-256 `f70f1365d67d65d7b9f17cc14b3f19ed3f92b134ea1a6dd35ad3135c29d5cf46`, a compressed size of **1,558,803,176 bytes** and an extracted size of **1,610,225,124 bytes**. It contains **1,531 files**: **581 PDFs**, **777 JPG**, **136 JPEG** and **37 PNG** files. The **581 PDFs** were processed with `pdfinfo`; no encrypted document was detected and they total **938 pages**. No executable file matching the checked extensions was observed.

  Filename analysis identified document markers compatible with administrative and academic files: **187** passport references, **61** dossier references, **46** certificate references, **44** appointment references and **20** diploma references. Text extraction returned content from **57 documents**. Within those documents, markers relating to teaching appeared in **13**, higher education or universities in **14**, birth or personal data in **15**, diplomas or certificates in **7**, and employment, appointments or personnel numbers in **7**. These counts are content indicators, not counts of people or proof of completeness.

  **Analytical assessment:** The consistency between the ministry, its institutional domain, the platform theme, filenames and document categories makes attribution of the corpus to the MINESURSI scope plausible. The presence of administrative files, identity documents, diplomas and career-related documents is compatible with a teacher-registration platform. The sources consulted do not specify whether the actor compromised ministry infrastructure or whether the archive represents the full advertised dump.

  **Unknown:** The access vector, systems actually affected, technical access timeline, technical origin of the files, number of unique people, duplicates, corpus completeness, exact nature of non-text content, presence of valid credentials or sessions, operational impact and any official confirmation remain unknown. The claimed 136 GB and 125,823-file totals are not validated by the sample.

- **Analysis scope and limitations:** The supplied archive was inventoried in full, and its PDFs received structural checks and aggregate text extraction. Images and document pages were not transcribed or published. The analysis establishes the existence and composition of the supplied artefact but does not confirm its system origin, acquisition date, initial access, exfiltration or official victim confirmation. Raw data remains outside the repository.
- **Risks:** Teacher identity theft, document fraud, targeted phishing, administrative fraud, privacy violations affecting personnel and exploitation of career documents or supporting identity records.
- **SOC / CTI recommendations:** Preserve platform and administrative-account logs; search for bulk exports, abnormal downloads and access from new devices; reset potentially exposed sessions and secrets; review access controls for teacher files and supporting documents; monitor phishing targeting institutions and teachers; coordinate response with the competent Congolese authority; do not download or redistribute additional data.
- **AFRINTEL assessment:** Publication observed; sample archive provided and analysed; MINESURSI attribution plausible; document structure and categories consistent; overall volume and completeness unverified; unauthorised access and exfiltration unconfirmed; official confirmation not observed.

### October 21, 2026

#### 🇬🇦 Gabon - Gabon Meca (`gabonmeca.com`)

- **Initial publication date:** 21 October 2026
- **AFRINTEL observation date:** 23 October 2026
- **Actor / Group:** HYFLOCK
- **Sector:** Retail and distribution / IT and office equipment
- **Website:** [gabonmeca.com](https://gabonmeca.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Claimed effect:** Potential data exfiltration and disclosure
- **Confidence level:** Low
- **Impact level:** Level 2
- **Source type:** HYFLOCK disclosure site and supplied material

- **Victim Description:** **Gabon Meca** is a Gabonese company specialising in the distribution of school and office supplies, furniture, IT hardware, printing equipment and office solutions. A post associated with the `gabonmeca.com` domain presents it as a HYFLOCK victim.

- **Claimed data:** The exact nature of the allegedly obtained data is not specified in the available public material. A secondary monitoring system reports a volume of **60 GB**; this figure has not been corroborated by a sample, technical publication or victim statement.

- **Analysis:**

  **Observed:** The supplied material, originating from the HYFLOCK disclosure site, shows an entry titled `gabonmeca.com leak incident` associated with HYFLOCK, Gabon and the `gabonmeca.com` domain. The page shows a disclosure countdown still pending at collection time, together with a description of Gabon Meca and a public LinkedIn page for the company. No data sample was accessible or analysed by AFRINTEL.

  **Assumption:** The correspondence between the published domain and Gabon Meca’s public business activity makes the victim identification plausible. The post may be consistent with an extortion attempt based on an alleged compromise and data exfiltration, but it does not by itself demonstrate access, extraction or encryption.

  **Unknown:** Initial access vector, affected systems, compromise period, presence of encryption, data nature, volume actually extracted, operational impact, any negotiation or payment, and public confirmation by Gabon Meca all remain unknown.

- **Analysis scope and limitations:** No sample, download link or file was opened or analysed. The 60 GB volume remains a secondary claim and must not be presented as a confirmed measurement.
- **Risk assessment:** Potential risks include exposure of customer, employee or supplier information, supplier fraud, targeted phishing, exploitation of commercial information and disruption of business activity if encryption is later demonstrated.
- **SOC/CTI recommendations:** Preserve VPN, IAM, EDR, firewall, email and business-application logs; search for unusual administrative connections, archive creation, bulk exports and outbound transfers; review new authentication devices and countries; revoke suspicious sessions; audit access to business systems and customer databases; verify backup integrity; monitor lookalike domains and phishing campaigns; do not download any data potentially published by the actor.
- **MITRE ATT&CK detection hypotheses:** `T1078 Valid Accounts`, `T1110 Brute Force`, `T1560 Archive Collected Data`, `T1041 Exfiltration Over C2 Channel`, `T1021 Remote Services` and `T1486 Data Encrypted for Impact` are general detection hypotheses; none is established as executed in this incident.
- **AFRINTEL assessment:** Leak-site publication observed; victim identification plausible; sample not observed or analysed; unauthorised access, exfiltration, encryption and service disruption unconfirmed; attribution to HYFLOCK based on the published claim.
- **Sources / Evidence:** Material originating from the HYFLOCK site and supplied on 23 October 2026; [Gabon Meca public website](https://gabonmeca.com/). No direct link to a criminal resource, personal data or sample is published.

<!-- afrintel:ransomware-lifecycle
listing_status: observed
listing_first_observed_at:
listing_last_observed_at:
sample_status: none-observed
deadline_at:
deadline_status: unknown
disclosure_status: not-observed
victim_confirmation: none-observed
negotiation_status: unknown
ransom_payment_status: unknown
resale_status: unknown
last_checked_at: 2026-10-23
-->

### October 23, 2026

#### 🇿🇦 South Africa - Rand Mutual Assurance: Workers' Compensation Services
- **Date RMA received the alert and public claim:** 23 October 2026
- **Actor / Group:** Unattributed
- **Sector:** Insurance / Workers' compensation
- **Website:** [randmutual.co.za](https://www.randmutual.co.za/)
- **Status:** Under Investigation
- **Incident type:** System Intrusion
- **Confidence level:** Medium for the existence of the alert and investigation; Low for effective access, exfiltration and claimed volumes
- **Impact level:** Level 4 (high-sensitivity insurance and workers' compensation dataset; overall claimed volume not specified in the sources consulted by the sample)
- **Deadline:** 5 November 2026; timezone not specified
- **Claimed ransom:** USD 95,000
- **Claimed volume:** 366 GB; 1,683,810 claim-information records and 593,786 files
- **Description:** Rand Mutual Assurance (RMA) is a South African insurance organisation providing workers' compensation and related insurance services, particularly for mining, metals, steel and associated industries.
- **Analysis:** RMA confirmed receiving a security alert on 23 October 2026 and opening a specialist investigation. The company has not documented in the public sources that information was accessed, acquired or disclosed without authorisation. The public claim attributes 366 GB, 1,683,810 claim records and 593,786 files to an unidentified actor; these figures remain unverified and do not necessarily represent the same number of people. A read-only analysis of the locally supplied `Samples.zip` archive (SHA-256 `46e45f8a368a626d57fe6dbe932257bdbfc6f57dfe6c8ba65c4a9a8d5c45bbe4`) covered all 262 supplied files: 180 JSON files, 71 PDFs, 9 EML messages, 1 DOC document and 1 JPG image, totalling approximately 75,941,802 uncompressed bytes. The sample's consistency with RMA's business environment supports contextual attribution, but does not by itself prove access or the alleged extraction.

  The 180 JSON files follow a homogeneous claims-event schema and contain 192 embedded person events. They include claim references, employer information, incident details, earnings data, claims and medical-tracking structures. Observed event dates range from May 2023 to August 2026; observed advice dates extend to September 2026. The records contain 135 distinct company or site identifiers, 22 events with accident-detail structures, 19 with disease-detail structures and 1 event marked fatal. All 192 embedded events are marked as not deleted.

  The 71 PDFs represent 117 pages; 35 yielded extractable text and 36 did not in automated extraction. Among the text-bearing documents, multiple files explicitly contain `Rand Mutual Assurance`, `RMA`, `@randmutual.co.za` addresses, claim numbers and workers' compensation claim-management material. The 9 EML files also contain RMA claim subjects and references, including exchanges linked to the organisation's domain. The DOC file contains internal metadata referring to `RMA` and an RMA letterhead template.

  **Sample attribution conclusion:** the combination of a coherent application schema, claims references, repeated organisational markers across JSON, PDF, email and office-document artefacts, and use of the `randmutual.co.za` domain is consistent with a corpus originating from Rand Mutual Assurance's business environment. Contextual attribution of the supplied sample to RMA is therefore strongly supported. This conclusion does not confirm that the actor obtained the sample through unauthorised access to RMA, nor the technical access timeline, exfiltration, encryption, corpus completeness or claimed volumes.

  No raw personal data, address, claim number or individual document content is reproduced in the repository. The analysis was performed without executing files, following links or contacting the victim or actor.
- **Evidence limitations:** RMA confirms the alert and investigation, but not effective data access or extraction. The claim, ransom demand, deadline and volumes remain attributed to an unidentified actor. RMA's public media centre did not yet contain an investigation outcome at the last check.
- **SOC/CTI action:** Preserve IAM, VPN, EDR, claims-database, document-storage and outbound-gateway logs preceding 23 October; search for bulk access or exports; revoke suspicious sessions and secrets; monitor fraudulent changes to bank details linked to compensation payments.
- **Sources / Evidence:** [ITWeb](https://www.itweb.co.za/article/rand-mutual-probes-alleged-breach-of-168m-claims/G98YdqLGAgXMX2PD); [TechCentral](https://techcentral.co.za/rand-mutual-assurance-data-breach-claim/287621/); [RMA media centre](https://www.randmutual.co.za/media). RMA confirms the alert and investigation, not the complete compromise.

#### 🇪🇹 Ethiopia - Horn of Africa Regional Environment Centre and Network (HoA-REC&N) [Data Leak]
- **Publication date:** 23 October 2026
- **Domain:** `hoarec.org`
- **Actor / Group:** N0n
- **Sector:** Environment / Research / Regional cooperation
- **Status:** Claim - Unverified
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim description:** HoA-REC&N is an Ethiopian regional organisation active in environment, research and cooperation in East Africa.
- **Analysis:** The publication claims SAP Business One, accounting, partner, inventory and procurement data. No sample was examined. The organisation's identity is verified, but access, exfiltration and volumes remain actor claims.

#### 🇹🇳 Tunisia - PROTEX Confection [Data Leak]
- **Publication date:** 23 October 2026
- **Official website:** [sidt.ci](https://www.sidt.ci/)
- **Actor / Group:** N0n
- **Sector:** Textile industry / Garment manufacturing
- **Status:** Claim - Unverified
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim description:** PROTEX Confection is presented as a Tunisian textile and garment-manufacturing company.
- **Analysis:** The publication claims customer, supplier, article, inventory, quotation, invoice, delivery and production-pattern data. The exact legal entity, domain, data origin and volumes are not corroborated.

### October 24, 2026

#### 🇪🇬 Egypt - MODON Developments S.A.E [Ransomware]
- **Publication date:** 24 October 2026
- **Domain:** `modon-egypt.com`
- **Actor / Group:** KryBit
- **Sector:** Real estate
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim description:** MODON Developments S.A.E is an Egyptian real-estate and project-development company.
- **Analysis:** The victim appears on a source associated with KryBit. No data type, volume or public evidence of intrusion, exfiltration or encryption was established.

#### 🇿🇦 South Africa - Government Communication and Information System (GCIS) [System Intrusion]
- **Notification and public discovery date:** 30 October 2026
- **Official domain:** [gcis.gov.za](https://www.gcis.gov.za/)
- **Affected system:** [erecruitment.gcis.gov.za](http://erecruitment.gcis.gov.za/), a recruitment portal referenced by GCIS
- **Actor / Group:** Non identifié
- **Sector:** Public administration / Government communications
- **Status:** Incident Confirmed by Victim
- **Incident type:** System Intrusion
- **Confidence level:** High for the existence and compromise of the system; Medium for effective data exposure
- **Impact level:** Level 3 (potential)
- **Victim description:** The Government Communication and Information System (GCIS) is a South African public administration responsible for coordinating government communications and information services.
- **Analysis:** GCIS stated that its e-recruitment system was compromised after suspicious activity targeting its web systems was detected on 24 October 2026. The portal was isolated and the incident reported to the Information Regulator, the South African Police Service and the State Security Agency. Potentially affected information includes applicant identity numbers, telephone numbers and email addresses, but access to each data item and the scope of exposure remain under investigation. No ransomware, encryption, leak-site publication or service outage has been established.
- **Observed:** GCIS acknowledged compromise of the recruitment system; suspicious activity was detected on 24 October; system isolation and authority notifications were confirmed; personal-data exposure was described as potential.
- **Unknown:** Access vector, accounts used, queries and objects accessed or exported, number of affected applicants, volume, access duration, persistence and any misuse of the data remain unknown.
- **Risk assessment:** Applicants may face identity theft, phishing, fake interview invitations, fraudulent job offers and requests for identity documents.
- **SOC/CTI action:** Preserve WAF, web-server, database, IAM and EDR logs preceding 24 October; identify accounts, queries and accessed or exported objects; revoke affected sessions and application secrets; monitor impersonation campaigns targeting applicants.
- **Sources / Evidence:** [GCIS official vacancies page](https://www.gcis.gov.za/content/about-us/hr/vacancies), which references the recruitment portal; [ITWeb - GCIS warns of information breach](https://www.itweb.co.za/article/gcis-warns-of-information-breach/wbrpO7g2ea3vDLZn), published on 30 October 2026.

### October 25, 2026

#### 🇧🇯 Benin - YOD Ingénierie (`yodingenierie.com`) [Ransomware]
- **Initial publication date:** 25 October 2026 (displayed timestamp; time and timezone not indicated)
- **AFRINTEL discovery date:** 30 October 2026
- **Actor / Group:** Panzer (ransomware and data-extortion group; publication claim and affiliation unverified)
- **Displayed deadline:** Around 15 November 2026, based on the 12 days remaining stated by the actor on 3 November 2026; the exact time is not specified
- **Deadline:** Ongoing on 3 November 2026; the actor states that negotiations failed and that no ransom was paid; no disclosure was observed in the material reviewed
- **Sector:** Engineering / Information technology / Digital transformation
- **Official website:** [yodingenierie.com](https://yodingenierie.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Medium for the existence of the publication and company identification; Low to Medium for technical attribution of the data
- **Impact level:** Level 4 (potential)
- **Source type:** Ransomware leak-site publication and local file inventory examined read-only
- **Victim description:** YOD Ingénierie is a Beninese engineering and information-technology company and a member of the NED&CO Group. It works in digital transformation, information-systems governance and artificial-intelligence-related projects.
- **Analysis:** The publication attributed to the Panzer ransomware group claims a **48 GB** corpus in an extortion context, containing identity documents, passport scans, KYC forms, bank documents, signatures, payslips, personnel records, contracts, invoices, budgets, audits, donor lists, internal correspondence and project-planning documents. No system encryption is demonstrated by the available material.

  The supplied directory contains only a tree inventory of **15,878 lines**. File names indicate several categories consistent with the published description, including administrative documents, personnel records, KYC material, financial items, contracts, budgets and project documents. No source files were available for examination; the claimed **48 GB** and the exact content have therefore not been validated.

  **Observed:** The company is linked to Benin through its official website; the publication displays YOD Ingénierie, a claimed 48 GB volume, a 25 October 2026 date and the Panzer group. Public CTI sources describe Panzer as a ransomware and data-extortion group. On 3 November 2026, the actor stated that 12 days remained and said that negotiations had failed without a ransom payment. The local inventory confirms numerous documentary references consistent with the announced categories, without making their content readable.

  **Assumption:** If authentic, the claim could involve personal, financial, HR, contractual and operational data belonging to YOD Ingénierie and its partners. References to documents from other African countries may reflect the group's regional activity, but are not sufficient to attribute all data to Benin.

  **Unknown:** Access vector, extraction date, file authenticity, corpus completeness, number of affected people or organisations, availability of a genuine downloadable sample, current validity of the documents, outcome of the deadline, whether the actor's non-payment statement is accurate and any confirmation by YOD Ingénierie remain unknown.
- **Analysis scope and limitations:** Structural and preliminary analysis based on the publication, public company information and the local inventory. Document contents could not be examined; no raw personal data, identity document, secret or download link is reproduced in the repository.
- **Risk assessment:** If authentic, potential risks include identity theft, document and financial fraud, targeted phishing, loss of employee and partner confidentiality, and exposure of contractual and operational information.
- **Sources / Evidence:** Publication attributed to Panzer observed on 30 October 2026; supplied publication image and actor statement concerning the failed negotiation, 12 days remaining and alleged absence of payment; local `yodingenierie-tree.txt` inventory; [YOD Ingénierie official website](https://yodingenierie.com/); [public Panzer CTI profile](https://secureresearch.com/threat-actors/panzer.html). Potentially sensitive files remain outside the repository.

### October 26, 2026

#### 🇿🇦 South Africa - Lydenburg Toyota [Ransomware]
- **Publication date:** 26 October 2026
- **Domain:** `lydenburg.toyota.co.za`
- **Actor / Group:** The Gentlemen
- **Sector:** Automotive / Dealership and after-sales
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim description:** Lydenburg Toyota is a South African automotive dealership providing sales and after-sales services.
- **Analysis:** The criminal publication and dealership identity are corroborated. No data type or volume was established; intrusion, exfiltration and encryption have not been confirmed by Toyota or the dealership.

### October 28, 2026

#### 🇳🇬 Nigeria - InvestNaija / Chapel Hill Denham [System Intrusion]
- **Public notification date:** 28 October 2026
- **Official domains:** [investnaija.com](https://investnaija.com/); [chapelhilldenham.com](https://chapelhilldenham.com/)
- **Actor / Group:** Non identifié
- **Sector:** Financial services / Investment management
- **Status:** Incident Confirmed by Victim
- **Incident type:** System Intrusion
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim description:** InvestNaija and Chapel Hill Denham are Nigerian entities associated with financial services and investment management.
- **Analysis:** Chapel Hill Denham notified InvestNaija customers of unusual activity suggesting that some customer information may have been accessed without authorisation. The company took containment measures and reported the incident to the relevant authorities. Less than 1% of customer information may be involved; investments were reportedly unaffected according to the notice. Email addresses and other contact details may have been obtained, but effective access, record count and scope remain under investigation. No ransomware, encryption or service outage has been established.
- **Potentially affected data:** email addresses and other contact details; number of people and byte volume not specified in the sources consulted.
- **SOC/CTI action:** Preserve WAF, API, IAM, mobile-application and web-channel logs preceding 28 October; identify the source of the unusual activity and accessed accounts or objects; revoke affected sessions and tokens; monitor phishing and unusual financial requests targeting customers.
- **Sources / Evidence:** [The Sun Nigeria](https://thesun.ng/chapel-hill-denham-alerts-customers-to-potential-data-breach-says-investments-safe/); [InvestNaija](https://investnaija.com/); [Chapel Hill Denham](https://chapelhilldenham.com/).

#### 🇸🇱 Sierra Leone - GIO Dental (`giodentalsl.com`) [Ransomware]
- **Initial publication date:** 28 October 2026
- **Domain:** [giodentalsl.com](https://www.giodentalsl.com/)
- **Actor / Group:** The Gentlemen
- **Sector:** Healthcare / Dental services
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3 (potential)
- **Victim description:** GIO Dental is presented as a dental clinic and laboratory operating in Freetown and Koidu, Sierra Leone. The founder is described as Nigerian, but the operational victim is located in Sierra Leone.
- **Analysis:** GIO Dental appears in a claim associated with The Gentlemen. OSINT sources place it in Sierra Leone, but no sample, volume, proof of encryption, exfiltration or statement from the clinic was identified.
- **Risk assessment:** If authentic, a claim could concern patient records, administrative data and laboratory systems. None of these elements is established.
- **Sources / Evidence:** [CTIWatch](https://ctiwatch.com/victims/gio-dental-924d6f76); [The Gentlemen victim list](https://ctiwatch.com/threats/thegentlemen/victims); [GIO Dental website](https://www.giodentalsl.com/). The tracking sources specify that this is an publication attributed to the actor.

### October 29, 2026

#### 🇪🇬 Egypt - BlueBus (`bluebus.com.eg`) [Data Leak]
- **Initial publication date:** 29 October 2026 at 06:02 (displayed timestamp; timezone not specified)
- **Actor / Group:** Lenken (displayed account; identity and affiliation unverified)
- **Sector:** Transport / Mobility / Ticketing
- **Associated website:** [bluebus.com.eg](https://bluebus.com.eg/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High for the existence and analysis of the published sample; Medium for technical attribution to BlueBus
- **Impact level:** Level 4
- **Source type:** Forum publication and local samples examined read-only
- **Victim description:** BlueBus is an Egyptian bus transportation booking and ticketing service. The Lenken publication associates the `bluebus.com.eg` domain with orders and data relating to customers, tickets, payments and drivers.
- **Analysis:** The publication claims more than **300,000 orders**, **305,520 lines**, **651 drivers** and an order database covering 2026. These volumes are author claims and were not validated against the local files.

  AFRINTEL examined `sample.csv` in full, read-only: **2,999 rows**, **16 columns**, and **0 malformed rows**. The observed columns cover orders or tickets, statuses, prices, customer identifiers, contact details, birth dates, national identifiers, payment methods, transaction identifiers and ticket information. The sample contains **1,178 distinct customer identifiers**, **1,178 distinct phone numbers**, **350 distinct email addresses** and **358 rows containing a national identifier**. Name and phone fields are present on all 2,999 rows; last names and birth dates are populated on 228 rows. Status or code fields are populated on 1,541 rows, payment and ticket fields on 1,458 rows, and transaction identifiers on 218 rows.

  Observed statuses are `Paid` (947), `Expired` (415), `Cancelled` (135), `Pending` (26) and `Modified` (18). Observed payment methods include `StoreCash`, `Fawry`, `PartnerCredit`, `Cash`, `Card`, `StoreCard`, `Aman` and `AutoConfirmed`. The arithmetic sum of prices in the snapshot is approximately **1,189,773.62** in the unit shown by the file, but repeated orders and customers prevent interpreting it as a unique financial total or total exposed sales value.

  `drivers.txt` contains **9 JSONL objects**. They include nested user and driver information, stations, amounts and timestamps. The sample contains **9 driver identifiers**, **9 user identifiers** and **5 station identifiers**; observed timestamps range from **1 to 20 October 2026**. The structures also include contact information and sensitive driver identifiers; no individual value is reproduced in the repository. The presence of 9 local objects does not validate the claimed **651 drivers**.

  **Assumption:** The published domain, booking structure, order categories, station references and data organisation are compatible with a transport-ticketing platform associated with BlueBus. This consistency supports contextual attribution of the sample, but does not document the access vector, exfiltration by Lenken, the technical provenance of each record, corpus completeness or a BlueBus-confirmed compromise.

  **Unknown:** Access date, exact source system, number of unique persons in the full database, current validity of identifiers, existence of unauthorized access, geographic scope, completeness of the claimed **305,520 lines**, actual driver count and any official confirmation remain unknown.
- **Analysis scope and limitations:** Both local files were examined in full, read-only; file types, sizes, SHA-256 hashes, encoding, schema, missing values, duplicates, aggregates, statuses and time ranges were checked. The RAR archive was inspected without active extraction or execution. Personal values, identifiers, download links and secrets were not published, tested or followed.
- **Risk assessment:** If authentic, the sample could facilitate targeted phishing, ticket and payment fraud, customer or driver impersonation, misuse of national identifiers and mobility-data correlation. These are potential risks and do not confirm the incident.
- **Sources / Evidence:** Forum publication supplied on 30 October 2026; local `sample.csv` and `drivers.txt` examined read-only. The archive and source files remain outside the repository; no raw personal data is reproduced.

#### 🇪🇬 Egypt - Egyptian organisations, clinics, pharmacies, hospitals and doctors [Data Leak]
- **Initial publication date:** 29 October 2026 at 03:53 (displayed timestamp; timezone not specified)
- **Actor / Group:** Marx (displayed account; identity and affiliation unverified)
- **Sector:** Healthcare / Professional and organisation directory
- **Associated website:** Not specified in the publication
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High for the existence and analysis of the doctor file; Medium for attribution to the claimed Egyptian scope
- **Impact level:** Level 3
- **Source type:** Forum publication and local XLSX workbook examined read-only
- **Victim description:** The Marx publication presents a dataset relating to doctors, clinics, pharmacies, hospitals and healthcare organisations in Egypt. The available local file corresponds to the “Doctor File” component and appears to be a healthcare-professional directory; the “Organizations File” announced in the post was not available for analysis.
- **Analysis:** The publication claims a doctor file containing more than **33,000 lines** and an organisation file containing more than **48,000 lines**. AFRINTEL examined `Doctor.xlsx` in full, read-only; its structure contains **33,120 data rows**, **11 named columns** and one additional blank column. Observed columns cover a professional code, doctor name, type, specialty, class, an account-related field, organisation codes and names, activity status, mobile number and email address.

  The doctor field contains **28,138 distinct values** across 33,120 rows. The specialty field has **38 distinct values**, the class field **16**, the account-related field **9**, and the activity-status field **2**. A mobile number is populated on **5,746 rows**; no email value is populated in this workbook. Code and professional-identification fields are present across all rows. The organisation-code and organisation-name columns are empty in the local file, preventing identification of the specific healthcare structures associated with each professional.

  The correspondence between the local **33,120-row** workbook and the “+33K” claim supports the existence of a genuinely structured sample. The **+48K** organisation file was not supplied. The workbook structure is compatible with an Egyptian healthcare-professional directory; the sources consulted do not specify the source system, access vector, exfiltration by Marx, corpus completeness or confirmation by a healthcare organisation.

  **Assumption:** The post title, workbook nature and presence of doctor, specialty, account, mobile and activity-status fields make an association with the Egyptian healthcare ecosystem plausible. This consistency does not document that the data came from an official register or a specific healthcare organisation.

  **Unknown:** Victim organisation identity, technical workbook provenance, extraction date, number of unique persons in the full corpus, meaning of the account fields, current data validity, existence of unauthorised access, contents of the “Organizations File” and any official confirmation remain unknown.
- **Analysis scope and limitations:** `Doctor.xlsx` was examined in full, read-only, at the XLSX/XML level, including structure, rows, columns, empty fields and distinct-value counts. No organisation file was present in the local directory. No name, number, email address or other raw personal data is reproduced in the repository.
- **Risk assessment:** If authentic, the file could facilitate targeted phishing, doctor or organisation impersonation, appointment fraud and mapping of healthcare professionals. No patient record or clinical data was observed in the analysed file.
- **Sources / Evidence:** Forum publication supplied on 30 October 2026 and local `Doctor.xlsx` examined read-only. The file remains outside the repository; no raw personal data is published.

#### 🇪🇬 Egypt - Al Arabia United [System Intrusion]
- **Publication / public confirmation date:** 29 October 2026
- **Official domain:** [audegypt.com](https://audegypt.com/)
- **Location:** 26 July Corridor, Giza Governorate
- **Actor / Group:** Leakers$ (public claim; technical attribution unverified)
- **Sector:** Outdoor advertising / Digital-display infrastructure
- **Status:** Incident Confirmed by Victim
- **Incident type:** System Intrusion
- **Confidence level:** Very High
- **Impact level:** Level 2
- **Victim description:** Al Arabia United is an Egyptian company specialising in outdoor advertising and the operation of digital billboards.
- **Analysis:** On 29 October, a billboard operated by Al Arabia United on the 26 July Corridor in Giza displayed unauthorised explicit content. The company acknowledged unauthorised access to one of its screens, immediately disabled it and stated that it was cooperating with the authorities. Egypt's Ministry of Interior confirmed that an advertising company used an international company to distribute content electronically and that the international company's website had been compromised; the same content was then reportedly displayed simultaneously on screens in several countries.
- **Observed elements:** effective display of unauthorised content; acknowledgement of unauthorised access by Al Arabia United; preventive shutdown of the screen; official confirmation of the incident and reported simultaneous impact in several countries.
- **Claimed but not technically confirmed:** Leakers$ claims to have exploited a vulnerability in software used to transmit content to LED displays. No CVE, technical proof or identity of the compromised provider has been published; the exact initial-access method remains unknown.
- **Not established:** data exposure or exfiltration, system encryption, compromise of `audegypt.com`, compromise of Al Arabia United's wider network and persistence in the provider environment.
- **Risk assessment:** The incident demonstrates a risk of content hijacking and coordinated propagation when a centralised digital-display management platform is connected to multiple countries. No impact on data or on Al Arabia United's internal systems has been established.
- **Sources / Evidence:** [audegypt.com](https://audegypt.com/); [Egyptian Ministry of Interior](https://www.moi.gov.eg/news/GetDetails?newsId=bbfb00a8-b8e2-4c10-81bd-161ba437d035); [Al-Ahram Gate](https://gate.ahram.org.eg/News/5974509.aspx); [The Cairo Report](https://www.cairoreport.org/p/egypt-brazil-iraq-billboard-hack); [x.com/IntCyberDigest](https://x.com/IntCyberDigest/status/2116519809445675248).

### October 30, 2026

#### 🇨🇮 Ivory Coast - Société Ivoirienne de Télédiffusion [Ransomware]
- **Claim publication / public discovery date:** 30 October 2026; first indexing observed at approximately 17:26 UTC
- **Domain:** Not established
- **Actor / Group:** Qilin (claimed attribution only)
- **Displayed deadline:** approximately 4 November 2026 at 14:00, calculated from the 108-hour-and-17-minute countdown observed on 31 October 2026 at approximately 01:43; timezone not displayed
- **Deadline:** Ongoing at the time of observation; disclosure not observed
- **Sector:** Broadcasting / Audiovisual infrastructure
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3 (potential)
- **Victim description:** Société Ivoirienne de Télédiffusion (SIDT) is an Ivorian state-owned company established in 2017. It broadcasts radio and television programmes, including through TNT, and provides multiplexing, infrastructure and technical-support services.
- **Analysis:** The victim appears in a public tracking system associated with Qilin's leak site. The observed page displays a **108-hour-and-17-minute** countdown, with no data publication or claimed volume. The observed material is limited to the victim listing and displayed deadline; no technical material concerning access, exfiltration, encryption or disruption of broadcasting services was provided.
- **Observed:** Publication attributed to Qilin, victim identified as Société Ivoirienne de Télédiffusion, first indexed on 30 October 2026 at approximately 17:26 UTC; a 108-hour-and-17-minute countdown was displayed when observed on 31 October 2026 at approximately 01:43.
- **Unknown:** Domain, access vector, affected systems, technical access timeline, data nature, volume, encryption, service disruption, deadline outcome, victim confirmation and any statement from an Ivorian authority or CERT remain unknown.
- **Risk assessment:** If authentic, potential risks could involve broadcast continuity, audiovisual systems, administrative data and provider relationships. These risks remain potential.
- **Sources / Evidence:** Public indexing of a Qilin claim observed on 30 October 2026 and page status checked on 31 October 2026; [SIDT official website](https://www.sidt.ci/). No sample, direct criminal link or raw data is reproduced in the repository.
