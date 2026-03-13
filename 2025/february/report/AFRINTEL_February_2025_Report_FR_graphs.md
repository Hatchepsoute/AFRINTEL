[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# Rapport CTI : Cyberattaques en Afrique --- Février 2025

👉 English version: README.md

------------------------------------------------------------------------

# 1. Introduction

Ce rapport CTI analyse les cyberattaques ransomware ayant touché des
organisations africaines durant février 2025.

------------------------------------------------------------------------

# 2. Résumé exécutif

-   Nombre total d'attaques : **8**
-   Acteurs les plus actifs : **RansomHub, KillSec**
-   Pays le plus ciblé : **🇪🇬 Égypte**
-   Plus grand volume de données volées : **444,8 Go (SPEED Co)**

------------------------------------------------------------------------

# 3. Tableau des victimes

  ------------------------------------------------------------------------
  Date         Victime        Pays           Secteur        Groupe
  ------------ -------------- -------------- -------------- --------------
  03 Feb       Xlab Group     🇪🇬 Égypte      IT             fog

  12 Feb       ASK Gras       🇲🇦 Maroc       Assurances     ransomhub
               Savoye                                       

  12 Feb       South African  🇿🇦 Afrique du  Services       ransomhub
               Weather        Sud            publics        
               Service                                      

  19 Feb       Government     🇿🇲 Zambie      Gouvernement   flocker
               Portal                                       

  19 Feb       Brolly         🇬🇭 Ghana       Insurtech      killsec

  21 Feb       Paratus        🇳🇦 Namibie     Télécom        akira

  22 Feb       SPEED Co       🇪🇬 Égypte      Logistique     hunter

  23 Feb       Shaghalni      🇪🇬 Égypte      Recrutement    killsec
  ------------------------------------------------------------------------

------------------------------------------------------------------------

# 4. Répartition par groupe

``` mermaid
pie title Répartition par groupe ransomware
"ransomhub" : 2
"killsec" : 2
"fog" : 1
"flocker" : 1
"akira" : 1
"hunter" : 1
```

------------------------------------------------------------------------

# 5. Répartition par secteur

``` mermaid
xychart-beta
title "Attaques par secteur"
x-axis ["Services","Assurances","Télécom","Logistique","Services publics","Gouvernement"]
y-axis "Attaques" 0 --> 3
bar [2,2,1,1,1,1]
```

------------------------------------------------------------------------

# 6. Répartition géographique

``` mermaid
xychart-beta
title "Attaques par pays"
x-axis ["🇪🇬 Égypte","🇿🇦 Afrique du Sud","🇲🇦 Maroc","🇿🇲 Zambie","🇬🇭 Ghana","🇳🇦 Namibie"]
y-axis "Attaques" 0 --> 4
bar [3,1,1,1,1,1]
```

------------------------------------------------------------------------

# 7. Graphe Acteur → Victime → Pays

``` mermaid
graph LR
fog -->|Xlab Group| Égypte
ransomhub -->|ASK Gras Savoye| Maroc
ransomhub -->|SAWS| AfriqueDuSud
flocker -->|services.gov.zm| Zambie
killsec -->|Brolly| Ghana
akira -->|Paratus| Namibie
hunter -->|SPEED Co| Égypte
killsec -->|Shaghalni| Égypte
```

------------------------------------------------------------------------

# 8. Chronologie des attaques

``` mermaid
timeline
title Chronologie AFRINTEL février 2025

section 03 Feb
fog : Xlab Group

section 12 Feb
ransomhub : ASK Gras Savoye
ransomhub : SA Weather Service

section 19 Feb
flocker : Zambia Gov Portal
killsec : Brolly

section 21 Feb
akira : Paratus

section 22 Feb
hunter : SPEED Co

section 23 Feb
killsec : Shaghalni
```

------------------------------------------------------------------------

AFRINTEL --- Initiative africaine de Cyber Threat Intelligence
