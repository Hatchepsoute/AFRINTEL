# CTI Report - AFR-2026-04-ENA-TCHAD

## Executive summary

AFRINTEL identified and documented in October 2026 a publication attributed to the account `NormalLeVrai`, presenting the École nationale d'administration du Tchad (ENA Tchad) as a victim and announcing an email database. The observed publication is dated April 29, 2026 at 22:55. The incident is therefore assigned to April 2026; its discovery and reporting by AFRINTEL took place in October 2026.

The local analysis covered all 1,934 accessible files in the supplied corpus, totaling 213,937,991 bytes. The corpus includes 1,109 messages, 118 PDF or PDF-like files, 5,651 pages, 4 DOCX files, 4 DOC files, 85 images and 2 ZIP archives. These elements establish a coherent corpus associated with the claimed organization, but do not by themselves prove the acquisition method, the completeness of the compromise, or official confirmation by the victim.

**AFRINTEL classification:** Data Leak · Claim - Data Sample Published · high confidence for attribution of the supplied corpus, medium confidence for compromise scope · impact Level 3.

## 1. Timeline and scope

| Item | Value | Status |
|---|---|---|
| Observed incident publication | April 29, 2026, 22:55 | Observed |
| Message date range | November 21, 2025 - April 25, 2026 | Observed |
| AFRINTEL discovery and reporting | October 2026, reported October 23, 2026 | Observed |
| Claimed victim | École nationale d'administration du Tchad (ENA Tchad) | Observed |
| Country | Chad | Observed |
| Observed organizational domain | `ena.td` | Observed |
| Publishing actor/account | `NormalLeVrai` | Observed, account attribution only |

The incident remains classified as **April 2026**. This report is published in the October package to preserve late-discovery traceability without changing already closed April reports or statistics.

## 2. Preserved evidence

Original evidence and detailed outputs remain in a restricted local evidence area and are not included in the public repository. The identifiers below link the report to preserved material without publishing personal data.

| ID | Item | Result / SHA-256 | Evidentiary role |
|---|---|---|---|
| E1 | Actor publication screenshot | `b4f14cdeb57770465ef86f82627fe75de9a071bb5eca6e1050efbc25b73aa88f` | Date, title, claimed victim and publishing account |
| E2 | Message JSON export | `cc5625a58a621753fe4fb44b714a823521c89f50c3888734b2aecfc8d863b2ca` | Structure and aggregate content of 1,109 messages |
| E3 | Message CSV export | `8163b813fd5748ee68afe1c6097742f429a38ef3010a570a22b5c46ebe65264d` | Concordant tabular representation |
| E4 | File and attachment corpus | Local inventory of 1,934 files / 213,937,991 bytes | Nature, size and consistency of supplied corpus |
| E5 | Aggregate analysis report | `c68ad8062752c4c5da46a7296153e7d73fb292caf327409dc5c2fa04eef6fa02` | Reproducibility of counts and checks |

Evidence E1 proves a publication and claim; it is not official confirmation by ENA Tchad. Exports E2 to E4 are supplied analytical artifacts and do not, by themselves, prove how they were obtained.

## 3. Corpus analysis

### 3.1 Structure and coverage

- 1,109 messages analyzed; 87 distinct senders.
- Observed folders: INBOX 439, Trash 649, Sent 18, Drafts 3.
- 131 attachment references in messages, corresponding to 75 distinct names.
- 65 message groups with the same body and subject digest.
- 155 exact duplicate groups covering 487 files; this is consistent with attachment copies across folders and must not be counted as 487 unique documents.
- Recipients are primarily associated with `ena.td`, with external mail domains also observed. Individual values are not reproduced.

### 3.2 Documents actually observed

- 118 PDF or PDF-like files, totaling 5,651 pages; 116 contain an exploitable text layer and 2 are image-only PDFs.
- 5 files with atypical extensions were verified as valid PDFs and included in the PDF count.
- 4 DOCX files were inspected through local XML extraction, without enabling macros or embedded active content.
- 4 legacy DOC files underwent cautious extraction of readable strings; complete structured conversion is not guaranteed.
- 85 images were processed with local OCR; 63 produced non-empty text.
- 2 identical ZIP archives were inspected without execution; each contains one PDF named `RedefiningCapitalism.pdf`.

Observed content primarily concerns administrative correspondence, education and training, professional exchanges, events and related attachments. References to identities, contact details, accounts, administrative documents and security alerts are present; raw values are not reproduced here.

### 3.3 Sensitivity and potential impact

The observed categories could enable targeted phishing, impersonation, administrative or document fraud, social engineering against staff, students and partners, and reuse of metadata in account-takeover attempts.

No password, token or secret is published in this report. The analysis does not establish that observed credentials remain valid or that an active account was accessed using the corpus.

## 4. Analytical assessment

### Observed

- A public publication associates the account `NormalLeVrai` with a claim targeting ENA Tchad.
- A coherent local corpus contains messages and documents attributable to the `ena.td` domain.
- The above volumes and categories were calculated across all accessible files.

### Assumptions / inferences

- The corpus is likely a mailbox export or mail collection, based on its folder structure, message data and attachment copies.
- The organizational association is strongly supported by the observed domains and institutional content.

### Unknown

- Initial access method and technical operator identity.
- Completeness relative to ENA Tchad's actual environment.
- Exfiltration, persistence, reuse or sale of the data.
- Official confirmation, regulatory notification and exact operational impact.

## 5. Method and chain of handling

The examination was performed locally and read-only using SHA-256 hashing, file inventory, PDF/DOCX/HTML/TXT/JSON text extraction, archive inspection and image OCR. No binary, script, macro, embedded link, signed URL or token was executed or followed. Published results are aggregated and minimized.

Coverage is complete for inventory and hashing of the supplied corpus. Exhaustive semantic reading of every page and image is not claimed; legacy DOC files and image-only PDFs have the limitations described above. The detailed local report is preserved as `afrintel-evidence-ena-analysis.json`.

## 6. Defensive recommendations

1. Preserve mail, authentication, forwarding and administration logs for November 2025 - April 2026.
2. Reset potentially exposed secrets after validating scope and enforce MFA on sensitive accounts.
3. Search for unknown forwarding rules, delegations, sessions and OAuth applications.
4. Monitor for domain impersonation and contextual phishing campaigns.
5. Classify exposed documents, notify competent parties under the applicable framework and document remediation.

## 7. OpenCTI-ready structured data

| Field | Value |
|---|---|
| Incident ID | `AFR-2026-04-ENA-TCHAD` |
| Incident type | `Data Leak` |
| Victim | École nationale d'administration du Tchad |
| Country | Chad |
| Domain | `ena.td` |
| Actor | `NormalLeVrai` (publishing account) |
| Incident date | `2026-04-29` |
| AFRINTEL reporting date | `2026-10-23` |
| Status | `Claim - Data Sample Published` |
| Confidence | `High` for supplied-corpus attribution; `Medium` for compromise scope |
| Impact | `Level 3` |

This report does not convert the claim into official confirmation and does not alter April historical statistics.
