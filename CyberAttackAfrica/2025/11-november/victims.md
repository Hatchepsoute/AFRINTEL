[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# African victims - November 2025

👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

**15 documented cyber incidents** under AFRINTEL Taxonomy v2: Ransomware 10, Data Leak 4, Defacement 1.

> Public-source links are added to supplementary incidents identified through online research to complete the corpus. They are not retroactively imposed on historical AFRINTEL records, including Dark Web observations.

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
