[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Période](https://img.shields.io/badge/Période-2025-blue)

# Rapport CTI : Cyberattaques en Afrique - Mai 2025
👉🏾 [**English version available here**](./README.md)

## 1. Résumé exécutif
- **Nombre total d'attaques recensées** : 21
- **Acteurs les plus actifs** : devman (6 attaques), kill9 (6), killsec (1), nightspire (1), incransom (1), Phantom Atlas (1), arkana (1), everest (1), datacarry (1), worldleaks (1), cache (1).
- **Secteurs les plus ciblés** : Banque / Services financiers (6), Technologies (4), Santé (2), Finance / Assurance (2), Services aux entreprises (1), Industrie (1), Transport (1), Gouvernement (1), Éducation (1), Mines (1), Retail (1).
- **Pays les plus touchés** : Afrique du Sud (9), Mauritanie (6), Égypte (1), Kenya (1), Botswana (1), Algérie (1), Cameroun (1), Togo (1).
- **Volume de données exfiltrées** : 2,5 To pour NSSF Kenya, 1 Go pour Netmaster Togo. La revendication bancaire mauritanienne (kill9) a publié des échantillons clients et de cartes bancaires sans volume total précisé ; les autres volumes ne sont pas précisés.


## 2. Méthodologie
Ce rapport de Cyber Threat Intelligence (CTI) présente une analyse détaillée des cyberattaques survenues en Afrique durant le mois de mai 2025. Les informations sont issues de sources OSINT et de sites de fuites de groupes ransomware, compilées dans le cadre du projet AFRINTEL. L'objectif est de fournir une vision claire des tendances, des acteurs menaçants, des secteurs ciblés et des indicateurs de compromission associés.


## 3. Vue d'ensemble

### 3.1 Répartition par acteur malveillant
| Acteur | Nombre d'attaques |
|-------------------|-------------------|
| devman            | 6                 |
| kill9             | 6                 |
| killsec           | 1                 |
| nightspire        | 1                 |
| incransom         | 1                 |
| Phantom Atlas     | 1                 |
| arkana            | 1                 |
| everest           | 1                 |
| datacarry         | 1                 |
| worldleaks        | 1                 |
| cache             | 1                 |
| **Total**         | **21**            |

```mermaid
pie showData
    title Répartition des attaques par acteur
    "devman" : 6
    "kill9" : 6
    "killsec" : 1
    "nightspire" : 1
    "incransom" : 1
    "Phantom Atlas" : 1
    "arkana" : 1
    "everest" : 1
    "datacarry" : 1
    "worldleaks" : 1
    "cache" : 1
```

### 3.2 Répartition par secteur d'activité
| Secteur | Nombre d'attaques |
|---------|-------------------|
| Banque / Services financiers | 6 |
| Technologies | 4 |
| Santé / Pharmacie | 2 |
| Finance / Assurance | 2 |
| Services aux entreprises (RH) | 1 |
| Industrie (EPI) | 1 |
| Transport aérien | 1 |
| Gouvernement / Social | 1 |
| Éducation | 1 |
| Mines | 1 |
| Retail / Distribution | 1 |
| **Total** | **21** |

```mermaid
pie showData
    title Répartition par secteur d'activité
    "Banque" : 6
    "Technologies" : 4
    "Santé" : 2
    "Finance" : 2
    "Services RH" : 1
    "Industrie" : 1
    "Transport" : 1
    "Gouvernement" : 1
    "Éducation" : 1
    "Mines" : 1
    "Retail" : 1
```

### 3.3 Répartition par pays
| Pays | Nombre d'attaques |
|------|-------------------|
| 🇿🇦 Afrique du Sud | 9 |
| 🇲🇷 Mauritanie | 6 |
| 🇪🇬 Égypte | 1 |
| 🇰🇪 Kenya | 1 |
| 🇧🇼 Botswana | 1 |
| 🇩🇿 Algérie | 1 |
| 🇨🇲 Cameroun | 1 |
| 🇹🇬 Togo | 1 |
| **Total** | **21** |

```mermaid
pie showData
    title Répartition par pays (Mai 2025)
    "🇿🇦 Afrique du Sud" : 9
    "🇲🇷 Mauritanie" : 6
    "🇪🇬 Égypte" : 1
    "🇰🇪 Kenya" : 1
    "🇧🇼 Botswana" : 1
    "🇩🇿 Algérie" : 1
    "🇨🇲 Cameroun" : 1
    "🇹🇬 Togo" : 1
```

<!-- AFRINTEL_CURRENT_MODEL_START -->
### 3.4 Vue globale standardisée

| Pays | Ransomware | Exposition des données (fuites + accès) | Total | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| 🇿🇦 Afrique du Sud | 9 | 0 | 9 | 🟧🟧🟧🟧🟧🟧🟧🟧🟧 |
| 🇲🇷 Mauritanie | 0 | 6 | 6 |  🟦🟦🟦🟦🟦🟦 |
| 🇩🇿 Algérie | 0 | 1 | 1 |  🟦 |
| 🇧🇼 Botswana | 1 | 0 | 1 | 🟧 |
| 🇨🇲 Cameroun | 1 | 0 | 1 | 🟧 |
| 🇪🇬 Égypte | 1 | 0 | 1 | 🟧 |
| 🇰🇪 Kenya | 1 | 0 | 1 | 🟧 |
| 🇹🇬 Togo | 0 | 1 | 1 |  🟦 |

```mermaid
pie showData
    title Types d’incidents
    "Ransomware" : 13
    "Fuites de données + ventes d’accès" : 8
```

### Vue agrégée mensuelle de l’exposition

La vue CTI mensuelle regroupe les fuites de données et les ventes d’accès sous **exposition des données** : **8 fiches** (38,1% du corpus mensuel). Les fiches sources restent la référence ; une vente d’accès ne prouve pas à elle seule l’exfiltration de données.


### Répartition géographique par région

| Région | Occurrences | Ransomware | Exposition des données (fuites + accès) | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| Afrique du Nord | 8 | 1 | 7 | 🟧 🟦🟦🟦🟦🟦🟦🟦 |
| Afrique australe | 10 | 10 | 0 | 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧 |
| Afrique de l’Ouest | 1 | 0 | 1 | 🟦 |
| Afrique centrale | 1 | 1 | 0 | 🟧 |
| Afrique de l’Est | 1 | 1 | 0 | 🟧 |

```mermaid
xychart
    title "Occurrences par région"
    x-axis ["NA","SA","AO","AC","AE"]
    y-axis "Occurrences" 0 --> 11
    bar [8,10,1,1,1]
```
Légende : NA = Afrique du Nord ; SA = Afrique australe ; AO = Afrique de l’Ouest ; AC = Afrique centrale ; AE = Afrique de l’Est

### Répartition sectorielle

| Secteur | Fiches | Part | Activité |
| :--- | ---: | ---: | :--- |
| Finance / banque | 8 | 38,1% | ██████████ |
| Technologies / informatique | 4 | 19,0% | █████ |
| Santé / médical | 2 | 9,5% | ██ |
| Éducation / universités | 1 | 4,8% | █ |
| Énergie / services publics | 1 | 4,8% | █ |
| Gouvernement / administration | 1 | 4,8% | █ |
| Industrie / fabrication | 1 | 4,8% | █ |
| Services professionnels | 1 | 4,8% | █ |
| Commerce / e-commerce | 1 | 4,8% | █ |
| Transport / logistique | 1 | 4,8% | █ |

### Acteurs / groupes les plus présents

| Acteur / Groupe | Fiches | Activité |
| :--- | ---: | :--- |
| devman | 6 | ██████████ |
| kill9 | 6 | ██████████ |
| Datacarry | 1 | ██ |
| Phantom Atlas | 1 | ██ |
| arkana | 1 | ██ |
| cache | 1 | ██ |
| everest | 1 | ██ |
| incransom | 1 | ██ |
| killsec | 1 | ██ |
| nightspire | 1 | ██ |
<!-- AFRINTEL_CURRENT_MODEL_END -->

### Comparaison avec le mois précédent

À partir des fiches incidents validées comme source de comptage, mai 2025 compte **21** incidents contre **17** le mois précédent (une hausse de **+4** ; **+23.5%**). Cette comparaison décrit les publications enregistrées par AFRINTEL et ne prouve pas à elle seule une évolution de l'activité des attaquants ni un impact confirmé sur les victimes.

| Indicateur | Mois précédent | Mois en cours | Variation |
|---|---:|---:|---:|
| Fiches incidents enregistrées | 17 | 21 | +4 (+23.5%) |

## 4. Analyse détaillée par type d'incident

## 5. Impact sectoriel
- **Banque / Services financiers** : 6 attaques, toutes revendiquées par kill9 contre des banques mauritaniennes (BAMIS, Banque Mauritanienne pour le Commerce International, BCI, Orabank Mauritanie-SA, BIM Bank, GBM) dans un unique post coordonné. Des échantillons de cartes spécifiquement attribués soutiennent quatre des six revendications avec un niveau de confiance moyen ; les deux autres restent non vérifiées.
- **Technologies** : 4 attaques (iOCO, DovesIT, Netstar, Netmaster). devman domine, avec une fuite de données touchant un registrar togolais revendiquée par le cybercriminel cache.
- **Santé / Pharmacie** : 2 attaques (Medswana, Mediclinic). killsec et everest ciblent des acteurs de la santé au Botswana et en Afrique du Sud.
- **Finance / Assurance** : 2 attaques (Future Microfinance, ASCOMA). nightspire et worldleaks visent une ONG égyptienne et un courtier camerounais.
- **Services aux entreprises (RH)** : 1 attaque (South African HR company) par devman, montrant l'intérêt pour les données personnelles.
- **Industrie (EPI)** : 1 attaque (Pienaar Brothers) par devman, dans le secteur minier.
- **Transport aérien** : 1 attaque (SAA) par incransom, touchant la compagnie nationale sud-africaine.
- **Gouvernement / Social** : 1 attaque (NSSF Kenya) par devman, avec exfiltration massive.
- **Mines** : 1 attaque (Anglo American) par arkana, visant un géant minier.
- **Retail / Distribution** : 1 attaque (FrontierCo) par datacarry.


## 6. Profil des acteurs
### 6.1 Profil des acteurs

Les comptages d'acteurs et de sources restent ceux documentés en section 3 et dans les fiches victimes sources. L'attribution est conservée uniquement au niveau étayé par les éléments publics.

### 6.2 Évaluation du risque

Les pays et secteurs présentant plusieurs fiches ou des fonctions publiques, éducatives, sanitaires, financières ou critiques doivent faire l'objet d'une validation prioritaire. Il s'agit d'un signal de priorisation OSINT, et non d'une confirmation de compromission ou d'impact.

- **Afrique du Sud** : 9 attaques, dont 6 de devman. Tous les secteurs sont représentés, avec une forte concentration sur les technologies et les infrastructures critiques.
- **Mauritanie** : 6 attaques, toutes revendiquées par kill9 dans un unique post ciblant le secteur bancaire du pays ; la deuxième campagne mono-acteur/mono-pays la plus importante du mois après celle de devman en Afrique du Sud.
- **Égypte** : 1 attaque (microfinance) par nightspire.
- **Kenya** : 1 attaque majeure (NSSF) par devman, avec 2,5 To de données exfiltrées.
- **Botswana** : 1 attaque (pharmacie) par killsec.
- **Cameroun** : 1 attaque (assurance) par worldleaks.
- **Togo** : 1 attaque (hébergement web) revendiquée par le cybercriminel cache.

L'Afrique du Sud reste le pays le plus touché en volume, confirmant sa position de hub économique régional et de cible privilégiée, mais le secteur bancaire mauritanien a fait l'objet de la deuxième campagne revendiquée du mois.


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
- **Exfiltration massive** : NSSF Kenya (2,5 To) et Netmaster (1 Go) illustrent la collecte de grands volumes de données.
- **Ciblage coordonné multi-établissements** : kill9 a revendiqué six banques mauritaniennes en un seul post, avec des échantillons de cartes bancaires étayant quatre des six revendications.
- **Ciblage d'infrastructures critiques** : transport aérien (SAA), mines (Anglo American), santé (Mediclinic), gouvernement (NSSF), secteur bancaire (Mauritanie).
- **Domination de deux acteurs** : devman et kill9 sont chacun responsables de 6 des 20 incidents recensés (30 % chacun), traduisant deux campagnes actives en parallèle.
- **Diversité des victimes** : grands groupes (Anglo, SAA, Mediclinic) et PME (DovesIT, Pienaar) sont également visés.
- **Double extorsion / modèle de vente** : revendications avec échantillons de données publiés, dont un compte à rebours de vente de 48 heures dans le cas mauritanien.


## 9. Recommandations
- **Afrique du Sud** : renforcer la cybersécurité dans tous les secteurs, en particulier les technologies et les infrastructures critiques.
- **Secteur bancaire mauritanien** : les établissements cités doivent revoir en urgence la segmentation de leurs réseaux, faire tourner les identifiants exposés et surveiller les transactions frauduleuses sur les plages BIN mentionnées dans la revendication.
- **Secteur public** : les organismes comme la NSSF doivent mettre en place des sauvegardes hors ligne et une segmentation réseau.
- **Entreprises de technologies** : les MSP (iOCO, DovesIT, Netstar) sont des cibles privilégiées ; elles doivent sécuriser leurs accès et surveiller les activités anormales.
- **Secteur minier** : Anglo American doit protéger ses données sensibles et ses systèmes industriels.
- **Tous secteurs** : former les employés à la détection des phishing, authentification multi-facteurs, et audits réguliers.


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
Mai 2025 a été marqué par deux campagnes parallèles d'ampleur comparable : l'activité soutenue de devman contre l'Afrique du Sud et le Kenya, avec une attaque massive sur la NSSF (2,5 To), et la revendication coordonnée de kill9 contre six banques mauritaniennes, publiée comme une offre de vente avec un compte à rebours de 48 heures. La diversité sectorielle (technologies, santé, mines, transport, banque) montre que les attaquants ciblent aussi bien les infrastructures critiques que les entreprises de services. L'Afrique du Sud reste le pays le plus touché en volume, mais la revendication bancaire mauritanienne illustre un glissement vers un ciblage coordonné à l'échelle d'un secteur entier. La coopération régionale et le partage d'information sont plus que jamais nécessaires.


### Auteur
*Adama ASSIONGBON*  
*Consultant SOC & Cyber Threat Intelligence*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)

---
*AFRINTEL - Initiative ouverte de veille CTI sur l’Afrique*
