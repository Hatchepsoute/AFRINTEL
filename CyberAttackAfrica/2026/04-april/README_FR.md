[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Afrique-orange)
![Threat Type](https://img.shields.io/badge/Menace-Ransomware%20%26%20Data%20Breach-red)
![Period](https://img.shields.io/badge/P%C3%A9riode-Avril_2026-708090)
![Intel Type](https://img.shields.io/badge/Type%20d'Intel-CTI-purple)

# Rapport CTI - menaces cyber en Afrique (Avril 2026)

👉🏾 [**English version available here**](./README.md)

## 1. Synthèse exécutive

Avril 2026 a enregistré **60 incidents cyber revendiqués publiquement** sur le continent - **20 ransomwares** et **40 fuites de données / ventes d’accès**. La menace s’intensifie avec une prolifération de courtiers de données, des expositions très sensibles (personnel du palais royal, documents d’identité, dossiers médicaux) et des ventes d’accès ciblant les gouvernements. Les groupes de ransomware **payload**, **apt73/bashe**, **thegentlemen** et **krybit** maintiennent la pression, tandis que les acteurs de fuites **Grubder**, **anisanas2**, **dark07x**, **wh6ami** et **Rihana** dominent le marché souterrain.

Principales conclusions :
- **20 ransomwares (33,3 %)** et **40 fuites de données / ventes d’accès (66,7 %)**.
- **16 pays** touchés ; le **Maroc** (17 incidents), l’**Égypte** (11) et l’**Afrique du Sud** (8) concentrent 60 % des victimes.
- Plus de **30 acteurs distincts** ; les courtiers de données **Grubder** (7 victimes) et **anisanas2** (3 victimes) en tête.
- Les secteurs gouvernemental, éducatif et de la santé restent les plus visés (45 % combinés).
- Brèches massives : base du personnel du Palais Royal (3 300 fiches avec CNIE), Pick n Pay ASAP/Bottles.com (données bancaires complètes), Kenya Airports Authority (2 To revendiqués), fuite de la messagerie CNSS Bénin (7,1 Go).


### 📋 Liste des victimes

👉🏾 [Voir la liste complète des victimes](./victims_FR.md)

## 2. Méthodologie

- **Périmètre** : 54 pays africains.
- **Période** : 1er - 30 avril 2026 (incidents révélés ou revendiqués ; les attaques peuvent être antérieures).
- **Sources** : Dark web, DLS, OSINT, Telegram, forums underground.
- **Inclusion** : incidents publiquement revendiqués avec victime, pays et secteur identifiés.
- **Typologie** :
  - *Ransomware* : chiffrement + demande de rançon.
  - *Fuite de données / vente d’accès* : exfiltration sans chiffrement, base de données vendue ou publiée, ou vente d’accès à des systèmes compromis.

## 3. Vue d’ensemble

| Indicateur                     | Valeur |
|--------------------------------|--------|
| Nombre total de victimes       | 60     |
| Pays touchés                   | 16     |
| Acteurs distincts              | 30+    |
| Ransomwares                    | 20 (33,3 %) |
| Fuites de données / ventes d’accès | 40 (66,7 %) |

### Classement des pays les plus touchés

**Tous incidents confondus (60) :**
| Rang | Pays | Incidents | Graphique |
| :---: | :--- | :---: | :--- |
| **1** | 🇲🇦 Maroc | **17** | █████████████████ |
| **2** | 🇪🇬 Égypte | **11** | ███████████ |
| **3** | 🇿🇦 Afrique du Sud | **8** | ████████ |
| **4** | 🇳🇬 Nigeria | **4** | ████ |
| **5** | 🇩🇿 Algérie | **4** | ████ |
| **6** | 🇹🇳 Tunisie | **4** | ████ |
| **7** | 🇰🇪 Kenya | **2** | ██ |
| **8** | 🇬🇭 Ghana | **2** | ██ |
| **9** | 🇧🇯 Bénin | **1** | █ |
| **10** | 🇧🇼 Botswana | **1** | █ |
| **11** | 🇪🇹 Éthiopie | **1** | █ |
| **12** | 🇸🇨 Seychelles | **1** | █ |
| **13** | 🇸🇳 Sénégal | **1** | █ |
| **14** | 🇺🇬 Ouganda | **1** | █ |
| **15** | 🇿🇲 Zambie | **1** | █ |
| **–** | 🌍 Multi‑pays *(AO, ZA, NG)* | **1** | █ |

*Note : L'incident multi-pays est comptabilisé comme 1 victime globale.*

### 📊 Répartition des incidents par ransomware (Total : 20)

| Rang | Pays | Incidents | Graphique |
| :---: | :--- | :---: | :--- |
| **1** | 🇪🇬 Égypte | **9** | █████████ |
| **2** | 🇿🇦 Afrique du Sud | **3** | ███ |
| **3** | 🇲🇦 Maroc | **2** | ██ |
| **4** | 🇬🇭 Ghana | **2** | ██ |
| **5** | 🇰🇪 Kenya | **1** | █ |
| **6** | 🇧🇼 Botswana | **1** | █ |
| **7** | 🇸🇨 Seychelles | **1** | █ |
| **8** | 🇿🇲 Zambie | **1** | █ |

### 📊 Répartition des incidents par fuites de données (Total : 40)

| Rang | Pays | Incidents | Graphique |
| :---: | :--- | :---: | :--- |
| **1** | 🇲🇦 Maroc | **15** | ███████████████ |
| **2** | 🇿🇦 Afrique du Sud | **5** | █████ |
| **3** | 🇳🇬 Nigeria | **4** | ████ |
| **4** | 🇩🇿 Algérie | **4** | ████ |
| **5** | 🇹🇳 Tunisie | **4** | ████ |
| **6** | 🇪🇬 Égypte | **2** | ██ |
| **7** | 🇰🇪 Kenya | **1** | █ |
| **8** | 🇧🇯 Bénin | **1** | █ |
| **9** | 🇪🇹 Éthiopie | **1** | █ |
| **10** | 🇸🇳 Sénégal | **1** | █ |
| **11** | 🇺🇬 Ouganda | **1** | █ |
| **–** | 🌍 Multi‑pays Afrique | **1** | █ |


### Répartition des victimes par pays
```mermaid
pie showData
    title Répartition des victimes par pays-Avril 2026
    "🇲🇦 Maroc" : 17
    "🇪🇬 Égypte" : 11
    "🇿🇦 Afrique du Sud" : 8
    "🇳🇬 Nigeria" : 4
    "🇩🇿 Algérie" : 4
    "🇹🇳 Tunisie" : 4
    "🇰🇪 Kenya" : 2
    "🇬🇭 Ghana" : 2
    "🇧🇯 Bénin" : 1
    "🇧🇼 Botswana" : 1
    "🇪🇹 Éthiopie" : 1
    "🇸🇨 Seychelles" : 1
    "🇸🇳 Sénégal" : 1
    "🇺🇬 Ouganda" : 1
    "🇿🇲 Zambie" : 1
    "🌍 Multi pays Afrique" : 1
```

### 📊 Comparaison Ransomwares vs. Fuites de Données par Pays

| Pays | Ransomware | Fuites | Répartition Côte-à-Côte |
| :--- | :---: | :---: | :--- |
| 🇲🇦 Maroc | **2** | **15** | 🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| 🇪🇬 Égypte | **9** | **2** | 🟧🟧🟧🟧🟧🟧🟧🟧🟧 🟦🟦 |
| 🇿🇦 Afrique du Sud | **3** | **5** | 🟧🟧🟧 🟦🟦🟦🟦🟦 |
| 🇳🇬 Nigeria | **0** | **4** | 🟦🟦🟦🟦 |
| 🇩🇿 Algérie | **0** | **4** | 🟦🟦🟦🟦 |
| 🇹🇳 Tunisie | **0** | **4** | 🟦🟦🟦🟦 |
| 🇰🇪 Kenya | **1** | **1** | 🟧 🟦 |
| 🇬🇭 Ghana | **2** | **0** | 🟧🟧 |
| 🇧🇯 Bénin | **0** | **1** | 🟦 |
| 🇧🇼 Botswana | **1** | **0** | 🟧 |
| 🇪🇹 Éthiopie | **0** | **1** | 🟦 |
| 🇸🇨 Seychelles | **1** | **0** | 🟧 |
| 🇸🇳 Sénégal | **0** | **1** | 🟦 |
| 🇺🇬 Ouganda | **0** | **1** | 🟦 |
| 🇿🇲 Zambie | **1** | **0** | 🟧 |
| 🌍 Multi‑pays Afrique | **0** | **1** | 🟦 |
| **Total (60)** | **20** | **40** | *Légende : 🟧 Ransomware \| 🟦 Fuite de Données* |

### 📊 Synthèse des secteurs ciblés par pays

| Rang | Pays | Vol. Secteurs | Secteurs ciblés & Répartition |
| :---: | :--- | :--- | :--- |
| **1** | 🇲🇦 Maroc | ███████████████ | Éducation (**3**), Santé (**3**), Sports (**3**), Gouvernement (**2**), Finance (**2**), Identité numérique (**1**), Services (**1**), Agroalimentaire/Retail (**1**), Données personnelles (**1**) |
| **2** | 🇪🇬 Égypte | █████████ | Éducation (**2**), Énergie (**2**), Finance (**1**), Automobile (**1**), Ingénierie (**1**), Manufacture (**1**), Construction (**1**) |
| **3** | 🇿🇦 Afrique du Sud | ███████ | E‑commerce (**2**), Gouvernement (**2**), Éducation (**1**), Télécoms (**1**), Tourisme (**1**), Agroalimentaire (**1**) + *Accès gouv. multi‑pays* |
| **4** | 🇳🇬 Nigeria | ████ | Gouvernement (**3**), ONG (**1**) + *Accès gouv. multi‑pays* |
| **5** | 🇩🇿 Algérie | ████ | Gouvernement (**2**), Assurance (**1**), Sports (**1**) |
| **6** | 🇹🇳 Tunisie | ████ | E‑commerce (**1**), Éducation (**1**), Services (**1**), Réseau social (**1**) |
| **7** | 🇰🇪 Kenya | ██ | Gouvernement (**1**), Aviation (**1**) |
| **8** | 🇬🇭 Ghana | ██ | Santé (**1**), Finance (**1**) |
| **9** | 🇧🇯 Bénin | █ | Gouvernement (**1**) |
| **10** | 🇧🇼 Botswana | █ | Éducation (**1**) |
| **11** | 🇪🇹 Éthiopie | █ | Énergie (**1**) |
| **12** | 🇸🇳 Sénégal | █ | Gouvernement (**1**) |
| **13** | 🇸🇨 Seychelles | █ | Gouvernement (**1**) |
| **14** | 🇺🇬 Ouganda | █ | Gouvernement (**1**) |
| **15** | 🇿🇲 Zambie | █ | Assurance (**1**) |
| **–** | 🌍 Angola | █ | *Accès gouvernemental multi‑pays (incident combiné)* |

**Répartition des ransomwares par pays - Avril 2026**

```mermaid
pie showData
    title Répartition des ransomwares par pays
    "🇪🇬 Égypte" : 9
    "🇿🇦 Afrique du Sud" : 3
    "🇲🇦 Maroc" : 2
    "🇬🇭 Ghana" : 2
    "🇰🇪 Kenya" : 1
    "🇧🇼 Botswana" : 1
    "🇸🇨 Seychelles" : 1
    "🇿🇲 Zambie" : 1
```

**Fuites de données par pays - Avril 2026**

```mermaid
pie showData
    title Répartition des fuites de données par pays
    "🇲🇦 Maroc" : 15
    "🇿🇦 Afrique du Sud" : 5
    "🇳🇬 Nigeria" : 4
    "🇩🇿 Algérie" : 4
    "🇹🇳 Tunisie" : 4
    "🇪🇬 Égypte" : 2
    "🇰🇪 Kenya" : 1
    "🇧🇯 Bénin" : 1
    "🇪🇹 Éthiopie" : 1
    "🇸🇳 Sénégal" : 1
    "🇺🇬 Ouganda" : 1
    "🌍 Multi pays Afrique" : 1
```

### 📊 Répartition géographique des incidents par région

| Région | Total Incidents | Ransomware | Fuites | Répartition Côte-à-Côte |
| :--- | :---: | :---: | :---: | :--- |
| **Afrique du Nord** | **36** (58,1 %) | 11 | 25 | 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦  |
| **Afrique australe** | **11** (17,7 %) | 5 | 6 | 🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦|
| **Afrique de l'Ouest** | **9** (14,5 %) | 2 | 7 | 🟧🟧 🟦🟦🟦🟦🟦🟦🟦 |
| **Afrique de l'Est** | **5** (8,1 %) | 2 | 3 | 🟧🟧 🟦🟦🟦 |
| **Afrique centrale** | **1** (1,6 %) | 0 | 1 | 🟦 |
| **Total régionalisé** | **62** | **20** | **42** ||

*Légende : 🟧 Ransomware | 🟦 Fuites de données (Data Leaks)*
*Note : Le total régionalisé atteint 62 car l’incident multi-pays (Angola / Nigeria / Afrique du Sud), compté comme un seul incident dans le total global de 60, est ventilé par zones géographiques afin de refléter son impact territorial réel.*

### 📊 Répartition des cyberattaques par secteur d'activité

| Secteur d'activité | Incidents | Part (%) | Graphique |
| :--- | :---: | :---: | :--- |
| **Gouvernement / Administration** | **15** | 25,0 % | ███████████████ |
| **Éducation / Université** | **8** | 13,3 % | ████████ |
| **Santé / Médical** | **4** | 6,7 % | ████ |
| **Finance / Banque** | **4** | 6,7 % | ████ |
| **Sports / Fédérations** | **4** | 6,7 % | ████ |
| **E-commerce / Retail** | **3** | 5,0 % | ███ |
| **Pétrole & Énergie** | **3** | 5,0 % | ███ |
| **Télécommunications** | **1** | 1,7 % | █ |
| **Autres** *(Secteurs diffus)* | **18** | 30,0 % | ██████████████████ |
| **Total** | **60** | **100 %** | |

```mermaid
pie showData
    title Répartition sectorielle des incidents - Avril 2026
    "🏛️ Gouvernement / Administration" : 15
    "🎓 Éducation / Université" : 8
    "🏥 Santé / Médical" : 4
    "💰 Finance / Banque" : 4
    "🛒 E-commerce / Retail" : 3
    "⚽ Sports / Fédérations" : 4
    "⛽ Pétrole & Énergie" : 3
    "📡 Télécommunications" : 1
    "🏭 Autres secteurs" : 18
```


### 📊 Acteurs de menaces les plus actifs

| Acteur de menace / Groupe | Incidents | Activité dominante | Graphique & Méthode |
| :--- | :---: | :--- | :--- |
| **Grubder** | **7** | Fuites de données | 🟦🟦🟦🟦🟦🟦🟦 |
| **Payload** | **4** | Ransomware | 🟧🟧🟧🟧 |
| **APT73 / BASHE** | **4** | Ransomware | 🟧🟧🟧🟧 |
| **TheGentlemen** | **4** | Ransomware | 🟧🟧🟧🟧 |
| **Krybit** | **3** | Ransomware | 🟧🟧🟧 |
| **Anisanas2** | **3** | Fuites de données | 🟦🟦🟦 |
| **DragonForce** | **2** | Ransomware | 🟧🟧 |
| **LockBit5** | **2** | Ransomware | 🟧🟧 |
| **Rihana** | **2** | Fuites de données | 🟦🟦 |
| **wh6ami** | **2** | Fuites de données | 🟦🟦 |
| **dark07x** | **2** | Fuites de données | 🟦🟦 |
| **NormalLeVrai** | **2** | Fuites de données | 🟦🟦 |

*Légende : 🟧 Ransomware \| 🟦 Fuite de Données*

```mermaid
pie showData
    title Acteurs les plus actifs - Avril 2026
    "Grubder (7)" : 7
    "Payload (4)" : 4
    "APT73/BASHE (4)" : 4
    "TheGentlemen (4)" : 4
    "Krybit (3)" : 3
    "Anisanas2 (3)" : 3
    "DragonForce (2)" : 2
    "LockBit5 (2)" : 2
    "Rihana (2)" : 2
    "wh6ami (2)" : 2
    "dark07x (2)" : 2
    "NormalLeVrai (2)" : 2
    "Autres (23)" : 23
```
*Parmi les acteurs ayant réalisé un seul incident figurent notamment Nullsec/0xLei, MDGhost, RubiconH4ck, Keymous, xNov, superduper1, w00l_ysh1, BlueEx, Sejjil, forrest, mecrobyte, et d’autres (voir la liste complète des victimes).*

## 4. Vue d’ensemble pays par pays

> Tous les éléments présentés proviennent d’incidents revendiqués publiquement. Les revendications restent non confirmées sauf preuve indépendante.

### 🇲🇦 Maroc (17 incidents : 2 ransomwares, 15 fuites de données)

Le Maroc est le pays le plus touché en avril avec 17 incidents, alimentés par une vague intense d’activité de courtiers en données. La fuite la plus critique concerne le **Laboratoire National Mohammed VI (LNM6)** (anisanas2) : 100 Go de rapports médicaux PDF exposant des résultats de dépistage HIV, HPV, IST, tuberculose, données hormonales et génétiques, incluant des données pédiatriques et néonatales. La **base de données du personnel du Palais Royal** (Rihana, 3 300 enregistrements avec numéros CNIE et adresses physiques) soulève des risques de harponnage et d’espionnage ciblé de personnels sensibles. La **CNOPS** (plus de 3 millions d’enregistrements) expose les identités complètes et les numéros CIN des assurés. L’**OFPPT** (anisanas2, plus de 400 000 profils) et l’**Université Al Akhawayn** ont également été compromis. La fédération royale marocaine de football (FRMF, MDGhost, 1,2 To) contient des données de mineurs. Un jeu de 4 millions d’adresses email marocaines a aussi été publié à des fins de spam et de phishing. Côté ransomware : Equatorial Coca-Cola Bottling (worldleaks) et planetsport.ma (LockBit 5.0).

### 🇪🇬 Égypte (11 incidents : 9 ransomwares, 2 fuites de données)

L’Égypte enregistre la plus forte concentration de ransomwares en avril avec 9 attaques. Le groupe **payload** a frappé 4 victimes : United Finance Egypt (IFNB, leasing/affacturage), El Wastani Petroleum (pétrole/gaz), Better House (immobilier), et Oriental Weavers (plus grand fabricant mondial de tapis). **APT73/BASHE** a revendiqué Alexandria Petroleum (raffinerie pétrolière publique). **The Gentlemen** a ciblé ACE Consulting Engineers (management de projets, 35+ pays). **LockBit 5.0** a frappé un concessionnaire Mercedes-Benz. **DragonForce** a touché AUG Pharma. L’activité data leak reste moindre mais comprend deux fuites universitaires majeures signées Grubder : Université du Caire (284 000 enregistrements avec numéros d’identité nationale) et Université Ain Shams (563 000 enregistrements avec données d’authentification).

### 🇿🇦 Afrique du Sud (8 incidents : 3 ransomwares, 5 fuites de données)

L’Afrique du Sud enregistre un mélange significatif de ransomwares et d’activité de courtiers en données. La fuite la plus critique est **Pick n Pay ASAP / Bottles.com** (p4pr1k4) : données de cartes bancaires VISA, Mastercard et 3DS, coordonnées GPS de livraison et mots de passe. **Buffalo City Metropolitan Municipality** et le **Département des Routes et des Travaux publics du Cap-Nord** (tous deux par wh6ami) ont exposé des journaux administratifs, des données d’appels d’offres et des dossiers d’employés municipaux. Grubder a vendu deux bases supplémentaires : Takealot.com (adresses de livraison avec instructions d’accès domicile) et MySchool SA (437 000 dossiers étudiants). Les groupes DragonForce (Singita, lodges de luxe), Krybit (MegaSurf ISP) et The Gentlemen (Sunspray Food) ont tous frappé en avril.

### 🇳🇬 Nigeria (4 incidents : 0 ransomware, 4 fuites de données)

Le Nigeria enregistre quatre fuites de données à fort impact. Le **Ministère du Commerce et de l’Industrie de l’État d’Oyo** (AckLine) : 275 000 cartes d’identification commerciale (21,5 Go) incluant des photos biométriques, créant des risques d’usurpation d’identité et de fraude KYC. L’**EFCC** (agence anti-corruption nigériane, ki4t/Nullsec Nigeria) a eu un dump SQL partiel publié exposant des données d’agents, des IPs internes et des hachages bcrypt. La **Federal Housing Authority** (0xLei/Nullsec) a eu son code source et ses fichiers de configuration divulgués. Welfare.org.ng (NormalLeVrai) a été compromise avec code source, sauvegardes et plus de 12 000 enregistrements.

### 🇩🇿 Algérie (4 incidents : 0 ransomware, 4 fuites de données)

L’Algérie a été exclusivement ciblée par des courtiers en données en avril. **Algeria Post** (BlueEx, plus de 500 000 enregistrements) est particulièrement critique : la fuite inclut des photographies de cartes nationales d’identité algériennes, permettant la fraude documentaire, le SIM swapping et l’usurpation d’identité à grande échelle. **Inter Partner Assistance Algérie** (dark07x) a exposé des rapports d’accidents automobiles, cartes d’identité nationale et documents d’assurance. La **Ligue Régionale de Football d’Alger** (dark07x) a eu les données de joueurs et entraîneurs exposées via la plateforme Foot’Up. Le **Ministère de la Culture** (Grubder, 247 000 enregistrements) a également été compromis.

### 🇹🇳 Tunisie (4 incidents : 0 ransomware, 4 fuites de données)

La Tunisie a été touchée par quatre incidents de courtiers en données. Grubder a vendu deux bases CRM volumineuses : **Fatales.tn** (431 000 clients avec historique de réservations, données de fidélité VIP et informations de paiement) et **NSSTunis** (312 000 enregistrements avec données démographiques et marketing). **Tawjih.tn**, une plateforme d’orientation académique, a été compromise par mecrobyte. **Exscape App** (forrest) a exposé 5 000 profils incluant des coordonnées GPS et potentiellement des comptes de mineurs.

### 🇰🇪 Kenya (2 incidents : 1 ransomware, 1 fuite de données)

Le Kenya a fait face à des attaques ciblant des infrastructures publiques critiques. L’**IFMIS** (système national de gestion financière pour tous les niveaux gouvernementaux) a été revendiqué par APT73/BASHE, représentant une menace directe pour les opérations financières gouvernementales. La **Kenya Airports Authority** (KAA, RubiconH4ck) : revendication de 2 To de données incluant des systèmes d’information aéronautiques, posant des risques sur la confidentialité et la sécurité opérationnelle des infrastructures de transport.

### 🇬🇭 Ghana (2 incidents : 2 ransomwares, 0 fuite de données)

Le Ghana enregistre deux incidents ransomware. L’**International Maritime Hospital** de Tema (The Gentlemen) est un établissement de santé affilié au gouvernement. **Provident Insurance** (APT73/BASHE) est une firme de gestion de patrimoine. Ces deux secteurs illustrent l’expansion du groupe APT73/BASHE au-delà de l’Afrique du Nord et de l’Est vers les industries de services ouest-africaines.

### 🇪🇹 Éthiopie (1 incident : 0 ransomware, 1 fuite de données)

**National Oil Ethiopia PLC** (ByteToBreach, plus de 800 Go de base de données ERP) représente l’une des revendications techniquement les plus détaillées du mois. L’acteur décrit une chaîne d’intrusion complète allant de l’exploitation initiale de MS Exchange ProxyLogon jusqu’au déploiement de ransomware, avec accès aux données clients, contrats, salaires, comptes email et systèmes ERP sensibles.

### 🇧🇼 Botswana (1 incident : 1 ransomware)

Livingstone Kolobeng College, une école secondaire privée de Gaborone, a été revendiquée par Krybit.

### 🇸🇨 Seychelles (1 incident : 1 ransomware)

Le portail e-gouvernemental officiel **egov.sc** a été revendiqué par APT73/BASHE, ciblant les services numériques publics nationaux.

### 🇸🇳 Sénégal (1 incident : 0 ransomware, 1 vente d’accès)

**DGCPT** (Direction générale de la comptabilité publique et du Trésor, w00l_ysh1) : identifiants VPN, accès administrateur Windows Server, accès Contrôleur de Domaine et un réseau de plus de 200 ordinateurs mis en vente (VPN 500 $, serveurs 2 000 $, DC 15 000 $). Si authentique, cela constitue une compromission avancée de l’infrastructure financière souveraine du Sénégal.

### 🇧🇯 Bénin (1 incident : 0 ransomware, 1 fuite de données)

**CNSS Bénin** (Caisse nationale de sécurité sociale, NormalLeVrai) : 7,1 Go de données de messagerie incluant environ 5 993 emails, 9 019 pièces jointes et plus de 31 000 fichiers. Contenu : cartes de pension, documents d’identité, passeports, données RH, données médicales et informations bancaires d’assurés et retraités.

### 🇺🇬 Ouganda (1 incident : 0 ransomware, 1 fuite de données)

**Ministère de l’Agriculture de l’Ouganda - plateforme E-Extension** (vicmeow) : dump CSV exposant emails, noms, numéros de téléphone, mots de passe en clair et un token API de passerelle SMS, permettant l’abus direct d’identifiants et des opérations de messagerie de masse.

### 🇿🇲 Zambie (1 incident : 1 ransomware)

**ZSIC Life** (assurance vie et gestion de patrimoine) a été revendiquée par Krybit.

### Incident multi-pays

| Incident | Acteur | Type d’artefact | Pays concernés |
| :--- | :--- | :--- | :--- |
| Vente d’accès à des messageries et panneaux d’administration gouvernementaux | superduper1 | Accès admin revendiqué : panneaux eGov, messageries policières, accès militaires/renseignement | 🇦🇴 Angola, 🇿🇦 Afrique du Sud, 🇳🇬 Nigeria |

---

## 5. Analyse détaillée par type d’incident

### 5.1 Ransomware (20 incidents)

| Rang | Pays | Attaques | Graphique | Acteurs principaux |
| :---: | :--- | :---: | :--- | :--- |
| **1** | 🇪🇬 Égypte | **9** | █████████ | payload (4), dragonforce, lockbit5, thegentlemen, apt73/bashe |
| **2** | 🇿🇦 Afrique du Sud | **3** | ███ | dragonforce, krybit, thegentlemen |
| **3** | 🇲🇦 Maroc | **2** | ██ | worldleaks, lockbit5 |
| **4** | 🇬🇭 Ghana | **2** | ██ | thegentlemen, apt73/bashe |
| **5** | 🇰🇪 Kenya | **1** | █ | apt73/bashe |
| **6** | 🇧🇼 Botswana | **1** | █ | krybit |
| **7** | 🇸🇨 Seychelles | **1** | █ | apt73/bashe |
| **8** | 🇿🇲 Zambie | **1** | █ | krybit |

**Observations :** Le groupe ransomware **payload** a lourdement ciblé l’économie égyptienne (finance, pétrole, industrie). Le groupe **apt73/bashe** s’est étendu des gouvernements (Seychelles, Kenya) aux assurances et au pétrole.



### 5.2 Fuites de données et ventes d'accès (40 incidents)

| Rang | Pays | Incidents | Graphique | Acteurs principaux |
| :---: | :--- | :---: | :--- | :--- |
| **1** | 🇲🇦 Maroc | **15** | ███████████████ | anisanas2, Sejjil, Rihana, MDGhost, Keymous, xNov, bxxxx1 |
| **2** | 🇿🇦 Afrique du Sud | **5** | █████ | wh6ami, p4pr1k4, Grubder |
| **3** | 🇩🇿 Algérie | **4** | ████ | dark07x, BlueEx, Grubder |
| **4** | 🇹🇳 Tunisie | **4** | ████ | Grubder, mecrobyte, forrest |
| **5** | 🇳🇬 Nigeria | **4** | ████ | NormalLeVrai, 0xLei, ki4t, AckLine |
| **6** | 🇪🇬 Égypte | **2** | ██ | Grubder |
| **–** | 🌍 Autres | **6** | ██████ | Divers (voir liste des victimes) |

**Observations :** **Grubder** a vendu des bases allant de petites CRM (Customer Relationship Management) à des universités. **anisanas2** a ciblé la santé et le football marocains. **dark07x** a exposé des cartes d’identité et des dossiers automobiles. La fuite **Pick n Pay ASAP / Bottles.com** inclut des données de paiement complètes.

## 6. Impact sectoriel

| Secteur d'activité | Incidents | Part (%) | Impact visuel |
| :--- | :---: | :---: | :--- |
| **Gouvernement / Administration** | **15** | 25,0 % | ███████████████ |
| **Éducation / Université** | **8** | 13,3 % | ████████ |
| **Santé / Médical** | **4** | 6,7 % | ████ |
| **Finance / Banque** | **4** | 6,7 % | ████ |
| **Sports / Fédérations** | **4** | 6,7 % | ████ |
| **E-commerce / Retail** | **3** | 5,0 % | ███ |
| **Pétrole & Énergie** | **3** | 5,0 % | ███ |
| **Télécommunications** | **1** | 1,7 % | █ |
| **Autres** *(Secteurs diffus)* | **18** | 30,0 % | ██████████████████ |

**Observations clés :**
* **Dominance du secteur public :** Le bloc secteur public (Gouvernement + Éducation) concentre à lui seul **38,3 %** des incidents.
* **Données critiques convoitées :** Les données de santé restent une cible hautement stratégique pour les attaquants (incidents notables touchant la CNOPS, LNM6, Chezpara.ma et SUPTECH SANTÉ).
* **Nouvelles tendances :** Les fédérations et ligues sportives (FRMF, FRMT, LRFA) émergent désormais comme des cibles de choix pour l'exfiltration et la revente de données.

## 7. Profil des acteurs de menaces

| Acteur de menace / Groupe | Type | Incidents | Graphique | Cibles principales |
| :--- | :--- | :---: | :--- | :--- |
| **Grubder** | Data broker | **7** | ███████ | Gouvernements, universités, e‑commerce |
| **payload** | Ransomware | **4** | ████ | Finance, pétrole, industrie |
| **APT73 / BASHE** | Ransomware | **4** | ████ | e‑gouvernement, pétrole, assurance |
| **TheGentlemen** | Ransomware | **4** | ████ | Santé, agroalimentaire, ingénierie |
| **anisanas2** | Fuite de données | **3** | ███ | Éducation, santé, football marocain |
| **dark07x** | Fuite de données | **2** | ██ | Assurance, football algérien |
| **DragonForce** | Ransomware | **2** | ██ | Tourisme, industrie pharmaceutique |
| **LockBit5** | Ransomware | **2** | ██ | Automobile, sports |
| **wh6ami** | Fuite de données | **2** | ██ | Municipalités sud-africaines |
| **Rihana** | Fuite de données | **2** | ██ | Maison royale, emails |
| **NormalLeVrai** | Fuite de données | **2** | ██ | ONG, gouvernement (sécurité sociale) |

**Acteurs émergents :** * **wh6ami** (accès d'administration municipale)
* **forrest** (données d'applications mobiles)
* **mecrobyte** (éducation tunisienne)
* **Keymous** (tennis marocain)

### 7.1 Niveau de risque

| Pays | Risque |
|------|--------|
| Maroc | 🔴 Critique |
| Égypte | 🔴 Élevé |
| Afrique du Sud | 🔴 Élevé |
| Nigeria | 🟠 Moyen-Élevé |
| Algérie | 🟠 Moyen |
| Tunisie | 🟠 Moyen |
| Autres | 🟡 Faible-Moyen |

## 8. Tendances clés et lacunes de renseignement

### 📈 Tendances majeures des cybermenaces

* **Explosion de l'activité des Data Brokers :** On observe une monétisation agressive des données exfiltrées. Un seul acteur prolifique (**Grubder**) totalise à lui seul 7 victimes en un mois, revendant indifféremment des fichiers d'inscription universitaire ou des bases de données CRM d'entreprises.
* **Marchandisation des documents d'identité (KYC) :** Les pièces d'identité officielles deviennent des produits de commodité sur le *dark web*. Plusieurs publications d'acteurs de menaces proposaient des lots de passeports scannés, de cartes nationales d'identité et de dossiers de conformité KYC (notamment via des fuites ciblant les *Documents d'identité marocains*, *Algérie Poste*, ou encore *Inter Partner Assistance*).
* **Vente d'accès initiaux visant les infrastructures étatiques :** Les Initial Access Brokers (IAB) haussent considérablement leur niveau d'impact. Des profils comme **superduper1** (accès étatiques multi-pays) ou **w00l_ysh1** (Trésor Public du Sénégal) ont mis aux enchères des accès à privilèges élevés, incluant le compromis direct de Contrôleurs de Domaine (Domain Controllers).
* **Diversification du ciblage par Ransomware :** Les groupes d'extorsion traditionnels ne se cantonnent plus aux entreprises de services standard. Le groupe **payload**, par exemple, s'est diversifié de manière agressive dans l'industrie lourde, l'immobilier, l'automobile et les infrastructures énergétiques et pétrolières.
* **Compromission d'E-commerce et fuites de données de paiement :** Les failles applicatives exposent lourdement la chaîne monétique. L'incident ayant touché **Pick n Pay ASAP / Bottles.com** a révélé la fuite de numéros de cartes complets et de logs de validation 3D-Secure (3DS), illustrant un défaut majeur de conformité PCI-DSS dans la région.
* **Aspiration ciblée de messageries officielles (Mailbox Scraping) :** L'exfiltration d'archives de messagerie complètes s'affirme comme une méthode de choix pour contourner la persistance complexe. Le cas de la **CNSS Bénin**, dont l'intégralité de la boîte mail officielle a été siphonnée, a exposé des milliers de cartes de pensionnés et de certificats de vie.

## 9. Cartographie MITRE ATT&CK (contextuelle)

| Phase | Identifiant | Nom de la technique | Contexte / Incidents |
| :--- | :---: | :--- | :--- |
| **Accès Initial / Persistance** | **T1078** | Valid Accounts (Comptes valides) | Pick n Pay, Royal Palace, Kenya Airports, DGCPT |
| **Collecte** | **T1005** | Data from Local System | Pick n Pay/Bottles, Royal Palace DB, CNSS Bénin |
| **Collecte** | **T1114.002** | Remote Email Collection | CNSS Bénin |
| **Élévation de Privilèges** | **T1068** | Exploitation for Privilege Escalation | DGCPT Sénégal |
| **Déplacement Latéral** | **T1021.002** | SMB/Windows Admin Shares (RDP) | DGCPT Sénégal |
| **Exfiltration** | **T1041** | Exfiltration Over C2 Channel | Pick n Pay/Bottles, Kenya Airports Authority |

> 🔑 **Techniques génériques prédominantes observées sur la région :**
> * **T1190** – Exploit Public-Facing Application (Vecteur d'entrée principal sur les portails web)
> * **T1078** – Valid Accounts (Exploitation d'accès IAB et de secrets OAuth fuyards)
> * **T1041** – Exfiltration Over C2 Channel (Extraction massive de bases de données et CRM)
> * **T1486** – Data Encrypted for Impact (Phase finale de chiffrement par ransomware)

---

## 10. Recommandations globales

* **Gouvernements :** Imposer l'authentification multifacteur (MFA) forte sur tous les portails externes, auditer régulièrement les architectures e-gov et surveiller activement les places de marché cyber pour détecter la vente d'accès (IAB).
* **Secteur Financier & E-commerce :** Durcir l'application des contrôles PCI-DSS, généraliser la tokenisation des données de paiement au repos et déployer une surveillance comportementale des transactions.
* **Établissements d'Enseignement & de Santé :** Segmenter strictement les réseaux pour isoler les bases de données sensibles, chiffrer les données au repos et tester régulièrement les plans de réponse aux incidents (tabletop exercises).
* **Particuliers :** Redoubler de vigilance face aux campagnes de phishing ciblées et proscrire la réutilisation des mots de passe (particulièrement après les fuites massives de listes de diffusion locales).

---

## 11. Recommandations SOC tactiques

* **[T1078] Détection d'abus de privilèges :** Configurer des alertes sur les connexions géographiques anormales ou les sessions simultanées sur les portails d'administration étatiques.
* **[T1005] Surveillance des exfiltrations locales :** Mettre en place des règles de détection (DLP) sur les téléchargements de volumes massifs de données depuis les bases médicales ou universitaires.
* **[T1041] Analyse des flux sortants :** Établir une ligne de base (baseline) du trafic réseau sortant pour identifier des anomalies de volume vers des adresses IP externes non certifiées.
* **[Banque] Surveillance des anomalies de guichet :** Implémenter des profils de corrélation en temps réel pour détecter les vagues de retraits GAB/DAB inhabituelles ou les modifications suspectes de plafonds.

---

## 12. Recommandations stratégiques

* **Écosystème de Threat Intelligence :** Renforcer les partenariats public-privé de partage de renseignements sur les menaces, notamment pour anticiper les ventes de accès par les Initial Access Brokers (IAB).
* **Régulation sectorielle :** Durcir le cadre réglementaire des plateformes de paiement tierces en exigeant une conformité PCI-DSS stricte et vérifiée.
* **Résilience des infrastructures critiques :** Rendre obligatoire le maintien de capacités SOC opérationnelles et de mécanismes de notification d'incidents pour les opérateurs d'importance vitale (OIV).

---

## 13. Conclusion

Le mois d'avril 2026 s'est distingué par une accélération marquée des opérations des data brokers et par des intrusions profondes ciblant les infrastructures étatiques, éducatives et médicales africaines. L'expansion du commerce de documents d'identité et des ventes d'accès confirme la structuration d'une économie souterraine mature. Si le Maroc, l'Égypte et l'Afrique du Sud restent l'épicentre de cette activité, l'émergence de nouveaux foyers (Algérie, Tunisie, Kenya) appelle à une vigilance accrue. AFRINTEL poursuivra le suivi et la documentation de ces dynamiques de menaces.

**AFRINTEL** – African Cyber Threat Intelligence  
🔗 [Dépôt GitHub AFRINTEL](https://github.com/Hatchepsoute/AFRINTEL)
