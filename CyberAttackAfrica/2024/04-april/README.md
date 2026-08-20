[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Month](https://img.shields.io/badge/Month-April%202024-lightgrey)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
![TLP](https://img.shields.io/badge/TLP-CLEAR-brightgreen)

# CTI Report - April 2024: Energy and crypto assets targeted across the continent

👉🏾 [Version française disponible ici](./README_FR.md)

### 1. Executive summary

In April 2024, Africa recorded **6 documented victims**: **5 ransomware claims** across 5 different countries, plus **1 data leak claim** in Burkina Faso. The month is notable for two high-profile ransomware targets: a **major Libyan oil & gas joint venture** (~1 TB exfiltrated) and a **cryptocurrency exchange platform** in the Seychelles. The SpaceBears group appears for the first time with two simultaneous claims, alongside an unrelated data leak claim against a Burkinabe government employment agency.

👉🏾 [Victims list](./victims.md)

**Key figures:**
- 🔹 **6 victims** identified
- 🔹 **5 active sources**: InCransom (1), Hunters (1), SpaceBears (2), RansomHub (1), Pedi (1)
- 🔹 **Countries affected**: South Africa (2), Seychelles (1), Morocco (1), Libya (1), Burkina Faso (1)
- 🔹 **Sectors**: Banking/Crypto, Media & Publishing, Manufacturing/Packaging, Technologies, Oil & Gas, Government/Employment and Training
- 🔹 **Incident types**: Ransomware (5), Data Leak (1)
### Monthly aggregate exposure view

The monthly CTI view combines data leaks and access sales as **data exposure**: **1 records** (16.7% of the monthly corpus). Source cards remain authoritative; an access sale does not by itself prove data exfiltration.


---

### 2. Attack timeline

| Date | Victim | Country | Actor / Group | Type |
|------|--------|---------|----------------|------|
| April 4 | Remitano (Cryptocurrency Exchange) | Seychelles | InCransom | Ransomware |
| April 13 | Caxton and CTP Publishers and Printers | South Africa | Hunters | Ransomware |
| April 23 | ONEF (National Observatory for Employment and Training) | Burkina Faso | Pedi | Data leak (SQL sample) |
| April 29 | SM Emballage | Morocco | SpaceBears | Ransomware |
| April 29 | Thinkadam | South Africa | SpaceBears | Ransomware |
| April 30 | Mellitah Oil & Gas (Eni / NOC JV) | Libya | RansomHub | Ransomware |

```mermaid
timeline
    title Attacks recorded in this file - April 2024
    April 4 : Remitano (Seychelles) - InCransom
    April 13 : Caxton & CTP Publishers (South Africa) - Hunters
    April 23 : ONEF (Burkina Faso) - Pedi
    April 29 : SM Emballage (Morocco) - SpaceBears
               Thinkadam (South Africa) - SpaceBears
    April 30 : Mellitah Oil & Gas (Libya) - RansomHub
```

---

### 3. Victim analysis

#### 3.1 By country

| Country | Number of attacks |
|---------|-----------------|
| South Africa | 2 |
| Seychelles | 1 |
| Morocco | 1 |
| Libya | 1 |
| Burkina Faso | 1 |

```mermaid
pie
    title Distribution by country - April 2024 (6 victims)
    "South Africa" : 2
    "Seychelles" : 1
    "Morocco" : 1
    "Libya" : 1
    "Burkina Faso" : 1
```

#### 3.2 By sector

| Sector | Count |
|--------|-------|
| Banking / Crypto assets | 1 |
| Media & Publishing | 1 |
| Manufacturing / Industrial Packaging | 1 |
| Technologies | 1 |
| Oil & Gas / Energy | 1 |
| Government / Employment and Training | 1 |

```mermaid
xychart-beta
    title "Targeted Sectors - April 2024"
    x-axis ["Banking/Crypto", "Media", "Manufacturing", "Technologies", "Oil & Gas", "Government/Employment"]
    y-axis "Number of attacks" 0 to 2
    bar [1, 1, 1, 1, 1, 1]
```

#### 3.3 Ransomware groups

| Ransomware group | Number of attacks |
|-----------------|-----------------|
| SpaceBears | 2 |
| InCransom | 1 |
| Hunters | 1 |
| RansomHub | 1 |

#### 3.4 Data leak sources

| Source | Number of claims |
|--------|-----------------|
| Pedi | 1 |

```mermaid
gantt
    title Active Ransomware Groups - April 2024
    dateFormat X
    axisFormat %s
    section SpaceBears
    SpaceBears : 0, 2
    section InCransom
    InCransom : 0, 1
    section Hunters
    Hunters : 0, 1
    section RansomHub
    RansomHub : 0, 1
```

---

### 4. Key observations

- **High-impact energy sector attack**: Mellitah Oil & Gas (Eni/NOC joint venture in Libya) is claimed by RansomHub with approximately **1 TB of exfiltrated data**, the highest-impact claim of the month, involving a strategic energy asset co-owned by an international major.
- **Cryptocurrency in the crosshairs**: Remitano (Seychelles-registered P2P crypto exchange) is targeted by InCransom. This same victim will be claimed again in August 2024 by a different group (Meow), an early double-claim pattern.
- **SpaceBears emergence**: the group strikes twice on April 29 (Morocco and South Africa simultaneously), signalling a coordinated campaign or active prospection phase.
- **Media targeted**: Caxton and CTP Publishers, one of South Africa's largest print/media groups, highlights ransomware actors' interest in organizations holding large consumer datasets.
- **Burkina Faso data leak claim**: ONEF (National Observatory for Employment and Training), discovered April 23, 2024, concerns a forum publication by the actor `Pedi` presenting a database associated with onef.gov.bf as a free SQL release. The screenshot shows the structure of a news/publication table but does not establish the dataset's authenticity or initial access method. It is not attributed to a ransomware group and is tracked separately as a data leak claim against a Burkinabe public employment institution.

---

```mermaid
xychart-beta
    title "Monthly Evolution of Attacks (Jan - Apr 2024)"
    x-axis ["Jan", "Feb", "Mar", "Apr"]
    y-axis "Number of attacks" 0 to 14
    bar [12, 5, 8, 6]
```

### 5. Recommendations

| Domain | Recommended action |
|--------|--------------------|
| Oil & Gas / Energy | Assess vendor access controls, implement data loss prevention (DLP), monitor bulk data transfers. |
| Crypto / Fintech platforms | Enforce MFA on all admin interfaces, monitor API anomalies, prepare incident response plans. |
| Media & Publishing | Protect subscriber and advertiser databases, segment editorial systems from business IT. |
| Manufacturing | Audit internet-facing systems, enforce patch management for industrial platforms. |
| Government / employment and training | ONEF should verify the claim against application and database logs, confirm whether the referenced SQL export is genuine, and rotate any credentials if exposure is confirmed. |
| All organizations | Track SpaceBears and RansomHub IOCs, both show increasing African activity. |

---

*Report generated from AFRINTEL OSINT data. Free distribution (TLP:CLEAR)*
