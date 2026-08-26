# Akira - Threat Actor / Ransomware Profile

👉🏾 [**Version française**](./akira_profile_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Actor / Operation:** Akira
- **Threat type:** Ransomware / Double extortion
- **Operating model:** Ransomware-as-a-Service (RaaS)
- **Motivation:** Financial
- **Activity tracked:** 2023-2026
- **Technical evidence covered here:** public reporting through November 2025
- **Targeted environments:** Windows, VMware ESXi, Hyper-V, Nutanix AHV
- **Assessment status:** Active monitoring
- **Last updated:** 26 August 2026

---

## 1. Intelligence summary

Akira is a financially motivated ransomware operation active since 2023. Public reporting shows a mix of stolen credentials, exposed remote services, exploitation of edge devices and unpatched systems, rapid internal discovery, credential theft, data exfiltration and encryption.

The November 2025 FBI/CISA/DC3/HHS update expanded the known Akira tradecraft. It documents activity involving VPN credentials, password spraying, SSH, Veeam exploitation, domain-account creation, LSASS/SAM/NTDS access, EDR disruption, tunneling, remote-access tools and newer Akira_v2 capabilities.

Historical Akira builds were mainly C++. Megazord and Akira_v2 introduced Rust-based encryptors. The joint advisory states that Megazord has likely fallen out of use since 2024, while Akira_v2 represents a more recent evolution.

> **AFRINTEL boundary:** These are actor-level or externally reported behaviors. They must not be attached to a specific AFRINTEL victim without incident-specific evidence.

---

## 2. Key TTPs

| Tactic | Technique | ATT&CK | Behavior | Evidence | Scope | Confidence | Provenance |
|---|---|---|---|---|---|---|---|
| Initial Access | Exploit Public-Facing Application | T1190 | Exploitation of vulnerable VPN, edge and backup products | Reported | Actor-level | High | FBI/CISA joint advisory |
| Initial Access | Valid Accounts | T1078 | Use of compromised VPN credentials | Reported | Actor-level | High | FBI/CISA joint advisory |
| Initial Access | External Remote Services | T1133 | Access through exposed remote services including RDP/VPN | Reported | Actor-level | High | FBI/CISA joint advisory |
| Credential Access | Brute Force | T1110 | Brute-forcing VPN and SSH endpoints | Reported | Actor-level | High | FBI/CISA joint advisory |
| Credential Access | Password Spraying | T1110.003 | SharpDomainSpray used for password spraying | Reported | Actor-level | High | FBI/CISA joint advisory |
| Execution | Visual Basic | T1059.005 | VB scripts used to execute malicious commands | Reported | Actor-level | High | FBI/CISA joint advisory |
| Persistence | Create Domain Account | T1136.002 | New domain accounts created; `itadm` observed in some incidents | Reported | Actor-level | High | FBI/CISA joint advisory |
| Credential Access | LSASS Memory | T1003.001 | Credential extraction from LSASS; Mimikatz and LaZagne also observed | Reported | Actor-level | High | FBI/CISA joint advisory |
| Credential Access | Security Account Manager | T1003.002 | SYSTEM/SAM-related credential extraction in documented activity | Reported | Actor-level | High | FBI/CISA joint advisory |
| Credential Access | NTDS | T1003.003 | NTDS.dit obtained from a domain-controller VM workflow | Reported | Actor-level | High | FBI/CISA joint advisory |
| Discovery | Network Service Discovery | T1046 | Advanced IP Scanner, NetScan and similar tools | Reported | Actor-level | High | FBI/CISA joint advisory |
| Discovery | Remote System Discovery | T1018 | `nltest` and Windows commands used to identify systems/DCs | Reported | Actor-level | High | FBI/CISA joint advisory |
| Discovery | Domain Trust Discovery | T1482 | Domain trust enumeration | Reported | Actor-level | High | FBI/CISA joint advisory |
| Defense Evasion | Disable or Modify Tools | T1562.001 | PowerTool/BYOVD and EDR removal used to impair defenses | Reported | Actor-level | High | FBI/CISA joint advisory |
| Defense Evasion | Disable or Modify System Firewall | T1562.004 | Firewall changes observed in updated reporting | Reported | Actor-level | High | FBI/CISA joint advisory |
| Lateral Movement | Remote Desktop Protocol | T1021.001 | RDP used to move through compromised networks | Reported | Actor-level | High | FBI/CISA joint advisory |
| Lateral Movement | SSH | T1021.004 | SSH used for access and lateral movement | Reported | Actor-level | High | FBI/CISA joint advisory |
| C2 | Proxy | T1090 | Ngrok/SystemBC used for proxying and concealed traffic | Reported | Actor-level | High | FBI/CISA joint advisory |
| C2 | Ingress Tool Transfer | T1105 | Tools and Cobalt Strike beacons downloaded; STONESTOP used as loader | Reported | Actor-level | High | FBI/CISA joint advisory |
| C2 | Remote Access Software | T1219 | AnyDesk, LogMeIn and other legitimate tools abused | Reported | Actor-level | High | FBI/CISA joint advisory |
| C2 | Protocol Tunneling | T1572 | Ngrok used to tunnel traffic through HTTPS | Reported | Actor-level | High | FBI/CISA joint advisory |
| Collection | Archive via Utility | T1560.001 | WinRAR used to prepare data | Reported | Actor-level | High | FBI/CISA joint advisory |
| Exfiltration | Exfiltration Over Alternative Protocol | T1048 | WinSCP and related tools used for transfer | Reported | Actor-level | High | FBI/CISA joint advisory |
| Exfiltration | Transfer Data to Cloud Account | T1537 | Cloud storage used as an exfiltration destination | Reported | Actor-level | High | FBI/CISA joint advisory |
| Exfiltration | Exfiltration to Cloud Storage | T1567.002 | RClone used to sync data to cloud storage | Reported | Actor-level | High | FBI/CISA joint advisory |
| Impact | Data Encrypted for Impact | T1486 | Windows and virtual infrastructure encryption | Reported | Actor-level | High | FBI/CISA joint advisory |
| Impact | Inhibit System Recovery | T1490 | VSS copies deleted on Windows systems | Reported | Actor-level | High | FBI/CISA joint advisory |

---

## 3. Vulnerabilities documented in Akira operations

| CVE | Product / context | Documented use | Confidence |
|---|---|---|---|
| CVE-2020-3259 | Cisco ASA / FTD | Initial access / credential exposure | High |
| CVE-2023-20269 | Cisco ASA / FTD | Initial access | High |
| CVE-2020-3580 | Cisco ASA / FTD | Added in November 2025 update | High |
| CVE-2023-28252 | Microsoft Windows CLFS | Akira-associated CVE in the 2025 advisory; the CVE itself is a Windows privilege-escalation flaw | High for association; incident context required |
| CVE-2024-37085 | VMware ESXi | Authentication bypass; listed as Akira-associated in the 2025 advisory | High |
| CVE-2023-27532 | Veeam Backup & Replication | Exploitation of unpatched Veeam systems | High |
| CVE-2024-40711 | Veeam Backup & Replication | Exploitation / privilege-escalation context | High |
| CVE-2024-40766 | SonicWall SonicOS | Initial access; also linked to June 2025 AHV incident chain | High |

AFRINTEL does not assume that one of these CVEs was used against an African Akira victim unless the incident provides evidence for it.

---

## 4. Tooling and malware

| Tool / Malware | Role | Evidence | Scope |
|---|---|---|---|
| Advanced IP Scanner / NetScan | Network discovery | Reported | Actor-level |
| Mimikatz / LaZagne / NetExec | Credential access | Reported | Actor-level |
| SharpDomainSpray | Password spraying | Reported | Actor-level |
| AnyDesk / LogMeIn / MobaXterm | Remote access / lateral movement | Reported | Actor-level |
| Impacket / `wmiexec.py` | Remote execution | Reported | Actor-level |
| PowerTool | Disable antivirus processes | Reported | Actor-level |
| POORTRY | BYOVD driver abuse | Reported | Actor-level |
| STONESTOP | Loader / installer for additional payloads | Reported | Actor-level |
| SystemBC | RAT / proxy bot | Reported | Actor-level |
| Cobalt Strike | Post-exploitation / C2 | Reported | Actor-level |
| Ngrok / Cloudflare Tunnel | Tunneling / C2 / exfiltration support | Reported | Actor-level |
| RClone / WinSCP / FileZilla | Data transfer / exfiltration | Reported | Actor-level |
| WinRAR | Data archiving | Reported | Actor-level |
| Akira_v2 | Ransomware encryptor | Reported | Actor-level |
| Megazord | Historical Rust encryptor; likely out of use since 2024 | Reported | Actor-level |

Legitimate administration tools are not malicious by themselves. They require context before being treated as an Akira indicator.

---

## 5. Ransomware artifacts

Documented encrypted-file extensions include:

```text
.akira
.powerranges
.akiranew
.aki
```

Documented ransom-note names include:

```text
fn.txt
akira_readme.txt
akiranew.txt
```

Akira_v2 uses Rust and supports more granular encryption behavior, including VM-focused options. Public reporting also documents Akira activity against VMware ESXi, Hyper-V and, in a June 2025 incident, Nutanix AHV disk files.

---

## 6. Detection and threat-hunting opportunities

Useful behaviors to correlate include:

- new or unusual VPN/RDP/SSH access followed by rapid discovery;
- password spraying against remote-access services;
- creation of unexpected domain administrator accounts such as `itadm`;
- `nltest`, Advanced IP Scanner or NetScan after remote access;
- LSASS, SAM or NTDS access;
- unexpected AnyDesk, LogMeIn, MobaXterm, Ngrok or SystemBC activity;
- EDR uninstall attempts or PowerTool/BYOVD activity;
- tools staged in `PerfLogs`;
- `WebClient.DownloadString()` followed by Cobalt Strike-related activity;
- RClone/WinSCP transfers after large archive creation;
- VSS deletion followed by ransomware execution.

These are hunting leads, not standalone attribution rules.

---

## 7. AFRINTEL assessment

The strongest way to use this profile is as **actor-level context**. It helps analysts understand what Akira affiliates have done across documented incidents.

For an AFRINTEL victim, the analyst should separately establish the initial access vector, exploited CVE, compromised account, tooling, lateral movement, exfiltration and ransomware deployment method before assigning victim-specific TTPs.

### Intelligence gaps at victim level

- initial access vector;
- exact compromised account;
- CVE actually exploited;
- C2 infrastructure;
- tool and ransomware hashes;
- observed command lines;
- lateral-movement method;
- exfiltration destination;
- encryption/deployment method.

---

## 8. Sources

- FBI / CISA / DC3 / HHS - **#StopRansomware: Akira Ransomware (AA24-109A)**, updated 13 November 2025
- MITRE ATT&CK
- AFRINTEL victim intelligence when a specific African incident is referenced

---

**AFRINTEL - African Cyber Threat Intelligence**
