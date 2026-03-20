# AFRINTEL 2025 — CTI Ecosystem Map

This visualization provides a **readable strategic map** of the 2025 AFRINTEL dataset by focusing on:
- the **most active threat actors**
- the **most targeted countries**
- the **most exposed sectors**
- a limited set of **representative victims**

For the full 2025 dataset, this map should be read together with the yearly statistics and the dedicated double-claims graph.

## 1. Strategic ecosystem view

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
end

subgraph Representative_Victims
V1[KenGen]
V2[NSSF Kenya]
V3[Netstar]
V4[Hopital La Rabta]
V5[INTELS Nigeria]
V6[DGID Senegal]
V7[ASK Gras Savoye]
V8[ELSEWEDYELECTRIC]
V9[South African Airways]
V10[MeamarGroup]
V11[Leadway Assurance]
V12[Marjane]
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
S7[Retail]
S8[Insurance]
S9[Education]
end

A1 --> V1
A2 --> V2
A2 --> V3
A1 --> V4
A8 --> V5
A7 --> V8
A3 --> V9
A6 --> V7
A5 --> V10
A10 --> V4
A1 --> V11
A7 --> V12
A9 --> V4

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
V11 --> C4
V12 --> C6

C1 --> S1
C1 --> S2
C2 --> S3
C2 --> S6
C3 --> S4
C4 --> S5
C5 --> S2
C6 --> S8
C6 --> S7
C7 --> S3
C7 --> S5
C7 --> S9

class A1,A2,A3,A4,A5,A6,A7,A8,A9,A10 actor
class V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12 victim
class C1,C2,C3,C4,C5,C6,C7 country
class S1,S2,S3,S4,S5,S6,S7,S8,S9 sector
```

## 2. Reading guide

- **Red nodes**: threat actors / ransomware groups / malicious actors
- **Yellow nodes**: representative victims
- **Blue nodes**: countries
- **Green nodes**: sectors

## 3. Analytical notes

- The 2025 African threat landscape is dominated by **Egypt, South Africa, and Morocco**.
- **qilin**, **devman**, and **incransom** are among the most visible actors in the yearly dataset.
- High-pressure sectors include **technology**, **public administration**, **finance**, **education**, and **healthcare**.
- This map is intentionally **condensed for readability** and does not attempt to display all 149 victim entries in one Mermaid diagram.
