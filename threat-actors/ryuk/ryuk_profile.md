# Ryuk / Wizard Spider - Threat Actor & Ransomware Profile

👉🏾 [**French version available here**](./ryuk_profile_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Ransomware / Malware:** Ryuk
- **MITRE ATT&CK software:** S0446
- **Associated threat group:** Wizard Spider
- **MITRE ATT&CK group:** G0102
- **Historical/current ATT&CK alias:** UNC1878 (among other Wizard Spider aliases)
- **Threat type:** Ransomware / Big-game hunting
- **Motivation:** Financial
- **DFIR reference case:** Ryuk Speed Run - 2 Hours to Ransom
- **Reference case date:** 2020
- **Geography:** External DFIR reference case; not an AFRINTEL Africa-specific victim case
- **Assessment status:** Historical reference / tradecraft study
- **Last updated:** 25 August 2026

---

## 1. Entity Modeling Note

Ryuk is **malware/ransomware**, not a threat actor by itself.

MITRE ATT&CK tracks Ryuk as software **S0446** and lists **Wizard Spider (G0102)** and **FIN6 (G0037)** among groups that have used it. MITRE currently includes **UNC1878** among Wizard Spider aliases.

AFRINTEL therefore separates:

- **Ryuk** - ransomware / malware;
- **Wizard Spider / UNC1878** - threat actor / intrusion-cluster attribution;
- **this DFIR case** - incident-specific observed tradecraft;
- **generic Ryuk TTPs** - actor/malware-level intelligence that must not automatically be applied to every Ryuk incident.

---

## 2. Intelligence Summary

The DFIR Report documented a real intrusion in which operators progressed from **BazarLoader execution to Ryuk deployment in approximately two hours**, with the full environment encrypted approximately three hours after initial execution.

The case provides a complete evidence chain including phishing, BazarLoader, Cobalt Strike, Active Directory discovery, Rubeus/Kerberoasting, Zerologon, RDP/SMB lateral movement, FTP exfiltration, Ryuk deployment, hashes, network infrastructure and ATT&CK mappings.

AFRINTEL uses this as a **DFIR reference case** and does not assume the same chain occurred in every Ryuk intrusion.

---

## 3. DFIR Reference Case - Ryuk Speed Run

**Primary source:** The DFIR Report  
**Publication:** 5 November 2020  
**Evidence type:** Incident-response / DFIR technical reporting

| Approx. time | Phase | Activity | Evidence |
|---|---|---|---|
| T+00 | Initial Access | User follows phishing link and downloads BazarLoader | DFIR_OBSERVED |
| T+00 | Execution | User executes BazarLoader | DFIR_OBSERVED |
| < T+05 | Discovery | `net view`, `nltest`, group/domain discovery | DFIR_OBSERVED |
| ~ T+07 | Discovery | AdFind used for AD discovery | DFIR_OBSERVED |
| < T+10 | C2 | Cobalt Strike beacons deployed | DFIR_OBSERVED |
| Early intrusion | Persistence | Scheduled tasks and Registry Run key created | DFIR_OBSERVED |
| Early intrusion | Privilege Escalation | Zerologon (`CVE-2020-1472`) exploited for Domain Admin | DFIR_OBSERVED |
| Early intrusion | Credential Access | Rubeus used for Kerberoasting | DFIR_OBSERVED |
| Early intrusion | Defense Evasion | Process injection into `svchost.exe` | DFIR_OBSERVED |
| ~ T+60 | Lateral Movement | RDP + SMB/ADMIN$ to domain controllers | DFIR_OBSERVED |
| Before impact | Exfiltration | AdFind/Rubeus output sent via FTP to `5.2.70.149:21` | DFIR_OBSERVED |
| ~ T+120 | Impact | Ryuk deployment begins via RDP | DFIR_OBSERVED |
| ~ T+180 | Impact | Environment encryption completed | DFIR_OBSERVED |

**Analytical note:** two hours refers to the start of Ryuk deployment, not completion of the entire intrusion.

---

## 4. MITRE ATT&CK Mapping

| Tactic | Technique | ID | Incident behavior | Evidence |
|---|---|---|---|---|
| Initial Access | Spearphishing Link | T1566.002 | Phishing link leads to BazarLoader | DFIR_OBSERVED |
| Execution | User Execution | T1204 | User runs BazarLoader | DFIR_OBSERVED |
| Defense Evasion | Process Injection | T1055 | Injection into `svchost.exe` | DFIR_OBSERVED |
| Persistence | Scheduled Task | T1053.005 | Scheduled tasks on beachhead | DFIR_OBSERVED |
| Persistence | Registry Run Keys / Startup Folder | T1547.001 | Registry Run persistence | DFIR_OBSERVED |
| Privilege Escalation | Exploitation for Privilege Escalation | T1068 | Zerologon | DFIR_OBSERVED |
| Credential Access | Kerberoasting | T1558.003 | Rubeus | DFIR_OBSERVED |
| Discovery | Domain Trust Discovery | T1482 | `nltest` / AdFind | DFIR_OBSERVED |
| Discovery | Domain Groups | T1069.002 | Domain-group enumeration | DFIR_OBSERVED |
| Discovery | Domain Account | T1087.002 | Account/person discovery | DFIR_OBSERVED |
| Discovery | Remote System Discovery | T1018 | Host/computer enumeration | DFIR_OBSERVED |
| Lateral Movement | Remote Desktop Protocol | T1021.001 | RDP to DCs/servers | DFIR_OBSERVED |
| Lateral Movement | SMB/Windows Admin Shares | T1021.002 | Payloads via `ADMIN$` | DFIR_OBSERVED |
| Execution | Service Execution | T1569.002 | Remote binaries executed as services | DFIR_OBSERVED |
| Exfiltration | Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol | T1048.003 | FTP exfiltration | DFIR_OBSERVED |
| Defense Evasion | Code Signing | T1553.002 | Signed malware/beacon-related binaries | DFIR_OBSERVED |
| Impact | Data Encrypted for Impact | T1486 | Ryuk encryption | DFIR_OBSERVED |

**Boundary:** The DFIR Report provides incident evidence. MITRE ATT&CK provides taxonomy and actor/software context.

---

## 5. Discovery Artifacts

```text
net view /all
net view /all /domain
nltest /domain_trusts /all_trusts
net localgroup "administrator"
net group "domain admins" /dom
```

```text
AdFind.exe -f "(objectcategory=person)"
AdFind.exe -f "(objectcategory=computer)"
AdFind.exe -f "(objectcategory=organizationalUnit)"
AdFind.exe -sc trustdmp
AdFind.exe -subnets -f "(objectCategory=subnet)"
AdFind.exe -f "(objectcategory=group)"
AdFind.exe -gcb -sc trustdmp
```

---

## 6. Tooling and Malware

| Tool / Malware | Role | Evidence |
|---|---|---|
| BazarLoader | Initial malware / backdoor | DFIR_OBSERVED |
| Cobalt Strike | Post-exploitation C2 | DFIR_OBSERVED |
| AdFind | Active Directory discovery | DFIR_OBSERVED |
| Rubeus | Kerberoasting | DFIR_OBSERVED |
| Zerologon exploit | Privilege escalation | DFIR_OBSERVED |
| PowerShell AD module | Domain-controller discovery | DFIR_OBSERVED |
| RDP | Lateral movement / Ryuk deployment | DFIR_OBSERVED |
| SMB / ADMIN$ | Payload transfer | DFIR_OBSERVED |
| Ryuk | Ransomware impact | DFIR_OBSERVED |

---

## 7. C2 and Network Infrastructure

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

### TLS fingerprints

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

---

## 8. Incident-Specific File IOCs

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

These are **historical incident-specific IOCs**, not current Ryuk infrastructure.

---

## 9. Attribution Assessment

The DFIR report references FireEye tracking of **UNC1878** and notes alignment with Ryuk tradecraft.

Current MITRE ATT&CK context:

- Ryuk = **S0446**
- Wizard Spider = **G0102**
- UNC1878 is currently listed as a Wizard Spider alias
- Ryuk is listed among software used by Wizard Spider
- FIN6 is also listed as a group that has used Ryuk

AFRINTEL therefore models:

```text
Incident
  +-- uses --> BazarLoader
  +-- uses --> Cobalt Strike
  +-- uses --> AdFind
  +-- uses --> Rubeus
  +-- exploits --> CVE-2020-1472
  +-- deploys --> Ryuk (S0446)
  +-- attribution context --> UNC1878 / Wizard Spider
```

AFRINTEL does **not** treat "Ryuk detected" as sufficient to attribute an unrelated incident to Wizard Spider.

---

## 10. Evidence Model

- **DFIR_OBSERVED** - directly documented in incident-response evidence.
- **EXTERNAL_REPORTED** - reported by a trusted external CTI source.
- **ATTACK_CONTEXT** - current MITRE ATT&CK taxonomy/relationship.
- **ANALYST_MAPPED** - behavior normalized by AFRINTEL to ATT&CK.
- **INFERRED** - plausible but not confirmed.

---

## 11. Excluded Artifact

The Cobalt Strike named-pipe example:

```text
\\.\pipe\msagent_xx
```

is **not documented in the cited Ryuk Speed Run case** and is therefore excluded from this incident-specific IOC set.

---

## 12. Intelligence Gaps

The public case does not establish:

- the identity of individual operators;
- that all Ryuk intrusions used the same team;
- that historical infrastructure remained active after the case;
- that every Ryuk infection should be attributed to Wizard Spider;
- any state/geopolitical motivation for this incident.

---

## 13. Sources

- The DFIR Report - Ryuk Speed Run, 2 Hours to Ransom  
  https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/

- MITRE ATT&CK - Ryuk S0446  
  https://attack.mitre.org/software/S0446/

- MITRE ATT&CK - Wizard Spider G0102  
  https://attack.mitre.org/groups/G0102/

---

**AFRINTEL - African Cyber Threat Intelligence**
