[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Breach-red)
![Period](https://img.shields.io/badge/Period-March%202026-lightgrey)
![Intel Type](https://img.shields.io/badge/Intel%20Type-CTI-purple)

# CTI Report - Cyberattacks in Africa (March 2026)

## 1. Executive Summary

In March 2026, **36 cyber incidents** targeting African entities were publicly claimed or detected. The continent continues to face a dual threat: **ransomware** (encryption with ransom demand) and **data breaches / system intrusions** (exfiltration without encryption or direct financial fraud). Key findings:

- **19 ransomware attacks (53%)** and **17 data breaches / intrusions (47%)**.
- **11 countries** affected; **South Africa** (11 incidents), **Morocco** (8) and **Egypt** (8) account for 75% of all victims.
- **23 distinct threat actors**; **CrowStealer** (5 incidents), **APT73/BASHE** (4) and **XP95** (3) are the most active.
- **Government and education sectors** represent 44% of victims, highlighting a strategic focus on public institutions.
- Massive data leaks: Egyptian health ministry (3.8M records), Gauteng provincial government (3.8 TB), Remita Nigeria (3 TB), Stats SA (154 GB).
- New major incident: **UBA Senegal** – a coordinated cyber heist involving system compromise, database manipulation, and over 3,400 fraudulent ATM withdrawals totaling 1.143 billion FCFA (~$1.9M USD), disclosed in March but executed in late January.

## 2. Methodology

- **Scope**: 54 African countries.
- **Period**: 1 – 31 March 2026 (incidents disclosed or claimed during this month; actual attack dates may be earlier).
- **Sources**: DLS (leak sites), OSINT, Telegram channels, underground forums, media reports.
- **Inclusion**: Publicly claimed or attributed incidents with identified victim, country, sector.
- **Typology**:
  - *Ransomware*: encryption + ransom demand (claim on DLS).
  - *Data breach / intrusion*: unencrypted exfiltration, database sold or published, or system compromise leading to financial fraud.

## 3. Global Overview

| Indicator                     | Value |
|-------------------------------|-------|
| Total victims                 | 36    |
| Countries affected            | 11    |
| Distinct actors               | 23    |
| Ransomware incidents          | 19 (53%) |
| Data breaches / intrusions    | 17 (47%) |

**Most targeted countries:**
- 🇿🇦 South Africa: 11 victims
- 🇲🇦 Morocco: 8 victims
- 🇪🇬 Egypt: 8 victims
- 🇳🇬 Nigeria: 2 victims
- 🇸🇳 Senegal: 1 victim
- 🇿🇲 Zambia: 1 victim
- 🇲🇬 Madagascar: 1 victim
- 🇹🇳 Tunisia: 1 victim
- 🇳🇦 Namibia: 1 victim
- 🇹🇿 Tanzania: 1 victim
- 🇨🇩 DRC: 1 victim

**Ransomware vs Data Breaches by country:**
| Country               | Ransomware | Data Breach/Intrusion |
|-----------------------|------------|----------------------|
| 🇿🇦 South Africa       | 7          | 4                    |
| 🇲🇦 Morocco            | 5          | 3                    |
| 🇪🇬 Egypt              | 3          | 5                    |
| 🇳🇬 Nigeria            | 0          | 2                    |
| 🇸🇳 Senegal            | 0          | 1                    |
| 🇿🇲 Zambia             | 0          | 1                    |
| 🇲🇬 Madagascar         | 1          | 0                    |
| 🇹🇳 Tunisia            | 1          | 0                    |
| 🇳🇦 Namibia            | 1          | 0                    |
| 🇹🇿 Tanzania           | 1          | 0                    |
| 🇨🇩 DRC                | 0          | 1                    |

**Sector distribution:**
| Sector                    | Incidents | Percentage |
|---------------------------|-----------|------------|
| Government / Admin        | 9         | 25%        |
| Education / University    | 7         | 19%        |
| Health                    | 3         | 8%         |
| Insurance                 | 3         | 8%         |
| Telecommunications        | 3         | 8%         |
| Engineering/Construction  | 3         | 8%         |
| Finance / Banking         | 2         | 6%         |
| IT/Consulting             | 2         | 6%         |
| Fintech                   | 1         | 3%         |
| Others                    | 3         | 8%         |

**Most prolific actors:**
| Actor            | Type            | Incidents | Primary targets |
|------------------|-----------------|-----------|-----------------|
| CrowStealer      | Data broker     | 5         | Egyptian government & education |
| APT73/BASHE      | Ransomware      | 4         | Moroccan state institutions |
| XP95             | Ransomware      | 3         | South African government |
| Qilin            | Ransomware      | 2         | Morocco, Madagascar |
| The Gentlemen    | Ransomware      | 2         | Tunisia, South Africa |
| INC Ransom       | Ransomware      | 2         | Namibia, South Africa |
| xNov             | Data breach     | 2         | Moroccan supply chain |

**Daily timeline (March 2026 – disclosure dates):**
- 01/03: 3 incidents
- 02/03: 3
- 03/03: 3
- 04/03: 1
- 05/03: 1
- 06/03: 2
- 09/03: 1
- 12/03: 1
- 13/03: 2
- 14/03: 1
- 19/03: 1
- 20/03: 2
- 21/03: 1
- 22/03: 1
- 24/03: 1 (UBA Senegal disclosure)
- 26/03: 4
- 29/03: 2
- 30/03: 3
- 31/03: 3

## 4. Detailed Analysis by Incident Type

### 4.1 Ransomware (19 incidents)

| Country          | Ransomware attacks | Main actors |
|------------------|--------------------|-------------|
| South Africa     | 7                  | XP95 (3), LockBit 5.0, Lynx, DragonForce, The Gentlemen, NightSpire, INC Ransom, Coinbase Cartel |
| Morocco          | 5                  | APT73/BASHE (3), Qilin, The Gentlemen |
| Egypt            | 3                  | Crypto24, PEAR, Payload |
| Madagascar       | 1                  | Qilin |
| Tunisia          | 1                  | The Gentlemen |
| Namibia          | 1                  | INC Ransom |
| Tanzania         | 1                  | Morpheus |

**Key observations**:
- **XP95** emerged as a major threat in South Africa, striking Gauteng provincial government (3.8 TB), Stats SA (154 GB) and GCRA (147 GB). Data is being sold, not just encrypted.
- **APT73/BASHE** targeted strategic Moroccan institutions (HACA, Maroc Telecom, 2M TV, IRES), suggesting possible geopolitical motivation.
- Insurance sector heavily hit in South Africa (Lion of Africa, The Unlimited).

### 4.2 Data Breaches / System Intrusions (17 incidents)

| Country          | Breaches/Intrusions | Main actors |
|------------------|---------------------|-------------|
| Egypt            | 5                   | CrowStealer (5) |
| Morocco          | 3                   | xNov (2), anisanas2 |
| South Africa     | 4                   | TelephoneHooliganism, XP95 (already counted in ransomware), Walter Sisulu University (data breach) |
| Nigeria          | 2                   | AshleyWood2022, Bytetobreach |
| Senegal          | 1                   | Coordinated network |
| Zambia           | 1                   | Spirigatito |
| DRC              | 1                   | privillege |

**Key observations**:
- **CrowStealer** dominates Egyptian breaches, including a medical database of 3.8 million patients (Ministry of Health) sold for $2,500.
- **xNov** exposed student records (ONOUSC, 3,631 entries) and L'Oréal Morocco supply chain data (296 pharmacies, 361,000 sales records, OAuth2 secrets).
- **UBA Senegal** (disclosed in March, executed in late January): attackers compromised the internal information system, manipulated databases (created/modified accounts, increased withdrawal limits, transferred funds), then coordinated over 3,400 ATM withdrawals across multiple cities in a few hours, netting 1.143 billion FCFA (~$1.9M). Potential exploited vulnerabilities: lack of real-time SOC monitoring, insufficient anti-fraud procedures, possible internal complicity.
- Massive Nigerian breaches: Remita (3 TB, including KYC documents and government HSM keys) and Ahmadu Bello University (11,000+ staff records).

## 5. Sectoral Impact

| Sector                | Incidents | Percentage |
|-----------------------|-----------|------------|
| Government / Admin    | 9         | 25%        |
| Education / University| 7         | 19%        |
| Health                | 3         | 8%         |
| Insurance             | 3         | 8%         |
| Telecommunications    | 3         | 8%         |
| Engineering/Construction | 3      | 8%         |
| Finance / Banking     | 2         | 6%         |
| IT/Consulting         | 2         | 6%         |
| Fintech               | 1         | 3%         |
| Others                | 3         | 8%         |

**Takeaways**:
- Public sector (government + education) accounts for **44%** of all incidents.
- Health data remains highly valued: Egyptian health ministry breach (3.8M records) and South African insurance leaks.
- Telecoms (Orange Madagascar, Maroc Telecom) are strategic targets.
- The UBA Senegal incident highlights a new trend: **direct financial fraud through system compromise**, bypassing traditional ransomware.

## 6. Threat Actor Profile

| Actor            | Type            | Incidents | Primary targets |
|------------------|-----------------|-----------|-----------------|
| CrowStealer      | Data broker     | 5         | Egyptian government & education |
| APT73/BASHE      | Ransomware      | 4         | Moroccan state institutions |
| XP95             | Ransomware      | 3         | South African government |
| Qilin            | Ransomware      | 2         | Morocco, Madagascar |
| The Gentlemen    | Ransomware      | 2         | Tunisia, South Africa |
| INC Ransom       | Ransomware      | 2         | Namibia, South Africa |
| xNov             | Data breach     | 2         | Moroccan supply chain |

**Emerging actors**: xNov (supply chain focus), XP95 (South African government targeting). The UBA Senegal attack involved a **coordinated network** possibly with internal complicity – not a traditional ransomware group but a financially motivated intrusion team.

### 6.1 Risk Assessment

| Country | Risk Level |
|--------|-----------|
| South Africa | 🔴 Critical |
| Morocco | 🔴 High |
| Egypt | 🔴 High |
| Nigeria | 🟠 Medium-High |
| Senegal | 🟠 Medium (post-UBA) |
| Others | 🟠 Medium |

## 7. Key Trends & Intelligence Gaps

### Trends
1. **Ransomware evolves into data extortion** – XP95 and others sell exfiltrated data instead of merely encrypting.
2. **Supply chain attacks** – Smarteez (L'Oréal Morocco provider) shows vulnerability of digital service providers.
3. **Massive health data leaks** – Egyptian health ministry breach (3.8M records) highlights poor security in public health IT.
4. **Geopolitical targeting** – APT73/BASHE focus on Moroccan state media and telecoms.
5. **Direct financial fraud via system compromise** – UBA Senegal demonstrates that attackers bypass ransomware to go straight for the money, exploiting weak SOC and anti-fraud controls.

### Gaps
- Many attacks go undetected or unreported; this list only includes publicly disclosed incidents.
- Attribution uncertainty for some groups (e.g., CrowStealer may be a reseller, not attacker).
- Actual data volumes may be inflated by actors.
- The UBA Senegal attack was executed in late January but only disclosed in March – significant delay in public awareness.

## 8. MITRE ATT&CK Mapping (Contextual)

| Incident | Techniques |
|---------|-----------|
| Smarteez | T1552 - Credentials in Files |
| Gauteng | T1041 - Exfiltration |
| ONOUSC | T1078 - Valid Accounts |
| Egypt Health DB | T1005 - Data from Local System |
| UBA Senegal | T1190 - Exploit Public-Facing App, T1078 - Valid Accounts, T1048 - Exfiltration over Alternative Protocol, T1531 - Account Manipulation |

**Common techniques observed**:
- T1566 - Phishing  
- T1190 - Exploit Public-Facing Application  
- T1041 - Exfiltration  
- T1078 - Valid Accounts  
- T1486 - Ransomware  
- T1531 - Account Manipulation (UBA Senegal)

## 9. Recommendations

### For African governments and enterprises
- **Database security**: Encrypt sensitive data, implement access controls, regular audits.
- **Third-party risk management**: Audit digital service providers, enforce cybersecurity clauses.
- **Incident response**: Offline backups, tabletop exercises, communication protocols.
- **Staff training**: Phishing awareness (primary initial vector).
- **Real-time monitoring**: Deploy or strengthen Security Operations Centers (SOC) with 24/7 capability; implement transaction anomaly detection (especially for financial institutions).
- **Anti-fraud mechanisms**: Dynamic withdrawal limits, automatic blocking on abnormal patterns, behavioral analysis.

### For CTI analysts
- Monitor **XP95** and **xNov** for new campaigns.
- Track supply chain exposures (especially digital marketing and logistics providers).
- Prioritize monitoring of government, education, and health sectors in North and Southern Africa.
- Watch for **non-ransomware financial intrusions** – UBA Senegal is likely not an isolated case.

## 10. SOC Recommendations

### Detection priorities
- Monitor **data exfiltration patterns (T1041)**  
- Detect **privileged account abuse (T1078)**  
- Track **API / OAuth misuse**  
- Analyze **outbound traffic anomalies**  
- For banks: implement **real-time ATM transaction anomaly detection** (velocity, location, amount spikes)

### Monitoring sources
- EDR / Sysmon  
- Firewall / Proxy  
- DNS logs  
- Identity logs  
- Core banking system logs (for financial institutions)

## 11. Strategic Recommendations

- Enforce **MFA on all critical systems**  
- Implement **network segmentation** (separate ATM network from core banking)  
- Audit **third-party providers**  
- Maintain **offline backups**  
- Conduct **incident response exercises** including red-team simulations  
- **Regulatory push**: Central banks should mandate minimum SOC and fraud detection standards for financial institutions

## 12. Conclusion

March 2026 confirms that **Africa is a prime target for industrialized cybercrime**. The convergence of ransomware groups, data brokers, supply chain attacks, and now **direct financial system intrusions** (UBA Senegal) creates a high-risk environment. South Africa, Morocco, and Egypt remain the most affected, but the UBA incident shows that **West Africa is also under serious threat**. Financial institutions must urgently strengthen real-time monitoring and anti-fraud capabilities. AFRINTEL will continue tracking these trends.

**AFRINTEL** - African Cyber Threat Intelligence Initiative  
[GitHub AFRINTEL](https://github.com/Hatchepsoute/AFRINTEL)