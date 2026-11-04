# AFRINTEL CTI report - cyber incidents in Africa (October 2026)

![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

English version - [Version française](./README_FR.md) - [Victim records](./victims.md)

## 1. Executive summary

The October 2026 corpus contains **48 documented incidents**. This is AFRINTEL's documented visibility for the month, not an exhaustive measure of all cyberattacks affecting Africa.

Data leaks were the leading category with 23 incidents, followed by ransomware with 17, system intrusions with 5 and access sales with 3. Egypt and Morocco each account for 12 incidents, followed by South Africa with 9. The most represented sectors are public administration, commerce and retail, and technology or digital services.

Actor names and account labels are retained as identifiers observed in the publications. They do not, by themselves, establish independent technical attribution. Four incidents remain without an established actor.

### 1.1 Comparison with September 2026

| Incident type | September | October | Change |
|---|---:|---:|---:|
| Ransomware | 20 | 17 | -3 (-15.0%) |
| Data Leak | 11 | 23 | +12 (+109.1%) |
| Access Sale | 0 | 3 | +3 |
| System Intrusion | 2 | 5 | +3 (+150.0%) |
| **Total** | **33** | **48** | **+15 (+45.5%)** |

## 2. Methodology

Monthly assignment follows the publication date or the first documented AFRINTEL observation, rather than an inferred compromise date. Incidents were deduplicated at victim and event level. The two Malagasy offers, `staging.sso.gov.mg` and `e-koragna.gov.mg`, are counted as two separate incidents linked to the same seller account.

Statistics are derived from the [French victim records](./victims_FR.md), then checked against the [English victim records](./victims.md). Both files contain 48 records in the same order. Sectors are normalized using the [2026 sector mapping](../../../normalization/sector_mapping_2026.csv). A multi-country incident counts once in the global total.

The supplied visual material, observed publications and accessible local samples were used according to their information level. Incident-specific limitations are documented in the corresponding victim records.

## 3. Global overview

### 3.1 Incident type distribution

| Type | Count | Share |
|---|---:|---:|
| Data Leak | 23 | 47.9% |
| Ransomware | 17 | 35.4% |
| System Intrusion | 5 | 10.4% |
| Access Sale | 3 | 6.3% |
| **Total** | **48** | **100.0%** |

![Incident type distribution](assets/type_EN.png)
![Circular incident type distribution](assets/type_pie_EN.png)

### 3.2 Countries and regions

| Country | Incidents |
|---|---:|
| Egypt | 12 |
| Morocco | 12 |
| South Africa | 9 |
| Democratic Republic of the Congo | 2 |
| Ethiopia | 2 |
| Madagascar | 2 |
| Republic of the Congo | 1 |
| Rwanda | 1 |
| Mozambique | 1 |
| Gabon | 1 |
| Tunisia | 1 |
| Benin | 1 |
| Nigeria | 1 |
| Sierra Leone | 1 |
| Côte d'Ivoire | 1 |

North Africa leads the regional distribution, followed by Southern Africa. Regional charts should be read as a distribution of documented occurrences, not as an estimate of actual prevalence.

| Region | Incidents | Included countries |
|---|---:|---|
| North Africa | 25 | Egypt (12), Morocco (12), Tunisia (1) |
| Southern Africa | 10 | South Africa (9), Mozambique (1) |
| East Africa | 5 | Ethiopia (2), Madagascar (2), Rwanda (1) |
| Central Africa | 4 | DRC (2), Gabon (1), Republic of the Congo (1) |
| West Africa | 4 | Benin (1), Côte d'Ivoire (1), Nigeria (1), Sierra Leone (1) |
| **Total** | **48** | **15 countries** |

![Top 5 countries](assets/country_top5_EN.png)
![Geographic distribution](assets/geo_EN.png)
![Regional distribution](assets/region_pie_EN.png)

### 3.3 Evidence status

| Tracked status | Incidents | Share |
|---|---:|---:|
| Claim - Unverified | 20 | 41.7% |
| Data Sample Published | 21 | 43.8% |
| Data Fully Published | 2 | 4.2% |
| Victim / authority communication | 4 | 8.3% |
| Under Investigation | 1 | 2.1% |
| **Total** | **48** | **100.0%** |

These statuses describe the information available in the corpus. They do not all constitute independent technical confirmation.

![Evidence status](assets/evidence_EN.png)
![Circular evidence status](assets/evidence_pie_EN.png)

### 3.4 Most visible actors or accounts

| Observed account or label | Incidents |
|---|---:|
| Nameless511 | 9 |
| UmBra | 4 |
| N0n | 4 |
| The Gentlemen | 3 |
| SensitiveDarkForum | 2 |
| Krybit | 2 |
| Qilin | 2 |
| Lenken | 2 |
| Kazu | 2 |
| List1 | 2 |

The `bytetobreach` account is retained as the publication identifier for Ampath. Four records have no established attribution. Rankings measure the frequency of source labels, not the actors' actual operational capability.

![Most represented actors](assets/actor_top10_EN.png)

### 3.5 Quick sector view

| Normalized sector | Incidents |
|---|---:|
| Government / Public administration | 12 |
| Commerce / Retail | 8 |
| Technology / Digital services | 6 |
| Healthcare | 5 |
| Education | 5 |
| Finance / Insurance | 3 |
| Transport | 2 |
| Industry / Engineering | 2 |
| Other sectors | 5 |

![Top sectors](assets/sector_top10_EN.png)
![Sector distribution](assets/sector_EN.png)
![Circular sector distribution](assets/sector_pie_EN.png)

## 4. Detailed analysis by incident type

### 4.1 Data Leaks - 23 incidents

Data leaks were the leading signal of the month. Cases include customer databases, identity data, health data, education data, administrative documents and professional information. Sensitivity is especially high for government, healthcare and human resources environments.

The Ampath Laboratories of the Zululand case includes a structured local sample with files related to employees, patients, admissions, payments and health data. The reviewed files show exposure of personal and medical data categories. The accessible material does not establish the claimed scope of the disclosure or the hundreds of databases mentioned in the publication.

### 4.2 Ransomware - 17 incidents

Victims appear in ransomware group publications. The records distinguish a listing, an available sample, a displayed deadline and an actually observed disclosure. A listing is not automatically treated as a complete disclosure. Among the 17 cases, Eurogate Tanger has a published archive that was analyzed in read-only mode; YOD Ingénierie and CNESTEN underwent a structural review of the publication and a local artifact, without examining the contents of the announced documents. For the other 14 cases, no exploitable content was analyzed in the available corpus. Some publications show no deadline, while others still displayed a countdown at report close. These elements do not establish the outcome of negotiations, any payment or complete exfiltration.

### 4.3 System Intrusions - 5 incidents

The five cases describe system access or intrusions documented in the month's sources. They remain separate from access sales: a publication describing potential access is not merged with another victim or another platform.

### 4.4 Access Sales - 3 incidents

Access sales concern environments or accounts presented by sellers as accessible. The Malagasy case contains two separate records for the two platforms offered by the same actor. The seller and account are documented as observed elements; technical attribution and current access validity are separate questions.

### 4.5 Priority cases and evidence

The following cases were selected for intelligence value, sensitivity or the quality of accessible evidence. They do not replace the complete 48-record register.

1. **Tera.ma.** A documented Odoo export contains 8,140 files, 2,389,358,436 bytes, 282 CSV files, 3,693 PDFs and several thousand images. Observed counts include 19,595 partners, 69,197 orders and 124,088 accounting entries. The initial vector and actual extraction date remain unknown.
2. **NextLevel PC.** The eight reviewed CSV files match the published figures: 52,545 customers, 60,262 addresses, approximately 47,653 orders, 11 internal accounts and 14,160 commercial rules. The corpus describes the analyzed sample, not necessarily the full database.
3. **Moroccan Ministry of Habous.** The available files contain 33 XLSX workbooks and one CSV. The inventory contains approximately 109,640 data rows after removing presumed headers. Technical provenance from the ministry infrastructure is not established.
4. **Rwanda Ministry of Health.** The publication claims 375 tables and 5.7 GB compressed. The accessible corpus contains 375 CSV files and 6,050,914,271 bytes, with 42,509,228 physical lines. Embedded line breaks prevent direct conversion into a patient count.
5. **Ampath Laboratories of the Zululand.** Local samples include employee, patient, admission, Medicaid and payment data. They establish the presence of medical, personal and financial data categories, but do not validate the claimed 80 million records.
6. **Lawyers for Human Rights.** The organization stated that a database hosted by a service provider was accessed and downloaded without authorization. The system was secured and an investigation started. No ransomware encryption is documented.
7. **e-Solde, Republic of the Congo.** The offer mentions a public platform and administrative, payroll and account data. The earlier June repost is linked to the same case and is not counted separately.
8. **Madagascar.** The offers for `staging.sso.gov.mg` and `e-koragna.gov.mg` are counted as two separate incidents despite the same seller. The visual material suggests an identity interface; no interactive access was tested.
9. **Eurogate Tanger.** An archive of 355 files and 373,065,003 uncompressed bytes includes office documents, messages, EDI/XML files and technical material. Document disclosure does not prove encryption or port disruption.
10. **MINESURSI, DRC.** The announcement claims 136 GB and 125,823 files. The examined archive is smaller: 1,531 files, including 581 PDFs and 950 images, consistent with teacher records. The number of people concerned is unknown.
11. **Mozambique PGR.** The sample describes 262 files totaling 75,941,802 bytes. The same composition and size appear in the Rand Mutual Assurance record. This must be resolved before treating both corpora as independent corroboration.
12. **Rand Mutual Assurance.** The organization acknowledged a security alert and opened an investigation. Claimed volumes of 366 GB, 1,683,810 claims and 593,786 files are not validated by the local sample.
13. **GCIS, South Africa.** The recruitment portal was reported compromised after suspicious activity detected on 24 October. The scope of access to applicant identities, phone numbers and emails remains to be determined.
14. **InvestNaija / Chapel Hill Denham.** Unusual activity may have exposed part of customer information. The organization indicated that less than 1% of information could be involved, without specifying the exact record count.
15. **BlueBus, Egypt.** The sample contains 2,999 order rows, 1,178 distinct customer identifiers, 350 distinct emails and 358 rows containing a national identifier. These figures do not describe the full claimed database.
16. **Al Arabia United, Egypt.** The company acknowledged unauthorized content on a public advertising screen and disabled it. The incident is linked to a distribution chain, with no evidence of a confirmed data leak.
17. **ServerUnlockApp, DRC.** An application backup of 7,329 files and 158,750,705 bytes exposes management, order, payment and configuration material. The current validity of any secrets was not tested.

**CNESTEN update.** The CNESTEN case, initially treated as a claim without a sample, now has a directory inventory recovered before the link became unavailable. The inventory contains 158,539 lines and lists 110,803 files totaling 205,805,114,681 stated bytes. It was structurally analyzed, without recovering or examining file contents. The record status was raised to `Claim - Data Sample Published` with `Medium` confidence.

## 5. Strategic trends

### 5.1 Industrialization of commercial data leaks

The Tera.ma, NextLevel PC, Midipcom and Karamtech cases show the value of ERP and e-commerce exports for supplier fraud, tailored phishing and payment-request manipulation. Observed volumes in Tera.ma and NextLevel PC are better supported than the claimed volumes in the other cases.

### 5.2 Convergence of identity, recruitment and healthcare data

Recruitment portals, public bodies, universities and healthcare organizations concentrate civil identities, diplomas, addresses, supporting documents and professional information. These data can support fake summonses, identity theft and campaigns targeting vulnerable people.

### 5.3 Ransomware visibility exceeds technical evidence

The 17 ransomware records do not all demonstrate encryption, service disruption or a verified exfiltration scope. A victim listing, a sample and a full disclosure remain distinct events.

### 5.4 Dependencies and trust chains

The Lawyers for Human Rights, Al Arabia United and Madagascar cases show the role of providers, distribution chains and identity platforms. Third-party security, environment separation and rapid access revocation should be treated as core controls.

## 6. Sector impact

Public administration is the most represented normalized sector family. It concentrates risks involving identities, public services, privileged accounts and citizen data. Commerce and retail primarily expose customer and transaction data. Technology and digital services may provide relay points into other organizations.

Healthcare and education each account for five occurrences. These sectors combine sensitive personal data with patient or student information and operational processes that can be difficult to interrupt. The counts represent incident occurrences, not affected-person volumes.

## 7. Threat actor profile and risk assessment

The month's sources show a mixture of ransomware groups, forum accounts and access sellers. The most visible labels are Nameless511, UmBra, N0n and The Gentlemen. This visibility measures publication frequency and does not establish technical attribution.

### 7.1 Country risk assessment

Egypt and Morocco have the highest number of documented occurrences, followed by South Africa. This supports increased monitoring of public administration, digital services and exposed platforms. The risk level here is relative to AFRINTEL's documented corpus and is not a comprehensive national measure.

## 8. Trends and intelligence gaps

The main trends are the monthly increase in total documented volume, the weight of data leaks and the growth of system intrusions and access sales. The main intelligence gaps concern official confirmation, technical actor identification, sample completeness, the actual initial-access date and the outcome of ransomware negotiations.

The four incidents without established attribution remain in the global total. Names displayed in the sources are not converted into independent attribution.

## 9. Contextual MITRE ATT&CK mapping

The mappings below are contextual and do not prove that each technique was used:

| Technique | CTI interpretation |
|---|---|
| T1190 - Exploit Public-Facing Application | Hypothesis relevant to access or intrusion involving exposed services |
| T1078 - Valid Accounts | Hypothesis relevant to access sales or compromised accounts |
| T1005 - Data from Local System | Hypothesis relevant to data extraction |
| T1567 - Exfiltration Over Web Service | Hypothesis when remote publication or hosting is mentioned |
| T1486 - Data Encrypted for Impact | Ransomware context only; encryption is not assumed without source evidence |

## 10. Recommendations by organization type

- Government: inventory exposed domains, strengthen MFA and privileged accounts, segment sensitive services and prepare notification procedures.
- Healthcare and education: protect sensitive databases, limit exports, monitor privileged accounts and test continuity plans.
- Commerce and finance: strengthen customer-account, administration-interface and payment-flow protection; detect unusual exports.
- Digital providers: segment customers, control administrative access and log export operations.

## 11. SOC and tactical recommendations

**Observed:** data-leak publications, ransomware listings, access offers and, for Ampath, a structured sample containing several sensitive data categories.

**Hypotheses to test:** exploitation of an exposed service, credential reuse, automated extraction, transfer to a remote service or reuse of a sold access.

**Preventive measures:** investigate anomalous connections, reset affected secrets after qualification, revoke sessions, review external-access rules, preserve logs and monitor database exports. Do not test a sold access against a live infrastructure.

## 12. Strategic recommendations

Organizations should connect criminal-publication monitoring with asset inventory, identity management and incident response. Priorities are exposed-asset visibility, phishing-resistant MFA, sensitive-data segmentation, log retention and regular crisis exercises. Metrics should distinguish publication volume, corroborated incidents and established impact.

## 13. Operational action plan

### Immediate priority - 0 to 7 days

Identify the environments cited in the records, preserve IAM, WAF, application, database, backup and network-egress logs, then invalidate exposed sessions and secrets after qualification. Strengthen controls over bank-detail changes and large exports.

### Short term - 8 to 30 days

Map sensitive data held by recruitment portals, ERP systems, healthcare services and external providers. Audit service accounts, administrators, contractors and staging environments. Deploy detections for bulk downloads and token reuse.

### Consolidation - 30 to 90 days

Exercise crisis scenarios covering an ERP leak, identity-document exposure, provider compromise and advertising-system hijacking. Measure log coverage, secret-revocation time and MFA protection for privileged accounts.

## 14. Intelligence quality and caveats

- **Deduplication:** the e-Solde repost observed in June and October is counted once.
- **Attribution:** a forum pseudonym proves neither the real identity nor group membership.
- **Quantification:** a row, file, order or case does not necessarily represent one unique person.
- **Traceability:** the similarity between the Mozambique PGR and Rand Mutual samples must be resolved through hash and provenance comparison before any independent-corroboration conclusion.

### 14.1 November monitoring outlook

The following are monitoring hypotheses, not observed events:

- **Reuse of commercial documents:** monitor payment fraud, bank-detail changes and messages citing exact order references.
- **Fraud around public recruitment:** monitor fake summonses, fee requests and domains resembling institutional websites.
- **Reuse of access and secrets:** search for new privileged terminals, service accounts used from a new ASN and exports after role changes.
- **Amplification of ransomware claims:** monitor new samples, victim confirmations and archives reused under multiple names.

### 14.2 Source traceability

The report's primary sources are the validated pair [victims_FR.md](./victims_FR.md) and [victims.md](./victims.md), observed publications, organizational communications and accessible visual material or samples. Criminal links, raw personal data, secrets and tokens are not reproduced. Conclusions remain revisable if official confirmation or new independent evidence becomes available.

## 15. Conclusion

October 2026 is characterized by strong data-leak visibility and an increase in total documented incidents. The corpus highlights exposure across public administration, commerce, digital services, healthcare and education. The detailed review shows that the depth of some datasets and their possible reuse for fraud matter more than the number of alleged victims alone. Results should support defensive prioritization and further collection.

AFRINTEL - Cyber Threat Intelligence for Africa
[GitHub repository](https://github.com/Hatchepsoute/AFRINTEL)
