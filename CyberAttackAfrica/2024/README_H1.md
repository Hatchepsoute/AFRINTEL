# AFRINTEL Semiannual CTI Report - Cyber Threats in Africa - H1 2024

## 1. Executive summary

Across January-June 2024, AFRINTEL retains **46 canonical incidents across 16 countries**. Ransomware accounts for **34 records (73.9%)**, followed by Data Leak **5 (10.9%)**. The retrospective addition is the January 25 Daeyang University Data Leak in Malawi.

### 1.1 H1 vs H2 2024 comparison

H1 is the first half of the corrected 2024 baseline; H1/H2 comparison appears in the H2 and annual reports.

## 2. Methodology

The same taxonomy, date policy, and evidence rules used in monthly reports apply. Historical reposts and duplicates are excluded from canonical statistics but retained separately.

## 3. Monthly evolution

| Month | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware | Operational Fraud |
|---|---|---|---|---|---|---|---|---|---|---|
| January | 8 | 4 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 |
| February | 8 | 6 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| March | 9 | 8 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| April | 9 | 5 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| May | 9 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| June | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## 4. Incident types

| Type | Records | Share |
|---|---|---|
| Ransomware | 34 | 73.9% |
| Data Leak | 5 | 10.9% |
| Access Sale | 1 | 2.2% |
| DDoS | 2 | 4.3% |
| Defacement | 0 | 0.0% |
| Account Takeover | 0 | 0.0% |
| System Intrusion | 3 | 6.5% |
| Malware | 0 | 0.0% |
| Operational Fraud | 1 | 2.2% |

```mermaid
pie showData
    title Incident types - H1 2024
    "Ransomware" : 34
    "Data Leak" : 5
    "Access Sale" : 1
    "DDoS" : 2
    "System Intrusion" : 3
    "Operational Fraud" : 1
```

## 5. Geographic distribution

| Country | Records | Share |
|---|---|---|
| South Africa | 18 | 39.1% |
| Egypt | 7 | 15.2% |
| Cameroon | 2 | 4.3% |
| Tunisia | 2 | 4.3% |
| Ivory Coast | 2 | 4.3% |
| Namibia | 2 | 4.3% |
| Morocco | 2 | 4.3% |
| Libya | 2 | 4.3% |
| Angola | 1 | 2.2% |
| Malawi | 2 | 4.3% |
| Cabo Verde | 1 | 2.2% |
| Seychelles | 1 | 2.2% |
| Burkina Faso | 1 | 2.2% |
| Nigeria | 1 | 2.2% |
| Senegal | 1 | 2.2% |
| Congo | 1 | 2.2% |

## 6. Regions

| Region | Records | Share |
|---|---|---|
| Southern Africa | 23 | 50.0% |
| North Africa | 13 | 28.3% |
| West Africa | 6 | 13.0% |
| Central Africa | 3 | 6.5% |
| Indian Ocean | 1 | 2.2% |

## 7. Sectors

| Sector | Records | Share |
|---|---|---|
| Government / Administration | 8 | 17.4% |
| Finance / Banking | 8 | 17.4% |
| Professional / Business Services | 4 | 8.7% |
| Manufacturing / Industry | 4 | 8.7% |
| Healthcare / Medical | 4 | 8.7% |
| Energy / Utilities | 3 | 6.5% |
| Technology / IT | 3 | 6.5% |
| Media / Entertainment | 3 | 6.5% |
| Education / University | 3 | 6.5% |
| Retail / E-commerce | 2 | 4.3% |
| Water / Utilities | 1 | 2.2% |
| Construction / Real Estate | 1 | 2.2% |
| Agriculture / Agribusiness | 1 | 2.2% |
| Legal / Justice | 1 | 2.2% |

## 8. Actors / groups

| Actor / Group | Records |
|---|---|
| lockbit3 | 14 |
| Unknown | 10 |
| hunters | 4 |
| ransomhub | 4 |
| spacebears | 2 |
| arcusmedia | 2 |
| cnHunter | 1 |
| medusa | 1 |
| X0Frankenstein | 1 |

## 9. Evidence maturity

| Evidence | Records | Share |
|---|---|---|
| Claim - Unverified | 32 | 69.6% |
| Confirmed | 10 | 21.7% |
| Claim - Data Sample Published | 4 | 8.7% |

## 10. CTI analysis

- **Ransomware: 34**. Leak-site presence does not always prove encryption.
- **Data Leak: 5**. The count now includes Daeyang University (Malawi), where a visible SQL sample supports a Data Leak classification; the actor's claimed 224k+ SQL lines remain unverified.
- **System Intrusion: 3**. Used where intrusion/access is better supported than ransomware or data exposure.
- **Access Sale: 1**, **DDoS: 2**, **Defacement: 0**, **Operational Fraud: 1**.

## 11. Key findings

Evidence maturity and incident type remain separate analytical dimensions.

## 12. Intelligence gaps

Initial vectors, technical dates, exact volumes, exfiltration, and public DFIR conclusions remain incomplete for part of the corpus.

## 13. Recommendations

Phishing-resistant MFA, PAM, segmentation, immutable backups, centralized logging, and separate tracking of historical reposts.

## 14. Conclusion

H1 2024 retains **46 canonical incidents**.

**AFRINTEL** - TLP:CLEAR
