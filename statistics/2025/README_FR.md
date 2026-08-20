![AFRINTEL](https://img.shields.io/badge/AFRINTEL-CTI-blue)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Période](https://img.shields.io/badge/Période-2025-blue)

# Statistiques annuelles AFRINTEL — 2025

👉🏾 [English version](./README.md)

## 1. Périmètre et source

Cette vue statistique est dérivée des douze fichiers mensuels `victims.md` et contient **197 fiches**. Une fiche est une publication ou une revendication documentée ; elle ne constitue pas nécessairement une intrusion confirmée ni une victime unique. Les fichiers sources restent autoritatifs. Les republications et revendications distinctes sont conservées lorsqu’elles sont documentées comme des fiches mensuelles séparées.

Tous les totaux ci-dessous sont réconciliés avec la même base de 197 fiches. Les noms de pays sont normalisés et les graphes utilisent les codes ISO alpha-2. Les secteurs suivent la taxonomie annuelle contrôlée du rapport CTI. Les deux fiches `Non précisé` restent indéterminées dans la source et ne sont pas reclassées sans preuve.

## 2. Évolution mensuelle

| Mois | Fiches |
|---|---:|
| Janvier | 16 |
| Février | 8 |
| Mars | 11 |
| Avril | 17 |
| Mai | 21 |
| Juin | 21 |
| Juillet | 21 |
| Août | 13 |
| Septembre | 18 |
| Octobre | 19 |
| Novembre | 14 |
| Décembre | 18 |
| **Total** | **197** |

## 3. Répartition par pays

| Rang | Pays | ISO | Fiches |
|---:|---|:---:|---:|
| 1 | Égypte | EG | 33 |
| 2 | Maroc | MA | 31 |
| 3 | Afrique du Sud | ZA | 30 |
| 4 | Algérie | DZ | 19 |
| 5 | Nigeria | NG | 14 |
| 6 | Tunisie | TN | 13 |
| 7 | Kenya | KE | 10 |
| 8 | Mauritanie | MR | 8 |
| 9 | Zambie | ZM | 4 |
| 10 | Ghana | GH | 3 |
| 11 | Côte d’Ivoire | CI | 3 |
| 12 | Namibie | NA | 3 |
| 13 | Tanzanie | TZ | 3 |
| 14 | Botswana | BW | 2 |
| 15 | RDC | CD | 2 |
| 16 | Maurice | MU | 2 |
| 17 | Sénégal | SN | 2 |
| 18 | Togo | TG | 2 |
| 19 | Ouganda | UG | 2 |
| 20 | Zimbabwe | ZW | 2 |
| 21 | Angola | AO | 1 |
| 22 | Burkina Faso | BF | 1 |
| 23 | Cameroun | CM | 1 |
| 24 | Djibouti | DJ | 1 |
| 25 | Érythrée | ER | 1 |
| 26 | Gabon | GA | 1 |
| 27 | Madagascar | MG | 1 |
| 28 | Rwanda | RW | 1 |
| 29 | Burundi | BI | 1 |
| **Total** |  |  | **197** |

## 4. Répartition sectorielle

| Secteur normalisé | Fiches | Part |
|---|---:|---:|
| Gouvernement / Administration | 40 | 20,3 % |
| Finance / Banque | 39 | 19,8 % |
| Technologies / Informatique | 25 | 12,7 % |
| Éducation / Université | 17 | 8,6 % |
| Santé / Médical | 14 | 7,1 % |
| Industrie / Fabrication | 10 | 5,1 % |
| Transport / Logistique | 10 | 5,1 % |
| Commerce / E-commerce | 9 | 4,6 % |
| Services professionnels / aux entreprises | 7 | 3,6 % |
| Construction / Immobilier | 6 | 3,0 % |
| Défense / Sécurité | 6 | 3,0 % |
| Énergie / Services publics | 4 | 2,0 % |
| Agriculture / Agro-industrie | 3 | 1,5 % |
| Juridique / Justice | 2 | 1,0 % |
| Mines | 2 | 1,0 % |
| Non précisé | 2 | 1,0 % |
| Société civile / ONG | 1 | 0,5 % |
| **Total** | **197** | **100,0 %** |

## 5. Classification des incidents

| Type | Fiches | Part |
|---|---:|---:|
| Ransomware | 122 | 61,9 % |
| Fuite de données | 72 | 36,5 % |
| Vente d’accès | 3 | 1,5 % |
| Défacement | 0 | 0,0 % |
| **Total** | **197** | **100,0 %** |

### Vue agrégée de l’exposition

| Catégorie agrégée | Fiches | Part du corpus |
|---|---:|---:|
| Fuites de données + ventes d’accès | **75** | **38,1 %** |

Cette vue analytique dérivée (`72 + 3`) ne constitue pas une catégorie supplémentaire. Les ventes d’accès restent comptées séparément, car elles ne prouvent pas automatiquement une exfiltration de données.

## 6. Acteurs / sources les plus visibles

| Acteur / source | Fiches |
|---|---:|
| qilin | 11 |
| nightspire | 10 |
| devman | 10 |
| incransom | 8 |
| funksec | 7 |
| Phantom Atlas | 7 |
| killsec | 6 |
| kill9 | 6 |
| Dark 07x Team | 5 |
| ransomhub | 4 |

Cette vue présente les dix premiers acteurs. Les alias, comptes sources et annotations de publication sont normalisés pour le classement ; l’attribution complète au niveau des fiches reste disponible dans les victimes mensuelles et les bundles STIX.

## 7. Interprétation et priorités SOC

La répartition mesure la visibilité AFRINTEL et non la prévalence des compromissions réelles. Les revendications ransomware dominent le corpus, tandis que les fuites et ventes d’accès constituent un signal d’exposition distinct. Les équipes SOC doivent vérifier les revendications avec les journaux IAM, VPN, EDR, sauvegardes, DNS, proxy, WAF et applicatifs, et distinguer une nouvelle compromission d’une republication ou d’une revendication non vérifiée.

## Conclusion

La base statistique 2025 est réconciliée à **197 fiches** : **122 ransomware**, **72 fuites de données**, **3 ventes d’accès** et **0 défacement**. Les vues pays, secteurs et acteurs doivent être régénérées depuis les fiches mensuelles à chaque évolution de la source.

**AFRINTEL** — TLP:CLEAR
