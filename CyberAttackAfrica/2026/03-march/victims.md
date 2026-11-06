[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL) ![Scope](https://img.shields.io/badge/Scope-Africa-orange) ![Disclosure](https://img.shields.io/badge/TLP-CLEAR-green)

# African victims - March 2026 (45 documentary records)
👉🏾 [Version française](./victims_FR.md) | [CTI Report](./README.md)

## Methodology and evidence caveats

**45 records observed or indexed in March 2026 across 12 African countries plus one multi-country record**: 19 ransomware claims, 24 data leak records, one access sale and one operational fraud case. They do not prove 45 distinct intrusions. **Initial publication**, **technical event**, **AFRINTEL discovery** and **follow-up dates** are separate. Earlier data identified in March retain their original chronology. The Diesel-Electric record may overlap with February; Gauteng/Kazu May is linked but non-canonical. A leak-site post or sample is not first-party confirmation.

### Types
| Category | Records | Share |
|---|---:|---:|
| Data Leak | 24 | 53.3% |
| Ransomware | 19 | 42.2% |
| Access Sale | 1 | 2.2% |
| Operational Fraud | 1 | 2.2% |
| **Total** | **45** | **100%** |

### Geographic scope
| Country / scope | Records |
|---|---:|
| South Africa | 17 |
| Morocco | 8 |
| Egypt | 8 |
| Nigeria | 2 |
| Senegal | 2 |
| Algeria | 1 |
| Guinea | 1 |
| Madagascar | 1 |
| Multi-country Africa | 1 |
| Namibia | 1 |
| Tanzania | 1 |
| Tunisia | 1 |
| Zambia | 1 |
| **Total** | **45** |

> **Editorial review of 6 November 2026.** Institutional domain validation does not verify a compromise. Historical text is retained for provenance with explicit CTI follow-up notes. No personal record or secret is added.

## Detailed records - March 2026

### March 01, 2026

#### 🇿🇦 South Africa - Diesel-Electric Group
- **Initial publication date:** March 01, 2026


- **Ransomware group:** LockBit 5.0
- **Sector:** Automotive (Distribution & Services)
- **Website:** [diesel-electric.co.za](https://diesel-electric.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Major automotive component distributor in Southern Africa, including Bosch Service franchises and e-CAR centers.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The LockBit 5.0 listing concerns the same organisation as a February 2026 record. The two posts may be a repost or a separate episode; do not count two proven intrusions before comparing samples and dates. Review remote-access logs, EDR, backup access and shared files.

#### 🇿🇲 Zambia - ZISPIS (Zambia Integrated Social Protection Information System)
- **Initial publication date:** March 01, 2026


- **Threat Actor:** Spirigatito
- **Sector:** Government / Social Protection
- **Website:** [mcdss.gov.zm](https://www.mcdss.gov.zm)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim Description:** The ZISPIS system, a unified national registry used by the Zambian government to manage social protection programs, is the subject of an alleged compromise. The actor claims to have affected approximately 15 million individuals and exposed over 34 million records. The leaked data includes full personal information (name, date of birth, gender, national identifiers), detailed socio-economic data (household conditions, education level, living standards), financial data (payments, balances, cycles), and geographic information (GPS coordinates). Published samples also confirm the exposure of system audit logs and user activity, indicating a deep compromise of the application infrastructure.

- **Analysis:**
  AFRINTEL reviewed a post by the threat actor Spirigatito on a cybercriminal forum, titled "Government of Zambia (ZIPSIS) - 34M", along with an associated data sample. The sample consists of JSON exports from the ZISPIS system, operated by the Ministry of Community Development and Social Services (mcdss.gov.zm) as part of the Social Cash Transfer program. Observed beneficiary records include full name, gender, date of birth, national identifier, household GPS coordinates, district and village of residence, detailed socio-economic status (dwelling type, water and electricity access, food security, disability status) and payment data (amounts, cycles, delivery channel, and the named payment point representative with contact details). The sample also includes application activity logs tied to named government agent accounts (email addresses on the mcdss.gov.zm and cbt.gov.zm domains), with actions such as beneficiary record updates, payment validation, report generation and case closure due to death. These elements are consistent with direct access to the ZISPIS application database and its audit logs, rather than a limited partial export. AFRINTEL does not reproduce any individual name, national identifier, phone number or GPS coordinate from this sample. AFRINTEL did not have access to the full claimed 34 million records and cannot confirm this total volume or the initial access vector.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record concerns an alleged data publication; authenticity and full scope are not established beyond the described evidence. Defensive auditing of access and exports is recommended.

#### 🇿🇦 South Africa - Eventing South Africa
- **Initial publication date:** March 01, 2026


- **Actor / Group:** xNov
- **Sector:** Sports / Leisure
- **Website:** [eventingsa.co.za](https://www.eventingsa.co.za)
- **Leak Date:** January 16, 2026 (Identified in March 2026)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Eventing South Africa is the national governing body for eventing equestrian sports. xNov leaked a database containing club and member information: names, email addresses, login credentials (passwords), affiliation details, horse and rider records, competition data, and administrative/financial records (payments, invoices).


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record concerns an alleged data publication; authenticity and full scope are not established beyond the described evidence. Defensive auditing of access and exports is recommended.

#### 🇩🇿 Algeria - Bridges (tebridges.dz)
- **Initial publication date:** March 01, 2026


- **Actor / Group:** Grubder
- **Sector:** Technology / Business Services (CRM)
- **Website:** [tebridges.dz](https://www.tebridges.dz)
- **Incident Date:** February 02, 2026
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Bridges is a technology solutions provider in Algeria. Grubder listed a database with ~672,000 active records (PII and CRM) including full names, primary phone numbers, detailed local addresses, postal codes, and account statuses. A data sample (CSV) validated the extraction.

  On the same day (February 02, 2026), a second account, Dripper, posted a separate listing offering the same claimed volume (~672,000 records) for the same domain, priced at 143 dollars with a Telegram/Session contact. AFRINTEL assesses this as most likely a repost or resale of the same database rather than a distinct intrusion. The Dripper account has since been banned by the forum for attempted scamming involving public data, and the sample attached to this repost mixed one record labeled Afghanistan with Algeria-labeled records, which weakens the reliability of this specific repost without calling into question the existence of Grubder's original claim.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record concerns an alleged data publication; authenticity and full scope are not established beyond the described evidence. Defensive auditing of access and exports is recommended.

#### 🌍 Africa (Multi-country) - Loozap (loozap.com)
- **Initial publication date:** March 01, 2026


- **Actor / Group:** zimablue
- **Sector:** E-commerce / Online classifieds
- **Website:** [loozap.com](http://loozap.com/)
- **Incident Date:** January 28, 2026 (identified in March 2026)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim description:** Loozap is a pan-African online classifieds platform (formerly Listings360) operating country-specific sections across dozens of African markets from a single shared application, rather than a standalone national service. A threat actor published a database containing approximately 34,000 user accounts.
- **Analysis:** AFRINTEL reviewed a structured sample of the published user table. The records are not tied to a single country: reviewed entries list users located in, among others, Egypt, Kenya, Ghana, Ethiopia, Nigeria and Mozambique, consistent with Loozap's role as a single shared platform database serving its country-specific subdomains rather than a per-country deployment. The reviewed fields include full name, email address, an SHA1-format password hash, registration IP address, precise geolocation coordinates, date of birth, gender and social-activity metadata (followers, likes, group memberships). The consistent database schema across records from different countries, together with the volume and internal structure of the sample, supports a high confidence assessment of a genuine, full compromise of the platform's shared user database rather than a claim limited to one national instance. Given the multi-country scope, the presence of precise geolocation data and weak (SHA1) password hashing, this incident creates a risk of large-scale account takeover, credential-stuffing against reused passwords, and targeted phishing affecting users across multiple African countries simultaneously. AFRINTEL does not reproduce any name, email address, password hash, IP address or geolocation coordinate from the reviewed sample.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record concerns an alleged data publication; authenticity and full scope are not established beyond the described evidence. Defensive auditing of access and exports is recommended.

### March 02, 2026

#### 🇪🇬 Egypt - Waste Management Regulatory Authority (WMRA)
- **Initial publication date:** March 02, 2026


- **Actor / Group:** CrowStealer
- **Sector:** Government / Environment
- **Website:** [wmra.gov.eg](https://wmra.gov.eg/en/)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Agency under the Ministry of Environment responsible for waste management regulation. Database containing administrative data, internal records, information on partners and staff.


- **Originally cited domain :** `garb.gov.eg` - relationship unverified.

- **Institutional verification :** [source publique](https://wmra.gov.eg/en/). Verifying an institutional domain does not confirm the alleged intrusion.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The WMRA institutional portal is identified at wmra.gov.eg; a technical link between the original garb.gov.eg domain and the alleged leak remains unestablished. The agency’s existence does not validate the provenance of the data or a compromise of its official portal.

#### 🇪🇬 Egypt - Orascom Construction
- **Initial publication date:** March 02, 2026


- **Actor / Group:** CrowStealer
- **Sector:** Engineering & Construction
- **Website:** [orascom.com](https://orascom.com/)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Leading engineering and construction company operating in the Middle East, North Africa, and the United States. Compromised data: staff_id, full names, professional emails, departments, positions.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record concerns an alleged data publication; authenticity and full scope are not established beyond the described evidence. Defensive auditing of access and exports is recommended.

#### 🇪🇬 Egypt - Ministry of Health and Population (E-Portal)
- **Initial publication date:** March 02, 2026


- **Actor / Group:** CrowStealer
- **Sector:** Government / Health
- **Website:** [mohp.gov.eg](https://www.mohp.gov.eg)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Database of 3.8 million records (2019-2026) including full names, National ID, phone numbers, addresses, precise medical diagnoses, types of surgeries, treatment facilities.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The claimed 3.8 million records and detailed medical data are not independently verified as a full volume. The main potential risks are health-data confidentiality, impersonation and targeting; the ownership of the affected databases and providers requires validation.

### March 03, 2026

#### 🇿🇦 South Africa - Walter Sisulu University (WSU)
- **Initial publication date:** March 03, 2026


- **Actor / Group:** TelephoneHooliganism
- **Sector:** Education / University
- **Website:** [wsu.ac.za](https://www.wsu.ac.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Public university in the Eastern Cape. Data structured in three sections (Contacts, Enrollments, Tickets): dates of birth, emails, addresses, GPAs, scholarships, support history.

- **Analysis:**
  AFRINTEL reviewed a data sample corresponding to the Tickets section of this claim: an export of internal IT helpdesk tickets, structured with contact ID, email, phone number, first and last name, ticket status and category, priority, origin channel, assigned agent, opening and closing dates, resolution summary, internal agent notes, an SLA breach flag and region (among them Western Cape, Gauteng, KwaZulu-Natal, Eastern Cape and Northern Cape). Observed ticket categories include student portal access issues, email access, software installations and one case classified as Security involving suspicious account activity. This sample is consistent with the university's support helpdesk ticketing system and confirms, in addition to the Contacts and Enrollments sections already mentioned in the description, exposure of contact details and internal support operational content. AFRINTEL did not have access to the Contacts and Enrollments sections themselves during this review and cannot confirm the total volume of tickets involved or the initial access vector.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record concerns an alleged data publication; authenticity and full scope are not established beyond the described evidence. Defensive auditing of access and exports is recommended.

#### 🇪🇬 Egypt - Ministry of Education and Technical Education
- **Initial publication date:** March 03, 2026


- **Actor / Group:** CrowStealer
- **Sector:** Government / Education
- **Website:** [moe.gov.eg](https://moe.gov.eg)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Data on students and staff: national IDs, full names, addresses, academic records.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** “Data Fully Published” describes a publication status, not an institutional confirmation of the initial access or full dataset. Priorities include the integrity of education records and privileged-account monitoring.

#### 🇲🇦 Morocco - National Office of University, Social and Cultural Works (ONOUSC)
- **Initial publication date:** March 03, 2026


- **Actor / Group:** xNov
- **Sector:** Education / Government
- **Website:** [amo.onousc.ma](https://amo.onousc.ma)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Body responsible for student social services in Morocco (scholarships, university housing, health coverage). Exposure of 3,631 student records related to Mandatory Health Insurance (AMO): names, CINE numbers, university registration numbers, CNE, dates of birth, enrollment statuses.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The stated 3,631 student AMO records concern potential exposure of educational social-service data. The full dataset and affected systems require independent confirmation; possible consequences include identity fraud and administrative impersonation.

### March 04, 2026

#### 🇲🇦 Morocco - Outsourcia
- **Initial publication date:** March 04, 2026


- **Ransomware group:** Qilin
- **Sector:** Business Process Outsourcing (BPO)
- **Website:** [outsourcia.com](https://www.outsourcia.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Major customer relationship operator based in Casablanca, managing business processes for international accounts.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** A BPO-provider claim raises a potential downstream customer risk if outsourced data or remote access were involved. The record does not establish any client-specific impact or intrusion method; review supplier access without assuming a confirmed client breach.

### March 05, 2026

#### 🇪🇬 Egypt - Rowad Modern Engineering
- **Initial publication date:** March 05, 2026


- **Ransomware group:** Crypto24
- **Sector:** Engineering & Construction
- **Website:** [rowad-rme.com](http://www.rowad-rme.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Egyptian construction company specializing in infrastructure projects and commercial buildings.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

### March 06, 2026

#### 🇪🇬 Egypt - INTERACT TECHNOLOGY SOLUTIONS
- **Initial publication date:** March 06, 2026


- **Ransomware group:** PEAR
- **Sector:** IT Consulting
- **Website:** [interactts.com](http://interactts.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Company providing critical technology and infrastructure solutions in Egypt.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

#### 🇲🇬 Madagascar - Orange Madagascar
- **Initial publication date:** March 06, 2026


- **Ransomware group:** Qilin
- **Sector:** Telecommunications
- **Website:** [orange.mg](https://www.orange.mg/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Telecommunications leader in Madagascar, operating internet, mobile, and mobile banking services.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The telecommunications claim calls for continuity and third-party access review. No compromise of the core network or mobile-money transaction systems is demonstrated; both remain defensive risk hypotheses.

### March 08, 2026

#### 🇸🇳 Senegal - Directorate General of Public Accounting and Treasury (DGCPT) [Access Sale]
- **Initial publication date:** March 08, 2026



- **Threat Actor / Group :** w00l_ysh1
- **Sector :** Government / Public Finance
- **Web site :** [sentresor.org](https://www.sentresor.org/)
- **Status :** Claim - Unverified
- **Incident type:** Access Sale

- **Description :** A cybercriminal forum post advertises the sale of access to the infrastructure of Senegal’s Directorate General of Public Accounting and Treasury (DGCPT).

- **Claimed Accesses :**
  - VPN credentials
  - Windows Server administrator access
  - Domain Controller (DC) access
  - access to a network of more than 200 computers
  - access to financial databases and internal servers

- **Observed Pricing :**
  - VPN access: USD 500
  - administrator access to two servers: USD 2,000
  - Domain Controller access: USD 15,000

- **CTI Analysis :**
  The published elements potentially indicate an advanced compromise of a governmental financial environment. Domain Controller access could enable:
  - lateral movement,
  - persistence,
  - data exfiltration,
  - ransomware deployment,
  - or full Active Directory compromise.

- **CTI Note :**
  No independent technical evidence currently confirms the authenticity of the claimed accesses. However, the segmented offers (VPN, servers, DC) align with common Initial Access Broker (IAB) tradecraft observed on cybercriminal marketplaces.
---

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** An alleged access sale must be distinguished from ransomware and data leaks. An offered domain-controller account does not prove current privilege validity. SOC hypotheses include anomalous VPN access, privileged group changes, service creation, domain-controller logons and supplier-account use.

### March 09, 2026

#### 🇹🇳 Tunisia - K.PROPHA (Karray Produits Pharmaceutiques)
- **Initial publication date:** March 09, 2026


- **Ransomware group:** TheGentlemen
- **Sector:** Health / Pharmaceutical
- **Website:** [kpropha.com](http://kpropha.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Tunisian company specializing in the distribution of pharmaceutical and para-pharmaceutical products.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

### March 12, 2026

#### 🇲🇦 Morocco - HACA (High Authority for Audiovisual Communication)
- **Initial publication date:** March 12, 2026


- **Ransomware group:** APT73 / Bashe
- **Sector:** Government / Media
- **Website:** [haca.ma](http://haca.ma)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Constitutional body responsible for regulating audiovisual communication in Morocco.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

### March 13, 2026

#### 🇿🇦 South Africa - Lion of Africa Insurance
- **Initial publication date:** March 13, 2026


- **Ransomware group:** Lynx
- **Sector:** Insurance services
- **Website:** [lionsureins.com](http://lionsureins.com/)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** South African insurance company handling large volumes of personal and financial data.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

#### 🇿🇦 South Africa - Gauteng Provincial Government
- **Initial publication date:** March 13, 2026


- **Actor / Group:** XP95
- **Sector:** Government / Public administration
- **Website:** [gauteng.gov.za](https://www.gauteng.gov.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Manages the most populous province in South Africa (Johannesburg, Pretoria). 3.8 TB of data (3.6 million files) exfiltrated: health, education, housing, economic development.

- **Related Kazu claim type:** Ransomware / extortion context. This is a linked secondary claim and is not counted as a separate canonical incident; the available material does not establish encryption or a distinct intrusion.

**Related secondary claim - not counted as a new canonical incident:** A separate Kazu publication dated **16 May 2026** also names the Gauteng Provincial Government. It advertises **3,673,556 files**, approximately **3.8 TB**, and a **USD 25,000** price. The locally supplied archive contains **1,905 files** and approximately **1.905 GB**; its SHA-256 is `3fd8dcb059e77bad240e50d7e5691fdcf75fd81d4c9680e6f56e431ed6e42261`. The overlap in victim and claimed volume with the XP95 record is consistent with a duplicate claim, transfer/resale, or a separate exposure, but the available evidence does not distinguish these hypotheses. The Kazu claim is therefore retained as a linked, non-canonical claim and does not increase the incident total.

This chronology is recorded as **two observed claims** - XP95 in March and Kazu in May - but **one canonical incident** pending evidence that the Kazu material represents a distinct compromise.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The asserted 3.8 TB volume is an actor claim; a later Kazu posting in May remains a linked claim, not a separate canonical incident. Prioritise cross-agency exposure assessment and source-metadata comparison over unsupported forensic attribution.

#### 🇿🇦 South Africa - Buffalo City Metropolitan Municipality [Data Leak]
- **Initial publication date:** March 13, 2026



- **Threat Actor / Group :** wh6ami
- **Sector :** Government / Municipal Administration
- **Website :** [buffalocitymetro.gov.za](https://www.buffalocitymetro.gov.za/)
- **Leak Date :** March 13, 2026
- **Status :** Claim - Data Sample Published
- **Incident type:** Data Leak

- **Description :** A cybercriminal forum post claims the sale of a database allegedly linked to Buffalo City Metropolitan Municipality in South Africa. The threat actor claims to possess administrator-level access and publishes multiple samples related to municipal services, internal users, and administrative logs.

- **Observed Data :**
  - full names
  - government email addresses
  - phone numbers
  - internal departments
  - user roles
  - login logs
  - administrator actions
  - tender-related information
  - municipal employee data
  - office addresses

- **CTI Analysis :**
  The published elements suggest exposure of a government backend database containing user data, administrative logs, and municipal service information. The observed logs notably include:
  - account creation/deletion,
  - password modifications,
  - administrator logins,
  - content publication,
  - and tender-related operations.

  Risks include:
  - compromise of government accounts,
  - targeted spear phishing,
  - tender fraud,
  - or abuse of persistent administrative access.

- **CTI Note :**
  The published samples contain data consistent with an operational municipal platform along with detailed administrative activity logs.

- **Institutional verification :** [source publique](https://www.gov.za/nso/about-government/contact-directory/ec-municipalities/buffalo-city-metropolitan-municipality). Verifying an institutional domain does not confirm the alleged intrusion.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The municipal site can be verified independently, but the forum logs do not establish current administrator access. Risks include tender fraud, spear phishing and potential account misuse; investigate identity and content-management audit trails.

### March 14, 2026

#### 🇪🇬 Egypt - Grid Fine Finishes
- **Initial publication date:** March 14, 2026


- **Ransomware group:** Payload
- **Sector:** Fit-out / Construction
- **Website:** [gridff.com](http://gridff.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Egyptian company specializing in high-end interior fit-out for commercial and residential sectors.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

### March 16, 2026

#### 🇿🇦 South Africa - Northern Cape Department of Roads & Public Works [Data Leak]
- **Initial publication date:** March 16, 2026


- **Threat Actor / Group :** wh6ami
- **Sector :** Government / Public Infrastructure / Transportation
- **Website :** [ncrpw.ncpg.gov.za](http://ncrpw.ncpg.gov.za/)
- **Leak Date :** March 16, 2026
- **Status :** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Description :** A cybercriminal forum post claims the sale of a database allegedly linked to South Africa’s Northern Cape Department of Roads & Public Works. The published samples contain data extracted from contact forms and administrative exchanges related to public infrastructure, tenders, internships, applications, and institutional requests.
- **Observed Data :**
  - full names
  - email addresses
  - phone numbers
  - full message contents
  - tender-related requests
  - internships and job applications
  - supplier inquiries
  - public road and infrastructure information

- **CTI Analysis :**
  The observed elements suggest exposure of a backend database handling government contact forms and administrative communications. The leaked information could be leveraged for:
  - targeted spear phishing,
  - tender fraud,
  - identity impersonation,
  - or BEC attacks targeting suppliers and government partners.

- **CTI Note :**
  The published samples contain real exchanges related to public infrastructure, suppliers, road projects, and governmental administrative processes.

- **Institutional verification :** [source publique](https://provincialgovernment.co.za/units/view/94/northern-cape/roads-and-public-works). Verifying an institutional domain does not confirm the alleged intrusion.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The departmental domain appears in official directories. Published form submissions and correspondence are consistent with a back-office dataset exposure, but neither privileged access nor total scope is established. Monitor supplier-bank changes and administrative mailbox misuse.

### March 17, 2026

#### 🇿🇦 South Africa - University of South Africa (UNISA)
- **Initial publication date:** March 17, 2026


- **Actor / Group:** Blackwinter99
- **Sector:** Education / Higher Education
- **Website:** [unisa.ac.za](https://www.unisa.ac.za)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** UNISA is Africa's largest distance learning institution. Blackwinter99 publicly disclosed login credentials for the site's administration page on an underground forum, which, if valid, could provide elevated platform privileges, enabling massive student data exfiltration, tampering with academic records, or complete takeover of the web infrastructure.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** Publication of allegedly privileged credentials does not prove that they remain valid. Portal takeover and mass exfiltration are potential scenarios, not demonstrated outcomes.

### March 19, 2026

#### 🇳🇦 Namibia - Namibia Airports Company
- **Initial publication date:** March 19, 2026


- **Ransomware group:** INC Ransom
- **Sector:** Air transport
- **Website:** [airports.com.na](http://airports.com.na)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Official manager of national airports in Namibia.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

### March 20, 2026

#### 🇿🇦 South Africa - The Unlimited
- **Initial publication date:** March 20, 2026


- **Ransomware group:** DragonForce
- **Sector:** Insurance services
- **Website:** [theunlimited.co.za](http://theunlimited.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Provider of insurance products including health, auto, legal, and life.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

#### 🇲🇦 Morocco - Ministry of Justice
- **Initial publication date:** March 20, 2026


- **Actor / Group:** anisanas2
- **Sector:** Government / Justice
- **Website:** [justice.gov.ma](https://www.justice.gov.ma)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** The actor claims exfiltration of 300 GB including more than 150,000 court case files (2019-2026). Disputes between major Moroccan companies and individuals (12 billion MAD). Documents: IDs, bank statements, court records, invoices.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The 300 GB and 150,000 case files are source claims; the complete archive is not independently verified in the supplied evidence. Treat confidentiality of legal case data as the priority and avoid declaring all court records compromised.

### March 21, 2026

#### 🇿🇦 South Africa - Elundini Local Municipality
- **Initial publication date:** March 21, 2026


- **Ransomware group:** TheGentlemen
- **Sector:** Local government
- **Website:** [elundini.gov.za](http://elundini.gov.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Municipal administration dedicated to sustainable development in the Eastern Cape province.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

### March 22, 2026

#### 🇿🇦 South Africa - Semenya Furumele Consulting Engineers
- **Initial publication date:** March 22, 2026


- **Ransomware group:** NightSpire
- **Sector:** Engineering consulting
- **Website:** [sfce.co.za](http://www.sfce.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Engineering consulting firm based in South Africa.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

### March 23, 2026

#### 🇿🇦 South Africa - Standard Bank South Africa
- **Initial publication date:** March 23, 2026



- **Incident / first communication date:** March 23, 2026
- **Public updates:** April 2, 13 and 14, 2026
- **Actor / Group:** Not officially attributed; separate PrinzEugen claim uncorroborated
- **Sector:** Finance / Banking
- **Website:** [standardbank.co.za](https://www.standardbank.co.za/southafrica/personal)
- **Status:** Incident Confirmed by Victim
- **Incident type:** Data Leak
- **Confidence:** Very High
- **Impact:** Level 4
- **Description:** **Standard Bank South Africa** represents the South African banking operations of **Standard Bank Group**, offering accounts, payments, financing, business banking and investment-related services. **The Standard Bank of South Africa Limited** is identified among the group's South African legal entities in its institutional documentation ([official privacy statement](https://www.standardbank.co.za/southafrica/personal/about-us/legal/privacy-statement)).

- **Independent verification as of 18 October 2026:** **First-party confirmation:** on 23 March 2026, Standard Bank disclosed unauthorised access to a limited set of data and said transactional systems and customer funds were unaffected. This predates September.

- **Additional verification sources:** [Source 1](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank)

- **Sources / Evidence:** [Standard Bank, March 23, 2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank); [Standard Bank, April 14, 2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-data-incident-update-14-april)

Standard Bank confirmed unauthorised access to internal administrative systems and document repositories, potentially exposing names, identifiers, contact details, addresses and account numbers. Transactional and core systems were reportedly not accessed. The vector, number of people and copied volume remain unknown. This record is distinct from the May Standard Bank Group claim.


- **Official source :** [Standard Bank – 23/03/2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank) ; [14/04/2026](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-data-incident-update-14-april).

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** First-party confirmation: Standard Bank acknowledged unauthorised access to some data on 23 March. Its 14 April update identifies internal administrative and document systems, while core banking and transactional systems were reportedly not accessed. The main risk is targeted impersonation rather than proven payment-system compromise.

#### 🇿🇦 South Africa - Pick n Pay ASAP / Bottles.com [Data Leak]
- **Initial publication date:** March 23, 2026



- **Threat Actor / Group :** p4pr1k4
- **Sector :** E-commerce / Delivery / Retail
- **Website :** bottles.com
- **Leak Date :** March 23, 2026
- **Status :** Claim - Data Sample Published
- **Incident type:** Data Leak

- **Description :** A cybercriminal forum post claims the sale of a database allegedly linked to Bottles.com, later integrated into Pick n Pay ASAP following its acquisition by Pick n Pay. The exposed data reportedly relates to South African delivery platform users.

- **Observed Data :**
  - full names
  - email addresses
  - phone numbers
  - birth dates
  - passwords
  - banking card information
  - VISA and Mastercard details
  - 3DS-related data
  - delivery addresses and history
  - GPS coordinates
  - customer service notes

- **CTI Analysis :**
  The published samples suggest exposure of a sensitive e-commerce database containing personal information, address history, and payment-related data. Risks include banking fraud, identity theft, targeted phishing, and customer account compromise.

- **CTI Note :**
  The observed samples include structured SQL extracts, address history records, and payment card/3DS-related information.
---

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The listing suggests delivery and payment-related data; card and 3DS fields need independent characterisation. Historic integration of Bottles into Pick n Pay ASAP does not establish compromise of current acquirer systems. Focus on provenance and customer-fraud monitoring.

### March 24, 2026

#### 🇸🇳 Senegal - United Bank for Africa (UBA Senegal)
- **Initial publication date:** March 24, 2026



- **Incident date:** 30-31 January 2026
- **Actor / Group:** Unattributed
- **Sector:** Finance / Banking
- **Website:** [ubasenegal.com](https://www.ubasenegal.com)
- **AFRINTEL status:** Under Investigation
- **Incident type:** Operational Fraud / Cyber-enabled ATM Cash-Out
- **Confidence level:** High
- **Impact level:** Level 4

- **Description:**

  UBA Senegal was affected by a coordinated cyber-enabled ATM cash-out operation conducted between 30 and 31 January 2026.

- **Analysis:**

  According to ngCERT advisory ngCERT-2026-060005, the operation involved 3,421 ATM withdrawal transactions and caused losses exceeding USD 2 million. Earlier reporting placed the losses at approximately 1.143 billion FCFA.  ngCERT assesses that privileged access to card-authorization infrastructure likely enabled the attackers to manipulate transaction controls and coordinate fraudulent withdrawals.

  The occurrence and financial impact of the fraudulent operation are therefore corroborated by a national CERT source. However, the initial access vector, the exact technical sequence, the identity of the threat actor and any possible insider involvement remain unconfirmed.

  Phishing, supply-chain compromise, insider access and ATM malware are possible scenarios discussed by ngCERT for this attack class and must not be presented as confirmed techniques used against UBA Senegal.

- **AFRINTEL correction note:**
  The incident occurred on 30-31 January 2026 but was identified/documented by AFRINTEL on 24 March 2026. It remains part of the March corpus according to the AFRINTEL detection-date methodology.
  The previous status "Under Investigation" should be refined because the operational fraud itself is corroborated. What remains under investigation is the technical intrusion path and threat-actor attribution.

- **Taxonomy note:**
  Operational Fraud is retained as a non-standard AFRINTEL incident category. The incident remains excluded from Ransomware, Data Leak, Access Sale and  Defacement counters.

- **External corroborating source :** [ngCERT, 25/06/2026, ngCERT-2026-060005](https://cert.gov.ng/advisories/alert-on-cyber-enabled-atm-cash-out-attacks-targeting-african-financial-institutions). No first-party victim confirmation identified in the consulted material.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The fraud occurred in late January and is included in March by documentation date. The 25 June ngCERT advisory cites 3,421 withdrawals and losses above USD 2 million, corroborating the operation but not attribution or the access path. Phishing, insiders and ATM malware are generic possibilities in the advisory, not proven methods in this case.

### March 26, 2026

#### 🇿🇦 South Africa - ETFSA
- **Initial publication date:** March 26, 2026


- **Ransomware group:** INC Ransom
- **Sector:** Wealth Management
- **Website:** [etfsa.co.za](http://ETFSA.co.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim description:** South African financial services platform specializing in exchange-traded funds (ETFs).

- **Analysis:**
  AFRINTEL reviewed the extortion post published for this victim, which references a claimed company revenue of approximately USD 8 million and names an individual identified as the platform's managing director. The post states that confidential and personal client data would be published, and displays thumbnail previews of numerous documents. AFRINTEL reviewed one accessible sample: an abridged death certificate issued by the South African Department of Home Affairs, containing an identity number, full name, date of birth and cause of death. This indicates that the exposed material includes client Know Your Customer (KYC) and estate-related identity documents rather than only account or transaction records, consistent with a wealth management and financial advisory client base. AFRINTEL did not access the remaining files and cannot confirm the total number of clients affected or the initial access vector.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

#### 🇲🇦 Morocco - Maroc Telecom
- **Initial publication date:** March 26, 2026


- **Ransomware group:** APT73 / Bashe
- **Sector:** Telecommunications
- **Website:** [iam.ma](http://iam.ma)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim description:** Historic telecommunications operator in Morocco, providing mobile, internet, and fixed-line services.

- **Analysis:**
  AFRINTEL reviewed sample screenshots published in connection with this claim. The material shows internal customer relationship and technical support screens (GRC/complaint-tracking interfaces) referencing client identifiers, contact details, installation addresses and fault-ticket records related to fixed-line and fiber-optic service issues. This is consistent with access to Maroc Telecom's customer support and complaint-management systems rather than a bulk subscriber database export. AFRINTEL did not access the underlying systems and cannot confirm the volume of records involved or the initial access vector.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The reviewed screenshots concern fixed-line/fibre service and support complaints. They do not establish an export of the complete subscriber base or network-equipment compromise. Monitor abnormal ticket access and excessive CRM queries.

#### 🇲🇦 Morocco - 2M TV
- **Initial publication date:** March 26, 2026


- **Ransomware group:** APT73 / Bashe
- **Sector:** Media & Audiovisual
- **Website:** [2m.ma](http://2m.ma)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim description:** Moroccan national television channel.

- **Analysis:**
  AFRINTEL reviewed sample documents published in connection with this claim, consisting of internal human resources material: an employee curriculum vitae for an audiovisual staff member, an internal list of employees holding driving licences, and an employment certificate ("attestation de travail") template bearing the 2M letterhead. This indicates exposure of staff personnel records rather than broadcast systems or customer data. AFRINTEL also reviewed a separate dataset: a full mailbox export in .eml format (1,777 messages), whose associated metadata (message identifiers in Microsoft Exchange/Office 365 format and a last-received timestamp dated November 2025) indicates the compromise of an individual professional mailbox, likely tied to 2M's Rédaction/News department, rather than a static set of documents. The correspondence covers 123 distinct internal 2m.ma addresses and relates notably to editorial planning for an internal show, administrative processes (including a press card request) and HR exchanges; approximately 348 messages carry attachments (images, PDFs, Word documents and Excel spreadsheets). Several message subjects do not correspond to any identifiable editorial activity and are consistent with unsolicited spam or social-engineering attempts received in this mailbox. AFRINTEL does not name the mailbox owner and does not reproduce message content or the identity of third-party correspondents. AFRINTEL did not access further files and cannot confirm the total number of employee records involved, the current access status of this mailbox, or the initial access vector.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** A professional mailbox export and HR documents support a mailbox or document-exposure hypothesis without proving access to broadcast infrastructure. SOC controls: anomalous M365/Exchange logons, forwarding rules, OAuth grants and bulk exports.

#### 🇲🇦 Morocco - Royal Institute for Strategic Studies (IRES)
- **Initial publication date:** March 26, 2026


- **Ransomware group:** APT73 / Bashe
- **Sector:** Research / Think tank
- **Website:** [ires.ma](http://ires.ma)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim description:** Strategic analysis center attached to the Moroccan Royal Cabinet.

- **Analysis:**
  AFRINTEL reviewed sample documents published in connection with this claim, consisting of curricula vitae of researchers and consultants associated with the institute, covering academic profiles (doctoral and master's-level research in public law and international relations), professional experience references and, in one case, contact details including an email address and phone number. This indicates exposure of staff and researcher personnel records. AFRINTEL did not access further files and cannot confirm the total number of records involved or the initial access vector.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

### March 29, 2026

#### 🇿🇦 South Africa - Statistics South Africa (Stats SA)
- **Initial publication date:** March 29, 2026


- **Ransomware group:** XP95
- **Sector:** Government / National Statistics
- **Website:** [statssa.gov.za](https://www.statssa.gov.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Stats SA is the national statistical agency of South Africa. XP95 claims to have exfiltrated 154 GB of data (453,362 files). The breach potentially compromises sensitive socio-economic data, census records, employment information, inflation data, and national administrative records. A $100,000 ransom has been demanded, with a public sale deadline set for April 20, 2026.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The 154 GB and 453,362 files are XP95 claims. National statistical confidentiality is a strategic concern, but the exact sensitive datasets are not established by the material provided; do not claim the entire census database was compromised.

#### 🇿🇦 South Africa - Gauteng City Region Academy (GCRA)
- **Initial publication date:** March 29, 2026


- **Ransomware group:** XP95
- **Sector:** Education / Training (Provincial Government)
- **Website:** [gcra.gauteng.gov.za](https://gcra.gauteng.gov.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** The GCRA is the agency responsible for skills development in the Gauteng province. The exfiltration of 147 GB of data potentially compromises student records (bursaries, registrations, PII), training program data, and the academy's administrative documents. XP95 has set a ransom deadline before the public sale of the files.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The announced 147 GB remains an actor claim. Exposure of scholarship and enrollment data, if confirmed, could enable financial fraud and targeting of students; verify the affected services and export trails.

### March 30, 2026

#### 🇹🇿 Tanzania - SBC Tanzania Limited
- **Initial publication date:** March 30, 2026


- **Ransomware group:** Morpheus
- **Sector:** Food & Beverage
- **Website:** [sbctanzania.co.tz](http://sbctanzania.co.tz)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Beverage manufacturer and distributor, official bottler of PepsiCo in Tanzania.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

#### 🇿🇦 South Africa - Nashua
- **Initial publication date:** March 30, 2026


- **Ransomware group:** Coinbase Cartel
- **Sector:** IT & Managed Services
- **Website:** [nashua.co.za](http://nashua.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim description:** Major provider of integrated technology solutions and managed services for businesses.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The record documents a ransomware claim only. Encryption, service disruption and complete exfiltration are not demonstrated; review backups, privileged access and potential third-party data exposure.

#### 🇳🇬 Nigeria - Ahmadu Bello University (ABU Zaria)
- **Initial publication date:** March 30, 2026


- **Actor / Group:** AshleyWood2022
- **Sector:** Education / Higher education
- **Website:** [abu.edu.ng](https://www.abu.edu.ng)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim description:** One of the largest research universities in Nigeria. Database (`tbl_flattened.csv` & `abu.sql`) with over 11,000 records: academic and non-academic staff (names, departments, ranks, qualifications, gender, date of birth, districts of origin).

- **Reliability note:**
  AFRINTEL reviewed the forum post by AshleyWood2022 dated March 30, 2026, together with a posted download link (gofile.io) and a visible data sample. The reviewed sample covers staff attached to the Office of the Vice Chancellor and its sub-units (ABU/FM Radio, ABUCONS, Central Procurement Unit, Academic Planning, University Advancement, Equipment Maintenance and Development Centre, Internal Audit, ITF/SIWES Coordination Centre, Procurement and Security Division), with 237 rows in this section alone, consistent in scale with the broader 11,000-plus record claim.

- **Analysis:**
  The sample follows a consistent schema: local government area and senatorial district of origin, state, geopolitical zone, date of birth, gender, faculty, department, staff category (academic or non-academic), rank and highest qualification. In the reviewed rows, the date-of-birth field is uniformly masked (`0000-00-00`) and no staff names, phone numbers or national identifiers are visible; the actor's post claims that names and other personal fields are present in the full dataset, which AFRINTEL did not download or independently verify. The structural consistency across 237 rows and the presence of a working download link support a stronger assessment than a bare claim, though the completeness, authenticity and full content of the archive remain unconfirmed. If the full claim is accurate, exposure of staff demographic and organisational data could support targeted social engineering, profiling by region, gender or department, and impersonation of university staff. AFRINTEL does not reproduce any record, field value or download link from the reviewed material.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** “Data Fully Published” reflects the post; the detailed review describes only 237 visible rows in one section against more than 11,000 claimed. The full dataset and presence of identifying fields remain unconfirmed.

### March 31, 2026

#### 🇳🇬 Nigeria - Remita (SystemSpecs)
- **Initial publication date:** March 31, 2026


- **Actor / Group:** Bytetobreach
- **Sector:** Fintech / Payment services
- **Website:** [remita.net](https://www.remita.net)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Major payment platform in Nigeria used by individuals, businesses, and government. Actor-claimed 3 TB leak: 800 GB of KYC documents (IDs, passports, bank statements, invoices), MySQL/Postgres databases, source code, Docker registries, government HSM keys, over 35,000 password hashes.

- **Analysis:**
  AFRINTEL reviewed a set of technical elements associated with this claim. A credentials file lists approximately 35,800 email address / password hash pairs (bcrypt format), covering both internal accounts (agents, operators) and likely platform customer accounts; AFRINTEL did not extract or attempt to crack any hash. Screenshots show a restored instance of the platform's databases in a SQL administration tool, including a business owner table (BVN number, ID type and number, base64-encoded identity document), an interbank transaction table (amounts, beneficiary bank codes, channel, payment reference), an internal admin account table (SystemSpecs agents with role and status) and a customer personal information table (date of birth, email, phone number, KYC status, hashed password). Other screenshots show a source code archive covering several platform microservices, including an SFTP-based encrypted communication module with the Central Bank of Nigeria (CBN) for exchanging payment instructions, an integration with the Pan-African Payment and Settlement System (PAPSS), a virtual wallet system built in partnership with OPay, and OTP verification logic. An additional screenshot shows a directory of key files named after more than twenty Nigerian banks (including GTBank, Zenith, UBA, First Bank, Access, FCMB, Fidelity, Sterling, Stanbic, Ecobank, UBN, Wema, Unity, Providus, Heritage and Citibank), consistent with master encryption keys tied to interbank integration; AFRINTEL did not verify the content or validity of these files. Secret-scanning tool results run against the source code repositories show detection of API keys, cloud access tokens and hardcoded database credentials in several configuration files, associated with SystemSpecs employee email addresses. AFRINTEL also reviewed the structure of a Git backup archive (approximately 34,800 files) covering roughly forty distinct internal repositories with full commit history, corresponding to the entire internal "remitacenta" GitLab organization: interbank and pan-African payment components (including a PAPSS connector and an ISO 20022 payment message builder, a standard used for interbank messaging), a fraud detection engine, a card tokenization SDK, Kubernetes infrastructure-as-code (three separate manifest sets) and a business intelligence module (Superset), the latter alone accounting for over a quarter of the archive's files. The archive contains approximately 200 production configuration files, 354 Helm "values.yaml" files and more than 400 file names explicitly referencing secrets, consistent with potential exposure of numerous additional credentials beyond those already flagged by the scanning tools; AFRINTEL did not open these files individually and does not reproduce any further secret. One additional file, marked as an unfinished download, corresponds to a backup image in Veeam Backup & Replication format (XBSTCK01 signature, tool version 12.1.2) referencing InnoDB log files, consistent with a system-level backup including a MySQL/MariaDB database; as this file is incomplete, AFRINTEL was unable to mount it or review its content. A final screenshot shows access, via cloud credentials extracted from the source code, to a cloud storage bucket dedicated to KYC documents containing approximately 657,000 files for a raw volume of approximately 588 GB, as well as several other buckets tied to the company's internal GitLab infrastructure (backups, artifacts, container registry). AFRINTEL does not reproduce any individual credential, key, token, hash, account name or identity document from these elements. Taken together, these observations are consistent with a deep compromise of Remita's development and production infrastructure, potentially extending to its banking and pan-African integration systems, but AFRINTEL did not verify the authenticity or currency of each individual element and cannot confirm the exact extent of access obtained or the initial access vector.


- **Regulatory follow-up :** [NDPC / presse indépendante, 06/04/2026](https://www.premiumtimesng.com/news/top-news/869669-ndpc-investigates-remita-sterling-bank-for-alleged-data-breach.html). Investigation opened; impact scope not confirmed.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** Material described by AFRINTEL suggests possible exposure beyond business records, including Git backups, configurations, KYC data and financial-integration references. Nigeria’s NDPC opened an investigation in April 2026. This official investigation confirms neither the claimed 3 TB nor validity of all keys nor actual interbank access; prioritise secrets, cloud identities, source code and third-party dependencies.

#### 🇲🇦 Morocco - Smarteez (L'Oréal Morocco Supply Chain Provider)
- **Initial publication date:** March 31, 2026


- **Actor / Group:** xNov
- **Sector:** Digital Marketing / Cosmetics (L'Oréal Supply Chain)
- **Website:** [smarteez.eu](https://smarteez.eu)
- **Status:** Data Fully Published
- **Incident type:** Data Leak
- **Victim description:** Smarteez is a Moroccan digital provider used by L'Oréal Morocco for field operations management. Exposure of critical data: information on 296 pharmacies (GPS, segmentation), 361,000 sales/KPI records, 22 plaintext OAuth2 application secrets, complete administrative logs. A production APK was also disclosed.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The reported OAuth2 secrets and commercial records warrant legitimacy checks and defensive rotation by authorised operators. The supply-chain connection to L’Oréal Morocco may enable partner fraud, but does not prove compromise of L’Oréal systems.

#### 🇪🇬 Egypt - Semsar Masr (semsarmasr.com)
- **Initial publication date:** March 31, 2026


- **Actor / Group:** Al-Sheikh
- **Sector:** Real Estate / Online Classifieds
- **Website:** [semsarmasr.com](https://www.semsarmasr.com)
- **Date of breach:** January 2026 (identified in March 2026)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Victim description:** Semsar Masr is an Egyptian real estate classifieds platform, active since 2007, enabling the posting and browsing of listings for apartments, land and other properties for sale or rent in Egypt.
- **Analysis:** AFRINTEL reviewed a post published on January 28, 2026 by the actor Al-Sheikh concerning the `tb_members_Profiles` table of semsarmasr.com, stating it contains 185,024 rows and that user passwords are stored in plaintext. The sample displayed in the post includes a field schema covering user ID, account status, email address, phone number, password, user role, contact name, company name, address, social media handles (WhatsApp, Telegram, LinkedIn, Twitter, Facebook), date of birth, occupation, gender, marital status, email/phone verification flags, and account creation/update dates. Ten complete records are directly visible in the sample, with email addresses, Egyptian and international phone numbers, full names and plaintext passwords tied to accounts created on January 28, 2026. The consistency of the schema with a real-estate classifieds platform and the presence of unhashed passwords in the sample support a high confidence level regarding the authenticity of this leak, although the total claimed volume of 185,024 rows could not be independently verified beyond the observed sample. The exposure of plaintext passwords, combined with user contact details and identity, creates a high risk of account takeover, password reuse across other services and targeted phishing. AFRINTEL does not reproduce any name, email address, phone number or password from the reviewed sample.


- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The analysed forum post originated on 28 January 2026 and was identified later. Ten visible rows do not verify the claimed 185,024 records; plaintext passwords, if authentic, warrant account-reset and password-reuse controls.

#### 🇬🇳 Guinea - Ministry of Health (sante.gov.gn)
- **Initial publication date:** March 31, 2026


- **Actor / Group:** Keymous
- **Sector:** Government / Public Health
- **Website:** [sante.gov.gn](https://sante.gov.gn/)
- **Date of incident:** July 2025 (observed activity, identified in March 2026)
- **Status:** Under Investigation
- **Incident type:** Data Leak
- **Victim description:** The official website of Guinea’s Ministry of Health is directly linked to compromised internal systems, including DHIS2 dashboards exposed by Keymous. The correlation between access to health surveillance tools, leaked government data (emails, staff records), and ministerial infrastructure strongly suggests a broader compromise of the ministry’s digital ecosystem. This exposure may enable targeted attacks, data manipulation, and influence operations.

- **AFRINTEL CTI follow-up (analytical review, 2026-11-06) :** The observed activity is attributed to July 2025, while AFRINTEL identified it in March 2026. Alleged DHIS2 dashboard exposure does not establish tampering with public-health indicators or persistent access; validate access permissions, audit logs and indicator integrity.

