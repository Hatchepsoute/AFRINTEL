# Comparaison AFRINTEL : juin et juillet 2026

👉🏾 [Version anglaise](README.md)

## Comparaison générale

| Indicateur | Juin | Juillet | Évolution |
|---|---:|---:|---:|
| Fiches d'incidents uniques | 40 | 42 | +2 (+5,0 %) |
| Ransomware | 20 | 18 | -2 (-10,0 %) |
| Ventes d'accès | 2 | 6 | +4 (+200,0 %) |
| Fuites et ventes d'accès regroupées | 20 | 24 | +4 (+20,0 %) |
| Occurrences géographiques | 53 | 43 | -10 (-18,9 %) |
| Pays dans la vue géographique | 20 | 12 | -8 |

Juillet compte deux fiches uniques de plus que juin, mais les publications ransomware reculent. Les ventes d'accès progressent de deux à six fiches. La baisse des occurrences géographiques s'explique par les deux grandes offres d'accès multi-pays de juin, alors que juillet comprend une fiche multi-pays relative à des données d'identité et une fiche MTN dont l'entité nationale reste non confirmée.

## Évolution par type d'incident

| Type d'incident | Juin | Juillet | Évolution |
|---|---:|---:|---:|
| Ransomware | 20 | 18 | -2 |
| Fuites de données | 18 | 18 | 0 |
| Ventes d'accès | 2 | 6 | +4 |
| Défacement | 0 | 0 | 0 |
| **Total** | **40** | **42** | **+2** |

Le changement mensuel vient surtout de la hausse de la catégorie regroupant fuites et ventes d'accès, parallèlement au recul des publications ransomware. Juillet distingue séparément 18 fuites de données et 6 ventes d'accès.

## Évolution par pays

Le tableau utilise les occurrences géographiques. Les allocations multi-pays apparaissent dans chaque vue nationale, mais restent une seule fiche dans le total global.

| Pays | Juin | Juillet | Évolution |
|---|---:|---:|---:|
| 🇲🇦 Maroc | 10 | 6 | -4 |
| 🇿🇦 Afrique du Sud | 6 | 6 | 0 |
| 🇪🇬 Égypte | 6 | 7 | +1 |
| 🇳🇬 Nigeria | 5 | 4 | -1 |
| 🇹🇳 Tunisie | 4 | 7 | +3 |
| 🇱🇾 Libye | 3 | 0 | -3 |
| 🇹🇿 Tanzanie | 3 | 0 | -3 |
| 🇰🇪 Kenya | 3 | 1 | -2 |
| 🇿🇲 Zambie | 2 | 0 | -2 |
| 🇨🇮 Côte d'Ivoire | 0 | 3 | +3 |
| 🇩🇿 Algérie | 1 | 4 | +3 |
| 🇬🇭 Ghana | 0 | 2 | +2 |
| 🇨🇲 Cameroun | 0 | 1 | +1 |
| 🇸🇸 Soudan du Sud | 0 | 1 | +1 |
| Autres pays présents seulement en juin | 5 | 0 | -5 |

Le Maroc reste un point important, mais passe de dix à six occurrences géographiques. La Tunisie passe de quatre à sept, sous l'effet des fuites et des ventes d'accès. La Côte d'Ivoire et le Ghana apparaissent dans la vue de juillet, tandis que plusieurs pays présents seulement en juin étaient liés aux offres d'accès multi-pays.

## Évolution par secteur

Les libellés sectoriels sont normalisés dans chaque corpus mensuel. La comparaison est indicative, car juillet utilise des libellés plus détaillés pour plusieurs secteurs unitaires.

| Secteur | Juin | Juillet | Évolution |
|---|---:|---:|---:|
| Gouvernement / Administration | 12 | 11 | -1 |
| Télécommunications | 0 | 5 | +5 |
| Santé / Médical | 3 | 4 | +1 |
| Éducation / Universités | 4 | 3 | -1 |
| E-commerce / Distribution | 4 | 3 | -1 |
| Technologie / Ingénierie | 0 | 3 | +3 |
| Finance / Banque | 6 | 1 | -5 |
| Pétrole et énergie | 0 | 2 | +2 |
| Transport / Logistique | 2 | 1 | -1 |
| Services de sécurité | 1 | 1 | 0 |
| Mines | 1 | 1 | 0 |
| Autres secteurs identifiés | 7 | 8 | +1 |

Le gouvernement reste le premier secteur sur les deux mois. Juillet est davantage marqué par les télécommunications et la technologie, tandis que juin présentait une concentration plus forte dans la finance.

## Évolution des acteurs

| Acteur ou source | Juin | Juillet |
|---|---:|---:|
| anisanas2 | 7 | 0 |
| DeadLock | 4 | 0 |
| LockBit 5 | 3 | 0 |
| arcusmedia | 0 | 4 |
| dragonforce | 0 | 3 |
| krybit | 2 | 2 |
| BIGBROTHER | 0 | 2 |
| TheGentlemen | 0 | 2 |
| Phantom Atlas | 0 | 2 |

Le profil des acteurs change nettement. Juin était dominé par anisanas2 et DeadLock, tandis que juillet est porté par arcusmedia et dragonforce. Krybit est présent dans les deux mois avec deux fiches à chaque période.

## Évaluation CTI

Juillet ne doit pas être lu comme une simple continuation de juin. Le total augmente légèrement, mais la répartition s'éloigne du ransomware au profit du courtage d'accès. La Tunisie devient plus présente, tandis que le Maroc reste important avec une concentration moindre qu'en juin.

La structure géographique diffère également. Juin comprenait des offres d'accès multi-pays touchant de nombreux États africains. Juillet présente une empreinte géographique plus réduite, avec une fiche de données d'identité concernant le Nigeria et la Côte d'Ivoire, ainsi qu'une incertitude sur l'entité nationale MTN.

## Priorités SOC

1. Maintenir la préparation ransomware malgré le léger recul des publications.
2. Renforcer la surveillance des offres d'accès administratifs, Fortinet, VPN, webmail et télécoms.
3. Prioriser les référentiels d'identité, de santé, d'éducation et de paiement pour la détection des exports massifs.
4. Améliorer l'inventaire des filiales nationales lorsqu'un domaine de groupe est mentionné.
5. Séparer les compromissions originales, les republications et les revendications de vente d'accès lors du triage.
6. Suivre les victimes récurrentes entre les mois sans fusionner les fiches lorsqu'aucun élément ne démontre une intrusion commune.

## Conclusion

Juin compte 40 incidents uniques contre 42 en juillet. Le ransomware recule de 20 à 18 fiches. La catégorie regroupant fuites et ventes d'accès passe de 20 à 24, tandis que les ventes d'accès explicitement classées progressent de deux à six. Le changement opérationnel principal est la visibilité accrue du courtage d'accès en juillet.

*AFRINTEL, Open African CTI Monitoring Initiative*
