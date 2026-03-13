[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# CTI Report: Cyber Attacks in Africa --- February 2025

👉 French version: README_FR.md

------------------------------------------------------------------------

# 1. Introduction

This Cyber Threat Intelligence (CTI) report analyzes ransomware attacks
affecting African organizations during February 2025 using OSINT sources
and ransomware leak sites collected by the AFRINTEL project.

------------------------------------------------------------------------

# 2. Executive Summary

-   Total attacks recorded: **8**
-   Most active actors: **RansomHub, KillSec**
-   Most targeted country: **🇪🇬 Egypt**
-   Largest data exfiltration: **444.8 GB (SPEED Co)**

------------------------------------------------------------------------

# 3. Victim Overview

  ------------------------------------------------------------------------------
  Date         Victim         Country        Sector               Actor
  ------------ -------------- -------------- -------------------- --------------
  03 Feb       Xlab Group     🇪🇬 Egypt       IT Services          fog

  12 Feb       ASK Gras       🇲🇦 Morocco     Insurance            ransomhub
               Savoye                                             

  12 Feb       South African  🇿🇦 South       Public Services      ransomhub
               Weather        Africa                              
               Service                                            

  19 Feb       Government     🇿🇲 Zambia      Government           flocker
               Services                                           
               Portal                                             

  19 Feb       Brolly         🇬🇭 Ghana       Insurtech            killsec

  21 Feb       Paratus        🇳🇦 Namibia     Telecommunications   akira

  22 Feb       SPEED Co       🇪🇬 Egypt       Logistics            hunter

  23 Feb       Shaghalni      🇪🇬 Egypt       Recruitment          killsec
  ------------------------------------------------------------------------------

------------------------------------------------------------------------

# 4. Attacks by Ransomware Group

  Group       Attacks
  ----------- ---------
  ransomhub   2
  killsec     2
  fog         1
  flocker     1
  akira       1
  hunter      1

``` mermaid
pie title Attacks by Ransomware Group
"ransomhub" : 2
"killsec" : 2
"fog" : 1
"flocker" : 1
"akira" : 1
"hunter" : 1
```

------------------------------------------------------------------------

# 5. Sector Distribution

  Sector                  Attacks
  ----------------------- ---------
  Business Services       2
  Insurance / Insurtech   2
  Telecommunications      1
  Logistics               1
  Public Services         1
  Government              1

``` mermaid
xychart-beta
title "Attacks by Sector"
x-axis ["Business Services","Insurance","Telecom","Logistics","Public Services","Government"]
y-axis "Attacks" 0 --> 3
bar [2,2,1,1,1,1]
```

------------------------------------------------------------------------

# 6. Geographic Distribution

  Country           Attacks
  ----------------- ---------
  🇪🇬 Egypt          3
  🇿🇦 South Africa   1
  🇲🇦 Morocco        1
  🇿🇲 Zambia         1
  🇬🇭 Ghana          1
  🇳🇦 Namibia        1

``` mermaid
xychart-beta
title "Attacks by Country"
x-axis ["🇪🇬 Egypt","🇿🇦 South Africa","🇲🇦 Morocco","🇿🇲 Zambia","🇬🇭 Ghana","🇳🇦 Namibia"]
y-axis "Attacks" 0 --> 4
bar [3,1,1,1,1,1]
```

------------------------------------------------------------------------

# 7. Actor → Victim → Country

``` mermaid
graph LR
fog -->|Xlab Group| Egypt
ransomhub -->|ASK Gras Savoye| Morocco
ransomhub -->|SAWS| SouthAfrica
flocker -->|services.gov.zm| Zambia
killsec -->|Brolly| Ghana
akira -->|Paratus| Namibia
hunter -->|SPEED Co| Egypt
killsec -->|Shaghalni| Egypt
```

------------------------------------------------------------------------

# 8. Attack Timeline

``` mermaid
timeline
title AFRINTEL February 2025 Timeline

section 03 Feb
fog : Xlab Group (Egypt)

section 12 Feb
ransomhub : ASK Gras Savoye (Morocco)
ransomhub : SA Weather Service (South Africa)

section 19 Feb
flocker : Zambia Gov Portal
killsec : Brolly (Ghana)

section 21 Feb
akira : Paratus (Namibia)

section 22 Feb
hunter : SPEED Co (Egypt)

section 23 Feb
killsec : Shaghalni (Egypt)
```

------------------------------------------------------------------------

# 9. Observed Threat Behavior

-   Massive data exfiltration before encryption
-   Double-extortion ransomware model
-   Opportunistic targeting of digital services, telecom, and public
    infrastructure

------------------------------------------------------------------------

# 10. Strategic Forecast

Expected trends:

1.  Increased targeting of **logistics companies**
2.  Rising attacks against **telecom infrastructure**
3.  More attacks against **SaaS and digital platforms**

------------------------------------------------------------------------

AFRINTEL --- African Cyber Threat Intelligence Initiative
