# AFRINTEL -- Statistiques par acteur et par pays (Février 2026)

Ce dossier contient les statistiques détaillées des incidents ransomware recensés en Afrique pour le mois de février 2026.

---

## 📊 Vue d'ensemble

| Métrique | Valeur |
|----------|--------|
| **Total des incidents** | 20 |
| **Pays touchés** | 13 |
| **Acteurs de menace actifs** | 10 |
| **Volume total de données exfiltrées** | ~147 To |

---

## 🗺️ Répartition par pays

| Pays | Nombre d'incidents | Principaux acteurs |
|------|-------------------|---------------------|
| 🇿🇦 **Afrique du Sud** | 3 | `thegentlemen` (2), `Lockbit5` (1), `vect` (1) |
| 🇪🇬 **Égypte** | 3 | `thegentlemen` (1), `lockbit5` (1), `payload` (1) |
| 🇳🇬 **Nigeria** | 2 | `killsec` (1), `incransom` (1) |
| 🇬🇭 **Ghana** | 2 | `0APT` (1), `thegentlemen` (1) |
| 🇸🇳 **Sénégal** | 1 | `The Green Blood Group` (1) ⚠️ **139 To** |
| 🇸🇴 **Somalie** | 1 | `0APT` (1) |
| 🇹🇿 **Tanzanie** | 1 | `0APT` (1) |
| 🇰🇪 **Kenya** | 1 | `thegentlemen` (1) |
| 🇲🇺 **Maurice** | 1 | `lockbit5` (1) |
| 🇹🇳 **Tunisie** | 1 | `thegentlemen` (1) |
| 🇸🇩 **Soudan** | 1 | `apt73/bashe` (1) |
| 🇨🇮 **Côte d'Ivoire** | 1 | `incransom` (1) |
| 🇲🇦 **Maroc** | 1 | `tengu` (1) |
| 🇳🇦 **Namibie** | 1 | `qilin` (1) |

---

## 🎯 Répartition par acteur de menace

| Acteur | Incidents | Pays ciblés | Volume total |
|--------|-----------|-------------|--------------|
| `thegentlemen` | **5** | Kenya, Ghana, Égypte, Afrique du Sud (×2), Tunisie | ~? |
| `0APT` | **3** | Somalie, Ghana, Tanzanie | **~7 To** |
| `lockbit5` | **2** | Maurice, Égypte | ~? |
| `incransom` | **2** | Nigeria, Côte d'Ivoire | ~? |
| `The Green Blood Group` | **1** | Sénégal | **139 To** ⚠️ |
| `killsec` | **1** | Nigeria | ~? |
| `vect` | **1** | Afrique du Sud | 151 Go |
| `qilin` | **1** | Namibie | ~? |
| `payload` | **1** | Égypte | ~? |
| `tengu` | **1** | Maroc | ~? |
| `apt73/bashe` | **1** | Soudan | ~? |

---

## 📈 Analyse par secteur

| Secteur | Incidents | Acteurs principaux |
|---------|-----------|---------------------|
| **Gouvernement** | 3 | `The Green Blood Group`, `lockbit5`, `thegentlemen` |
| **Aviation** | 3 | `0APT` (2), `thegentlemen`, `incransom` |
| **Énergie** | 2 | `incransom`, `vect` |
| **Banque/Fintech** | 2 | `thegentlemen`, `killsec` |
| **Média** | 1 | `0APT` |
| **Juridique** | 1 | `0APT` |
| **Hôtellerie** | 1 | `lockbit5` |
| **Immobilier** | 1 | `payload` |
| **Conseil** | 1 | `apt73/bashe` |
| **Commerce** | 1 | `qilin` |
| **Automobile** | 1 | `Lockbit5` |
| **IT Consulting** | 1 | `thegentlemen` |
| **Service public** | 1 | `thegentlemen` |

---
## 🔍 Top 5 des pays les plus ciblés

- Afrique du Sud ████████████░░░░ 3
- Égypte ████████████░░░░ 3
- Nigeria ████████░░░░░░░░ 2
- Ghana ████████░░░░░░░░ 2
- Sénégal ████░░░░░░░░░░░░ 1 (139 To)
---
```mermaid
graph LR
  %% Actor -> Country (weighted by incident count)

  A0["0APT"] -->|1| SO["Somalia 🇸🇴"]
  A0 -->|1| GH["Ghana 🇬🇭"]
  A0 -->|1| TZ["Tanzania 🇹🇿"]

  AG["thegentlemen"] -->|1| KE["Kenya 🇰🇪"]
  AG -->|1| GH
  AG -->|1| EG["Egypt 🇪🇬"]
  AG -->|1| ZA["South Africa 🇿🇦"]
  AG -->|1| TN["Tunisia 🇹🇳"]

  AL["lockbit5"] -->|1| MU["Mauritius 🇲🇺"]
  AL -->|1| EG
  AL -->|1| ZA

  AI["incransom"] -->|1| NG["Nigeria 🇳🇬"]
  AI -->|1| CI["Ivory Coast 🇨🇮"]

  AP["payload"] -->|1| EG
  AT["tengu"] -->|1| MA["Morocco 🇲🇦"]
  AQ["qilin"] -->|1| NA["Namibia 🇳🇦"]
  AV["vect"] -->|1| ZA
  AB["The Green Blood Group"] -->|1| SN["Senegal 🇸🇳"]
  AS["apt73/bashe"] -->|1| SD["Sudan 🇸🇩"]
  AK["killsec"] -->|1| NG
```
---

## 🔴 Incident critique : DAF SÉNÉGAL

- **Acteur** : `The Green Blood Group`
- **Volume** : 139 To
- **Pays** : Sénégal
- **Secteur** : Gouvernement
- **Données** : Base citoyens, biométrie, immigration

**⚠️ Plus grande fuite de données jamais recensée en Afrique.**

---

## 🔗 Liens utiles

- [Rapport complet (FR)](../README.md)
- [Full report (EN)](../README_EN.md)
---
## ✍🏿 Auteur
**Adama ASSIONGBON**  
Consultant SOC & Cyber Threat Intelligence  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)
---

*AFRINTEL -- Initiative de Veille Open CTI*\
*TLP:CLEAR - Partage public autorisé*

