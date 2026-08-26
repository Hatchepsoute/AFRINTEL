# AFRINTEL - African victims - H2 2025

**114 documented cyber incidents under AFRINTEL.**

> **Reading dates:** `Incident date` indicates when the event occurred or was detected according to available evidence. `Initial publication date` indicates when it was first publicly disclosed, claimed or communicated. The two dates may fall in different months.

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
- **Actor / Group:** sanji_shi5
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
- **Incident type:** Ransomware
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

### 10 July 2025
#### Tunisia - University network / Centre Al-Khwarizmi
- **Actor / Group:** Unknown
- **Sector:** Education / University
- **Website:** University network / Centre Al-Khwarizmi
- **Incident date:** No later than 10 July 2025 - exact start date not publicly disclosed
- **Initial publication date:** 10 July 2025
- **Status:** Attempted - Outcome Unknown
- **Incident type:** System Intrusion
- **Subtype:** Attempted attack against university-network infrastructure
- **Confidence level:** High
- **Impact level:** Level 4
- **Source type:** Institutional Statement + Public Media
- **Analysis:** The Centre Al-Khwarizmi and Tunisian authorities reported an attempted cyberattack targeting university-network infrastructure and data. The available source does not confirm a successful data leak. AFRINTEL therefore tracks the attempt separately from the six successful/core incident types.
- **Sources:** [Source](https://www.tunisienumerique.com/cyberattaque-ciblant-les-universites-tunisiennes-mesures-durgence-et-renforcement-de-la-securite/)

### 13 July 2025
#### 🇹🇿 Tanzania - Twaweza
- **Ransomware Group:** nightspire
- **Sector:** NGO (Education & Governance)
- **Website:** https://twaweza.org
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
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
- **Analysis:** AFRINTEL reviewed a small local sample of four documents associated with this claim: a vendor invoice for telecom site installation work (antennas, feeder cable and RRU installation) issued to Adrian Kenya, a Kenya Revenue Authority (KRA) VAT payment slip for Adrian Group Limited covering January to March 2025, a fuel-supplier credit note addressed to Adrian Kenya Limited with vehicle, banking and payment-advice details, and an internal email thread between Adrian Kenya and Adrian Group staff (adriankenya.com and adriangroup.tech domains) discussing a telecom site rollout at a warehouse location. The documents are internally consistent, referencing matching company names, domains and project context, and include full personal identifiers, banking details and a tax PIN, none of which AFRINTEL reproduces here. The sample indicates exposure of financial, tax-compliance, vendor and internal-communication records, but its scope is limited to four documents and does not establish the total volume or extent of the underlying compromise. AFRINTEL does not independently confirm the intrusion.

### 15 July 2025
#### 🇪🇬 Egypt - Egyptian Electricity Holding Company (EEHC, eehc.gov.eg)
- **Ransomware Group:** devman
- **Sector:** Government / Energy (Electricity)
- **Website:** https://eehc.gov.eg
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
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
- **Incident type:** Ransomware
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

### 22 July 2025
#### South Africa - National Treasury - Infrastructure Reporting Model (IRM) website
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** https://www.treasury.gov.za/
- **Incident date:** 22 July 2025 - malware detection date stated by National Treasury
- **Initial publication date:** 23 July 2025
- **Status:** Government Confirmed
- **Incident type:** Malware
- **Subtype:** Malware intrusion on public-facing reporting system
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Source type:** Government Statement
- **Analysis:** South Africa's National Treasury identified malware on the Infrastructure Reporting Model website and isolated the affected servers. Other Treasury systems continued operating normally and no data exfiltration was confirmed. AFRINTEL preserves the confirmed malware intrusion as a supplementary observation because Malware is not one of the six core incident types.
- **Sources:** [South African National Treasury - official statement](https://www.treasury.gov.za/comm_media/press/2025/2020072301%20Media%20Statement%20-%20Malware%20Intrusion%20on%20National%20Treasury%E2%80%99s%20Infrastructure%20Reporting%20Model%20Website%20.pdf)

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

### 31 July 2025
#### Tunisia - Le Groupement Pharmaceutique (LGP)
- **Actor / Group:** Jokeir 07x / Dr Shell 08x (claim)
- **Sector:** Healthcare / Medical
- **Website:** Not independently confirmed
- **Incident date:** 31 July 2025 - date reported by the secondary CTI source
- **Initial publication date:** 31 July 2025
- **Status:** Claim - Secondary Evidence / Screenshots
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Victim Description:** Le Groupement Pharmaceutique was identified in a secondary CTI report concerning alleged exposure of internal-portal access.
- **Analysis:** Credentials and screenshots allegedly providing access to an internal portal were published, potentially exposing commercial information, references, prices, margins and suppliers. No victim confirmation was identified in the supplied audit. AFRINTEL records the case with medium confidence and does not reproduce credentials or sensitive values.
- **Source type:** Secondary CTI
- **Public sources:** [CyHawk Africa](https://cyhawk-africa.com/compromised-credentials/tunisian-pharmaceutical-group-breached-internal-portal-access-shared-publicly/)

### July 2025 - exact incident date not publicly disclosed
#### Seychelles - Seychelles Commercial Bank
- **Actor / Group:** Unknown
- **Sector:** Finance / Banking
- **Website:** Seychelles Commercial Bank
- **Incident date:** July 2025 - exact incident date not publicly disclosed
- **Initial publication date:** 29 July 2025
- **Status:** Bank + Central Bank Confirmed
- **Incident type:** Data Leak
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** Seychelles Commercial Bank is a banking institution serving customers in Seychelles.
- **Analysis:** The bank reported that it had identified and contained a cyber incident in which some personal information of Internet-banking customers was exposed. No customer funds were reported compromised. Because the public notice did not provide a precise incident date, AFRINTEL places the event in July without inventing a specific compromise day.
- **Source type:** Bank / Central Bank Confirmation via Public Reporting
- **Public sources:** [Security Affairs](https://securityaffairs.com/180513/data-breach/seychelles-commercial-bank-reported-cybersecurity-incident.html)

---

## August 2025

### 06 August 2025
#### 🇹🇳 Tunisia - Yasat (yasat.tn)
- **Incident type:** Data Leak
- **Actor / Group:** RainbowDF
- **Sector:** Technology / Multimedia Distribution
- **Website:** yasat.tn
- **Status:** Claim - Data Sample Published
- **Victim Description:** Tunisian wholesale platform for multimedia services and digital subscriptions, serving as a supplier to many local shop owners and resellers.
- **Analysis:** AFRINTEL reviewed the structured data referenced in the actor's claim, corresponding to production database exports from Yasat's wholesale IPTV/satellite-TV subscription platform, including beIN Sports-branded products and generic IPTV offerings with M3U stream-link fields. The reviewed tables comprise 52,733 invoice line items (products, quantities, pricing, discounts, tax, paid/due amounts), 46,522 general sales records including customer mobile numbers, email addresses and IPTV stream (M3U) links, 8,623 beIN-specific sales records with similar customer contact fields, 211 customer profile records (last/first name, company, address, phone, gender, date of birth) and a 22-record user/account table containing a password field. The combined dataset indicates tens of thousands of exposed customer and transaction records, creating a significant risk of subscription-service fraud, credential reuse and targeted phishing against Yasat's reseller and customer base. AFRINTEL does not reproduce any customer names, contact details, stream links or credentials from the reviewed sample.

### 06 August 2025
#### 🇰🇪 Kenya - KenGen
- **Ransomware Group:** qilin
- **Sector:** Energy / Critical Infrastructure (Electricity Generation)
- **Website:** www.kengen.co.ke
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Kenya Electricity Generating Company PLC (KenGen) is Kenya's main electricity producer, supplying approximately 70% of the country's power.
- **Analysis:** AFRINTEL reviewed a local set of documents associated with this claim. The sample includes internal KenGen contract-management records for a geothermal training centre construction project (a contract implementation team memo, an official purchase order and a bank performance-bond letter from a commercial bank), a detailed CAPEX budget schedule for the Geothermal Development division, a payroll-style financial ledger, an employee roster from the Geothermal Development department listing employee identifiers, names, gender, job titles and grade levels, a signed tender confidentiality declaration tied to an internal ICT procurement, an official letter from Kenya's Ministry of Energy and Petroleum addressed to the CEOs of KenGen and other national energy-sector entities regarding a human-resource and research-and-development framework, and an engineering floor-plan drawing of a plant auxiliary/switch room. The documents share consistent KenGen letterhead, stamps, signatures and cross-referenced contract numbers across independently structured files, which increases confidence that the sample originates from KenGen's internal systems. The dataset combines employee personal data, internal financial and procurement records, engineering documentation and correspondence with national energy-sector institutions, indicating exposure spanning multiple internal systems rather than a single application. AFRINTEL does not reproduce employee names, identifiers, signatures or monetary values from the sample and does not independently confirm the intrusion.

### 06 August 2025
#### 🇲🇦 Morocco - New Era Com
- **Incident type:** Data Leak
- **Actor / Group:** Chucky_BF
- **Sector:** Telecoms / Infrastructure / IT Services
- **Website:** neweracom.ma
- **Status:** Data Fully Published
- **Victim Description:** Moroccan company specializing in telecom engineering, network infrastructure installation, and ERP/CRM solutions. The actor published a 607 MB SQL dump containing over 476,000 records.

### 08 August 2025
#### Egypt - Multiple government and institutional portals
- **Actor / Group:** Hider_Nex / Keymous Plus (claim)
- **Sector:** Government / Administration
- **Website:** Multiple Egyptian government and institutional portals
- **Incident date:** 8 August 2025 - reported DDoS campaign date
- **Initial publication date:** 8 August 2025
- **Status:** Claim - OSINT Availability Evidence
- **Incident type:** DDoS
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Victim Description:** The reported campaign targeted multiple Egyptian government and institutional web services.
- **Analysis:** A DDoS campaign was claimed against several Egyptian government and institutional services, with service unavailability reported. The attribution remains self-claimed and independent validation for every target was not available in the supplied audit. AFRINTEL records the campaign as one incident with explicit caveats.
- **Source type:** Secondary CTI + Availability Evidence
- **Public sources:** [CyHawk Africa](https://cyhawk-africa.com/ddos/multiple-egyptian-government-and-institutional-websites-allegedly-attacked-by-hacktivist-group/)

### 09 August 2025
#### 🇳🇬 Nigeria - Zenith Bank Plc
- **Actor / Group:** KaruHunters
- **Sector:** Banking / Financial Services
- **Website:** zenithbank.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** One of the largest financial institutions in Nigeria and Anglophone Africa, listed on the Nigerian and London Stock Exchanges. The actor claims exfiltration and sale of over 1.8 million customer records, together with employee data. AFRINTEL reviewed a local CSV sample containing 18 data rows and eight columns covering index, code, identifier, name, amount, address, telephone and email fields. No raw values are reproduced.

### 11 August 2025
#### 🇿🇦 South Africa - Body Graphics Tattoo Supply
- **Incident type:** Data Leak
- **Actor / Group:** N1KA
- **Sector:** Retail / E-commerce
- **Website:** bodygraphicstattoosupply.co.za
- **Source publication date:** 11 August 2025
- **Status:** Data Fully Published
- **Victim Description:** Major online retailer based in Johannesburg, specializing in the supply of professional tattoo equipment and aftercare products in South Africa.
- **Analysis:** AFRINTEL reviewed two structured export files referenced in a post observed on DarkForums, together totaling 6,501 records, matching the volume claimed by the actor. The dataset corresponds to a WordPress/WooCommerce customer and administrator export, including login names, email addresses, hashed passwords (phpass format), physical addresses, phone numbers, IP addresses, browser user-agent strings and session tokens. The structural consistency between the claimed volume and the reviewed files, together with fields matching the victim's e-commerce platform, supports a high confidence assessment, and the publication identifies the source account as N1KA. AFRINTEL does not reproduce any customer names, contact details, addresses or credentials from the reviewed sample.

### 13 August 2025
#### 🇩🇿 Algeria - Cevital
- **Ransomware Group:** akira
- **Sector:** Agribusiness / Industry / Logistics
- **Website:** www.cevital.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Leader in the agrifood industry in Algeria, active in electronics, steel, glass, and distribution.

### 17 August 2025
#### 🇿🇦 South Africa - SYSPRO
- **Ransomware Group:** warlock
- **Sector:** Technology (Software Publisher)
- **Website:** syspro.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** SYSPRO is a South African ERP (Enterprise Resource Planning) software publisher, providing integrated management solutions for manufacturing and distribution companies.

### 18 August 2025
#### 🇺🇬 Uganda - Uganda Electricity Transmission Company Limited
- **Ransomware Group:** qilin
- **Sector:** Energy (Electricity)
- **Website:** https://www.uetcl.go.ug / www.uetcl.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Ugandan public company responsible for electricity transmission.

### 18 August 2025
#### 🇹🇳 Tunisia - International Freight & Commerce
- **Ransomware Group:** direwolf
- **Sector:** Logistics
- **Website:** ifc-tunisie.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Tunisian company providing maritime, air, and land transport services, as well as logistics management and customs formalities for importing and exporting companies.

### 20 August 2025
#### 🇿🇦 South Africa - Netstar South Africa (second attack)
- **Ransomware Group:** incransom
- **Sector:** Technology / Telematics / IoT Security
- **Website:** www.netstar.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Netstar, a subsidiary of the Altron group, is the pioneer of the stolen vehicle recovery (SVR) industry in South Africa.
- **Analysis:** AFRINTEL previously recorded a claim against this same company by devman on 23 May 2025. This second claim, published roughly three months later by a different actor, could reflect either a genuine separate intrusion or a republication/resale of the earlier claim; AFRINTEL has not independently confirmed which scenario applies.

### 23 August 2025
#### 🇪🇬 Egypt - TEAM4 Security
- **Incident type:** Data Leak
- **Actor / Group:** GhostCrawl
- **Sector:** Security Services / Defense / Human Resources
- **Website:** team4security.com
- **Status:** Claim - Data Sample Published
- **Victim Description:** Egyptian company specializing in private security services, infrastructure protection, and risk management consulting. TEAM4 Security is a multi-dimensional security company established in 2017, operating out of the UK and Egypt, offering integrated digital and physical security, human guarding and professional K-9 systems, and targeting critical infrastructure, safe cities, government and defense-sector clients.
- **Analysis:** AFRINTEL reviewed the leak batches published by the actor GhostCrawl on DarkForums; the forum thread's own posting timestamps run from 29 to 31 August 2025 (part 1 posted 29 August 2025, 23:55), slightly later than this file's detection date of 23 August. The material corresponds to an exfiltrated administrative/support mailbox (contacts, inbox and sent email in .eml/.mbox format) together with several hundred attached office documents and images across the five batches. Reviewed samples include monthly payroll spreadsheets for security personnel across multiple 2025 pay periods (guards, supervisors and K-9 unit staff), a detailed HR/payroll record listing employee number, full name, national ID number, post/role, birth date, hiring date, social insurance, fixed and variable salary and bonus fields for over twenty staff, internal incident memoranda (including a theft-investigation report dated 3 November 2024), monthly manpower and staff-evaluation forms, an internal phone-extension directory, and individual employee case documents, alongside official company letterhead confirming TEAM4 Security's Egypt head office and branch office addresses. The combination of national ID numbers, birth dates, hiring dates and salary data for security guard personnel creates a significant risk of identity fraud and targeted social engineering against staff, while the internal incident and site-operations records could expose details relevant to protected client sites. AFRINTEL does not reproduce any employee names, national ID numbers, salary figures or other personal data from the reviewed sample.

### 25 August 2025
#### 🇲🇺 Mauritius - SWAN Mauritius
- **Ransomware Group:** qilin
- **Sector:** Insurance / Financial Services
- **Website:** www.swan.mu / swanforlife.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** SWAN (Swan General Ltd and Swan Life Ltd) is the market leader in insurance and financial services in Mauritius.

### 25 August 2025
#### 🇹🇬 Togo - Government Infrastructures
- **Incident type:** Access Sale
- **Actor / Group:** BIGBROTHER
- **Sector:** Government / Critical Infrastructures
- **Website:** gouv.tg
- **Status:** Claim - Data Sample Published
- **Victim Description:** Official portal and digital infrastructures of the Togolese Republic, hosting administrative services and state data.
- **Analysis:** Material corroborates the actor's claim, including the DarkForums listing itself and several elements showing active administrative access across multiple Togolese government digital platforms: the DSNIC identity and civil-status management system (justice.xflow.gouv.tg), a Nextcloud-based government file-sharing and collaboration platform (cloud.numerique.gouv.tg) with shared folders and configuration files, a KoboToolbox data-collection instance (kf.form.gouv.tg) hosting dozens of active government surveys and forms, and an education-statistics reporting system (stateduc.planifeducation.gouv.tg). The material shows genuine administrative-level access to live dashboards rather than a public-facing sample, consistent with the actor's description of the offer as a "0day vulnerability" granting privileged access. This breadth of access across distinct systems and subdomains under the gouv.tg domain supports a high confidence assessment of an active, unremediated compromise affecting multiple government digital services, independent of the actor's Monero-based pricing claim, which AFRINTEL cannot verify. AFRINTEL does not reproduce any credentials, configuration values, citizen data or session details from the reviewed material.
---
[August 2025 report](./report/README.md)

### 27 August 2025
#### Morocco - Multiple Moroccan websites (OurSec campaign)
- **Actor / Group:** OurSec (claim)
- **Sector:** Not specified
- **Website:** Multiple Moroccan websites
- **Incident date:** 27 August 2025 - reported campaign date; secondary publication on 31 August
- **Initial publication date:** 31 August 2025
- **Status:** Claim - OSINT Corroborated
- **Incident type:** Defacement
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** The reported campaign involved multiple Moroccan websites allegedly defaced in a coordinated hacktivist action.
- **Analysis:** OurSec claimed the defacement of multiple Moroccan websites. Defacement messages/images and archive references were reported, but the supplied audit recommends validating each affected domain and timestamp independently. AFRINTEL therefore records the campaign with medium confidence and retains the actor as a claim.
- **Source type:** Secondary CTI + Archive References
- **Public sources:** [CyHawk Africa](https://cyhawk-africa.com/ddos/oursec-claims-responsibility-for-moroccan-website-defacements/)

### 30 August 2025
#### Egypt - cg.eg; gags.gov.eg; kayani.gov.eg; shmft.gov.eg
- **Actor / Group:** BIGBROTHER (claimed seller)
- **Sector:** Government / Administration
- **Website:** cg.eg / gags.gov.eg / kayani.gov.eg / shmft.gov.eg
- **Incident date:** 30 August 2025 - reported date of the access-sale publication
- **Initial publication date:** 30 August 2025
- **Status:** Claim - Marketplace Listing / Screenshots
- **Incident type:** Access Sale
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Victim Description:** Unauthorized access to four Egyptian government-related domains was advertised for sale.
- **Analysis:** An actor advertised unauthorized access to four government-related domains for sale, with screenshots referenced in the secondary report. The validity of the access was not independently confirmed. The record is not merged with the separate January ransomware record concerning gags.gov.eg because the evidence describes a distinct access-sale publication at a different time.
- **Source type:** Secondary CTI + Marketplace Screenshots
- **Public sources:** [CyHawk Africa](https://cyhawk-africa.com/initial-access/alleged-sale-of-access-to-four-egyptian-government-sites/)

## September 2025

### 02 September 2025
#### 🇩🇿 Algeria - Université des Frères Mentouri Constantine 1 (UMC1)
- **Incident type:** Data Leak
- **Actor / Group:** Fire Wire
- **Sector:** Education / Higher Education
- **Website:** university-dz.net
- **Status:** Claim - Data Sample Published
- **Victim Description:** Université des Frères Mentouri Constantine 1 (UMC1) is a major Algerian public university. The claiming actor states an exfiltration of over 10 GB, a volume AFRINTEL did not collect or analyze. The reviewed files, exfiltrated via what appears to be a shared academic web platform (university-dz.net), include Master 2 semester 1 (January 2025) exam schedules with dates, modules, rooms and departments; a set of over 200 detailed student records (full name, university enrollment number, TD group and per-subject grades, including exclusion/pass status annotations) from L1 students (2015-2016 cohort); a vehicle compliance directory with phone numbers and emails; and a conference template listing contacts and affiliations for a 2024 academic event (NCME). The combination of academic records, personal contact details and administrative documents creates a significant risk of identity fraud, targeted phishing and vishing against students, staff and affiliated contacts. The claiming actor identifies itself as "Fire Wire".

### 03 September 2025
#### Morocco - Government portals + Maroc Telecom (campaign)
- **Actor / Group:** Keymous (claim)
- **Sector:** Government / Administration
- **Website:** Multiple government portals / Maroc Telecom
- **Incident date:** 3 September 2025 - reported campaign date; secondary publication on 10 September
- **Initial publication date:** 10 September 2025
- **Status:** Claim - OSINT Availability Evidence
- **Incident type:** DDoS
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Victim Description:** The reported campaign affected Moroccan government portals and telecommunications services, including references to Maroc Telecom.
- **Analysis:** Multiple Moroccan government portals and telecommunications services were reportedly disrupted during a claimed DDoS campaign, including HTTP 522-525 errors and timeouts. Attribution is self-claimed and the exact target scope remains incompletely validated. AFRINTEL records one campaign incident with medium confidence.
- **Source type:** Secondary CTI + Availability Evidence
- **Public sources:** [CyHawk Africa](https://cyhawk-africa.com/ddos/multiple-government-websites-reportedly-disrupted-in-retaliatory-cyber-campaign/)

### 04 September 2025
#### 🇳🇬 Nigeria - MobileSub
- **Actor / Group:** Not specified
- **Sector:** Fintech / Payment Services
- **Website:** [mobilesub.com.ng](https://mobilesub.com.ng)
- **Source file date:** 4 September 2025
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** MobileSub is a Nigerian digital-services platform providing mobile airtime, data, utility, cable-TV, betting and related payment functions.
- **Analysis:** AFRINTEL reviewed a local SQL dump of approximately 14.3 MB containing 42 tables and 306 INSERT blocks. The schema includes user accounts, KYC, API keys, transaction history, transfers, airtime, data, electricity, examination registration, betting, cable-TV and other payment-service modules, as well as user backup tables. The source file timestamp is 4 September 2025; this is treated as the AFRINTEL discovery/source timestamp, not proof of the original compromise date. The dataset may expose customer identity, contact, KYC, transaction and authentication-related information. No personal values, API keys or credentials are reproduced. The authenticity, completeness and publication context remain unverified.
- **Source analysis note:** The dump contains credential- and secret-sensitive table categories; AFRINTEL did not attempt authentication, access or secret recovery.

### 05 September 2025
#### 🇪🇬 Egypt - MeamarGroup
- **Ransomware Group:** obscura
- **Sector:** Real Estate / Construction / Engineering
- **Website:** https://meamargroup.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** MeamarGroup (including Meamar Real Estate Development and Meamar Construction) is a major player in the Egyptian construction sector for over 25 years. Based in Cairo (New Cairo), the group manages over 400 projects ranging from luxury residential complexes to industrial and medical facilities (like the Biogeneric Pharma factory).
- **Analysis:** AFRINTEL reviewed a local server-side filesystem archive (491 files and directories, all owned by the www-data web-server account) consistent with this claim. Directory-level timestamps for this collection cluster around 05 September 2025, matching this entry's claim date, while the bulk of the underlying files carry an earlier timestamp of 27 August 2025, suggesting an initial data-staging event ahead of the public claim. The reviewed content includes multi-year internal accounting workbooks, an extensive sales call-center/prospect-contact archive, employee CVs and internal design/CAD material for real-estate projects. A nested archive contains original files alongside copies bearing the `.obscura` ransomware encryption extension, directly supporting a file-encryption stage rather than an exfiltration claim alone. A short text file consistent with a Tor negotiation-portal countdown was also present. The combination of web-server ownership, internally consistent timestamps and actor-encrypted file copies supports a very high confidence assessment of a genuine compromise of MeamarGroup's internal file environment. AFRINTEL does not reproduce any client name, contact number, employee name or financial figure from the reviewed material.

### 06 September 2025
#### 🇨🇮 Ivory Coast - NSIA Assurances
- **Incident type:** Data Leak
- **Actor / Group:** Tanaka
- **Sector:** Insurance / Financial Services
- **Website:** https://www.nsiaassurances.com
- **Status:** Claim - Unverified
- **Victim Description:** Leader in insurance and banking in West and Central Africa, a systemic player based in Abidjan, Ivory Coast. The actor claims to be circulating a database of over 2.5 million transactional and financial records; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 08 September 2025
#### 🇳🇬 Nigeria - The Promise Nigeria
- **Ransomware Group:** yurei
- **Sector:** Catering / Food Services / Industrial Catering
- **Website:** https://www.thepromisenig.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** The Promise is a leading Quick Service Restaurant (QSR) chain and industrial catering service in Nigeria, particularly established in Port Harcourt and the Niger Delta region.

### 09 September 2025
#### 🇲🇦 Morocco - Dolidol
- **Ransomware Group:** TheGentlemen
- **Sector:** Manufacturing Industry / Bedding / Furniture
- **Website:** https://www.dolidol.ma
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Dolidol (a subsidiary of the Palmeraie Industries et Services group) is the undisputed leader in bedding and polyurethane foam in Morocco.

### 09 September 2025
#### 🇿🇼 Zimbabwe - Proplastics Limited
- **Ransomware Group:** TheGentlemen
- **Sector:** Manufacturing Industry (Plastics)
- **Website:** https://www.proplastics.co.zw
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Proplastics Limited is the leading manufacturer and supplier of plastic piping systems (PVC, HDPE) in Zimbabwe.
- **Analysis:** The supplied local evidence set contains 63 files associated with Proplastics, including PDFs, spreadsheets, image files and text files. Filenames indicate business records covering invoices and credit memos, account balances, bills of materials, backorders, deliveries, sales analysis and branch reporting. The files carry dates spanning 2023-2024, while the directory metadata places the collection in September 2025; these timestamps are treated as evidence context, not as a confirmed intrusion or publication date. The material supports the plausibility and potential sensitivity of the September 2025 claim, but does not independently establish the access vector, the complete scope of the dataset or the attribution to TheGentlemen. AFRINTEL does not reproduce names, account details, financial values, customer records or document contents.

### 10 September 2025
#### 🇳🇬 Nigeria - Princeps Credit Systems Limited
- **Ransomware Group:** killsec
- **Sector:** Finance
- **Website:** https://princepsfinance.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Financial institution based in Lagos, specializing in consumer credit and SME financing.

### 11 September 2025
#### 🇳🇦 Namibia - Epia Financial Services
- **Ransomware Group:** radar
- **Sector:** Financial Services
- **Website:** https://epiafs.com
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Financial institution based in Windhoek, offering wealth management, investment advice, and brokerage services in Namibia.
- **Analysis:** Exfiltrated mailbox material attributed to the claim (email correspondence sent to and from EPIA's reception and administration mailboxes with Bank Windhoek/Capricorn Group, First National Bank of Namibia and NamPost regarding client account verifications) is examined, together with the structure of a representative sample of pension fund administration files at the field/column level, without opening or extracting individual member-level rows. The reviewed material corresponds to EPIA's role as administrator for the Namibia Building Workers Pension Fund (NBWPF) and other corporate clients. Membership data workbooks (e.g. a January 2025 extract) contain multiple sheets of several thousand member records each (Actives, Deferred, Unclaimed, Exits) sharing a consistent field schema: member number, surname, first name, other names, company reference, date of birth, national ID number, passport number, contributor status, member status, employer name, gender, employment and fund-membership dates, monthly and annual salary, fund credit amount and date, last contribution date, exit date and payment details. A separate actuarial data extract covers the period September 2022 to April 2024 with a comparable schema and scale. Additional files inspected structurally include multi-year admin and income-allocation reports (aggregate financial transaction summaries per period) and signed client authorization forms, the most recent dated June 2025. AFRINTEL did not open every file in the set; the consistent file-naming pattern and email correspondence indicate the same categories of records recur across the full 2022-2025 period. The combination of national identification numbers, dates of birth, salary and pension fund-credit data for several thousand individuals, together with employer and banking correspondence, represents a high-impact exposure. The breadth, continuity through mid-2025 and organisational specificity of the reviewed material support a high confidence assessment of mailbox and file compromise, independent of the ransomware group's public claim. The local evidence set contains 73 files totaling approximately 79.8 MB, including spreadsheets, reports, presentations, a DOCX employer file and image files. The January 2025 membership workbook contains a summary sheet and member-state worksheets (Actives, Deferred, Unclaimed and Exits), with worksheet dimensions reaching 8,652 summary rows and up to 35 columns; the reviewed field structure includes member, employer, identity, employment, salary, pension-credit, contribution, exit and payment fields. The actuarial extract contains 8,168 rows and 167 columns for a period extending from September 2022 to April 2024. Material timestamped 11 September 2025 is consistent with the September discovery context. No member names, identification numbers, account details, signatures, salary figures or correspondence content are reproduced from the reviewed sample.

### 11 September 2025
#### 🇦🇴 Angola - Angola Government Employees Database (pape.gov.ao)
- **Incident type:** Data Leak
- **Actor / Group:** privilege
- **Sector:** Government / Public Administration
- **Website:** [pape.gov.ao](https://pape.gov.ao)
- **Status:** Claim - Data Sample Published
- **Victim Description:** The source presents pape.gov.ao as an Angolan government-related platform and claims to offer employee records from different sectors and administrative areas.
- **Analysis:** The publication dated 11 September 2025 claims a database of 245 Angolan government employees and lists fields for employee identifiers, names, dates of birth, administrative area and function. The local TXT file supplied for review contains 244 non-empty comma-separated lines, including one header and approximately 243 data rows, with six fields per row. This supports the existence of a structured employee-data sample but does not independently confirm the advertised total, the exact government body, the dataset's authenticity or its completeness. AFRINTEL does not reproduce any names, identifiers, dates of birth or other personal data from the file.

### 12 September 2025
#### 🇨🇩 Congo (DRC) - Public Administration Reform Fund (FRAP)
- **Incident type:** Data Leak
- **Actor / Group:** privilege
- **Sector:** Government / Administration
- **Website:** [frap.cd](https://frap.cd/)
- **Status:** Data Fully Published
- **Victim description:** Body responsible for modernizing public administration in the DRC.
- **Analysis:** AFRINTEL reviewed the DarkForums listing itself, posted on 12 September 2025 by the threat actor privilege (VIP tier, account created September 2025), titled "FRAP.CD - 1,136 LINES | Full User Data | Gov/Staff Access". The post describes a database of 1,136 records comprising usernames and hashed passwords (multiple hash formats), personal identifiers (first name, last name, gender), contact details (email, phone) where available, internal reference and document-designation fields, and system metadata (creation time, last login, last password update, created/updated by, account status). The actor describes the material as covering administrator and sector-staff accounts on the FRAP.CD portal, consistent with the platform's role in managing administrative profiles and internal staff accounts for the Public Administration Reform Fund. The full dataset is offered through an external hosted link rather than shown directly in the post; AFRINTEL was unable to independently validate the hosted file's authenticity or completeness. Given the account credentials and personal identifiers described, exposure of this material would create a risk of credential-based access to the portal and of targeted phishing against DRC public administration staff. AFRINTEL does not reproduce any usernames, passwords, personal identifiers or contact details from the reviewed post.

### 14 September 2025
#### 🇰🇪 Kenya - Office Of The Registrar Of Political Parties
- **Ransomware Group:** qilin
- **Sector:** Public administrations
- **Website:** https://www.orpp.go.ke
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Kenyan state body responsible for the registration, regulation, and supervision of political party funding.

### 16 September 2025
#### 🇰🇪 Kenya - Jubilee Life Insurance
- **Ransomware Group:** warlock
- **Sector:** Insurance / Financial Services
- **Website:** https://jubileelife.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Major player in life insurance and fund management in Kenya, a subsidiary of Jubilee Holdings Limited.

### 17 September 2025
#### 🇪🇬 Egypt - Accflex ERP
- **Ransomware Group:** arcusmedia
- **Sector:** Technology / ERP Software Publishing
- **Website:** https://www.accflex.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Egyptian publisher of integrated management solutions (accounting, HR, production) used by numerous companies in the Middle East and Africa.

### 22 September 2025
#### 🇲🇦 Morocco - Fractalite (fractalite.com)
- **Ransomware Group:** killsec
- **Sector:** Technology / Digital Services / Software Development
- **Website:** https://fractalite.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Fractalite is a Moroccan digital consulting and engineering agency, specializing in software development and digital support for businesses.

### 24 September 2025
#### 🇳🇬 Nigeria - Kolomoni Microfinance Bank
- **Actor / Group:** Not specified
- **Sector:** Microfinance / Banking
- **Website:** [kolomonimfb.com](https://kolomonimfb.com)
- **Source archive date:** 24 September 2025
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Kolomoni Microfinance Bank is a Nigerian financial institution serving account holders through digital and microfinance banking services.
- **Analysis:** AFRINTEL reviewed the supplied RAR extraction and its Kolomoni CSV. The file contains 37,825 data rows and 12 columns covering account name and number, email, phone, gender, date of birth, account status, address, local-government area, state, last login and record date. The combination of financial identifiers, contact details, demographic fields, location and authentication metadata creates risks of phishing, account takeover, identity fraud and targeted financial scams. The archive timestamp is 24 September 2025, while the internal CSV metadata includes an earlier 24 August 2025 file date; neither proves the original compromise date. No personal values are reproduced. The actor, publication venue, authenticity and completeness remain unspecified or unverified.

### 29 September 2025
#### 🇸🇳 Senegal - Direction Générale des Impôts et des Domaines (DGID)
- **Ransomware Group:** BlackShrantac
- **Sector:** Public Administration / Finance / Taxation
- **Website:** https://www.impots.gouv.sn
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** The **DGID** is the central agency of Senegal's Ministry of Finance and Budget, responsible for tax collection, national domain management, and the land registry (cadastre). The ransomware group claims to have leaked 1 terabyte (1 TB) of sensitive data, including structured tax databases, land registries and taxpayer banking information; AFRINTEL observed the claim on the actor's site but did not collect or analyze the underlying data.

### 30 September 2025
#### 🇪🇬 Egypt - Telecom Egypt (TE Data)
- **Incident type:** Data Leak
- **Actor / Group:** KILLUAX
- **Sector:** Telecommunications
- **Website:** te.eg
- **Status:** Claim - Data Sample Published
- **Victim Description:** Telecom Egypt operates the TE Data broadband/ISP service. The reviewed sample contains RADIUS-style session accounting records (subscriber usernames in tedata.net.eg format, NAS IP addresses, MAC addresses, assigned IP addresses, session start/stop times and connection type). Only a small number of records (36) were available for review, which limits assessment of the total scope; the exposure could nonetheless support subscriber identification and network reconnaissance.

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

## November 2025

### 04 November 2025
#### 🇲🇦 Morocco - DOVERN Import
- **Ransomware Group:** spacebears
- **Sector:** Logistics
- **Website:** https://dovern-import.com/
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Import company based in Morocco, specializing in the distribution of fine wines, spirits, and prestige champagnes.

### 04 November 2025
#### 🇿🇦 South Africa - Wannabees (wannabees.co.za)
- **Incident type:** Data Leak
- **Actor / Group:** Unknown
- **Sector:** Human Resources / Recruitment
- **Website:** wannabees.co.za
- **Status:** Claim - Data Sample Published
- **Victim Description:** Wannabees appears to be a South African recruitment and temporary-employment platform, based on the structure and content of the reviewed applicant database.
- **Analysis:** AFRINTEL reviewed two identical files from the provided evidence set (DB.txt and HoJmS, matching by SHA-256), containing a five-record applicant export. The schema includes applicant identifiers, national identity numbers, names, addresses, phone numbers, email fields, dates of birth, nationality, employment history, current occupation, salary expectations and remuneration-related fields, alongside a password field. The sample is structurally consistent with a recruitment or staffing database and contains highly sensitive personal and employment information. The files are dated 4 November 2025 in the evidence directory; this is treated as the discovery/evidence date, not as a confirmed publication or intrusion date. The available material does not identify a threat actor, forum, access method or complete dataset volume. AFRINTEL records the case as a data-leak claim with a published sample and does not reproduce names, identity numbers, contact details, passwords or other raw personal data.

### 05 November 2025
#### 🇨🇮 Ivory Coast - Anka (Anka.africa)
- **Actor / Group:** Spirigatito
- **Sector:** Logistics
- **Website:** https://www.anka.africa/
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** Leading Ivorian platform facilitating export, payments, and logistics for African creators and merchants to the global market.
- **Analysis:** The forum post advertises the sale of a database attributed to Anka, claiming 537,877 unique users and a 12.1 GB volume, with a stated field list of id, username, fullname, email, token, avatar, gender, date of birth and phone, among others. AFRINTEL reviewed structured sample extracts derived from the sample published with the post, comprising a small number of individual user records (fewer than 30). The reviewed schema matches the field list advertised in the post, extending it with additional attributes: last sign-in date, account lock and deletion flags, account type, purchase count and amount, wallet balance, and marketplace seller-sales fields. Reviewed records show account-creation timestamps ranging from May 2017 to May 2024, currencies including EUR, USD and GMD, and locales in French and English, consistent with an international user base for an African cross-border e-commerce and payments platform. The structural consistency between the advertised field list and the reviewed sample, and the plausibility of the record values (multi-year timestamps, mixed currencies, mixed locales), support raising this case from an unverified claim to a claim with a published data sample. AFRINTEL has not independently verified the claimed total volume of 537,877 users / 12.1 GB, the origin or method of compromise, or the actor's separate claim of $10 million in platform revenue. Exposure of this dataset would combine full names, contact details, dates of birth, gender, account tokens and wallet/purchase information, creating a significant risk of account takeover, targeted phishing and financial fraud against platform users. AFRINTEL does not reproduce any name, email address, phone number, token, username or other individual record from the reviewed sample.

### 06 November 2025
#### 🇪🇬 Egypt - ELSEWEDYELECTRIC.COM
- **Ransomware Group:** clop
- **Sector:** Technology / Industry
- **Website:** www.elsewedyelectric.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 2
- **Victim Description:** Major Egyptian manufacturer of cables, electrical systems, and engineering products.
- **Analysis:** AFRINTEL reviewed a screenshot of Clop's leak-site listing page for elsewedyelectric.com, using the group's standard victim-profile template (Headquarters, Phone, Website, Revenue and Industry fields, followed by the group's recurring boilerplate warning text). The listed company profile (revenue of approximately $4.9 billion, industry described as manufacturing, wire and cable) is consistent with Elsewedy Electric's publicly known profile as a major Egyptian cable and electrical-systems manufacturer. This listing appeared alongside numerous other multinational organisations on the same Clop leak-site page, consistent with the group's mass-exploitation campaign targeting Oracle E-Business Suite customers disclosed in 2025. The matching company profile supports a medium confidence assessment that the listing is genuine, though AFRINTEL did not review any underlying exfiltrated file, magnet link or data sample beyond the listing page itself, and the scope, volume and sensitivity of any data actually held by the actor remain unverified. AFRINTEL does not reproduce the company's headquarters address or phone number from the reviewed material.

### 06 November 2025
#### 🇿🇲 Zambia - ZANACO.CO.ZM
- **Ransomware Group:** clop
- **Sector:** Financial Services (Banking)
- **Website:** www.zanaco.co.zm
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Zambia National Commercial Bank, one of Zambia's leading commercial banks.
- **Analysis:** AFRINTEL reviewed screenshots of Clop's leak-site listing page for zanaco.co.zm, including the group's navigation bar showing this entry alongside numerous other multinational organisations (among them Logitech, The Washington Post, Trimble and Elsewedy Electric), consistent with Clop's mass-exploitation campaign targeting Oracle E-Business Suite customers disclosed in 2025. The listed company profile (revenue of approximately $337.9 million, industry described as finance/banking) is consistent with Zambia National Commercial Bank's publicly known profile. The listing uses the same standard template and boilerplate warning text observed across other Clop victim pages, supporting a medium confidence assessment that the entry is genuine, though AFRINTEL did not review any underlying exfiltrated file, magnet link or data sample beyond the listing pages, and the scope, volume and sensitivity of any customer or banking data actually held by the actor remain unverified. Given ZANACO's role as a major commercial bank, any confirmed data exposure would carry a significant risk of financial fraud and targeted phishing against its customers. AFRINTEL does not reproduce the bank's headquarters address or phone number from the reviewed material.

### 06 November 2025
#### 🇲🇦 Morocco - www.marjane.ma
- **Ransomware Group:** stormous
- **Sector:** Retail / Mass retail / E-commerce
- **Website:** www.marjane.ma
- **Status:** Data Fully Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** Groupe Marjane is the largest Moroccan mass retail group, operating hypermarkets and supermarkets.
- **Analysis:** AFRINTEL reviewed a proof screenshot published in connection with the claim made by the threat actor stormous, showing an active session on a Fortinet SSL-VPN portal dated 10 November 2025. The portal's bookmark list references internal infrastructure consistent with Marjane's corporate environment, including a marjane.ma subdomain, a Confluence wiki instance hosted under a confluence.marjane subdomain, a collaboration bookmark labelled "huddle/Store Managers" consistent with the retailer's multi-branch store-management operations, and a direct SSH bookmark to an internal host. The presence of Marjane-specific internal hostnames and a functional SSH access point supports a high confidence assessment that the screenshot reflects genuine internal network access rather than a fabricated proof. Following this initial sample, the actor reportedly published the claimed dataset in full on its leak site; AFRINTEL was unable to collect or review this subsequent publication, and its content, volume and authenticity are therefore not independently assessed. Demonstrated internal VPN and SSH-level access into the network of Morocco's largest mass-retail group creates a risk extending beyond any single data category, including potential disruption or further compromise of point-of-sale, logistics and store-management systems across Marjane's branch network. AFRINTEL does not reproduce any credential, session token, IP address or internal hostname from the reviewed material.

### 08 November 2025
#### 🇲🇦 Morocco - NARSA (Agence Nationale de la Sécurité Routière)
- **Incident type:** Data Leak
- **Actor / Group:** anisanas2
- **Sector:** Government / Transportation / Road Safety
- **Website:** Not identified with sufficient confidence
- **Status:** Claim - Data Sample Published
- **Victim Description:** NARSA is the Moroccan national agency responsible for road safety, vehicle registration and technical inspection.
- **Analysis:** AFRINTEL reviewed a structured CSV export consistent with a vehicle-registration record set, with fields including owner full name, address, national ID number (CIN), vehicle make, category, type, chassis number, engine displacement, registration-centre and circulation dates, purchase price and licence-plate number. The sample size and field structure are consistent with the claimed approximately 150,000-row dataset, though AFRINTEL could not independently confirm the claiming actor's identity or the exact total scope from the reviewed material. The combination of national ID numbers, home addresses and vehicle identification data creates a risk of identity fraud, vehicle-related fraud (including counterfeit registration documents) and physical-security risks from address exposure. AFRINTEL does not reproduce any owner names, addresses, national ID numbers or plate numbers from the reviewed sample.

### 09 November 2025
#### 🇿🇦 South Africa - Eastern Cape Department of Human Settlements (ECDHS)
- **Ransomware Group:** nightspire
- **Sector:** Public administrations / Social Housing
- **Website:** ecdhs.gov.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** The Eastern Cape Department of Human Settlements in South Africa is the provincial body responsible for housing policy, urban planning, and access to property for vulnerable populations in South Africa.

### 09 November 2025
#### 🇳🇬 Nigeria - Fidelity Pension Managers, Nigeria
- **Ransomware Group:** nightspire
- **Sector:** Financial Services (Pension Management)
- **Website:** fidelitypensionmanagers.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Nigerian pension fund manager.

### 11 November 2025
#### 🇪🇬 Egypt - Samcrete Holding
- **Ransomware Group:** clop
- **Sector:** Construction
- **Website:** www.samcrete.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Samcrete Holding is a fully integrated engineering, contracting, development, manufacturing, and investment company established in 1963.

### 17 November 2025
#### Kenya - Multiple Government of Kenya websites
- **Actor / Group:** PCP@Kenya (preliminary government attribution)
- **Sector:** Government / Administration
- **Website:** Multiple government domains
- **Incident date:** 17 November 2025 - incident date publicly confirmed by Kenyan authorities
- **Initial publication date:** 17 November 2025
- **Status:** Government Confirmed + Preliminary Actor Attribution
- **Incident type:** Defacement
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** The incident affected multiple Kenyan government websites across ministries, State House and public agencies.
- **Analysis:** Kenyan officials confirmed that on 17 November 2025 a cybersecurity incident made several government websites temporarily unavailable, and contemporary reporting documented defacement messages on multiple ministries and agencies. Initial investigations pointed to a group presenting itself as PCP@Kenya. AFRINTEL records one coordinated multi-agency Defacement incident, keeps PCP@Kenya as preliminary attribution, and does not infer data theft.
- **Source type:** Government Confirmation + Public Media
- **Public sources:** [The Star - restoration statement](https://www.the-star.co.ke/news/2025-11-17-state-websites-restored-after-cyber-breach) | [The Star - affected sites](https://www.the-star.co.ke/news/2025-11-17-hackers-take-down-key-government-websites)

### 25 November 2025
#### 🇪🇬 Egypt - LAMAICA, Egypt
- **Ransomware Group:** nightspire
- **Sector:** Wood and Building Materials Manufacturing
- **Website:** lamaica.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** LAMAICA is one of the leaders in the Egyptian market in the production of melamine faced panels, high-pressure laminates (HPL), edge bands, and furniture components.

### 26 November 2025
#### 🇪🇬 Egypt - Arabia Holding
- **Ransomware Group:** qilin
- **Sector:** Real Estate / Investment / Urban Development
- **Website:** arabia-holding.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Egyptian holding company with interests in various sectors, including real estate and management.

### 26 November 2025
#### 🇨🇮 Ivory Coast - Santé Espoir Vie Côte d'Ivoire (SEV-CI)
- **Ransomware Group:** benzona
- **Sector:** Health / NGO / Humanitarian
- **Website:** sevci.org
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Santé Espoir Vie Côte d'Ivoire (SEV-CI) is a leading Ivorian non-governmental organization. It works to improve the health of populations, with a particular focus on the fight against HIV/AIDS, tuberculosis, and the strengthening of community health systems.

### 30 November 2025
#### 🇲🇦 Morocco - Joutech
- **Incident type:** Data Leak
- **Actor / Group:** RL000
- **Sector:** Technology / Digital services (exact business activity not independently confirmed)
- **Website:** joutech.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** Joutech is a Moroccan company operating the joutech.ma domain. The reviewed file is a newsletter/contact-list export of 1,350 records, containing title, first name, last name, email address, company field, sales/marketing flags and registration date. No passwords or financial data were observed in the reviewed sample. The exposure could support targeted phishing and spam campaigns against the listed contacts; the completeness and origin of the file have not been independently confirmed.

## December 2025

### 05 December 2025
#### 🇪🇬 Egypt - 3S Software (Secured Smart Systems Overview Metrics)
- **Ransomware Group:** dragonforce
- **Sector:** Technology
- **Website:** 3s-software.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Egyptian technology service provider specializing in software development.

### 05 December 2025
#### 🇿🇲 Zambia - National Health Insurance Management Authority
- **Ransomware Group:** nova
- **Sector:** Insurance (Health)
- **Website:** https://nhima.co.zm/
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Zambian authority managing the national health insurance scheme.

### 06 December 2025
#### 🇬🇭 Ghana - Kasapreko Company Limited
- **Ransomware Group:** qilin
- **Sector:** Agribusiness / Beverages (Alcoholic and non-alcoholic)
- **Website:** www.kasapreko.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Kasapreko is one of the largest beverage manufacturers in Ghana and a major exporter throughout the ECOWAS region.

### 06 December 2025
#### 🇿🇦 South Africa - Diesel Electric
- **Ransomware Group:** qilin
- **Sector:** Automotive Distribution / Diagnostic Equipment
- **Website:** diesel-electric.co.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Diesel-Electric is one of South Africa's largest distributors specializing in automotive components, diesel injection systems, and diagnostic equipment (a major Bosch partner).

### 07 December 2025
#### 🇪🇬 Egypt - incolease.com
- **Ransomware Group:** lockbit5
- **Sector:** Finance
- **Website:** www.incolease.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Egyptian leasing company.

### 07 December 2025
#### 🇿🇦 South Africa - elundini.gov.za
- **Ransomware Group:** lockbit5
- **Sector:** Public Administration / Local Government
- **Website:** elundini.gov.za
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Elundini Local Municipality is a key administrative authority located in the Joe Gqabi District (Eastern Cape), encompassing the towns of Maclear, Ugie, and Mount Fletcher.

### 08 December 2025
#### 🇪🇬 Egypt - Arkan
- **Ransomware Group:** ransomhouse
- **Sector:** Finance / Trade
- **Website:** arkanonline.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Egyptian conglomerate, Arkan Group, active in industry, agriculture, and wholesale trade.

### 11 December 2025
#### 🇳🇬 Nigeria - Leadway Assurance / Leadway Health
- **Ransomware Group:** kazu
- **Sector:** Insurance
- **Website:** leadwayhealth.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Leadway Assurance is the largest private insurance company in Nigeria.

### 12 December 2025
#### 🇹🇳 Tunisia - Hopital La Rabta (University Hospital Center)
- **Ransomware Group:** devman
- **Sector:** Healthcare
- **Website:** www.chularabta.tn
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** La Rabta Hospital is one of the largest hospital complexes in Tunisia.

### 15 December 2025
#### 🇹🇳 Tunisia - Tunisian Society of Radiology (strtn.org)
- **Ransomware Group:** nova
- **Sector:** Health / Medical Association / Education
- **Website:** strtn.org
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** The Tunisian Society of Radiology (STR) is the reference organization for radiologists in Tunisia.

### 22 December 2025
#### 🇪🇬 Egypt - Polaris Parks
- **Ransomware Group:** direwolf
- **Sector:** Real Estate Development / Management of Industrial and Leisure Parks
- **Website:** polarisparks.com
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Polaris Parks is one of Egypt's leading private industrial park developers.

### 24 December 2025
#### 🇿🇦 South Africa - National Credit Regulator (NCR)
- **Ransomware Group:** dragonforce
- **Sector:** Public administrations (Financial Regulation)
- **Website:** www.ncr.org.za
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim Description:** South African public body responsible for regulating the consumer credit industry.
- **Analysis:** AFRINTEL reviewed a local sample of documents associated with this claim. The material includes approximately 25 individually named consumer case files consistent with debt-review/debt-counselling matters handled by the NCR, roughly 20 emails referencing named individuals together with partial identifiers resembling South African ID-number date-of-birth prefixes, and an internal enforcement memo dated 24 June 2022 from the NCR's Manager: Complaints Department to the Acting Manager: Investigations and Enforcement, opening an investigation into an entity referred to as "Debt Accord Solutions" for allegedly operating as an unregistered debt counsellor. The sample also includes an internal administrator spreadsheet tracking case-related email volumes on a near-daily to monthly basis from August 2020 through December 2024, NCR-branded logo files, regulatory forms (including a Form 29 and a written-consent document under Regulation 50(5)), a mandate document and a bank-details record. The documents are internally consistent with the NCR's branding, organisational structure (named managers and departments) and regulatory casework format. The sample indicates exposure of consumer debt-review case files, internal investigation and enforcement records, and multi-year operational tracking data, creating a material risk of identity fraud and targeted phishing against named consumers and NCR staff, as well as potential interference with ongoing regulatory investigations. AFRINTEL does not reproduce any consumer name, identifier, case file content, staff name or investigation detail from the reviewed material.

### 26 December 2025
#### 🇹🇳 Tunisia - Hopital La Rabta (second ransomware claim)
- **Ransomware Group:** qilin
- **Sector:** Healthcare
- **Website:** www.chularabta.tn
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** La Rabta Hospital is one of the largest hospital complexes in Tunisia.
- **Analysis:** AFRINTEL previously recorded a claim against this same hospital by devman on 12 December 2025. This second claim, published two weeks later by a different actor, could reflect either a genuine separate intrusion or a republication/resale of the earlier claim; AFRINTEL has not independently confirmed which scenario applies.

### 26 December 2025
#### 🇿🇼 Zimbabwe - Proplastics Limited (second ransomware claim)
- **Ransomware Group:** lockbit5
- **Sector:** Manufacturing Industry (Plastics)
- **Website:** proplastics.co.zw
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Victim Description:** Proplastics Limited is the leading manufacturer and supplier of plastic piping systems (PVC, HDPE) in Zimbabwe.
- **Analysis:** AFRINTEL previously recorded a claim against this same company by TheGentlemen on 9 September 2025. This second claim, published roughly three and a half months later by a different actor, could reflect either a genuine separate intrusion or a republication/resale of the earlier claim; AFRINTEL has not independently confirmed which scenario applies.

### 26 December 2025
#### 🇪🇬 Egypt - Yalla Tager Marketplace
- **Actor / Group:** Habibi
- **Sector:** Retail / E-commerce
- **Website:** yallatager.com
- **Incident date:** Unknown
- **Initial publication date:** 26 December 2025
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Victim Description:** Yalla Tager Marketplace is the organization explicitly named in the forum publication and associated there with the `yallatager.com` domain. The post presents the dataset as a 2025 CSV containing approximately 20,000 users.
- **Analysis:** On 26 December 2025, the actor `Habibi` published a forum entry titled **"Yalla Tager Marketplace - Database"** and presented a CSV dataset attributed to `yallatager.com`. The advertised schema includes internal IDs, names, email addresses, customer codes, shop names, customer groups, telephone numbers, interests, postal/location fields, a `Customer Since` timestamp and the originating website channel. AFRINTEL reviewed the supplied post and a text excerpt containing **23 visible records**. The sample is structurally consistent with customer and merchant records from an Egyptian marketplace: several entries identify Egypt and Egyptian governorates/cities, some telephone values use the Egyptian `+20` country code, and some profiles are marked as wholesale merchants with shop-related information. The `Customer Since` values visible in the excerpt include dates in July 2025; these are account/customer timestamps and **do not establish the date of compromise or extraction**. The claimed total of approximately **20,000 users** cannot be verified from the supplied sample. The initial-access vector, source system, extraction date, completeness of the dataset and any official confirmation remain unknown. The combination of identity, contact, location and merchant-profile data creates a credible risk of targeted phishing, smishing, impersonation and fraud. AFRINTEL does not reproduce any name, email address, telephone number, shop address or other personal record from the sample.

### 29 December 2025
#### 🇩🇿 Algeria - Oran University 1 Ahmed Ben Bella
- **Incident type:** Data Leak
- **Actor / Group:** GhostVector
- **Sector:** Education / University
- **Website:** Not specified
- **Source publication date:** 29 December 2025
- **Status:** Claim - Data Sample Published
- **Victim Description:** Oran University 1 Ahmed Ben Bella is a public higher-education institution in Oran, Algeria. The supplied post advertises a database dated 2023 with approximately 58,000 records and fields including names, birth dates, phone numbers, gender, email addresses, password hashes and nationality.
- **Analysis:** The post displays a structured sample associated with the university and identifies GhostVector as the source account. If valid, the dataset could enable identity fraud, phishing and account-targeting against students or staff. No personal record, credential, hash or contact detail is reproduced, and the claim and dataset provenance have not been independently confirmed.

### 29 December 2025
#### 🇪🇬 Egypt - 100 Watt Plast (100wattplast.com)
- **Incident type:** Data Leak
- **Actor / Group:** camillabf
- **Sector:** Industrial / Electrical and Plastic Products Manufacturing
- **Website:** [100wattplast.com](https://100wattplast.com)
- **Status:** Claim - Data Sample Published
- **Victim Description:** 100 Watt Plast is an industrial company based in Egypt, with activities also in Lebanon and Saudi Arabia, specializing in the manufacture of electrical and plastic products.
- **Analysis:** The actor camillabf published a claim on December 29, 2025 concerning 100wattplast.com, described as a dataset of 180,000 records in CSV format, comprising first name, last name, email, phone and password. The sample shown in the post displays a field schema including two password values per record: an MD5-type hash (32 hexadecimal characters) and a second, markedly more complex value of variable length, along with three additional undocumented fields (`aa`, `bb`, `already`).

  About twenty complete records are directly visible in the sample, with names, email addresses and Egyptian phone numbers tied to both password values. The consistency of the schema and the number of individual records observed support a high confidence level regarding the authenticity of this leak, although the total claimed volume of 180,000 rows could not be independently verified beyond the observed sample, and the exact nature of the second password field (alternate hash or plaintext value) could not be determined with certainty. Exposure of this data could facilitate account takeover, password reuse across other services and targeted phishing against the company's customers. AFRINTEL does not reproduce any name, email address, phone number or password value from the reviewed sample.

### 31 December 2025
#### 🇲🇦 Morocco - Pharmacie.ma
- **Incident type:** Data Leak
- **Actor / Group:** KaruHunters
- **Sector:** Healthcare / Pharmacy e-commerce
- **Website:** pharmacie.ma
- **Status:** Claim - Data Sample Published
- **Victim Description:** Pharmacie.ma is a Moroccan pharmacy directory and e-commerce platform. Two full SQL database backups, dated September 2025, were reviewed, covering the platform's full application schema (clients, addresses, drugs, pharmacists, newsletters, articles and related tables). The `clients` table structure indicates up to approximately 27,900 registered accounts (pharmacists, doctors, pharmacy staff, pharmacy students and other users) with email address, hashed password, name, professional address, city, specialty, phone/mobile numbers, country and date of birth. The volume and structure of the backups support a significant exposure of healthcare-sector professional accounts; the completeness of the extraction and its origin have not been independently confirmed.

### 31 December 2025
#### 🇰🇪 Kenya - Kenya Electricity Transmission Company (KETRACO)
- **Incident type:** Data Leak
- **Actor / Group:** LindaBF
- **Sector:** Energy / Electricity Transmission (Critical Infrastructure)
- **Website:** [ketraco.co.ke](https://ketraco.co.ke)
- **Status:** Claim - Data Sample Published
- **Victim Description:** The Kenya Electricity Transmission Company (KETRACO) is a Kenyan state corporation responsible for developing, operating and maintaining the country's high-voltage electricity transmission grid.
- **Analysis:** The actor LindaBF published a post on December 31, 2025 titled "ketraco.co.ke database Kenya", with the download link restricted to forum members who reply to the thread. The visible sample shows a structured user-directory export (fields USER_ID, USER_NAME, USER_PASSWORD, USER_FIRSTNAME, USER_LASTNAME, USER_EMAIL, USER_LASTLOGIN, USER_FLAGS, USER_OU, USER_DATECREATED) tied to an organisational-unit path labelled "nl_KETRACO_Newsletter_Unit", consistent with a newsletter-subscriber or directory-service account list rather than core operational systems. Real-looking Kenyan names, email addresses and account-creation timestamps are visible, but numerous rows in the sample share an identical password value, which is inconsistent with independently generated per-user hashes and may indicate a shared default value, a placeholder, or a partially fabricated sample; this anomaly lowers AFRINTEL's confidence in the sample to a medium level. Given KETRACO's role in national power-transmission infrastructure, any confirmed compromise, even one limited to a newsletter or directory service, would be of concern for a critical-infrastructure operator and could indicate a broader foothold. AFRINTEL does not reproduce any username, email address, password value or record from the sample and has not accessed the linked download.

---

*AFRINTEL compilation - source of truth: monthly files.*

