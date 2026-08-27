# Ryuk / Wizard Spider - Ransomware, Actor Context & DFIR Reference

👉🏾 [**Version française**](./ryuk_profile_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Ransomware / Malware:** Ryuk
- **MITRE ATT&CK software:** S0446
- **Associated threat group:** Wizard Spider
- **MITRE ATT&CK group:** G0102
- **Associated groups / aliases include:** UNC1878, FIN12 and others listed by MITRE ATT&CK
- **Threat type:** Ransomware / Big-game hunting
- **Motivation:** Financial
- **DFIR reference:** Ryuk Speed Run - 2 Hours to Ransom
- **Reference date:** 5 November 2020
- **Geography:** external DFIR case, not an AFRINTEL African victim
- **Status:** Historical tradecraft reference
- **Last updated:** 26 August 2026

---

## 1. Entity-modeling note

Ryuk is **malware**, not a threat actor by itself. MITRE ATT&CK tracks Ryuk as software **S0446**. Wizard Spider is tracked separately as group **G0102**, with UNC1878 among its associated-group names.

AFRINTEL therefore keeps these entities separate:

```text
Ryuk (malware)
Wizard Spider / UNC1878 (actor context)
Ryuk Speed Run (one DFIR incident)
```

A Ryuk binary in an unrelated incident is not enough, on its own, to attribute that incident to Wizard Spider.

---

## 2. Intelligence summary

The DFIR Report documented a real intrusion that moved from BazarLoader execution to Ryuk deployment in about two hours. The environment was fully encrypted roughly three hours after the initial BazarLoader execution.

The case included phishing, BazarLoader, Cobalt Strike, Active Directory discovery, Rubeus/Kerberoasting, exploitation of Zerologon (`CVE-2020-1472`), process injection, RDP/SMB lateral movement, FTP exfiltration and Ryuk deployment.

This profile keeps **incident evidence** separate from broader Wizard Spider and Ryuk context.

---

## 3. DFIR timeline

| Approx. time | Activity | Evidence | Scope | Confidence | Provenance |
|---|---|---|---|---|---|
| T+00 | Phishing link leads to BazarLoader download and execution | Observed | Incident | High | The DFIR Report |
| < T+05 | `net view`, `nltest` and domain discovery | Observed | Incident | High | The DFIR Report |
| ~ T+07 | AdFind used for Active Directory discovery | Observed | Incident | High | The DFIR Report |
| < T+10 | Cobalt Strike beacons deployed | Observed | Incident | High | The DFIR Report |
| Early | Scheduled tasks and Registry Run key established | Observed | Incident | High | The DFIR Report |
| Early | Zerologon exploited for Domain Admin privileges | Observed | Incident | High | The DFIR Report |
| Early | Rubeus used for Kerberoasting | Observed | Incident | High | The DFIR Report |
| Early | Process injection into `svchost.exe` | Observed | Incident | High | The DFIR Report |
| ~ T+60 | RDP and SMB/ADMIN$ movement to domain controllers | Observed | Incident | High | The DFIR Report |
| Before impact | AdFind/Rubeus output exfiltrated over FTP to `5.2.70.149:21` | Observed | Incident | High | The DFIR Report |
| ~ T+120 | Ryuk deployment begins through RDP | Observed | Incident | High | The DFIR Report |
| ~ T+180 | Environment encryption completed | Observed | Incident | High | The DFIR Report |

The phrase **"2 Hours to Ransom"** refers to the start of Ryuk deployment, not completion of the whole attack.

---

## 4. MITRE ATT&CK mapping for this incident

| Tactic | Technique | ATT&CK | Incident behavior | Evidence | Provenance |
|---|---|---|---|---|---|
| Initial Access | Spearphishing Link | T1566.002 | Link leads to BazarLoader | Observed | The DFIR Report |
| Execution | User Execution | T1204 | User executes BazarLoader | Observed | The DFIR Report |
| Defense Evasion | Process Injection | T1055 | Injection into `svchost.exe` | Observed | The DFIR Report |
| Defense Evasion | Code Signing | T1553.002 | BazarLoader and Cobalt Strike-related binaries used signing certificates | Observed | The DFIR Report |
| Persistence | Scheduled Task | T1053.005 | Scheduled tasks on initial host | Observed | The DFIR Report |
| Persistence | Registry Run Keys / Startup Folder | T1547.001 | Registry Run persistence | Observed | The DFIR Report |
| Privilege Escalation | Exploitation for Privilege Escalation | T1068 | Zerologon (`CVE-2020-1472`) | Observed | The DFIR Report |
| Credential Access | Kerberoasting | T1558.003 | Rubeus used to Kerberoast | Observed | The DFIR Report |
| Discovery | Domain Trust Discovery | T1482 | `nltest` / AdFind | Observed | The DFIR Report |
| Discovery | Permission Groups Discovery: Domain Groups | T1069.002 | Domain-group enumeration | Observed | The DFIR Report |
| Discovery | Account Discovery: Domain Account | T1087.002 | Domain-account enumeration | Observed | The DFIR Report |
| Discovery | Remote System Discovery | T1018 | Host discovery | Observed | The DFIR Report |
| Lateral Movement | Remote Desktop Protocol | T1021.001 | RDP to domain controllers and servers | Observed | The DFIR Report |
| Lateral Movement | SMB/Windows Admin Shares | T1021.002 | Payloads copied through `ADMIN$` | Observed | The DFIR Report |
| Execution | Service Execution | T1569.002 | Remote executables run as services | Observed | The DFIR Report |
| Exfiltration | Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol | T1048.003 | Discovery output sent over FTP | Observed | The DFIR Report |
| Impact | Service Stop | T1489 | Veeam/SQL-related services and processes stopped before encryption | Observed | The DFIR Report + AFRINTEL mapping |
| Impact | Data Encrypted for Impact | T1486 | Ryuk encryption | Observed | The DFIR Report |

---

## 5. Tools and malware

| Tool / Malware | Role | Evidence | Scope |
|---|---|---|---|
| BazarLoader | Initial malware / backdoor | Observed | Incident |
| Cobalt Strike | Post-exploitation / C2 | Observed | Incident |
| AdFind | Active Directory discovery | Observed | Incident |
| Rubeus | Kerberoasting | Observed | Incident |
| Zerologon exploit | Privilege escalation | Observed | Incident |
| PowerShell AD module | Domain-controller discovery | Observed | Incident |
| RDP | Lateral movement / Ryuk deployment | Observed | Incident |
| SMB / ADMIN$ | Payload transfer | Observed | Incident |
| Ryuk | Ransomware impact | Observed | Incident |

---

## 6. Network infrastructure and historical IOCs

| Indicator | Context |
|---|---|
| `dghns.xyz` | BazarLoader C2 |
| `34.222.33.48:443` | BazarLoader C2 |
| `checktodrivers.com` | Suspected Cobalt Strike |
| `45.153.240.240:443` | Suspected Cobalt Strike |
| `topservicebooster.com` | Suspected Cobalt Strike |
| `108.62.12.121:443` | Suspected Cobalt Strike |
| `chaseltd.top` | C2 / gate |
| `161.117.191.245:80` | C2 |
| `5.2.70.149:21` | FTP exfiltration destination |

### TLS fingerprints from the case

```text
BazarLoader
JA3:  9e10692f1b7f78228b2d4e424db3a98c
JA3s: 2b33c1374db4ddf06942f92373c0b54b

checktodrivers.com
JA3:  37f463bf4616ecd445d4a1937da06e19
JA3s: ae4edc6faf64d08308082ad26be60767

topservicebooster.com
JA3:  2c14bfb3f8a2067fbc88d8345e9f97f3
JA3s: 649d6810e8392f63dc311eecb6b7098b
```

These are historical IOCs from the 2020 case and should not be treated as current infrastructure.

---

## 7. File IOCs from the incident

| File | SHA-256 |
|---|---|
| `Report-Review20-10.exe.exe` | `0d468fc1b02bbc7c3050c67e0a80b580c69abd8eea5f8dad06c7d7ff396f7789` |
| `Firefox.exe` | `3fc65b7e7967353f340ead51617558a23f14447ab91d974268f53ab0c17052e0` |
| `pagefilerpqy.exe` | `a4468c28e4830acf526209c0da25536ff0f682a0239ced1983a08d1ddd476963` |
| `pagefileU6Gl.sys` | `13671077b66a29874a2578b5240319092ef2a1043228e433e9b006b5e53e7513` |
| `pagefilerpqy.sys` | `8241649609f88ccd2a0a5b233a07a538ec313ff6adf695aa44a969dbca39f67d` |
| `AdFind.exe` | `68d0f5659cf3cc1cf53519e1be482ca9a63f2deebdcd2cb7ee12515adc6db0a7` |
| `PL64.exe` | `a7514209db9d9c7c51927308d4f0b491464e11391af3c6ae31cb87d91fac995d` |
| `fx2-12_multi_for_crypt_x86.exe` | `34007d53a8e64bf1dbbeace9e4878fb209878e6a6843251895d4dc9c2699056e` |

---

## 8. Detection and threat-hunting opportunities

Useful signals from this case include:

- phishing download followed by BazarLoader execution;
- domain discovery within minutes of first execution;
- AdFind and Rubeus appearing early in the intrusion;
- Cobalt Strike deployment shortly after initial access;
- Zerologon exploitation followed by rapid Domain Admin activity;
- RDP from the beachhead to domain controllers;
- executables copied to `ADMIN$` and run as services;
- FTP to an unusual external server after discovery output is produced;
- bulk stop/kill of Veeam and SQL services shortly before encryption;
- Ryuk deployment from domain controllers over RDP.

---

## 9. Attribution assessment

The DFIR Report referenced FireEye tracking of UNC1878 and noted alignment with Ryuk tradecraft. Current MITRE ATT&CK lists UNC1878 among the associated-group names for Wizard Spider.

AFRINTEL therefore records the relationship as **attribution context**, not as a universal rule:

```text
DFIR Incident
  +-- uses --> BazarLoader
  +-- uses --> Cobalt Strike
  +-- uses --> AdFind / Rubeus
  +-- exploits --> CVE-2020-1472
  +-- deploys --> Ryuk (S0446)
  +-- attribution context --> UNC1878 / Wizard Spider (G0102)
```

### Intelligence gaps

The public case does not establish:

- the identity of individual operators;
- that all Ryuk intrusions used the same team;
- that the infrastructure remained active after 2020;
- that every Ryuk infection should be attributed to Wizard Spider;
- a state or geopolitical motivation for the incident.

---

## 10. Sources

- The DFIR Report - **Ryuk Speed Run, 2 Hours to Ransom**, 5 November 2020
- MITRE ATT&CK - **Ryuk S0446**
- MITRE ATT&CK - **Wizard Spider G0102**

---

**AFRINTEL - African Cyber Threat Intelligence**
