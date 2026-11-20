![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# List of African cyberattack victims in November 2026 (2 records)

👉🏾 [**French version available here**](./victims_FR.md)

## November 2026

**Monthly tracking status: Draft** - initial corpus of two records published or observed in November 2026. Monthly statistics are not generated at this stage.

### November 16, 2026

#### 🇪🇬 Egypt - Egyptian Drug Store (`egyptiandrugstore.com`) [Data Leak]
- **Initial publication date:** November 16, 2026 at 11:30
- **Displayed export date:** November 2026
- **Incident date:** Not established
- **Actor / Group:** Sophia
- **Sector:** Retail / Pharmacy / E-commerce
- **Associated website:** [egyptiandrugstore.com](http://egyptiandrugstore.com/)
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Offer nature:** Alleged sale of a database; visible sample, access to the complete corpus unverified
- **Claimed volume:** 10,000 records, unverified
- **Confidence level:** Medium for the existence of the publication, schema consistency and contextual association with the domain; technical provenance and completeness remain uncorroborated
- **Impact level:** Level 4
- **Source type:** Underground forum publication and visual capture of a database sample

- **Victim description:** Egyptian Drug Store is presented in the publication as an online store associated with pharmacy or health-product distribution activity. The domain displayed in the publication is `egyptiandrugstore.com`.

- **Analysis:** The November 16, 2026 publication is placed in a selling category and presents an alleged “10K Full Database”. It explicitly tells buyers to send a message to purchase the database and then displays a “Samples” section containing a structured excerpt. It is therefore an alleged database-sale offer accompanied by a visible sample. The claimed volume of 10,000 records, database completeness and any actual transfer of the corpus to a buyer remain unverified.

  The capture exposes several tabular representations consistent with an e-commerce database:

  1. **Customer table:** customer and store identifiers, first and last names, email address, telephone, fax, associated address, customer group, status and approval;
  2. **Account and session fields:** columns named `password`, `salt`, `token`, cart, wishlist, newsletter subscription and IP address; the capture does not establish the hashing algorithm, current validity of the values or whether any password is stored in cleartext;
  3. **Address table:** customer and address identifiers, company, tax identifier, address lines, city, postcode, country and administrative zone;
  4. **Order table:** order and invoice identifiers, customer information, billing and shipping details, payment method and code, amount, currency, status, IP address, user agent and preferred language.

  The combination of `customer_group_id`, `cart`, `wishlist`, `order_status_id`, `payment_method`, `payment_code`, `shipping_method` and `currency_code` is compatible with an OpenCart-like e-commerce application. This is a structural inference, not proof of the platform used or the technical origin of the data.

  The visible data appears to cover multiple countries and currencies, which may reflect an international customer base or a historical commercial export. The capture does not allow reliable counting of unique customers, orders, countries, transactions or affected persons. No reliable financial total can be calculated from the image.

  **Observed:** Publication timestamped November 16, 2026 at 11:30; selling category displayed; `egyptiandrugstore.com` shown; export date shown as November 2026; invitation to contact the seller to purchase a database advertised at 10,000 records; “Samples” section showing customer, address and order tables; columns relating to personal data, accounts, orders, payments and technical information.

  **Assumption:** The presence of the domain, store name and a coherent e-commerce schema makes contextual association of the sample with Egyptian Drug Store plausible. This consistency does not confirm that the files came from the company’s servers, that they were acquired by the publication author or that they represent the full production database.

  **Unknown:** Source system, access vector and date, acquisition method, actual line and person counts, account uniqueness, password or token validity, IP-address status, export integrity, covered period, presence of complete payment data, exfiltration, company confirmation and notification to a competent authority.

- **Analysis scope and limitations:** The analysis is structural and preliminary, based on a visual capture; the original CSV and alleged database were not available. Visible personal data, addresses, identifiers, authentication values, tokens and IP addresses were not transcribed, tested or added to the repository. The capture does not support exhaustive analysis, deduplication, reliable counting or validation of the claimed 10,000 records.
- **Risk assessment:** If authentic, the sample could facilitate credential stuffing, account takeover, targeted phishing, order and payment fraud, customer impersonation, delivery fraud, misuse of tax information and correlation of personal and technical data. `password`, `salt` and `token` fields require controlled operator-side verification and rotation, without assuming that an exploitable value remains active.
- **SOC / CTI recommendations:** Preserve web, application, database, IAM, administration and order-system logs covering at least the period preceding November 16; investigate bulk exports, unusual queries, privileged access and outbound transfers; reset secrets and sessions after scoping; review payment, order, delivery and customer-account functions; monitor phishing, account takeover and order fraud; notify relevant parties under applicable regulations.
- **Sources / Evidence:** Underground forum publication and visual capture supplied on November 17, 2026; domain and store name visible in the publication. No criminal link, identifier, address, secret, token or raw value is reproduced in the repository.

### November 17, 2026

#### 🇲🇦 Morocco - Ard Essalam 2 School, Salé [Data Leak]
- **Initial publication date:** November 17, 2026
- **Incident date:** Not established
- **Actor / Group:** Blacknet00
- **Sector:** Education / Private education
- **Claimed administrative scope:** Regional Academy of Education and Training of Rabat-Salé-Kénitra
- **Institution identified in the samples:** Ard Essalam 2, Salé
- **Status:** Claim - Data Sample Published
- **Incident type:** Data Leak
- **Confidence level:** Medium for the existence of the publication and the contextual association of the samples with Ard Essalam 2; file provenance and compromise remain uncorroborated
- **Impact level:** Level 4
- **Source type:** Underground forum publication and five local JPEG samples examined read-only

- **Victim description:** Ard Essalam 2 is a private school located in Salé. The visible certificates carry the header of the Regional Academy of Education and Training of Rabat-Salé-Kénitra and the Salé Provincial Directorate. Public sources also associate “مؤسسة أرض السلام 2” with Salé, but they do not confirm the incident.

- **Analysis:** The publication observed on November 17, 2026 claims to target the Rabat-Salé-Kénitra education ecosystem and presents documents attributed to that environment. Visual analysis of the five supplied JPEGs identifies school certificates presented as official for the 2026-2027 school year, a child photograph and a partial table extract containing information relating to teachers or staff. Visible categories include names, dates of birth, school identifiers, education levels, subjects taught and contact details. Individual values are not reproduced.

  The publication also claims the existence of birth-certificate extracts containing family information and national identification numbers. These elements were not visible in the five examined samples and remain claims only. The presence of an Academy and Provincial Directorate header on the certificates does not demonstrate that those administrations' systems were compromised. It also does not establish that Ard Essalam 2 was the source system for the files.

  **Observed:** Publication dated November 17, 2026; five local JPEG files examined read-only; school certificates, a child photograph and a partial table visible; contextual association of the certificates with Ard Essalam 2, Salé and the Rabat-Salé-Kénitra Academy.

  **Assumption:** Consistency between the school name visible on the certificates, the Salé location and the administrative references makes association of the samples with Ard Essalam 2 plausible. This consistency does not confirm file provenance, acquisition method or compromise of the school or the Academy.

  **Unknown:** Access date and vector, source system, independent authenticity of the documents, number of affected persons, total volume, completeness, actual presence of the claimed birth-certificate extracts, author's identity, exfiltration and confirmation by the school, the Academy or a competent authority.

- **Analysis scope and limitations:** All five supplied JPEGs were visually reviewed read-only. Their combined size is 446,573 bytes. No native file, export, database or complete corpus was supplied. Visible personal data, names, identifiers, contact details and photographs are not reproduced in the repository. The analysis is limited to elements visible in the supplied samples.
- **Risk assessment:** If the documents are authentic and originate from unauthorised access, potential risks include identity theft, targeted phishing, document fraud, exploitation of children's data, privacy harm to families and impersonation of staff members. These risks do not confirm the incident.
- **SOC / CTI recommendations:** Preserve IAM, school-application, database, administrative-workstation and storage logs; investigate bulk exports, privileged access and outbound transfers; revoke potentially exposed sessions and secrets; review sharing rules and third-party accounts; strengthen MFA, segmentation and monitoring of access to student data; prepare regulatory notifications under the applicable process.
- **Sources / Evidence:** Underground forum publication and five locally supplied JPEGs; [public listing for Ard Essalam 2 School in Salé](https://www.schoolandcollegelistings.com/MA/Sal%C3%A9/277600618767530/Etablissement-Ard-Essalam-2); [public document mentioning مؤسسة أرض السلام 2 in Salé](https://s4a988bdcec69bd04.jimcontent.com/download/version/1742606078/module/14453774392/name/classement%20final%20des%20arts%20martiaux%20scolaire%202025.pdf). Local files and personal data remain outside the repository.

