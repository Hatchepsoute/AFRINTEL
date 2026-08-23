[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%7C%20Data%20Leak%20%7C%20Access%20Sale-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Cyber Attacks in Africa: November 2024: List of 16 Victims

👉🏾 [**Version française disponible ici**](./victims_FR.md)

## November 2024

## Monthly snapshot

November 2024 contains **16 documented incident records**: **12 Ransomware**, **2 Data Leak**, **2 Access Sale**, **0 DDoS**, **0 Defacement** and **0 Operational Fraud**, across **11 African countries**.

The retrospective correction adds **SABS**, a government-confirmed ransomware incident with confirmed system encryption and major operational disruption. The official record differs by one day on the incident date, so AFRINTEL preserves **20-21 November 2024**.

### November 2, 2024

#### 🇿🇦 South Africa - Sumitomo Rubber South Africa
- **Ransomware Group:** killsec
- **Sector:** Manufacturing / Industry
- **Website:** [srigroup.co.za](https://www.srigroup.co.za)
- **Status:** Claim - Data Sample Published
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Victim Description:** Sumitomo Rubber South Africa is a tyre manufacturing company operating in South Africa and affiliated with the Sumitomo Rubber Industries group.
- **Analysis:** AFRINTEL reviewed a local sample of the archive associated with this claim, comprising approximately 239,600 individual PDF files (roughly 23 GB uncompressed), each named with a random UUID rather than an original filename. The files reviewed by AFRINTEL are genuine customer statements of account issued under the letterhead of Sumitomo Rubber South Africa (Pty) Ltd, specifically its "Export DQC - Africa East (USD)" division, listing per-account transaction history (SAP invoice references, dates, credit amounts and running balances) tied to a named account number and a named export sales contact and email address on the srigroup.co.za domain. The consistent company letterhead, real contact names and SAP-linked invoice numbering across the reviewed sample, together with the very large volume and UUID-based naming pattern consistent with a bulk export from a document-management or ERP archive, support a very high confidence assessment of a genuine, large-scale compromise. Given the scale of the archive and its coverage of the company's Africa-wide export accounts-receivable records, this incident presents a risk of large-scale invoice fraud, business email compromise and competitive intelligence exposure extending to Sumitomo Rubber South Africa's export client base across the continent. AFRINTEL does not reproduce any account number, contact name, email address, invoice reference or financial figure from the reviewed material.

----------------------------

- **Evidence qualification:** The reviewed archive strongly supports a genuine large-scale internal-data compromise associated with Sumitomo Rubber South Africa. It does not independently establish the initial-access vector, ransomware encryption behavior or the full scope of any separate exfiltration beyond the reviewed archive.
### November 4, 2024

#### 🇹🇿 Tanzania - College of Business Education (CBE)
- **Ransomware Group:** hellcat
- **Sector:** Education / University
- **Website:** [cbe.ac.tz](https://www.cbe.ac.tz)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The College of Business Education (CBE) is a Tanzanian higher education institution offering programmes in business, management, accounting, and related professional fields.

----------------------------

### November 4, 2024

#### 🇸🇩 Sudan - Kenana Sugar Company
- **Ransomware Group:** ransomhub
- **Sector:** Agriculture / Agribusiness
- **Website:** [kenanasugarcompany.com](https://www.kenanasugarcompany.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Kenana Sugar Company is a major Sudanese agro-industrial complex specialised in sugarcane cultivation, sugar production, and associated agricultural and industrial activities.

----------------------------

### November 12, 2024

#### 🇲🇦 Morocco - Arab Civil Aviation Organization (ACAO)
- **Actor / Group:** Unknown
- **Source context:** Reposted by Hxp7; the November post references an earlier claim.
- **Sector:** Aviation
- **Website:** [acao.org.ma](https://acao.org.ma)
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Victim Description:** The Arab Civil Aviation Organization (ACAO) is an intergovernmental body headquartered in Rabat, Morocco, that coordinates civil aviation policy, safety and regulatory cooperation among Arab states.
- **Analysis:** A forum post dated November 12, 2024 reposts an earlier claim that the ACAO database (acao.org.ma) was compromised, referencing approximately 800 files described as database columns and an external download link. No data extract or sample was directly visible in the observed post, so the content, authenticity and scope of the alleged database cannot be assessed. AFRINTEL does not access or reproduce the linked file. This entry is recorded as an unverified claim pending independent confirmation.

----------------------------

### November 14, 2024

#### 🇳🇬 Nigeria - Environmental Design International
- **Ransomware Group:** akira
- **Sector:** Professional / Business Services
- **Website:** [environmentaldesigninternational.com](http://environmentaldesigninternational.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Environmental Design International is a Nigerian engineering and consulting firm; the claim referenced engineering, financial, and personal documents.

----------------------------

### November 17, 2024

#### 🇪🇬 Egypt - Egyptian Tax Authority (ETA)
- **Ransomware Group:** moneymessage
- **Sector:** Government / Administration
- **Website:** [eta.gov.eg](https://www.eta.gov.eg)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** The Egyptian Tax Authority (ETA) is the Egyptian public tax administration responsible for tax collection, compliance, taxpayer services, and fiscal management.

----------------------------

### November 20-21, 2024 - official sources differ by one day

#### 🇿🇦 South Africa - South African Bureau of Standards (SABS)
- **Incident date:** 20-21 November 2024 - official sources differ by one day
- **Initial publication date:** Retrospective official disclosure; exact first public date not established in reviewed sources
- **AFRINTEL correction date:** 23 August 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [sabs.co.za](https://www.sabs.co.za/)
- **Status:** Government Confirmed
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Date discrepancy note:** An official SABS presentation dates the incident to 20 November 2024, while a later ministerial parliamentary letter states 21 November 2024. AFRINTEL preserves the range instead of silently selecting one date.
- **Victim Description:** SABS is South Africa's national standards body, supporting standards development, testing, certification and related services.
- **Analysis:** Official South African government and parliamentary material confirms that SABS suffered a ransomware attack in November 2024 that encrypted information systems and caused major operational disruption. The encrypted environment prevented access to data required for audit work, delayed financial reporting and required extensive rebuilding of virtual machines and applications. Later audit reporting described a complete shutdown of business applications and prolonged recovery. The attacker was not identified in the official sources reviewed. No monetary loss, affected-record count or confirmed exfiltrated-data volume is established in the reviewed material.
- **Evidence qualification:** Encryption and operational disruption are government-confirmed. The attacker identity, initial-access vector and any data-exfiltration scope remain unestablished.
- **Public sources:** [the dtic / SABS presentation](https://www.thedtic.gov.za/wp-content/uploads/Revised-SABS-Allegations-against-the-SABS.pdf) | [Parliamentary letter](https://www.parliament.gov.za/storage/app/media/Docs/atc/01ls62wgbe2fcfr3dgmfh2s7hbu5b7hej4.pdf)

----------------------------

### November 24, 2024

#### 🇰🇪 Kenya - EFI Sales
- **Ransomware Group:** killsec
- **Sector:** Manufacturing / Industry
- **Website:** [efisales.co.ke](https://www.efisales.co.ke)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** EFI Sales is a Kenyan company in the distribution sector, associated with the supply of industrial equipment and related services.

----------------------------

### November 27, 2024

#### 🇪🇹 Ethiopia - Habesha Cement
- **Ransomware Group:** lockbit3
- **Sector:** Manufacturing / Industry
- **Website:** [habeshacement.com](https://www.habeshacement.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Habesha Cement is an Ethiopian cement company founded in 2008, specialised in cement production and construction materials for infrastructure and real estate sectors.

----------------------------

### November 27, 2024

#### 🇪🇬 Egypt - Contrack Facilities Management
- **Ransomware Group:** raworld
- **Sector:** Professional / Business Services
- **Website:** [contrackfm.com](https://www.contrackfm.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Contrack Facilities Management is an Egyptian facility management company providing maintenance, operations, and support services for corporate buildings and sites.

----------------------------

### November 28, 2024

#### 🇧🇫 Burkina Faso - Burkina Faso Public Health System Portal
- **Actor / Group:** Sentap
- **Sector:** Healthcare / Medical
- **Website:** Not specified
- **Status:** Claim - Unverified
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Access Sale
- **Description:** A forum publication describes a government-run public-health portal in Burkina Faso that may manage health personnel information, health-service reporting, vaccination campaigns, resource planning and internal communications.
- **Analysis:** The publication presents potential portal functions and categories of data, including health personnel and patient-related information, but does not provide a verifiable domain, technical access evidence or a data sample. AFRINTEL records this as an unverified access-sale claim attributed to Sentap. A possible relationship with the COVID-19 data-management system published by the same source later in November remains unconfirmed.

----------------------------

### November 28, 2024

#### 🇧🇫 Burkina Faso - Government COVID-19 Data Management System
- **Actor / Group:** Sentap
- **Sector:** Healthcare / Medical
- **Website:** Not specified
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Access Sale
- **Description:** A forum publication presents a Burkina Faso government COVID-19 data-management dashboard covering PCR and TDR results, vaccination records and historical reporting.
- **Analysis:** The screenshots show dashboard metrics, vaccination summaries and a historical-results interface, including a claimed total of approximately 3.795 million records. The publication also advertises access for sale, but the domain, provenance, completeness and authenticity of the records are not independently verified. AFRINTEL does not reproduce personal records or contact details. This claim is kept separate from the public-health portal entry because a technical link between the systems is not demonstrated.

----------------------------

### November 28, 2024

#### 🇳🇬 Nigeria - Briatek
- **Ransomware Group:** killsec
- **Sector:** Technology / IT
- **Website:** [briatek.com.ng](https://www.briatek.com.ng)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Briatek is a Nigerian technology company specialised in IT consulting, software integration, and digital solutions for organisations.

----------------------------

### November 28, 2024

#### 🇨🇲 Cameroon - Chanas Assurances S.A.
- **Ransomware Group:** fog
- **Sector:** Finance / Banking
- **Website:** [chanasassurances.com](https://www.chanasassurances.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Chanas Assurances S.A. is a Cameroonian insurance company operating in the insurance services sector.

----------------------------

### November 29, 2024

#### 🇳🇦 Namibia - Namforce Life Insurance
- **Ransomware Group:** spacebears
- **Sector:** Finance / Banking
- **Website:** [namforce.com.na](https://www.namforce.com.na)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** Namforce Life Insurance is a Namibian company specialised in life insurance products, financial protection, and risk management solutions for individuals and organisations.

----------------------------

### November 29, 2024

#### 🇿🇦 South Africa - PPOTTS
- **Ransomware Group:** ransomhub
- **Sector:** Technology / IT
- **Website:** [ppotts.com](https://www.ppotts.com)
- **Status:** Claim - Data Sample Published
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Analysis:** AFRINTEL reviewed eight screenshots from the RansomHub evidence set. The visible material includes an Uganda National Examinations Board certificate, South African pathology laboratory results and personal-credential disclosure forms containing candidate and company information. The material is sensitive, but the screenshots do not establish whether these records originated from PPOTTS directly, a customer environment, a third-party system or a wider dataset obtained through the claimed intrusion. The evidence supports recording a published sample while keeping the attribution and data provenance under review. AFRINTEL does not reproduce names, identity numbers, medical results or contact details.
- **Victim Description:** PPOTTS is a South African technology company operating in software, digital services, or enterprise technology solutions.

----------------------------

## ✍🏿 Author
*Adama ASSIONGBON*
*SOC & Cyber Threat Intelligence Consultant*
[LinkedIn profile](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)
