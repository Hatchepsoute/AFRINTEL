# AFRINTEL — Cyberattacks in Africa, July 2026

👉🏾 [Lire la version française](./README_FR.md) · [Full victim list](./victims.md)

## Executive summary

July didn't belong to one group. AFRINTEL logged 42 incident records across 12 countries this month: 18 ransomware claims, 18 data leaks, 6 access-sale offers.

Egypt and Tunisia lead with seven geographic occurrences apiece, then Morocco with six and South Africa also with six. One identity-photo claim touches both Nigeria and Côte d’Ivoire, so it counts once as an incident but twice on the map.

What stands out isn't just ransomware. Land records, national ID data, hospital files, university accounts, utility payments, alleged access to government systems, the spread is wide. AFRINTEL could check some of it against a sample or a screenshot. The rest is still just what an actor says.

## Methodology

The source for this report is [victims.md](./victims.md). Each entry is counted once, by AFRINTEL's detection date. Add up the country column and it comes to 43, not 42: the identity-photo case counts twice geographically, and MTN's national entity is still unclear.

Claimed volumes stay claims until something backs them up. A forum post alone doesn't count as proof. No defacement this month.

## Geographic distribution

| Country | Occurrences |
| :--- | ---: |
| 🇪🇬 Egypt | 7 |
| 🇹🇳 Tunisia | 7 |
| 🇲🇦 Morocco | 6 |
| 🇿🇦 South Africa | 6 |
| 🇳🇬 Nigeria | 4 |
| 🇩🇿 Algeria | 4 |
| 🇨🇮 Côte d’Ivoire | 3 |
| 🇬🇭 Ghana | 2 |
| 🇧🇼 Botswana | 1 |
| 🇨🇲 Cameroon | 1 |
| 🇰🇪 Kenya | 1 |
| 🇸🇸 South Sudan | 1 |
| **Total geographic occurrences** | **43** |

~~~pie showData
title Geographic occurrences — July 2026
"Egypt" : 7
"Tunisia" : 7
"Morocco" : 6
"South Africa" : 6
"Nigeria" : 4
"Algeria" : 4
"Côte d’Ivoire" : 3
"Ghana" : 2
"Botswana" : 1
"Cameroon" : 1
"Kenya" : 1
"South Sudan" : 1
~~~

## Incident types

| Type | Records | Share |
| :--- | ---: | ---: |
| 🟧 Ransomware | 18 | 42.9% |
| 🟦 Data leak | 18 | 42.9% |
| 🟪 Access sale | 6 | 14.3% |
| **Total** | **42** | **100%** |

Ransomware claims cluster around four names: arcusmedia (4), dragonforce (3), krybit (2) and thegentlemen (2). These are leak-site listings, not confirmation that anything was actually encrypted, stolen or disrupted.

The leak side is more varied: identity documents, medical and laboratory data, university accounts, government files, commercial databases. The six access offers involve alleged Fortinet, webmail, government-portal or university-system access. Someone advertising access is not the same thing as that access working.

## What stood out

The Egyptian Ministry of Agriculture produced one of the strongest records this month: correspondence, contracts, payment records, inspection reports, technical inventories, application screenshots, a genuinely coherent set. If it holds up, this kind of material supports land fraud, forged documents and phishing built around real case details.

Nerasolgh, in Ghana, is worth flagging too. The exports reviewed show customer, staff and USSD-payment structures, banking fields, geolocation data, password hashes, transaction records. The actor claims 26 million records; what could actually be reviewed was far smaller. That gap hasn't been resolved.

Heliopolis University and HIMS shouldn't be lumped together even though they look similar on paper. Heliopolis's sample shows parent and student account structures. HIMS's publication claims student, staff, financial and payment data. Neither advertised total has been independently confirmed, and in both cases the structured samples say more than the headline numbers.

Adex, in Tunisia, was an explicit repost by BIGBROTHER. The screenshot shows an administration interface with a record count that roughly matches the advertised “15k”. That makes the access plausible. It says nothing about who broke in first or how much data actually exists.

Planet Sport is a case worth keeping two separate threads on. LockBit 5 listed the domain back in April; a free July post attributed to Mozvo covers the same target. Repost, resale, an affiliate link, any of those would explain it, and none is confirmed. The two records stay linked, not merged.

