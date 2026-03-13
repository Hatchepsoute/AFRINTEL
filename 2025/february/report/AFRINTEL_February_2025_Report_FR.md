[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)

# Rapport CTI : Cyberattaques en Afrique --- Février 2025

👉 English version: README.md

------------------------------------------------------------------------

# 1. Introduction

Ce rapport de Cyber Threat Intelligence (CTI) analyse les cyberattaques
ransomware ayant touché des organisations africaines durant le mois de
février 2025.

Les informations proviennent de : - sources OSINT - sites de fuite de
groupes ransomware - veille CTI AFRINTEL

L'objectif est de fournir une vision claire des acteurs, secteurs et
pays ciblés.

------------------------------------------------------------------------

# 2. Résumé exécutif

-   **Nombre total d'attaques :** 8
-   **Groupes les plus actifs :** RansomHub (2), KillSec (2)
-   **Pays le plus ciblé :** 🇪🇬 Égypte (3 attaques)
-   **Plus grand volume de données volées :** 444,8 Go (SPEED Co)

Ces incidents illustrent la montée des **campagnes de ransomware à
double extorsion visant les organisations africaines.**

------------------------------------------------------------------------

# 3. Vue d'ensemble des victimes

  ------------------------------------------------------------------------------
  Date         Victime        Pays           Secteur              Groupe
  ------------ -------------- -------------- -------------------- --------------
  03 Feb       Xlab Group     🇪🇬 Égypte      Services IT          fog

  12 Feb       ASK Gras       🇲🇦 Maroc       Assurances           ransomhub
               Savoye                                             

  12 Feb       South African  🇿🇦 Afrique du  Services publics     ransomhub
               Weather        Sud                                 
               Service                                            

  19 Feb       Government     🇿🇲 Zambie      Gouvernement         flocker
               Services                                           
               Portal                                             

  19 Feb       Brolly         🇬🇭 Ghana       Insurtech            killsec

  21 Feb       Paratus        🇳🇦 Namibie     Télécommunications   akira

  22 Feb       SPEED Co       🇪🇬 Égypte      Logistique           hunter

  23 Feb       Shaghalni      🇪🇬 Égypte      Plateforme RH        killsec
  ------------------------------------------------------------------------------

------------------------------------------------------------------------

# 4. Répartition par groupe ransomware

  Groupe      Attaques
  ----------- ----------
  ransomhub   2
  killsec     2
  fog         1
  flocker     1
  akira       1
  hunter      1

------------------------------------------------------------------------

# 5. Répartition sectorielle

  Secteur                    Attaques
  -------------------------- ----------
  Services aux entreprises   2
  Assurances / Insurtech     2
  Télécommunications         1
  Logistique                 1
  Services publics           1
  Gouvernement               1

------------------------------------------------------------------------

# 6. Répartition géographique

  Pays                Attaques
  ------------------- ----------
  🇪🇬 Égypte           3
  🇿🇦 Afrique du Sud   1
  🇲🇦 Maroc            1
  🇿🇲 Zambie           1
  🇬🇭 Ghana            1
  🇳🇦 Namibie          1

L'Égypte représente **37,5 % des incidents**, ce qui confirme son statut
de hub numérique régional.

------------------------------------------------------------------------

# 7. Matrice Acteur → Secteur

  Acteur      Finance   Gouvernement   Télécom   Services
  ----------- --------- -------------- --------- ----------
  ransomhub   ✓         ✓                        ✓
  killsec     ✓                                  ✓
  akira                                ✓         
  fog                                            ✓
  hunter                                         ✓

------------------------------------------------------------------------

# 8. TTP observées

### Exfiltration massive

Les attaquants exfiltrent de grandes quantités de données avant
chiffrement.

Exemples : - SPEED Co : **444,8 Go** - Portail gouvernemental zambien :
**1,2 Go**

### Double extorsion

Processus typique :

1.  Vol de données
2.  Chiffrement
3.  Menace de divulgation

### Ciblage opportuniste

Les cibles incluent :

-   startups
-   services numériques
-   infrastructures publiques
-   opérateurs télécom

Cela indique des campagnes **automatisées et opportunistes**.

------------------------------------------------------------------------

# 9. Évaluation confiance / impact

  Incident             Confiance   Impact
  -------------------- ----------- ----------
  ASK Gras Savoye      Moyen       Niveau 2
  SA Weather Service   Moyen       Niveau 2
  Brolly               Moyen       Niveau 2
  Paratus              Moyen       Niveau 3
  SPEED Co             Élevé       Niveau 3
  Portail Zambie       Moyen       Niveau 3

------------------------------------------------------------------------

# 10. Prévisions CTI

Tendances probables :

1.  Augmentation des attaques contre **la logistique africaine**
2.  Ciblage accru des **opérateurs télécom**
3.  Attaques contre **plateformes SaaS et services numériques**

------------------------------------------------------------------------

# 11. Recommandations

Priorités pour les organisations :

-   MFA obligatoire
-   sauvegardes hors ligne
-   segmentation réseau
-   surveillance SOC
-   formation phishing

Les portails gouvernementaux doivent être sécurisés en priorité.

------------------------------------------------------------------------

# Auteur

Adama ASSIONGBON\
Consultant SOC & Cyber Threat Intelligence

AFRINTEL --- Initiative CTI africaine
