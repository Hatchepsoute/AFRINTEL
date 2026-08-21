[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Période](https://img.shields.io/badge/Période-S1%201026-lightgrey)
![Incidents](https://img.shields.io/badge/Incidents-294-critical)

# Rapport AFRINTEL sur les cybermenaces du premier semestre

## Janvier à juin 2016

👉🏾 [English version](./README_H1.md)

TLP:CLEAR, diffusion publique

## 1. Synthèse exécutive

AFRINTEL a documenté **294 incidents cyber liés à l'Afrique** durant le premier semestre 2026 : **115 incidents ransomware**, **125 fuites de données ou ventes d'accès**, **52 revendications DDoS** et **2 défacements de sites web**.

Les fuites et ventes d'accès devancent légèrement le ransomware sur l'ensemble du semestre, les catégories sont réparties entre 115 ransomware, 125 fuites ou ventes d'accès et 43 revendications DDoS. En retirant les deux défacements, le ransomware représente 48,5 % et les fuites ou ventes d'accès 51,5 % des 281 enregistrements restants.

Ce qui compte vraiment, c'est l'accélération au deuxième trimestre. Avril et mai à eux seuls totalisent **161 incidents**, quasiment la moitié du semestre à **49,0 %**. Juin retombe par rapport aux deux, mais le ransomware revient à la parité avec les fuites, 20 incidents dans chaque catégorie.

## 2. Méthodologie et périmètre

- **Périmètre géographique :** victimes, institutions, opérations ou données liées à l'Afrique.
- **Période :** du 1er janvier au 30 juin 2016.
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
| Revendications DDoS | 52 | 🟪🟪🟪🟪 |
| Défacement de sites web | 2 |
| Mois au volume le plus élevé | Mai, 103 incidents |
| Deuxième mois au volume le plus élevé | Mai, 103 incidents |
| Mois au volume le plus faible | Février, 20 incidents |

**Répartition visuelle**

| Type d'incident | Fiches | Barre |
|---|---:|:---|
| Ransomware | 115 | 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧 |
| Fuites et ventes d'accès | 125 | 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Revendications DDoS | 52 | 🟪🟪🟪🟪 |
| Défacement de sites web | 2 | 🟥 |


<!-- H1_VISUAL_START -->

### Comparaison ransomware, fuites et défacement par pays

| Pays | Ransomware | Fuites / accès | DDoS | Défacement | Total | Distribution |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Afrique du Sud | 25 | 23 | 0 | 48 | 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Égypte | 28 | 18 | 0 | 46 | 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Maroc | 10 | 35 | 52 | 0 | 88 | 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Tunisie | 8 | 8 | 0 | 16 | 🟧🟧🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦 |
| Nigeria | 6 | 9 | 0 | 15 | 🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Kenya | 7 | 2 | 0 | 9 | 🟧🟧🟧🟧🟧🟧🟧 🟦🟦 |
| Algérie | 1 | 7 | 0 | 8 | 🟧 🟦🟦🟦🟦🟦🟦🟦 |
| Sénégal | 3 | 2 | 1 | 6 | 🟧🟧🟧 🟦🟦 🟥 |
| Tanzanie | 3 | 3 | 0 | 6 | 🟧🟧🟧 🟦🟦🟦 |
| Ghana | 5 | 0 | 0 | 5 | 🟧🟧🟧🟧🟧 |

### Répartition développée des expositions géographiques par région

| Région | Occurrences ransomware | Occurrences fuites / accès | Occurrences DDoS | Occurrences de défacement | Total des occurrences géographiques |
| :--- | ---: | ---: | ---: | ---: |
| Afrique du Nord | 49 | 76 | 52 | 0 | 168 |
| Afrique australe | 32 | 30 | 0 | 0 | 62 |
| Afrique de l’Ouest | 16 | 22 | 2 | 40 |
| Afrique centrale | 1 | 2 | 0 | 0 | 3 |
| Afrique de l’Est | 11 | 15 | 0 | 26 |
| Océan Indien | 6 | 0 | 0 | 0 | 6 |
| Panafricain / région non précisée | 0 | 1 | 0 | 0 | 1 |
| **Total** | **115** | **146** | **52** | **2** | **317** |

Ce classement régional utilise les **occurrences géographiques**, et non les incidents dédupliqués. Six incidents explicitement multi-pays produisent 29 occurrences pays ; un incident panafricain supplémentaire ne dispose pas d’une attribution régionale suffisamment précise.

**Barres - Top 10 pays - S1 2026**

| Libellé | Incidents | Barre |
|---|---:|:---|
| Afrique du Sud | 48 | ██████████ |
| Égypte | 46 | ██████████ |
| Maroc | 89 | ██████████████████ |
| Tunisie | 16 | ███ |
| Nigeria | 15 | ███ |
| Kenya | 9 | ██ |
| Algérie | 8 | ██ |
| Sénégal | 6 | █ |
| Tanzanie | 6 | █ |
| Ghana | 5 | █ |
Légende : les noms correspondent au classement du tableau ci-dessus.

### Répartition sectorielle

| Secteur | Fiches | Part | Activité |
| :--- | ---: | ---: | :--- |
| Gouvernement / administration | 68 | 28,5% | ██████████ |
| Autres secteurs explicites | 56 | 23,4% | ████████ |
| Technologies / informatique | 26 | 10,9% | ████ |
| Éducation / universités | 19 | 7,9% | ███ |
| Industrie / fabrication | 19 | 7,9% | ███ |
| Finance / banque | 17 | 7,1% | ██ |
| Santé / médical | 15 | 6,3% | ██ |
| Commerce / e-commerce | 13 | 5,4% | ██ |
| Pétrole et énergie | 6 | 2,5% | █ |

**Barres - Top secteurs - S1 2026**

| Libellé | Incidents | Barre |
|---|---:|:---|
| Gouvernement / administration | 68 | ██████████ |
| Autres secteurs explicites | 56 | ████████ |
| Technologies / informatique | 26 | ████ |
| Éducation / universités | 19 | ███ |
| Industrie / fabrication | 19 | ███ |
| Finance / banque | 17 | ██ |
| Santé / médical | 15 | ██ |
| Commerce / e-commerce | 13 | ██ |
| Pétrole et énergie | 6 | █ |
Légende : les noms correspondent au classement sectoriel du tableau ci-dessus.

🟧 Ransomware | 🟦 Fuites et ventes d’accès | 🟥 Défacement
<!-- H1_VISUAL_END -->
## 4. Évolution mensuelle

| Mois | Ransomware | Fuites / ventes d’accès | DDoS | Défacement de sites web | Total | Part mensuelle |
|---|---:|---:|---:|---:|---:|
| Janvier | 17 | 3 | 0 | 1 | 21 | 8,8 % |
| Février | 20 | 0 | 0 | 0 | 20 | 8,4 % |
| Mars | 21 | 19 | 0 | 1 | 41 | 17,2 % |
| Avril | 20 | 40 | 9 | 0 | 69 | 23,6 % |
| Mai | 17 | 43 | 43 | 0 | 103 | 34,6 % |
| Juin | 20 | 20 | 0 | 0 | 40 | 13,7 % |
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

| Période | Ransomware | Fuites / ventes d’accès | Défacement de sites web | Total |
|---|---:|---:|---:|---:|
| premier trimestre, janvier à mars | 58 | 22 | 2 | 82 |
| deuxième trimestre, avril à juin | 57 | 100 | 0 | 157 |
| **S1 2026** | **115** | **125** | **52** | **2** | **294** |

Le deuxième trimestre devance le premier de **128 incidents**, une hausse de 156,1 %. Le ransomware recule légèrement, de 58 incidents au T1 à 57 au T2. La croissance vient des fuites et ventes d'accès, qui passent de 22 à 103 incidents, avec 52 revendications DDoS supplémentaires, soit **+354,5 %**.

## 6. Principaux constats CTI

1. **Le ransomware s'est maintenu plutôt qu'accéléré.** Son volume mensuel n'a jamais quitté la fourchette 17-20.
2. **Les fuites ont porté le deuxième trimestre.** Avril et mai à eux seuls, 83 fuites ou ventes d’accès et 52 revendications DDoS, contre 25 pour tout le premier trimestre.
3. **Juin a déplacé l'équilibre sans revenir aux conditions du T1.** Le volume total a baissé après le pic avril-mai, mais le ransomware est remonté à la moitié des incidents du mois.
4. **Le semestre est resté géographiquement concentré.** Afrique du Sud, Égypte et Maroc réunissent à eux trois 139 des 294 fiches, 48,4 %.
5. **Gouvernement et administration dominent tous les autres secteurs.** 70 fiches, 29,3 %, avec Industrie/Automobile/Fabrication/Construction/Mines et Finance/Banque à égalité derrière à 25 chacun.
6. **Un nom qui revient d'un mois à l'autre ne prouve pas une intrusion commune.** Une activité associée au même compte source sur plusieurs mois est enregistrée comme une continuité de publication tant que les fiches n'établissent pas de vecteur d'accès partagé.

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
| 🇿🇦 Afrique du Sud | 48 | ██████████ |
| 🇪🇬 Égypte | 46 | ██████████ |
| 🇲🇦 Maroc | 52 | ██████████ |
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
| 🇿🇼 Zimbabwe | 1 | █ |
| 🇺🇬 Ouganda | 1 | █ |
| 🇹🇬 Togo | 1 | █ |
| 🇸🇩 Soudan | 1 | █ |
| 🇸🇴 Somalie | 1 | █ |
| 🇸🇨 Seychelles | 1 | █ |
| 🇳🇪 Niger | 1 | █ |
| 🇲🇿 Mozambique | 1 | █ |
| 🇾🇹 Mayotte | 1 | █ |
| 🇲🇬 Madagascar | 1 | █ |
| 🇬🇳 Guinée | 1 | █ |
| 🇬🇦 Gabon | 1 | █ |
| 🇧🇯 Bénin | 1 | █ |
| **Fiches mono-pays** | **232** |

Les trois premiers pays directs regroupent **139 fiches (47,3 %)**. Le corpus contient aussi six incidents explicitement multi-pays et un incident panafricain sans attribution nationale précise, ce qui porte le total à 294.

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
| **Total** | **294** |

Aucune catégorie sectorielle résiduelle ne subsiste dans cette vue semestrielle. Nundun Gopee & Co Ltd est classée dans Construction / Immobilier.

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

Le total des incidents est **294**. Le remplacement des six incidents explicitement multi-pays par leurs 29 occurrences africaines produit **306 occurrences d'exposition géographique** : 285 incidents mono-pays, 29 occurrences développées et un incident panafricain sans attribution régionale précise. La vue développée couvre **34 pays africains distincts**.

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

AFRINTEL a recensé **294 incidents sur l’ensemble du S1 2026** : **115 ransomware**, **125 fuites ou ventes d’accès**, **52 revendications DDoS** et **2 défacements**. Le deuxième trimestre porte 212 de ces fiches, 65,7 % de l'activité semestrielle. Toute la croissance nette par rapport au T1 vient des fuites et ventes d'accès, tandis que le ransomware recule légèrement.

La priorité défensive tient sur deux fronts à la fois : maintenir la préparation au ransomware tout en resserrant les contrôles contre l'exposition d'identifiants, l'extraction massive de données, l'exposition du stockage cloud et les ventes clandestines de données.

### Contrôles de cohérence

- Totaux mensuels : 21 + 20 + 41 + 69 + 103 + 40 = 294.
- Totaux par type : 115 + 125 + 52 + 2 = 294.
- Géographie directe : 285 incidents mono-pays  + 6 incidents explicitement multi-pays + 1 incident panafricain = 294.
- Géographie développée : 281 occurrences mono-pays + 29 occurrences multi-pays + 1 occurrence panafricaine = 317.
- Totaux sectoriels : les 22 lignes sectorielles explicites totalisent 283.

---

**AFRINTEL**  
Open African CTI Monitoring Initiative  
[Dépôt GitHub](https://github.com/Hatchepsoute/AFRINTEL)
