# DevMan Ransomware Group - Comprehensive Profile

**Date of Analysis:** 2026-03-08  
**Source:** Halcyon Threat Intelligence (October 2025) & internal research  
**Threat Level:** 7.2 (High)  
**Current Status:** Active (as of October 2025, with sustained operations through 2026)

---

## Description
Emerging in **April 2025**, DevMan is a **closed‑operation ransomware group** that operates as a **multi‑RaaS affiliate** (Qilin, DragonForce, Apos, RansomHub) while also running its own direct attacks. It maintains full control over the attack lifecycle and targets small‑to‑medium enterprises, with revenue thresholds of **$100M+ for critical infrastructure** and **$50M+ for healthcare**.  

Despite the **June 2025 GangExposed doxing**, the group rapidly evolved to **version 2.0** (rewritten in Rust) and continues to acquire victims across Asia‑Pacific, North America, and Europe.

---

## Classifications & Affiliations
- **Type:** Closed Group – no external affiliate recruitment; direct attacks with proprietary toolset.
- **Multi‑RaaS Partnerships:**
  - **Qilin** (primary) – 80‑85% revenue share.
  - **DragonForce** (technical lineage, builder usage).
  - **Apos, RansomHub** – additional affiliate roles.
  - Former connections to **INC Ransom**.
- **Revenue‑Threshold Targeting:**  
  - Critical infrastructure: ≥ $100M annual revenue.  
  - Healthcare: ≥ $50M annual revenue.

---

## Evolution Timeline
| Version | Period        | Key Characteristics                                                                 |
|---------|---------------|--------------------------------------------------------------------------------------|
| 1.0     | Apr – Jun 2025 | C++ based, DragonForce builder, TOR leak site (v1), ransom $60K–$2.5M.              |
| 2.0     | Jul 2025 –    | Rust implementation, new TOR infrastructure, GPO deployment, ransom $1M–$91M.       |

- **June 2025:** GangExposed doxing causes temporary affiliate abandonment.
- **July 2025:** Rapid migration to Rust, sustained attack tempo.

---

## Technical Lineage
- **Conti** source code leak (Feb 2022) → **DragonForce** (2023‑2024) → **DevMan** (Apr 2025).
- Shared characteristics: identical ransom note templates, Windows Restart Manager exploitation, three‑mode encryption, DragonForce builder usage.

---

## Key Technical Details

| Feature               | Details                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Encryption**        | Hybrid AES‑256 (CBC) + RSA‑2048. Three modes: full, header‑only, custom. Inherited from DragonForce/Conti.                                 |
| **File Extensions**   | Version 1.0: `.DEVMAN`, `.devmanv1`, `.yAGRTb`<br>Version 2.0: `.devman1`<br>Builder flaw: `e47qfsnz2trbkhnt.devman`                       |
| **Ransom Notes**      | `README.devmanv1.txt` (v1), `README.txt`, `README.yAGRTb.txt`                                                                               |
| **Exfiltration**      | Data‑extortion‑first. Typical 50‑300GB, max 2.5TB. Uploaded to **Mega.nz**. Dedicated TOR leak sites with countdown timers.                |
| **Communication**     | Offline architecture (no C2 beaconing). Post‑compromise: **TOX** protocol, **TOR hidden services**, email `devman@cyberfear.com`.          |
| **Deployment Speed**  | Windows Restart Manager API abuse (file lock bypass), PowerShell/CMD scripts, GPO push (v2.0).                                             |
| **Payment**           | Bitcoin, routed via affiliate wallets (Qilin structure: 80‑85% affiliate cut).                                                              |

### TOR Leak Sites
- Version 1.0: `qljmlmp4psnn3wqskkf3alqquatymo6hntficb4rhq5n76kuogcv7zyd.onion`
- Version 2.0: `wugurgyscp5rxpihef5vl6b6m5ont3b6sezhl7boboso2enib2k3q6qd.onion`

---

