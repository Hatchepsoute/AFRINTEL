# AFRINTEL Cyber Incidents - July 2024 - canonical corpus (11 records)

👉🏾 [Version française](./victims_FR.md)

> This file contains only incidents retained in canonical 2024 statistics. Historical discoveries, republications, duplicates, and unresolved-chronology cases are preserved separately at the 2024 root.


### July 1, 2024
#### 🇹🇳 Tunisia - Maxcess-logistics
- **Actor / Group:** killsec
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
- **Actor / Group:** blacksuit
- **Sector:** Healthcare / Medical
- **Website:** [nhls.ac.za](https://www.nhls.ac.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 3
- **Victim Description:** National Health Laboratory Service (NHLS) is a South African public laboratory-services organization classified under Healthcare / Medical.


- **Reliability note:**
  The card documents a ransomware leak-site publication without a technical sample or independent victim confirmation in the supplied material. AFRINTEL therefore does not confirm intrusion, encryption or exfiltration on the basis of this publication alone.

### July 10, 2024

#### 🇩🇿 Algeria - EmploiPartner
- **Incident date:** July 10, 2024
- **Initial publication / retained source date:** July 14, 2024
- **AFRINTEL discovery date:** August 23, 2026 - retrospective audit
- **Timeline precision:** Wednesday, July 10 date supported by the audit sources.
- **Actor / Group:** Unknown
- **Sector:** Professional / Business Services
- **Website:** [emploipartner.com](https://www.emploipartner.com/)
- **Status:** Victim Confirmed
- **Incident type:** System Intrusion
- **Confidence level:** High
- **Impact level:** Level 3
- **Analysis:** EmploiPartner said it detected and contained unauthorized access, opened an investigation, and strengthened its platform. Public sources used in the audit are insufficient to confirm data exfiltration, ransomware, DDoS, or an access sale. AFRINTEL retains `System Intrusion`.
- **Public sources:** [Le Jeune Indépendant](https://www.jeune-independant.net/wp-content/uploads/2024/07/EDITION-14-07-2024.pdf) | [KonBriefing](https://konbriefing.com/en-topics/cyber-attacks-2024.html) | [EmploiPartner](https://www.emploipartner.com/)

----------------------------

### July 12, 2024
#### 🇺🇬 Uganda - Ministry of Education and Sports

- **Incident date:** Not established; the date below is the access-offer publication date
- **Initial publication date:** July 12, 2024 at 06:53 (displayed time; timezone not specified)
- **AFRINTEL discovery date:** September 25, 2026 (supplied screenshot)
- **Actor / Group:** 303 (displayed forum account; identity and affiliation unverified)
- **Sector:** Government / Administration
- **Website:** [education.go.ug](https://www.education.go.ug/)
- **Status:** Claim - Unverified
- **Incident type:** Access Sale
- **Subtype:** WordPress administrator access offer
- **Confidence level:** Medium
- **Impact level:** Level 3

- **Description:** Uganda's Ministry of Education and Sports is presented in the post as the target of a WordPress administrator-access offer associated with `education.go.ug`.

- **Analysis:**

  **Observed:** The supplied screenshot shows a forum post titled “Uganda Ministry of Education WordPress Access (Administration Account)”, attributed to the **303** account and timestamped 12 July 2024 at 06:53, with an edit displayed at 06:54. It cites `https://www.education.go.ug/` and advertises WordPress administrator access. The area containing the credentials is hidden by the forum and was not accessed, reproduced or tested.

  **Assumption:** The post title and cited domain make a link to Uganda's ministry plausible. They do not establish that the access was real, current, administrative, or related to the ministry's infrastructure rather than a third-party component.

  **Unknown:** credential validity, actual privileges, access-acquisition vector and date, affected systems, any content modification, data exposure, exploitation, and confirmation by the ministry or an authority remain unknown.

- **Risk assessment:** if authentic, WordPress administrator access could enable modification of public content, dissemination of false information, use of the site for phishing, or access to site-management data. The post does not confirm any of these effects.

- **Recommendations:**
1. Preserve WordPress, hosting, WAF, authentication and administration logs covering July 2024 and any period still available.
2. Review administrator accounts, roles, plugins, themes, SFTP or hosting access, and content or configuration changes.
3. Reset administration access and revoke sessions as justified by the ministry's defensive investigation; enable phishing-resistant MFA where feasible.
4. Do not attempt to retrieve, view or test the advertised credentials.
5. Monitor for defacement, fraudulent content and phishing campaigns impersonating ministry services.

- **Sources / Evidence:** forum post visible in the screenshot supplied on 25 September 2026; the original URL and hidden content were not accessed.

### July 13, 2024
#### 🇰🇪 Kenya - Kenya urban roads authority
- **Actor / Group:** hunters
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
- **Actor / Group:** madliberator
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
- **Actor / Group:** madliberator
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
- **Actor / Group:** lockbit3
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
- **Actor / Group:** ransomhouse
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
### 26 July 2024

#### 🇲🇦 Morocco - Arab Civil Aviation Organization (ACAO)
- **Compromise date:** Unknown - no later than 26 July 2024
- **Initial observed publication date:** 26 July 2024
- **Observed repost date:** 12 November 2024
- **Later observed publication:** 24 December 2024
- **Actor / Group:** vjvjvj
- **Claimed affiliation:** The Night Hunters - according to the observed post
- **Sector:** Aviation
- **Website:** [acao.org.ma](https://acao.org.ma)
- **Status:** Corroborated
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Victim description:** The Arab Civil Aviation Organization (ACAO) is an intergovernmental organization based in Rabat, Morocco, involved in coordinating civil aviation among Arab states.
- **Analysis:** AFRINTEL now has a more complete chronology. A 26 July 2024 publication announced an ACAO database and included a sample and an advertised archive. A 12 November 2024 publication is explicitly marked `[REPOST]`, so it is not counted as a new compromise. A further 24 December 2024 publication again claimed a breach and displayed an ACAO-related sample. Material visible in the screenshots and structured file reviewed is consistent with data linked to ACAO and the civil-aviation ecosystem, including contact, role, and professional information. AFRINTEL does not reproduce raw personal data. These elements corroborate data exposure, but do not establish the exact technical date of initial access or prove that the December publication represents a second independent intrusion.
- **Evidence qualification:** `Corroborated`. Multiple distinct publications overlap and samples consistent with ACAO are visible. No public victim or authority confirmation was identified in the material reviewed.
- **Source / provenance:** Underground publications observed and analyzed by AFRINTEL; screenshots preserved. No operational forum or download URL is published.

----------------------------
