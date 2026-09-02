# AFRINTEL - Threat Actor Intelligence

👉🏾 [**Version française**](./README_FR.md)

This section contains threat actor profiles and DFIR case studies used by AFRINTEL to understand the tradecraft behind cyber incidents affecting African organizations.

The goal is simple: go beyond a leak-site name and document what is actually known about an actor, a campaign or a specific intrusion.

## Available analysis

| Entry | Type | Main focus | Languages |
|---|---|---|---|
| [Akira](./akira/akira_profile.md) | Threat actor / ransomware profile | TTPs, CVEs, tooling, exfiltration, ransomware evolution | EN / FR |
| [NightSpire](./nightspire/profile.md) | Threat actor / ransomware profile | African victimology, incident tradecraft, IOCs, evidence boundaries | EN / FR |
| [PYSA / Mespinoza](./pysa-mespinoza/dfir_case_study.md) | DFIR case study | Eight-hour intrusion, credential theft, RDP, Koadic, Empire, exfiltration | EN / FR |
| [Ryuk / Wizard Spider](./ryuk/ryuk_profile.md) | Malware / actor + DFIR reference | Entity separation, BazarLoader, Cobalt Strike, Zerologon, Ryuk deployment | EN / FR |
| [UNC6040 / Salesforce](./unc6040-salesforce/case_study.md) | SaaS campaign / threat cluster | Vishing, malicious Connected Apps, OAuth abuse, Salesforce API exfiltration | EN / FR |
<<<<<<< HEAD
=======
| [Qilin / Agenda](./qilin/profile.md) | Threat actor / ransomware profile | VPN access, credential theft, ESXi targeting, exfiltration, Qilin campaign evolution | EN / FR |
| [Gunra](./gunra/profile.md) | Threat actor / ransomware profile | Fortinet exploitation, NTDS dumping, SSH tunnels, cloud data theft, recovery inhibition | EN / FR |
>>>>>>> origin/update/threat-actors-v2-2026-08-26

## How AFRINTEL qualifies intelligence

AFRINTEL keeps four things separate:

### Evidence

- **Observed** - directly seen in telemetry, malware analysis, DFIR evidence or primary-source material.
- **Reported** - documented by a trusted technical, institutional or incident-response source.
- **Assessed** - analytical conclusion based on several available observations.
- **Inferred** - plausible relationship, but the evidence is not strong enough for a firm conclusion.

### Scope

- **Actor-level** - behavior associated with the broader actor or ransomware ecosystem.
- **Campaign-level** - behavior tied to a defined campaign or cluster of related activity.
- **Incident-level** - behavior confirmed in one documented intrusion.
- **Victim-specific** - evidence directly tied to one AFRINTEL victim.

### Confidence

AFRINTEL uses **High**, **Medium** and **Low** confidence. Confidence reflects the quality and consistency of the evidence, not the severity of the incident.

### Provenance

The source of each important claim should be clear: AFRINTEL, DFIR reporting, CERT/government advisory, security vendor, MITRE ATT&CK or another CTI source.

## Main analytical rule

A ransomware claim against a victim does **not** prove that every known TTP of that ransomware operation was used in the intrusion.

For example, if an Akira victim appears in AFRINTEL, actor-level reporting about Mimikatz, RClone or PowerTool is not automatically treated as victim-specific evidence. Those TTPs are only attached to the victim when incident evidence supports it.

The same rule applies to IOCs. Historical hashes, domains and IP addresses are kept with their date and context and should not be treated as active infrastructure without validation.

## Source priority

When sources disagree, AFRINTEL gives priority to:

1. incident telemetry and primary DFIR evidence;
2. CERT, government and law-enforcement advisories;
3. well-documented security-vendor research;
4. MITRE ATT&CK for taxonomy and entity context;
5. community CTI repositories as supporting research leads.

Community repositories are useful for finding leads, but important claims should be checked against the original source when possible.

---

**AFRINTEL - African Cyber Threat Intelligence**