Zenith Bank shows up twice as well, once in an earlier data claim, once in a July ransomware listing. That's enough to watch closely. It isn't enough to say both came from the same breach.

## Sectoral impact

| Sector | Records | Share |
| :--- | ---: | ---: |
| Government / Administration | 11 | 26.8% |
| Healthcare / Medical | 4 | 9.8% |
| Telecommunications | 5 | 11.9% |
| Education / University | 3 | 7.3% |
| E-commerce / Retail | 3 | 7.3% |
| Technology / Engineering | 3 | 7.3% |
| Oil & Energy | 2 | 4.9% |
| Investment Holding / Energy | 1 | 2.4% |
| Finance / Banking | 1 | 2.4% |
| Transport / Logistics | 1 | 2.4% |
| Real Estate | 1 | 2.4% |
| Mining | 1 | 2.4% |
| Accounting / Audit | 1 | 2.4% |
| Travel / Events | 1 | 2.4% |
| Chemical Manufacturing | 1 | 2.4% |
| Security Services | 1 | 2.4% |
| Gaming / Entertainment | 1 | 2.4% |
| Rubber / Agriculture | 1 | 2.4% |
| **Total** | **42** | **100%** |

Government systems keep taking the most hits: procurement, justice, employment, identity, land, public utilities. The risk doesn't end when the post goes up. Impersonation, fraudulent applications and social engineering built on leaked government data can keep paying off for an actor long afterward.

## Actors

| Actor / source | Records | Main activity |
| :--- | ---: | --- |
| arcusmedia | 4 | Ransomware |
| dragonforce | 3 | Ransomware |
| krybit | 2 | Ransomware |
| BIGBROTHER | 2 | Access sale / repost |
| thegentlemen | 2 | Ransomware |
| Phantom Atlas | 2 | Data leak |
| Other named sources | 27 | Mixed |

A name showing up more than once doesn't establish a campaign. July mixes source accounts, reposts and claims of very different evidentiary quality, so read the actor table as a tally, not a threat map.

## Risk assessment

- 🔴 **High:** Egypt, Tunisia and Morocco.
- 🟠 **Medium:** South Africa, Nigeria, Algeria, Ghana, Côte d’Ivoire and South Sudan.
- 🟡 **Low to medium:** Kenya, Cameroon and Botswana.

The main intelligence gaps are victim confirmation, real volumes, access path, archive completeness and remediation.

## Contextual ATT&CK mapping

| Phase | Technique | Context |
| :--- | :--- | :--- |
| Initial Access | T1190 — Exploit Public-Facing Application | Public portals and exposed applications. |
| Initial Access | T1078 — Valid Accounts | Alleged webmail, Fortinet and privileged access. |
| Credential Access | T1003 — OS Credential Dumping | Claims involving credentials or hashes. |
| Collection | T1213 — Data from Information Repositories | Government, university and corporate repositories. |
| Exfiltration | T1041 — Exfiltration Over C2 Channel | Contextual hypothesis only. |
| Impact | T1486 — Data Encrypted for Impact | Only where encryption is explicitly evidenced. |

## Recommendations

Public bodies: separate identity, land, justice and employment systems, put MFA on every admin account, alert on bulk exports. Universities and healthcare organisations: kill exposed sessions, rotate credentials, check for password reuse. Telecoms and financial firms: watch mailbox forwarding rules, VPN activity, privileged logins and anything touching payment changes.

None of this is exotic. Offline backups, centralised logs, evidence handled carefully, and a response plan that covers both ransomware and plain data exposure, that's still what holds up on the day one of these claims turns out to be real.

## Conclusion

July's threat picture is broad and uneven. Ransomware hasn't slowed down, but data leaks and access offers are pulling in a growing share of identity, health, education, government and payment information. Some of what's above rests on material AFRINTEL actually reviewed. Some of it is still just an actor's word. Keeping that line visible is what makes this report useful.

**AFRINTEL — Adama ASSIONGBON, Consultant SOC & CTI**  
[Repository](https://github.com/Hatchepsoute/AFRINTEL)
