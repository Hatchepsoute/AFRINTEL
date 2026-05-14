# African victims - May 2026

### May 01, 2026
#### 🇪🇹 Ethiopia - National Oil Ethiopia PLC (NOC) [Data Leak]

- **Threat Actor / Group :** MDGhost
- **Sector :** Energy / Oil & Gas / Critical Infrastructure
- **Website :** [nationaloilethiopia.com](https://www.nationaloilethiopia.com/)
- **Status :** Claimed Full Compromise / Technical Publication and Data Sale
- **Victim Description :** National Oil Ethiopia PLC (NOC) is a strategic Ethiopian energy company involved in petroleum operations, fuel distribution, and national energy services. A cybercriminal forum post discovered on May 01, 2026 claims a full compromise of the organization’s infrastructure leading to the exfiltration of multiple critical databases totaling approximately 1.3TB of data. The threat actor claims the intrusion started through a Microsoft Exchange ProxyLogon vulnerability before obtaining broad access to internal systems, Active Directory servers, ERP databases, and network infrastructure. The allegedly stolen data includes customer information, contracts, salaries, emails, financial records, inventory data, production information, personally identifiable information (PII), and internal business operations data.

- **Preliminary Technical Analysis :**
  - Main ERP database claimed: ~800GB
  - Total claimed data size: ~1.3TB
  - Number of tables: 512
  - `transaction` table: ~45.6 million records
  - `production data` table: ~98.7 million records
  - `financial record` table: ~23.4 million records
  - `inventory` table: ~12.3 million records

- **Observed Infrastructure Elements :**
  - Active Directory environment `noc.com.et`
  - Windows Server 2008 R2 and 2012 R2 systems identified
  - Multiple legacy Windows XP hosts still active
  - Accessible LDAP, SMB, RDP, Exchange, MySQL, and web services
  - References to Metasploit reverse shells and Ligolo tunneling
  - Mention of final ransomware deployment after full compromise

- **CTI Assessment :**
  The claimed exposure suggests a long-term and advanced compromise of the internal environment with potentially severe impact on:
  - energy operations,
  - financial systems,
  - industrial and logistics infrastructure,
  - and customer/employee data confidentiality.

- **IoC / Technical Artifacts Mentioned :**  
  Internal domain observed: `noc.com.et`  
  Hosts observed: `V-HOF-ADC`, `BACKUPSRV`, `SRVBACKUP`, `S-HOF-TMG-001`  
  Mentioned vulnerability: Microsoft Exchange ProxyLogon  
  Mentioned tools: Metasploit, Ligolo :contentReference[oaicite:1]{index=1}

### CTI Note

This victim has been the subject of **two separate claims by different cybercriminal actors** :

1. **ByteToBreach** - initial publication dated March 24, 2026  
2. **MDGhost** - new publication observed on May 01, 2026

Both publications claim:
- a full compromise of National Oil Ethiopia PLC (NOC) infrastructure,
- exfiltration of massive databases,
- ERP-related data,
- financial and operational information,
- as well as extensive access to the internal environment.

The published technical elements share multiple similarities (large ERP databases, Active Directory environment, business data, ProxyLogon exploitation, internal access), which may suggest:
- resale or republication of the same dataset,
- shared access between threat actors,
- secondary leakage following the initial compromise,
- or separate operations leveraging the same historical intrusion.

At this stage, it is not possible to confirm with certainty whether both actors had independent access or if this is a reuse of the same underlying data corpus.
---
### May 04, 2026
#### 🇩🇿 Algeria - Ministry of Pharmaceutical Industry [Data Leak]

- **Threat Actor / Group :** kamalsheikhxx
- **Sector :** Government / Healthcare / Pharmaceutical Industry
- **Status :** Claimed Full Dump Publication

- **Description :** A cybercriminal forum post claims the leak of approximately 34.3GB of data allegedly linked to the Algerian Ministry of Pharmaceutical Industry, including more than 52,000 files and 17,800 folders covering the 2019–2025 period.

- **Observed Data :**
  - drug import reports
  - invoices and customs declarations
  - pharmaceutical commercial registers
  - personal data of company officials
  - official authorizations
  - pharmaceutical inventories
  - psychotropic substance lists
  - PDF, Excel, Word, and ZIP files

- **CTI Analysis :**
  The exposed data suggests potential compromise of sensitive regulatory, commercial, and administrative records linked to Algeria’s pharmaceutical sector. Risks include economic espionage, document fraud, and exploitation of sensitive regulatory information.

- **CTI Note :**
  The published document structure and file categories increase the potential credibility of the claimed leak.
---
### May 06, 2026
#### 🇿🇦 South Africa - Consumer Goods Council of South Africa (CGCSA) [Data Leak]

- **Threat Actor / Group :** XOverStm / Stormous
- **Sector :** Retail / Distribution / Industry Council
- **Website :** [cgcsa.co.za](https://www.cgcsa.co.za/)
- **Status :** Claimed Full Dump Publication

- **Description :** A cybercriminal forum post claims the release of approximately 20GB of data allegedly linked to the Consumer Goods Council of South Africa (CGCSA). The threat actor states the publication occurred after failed negotiations and a public denial of the breach.

- **Observed Data :**
  - customer databases
  - internal reports
  - scripts and administrative documents
  - invoices and executive reports
  - accounting backups
  - Sage200EVO SQL databases
  - financial and commercial records

- **CTI Analysis :**
  The published elements suggest exposure of sensitive commercial, accounting, and customer-related data linked to South Africa’s consumer goods and retail sector. Risks include financial fraud, commercial espionage, and compromise of customer information.

- **CTI Note :**
  The publication explicitly references a post-compromise dispute with the victim as well as public distribution of the leaked archives.
---
### May 12, 2026
#### 🇲🇦 Morocco - SDTM / Groupe Barid Al-Maghrib

- **Threat Actor / Group :** Sejjil
- **Sector :** Logistics / Transportation / Postal Services / ERP
- **Targeted Organization :** SDTM – Groupe Barid Al-Maghrib
- **Web site :** [poste.ma](https://www.poste.ma)
- **Status :** Data Leak / Claim
- **Victim Description :**  
  SDTM is a logistics subsidiary of Groupe Barid Al-Maghrib involved in transportation, distribution, fleet management, and operational support services linked to postal and financial activities in Morocco.

- **Leak Description :**  
  A post published on May 12, 2026 claims the complete exposure of SDTM’s ERP and financial infrastructure. The actor alleges possession of 129 structured CSV files originating from SAGE ERP systems, SMS gateways, banking datasets, and internal operational platforms associated with logistics and financial workflows.

- **Sample Analysis :**  
  The analyzed samples contain administrative metadata, ERP user accounts, MD5 password hashes, active session tokens, corporate email addresses, agency information, phone numbers, internal financial records, bank account identifiers (RIB), account designations, and customer-related information including national ID references and physical addresses.

- **CTI Note :**  
  The exposed data suggests a deep compromise of internal ERP and application environments. The presence of active tokens, administrative accounts, and structured financial datasets could facilitate fraud operations, persistent access, or lateral compromise activities. The full authenticity and exact scope of the claimed dataset remain independently unverified.
