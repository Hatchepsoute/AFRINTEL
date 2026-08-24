[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# African victims - February 2025

👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

**10 documented cyber incidents** under AFRINTEL Taxonomy v2: Ransomware 8, Account Takeover 2.

> Public-source links are added to supplementary incidents identified through online research to complete the corpus. They are not retroactively imposed on historical AFRINTEL records, including Dark Web observations.

## February 2025

### 03 February 2025
#### 🇪🇬 Egypt - Xlab Group
- **Ransomware Group:** fog
- **Sector:** Business Services / Technology Consulting (IT & Digital Solutions)
- **Website:** https://xlab-group.com/
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Xlab Group is an Egyptian company specializing in digital marketing solutions, software development, brand strategy consulting, and digital transformation for Middle Eastern companies.

### 06 February 2025
#### Kenya - K24 TV
- **Actor / Group:** Unknown
- **Sector:** Media / Entertainment
- **Website:** https://k24.digital/
- **Incident date:** Around 6 February 2025 - date reported by public media
- **Initial publication date:** 6 February 2025
- **Status:** Victim Confirmed
- **Incident type:** Account Takeover
- **Subtype:** Compromised X account / cryptocurrency fraud
- **Confidence level:** High
- **Impact level:** Level 3
- **Source type:** Victim Confirmation + Public Media
- **Analysis:** K24 TV's X account was hijacked, transformed into a Beyoncé fan page and used for fraudulent cryptocurrency posts. No reliable technical attribution was established.
- **Sources:** [Source](https://www.standardmedia.co.ke/amp/business/newsbeat-tech/article/2001511149/concern-as-k24-x-account-hacked-turned-into-beyonce-fan-page-days-after-kbc-breach)

### 09 February 2025
#### Kenya - Directorate of Criminal Investigations (DCI)
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** https://www.dci.go.ke/
- **Incident date:** 9 February 2025 - incident acknowledged by DCI in its statement that day
- **Initial publication date:** 9 February 2025 - DCI statement; cited media article published 10 February 2025
- **Status:** Victim Confirmed
- **Incident type:** Account Takeover
- **Subtype:** Compromised X / Facebook accounts
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Source type:** Victim Statement + Public Media
- **Analysis:** DCI warned that its official X and Facebook accounts had been compromised and used to distribute fraudulent cryptocurrency content. The event is limited to the confirmed social-media assets unless broader compromise evidence emerges.
- **Sources:** [Nairobi Leo - DCI statement of 9 February reported on 10 February](https://nairobileo.co.ke/news/article/19211/dci-cautions-kenyans-after-being-hacked-on-x-and-facebook)

### 12 February 2025
#### 🇲🇦 Morocco - ASK Gras Savoye (askgs.ma)
- **Ransomware Group:** ransomhub
- **Sector:** Insurance / Brokerage
- **Website:** askgs.ma
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** ASK Gras Savoye is one of the leading insurance brokers in Morocco.

### 12 February 2025
#### 🇿🇦 South Africa - South African Weather Service (SAWS)
- **Ransomware Group:** ransomhub
- **Sector:** Public Services / Environment (Meteorology)
- **Website:** weathersa.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** The South African Weather Service (SAWS) is South Africa's national meteorological service, providing weather forecasts and warnings.

### 19 February 2025
#### 🇿🇲 Zambia - Government Services Portal (services.gov.zm)
- **Ransomware Group:** flocker
- **Sector:** Government / Digital Public Services
- **Website:** http://services.gov.zm/
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim Description:** The services.gov.zm portal is the central platform of the Zambian government (Smart Zambia Institute). It brings together over 322 online services, ranging from visa and permit applications to tax and administrative services for citizens and businesses.
- **Analysis:** AFRINTEL opened and inspected (without reproducing) a large set of files attributed to the claim, corresponding to a full profile export from a Windows host named GSB, harvested under the Administrator account by a collection tool whose output is consistently labelled "_throne_" across three distinct, timestamped collection runs spanning roughly 13 hours (evening of 10 February to mid-morning of 11 February 2025), indicating repeated or persistent tool execution rather than a single pass. The material is packaged into 44 archive parts of 1.7-52 MB each (consistent with exfiltration chunked to a size-capped channel) and totals roughly 1.6 GB. Verified contents include: Chrome and Firefox browser artifacts (autofill databases, session stores, site-security state, the Firefox NSS key database, and a 45 MB browser disk-cache container found on inspection to hold cached Microsoft 365/SharePoint/OneDrive/Akamai CDN HTTP traffic); Windows DPAPI protection blobs and certificate/private-key material tied to the Administrator's Windows security identifier; an RDP connection file whose target field, on inspection, resolves to an internal (RFC1918) address; a Firefox history database whose limited browsing activity, on inspection, includes a second distinct internal address; an empty, unused dial-up/VPN phonebook file; and Visual Studio 2017 project backups. One recovered SQL file contains a query against the `ASPStateTempSessions` table together with an internal support note referencing a system named "ZIGS", indicating an ASP.NET application backed by Microsoft SQL Server and consistent with genuine administrative access to the portal's operating environment rather than a superficial claim; a separate file is the well-known public Ola Hallengren SQL Server maintenance script, confirming SQL Server as the database engine. The set also includes an Office 365 tenant user list: on inspection, all 89 listed accounts are licensed (Microsoft 365 E3), 85 under the domain dotgovsolutions.net, 3 under the tenant's default onmicrosoft.com domain, and 1 under an unrelated external domain (a guest/foreign account within the same tenant) - indicating the portal's Microsoft 365 tenant is operated by a third-party IT services provider, with at least one additional external party granted access. A 10-byte password file was present but not opened by AFRINTEL. No Chrome or Firefox saved-password database was found in the reviewed set. The scale, internal consistency, multiple collection runs, and presence of DPAPI/certificate material, internal-network addresses and RDP artifacts support a high confidence assessment of a genuine administrator-level endpoint compromise, independent of the ransomware group's public claim; this differs materially from the actor's framing as a straightforward "1.2 GB data leak", since the reviewed material is predominantly system, credential-adjacent and internal-network artifacts rather than citizen records. AFRINTEL does not reproduce any credentials, certificates, session data, account names, IP addresses or file content from the reviewed sample.

### 19 February 2025
#### 🇬🇭 Ghana - Brolly
- **Ransomware Group:** killsec
- **Sector:** Insurance / Insurtech
- **Website:** brolly.africa
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim Description:** Brolly is a Ghanaian insurtech startup offering flexible and affordable car insurance solutions (pay-as-you-go model). It allows drivers to spread their insurance payments weekly or monthly via a digital platform.
- **Analysis:** AFRINTEL reviewed the provided KillSec proof without reproducing personal data. The directory contains 4 CSV policy exports with 183 data rows in total, 77 PDF documents and approximately 10.4 MB of material. The CSV structure is consistent with Brolly's vehicle-insurance operations and includes policy/customer fields, coverage type, insurer and vehicle attributes, policy dates, premiums and registration-related fields. The PDFs comprise 50 car-insurance instalment agreements, 25 loan agreements and 2 motor-insurance policy schedules. File names indicate policy-export periods covering August to October 2024, while the documents include agreements generated during October-November 2024; these are evidence dates, not a confirmed intrusion or publication date. The sample contains personal, contact, insurance and vehicle-related information with potential risks of targeted phishing, identity fraud, insurance fraud and social engineering. The observed material supports a medium-to-high confidence assessment that the sample is thematically and structurally consistent with Brolly data, but AFRINTEL has not independently confirmed the intrusion, the full scope of access or the completeness of the dataset. The group KillSec is the claimed actor; no independent attribution beyond the observed ransomware publication is established. AFRINTEL does not reproduce names, phone numbers, registration numbers, chassis numbers, policy identifiers or other raw personal data.

### 21 February 2025
#### 🇳🇦 Namibia - Paratus
- **Ransomware Group:** akira
- **Sector:** Telecommunications
- **Website:** www.paratus.africa
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Pan-African telecommunications operator, investing in network infrastructure across Africa.

### 22 February 2025
#### 🇪🇬 Egypt - SPEED Co
- **Ransomware Group:** hunter
- **Sector:** Logistics / Distribution
- **Website:** speed-com.eg
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** SPEED Co (Speed Ahmed Hassan) is one of the largest logistics and distribution service providers in Egypt. The company manages storage and transportation of Fast-Moving Consumer Goods (FMCG) for major multinationals and local brands, relying on a vast fleet of vehicles and automated distribution centers. The group claims to have extracted a volume of 444.8 GB of data, comprising 285,891 files; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 23 February 2025
#### 🇪🇬 Egypt - Shaghalni
- **Ransomware Group:** killsec
- **Sector:** Services / Recruitment (HR Tech)
- **Website:** shaghalni.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** Shaghalni is one of the leading recruitment platforms in Egypt, specializing in connecting job seekers (notably technical and blue-collar profiles) with companies.
- **Analysis:** The KillSec leak-site listing for Shaghalni offers the data for sale at €5,000, accompanied by a local sample of documents referenced by the listing. The leak-site description matches Shaghalni's publicly known profile as a free Egyptian online job-search platform connecting candidates with employers. The reviewed sample includes an employer-accounts CSV export listing companies registered on the platform (company name, phone number, registration date, country, sector, company size, website and profile text), predominantly Egyptian businesses, and a set of company verification documents uploaded by employers, including Egyptian national ID cards, Egyptian Tax Authority correspondence and registration certificates, an Egyptian Ministry of Tourism company license, and a Saudi Arabia Ministry of Commerce and Investment company registration certificate, indicating the platform's employer base extends beyond Egypt. The documents are internally consistent with Shaghalni's stated activity as an employer-facing recruitment platform. AFRINTEL does not reproduce any national ID numbers, company registration numbers, tax references, phone numbers or names from the reviewed sample. The reviewed material pertains to employer/company accounts and their verification documents; it does not establish whether job-seeker/candidate personal data was also part of the claimed dataset.

---
