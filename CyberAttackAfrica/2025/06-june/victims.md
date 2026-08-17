[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# List of African cyberattack victims in June 2025 (21 victims)
👉🏾 [**French version available here**](./victims_FR.md)

## June 2025

### 02 June 2025
#### 🇲🇦 Morocco - ANCFCC (Agence Nationale de la Conservation Foncière)
- **Incident type:** Data Leak
- **Actor / Group:** nightspire
- **Sector:** Government / Real Estate and Land Registry.
- **Website:** https://www.ancfcc.gov.ma/
- **Status:** Claim - Data Sample Published
- **Victim Description:** The ANCFCC is the vital body responsible for land registration, cadastre, and cartography in Morocco. NightSpire's original claim cited a 3.1 GB leak comprising over 10,080 property certificates.
  A forum post attributed to vyngrich advertised several collections presented as originating from ANCFCC: more than 10,000 sample property certificates, a claimed underlying set exceeding 10 million certificates, and 20,000 sample documents from a collection allegedly exceeding 4 million documents and 4 TB. The claimed categories included property deeds, civil-status records, identity documents, passports and banking documents, as well as a folder allegedly concerning senior officials and public figures. AFRINTEL does not reproduce identities. AFRINTEL subsequently obtained and reviewed local archive copies of the claimed release, confirming the presence of several thousand individual property-certificate PDF files, sequentially named (e.g. CERTIFICAT_1.pdf through numbers in the thousands), consistent with the claimed sample size, together with a separately labelled folder referencing senior officials and public figures; AFRINTEL did not open or analyse the contents of that folder and does not reproduce any identities from it. The proximity between the more-than-10,000 certificate sample and NightSpire’s 10,080 certificates suggests possible overlap, republication, resale or amplification. The July post is retained as supplementary reporting and is not counted as a separate incident. The authenticity, age, completeness and technical origin of the additional claimed collections remain unknown.

### 02 June 2025
#### 🇲🇦 Morocco - Bar Association Portal (avocatsmaroc.com / mossaada.ma)
- **Incident type:** Data Leak
- **Actor / Group:** B4baYega
- **Sector:** Legal Services / Professional Association
- **Website:** avocatsmaroc.com / mossaada.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** avocatsmaroc.com is a Moroccan legal-profession portal supporting lawyers' case and enforcement-procedure management; mossaada.ma is an associated legal-aid platform.
- **Analysis:** AFRINTEL reviewed application source code and SQL database backups referencing the domains bureau.avocatsmaroc.com and app2.mossaada.ma, distributed by the actor B4baYega alongside a password-protected archive. The application's PHP source files use Arabic-transliterated function and field names consistent with judicial case-management and enforcement terminology (e.g. "Tanfid"/enforcement, "Khazina"/treasury or fund, "Tabligh"/notification, "Diligence", "Tribunal"), together with client-search, client-record-modification and diligence-tracking functions, and multiple dated SQL backup files. This indicates a compromise of a legal case-management application used by or for Moroccan lawyers, rather than a simple static website. AFRINTEL did not extract or review the SQL backups' row-level content and does not reproduce any client names, case references or other personal data from the reviewed sample. The scope and volume of records actually contained in the backups could not be independently confirmed.

### 06 June 2025
#### 🇲🇦 Morocco - MTT EXPERTISES
- **Ransomware Group:** incransom
- **Sector:** Business Services
- **Website:** https://mttexpertises.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** MTT Expertises is a multidisciplinary engineering and expertise firm based in Casablanca (with offices in Agadir and Tangier).
- **Analysis:** AFRINTEL reviewed a small local sample of documents consistent with the claim made by the threat actor incransom, including an unredacted client cheque issued by a Casablanca-based company and made payable through Crédit du Maroc, showing a full bank account number, a banking attestation issued by Crédit du Maroc confirming an account held by MTT Expertise, a client invoice referencing an agri-food company (Quality Tomatos Morocco) with its bank account details, and an industrial-site floor plan ("Plan de masse") bearing the MTT Expertises logo, consistent with an asset-valuation and insurance-loss-assessment engagement. The presence of genuine banking instruments and site-survey documentation tied to distinct third-party clients, together with MTT Expertises' own banking attestation, supports a medium confidence assessment of an actual compromise of the firm's internal files. The exposure of client and firm banking details creates a risk of payment fraud and business email compromise against MTT Expertises and its corporate clients. AFRINTEL does not reproduce any bank account number, cheque number or client name from the reviewed sample.

### 06 June 2025
#### 🇿🇦 South Africa - Ingonyama Trust Board
- **Ransomware Group:** nightspire
- **Sector:** Land Administration / Public Sector.
- **Website:** ingonyamatrust.org.za
- **Status:** Claim - Unverified
- **Victim Description:** The Ingonyama Trust Board (ITB) is a South African administrative authority responsible for managing approximately 2.8 million hectares of communal land in KwaZulu-Natal province.

### 06 June 2025
#### 🇲🇦 Morocco - Best Profil (bestprofil.ma)
- **Ransomware Group:** lynx
- **Sector:** Human Resources / Recruitment / Temporary Work.
- **Website:** https://bestprofil.ma
- **Status:** Data Fully Published
- **Victim Description:** Best Profil is one of the leaders in recruitment and temporary work in Morocco. The Lynx group describes this as a total exfiltration of 26 GB, now freely accessible on its leak site after ransom negotiations reportedly failed.
- **Analysis:** AFRINTEL reviewed a local sample of the leaked material, consisting of internal administrative and operational documents referencing "PEGASE" (an internal system/tool), staff attendance and payroll-tracking spreadsheets, invoice-verification and billing-detail files, and a client-complaint record for an industrial site. The presence of internal system manuals, payroll and timekeeping data and site-level administrative correspondence is consistent with a genuine internal-systems compromise rather than a superficial claim. The exposure of staff attendance, payroll and billing records creates a risk of payroll fraud, business-email compromise and social engineering against Best Profil's staff and corporate clients. AFRINTEL does not reproduce any employee names, client names or financial figures from the reviewed sample.

### 08 June 2025
#### 🇩🇿 Algeria - Crédit Populaire d'Algérie (cpa-bank.dz)
- **Incident type:** Data Leak
- **Actor / Group:** TajineSec / Tajinesec_MA (publication claim)
- **Sector:** Banking / Financial Services.
- **Website:** https://cpa-bank.dz
- **Status:** Claim - Unverified
- **Victim Description:** Crédit Populaire d'Algérie (CPA) is one of the country's main public banks. TajineSec claims to have exfiltrated more than 30 GB, including identity documents, employee and customer information, banking and money-transfer records, and internal administrative documents. A 500 MB sample is announced but is not visible in the supplied evidence.
- **Analysis:** The publication documents a public claim attributed to TajineSec / Tajinesec_MA and describes potentially highly sensitive banking and identity data. The compromise, the claimed volume, the alleged Moroccan attribution, and the publication of the announced sample are not independently verified. The status therefore remains **Claim - Unverified**.

### 09 June 2025
#### 🇩🇿 Algeria - Algérie Télécom (algerietelecom.dz)
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Telecommunications / National Internet Infrastructure
- **Website:** [algerietelecom.dz](https://www.algerietelecom.dz)
- **Status:** Claim - Data Sample Published
- **Victim Description:** Algérie Télécom is the incumbent operator and main provider of fixed internet and fixed telephony access in Algeria, operating the national network infrastructure linking regional access points to international content servers.
- **Analysis:** Phantom Atlas claims full access to Algérie Télécom's internal internet network map for the Tizi Ouzou, Boumerdes and Bouira provinces, stating it holds detailed information on the critical infrastructure connecting access points (BNG) to global content servers (FNA, GGC), as well as core routers, content distribution rings and per-municipality data consumption.

  The reviewed material shows interfaces of a "Network Weathermap"-type network monitoring tool, displaying several distinct topology maps: a diagram of the Tizi Ouzou BNG project with identified routers (PE-01, PE-02, ASBR-01, ASBR-02) and peering links to Google (GGC) and Facebook (FNA) with traffic loads in Gbit/s; a regional metro-loop diagram naming dozens of sites and municipalities across the provinces concerned; and a detailed bandwidth-consumption table by municipality for Tizi Ouzou, Boumerdes and Bouira. A second message states that access had been maintained since at least May 28, 2025 (noting a connection drop during a test on that date) and claims to hold data going beyond simple maps.

  The technical consistency of the observed interfaces (a real network monitoring tool, plausible equipment and site designations, traffic figures consistent across the different views) supports a high confidence level regarding authentic access to an internal Algérie Télécom monitoring system, at least for the provinces mentioned. The disclosure of detailed network maps of a national telecom operator constitutes a critical exposure that could facilitate targeted infrastructure mapping ahead of further intrusions, denial-of-service attacks against identified links, or service disruption in the affected areas. AFRINTEL does not reproduce any topology detail, equipment identifier or additional traffic figure beyond what is necessary to characterize the nature of the exposure.

### 09 June 2025
#### 🇬🇭 Ghana - Priority Insurance Company Limited
- **Incident type:** Data Leak
- **Actor / Group:** 0x0day, post published on the cybercriminal forum DarkForums
- **Sector:** Insurance / Financial Services
- **Website:** priorityinsuranceghana.net
- **Status:** Claim - Data Sample Published
- **Victim Description:** Priority Insurance Company Limited is a Ghanaian non-life insurance company headquartered in Accra, licensed by the National Insurance Commission (NIC) and operating a network of more than 30 branches across the country, including Accra, Kumasi, Tema, Cape Coast and Ho.
- **Analysis:** AFRINTEL identified the originating post, titled "GHANA Inusrance database", published on the cybercriminal forum DarkForums by the account 0x0day on 9 June 2025, superseding an earlier under-investigation record that had provisionally placed this dataset in February 2025 based only on a file-modification timestamp with no located source post. The post displays a JSON sample record consistent with an internal policy-management export, with fields including a customer ID, policy number, branch ID and branch name (Tema), customer type, full name, email, phone number, digital/postal/residential address, tax identification number, company ID and company name (explicitly "Priority Insurance Company Limited"), and a national ID field. This matches the structure and branch network (Accra, Kumasi, Tema, Cape Coast, Ho, Bolga) of the customer-database file previously reviewed by AFRINTEL, which contained 349,288 records including roughly 159,000 with an email address and roughly 159,000 with a national ID number. The combination of a confirmed source account, an explicit publication date and a sample matching the previously reviewed dataset raises the confidence level from under investigation to a dated, attributed claim. Given the volume of records and the combination of national identity numbers, dates of birth, occupation, contact details and insurance policy association, exposure of this dataset would create a significant risk of identity theft, insurance fraud and targeted phishing against policyholders. AFRINTEL does not reproduce any customer name, phone number, address, national ID number or date of birth from the reviewed material.

### 11 June 2025
#### 🇲🇺 Mauritius - Currimjee Jeewanjee & Co
- **Ransomware Group:** warlock
- **Sector:** Conglomerate / Multi-sectoral
- **Website:** https://www.currimjee.com
- **Status:** Claim - Unverified
- **Victim Description:** One of the oldest and most important conglomerates in Mauritius, operating in telecommunications (Emtel), energy, real estate, tourism, and financial services.

### 11 June 2025
#### 🇩🇿 Algeria - Banque Nationale d'Algérie (bna.dz)
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Banking / Financial Services.
- **Website:** https://bna.dz / https://ebanking.bna.dz
- **Status:** Claim - Unverified
- **Victim Description:** The Banque Nationale d'Algérie (BNA) is the primary commercial bank of the Algerian state. The actor claims a massive exfiltration of 90 GB with a partial publication of 7 GB; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.
- **Analysis:** An earlier Phantom Atlas message, posted on June 10, 2025 on the actor's Telegram channel, provides further detail on this claim: the group states it holds more than 90 GB of documents covering the 2016-2025 period, with a staged release plan ("we will start with 2016 ones"), the archive being protected by the password `phantomatlas`. The download link mentioned on DarkForums is no longer accessible at the time of writing this entry; AFRINTEL was therefore unable to collect or review the claimed archive, and cannot confirm either the completeness or the authenticity of the announced content.

### 11 June 2025
#### 🇿🇦 South Africa - carducci
- **Ransomware Group:** warlock
- **Sector:** Retail (Fashion)
- **Website:** http://carducci.co.za/
- **Status:** Claim - Unverified
- **Victim Description:** Carducci is a South African fashion brand based in Cape Town, founded in 1978. It specializes in elegant menswear, including suits, casual wear, and accessories. The brand is renowned for its craftsmanship and refined fabrics. Carducci is part of the Seardel group.

### 14 June 2025
#### 🇪🇬 Egypt - Ministry of Social Solidarity
- **Incident type:** Data Leak
- **Actor / Group:** Keymous
- **Sector:** Government / Public Administration / Social Affairs
- **Website:** [moss.gov.eg](https://www.moss.gov.eg)
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Ministry of Social Solidarity is an Egyptian government administration responsible for policies and services related to social protection and social affairs.
- **Analysis:** A post attributed to the actor Keymous presents data allegedly obtained from the ministry and involving government and institutional representatives from several countries. The publication advertises confidential documents and personal information relating to ministers, government officials and institutional representatives from several African, Arab and Asian countries, specifically mentioning passports or identity documents, names, phone numbers and email addresses; the actor claims a total of 237 elements, described in the post as "Line and file".

  The CSV sample reviewed by AFRINTEL contains 26 records across 8 columns: `Name`, `Phone`, `Email`, `Title / Position`, `Country`, `City`, `Passport / ID` and `Photos`. The records cover Egypt, Djibouti, Benin, Burkina Faso, Senegal, Morocco, Sudan, Türkiye, the United Arab Emirates, Malaysia, Indonesia and Kuwait, as well as OIC-affiliated organisations. All 26 records contain names, phone numbers, email addresses, professional positions and passport or identity document references, and several positions correspond to government, diplomatic or institutional officials. The `Photos` column also contains the value "Back" for 5 records, although no image is directly embedded in the supplied CSV; several location values are missing or represented by a placeholder, and at least one email address is partially masked.

  The combination of identity information, direct contact details and institutional positions creates a significant risk of spear phishing, identity impersonation, document fraud and targeted social engineering, and the exposed professional roles could help an actor identify high-value individuals and build contextualised campaigns against government entities or partner organisations. The forum post includes a download link presented as the "Full file", but the CSV supplied to AFRINTEL contains only 26 records against the 237 elements claimed; the reviewed material should therefore be treated as an observed sample rather than confirmation that the complete claimed dataset was obtained. No asking price is displayed and the data is not presented as being offered for sale. AFRINTEL does not reproduce any name, phone number, email address, passport/ID reference or other personal data from the reviewed sample.

### 14 June 2025
#### 🇩🇿 Algeria - Ministry of Youth and Sports (MJS) / Directorates of Youth and Sports (DJS)
- **Incident type:** Data Leak
- **Actor / Group:** mrdump, post published on a cybercriminal forum (DarkForums)
- **Sector:** Government / Public Administration / Youth and Sports
- **Website:** [mjs.gov.dz](https://www.mjs.gov.dz)
- **Status:** Data Fully Published
- **Victim Description:** The Ministry of Youth and Sports (MJS) is the Algerian government administration in charge of youth and sports policy, supported by a network of Directorates of Youth and Sports (DJS) in each wilaya. The reviewed documents mostly concern the Boumerdes wilaya directorate, along with correspondence from other wilayas (Illizi, El Meghaier, Tlemcen, Bechar) and the central ministry.
- **Analysis:** The actor mrdump posted a claim on a cybercriminal forum (DarkForums) that the ministry's database had been breached, along with a link to an external Telegram channel presented as the source of the full publication. The post states that "all sensitive files and internal data" of the ministry have been published.

  AFRINTEL directly reviewed the full set of files associated with this post, totaling approximately 730 MB across 772 files (610 PDFs, 109 images, 22 unextracted RAR archives, 20 Excel workbooks, plus a few Word documents, videos and text files). The content consists of authentic-looking internal administrative correspondence: budget monitoring and program execution notes (DIEEP notes, draft settlement bills, payment credit requirements), sports infrastructure inventories (stadiums, pools, multi-purpose gyms), youth holiday and camp programs, inter-wilaya twinning agreements, an information databank listing youth institutions, and a circular addressed to youth and sports directors across several wilayas. Document dates range from around 2014 to early June 2025, with the most recent file predating the June 14, 2025 post by only a few days.

  Two Excel workbooks display an abnormally high row count (roughly 1,047,700 rows each) due to a formatting artifact from an accounting-system export; only about a dozen rows actually contain data in each file, corresponding to budget nomenclature fields (program, sub-program, action, category, spending officer) rather than a massive volume of individual records.

  A standalone text file contains an excerpt from an individual career file of a ministry employee (name, original grade, hiring date), confirming exposure of named HR data in addition to the administrative correspondence. The 22 attached RAR archives were not extracted by AFRINTEL, so their exact contents remain unverified beyond their filenames, which reference activity reports, association-funding case files and partnership-related documents.

  The internal consistency of the corpus (official letterheads, a structure consistent with Algerian public administration, a plausible chronology, and a named employee reference) and its volume support a high confidence level regarding authentic access to internal data of the ministry or one of its decentralized directorates. This exposure could facilitate impersonation of civil servants, targeted phishing against the nationwide network of wilaya directorates, reconstruction of the ministry's internal budget organization, and exploitation of HR career data. AFRINTEL does not reproduce any name, HR data, personal contact detail or document from the reviewed corpus.

### 18 June 2025
#### 🇩🇿 Algeria - Ministry of National Defense (MDN)
- **Incident type:** Data Leak
- **Actor / Group:** mrdump, post published on a cybercriminal forum (DarkForums)
- **Sector:** Defense / National Security
- **Website:** Not specified (internal file, no institutional domain visible)
- **Status:** Claim - Unverified
- **Victim Description:** The Ministry of National Defense (MDN) is the Algerian administration responsible for national defense. The post claims to have obtained classified internal documents related to the ministry's logistics and supply chain operations.
- **Analysis:** The actor mrdump, already behind a post targeting the Ministry of Youth and Sports on June 14, 2025, published a new claim on June 18, 2025, this time concerning the Ministry of National Defense, announcing the acquisition of "classified internal documents" related to logistics and supply chain operations.

  An Excel file titled "جدول اللوجستيك لوزارة الدفاع" ("Ministry of Defense logistics table") was shared with AFRINTEL in connection with this post. Given the claimed nature of the document (material presented as classified, related to national defense), AFRINTEL performed a limited, non-content structural review: the workbook is an XLSX file of approximately 15 KB containing one worksheet, 77 rows and 14 columns; roughly 65 populated rows form a repeated structured table, while the remaining rows are document headings or other non-record content. AFRINTEL did not reproduce or extract names, identifiers, locations, quantities, procurement details or other potentially sensitive values.

  The file structure is consistent with a logistics-related administrative table, but the structural review does not establish that the document is authentic, classified, current, complete or sourced from the Ministry of National Defense. The claim therefore remains recorded as unverified. If the claimed provenance were confirmed, exposure of military logistics or supply-chain information could create a high national-security risk; this is a conditional impact assessment, not a confirmation of compromise.

### 18 June 2025
#### 🇲🇦 Morocco - Ministry of National Education (men.gov.ma / massar.men.gov.ma)
- **Incident type:** Data Leak
- **Actor / Group:** RiseAgainLuigi & B4baYega
- **Sector:** Government / Education.
- **Website:** https://men.gov.ma / massar.men.gov.ma
- **Status:** Claim - Unverified
- **Victim Description:** The Ministry of National Education of Morocco. The Massar platform is the ministry's digital backbone, centralizing grades, registrations, and tracking for all students in the Kingdom. The actors claim a data leak and sale listing of over 6 million records; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 19 June 2025
#### 🇩🇿 Algeria - General Directorate of Customs (DGD) / Export and Import Control Service
- **Incident type:** Data Leak
- **Actor / Group:** mrdump (Telegram channel "Server dump")
- **Sector:** Government / Customs and Foreign Trade
- **Website:** [douane.gov.dz](https://www.douane.gov.dz)
- **Status:** Claim - Unverified
- **Victim Description:** The General Directorate of Customs (DGD) is the Algerian administration responsible for customs control, collection of duties and taxes, and regulation of foreign trade, including through its Export and Import Control Service.
- **Analysis:** On June 19, 2025, the Telegram channel "Server dump" (attributed to the same actor, mrdump, behind the June 14 and June 18, 2025 posts) published an image stamped "HACKED" showing a dashboard presented as belonging to the Algerian General Directorate of Customs, along with a message claiming a "takeover of the information system" and "confirmed access to the digital infrastructure and the administration panel." A second message announced that customs documents would be highlighted allegedly showing Algeria exporting goods to Israel, in contradiction with Algeria's official position, and promised the imminent release of detailed PDF files.

  A ZIP archive containing two PDF files was shared with AFRINTEL in connection with this post: a "maritime and commercial shipment record" concerning the vessel "Captain Christos" (IMO 9475410), and a "document retention certificate" presented as issued by the DGD's Export and Import Control Service, both relating to an export from the port of Bejaia to the port of Ashdod (Israel) between April 20 and April 28, 2025.

  AFRINTEL's technical review of both PDFs revealed several converging indicators of fabrication rather than an authentic extraction from a customs system: the metadata of both files show an author named "Yassine," creation via Microsoft Word 2016, and conversion through the online service ilovepdf.com, with creation timestamps matching exactly the day of the post (June 19, 2025) — inconsistent with scanned documents or a direct export from a real information system. The IMO number cited for the vessel, 9475410, fails the standard IMO check-digit calculation (expected check digit: 6; digit given: 0), which is objective technical evidence that this vessel identifier is invalid. The certification document also cites an "executive decree No. 2021-10" dated "June 15, 2010," an internal inconsistency between the decree's number and its stated date. The Israeli importing companies named in the document (ChemImport LTD, Precious Metals Ltd, GasTech Israel, Fashion Importers) could not be verified and appear generic.

  These findings converge on a low-confidence assessment regarding the authenticity of the reviewed documents, which appear to have been drafted to support a pre-existing political narrative rather than extracted from a compromised system. This technical conclusion applies specifically to the two reviewed PDFs; it neither confirms nor independently rules out the separate claim of access to the DGD's administration dashboard, which is visible only via a published image and was not independently verified. Given the fabrication identified in the associated documentary material, the overall claim is assessed with a low confidence level. No named data, complete customs file reference, or other element that could validate or amplify the actor's narrative is reproduced.

### 19 June 2025
#### 🇲🇦 Morocco - Royal Moroccan Football Federation (FRMF)
- **Incident type:** Data Leak
- **Actor / Group:** Keymous
- **Sector:** Sports / Public Administration
- **Website:** https://frmf.ma/
- **Status:** Claim - Data Sample Published
- **Victim Description:** Founded in 1956, the FRMF is the body responsible for organizing, managing, and developing football in Morocco. It oversees national teams, professional and amateur competitions, as well as regional leagues.
- **Analysis:** AFRINTEL identified the source publication as a DarkForums post by the actor Keymous, titled "Football federation morocco Leak," claiming a database of FRMF players and staff covering more than 4,289 named records. AFRINTEL reviewed a local sample of documents consistent with FRMF's official registration and licensing records. The sample includes a FIFA Connect team-official registration record and a CAF Pro coaching-license record, each containing a full name, date of birth, gender, nationality, home address, phone number, a FIFA or license identification number, license validity date and a photograph, together with a club registration request form listing a license holder's full name, date and place of birth, national ID/passport number, nationality and affiliated club. Two small spreadsheet extracts, structured as a football-official/member registry (registration ID, status, name, nationality, date and year of birth, region, city, address, postal code, phone, email, club and badge/authorization code), were also present, covering roughly three dozen records combined, and match the field structure described in Keymous's post. This is consistent with exposure of parts of FRMF's official and licensing database rather than only generic administrative correspondence. At least one reviewed record concerns an individual whose date of birth indicates they were a minor around the time of registration. AFRINTEL does not reproduce any name, address, identification number, contact detail or photograph from the reviewed sample. The total scope, completeness and current validity of the underlying database could not be independently confirmed beyond the limited sample available.

### 20 June 2025
#### 🇲🇦 Morocco - INWI (inwi.ma)
- **Incident type:** Data Leak
- **Actor / Group:** Evil_BYTE_Officiel
- **Sector:** Telecommunications.
- **Website:** https://inwi.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** INWI is one of the three main telecommunications operators in Morocco, providing mobile, fixed-line, and internet services (ADSL/Fiber). The actor published a sample of sensitive data including PII (name, national ID), contact information and password hashes (bcrypt).

### 26 June 2025
#### 🇩🇿 Algeria - Ministry of Transportation
- **Incident type:** Data Leak
- **Actor / Group:** KickingPigs
- **Sector:** Government / Transportation
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Victim Description:** Algeria's Ministry of Transportation is the public administration responsible for national transportation policy and related administrative services.
- **Analysis:** A forum publication dated 26 June 2025, attributed to KickingPigs, presents an alleged leak from the Algerian Ministry of Transportation. The post lists vehicle-registration and transport-administration records, including names, national identification numbers, parent names, company registration numbers, vehicle and registration details, driving-licence documents and internal Excel files. The visible sample contains structured vehicle records and sensitive personal-data fields; AFRINTEL does not reproduce the records or identifiers. The authenticity, completeness and technical origin of the dataset could not be independently confirmed.

### 20 June 2025
#### 🇹🇳 Tunisia - Ministry of National Defense / Armed Forces
- **Incident type:** Data Leak
- **Actor / Group:** mrdump (publication on the Telegram channel \"Server dump\")
- **Sector:** Defense / National Security
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Tunisian Ministry of National Defense is the government administration responsible for national defense and the armed forces.
- **Analysis:** A publication dated 20 June 2025, attributed to mrdump, claims successful access to several systems belonging to Tunisia's Ministry of National Defense, specifically its Armed Forces division. The publication alleges that an underground weapons depot was discovered at Mount Chaambi in Kasserine Governorate and refers to thermal imagery, engineering plans and information concerning stored weapons and ammunition. An associated ZIP archive was provided to AFRINTEL; a non-content structural review identified 10 archive members (six PNG images, one XLSX workbook, one PDF and one JPG), approximately 6.2 MB compressed and 6.3 MB uncompressed. AFRINTEL did not open or reproduce the files because the material is presented as military and potentially operationally sensitive. The archive structure does not independently establish the authenticity, provenance, classification or completeness of the material, and the claimed access remains unverified.

### 29 June 2025
#### 🇩🇯 Djibouti - Embassy of Djibouti in Morocco
- **Incident type:** Data Leak

- **Actor / Group:** MdHackersArmy (post published by Doxeur23azi on a cybercriminal forum, DarkForums)
- **Sector:** Government / Diplomatic
- **Status:** Claim - Unverified
- **Website:** Not specified

- **Description:**
  The Embassy of Djibouti in Morocco is Djibouti's diplomatic mission accredited to the Kingdom of Morocco.

- **Analysis:**
  A post titled "Leak db of the Embassy of Djibouti in Morocco" was published on 29 June 2025 on the cybercriminal forum DarkForums by the account Doxeur23azi, crediting the claim to MdHackersArmy. The post consists solely of an external download link and does not describe the data type, field structure, record volume or sensitivity of the alleged database, and no sample is visible. AFRINTEL did not access the external link. The data at risk, the affected population and the technical origin of the claim remain unknown at this stage.
## ✍🏿 Author
*Adama ASSIONGBON*  
*SOC & Cyber Threat Intelligence Consultant*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)

---
*AFRINTEL - Open CTI Monitoring Initiative on Africa*
