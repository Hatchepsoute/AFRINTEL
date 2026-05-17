# AFRINTEL 2025 - Carte de l’écosystème CTI
👉🏾 [**English version available here**](./ecosystem-map_2025.md)

Cette carte présente une vue lisible et synthétique du paysage des cyberattaques en Afrique pour l'année 2025, en mettant l'accent sur :
- les **groupes ransomware les plus actifs**
- les **pays les plus ciblés**
- les **secteurs les plus exposés**
- un échantillon de **victimes représentatives**

Pour le détail complet des 149 incidents, veuillez vous référer aux rapports mensuels et aux statistiques annuelles.

## 1. Carte stratégique de l'écosystème

```mermaid
flowchart LR

classDef actor fill:#ff4d4d,stroke:#990000,color:#fff
classDef victim fill:#ffcc00,stroke:#cc9900,color:#000
classDef country fill:#4da6ff,stroke:#0059b3,color:#fff
classDef sector fill:#66cc66,stroke:#2d862d,color:#000

subgraph Acteurs
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

subgraph Victimes_représentatives
    V1[KenGen]
    V2[NSSF Kenya]
    V3[Netstar]
    V4[Hôpital La Rabta]
    V5[INTELS Nigeria]
    V6[DGID Sénégal]
    V7[ASK Gras Savoye]
    V8[ELSEWEDYELECTRIC]
    V9[South African Airways]
    V10[GAGS]
    V11[INI Investments]
    V12[Princeps Credit]
    V13[BH Bank]
    V14[SYSPRO]
end

subgraph Pays
    C1[Kenya]
    C2[Afrique du Sud]
    C3[Tunisie]
    C4[Nigeria]
    C5[Sénégal]
    C6[Maroc]
    C7[Égypte]
end

subgraph Secteurs
    S1[Énergie]
    S2[Gouvernement]
    S3[Technologie]
    S4[Santé]
    S5[Finance]
    S6[Logistique]
    S7[Transport]
    S8[Assurance]
end

%% Liens acteurs -> victimes
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

%% Liens victimes -> pays
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

%% Liens pays -> secteurs
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

## 2. Guide de lecture

- 🔴 **Acteurs** : groupes ransomware ou cybercriminels
- 🟡 **Victimes** : organisations représentatives touchées
- 🔵 **Pays** : localisation géographique des victimes
- 🟢 **Secteurs** : domaines d'activité impactés

## 3. Remarques analytiques

- L'année 2025 est marquée par la prédominance de l'**Égypte**, de l'**Afrique du Sud** et du **Maroc** comme cibles principales.
- Les groupes **Qilin, Devman et Incransom** sont les plus prolifiques.
- Les secteurs **technologique, gouvernemental, financier, logistique et sanitaire** sont sous forte pression.
- Cette carte est une **synthèse visuelle** ; elle ne prétend pas à l'exhaustivité. Les doubles revendications (ex. Hôpital La Rabta) sont symbolisées par des liens multiples.

Pour une analyse détaillée, consulter les rapports mensuels et les statistiques annuelles.
