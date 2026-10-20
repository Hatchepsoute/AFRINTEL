# AFRINTEL - Monthly Cyber Threat Intelligence Report
👉🏾[**French version available here**](./README_FR.md)

## Table of contents

1. [Reading note and analytical warning](#reading-note-and-analytical-warning)
2. [Executive summary](#executive-summary)
3. [01. Scope, sources and method](#01-scope-sources-and-method)
4. [02. September 2026 dashboard](#02-september-2026-dashboard)
5. [03. Priority intelligence cases](#03-priority-intelligence-cases)
6. [04. Operational lessons and attack hypotheses](#04-operational-lessons-and-attack-hypotheses)
7. [05. Hunt plan - SOC / CERT / CSIRT](#05-hunt-plan---soc--cert--csirt)
8. [06. Risk-reduction roadmap](#06-risk-reduction-roadmap)
9. [07. Earlier incidents: context not to confuse with September](#07-earlier-incidents-context-not-to-confuse-with-september)
10. [08. Intelligence prioritisation](#08-intelligence-prioritisation)
11. [Appendices A to D](#appendix-a---register-of-29-september-publications)

> The detailed English sections corresponding to items 03 to 11 are being synchronised with the French report. The current English edition retains the validated dashboard, CTI cases, defensive implications and conclusion below.
**Africa - September 2026**
**Ransomware, data leaks and extortion monitoring**

Monitoring overview of publications affecting African organisations, based on ransomware-group sites, leak sites and underground forums.

| **29** | **12** | **41** |
|:---:|:---:|:---:|
| September-dated publications | Earlier incidents integrated | Total unique corpus |

**Edition:** 17 October 2026
**Scope:** Africa, AFRINTEL OSINT and monitoring records
**Audience:** CISOs, SOC teams, CERT/CSIRT teams, risk owners and CTI analysts
**Distribution:** Monitoring analysis. No personal data or criminal links reproduced.

## Reading note

This report describes a monitoring corpus built from observed underground publications. It is not a list of 29 confirmed intrusions and it is not an exhaustive measure of cybercrime in Africa.

The English and French victim files contain the same 41 records and are treated as one bilingual source. Only 29 records concern publications dated in September 2026; the other 12 concern earlier incidents integrated retrospectively. Publication dates are not automatically incident dates. A victim listing, a visible sample and a later disclosure are separate events. Payment, negotiation, resale or removal are not inferred from the presence or absence of a file.

## Executive summary

The September signal is dominated by ransomware-related claims, but most publications are not corroborated by independent technical evidence.

| Indicator | Value | CTI reading |
|---|---:|---|
| Corpus records | 41 | 29 September publications and 12 earlier incidents |
| September publications | 29 | Across 12 countries |
| Ransomware | 20 / 29 (69.0%) | Monitoring label or claim, not proven encryption |
| Data Leak | 7 / 29 (24.1%) | Publications concerning alleged data exposure |
| System Intrusion | 2 / 29 (6.9%) | Documented access or attempt, with limited outcome |
| Claim - Unverified | 12 / 29 (41.4%) | Publication without associated public confirmation |
| Claim - Data Sample Published | 12 / 29 (41.4%) | Visible extract or local corpus, without automatic access confirmation |
| Data Fully Published | 1 / 29 (3.4%) | AFRICA-TECH: 10 released files examined |
| South Africa + Egypt | 15 / 29 (51.7%) | Monitoring concentration, not an attack rate |

### Five strategic conclusions

1. Disclosure-based extortion dominates the visible signal: 20 of 29 September publications are classified as Ransomware, although encryption generally cannot be confirmed.
2. The corpus is geographically concentrated: South Africa accounts for 8 publications and Egypt for 7. This also reflects monitored sources, campaign visibility and editorial selection.
3. The intelligence value is highest where artefacts were observed: Centre Atlantique Formation, SEPE, AFRICA-TECH, Apollo 21, ARCA and FCT-IRS provide more substance than a simple leak-site listing.
4. Priority risks include identity fraud, payment fraud, reuse of administrative documents, targeted phishing and disclosure of plans, banking documents or certificates. Operational damage is not assumed.
5. Two September-dated cases have confirmation statuses in the cards: RelyComply is recorded as `Victim Confirmed - Unauthorized Access`, and the Namibian Defence Force as `Government Confirmed - Unauthorized Access`. These statuses concern access or an incident, not automatically encryption, exfiltration or claimed volumes.

## 1. Scope, sources and method

### 1.1 Three timelines to keep separate

**Incident date:** the actual time of access or disruption, often unknown for September publications.
**Initial publication date:** the date displayed on a forum, extortion list or message, used to place a record in the September publication cohort.
**Discovery or integration date:** when AFRINTEL obtained an artefact or integrated the case, which may be later than the month concerned.

An item published on 27 September and reviewed on 8 October remains a September publication. Conversely, a January 2026 incident added to the inventory in September is not treated as an incident occurring in September.

### 1.2 Observation status and documentary depth

| Status | Operational meaning | Limitation |
|---|---|---|
| Claim - Unverified | Publication observed without associated public confirmation | A listing alone does not establish access |
| Claim - Data Sample Published | Publication accompanied by an extract or images | Data origin may remain unknown |
| Data Fully Published | Release reviewed according to the collection | Does not prove that all obtained data was released |
| Victim / Government Confirmed | Public confirmation by an organisation or authority | Vector and scope may remain unknown |
| Corroborated | Several public elements converge | Does not establish every claimed effect |

To avoid conflating status and analytical depth, AFRINTEL also uses this descriptive scale:

| Level | Description | What cannot be inferred |
|---|---|---|
| P0 - Publication observed | Victim, domain, account or threat displayed at a given time | Intrusion, data authenticity or technical responsibility |
| P1 - Visible or reviewed sample | Extract, image or file structure consistent with the organisation | Certain technical source, total volume, unique persons or encryption |
| P2 - Published batch reviewed | Batch made accessible during collection and characterised locally | Complete exfiltration, initial access, restoration or payment |

This scale complements, but does not replace, AFRINTEL statuses. A third-party exposure can be confirmed at the exposure level without establishing a direct intrusion at the named organisation.

### 1.3 Methodological limits

The corpus is primarily based on monitoring ransomware-group sites, leak sites and underground forums, supplemented where available by public communications and visible material associated with the publications. These sources document listings, displayed actors, dates, deadlines, samples and possible releases. They do not always establish initial access, data completeness or the outcome of a negotiation.

The French and English victim files are the consolidated editorial record of this monitoring. Raw artefacts, screenshots and external manifests are not treated as official confirmation. No personal data, credentials, secrets or tokens are reproduced.

The corpus is not exhaustive. Visibility varies by country, language, sector, source availability and publication access. Counts measure AFRINTEL's observable monitoring activity, not the actual number of intrusions.

For ransomware cases, listing, sample, deadline, disclosure and last verification are tracked separately. Payment, negotiation, removal, resale and transfer remain `unknown` unless specific public information supports a qualification.

## 2. September dashboard

The following visualisations measure known AFRINTEL publications, not confirmed attacks.

![Figure 1: corpus composition](AFRINTEL_figures/01_corpus.png)

*Figure 1 - Unique corpus: 29 September publications and 12 earlier incidents.*

![Figure 2: documentary depth](AFRINTEL_figures/08_profondeur.png)

*Figure 2 - Documentary depth: 11 detailed analyses and 18 complementary monitoring cards.*

The 18 complementary cards mainly provide alerting and initial qualification. They should not be treated as equivalent to cases supported by reviewed samples or local artefacts.

![Figure 3: publications by country](AFRINTEL_figures/02_pays.png)

*Figure 3 - Countries associated with the 29 September publications.*

![Figure 4: classification and observation status](AFRINTEL_figures/03_typologie_preuve.png)

*Figure 4 - Incident type on the left and publication status on the right.*

The September cohort contains 12 `Claim - Unverified` records, 12 `Claim - Data Sample Published` records, 2 acknowledged indirect exposures, 1 `Victim Confirmed` record, 1 `Government Confirmed` record and 1 `Data Fully Published` record. These categories describe different observation levels and do not automatically establish complete exfiltration, access vector or claimed volumes.

![Figure 5: incident-type comparison](AFRINTEL_figures/09_types_comparison.png)

*Figure 5 - Incident types in the 29 September-dated publications compared with the complete 41-record corpus.*

The September publication cohort contains 20 Ransomware records, 7 Data Leak records and 2 System Intrusion records. The complete corpus contains 24 Ransomware, 10 Data Leak, 4 System Intrusion, 2 Defacement and 1 Access Sale records.

![Figure 6: publication chronology](AFRINTEL_figures/04_chronologie.png)

*Figure 6 - Displayed first-publication dates in September.*

The peaks on 1, 7, 12 and 21 September each contain three publications. They may reflect grouped deposits or source selection and do not establish common intrusion dates.

![Figure 7: country and incident type](AFRINTEL_figures/07_pays_typo.png)

*Figure 7 - Country and declared incident-type cross-tabulation.*

![Figure 8: sector distribution](AFRINTEL_figures/05_secteurs.png)

*Figure 8 - Editorial grouping into ten sector families.*

For the September cohort, Finance, Insurance and Compliance account for 7 publications (24.1%). Transport and Logistics and Real Estate, Construction and Architecture account for 4 each. Health, Government and Technology account for 3 each. These are corpus concentrations, not national attack rates.

![Figure 9: most visible actors](AFRINTEL_figures/06_acteurs.png)

*Figure 9 - Most frequent displayed actor labels in the September cohort.*

The most visible labels are `krybit` (6), `TheGentlemen` (4), `BLACKLOCKS` (2), `N0n` (2) and `lockbit5` (2). The 13 remaining records include less frequent labels and records without public attribution. Actor labels do not constitute forensic attribution or a count of distinct groups.

## 3. Geographic and sector distribution

### September-dated publications: 29 records

| Country | Records | Share |
|---|---:|---:|
| South Africa | 8 | 27.6% |
| Egypt | 7 | 24.1% |
| Morocco | 3 | 10.3% |
| Nigeria | 2 | 6.9% |
| Angola | 2 | 6.9% |
| Namibia, Tunisia, Ethiopia, Mali, Tanzania, Uganda and Kenya | 1 each | 3.4% each |
| **Total** | **29** | **100%** |

For the complete 41-record corpus, South Africa accounts for 16 records, Egypt 7, Morocco and Kenya 3 each, Nigeria and Angola 2 each, and the other countries 1 each. This complete-corpus view includes the 12 earlier incidents.

After cautious normalisation of sector labels in the complete corpus, Health and Government / Administration each account for 5 records, Insurance for 3, and Real Estate, Education, Financial Services and Air Transport for 2 each. The remaining 20 records belong to distinct or specialised sectors. For the September cohort alone, the leading sector family is Finance, Insurance and Compliance with 7 records.

## 4. Priority CTI cases

The priority selection is based on data sensitivity, analytical depth and defensive value. Each card separates observation, claim, assumptions and unknowns.

| Priority case | Observed or reported elements | Still unknown |
|---|---|---|
| MDCN - Nigeria | Local 50-row, 24-column CSV with checked structure | Technical provenance, unique persons, intrusion and full volume |
| Centre Atlantique Formation - Morocco | Training records and documents described in the sample | Completeness, number of people and source system |
| SEPE - Angola | 1,189 local files, including 111 JSON files, reviewed in the card | Actual exfiltrated volume, encryption and access vector |
| AFRICA-TECH - Mali | Published file set examined in the card | Completeness, backup destruction and victim confirmation |
| FNB - South Africa | Five images of apparent business-account statements | Banking provenance, account access and full business authenticity |
| VSB Attorneys - South Africa | Incomplete multipart RAR5 fragment tested read-only | Content, completeness and actual disclosure |
| Air Tanzania - Tanzania | Files and images described in the available sample | Acquisition source, unique persons and full scope |

Selected measurements illustrate the limits of claimed volumes. The SEPE sample contains 1,189 local files, including 111 JSON files, totalling 544,921,521 bytes, while the publication claims 364,841 files, 110,021 users and 179 GB. The FCT-IRS PDF contains 2,541 email-pattern matches, 2,540 distinct textual values and 61 Nigerian phone-pattern matches. These are technical matches, not affected-person counts. Apollo 21 and ARCA references to 400 GB and 400G remain actor claims. The VSB directory contains an incomplete 1,082,440,568-byte RAR5 fragment and an empty companion file; the archive test failed, so no disclosure is treated as analysed.

The MDCN CSV contains 50 data rows and 24 columns, with constant row width and no fully duplicated row. Individual values were not copied into the repository. The structure supports analysis of the supplied sample, not validation of the claimed 65,580 users or a technical compromise of MDCN.

For each case, publication, sample and compromise are separate levels. Amounts, sizes and volumes attributed to an actor remain claims when not independently corroborated. References to third parties visible in a document do not automatically create a separate incident.

## 5. Defensive implications

- Protect identity, administrative, health and payment data against phishing, impersonation and fraud.
- Monitor unusual exports, archive creation, privileged access, VPN/RDP activity, role changes and external sharing.
- Verify MFA, segmentation, administrative logging, isolated backups and tested restoration.
- Treat leak, access-sale, ransomware and defacement signals as separate event types.
- Preserve captures, timestamps, hashes and manifests outside the repository without testing credentials or following criminal links.

These are defensive hypotheses, not technique attributions to the observed actors. Relevant ATT&CK hypotheses include Valid Accounts (`T1078`), Data from Information Repositories (`T1213`), Archiving Collected Data (`T1560`), Exfiltration to external infrastructure (`T1041`) and Data Encrypted for Impact (`T1486`, confirmation required).

## 6. Conclusion and quality checks

The September 2026 corpus contains 29 publications dated in the month and 12 earlier incidents integrated for retrospective tracking, for 41 records overall. It reflects AFRINTEL monitoring of ransomware-group sites, leak sites and underground forums. It is not a count of intrusions that actually occurred in September and it is not an exhaustive measure of African cybercrime.

The observed publications are mostly associated with ransomware claims. Some include visible samples or released data, while a small number have public confirmation of access or an incident. These observation levels remain separate from exfiltration completeness, initial vector, encryption, ransom payment and operational impact.

The collection does not establish a common technical campaign, a dominant access vector or a real increase in attacks compared with August. It does highlight recurring risks involving identities, administrative documents, financial data, document repositories and supplier relationships. These risks justify targeted validation of assets, privileged access, exports, external sharing and payment-fraud controls.

For affected organisations, an underground publication should be treated as a signal for verification and preparation, without waiting for a complete release and without automatically concluding that a compromise occurred. CTI follow-up should focus on changes to the victim listing, samples, deadlines, possible releases, public confirmations and republications. Payments, negotiations, removals, resales and transfers remain unknown unless specific public information supports a qualification.

This report provides a documented monitoring baseline for defensive prioritisation. It should be updated when the public status of a victim changes, without turning an underground observation into technical or institutional confirmation.

Checks completed:

- 41 French cards and 41 English cards;
- one FR/EN correspondence per card, preserving analytical order;
- incident-type total = 41;
- country total = 41;
- regional total = 41;
- observation-status total = 41;
- incident, publication and integration dates remain separate;
- normalised types and statuses checked against the structured card values.

Full details, source notes and limitations are available in the [English victim cards](./victims.md) and [French victim cards](./victims_FR.md).

**AFRINTEL - TLP:CLEAR**
