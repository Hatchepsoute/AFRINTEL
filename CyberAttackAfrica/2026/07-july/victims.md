

### 21 July 2026
#### 🇹🇳 Tunisia - Ministry of Justice
- **Actor / Group:** R3V4ULT
- **Sector:** Government / Justice / Public administration
- **Website:** justice.gov.tn
- **Status:** Data leak
- **Description:**

The Tunisian Ministry of Justice is the public administration responsible for the judicial sector in Tunisia. Its activities include the administration of courts, correctional facilities and judicial services.

- **Analysis:**

The actor R3V4ULT published an initial dataset on a cybercriminal forum, presenting it as originating from the Tunisian Ministry of Justice. The post uses a hacktivist narrative related to water and electricity disruptions in Tunisia, contains two download links and announces possible additional disclosures.

The analysed CSV file contains 6,599 unique contact records, structured into four fields: first name, surname, email address and domain. Of these records, 6,593 addresses use the institutional domains justice.gov.tn, mail.justice.gov.tn, e-justice.tn or mail.e-justice.tn. No passwords, hashes, authentication tokens or email content were identified.

The sample also includes a three-page scanned administrative document dated 23 October 2024, containing internal references, budget lines, financial amounts, stamps and signatures. The visible expenses relate to water, electricity, gas, telecommunications, rent, transportation, maintenance, administrative supplies and certain medical expenses associated with detainees. A fuel supply request is also visible in the forum publication.

The observed files represent an initial sample, not a complete release. They do not confirm access to email accounts, compromised credentials or the intrusion vector. The exposed information could nevertheless support targeted phishing, impersonation of public officials, mapping of judicial departments and fraud using credible administrative references.

As an Ethiopian proverb states, “When spider webs unite, they can tie up a lion.” The Ministry should strengthen multifactor authentication, monitor abnormal use of institutional accounts and investigate the source of the exposure.

As the government sector remains particularly exposed to data leaks in Africa, other public institutions should treat this publication as a sector-wide warning, review exposed directories, notify their SOC teams and prepare employees for phishing campaigns that may reuse the leaked information.

---
### 24 July 2026
#### 🇲🇦 Morocco - Distamed

- **Actor / Group :** anisanas2
- **Sector:** Healthcare / Medical equipment
- **Website:** [distamed.ma](https://distamed.ma)
- **Status:** Claim - Data Sample Published

- **Description:**

Distamed is a Moroccan company specialising in medical equipment and digital healthcare solutions. Its activities include cardiology, pulmonology, neurology, sleep diagnostics, rehabilitation and medical imaging.

- **Analysis:**

The actor anisanas2 claims to have extracted Distamed’s data and is offering the company’s internal archives for sale for **USD 5,000**. The publication also announces the future release of the complete dataset.

The reviewed files contain **8,823 patient rows**, including 8,776 distinct rows, with names, dates of birth, ages, national identity numbers, telephone numbers, cities, insurance details and visit dates. They also include **8,147 client entries**, **1,195 entries presented as a doctor list**, **1,550 contracts**, **1,455 invoices** and **3,251 payments**.

The observed documents also include medical reports containing pathologies, examination results and clinical conclusions. Some entries refer to Moroccan public and military hospitals.

The consistency between the administrative, medical and financial data confirms a significant exposure. However, the claim that the complete archive dates back to 2013 is not demonstrated by the reviewed material, whose observed dates mainly cover **2018 to 2026**.

This exposure creates high risks of medical confidentiality breaches, identity theft, document fraud, invoice fraud and targeted phishing against patients, doctors and partner institutions.

- **Recommendations:**

1. Investigate unusual access, exports and download activity, then immediately revoke potentially compromised accounts, sessions and keys.
2. Notify affected individuals and institutions, then strengthen monitoring for identity fraud, invoice fraud and fraudulent changes to banking details.
