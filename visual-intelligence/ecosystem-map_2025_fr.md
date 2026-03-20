# AFRINTEL 2025 - Carte de l’écosystème CTI
👉🏾 [**English version available here**](./ecosystem-map_2025.md)

Cette visualisation propose une **vue stratégique lisible** du dataset AFRINTEL 2025 en se concentrant sur :
- les **acteurs les plus actifs**
- les **pays les plus ciblés**
- les **secteurs les plus exposés**
- un sous-ensemble de **victimes représentatives**

Pour la couverture complète 2025, cette carte doit être lue avec les statistiques annuelles et le graphe dédié aux doubles revendications.

## 1. Vue stratégique de l’écosystème

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
end

subgraph Victimes_representatives
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

subgraph Pays
C1[Kenya]
C2[Afrique du Sud]
C3[Tunisie]
C4[Nigeria]
C5[Senegal]
C6[Maroc]
C7[Egypte]
end

subgraph Secteurs
S1[Energie]
S2[Gouvernement]
S3[Technologie]
S4[Sante]
S5[Finance]
S6[Logistique]
S7[Commerce]
S8[Assurance]
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

## 2. Guide de lecture

- **Rouge** : acteurs / groupes ransomware / acteurs malveillants
- **Jaune** : victimes representatives
- **Bleu** : pays
- **Vert** : secteurs

## 3. Notes d’analyse

- Le paysage 2025 est domine par **l’Egypte, l’Afrique du Sud et le Maroc**.
- **qilin**, **devman** et **incransom** figurent parmi les acteurs les plus visibles du dataset annuel.
- Les secteurs a plus forte pression incluent **technologies**, **administrations publiques**, **finance**, **education** et **sante**.
- Cette carte est volontairement **condensee pour rester lisible** et n’affiche donc pas les 149 entrees du dataset dans un seul diagramme Mermaid.
