[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# African victims - October 2025

👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

**20 documented cyber incidents** under AFRINTEL Taxonomy v2: Ransomware 16, Data Leak 3, Access Sale 1.

> Public-source links are added to supplementary incidents identified through online research to complete the corpus. They are not retroactively imposed on historical AFRINTEL records, including Dark Web observations.

## October 2025

### 01 October 2025
#### 🇿🇦 South Africa - Climatron (Pty) Ltd
- **Ransomware Group:** incransom
- **Sector:** Construction / HVAC
- **Website:** https://climatron.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Climatron (Pty) Ltd is a company specializing in industrial and commercial air conditioning solutions, based in Johannesburg.

### 05 October 2025
#### 🇿🇦 South Africa - The Methodist Church of Southern Africa
- **Ransomware Group:** beast
- **Sector:** Religion / Charitable Organization
- **Website:** www.methodist.org.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** The Methodist Church of Southern Africa (MCSA) is one of the most influential Christian denominations in the region. It operates not only in South Africa but also in Botswana, Lesotho, Namibia, Eswatini, and Mozambique.

### 10 October 2025
#### 🇿🇦 South Africa - Momentum Logistics
- **Ransomware Group:** brotherhood
- **Sector:** Transport / Logistics
- **Website:** www.momentumlogistics.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Momentum Logistics is a South African logistics provider based in Johannesburg.

### 13 October 2025
#### 🇲🇦 Morocco - LA VOIE EXPRESS
- **Ransomware Group:** medusa
- **Sector:** Logistics
- **Website:** https://lavoieexpress.ma / https://lavoieexpress.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** Moroccan logistics company based in Casablanca, offering courier, transport, and warehousing services.
- **Analysis:** AFRINTEL reviewed a local sample of multi-sheet spreadsheet exports consistent with the claim made by the threat actor medusa, each watermarked with the group's Tor leak-site address. The reviewed material includes a general accounting ledger (bank and journal entries dated 2020-2021), warehouse and logistics workbooks covering goods reception, dispatch, stock-preparation and internal-transfer movements for major appliance brands (referencing BSH/Bosch-Siemens product lines) tied to named internal staff handling the operations, and a client accounts-receivable ageing report listing several dozen named corporate clients across multiple Moroccan cities (Casablanca, Agadir, Tanger, Marrakech, Fès, Settat and others), including well-known national and multinational accounts (among them Procter & Gamble-affiliated entities, Savola Maroc, Centrale Laitière, Ciment du Maroc, BSH Electroménager and Ecolab), together with named client contacts, phone numbers, outstanding balances, payment terms and collections/dispute status. The internal consistency of the data across accounting, warehouse and commercial modules, the presence of real, identifiable Moroccan and multinational client accounts, and the multi-year date range (2020-2023) spanning multiple branches support a very high confidence assessment of a genuine, broad compromise of La Voie Express's internal ERP and accounting systems. Given the scale of the exposed accounts-receivable and banking-ledger data and its extension into the client base of a major national logistics provider, this incident creates a material risk of invoice fraud, business email compromise and targeted social engineering against La Voie Express and its corporate clients, beyond the company's own operational exposure. AFRINTEL does not reproduce any client name, contact name, phone number, financial figure or staff identifier from the reviewed material.

### 15 October 2025
#### 🇰🇪 Kenya - Turnkey Africa
- **Ransomware Group:** qilin
- **Sector:** Technology / Fintech (Insurance Solutions)
- **Website:** https://turnkeyafrica.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Turnkey Africa is a pan-African technology leader. The company develops and provides software management solutions (Core Insurance Systems) for insurance and reinsurance companies in over 10 African countries.

### 17 October 2025
#### 🇲🇬 Madagascar - Madagascar Airlines
- **Ransomware Group:** TheGentlemen
- **Sector:** Air transport
- **Website:** www.madagascarairlines.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Madagascar Airlines is the national airline of the Republic of Madagascar.

### 18 October 2025
#### 🇨🇩 Congo (DRC) - TK HOLDINGS GROUP
- **Ransomware Group:** radar
- **Sector:** Mining / Conglomerate
- **Website:** https://congomineralservices.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim Description:** Congolese holding with activities in timber, logistics, and mineral exploration.

- **Confidence level:** Medium
- **Impact level:** Level 4
- **Analysis:** AFRINTEL reviewed the analyst-provided CTI workbook and 32 screenshots associated with the radar publication. The evidence set contains seven document categories: DRC customs and legal texts, public-procurement and governance material, TK Holdings salary and recruitment policies, a geological report from Congo Mineral Services concerning the Mikuba Mining copper exploration project, and an environmental-control decree. The workbook classifies the salary policy and the Mikuba geological report as critical sensitivity. The geological material references drilling campaigns and copper grades, creating a plausible industrial-espionage and strategic-resource risk. The HR policies expose internal salary, bonus, leave, recruitment and confidentiality procedures, creating risks of employee targeting, insider abuse and reputational harm. The legal and regulatory documents could support document fraud, corruption or manipulation of compliance and import processes if their authenticity and currency were established. The evidence confirms that sensitive-looking documents were displayed in the collection, but it does not independently confirm the intrusion path, the completeness of the published dataset, the authenticity of every document, or operational impact. AFRINTEL does not reproduce document contents, personal names, signatures or other sensitive material.

### 18 October 2025
#### 🇿🇦 South Africa - University of the Witwatersrand (WITS)
- **Ransomware Group:** clop
- **Sector:** Education (University)
- **Website:** https://www.wits.ac.za
- **Status:** Data Fully Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 3
- **Victim Description:** The University of the Witwatersrand, located in Johannesburg, is one of Africa's most prestigious research institutions.
- **Analysis:** AFRINTEL reviewed a screenshot of Clop's leak-site listing page for wits.ac.za, using the group's standard victim-profile template (Headquarters, Phone, Website, Revenue and Industry fields). Unlike listing pages reviewed for other African entries on the same leak site, this page includes a dedicated "Torrent Magnet Link" section referencing wits.ac.za, indicating that the actor has made a downloadable dataset available rather than only a claim page. The listed company profile (industry described as Colleges & Universities, Education) is consistent with the University of the Witwatersrand's public profile. AFRINTEL did not download or review the content of the referenced torrent, and the volume, content and sensitivity of the published dataset are therefore not independently assessed. The presence of a functioning magnet-link section, distinct from the claim-only pages seen for other entries, supports a high confidence assessment that data has genuinely been made available for download. Given WITS's status as a major research university, a confirmed dataset could include student, staff or research-related personal data, creating a risk of identity fraud and targeted phishing against the university community. AFRINTEL does not reproduce the magnet link, headquarters address or phone number from the reviewed material.

### 19 October 2025
#### 🇬🇦 Gabon - SANgel
- **Ransomware Group:** qilin
- **Sector:** Agribusiness
- **Website:** https://sangel-gabon.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Gabonese food production and distribution company based in Libreville, specializing in frozen products.

### 20 October 2025
#### 🇪🇬 Egypt - Al Ahly Leasing & Factoring Company
- **Ransomware Group:** BlackShrantac
- **Sector:** Finance
- **Website:** alahlyleasing.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Egyptian financial institution specializing in leasing and factoring, a subsidiary of the National Bank of Egypt.

### 20 October 2025
#### South Africa - Companies and Intellectual Property Commission (CIPC) eServices
- **Actor / Group:** fuckoverflow (claimed seller)
- **Sector:** Government / Administration
- **Website:** https://www.cipc.co.za/
- **Incident date:** 20 October 2025 - reported date of the access-sale publication
- **Initial publication date:** 20 October 2025
- **Status:** Claim - Unverified Marketplace Listing
- **Incident type:** Access Sale
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Victim Description:** The Companies and Intellectual Property Commission operates South Africa's corporate-registration and intellectual-property services.
- **Analysis:** An actor advertised allegedly compromised CIPC eServices accounts for sale, potentially enabling record modification and data collection. CIPC did not confirm the validity of the allegedly compromised accounts in the supplied audit. AFRINTEL records the marketplace claim with medium confidence and does not treat successful access as independently confirmed.
- **Source type:** Secondary CTI + Marketplace Claim
- **Public sources:** [CyHawk Africa](https://cyhawk-africa.com/compromised-credentials/threat-actor-advertises-alleged-compromised-cipc-eservices-accounts-on-a-dark-web-forum/)

### 23 October 2025
#### 🇲🇦 Morocco - STAR LÉGUMES
- **Ransomware Group:** tengu
- **Sector:** Wholesale Trade (Food Products)
- **Website:** https://starlegumes.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** Moroccan wholesaler of fruits, vegetables, spices, and dried seeds based in Casablanca.
- **Analysis:** AFRINTEL reviewed the leak-site listing and a local sample of documents consistent with the claim made by the threat actor tengu. The leak-site page itself was captured (view counter and elapsed-time indicator visible), alongside a Moroccan commercial-registry extract (Tribunal de Commerce de Casablanca) confirming the company's legal identity, registration date, share capital, registered address and manager name; multiple client invoices dated between November 2021 and March 2025 bearing the company's ONSSA food-safety registration number, client names, addresses and transaction amounts; and a system-generated "Journal Factures Clients" accounting-ledger export covering October 2024, printed in February 2025, listing roughly 50 sequential invoice records with client names, invoice numbers and HT/TVA/TTC amounts. A structured analyst summary workbook built from this material further itemises a legal-identity record, a client-contact sample (name, tax ID/ICE, address) and an invoice sample. The combination of an official leak-site listing, a genuine commercial-registry extract, dated system-generated accounting exports and internally consistent branding across documents spanning more than three years supports a very high confidence assessment of a genuine compromise of Star Légumes' invoicing and accounting systems. Given the scale of exposed client contact and transaction data, this incident creates a risk of supplier/customer fraud, business email compromise and resale of the client base. AFRINTEL does not reproduce any client name, address, tax identifier or financial figure from the reviewed material.

### 24 October 2025
#### 🇲🇦 Morocco - Le MULTI LABORATOIRE LC2A
- **Ransomware Group:** tengu
- **Sector:** Pharmaceutical Industry / Laboratory
- **Website:** https://multi-laboratoire-lc2a.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 2
- **Victim Description:** Moroccan laboratory offering a platform for configuring analytical projects for businesses.
- **Analysis:** AFRINTEL reviewed a local sample of internal documents consistent with the claim made by the threat actor tengu, addressed to or generated by LC2A. The reviewed material includes a supplier price quote from a laboratory-equipment vendor (dated May 2022) addressed to LC2A's purchasing department, itemising reagents and analytical equipment with unit and total pricing, and an internal equipment-calibration log ("Carte de contrôle des équipements", quality-management form reference FOR06/PRT06) for a laboratory balance, recording daily calibration checks through October 2021. The company name, internal form references and consistent document branding across both files support a high confidence assessment that the sample originates from LC2A's internal systems rather than a fabricated claim. A separate bulk data package referenced alongside this sample did not complete transfer and could not be reviewed; this analysis is limited to the two documents described above. Given the operational and supplier nature of the reviewed material, this incident presents a moderate risk of supplier impersonation and disclosure of internal quality-control and procurement practices, with no patient or clinical data observed in the reviewed sample. AFRINTEL does not reproduce any supplier name, pricing detail, equipment code or staff identifier from the reviewed material.

### 24 October 2025
#### 🇳🇬 Nigeria - Henrietta Ezeoke Law Firm
- **Ransomware Group:** qilin
- **Sector:** Legal Services
- **Website:** https://houstonwrongfuldeathlawyers.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Nigerian law firm.

### 28 October 2025
#### 🇹🇿 Tanzania - Alios Finance Group
- **Ransomware Group:** incransom
- **Sector:** Finance
- **Website:** https://aliosfinance.co.tz
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Pan-African financial operator present in Tanzania, offering specialized financing solutions. 100 GB of data exfiltrated.

### 28 October 2025
#### 🇹🇳 Tunisia - Alios Finance Group
- **Ransomware Group:** incransom
- **Sector:** Finance
- **Website:** https://aliosfinance.tn
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Pan-African financial operator present in Tunisia, specializing in financing for businesses and individuals. During this intrusion, 100 GB of data were exfiltrated by the incransom group.

### 28 October 2025
#### 🇰🇪 Kenya - M-TIBA / CarePay
- **Incident date:** October 2025 - exact compromise date not established in the selected public sources
- **Initial publication date:** 28 October 2025
- **Actor / Group:** Kazu (claim)
- **Sector:** Healthcare / Health Technology
- **Website:** https://www.mtiba.com/
- **Status:** Corroborated - Data Sample Independently Reviewed + Regulator Investigation
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** M-TIBA is a health-technology platform operated by CarePay in Kenya and used to support healthcare services, programmes and payments.
- **Analysis:** On 28 October 2025, TechCabal reported a claim by the Kazu group involving unauthorized access to M-TIBA servers. Kazu claimed more than 17 million files and about 2.15 TB of data, but AFRINTEL does not treat those aggregate volumes as independently confirmed. TechCabal states that it reviewed a 2 GB sample containing data attributed to about 114,000 people, including identities, national identification numbers, dates of birth, phone contacts and, in some cases, medical diagnoses and billing information. On 29 October 2025, Kenya's Office of the Data Protection Commissioner (ODPC) announced an investigation to establish the nature and scope of the possible breach. CarePay had not confirmed the leak in the initial article and requested material to support its own investigation. AFRINTEL therefore records a Data Leak based on the independently reviewed sample and regulator investigation, while retaining Kazu's overall volume claims as unverified.
- **Source type:** Independent Media Sample Review + Regulator Investigation
- **Public sources:** [TechCabal - Safaricom-backed M-Tiba hit by massive data breach exposing patient records](https://techcabal.com/2025/10/28/safaricom-backed-m-tiba-hacked-exposing-4-8-patient-records/) | [The Star - ODPC probes possible M-Tiba data breach](https://www.the-star.co.ke/news/2025-10-29-odpc-probes-possible-m-tiba-data-breach)

### 31 October 2025
#### 🇩🇿 Algeria - TMF Logistics
- **Ransomware Group:** incransom
- **Sector:** Logistics
- **Website:** https://tmf-logistics.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Victim Description:** TMF Logistics is an Algerian company specializing in transport and logistics solutions. During this attack, the incransom group claimed the exfiltration of 39 GB of sensitive company data.
- **Analysis:** Internal financial and operational documents reviewed by AFRINTEL corroborate the incransom claim. A November 2024 revenue-by-client spreadsheet lists roughly thirty corporate clients served by TMF Logistics, including major food, beverage and pharmaceutical companies operating in Algeria (e.g. Danone Algérie, Institut Pasteur d'Algérie, GlaxoSmithKline Algérie, Fromagerie Bel Algérie), alongside refrigerated and general freight service categories (frigo, bâché and flatbed trailers). A separate detailed billing export covers invoice-level transport operations across numerous Algerian wilayas (including Béjaïa, Bouira, Batna, Constantine, Djelfa, Ghardaïa, Ouargla and Tindouf), indicating a national delivery network. A delivery discharge document confirms the company's official identity: SPA TMF Logistics, based in the Taharacht industrial zone, Akbou (Béjaïa wilaya), with its registered contact details and business registration references. The combination of a national client portfolio, route network data and business registration details creates a supply-chain risk (client impersonation, invoice fraud, competitive intelligence) extending beyond TMF Logistics' own operational exposure.

### 31 October 2025
#### 🇲🇦 Morocco - Institut Agronomique et Vétérinaire Hassan II (IAV Hassan II)
- **Incident type:** Data Leak
- **Actor / Group:** DBhacker_BF
- **Sector:** Education / Higher Education / Agronomy and Veterinary Sciences
- **Website:** iav.ac.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** IAV Hassan II is a leading Moroccan public institution for agronomic and veterinary higher education, based in Rabat. The reviewed database contains 4,208 applicant/candidate records and covers applicants/candidates and includes full name, date and place of birth, nationality, gender, address, national ID number (CIN), phone number, email address, enrollment status, academic track (filière) and an account password field (largely empty in the reviewed sample). The combination of national ID, contact details and academic data creates a risk of identity fraud, targeted phishing and account-recovery abuse; the completeness and origin of the file have not been independently confirmed.

### 31 October 2025
#### 🇲🇦 Morocco - Ministry of Higher Education, Scientific Research and Innovation (enssup.gov.ma)
- **Incident type:** Data Leak
- **Actor / Group:** EternalRed
- **Sector:** Government / Education / Higher Education
- **Website:** enssup.gov.ma
- **Source publication date:** 25 October 2025
- **Status:** Claim - Data Sample Published
- **Victim Description:** enssup.gov.ma is the Moroccan Ministry of Higher Education, Scientific Research and Innovation. The supplied text file contains exactly 942,930 lines, matching the advertised record count; it is a nationwide student extract covering 942,930 records, with fields including national ID number (CIN), national student identifier (code Massar), full name in Arabic and French, gender, date of birth, nationality, institution code and name, academic program (filière) and education level. The internal file metadata indicates the extract was originally compiled around December 2022, though AFRINTEL reviewed it as part of a 2025 data collection. The scale and structure of the dataset indicate a significant nationwide exposure of higher-education student records, creating risks of identity fraud and targeted phishing against students and institutions; completeness and the exact source of the extraction have not been independently confirmed.
