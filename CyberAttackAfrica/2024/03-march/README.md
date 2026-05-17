# 📑 CYBER THREAT INTELLIGENCE (CTI) REPORT
**Scope:** African Continent | **Period:** March 2024  
**Classification:** TLP:CLEAR  
**Project:** AFRINTEL (African Threat Intelligence Repository)
👉🏾 [Version française disponible ici](./README_FR.md)

---

## 1. EXECUTIVE SUMMARY

The month of March 2024 was marked by sustained threat actor activity from ransomware groups targeting critical infrastructure, financial institutions, and major public sector entities across the African continent. In total, **7 critical incidents** were officially recorded and analyzed within the scope of the AFRINTEL project.

Cybercriminals continue to exploit vulnerabilities on exposed network perimeters and exfiltrate massive volumes of corporate data to conduct double-extortion campaigns. The geographical distribution highlights a concentration of attacks in **Egypt** (3 incidents) and **South Africa** (2 incidents), followed by **Tunisia** and **Namibia**.

### Key Indicators — March 2024
* **Total Validated Victims:** 7
* **Identified Threat Actors:** LockBit 3.0 (4 attacks), RansomHub (2 attacks), Hunters International (1 attack).
* **Most Targeted Sectors:** Financial & Banking Services (2), Public Administrations & State Infrastructure (1), Healthcare & Pharmaceutical Retail (1), Energy & Utilities (1), Industrial Manufacturing (1), Sports Media (1).

---

## 2. THREAT ACTOR LANDSCAPE (RANSOMWARE)

Three organized cybercrime syndicates account for all the claimed attacks this month:

1. **LockBit 3.0 (42.8% of attacks):** Despite suffering international law enforcement disruptions (Operation Cronos) earlier in 2024, the LockBit franchise demonstrates significant resilience across the African continent, striking 4 prominent entities through its active network of affiliates.
2. **RansomHub (28.6% of attacks):** This emerging threat group confirms its rapid rise in power, specifically targeting high-visibility energy infrastructure and digital media outlets in Egypt.
3. **Hunters International (14.3% of attacks):** An opportunistic threat actor exploiting the Hive ransomware codebase, identified this month targeting the North African financial services sector.

---

## 3. DETAILED INCIDENT MAPPING (MARCH 2024)

