[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
# List of African cyberattack victims in August 2025 (13 victims)
👉🏾 [**French version available here**](./victims_FR.md)

## Monthly snapshot

August 2025 includes **13 unique incidents**: **7 Ransomware**, **5 Data Leak**, **1 Access Sale**, **0 DDoS**, **0 Defacement** and **0 Operational Fraud**, across **10 African countries**.

> `victims_FR.md` is the editorial control file. After validation, `victims.md` is synchronized with the same facts, classifications and structured values.

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
- **Correlation note:** The same organization and domain were listed again on 26 July 2026 by ExfilSquad in a ransomware claim. This establishes an identity and temporal correlation, not a confirmed connection between the two events. The 2025 record concerns an alleged sale of 1.8 million records with a reviewed 18-row sample; the 2026 record provides no sample, volume, encryption evidence or victim confirmation. No matching archive, data schema, shared infrastructure or explicit reference links the claims. AFRINTEL therefore tracks them as related records / possible separate claims, with the relationship unresolved.

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

## ✍🏿 Author
*Adama ASSIONGBON*  
*SOC & Cyber Threat Intelligence Consultant*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)

---
*AFRINTEL - Open CTI Monitoring Initiative on Africa*
---
