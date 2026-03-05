![Visualization](https://img.shields.io/badge/Visualization-Map-blue)
![Data Source](https://img.shields.io/badge/Data%20Source-Leak%20Sites-black)
![Period](https://img.shields.io/badge/Period-2026--01%20to%202026--02-informational)
![Coverage](https://img.shields.io/badge/Coverage-41%20Incidents-brightgreen)
![Countries](https://img.shields.io/badge/Countries-18-yellow)
![Threat Actors](https://img.shields.io/badge/Threat%20Actors-12-orange)
![Sectors](https://img.shields.io/badge/Sectors-13-purple)
## 🔗 Cartographie des acteurs de menace - Janvier & Février 2026
👉🏾 [English version](/visual-intelligence/ecosystem-map.md)

Ce graphique illustre les connexions entre les groupes ransomware et leurs cibles à travers l'Afrique, basé sur 41 incidents documentés dans 18 pays.

```mermaid
flowchart LR

%% ===== STYLES =====
classDef actor fill:#ffe6cc,stroke:#cc7a00,stroke-width:2px;
classDef country fill:#e8ffe6,stroke:#2b8a3e,stroke-width:2px;
classDef sector fill:#f3e6ff,stroke:#6f42c1,stroke-width:2px;

%% ===== ACTEURS =====
A1["thegentlemen"]:::actor
A2["tengu"]:::actor
A3["0APT"]:::actor
A4["lockbit5"]:::actor
A5["The Green Blood Group"]:::actor
A6["incransom"]:::actor
A7["qilin"]:::actor
A8["vect"]:::actor
A9["payload"]:::actor
A10["apt73/bashe"]:::actor
A11["killsec"]:::actor
A12["Bigbrother"]:::actor

%% ===== PAYS =====
C1["🇸🇳 Sénégal"]:::country
C2["🇿🇦 Afrique du Sud"]:::country
C3["🇰🇪 Kenya"]:::country
C4["🇪🇬 Égypte"]:::country
C5["🇳🇬 Nigeria"]:::country
C6["🇬🇭 Ghana"]:::country
C7["🇲🇦 Maroc"]:::country
C8["🇹🇳 Tunisie"]:::country
C9["🇲🇺 Maurice"]:::country
C10["🇹🇿 Tanzanie"]:::country
C11["🇸🇴 Somalie"]:::country
C12["🇳🇦 Namibie"]:::country
C13["🇲🇿 Mozambique"]:::country
C14["🇨🇮 Côte d'Ivoire"]:::country
C15["🇸🇩 Soudan"]:::country
C16["🇹🇬 Togo"]:::country
C17["🇳🇪 Niger"]:::country
C18["🇩🇿 Algérie"]:::country

%% ===== SECTEURS =====
S1["Gouvernement"]:::sector
S2["Aviation"]:::sector
S3["Énergie"]:::sector
S4["Finance"]:::sector
S5["Média"]:::sector
S6["Hôtellerie"]:::sector
S7["Admin. publique"]:::sector
S8["Commerce"]:::sector
S9["Conseil IT"]:::sector
S10["Bâtiment"]:::sector
S11["Tourisme"]:::sector
S12["Mines"]:::sector
S13["Agroalimentaire"]:::sector

%% ===== RELATIONS ACTEURS → PAYS =====
A1 --> C2
A1 --> C3
A1 --> C4
A1 --> C6
A1 --> C9

A2 --> C1
A2 --> C4
A2 --> C3
A2 --> C7
A2 --> C8
A2 --> C11
A2 --> C13
A2 --> C18

A3 --> C2
A3 --> C3
A3 --> C6
A3 --> C10
A3 --> C11

A4 --> C4
A4 --> C7
A4 --> C8
A4 --> C9

A5 --> C1

A6 --> C5
A6 --> C13
A6 --> C14

A7 --> C12

A8 --> C2

A9 --> C4

A10 --> C15

A11 --> C5

A12 --> C16

%% ===== RELATIONS PAYS → SECTEURS =====
C1 --> S1
C2 --> S3
C2 --> S7
C2 --> S11
C3 --> S4
C3 --> S7
C3 --> S12
C4 --> S1
C4 --> S2
C4 --> S4
C4 --> S11
C5 --> S3
C5 --> S4
C6 --> S5
C6 --> S7
C7 --> S2
C7 --> S3
C7 --> S10
C8 --> S4
C8 --> S9
C8 --> S13
C9 --> S4
C9 --> S6
C10 --> S4
C10 --> S13
C11 --> S2
C12 --> S8
C13 --> S3
C14 --> S2
C15 --> S9
C16 --> S1
C17 --> S7
C18 --> S11
