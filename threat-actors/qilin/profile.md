# Qilin / Agenda - Threat Actor & Ransomware Profile

👉🏾 [**Version française disponible ici**](./profile_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Actor / Group:** Qilin (formerly Agenda)
- **Threat Type:** Ransomware / Double Extortion
- **Operating Model:** Ransomware-as-a-Service (RaaS)
- **Primary Motivation:** Financial
- **Known Platforms:** Windows, Linux, VMware ESXi and virtualized environments
- **Activity:** Active since 2022
- **Assessment Status:** Active monitoring
- **Last Updated:** 27 August 2026

---

## 1. Intelligence Summary

Qilin is a mature ransomware-as-a-service operation active since 2022. It combines data theft, extortion and encryption, with affiliates responsible for much of the intrusion activity.

Qilin grew sharply during 2025 and 2026. Black Kite's 2026 ransomware report recorded **1,358 Qilin victim disclosures** during its reporting period, up from 250 in the previous period. These figures reflect observed ransomware disclosures and should not be presented as 1,358 independently confirmed compromises.

Cisco Talos documented several Qilin incidents in 2025 and showed that affiliates do not always follow one fixed playbook. Initial access, tooling, credential theft, exfiltration and ransomware deployment can differ between incidents.

> **AFRINTEL rule:** actor-level Qilin TTPs are not automatically applied to every victim claimed by Qilin. Victim-specific TTPs require victim-specific technical evidence.

---

## 2. AFRINTEL Observation in Africa

### 8 May 2026 - Egypt - Imex International

AFRINTEL recorded a Qilin ransomware claim against **Imex International**, an Egyptian logistics and freight-forwarding company.

- **Country:** Egypt
- **Sector:** Logistics & Transport
- **Website:** imex-logistics.com
- **Status:** Ransomware Claimed
- **Evidence scope:** Victim association / claim

AFRINTEL does not currently have victim-specific telemetry proving that the broader Qilin TTPs documented below were used against Imex International.

**Evidence:** Observed claim  
**Scope:** Victim-specific association  
**Confidence:** High for the claim; insufficient evidence for victim-specific TTP attribution  
**Provenance:** AFRINTEL

---

## 3. Initial Access

### Valid accounts and external remote services

Cisco Talos reported that, in some 2025 incidents, attackers likely abused administrative credentials that had previously appeared on the dark web and then used those credentials against VPN infrastructure.

Talos assessed this link with **moderate confidence** and explicitly noted that credential exposure and the later intrusion were temporally correlated, but not proven to be causally linked.

Relevant ATT&CK techniques:

- **T1078 - Valid Accounts**
- **T1133 - External Remote Services**
- **T1110 / T1110.003 - Brute Force / Password Spraying**

A lack of MFA on the affected VPN materially increased the risk in the documented case.

### CVE-2026-50751 - Check Point VPN

Check Point documented active exploitation of **CVE-2026-50751**, an authentication-bypass vulnerability affecting Remote Access VPN and Mobile Access deployments using deprecated IKEv1 configurations.

Check Point assessed with **medium confidence** that the actor behind the observed exploitation was financially motivated and used Qilin ransomware. At least one post-compromise case was associated with a Qilin affiliate.

- **ATT&CK:** T1190 - Exploit Public-Facing Application
- **Evidence:** Reported
- **Scope:** Campaign-level
- **Confidence:** Medium
- **Provenance:** Check Point Research

### CVE-2026-0257 - Palo Alto Networks GlobalProtect

Arctic Wolf investigated multiple June 2026 intrusions that began with exploitation of **CVE-2026-0257** against Palo Alto Networks firewall appliances and ended with Qilin ransomware deployment.

- **ATT&CK:** T1190 - Exploit Public-Facing Application
- **Evidence:** Observed / Reported
- **Scope:** Incident / campaign-level
- **Confidence:** High
- **Provenance:** Arctic Wolf Labs

### Important exclusion

**CVE-2025-61882 (Oracle E-Business Suite) is not included in this Qilin profile.**

Public technical reporting ties that Oracle EBS exploitation campaign to **CL0P data-theft extortion**, not Qilin. AFRINTEL therefore does not use CVE-2025-61882 as a Qilin initial-access technique.

---

## 4. Discovery

Talos observed Qilin affiliates using common Windows and Active Directory utilities for internal reconnaissance.

Examples:

```text
nltest /dclist:<Domain>
net user <Username> /domain
whoami.exe /priv
tasklist /FI "IMAGENAME eq explorer.exe" /FO CSV /NH
```

PowerShell was also used to enumerate Active Directory systems:

```powershell
Import-Module ActiveDirectory
Get-ADComputer -Filter * | Select-Object -ExpandProperty DNSHostName
```

Relevant ATT&CK:

- **T1482 - Domain Trust Discovery**
- **T1018 - Remote System Discovery**
- **T1087.002 - Domain Account Discovery**
- **T1033 - System Owner/User Discovery**
- **T1057 - Process Discovery**
- **T1046 - Network Service Discovery**
- **T1082 - System Information Discovery**
- **T1059.001 - PowerShell**

**Evidence:** Observed  
**Scope:** Incident-level / actor-level tradecraft  
**Confidence:** High  
**Provenance:** Cisco Talos

---

## 5. Credential Access

Talos identified a password-protected folder containing credential-theft tooling. Available artifacts included or suggested:

- Mimikatz;
- NirSoft password-recovery tools;
- SharpDecryptPwd;
- custom scripts.

A batch script changed the WDigest configuration:

```text
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /f /d 1
```

SharpDecryptPwd was used to recover stored credentials from applications including WinSCP, Navicat, TeamViewer, FileZilla, Chrome and RDCMan.

Relevant ATT&CK:

- **T1003 - OS Credential Dumping**
- **T1555 - Credentials from Password Stores**

**Evidence:** Observed  
**Scope:** Incident-level  
**Confidence:** High  
**Provenance:** Cisco Talos

> AFRINTEL does not state that Qilin systematically purchases RedLine or Lumma stealer logs. The selected technical sources support leaked dark-web credentials, but do not establish those specific stealer families as a general Qilin access method.

---

## 6. Lateral Movement and Remote Access

Observed activity included:

- RDP;
- PsExec;
- SMB / Windows administrative shares;
- modified firewall and RDP settings;
- attacker-created local administrator access;
- remote monitoring and management tools.

Example RDP enablement:

```text
reg add HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

Talos observed remote-access tools including AnyDesk, Chrome Remote Desktop, Distant Desktop, GoToDesk, QuickAssist and ScreenConnect.

Qilin encryptors were also distributed with PsExec:

```text
cmd /C [PsExec] -accepteula \\IP -c -f -h -d -i <encryptor>.exe --password [PASSWORD] --spread --spread-process
```

Relevant ATT&CK:

- **T1021.001 - Remote Desktop Protocol**
- **T1021.002 - SMB/Windows Admin Shares**
- **T1219 - Remote Access Software**
- **T1569.002 - Service Execution**

---

## 7. Defense Evasion

Talos documented obfuscated PowerShell and several attempts to weaken endpoint defenses.

Observed behavior included:

- disabling AMSI;
- disabling TLS certificate validation;
- changing Restricted Admin settings;
- stopping or uninstalling EDR components;
- using tools such as `dark-kill` and HRSword;
- clearing Windows event logs.

Example driver/service activity:

```text
sc create dark type= kernel binPath=dark.sys
sc start dark
sc delete dark
```

Relevant ATT&CK:

- **T1562.001 - Impair Defenses**
- **T1070.001 - Clear Windows Event Logs**
- **T1112 - Modify Registry**
- **T1059.001 - PowerShell**

---

## 8. Collection and Exfiltration

Talos observed several exfiltration workflows.

### Credential-data exfiltration

A VBS script formatted collected credential information into `result.txt` and sent it to an attacker-controlled SMTP server.

### Archive and cloud transfer

WinRAR was used to package selected data. Talos also documented **Cyberduck** with **Backblaze** as a cloud destination in Qilin-related cases.

Relevant ATT&CK:

- **T1560.001 - Archive via Utility**
- **T1048 - Exfiltration Over Alternative Protocol**
- **T1537 - Transfer Data to Cloud Account**

**Evidence:** Observed  
**Scope:** Incident-level  
**Confidence:** High  
**Provenance:** Cisco Talos

> **Cloudflare Tunnel is not used as a default Qilin exfiltration statement in this profile.** The main technical sources used here document Cyberduck/Backblaze, SMTP-based transfer and other channels instead.

---

## 9. Virtualization and ESXi Targeting

Talos documented PowerShell-based operations against VMware environments. The scripts were used to:

- connect to vCenter;
- enumerate datacenters and clusters;
- disable HA and DRS;
- enumerate ESXi hosts;
- change ESXi root passwords;
- enable SSH;
- upload a payload to `/tmp`;
- change execution permissions;
- execute the payload across selected hosts.

**Evidence:** Observed  
**Scope:** Incident-level / actor-level tradecraft  
**Confidence:** High  
**Provenance:** Cisco Talos

---

## 10. Impact and Recovery Inhibition

Talos observed Qilin changing the Volume Shadow Copy Service configuration and deleting shadow copies before encryption.

```text
cmd /C net start vss
cmd /C wmic service where name='vss' call ChangeStartMode Manual
cmd /C vssadmin.exe Delete Shadows /all /quiet
cmd /C net stop vss
cmd /C wmic service where name='vss' call ChangeStartMode Disabled
```

Relevant ATT&CK:

- **T1490 - Inhibit System Recovery**
- **T1489 - Service Stop**
- **T1486 - Data Encrypted for Impact**

The Qilin configuration also contains process and service stop lists covering database, backup, security and remote-management software, including Veeam-related services.

> AFRINTEL does not use `net stop "VeeamEndpointBackupSvc"` as a documented Qilin command unless an incident source specifically shows that exact command.

---

## 11. Detection and Hunting Opportunities

| Signal | Why it matters |
|---|---|
| VPN access from unusual infrastructure | Possible initial access |
| Successful VPN login after many NTLM attempts | Credential-driven intrusion |
| `UseLogonCredential=1` | WDigest weakening / credential exposure |
| New RDP enablement through registry | Remote access preparation |
| PsExec distributing password-protected executors | Ransomware deployment |
| `dark.sys`, HRSword or EDR uninstall attempts | Defense evasion |
| Bulk event-log clearing | Anti-forensics |
| VSS mode changes + shadow-copy deletion | Recovery inhibition |
| PowerShell enumeration of vCenter / ESXi | Virtualization targeting |
| Cyberduck history to unusual cloud storage | Possible exfiltration |

These are hunting signals, not attribution proof by themselves.

---

## 12. AFRINTEL Assessment

Qilin is a high-volume RaaS with a broad affiliate ecosystem. Available investigations show meaningful variation between affiliates and incidents.

AFRINTEL therefore separates:

- **Qilin actor-level reporting**;
- **campaign-level vulnerability exploitation**;
- **incident-level TTPs documented by incident responders**;
- **victim-specific AFRINTEL evidence**.

A Qilin leak-site claim alone does not prove which CVE, credential source, exfiltration tool or encryptor workflow was used against that victim.

---

## 13. Sources

- Cisco Talos - *Uncovering Qilin attack methods exposed through multiple cases*  
  https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/
- Check Point Research - *Active Exploitation of CVE-2026-50751*  
  https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/
- Arctic Wolf Labs - *Exploitation of CVE-2026-0257 Leads to Qilin Ransomware*
- Black Kite - *2026 Ransomware Report*  
  https://blackkite.com/reports/2026-ransomware-report
- AFRINTEL - African ransomware victim intelligence, May 2026

---

**AFRINTEL - African Cyber Threat Intelligence**
