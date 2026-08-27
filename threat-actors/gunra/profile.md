# Gunra - Threat Actor & Ransomware Profile

👉🏾 [**Version française disponible ici**](./profile_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Actor / Group:** Gunra
- **Known Alias / Branding:** Golden Community
- **Threat Type:** Ransomware / Double Extortion
- **Operating Model:** Ransomware-as-a-Service (RaaS)
- **Primary Motivation:** Financial
- **Platforms:** Windows and Linux
- **First observed by FBI:** April 2025
- **Formal RaaS expansion:** January 2026
- **Primary Source:** Joint #StopRansomware Advisory AA26-222A
- **Assessment Status:** Active monitoring
- **Last Updated:** 27 August 2026

---

## 1. Intelligence Summary

Gunra is a ransomware operation first observed by the FBI in April 2025. By January 2026, the operators had expanded into a formal RaaS program advertised on dark-web forums.

The operation uses a double-extortion model: affiliates steal data before encryption and threaten to publish or sell the material if the victim does not pay.

The August 2026 joint advisory from the FBI, CISA, NSA, DC3, USSS and the Republic of Korea National Police Agency documents activity against government, critical infrastructure and commercial organizations worldwide.

Gunra has also recruited penetration testers and ethical hackers as initial-access brokers in exchange for a share of ransom profits.

> **AFRINTEL rule:** Gunra affiliate behavior can vary. Techniques documented in the joint advisory are actor/campaign intelligence and are not automatically assigned to every Gunra victim.

---

## 2. AFRINTEL Observation in Africa

### 23 April 2025 - Egypt - Dar Al Teb

AFRINTEL recorded a Gunra ransomware claim against **Dar Al Teb**, an Egyptian medical center.

- **Country:** Egypt
- **Sector:** Healthcare
- **Website:** daralteb.com
- **Status:** Claim - Data Sample Published
- **Confidence level:** High
- **Impact level:** Level 4

AFRINTEL reviewed samples that included sensitive healthcare records and internal infrastructure material. The available evidence supported a high-confidence assessment of a genuine and extensive compromise.

The technical material reviewed by AFRINTEL included internal network and remote-access configuration artifacts. AFRINTEL does not reproduce patient information, secrets or internal access details.

**Important boundary:** the 2026 government advisory documents Gunra TTPs across several victims. AFRINTEL does not assume that every technique in that advisory was used against Dar Al Teb unless victim-specific evidence supports it.

**Evidence:** Observed sample / AFRINTEL analysis  
**Scope:** Victim-specific  
**Confidence:** High  
**Provenance:** AFRINTEL

---

## 3. Initial Access

The joint advisory states that Gunra actors primarily obtain access by exploiting known vulnerabilities in internet-facing devices, especially firewalls and VPN appliances.

### Documented vulnerabilities

| CVE | Product family | Role |
|---|---|---|
| CVE-2024-55591 | FortiOS / FortiProxy | Authentication bypass / initial access |
| CVE-2025-24472 | FortiOS / FortiProxy | Authentication bypass / initial access |

Relevant ATT&CK:

- **T1190 - Exploit Public-Facing Application**

The Republic of Korea National Police Agency also observed Gunra actors exploiting credential exposure and SSH access-control weaknesses on internet-facing VPN gateways.

Gunra has also used default credentials where account-lockout controls were absent.

Relevant ATT&CK:

- **T1078.001 - Valid Accounts: Default Accounts**
- **T1078.002 - Valid Accounts: Domain Accounts**
- **T1133 - External Remote Services**

---

## 4. Persistence and Command & Control

Gunra actors have modified existing accounts to keep access.

In one case, the actors changed an unused account so that the mandatory password-change requirement no longer applied.

- **T1098 - Account Manipulation**

The actors also downloaded OpenSSH from attacker-controlled infrastructure and used it to build persistent tunnels between compromised systems.

- **T1105 - Ingress Tool Transfer**
- **T1572 - Protocol Tunneling**

---

## 5. Credential Access

Gunra has a broad credential-access playbook.

### NTDS dumping

The FBI observed `secretsdump.py` being used against domain controllers to extract password hashes from NTDS.

- **T1003.003 - OS Credential Dumping: NTDS**

The stolen authentication material enabled:

- **T1550.002 - Pass the Hash**
- **T1550.003 - Pass the Ticket**

### Network sniffing and session theft

In one victim environment, Gunra actors abused SSL-VPN traffic controls to collect credentials and VDI session information in transit.

- **T1040 - Network Sniffing**
- **T1539 - Steal Web Session Cookie**

### MFA bypass

The actors modified authentication-processing files in a VDI portal so that an attacker-selected OTP value was accepted.

- **T1556.006 - Modify Authentication Process: Multi-Factor Authentication**

### Enterprise password stores

Gunra also stole an encryption key from a Hiware access-control server and used it to decrypt stored enterprise-server credentials.

- **T1555 - Credentials from Password Stores**
- **T1003 - OS Credential Dumping**

---

## 6. Discovery and Stealth

The Gunra binary enumerates files and directories across accessible drive letters using native Windows APIs.

- **T1106 - Native API**
- **T1083 - File and Directory Discovery**

The actors also enumerate active network connections to understand reachable internal infrastructure.

- **T1049 - System Network Connections Discovery**

Stealth behavior includes:

- clearing command history;
- deleting or clearing system/network access logs;
- performing reconnaissance late at night or early in the morning;
- using `IsDebuggerPresent` to detect debugging;
- excluding system-critical folders and file types from encryption.

Relevant ATT&CK includes:

- **T1070.003 - Clear Command History**
- **T1622 - Debugger Evasion**
- **T1678 - Delay Execution**
- **T1679 - Selective Exclusion**

---

## 7. Lateral Movement

Gunra actors use Impacket heavily.

Documented libraries include:

- `psexec.py`;
- `smbclient.py`;
- `secretsdump.py`.

For lateral movement, the advisory documents:

- SMB administrative shares;
- RDP;
- pass-the-hash;
- pass-the-ticket.

Relevant ATT&CK:

- **T1021.001 - Remote Desktop Protocol**
- **T1021.002 - SMB/Windows Admin Shares**
- **T1550.002 - Pass the Hash**
- **T1550.003 - Pass the Ticket**

---

## 8. Collection and Exfiltration

Gunra collects business documents, databases, PII and internal email.

### Cloud data collection

The FBI observed a malicious executable named `main.exe` used to target data stored in Microsoft OneDrive and Microsoft SharePoint.

Relevant ATT&CK:

- **T1530 - Data from Cloud Storage**
- **T1114 - Email Collection**
- **T1005 - Data from Local System**

### Archiving and transfer

Observed tools include:

- 7-Zip;
- WinRAR;
- RClone;
- FileZilla.

At least one victim had compressed archives exfiltrated to **Mega**, with the stolen volume reaching tens of terabytes.

Relevant ATT&CK:

- **T1560 - Archive Collected Data**
- **T1567 - Exfiltration Over Web Service**
- **T1048 - Exfiltration Over Alternative Protocol**

> The joint advisory documents Mega and FTP/FileZilla. AFRINTEL therefore does not describe the default Gunra exfiltration path as "masked system utilities over C2" unless a specific incident supports that statement.

---

## 9. Impact

Gunra uses a multi-threaded encryptor with **ChaCha20 + RSA-4096**.

The advisory documents Windows and Linux encryptors and encryption of critical systems including database servers and NAS assets.

Relevant ATT&CK:

- **T1486 - Data Encrypted for Impact**

### File extensions

Documented extensions include:

```text
.ENCRT
.CRYPT
```

The `.CRYPT` extension was documented in one July 2025 sample.

### Ransom note

The advisory text identifies a ransom note named:

```text
R3ADM3.txt
```

One mirrored ATT&CK table transcription shows `R34DM3.txt`. AFRINTEL keeps `R3ADM3.txt` as the main documented filename but notes this source transcription difference instead of silently treating both as separate indicators.

---

## 10. Inhibit System Recovery

The government advisory does **not** use `vssadmin.exe delete shadows /all /quiet` as its documented Gunra example.

The documented behavior uses WMI/WMIC to delete selected shadow copies:

```text
cmd.exe /c C:\Windows\System32\wbem\WMIC.exe shadowcopy where "ID='{GUID}'" delete
```

Relevant ATT&CK:

- **T1047 - Windows Management Instrumentation**
- **T1059.003 - Windows Command Shell**
- **T1490 - Inhibit System Recovery**

In one incident, Gunra actors also deleted backup and archived data stored in both the primary data center and the disaster recovery center.

> AFRINTEL does not include "registry modification to block security alerts" as a core Gunra behavior because the selected joint advisory does not support that claim.

---

## 11. Notable Tools

| Tool | Documented role |
|---|---|
| Impacket `psexec.py` | Lateral movement |
| Impacket `smbclient.py` | SMB access / movement |
| Impacket `secretsdump.py` | NTDS credential dumping |
| OpenSSH | Persistent tunneling |
| 7-Zip | Archiving |
| WinRAR | Archiving |
| RClone | Collection / transfer |
| FileZilla | FTP exfiltration |
| MobaXterm | Remote administration |
| AnyDesk | Remote access |
| Google Remote Desktop | Remote access |
| Mimikatz | Credential access |

The presence of one of these tools alone is not proof of Gunra activity.

---

## 12. Detection and Hunting Opportunities

| Signal | Why it matters |
|---|---|
| Exploitation attempts against vulnerable FortiOS/FortiProxy | Initial access |
| New or altered Fortinet privileged accounts | Persistence / exploitation artifact |
| `secretsdump.py` against domain controllers | NTDS dumping |
| OpenSSH downloaded to systems that do not normally use it | Tunnel persistence |
| Unexpected RDP from VDI sessions | Lateral movement |
| VDI authentication files modified | MFA bypass |
| `main.exe` accessing OneDrive/SharePoint data | Cloud collection |
| Large archives followed by Mega or FTP transfer | Exfiltration |
| WMIC shadow-copy deletion | Recovery inhibition |
| `.ENCRT` files or `R3ADM3.txt` | Encryption activity |

These are detection signals and must be correlated with context before attribution.

---

## 13. AFRINTEL Assessment

The initial draft correctly identified Gunra as a new RaaS that expanded in 2026, but several technical details needed correction.

The strongest current evidence supports:

- Fortinet vulnerability exploitation for initial access;
- default/stolen account abuse;
- NTDS dumping and session theft;
- SSH tunneling;
- RDP/SMB lateral movement;
- OneDrive/SharePoint collection;
- Mega and FTP exfiltration;
- WMI-based shadow-copy deletion;
- Windows and Linux encryption.

AFRINTEL keeps these government-documented TTPs separate from the evidence collected for the Dar Al Teb victim.

---

## 14. Sources

- CISA / FBI / NSA / DC3 / USSS / KNPA - **#StopRansomware: Gunra Ransomware (AA26-222A)**  
  https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a
- CISA release notice  
  https://content.govdelivery.com/accounts/USDHSCISA/bulletins/4244745
- NSA - *Guidance to Defend Against Gunra Ransomware*  
  https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4567025/nsa-joins-fbi-and-others-in-releasing-guidance-to-defend-against-gunra-ransomwa/
- AFRINTEL - Dar Al Teb / Egypt, 23 April 2025

---

**AFRINTEL - African Cyber Threat Intelligence**
