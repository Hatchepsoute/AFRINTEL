# AFRINTEL - Comparative Cyber Threat Analysis  
👉🏾 [Version française disponible ici](README_FR.md)

## March vs April 2026 (Africa)

This report provides a comparative Cyber Threat Intelligence (CTI) analysis of cyber incidents affecting Africa during March and April 2026.

---

# 📊 General Comparison

| Indicator | March 2026 | April 2026 |
|---|---|---|
| Incidents | 48 | 60 |
| Countries affected | 14 | 16 |
| Threat actors | 24+ | 30+ |
| Ransomware | 22 | 20 |
| Data leaks / Access sales | 26 | 40 |
| Government-related incidents | High | Very High |
| Identity / KYC leaks | Moderate | Massive increase |

---

# 🌍 Geographic Distribution Comparison

```mermaid
flowchart LR

MAR["March 2026
48 incidents"]
APR["April 2026
60 incidents"]

MA["🇲🇦 Morocco"]
EG["🇪🇬 Egypt"]
ZA["🇿🇦 South Africa"]
DZ["🇩🇿 Algeria"]
TN["🇹🇳 Tunisia"]
NG["🇳🇬 Nigeria"]
KE["🇰🇪 Kenya"]

MAR --> MA
MAR --> EG
MAR --> ZA
MAR --> NG

APR --> MA
APR --> EG
APR --> ZA
APR --> DZ
APR --> TN
APR --> KE
APR --> NG
```

---

# 📈 Incident Volume by Month

```mermaid
xychart-beta
title "Cyber incidents by month"
x-axis ["March","April"]
y-axis "Incidents" 0 --> 70
bar [48,60]
```

---

# 🎯 Threat Actor Activity

```mermaid
flowchart TB

classDef high fill:#ff4d4d,color:#ffffff
classDef medium fill:#ffa64d,color:#000000
classDef low fill:#ffe6b3,color:#000000

GRUB["Grubder"]:::high
PAY["Payload"]:::high
APT["APT73/BASHE"]:::medium
GENT["TheGentlemen"]:::medium
KRY["Krybit"]:::low
ANI["Anisanas2"]:::low
RIH["Rihana"]:::low
WH["wh6ami"]:::low
```

## Key observations

- Grubder became the dominant African data broker actor in April.
- Payload intensified ransomware campaigns against Egyptian strategic sectors.
- Government access sales sharply increased.
- Identity-centric cybercrime exploded across Morocco and North Africa.

---

# 🏭 Comparison of Targeted Sectors

```mermaid
pie
title Evolution of targeted sectors
"Government / Administration" : 15
"Education / Universities" : 8
"Healthcare / Medical" : 4
"Finance / Banking" : 4
"Sports / Federations" : 4
"Oil & Energy" : 3
"E-commerce / Retail" : 3
"Others" : 19
```

---

# 🔥 Major Incidents

## March 2026

- Smarteez / L’Oréal Morocco supply-chain exposure
- AuditTeam Senegal ransomware operations
- Multiple African ransomware waves targeting finance and industry

## April 2026

- CNOPS Morocco massive healthcare leak
- Royal Palace staff database exposure
- Kenya Airports Authority claimed 2 TB compromise
- CNSS Benin mailbox leak
- Pick n Pay ASAP / Bottles.com banking data exposure

---

# 🧠 Strategic CTI Findings

1. Industrialization of African data brokers accelerated significantly.
2. Government systems became primary monetization targets.
3. Identity-document trading became a dominant underground business model.
4. Healthcare and educational ecosystems remain critically exposed.

---

# 🔮 Threat Outlook

Priority targets expected in coming months:

- Government institutions
- Healthcare ecosystems
- Financial infrastructures
- Educational platforms
- E-commerce environments

Priority countries:

🇲🇦 Morocco • 🇪🇬 Egypt • 🇿🇦 South Africa • 🇳🇬 Nigeria • 🇩🇿 Algeria

---

# AFRINTEL

African Threat Intelligence Initiative  
TLP:CLEAR – Public distribution
