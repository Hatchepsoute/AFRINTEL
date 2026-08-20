[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple) ![Période](https://img.shields.io/badge/Période-2025-blue)

# Rapport CTI : Cyberattaques en Afrique - Avril 2025
👉🏾 [**English version available here**](./README.md)

## 1. Résumé exécutif
- **Nombre total d'attaques recensées** : 17
- **Acteurs les plus actifs** : Phantom Atlas (3 attaques), Jabaroot DZ (2), devman (2), dragonforce (1), ransomhouse (1), crypto24 (1), cicada3301 (1), gunra (1), p4xar (1), B4baYega (1), Killer_Bee (1), oblivion666 (1).
- **Secteurs les plus ciblés** : Gouvernement / Administrations publiques (5), Finance / Banque / Assurance (2), Santé (2), Agroalimentaire (2), Défense / Sécurité nationale (1), Télécommunications (1), Services aux entreprises / RH (1), Technologie / Services IT (1), Éducation (1).
- **Pays les plus touchés** : Égypte (4), Maroc (4), Algérie (3), Afrique du Sud (2), Sénégal (1), Mauritanie (1), Tunisie (1).
- **Volume de données exfiltrées** : 27,75 Go pour IACC Holdings. Les autres volumes ne sont pas précisés.


## 2. Méthodologie
Ce rapport de Cyber Threat Intelligence (CTI) présente une analyse détaillée des cyberattaques survenues en Afrique durant le mois d'avril 2025. Les informations sont issues de sources OSINT et de sites de fuites de groupes ransomware, compilées dans le cadre du projet AFRINTEL. L'objectif est de fournir une vision claire des tendances, des acteurs menaçants, des secteurs ciblés et des indicateurs de compromission associés.


## 3. Vue d'ensemble

### 3.1 Répartition par acteur/source
| Acteur / Groupe | Nombre d'attaques |
|-------------------|-------------------|
| Phantom Atlas     | 3                 |
| Jabaroot DZ       | 2                 |
| devman            | 2                 |
| dragonforce       | 1                 |
| ransomhouse       | 1                 |
| crypto24          | 1                 |
| cicada3301        | 1                 |
| gunra             | 1                 |
| p4xar             | 1                 |
| B4baYega          | 1                 |
| Killer_Bee        | 1                 |
| oblivion666       | 1                 |
| **Total**         | **16**            |

```mermaid
pie showData
    title Répartition des attaques par acteur (avril 2025)
    "Phantom Atlas" : 3
    "Jabaroot DZ" : 2
    "devman" : 2
    "dragonforce" : 1
    "ransomhouse" : 1
    "crypto24" : 1
    "cicada3301" : 1
    "gunra" : 1
    "p4xar" : 1
    "B4baYega" : 1
    "Killer_Bee" : 1
    "oblivion666" : 1
```
### 3.2 Répartition par secteur d'activité
| Secteur | Nombre d'attaques |
|---------|-------------------|
| Gouvernement / Administrations publiques | 5 |
| Finance / Banque / Assurance | 2 |
| Santé | 2 |
| Agroalimentaire | 2 |
| Défense / Sécurité nationale | 1 |
| Télécommunications | 1 |
| Services aux entreprises / RH | 1 |
| Technologie / Services IT | 1 |
| Éducation | 1 |
| **Total** | **16** |

```mermaid
pie showData
    title Répartition par secteur d'activité
    "Administrations publiques" : 5
    "Finance / Banque / Assurance" : 2
    "Santé" : 2
    "Agroalimentaire" : 2
    "Défense / Sécurité nationale" : 1
    "Télécommunications" : 1
    "Services aux entreprises" : 1
    "Technologie / IT" : 1
    "Éducation" : 1
```

### 3.3 Répartition par pays
| Pays | Nombre d'attaques |
|------|-------------------|
|🇪🇬 Égypte | 4 |
|🇲🇦 Maroc | 4 |
|🇩🇿 Algérie | 3 |
|🇿🇦 Afrique du Sud | 2 |
|🇸🇳 Sénégal | 1 |
|🇲🇷 Mauritanie | 1 |
|🇹🇳 Tunisie | 1 |
| **Total** | **16** |

```mermaid
pie showData
    title Répartition par pays (Avril 2025)
    "🇪🇬 Égypte" : 4
    "🇲🇦 Maroc" : 4
    "🇩🇿 Algérie" : 3
    "🇿🇦 Afrique du Sud" : 2
    "🇸🇳 Sénégal" : 1
    "🇲🇷 Mauritanie" : 1
    "🇹🇳 Tunisie" : 1
```


<!-- AFRINTEL_CURRENT_MODEL_START -->
### 3.4 Vue globale standardisée

| Pays | Ransomware | Exposition des données (fuites + accès) | Total | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| 🇪🇬 Égypte | 4 | 1 | 5 | 🟧🟧🟧🟧 🟦 |
| 🇲🇦 Maroc | 0 | 4 | 4 |  🟦🟦🟦🟦 |
| 🇩🇿 Algérie | 0 | 3 | 3 |  🟦🟦🟦 |
| 🇿🇦 Afrique du Sud | 2 | 0 | 2 | 🟧🟧 |
| 🇲🇷 Mauritanie | 0 | 1 | 1 |  🟦 |
| 🇸🇳 Sénégal | 0 | 1 | 1 |  🟦 |
| 🇹🇳 Tunisie | 1 | 0 | 1 | 🟧 |

```mermaid
pie showData
    title Types d’incidents
    "Ransomware" : 7
    "Fuites de données + ventes d’accès" : 10
```

### Vue agrégée mensuelle de l’exposition

La vue CTI mensuelle regroupe les fuites de données et les ventes d’accès sous **exposition des données** : **10 fiches** (58,8% du corpus mensuel). Les fiches sources restent la référence ; une vente d’accès ne prouve pas à elle seule l’exfiltration de données.


### Répartition géographique par région

| Région | Occurrences | Ransomware | Exposition des données (fuites + accès) | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| Afrique du Nord | 14 | 5 | 9 | 🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Afrique australe | 2 | 2 | 0 | 🟧🟧 |
| Afrique de l’Ouest | 1 | 0 | 1 |  🟦 |
| Afrique centrale | 0 | 0 | 0 |  |
| Afrique de l’Est | 0 | 0 | 0 |  |

```mermaid
xychart
    title "Occurrences par région"
    x-axis ["NA","SA","AO","AC","AE"]
    y-axis "Occurrences" 0 --> 15
    bar [14,2,1,0,0]
```
Légende : NA = Afrique du Nord ; SA = Afrique australe ; AO = Afrique de l’Ouest ; AC = Afrique centrale ; AE = Afrique de l’Est

### Répartition sectorielle

| Secteur | Fiches | Part | Activité |
| :--- | ---: | ---: | :--- |
| Gouvernement / administration | 6 | 35,3% | ██████████ |
| Finance / banque | 4 | 23,5% | ███████ |
| Technologies / informatique | 2 | 11,8% | ███ |
| Agriculture / agro-industrie | 1 | 5,9% | ██ |
| Éducation / universités | 1 | 5,9% | ██ |
| Santé / médical | 1 | 5,9% | ██ |
| Industrie / fabrication | 1 | 5,9% | ██ |
| Services professionnels | 1 | 5,9% | ██ |

### Acteurs / groupes les plus présents

| Acteur / Groupe | Fiches | Activité |
| :--- | ---: | :--- |
| Phantom Atlas | 3 | ██████████ |
| Jabaroot DZ | 2 | ███████ |
| devman | 2 | ███████ |
| B4baYega | 1 | ███ |
| Killer_Bee | 1 | ███ |
| cicada3301 | 1 | ███ |
| crypto24 | 1 | ███ |
| dragonforce | 1 | ███ |
| gunra | 1 | ███ |
| nightspire | 1 | ███ |
<!-- AFRINTEL_CURRENT_MODEL_END -->

### Comparaison avec le mois précédent

À partir des fiches incidents validées comme source de comptage, avril 2025 compte **17** incidents contre **11** le mois précédent (une hausse de **+6** ; **+54.5%**). Cette comparaison décrit les publications enregistrées par AFRINTEL et ne prouve pas à elle seule une évolution de l'activité des attaquants ni un impact confirmé sur les victimes.

| Indicateur | Mois précédent | Mois en cours | Variation |
|---|---:|---:|---:|
| Fiches incidents enregistrées | 11 | 17 | +6 (+54.5%) |

## 4. Analyse détaillée par type d'incident

## 5. Impact sectoriel
- **Administrations publiques** : 4 attaques (CNSS, Ministère de l'Industrie, Ministère de l'Habitat, MGPTT). Les groupes Jabaroot DZ, B4baYega et Phantom Atlas ont ciblé des institutions clés au Maroc et en Algérie, avec des données sensibles (bénéficiaires, documents administratifs).
- **Agroalimentaire** : 2 attaques (Premier Meats, Natilait) par devman et cicada3301, visant des entreprises de transformation alimentaire en Afrique du Sud et Tunisie.
- **Finance/Logistique** : 1 attaque (IACC Holdings) par dragonforce, avec exfiltration de 27,75 Go.
- **Télécommunications** : 1 attaque (Cell C) par ransomhouse, touchant un opérateur majeur sud-africain.
- **Services aux entreprises** : 1 attaque (IBS) par crypto24, ciblant un prestataire BPO égyptien.
- **Technologies** : 1 attaque (Tawasol) par devman, visant un intégrateur de solutions IT.
- **Santé** : 1 attaque (Dar Al Teb) par gunra, frappant un centre médical spécialisé.
- **Éducation** : 1 revendication de fuite (ISMAC) attribuée à p4xar, étayée par un échantillon SQL substantiel contenant des données sensibles d’étudiants.
- **Défense / Sécurité nationale** : 1 revendication de vente d'accès (Forces Armées Sénégalaises / armee.sn) par oblivion666, proposant des domaines et un accès administrateur serveurs/pare-feu, sans échantillon accessible.

### 5.1 Timeline des attaques
```mermaid
timeline
    title Chronologie des attaques - Avril 2025
    section 04 Avr
        oblivion666 : Forces Armées Sénégalaises (🇸🇳 Sénégal)
    section 06 Avr
        dragonforce : IACC Holdings (🇪🇬 Égypte)
    section 07 Avr
        ransomhouse : Cell C (🇿🇦 Afrique du Sud)
    section 08 Avr
        Jabaroot DZ : CNSS (🇲🇦 Maroc)
        Jabaroot DZ : Ministère Industrie (🇲🇦 Maroc)
        crypto24 : IBS (🇪🇬  Égypte)
    section 09 Avr
        Phantom Atlas : MGPTT (🇩🇿 Algérie)
    section 13 Avr
        Killer_Bee : BMI / SEDAD Mobile Wallet (🇲🇷 Mauritanie)
        devman : Tawasol (🇪🇬 Égypte)
        p4xar : ISMAC (🇲🇦 Maroc)
        B4baYega : Ministère de l'Habitat (🇲🇦 Maroc)
    section 20 Avr
        devman : Premier Meats (🇿🇦 Afrique du Sud)
    section 22 Avr
        cicada3301 : Natilait (🇹🇳 Tunisie)
    section 23 Avr
        gunra : Dar Al Teb (🇪🇬 Égypte)
```

## 6. Profil des acteurs
### 6.1 Profil des acteurs

Les comptages d'acteurs et de sources restent ceux documentés en section 3 et dans les fiches victimes sources. L'attribution est conservée uniquement au niveau étayé par les éléments publics.

### 6.2 Évaluation du risque

Les pays et secteurs présentant plusieurs fiches ou des fonctions publiques, éducatives, sanitaires, financières ou critiques doivent faire l'objet d'une validation prioritaire. Il s'agit d'un signal de priorisation OSINT, et non d'une confirmation de compromission ou d'impact.

- **Maroc** : 4 attaques (CNSS, Ministère de l'Industrie, Ministère de l'Habitat, ISMAC) - administration publique et éducation. Deux revendications ont été publiées par Jabaroot DZ le même jour ; celle visant l'ISMAC est étayée par un échantillon SQL substantiel, et celle visant le Ministère de l'Habitat reste non vérifiée en raison d'une archive protégée par mot de passe.
- **Égypte** : 4 attaques (IACC, IBS, Tawasol, Dar Al Teb) - finance, BPO, IT, santé. L'Égypte reste parmi les pays les plus ciblés du continent.
- **Afrique du Sud** : 2 attaques (Cell C, Premier Meats) - télécoms et agroalimentaire.
- **Algérie** : 1 attaque (MGPTT) - mutuelle de santé, avec publication de données personnelles.
- **Tunisie** : 1 attaque (Natilait) - agroalimentaire.
- **Mauritanie** : 1 revendication de fuite (BMI / SEDAD Mobile Wallet) - finance / paiement mobile.
- **Sénégal** : 1 revendication de vente d'accès (Forces Armées Sénégalaises / armee.sn) - défense, non vérifiée.

L'Afrique du Nord (Égypte, Maroc, Algérie, Tunisie) concentre 10 attaques sur 14, confirmant une forte pression sur la région.


## 7. Tendances et lacunes de renseignement
### 7.1 Tendances observées

Les répartitions par pays, secteur, acteur et type d'incident présentées ci-dessus constituent les tendances traçables du mois. Elles décrivent le corpus surveillé et n'établissent pas une campagne plus large sans éléments indépendants.

### 7.2 Lacunes de renseignement

Les rapports disponibles ne permettent pas d'établir pour chaque revendication le vecteur d'accès initial, l'exfiltration complète, la confirmation par la victime, la chronologie de remédiation ou l'impact opérationnel. Aucun détail DFIR public n'est inclus dans le corpus consulté pour cette fiche mensuelle ; cette absence est limitée aux sources examinées.

## 8. Cartographie MITRE ATT&CK (contextuelle)
| Phase | ID technique | Nom | Association à l'incident |
|---|---|---|---|
| Collecte | T1005 | Data from Local System | Correspondance contextuelle pour une collecte ou exposition revendiquée ; la méthode n'est pas confirmée. |
| Collecte | T1213 | Data from Information Repositories | Correspondance contextuelle pour les dossiers ou référentiels décrits publiquement ; la méthode n'est pas confirmée. |

Ces correspondances ATT&CK sont contextuelles et défensives. Elles ne prouvent pas qu'un acteur donné a utilisé la technique.

### Contextual observations
- **Exfiltration de données** : IACC Holdings (27,75 Go), MGPTT (listes de bénéficiaires) et l’échantillon SQL de l’ISMAC illustrent la collecte et l’exposition de données sensibles.
- **Ciblage d'institutions publiques** : 4 attaques sur des organismes gouvernementaux, avec des motivations potentiellement politiques (revendication "représailles" pour MGPTT).
- **Vente d'accès** : oblivion666 a proposé à la vente des domaines et un accès administrateur à l'infrastructure des forces armées sénégalaises, illustrant le segment courtier d'accès de l'écosystème aux côtés des revendications de ransomware et de fuite de données.
- **Diversité des acteurs** : 12 groupes différents actifs, dont des acteurs hacktivistes (Jabaroot DZ, Phantom Atlas) et des ransomwares traditionnels.
- **Double extorsion** : Revendications accompagnées de fuites de données pour pression.
- **Exploitation de failles web** : Probable pour les sites gouvernementaux.


## 9. Recommandations
- **Secteurs public et éducatif** : Renforcer les portails administratifs et étudiants, imposer la MFA aux accès privilégiés, limiter les exports de bases et surveiller la création anormale de dumps SQL, particulièrement au Maroc et en Algérie.
- **Égypte** : Accroître la vigilance dans les secteurs financier, BPO et santé, très ciblés.
- **Agroalimentaire** : Les entreprises comme Premier Meats et Natilait doivent sécuriser leurs chaînes d'approvisionnement numériques.
- **Télécoms** : Opérateurs comme Cell C doivent protéger les données des abonnés.
- **Tous secteurs** : Mettre en place une authentification multi-facteurs et des sauvegardes hors ligne.


## 10. Recommandations SOC et tactiques
### Observé

Les sources publiques documentent des revendications, des publications ou du matériel exposé. Elles ne fournissent pas à elles seules une télémétrie prouvant une technique ou une compromission active.

### Hypothèses

L'abus d'identifiants, un stockage exposé, des contrôles d'accès faibles ou des privilèges d'export excessifs peuvent expliquer certaines expositions, mais chaque hypothèse doit être vérifiée par l'organisation concernée.

### Préventif

Surveiller les journaux d'identité, VPN, cloud, bases de données, messagerie et transferts sortants. Imposer une MFA résistante au phishing, le moindre privilège, la segmentation, des sauvegardes testées et la révocation rapide des jetons ou identifiants.

## 11. Recommandations stratégiques
1. **Risques observés :** prioriser la validation des organisations, secteurs et types de données documentés dans le corpus mensuel.
2. **Hypothèses :** tester les chemins possibles liés aux identifiants, au stockage cloud et aux exports excessifs sans les présenter comme des faits établis.
3. **Socle préventif :** maintenir l'inventaire des actifs, la classification des données, les exercices de réponse, les plans de reprise et les procédures coordonnées de sécurité, de droit et de protection des données.

## 12. Conclusion
Avril 2025 a été marqué par une activité soutenue en Afrique du Nord, avec une forte proportion d'attaques contre les administrations publiques. Les groupes Jabaroot DZ et devman se distinguent par leur polyvalence. La diversité des acteurs (hacktivistes, ransomwares) souligne la complexité de la menace. Une coopération régionale renforcée est nécessaire pour faire face à ces cyberattaques.


### Auteur
*Adama ASSIONGBON*  
*Consultant SOC & Cyber Threat Intelligence*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)

---
*AFRINTEL - Initiative ouverte de veille CTI sur l’Afrique*

---
