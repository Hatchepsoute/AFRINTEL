![January 2026](https://img.shields.io/badge/January%202026-21%20Incidents-blue)
![February 2026](https://img.shields.io/badge/February%202026-20%20Incidents-blue)
![Data Source](https://img.shields.io/badge/Data%20Source-Leak%20Sites-black)
![AFRINTEL](https://img.shields.io/badge/Project-AFRINTEL-black)
![Africa Threat Map](https://img.shields.io/badge/Africa-Threat%20Monitoring-darkgreen)
# AFRINTEL - Visual threat intelligence graphs
👉🏾 [**French version available here**](README_FR.md)

These graphs are designed for integration into AFRINTEL reports or statistical dashboards.

---

# 📊 Threat actors vs targeted countries

This graph shows which **ransomware groups or threat actors targeted specific African countries in January and February 2026**.

```mermaid
flowchart LR

classDef actor fill:#ffe6cc,stroke:#cc7a00,stroke-width:2px;
classDef country fill:#e6f2ff,stroke:#0066cc,stroke-width:2px;

A1["thegentlemen"]:::actor
A2["tengu"]:::actor
A3["0APT"]:::actor
A4["lockbit5"]:::actor
A5["incransom"]:::actor
A6["vect"]:::actor
A7["qilin"]:::actor
A8["payload"]:::actor
A9["killsec"]:::actor
A10["Bigbrother"]:::actor
A11["Unknown"]:::actor

C1["🇿🇦 Afrique du Sud"]:::country
C2["🇪🇬 Égypte"]:::country
C3["🇰🇪 Kenya"]:::country
C4["🇳🇬 Nigeria"]:::country
C5["🇬🇭 Ghana"]:::country
C6["🇲🇦 Maroc"]:::country
C7["🇹🇳 Tunisie"]:::country
C8["🇳🇦 Namibie"]:::country
C9["🇲🇺 Maurice"]:::country
C10["🇹🇬 Togo"]:::country
C11["🇳🇪 Niger"]:::country

A1 --> C1
A1 --> C2
A1 --> C3
A1 --> C5
A1 --> C7

A2 --> C6
A2 --> C2
A2 --> C3

A3 --> C5
A3 --> C4

A4 --> C2
A4 --> C9
A4 --> C1

A5 --> C4
A5 --> C6

A6 --> C1
A7 --> C8
A8 --> C2
A9 --> C4
A10 --> C10
A11 --> C11
```

---

# 🌍 Cyber threat map of Africa - January-February 2026

This visualization represents the cyber pressure observed on the African continent during the **January-February 2026** period, based on incidents documented by AFRINTEL. It highlights **areas of concentrated ransomware activity and cyberattacks**.

```mermaid
flowchart TB

classDef high fill:#ff4d4d,color:#ffffff,stroke:#990000,stroke-width:2px;
classDef medium fill:#ffa64d,color:#000000,stroke:#cc6600,stroke-width:2px;
classDef low fill:#ffe6b3,color:#000000,stroke:#cc9900,stroke-width:1px;

subgraph North_Africa["North Africa"]
EG["🇪🇬 Egypt"]
MA["🇲🇦 Morocco"]
TN["🇹🇳 Tunisia"]
end

subgraph West_Africa["West Africa"]
NG["🇳🇬 Nigeria"]
GH["🇬🇭 Ghana"]
SN["🇸🇳 Senegal"]
CI["🇨🇮 Ivory Coast"]
TG["🇹🇬 Togo"]
NE["🇳🇪 Niger"]
end

subgraph East_Africa["East Africa"]
KE["🇰🇪 Kenya"]
TZ["🇹🇿 Tanzania"]
SO["🇸🇴 Somalia"]
end

subgraph Southern_Africa["Southern Africa"]
ZA["🇿🇦 South Africa"]
NA["🇳🇦 Namibia"]
MU["🇲🇺 Mauritius"]
MZ["🇲🇿 Mozambique"]
end

class ZA high;
class EG high;
class KE high;

class NG medium;
class GH medium;
class MA medium;

class TZ low;
class SN low;
class CI low;
class NA low;
class MU low;
```

---

**AFRINTEL** - African Threat Intelligence Initiative
