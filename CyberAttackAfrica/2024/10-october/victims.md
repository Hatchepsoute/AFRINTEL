# AFRINTEL Cyber Incidents - October 2024 - canonical corpus (11 records)

👉🏾 [Version française](./victims_FR.md)

> This file contains only incidents retained in canonical 2024 statistics. Historical discoveries, republications, duplicates, and unresolved-chronology cases are preserved separately at the 2024 root.


### October 3, 2024

#### 🇲🇬 Madagascar - University of Antananarivo (univ-antananarivo.mg)
- **Incident type:** System Intrusion
- **Taxonomy note:** The observed listing claims database access, but the content is locked and no sample was accessible. `System Intrusion` is retained as an unauthorized-access claim; no data leak is confirmed.
- **Actor / Group:** Unknown
- **Source context:** RainbowBF is the forum account shown as publishing the locked database-access claim.
- **Sector:** Education / University
- **Website:** [univ-antananarivo.mg](https://www.univ-antananarivo.mg)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The University of Antananarivo is Madagascar's oldest and largest public university, comprising multiple faculties and higher-education institutes in the capital region.
- **Analysis:** AFRINTEL reviewed a forum listing on the Breached platform, posted by the account RainbowBF on 3 October 2024, titled "Madagascar univ-antananarivo.mg Database Access" and tagged under the platform's "Breached" content category. The underlying content is paywalled behind the forum's internal credit system and was not unlocked by AFRINTEL; no database export, record screenshot or other verifiable sample was accessible during collection. AFRINTEL treats this as an unconfirmed claim of database access and does not confirm the existence, scope or authenticity of any underlying data. The potential affected data categories and impact cannot currently be assessed because the underlying content was not accessible. AFRINTEL does not reproduce any content from the forum listing beyond its title and metadata.

----------------------------

### October 4, 2024

#### 🇿🇦 South Africa - Enterpriseoutsourcing
- **Actor / Group:** ransomhub
- **Sector:** Technology / IT
- **Website:** [enterpriseoutsourcing.com](https://www.enterpriseoutsourcing.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Enterpriseoutsourcing is a South African organisation operating in the information technologies consulting sector.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.

### October 5, 2024

#### 🇿🇦 South Africa - Winwinza
- **Actor / Group:** ransomhub
- **Sector:** Education / University
- **Website:** [winwinza.com](https://www.winwinza.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Winwinza is a South African organisation operating in the education sector.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.

### October 7, 2024

#### 🇩🇿 Algeria - Yassir
- **Actor / Group:** killsec
- **Sector:** Technology / IT
- **Website:** [yassir.com](https://www.yassir.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Yassir is an Algerian super-app providing ride-hailing, delivery, grocery, and digital services in Algeria and across regional markets.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.

### October 9, 2024

#### 🇳🇬 Nigeria - Unidentified healthcare facilities provider
- **Actor / Group:** grep/cn
- **Source context:** The October 9 forum publication was posted by Tanaka and attributes the leak to grep/cn.
- **Sector:** Healthcare / Medical
- **Website:** Not identified
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** The source describes an unidentified Nigerian healthcare facilities provider operating across multiple facilities. The organization name and the affected facilities could not be established from the source material.
- **Analysis:** A forum publication by Tanaka dated 9 October 2024 claims that approximately 130,000 patient records from multiple Nigerian healthcare facilities were leaked by the actor grep/cn. The local workbook supplied for analysis contains 84 data rows, not 129,825 or 130,000 rows, so the advertised volume cannot be independently confirmed from the available file. The workbook contains patient-related fields including names, identifiers, telephone numbers, age, dates of birth, sex, marital status and facility-related identifiers; raw records were not reproduced. The evidence supports a healthcare data-exposure claim with a high potential impact, but the exact provider, facility scope, acquisition method, completeness and total volume remain unknown.

### October 9, 2024

#### 🇿🇦 South Africa - GMG Mining Supplies
- **Actor / Group:** sarcoma
- **Sector:** Manufacturing / Industry
- **Website:** [gmgminingsupplies.com](https://gmgminingsupplies.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** GMG Mining Machines and Supplies is a South African company specialised in the supply, reconstruction, and rental of mining equipment, rail-less mobile machines, parts, and associated services.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.

### October 9, 2024

#### 🇿🇦 South Africa - National Edging
- **Actor / Group:** sarcoma
- **Sector:** Manufacturing / Industry
- **Website:** [nationaledging.com](https://nationaledging.com)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 3
- **Victim Description:** National Edging is a South African company specialised in the supply of edgebanding, adhesives, finishing materials, and industrial components for the furniture, kitchen, and fitment sectors.
- **Analysis:** AFRINTEL reviewed a local sample of documents consistent with the claim made by the threat actor sarcoma, comprising full passport scans of at least three individuals (two South African nationals and one Indian national holding a UAE residence permit), a signed contract with Freitan Group of Companies (Pty) Ltd bearing a financial director's signature, a corporate travel-booking form referencing the legal entity National Converting Agencies (Pty) Ltd, an email address on the nationaledging.co.za domain and a South African passport and identity number, and a delivery note documenting a shipment of edging and glue products between company branches (Gauteng) with onward collection referenced in Zimbabwe. The direct reference to the nationaledging.co.za domain, together with internally consistent corporate identity (National Converting Agencies/National Edging), signed contractual material and multiple full identity documents, supports a very high confidence assessment of a genuine internal compromise. The exposure of full passport and national identity data for multiple individuals, together with signed contracts and logistics records extending into a cross-border (Zimbabwe) supply chain, creates a significant risk of identity fraud, document forgery and targeted social engineering against employees, business partners and travellers associated with the company. AFRINTEL does not reproduce any name, passport number, identity number, date of birth or contact detail from the reviewed sample.

----------------------------

- **Evidence qualification:** The reviewed sample strongly supports an internal data compromise associated with National Edging. It does not independently establish ransomware encryption, the initial access method or the full exfiltration volume.

### October 11, 2024

#### 🇬🇭 Ghana - Volta River Authority (VRA)
- **Actor / Group:** blacksuit
- **Sector:** Energy / Utilities
- **Website:** [vra.com](https://www.vra.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Volta River Authority (VRA) is Ghana's main public electricity producer, responsible for hydroelectric and thermal power plants and strategic energy infrastructure.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.

### October 16, 2024

#### 🇱🇾 Libya - Ministry of Interior (moi.gov.ly)
- **Actor / Group:** killsec
- **Sector:** Government / Administration
- **Website:** [moi.gov.ly](https://www.moi.gov.ly)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Libyan Ministry of Interior is the government institution responsible for internal security, police forces, and the management of the country's administrative and security affairs.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.

### October 21, 2024

#### 🇲🇦 Morocco - Al Massira University Residences
- **Actor / Group:** bxxxx1
- **Sector:** Education / University
- **Website:** [ruam.ma](https://ruam.ma)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak

- **Description:**
  Al Massira University Residences provide student accommodation in Kenitra. The network includes the Al Massira 1, Al Massira 2 and Al Massira 3 residences near the city’s higher education institutions.

- **Analysis:**
  A cybercriminal-forum post attributed to bxxxx1 presents email addresses associated with people who searched for or applied for accommodation through the Al Massira University Residences platform. The actor claims the data was obtained after logging into the `ruam.ma` control panel, suggesting possible compromise of an administrative account or management interface; however, the screenshot provides no technical evidence identifying the access method. The visible sample contains email addresses only, mostly from public mail services with some university, administrative or professional domains. No passwords, identity numbers, telephone numbers, student documents or financial information are visible. The post states that the data was extracted in October 2024 and includes a text-file download link and an archive or access password, neither of which AFRINTEL reproduces. No total record count, file size, price or deadline is stated, and the screenshot does not establish whether the visible list is complete. The addresses could support targeted phishing impersonating student accommodation services, fraudulent admission or payment notifications, and password-spraying target lists. Since no passwords are visible, direct account compromise cannot be inferred from the sample.

----------------------------

### October 25, 2024

#### 🇪🇬 Egypt - Matouk Bassiouny
- **Actor / Group:** raworld
- **Sector:** Legal / Justice
- **Website:** [matoukbassiouny.com](https://www.matoukbassiouny.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Matouk Bassiouny is a prominent Egyptian law firm based in Cairo, recognised for corporate law, arbitration, litigation, and legal advisory services.

----------------------------

- **Reliability note:** The card documents a ransomware publication, but the supplied material contains no technical sample or public DFIR report confirming encryption, exfiltration or operational disruption.
