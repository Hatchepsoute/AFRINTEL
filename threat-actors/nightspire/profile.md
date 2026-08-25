# NightSpire - Threat Actor Profile
👉🏾 [**French version available here**](./profile_FR.md)
**AFRINTEL Threat Actor Intelligence**

- **Actor / Group:** NightSpire
- **Threat type:** Ransomware / Extortion
- **Motivation:** Financial
- **Activity tracked by AFRINTEL:** Yes
- **Primary AFRINTEL geography observed:** Egypt
- **Assessment status:** Active monitoring
- **Last updated:** 25 August 2026

---

## 1. Intelligence summary

NightSpire is a ransomware operation associated with data theft, extortion and file encryption.

Public incident-response reporting shows that NightSpire-associated intrusions may involve legitimate remote-access software and commercial utilities for remote control, file discovery, data staging and exfiltration.

AFRINTEL tracks NightSpire activity affecting African organizations and maintains a strict distinction between:

- ransomware-group claims;
- independently reported technical observations;
- AFRINTEL analytical assessments;
- technically confirmed victim-specific evidence.

The presence of an organization on the NightSpire leak site does not, by itself, demonstrate that every known NightSpire TTP was used against that organization.

---

## 2. AFRINTEL Observations in Africa

| Date | Country | Victim | Sector | AFRINTEL Evidence |
|---|---|---|---|---|
| 24 May 2026 | Egypt | Papa John's Egypt | Food & Beverage / Restaurants | NightSpire ransomware claim |
| 24 May 2026 | Egypt | Rawaj Consumer Finance | Financial Services | NightSpire ransomware claim |
| 26 May 2026 | Egypt | B Investments (Basata / Basatamfi) | Financial Services & Private Equity | NightSpire ransomware claim |

### AFRINTEL assessment

AFRINTEL observed a cluster of three NightSpire claims targeting Egyptian organizations within a three-day period.

Two of the three organizations operate in financial services, while the third operates in the food-service sector.

This temporal and geographic concentration is relevant for victimology and campaign monitoring.

However, AFRINTEL currently has no victim-specific telemetry proving that the TTPs documented in external NightSpire investigations were used against these three Egyptian organizations.

**Assessment confidence:** High for the actor claims and victim association; insufficient evidence for victim-specific TTP attribution.

---

## 3. Documented NightSpire Operational Behavior

The following behaviors are derived from independent technical investigation and must not automatically be attributed to every NightSpire incident tracked by AFRINTEL.

| ATT&CK Tactic | Technique | ATT&CK ID | Observed behavior | Evidence | Confidence |
|---|---|---|---|---|---|
| Lateral Movement | Remote Desktop Protocol | T1021.001 | Threat actor accessed an endpoint using RDP | Observed | High |
| Command and Control | Remote Desktop Software | T1219.002 | Chrome Remote Desktop and AnyDesk deployed for remote access / persistence | Observed | High |
| Discovery | File and Directory Discovery | T1083 | Everything used to search and access files | Observed | High |
| Collection | Archive via Utility | T1560.001 | 7-Zip used to archive files from a selected folder | Observed | High |
| Exfiltration | Exfiltration to Cloud Storage | T1567.002 | MEGASync executed during the intrusion and assessed as likely used for exfiltration | Assessed | Medium |
| Impact | Data Encrypted for Impact | T1486 | NightSpire ransomware encryptor executed and encrypted files | Observed | High |

---

## 4. Tooling

| Tool | Role | Evidence status |
|---|---|---|
| RDP | Remote access | Observed |
| Chrome Remote Desktop | Remote access / persistence | Observed |
| AnyDesk | Remote access / persistence | Observed |
| Everything | File discovery / collection support | Observed |
| 7-Zip | Data staging / archiving | Observed |
| MEGASync | Possible data exfiltration | Assessed |
| VMware Workstation | Observed in compromised environment | Observed |
| WPS Office | Observed in compromised environment | Observed |

---

## 5. Indicators of Compromise

The following indicators were reported during independent
NightSpire investigations.

| Indicator type | Context | Confidence |
|---|---|---|
| SHA-256 | NightSpire encryptor - December 2025 sample | High |
| SHA-256 | NightSpire encryptor - March 2026 sample | High |
| File extension | `.nspire` encrypted files | High |
| Ransom note | `_nightspire_readme.txt` | High |
| Ransom note | `[nspire_msg].txt` | High |

AFRINTEL does not assert that these indicators were observed against the African victims listed above unless victim-specific technical evidence becomes available.

---

## 6. Attribution Assessment

### Evidence model

AFRINTEL uses four evidence qualifiers:

**Observed**  
Directly observed in technical telemetry, malware analysis, incident-response evidence or primary-source material.

**Reported**  
Documented by a trusted external intelligence or incident-response source.

**Assessed**  
Analytical conclusion derived from multiple available observations.

**Inferred**  
Plausible relationship with insufficient technical evidence for strong attribution.

### Current NightSpire assessment

The association between NightSpire and the African organizations listed by AFRINTEL is based on observed ransomware-group claims.

External incident-response evidence independently documents NightSpire-associated tooling and TTPs.

AFRINTEL does not currently have sufficient technical evidence to assert that the exact same intrusion chain was used against B Investments, Rawaj Consumer Finance or Papa John's Egypt.

This distinction prevents actor-level intelligence from being incorrectly represented as victim-specific telemetry.

---

## 7. Analytical Notes

External investigations show variations between NightSpire incidents, including changes to the ransomware encryptor, ransom-note naming and operational tooling.

This means NightSpire should not be modeled as having one immutable set of IOCs or TTPs.

Possible explanations include:

- evolution of the ransomware operation;
- changes in operator tradecraft;
- different affiliates or intrusion teams;
- campaign-specific tooling.

For AFRINTEL, NightSpire intelligence should therefore be maintained
at both:

1. **Actor level** - known and reported behaviors;
2. **Incident level** - techniques actually confirmed for a specific victim.

---

## 8. AFRINTEL Intelligence Gap

Current gaps for the African NightSpire cases include:

- initial-access vector;
- victim-specific malware hashes;
- attacker infrastructure;
- authentication artifacts;
- confirmed lateral-movement techniques;
- confirmed exfiltration channel;
- exact encryption/deployment method.

These fields should be updated if additional technical evidence becomes publicly available or is obtained during AFRINTEL analysis.

---

## 9. Sources

- Huntress - Decoding NightSpire: Ransomware IOCs Aren't Set in Stone
- MITRE ATT&CK - T1021.001 Remote Desktop Protocol
- MITRE ATT&CK - T1219.002 Remote Desktop Software
- MITRE ATT&CK - T1083 File and Directory Discovery
- MITRE ATT&CK - T1560.001 Archive via Utility
- MITRE ATT&CK - T1567.002 Exfiltration to Cloud Storage
- MITRE ATT&CK - T1486 Data Encrypted for Impact
- AFRINTEL - May 2026 African ransomware victim intelligence

---

**AFRINTEL - African Cyber Threat Intelligence**