### 🗓️ March 19, 2024
#### 🇪🇬 Egypt — Go4Kora
* **Incident Identifier:** AFRINTEL-2024-13649
* **Ransomware Group:** RansomHub
* **Work Sector:** Sports Media & Audience Entertainment
* **Website:** [go4kora.tv](https://go4kora.tv)
* **Attack Status:** Official claim and data exfiltration of subscriber databases.
* **Description & Context:** Go4Kora is one of the most visited sports news and live football streaming portals in Egypt and the MENA region. The attack targeted the broadcasting infrastructure and subscriber records, impacting platform integrity.

---

### 🗓️ March 20, 2024
#### 🇿🇦 South Africa — Government Printing Works (GPW)
* **Incident Identifier:** AFRINTEL-2024-13658
* **Ransomware Group:** LockBit 3.0
* **Work Sector:** Public Administrations & State Security Printing
* **Website:** [gpw.gov.za](https://www.gpw.gov.za)
* **Attack Status:** Confirmed claim, threat of leaking sovereign government documentation.
* **Description & Context:** A strategic South African state-owned entity under the Department of Home Affairs, GPW is responsible for printing secure identity documents, passports, visas, and official government gazettes. This constitutes a major compromise impacting digital sovereignty.

---

### 🗓️ March 25, 2024
#### 🇹🇳 Tunisia — Arab Tunisian Leasing (ATL Leasing)
* **Incident Identifier:** AFRINTEL-2024-13740
* **Ransomware Group:** Hunters International
* **Work Sector:** Financial Services & Asset Leasing
* **Website:** [atlleasing.com.tn](https://www.atlleasing.com.tn)
* **Attack Status:** Claimed on the leak site, exfiltration of corporate financial data.
* **Description & Context:** Listed on the Tunis Stock Exchange, ATL is a prominent Tunisian financial institution specializing in leasing options for professional equipment and real estate dedicated to SMEs.

---

### 🗓️ March 25, 2024
#### 🇪🇬 Egypt — El Ezaby Pharmacy
* **Incident Identifier:** AFRINTEL-2024-13743
* **Ransomware Group:** LockBit 3.0
* **Work Sector:** Healthcare & Pharmaceutical Retail
* **Website:** [elezabypharmacy.com](https://www.elezabypharmacy.com)
* **Attack Status:** Encryption of management systems and claims of compromised customer/supplier records.
* **Description & Context:** Represents one of the largest pharmaceutical retail networks in Egypt, managing a nationwide network of megastores and a critical supply logistics ecosystem.

---

### 🗓️ March 26, 2024
#### 🇳🇦 Namibia — Agricultural Bank of Namibia (Agribank)
* **Incident Identifier:** AFRINTEL-2024-13757
* **Ransomware Group:** LockBit 3.0
* **Work Sector:** Banking & Agricultural Finance
* **Website:** [agribank.com.na](https://www.agribank.com.na)
* **Attack Status:** Published on the LockBit leak site following failed negotiations.
* **Description & Context:** A state-owned banking institution crucial to the Namibian economy, exclusively dedicated to financing agricultural expansion, aquaculture, and rural land acquisition.

---

### 🗓️ March 29, 2024
#### 🇪🇬 Egypt — PGESCo (Power Generation Engineering and Services Company)
* **Incident Identifier:** AFRINTEL-2024-13908
* **Ransomware Group:** RansomHub
* **Work Sector:** Energy, Oil/Gas & Infrastructure Engineering
* **Website:** [pgesco.com](https://www.pgesco.com)
* **Attack Status:** Official claim and encryption of engineering network shares.
* **Description & Context:** A major Egyptian engineering firm with international operations, providing project management, consultancy, and engineering for large-scale power plants and industrial infrastructure across the region.

---

### 🗓️ March 31, 2024
#### 🇿🇦 South Africa — Nampak
* **Incident Identifier:** AFRINTEL-2024-13957
* **Ransomware Group:** LockBit 3.0
* **Work Sector:** Industrial Manufacturing (Packaging Solutions)
* **Website:** [nampak.com](https://www.nampak.com)
* **Attack Status:** Leaking of sensitive corporate data.
* **Description & Context:** The largest packaging manufacturer and exporter on the African continent, headquartered in South Africa and operating numerous production plants across sub-Saharan networks.

---

## 4. SOC RECOMMENDATIONS & MITigation STRATEGIES

In light of the observed tactics, techniques, and procedures (TTPs) utilized by LockBit 3.0 and RansomHub, the SOC and Threat Intelligence teams recommend the immediate deployment of the following mitigation controls:

1. **Active Identity & Access Monitoring:** Enforce robust Multi-Factor Authentication (MFA) across all remote access vectors (VPNs, jump hosts, cloud portals) and strictly audit accounts with administrative privileges.
2. **Perimeter Hardening against RansomHub:** As this group frequently leverages compromised legitimate credentials or known unpatched vulnerabilities on edge servers, a comprehensive external asset scan (via Shodan/Censys) is urgently required.
3. **Strict Network Segmentation:** Isolate industrial control systems (OT/SCADA) or critical production environments (such as manufacturing lines or secure printing networks) from corporate office networks.
4. **Persistence Detection Engineering:** Monitor for anomalous PowerShell execution patterns and the unauthorized use of dual-use administration utilities (Living-off-the-Land) such as AnyDesk, NetSupport, or Rclone used for data staging and exfiltration.

---

## 5. ACKNOWLEDGEMENTS & EDITORIAL TEAM

**Principal Author:** *Adama ASSIONGBON* *Senior SOC & Cyber Threat Intelligence (CTI) Consultant* Casablanca, Morocco.  
[LinkedIn Professional Profile](https://www.linkedin.com/in/adama-assiongbon-3bb941193/)

**Data Source:** OSINT Registries & Dark Web Leak Site Monitoring — AFRINTEL Project 2024.
