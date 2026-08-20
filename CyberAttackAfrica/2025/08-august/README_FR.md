[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple) ![Période](https://img.shields.io/badge/Période-2025-blue)
# Rapport CTI : Cyberattaques en Afrique - Août 2025 (13 victimes)
👉🏾 [**English version available here**](./README.md)

## 1. Introduction
Ce rapport de Cyber Threat Intelligence (CTI) présente une analyse détaillée des cyberattaques survenues en Afrique durant le mois d'août 2025. Les informations sont issues de sources OSINT et de sites de fuites de groupes ransomware, compilées dans le cadre du projet AFRINTEL. L'objectif est de fournir une vision claire des tendances, des acteurs menaçants, des secteurs ciblés et des indicateurs de compromission associés.

## 2. Résumé exécutif
- **Nombre total d'attaques recensées** : 13
- **Acteurs les plus actifs** : qilin (3 attaques), inconnu (2), akira (1), warlock (1), direwolf (1), incransom (1), RainbowDF (1), Chucky_BF (1), GhostCrawl (1), BIGBROTHER (1).
- **Secteurs les plus ciblés** : Technologies (4), Énergie (2), Banque/Finance (2), Agroalimentaire/Industrie (1), Logistique (1), Commerce de détail (1), IoT/Sécurité (1), Gouvernement (1).
- **Pays les plus touchés** : Afrique du Sud (3), Tunisie (2), Kenya (1), Maroc (1), Nigeria (1), Algérie (1), Ouganda (1), Égypte (1), Maurice (1), Togo (1).
- **Volumes de données exfiltrés notables** : Zenith Bank (Nigeria) - 1,8 million d'enregistrements ; New Era Com (Maroc) - 607 Mo (dump SQL) ; Body Graphics (Afrique du Sud) - plus de 6 500 fiches clients ; TEAM4 Security (Égypte) - lots de données multiples.

## 3. Statistiques clés

### 3.1 Répartition par groupe/acteur
| Groupe/Acteur | Nombre d'attaques |
|---------------|-------------------|
| qilin | 3 |
| Inconnu | 2 |
| akira | 1 |
| warlock | 1 |
| direwolf | 1 |
| incransom | 1 |
| RainbowDF | 1 |
| Chucky_BF | 1 |
| GhostCrawl | 1 |
| BIGBROTHER | 1 |
| **Total** | **13** |

```mermaid
pie title Répartition des attaques par acteur (août 2025)
    "qilin" : 3
    "Inconnu" : 2
    "akira" : 1
    "warlock" : 1
    "direwolf" : 1
    "incransom" : 1
    "RainbowDF" : 1
    "Chucky_BF" : 1
    "GhostCrawl" : 1
    "BIGBROTHER" : 1
```

### 3.2 Répartition par secteur d'activité
| Secteur | Nombre d'attaques |
|---------|-------------------|
| Technologies | 4 |
| Énergie | 2 |
| Banque / Finance | 2 |
| Agroalimentaire / Industrie | 1 |
| Logistique | 1 |
| Commerce de détail / E‑commerce | 1 |
| IoT / Sécurité télématique | 1 |
| Gouvernement | 1 |
| **Total** | **13** |

```mermaid
xychart-beta
    title "Attaques par secteur - Août 2025"
    x-axis ["Technology", "Energy", "Finance", "Agribusiness", "Logistics", "Retail", "IoT/Security", "Government"]
    y-axis "Nombre d'attaques" 0 --> 5
    bar [4, 2, 2, 1, 1, 1, 1, 1]
```

### 3.3 Répartition par pays
| Pays | Nombre d'attaques |
|------|-------------------|
| 🇿🇦 Afrique du Sud | 3 |
| 🇹🇳 Tunisie | 2 |
| 🇰🇪 Kenya | 1 |
| 🇲🇦 Maroc | 1 |
| 🇳🇬 Nigeria | 1 |
| 🇩🇿 Algérie | 1 |
| 🇺🇬 Ouganda | 1 |
| 🇪🇬 Égypte | 1 |
| 🇲🇺 Maurice | 1 |
| 🇹🇬 Togo | 1 |
| **Total** | **13** |

```mermaid
xychart-beta
    title "Attaques par pays - Août 2025"
    x-axis ["🇿🇦Afrique Sud", "🇹🇳Tunisie", "🇰🇪Kenya", "🇲🇦Maroc", "🇳🇬Nigeria", "🇩🇿Algérie", "🇺🇬Ouganda", "🇪🇬Égypte", "🇲🇺Maurice", "🇹🇬Togo"]
    y-axis "Nombre d'attaques" 0 --> 4
    bar [3, 2, 1, 1, 1, 1, 1, 1, 1, 1]
```

<!-- AFRINTEL_CURRENT_MODEL_START -->
### 3.4 Vue globale standardisée

| Pays | Ransomware | Exposition des données (fuites + accès) | Total | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| 🇿🇦 Afrique du Sud | 2 | 1 | 3 | 🟧🟧 🟦 |
| 🇹🇳 Tunisie | 1 | 1 | 2 | 🟧 🟦 |
| 🇩🇿 Algérie | 1 | 0 | 1 | 🟧 |
| 🇪🇬 Égypte | 0 | 1 | 1 |  🟦 |
| 🇰🇪 Kenya | 1 | 0 | 1 | 🟧 |
| 🇲🇺 Maurice | 1 | 0 | 1 | 🟧 |
| 🇲🇦 Maroc | 0 | 1 | 1 |  🟦 |
| 🇳🇬 Nigeria | 0 | 1 | 1 |  🟦 |
| 🇹🇬 Togo | 0 | 1 | 1 |  🟦 |
| 🇺🇬 Ouganda | 1 | 0 | 1 | 🟧 |

```pie
    title Types d’incidents
    "Ransomware" : 7
    "Fuites de données + ventes d’accès" : 6
```

### Vue agrégée mensuelle de l’exposition

La vue CTI mensuelle regroupe les fuites de données et les ventes d’accès sous **exposition des données** : **6 fiches** (46,2% du corpus mensuel). Les fiches sources restent la référence ; une vente d’accès ne prouve pas à elle seule l’exfiltration de données.


### Répartition géographique par région

| Région | Occurrences | Ransomware | Exposition des données (fuites + accès) | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| Afrique du Nord | 5 | 2 | 3 | 🟧🟧 🟦🟦🟦 |
| Afrique australe | 4 | 3 | 1 | 🟧🟧🟧 🟦 |
| Afrique de l’Ouest et centrale | 2 | 0 | 2 |  🟦🟦 |
| Afrique de l’Est | 2 | 2 | 0 | 🟧🟧 |

```mermaid
xychart-beta
    title "Occurrences par région"
    x-axis ["NA","SA","WC","EA"]
    y-axis "Occurrences" 0 --> 6
    bar [5,4,2,2]
```
Légende : NA = Afrique du Nord ; SA = Afrique australe ; WC = Afrique de l’Ouest et centrale ; EA = Afrique de l’Est

### Répartition sectorielle

| Secteur | Fiches | Part | Activité |
| :--- | ---: | ---: | :--- |
| Technologies / informatique | 6 | 46,2% | ██████████ |
| Finance / banque | 2 | 15,4% | ███ |
| Gouvernement / administration | 2 | 15,4% | ███ |
| Transport / logistique | 2 | 15,4% | ███ |
| Commerce / e-commerce | 1 | 7,7% | ██ |

### Acteurs / groupes les plus présents

| Acteur / Groupe | Fiches | Activité |
| :--- | ---: | :--- |
| qilin | 3 | ██████████ |
| BIGBROTHER | 1 | ███ |
| Chucky_BF | 1 | ███ |
| GhostCrawl | 1 | ███ |
| KaruHunters | 1 | ███ |
| N1KA | 1 | ███ |
| RainbowDF | 1 | ███ |
| akira | 1 | ███ |
| direwolf | 1 | ███ |
| incransom | 1 | ███ |
<!-- AFRINTEL_CURRENT_MODEL_END -->
## 4. Détail des attaques par groupe/acteur

### 4.1 qilin (3 attaques)
- **06/08/2025** : KenGen (Kenya, énergie) - Revendication & divulgation.
- **18/08/2025** : Uganda Electricity Transmission Company Limited (Ouganda, énergie) - Revendication & divulgation.
- **25/08/2025** : SWAN Mauritius (Maurice, assurances) - Revendication & divulgation.

*Remarque* : qilin a ciblé des infrastructures énergétiques critiques en Afrique de l'Est ainsi qu'un assureur majeur à Maurice, montrant sa polyvalence.

### 4.2 Acteurs inconnus (2 attaques)
- **09/08/2025** : Zenith Bank (Nigeria, banque) - Fuite massive et mise en vente de 1,8 million d'enregistrements.
- **18/08/2025** : Body Graphics Tattoo Supply (Afrique du Sud, commerce de détail) - Fuite complète de plus de 6 500 fiches clients et administrateurs.

*Remarque* : Ces deux incidents ont entraîné des exfiltrations de données importantes, le secteur bancaire étant particulièrement touché.

### 4.3 akira (1 attaque)
- **13/08/2025** : Cevital (Algérie, agroalimentaire/industrie) - Revendication & divulgation.

### 4.4 warlock (1 attaque)
- **17/08/2025** : SYSPRO (Afrique du Sud, technologies/ERP) - Revendication & divulgation.

### 4.5 direwolf (1 attaque)
- **18/08/2025** : International Freight & Commerce (Tunisie, logistique) - Revendication & divulgation.

### 4.6 incransom (1 attaque)
- **20/08/2025** : Netstar South Africa (Afrique du Sud, IoT/sécurité télématique) - Deuxième attaque contre cette entreprise, revendication & divulgation.

### 4.7 RainbowDF (1 attaque)
- **06/08/2025** : Yasat (Tunisie, technologies/distribution multimédia) - Dump SQL massif de la base de production.

### 4.8 Chucky_BF (1 attaque)
- **06/08/2025** : New Era Com (Maroc, télécoms/services IT) - Dump SQL public de 607 Mo contenant plus de 476 000 enregistrements.

### 4.9 GhostCrawl (1 attaque)
- **23/08/2025** : TEAM4 Security (Égypte, sécurité/défense/RH) - Fuite massive et mise en vente de 5 lots de données RH, médicales, civiles et financières.

### 4.10 BIGBROTHER (1 attaque)
- **25/08/2025** : Infrastructures Gouvernementales (Togo, gouvernement) - Mise en vente d'accès privilégiés (accès administrateur proposé pour 1 000 $).
### 4.11 Graphe : Acteur → victime → pays
```mermaid
graph LR
    qilin -->|KenGen| Kenya["🇰🇪 Kenya"]
    qilin -->|Uganda Electricity| Ouganda["🇺🇬 Ouganda"]
    qilin -->|SWAN| Maurice["🇲🇺 Maurice"]
    inconnu1["Inconnu"] -->|Zenith Bank| Nigeria["🇳🇬 Nigeria"]
    inconnu2["Inconnu"] -->|Body Graphics| AfriqueSud["🇿🇦 Afrique du Sud"]
    akira -->|Cevital| Algerie["🇩🇿 Algérie"]
    warlock -->|SYSPRO| AfriqueSud2["🇿🇦 Afrique du Sud"]
    direwolf -->|International Freight| Tunisie["🇹🇳 Tunisie"]
    incransom -->|Netstar| AfriqueSud3["🇿🇦 Afrique du Sud"]
    RainbowDF -->|Yasat| Tunisie2["🇹🇳 Tunisie"]
    Chucky_BF -->|New Era Com| Maroc["🇲🇦 Maroc"]
    GhostCrawl -->|TEAM4| Egypte["🇪🇬 Égypte"]
    BIGBROTHER -->|Govt Infrastructures| Togo["🇹🇬 Togo"]
```
## 5. Analyse sectorielle
- **Technologies** : 4 attaques (Yasat, New Era Com, SYSPRO, TEAM4 Security). Le secteur reste une cible de choix, avec des injections SQL et des fuites de données touchant des plateformes multimédia, des services IT, des éditeurs de logiciels et des sociétés de sécurité.
- **Énergie** : 2 attaques (KenGen, Uganda Electricity). qilin a frappé des infrastructures critiques en Afrique de l'Est, soulevant des inquiétudes sur la sécurité des réseaux électriques.
- **Banque/Finance** : 2 attaques (Zenith Bank, SWAN Mauritius). De grandes institutions financières au Nigeria et à Maurice ont subi des fuites, Zenith Bank perdant 1,8 million d'enregistrements.
- **Agroalimentaire/Industrie** : 1 attaque (Cevital) par akira, visant le plus grand conglomérat industriel algérien.
- **Logistique** : 1 attaque (International Freight & Commerce) par direwolf, touchant une entreprise tunisienne.
- **Commerce de détail/E‑commerce** : 1 attaque (Body Graphics) par un acteur inconnu, avec fuite de données clients.
- **IoT/Sécurité télématique** : 1 attaque (Netstar) par incransom, deuxième incident pour cette société sud-africaine.
- **Gouvernement** : 1 attaque (infrastructures togolaises) par BIGBROTHER, avec vente d'accès privilégiés.

## 6. Analyse géographique
- **Afrique du Sud** : 3 attaques (SYSPRO, Body Graphics, Netstar) - secteurs technologique, commercial et IoT.
- **Tunisie** : 2 attaques (Yasat, International Freight) - technologies et logistique.
- **Kenya, Maroc, Nigeria, Algérie, Ouganda, Égypte, Maurice, Togo** : 1 attaque chacun, illustrant une large dispersion géographique.

L'Afrique du Nord (🇹🇳 Tunisie, 🇲🇦 Maroc, 🇩🇿 Algérie, 🇪🇬 Égypte) totalise 5 attaques, tandis que l'Afrique subsaharienne (Afrique du Sud, Kenya, Nigeria, Ouganda, Maurice, Togo) en compte 8, confirmant l'étendue de la menace sur tout le continent.

### 6.1 Chronologie des attaques
```mermaid
timeline
    title Chronologie des attaques - Août 2025

    section 06 Août
        qilin : KenGen (Kenya)
        RainbowDF : Yasat (Tunisie)
        Chucky_BF : New Era Com (Maroc)
    section 09 Août
        Inconnu : Zenith Bank (Nigeria)
    section 13 Août
        akira : Cevital (Algérie)
    section 17 Août
        warlock : SYSPRO (Afrique du Sud)
    section 18 Août
        qilin : Uganda Electricity (Ouganda)
        Inconnu : Body Graphics (Afrique du Sud)
        direwolf : International Freight (Tunisie)
    section 20 Août
        incransom : Netstar (Afrique du Sud)
    section 23 Août
        GhostCrawl : TEAM4 (Égypte)
    section 25 Août
        qilin : SWAN (Maurice)
        BIGBROTHER : Govt Infrastructures (Togo)
```
## 7. TTPs observées
- **Injections SQL** : probablement utilisées contre Yasat et New Era Com, aboutissant à des dumps complets de bases de données.
- **Exfiltration et vente de données** : plusieurs acteurs (Inconnu, GhostCrawl, BIGBROTHER) ont mis en vente les données volées sur des forums clandestins.
- **Ciblage d'infrastructures critiques** : qilin s'est concentré sur des compagnies d'électricité au Kenya et en Ouganda.
- **Attaques répétées** : Netstar a été de nouveau frappée par incransom après un premier incident en mai 2025.
- **Vente d'accès privilégiés** : BIGBROTHER a proposé un accès administrateur aux systèmes gouvernementaux togolais, indiquant probablement une compromission RDP/VPN.

## 8. Recommandations
- **Entreprises technologiques** : mettre en place une validation rigoureuse des entrées et des pare-feu applicatifs pour prévenir les injections SQL. Des audits de sécurité et des tests d'intrusion réguliers sont indispensables.
- **Secteur de l'énergie** : les infrastructures critiques doivent adopter une surveillance avancée des menaces, une segmentation réseau et des plans de réponse aux incidents.
- **Banque/finance** : les institutions financières devraient imposer l'authentification multi-facteurs, chiffrer les données sensibles et surveiller les schémas d'accès anormaux.
- **Tous secteurs** : la formation des employés à la détection du phishing, les sauvegardes hors ligne et l'application régulière des correctifs restent fondamentales.

## 9. Conclusion
Août 2025 a vu une grande variété d'attaques à travers l'Afrique, les secteurs technologique et énergétique étant les plus touchés. L'implication de multiples acteurs (qilin, pirates inconnus, hacktivistes) et la vente d'accès privilégiés soulignent l'évolution de la menace. La réitération des attaques contre Netstar montre la persistance des groupes ransomware. Une coopération régionale renforcée et le partage d'informations sont cruciaux pour contrer ces menaces.

## ✍🏿 Auteur
*Adama ASSIONGBON*  
*Consultant SOC & Cyber Threat Intelligence*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)
