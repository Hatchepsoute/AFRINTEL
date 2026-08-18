# AFRINTEL comparison: June vs July 2026

👉🏾 [French version](README_FR.md)

## Executive comparison

| Indicator | June | July | Change |
|---|---:|---:|---:|
| Unique incident records | 40 | 42 | +2 (+5.0%) |
| Ransomware | 20 | 18 | -2 (-10.0%) |
| Access sales | 2 | 6 | +4 (+200.0%) |
| Leaks and access sales combined | 20 | 24 | +4 (+20.0%) |
| Geographic occurrences | 53 | 43 | -10 (-18.9%) |
| Countries in geographic view | 20 | 12 | -8 |

July brought two more unique records than June, but ransomware listings declined. Access-sale activity increased from two records to six. The geographic count is lower because June included two large multi-country access schemes, while July included one multi-country identity-data record and one MTN record whose national entity remains unconfirmed.

## Incident-type evolution

| Incident type | June | July | Change |
|---|---:|---:|---:|
| Ransomware | 20 | 18 | -2 |
| Data leaks | 18 | 18 | 0 |
| Access sales | 2 | 6 | +4 |
| Defacements | 0 | 0 | 0 |
| **Total** | **40** | **42** | **+2** |

The month-to-month shift is mainly an increase in the combined leak and access-sale category, alongside a decline in ransomware listings. July separately records 18 data leaks and 6 access sales.

## Country evolution

The table uses geographic occurrences. Multi-country allocations are counted in each country view but remain one incident in the global total.

| Country | June | July | Change |
|---|---:|---:|---:|
| 🇲🇦 Morocco | 10 | 6 | -4 |
| 🇿🇦 South Africa | 6 | 6 | 0 |
| 🇪🇬 Egypt | 6 | 7 | +1 |
| 🇳🇬 Nigeria | 5 | 4 | -1 |
| 🇹🇳 Tunisia | 4 | 7 | +3 |
| 🇱🇾 Libya | 3 | 0 | -3 |
| 🇹🇿 Tanzania | 3 | 0 | -3 |
| 🇰🇪 Kenya | 3 | 1 | -2 |
| 🇿🇲 Zambia | 2 | 0 | -2 |
| 🇨🇮 Côte d’Ivoire | 0 | 3 | +3 |
| 🇩🇿 Algeria | 1 | 4 | +3 |
| 🇬🇭 Ghana | 0 | 2 | +2 |
| 🇨🇲 Cameroon | 0 | 1 | +1 |
| 🇸🇸 South Sudan | 0 | 1 | +1 |
| Other June-only countries | 5 | 0 | -5 |

Morocco remains a major focus but declined from ten to six geographic occurrences. Tunisia increased from four to seven, driven by data leaks and access sales. Côte d’Ivoire and Ghana appeared in the July geographic view, while several June-only countries were linked to the earlier multi-country access schemes.

## Sector evolution

Sector labels are normalised within each monthly dataset. The comparison is directional because July uses more granular labels for several single-occurrence sectors.

| Sector | June | July | Change |
|---|---:|---:|---:|
| Government / Administration | 12 | 11 | -1 |
| Telecommunications | 0 | 5 | +5 |
| Healthcare / Medical | 3 | 4 | +1 |
| Education / Universities | 4 | 3 | -1 |
| E-commerce / Retail | 4 | 3 | -1 |
| Technology / Engineering | 0 | 3 | +3 |
| Finance / Banking | 6 | 1 | -5 |
| Oil and Energy | 0 | 2 | +2 |
| Transport / Logistics | 2 | 1 | -1 |
| Security Services | 1 | 1 | 0 |
| Mining | 1 | 1 | 0 |
| Other identified sectors | 7 | 8 | +1 |

Government remained the leading sector in both months. July was more visible in telecommunications and technology, while June had a stronger concentration in finance.

## Actor evolution

| Actor or source | June | July |
|---|---:|---:|
| anisanas2 | 7 | 0 |
| DeadLock | 4 | 0 |
| LockBit 5 | 3 | 0 |
| arcusmedia | 0 | 4 |
| dragonforce | 0 | 3 |
| krybit | 2 | 2 |
| BIGBROTHER | 0 | 2 |
| TheGentlemen | 0 | 2 |
| Phantom Atlas | 0 | 2 |

The actor profile changed substantially. June was led by anisanas2 and DeadLock, while July was led by arcusmedia and dragonforce. Krybit was present in both months with two records each.

## CTI assessment

July should not be read as a simple continuation of June. The total increased slightly, but the threat mix moved away from ransomware and toward access brokerage. Tunisia became more prominent, while Morocco remained important but less concentrated than in June.

The two months also differ in geographic structure. June included multi-country access schemes touching many African states. July had a smaller geographic footprint, with a distinct identity-data record involving Nigeria and Côte d’Ivoire and a national-entity uncertainty around MTN.

## SOC priorities

1. Maintain ransomware readiness despite the small decline in listings.
2. Increase monitoring of administrative, Fortinet, VPN, webmail and telecom access offers.
3. Prioritise identity, healthcare, education and payment repositories for bulk-export detection.
4. Review national subsidiary inventories when a group-wide domain is mentioned.
5. Separate original compromises, reposts and access-sale claims during incident triage.
6. Track repeated victims across months without merging records unless evidence supports a common intrusion.

## Conclusion

June recorded 40 unique incidents and July 42. Ransomware declined from 20 to 18. The combined leak and access-sale category increased from 20 to 24, while explicitly classified access sales rose from two to six. The most important operational change is the stronger visibility of access brokerage in July.

*AFRINTEL, Open African CTI Monitoring Initiative*
