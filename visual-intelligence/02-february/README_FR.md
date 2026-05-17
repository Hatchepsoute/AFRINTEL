![January 2026](https://img.shields.io/badge/January%202026-21%20Incidents-blue)
![February 2026](https://img.shields.io/badge/February%202026-20%20Incidents-blue)
![Data Source](https://img.shields.io/badge/Data%20Source-Leak%20Sites-black)
![AFRINTEL](https://img.shields.io/badge/Project-AFRINTEL-black)
![Africa Threat Map](https://img.shields.io/badge/Africa-Threat%20Monitoring-darkgreen)
# AFRINTEL - Graphes de renseignement sur les cybermenaces

👉🏾 [Version anglaise disponible ici](README.md)

Ces graphes sont conçus pour être intégrés dans les **rapports AFRINTEL** ou dans des **tableaux de bord statistiques CTI**.

---

# 📊 Acteurs de menace vs pays ciblés

Ce graphe montre quels **groupes ransomware ou acteurs de menace ont ciblé certains pays africains** en Janvier et Février 2026.

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

# 🌍 Carte des cybermenaces en Afrique - janvier - février 2026

Cette visualisation représente la **pression cyber observée sur le continent africain sur la période janvier-février 2026**, basée sur les incidents documentés par AFRINTEL. Elle met en évidence les **zones de concentration d’activité ransomware et d’attaques cyber**.

```mermaid
flowchart TB

classDef high fill:#ff4d4d,color:#ffffff,stroke:#990000,stroke-width:2px;
classDef medium fill:#ffa64d,color:#000000,stroke:#cc6600,stroke-width:2px;
classDef low fill:#ffe6b3,color:#000000,stroke:#cc9900,stroke-width:1px;

subgraph Afrique_du_Nord["Afrique du Nord"]
EG["🇪🇬 Égypte"]
MA["🇲🇦 Maroc"]
TN["🇹🇳 Tunisie"]
end

subgraph Afrique_de_lOuest["Afrique de l'Ouest"]
NG["🇳🇬 Nigeria"]
GH["🇬🇭 Ghana"]
SN["🇸🇳 Sénégal"]
CI["🇨🇮 Côte d’Ivoire"]
TG["🇹🇬 Togo"]
NE["🇳🇪 Niger"]
end

subgraph Afrique_de_lEst["Afrique de l'Est"]
KE["🇰🇪 Kenya"]
TZ["🇹🇿 Tanzanie"]
SO["🇸🇴 Somalie"]
end

subgraph Afrique_Australe["Afrique australe"]
ZA["🇿🇦 Afrique du Sud"]
NA["🇳🇦 Namibie"]
MU["🇲🇺 Île Maurice"]
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
class TG low;
class NE low;
class NA low;
class MU low;
```

---
👉🏾 [Explorer la cartographie des menaces](/visual-intelligence/ecosystem-map_fr.md)

*AFRINTEL - Initiative africaine de Cyber Threat Intelligence*
