![AFRINTEL](https://img.shields.io/badge/AFRINTEL-CTI-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Period](https://img.shields.io/badge/Period-2025-blue)

# AFRINTEL annual statistics - 2025

👉🏾 [French version](./README_FR.md)

## 1. Scope and source

This statistical view is derived from the twelve monthly `victims.md` files and contains **197 records**. A record is a documented publication or claim; it is not necessarily a confirmed intrusion or a unique victim. The source files remain authoritative. Reposts and distinct claims are retained when documented as separate monthly records.

All totals below reconcile to the same 197-record source. Country names use the standard English names and ISO alpha-2 codes in visualisations. Sectors use the controlled annual vocabulary from the CTI report. The two `Not specified` sector records remain unresolved in the source and are not reassigned without evidence.

## 2. Monthly evolution

| Month | Records |
|---|---:|
| January | 16 |
| February | 8 |
| March | 11 |
| April | 17 |
| May | 21 |
| June | 21 |
| July | 21 |
| August | 13 |
| September | 18 |
| October | 19 |
| November | 14 |
| December | 18 |
| **Total** | **197** |

## 3. Distribution by country

| Rank | Country | ISO | Records |
|---:|---|:---:|---:|
| 1 | Egypt | EG | 33 |
| 2 | Morocco | MA | 31 |
| 3 | South Africa | ZA | 30 |
| 4 | Algeria | DZ | 19 |
| 5 | Nigeria | NG | 14 |
| 6 | Tunisia | TN | 13 |
| 7 | Kenya | KE | 10 |
| 8 | Mauritania | MR | 8 |
| 9 | Zambia | ZM | 4 |
| 10 | Ghana | GH | 3 |
| 11 | Ivory Coast | CI | 3 |
| 12 | Namibia | NA | 3 |
| 13 | Tanzania | TZ | 3 |
| 14 | Botswana | BW | 2 |
| 15 | Congo (DRC) | CD | 2 |
| 16 | Mauritius | MU | 2 |
| 17 | Senegal | SN | 2 |
| 18 | Togo | TG | 2 |
| 19 | Uganda | UG | 2 |
| 20 | Zimbabwe | ZW | 2 |
| 21 | Angola | AO | 1 |
| 22 | Burkina Faso | BF | 1 |
| 23 | Cameroon | CM | 1 |
| 24 | Djibouti | DJ | 1 |
| 25 | Eritrea | ER | 1 |
| 26 | Gabon | GA | 1 |
| 27 | Madagascar | MG | 1 |
| 28 | Rwanda | RW | 1 |
| 29 | Burundi | BI | 1 |
| **Total** |  |  | **197** |

## 4. Sector distribution

| Normalized sector | Records | Share |
|---|---:|---:|
| Government / Administration | 40 | 20.3% |
| Finance / Banking | 39 | 19.8% |
| Technology / IT | 25 | 12.7% |
| Education / University | 17 | 8.6% |
| Healthcare / Medical | 14 | 7.1% |
| Manufacturing / Industry | 10 | 5.1% |
| Transport / Logistics | 10 | 5.1% |
| Retail / E-commerce | 9 | 4.6% |
| Professional / Business Services | 7 | 3.6% |
| Construction / Real Estate | 6 | 3.0% |
| Defense / Security | 6 | 3.0% |
| Energy / Utilities | 4 | 2.0% |
| Agriculture / Agribusiness | 3 | 1.5% |
| Legal / Justice | 2 | 1.0% |
| Mining | 2 | 1.0% |
| Not specified | 2 | 1.0% |
| Civil Society / NGO | 1 | 0.5% |
| **Total** | **197** | **100.0%** |

## 5. Incident classification

| Type | Records | Share |
|---|---:|---:|
| Ransomware | 122 | 61.9% |
| Data Leak | 72 | 36.5% |
| Access Sale | 3 | 1.5% |
| Defacement | 0 | 0.0% |
| **Total** | **197** | **100.0%** |

### Aggregate exposure view

| Aggregate category | Records | Share of corpus |
|---|---:|---:|
| Data leaks + access sales | **75** | **38.1%** |

This is a derived analytical view (`72 + 3`), not an additional incident category. Access sales remain separately counted because they do not automatically establish data exfiltration.

## 6. Most visible actors / publication sources

| Actor / source | Records |
|---|---:|
| qilin | 11 |
| nightspire | 10 |
| devman | 10 |
| incransom | 8 |
| funksec | 7 |
| Phantom Atlas | 7 |
| killsec | 6 |
| kill9 | 6 |
| Dark 07x Team | 5 |
| ransomhub | 4 |

This is a top-10 view. Actor aliases, source accounts and publication annotations are normalized for the ranking; the complete incident-level attribution remains in the monthly victim cards and STIX bundles.

## 7. Interpretation and SOC priorities

The distribution measures AFRINTEL visibility, not the prevalence of real-world compromises. Ransomware claims dominate the corpus, while data leaks and access sales form a separate exposure signal. SOC teams should validate claims against IAM, VPN, EDR, backup, DNS, proxy, WAF and application telemetry, and should distinguish a new compromise from a repost or an unverified listing.

## Conclusion

The 2025 statistical baseline is internally reconciled at **197 records**: **122 ransomware**, **72 data leaks**, **3 access sales** and **0 defacements**. Country, sector and actor views must be regenerated from the monthly victim source whenever the source cards change.

**AFRINTEL** - TLP:CLEAR
