# UNC6040 — Case Study: Salesforce OAuth Vishing & SaaS Data Theft

👉🏾 [**Version française disponible ici**](./case_study_FR.md)

**AFRINTEL Threat Actor Intelligence**

- **Actor / Group:** UNC6040
- **Threat Type:** SaaS Data Theft / Extortion
- **Primary Vector:** Vishing / Social Engineering
- **Target Environment:** Salesforce / SaaS
- **Primary Motivation:** Financial
- **Documented Period:** 2025–2026
- **Primary Source:** Google Threat Intelligence Group / Mandiant
- **Confidence Level:** High
- **Last AFRINTEL Update:** 26 August 2026

---

## 1. Intelligence Summary

UNC6040 is a financially motivated threat cluster specializing in vishing campaigns targeting Salesforce environments.

Operators impersonate IT support personnel and persuade users to authorize a malicious Connected App in their Salesforce instance.

The observed application is often a modified or impersonated version of Salesforce Data Loader.

This technique enables the attacker to access Salesforce data directly through SaaS APIs without first compromising the traditional internal network perimeter.

> **AFRINTEL qualification:**  
> AFRINTEL distinguishes between SaaS access obtained through social engineering, OAuth authorization granted by the user, and direct technical compromise. An OAuth authorization obtained through manipulation does not by itself mean that the primary network perimeter was compromised.

---

## 2. Initial Access

### T1566.004 — Spearphishing Voice

The actor contacts the victim by phone while impersonating IT support personnel.

The victim is guided to the Salesforce Connected Apps configuration page and instructed to authorize an application controlled by the attacker.

**Evidence:** Observed  
**Confidence:** High

---

## 3. OAuth Authorization

### T1528 — Steal Application Access Token

Authorizing the application provides the actor with OAuth access that can be used to interact with Salesforce resources on behalf of the user.

In this scenario, the token is not necessarily obtained through a technical compromise of the user's workstation. Access is granted as a consequence of social engineering.

**Evidence:** Observed  
**Confidence:** High

---

## 4. SaaS Persistence

### T1671 — Cloud Application Integration

The authorized OAuth application can allow the actor to maintain access to SaaS data through the cloud integration.

Refresh tokens may allow new access tokens to be obtained without requiring a new interactive login from the user.

> `T1098.003` should not be used here by default because that technique concerns adding cloud roles or permissions, which is not the primary behavior documented in this campaign.

**Evidence:** Observed / Assessed  
**Confidence:** High

---

## 5. Token Use

### T1550.001 — Application Access Token

Once OAuth access has been obtained, the actor can use the application and associated tokens to perform Salesforce API calls without following the normal interactive user authentication flow.

**Evidence:** Observed  
**Confidence:** High

---

## 6. Collection and Exfiltration

UNC6040 has been observed using Salesforce Data Loader to rapidly extract large volumes of data.

Activities may include:

- API queries;
- Bulk API operations;
- report exports;
- retrieval of contacts and accounts;
- extraction of sensitive CRM data.

### Relevant Salesforce Telemetry Sources

- `ApiEventStream`
- `BulkApiResultEvent`
- `ReportEventStream`
- `ListViewEventStream`
- `FileEvent`
- `LoginEvent`

**Evidence:** Observed  
**Confidence:** High

---

## 7. SaaS Lateral Movement

After obtaining Salesforce access, UNC6040 has also been observed using credentials obtained through vishing or credential harvesting to access other cloud platforms, including:

- Okta;
- Microsoft 365.

This represents lateral movement across SaaS services rather than traditional Windows lateral movement.

**Evidence:** Reported / Observed depending on incident  
**Confidence:** High

---

## 8. Observed Infrastructure

UNC6040 has used IP addresses associated with VPN services to access Salesforce environments and perform data extraction activity.

Phishing infrastructure has also been used to host pages imitating identity services such as Okta.

> Network IoCs must be contextualized by date and incident. A commercial VPN IP address is not malicious by itself.

---

## 9. Detection Artifacts

| Signal | Context |
|---|---|
| `LoginType = Remote Access 2.0` | Salesforce OAuth authentication |
| Unknown Connected App | Unapproved or newly authorized application |
| New OAuth grant | Potentially malicious authorization |
| Scopes `api`, `refresh_token`, `offline_access` | Broad / durable access |
| Unusual Bulk API activity | Large-scale extraction |
| High volume of `Query` / `QueryMore` | API-based collection |
| Login from VPN / unusual infrastructure | Contextual risk signal |
| Large export shortly after OAuth authorization | OAuth → exfiltration chain |

---

## 10. Analytical Attack Chain

```text
Vishing
   │
   ▼
IT Support Impersonation
   │
   ▼
Connected App Authorization
   │
   ▼
OAuth Access / Refresh Token
   │
   ├── T1671
   ├── T1528
   └── T1550.001
   │
   ▼
Salesforce API / Data Loader
   │
   ▼
Bulk Data Collection
   │
   ▼
Data Exfiltration
   │
   ▼
Possible SaaS Pivot → Okta / Microsoft 365
   │
   ▼
Extortion
```

---

## 11. AFRINTEL Assessment

This campaign illustrates an important evolution in attack chains: compromise of the traditional network perimeter is no longer required to cause a major data breach.

A legitimate OAuth authorization obtained through social engineering can directly provide access to sensitive SaaS data.

For SOC teams, detection therefore needs to include identity, OAuth, Connected Apps and SaaS API telemetry in addition to endpoint and network logs.

AFRINTEL systematically distinguishes between:

- OAuth authorizations obtained through manipulation;
- tokens actually observed as compromised;
- anomalous API activity;
- confirmed data exfiltration;
- pivots to other SaaS services;
- relationships that are only assessed or inferred.

---

## 12. Sources

- Google Threat Intelligence Group / Mandiant — *The Cost of a Call: From Voice Phishing to Data Extortion*
- Mandiant — *Cybercrime Observations from the Frontlines: UNC6040 Proactive Hardening Recommendations*
- MITRE ATT&CK — T1566.004
- MITRE ATT&CK — T1528
- MITRE ATT&CK — T1550.001
- MITRE ATT&CK — T1671

---

**AFRINTEL — African Cyber Threat Intelligence**
