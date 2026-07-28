# AFRINTEL - Threat actor intelligence
## Most active actors - May 2026

```mermaid
pie showData
    title Most active threat actors - May 2026
    "Databasehooligan (8)" : 8
    "404Crew Cyber Team (5)" : 5
    "TheGentlemen (4)" : 4
    "NightSpire (3)" : 3
    "INT3X (2)" : 2
    "Keymous (2)" : 2
    "cc5ab (2)" : 2
    "NullSec Nigeria (2)" : 2
    "anisanas2 (2)" : 2
    "Others (27)" : 27
```

## Actor profiles

### Databasehooligan, data broker (8 victims)

```mermaid
flowchart LR
DBH["Databasehooligan"] --> TN["🇹🇳 Keejob / MyTelnet / OptionCarriere.tn"]
DBH --> ZA["🇿🇦 Telkom SA / Wanderers Club / MIDAS SA"]
DBH --> EG["🇪🇬 Wuzzuf.net"]
DBH --> DZ["🇩🇿 OGEBC Algeria"]
```

**Profile:** Dominant data broker. Sells structured CRM and consumer databases. Price range: $900-$1,400. Four countries in May 2026. Systematic exploitation of shared platform vulnerabilities or CRM software.

---

### TheGentlemen, ransomware (4 victims)

```mermaid
flowchart LR
GENT["TheGentlemen"] --> EG["🇪🇬 Egypt (1)"]
GENT --> TN["🇹🇳 Tunisia (1)"]
GENT --> GH["🇬🇭 Ghana (1)"]
GENT --> CI["🇨🇮 Ivory Coast (1)"]
```

**Profile:** Ransomware group with notable geographic reach. Hit 4 African countries in a single month targeting industry, automotive, and food sectors.

---

### NightSpire, ransomware (3 victims, Egypt)

```mermaid
flowchart LR
NIGHT["NightSpire"] --> PJ["Papa John's Egypt"]
NIGHT --> RW["Rawaj Consumer Finance"]
NIGHT --> BI["B Investments"]
```

**Profile:** Emerging ransomware group. Concentrated campaign against Egyptian food services and finance sector. Leading ransomware group for May 2026 by African victim count.

---

### 404Crew Cyber Team, data leak coalition (4+ victims, South Africa)

```mermaid
flowchart LR
C404["404Crew CT\n+ NullSec Nigeria\n+ Infernalis"] --> EM["Ephraim Mogale Municipality"]
C404 --> DCS["DCS South Africa"]
C404 --> BS["Bellavista School"]
C404 --> SITA["SITA"]
C404 --> SARS["SARS"]
C404 --> MEV["mevent."]
C404 --> CERVI["CERVI"]
C404 --> SRW["Sheriff Randburg West"]
```

**Profile:** Multi-actor coalition running OpSouthAfrica campaign. Political motivation (xenophobia grievances). Targets South African public institutions combining data leak publication with political messaging.

---

### anisanas2, data leak and data sale (2 victims, Morocco)

```mermaid
flowchart LR
ANI["anisanas2"] --> RADEM["🇲🇦 RADEM Meknès (water and electricity utility)"]
ANI --> BUNDLE["🇲🇦 Multi-entity bundle (Ministry of Justice, NARSA, OFPPT, logistics, insurance)"]
```

**Profile:** Threat actor active on Darkforums. Conducted two large-scale operations targeting Moroccan public infrastructure and institutions in May 2026. The RADEM Meknès breach exposed approximately 1.1 million documents from a critical utility. The multi-entity bundle (attributed to anisanas2) covered over 12 million rows across government, transport, and vocational training sectors, offered at 5,500 USD globally. Continuation of a campaign that began in April 2026.

---

### AuditTeam, ransomware and double extortion (1 victim, Senegal)

**Profile:** Ransomware group. Attacked Tresor Public du Senegal with confirmed double extortion. Most impactful government ransomware incident of May 2026: ~1.66M records exfiltrated (national taxpayer registry, payroll, payment orders with NINEA identifiers and banking coordinates).

---

## Actor activity matrix

| Actor | Type | Ransomware | Data Leak | Access Sale | Countries |
|---|:---:|:---:|:---:|:---:|:---|
| Databasehooligan | Data broker | | 8 | | TN, ZA, EG, DZ |
| TheGentlemen | Ransomware | 4 | | | EG, TN, GH, CI |
| 404Crew CT | Coalition | | 4+ | | ZA |
| NightSpire | Ransomware | 3 | | | EG |
| INT3X | Data leak | | 2 | | EG |
| Keymous | Access/Leak | | 1 | 1 | Multi-country |
| cc5ab | Data leak | | 2 | | EG, KE |
| NullSec Nigeria | Coalition | | 2+ | | ZA |
| anisanas2 | Data leak/sale | | 2 | | MA |
| AuditTeam | Ransomware | 1 | | | SN |
| Kampuchean | Data broker | | 1 | | TZ |
