# Rapport CTI semestriel AFRINTEL - Cybermenaces en Afrique - S2 2025

👉🏾 [English version](./README_H2.md)

![Scope](https://img.shields.io/badge/Scope-Africa-darkgreen) ![Type](https://img.shields.io/badge/Type-Cyber%20Threat%20Intelligence-blueviolet) ![Période](https://img.shields.io/badge/Période-S2%202025-blue) ![TLP](https://img.shields.io/badge/TLP-CLEAR-green)

## 1. Synthèse exécutive

Entre juillet-décembre 2025, AFRINTEL a documenté **114 cyberincidents** affectant des organisations, institutions et services numériques en Afrique.

Le semestre est dominé par le **Ransomware avec 63 fiches (55,3 %)** et les **Data Leak avec 42 (36,8 %)**. Ensemble, ces deux catégories représentent **105 incidents, soit 92,1 % du corpus semestriel**. Les autres événements comprennent 3 Access Sale, 0 Account Takeover, 2 Defacement, 2 DDoS, 1 System Intrusion et 1 Malware.

La concentration géographique est marquée : **Maroc (19)**, **Égypte (18)** et **Afrique du Sud (15)** arrivent en tête. Ensemble, ces trois pays représentent **52 fiches, soit 45,6 %** du semestre.

Sur le plan sectoriel, **Finance / Banque (24)**, **Gouvernement / Administration (24)** et **Éducation / Université (8)** sont les secteurs les plus représentés. Les deux premiers concentrent **48 fiches, soit 42,1 %**.

L'activité varie au fil du semestre : **Juillet est le mois le plus volumineux avec 25 incidents**, tandis que **Novembre en compte 15**.

La maturité des preuves demeure hétérogène. AFRINTEL distingue les revendications non vérifiées, les publications accompagnées d'échantillons, les publications complètes revendiquées, les corroborations indépendantes et les confirmations par victimes ou autorités. **Une revendication criminelle, une attribution ou un volume annoncé ne sont pas considérés comme confirmés sans éléments suffisants.**

> **Note de lecture :** les chiffres AFRINTEL mesurent les incidents documentés et la visibilité des menaces observées. Ils ne constituent pas une mesure exhaustive de toutes les compromissions réellement survenues en Afrique.

👉🏾 [Voir les victimes du semestre](./victims_H2_FR.md)

## 2. Méthodologie

- **Période :** juillet-décembre 2025.
- **Source de vérité :** les six couples mensuels validés `victims_FR.md` / `victims.md`.
- **Comptage :** une fiche canonique correspond à un cyberincident documenté ; les dossiers en investigation restent hors statistiques.
- **Classification :** Ransomware, Data Leak, Access Sale, DDoS, Defacement, Account Takeover, System Intrusion, Malware et Operational Fraud.
- **Chronologie :** `Date de l'incident` et `Date de publication initiale` restent séparées.
- **Dates incertaines :** lorsqu'un jour exact n'est pas établi, le mois ou la fenêtre soutenue par les preuves est conservé ; aucun jour n'est inventé.
- **Sources :** les liens publics sont conservés pour les ajouts retrouvés en ligne ; ils ne sont pas imposés rétroactivement aux observations historiques ou Dark Web directes.
- **Secteurs :** normalisation calculée une seule fois puis appliquée avec les mêmes valeurs en FR et EN.
- **Limite :** le corpus représente la visibilité AFRINTEL et non l'ensemble des cyberattaques réellement survenues sur le continent.

## 3. Comparaison S2 2024 corrigé vs S2 2025

Le corpus final corrigé du S2 2024 contient **74 incidents canoniques**, contre **114** au S2 2025. La baseline 2024 a fait l'objet d'un contrôle chronologique et d'une reclassification selon les **mêmes neuf types d'incident** que 2025 ; les catégories ci-dessous sont donc directement comparables et les valeurs nulles valides ne sont plus présentées en `N/A`.

| Indicateur | 2024 final corrigé | 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 74 | 114 | **+40 (+54,1 %)** |
| Ransomware | 57 | 63 | **+6 (+10,5 %)** |
| Data Leak | 9 | 42 | **+33 (+366,7 %)** |
| Access Sale | 3 | 3 | **0 (0,0 %)** |
| DDoS | 0 | 2 | **+2 (nouvellement observé)** |
| Defacement | 1 | 2 | **+1 (+100,0 %)** |
| Account Takeover | 0 | 0 | **Stable** |
| System Intrusion | 4 | 1 | **-3 (-75,0 %)** |
| Malware | 0 | 1 | **+1 (nouvellement observé)** |
| Operational Fraud | 0 | 0 | **Stable** |

Le corpus documenté du S2 passe de **74 à 114 incidents**, soit **+40 (+54,1 %)**. Les Data Leak présentent l'écart absolu le plus important (**+33**), tandis que le Ransomware progresse de six fiches. Ces chiffres décrivent la visibilité du corpus AFRINTEL et ne démontrent pas à eux seuls une hausse équivalente du nombre réel de compromissions réussies.
### 3.1 S1 vs S2 2025

| Indicateur | S1 2025 | S2 2025 | Évolution |
|---|---:|---:|---:|
| Total incidents | 111 | 114 | **+3 (+2,7 %)** |
| Ransomware | 58 | 63 | **+5 (+8,6 %)** |
| Data Leak | 39 | 42 | **+3 (+7,7 %)** |
| Access Sale | 3 | 3 | **0 (0,0 %)** |
| DDoS | 1 | 2 | **+1 (+100,0 %)** |
| Defacement | 2 | 2 | **0 (0,0 %)** |
| Account Takeover | 6 | 0 | **-6 (-100,0 %)** |
| System Intrusion | 2 | 1 | **-1 (-50,0 %)** |
| Malware | 0 | 1 | **+1 (nouveau)** |
| Operational Fraud | 0 | 0 | **Stable** |

Le volume global est presque stable : **111 incidents au S1 contre 114 au S2**. La structure évolue néanmoins : les six Account Takeover de l'année sont concentrés au S1, alors que le S2 compte davantage de Ransomware et contient l'unique incident Malware de 2025.


## 4. Évolution mensuelle

| Mois | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware | Operational Fraud |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Juillet | 25 | 5 | 18 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| Août | 16 | 7 | 5 | 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| Septembre | 19 | 11 | 7 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Octobre | 20 | 16 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Novembre | 15 | 10 | 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Décembre | 19 | 14 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **114** | **63** | **42** | **3** | **2** | **2** | **0** | **1** | **1** | **0** |

### 4.1 Volume mensuel

| Mois | Fiches | Volume |
|---|---:|---|
| Juillet | 25 | █████████████████████████ |
| Août | 16 | ████████████████ |
| Septembre | 19 | ███████████████████ |
| Octobre | 20 | ████████████████████ |
| Novembre | 15 | ███████████████ |
| Décembre | 19 | ███████████████████ |

```mermaid
timeline
    title Activité mensuelle - S2 2025
    Juillet : 25
    Août : 16
    Septembre : 19
    Octobre : 20
    Novembre : 15
    Décembre : 19
```

## 5. Répartition par type d'incident

| Type d'incident | Fiches | Part |
|---|---:|---:|
| Ransomware | **63** | 55,3 % |
| Data Leak | **42** | 36,8 % |
| Access Sale | **3** | 2,6 % |
| DDoS | **2** | 1,8 % |
| Defacement | **2** | 1,8 % |
| Account Takeover | **0** | 0,0 % |
| System Intrusion | **1** | 0,9 % |
| Malware | **1** | 0,9 % |
| Operational Fraud | **0** | 0,0 % |
| **Total** | **114** | **100 %** |

```mermaid
pie showData
    title Types d incident - H2 2025
    "Ransomware" : 63
    "Data Leak" : 42
    "Access Sale" : 3
    "DDoS" : 2
    "Defacement" : 2
    "System Intrusion" : 1
    "Malware" : 1
```

Le Ransomware et les Data Leak représentent ensemble **105 fiches (92,1 %)**.

## 6. Répartition géographique

### 6.1 Pays par type d'incident

| Pays | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Maroc | **19** | 7 | 10 | 0 | 1 | 1 | 0 | 0 | 0 |
| Égypte | **18** | 12 | 4 | 1 | 1 | 0 | 0 | 0 | 0 |
| Afrique du Sud | **15** | 11 | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| Tunisie | **13** | 5 | 7 | 0 | 0 | 0 | 0 | 1 | 0 |
| Nigeria | **9** | 5 | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kenya | **9** | 5 | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| Algérie | **6** | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| Côte d'Ivoire | **3** | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tanzanie | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Namibie | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zimbabwe | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Congo (RDC) | **2** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zambie | **2** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mauritanie | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Érythrée | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Burundi | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Seychelles | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ouganda | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Maurice | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Togo | **1** | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Angola | **1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Sénégal | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Madagascar | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Gabon | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ghana | **1** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **114** | **63** | **42** | **3** | **2** | **2** | **0** | **1** | **1** |

> `Operational Fraud = 0` sur ce semestre ; la colonne est omise pour préserver la lisibilité.

### 6.2 Répartition régionale

| Région | Total | Part | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Afrique du Nord | **56** | 49,1 % | 26 | 25 | 1 | 2 | 1 | 0 | 1 | 0 |
| Afrique australe | **22** | 19,3 % | 17 | 3 | 1 | 0 | 0 | 0 | 0 | 1 |
| Afrique de l'Ouest | **16** | 14,0 % | 8 | 7 | 1 | 0 | 0 | 0 | 0 | 0 |
| Afrique de l'Est | **14** | 12,3 % | 8 | 5 | 0 | 0 | 1 | 0 | 0 | 0 |
| Océan Indien | **3** | 2,6 % | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Afrique centrale | **3** | 2,6 % | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **114** | **100 %** | **63** | **42** | **3** | **2** | **2** | **0** | **1** | **1** |

La région la plus représentée est **Afrique du Nord avec 56 incidents (49,1 %)**.

## 7. Répartition sectorielle

| Secteur | Fiches | Part | Activité |
|---|---:|---:|---|
| Finance / Banque | 24 | 21,1 % | ████████████ |
| Gouvernement / Administration | 24 | 21,1 % | ████████████ |
| Éducation / Université | 8 | 7,0 % | ████ |
| Technologie / IT | 8 | 7,0 % | ████ |
| Santé / Médical | 7 | 6,1 % | ████ |
| Transport / Logistique | 7 | 6,1 % | ████ |
| Construction / Immobilier | 6 | 5,3 % | ███ |
| Industrie / Fabrication | 6 | 5,3 % | ███ |
| Non précisé | 6 | 5,3 % | ███ |
| Télécommunications | 4 | 3,5 % | ██ |
| Commerce / E-commerce | 4 | 3,5 % | ██ |
| Énergie / Services publics | 3 | 2,6 % | ██ |
| Mines | 2 | 1,8 % | █ |
| Services professionnels / Business | 2 | 1,8 % | █ |
| Agriculture / Agro-industrie | 2 | 1,8 % | █ |
| Juridique | 1 | 0,9 % | █ |
| **Total** | **114** | **100 %** | |

## 8. Profil des acteurs / groupes

`Unknown` représente une absence d'attribution et non un acteur cybercriminel.

| Acteur / Groupe | Fiches | Activité |
|---|---:|---|
| qilin | 11 | ███████████ |
| Unknown | 6 | ██████ |
| incransom | 6 | ██████ |
| Dark 07x Team | 5 | █████ |
| nightspire | 4 | ████ |
| clop | 4 | ████ |
| TheGentlemen | 3 | ███ |
| lockbit5 | 3 | ███ |
| devman | 2 | ██ |
| KaruHunters | 2 | ██ |
| warlock | 2 | ██ |
| direwolf | 2 | ██ |
| Not specified | 2 | ██ |
| killsec | 2 | ██ |
| radar | 2 | ██ |
| privilege | 2 | ██ |
| BlackShrantac | 2 | ██ |
| tengu | 2 | ██ |
| dragonforce | 2 | ██ |
| nova | 2 | ██ |

## 9. Maturité des preuves

| Regroupement analytique | Fiches | Part |
|---|---:|---:|
| Claim - Unverified | 54 | 47,4 % |
| Claim - Data Sample Published | 42 | 36,8 % |
| Data Fully Published | 7 | 6,1 % |
| Confirmation victime / gouvernement / autorité | 3 | 2,6 % |
| Corroboré / preuve secondaire | 7 | 6,1 % |
| Tentative | 1 | 0,9 % |
| **Total** | **114** | **100 %** |

Ce regroupement facilite la lecture semestrielle sans remplacer les statuts détaillés des fiches victimes.

## 10. Analyse CTI par type d'incident

### Ransomware - 63

Le Ransomware représente **63 fiches (55,3 %)**. Les pays les plus représentés sont Égypte (12), Afrique du Sud (11), Maroc (7). Une présence sur un leak site ne prouve pas à elle seule un chiffrement.

### Data Leak - 42

Les Data Leak représentent **42 fiches (36,8 %)**. Les principaux pays sont Maroc (10), Tunisie (7), tandis que le Nigeria, l'Algérie et l'Égypte en comptent 4 chacun. Publication, échantillon observé et volume global revendiqué restent des niveaux de preuve distincts.

### Access Sale - 3

Le semestre compte **3 Access Sale**. Répartition principale : Togo (1), Égypte (1), Afrique du Sud (1). Une offre d'accès ne prouve ni une fuite de données ni un accès à l'ensemble de l'infrastructure interne.

### DDoS - 2

Le semestre documente **2 campagnes DDoS**. Répartition : Égypte (1), Maroc (1). Le comptage porte sur les campagnes documentées, pas nécessairement sur chaque domaine individuel ciblé.

### Defacement - 2

Le semestre compte **2 Defacement**. Répartition : Maroc (1), Kenya (1). Un contenu visible modifié n'est pas reclassé en Data Leak sans preuve distincte.

### Account Takeover - 0

Aucun incident n'est classé `Account Takeover` sur ce semestre. Cette valeur nulle reflète le corpus canonique AFRINTEL du S2 2025 et ne signifie pas une absence de compromission de comptes en Afrique.

### System Intrusion - 1

Le semestre compte **1 System Intrusion**. Répartition : Tunisie (1). Ce type est retenu lorsque l'accès ou la tentative d'accès système est établi sans preuve suffisante pour une catégorie plus spécifique.

### Malware - 1

Le semestre documente **1 incident Malware**. Répartition : Afrique du Sud (1). Le type est utilisé lorsque la présence d'un logiciel malveillant est explicitement établie.

### Operational Fraud - 0

Aucun incident n'est classé `Operational Fraud` sur ce semestre. Cette absence dans le corpus ne signifie pas absence de fraude cyber sur le continent.

## 11. Pays les plus exposés par type

### 11.1 Top 10 Ransomware

| Rang | Pays | Fiches |
|---:|---|---:|
| 1 | Égypte | **12** |
| 2 | Afrique du Sud | **11** |
| 3 | Maroc | **7** |
| 4 | Kenya | **5** |
| 5 | Tunisie | **5** |
| 6 | Nigeria | **5** |
| 7 | Tanzanie | **2** |
| 8 | Namibie | **2** |
| 9 | Algérie | **2** |
| 10 | Zimbabwe | **2** |

### 11.2 Top 10 Data Leak

| Rang | Pays | Fiches |
|---:|---|---:|
| 1 | Maroc | **10** |
| 2 | Tunisie | **7** |
| 3 | Nigeria | **4** |
| 4 | Algérie | **4** |
| 5 | Égypte | **4** |
| 6 | Kenya | **3** |
| 7 | Afrique du Sud | **2** |
| 8 | Côte d'Ivoire | **2** |
| 9 | Mauritanie | **1** |
| 10 | Érythrée | **1** |

### 11.3 Autres types d'incident

| Type | Répartition pays | Total |
|---|---|---:|
| Access Sale | Togo (1), Égypte (1), Afrique du Sud (1) | **3** |
| DDoS | Égypte (1), Maroc (1) | **2** |
| Defacement | Maroc (1), Kenya (1) | **2** |
| Account Takeover | - | **0** |
| System Intrusion | Tunisie (1) | **1** |
| Malware | Afrique du Sud (1) | **1** |

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

Le S2 2025 compte **114 cyberincidents documentés**. Le Ransomware et les Data Leak restent dominants, mais les autres types confirment un paysage de menace plus diversifié qu'une lecture limitée à l'extorsion et aux fuites.

La valeur CTI du rapport repose sur la séparation entre **type d'incident, chronologie, niveau de preuve, géographie, secteur et acteur**, afin de présenter une photographie structurée de la menace observable en Afrique sans transformer les zones d'incertitude en certitudes.

**AFRINTEL** - TLP:CLEAR
