# Akira - Threat Actor Profile

👉🏾 [**French version available here**](./akira_profile_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Actor / Group:** Akira
- **Threat Type:** Ransomware / Extortion
- **Operating Model:** Ransomware-as-a-Service (RaaS)
- **Primary Motivation:** Financial
- **Period Covered:** 2024-2026
- **Targeted Environments:** Windows, VMware ESXi, Hyper-V, Nutanix AHV
- **Assessment Status:** Active monitoring
- **Last Updated:** 25 August 2026

---

## 1. Intelligence Summary

Akira is a ransomware operation active since 2023 and associated with attacks against Windows environments and virtualization infrastructure.

Historical versions of the ransomware were primarily developed in C++, while more recent variants, including **Megazord** and **Akira_v2**, use Rust.

Akira-attributed campaigns commonly combine initial access through exposed services, compromised VPN accounts or vulnerable systems, internal reconnaissance, credential theft, data exfiltration and encryption.

> **AFRINTEL qualification:**  
> The TTPs below represent behaviors documented at the Akira ecosystem level by the FBI, CISA and partner organizations. They must not automatically be attributed to every Akira victim tracked by AFRINTEL without incident-specific technical evidence.

---

## 2. Key Documented TTPs

### 2.1 Initial Access

- **T1190 - Exploit Public-Facing Application**
  - Exploitation of vulnerabilities affecting Internet-facing systems.
  - Documented exploitation of **CVE-2023-20269** affecting Cisco ASA / FTD.
  - Documented exploitation of **CVE-2024-40766** affecting SonicWall.

- **T1078 - Valid Accounts**
  - Use of compromised VPN accounts.

- **T1110 / T1110.003 - Brute Force / Password Spraying**
  - Brute-force and password-spraying attempts against VPN accounts.

- **T1566.001 / T1566.002 - Spearphishing**
  - Use of malicious attachments or links.

- **T1068 - Exploitation for Privilege Escalation**
  - Exploitation of vulnerable Veeam servers, including **CVE-2023-27532** and **CVE-2024-40711**.

**Evidence Type:** Reported / Observed by partner authorities  
**Confidence:** High

---

### 2.2 Internal Reconnaissance and Discovery

- **T1046 - Network Service Discovery**
  - Use of **Advanced IP Scanner**, **NetScan** and **SoftPerfect Network Scanner** to identify hosts, ports, network devices and accessible shares.

- **T1018 - Remote System Discovery**
  - Use of Windows commands and `nltest` to identify systems and domain controllers.

- **T1482 - Domain Trust Discovery**
  - Reconnaissance of Active Directory trust relationships.

- **T1069.001 / T1069.002 - Permission Groups Discovery**
  - Use of `net` commands to identify local administrators and Domain Admin groups.

**Observed Tools:**
- Advanced IP Scanner
- NetScan
- SoftPerfect Network Scanner
- `net.exe`
- `nltest`

**Confidence:** High

---

### 2.3 Credential Access

- **T1003 - OS Credential Dumping**
  - Use of **Mimikatz** and **LaZagne** to extract authentication material.

- **T1003.001 - LSASS Memory**
  - Attempts to retrieve secrets from LSASS process memory.
  - Documented use of `rundll32.exe` with `comsvcs.dll` to create an LSASS memory dump.

- **T1555.003 / T1555.004**
  - Credential extraction from web browsers and Windows Credential Manager through tools such as NetExec or Mimikatz.

**Evidence Type:** Observed / Reported  
**Confidence:** High

---

### 2.4 Collection and Exfiltration

- **T1560.001 - Archive via Utility**
  - Use of **WinRAR** to compress data before exfiltration.

- **T1567.002 - Exfiltration to Cloud Storage**
  - Use of **RClone** to synchronize and exfiltrate data to cloud-storage services such as **MEGA**.

- **T1048 - Exfiltration Over Alternative Protocol**
  - Use of **WinSCP** and **FileZilla** to transfer data.

- **T1537 - Transfer Data to Cloud Account**
  - Use of cloud services or cloud accounts to transfer compromised data.

**Observed Tools:**
- RClone
- WinSCP
- FileZilla
- WinRAR
- MEGA

**Confidence:** High

---

### 2.5 Command and Control / Remote Access

Akira has also been associated with legitimate remote-access and tunneling tools that may be abused to maintain access or establish communication channels:

- AnyDesk
- RustDesk
- MobaXterm
- Cloudflare Tunnel
- Ngrok
- LogMeIn

These tools are not malicious by themselves. Attribution to Akira activity requires additional technical context.

---

### 2.6 Impact and Recovery Inhibition

- **T1486 - Data Encrypted for Impact**
  - Encryption of Windows systems and virtualization environments.

- **T1490 - Inhibit System Recovery**
  - Deletion of Volume Shadow Copies to reduce recovery options.

Recent ransomware versions may target:

- Windows;
- VMware ESXi;
- Hyper-V;
- Nutanix AHV.

Documented variants include:

- **Akira**
- **Akira_v2**
- **Megazord**

Historical Akira variants primarily use C++, while Megazord and Akira_v2 introduce components written in Rust.

**Confidence:** High

---

## 3. Documented Technical Artifacts

| Artifact | Type | Usage | ATT&CK |
|---|---|---|---|
| `Advanced IP Scanner` | Tool | Network reconnaissance | T1046 |
| `NetScan` | Tool | Network / port scanning | T1046 |
| `Mimikatz` | Tool | Credential dumping | T1003 |
| `rundll32.exe` + `comsvcs.dll` | LOLBin | LSASS dump | T1003.001 |
| `RClone` | Tool | Cloud exfiltration | T1567.002 |
| `WinSCP` | Tool | Data transfer | T1048 |
| `WinRAR` | Tool | Pre-exfiltration archiving | T1560.001 |
| `vssadmin.exe` | LOLBin | Shadow copy deletion | T1490 |
| `Akira_v2` | Ransomware | Encryption | T1486 |
| `Megazord` | Ransomware | Encryption | T1486 |

---

## 4. Example Command Lines / Behaviors

The following commands or behaviors are relevant for detection when they appear in a context consistent with ransomware activity:

```text
vssadmin.exe delete shadows /all /quiet
rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump <PID> <output.dmp> full
rclone.exe copy ...
```

> These artifacts should be correlated with execution context, parent process, user, host, network activity and incident timeline to reduce false positives.

---

## 5. Vulnerabilities Associated with Akira Operations

| CVE | Product | Documented Usage |
|---|---|---|
| CVE-2023-20269 | Cisco ASA / FTD | Initial access |
| CVE-2024-40766 | SonicWall | Initial access |
| CVE-2023-27532 | Veeam Backup & Replication | Exploitation of vulnerable server |
| CVE-2024-40711 | Veeam Backup & Replication | Exploitation of vulnerable server |

---

## 6. AFRINTEL Assessment

The TTPs presented in this profile correspond to behaviors documented at the Akira ecosystem level.

AFRINTEL systematically distinguishes between:

- **actor-level known TTPs**;
- **TTPs observed during an independent investigation**;
- **TTPs confirmed for a specific AFRINTEL victim**;
- **assessed or inferred TTPs**.

An Akira claim against an African organization is therefore not sufficient to conclude that the entire attack chain described above was used against that victim.

### Evidence Levels

- **Observed:** directly seen in telemetry, malware analysis, incident response evidence or primary-source material.
- **Reported:** documented by a trusted technical or institutional source.
- **Assessed:** analytical conclusion based on multiple available observations.
- **Inferred:** plausible relationship with insufficient technical evidence for strong attribution.

---

## 7. Incident-Level Intelligence Gaps

For each Akira victim tracked by AFRINTEL, the following elements should be investigated before assigning victim-specific TTPs:

- initial-access vector;
- compromised account or identity;
- CVE actually exploited;
- command-and-control infrastructure;
- ransomware or tool hashes;
- observed command lines;
- lateral-movement mechanism;
- exfiltration channel;
- backup-removal method;
- ransomware deployment method.

---

## 8. Sources

- FBI / CISA / DC3 / HHS and international partners - **#StopRansomware: Akira Ransomware (AA24-109A)**
- MITRE ATT&CK
- Additional AFRINTEL technical sources according to the incidents analyzed

---

**AFRINTEL - African Cyber Threat Intelligence**
