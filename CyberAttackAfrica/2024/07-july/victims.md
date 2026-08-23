[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%7C%20Data%20Leak-red)

# Cyber Attacks in Africa - July 2024: List of 11 Victims
👉🏾 [**French version available here**](./victims_FR.md)

## 📅 July 2024

## Monthly snapshot

July 2024 contains **11 documented incident records**: **7 Ransomware**, **4 Data Leak**, **0 Access Sale**, **0 DDoS**, **0 Defacement** and **0 Operational Fraud**, across **7 African countries**.

Three of the four Data Leak records are July republications of older Algerian datasets and must not be interpreted as three new July compromises.

### July 1, 2024
#### 🇹🇳 Tunisia - Maxcess-logistics
- **Ransomware Group:** killsec
- **Sector:** Transport / Logistics
- **Website:** [maxcess-logistics.com](https://www.maxcess-logistics.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Maxcess-logistics is a Tunisia-based organization classified under Transport / Logistics in the AFRINTEL corpus.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.
### July 2, 2024
#### 🇪🇹 Ethiopia - F.D.R.E Defence War College (cited domain: nwc.ndu.edu)

- **Actor / Group:** TheColorYellow
- **Source context:** Data-sale post published on RaidForums
- **Sector:** Defense / Security
- **Status:** Claim - Data Sample Published
- **Website:** [dwc.edu.et](https://dwc.edu.et/wc/) (organization observed in the samples); actor-cited domain: nwc.ndu.edu
- **Confidence level:** Medium
- **Impact level:** Level 4
- **Incident type:** Data Leak
- **Discovery date:** July 2, 2024

- **Reliability note:**
  TheColorYellow's post presents a victim called the "National War College of Ethiopia" and cites nwc.ndu.edu. That domain corresponds to the National War College of the US National Defense University. However, the five locally provided PNG files display the emblem and Amharic-language header of Ethiopia's "F.D.R.E Defence War College", together with internal documents, a visible inventory of 29 workstations, and a visible table of 17 telephone entries. A domain error in the announcement, a naming confusion, or incorrect technical attribution therefore remains possible. AFRINTEL records the F.D.R.E Defence War College as the organization observed in the samples and retains nwc.ndu.edu as the announced but unverified domain.

- **Description:**
  The visible elements correspond to the F.D.R.E Defence War College, an Ethiopian military-education institution. The official link observed for that organization is [dwc.edu.et](https://dwc.edu.et/wc/). nwc.ndu.edu remains only the domain cited in the actor's announcement.

- **Analysis:**
  TheColorYellow claims to hold 747 MB of confidential emails allegedly stolen directly from the institution's Exchange server, exported as PST mailbox files, and offers the data for $500 through escrow. The local directory contains five PNG files but no PST, EML, MSG, or Exchange export. The images include institutional documents, a Chinese notice for international students, a visible inventory of 29 workstations, and a visible table of 17 telephone entries. These elements are consistent with internal documents from the F.D.R.E Defence War College and strengthen sample attribution, but do not confirm access to the Exchange server, the existence of 747 MB, or the completeness or origin of the data. Amharic and Chinese OCR was not used to transcribe values; no name, hardware identifier, or telephone number is reproduced.

### July 5, 2024
#### 🇿🇦 South Africa - National health laboratory services
- **Ransomware Group:** blacksuit
- **Sector:** Healthcare / Medical
- **Website:** [nhls.ac.za](https://www.nhls.ac.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** National Health Laboratory Service (NHLS) is a South African public laboratory-services organization classified under Healthcare / Medical.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.
### July 11, 2024
#### 🇩🇿 Algeria - Hôpital Chahids Mahmoudi (hcm-dz.com)

- **Actor / Group:** Unknown
- **Source context:** Repost by Addka72424 of material attributed to FriendlyChemist
- **Sector:** Healthcare / Medical
- **Status:** Claim - Data Sample Published
- **Website:** [hcm-dz.com](https://hcm-dz.com)
- **Confidence level:** Medium
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Leak date:** September 21, 2023
- **Discovery date:** July 11, 2024

- **Reliability note:**
  The post is explicitly presented as a repost ("REPOST") of a compilation titled "Algerian Databases Collection", itself reposted from an original post attributed to the account FriendlyChemist. The date and content of the original post are not provided, and the initial collection or access method is not specified.

- **Description:**
  Hôpital Chahids Mahmoudi is an Algerian hospital based in Tizi Ouzou, specialized in oncology and nuclear medicine, with an extension in Algiers and a clinic opened in Constantine in 2024. It operates the hcm-dz.com domain for its professional communications.

- **Analysis:**
  The file associated with hcm-dz.com in the compilation reposted on July 11, 2024 is dated September 21, 2023 and presented as covering approximately 1,900 users. The sample reviewed by AFRINTEL corresponds to email filtering logs (an anti-spam gateway type), not an export of medical records or full mailboxes.

  The visible lines indicate, for each message, the sender, recipient, source IP address, subject, size, a filtering score, direction (inbound, outbound or internal) and a message identifier. Several message subjects reference patient names and types of medical examinations (lab results, imaging, cardiology), indicating professional use of the hospital's email system to transmit results, without the message content itself being visible in the sample.

  The consistency of the log format and the observed volume of lines support a medium confidence level regarding the origin of these logs. AFRINTEL could not, however, confirm effective access to the mailboxes themselves, nor the completeness of any compromise beyond the reposted log lines. The presence of message subjects referencing named patients constitutes exposure of sensitive health-related metadata, which could facilitate targeted phishing, impersonation of medical or administrative staff, and partial reconstruction of care pathways. AFRINTEL does not reproduce any patient name, email address, IP address or message subject from the reviewed sample.

### July 11, 2024
#### 🇩🇿 Algeria - University of Tlemcen (univ-tlemcen.dz)

- **Actor / Group:** Unknown
- **Source context:** Repost by Addka72424 of material attributed to FriendlyChemist
- **Sector:** Education / University
- **Status:** Claim - Data Sample Published
- **Website:** [univ-tlemcen.dz](https://www.univ-tlemcen.dz)
- **Confidence level:** High
- **Impact level:** Level 3
- **Incident type:** Data Leak
- **Leak date:** June 27, 2022
- **Discovery date:** July 11, 2024

- **Reliability note:**
  As with the other files in the same compilation, the exact origin, initial access method and the date of FriendlyChemist's original post are not specified. The sample, however, shows a complete application table structure and consistent individual records.

- **Description:**
  The University of Tlemcen (Abou Bekr Belkaïd) is an Algerian public higher-education institution. It operates a Moodle e-learning platform accessible via the univ-tlemcen.dz domain.

- **Analysis:**
  The file associated with univ-tlemcen.dz in the compilation reposted on July 11, 2024 is dated June 27, 2022 and presented as covering approximately 80,000 users. The sample reviewed by AFRINTEL shows the structure of the `mdl_user` table, specific to the Moodle learning management system, along with an excerpt of real user records.

  The structural fields include the user ID, username, hashed password, first name, last name, email address, institution, department, country, language, and account creation/last-login dates. The visible records include an administrator account associated with the univ-tlemcen.dz domain, as well as accounts linked to email addresses from other Algerian universities, suggesting a shared authentication federation across several universities via this Moodle system rather than a scope limited to Tlemcen alone. Passwords are hashed using heterogeneous formats, including bcrypt for some recent accounts and older, weaker formats for others, without AFRINTEL being able to confirm their actual strength.

  The consistency of the Moodle table structure with the observed records, combined with the presence of an identifiable administrator account, supports a high confidence level regarding the authenticity of this dataset. A compromise of this scale could facilitate takeover of student and staff accounts, academic identity impersonation, and cascading access to other Algerian institutions potentially sharing the same authentication federation. AFRINTEL does not reproduce any credential, hashed password, email address or individual record from the reviewed sample.

### July 11, 2024
#### 🇩🇿 Algeria - Algeria.com (web portal)

- **Actor / Group:** Unknown
- **Source context:** Repost by Addka72424 of material attributed to FriendlyChemist
- **Sector:** Media / Entertainment
- **Status:** Claim - Data Sample Published
- **Website:** [algeria.com](https://www.algeria.com)
- **Confidence level:** Low
- **Impact level:** Level 2
- **Incident type:** Data Leak
- **Leak date:** September 2019
- **Discovery date:** July 11, 2024

- **Reliability note:**
  The data in this file is notably older (2019) than the other elements of the compilation. The domain algeria.com is a generic portal dedicated to Algeria rather than a national .dz domain; the exact origin of the leak and the period during which the associated user-account service was active are not specified.

- **Description:**
  Algeria.com is a web portal dedicated to Algeria (travel, news and lifestyle), which in the past offered user accounts and email addresses under its own domain to some of its visitors.

- **Analysis:**
  The file associated with algeria.com in the compilation reposted on July 11, 2024 is dated September 2019 and presented as covering approximately 3,600 user accounts. The sample reviewed by AFRINTEL includes the fields user ID, username, IP address, email address, a token, and a second field labeled "secret".

  The values observed in the token and secret fields do not match any standard cryptographic hash format clearly identifiable by AFRINTEL, and could correspond to an old proprietary mechanism of the portal rather than a directly exploitable password. The age of the data and the generic nature of the domain, distinct from Algerian institutional .dz domains, limit the current operational relevance of this exposure, although the associated email addresses and usernames could still be reused elsewhere by the individuals concerned.

  Given the age of the data, the limited volume and the absence of a clearly identifiable password field, AFRINTEL assesses this claim with a low confidence level and limited impact. AFRINTEL does not reproduce any identifier, email address, IP address or token value from the reviewed sample.

### July 13, 2024
#### 🇰🇪 Kenya - Kenya urban roads authority
- **Ransomware Group:** hunters
- **Sector:** Transport / Logistics
- **Website:** [kura.go.ke](https://www.kura.go.ke)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Kenya Urban Roads Authority (KURA) is a Kenyan public authority responsible for urban road infrastructure and is classified under Transport / Logistics.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.
### July 17, 2024
#### 🇿🇼 Zimbabwe - Zb financial holdings
- **Ransomware Group:** madliberator
- **Sector:** Finance / Banking
- **Website:** [zb.co.zw](https://www.zb.co.zw)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** ZB Financial Holdings is a Zimbabwean financial-services organization classified under Finance / Banking.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.
### July 17, 2024
#### 🇿🇦 South Africa - Cities network
- **Ransomware Group:** madliberator
- **Sector:** Professional / Business Services
- **Website:** [sacities.net](https://www.sacities.net)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** South African Cities Network is classified under Professional / Business Services in the AFRINTEL corpus.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.
### July 17, 2024
#### 🇪🇬 Egypt - Assih
- **Ransomware Group:** lockbit3
- **Sector:** Professional / Business Services
- **Website:** [assih.com](https://www.assih.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Assih is an Egypt-based organization classified under Professional / Business Services in the AFRINTEL corpus.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.
### July 22, 2024
#### 🇿🇦 South Africa - Sibanye-stillwater
- **Ransomware Group:** ransomhouse
- **Sector:** Mining / Extractive Industries
- **Website:** [sibanyestillwater.com](https://www.sibanyestillwater.com)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Sibanye-Stillwater is a South Africa-based mining organization classified under Mining / Extractive Industries.

---

- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.
## ✍🏿 Author
*Adama ASSIONGBON* *Senior SOC & Cyber Threat Intelligence (CTI) Consultant*
