# AFRINTEL 2025 - double claims map

This graph focuses on the **double-claim phenomenon**, where the same victim appears under two distinct threat actors / ransomware groups during 2025.

```mermaid
flowchart LR

classDef actor fill:#ff4d4d,stroke:#990000,color:#fff
classDef victim fill:#ffcc00,stroke:#cc9900,color:#000
classDef country fill:#4da6ff,stroke:#0059b3,color:#fff

subgraph Threat_Actors
A1[devman]
A2[qilin]
A3[incransom]
A4[TheGentlemen]
A5[lockbit5]
end

subgraph Victims
V1[Hopital La Rabta]
V2[Netstar South Africa]
V3[Proplastics Limited]
end

subgraph Countries
C1[Tunisia]
C2[South Africa]
C3[Zimbabwe]
end

A1 --> V1
A2 --> V1

A1 --> V2
A3 --> V2

A4 --> V3
A5 --> V3

V1 --> C1
V2 --> C2
V3 --> C3

class A1,A2,A3,A4,A5 actor
class V1,V2,V3 victim
class C1,C2,C3 country
```

## Interpretation

- **Hopital La Rabta** was claimed by **devman** and later by **qilin**.
- **Netstar South Africa** was claimed by **devman** and later by **incransom**.
- **Proplastics Limited** was claimed by **TheGentlemen** and later by **lockbit5**.

This pattern may indicate:
- access resale
- shared broker infrastructure
- re-exploitation of already compromised organizations
- opportunistic reuse of exposed data
