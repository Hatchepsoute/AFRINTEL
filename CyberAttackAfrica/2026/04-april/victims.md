[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat%20Landscape](https://img.shields.io/badge/Threat%20Landscape-Ransomware%20%26%20Data%20Leaks-red)
![Period](https://img.shields.io/badge/Period-April%202026-lightgrey)
![Victims](https://img.shields.io/badge/Victims-60-critical)
![Ransomware](https://img.shields.io/badge/Ransomware-20-red)
![Data%20Leaks](https://img.shields.io/badge/Data%20Leaks-40-orange)
![Countries](https://img.shields.io/badge/Countries%20Affected-16-blueviolet)
![Threat%20Actors](https://img.shields.io/badge/Threat%20Actors-30%2B-darkred)
![Intel%20Type](https://img.shields.io/badge/Intel%20Type-CTI-purple)
![Status](https://img.shields.io/badge/Status-OSINT%20Monitoring-success)
# African Victims - April 2026

## Summary
- **Total victims** : 60
- **Ransomware attacks** : 20
- **Data leaks (non‑ransomware)** : 40

### Notable incidents

- **Morocco:** a database attributed to Royal Palace staff reportedly contained 3,300 records.
- **South Africa:** the Pick n Pay ASAP/Bottles.com exposure included payment-card and location data.
- **Kenya:** a ransomware claim targeting the Kenya Airports Authority cited a volume of 2 TB.
- **Benin:** a 7.1 GB mailbox publication was attributed to CNSS Benin.

> The entries below document observed claims or publications. Claimed volumes and compromises remain unconfirmed without independent evidence.

---

### April 01, 2026
#### 🇩🇿 Algeria - Ministry of Culture [Data Leak]
- **Threat Actor / Group :** Grubder
- **Sector :** Government / Culture / Public Administration
- **Website :** [m-culture.gov.dz](https://www.m-culture.gov.dz/)
- **Status :** Claim - Unverified
- **Description :** Algeria’s Ministry of Culture is the governmental institution responsible for cultural policies, artistic events, and cultural support programs. A database advertised on a cybercriminal forum allegedly exposes approximately 247,000 records related to administrative contacts, cultural event registrations, and grant applications. Exposed data includes names, emails, phone numbers, payment statuses, funding details, and application submissions.


#### 🇪🇬 Egypt - Cairo University (cu.edu.eg) [Data Leak]
- **Threat Actor / Group :** Grubder
- **Sector :** Education / University
- **Website :** [cu.edu.eg](https://cu.edu.eg/)
- **Status :** Claim - Unverified
- **Description :** Cairo University is one of Egypt’s oldest and most prestigious public universities, located in Cairo and serving hundreds of thousands of students. A database advertised on a cybercriminal forum allegedly exposes approximately 284,000 records related to students, academic enrollments, and university support systems. The exposed data reportedly includes personal information, national identification numbers, email addresses, phone numbers, academic details, enrollment records, financial statuses, and support ticket information. Preliminary analysis suggests the exposure of a university backend database used for student management, admissions, academic enrollments, and administrative support operations.
 
#### 🇪🇹 Ethiopia - National Oil Ethiopia PLC (NOC) [Data Leak]

- **Threat Actor / Group :** ByteToBreach
- **Sector :** Energy / Oil & Gas / Critical Infrastructure
- **Website :** [nationaloilethiopia.com](https://www.nationaloilethiopia.com/)
- **Leak date :** March 24, 2026 (discovered in April 2026)
- **Status :** Claim - Data Sample Published
- **Description :** National Oil Ethiopia PLC (NOC) is a major Ethiopian energy company involved in petroleum operations, fuel distribution, and related services. A cybercriminal forum post claims a full compromise of the organization’s infrastructure leading to the exfiltration of multiple databases, including a primary ERP database allegedly exceeding 800GB in size. The threat actor claims access to sensitive information including client data, contracts, salaries, email accounts, addresses, personally identifiable information (PII), and internal business operations data. The publication also describes a full intrusion chain ranging from an initial Microsoft Exchange ProxyLogon exploitation to the final deployment of ransomware. The screenshots and technical details shared by the actor suggest an advanced compromise affecting internal systems, administrative access, databases, and potentially security solutions deployed within the infrastructure.

---

### April 02, 2026
#### 🇿🇦 South Africa - singita.com [Ransomware]
- **Ransomware Group :** dragonforce
- **Sector :** Travel and tourism industry
- **Website :** [singita.com](https://singita.com)
- **Status :** Claim - Unverified
- **Description :** Singita is a luxury ecotourism and conservation brand operating high‑end lodges and private game reserves across Africa.

#### 🇿🇦 South Africa - Takealot.com [Data Leak]
- **Threat Actor / Group :** Grubder
- **Sector :** E‑commerce
- **Website :** [takealot.com](https://www.takealot.com)
- **Status :** Claim - Data Sample Published
- **Description :** South Africa’s largest online retailer. A leaked CSV file (`DeliveryAddress_South Africa.csv`) exposes detailed delivery addresses, GPS coordinates, phone numbers, and private home access instructions. Data spans until late 2023.

#### 🇿🇦 South Africa - MySchool South Africa [Data Leak]
- **Threat Actor / Group :** Grubder
- **Sector :** Education / Student Services
- **Website :** [myschool.co.za](https://www.myschool.co.za/)
- **Status :** Claim - Unverified
- **Description :** Alleged leak of ~437,000 records including student contacts, enrollments, support tickets, names, emails, phones, birth dates, payment statuses.

#### 🇹🇳 Tunisia - Fatales.tn [Data Leak]

- **Threat Actor / Group :** Grubder
- **Sector :** E-commerce / Beauty / CRM
- **Website :** [fatales.tn](https://www.fatales.tn/)
- **Status :** Claim - Data Sample Published
- **Description :** A cybercriminal forum post claims the sale of a database allegedly linked to Fatales.tn containing approximately 431,000 customer records associated with user contacts, booking history, and loyalty program operations. The threat actor states that the data is organized into multiple structured datasets covering customer management, bookings, and marketing activities.

- **Observed Data :**
  - full names
  - email addresses
  - phone numbers
  - physical addresses
  - birth dates
  - booking history
  - payment statuses and methods
  - CRM and loyalty data
  - marketing preferences and segmentation
  - VIP levels and loyalty points

- **CTI Analysis :**
  The exposed elements suggest a centralized CRM/e-commerce database used for customer management and marketing operations. The combination of personal, behavioral, and transactional data significantly increases the risks of targeted phishing, marketing fraud, mass spam campaigns, and identity theft.

- **CTI Note :**
  The full authenticity of the dataset cannot currently be independently confirmed, although the detailed CRM-oriented structure and field consistency increase the potential credibility of the claimed leak.

#### 🇹🇳 Tunisia - NSSTunis [Data Leak]
- **Threat Actor / Group :** Grubder
- **Sector :** Services / CRM
- **Website :** [nsstunis.com](https://www.nsstunis.com/)
- **Status :** Claim - Unverified
- **Description :** ~312,000 records with names, emails, phones, family info, product interests, marketing statuses, demographic data.


#### 🇪🇬 Egypt - Ain Shams University (ums.asu.edu.eg)  [Data Leak]

- **Threat Actor / Group :** Grubder
- **Sector :** Education / University
- **Website :** [ums.asu.edu.eg](https://ums.asu.edu.eg/)
- **Status :** Claim - Unverified
- **Description :** Ain Shams University is one of Egypt’s leading public universities, located in Cairo and widely recognized for its academic and research programs. A database advertised on a cybercriminal forum allegedly exposes approximately 563,000 records related to students, academic enrollments, and authentication systems. The exposed data reportedly includes personal information, email addresses, phone numbers, university identifiers, enrollment details, academic program information, financial statuses, and identity verification or authentication-related records. Preliminary analysis suggests the exposure of a university backend database used for student management, enrollment operations, and academic verification mechanisms.
---

### April 03, 2026
#### 🇪🇬 Egypt - United Finance Egypt [Ransomware]
- **Ransomware Group :** payload
- **Sector :** Finance
- **Website :** [uf-eg.com](https://uf-eg.com)
- **Status :** Claim - Unverified
- **Description :** Egyptian non‑bank financial institution (NBFI) offering leasing, factoring, and mortgages. The attack compromised its entire infrastructure and exposed customer data.

---

### April 04, 2026
#### 🇧🇼 Botswana - lkc.ac.bw [Ransomware]
- **Ransomware Group :** krybit
- **Sector :** Academic Institutions
- **Website :** [lkc.ac.bw](https://lkc.ac.bw)
- **Status :** Claim - Unverified
- **Description :** Livingstone Kolobeng College, a private secondary school in Gaborone, Botswana.

#### 🇪🇬 Egypt - AUG Pharma [Ransomware]
- **Ransomware Group :** dragonforce
- **Sector :** Pharmacy and drugs manufacturing
- **Website :** [augpharma.com](https://augpharma.com)
- **Status :** Claim - Unverified
- **Description :** Egyptian pharmaceutical company developing and commercialising innovative products.

#### 🇦🇴 🇿🇦 🇳🇬 Africa - Government Data Leak and Administrative Access Sale [Data Leak]

- **Threat Actor / Group :** superduper1
- **Sector :** Government / Defense / Healthcare / Intelligence
- **Status :** Claim - Unverified
- **Web site :** N/A
- **Description :** A cybercriminal forum post advertises the sale of access to multiple government mailboxes, administrator panels, and institutional accounts linked to African public entities.

- **Observed Countries :**
  - 🇦🇴 Angola
  - 🇿🇦 South Africa
  - 🇳🇬 Nigeria

- **Claimed Accesses :**
  - eGov administrator panels
  - Angolan national police mailboxes
  - government medical domains in Angola
  - military and intelligence-related access
  - South African government accounts
  - South African sports department accounts
  - Nigerian government staff accounts

- **CTI Analysis :**
  The published elements potentially suggest resale of compromised credentials or persistent access to African governmental infrastructures. Risks include institutional spear phishing, espionage, Business Email Compromise (BEC), and compromise of official communications.

- **CTI Note :**
  No technical evidence currently allows independent verification of the claimed accesses.
---
  
### April 05, 2026
#### 🇸🇳 Senegal - Directorate General of Public Accounting and Treasury (DGCPT) [Claimed Government Access]

- **Threat Actor / Group :** w00l_ysh1
- **Sector :** Government / Public Finance
- **Web site :** [sentresor.org](https://www.sentresor.org/)
- **Status :** Claim - Unverified
- **Initial publication date :** March 08, 2026
- **Discovery date :** April 05, 2026

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
### April 06, 2026
#### 🇪🇬 Egypt - gas.mercedes-benz.com.eg [Ransomware]
- **Ransomware Group :** lockbit5
- **Sector :** Automotive
- **Website :** [gas.mercedes-benz.com.eg](https://gas.mercedes-benz.com.eg)
- **Status :** Claim - Unverified
- **Description :** German Auto Service, an authorised Mercedes‑Benz dealer in Giza, Egypt.

#### 🇳🇬 Nigeria - Welfare.org.ng [Data Leak]
- **Threat Actor / Group :** Citizen / NormalLeVrai
- **Sector :** NGO / Social Welfare
- **Website :** [welfare.org.ng](https://welfare.org.ng/)
- **Status :** Claim - Unverified
- **Description :** Nigerian platform for community services. Claimed compromise of main website and subdomains, with alleged access to emails, source code, backups, and a database of >12,000 records.

---

### April 08, 2026
#### 🇪🇬 Egypt - El Wastani Petroleum Company (WASCO) [Ransomware]
- **Ransomware Group :** payload
- **Sector :** Oil
- **Website :** [egyptoil-gas.com](https://egyptoil-gas.com)
- **Status :** Claim - Unverified
- **Description :** Egyptian oil and gas company focused on exploration, production, and processing in the Nile Delta and North Sinai.

#### 🇪🇬 Egypt - ACE Consulting Engineers [Ransomware]
- **Ransomware Group :** thegentlemen
- **Sector :** Engineering consulting
- **Website :** [ace-mb.com](https://ace-mb.com)
- **Status :** Claim - Unverified
- **Description :** International engineering consultancy and project management firm, founded in 1950, operating in over 35 countries.

#### 🇲🇦 Morocco - CNOPS [Data Leak]
- **Threat Actor / Group :** JBT2026 (relayed by Jabaroot)
- **Sector :** Healthcare / Health Insurance / Public Administration
- **Website :** [cnops.org.ma](https://www.cnops.org.ma/)
- **Status :** Claim - Unverified
- **Description :** Moroccan public health insurance institution. A leak of >3 million records exposes full names, membership numbers, national ID (CIN), and complete addresses of insured individuals.

---

### April 09, 2026
#### 🇸🇨 Seychelles - egov.sc [Ransomware]
- **Ransomware Group :** apt73/bashe
- **Sector :** Government and administrations
- **Website :** [egov.sc](https://egov.sc)
- **Status :** Claim - Unverified
- **Description :** Official e‑government portal of the Republic of Seychelles.

#### 🇿🇦 South Africa - megasurf.co.za [Ransomware]
- **Ransomware Group :** krybit
- **Sector :** Internet Service providers
- **Website :** [megasurf.co.za](https://megasurf.co.za)
- **Status :** Claim - Unverified
- **Description :** South African ISP and data centre operator offering fibre and wireless broadband.

---

### April 12, 2026
#### 🇲🇦 Morocco - OFPPT [Data Leak]
- **Threat Actor / Group :** anisanas2
- **Sector :** Vocational Training / Education
- **Website :** [ofppt.ma](https://www.ofppt.ma)
- **Status :** Claim - Unverified
- **Description :** Morocco’s main public vocational training institution. Exposed data: full names, phone numbers, emails, national ID (CNI), Massar code, city, status, activity logs.

#### 🇲🇦 Morocco - Moroccan Identity Documents (Passports/KYC) [Data Leak]
- **Threat Actor / Group :** Arnoldsudney
- **Sector :** Digital Identity / Official Documents
- **Website :** N/A
- **Status :** Claim - Unverified
- **Description :** A cybercriminal forum post offers Moroccan passports, ID cards, verification selfies, driving licences, and full KYC packages.

---

### April 13, 2026
#### 🇰🇪 Kenya - ifmis.go.ke [Ransomware]
- **Ransomware Group :** apt73/bashe
- **Sector :** Central administration and government
- **Website :** [ifmis.go.ke](https://ifmis.go.ke)
- **Status :** Claim - Unverified
- **Description :** Kenya’s Integrated Financial Management Information System for national and county governments.

#### 🇲🇦 Morocco - GET / GENERAL ELECTRIC TRADING (gemaroc.com) [Data Leak]
- **Threat Actor / Group :**  bxxxx1
- **Sector :** Industrial Services / IT Infrastructure
- **Website :** [gemaroc.com](https://gemaroc.com/)
- **Status :** Claim - Data Sample Published
- **Description :** Moroccan technical services company. A SQL dump (September 2024) includes Dolibarr ERP/CRM, WordPress databases, HR records, financial data, and internal logs.

---

### April 14, 2026
#### 🇬🇭 Ghana - International Maritime Hospital [Ransomware]
- **Ransomware Group :** thegentlemen
- **Sector :** Healthcare services
- **Website :** [imah.gov.gh](https://imah.gov.gh)
- **Status :** Claim - Unverified
- **Description :** Government‑affiliated hospital in Tema, Ghana, specialising in maritime and general health services.


#### 🇲🇦 Morocco - Alleged Royal Palace Staff Database (Dar El Makhzen) [Data Leak]

- **Threat Actor / Group :** Rihana
- **Sector :** Government / Royal Household
- **Website :** N/A (institution)
- **Status :** Claim - Data Sample Published
- **Description :** A cybercriminal forum post claims the sale of a database allegedly linked to Moroccan Royal Palace staff (Dar El Makhzen). The analyzed sample contains approximately 3,300 records including multiple categories of sensitive personal and administrative information.

- **Observed Data Elements :**
  - Full names
  - Birth dates
  - Birth places
  - Gender
  - Nationality
  - Moroccan CNIE identification numbers
  - Physical addresses
  - Recruitment dates

- **Preliminary CTI Analysis :**
  The analyzed data structure potentially suggests extraction from:
  - an internal HR database,
  - a personnel management system,
  - or a centralized administrative dataset.

  The simultaneous exposure of:
  - national identity numbers,
  - physical addresses,
  - recruitment dates,
  - and detailed biographical information

  significantly increases the risk of:
  - targeted social engineering,
  - identity theft,
  - spear-phishing,
  - document fraud,
  - or impersonation operations targeting sensitive institutional personnel.

- **CTI note :**
  At this stage, the full authenticity of the dataset and its exact origin cannot be independently verified. However, the structured HR-oriented fields, administrative consistency, and homogeneous dataset formatting increase the potential credibility of the claimed leak. 
---

### April 16, 2026
#### 🇪🇬 Egypt - orientalweavers.com [Ransomware]
- **Ransomware Group :** payload
- **Sector :** Manufacturing
- **Website :** [orientalweavers.com](https://orientalweavers.com)
- **Status :** Claim - Unverified
- **Description :** One of the world’s largest manufacturers of carpets and rugs, headquartered in Cairo.

#### 🇰🇪 Kenya - Kenya Airports Authority (KAA)  [Data Leak]

- **Threat Actor / Group :** RubiconH4ck
- **Sector :** Aviation / Transportation / Critical Infrastructure
- **Website :** [kaa.go.ke](https://www.kaa.go.ke/)
- **Status :** Claim - Unverified
- **Description :** Kenya Airports Authority (KAA) is the Kenyan public organization responsible for managing and operating the country’s main airports, including strategic aviation infrastructure and related services. A cybercriminal forum post claims the sale of approximately 2TB of data allegedly linked to the organization. The threat actor states that the dataset includes information systems, user data, internal services, and complete user addresses. The publication suggests a potential compromise affecting critical infrastructure associated with Kenya’s aviation sector. Although the publicly exposed evidence remains limited, the claimed data volume and the nature of the information mentioned could represent significant risks to operational security, data confidentiality, and aviation-related infrastructure.
---

### April 19, 2026
#### 🇿🇦 South Africa - Sunspray Food [Ransomware]
- **Ransomware Group :** thegentlemen
- **Sector :** Food and drinks businesses
- **Website :** [sunspray.co.za](https://sunspray.co.za)
- **Status :** Claim - Unverified
- **Description :** South Africa’s largest independent manufacturer of spray‑dried food ingredients.

#### 🇲🇦 Morocco - Al Barid Bank [Data Leak]
- **Threat Actor / Group :** Sejjil
- **Sector :** Banking / Financial Services
- **Website :** [albaridbank.ma](https://www.albaridbank.ma/)
- **Status :** Claim - Data Sample Published
- **Description :** Moroccan bank. Claimed leak of internal financial logs (2025) showing instant transfers, direct debits, branch info, and phone numbers. Sample contains transaction timestamps, amounts, and post‑transaction balances.

#### 🇲🇦 Morocco - Chezpara.ma [Data Leak]
- **Threat Actor / Group :** Richard2002
- **Sector :** Online Pharmacy / Healthcare E‑commerce
- **Website :** [chezpara.ma](https://chezpara.ma/)
- **Status :** Claim - Unverified
- **Initial publication date :** February 23, 2026
- **Discovery Date :** April 19, 2026
- **Description :** ~400,000 customer records including names, phone numbers, detailed addresses, delivery info, and order comments.
---

### April 20, 2026
#### 🇪🇬 Egypt - Better House [Ransomware]
- **Ransomware Group :** payload
- **Sector :** Construction
- **Website :** [betterhouse-eg.com](https://betterhouse-eg.com)
- **Status :** Claim - Unverified
- **Description :** Egyptian real estate developer with over 150 projects.

#### 🇲🇦 Morocco - SUPTECH SANTÉ [Data Leak]
- **Threat Actor / Group :** xNov
- **Sector :** Education / Training / Health Technologies
- **Website :** suptech-sante.ma
- **Status :** Claim - Unverified
- **Description :** Moroccan higher education institution in biomedical engineering. Leak of >231 student dossiers including national ID cards, diploma scans, emails, phones, Massar codes, and registration details.

---

### April 21, 2026
#### 🇲🇦 Morocco - LNM6 (National Laboratory Mohammed VI) [Data Leak]
- **Threat Actor / Group :** anisanas2 
- **Sector :** Healthcare / Medical Laboratory
- **Website :** N/A
- **Status :** Claim - Data Sample Published
- **Description :** Multidisciplinary medical laboratory. Exposed PDF medical reports include full patient identity, biological test results (HIV, HPV, STIs, tuberculosis, hormonal, genetic), paediatric and neonatal data.

#### 🇳🇬 Nigeria - Federal Housing Authority (FHA) [Data Leak]
- **Threat Actor / Group :** 0xLei / Nullsec
- **Sector :** Public Administration / Housing
- **Website :** [fha.gov.ng](https://www.fha.gov.ng/)
- **Status :** Claim - Unverified
- **Description :** Nigerian government agency for public housing. ~170 MB of source code, backend files, configurations.

#### 🇳🇬 Nigeria - EFCC [Data Leak]
- **Threat Actor / Group :** ki4t / Nullsec Nigeria
- **Sector :** Law Enforcement / Anti‑corruption
- **Website :** [efcc.gov.ng](https://www.efcc.gov.ng/)
- **Status :** Claim - Data Sample Published
- **Description :** Nigeria’s Economic and Financial Crimes Commission. Exposed user accounts, emails, phones, internal roles, bcrypt password hashes, internal IPs, agent data.


#### 🇲🇦 Morocco - Royal Moroccan Football Federation (FRMF) [Data Leak]
- **Threat Actor / Group :** MDGhost
- **Sector :** Sports
- **Website :** [frmf.ma](https://frmf.ma/)
- **Status :** Claim - Data Sample Published
- **Description :** 1.2 TB of data allegedly for sale ($10,000 USD). Sample exposes player licensing records, full identities, addresses, phone numbers, sports IDs, and data on minors.


#### 🇲🇦 Morocco - Pharmacie.ma [Data Leak]
- **Threat Actor / Group :** Tanaka
- **Sector :** Healthcare / Pharmacy / E-health
- **Website :** [pharmacie.ma](https://www.pharmacie.ma)
- **Status :** Claim - Data Sample Published
- **Discovery Date:** April 21, 2026
- **Victim Description :**  
  Pharmacie.ma is a Moroccan online portal focused on pharmaceutical information, medicines, and healthcare-related content. The platform primarily targets pharmacists, pharmacy students, and users seeking medical information in Morocco.

- **Leak Description :**  
  On January 27, 2026, a user identified as “Tanaka” published a claim on an underground forum attributed to the threat actor “Karuhunters”, alleging that a breach occurring on September 29, 2025 resulted in the exfiltration of approximately 41,772 user records associated with Pharmacie.ma.
- **Sample Analysis :**  
  The analyzed SQL samples contain email addresses, names, phone numbers, “pharmacy_student” profiles, geographic information, and account status data.
- **CTI Note :**  
  The observed data appears to correspond to a historical user database associated with Pharmacie.ma. The exact claimed leak size remains independently unverified.

#### 🇲🇦 Morocco - Al Akhawayn University (AUI) [Data Leak]

- **Threat Actor / Group :** anisanas2
- **Sector :** Education / University
- **Website :** [Al Akhawayn University (AUI)](https://aui.ma/)
- **Status :** Claim - Unverified
- **Initial Publication Date :** February 08, 2026
- **Discovery Date :** April 21, 2026

- **Description :** A cybercriminal forum post claims the leak of a database allegedly linked to Al Akhawayn University (AUI), a Moroccan university located in Ifrane and considered one of the country’s leading academic institutions.

- **CTI Analysis :**
  The threat actor claims that a previously reported AUI breach was “fabricated” and presents this new dataset as “verified and authentic”.

  The observed elements suggest a potential compromise involving academic or administrative systems related to:
  - students,
  - user accounts,
  - administrative databases,
  - or internal university platforms.

  Such leaks may expose:
  - student personal data,
  - institutional email addresses,
  - academic information,
  - internal access data,
  - or reusable credentials across other systems.

- **CTI Note :**
  The full authenticity of the dataset has not been independently verified at this stage. However, the targeted institution is considered strategically important within Morocco’s academic ecosystem, increasing risks related to spear phishing, university account compromise, and BEC-style attacks targeting students, faculty members, or administrative staff.
---

### April 22, 2026
#### 🇲🇦 Morocco - Equatorial Coca-Cola Bottling [Ransomware]
- **Ransomware Group :** worldleaks
- **Sector :** Food and drinks businesses
- **Website :** [eccbc.com](https://eccbc.com)
- **Status :** Claim - Unverified
- **Description :** Bottling partner of The Coca‑Cola Company operating in North and West Africa.
---
### April 25, 2026
#### 🇧🇯 Benin - CNSS Benin [Data Leak]

- **Threat Actor / Group :** NormalLeVrai
- **Sector :** Government / Social Security
- **Website :** [cnss.bj](https://www.cnss.bj/)
- **Status :** Claim - Data Sample Published

- **Description :** A cybercriminal forum post claims the leak of data extracted from the official `info@cnss.bj` mailbox belonging to Benin’s National Social Security Fund (CNSS). The publication references approximately 5,993 emails, 9,019 attachments, and more than 31,000 analyzed files totaling around 7.1GB of sensitive data.

- **Observed Data :**
  - pension cards
  - certificates of life
  - passports and consular cards
  - identity documents
  - beneficiary files
  - HR and medical data
  - financial and banking information
  - sensitive administrative records

- **CTI Analysis :**
  The published elements suggest an automated mailbox scraping and mass attachment extraction operation. The exposed data creates significant risks related to identity theft, social security fraud, spear phishing, and exploitation of sensitive information linked to insured individuals and retirees.
---

### April 26, 2026
#### 🇪🇬 Egypt - EEC Group [Ransomware]
- **Ransomware Group :** thegentlemen
- **Sector :** Manufacturing
- **Website :** [eecegypt.com](https://eecegypt.com)
- **Status :** Claim - Unverified
- **Description :** Egyptian engineering, construction, and steel structure manufacturing conglomerate.

#### 🇲🇦 Morocco - Regional Investment Center Rabat‑Salé‑Kénitra (CRI) [Data Leak]
- **Threat Actor / Group :** kutam_dz
- **Sector :** Public Administration / Investment / Legal
- **Website :** [cri-rsk.ma](https://www.cri-rsk.ma/)
- **Status :** Claim - Data Sample Published
- **Description :** Moroccan public institution for investment promotion. Exposed professional records, mainly notaries: full names, multiple phone numbers, postal addresses, emails, province, profession.

#### 🇹🇳 Tunisia - Tawjih.tn [Data Leak]
- **Threat Actor / Group :** mecrobyte
- **Sector :** Education / Academic Guidance
- **Website :** [tawjih.tn](https://tawjih.tn/)
- **Leak Date :** April 26, 2026
- **Status :** Claim - Data Sample Published
- **Description :** Tawjih.tn is a Tunisian academic guidance platform mainly designed to help students and baccalaureate graduates plan their educational and career paths. The threat actor alleges possession of user-related information potentially including personal and academic data. Although the full dataset is not publicly exposed in the analyzed publication, the visible elements suggest a potential compromise affecting a backend database used for user account management and academic guidance services.

---

### April 27, 2026
#### 🇪🇬 Egypt - alx-pc.com [Ransomware]
- **Ransomware Group :** apt73/bashe
- **Sector :** Oil
- **Website :** [alx-pc.com](https://alx-pc.com)
- **Status :** Claim - Unverified
- **Description :** Alexandria Petroleum Company, a state‑owned oil refining company.

#### 🇬🇭 Ghana - providentgh.com [Ransomware]
- **Ransomware Group :** apt73/bashe
- **Sector :** Wealth Management
- **Website :** [providentgh.com](https://providentgh.com)
- **Status :** Claim - Unverified
- **Description :** Private insurance company in Ghana (Provident Insurance).

#### 🇺🇬 Uganda - Ministry of Agriculture (E‑Extension) [Data Leak]
- **Threat Actor / Group :** vicmeow
- **Sector :** Government / Agriculture
- **Website :** [extension.agriculture.go.ug](https://extension.agriculture.go.ug/)
- **Status :** Claim - Data Sample Published
- **Description :** Ugandan digital agricultural platform. Exposed emails, names, phones, addresses, weak/plaintext passwords, and an API token for SMS gateway.

#### 🇳🇬 Nigeria - Oyo State Ministry of Trade, Industry, Investment and Cooperatives [Data Leak]
- **Threat Actor / Group :** AckLine
- **Sector :** Public Administration / Trade
- **Website :** oyostate.gov.ng
- **Status :** Claim - Unverified
- **Description :** ~275,000 commercial ID cards (21.5 GB compressed) including full names, birth dates, addresses, professions, and facial photos. High risk of identity theft and KYC fraud.

---

### April 29, 2026
#### 🇲🇦 Morocco - planetsport.ma [Ransomware]
- **Ransomware Group :** lockbit5
- **Sector :** Sports
- **Website :** [planetsport.ma](https://planetsport.ma)
- **Status :** Claim - Unverified
- **Description :** Planet Sport is Morocco’s leading sports goods retailer operating a nationwide network of stores distributing international sports brands.

#### 🇿🇲 Zambia - zsiclife.co.zm [Ransomware]
- **Ransomware Group :** krybit
- **Sector :** Insurance services
- **Website :** [zsiclife.co.zm](https://zsiclife.co.zm)
- **Status :** Claim - Unverified
- **Description :** Zambian life insurance and wealth management company.

#### 🇲🇦 Morocco - Royal Moroccan Tennis Federation (FRMT) [Data Leak]
- **Threat Actor / Group :** Keymous
- **Sector :** Sports
- **Website :** [frmtennis.ma](https://frmtennis.ma/)
- **Status :** Claim - Unverified
- **Description :** Tennis federation. ~20,000 records of licensed players and club members: names, surnames, club affiliations, gender.

#### 🇲🇦 Morocco - List of 4 Million Moroccan Email Addresses  [Data Leak]
- **Threat Actor / Group :** Rihana
- **Sector :** Personal Data / Email Marketing / Data Aggregation
- **Website :** N/A
- **Status :** Claim - Unverified
- **Description :** A cybercriminal forum post claims the release of a dataset containing approximately 4 million email addresses associated with Moroccan users. The threat actor states that the data is mainly intended for spammers and email marketers. The publication references several popular domains commonly used in Morocco, including Gmail, Hotmail, Outlook, Yahoo, and Menara.ma. No specific organization is directly identified as the source of the leak, suggesting the dataset may originate from aggregated collections of multiple breaches, OSINT harvesting, or historical data leaks. Such datasets may be leveraged for phishing campaigns, mass spam operations, credential stuffing, or targeted social engineering activities.
---
### April 30, 2026
#### 🇹🇳 Tunisia - Exscape App [Data Leak]

- **Threat Actor / Group :** forrest
- **Sector :** Mobile Application / Social Network
- **Status :** Claim - Data Sample Published
- **Leak Date :** January 17, 2026 (discovered in April 2026)

- **Description :** A cybercriminal forum post claims the sale of a database allegedly linked to Exscape App containing approximately 5,000 Tunisian user profiles.

- **Observed Data :**
  - usernames
  - full names
  - email addresses
  - phone numbers
  - birth dates
  - gender
  - user biographies
  - GPS coordinates
  - subscription levels
  - age categories

- **CTI Analysis :**
  The exposed data suggests a leak originating from a mobile/social application backend containing precise geolocation information and potentially minor user profiles (“TEEN15”). Risks include doxxing, digital stalking, targeted phishing, and identity correlation through geolocation analysis.

- **CTI Note :**
  The dataset authenticity cannot currently be independently verified, although the observed structure appears consistent with a mobile application backend database.
  

#### 🇩🇿 Algeria - Algeria Post [Data Leak]

- **Threat Actor / Group :** BlueEx
- **Sector :** Postal Services / Government / Telecommunications
- **Website :** [poste.dz](https://www.poste.dz/)
- **Leak Date :** January 29, 2026 (discovered in April 2026)
- **Status :** Claim - Data Sample Published

- **Description :** A cybercriminal forum post claims the sale of more than 500,000 records allegedly linked to Algeria Post. The published samples include personal information associated with Algerian citizens as well as photographs of Algerian national identity cards.

- **Observed Data :**
  - full names
  - email addresses
  - phone numbers
  - photographs of national identity cards
  - associated personal information

- **CTI Analysis :**
  The exposed data suggests a leak involving sensitive personal information potentially linked to Algerian postal or administrative services. The simultaneous exposure of:
  - contact information,
  - identity-related data,
  - and official documents

  significantly increases the risks of:
  - identity theft,
  - administrative fraud,
  - targeted phishing,
  - SIM swapping,
  - or fraudulent account and service creation.

- **CTI Note :**
  The full authenticity of the dataset cannot currently be independently verified. However, the presence of structured samples, coherent personal data, and identity document photographs increases the potential credibility of the claimed leak.
  

#### 🇿🇦 South Africa - Northern Cape Department of Roads & Public Works [Data Leak]
- **Threat Actor / Group :** wh6ami
- **Sector :** Government / Public Infrastructure / Transportation
- **Website :** *.gov.za
- **Leak Date :** March 16, 2026 (discovered in April 2026)
- **Status :** Claim - Data Sample Published
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


#### 🇿🇦 South Africa - Buffalo City Metropolitan Municipality [Data Leak]

- **Threat Actor / Group :** wh6ami
- **Sector :** Government / Municipal Administration
- **Website :** *.gov.za
- **Leak Date :** March 13, 2026 (discovered in April 2026)
- **Status :** Claim - Data Sample Published

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
  

#### 🇿🇦 South Africa - Pick n Pay ASAP / Bottles.com [Data Leak]

- **Threat Actor / Group :** p4pr1k4
- **Sector :** E-commerce / Delivery / Retail
- **Website :** bottles.com
- **Leak Date :** March 23, 2026 (discovered in April 2026)
- **Status :** Claim - Data Sample Published

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

#### 🇩🇿 Algeria - Inter Partner Assistance Algeria [Data Leak]

- **Threat Actor / Group :** dark07x
- **Sector :** Insurance / Automotive Assistance / Assistance Services
- **Website :** [ipassistance-dz.com](https://ipassistance-dz.com)
- **Status :** Claim - Data Sample Published
- **Initial Publication Date :** January 19, 2026
- **Discovery Date :** April 30, 2026

- **Description :** A cybercriminal forum post claims the compromise of the official website of Inter Partner Assistance Algeria, a company specialized in automotive, travel, healthcare, and insurance assistance services.

- **Observed Exposed Documents :**
  - automobile accident reports,
  - Algerian national identity cards,
  - vehicle insurance information,
  - automotive expertise reports,
  - CRMA service orders,
  - personal contact information,
  - official signatures and stamps,
  - vehicle registration numbers,
  - driver and vehicle information,
  - internal administrative documents.

- **CTI Analysis :**
  The exposed documents contain sensitive personal and administrative information that could potentially enable:
  - identity theft,
  - insurance fraud,
  - document forgery,
  - targeted spear phishing,
  - or abuse of vehicle and administrative information.

  Several artifacts also reveal the exposure of official document scans and files related to real automobile accident cases.

- **CTI Note :**
  The published screenshots appear to indicate access to internal portals and customer/partner data. However, the full authenticity of all claimed accesses has not yet been independently verified.


#### 🇩🇿 Algeria - Algiers Regional Football League (LRFA) / Foot’Up [Data Leak]

- **Threat Actor / Group :** dark07x
- **Sector :** Sports / Sports Federation
- **Website :** [lrfa.org.dz](https://lrfa.org.dz)
- **Affected Platform :** Foot’Up
- **Status :** Claim - Data Sample Published
- **Initial Publication Date :** January 16, 2026
- **Discovery Date :** April 30, 2026

- **Description :** A cybercriminal forum post claims the compromise of the official management platform of the Algiers Regional Football League (LRFA). The actor claims to have extracted data related to several Algerian football clubs and regional football administrative infrastructures.

- **Clubs Mentioned in the Artifacts :**
  - Omar Ansar Club
  - Wifaq Sour Ghozlane
  - Chabab Amel Kouba

- **Observed Exposed Data :**
  - national identity cards,
  - sports licenses and records,
  - player information,
  - coach and management data,
  - match sheets,
  - administrative documents,
  - internal forms,
  - official signatures and stamps,
  - Foot’Up administrative interfaces,
  - scanned personal documents.

- **CTI Analysis :**
  The published elements suggest access to a centralized sports management platform containing sensitive administrative and personal information related to multiple Algerian football clubs.

  The screenshots also reveal:
  - access to the Foot’Up administration portal,
  - directories containing numerous scanned documents,
  - and files potentially linked to players, managers, and regional sports organizations.

  The exposed information could facilitate:
  - identity theft,
  - document fraud,
  - targeted spear phishing,
  - compromise of sports ecosystems,
  - or abuse of internal administrative information.

- **CTI Note :**
  The threat actor claims to possess broad access to Algeria’s regional football infrastructure. However, the full scope of the compromise and the authenticity of all claimed accesses cannot be independently verified at this stage.
  
