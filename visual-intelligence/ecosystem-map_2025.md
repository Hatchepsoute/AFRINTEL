# AFRINTEL 2025 – CTI Ecosystem strategic map
👉🏾 [**French version available here**](./ecosystem-map_2025_fr.md)

This map provides a **readable and synthetic view** of the cyberattack landscape in Africa for the year 2025, focusing on:
- the **most active ransomware groups**
- the **most targeted countries**
- the **most exposed sectors**
- a sample of **representative victims**

For the full 2025 dataset, this map should be read together with the yearly statistics and the dedicated double-claims graph.

## 1. Strategic ecosystem map

```mermaid
flowchart LR

classDef actor fill:#ff4d4d,stroke:#990000,color:#fff
classDef victim fill:#ffcc00,stroke:#cc9900,color:#000
classDef country fill:#4da6ff,stroke:#0059b3,color:#fff
classDef sector fill:#66cc66,stroke:#2d862d,color:#000

subgraph Actors
    A1[qilin]
    A2[devman]
    A3[incransom]
    A4[funksec]
    A5[nightspire]
    A6[killsec]
    A7[clop]
    A8[ransomhub]
    A9[warlock]
    A10[Dark 07x Team]
    A11[BlackShrantac]
end

subgraph Representative_Victims
    V1[KenGen]
    V2[NSSF Kenya]
    V3[Netstar]
    V4[La Rabta Hospital]
    V5[INTELS Nigeria]
    V6[DGID Senegal]
    V7[ASK Gras Savoye]
    V8[ELSEWEDYELECTRIC]
    V9[South African Airways]
    V10[GAGS]
    V11[INI Investments]
    V12[Princeps Credit]
    V13[BH Bank]
    V14[SYSPRO]
end

subgraph Countries
    C1[Kenya]
    C2[South Africa]
    C3[Tunisia]
    C4[Nigeria]
    C5[Senegal]
    C6[Morocco]
    C7[Egypt]
end

subgraph Sectors
    S1[Energy]
    S2[Government]
    S3[Technology]
    S4[Healthcare]
    S5[Finance]
    S6[Logistics]
    S7[Transport]
    S8[Insurance]
end

%% Actor -> Victim links
A1 --> V1
A2 --> V2
A2 --> V3
A2 --> V4
A1 --> V4
A8 --> V5
A11 --> V6
A8 --> V7
A7 --> V8
A3 --> V9
A4 --> V10
A5 --> V11
A6 --> V12
A10 --> V13
A9 --> V14

%% Victim -> Country links
V1 --> C1
V2 --> C1
V3 --> C2
V4 --> C3
V5 --> C4
V6 --> C5
V7 --> C6
V8 --> C7
V9 --> C2
V10 --> C7
V11 --> C7
V12 --> C4
V13 --> C3
V14 --> C2

%% Country -> Sector links
C1 --> S1
C1 --> S2
C2 --> S3
C2 --> S7
C3 --> S4
C3 --> S5
C4 --> S6
C4 --> S5
C5 --> S2
C6 --> S8
C7 --> S3
C7 --> S5
C7 --> S2

class A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11 actor
class V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14 victim
class C1,C2,C3,C4,C5,C6,C7 country
class S1,S2,S3,S4,S5,S6,S7,S8 sector
```

## 2. Reading guide

- 🔴 **Actors**: ransomware groups or cybercriminals
- 🟡 **Victims**: representative affected organizations
- 🔵 **Countries**: geographical location of victims
- 🟢 **Sectors**: impacted industries


## 3. Analytical notes

- The year 2025 is marked by the predominance of **Egypt, South Africa, and Morocco** as primary targets.
- The groups **qilin, devman**, and incransom are the most prolific.
- The **technology, government, finance, logistics, and healthcare** sectors are under high pressure.
- This map is a **visual synthesis**; it does not claim to be exhaustive. Double claims (e.g., La Rabta Hospital) are symbolized by multiple links.

For detailed analysis, please consult the monthly reports and annual statistics.
