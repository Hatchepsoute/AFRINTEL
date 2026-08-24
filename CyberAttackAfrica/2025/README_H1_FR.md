# Rapport CTI semestriel AFRINTEL - Cybermenaces en Afrique - S1 2025

👉🏾 [English version](./README_H1.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Période-S1%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Synthèse exécutive

Entre janvier-juin 2025, AFRINTEL a documenté **111 cyberincidents** affectant des organisations, institutions et services numériques en Afrique.

Le semestre est dominé par le **Ransomware avec 58 fiches (52,3 %)** et les **Data Leak avec 39 (35,1 %)**. Ensemble, ces deux catégories représentent **97 incidents, soit 87,4 % du corpus semestriel**. Les autres événements comprennent 3 Access Sale, 6 Account Takeover, 2 Defacement, 1 DDoS, 2 System Intrusion et 0 Malware.

La concentration géographique est marquée : **Afrique du Sud (23)**, **Égypte (17)** et **Maroc (16)** arrivent en tête. Ensemble, ces trois pays représentent **56 fiches, soit 50,5 %** du semestre.

Sur le plan sectoriel, **Gouvernement / Administration (27)**, **Finance / Banque (19)** et **Technologie / IT (12)** sont les secteurs les plus représentés. Les deux premiers concentrent **46 fiches, soit 41,4 %**.

L'activité varie au fil du semestre : **Mai est le mois le plus volumineux avec 26 incidents**, tandis que **Février en compte 10**.

La maturité des preuves demeure hétérogène. AFRINTEL distingue les revendications non vérifiées, les publications accompagnées d'échantillons, les publications complètes revendiquées, les corroborations indépendantes et les confirmations par victimes ou autorités. **Une revendication criminelle, une attribution ou un volume annoncé ne sont pas considérés comme confirmés sans éléments suffisants.**

> **Note de lecture :** les chiffres AFRINTEL mesurent les incidents documentés et la visibilité des menaces observées. Ils ne constituent pas une mesure exhaustive de toutes les compromissions réellement survenues en Afrique.

👉🏾 [Voir les victimes du semestre](./victims_H1_FR.md)

## 2. Méthodologie

- **Période :** janvier-juin 2025.
- **Source de vérité :** les six couples mensuels validés `victims_FR.md` / `victims.md`.
- **Comptage :** une fiche canonique correspond à un cyberincident documenté ; les dossiers en investigation restent hors statistiques.
- **Classification :** Ransomware, Data Leak, Access Sale, DDoS, Defacement, Account Takeover, System Intrusion, Malware et Operational Fraud.
- **Chronologie :** `Date de l'incident` et `Date de publication initiale` restent séparées.
- **Dates incertaines :** lorsqu'un jour exact n'est pas établi, le mois ou la fenêtre soutenue par les preuves est conservé ; aucun jour n'est inventé.
- **Sources :** les liens publics sont conservés pour les ajouts retrouvés en ligne ; ils ne sont pas imposés rétroactivement aux observations historiques ou Dark Web directes.
- **Secteurs :** normalisation calculée une seule fois puis appliquée avec les mêmes valeurs en FR et EN.
- **Limite :** le corpus représente la visibilité AFRINTEL et non l'ensemble des cyberattaques réellement survenues sur le continent.

## 3. Comparaison S1 2024 corrigé vs S1 2025

Le corpus corrigé de S1 2024 contient **54 fiches**, contre **111** sur S1 2025.

| Indicateur | 2024 corrigé | 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 54 | 111 | **+57 (+105,6 %)** |
| Ransomware | 35 | 58 | **+23 (+65,7 %)** |
| Data Leak | 17 | 39 | **+22 (+129,4 %)** |
| Access Sale | 1 | 3 | **+2 (+200,0 %)** |
| DDoS | 0 | 1 | **+1 (nouveau)** |
| Defacement | 0 | 2 | **+2 (nouveau)** |
| Operational Fraud | 1 | 0 | **-1 (-100,0 %)** |
| Account Takeover | N/A | 6 | **N/A** |
| System Intrusion | N/A | 2 | **N/A** |
| Malware | N/A | 0 | **N/A** |

`Account Takeover`, `System Intrusion` et `Malware` restent `N/A` côté 2024 tant que le corpus 2024 n'a pas été rétro-classifié intégralement selon la taxonomie actuelle.


## 4. Évolution mensuelle

| Mois | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware | Operational Fraud |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Janvier | 19 | 16 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Février | 10 | 8 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| Mars | 15 | 9 | 2 | 1 | 0 | 0 | 2 | 1 | 0 | 0 |
| Avril | 20 | 7 | 10 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| Mai | 26 | 13 | 9 | 0 | 0 | 2 | 1 | 1 | 0 | 0 |
| Juin | 21 | 5 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **111** | **58** | **39** | **3** | **1** | **2** | **6** | **2** | **0** | **0** |

### 4.1 Volume mensuel

| Mois | Fiches | Volume |
|---|---:|---|
| Janvier | 19 | ███████████████████ |
| Février | 10 | ██████████ |
| Mars | 15 | ███████████████ |
| Avril | 20 | ████████████████████ |
| Mai | 26 | ██████████████████████████ |
| Juin | 21 | █████████████████████ |

```mermaid
timeline
    title Activite mensuelle - S1 2025
    Janvier : 19
    Février : 10
    Mars : 15
    Avril : 20
    Mai : 26
    Juin : 21
```

## 5. Répartition par type d'incident

| Type d'incident | Fiches | Part |
|---|---:|---:|
| Ransomware | **58** | 52,3 % |
| Data Leak | **39** | 35,1 % |
| Access Sale | **3** | 2,7 % |
| DDoS | **1** | 0,9 % |
| Defacement | **2** | 1,8 % |
| Account Takeover | **6** | 5,4 % |
| System Intrusion | **2** | 1,8 % |
| Malware | **0** | 0,0 % |
| Operational Fraud | **0** | 0,0 % |
| **Total** | **111** | **100 %** |

```mermaid
pie showData
    title Types d incident - S1 2025
    "Ransomware" : 58
    "Data Leak" : 39
    "Access Sale" : 3
    "DDoS" : 1
    "Defacement" : 2
    "Account Takeover" : 6
    "System Intrusion" : 2
```

Le Ransomware et les Data Leak représentent ensemble **97 fiches (87,4 %)**.

## 6. Répartition géographique

### 6.1 Pays par type d'incident

| Pays | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Afrique du Sud | **23** | 17 | 3 | 0 | 0 | 1 | 1 | 1 | 0 |
| Égypte | **17** | 15 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| Maroc | **16** | 5 | 9 | 1 | 1 | 0 | 0 | 0 | 0 |
| Algérie | **13** | 2 | 11 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kenya | **7** | 3 | 1 | 0 | 0 | 0 | 3 | 0 | 0 |
| Mauritanie | **7** | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nigeria | **6** | 4 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| Ghana | **4** | 1 | 2 | 0 | 0 | 0 | 1 | 0 | 0 |
| Zambie | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Botswana | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tanzanie | **2** | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Tunisie | **2** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ouganda | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Namibie | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Burkina Faso | **1** | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Rwanda | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Sénégal | **1** | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Côte d'Ivoire | **1** | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Cameroun | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Togo | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Maurice | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Djibouti | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **111** | **58** | **39** | **3** | **1** | **2** | **6** | **2** | **0** |

> `Operational Fraud = 0` sur ce semestre ; la colonne est omise pour préserver la lisibilité.

### 6.2 Répartition régionale

| Région | Total | Part | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Afrique du Nord | **48** | 43,2 % | 23 | 23 | 1 | 1 | 0 | 0 | 0 | 0 |
| Afrique australe | **28** | 25,2 % | 22 | 3 | 0 | 0 | 1 | 1 | 1 | 0 |
| Afrique de l'Ouest | **21** | 18,9 % | 5 | 11 | 2 | 0 | 1 | 1 | 1 | 0 |
| Afrique de l'Est | **12** | 10,8 % | 6 | 2 | 0 | 0 | 0 | 4 | 0 | 0 |
| Afrique centrale | **1** | 0,9 % | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Océan Indien | **1** | 0,9 % | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **111** | **100 %** | **58** | **39** | **3** | **1** | **2** | **6** | **2** | **0** |

La région la plus représentée est **Afrique du Nord avec 48 incidents (43,2 %)**.

## 7. Répartition sectorielle

| Secteur | Fiches | Part | Activité |
|---|---:|---:|---|
| Gouvernement / Administration | 27 | 24,3 % | ██████████████ |
| Finance / Banque | 19 | 17,1 % | ██████████ |
| Technologie / IT | 12 | 10,8 % | ██████ |
| Éducation / Université | 10 | 9,0 % | █████ |
| Santé / Médical | 7 | 6,3 % | ████ |
| Services professionnels / Business | 7 | 6,3 % | ████ |
| Télécommunications | 5 | 4,5 % | ██ |
| Commerce / E-commerce | 4 | 3,6 % | ██ |
| Transport / Logistique | 3 | 2,7 % | ██ |
| Médias / Divertissement | 3 | 2,7 % | ██ |
| Non précisé | 3 | 2,7 % | ██ |
| Défense / Sécurité | 3 | 2,7 % | ██ |
| Agriculture / Agro-industrie | 2 | 1,8 % | █ |
| Industrie / Fabrication | 2 | 1,8 % | █ |
| Mines | 2 | 1,8 % | █ |
| Hôtellerie / Tourisme | 1 | 0,9 % | █ |
| Construction / Immobilier | 1 | 0,9 % | █ |
| **Total** | **111** | **100 %** | |

## 8. Profil des acteurs / groupes

`Unknown` représente une absence d'attribution et non un acteur cybercriminel.

| Acteur / Groupe | Fiches | Activité |
|---|---:|---|
| Unknown | 13 | █████████████ |
| devman | 8 | ████████ |
| funksec | 7 | ███████ |
| nightspire | 6 | ██████ |
| Phantom Atlas | 6 | ██████ |
| kill9 | 6 | ██████ |
| ransomhub | 4 | ████ |
| killsec | 4 | ████ |
| mrdump | 4 | ████ |
| GDLockerSec | 3 | ███ |
| babuk2 | 3 | ███ |
| spacebears | 2 | ██ |
| arcusmedia | 2 | ██ |
| lynx | 2 | ██ |
| Jabaroot DZ | 2 | ██ |
| B4baYega | 2 | ██ |
| incransom | 2 | ██ |
| warlock | 2 | ██ |
| Keymous | 2 | ██ |

## 9. Maturité des preuves

| Regroupement analytique | Fiches | Part |
|---|---:|---:|
| Claim - Unverified | 46 | 41,4 % |
| Claim - Data Sample Published | 47 | 42,3 % |
| Data Fully Published | 3 | 2,7 % |
| Confirmation victime / gouvernement / autorité | 11 | 9,9 % |
| Corroboré / preuve secondaire | 3 | 2,7 % |
| Tentative | 1 | 0,9 % |
| **Total** | **111** | **100 %** |

Ce regroupement facilite la lecture semestrielle sans remplacer les statuts détaillés des fiches victimes.

## 10. Analyse CTI par type d'incident

### Ransomware - 58

Le Ransomware représente **58 fiches (52,3 %)**. Les pays les plus représentés sont Afrique du Sud (17), Égypte (15), Maroc (5). Une présence sur un leak site ne prouve pas à elle seule un chiffrement.

### Data Leak - 39

Les Data Leak représentent **39 fiches (35,1 %)**. Les principaux pays sont Algérie (11), Maroc (9), Mauritanie (7). Publication, échantillon observé et volume global revendiqué restent des niveaux de preuve distincts.

### Access Sale - 3

Le semestre compte **3 Access Sale**. Répartition principale : Burkina Faso (1), Sénégal (1), Maroc (1). Une offre d'accès ne prouve ni une fuite de données ni un accès à l'ensemble de l'infrastructure interne.

### DDoS - 1

Le semestre documente **1 campagne(s) DDoS**. Répartition : Maroc (1). Le comptage porte sur les campagnes documentées, pas nécessairement sur chaque domaine individuel ciblé.

### Defacement - 2

Le semestre compte **2 Defacement**. Répartition : Afrique du Sud (1), Côte d'Ivoire (1). Un contenu visible modifié n'est pas reclassé en Data Leak sans preuve distincte.

### Account Takeover - 6

Le semestre documente **6 Account Takeover**. Répartition : Kenya (3), Afrique du Sud (1), Ghana (1). Cette catégorie représente les compromissions de comptes institutionnels sans les confondre avec un défacement de site.

### System Intrusion - 2

Le semestre compte **2 System Intrusion**. Répartition : Afrique du Sud (1), Nigeria (1). Ce type est retenu lorsque l'accès ou la tentative d'accès système est établi sans preuve suffisante pour une catégorie plus spécifique.

### Operational Fraud - 0

Aucun incident n'est classé `Operational Fraud` sur ce semestre. Cette absence dans le corpus ne signifie pas absence de fraude cyber sur le continent.

## 11. Pays les plus exposés par type

### 11.1 Top 10 Ransomware

| Rang | Pays | Fiches |
|---:|---|---:|
| 1 | Afrique du Sud | **17** |
| 2 | Égypte | **15** |
| 3 | Maroc | **5** |
| 4 | Nigeria | **4** |
| 5 | Kenya | **3** |
| 6 | Algérie | **2** |
| 7 | Zambie | **2** |
| 8 | Botswana | **2** |
| 9 | Ouganda | **1** |
| 10 | Ghana | **1** |

### 11.2 Top 10 Data Leak

| Rang | Pays | Fiches |
|---:|---|---:|
| 1 | Algérie | **11** |
| 2 | Maroc | **9** |
| 3 | Mauritanie | **7** |
| 4 | Afrique du Sud | **3** |
| 5 | Égypte | **2** |
| 6 | Ghana | **2** |
| 7 | Kenya | **1** |
| 8 | Nigeria | **1** |
| 9 | Togo | **1** |
| 10 | Tunisie | **1** |

### 11.3 Autres types d'incident

| Type | Répartition pays | Total |
|---|---|---:|
| Access Sale | Burkina Faso (1), Sénégal (1), Maroc (1) | **3** |
| DDoS | Maroc (1) | **1** |
| Defacement | Afrique du Sud (1), Côte d'Ivoire (1) | **2** |
| Account Takeover | Kenya (3), Afrique du Sud (1), Ghana (1), Tanzanie (1) | **6** |
| System Intrusion | Afrique du Sud (1), Nigeria (1) | **2** |
| Malware | - | **0** |

## 12. Principaux enseignements CTI

- Le Ransomware reste la première catégorie du semestre, mais les Data Leak représentent une part majeure du corpus.
- Une lecture globale par pays doit être complétée par une lecture par type d'incident.
- Les administrations et les organisations financières restent parmi les secteurs les plus représentés.
- Les ventes d'accès restent séparées des fuites de données tant que l'exfiltration n'est pas démontrée.
- Les prises de contrôle de comptes institutionnels constituent une menace distincte lorsqu'elles sont observées.
- La disponibilité des preuves techniques, confirmations officielles et conclusions DFIR reste inégale.

## 13. Intelligence gaps

- vecteurs d'accès initial souvent inconnus ;
- dates techniques exactes parfois non publiques ;
- volumes revendiqués rarement vérifiables dans leur intégralité ;
- attribution technique souvent limitée au pseudonyme ou label de publication ;
- informations publiques sur remédiation, cause racine et investigations post-incident limitées ;
- cas en investigation exclus des statistiques canoniques.

## 14. Recommandations

### 14.1 Organisations

- imposer MFA résistante au phishing pour comptes privilégiés, VPN, messagerie, réseaux sociaux et consoles d'administration ;
- appliquer PAM, moindre privilège, segmentation et rotation des secrets ;
- maintenir des sauvegardes immuables et tester la restauration ;
- renforcer applications publiques, API et interfaces administratives ;
- formaliser réponse à incident et notification des violations de données.

### 14.2 SOC et détection

- surveiller authentifications anormales, changements MFA, comptes privilégiés et élévations de rôles ;
- détecter lectures massives de bases, exports inhabituels, créations d'archives et transferts sortants volumineux ;
- corréler EDR, IAM, VPN, WAF, proxy, DNS, cloud et logs applicatifs ;
- surveiller les comptes institutionnels exposés sur les réseaux sociaux ;
- distinguer DDoS, intrusion interne et exposition de données.

### 14.3 CTI

- distinguer première observation, date d'incident, publication initiale, échantillon, divulgation et confirmation ;
- suivre republications et reventes sans les compter automatiquement comme nouvelles compromissions ;
- conserver la hiérarchie de preuve entre claim, corroboration et confirmation ;
- maintenir la parité FR/EN avant toute statistique.

## 15. Conclusion

Le S1 2025 compte **111 cyberincidents documentés**. Le Ransomware et les Data Leak restent dominants, mais les autres types confirment un paysage de menace plus diversifié qu'une lecture limitée à l'extorsion et aux fuites.

La valeur CTI du rapport repose sur la séparation entre **type d'incident, chronologie, niveau de preuve, géographie, secteur et acteur**, afin de présenter une photographie structurée de la menace observable en Afrique sans transformer les zones d'incertitude en certitudes.

**AFRINTEL** - TLP:CLEAR
