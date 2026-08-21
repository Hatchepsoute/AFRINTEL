[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Période](https://img.shields.io/badge/Période-Mai%202026-lightgrey)
![Victimes](https://img.shields.io/badge/Victimes-103-critical)
![Ransomwares](https://img.shields.io/badge/Ransomwares-17-red)
![Fuites](https://img.shields.io/badge/Fuites%20de%20données-43-orange)
![Pays](https://img.shields.io/badge/Pays%20touchés-18-blueviolet)
![Intel](https://img.shields.io/badge/Type-Statistiques%20CTI-purple)

# AFRINTEL - Statistiques cyber Afrique
## Mai 2026

👉🏾 [**English version available here**](./README.md)

## Note méthodologique

Ces statistiques couvrent les publications observées dans le périmètre AFRINTEL pour mai 2026. Chaque fiche conserve le statut documenté dans le fichier des victimes.

Les trois incidents multi-pays (Resume Docs, DHIS2, Scans de passeports) sont comptabilisés comme **1 incident chacun** dans le total global de 103. Dans les fichiers victimes, chaque entrée liste désormais les pays concernés explicitement plutôt qu'un label générique "Multi-pays", afin de permettre l'identification par pays. Dans le tableau d'exposition géographique (section 2.2), chaque pays touché est listé individuellement. La somme des expositions par pays dépasse donc le total de 103 incidents.

---

## 1. Synthèse statistique

| Indicateur | Valeur |
|---|---:|
| Total incidents | 103 |
| Publications ou divulgations ransomware | 17 |
| Fuites de données / ventes d'accès | 43 |
| Pays touchés | 18 (12 directs + 6 via incidents multi-pays) |
| Acteurs ou sources nommés distincts | 31 |
| Pays le plus touché | Égypte |
| Principal pays ransomware | Égypte |
| Principal pays fuites de données | Afrique du Sud |

### Répartition globale

| Type d'incident | Nombre | Pourcentage |
|---|---:|---:|
| Ransomware | 17 | 16,8 % |
| Fuites de données / ventes d'accès | 43 | 40,6 % |
| Revendications DDoS | 43 | 42,6 % |
| **Total** | **103** | **100 %** |

```mermaid
pie showData
    title Répartition globale des incidents - Mai 2026
    "Ransomware" : 17
    "Fuites de données et ventes d'accès" : 43
    "Revendications DDoS" : 43
```

---

## 2. Répartition des victimes par pays

### 2.1 Incidents directs par pays

Ces 98 incidents ont une seule victime identifiée par pays. Les 3 incidents multi-pays sont détaillés en section 2.2.

| Pays | Incidents |
|---|---:|
| 🇪🇬 Égypte | 17 |
| 🇿🇦 Afrique du Sud | 14 |
| 🇲🇦 Maroc | 51 |
| 🇹🇳 Tunisie | 5 |
| 🇳🇬 Nigéria | 3 |
| 🇩🇿 Algérie | 2 |
| 🇹🇿 Tanzanie | 2 |
| 🇪🇹 Éthiopie | 1 |
| 🇬🇭 Ghana | 1 |
| 🇨🇮 Côte d'Ivoire | 1 |
| 🇰🇪 Kenya | 1 |
| 🇸🇳 Sénégal | 1 |
| **Sous-total (directs)** | **98** |

```mermaid
xychart
    title "Incidents directs par pays - Mai 2026"
    x-axis ["Égypte","Afrique du Sud","Maroc","Tunisie","Nigéria","Algérie","Tanzanie","Éthiopie","Ghana","Côte d'Ivoire","Kenya","Sénégal"]
    y-axis "Incidents" 0 --> 17
    bar [17,14,51,5,3,2,2,1,1,1,1,1]
```

### 2.2 Exposition géographique des incidents multi-pays

3 incidents ont touché plusieurs pays simultanément. Chacun est comptabilisé une seule fois dans le total global de 103, mais expose plusieurs pays.

| Incident | Acteur | Pays concernés |
|---|---|---|
| Fuite de CV (Resume docs) | attackercompany | 🇰🇪 Kenya, 🇪🇹 Éthiopie, 🇳🇬 Nigéria, 🇿🇼 Zimbabwe |
| DHIS2 / Ministères de la Santé | Keymous | 🇲🇿 Mozambique, 🇱🇷 Liberia, 🇳🇬 Nigéria, 🇹🇬 Togo, 🇸🇱 Sierra Leone |
| Scans de passeports | raylie | 🇪🇬 Égypte, 🇱🇾 Libye |

### 2.3 Exposition géographique totale (18 pays)

> La colonne "Exposition multi-pays" comptabilise le nombre d'incidents multi-pays touchant chaque pays. Les sommes de colonnes dépassent 103 car ces incidents concernent plusieurs pays simultanément.

| Pays | Incidents directs | Exposition multi-pays | Exposition totale |
|---|---:|---:|---:|
| 🇪🇬 Égypte | 17 | 1 (Scans passeports) | 17 |
| 🇿🇦 Afrique du Sud | 14 | 0 | 14 |
| 🇲🇦 Maroc | 51 | 0 | 51 |
| 🇹🇳 Tunisie | 5 | 0 | 5 |
| 🇳🇬 Nigéria | 3 | 2 (Resume docs, DHIS2) | 5 |
| 🇩🇿 Algérie | 2 | 0 | 2 |
| 🇹🇿 Tanzanie | 2 | 0 | 2 |
| 🇬🇭 Ghana | 1 | 0 | 0 |
| 🇨🇮 Côte d'Ivoire | 1 | 0 | 0 |
| 🇰🇪 Kenya | 1 | 1 (Resume docs) | 2 |
| 🇸🇳 Sénégal | 1 | 0 | 0 |
| 🇪🇹 Éthiopie | 1 | 1 (Resume docs) | 2 |
| 🇿🇼 Zimbabwe | 0 | 1 (Resume docs) | 1 |
| 🇲🇿 Mozambique | 0 | 1 (DHIS2) | 1 |
| 🇱🇷 Liberia | 0 | 1 (DHIS2) | 1 |
| 🇹🇬 Togo | 0 | 1 (DHIS2) | 1 |
| 🇸🇱 Sierra Leone | 0 | 1 (DHIS2) | 1 |
| 🇱🇾 Libye | 0 | 1 (Scans passeports) | 1 |
| **Total** | **98 incidents directs** | **11 expositions pays** | **18 pays distincts** |

---

## 3. Ransomware vs fuites de données par pays

| Pays | Ransomware | Fuites de données / ventes d'accès | DDoS | Total |
|---|---:|---:|---:|
| 🇪🇬 Égypte | 7 | 9 | 0 | 16 |
| 🇿🇦 Afrique du Sud | 2 | 12 | 0 | 14 |
| 🇲🇦 Maroc | 0 | 8 | 43 | 51 |
| 🇹🇳 Tunisie | 2 | 3 | 0 | 5 |
| 🇳🇬 Nigéria | 3 | 0 | 0 | 3 |
| 🇩🇿 Algérie | 0 | 2 | 0 |
| 🇹🇿 Tanzanie | 0 | 2 | 0 |
| 🇪🇹 Éthiopie | 0 | 1 | 0 |
| 🇬🇭 Ghana | 1 | 0 | 0 |
| 🇨🇮 Côte d'Ivoire | 1 | 0 | 0 |
| 🇰🇪 Kenya | 0 | 1 | 0 |
| 🇸🇳 Sénégal | 1 | 0 | 0 |
| **Sous-total (directs)** | **17** | **38** | **43** | **99 |
| 🇰🇪🇪🇹🇳🇬🇿🇼 Resume docs | 0 | 1 | 0 | 1 |
| 🇲🇿🇱🇷🇳🇬🇹🇬🇸🇱 DHIS2 | 0 | 1 | 0 | 1 |
| 🇪🇬🇱🇾 Scans de passeports | 0 | 1 | 1 |
| **Total** | **17** | **43** | **43** | **103** |

### Ransomware par pays

```mermaid
xychart
    title "Ransomware par pays - Mai 2026"
    x-axis ["Égypte","Nigeria","Tunisie","Afrique du Sud","Ghana","Sénégal","Côte d'Ivoire"]
    y-axis "Ransomware" 0 --> 8
    bar [7,3,2,2,1,1,1]
```

### Fuites de données par pays

```mermaid
xychart
    title "Fuites de données par pays (directs) - Mai 2026"
    x-axis ["Afrique du Sud","Égypte","Maroc","Tunisie","Algérie","Tanzanie","Éthiopie","Kenya"]
    y-axis "Fuites de données" 0 --> 14
    bar [12,9,7,3,2,2,1,1]
```

---

## 4. Répartition géographique

| Région | Pays inclus | Incidents directs | Exposition multi-pays |
|---|---|---:|---:|
| Afrique du Nord | 🇪🇬 Égypte, 🇲🇦 Maroc, 🇹🇳 Tunisie, 🇩🇿 Algérie, 🇱🇾 Libye | 74 | +2 (Égypte via Scans passeports, Libye via Scans passeports) |
| Afrique australe | 🇿🇦 Afrique du Sud, 🇿🇼 Zimbabwe, 🇲🇿 Mozambique | 14 | +2 (Zimbabwe via Resume docs, Mozambique via DHIS2) |
| Afrique de l'Ouest | 🇳🇬 Nigéria, 🇬🇭 Ghana, 🇨🇮 Côte d'Ivoire, 🇸🇳 Sénégal, 🇱🇷 Liberia, 🇹🇬 Togo, 🇸🇱 Sierra Leone | 6 | +5 (Nigéria x2 via Resume docs + DHIS2, Liberia, Togo, Sierra Leone via DHIS2) |
| Afrique de l'Est | 🇹🇿 Tanzanie, 🇰🇪 Kenya, 🇪🇹 Éthiopie | 4 | +2 (Kenya via Resume docs, Éthiopie via Resume docs) |

> Les incidents multi-pays sont comptabilisés une seule fois dans le total global de 103. La colonne "Exposition multi-pays" indique les touches additionnelles par région issues de ces incidents. Total pays distincts : 18 répartis sur 4 régions.

```mermaid
xychart
    title "Incidents directs par région - Mai 2026"
    x-axis ["Afrique du Nord","Afrique australe","Afrique de l'Ouest","Afrique de l'Est"]
    y-axis "Incidents directs" 0 --> 32
    bar [74,14,6,4]
```

---

### 4.3 Revendications DDoS (43 incidents)

La collecte rétrospective de publications Keymous+ ajoute 43 observations marocaines datées entre le 9 et le 28 mai 2026. Chaque cible présente dans une publication de disponibilité datée compte comme un incident ; les captures répétées d une même cible dans la même fenêtre sont dédupliquées. Les résultats Check-Host et Cloudflare documentent une indisponibilité apparente, mais ne prouvent pas indépendamment l origine du trafic, la méthode DDoS ni l impact effectif.

## 5. Répartition sectorielle

| Secteur | Incidents | Pourcentage |
|---|---:|---:|
| Government / Administration | 20 | 35,09 % |
| Ressources humaines / Recrutement | 5 | 8,77 % |
| Industrie / Automobile / Fabrication | 5 | 8,77 % |
| E-commerce / Retail | 4 | 7,02 % |
| Education / University | 3 | 5,26 % |
| Finance / Banking | 3 | 5,26 % |
| Telecommunications | 3 | 5,26 % |
| Oil & Energy | 2 | 3,51 % |
| Alimentation / Boissons / Restauration | 2 | 3,51 % |
| Transport / Logistique | 2 | 3,51 % |
| ONG / Action sociale | 2 | 3,51 % |
| Hôtellerie / Événementiel | 2 | 3,51 % |
| Healthcare / Medical | 1 | 1,75 % |
| Sports / Federations | 1 | 1,75 % |
| Agrégation de données personnelles | 1 | 1,75 % |
| Services aux entreprises | 1 | 1,75 % |
| **Total** | **103** | **100 %** |

```mermaid
xychart
    title "Répartition sectorielle - Mai 2026"
    x-axis ["Gouvernement","RH","Industrie","E-commerce","Éducation","Finance","Télécoms","Énergie","Alimentation","Transport","ONG","Hôtellerie","Santé","Sports","Agrégation","Services"]
    y-axis "Incidents" 0 --> 52
    bar [49,5,5,4,3,8,3,2,2,7,2,2,1,1,1,1,5]
```

---

## 6. Acteurs de menaces les plus actifs

| Acteur / Groupe | Incidents | Type dominant |
|---|---:|---|
| Databasehooligan | 8 | Fuites de données |
| 404Crew Cyber Team | 5 | Fuites de données (coalitions) |
| TheGentlemen | 4 | Ransomware |
| NightSpire | 3 | Ransomware |
| INT3X | 2 | Fuites de données |
| Keymous | 2 | Ventes d'accès / fuites |
| cc5ab | 2 | Fuites de données |
| NullSec Nigeria | 2 | Fuites de données (coalitions) |
| anisanas2 | 2 | Fuites / ventes de données (Maroc) |
| Fiches hors classement affiché | 27 | Mixte |

```mermaid
xychart
    title "Acteurs les plus actifs - Mai 2026"
    x-axis ["Databasehooligan","404Crew CT","TheGentlemen","NightSpire","INT3X","Keymous","cc5ab","NullSec NG","anisanas2","Hors classement"]
    y-axis "Incidents" 0 --> 30
    bar [8,5,4,3,2,2,2,2,2,27]
```

---

## 7. Analyse des tendances CTI

### 7.1 L'Égypte enregistre le plus grand volume ransomware en mai

L'Égypte concentre **7 incidents ransomware**, soit **41,2 %** de l'activité ransomware du mois. NightSpire a revendiqué à lui seul trois cibles égyptiennes en un mois. Les secteurs visés incluent la finance, la restauration, l'industrie chimique, la logistique, l'agriculture et l'hôtellerie.

### 7.2 Afrique du Sud : 14 fiches dont les publications OpSouthAfrica

L'Afrique du Sud enregistre **14 incidents**, dont 12 fuites de données et 2 publications ransomware (PrinzEugen, Stormous). Au moins huit publications concernant des institutions sont associées à la bannière OpSouthAfrica et à des acteurs participants tels que 404Crew Cyber Team, NullSec Nigeria, NullSec Philippines et Infernalis. Les autres fiches impliquent d'autres acteurs.

### 7.3 Le secteur éducatif comme cible stratégique

Les revendications concernant l’éducation égyptienne mentionnent le Ministère de l’Éducation, la Professional Academy for Teachers, l’Université de Mansoura et une base combinée éducation/RH. Les volumes complets revendiqués ne sont pas confirmés indépendamment.

### 7.4 Offres de vente associées à Databasehooligan

Huit jeux de données CRM ou consommateurs structurés concernant des organisations en Tunisie, Afrique du Sud, Égypte et Algérie ont été proposés à la vente par le compte Databasehooligan, à des prix annoncés de 900 à 1 400 dollars chacun. Les fiches sources n'établissent ni plateforme partagée ni vecteur d'accès commun.

### 7.5 Exposition des identifiants gouvernementaux

Les plateformes gouvernementales marocaines (827 000 lignes d'identifiants), la messagerie de la police tanzanienne (10 000+ comptes officiers avec mots de passe en clair) et l'accès administrateur de Stats SA représentent des cibles à forte valeur pour l'ingénierie sociale, la fraude EDR et l'usurpation d'identité institutionnelle.

### 7.6 Compromission multi-pays du système de santé DHIS2

L’offre DHIS2 mentionne cinq pays africains : Mozambique, Liberia, Nigeria, Togo et Sierra Leone. Le Bhoutan et le Honduras figurent dans la source mais sont exclus des statistiques africaines AFRINTEL. AFRINTEL n’a pas testé les identifiants proposés.

---

## 8. Priorités de surveillance SOC

| Priorité | Axe de surveillance |
|---|---|
| Critique | Exposition d'identifiants gouvernementaux et des forces de l'ordre |
| Critique | Patterns d'accès aux bases éducatives (Égypte : Ministère, PAT, Mansoura) |
| Élevée | Exports massifs depuis des plateformes CRM / recrutement (cibles Databasehooligan) |
| Élevée | Indicateurs précoces de ransomware : suppression de copies shadow, chiffrement volumétrique, mouvement latéral RDP/SMB |
| Élevée | Réutilisation d'identifiants exposés dans les fuites gouvernementales marocaines |
| Moyenne | Alignement du profil de cibles NightSpire / TheGentlemen (finance, agroalimentaire, automobile) |
| Moyenne | Anomalies sur les panneaux d'administration DHIS2 / systèmes de santé |
| Moyenne | Annonces de comptes pour fraude EDR multi-pays |

---

## 9. Conclusion

Mai 2026 recense **103 incidents signalés ou revendiqués publiquement** concernant **18 pays africains** lorsque les incidents directs et les expositions multi-pays sont combinés, contre 69 incidents en avril (+34 ; +49,3 %). Les fiches ransomware passent de 20 à 17 (-15,0 %), tandis que les fuites de données et ventes d'accès passent à 43 (0,0 %). L’Égypte et l’Afrique du Sud représentent 31 fiches directes. Les revendications liées à l’éducation, les publications OpSouthAfrica et les offres de vente associées à Databasehooligan sont les principaux schémas observés.

**AFRINTEL** - [African Cyber Threat Intelligence](https://github.com/Hatchepsoute/AFRINTEL)
