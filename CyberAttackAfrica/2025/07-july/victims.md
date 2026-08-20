[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# List of African cyberattack victims in July 2025 (21 victims)
👉🏾 [**French version available here**](./victims_FR.md)

## July 2025

### 01 July 2025
#### 🇳🇬 Nigeria - Chartered Institute of Bankers of Nigeria (CIBN)
- **Incident type:** Data Leak
- **Actor / Group:** Hepd
- **Sector:** Financial Services / Professional Regulatory Body.
- **Website:** https://cibng.org
- **Status:** Claim - Data Sample Published
- **Victim Description:** The umbrella institution for the banking profession in Nigeria, responsible for the accreditation and ethics of bankers, including members of the Central Bank (CBN). The actor claims to have published a database including sensitive information on the country's banking elite, on the deep web. AFRINTEL reviewed the supplied CIBN archive structurally: 472 files and approximately 18 MB, including member addresses, bank details, employment, qualifications, documents, wallets, login-related tables, staff records, educational and fintech database exports, and access/logging artifacts. The archive also contains files named for member and user records. AFRINTEL did not reproduce any personal record, credential, token or document. The archive supports a substantial data-publication assessment, but its authenticity, completeness and direct provenance from CIBN remain independently unverified.

### 03 July 2025
#### 🇩🇿 Algeria - Algeria Post / ECCP
- **Incident type:** Data Leak
- **Actor / Group:** sanji_shi5 (source account)
- **Sector:** Postal Services / Financial Services
- **Website:** [poste.dz](https://www.poste.dz)
- **Source publication date:** 3 July 2025
- **Status:** Claim - Data Sample Published
- **Victim Description:** Algeria Post operates the ECCP service, which allows Algerian users to check postal-account balances and make online purchases. The supplied forum post displays a sample formatted as account identifiers and password-like values associated with ECCP/Algeria Post. No credential is reproduced or validated, and the underlying dataset was not collected.
- **Analysis:** The observed sample suggests a potential exposure of account-access data affecting a public postal and financial service. If valid, the data could enable account takeover, fraud and targeted phishing. The post identifies sanji_shi5 as the source account, but this does not independently confirm the compromise, the dataset's provenance or the validity of the displayed values.

### 08 July 2025
#### 🇿🇦 South Africa - MAFATE BUSINESS ENTERPRISE
- **Ransomware Group:** d4rk4rmy
- **Sector:** Industrial Supplies / Mining Support Services.
- **Website:** https://mafate.co.za
- **Status:** Claim - Unverified
- **Victim Description:** Mafate Business Enterprise is an industrial service provider established in Middelburg (Mpumalanga), at the heart of the South African mining region.

### 09 July 2025
#### 🇲🇦 Morocco - Fédération Nationale du Bâtiment et des Travaux Publics (FNBTP)
- **Incident type:** Data Leak
- **Actor / Group:** Evil_BYTE_Officiel
- **Sector:** Construction / Public Works / Professional Organisation
- **Website:** [fnbtp.ma](https://www.fnbtp.ma)
- **Status:** Data Fully Published
- **Victim Description:** The Fédération Nationale du Bâtiment et des Travaux Publics (FNBTP) is a professional organisation representing Moroccan companies operating in the construction and public works sector. On 9 July 2025, the actor Evil_BYTE_Officiel published on an underground forum a database attributed to the FNBTP and stated that the data was being released for free.
- **Analysis:** The publication exposes a table named `societe` containing information related to companies operating in the construction and public works sector. The fields listed in the publication are: `Id`, `nb_national`, `nb_regional`, `ENTREPRISE`, `secteur`, `adher`, `MONTANT_COTISATION`, `Responsable`, `Adress`, `Téléphone`, `Fax`, `GSM`, `VILLE` and `E-MAIL`.

  The CSV file analysed by AFRINTEL contains 180 rows and 14 columns. The observed data includes company names, internal references, membership-related information, contact persons, addresses, telephone numbers, fax numbers, mobile numbers, cities and professional email addresses.

  Among the 179 rows structured as company records, 166 contain a city, mainly Rabat, Salé, Temara and Khemisset. 146 contain a contact person, 145 a telephone number, 139 a fax number, 111 a mobile number and 81 at least one email address. Some records contain several contact details for the same company.

  An anomaly is present in the supplied file. The first row contains values that do not match the business structure observed throughout the remaining dataset. Subsequent records, including those visible in the underground forum post, are consistent with the structure described by the actor.

  The exposed information can support the mapping of companies operating in the construction sector and the identification of their representatives and direct contact details. Such information may be used to prepare spear phishing campaigns, impersonation attempts or targeted social engineering against companies and their business contacts.

  The data is published for free by the actor. No asking price or ransom demand is visible. The forum publication directly exposes database records and the analysed file confirms the presence of structured data. The incident therefore involves actual data publication rather than a claim without supporting material. AFRINTEL does not reproduce any company names, contact names or contact details from the reviewed sample.

### 13 July 2025
#### 🇹🇿 Tanzania - Twaweza
- **Ransomware Group:** nightspire
- **Sector:** NGO (Education & Governance)
- **Website:** https://twaweza.org
- **Status:** Claim - Unverified
- **Victim Description:** Twaweza East Africa is a leading pan-African organization, based in Tanzania (with offices in Kenya and Uganda).

### 14 July 2025
#### 🇲🇦 Morocco - IWACLUB (iwaclub.ma)
- **Incident type:** Data Leak
- **Actor / Group:** Keymous
- **Sector:** Telecommunications / Distribution & Retail.
- **Website:** https://iwaclub.ma
- **Status:** Claim - Unverified
- **Victim Description:** IWACLUB is the professional application dedicated to the reseller network of the company IWACO, one of the most important distributors of telecommunications solutions (notably the operator inwi) and technological products in Morocco.

### 14 July 2025
#### 🇩🇿 Algeria - Ministry of Energy, Mines and Renewable Energies / SARL SOPRETA
- **Incident type:** Data Leak
- **Actor / Group:** Phantom Atlas
- **Sector:** Government / Energy and Mining; named third party: chemical industry / building waterproofing
- **Website:** Not specified for the ministry; no official website identified for SOPRETA
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Ministry of Energy, Mines and Renewable Energies is the Algerian authority issuing authorizations for the acquisition of hazardous materials and chemical products. SARL SOPRETA (Société des Produits d'Étanchéité Algériens), based in Ain El Arbaa, Ain Temouchent province, is a company named in the leaked document.
- **Analysis:** On July 14, 2025, Phantom Atlas published an accusation targeting Minister Mohamed Arkab, claiming that the ministry had granted, in March 2025, an import license for more than 10 tons of hazardous chemical substances to a company described as "virtually unknown, not appearing in any known industrial registry," in the absence of any oversight or transparent environmental reporting, insinuating an operation with murky objectives.

  AFRINTEL reviewed the documents attached to the post: authorization No. 1000 dated March 6, 2025, issued by the ministry to SARL SOPRETA; the attached list of authorized materials (anhydrous hydrochloric acid, nonylphenol ethoxylate under the commercial names Indulin W-5 and Indulin AA-83, up to 10 and 8 tons respectively); and a proforma invoice from the Belgian company MBM International SA (Brussels) addressed to SOPRETA for 6,531.60 kg of Indulin W5 and 2,517.30 kg of Indulin AA-83, totaling €43,257.54, with delivery to the port of Oran. The three documents are mutually consistent (same authorization number, same company address, same commercial product names).

  Contrary to Phantom Atlas's insinuation, AFRINTEL identified SARL SOPRETA (Société des Produits d'Étanchéité Algériens) in several public Algerian business directories, at the exact address stated in the authorization; it is an established company specializing in building waterproofing and the manufacture of basic inorganic chemical products, including bitumen-based products. "Indulin" products are lignin-based emulsifiers marketed for producing bitumen emulsions and road waterproofing products, which directly matches SOPRETA's declared line of business rather than suggesting a diverted or unidentified use. The authorization procedure itself (monthly declaration, compliance with hazardous chemicals regulations, oversight by the wilaya's energy and mines directorate, one-year validity) corresponds to an existing regulatory framework, which contradicts the claim of a "complete absence of oversight."

  AFRINTEL therefore assesses that the leaked document is probably authentic and consistent with a legitimate, declared industrial import, but that Phantom Atlas's accusatory framing (an "unknown" company, absence of oversight, opaque objectives) is not corroborated by publicly available information on SOPRETA. This leak nonetheless constitutes an unauthorized disclosure of an internal ministry administrative document as well as commercial data belonging to a third-party company (the Belgian supplier's banking details, contractual specifics). AFRINTEL does not reproduce any banking data or information that could identify individuals associated with this file.

### 14 July 2025
#### 🇰🇪 Kenya - ICT Authority (icta.go.ke)
- **Incident type:** Data Leak
- **Actor / Group:** Unknown
- **Sector:** Government / Digital Infrastructure
- **Website:** [icta.go.ke](http://icta.go.ke)
- **Status:** Claim - Data Sample Published
- **Victim Description:** Kenya's ICT Authority is a public-sector technology institution responsible for coordinating and supporting government information and communication technology infrastructure and services.
- **Analysis:** AFRINTEL reviewed the supplied CSV export without reproducing personal data. The file contains 1,697 data rows and fields for display name, phone, email, identifier, mobile contact, name, address-related fields, user references and website links. The structure is consistent with an organisational contact or directory export containing ICT Authority personnel, public-sector contacts and associated technology-service records. The file metadata places the evidence on 14 July 2025; this is treated as an evidence/discovery date, not a confirmed publication or intrusion date. The available material does not identify the threat actor, publication venue, access method or complete dataset scope. The exposed contact and organisational information could support targeted phishing, impersonation and social engineering against Kenyan public-sector and technology stakeholders. AFRINTEL records this as a data-leak claim with a published sample and does not reproduce names, phone numbers, email addresses, identifiers or addresses.
### 15 July 2025
#### 🇰🇪 Kenya - Adrian Kenya
- **Ransomware Group:** lynx
- **Sector:** Telecommunications / Energy Infrastructure / ICT.
- **Website:** https://adrian.co.ke / www.adriankenya.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Adrian Group (Adrian Kenya) is a Kenyan leader in technological engineering.
- **Analysis:** AFRINTEL reviewed a local sample of four documents associated with this claim: a vendor invoice for telecom site installation work, a Kenya Revenue Authority (KRA) VAT payment slip, a fuel-supplier credit note and an internal email thread concerning a telecom site rollout. The documents are internally consistent, reference matching Adrian Kenya/Adrian Group names, domains and project context, and contain financial, tax-compliance, vendor and internal-communication records. AFRINTEL does not reproduce the personal identifiers, banking details or tax PIN visible in the sample. This assessment is limited to the four documents reviewed; AFRINTEL did not consult any subsequent disclosure or additional files published by the group.

### 15 July 2025
#### 🇪🇬 Egypt - Egyptian Electricity Holding Company (EEHC, eehc.gov.eg)
- **Ransomware Group:** devman
- **Sector:** Government / Energy (Electricity)
- **Website:** https://eehc.gov.eg
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** The Egyptian Electricity Holding Company (EEHC) is the state holding company overseeing electricity generation, transmission and distribution across Egypt, including its regional distribution subsidiaries. The actor demands $2,270,000 USD.
- **Analysis:** AFRINTEL reviewed a directory listing (not the underlying file contents) of an alleged internal file share hosted on a MEGA cloud mount, comprising roughly 8,000 folders and more than 50,000 file entries. The dominant file types are spreadsheets (over 31,000 Excel files) and PDFs (nearly 4,000), alongside Word documents, images and a small number of email exports. The folder structure includes subdirectories named after EEHC's regional distribution companies (matching Egypt's real electricity distribution structure: Alexandria, Canal, Beheira, Middle Egypt, North Delta, South Cairo and South Delta), employee-named personal folders, and material referencing Oracle Utilities Customer Care & Billing (CC&B), Meter Data Management (MDM) and Customer Self Service (CSS) systems, together with technical proposals and meeting records tied to a smart-meter (AMI) rollout programme. The consistency between this folder structure and EEHC's known regional and system architecture supports a high confidence assessment that the listing reflects genuine internal access, though AFRINTEL has not opened or verified the contents of individual files. Given the scale of the listing and EEHC's role as Egypt's national electricity holding company, potential exposure would combine employee personal data, internal operational and billing-system documentation, and technical infrastructure records for a critical national utility. AFRINTEL does not reproduce any employee name, file content or folder path containing personal identifiers from the reviewed listing.

### 15 July 2025
#### 🇳🇦 Namibia - Otjiwarongo Municipality
- **Ransomware Group:** incransom
- **Sector:** Public Administrations / Local Government.
- **Website:** www.otjimun.org.na
- **Status:** Claim - Data Sample Published
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** The municipality of Otjiwarongo is the local government body for the city of Otjiwarongo, capital of the Otjozondjupa region in Namibia.
- **Analysis:** AFRINTEL reviewed a local sample of documents consistent with the claim made by the threat actor incransom, consisting of an unredacted extract from the municipality's VIP Payroll System, a remuneration list for the pay period ending 28 February 2025 listing dozens of employee records with employee code, department, full name, net pay amount in Namibian dollars, bank code and bank account number. The document bears genuine system headers identifying it as an official municipal payroll run ("001 Municipality of Otjiwarongo"), consistent with a real internal HR/payroll system compromise rather than a fabricated sample. The combination of employee identity, remuneration and full banking details for a local government payroll supports a very high confidence assessment. Exposure of this data creates a significant risk of payroll fraud, targeted phishing and identity-related fraud against municipal employees. AFRINTEL does not reproduce any employee name, employee code, salary amount or bank account number from the reviewed sample.

### 15 July 2025
#### 🇲🇷 Mauritania - QCE Portal (qce.gov.mr)
- **Incident type:** Data Leak
- **Actor / Group:** Unknown
- **Sector:** Government / Public Procurement (Enterprise and Personnel Qualification)
- **Website:** qce.gov.mr
- **Status:** Claim - Data Sample Published
- **Victim Description:** qce.gov.mr is a Mauritanian government online platform used to host and process personnel and enterprise qualification dossiers, consistent with contractor/technical-staff vetting for public works and procurement processes; its precise institutional mandate could not be independently confirmed from the reviewed sample.
- **Analysis:** AFRINTEL reviewed a local sample of files consistent with personnel qualification dossiers submitted through the platform, including curricula vitae, national identity cards (CIN), academic diplomas, notarized employment-contract deposits and related supporting documents for individuals employed by several distinct Mauritanian private companies (including construction, drilling and technical-services firms). The documents display genuine official letterheads, notary seals and structured personal-data fields (full name, national identification number, date and place of birth, employer, position, signature, photograph), consistent with a real qualification/procurement dossier repository rather than fabricated content. No claiming actor, publication venue or forum post could be identified for this dataset; the sample was dated from local file metadata (mid-July 2025) in the absence of an explicit publication date. The combination of national ID numbers, diplomas and employment records for numerous private individuals creates a significant risk of identity fraud, document forgery and targeted social engineering against affected candidates and their employers. AFRINTEL does not reproduce any individual's name, national identification number, date of birth, employer contact details or signature from the reviewed sample.

### 18 July 2025
#### 🇲🇦 Morocco - Mohammed VI Polytechnic University (UM6P)
- **Incident type:** Data Leak
- **Actor / Group:** Mercobyte
- **Sector:** Education / Higher Education
- **Website:** https://um6p.ma
- **Status:** Claim - Unverified
- **Victim Description:** An excellence institution (University) based in Benguerir, a strategic hub for research, innovation, and executive training in Morocco. The actor claims a targeted data leak and influence operation, publishing student ID photos accompanied by a political message; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 25 July 2025
#### 🇹🇳 Tunisia - Ministry of Finance (finances.gov.tn)
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Government / Tax Administration.
- **Website:** https://finances.gov.tn
- **Status:** Claim - Unverified
- **Victim Description:** Tunisian Ministry of Finance.
- **Analysis:** AFRINTEL did not directly review technical evidence isolated to finances.gov.tn beyond the actor's "Full Access" claim. However, a credential-store export reviewed alongside this claim, attributed to the same Dark 07x Team campaign on the same date, contained dozens of plaintext username/password pairs for a separate Tunisian institution (the Academy of Banks and Finance, ABF), suggesting the actor pivoted between compromised organizations and reused harvested credentials across targets during this campaign. AFRINTEL does not reproduce any of the exposed credentials.

### 25 July 2025
#### 🇹🇳 Tunisia - Academy of Banks and Finance (abf.tn)
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Professional Training / Banking Sector.
- **Website:** abf.tn
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Academy of Banks and Finance (ABF) is the continuing education body of the Tunisian Professional Association of Banks and Financial Institutions (APTBEF).
- **Analysis:** Material shows an authenticated administrative session on the ABF website under a named staff account, confirming access beyond a simple claim. A separate credential-store export associated with the same campaign contained several dozen plaintext username/password pairs for ABF-linked platforms, including its video-conferencing/webinar system, its e-learning ("formation à distance") portal and a WordPress administration login, alongside a handful of associated email addresses. No exposed credentials or email addresses are reproduced.

### 25 July 2025
#### 🇹🇳 Tunisia - BTK Bank
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Banking / Financial Services.
- **Website:** https://btknet.com
- **Status:** Claim - Data Sample Published
- **Victim Description:** BTK Bank (Banque Tuniso-Koweïtienne) is a Tunisian banking institution resulting from a Tunisian-Kuwaiti joint venture.
- **Analysis:** Material shows a live, authenticated e-banking session on btknet.com, including an account listing, a wire-transfer initiation screen showing a beneficiary list, and a customer bank-identity statement (RIB/IBAN) for a named account holder, confirming an actual account takeover rather than a simple claim. The associated forum post, attributed to a collaboration between the handles Dark 07x, Jokeir 07x and Dr. SHell 08x operating as "Dark Hell 07X", advertised a tiered sale of the stolen data: a full database for $4,000, a bank-account data file for $2,000, and individual bank accounts priced from $100 (one account) to $450 (five accounts). No account numbers, IBANs or customer identities are reproduced from the reviewed sample.

### 25 July 2025
#### 🇹🇳 Tunisia - Banque de Tunisie (bt.com.tn)
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Banking / Financial Services.
- **Website:** https://bt.com.tn
- **Status:** Claim - Data Sample Published
- **Victim Description:** Banque de Tunisie (BT) is one of the oldest and largest private banks in the country.
- **Analysis:** Material shows a live, authenticated customer online-banking dashboard on bt.com.tn with multiple account balances, a foreign-exchange rate module, a securities/portfolio overview and a transaction-history chart, confirming genuine account-level access rather than a simple claim. No account numbers or balances are reproduced from the reviewed sample.

### 27 July 2025
#### 🇪🇷 Eritrea - Embassy of Eritrea in the United States
- **Incident type:** Data Leak

- **Actor / Group:** Gh1nDar
- **Sector:** Government / Diplomatic
- **Status:** Claim - Unverified
- **Website:** [us.eriembassy.org](https://us.eriembassy.org)

- **Description:**
  The Embassy of Eritrea in the United States is the official diplomatic representation of the State of Eritrea on US territory.

- **Analysis:**
  A threat actor using the alias Gh1nDar claims, in a BreachForums post dated July 27, 2025, to have uploaded a leak affecting approximately 5,000 citizens linked to the Embassy of Eritrea in the United States. The allegedly exposed data would include ID card number, full name, mother's name, passport number, email address, phone number, birthdate, religion and current job. No verifiable sample was accessible in the collected source. The account behind the post is recent and has no established reliability history. At this stage, AFRINTEL does not confirm the intrusion or the authenticity of the data.

### 28 July 2025
#### 🇹🇳 Tunisia - BH Bank
- **Incident type:** Data Leak
- **Actor / Group:** Dark 07x Team
- **Sector:** Banking / Financial Services.
- **Website:** https://bhbank.tn/
- **Status:** Claim - Data Sample Published
- **Victim Description:** Historic and systemic banking institution in Tunisia (Banque de l'Habitat), a pillar of real estate financing and the national economy.
- **Analysis:** The actor's forum post, published under the handle Jokeir07x as part of the "Dark Hell 07X" collaboration with Dr. SHell 08x (also behind the BTK Bank claim), states that the group gained full control of the website's infrastructure, emptied and analysed all databases, and confirmed compromise of both back-end and front-end access points; the post separately advertises a list of 200 "Yankee" accounts for sale for 100 USDT. Accompanying material shows live, authenticated online-banking sessions for at least two distinct customer accounts, including a corporate "BH Capital Plus" account, with visible balances, plus a bank-card transaction history including a withdrawal record. No account numbers, card numbers, customer identities or balances are reproduced from the reviewed sample.
### 29 July 2025
#### 🇲🇦 Morocco - Ministry of National Education, Preschool and Sports
- **Incident type:** Data Leak
- **Actor / Group:** Wieko
- **Sector:** Government / Public Administration / Education
- **Website:** [men.gov.ma](https://men.gov.ma)
- **Status:** Claim - Data Sample Published

- **Description:**
  The Ministry of National Education, Preschool and Sports is the Moroccan public administration responsible for government policy concerning preschool, primary and secondary education, as well as school sports. Its official institutional portal uses the `men.gov.ma` domain.

- **Analysis:**
  A cybercriminal-forum post attributed to Wieko advertises a text file containing 223,501 lines in `mail:pass` format. The visible sample includes accounts associated with several Moroccan education-related domains, including universities and training institutions. Individual credentials are not reproduced. A download section is visible but hidden by the forum, preventing verification of the advertised file, its integrity, record uniqueness or the validity of all credential pairs. The material appears to be a combined credential list rather than a structured export from a ministry database. The presence of accounts from several institutions does not demonstrate a direct compromise of the ministry’s central information systems; the credentials’ origin, collection method and technical connection to the central administration remain unknown. The combinations could facilitate credential stuffing, account takeover, unauthorized access to educational platforms, targeted phishing and digital impersonation, particularly where passwords were reused. No price, ransomware group, byte volume, deadline or extortion demand is stated.

- **Double-claim note:**
  AFRINTEL separately recorded a June 18, 2025 claim involving the ministry’s Massar platform. The actors and advertised datasets differ, and available evidence does not establish that both publications derive from the same compromise.

### 30 July 2025
#### 🇧🇮 Burundi - PesaBay

- **Incident type:** Data Leak
- **Actor / Group:** BabayoSysteam
- **Sector:** Retail / E-commerce
- **Status:** Data Fully Published
- **Confidence level:** Medium
- **Impact level:** Level 2
- **Website:** [pesabay.bi](https://pesabay.bi)

- **Description:**
  PesaBay is a Burundian online marketplace operated by AFRIREGISTER S.A. It enables sellers to list products and users to buy from or contact merchants using the platform.

- **Analysis:**
  A post attributed to the BabayoSysteam account, dated July 30, 2025, makes available a PesaBay database presented as complete and containing 1,850 records. The published fields include first name, last name, email address, phone number and account status. The presence of numerous phone numbers using Burundi's `+257` country code, combined with PesaBay branding and a coherent record structure, supports a medium-confidence attribution of the dataset to the platform. AFRINTEL therefore classifies the case as `Data Fully Published`. This classification describes publication of the dataset advertised as complete; it does not independently confirm the acquisition method, the initial intrusion, row uniqueness, or coverage of PesaBay's entire production database. The published contact data creates risks of targeted phishing, fraud, spam and digital impersonation, corresponding to a Level 2 impact. No name, email address, phone number or other raw personal data is reproduced.

---
[July 2025 Report](./report/README.md)
---
## ✍🏿 Author
*Adama ASSIONGBON*  
*SOC & Cyber Threat Intelligence Consultant*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)

*AFRINTEL - Open CTI Monitoring Initiative on Africa*
