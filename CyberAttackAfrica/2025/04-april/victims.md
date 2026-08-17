[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# List of African cyberattack victims in April 2025 (17 victims)
[**French version available here**](./victims_FR.md)
## April 2025

### 04 April 2025
#### 🇸🇳 Senegal - Senegalese Armed Forces (armee.sn)
- **Incident type:** Access Sale
- **Actor / Group:** oblivion666
- **Sector:** Defense / National Security
- **Website:** armee.sn (Army.sn, Sigrh.armee.sn, Srvmail.armee.sn, Spami.armee.sn)
- **Status:** Claim - Unverified
- **Victim Description:** armee.sn is the domain infrastructure of the Senegalese armed forces, covering several administrative and internal-service subdomains (Army.sn, Sigrh.armee.sn, Srvmail.armee.sn, Spami.armee.sn).
- **Analysis:** The actor oblivion666 offers the above domains for sale in a forum post, together with claimed administrator-level access to associated servers and a firewall, timed around the Senegalese independence period. No file, credential or other technical evidence accompanies the post; the listing is a bare access-sale advertisement without an accessible sample. Whether the claimed access is genuine, current or still available cannot be verified. Given the target (national defense infrastructure), a confirmed compromise would carry a high potential impact, but this remains an unverified claim pending independent evidence.

### 06 April 2025
#### 🇪🇬 Egypt - IACC Holdings
- **Ransomware Group:** dragonforce
- **Sector:** Finance / Logistics
- **Website:** www.iacc.holdings
- **Status:** Claim - Unverified
- **Victim Description:** Egyptian private investment holding company focused on maritime transport and logistics. 27.75 GB of data exfiltrated.

### 07 April 2025
#### 🇿🇦 South Africa - Cell C
- **Ransomware Group:** ransomhouse
- **Sector:** Technology (Telecommunications)
- **Website:** cellc.co.za
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 4
- **Analysis:** AFRINTEL reviewed 20 screenshots from the RansomHouse publication. The evidence covers Cell C customer and employee information, passport material, call records, SMS data, international voice activity, customer contracts, franchise records, confidential NDAs, internal documents and a revenue summary. This breadth is consistent with a material telecommunications data exposure. Potential impacts include subscriber privacy loss, targeted phishing and fraud, employee targeting, exposure of call and messaging metadata, commercial espionage and operational reconnaissance. The screenshots do not independently establish the initial access vector, dataset completeness, affected subscriber count or operational impact. AFRINTEL does not reproduce personal records, passport details, phone numbers, contracts or download links.
- **Victim Description:** South African telecommunications operator, one of the country's leading mobile service providers.

### 08 April 2025
#### 🇪🇬 Egypt - International Business Service
- **Ransomware Group:** crypto24
- **Sector:** Business Services / Outsourcing (BPO)
- **Website:** ibsns.com
- **Status:** Claim - Unverified
- **Victim Description:** International Business Service (IBS) is one of the largest outsourcing service providers in Egypt. The company specializes in human resources management, mass recruitment, payroll outsourcing, and maintenance/logistics services for large companies and multinationals operating in Egypt.

### 08 April 2025
#### 🇲🇦 Morocco - CNSS (Caisse Nationale de Sécurité Sociale)
- **Incident type:** Data Leak
- **Actor / Group:** Jabaroot DZ
- **Sector:** Public Administrations (Social Security)
- **Website:** www.cnss.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** National Social Security Fund of Morocco.
- **Analysis:** AFRINTEL reviewed two large structured exports matching CNSS's core databases, dated to the same day as the claim. The first, an employer/affiliate table, contains approximately 1,094,000 records with fields including company name, affiliate number, affiliation dates, employer type, telepayment method, agency and regional office, along with the administrator's first name, last name, national ID number (CIN), email address and phone number, plus banking details (account ID, bank code) linked to the employer. The second, an insured-persons table, contains approximately 1,996,000 records with fields including first name, last name, national ID number (CIN), passport number, residence-permit number, an internal registration/immatriculation number, creation date, application channel and the affiliated employer's name. The scale and structure of both tables are consistent with a genuine, near-complete extract of CNSS's national employer and insured-persons registries. The combination of national ID numbers, contact details and employer affiliations for close to two million individuals and over one million employers represents a very high-impact exposure, creating substantial risk of identity fraud, social-engineering campaigns and targeted phishing at national scale. AFRINTEL does not reproduce any names, national ID numbers, contact details or banking references from the reviewed sample.

### 08 April 2025
#### 🇲🇦 Morocco - Ministry of Industry and Commerce (miepeec.gov.ma)
- **Incident type:** Data Leak
- **Actor / Group:** Jabaroot DZ
- **Sector:** Government / Economy and Industry
- **Website:** miepeec.gov.ma
- **Status:** Claim - Unverified
- **Victim Description:** The MIEPEEC is the Moroccan government body responsible for steering industrial strategy, promoting investment, and regulating trade. It manages critical platforms for interaction between the state and the private sector.

### 08 April 2025
#### 🇩🇿 Algeria - CNAS (Caisse Nationale des Assurances Sociales des Travailleurs Salariés)
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Government / Social Security
- **Website:** [cnas.dz](https://www.cnas.dz)
- **Status:** Claim - Data Sample Published
- **Victim Description:** CNAS is the Algerian public body managing health insurance and in-kind social benefits for salaried workers, through a nationwide network of agencies and payment centers.
- **Analysis:** On April 8, 2025, Phantom Atlas published a claim presented as a direct response to recent cyberattacks targeting the actor, stating it had carried out a full intrusion into CNAS's databases and extracted more than 860,200 documents. The post adds broader accusations of opaque financial and logistical routes involving Algerian companies and Dubai, said to be revealed in a future release; these accusations are not documented in the material reviewed by AFRINTEL and are reported here only as the actor's stated narrative, without validation.

  AFRINTEL reviewed a local sample of 214 image files (approximately 97 MB) associated with this claim. The sample is homogeneous and corresponds to "Attestations d'ouverture des droits aux prestations en nature" (certificates opening entitlement to in-kind benefits) issued by several CNAS agencies (notably Tizi Ouzou/Boghni and Algiers/Belcourt), mostly dated between 2022 and 2024. Each document contains the full identity of the insured member (name, first name, date of birth, address, social security registration number, affiliation center) as well as that of the covered person (insured member, spouse, child or ascendant), the coverage rate, the issuance date, the name of the issuing agent, a stamp and a signature.

  The consistency of the format across the sample, the diversity of agencies and payment centers represented, and the presence of plausible stamps and signatures support a high confidence level regarding authentic access to CNAS systems or archives. The observed volume (214 documents), however, remains far below the 860,200 claimed and does not confirm the total announced scale of the leak. Exposure of these certificates could facilitate identity theft, social-benefit fraud and targeted phishing against insured members and their dependents. AFRINTEL does not reproduce any name, date of birth, address, registration number or other personal data from the reviewed documents.

### 09 April 2025
#### 🇩🇿 Algeria - MGPTT / Mutuelle Générale des Travailleurs de la Poste et des Télécoms
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Social / Health Insurance Fund
- **Website:** mgptt.dz
- **Status:** Claim - Data Sample Published
- **Victim Description:** The MGPTT is a major social institution in Algeria, covering employees in the Postal, Telecommunications, and Information sectors. It manages healthcare reimbursements and social benefits for tens of thousands of civil servants and contractors. The publication claims more than 13 GB of internal MGPTT data, including personal data and strategic documents/databases, and also references sensitive Ministry of Labor files.
- **Analysis:** Phantom Atlas's post is accompanied by a message framing the operation as a direct response to an earlier claimed breach of CNSS, and adopts an explicitly hacktivist tone tied to the Western Sahara territorial dispute between Morocco and Algeria; this political framing is reported by AFRINTEL as stated, without validating or taking a position on the territorial claims or the mutual hacking accusations.

  AFRINTEL reviewed a sample of 4 images (approximately 496 KB in total) associated with this post. The images show photographed or scanned identity and social-protection documents: Algerian social security insured-member cards, an MGPTT retiree membership card, a CNAS affiliation certificate, and a postal payment receipt together with a hospital admission certificate from a private clinic. These documents contain full names, dates of birth, social security registration numbers, addresses and, in some cases, photographs and medical or financial information relating to named individuals.

  The observed volume (four images) is far smaller than the claimed 13 GB and does not corroborate the announced scale of the leak or confirm that this is a representative extract of an internal MGPTT information system. One image also carries the visible watermark of a third-party online document-selling service, suggesting this particular sample may originate, at least in part, from documents already circulating elsewhere rather than from a direct extraction of MGPTT's systems. Taken together, these elements call for a cautious assessment: the presence of real personal and social-insurance data appears established, but the exact origin, completeness and direct link to a compromise of MGPTT's internal systems remain uncertain. AFRINTEL does not reproduce any name, registration number, date of birth, address, photograph or medical/financial detail from the reviewed images.

### 09 April 2025
#### 🇩🇿 Algeria - Ministry of Labor
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Government / Labor Administration
- **Website:** Not specified
- **Source publication date:** April 9, 2025
- **Status:** Claim - Unverified
- **Victim Description:** The supplied publication states that Phantom Atlas accessed sensitive files from Algeria's Ministry of Labor. No ministry-specific sample is provided; this target is therefore recorded separately from MGPTT without independent confirmation of the compromise.
- **Analysis:** The claim appears in the same Phantom Atlas publication as the MGPTT claim and may reflect one operation affecting multiple Algerian public institutions. No ministry-specific dataset was collected or reproduced.

### 13 April 2025
#### 🇲🇷 Mauritania - BMI / SEDAD Mobile Wallet
- **Actor / Group:** Killer_Bee
- **Sector:** Finance / Mobile Payment
- **Website:** [bmi.mr](https://bmi.mr)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Source publication date:** April 13, 2025
- **Observed sample dates:** April 6, 2025

- **Description:**
  The publication claims to expose a database associated with SEDAD, BMI's digital banking and mobile-wallet service in Mauritania. The post claims more than 90,000 records involving wallet complaints and administrative actions.

- **Analysis:**
  The visible sample is a structured JSON record from a customer-complaints workflow. It contains customer identity fields, a national identification number, a phone number, internal user attribution, creation and update timestamps, treatment status and an activation-related complaint type. AFRINTEL does not reproduce the personal values shown in the sample. The sample supports the presence of sensitive structured data, but the claimed database size, completeness, origin and compromise are not independently confirmed. The official BMI website identifies SEDAD as BMI's digital banking and electronic-wallet service.

- **Recommendations:**
  1. Verify the claim against SEDAD application, database, API and administrator audit logs, preserve evidence and determine whether customer identity and phone data were accessed.
  2. Rotate exposed administrative credentials or tokens if required, review privileged actions, enforce MFA, monitor account-takeover and phishing attempts, and notify affected users and authorities according to applicable requirements if the exposure is confirmed.

### 13 April 2025
#### 🇪🇬 Egypt - Tawasol
- **Ransomware Group:** devman
- **Sector:** Information Technology
- **Website:** tawasol-it.com
- **Status:** Claim - Unverified
- **Victim Description:** A technology solutions integrator based in Cairo that installs security and network infrastructure systems for businesses and smart buildings.

### 13 April 2025
#### 🇲🇦 Morocco - Higher Institute of Audiovisual and Cinema Professions (ISMAC)
- **Incident type:** Data Leak
- **Actor / Group:** p4xar
- **Sector:** Education / Higher Education / Audiovisual and Cinema
- **Website:** [ismac.ma](https://ismac.ma)
- **Status:** Claim - Data Sample Published

- **Description:**
  The Higher Institute of Audiovisual and Cinema Professions (ISMAC) is a Moroccan public higher education institution in Rabat. It trains professionals in cinema, audiovisual production, directing, production management, image and sound, under the supervision of the Moroccan Ministry of Youth, Culture and Communication.

- **Analysis:**
  A forum post attributed to p4xar claims that the application hosted at `sul.ismac.ac.ma/app/` was compromised and that a file named `db.sql`, presented as the complete database, was distributed free of charge through a Telegram channel. The visible sample is a substantial SQL export of the `n_etudiants` table, with syntax and structure compatible with MySQL or MariaDB. It contains student personal data, including identity-document fields, birth details, postal addresses, email addresses, telephone numbers, nationality references, student status and user-account identifiers. The combination of these data could facilitate identity fraud, targeted phishing, social engineering, document fraud and abusive account-recovery attempts. Some records contain null or incomplete fields and encoding anomalies. The sample supports the presence of sensitive structured data, but does not establish the total volume, record count, completeness of the distributed file or independent confirmation of the claimed compromise.

### 13 April 2025
#### 🇲🇦 Morocco - Ministry of Housing and Urban Policy (mhpv.gov.ma)
- **Incident type:** Data Leak
- **Actor / Group:** B4baYega
- **Sector:** Government / Housing / Urban Policy
- **Website:** mhpv.gov.ma
- **Status:** Claim - Unverified
- **Victim Description:** The Ministry of Housing and Urban Policy (Ministère de l'Habitat et de la Politique de la Ville) is the Moroccan government body responsible for housing policy and urban development.
- **Analysis:** AFRINTEL identified a password-protected archive bearing an internal archive comment explicitly attributed to the actor B4baYega, referencing a Telegram contact channel for further "fresh and private" databases. The archive's accessible content was limited to a single small image file; AFRINTEL could not access or verify the claimed underlying dataset due to the password protection, and therefore cannot confirm its content, volume or authenticity. This entry is recorded as an unverified claim pending further evidence.

### 17 April 2025
#### 🇪🇬 Egypt - INI Investments
- **Incident type:** Data Leak
- **Actor / Group:** nightspire
- **Sector:** Financial Services / Investment Banking / Project Finance Advisory
- **Website:** Not identified with sufficient confidence
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 2
- **Victim Description:** INI Investments is an Egyptian investment banking and project-finance advisory firm based in Cairo, involved in feasibility studies, financial structuring and closures for industrial and infrastructure projects.
- **Analysis:** AFRINTEL reviewed a local sample of documents consistent with the claim made by the threat actor nightspire, including internal financial feasibility models (multi-year IRR projections ranging from 39% to 58%, capital-structure and financing-source breakdowns) for a UPVC pipe-manufacturing project, a competitor market study comparing production volumes and market share of several named Egyptian UPVC manufacturers, a project-pipeline tracker titled "Pipe line projects for Allweiler Farid Hassanein Pumps co" listing multiple client deals with project values in EGP, USD and EUR, status and bidding dates (referencing clients and projects in Egypt, Russia and Saudi Arabia), a legal study and meeting minutes, a land-assessment report for a named company's UPVC project site, and a document referencing an order extension for Hassan Allam, a major Egyptian construction and engineering group. The file metadata places the evidence between 15 and 17 April 2025; this is treated as an evidence/discovery date, not a confirmed publication date. The internal consistency of the financial models, the naming of real Egyptian industrial counterparts (Allweiler Farid Hassanein Pumps, Hassan Allam) and the coherence between the feasibility study, market study and legal documentation support a high confidence assessment of a genuine compromise of INI Investments' internal project files. The exposed material consists of confidential deal, financing and market-intelligence data rather than personal or consumer records, creating a risk of competitive intelligence exposure, business email compromise and targeted social engineering against INI Investments and its industrial clients and counterparties. AFRINTEL does not reproduce any client name, project value, financial figure or document reference from the reviewed material.
- **Double-claim note:** The March and April records are retained separately because the source dates and evidence differ. They involve the same actor, domain and victim name, but AFRINTEL cannot determine from the available material whether the April publication is an update of the March claim or a separate claim. No merger is made pending confirmation.
### 20 April 2025
#### 🇿🇦 South Africa - Premier Meats South Africa
- **Ransomware Group:** devman
- **Sector:** Agribusiness
- **Website:** premiermeats.co.za
- **Status:** Claim - Unverified
- **Victim Description:** Premier Meats is a South African company specializing in the processing and distribution of quality meats.

### 22 April 2025
#### 🇹🇳 Tunisia - Natilait
- **Ransomware Group:** cicada3301
- **Sector:** Agribusiness / Dairy Industry
- **Website:** natilait.com.tn
- **Status:** Claim - Data Sample Published
- **Victim Description:** Natilait is a major player in the Tunisian agrifood sector, specializing in the production and marketing of milk (UHT), yogurt, and derived products.
- **Analysis:** The 12 supplied JPG/PNG images include at least one structured internal product and stock table with item codes, dairy-product descriptions, quantities and inventory or stock fields; the other images appear related to operational business records, although several are not sufficiently legible for reliable extraction. The material is consistent with a data sample from Natilait manufacturing or distribution operations and could support competitive intelligence, document fraud or supply-chain targeting. The intrusion vector, the complete dataset scope and whether the images were produced by cicada3301 are not independently established. No product records or commercial values are reproduced.

### 23 April 2025
#### 🇪🇬 Egypt - Dar Al Teb
- **Ransomware Group:** gunra
- **Sector:** Healthcare
- **Website:** daralteb.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Dar Al Teb is one of Egypt's most renowned medical centers, specializing in reproductive medicine, in vitro fertilization (IVF), and women's health.
- **Analysis:** The gunra ransomware group claims the compromise of Dar Al Teb (daralteb.com) and displays data samples on its leak-site page. The samples show patient/cycle tracking tables including husband name, wife name, file number, age, two phone numbers, and IVF-specific clinical fields (fresh/frozen semen status, expected oocyte/embryo counts, referring andrologist, referring doctor, and embryology outcome codes). A broader local set includes seven monthly workbooks (December 2022, then March through August 2023) totaling approximately 2,300 rows of patient/cycle records, plus two shorter additional workbooks and an Access database (not opened). The reviewed technical material includes a WLAN profile export containing a cleartext pre-shared key, associated network commands referencing an internal file share, a PowerShell script for deploying an Active Directory forest named "DarAlteb.local", and a preconfigured RDP connection file targeting an internal host with clipboard and smart-card redirection enabled. The combination of individually identifiable clinical data samples, a multi-year patient dataset and internal network/remote-access configuration material supports a high confidence assessment of a genuine, extensive compromise extending beyond a simple leak-site claim. The nature of the observed data, both individually identifiable reproductive-health information covering several thousand patients and internal infrastructure access material, supports a Level 4 impact rating. AFRINTEL does not reproduce any patient name, phone number, file number, Wi-Fi key, IP address or other personal data or secret from the reviewed material.
## ✍🏿 Author
*Adama ASSIONGBON*  
*SOC & Cyber Threat Intelligence Consultant*  
[LinkedIn profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)

---
*AFRINTEL - Open CTI Monitoring Initiative on Africa*
