[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Période](https://img.shields.io/badge/Période-S1%202026-lightgrey)
![Incidents](https://img.shields.io/badge/Incidents-294-critical)

# Rapport AFRINTEL sur les cybermenaces du premier semestre

## Janvier à juin 2026

👉🏾 [English version](./README_H1.md)

TLP:CLEAR, diffusion publique

## 1. Synthèse exécutive

AFRINTEL a documenté **294 incidents cyber liés à l'Afrique** durant le premier semestre 2026 : **115 incidents ransomware**, **125 fuites de données ou ventes d'accès**, **52 revendications DDoS** et **2 défacements de sites web**.

Sur l'ensemble des 294 fiches, les **fuites / ventes d'accès représentent 42,5 %**, le **ransomware 39,1 %**, les **revendications DDoS 17,7 %** et les **défacements 0,7 %**. Si l'on compare uniquement ransomware et fuites / ventes d'accès, les fuites devancent le ransomware, **52,1 % contre 47,9 %**.

Ce qui compte surtout, c'est l'accélération au deuxième trimestre. Avril et mai à eux seuls totalisent **172 incidents**, soit **58,5 %** du semestre. Juin retombe par rapport aux deux mois précédents, mais le ransomware revient à la parité avec les fuites, avec 20 incidents dans chaque catégorie.

## 2. Méthodologie et périmètre

- **Périmètre géographique :** victimes, institutions, opérations ou données liées à l'Afrique.
- **Période :** du 1er janvier au 30 juin 2026.
- **Sources uniques de vérité :** les six fichiers mensuels `victims.md`.
- **Ransomware :** incident attribué à un groupe ransomware, sans présumer un chiffrement lorsque les éléments disponibles ne le démontrent pas.
- **Fuites et ventes d'accès :** données ou échantillons publiés, ventes de bases, ventes d'identifiants et offres d'accès.
- **Défacement de sites web :** deux incidents, visant des sites de l’État nigérien en janvier et UBA Sénégal en mars.
- **Traitement des éléments :** chaque fiche conserve son statut AFRINTEL. Les publications de victimes, les échantillons accessibles et les publications complètes de données sont décrits selon les éléments documentés dans la fiche mensuelle.

Fichiers sources : [janvier](./01-january/victims.md), [février](./02-february/victims.md), [mars](./03-march/victims.md), [avril](./04-april/victims.md), [mai](./05-may/victims.md), [juin](./06-june/victims.md).

## 3. Vue d'ensemble du semestre

| Indicateur | Valeur |
|---|---:|
| Total des incidents documentés | 294 |
| Ransomware | 115 |
| Fuites de données / ventes d'accès | 125 |
| Revendications DDoS | 52 |
| Défacement de sites web | 2 |
| Mois au volume le plus élevé | Mai, 103 incidents |
| Deuxième mois au volume le plus élevé | Avril, 69 incidents |
| Mois au volume le plus faible | Février, 20 incidents |

**Répartition visuelle**

| Type d'incident | Fiches | Barre |
|---|---:|:---|
| Ransomware | 115 | 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧 |
| Fuites et ventes d'accès | 125 | 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Revendications DDoS | 52 | 🟪🟪🟪🟪 |
| Défacement de sites web | 2 | 🟥 |


<!-- H1_VISUAL_START -->

### Comparaison ransomware, fuites, DDoS et défacement par pays

| Pays | Ransomware | Fuites / accès | DDoS | Défacement | Total | Distribution |
| :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| Maroc | 10 | 36 | 43 | 0 | **89** | 🟧×10 🟦×36 🟪×43 |
| Égypte | 28 | 19 | 8 | 0 | **55** | 🟧×28 🟦×19 🟪×8 |
| Afrique du Sud | 25 | 23 | 0 | 0 | **48** | 🟧×25 🟦×23 |
| Tunisie | 8 | 8 | 0 | 0 | **16** | 🟧×8 🟦×8 |
| Nigeria | 6 | 9 | 0 | 0 | **15** | 🟧×6 🟦×9 |
| Kenya | 7 | 2 | 0 | 0 | **9** | 🟧×7 🟦×2 |
| Algérie | 1 | 7 | 0 | 0 | **8** | 🟧×1 🟦×7 |
| Sénégal | 3 | 2 | 0 | 1 | **6** | 🟧×3 🟦×2 🟥×1 |
| Tanzanie | 3 | 3 | 0 | 0 | **6** | 🟧×3 🟦×3 |
| Ghana | 5 | 0 | 0 | 0 | **5** | 🟧×5 |

### Répartition développée des expositions géographiques par région

| Région | Occurrences ransomware | Occurrences fuites / accès | Occurrences DDoS | Occurrences de défacement | Total des occurrences géographiques |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Afrique du Nord | 49 | 78 | 52 | 0 | 179 |
| Afrique australe | 32 | 30 | 0 | 0 | 62 |
| Afrique de l’Ouest | 16 | 22 | 0 | 2 | 40 |
| Afrique centrale | 1 | 2 | 0 | 0 | 3 |
| Afrique de l’Est | 11 | 15 | 0 | 0 | 26 |
| Océan Indien | 6 | 0 | 0 | 0 | 6 |
| Panafricain / région non précisée | 0 | 1 | 0 | 0 | 1 |
| **Total** | **115** | **148** | **52** | **2** | **317** |

Ce classement régional utilise les **occurrences géographiques**, et non les incidents dédupliqués. Six incidents explicitement multi-pays produisent 29 occurrences pays ; un incident panafricain supplémentaire ne dispose pas d’une attribution régionale suffisamment précise.

**Barres - Top 10 pays - S1 2026**

| Libellé | Incidents | Barre |
|---|---:|:---|
| Maroc | 89 | ██████████████████ |
| Égypte | 55 | ███████████ |
| Afrique du Sud | 48 | ██████████ |
| Tunisie | 16 | ███ |
| Nigeria | 15 | ███ |
| Kenya | 9 | ██ |
| Algérie | 8 | ██ |
| Sénégal | 6 | █ |
| Tanzanie | 6 | █ |
| Ghana | 5 | █ |

### Répartition sectorielle

Cette vue sectorielle couvre **239 fiches normalisées**. Elle ne doit pas être interprétée comme une décomposition des 294 incidents du semestre.

| Secteur | Fiches | Part | Activité |
| :--- | ---: | ---: | :--- |
| Gouvernement / administration | 70 | 29,3 % | ██████████ |
| Industrie / automobile / fabrication / construction / mines | 25 | 10,5 % | ████ |
| Finance / banque | 25 | 10,5 % | ████ |
| Éducation / universités / institutions académiques | 19 | 7,9 % | ███ |
| Technologie / numérique / services aux entreprises / identité numérique | 15 | 6,3 % | ███ |
| Santé / médical | 12 | 5,0 % | ██ |
| Sports / fédérations | 12 | 5,0 % | ██ |
| E-commerce / commerce de détail | 12 | 5,0 % | ██ |
| Autres secteurs normalisés | 49 | 20,5 % | ███████ |
| **Total des fiches normalisées** | **239** | **100 %** | |

**Barres - Top secteurs - S1 2026**

| Libellé | Incidents | Barre |
|---|---:|:---|
| Gouvernement / administration | 70 | ██████████ |
| Industrie / automobile / fabrication / construction / mines | 25 | ████ |
| Finance / banque | 25 | ████ |
| Éducation / universités / institutions académiques | 19 | ███ |
| Technologie / numérique / services aux entreprises / identité numérique | 15 | ███ |
| Santé / médical | 12 | ██ |
| Sports / fédérations | 12 | ██ |
| E-commerce / commerce de détail | 12 | ██ |

🟧 Ransomware | 🟦 Fuites et ventes d’accès | 🟪 DDoS | 🟥 Défacement
<!-- H1_VISUAL_END -->
## 4. Évolution mensuelle

| Mois | Ransomware | Fuites / ventes d’accès | DDoS | Défacement de sites web | Total | Part mensuelle |
|---|---:|---:|---:|---:|---:|---:|
| Janvier | 17 | 3 | 0 | 1 | 21 | 7,1 % |
| Février | 20 | 0 | 0 | 0 | 20 | 6,8 % |
| Mars | 21 | 19 | 0 | 1 | 41 | 13,9 % |
| Avril | 20 | 40 | 9 | 0 | 69 | 23,5 % |
| Mai | 17 | 43 | 43 | 0 | 103 | 35,0 % |
| Juin | 20 | 20 | 0 | 0 | 40 | 13,6 % |
| **S1 2026** | **115** | **125** | **52** | **2** | **294** | **100 %** |

**Barres - Incidents cyber mensuels en Afrique, S1 2026**

| Libellé | Incidents | Barre |
|---|---:|:---|
| Jan | 21 | ████ |
| Fév | 20 | ████ |
| Mar | 41 | ███████ |
| Avr | 69 | ██████████ |
| Mai | 103 | █████████████████ |
| Juin | 40 | ███████ |

### Évolution du ransomware et des fuites

**Barres - Activité ransomware, S1 2026**

| Libellé | Incidents | Barre |
|---|---:|:---|
| Jan | 17 | █████████ |
| Fév | 20 | ██████████ |
| Mar | 21 | ██████████ |
| Avr | 20 | ██████████ |
| Mai | 17 | █████████ |
| Juin | 20 | ██████████ |

**Barres - Fuites de données et ventes d'accès, S1 2026**

| Libellé | Incidents | Barre |
|---|---:|:---|
| Jan | 3 | █ |
| Fév | 0 |  |
| Mar | 19 | █████ |
| Avr | 40 | ██████████ |
| Mai | 43 | ██████████ |
| Juin | 20 | █████ |

## 5. Comparaison des trimestres

| Période | Ransomware | Fuites / ventes d’accès | DDoS | Défacement de sites web | Total |
|---|---:|---:|---:|---:|---:|
| Premier trimestre, janvier à mars | 58 | 22 | 0 | 2 | 82 |
| Deuxième trimestre, avril à juin | 57 | 103 | 52 | 0 | 212 |
| **S1 2026** | **115** | **125** | **52** | **2** | **294** |

Le deuxième trimestre devance le premier de **130 incidents**, soit une **hausse de 158,5 %** par rapport au T1. Le ransomware recule légèrement, de 58 incidents au T1 à 57 au T2. Les fuites et ventes d’accès passent de 22 à 103 incidents (**+368,2 %**), tandis que **52 revendications DDoS** sont enregistrées au T2 après aucune au T1.

## 6. Principaux constats CTI

1. **Le ransomware s’est maintenu plutôt qu’accéléré.** Son volume mensuel reste compris entre 17 et 21 incidents.
2. **Les fuites ont porté le deuxième trimestre.** Avril et mai totalisent à eux seuls 83 fuites ou ventes d’accès, contre 22 sur l’ensemble du premier trimestre ; ces deux mois concentrent également les 52 revendications DDoS du S1.
3. **Juin a déplacé l’équilibre sans revenir aux conditions du T1.** Le volume total a baissé après le pic avril-mai, mais le ransomware est revenu à la moitié des incidents du mois.
4. **Le semestre est fortement concentré géographiquement.** Le Maroc, l’Égypte et l’Afrique du Sud représentent **192 des 294 fiches (65,3 %)** lorsque tous les types d’incidents sont pris en compte.
5. **Gouvernement et administration dominent la vue sectorielle normalisée.** Ils représentent 70 des 239 fiches sectorielles normalisées (29,3 %), devant Industrie/Automobile/Fabrication/Construction/Mines et Finance/Banque, à 25 fiches chacune.
6. **Un nom qui revient d’un mois à l’autre ne prouve pas une intrusion commune.** Une activité associée au même compte source sur plusieurs mois est enregistrée comme une continuité de publication tant que les fiches n’établissent pas de vecteur d’accès partagé.

## 7. Limites du renseignement

- Le total représente 294 fiches d'incidents, chacune comptée selon son statut AFRINTEL structuré.
- La déduplication des victimes entre les mois n'est pas terminée.
- Une fiche multi-pays compte une fois dans le total global et plusieurs fois uniquement dans la vue géographique développée.
- Les variantes évidentes de noms et de versions d'acteurs sont normalisées. Les libellés de coalitions ne sont pas décomposés en comptes individuels.
- Les secteurs sont normalisés depuis le secteur explicite et la description de l'organisation dans chaque fiche source. Chaque fiche compte une seule fois.
- L'accès initial, le chiffrement et l'impact opérationnel ne sont pas documentés pour de nombreuses publications ransomware.

## 8. Priorités SOC et défensives

### Priorités du S1 fondées sur les données

| Libellé pays direct | Fiches | Barre |
|---|---:|:---|
| 🇲🇦 Maroc | 89 | ██████████████████ |
| 🇪🇬 Égypte | 55 | ███████████ |
| 🇿🇦 Afrique du Sud | 48 | ██████████ |
| 🇹🇳 Tunisie | 16 | ████ |
| 🇳🇬 Nigeria | 15 | ████ |
| 🇰🇪 Kenya | 9 | ██ |
| 🇩🇿 Algérie | 8 | ██ |
| 🇹🇿 Tanzanie | 6 | ██ |
| 🇸🇳 Sénégal | 6 | ██ |
| 🇬🇭 Ghana | 5 | ██ |
| 🇲🇺 Maurice | 3 | █ |
| 🇱🇾 Libye | 3 | █ |
| 🇿🇲 Zambie | 2 | █ |
| 🇳🇦 Namibie | 2 | █ |
| 🇨🇮 Côte d'Ivoire | 2 | █ |
| 🇪🇹 Éthiopie | 2 | █ |
| 🇧🇼 Botswana | 2 | █ |
| 🇸🇩 Soudan | 2 | █ |
| 🇿🇼 Zimbabwe | 1 | █ |
| 🇺🇬 Ouganda | 1 | █ |
| 🇹🇬 Togo | 1 | █ |
| 🇸🇴 Somalie | 1 | █ |
| 🇸🇨 Seychelles | 1 | █ |
| 🇳🇪 Niger | 1 | █ |
| 🇲🇿 Mozambique | 1 | █ |
| 🇾🇹 Mayotte | 1 | █ |
| 🇲🇬 Madagascar | 1 | █ |
| 🇬🇳 Guinée | 1 | █ |
| 🇬🇦 Gabon | 1 | █ |
| 🇧🇯 Bénin | 1 | █ |
| **Fiches mono-pays** | **287** | |

Les trois premiers pays directs regroupent **192 fiches (65,3 %)**. Le corpus contient aussi six incidents explicitement multi-pays et un incident panafricain sans attribution nationale précise, ce qui porte le total à 294.

| Secteur normalisé | Fiches | Barre |
|---|---:|:---|
| Government / Administration | 70 | ██████████ |
| Industrie / Automobile / Fabrication / Construction / Mines | 25 | ████ |
| Finance / Banking | 25 | ████ |
| Education / University / Institutions académiques | 19 | ███ |
| Technologie / Numérique / Services aux entreprises / Identité numérique | 15 | ███ |
| Healthcare / Medical | 12 | ██ |
| Sports / Federations | 12 | ██ |
| E-commerce / Retail | 12 | ██ |
| Alimentation / Boissons / Agriculture | 8 | ██ |
| Transport / Logistique / Aviation | 8 | ██ |
| Oil & Energy | 8 | ██ |
| Telecommunications | 5 | █ |
| Ressources humaines / Recrutement | 5 | █ |
| ONG / Action sociale | 3 | █ |
| Hôtellerie / Événementiel / Tourisme | 3 | █ |
| Médias / Audiovisuel | 2 | █ |
| Agrégation de données personnelles | 2 | █ |
| Services juridiques | 1 | █ |
| Immobilier | 1 | █ |
| Recherche / Think tank | 1 | █ |
| Organisations politiques / Partis | 1 | █ |
| Services de sécurité | 1 | █ |
| **Total des fiches normalisées** | **239** | |

Cette vue sectorielle normalisée couvre **239 fiches** et ne constitue pas une décomposition complète des 294 incidents. Nundun Gopee & Co Ltd est classée dans Construction / Immobilier.

#### Libellés d'acteurs normalisés les plus représentés

| Acteur ou groupe | Fiches | Barre |
|---|---:|:---|
| anisanas2 | 10 | ██████████ |
| TheGentlemen | 7 | ███████ |
| Databasehooligan | 7 | ███████ |
| 404Crew Cyber Team | 7 | ███████ |
| CrowStealer | 6 | ██████ |
| NightSpire | 6 | ██████ |
| LockBit 5 | 5 | █████ |
| Qilin | 4 | ████ |
| DeadLock | 4 | ████ |
| APT73 / Bashe | 4 | ████ |
| XP95 | 3 | ███ |
| xNov | 3 | ███ |
| Keymous | 3 | ███ |

Les variantes de casse et de version des noms d'acteurs sont normalisées dans les comptes et les graphiques.

#### Exposition multi-pays développée

| Mois | Fiche source | Pays africains explicitement cités | Expositions |
|---|---|---|---:|
| Avril | Fuite gouvernementale et vente d'accès administratif | Angola, Afrique du Sud, Nigeria | 3 |
| Mai | Fuite de CV | Kenya, Éthiopie, Nigeria, Zimbabwe | 4 |
| Mai | Publication régionale multi-pays | Mozambique, Liberia, Nigeria, Togo, Sierra Leone | 5 |
| Mai | Publication Égypte / Libye | Égypte, Libye | 2 |
| Juin | Vente d'adresses gouvernementales | Éthiopie, Tanzanie, Angola, Kenya, Zambie, Nigeria, Égypte, Maroc | 8 |
| Juin | Vente d'accès aux portails des forces de l'ordre | Égypte, Malawi, Tanzanie, Algérie, Kenya, Zambie, Sierra Leone | 7 |
| **Total** | **6 fiches sources** | | **29 expositions pays** |

Le total des incidents est **294**. Le remplacement des six incidents explicitement multi-pays par leurs 29 occurrences africaines produit **317 occurrences d’exposition géographique** : **287 incidents mono-pays**, **29 occurrences pays développées** et **1 incident panafricain** sans attribution régionale précise. La vue développée couvre **34 pays africains distincts**.

- Prioriser la télémétrie liée aux identités, VPN, messageries, stockages cloud et comptes privilégiés.
- Suivre séparément les publications de victimes, les éléments de chiffrement et la publication de données.
- Détecter les exports massifs, dumps de bases et expositions d'objets cloud publics.
- Imposer la MFA sur les portails gouvernementaux, éducatifs, financiers et de santé.
- Préparer des procédures rapides de révocation des identifiants gouvernementaux ou militaires exposés.
- Normaliser les noms d'acteurs entre les mois afin d'éviter les doubles comptages.
- Conserver les dates de revendication initiale, de découverte AFRINTEL et de publication.

## 9. Perspective stratégique

### Lacunes de renseignement

- Les données du dépôt ne permettent pas de distinguer la croissance réelle de l'activité d'une amélioration de la couverture de collecte.
- Les opérateurs de plusieurs plateformes non identifiées et jeux de données multi-organisations restent inconnus.
- Les libellés composites d'acteurs et les publications de coalitions limitent l'attribution précise par acteur.
- Le retour à une répartition 50/50 entre ransomware et fuites en juin constitue une observation mensuelle, pas encore une tendance établie pour le second semestre.

### Couverture MITRE ATT&CK contextuelle

| Technique | Nom | Usage défensif |
|---|---|---|
| T1078 | Valid Accounts | Surveiller les ventes d'accès et identifiants exposés |
| T1041 | Exfiltration Over C2 Channel | Hypothèse de détection des transferts sortants inhabituels |
| T1537 | Transfer Data to Cloud Account | Surveiller les déplacements de données cloud |
| T1486 | Data Encrypted for Impact | Seulement si le chiffrement est observé indépendamment |

Aucune technique n'est attribuée à un incident du S1 sans télémétrie probante.

Le premier semestre fait ressortir deux risques qui avancent en parallèle. Le ransomware a tenu une base opérationnelle stable, pendant que les fuites et ventes d'accès explosaient au deuxième trimestre. Réduire le semestre à une simple vague ransomware raterait l'essentiel. Le vrai changement structurel, c'est la montée du courtage de données, de l'exposition d'identifiants et de la publication de jeux de données structurés.

Pour le second semestre, AFRINTEL devra surveiller si la répartition 50/50 de juin devient un retour durable du ransomware, ou si ce n'était qu'une correction temporaire après le pic de fuites d'avril-mai.

## 10. Conclusion

AFRINTEL a recensé **294 incidents sur l’ensemble du S1 2026** : **115 ransomware**, **125 fuites ou ventes d’accès**, **52 revendications DDoS** et **2 défacements**. Le deuxième trimestre porte **212 fiches (72,1 %)** de l’activité semestrielle. La hausse du T2 est portée par les fuites / ventes d’accès et les revendications DDoS, partiellement compensées par le léger recul du ransomware et l’absence de défacement au T2.

La priorité défensive tient sur deux fronts à la fois : maintenir la préparation au ransomware tout en resserrant les contrôles contre l'exposition d'identifiants, l'extraction massive de données, l'exposition du stockage cloud et les ventes clandestines de données.

### Contrôles de cohérence

- Totaux mensuels : 21 + 20 + 41 + 69 + 103 + 40 = 294.
- Totaux par type : 115 + 125 + 52 + 2 = 294.
- Géographie directe : 287 incidents mono-pays + 6 incidents explicitement multi-pays + 1 incident panafricain = 294.
- Géographie développée : 287 incidents mono-pays + 29 occurrences pays développées + 1 occurrence panafricaine = 317.
- Totaux régionaux : 115 occurrences ransomware + 148 occurrences fuites / accès + 52 DDoS + 2 défacements = 317.
- Vue sectorielle normalisée : les 22 lignes sectorielles explicites totalisent 239 fiches.

---

**AFRINTEL**  
Open African CTI Monitoring Initiative  
[Dépôt GitHub](https://github.com/Hatchepsoute/AFRINTEL)
