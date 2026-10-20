![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in October 2026 (12 records)

👉🏾 [**French version available here**](./victims_FR.md)

## October 2026

**Monthly tracking status: In Progress / En cours**  -  provisional corpus of 12 records; monthly closure and statistics remain pending. The Yalidine case is documented but excluded from canonical statistics until its attribution is corroborated.

### 20 October 2026 - AFRINTEL discovery

#### 🇲🇦 Morocco - Eurogate Tanger (`eurogate-tanger.com`)

- **Incident date:** Not established
- **Initial publication date:** 12 October 2026 at 13:55:54 (displayed timestamp; timezone not specified)
- **Observed disclosure date:** 19 October 2026 at 13:27 UTC (announced first batch)
- **AFRINTEL discovery date:** 20 October 2026
- **Actor / Group:** N0n (name displayed by the source; identity and affiliation unverified)
- **Sector:** Maritime transport / container-terminal operations
- **Website:** `eurogate-tanger.com`
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4 (potential)
- **Source type:** Ransomware tracker and actor-published archive

- **Victim Description:** Eurogate Tanger is presented as a container-terminal operator in Morocco. The publication claims the removal of commercial correspondence, operational documents and internal working files from systems associated with `eurogate-tanger.com`.

- **Analysis:**

  **Observed:** The observed record identifies Eurogate Tanger, Morocco, the maritime-transport sector, the N0n group and a `NOT PAID – EXPOSED` statement. “Published data” is listed as `N/D`. The supplied local archive, `eurogate_tanger.com-leak.zip`, passed a read-only integrity test and contains **355 files**, **373,065,003 uncompressed bytes**, **373,150,373 archive bytes**, with no ZIP encryption. Files are grouped under `eurogate-tanger.com` and include DOCX, XLS/XLSX, PDF, MSG, PPTX, ODS, EDI, XML, log/trace, SQL, archive and technical files. The included README explicitly describes a **first publication batch** and announces possible additional batches.

  A read-only static analysis covered all **354 files extracted under the domain**: hashes, actual file types, structure and textual/XML content where extractable. It included **98 DOCX, 86 XLSX, 11 XLS, 5 PPTX, 2 ODS, 22 PDF, 10 MSG, 32 TRC files, 32 TRM files, 19 RAR, 5 ZIP, 1 JAR, 1 Java class, and EDI/XML/WSDL/SQL and log files**. XML analysis of the XLSX files represents approximately **652,708 row elements** and **13,686,923 cell elements**; these are structural indicators and do not directly represent unique people or operations.

  Text and XML content repeatedly contains references consistent with **EGT, Eurogate, Tanger, OPUS Terminal, terminal, port, containers, vessels, cargo, reefers, gates, cranes, yard, voyages, trucks and operational movements**. DOCX and XLSX files also contain references to release notes, hotfixes, SQL scripts, traces and technical exchanges associated with this environment. The RAR archives, ZIP archives and JAR were inventoried without execution; their members and sizes were checked.

  No file was executed. No VBA macro marker was detected in the inspected Office containers. PDFs and MSG files received static string and metadata analysis, without rendering or full interpretation of embedded objects. Email-address markers are present in several text-like files; no individual data is reproduced in this report.

  **Assumption:** The domain name in the archive tree, the organization name, the stated sector and the announced file categories are consistent with an exposure of Eurogate Tanger internal data. This supports archive-to-victim attribution, but does not prove the access method, initial compromise, data completeness or the absence of a provider or third-party environment.

  **Unknown:** The compromise date and vector, the total volume actually exfiltrated, N0n’s real identity and capabilities, completeness of the first batch, operational impact, any confirmation by Eurogate Tanger or an authority, and the exact content of the documents remain unknown.

- **Analyzed archive hash:** SHA-256 `87bb4495b774c21919af26daf9b3ab807e57f78d7fad5879d0176bd9df28c891`.
- **Analysis scope and limitations:** All 354 files extracted under the domain were covered by static analysis of actual type, hashes, structure and textual/XML content where extractable. This method does not decrypt protected files, visually render every page or validate every embedded object. It is not official confirmation of the incident. The archive remains outside the AFRINTEL repository.
- **Risk assessment:** Potential exposure of operational documents, vessel and container data, configurations or release notes, scripts and technical traces could facilitate social engineering, document fraud, employee targeting, preparation of port-operation disruption or identification of application dependencies. Level 4 reflects the potentially critical nature of this environment; actual disruption or access to control systems is not established.
- **Sources / Evidence:** public record observed on 20 October 2026; local archive supplied for analysis; no onion address, raw personal data or individual value is published.

#### 🇩🇿 Algeria - Yalidine El Djazair Service (`yalidine.com`) — attribution unconfirmed

- **Incident date:** Not established
- **Initial publication date:** 20 August 2026 at 05:27 (displayed timestamp; timezone not specified)
- **AFRINTEL discovery date:** 20 October 2026
- **Actor / Group:** TelephoneHooliganism (account displayed in the post; identity and affiliation unverified)
- **Claimed sector:** Transport / Logistics / Express Delivery
- **Claimed website:** [yalidine.com](https://www.yalidine.com/)
- **Status:** Under Investigation - Alleged
- **Incident type:** Data Leak
- **Confidence level:** Low
- **Impact level:** Level 3 (potential)
- **Source type:** Cybercriminal forum and CSV samples provided to AFRINTEL

- **Victim Description:** Yalidine El Djazair Service is an Algerian express-mail, parcel-delivery and domestic-logistics company that also provides e-commerce delivery and cash-on-delivery collection. The post associates the company with a database advertised as containing approximately **563,000 records**.

- **Analysis:**

  **Observed:** The 20 August 2026 post at 05:27, attributed to TelephoneHooliganism, presents `www.yalidine.com` as an Algerian database of **563,000 records**. It describes three datasets: contacts, booking history and support tickets. A moderator message displayed at 06:38 on the same day only restates the forum’s section rules; it does not confirm Yalidine, the files or a compromise.

  AFRINTEL examined three local CSV files read-only corresponding to those datasets: **50 contact rows**, **20 booking rows** and **20 ticket rows**. The files are structurally readable and total **90 tabular rows**, but that total does not represent 90 unique people. The files contain **34, 29 and 29 columns**, respectively. The fields cover contacts, CRM information, bookings, payments, support tickets and customer follow-up. No raw personal data is reproduced in this record.

  **Observed anomalies:** only **3 of 50 contacts** have `Algeria` as the country value; the remaining countries are predominantly foreign. The booking cities observed are not Algerian. The `contact_id` values used in bookings and tickets do not match the identifiers in the Contacts file. The 20 bookings contain only **2 distinct `booking_id` values**, and the 20 tickets contain only **2 distinct `ticket_id` values**. Links to booking records are also inconsistent. Ticket email and phone fields are empty, and several advertised contact fields are largely or entirely empty. Data-quality or encoding problems appear in some geographic values.

  Local SHA-256 hashes are: `Contacts_Algeria.csv` **fb87c90da9b74d186b3f5a3bbcef32ff63f177c908c48ad75b44b868e818da51**; `Booking_History_Algeria.csv` **964fe16260cd75f3994feb0dc9fe0393334ef37eb23e6a22851a6729b2244443**; `Support_Tickets_Algeria.csv` **49dc113a234b852ba97709a2dfc09ac26dae3b8af5397b543286885e3ac2218d**.

  **Assumption:** The domain name, Yalidine’s business activity and the three-table structure are compatible with the claim. That compatibility is weak: geographic, relational and completeness inconsistencies outweigh the elements linking the sample to Yalidine. The sample may be synthetic, misattributed, drawn from a multi-country environment, incomplete or built from a generic CRM template.

  A link with the **Afribaba** case from 20 August 2026 is possible only at campaign level: the displayed actor, publication date and broad data categories are similar. This could reflect a campaign targeting multiple Algerian organisations or reuse of a posting template. No shared identifier, domain, file or technical marker was observed; the link is therefore **not established** and must not merge the victims.

  **Unknown:** The files’ technical provenance, extraction date, authenticity, number of unique people, existence of unauthorised access, acquisition method, completeness of the advertised database, operational impact and any confirmation by Yalidine or an authority all remain unknown.

- **Analysis scope and limitations:** All three supplied CSV files were examined read-only, including structure, counts, blank fields, duplicates, inter-table relationships, date ranges and SHA-256 hashes. The files remain outside the repository. The analysis does not validate the claimed **563,000 records** and cannot attribute the sample to Yalidine.

- **Risk assessment:** If any part of the sample were authentic, the advertised categories could facilitate targeted phishing, social engineering, customer impersonation and order- or payment-related fraud. These are potential risks and do not establish actual exposure of Yalidine’s customers.

- **Counting decision:** The record is retained in the October corpus because the post was observed and a sample was supplied, but it is **excluded from the canonical total and statistical breakdowns** until attribution is corroborated.

- **Sources / Evidence:** publication screenshot and moderator-response screenshot supplied on 20 October 2026; three local CSV files examined read-only; [Yalidine official website](https://www.yalidine.com/). No onion link, criminal account, personal data or individual value is published.

### 09 October 2026

#### 🇲🇦 Morocco - National Press Council (CNP)

- **Incident date:** Not established
- **Initial publication date:** 9 October 2026 at 03:20 (displayed timestamp; timezone not specified)
- **AFRINTEL discovery date:** 9 October 2026
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

  **Assumption:** The institution’s name, displayed logo and cited data categories are consistent with CNP functions, including processes related to professional press cards. This consistency does not demonstrate that the data came from a CNP-operated system: a historical copy, provider, other source or misleading presentation remain possible.

  **Unknown:** Actual access to the advertised sample or database, file hashes and structure, their authenticity and currency, actual number of unique people affected, source system, acquisition method and date, exposure scope, operational impact, and confirmation by the CNP or an authority all remain unknown.

- **Analysis scope:** Preliminary analysis based on the supplied post; the advertised PDFs and database were not locally available or examined. This analysis cannot validate the claimed **39,000 records**, the documents’ authenticity or the existence of an intrusion.

- **Risk assessment:** If the advertised material is authentic, combining contact details, identity documents, professional information and press-card data could expose journalists and other professionals to identity abuse, targeted phishing, social engineering, doxxing and document fraud. Potential exposure of people working in the press may also increase risks of targeting and harassment.

- **Recommendations:**
  1. Preserve logs from press-card management applications, submission portals, document systems, directories and administrative accounts.
  2. Investigate bulk exports, unusual file access, anomalous privileged access, provider accounts and outbound transfers.
  3. Assess through authorised means whether the published data categories correspond to CNP systems, without opening or downloading files offered by the author.
  4. Prepare protection and communication measures for potentially affected people once the actual scope is established.
  5. Strengthen detection of phishing, impersonation, document fraud and harassment targeting press-card holders or applicants.

- **Sources / Evidence:** forum post and screenshot supplied on 9 October 2026; [CNP duties and powers](https://cnp.press.ma/fr/2020/05/06/missions-et-pouvoirs-du-conseil-national-de-la-presse/). No download link, document, individual data or author contact is published.

### 02 October 2026

#### 🇲🇦 Morocco - Ministry of Investment, Convergence and Evaluation of Public Policies (MICEPP)

- **Incident date:** Not established
- **Initial publication date:** 2 October 2026 at 23:55 (displayed forum timestamp; timezone not specified)
- **AFRINTEL discovery date:** 9 October 2026
- **Actor / Group:** anisanas2 (displayed forum account; identity and affiliation unverified)
- **Sector:** Government / Administration / Investment and public-policy evaluation
- **Website:** [micepp.gov.ma](https://micepp.gov.ma/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Source type:** Underground Forum and Telegram posts provided to AFRINTEL

- **Victim Description:** The supplied material identifies MICEPP as Morocco’s Ministry of Investment, Convergence and Evaluation of Public Policies. Its precise institutional role and any potentially affected systems are not established by the observed publications.

- **Analysis:**

  **Observed:** A forum post attributed to the account **anisanas2**, timestamped **2 October 2026 at 23:55** according to the displayed time, advertises “sample documents” and a “database” associated with MICEPP. Supplied Telegram posts, dated **2 October** without a visible year or timezone, repeat this attribution. They claim that more than **150,000 folders** and more than **50,000 investors** are affected, that the corpus exceeds **400 GB**, and that it is offered for sale in parts. These volumes, the acquisition method and the existence of a compromise remain author claims. The posts display a **1.6 GB** file named `part_1_sample.rar` and a **26 KB** file named `investors_sample_300.csv`. Neither the archive nor the CSV was supplied locally or examined. The visible column categories describe identity and contact data, identity-document references, nationality, address, territorial administrative data, and company information, including the Common Enterprise Identifier (ICE). No individual content is reproduced.

  **Assumption:** The name, institutional logo and displayed data categories are consistent with administrative procedures or investment-related schemes. This consistency does not demonstrate that the files came from a system operated by MICEPP: a historical copy, provider, other administration, aggregator or misleading presentation remain possible.

  **Unknown:** Actual access to the advertised files, their hashes, structure, authenticity, currency, number of folders and unique people or organisations, source system, acquisition method and date, scope of any exposure, operational impact, and confirmation by MICEPP or an authority all remain unknown.

- **Analysis scope:** Preliminary analysis based on the publication and supplied screenshots; the advertised source files were not available. The visible material cannot validate the claimed volumes, confirm the technical attribution of the data or establish a compromise.

- **Risk assessment:** If the advertised data is authentic, combining identity, contact, administrative and company data could facilitate targeted phishing, identity abuse, document fraud, social engineering and fraud targeting investors or administrative procedures. The alleged presence of company identifiers and identity-document references warrants prioritised scoping, without assuming that the files are actually available.

- **Recommendations:**
  1. Preserve logs from portals, case-management systems, document repositories, integrations and administrative accounts that may process investment files.
  2. Investigate bulk exports, unusual privileged access, anomalous queries, provider accounts and outbound transfers around the period to be established through investigation.
  3. Verify through authorised means whether the observed field categories correspond to internal systems or providers, without downloading or handling files offered by the author.
  4. Assess the potential scope for affected investors, companies and staff before notification, then strengthen detection of targeted phishing and document fraud.
  5. Establish out-of-band verification for unusual requests involving investments, company details or administrative procedures.

- **Sources / Evidence:** forum and Telegram posts, plus screenshots supplied on 9 October 2026. No download link, individual data, identifier, secret or archive is published.

### 02 October 2026

#### 🇲🇦 Morocco - Ministry of National Territory Planning, Land Planning, Housing and City Policy

- **Incident date:** Not established
- **Initial publication date:** 2 October 2026 at 15:20 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 8 October 2026
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Government / Administration / Housing and urban planning
- **Website:** `matnuhpv.gov.ma` (domain displayed by the actor in the publication; connection to the affected system unconfirmed)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication provided to AFRINTEL

- **Victim Description:** The Moroccan ministry is responsible for public policies relating to national territory planning, urban planning, housing and city policy. Its institutional identity and remit are documented in an organisational decree published by the Moroccan administration.

- **Analysis:**

  **Observed:** A forum post attributed to the **Nameless511** account, timestamped **2 October 2026 at 15:20** according to the displayed time, offers for sale data attributed to the ministry. Its presentation page displays the `matnuhpv.gov.ma` domain. Its title mentions **26,452 candidate records**, while the body claims that more than **2,772 records** were compromised and describes **2,772 full candidate profiles** as the material held and offered for sale. These figures remain contradictory and unverified actor claims. The “Samples” section is distinct: the visible rows that follow are the sample supplied in the exchange. This sample is structured as recruitment-application lists, including third-grade technician and first-grade state-engineer competitions. Visible categories include identity, national identity number, date and place of birth, contact details, address, application status, diplomas, specialisations, degree-awarding institution, examination centre and supporting-document references. No individual value, application-document filename or identifier is reproduced in this record.

  **Assumption:** The institutional logo, the administration’s name, the displayed domain and the data schema are consistent with candidate or recruitment processes connected to the ministry. This consistency does not demonstrate compromise of `matnuhpv.gov.ma` or another ministerial system: a historical copy, contractor, data aggregator, third-party source or misleading presentation remain possible.

  **Unknown:** The source file, its hash, the actual number of rows and unique people, the records’ authenticity, currency and completeness, originating system, acquisition date and method, any unauthorised access, exfiltration, operational effect and official confirmation by the ministry or an authority all remain unknown.

- **Analysis scope:** Preliminary analysis based on the supplied publication and data visible in the sample provided after the “Samples” section; the original source file was unavailable. This sample cannot validate the claimed volumes, deduplicate affected individuals or establish the data’s technical provenance.

- **Risk assessment:** If authentic, the observed data categories could facilitate identity fraud, targeted phishing, document fraud, social engineering and abuse of recruitment processes. The alleged references to supporting documents could increase risk to candidates; they do not establish that the documents themselves are accessible.

- **Recommendations:**
  1. Preserve logs for application portals, recruitment tools, document repositories and relevant administrative accounts.
  2. Investigate bulk exports, anomalous queries, unusual privileged access and third-party access around the period to be established by the investigation.
  3. Use authorised means to determine whether the field schema and application references correspond to ministerial applications or service providers.
  4. Assess the potential population affected before any notification, and strengthen detection for phishing or fraud targeting applicants.
  5. Do not download the offer, contact the seller or test disclosed individual data.

- **Sources / Evidence:** forum publication and visible sample supplied on 8 October 2026; [Moroccan decree on the ministry’s remit and organisation](https://bdj.mmsp.gov.ma/Fr/Document/10596-D%C3%A9cret-n-2-23-751-du-7-joumada-II-1445-21-d%C3%A9cemb.aspx?KeyPath=594%2F681%2F697%2F10596). No forum link or personal data is published.

### 01 October 2026

#### 🇲🇦 Morocco - Midipcom

- **Incident date:** Not established
- **Initial publication date:** 1 October 2026 at 21:25 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 8 October 2026
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

### 05 October 2026

#### 🇲🇦 Morocco - Tera.ma / Sté Tera.ma SARL

- **Incident date:** Not established
- **Initial publication date:** 5 October 2026 at 19:41 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 8 October 2026
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Technology / IT equipment distribution and retail
- **Website:** `tera.ma` (domain displayed in the publication)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication provided to AFRINTEL + local corpus analysed read-only

- **Victim Description:** Tera.ma is presented in the publication as a Moroccan IT-equipment distribution and retail company located in Témara / Rabat. The corpus contains material consistent with sales, inventory, e-commerce, accounting and partner-management operations.

- **Analysis:**

  **Observed:** A post attributed to **Nameless511**, dated **5 October 2026 at 19:41** according to the displayed timestamp, announces a “final release” of an Odoo export associated with Tera.ma. The author claims that the corpus was extracted on **27 September 2025** and comprises **2.3 GB**, **282 CSV files**, **19,595 customers**, **69,197 orders**, **124,088 accounting entries** and **124 internal accounts**. The claimed extraction date and statements concerning negotiation remain actor assertions. The supplied local corpus contains **8,140 files** totalling **2,389,358,436 bytes**, including **282 CSV files** totalling **1,392,426,551 bytes**, **3,693 PDFs**, **3,152 JPEG/JFIF/JPG images**, **413 PNG images**, audio files and a video. Line counts, excluding headers, match the advertised figures for `account_move.csv` (**124,088**), `res_partner.csv` (**19,595**) and `sale_order.csv` (**69,197**). The CSV files contain roughly **21.7 million lines** in total, including headers.

  The reviewed structures cover accounting entries and invoices, orders, partners, inventory, stock movements, mail and application logs. The corpus also includes attachments presented as invoices, scans, contracts, delivery proofs and identity-document images. Filenames, Odoo structures and references to commerce and logistics integrations are mutually consistent. No individual data, bank reference, document, audio file or download link is reproduced here.

  **Assumption:** The match between the published figures and the three key exports, corpus composition, Odoo structures and associated documents provides very strong structural evidence of an operational dataset linked to Tera.ma. It does not, by itself, establish the access vector, the author’s identity, actual extraction date, scope beyond the corpus or official confirmation of the incident.

  **Unknown:** The source and affected systems, access method and duration, production-database completeness, number of unique people and organisations, current validity of accounts or integrations, encryption, operational disruption, existence or outcome of negotiation, and confirmation by Tera.ma or an authority all remain unknown.

- **Analysis scope:** All **8,140 supplied files** were inventoried read-only. The **282 CSV files** were counted, and full structural checks were completed for the principal advertised exports. The corpus contains sensitive personal and commercial data: it remains outside the repository, with no extraction or reproduction of its content. Row counts do not establish the absence of duplicates or the number of unique people.

- **Risk assessment:** Based on the reviewed corpus, the release includes customer, supplier and employee information; invoices and orders; bank or payment information; application logs; commercial documents; and identity documents. If exploited, this material could enable identity abuse, bank-detail-change fraud, fraudulent payment requests, targeted phishing, privacy harm and commercial espionage. The risk is heightened by the presence of documents and third-party integration material.

- **Recommendations:**
  1. Isolate and preserve evidence across Odoo, database, e-commerce, mail, integration and backup environments; retain logs required for forensic investigation.
  2. Controlledly revoke potentially exposed sessions, API keys, tokens, technical accounts and provider access, then investigate anomalous reuse.
  3. Review bulk exports, administrator access, unusual queries, scheduled tasks and outbound transfers before and after 27 September 2025, without treating that date as confirmed.
  4. Prioritise protection for potentially affected customers, partners and employees; prepare applicable notification requirements once scope is established.
  5. Immediately strengthen payment-fraud, bank-detail-change and supplier-impersonation controls; require out-of-band verification for unusual financial requests.

- **Sources / Evidence:** forum post and screenshots supplied on 8 October 2026; local Tera.ma corpus supplied and analysed read-only. Criminal download links were neither followed nor published.

### 02 October 2026

#### 🇲🇦 Morocco - Karamtech

- **Incident date:** Not established
- **Initial publication date:** 2 October 2026 at 00:51 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 8 October 2026
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

  **Assumption:** The displayed logo and domains, Karamtech’s public activity and thematic consistency of the five samples support a plausible association with Karamtech’s commercial environment. They do not demonstrate that the **441 CSV files**, **18 GB**, claimed volumes or alleged secrets originate from a compromised organisational system.

  **Unknown:** The source corpus, its integrity, actual number of files and records, unique people affected, current validity of any secret, password or token, originating system, access vector and date, complete exfiltration, operational impact and confirmation by Karamtech or an authority all remain unknown.

- **Analysis scope and limitations:** The five samples were examined in full, including SHA-256 calculation, size and structural checks. However, each file contains only one line separator: records are concatenated into one continuous line. This anomaly prevents reliable row reconstruction, deduplication and validation of the claimed volumes. No 441-CSV corpus or 18-GB archive was supplied. The samples contain sensitive data and remain outside the repository.

- **Risk assessment:** If the claimed material is authentic, combining customer, commercial, HR, banking and messaging data could enable targeted phishing, supplier fraud, identity abuse and payment fraud. Potential exposure of secrets, passwords or tokens could increase the risk of unauthorised access and warrants precautionary rotation, without assuming that they are genuine or active.

- **Recommendations:**
  1. Preserve Odoo, IAM, database, e-commerce, mail and integration logs to establish the timeline of any incident.
  2. Controlledly rotate application secrets, API keys, service-account passwords, tokens and sessions; do not test values published by the actor.
  3. Investigate bulk exports, unusual privileged access, logins from new addresses, configuration changes and outbound transfers.
  4. Verify data held on customers, suppliers and employees, then prepare appropriate protection and notification measures once scope is established.
  5. Strengthen payment-fraud controls, bank-detail-change procedures and checks for unusual procurement or delivery requests.

- **Sources / Evidence:** forum publication and screenshot supplied on 8 October 2026; five locally supplied CSV files analysed read-only; [Karamtech official website](https://karamtech.ma/). No secret, password, token, bank value or individual data is published.

### 07 October 2026

#### 🇲🇦 Morocco - NextLevel PC

- **Incident date:** Not established
- **Initial publication date:** 7 October 2026 at 01:41 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 8 October 2026
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** E-commerce / IT equipment and gaming
- **Website:** `nextlevelpc.ma` (domain displayed in the publication)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication and sample provided to AFRINTEL

- **Victim Description:** NextLevel PC is presented by the author as a Moroccan e-commerce site specialising in IT equipment and gaming. This description and the domain are attributed to the publication; their technical connection to a compromised system has not been independently confirmed.

- **Analysis:**

  **Observed:** A post attributed to **Nameless511**, dated **7 October 2026 at 01:41** according to the displayed timestamp, announces free release of the “full database” for NextLevel PC after a period the author describes as **72 hours without response**. The author claims **52,545 customer accounts**, **60,262 shipping addresses**, **47,653 orders**, **11 internal accounts**, **14,160 cart/discount rules**, and transaction history worth **MAD 122.9 million**. The complete supplied and analysed local corpus contains **eight CSV files** totalling **30,556,090 bytes**, and exactly confirms the first five counts: `customers.csv` (**52,545** rows), `addresses.csv` (**60,262**), `orders.csv` (**47,653**), `employees.csv` (**11**) and `cart_rules.csv` (**14,160**). The **47,653 orders** total **122,865,604.60** in the payment field, consistent with the author’s claimed **MAD 122.9 million**. The currency is attributed to the publication; it is not independently established by that calculation.

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

### 05 October 2026

#### 🇲🇦 Morocco - Cadi Ayyad University (UCA)

- **Incident date:** Not established
- **Initial publication date:** 5 October 2026 at 02:25 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 8 October 2026
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

  **Assumption:** Consistency among the university’s identity, its official domain, APOGÉE identifiers, institutional addresses and academic information strongly supports attribution of the sample to the UCA ecosystem. It does not prove that the data came directly from a system administered by the university: a historical copy, provider or another source remain possible.

  **Unknown:** The complete source file, its hash, actual number of records and unique people, authenticity and currency of the records, originating system, acquisition method and date, scope beyond the claimed **270** records, complete exfiltration, operational impact and confirmation by UCA or an authority all remain unknown.

- **Analysis scope:** Analysis is limited to the supplied publication, screenshots and structured sample content; no source archive or download link was opened. The content contains highly sensitive personal data and photographs, so it was neither reconstructed nor retained in the repository. The sample cannot validate the claimed **270** records or assess duplicates.

- **Risk assessment:** If authentic, the observed data could facilitate identity abuse, document fraud, targeted phishing against students and staff, targeting of university accounts and abuse of administrative processes. Photographs combined with civil and academic identifiers heighten fraud and privacy risks.

- **Recommendations:**
  1. Preserve logs across APOGÉE, admissions, identity, directory, photo-storage and administrative-account systems.
  2. Investigate bulk exports, unusual privileged access, provider accounts and outbound transfers of student data.
  3. Assess the scope of potentially affected students, alumni and staff without reusing published values.
  4. Strengthen university-account protections and monitor phishing, document fraud and impersonation attempts targeting the UCA community.
  5. Apply appropriate notification and protection procedures after the actual scope is established.

- **Sources / Evidence:** forum publication, structured sample and screenshots supplied on 8 October 2026; [UCA official website](https://www.uca.ma/). No criminal link, national identifier, email address, telephone number, photograph or other individual data is published.

### 9 October 2026

#### 🇲🇦 Morocco - Ministry of Endowments and Islamic Affairs

- **Incident date:** Not established
- **Initial publication date:** 9 October 2026 at 03:44 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** 9 October 2026
- **Actor / Group:** Nameless511 (displayed forum account; identity and affiliation unverified)
- **Sector:** Government / Administration / Religious affairs
- **Website:** Not specified in the analysed material
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Underground Forum - Publication, screenshots and local corpus provided to AFRINTEL

- **Victim Description:** The Ministry of Endowments and Islamic Affairs is a Moroccan public institution responsible, among other functions, for religious affairs and endowments.

- **Analysis:**

  **Observed:** A post attributed to **Nameless511**, timestamped **9 October 2026 at 03:44** according to the displayed time, advertises a “full candidate database” associated with a first-grade state engineer recruitment examination. The author claims approximately **109,000 rows** in CSV, XLSX and PDF-attachment formats. Displayed categories include Arabic and Latin-script names, national identity number, date and place of birth, gender, address, contact information, diplomas, specialities, issuing institutions, application status, rejection reason, examination centre and uploaded documents. The supplied local corpus includes **33 XLSX files** and one CSV, totaling approximately **44.2 MB**. XML-structure analysis of all XLSX files identified **109,673 rows**, including **109,640 data rows** assuming one header row per file: a volume consistent with the claim. The visible sample has a structure consistent with candidate application files. No individual data, identity document or attachment is reproduced.

  **Assumption:** Consistency between the examination title, administrative fields and file structure supports a link to a Moroccan public-recruitment process attributed to the ministry. It does not prove the files came directly from a ministry-administered system or that the claimed full volume was exfiltrated.

  **Unknown:** The actual number of candidates and unique people, the corpus’s precise coverage, originating system, acquisition method and date, authenticity and currency of the files, actual presence of every claimed attachment, operational impact and any official confirmation remain unknown.

- **Analysis scope:** Analysis is limited to the publication, screenshots and a supplied local corpus. The author’s approximately **109,000**-row claim is consistent with AFRINTEL’s structural count of the XLSX files, but this does not confirm the number of unique people or completeness of the corpus. The highly sensitive observed data was neither reconstructed nor retained in the repository.

- **Risk assessment:** If authentic, the data could enable identity abuse, targeted phishing against candidates, document fraud, misuse of application information and large-scale privacy harm.

- **Recommendations:**
  1. Preserve logs for recruitment, application-submission, document-storage and administrative-account systems.
  2. Investigate bulk exports, unusual privileged access and outbound transfers related to the relevant recruitment processes.
  3. Establish the actual scope of potentially affected candidates without using published values.
  4. Strengthen account security, document-access controls and detection of phishing targeting candidates.
  5. Apply appropriate notification and protection procedures after validating the incident and its scope.

- **Sources / Evidence:** forum publication, screenshots, sample and local corpus supplied on 9 October 2026. No criminal link, national identifier, address, telephone number, email, document or other individual data is published.

### 10 October 2026
#### Decathlon Morocco

- **Sector:** Retail / Sporting Goods / E-commerce
- **Victim:** Decathlon Morocco
- **Website:** https://www.decathlon.ma/
- **Incident Type:** Data Leak / Alleged Personal Data Exposure
- **Threat Actor / Group:** Nameless511
- **Claimed Volume:** More than 24,438 customer orders
- **Status:** Threat actor claim supported by a published data sample
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

However, the available evidence does not establish whether the exposure resulted from:

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
