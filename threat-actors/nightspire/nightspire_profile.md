# NightSpire - Threat Actor / Ransomware Profile

👉🏾 [**Version française**](./nightspire_profile_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Actor / Operation:** NightSpire
- **Threat type:** Ransomware / Data theft / Extortion
- **Motivation:** Financial
- **First publicly reported:** 2025
- **AFRINTEL African geography observed:** Egypt
- **Operating model:** Not firmly established; public reporting differs on whether NightSpire is RaaS
- **Assessment status:** Active monitoring
- **Last updated:** 26 August 2026

---

## 1. Intelligence summary

NightSpire is a ransomware operation associated with data theft, extortion and file encryption. Public reporting does not fully agree on its operating model, so AFRINTEL does not label it RaaS as a confirmed fact.

A Huntress investigation published in 2026 provides useful incident-level evidence. In that case, the actor used RDP, Chrome Remote Desktop, AnyDesk, Everything, 7-Zip and MEGASync before NightSpire ransomware execution. Huntress also stressed that ransomware TTPs can change between incidents and possible affiliates.

AFRINTEL tracks separate NightSpire claims affecting Egyptian organizations, but does not treat the Huntress case as proof that the same intrusion chain was used against those African victims.

---

## 2. AFRINTEL observations in Africa

| Date | Country | Victim | Sector | Evidence | Scope | Confidence | Provenance |
|---|---|---|---|---|---|---|---|
| 24 May 2026 | Egypt | Papa John's Egypt | Food & Beverage / Restaurants | Ransomware claim | Victim-specific claim | High | AFRINTEL victim tracking |
| 24 May 2026 | Egypt | Rawaj Consumer Finance | Financial Services | Ransomware claim | Victim-specific claim | High | AFRINTEL victim tracking |
| 26 May 2026 | Egypt | B Investments (Basata / Basatamfi) | Financial Services & Private Equity | Ransomware claim | Victim-specific claim | High | AFRINTEL victim tracking |

AFRINTEL observed three NightSpire claims against Egyptian organizations in a three-day period. Two of the three victims were in financial services. This is useful for victimology and campaign monitoring, but there is not enough victim-specific telemetry to attach the externally documented NightSpire TTPs to these organizations.

---

## 3. Incident-level tradecraft documented by Huntress

| Tactic | Technique | ATT&CK | Behavior | Evidence | Scope | Confidence | Provenance |
|---|---|---|---|---|---|---|---|
| Lateral Movement | Remote Desktop Protocol | T1021.001 | Actor accessed an endpoint through RDP | Observed | Incident-level | High | Huntress, March 2026 incident |
| C2 / Persistence | Remote Desktop Software | T1219.002 | Chrome Remote Desktop and AnyDesk installed as footholds | Observed | Incident-level | High | Huntress |
| Discovery | File and Directory Discovery | T1083 | Everything used to locate and access files | Observed | Incident-level | High | Huntress |
| Collection | Archive via Utility | T1560.001 | 7-Zip used to archive files | Observed | Incident-level | High | Huntress |
| Exfiltration | Exfiltration to Cloud Storage | T1567.002 | MEGASync executed and assessed as likely used for exfiltration | Assessed | Incident-level | Medium | Huntress |
| Impact | Data Encrypted for Impact | T1486 | NightSpire encryptor executed | Observed | Incident-level | High | Huntress |

Huntress did **not** validate the ransomware note's claim that 2.5 TB of data had been taken. AFRINTEL therefore does not treat that volume as confirmed.

---

## 4. Tools seen in the Huntress case

| Tool | Role | Evidence | Scope |
|---|---|---|---|
| RDP | Initial/remote access in the documented case | Observed | Incident-level |
| Chrome Remote Desktop | Remote access foothold | Observed | Incident-level |
| AnyDesk | Remote access foothold | Observed | Incident-level |
| Everything | File discovery / collection support | Observed | Incident-level |
| 7-Zip | Data staging / archiving | Observed | Incident-level |
| MEGASync | Likely exfiltration | Assessed | Incident-level |
| VMware Workstation | Installed in compromised environment | Observed | Incident-level |
| WPS Office | Installed in compromised environment | Observed | Incident-level |

VMware Workstation and WPS Office were observed in the environment, but their exact malicious purpose was not established by the source.

---

## 5. Historical IOCs from Huntress investigations

| Indicator | Context | Date / Scope | Confidence |
|---|---|---|---|
| `bde50a42efc079edde1a314243ad339db2d42e343fbbcd39117803b0f5960355` | SHA-256, `enc.exe` | 2 Dec 2025 incident | High |
| `ad67031e2ca68764fe1a7d6632c02b02a299d59efb920710011a9a2ccf4399b7` | SHA-256, `enc.exe` | 25 Mar 2026 incident | High |
| `.nspire` | Encrypted-file extension | Dec 2025 incident | High |
| `_nightspire_readme.txt` | Ransom note | Dec 2025 incident | High |
| `[nspire_msg].txt` | Ransom note | Mar 2026 incident | High |

These are historical incident indicators. AFRINTEL does not claim they were seen against the three Egyptian victims listed above.

---

## 6. Detection and threat-hunting opportunities

Useful correlations include:

- RDP access followed by installation of Chrome Remote Desktop or AnyDesk;
- new remote-access tools on systems that did not previously use them;
- Everything followed by access to high-value folders;
- 7-Zip archiving shortly after file discovery;
- MEGASync execution from a compromised endpoint;
- unusual combinations of remote access + collection + archiving + cloud sync;
- creation of `.nspire` files or the documented ransom-note names.

Because legitimate tools are involved, context and process lineage matter more than a single executable name.

---

## 7. Attribution assessment

The African victim association is based on NightSpire ransomware claims tracked by AFRINTEL. The TTPs in sections 3 and 4 come from a separate Huntress incident.

AFRINTEL therefore models them separately:

```text
NightSpire actor-level context
        +-- AFRINTEL African victim claims
        +-- Huntress incident-level TTPs
```

No victim-specific evidence currently proves that the Huntress tradecraft was used against B Investments, Rawaj Consumer Finance or Papa John's Egypt.

### Intelligence gaps for African cases

- initial-access vector;
- malware hashes;
- attacker infrastructure;
- authentication artifacts;
- lateral-movement method;
- exfiltration channel and volume;
- ransomware deployment method.

---

## 8. Sources

- Huntress - **Decoding NightSpire: Ransomware IOCs Aren't Set in Stone**
- MITRE ATT&CK
- AFRINTEL - May 2026 African ransomware victim intelligence

---

**AFRINTEL - African Cyber Threat Intelligence**