## Activities & Targeting
- **Victim Count:** 40‑50 confirmed (Q2 2025), 70‑86 total (Q3 2025). Peak activity in May 2025.
- **Geographic Focus:**  
  - **Asia‑Pacific** (>60%): Taiwan, Thailand, China, Japan, Singapore.  
  - **Secondary:** South Africa, Egypt, Kenya.  
  - **Expanding:** Europe, North America (government & energy sectors, Sep 2025).
- **Top Targeted Industries:**  
  Manufacturing, business/professional services, IT & telecom, retail, construction, healthcare, government, critical infrastructure.

---

## Modus Operandi (MITRE ATT&CK Mapping)

| Tactic                | Technique ID      | Name                                             | DevMan Implementation                                                                                     |
|-----------------------|-------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Initial Access**    | T1566             | Phishing                                         | Malicious attachments                                                                                     |
|                       | T1078             | Valid Accounts                                   | RDP brute‑force, password spraying, credential stuffing                                                  |
|                       | T1190             | Exploit Public‑Facing Application                | VPN gateways, remote management interfaces, Microsoft Exchange (no specific CVE)                         |
| **Execution**         | T1059.001         | Command and Scripting Interpreter: PowerShell    | PowerShell & cmd scripts for payload deployment                                                           |
|                       | T1569.002         | System Services: Service Execution                | PsExec                                                                                                    |
| **Persistence**       | T1547.001         | Boot or Logon Autostart Execution: Registry Run Keys | Registry modifications at `HKCU\...\Run`                                                               |
|                       | T1543.003         | Create or Modify System Process: Windows Service | Malicious service creation                                                                                |
|                       | T1053.005         | Scheduled Task/Job: Scheduled Task               | Scheduled tasks                                                                                           |
| **Privilege Escalation** | T1543.003, T1053.005 | (same as above)                               |                                                                                                           |
| **Defense Evasion**   | T1562.001         | Impair Defenses: Disable or Modify Tools         | Terminates AV, EDR, backup software                                                                       |
|                       | T1070             | Indicator Removal on Host                         | Rapid registry deletion (ms), log tampering                                                               |
|                       | T1027             | Obfuscated Files or Information                   | Rust implementation (v2.0) to evade signature detection                                                   |
|                       | T1484.001         | Domain Policy Modification: Group Policy Modification | GPO deployment (v2.0) for domain‑wide distribution                                                       |
| **Credential Access** | T1003             | OS Credential Dumping                             | Mimikatz (LSASS memory)                                                                                   |
|                       | T1555             | Credentials from Password Stores                   | Custom info‑stealer for Chrome, Firefox, Edge                                                             |
| **Discovery**         | T1482             | Domain Trust Discovery                             | BloodHound                                                                                                |
|                       | T1018             | Remote System Discovery                            | SoftPerfect Network Scanner                                                                                |
|                       | T1135             | Network Share Discovery                            | SMB scanning for administrative shares                                                                    |
| **Lateral Movement**  | T1021.002         | Remote Services: SMB/Windows Admin Shares          | PsExec propagation                                                                                         |
|                       | T1021.001         | Remote Services: Remote Desktop Protocol           | RDP with stolen credentials                                                                                |
|                       | T1484.001         | (as above) – GPO also used for lateral movement   |                                                                                                           |
| **Collection**        | T1114             | Email Collection                                  | (likely, but not detailed)                                                                                |
| **Command and Control** | T1071           | Application Layer Protocol                         | Minimal C2; when needed: TOX, TOR                                                                         |
| **Exfiltration**      | T1041             | Exfiltration Over C2 Channel                       | Pre‑encryption exfiltration to attacker infrastructure                                                   |
|                       | T1567             | Exfiltration Over Web Service                      | Mega.nz uploads (50‑300GB typical, 2.5TB max)                                                             |
| **Impact**            | T1486             | Data Encrypted for Impact                           | File encryption with three modes; Windows Restart Manager API abuse                                       |
|                       | T1491.001         | Defacement: Internal Defacement                    | Desktop wallpaper change (Windows 10 only)                                                                |
|                       | T1529             | System Shutdown/Reboot                              | Forced reboot                                                                                              |
|                       | T1490             | Inhibit System Recovery                             | Volume Shadow Copy deletion                                                                                |

