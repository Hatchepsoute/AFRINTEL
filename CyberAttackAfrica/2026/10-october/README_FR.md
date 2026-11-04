# Rapport CTI AFRINTEL - cyberincidents en Afrique (octobre 2026)

Ce corpus validé contient **48 incidents ou cas documentés** publiés pour la première fois ou observés pour la première fois par AFRINTEL en octobre 2026. Le rattachement mensuel suit la date de publication ou de première observation documentée ; aucune date de compromission n'est déduite lorsqu'elle est indisponible.

![Répartition par type](assets/type_FR.png)
![Répartition géographique](assets/geo_FR.png)
![Répartition géographique circulaire](assets/geo_pie_FR.png)
![Répartition sectorielle](assets/sector_FR.png)
![Répartition sectorielle circulaire](assets/sector_pie_FR.png)
![Top 5 des pays](assets/country_top5_FR.png)
![Répartition des secteurs normalisés](assets/sector_top10_FR.png)
![Acteurs les plus représentés](assets/actor_top10_FR.png)
![Répartition des régions](assets/region_pie_FR.png)
![Répartition des types](assets/type_pie_FR.png)

## Ventilation mensuelle validée

| Type d incident | Nombre | Part |
|---|---:|---:|
| Fuite de données | 23 | 47.9% |
| Ransomware | 17 | 35.4% |
| Intrusion système | 5 | 10.4% |
| Vente d'accès | 3 | 6.2% |
| **Total** | **48** | **100.0%** |

## Pays les plus représentés

| Pays | Nombre |
|---|---:|
| Égypte | 12 |
| Maroc | 12 |
| Afrique du Sud | 9 |
| République démocratique du Congo | 2 |
| Éthiopie | 2 |
| Madagascar | 2 |
| République du Congo | 1 |
| Rwanda | 1 |
| Mozambique | 1 |
| Gabon | 1 |
| Tunisie | 1 |
| Bénin | 1 |
| Nigeria | 1 |
| Sierra Leone | 1 |
| Côte d'Ivoire | 1 |

## Acteurs les plus représentés

Les comptes et noms d’acteurs ont été regroupés lorsqu’ils désignaient le même libellé source. Les comptes affichés par la source restent distingués des incidents pour lesquels aucun acteur n’est identifié.

| Libellé acteur | Nombre |
|---|---:|
| Nameless511 | 9 |
| UmBra | 4 |
| N0n | 4 |
| The Gentlemen | 3 |
| SensitiveDarkForum | 2 |
| Krybit | 2 |
| Qilin | 2 |
| Lenken | 2 |
| Kazu | 2 |
| List1 | 2 |

**Attribution non identifiée ou non établie : 4 incidents.** Ces cas ne sont pas comptés comme des acteurs dans le classement. Le compte bytetobreach est ajouté comme identifiant de publication, sans attribution technique indépendante.

## Répartition des secteurs normalisés

Les secteurs ont été regroupés en familles analytiques afin d’éviter qu’une même activité soit fragmentée entre plusieurs libellés détaillés.

| Secteur | Nombre |
|---|---:|
| Gouvernement / Administration publique | 12 |
| Commerce / Distribution | 8 |
| Technologie / Services numériques | 6 |
| Santé | 5 |
| Éducation | 5 |
| Finance / Assurance | 3 |
| Transport | 2 |
| Industrie / Ingénierie | 2 |
| Autres secteurs | 5 |

## Lecture CTI

Les fuites de données constituent la première catégorie du mois avec 23 fiches, devant les ransomware avec 17 fiches. Les intrusions système représentent 5 fiches et les ventes d’accès 3. L’Égypte et le Maroc arrivent en tête avec 12 incidents chacun, ce qui reflète aussi la visibilité des sources suivies par AFRINTEL. La concentration sectorielle est dominée par les administrations publiques (12), le commerce et la distribution (8), puis la technologie et les services numériques (6). Les ventes d’accès sont moins nombreuses, mais leur exposition potentielle peut être plus critique lorsqu’elles concernent des environnements administratifs ou des comptes privilégiés. Les comptes affichés par les sources, notamment Nameless511, UmBra, N0n et bytetobreach, sont conservés comme identifiants de publication ; quatre fiches restent sans attribution établie. Ces résultats décrivent la visibilité documentée du mois et ne constituent pas une mesure exhaustive de la menace réelle.

## Méthodologie

Les chiffres sont calculés une seule fois depuis `victims_FR.md`, contrôlés contre `victims.md`, puis réutilisés dans les rapports, comparaisons et bundles STIX. La correspondance entre les secteurs détaillés et les familles normalisées est documentée dans le [fichier de normalisation sectorielle](../../../normalization/sector_mapping_2026.csv). Un incident multi-pays compte une fois au total ; les occurrences par pays peuvent donc dépasser le total global. Le corpus mesure la visibilité documentée par AFRINTEL, pas la prévalence réelle des cyberattaques.

[Victim records](./victims_FR.md)
