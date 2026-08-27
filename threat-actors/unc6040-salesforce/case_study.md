# UNC6040 - Salesforce OAuth Vishing & SaaS Data Theft

👉🏾 [**Version française**](./case_study_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Actor / Cluster:** UNC6040
- **Threat type:** SaaS data theft / extortion precursor
- **Primary vector:** Vishing / social engineering
- **Target environment:** Salesforce and connected SaaS services
- **Motivation:** Financial
- **Activity tracked:** 2025-2026
- **Technical evidence used here:** GTIG / Mandiant reporting published in 2025
- **Assessment status:** Active monitoring
- **Last updated:** 26 August 2026

---

## 1. Intelligence summary

UNC6040 is a financially motivated threat cluster tracked by Google Threat Intelligence Group. Its operators impersonate IT support staff during voice calls and convince users to perform actions that give the attacker access to Salesforce.

A common path is the authorization of a malicious Salesforce Connected App. Early activity often used a modified or spoofed Salesforce Data Loader application. GTIG later observed UNC6040 moving to custom applications, typically Python scripts, that performed similar collection functions.

The important point is that the attacker does not need to exploit a Salesforce vulnerability. The access is obtained by manipulating the user and abusing legitimate SaaS authorization and API mechanisms.

AFRINTEL treats the initial UNC6040 intrusion separately from later extortion activity. GTIG tracks the follow-on extortion cluster as **UNC6240**, which has claimed the **ShinyHunters** name in communications with victims.

---

## 2. Attack flow

```text
Vishing / fake IT support
        │
        ▼
User authorizes malicious Connected App
        │
        ▼
OAuth / application access to Salesforce
        │
        ▼
Data Loader or custom application
        │
        ▼
High-volume API collection
        │
        ▼
Salesforce data exfiltration
        │
        ├── possible pivot to Okta / Microsoft 365
        │
        ▼
Later extortion activity
        │
        └── tracked separately by GTIG as UNC6240
```

---

## 3. MITRE ATT&CK mapping

| Tactic | Technique | ID | Behavior | Evidence | Scope | Confidence | Provenance |
|---|---|---|---|---|---|---|---|
| Initial Access | Spearphishing Voice | T1566.004 | Operators impersonate IT support during vishing calls | Observed | Campaign-level | High | GTIG / Mandiant |
| Persistence | Cloud Application Integration | T1671 | Victims are deceived into authorizing a malicious Salesforce Connected App | Observed | Campaign-level | High | GTIG / Mandiant + MITRE ATT&CK |
| Defense Evasion / Credential Access context | Application Access Token | T1550.001 | OAuth/application tokens can be used to access SaaS resources after authorization | Reported / Assessed | Campaign-level | Medium | GTIG / Mandiant + ATT&CK normalization |

### T1528 note

**T1528 - Steal Application Access Token** should not be automatically assigned to the initial consent step. In the main UNC6040 flow, the victim is manipulated into authorizing the application. Use T1528 only when there is evidence that an application access token was actually stolen.

This distinction avoids turning OAuth abuse into token theft without evidence.

---

## 4. Collection and exfiltration

UNC6040 has been observed quickly extracting data from Salesforce after access is granted.

Reported collection methods include:

- Salesforce Data Loader;
- custom applications, including Python-based tooling;
- REST/API queries;
- Bulk API activity;
- report and list-view exports;
- large-scale file or attachment downloads.

GTIG also observed later pivots using credentials obtained through vishing or credential harvesting to access other cloud services such as **Okta** and **Microsoft 365**.

**Evidence:** Observed  
**Scope:** Campaign-level  
**Confidence:** High  
**Provenance:** GTIG / Mandiant

---

## 5. Infrastructure and access patterns

GTIG reported that UNC6040 primarily used **Mullvad VPN** IP addresses for access and exfiltration in Salesforce environments. Later activity also used **Tor** for parts of the social-engineering and automated collection workflow.

Phishing infrastructure associated with some investigations also hosted fake Okta pages used to collect credentials or MFA codes.

> VPN and Tor IP addresses are context indicators, not attribution proof by themselves.

---

## 6. Detection opportunities

Useful Salesforce signals include:

| Signal | Why it matters |
|---|---|
| `LoginType = Remote Access 2.0` | OAuth / connected-app authentication |
| New or unknown Connected App | Possible malicious integration |
| Broad scopes such as `api`, `refresh_token`, `offline_access` | Durable or wide API access |
| High-rate `Query`, `QueryMore` or `QueryAll` | Possible automated collection |
| Large `RowsProcessed` / `RecordCount` | Possible bulk extraction |
| `BulkApiResultEvent` downloads | Bulk API exfiltration signal |
| Large report/list-view exports | Possible CRM collection |
| Large file or attachment downloads | Possible data theft |
| OAuth followed quickly by API export | High-value correlation signal |
| Salesforce OAuth followed by Okta/M365 login from same risky IP | Cross-SaaS pivot signal |

Relevant telemetry includes:

- `LoginEvent` / `LoginEventStream`;
- `Setup Audit Trail`;
- `PermissionSetEvent`;
- `ApiEvent` / `ApiEventStream`;
- `BulkApiResultEvent`;
- `ReportEvent` / `ReportEventStream`;
- `ListViewEvent` / `ListViewEventStream`;
- `FileEvent` / `FileEventStore`;
- `ApiAnomalyEvent`;
- `ReportAnomalyEvent`.

These are hunting and detection opportunities. Their presence alone does not prove UNC6040 activity.

---

## 7. Attribution boundary

UNC6040 shares some social-engineering patterns with other financially motivated actors, including groups linked to the broader **The Com** ecosystem. Similar vishing or Okta-focused tradecraft is not enough to merge those actors.

AFRINTEL therefore keeps separate:

- UNC6040 - Salesforce-focused vishing and data theft;
- UNC6240 - later extortion activity tracked by GTIG;
- UNC3944 / Scattered Spider - a separate cluster with overlapping social-engineering tradecraft.

**Assessment:** the overlap is useful for hunting, but it is not direct attribution evidence.

---

## 8. Intelligence gaps

For a specific victim, confirm before making a victim-level attribution:

- the connected-app name and client ID;
- OAuth scopes granted;
- account that authorized the app;
- source IP / ASN and session timeline;
- API calls and data volumes;
- whether access tokens were actually stolen or simply issued after authorization;
- whether other SaaS platforms were accessed;
- whether the later extortion activity can be linked to the same operators.

---

## 9. Sources

- Google Threat Intelligence Group - *The Cost of a Call: From Voice Phishing to Data Extortion*, 4 June 2025
- Mandiant / Google Threat Intelligence - *UNC6040 Proactive Hardening Recommendations*, 30 September 2025
- MITRE ATT&CK - T1566.004 Spearphishing Voice
- MITRE ATT&CK - T1671 Cloud Application Integration / Salesforce Data Exfiltration
- MITRE ATT&CK - T1550.001 Application Access Token

---

**AFRINTEL - African Cyber Threat Intelligence**