---

## Indicators of Compromise (IOCs)

### File Hashes (SHA256 / MD5)
- **Version 1.0 primary SHA256:** `df5ab9015833023a03f92a797e20196672c1d6525501a9f9a94a45b0904c7403`
- **Version 1.0 secondary SHA256:** `018494565257ef2b6a4e68f1c3e7573b87fc53bd5828c9c5127f31d37ea964f8`
- **Version 1.0 primary MD5:** `e84270afa3030b48dc9e0c53a35c65aa`

### Domains / URLs (TOR hidden services)
- Version 1.0 leak site: `qljmlmp4psnn3wqskkf3alqquatymo6hntficb4rhq5n76kuogcv7zyd.onion`
- Version 2.0 leak site: `wugurgyscp5rxpihef5vl6b6m5ont3b6sezhl7boboso2enib2k3q6qd.onion`
- Victim contact email: `devman@cyberfear.com`

### TOX ID
`9D97F166730F865F793E2EA07B173C742A6302879DE1B0BBB03817A5A04B572FBD82F984981D`

### File Paths / Registry Keys
- Temporary Windows Restart Manager sessions:  
  `HKEY_CURRENT_USER\Software\Microsoft\RestartManager\Session0000`
- Persistence via Run key:  
  `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`

### File Extensions (encrypted files / ransom notes)
- `.DEVMAN`, `.devmanv1`, `.yAGRTb` (v1)
- `.devman1` (v2)
- Builder‑flaw deterministic name: `e47qfsnz2trbkhnt.devman`
- Ransom notes: `README.devmanv1.txt`, `README.txt`, `README.yAGRTb.txt`

### Process / Behavioral Indicators
- Hardcoded mutex: `hsfjuukjzloqu28oajh727190` (high confidence)
- Abnormal SMB traffic targeting administrative shares (ADMIN$, C$)
- Large‑volume exfiltration to `mega.nz`
- Rapid registry key deletions (milliseconds)
- Use of Windows Restart Manager API to bypass file locks

---

## Exploits and Vulnerabilities
| Exploit / Attack Vector                          | CVE   | CVSS | Description                                                                                |
|--------------------------------------------------|-------|------|--------------------------------------------------------------------------------------------|
| Phishing, RDP brute‑force, credential stuffing   | N/A   | N/A  | Initial access via user interaction or weak credentials.                                   |
| Unpatched edge‑facing services (VPN, Exchange)   | N/A   | N/A  | Exploitation of known vulnerabilities without specific CVE targeting; relies on unpatched systems. |
| Windows Restart Manager API abuse                 | N/A   | N/A  | Legitimate API used maliciously to unlock files during encryption.                         |

*No CVEs are currently associated with DevMan in public databases (NVD, CISA KEV).*

---

## Recommendations for Detection & Mitigation
1. **Monitor for behavioral IOCs:**
   - Windows Restart Manager API abuse (rapid creation/deletion of registry sessions).
   - Fast registry key deletions.
   - Large SMB scans for admin shares.
   - Connections to Mega.nz or TOR exit nodes.
2. **Harden credentials:**
   - Enforce MFA for all external‑facing services (RDP, VPN).
   - Use strong, unique passwords and monitor for brute‑force attempts.
3. **Limit administrative tools:**
   - Restrict use of PsExec, PowerShell remoting, and scheduled tasks to authorised administrators.
   - Enable logging and alerting on their usage.
4. **Protect backups:**
   - Store backups offline or in immutable storage to prevent deletion.
5. **Patch external services:**
   - Keep VPN gateways, Exchange servers, and remote management interfaces up‑to‑date.
6. **Deploy EDR solutions:**
   - Focus on behavioural detection (e.g., abnormal process creation, registry changes, SMB traffic).

---

## References
- [Halcyon Threat Group Profile – DevMan](https://www.halcyon.ai/threat-group/devman) (October 2025)
- Internal analysis of observed IOCs and TTPs.

**Last updated:** 2026-03-08