# AFRINTEL Cyber Incidents - January 2024 - canonical corpus (8 records)

👉🏾 [Version française](./victims_FR.md)

> This file contains only incidents retained in canonical 2024 statistics. Historical discoveries, republications, duplicates, and unresolved-chronology cases are preserved separately at the 2024 root.


### January 2, 2024

#### 🇿🇦 South Africa - International Trade Administration Commission of South Africa (ITAC)
- **Incident date:** January 2, 2024
- **Initial publication date:** April 15, 2024
- **AFRINTEL correction date:** August 23, 2026
- **Actor / Group:** Unknown
- **Sector:** Government / Administration
- **Website:** [itac.org.za](https://itac.org.za/)
- **Status:** Victim Confirmed
- **Incident type:** Ransomware
- **Confidence level:** Very High
- **Impact level:** Level 4
- **Evidence note:** ITAC officially confirmed a ransomware attack. Possible access to and exfiltration of personal information is reported by the victim but remains qualified as possible rather than confirmed.
- **Victim Description:** ITAC is South Africa's statutory trade-administration body and processes information relating to employees, service providers, importers, exporters and other stakeholders.
- **Analysis:** ITAC states that it suffered a ransomware attack on January 2, 2024. Malicious actors encrypted files, locked users out of systems and demanded a ransom. ITAC shut down affected servers, restored backups and initiated forensic work. The official notification also states that the attacker may have accessed and possibly extracted personal information held on ITAC servers. The exact actor, initial access vector, ransom amount and confirmed exfiltration scope were not publicly established in the reviewed source. The ransomware event is therefore victim-confirmed, while data exfiltration remains possible rather than confirmed.
- **Public source:** [ITAC official notification](https://itac.org.za/notification-of-a-personal-information-security-compromise/)

----------------------------

### January 6, 2024

#### 🇦🇴 Angola - Banco Nacional de Angola (BNA)
- **Incident date:** January 6, 2024
- **Initial publication / retained source date:** January 17, 2024
- **AFRINTEL discovery date:** August 23, 2026 - retrospective audit
- **Timeline precision:** Exact incident date supported by the audit sources.
- **Actor / Group:** Unknown
- **Sector:** Finance / Banking
- **Website:** [bna.ao](https://www.bna.ao/)
- **Status:** Victim Confirmed
- **Incident type:** System Intrusion
- **Confidence level:** Very High
- **Impact level:** Level 2
- **Analysis:** BNA stated that it suffered a cyberattack on January 6, 2024. The incident was contained with no significant reported impact on infrastructure or data, and access to technology infrastructure was controlled during response. Available sources do not establish ransomware, DDoS, a data leak, or an access sale. AFRINTEL therefore retains `System Intrusion` without extrapolating the access mechanism.
- **Public sources:** [Recorded Future News](https://therecord.media/angola-national-bank-cyberattack-mitigated) | [VerAngola](https://www.verangola.net/va/en/012024/BankingInsurance/38523/National-Bank-of-Angola-targeted-by-computer-attack.htm) | [KonBriefing](https://konbriefing.com/en-topics/cyber-attacks-2024.html)

----------------------------

### January 7, 2024

#### 🇨🇲 Cameroon - University of Buea (UB)

- **Actor / Group:** cnHunter
- **Sector:** Education / University
- **Status:** Claim - Unverified
- **Website:** [ubuea.cm](https://ubuea.cm)
- **Confidence level:** Low
- **Impact level:** Level 3
- **Incident type:** Access Sale
- **Discovery date:** January 7, 2024

- **Reliability note:**
  A forum post titled "[Admin Access] ubuea.cm", published January 7, 2024 and edited the same day, claims administrative-level access to a REDCap instance hosted at redcap.ubuea.cm, referencing an upload/import handler path and an external file hosted on a file-sharing service as "proof". AFRINTEL did not access the referenced proof file or the claimed target system. The posting account, cnHunter, was subsequently permanently banned from the forum for suspected scamming, which materially reduces confidence in the underlying claim.

- **Description:**
  The University of Buea (UB) is a public university in Cameroon's South-West Region, offering programmes across faculties including science, health sciences, engineering, arts, law, and social and management sciences. REDCap instances deployed by universities are typically used to manage academic, survey and clinical or research data.

- **Analysis:**
  The post asserts administrative access to a REDCap data-collection instance associated with the university's domain and is later marked "Unlocked" in an edit, but provides no visible data sample, no independently verifiable evidence and no listed price. Combined with the subsequent permanent ban of the posting account for suspected scamming, AFRINTEL treats this as a low-confidence, unverified claim. If genuine, unauthorised administrative access to a REDCap instance could expose research, survey or academic records tied to students, staff or study participants; neither the access nor any underlying dataset is confirmed.

----------------------------

### January 10, 2024

#### 🇿🇦 South Africa - TiAuto Investments
- **Actor / Group:** lockbit3
- **Sector:** Retail / E-commerce
- **Website:** [tiautoinvestments.co.za](https://www.tiautoinvestments.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** TiAuto Investments is a prominent South African holding company specialized in the retail and wholesale distribution of wheels, tires, and automotive accessories. Founded in 2006 and headquartered in Midrand, it controls leading continental brands like Tiger Wheel & Tyre and Tyres & More.

----------------------------

### January 10, 2024

#### 🇿🇦 South Africa - Tiger Wheel & Tyre
- **Actor / Group:** lockbit3
- **Sector:** Retail / E-commerce
- **Website:** [twt.co.za](https://twt.co.za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Tiger Wheel & Tyre is a flagship subsidiary of TiAuto Investments, boasting over 50 years of operation and managing more than 100 fitment centers across South Africa and Southern Africa. It specializes in wheel alignment, balancing, and premium tire retail services.

----------------------------

### January 25, 2024

#### 🇲🇼 Malawi - Daeyang University
- **Incident date:** Unknown
- **Initial publication date:** January 25, 2024
- **AFRINTEL correction date:** August 26, 2026
- **Actor / Group:** X0Frankenstein
- **Sector:** Education / University
- **Website:** [dyuni.ac.mw](https://www.dyuni.ac.mw/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** High
- **Impact level:** Level 4
- **Claimed volume:** More than 224,000 SQL lines
- **Evidence note:** AFRINTEL reviewed the forum publication and the visible SQL sample. The claimed volume was not independently verified and must not be interpreted as 224,000 distinct students or persons.
- **Victim Description:** Daeyang University is a higher-education institution in Malawi. The reviewed sample is consistent with a university information system and includes references to Commerce and ICT programmes as well as institutional `dyuni.ac.mw` email addresses.
- **Analysis:** On January 25, 2024, X0Frankenstein published a forum claim targeting Daeyang University and displayed SQL data associated with `dyuni.ac.mw`. The actor labels the material as relating to 2023, but this does not establish the technical compromise date; AFRINTEL therefore records the incident date as unknown and uses the initial publication date for 2024 chronology. The visible sample contains student identifiers, identity and contact fields, geographic information, previous-school information, guardian/emergency-contact fields, academic department/year/semester/specialisation data, and plaintext passwords in several records. Additional SQL content is consistent with Moodle-related application data. AFRINTEL does not reproduce personal data or credentials and did not test any account. The combination of institutional-domain addresses, university-specific academic fields and SQL structure supports attribution to Daeyang University with high confidence, while the complete dataset, acquisition method, number of affected persons and initial-access vector remain unverified.
- **Risk note:** Plaintext credential exposure materially increases the risk of account takeover, credential reuse, phishing, impersonation and follow-on compromise affecting students, staff or connected services.

----------------------------

### January 29, 2024

#### 🇿🇦 South Africa - Crowe Southern Africa
- **Actor / Group:** lockbit3
- **Sector:** Professional / Business Services
- **Website:** [crowe.com/za](https://www.crowe.com/za)
- **Status:** Claim - Unverified
- **Incident type:** Ransomware
- **Confidence level:** Low
- **Impact level:** Level 2
- **Victim Description:** Crowe Southern Africa is a premier professional services firm and an independent member of the global Crowe Global network. With established offices in Johannesburg, Cape Town, and Stellenbosch, it delivers high-quality audit, tax, forensic accounting, and corporate financial advisory.

----------------------------

### January 29, 2024

#### 🇨🇲 Cameroon - Eneo Cameroon
- **Incident date:** January 29, 2024
- **Initial publication date:** February 2, 2024
- **AFRINTEL correction date:** August 23, 2026
- **Actor / Group:** Unknown
- **Sector:** Energy / Utilities
- **Website:** [eneocameroon.cm](https://eneocameroon.cm/)
- **Status:** Victim Confirmed
- **Incident type:** System Intrusion
- **Confidence level:** High
- **Impact level:** Level 4
- **Taxonomy note:** The cyberattack and operational disruption are confirmed. Reviewed victim-facing reporting does not independently establish ransomware deployment; that qualification remains secondary.
- **Victim Description:** Eneo Cameroon is the country's principal electricity utility and operates customer billing and prepaid/postpaid electricity services.
- **Analysis:** Eneo confirmed that a cyberattack beginning on January 29, 2024 significantly disrupted its computer systems. Some applications were disabled as a security precaution, and prepaid/postpaid customer operations were affected, including difficulties buying electricity units. Public reporting and later African cybercrime assessments corroborate the attack. Some CTI sources classify the event as ransomware, but the reviewed victim-facing reporting does not provide enough technical detail to independently confirm ransomware deployment. The confirmed facts are therefore the cyberattack and material operational disruption; ransomware remains a qualified secondary assessment.
- **Public sources:** [ITWeb Africa](https://itweb.africa/article/cameroons-power-utility-suffers-a-cyber-attack/8OKdWqDXArbqbznQ) | [OBS-CC](https://obs-cc.org/incident/eneo-cameroon/)

----------------------------
