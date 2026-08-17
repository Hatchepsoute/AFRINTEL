[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Période](https://img.shields.io/badge/Période-Juillet%202026-lightgrey)
![Victimes](https://img.shields.io/badge/Victimes-42-critical)
![Ransomware](https://img.shields.io/badge/Ransomware-18-red)
![Fuites](https://img.shields.io/badge/Fuites%20de%20données-18-orange)
![Ventes d'accès](https://img.shields.io/badge/Ventes%20d'accès-6-yellow)
![Pays](https://img.shields.io/badge/Pays-12-blueviolet)

# AFRINTEL - Statistiques cyber en Afrique
## Juillet 2026

👉🏾 [Version anglaise disponible ici](./README.md)

## Note méthodologique

Ces statistiques sont dérivées des fiches victimes de juillet 2026. Chaque fiche est comptée une fois dans le total global. Une fiche relative à des documents d'identité concerne à la fois le Nigeria et la Côte d'Ivoire ; la vue géographique compte donc 43 occurrences pour 42 fiches. La fiche MTN est attribuée à l'Afrique du Sud dans la vue de travail, mais l'entité nationale n'est pas confirmée.

Les volumes annoncés ne sont pas traités comme des faits confirmés. Les données personnelles, identifiants et liens de téléchargement ne sont pas reproduits.

## 1. Résumé statistique

| Indicateur | Valeur |
|---|---:|
| Fiches d'incidents | **42** |
| Ransomware | **18** |
| Fuites de données | **18** |
| Ventes d'accès | **6** |
| Défacement | **0** |
| Occurrences géographiques | **43** |
| Pays représentés | **12** |
| Pays les plus représentés | Égypte et Tunisie, 7 chacune |
| Principal pays ransomware | Afrique du Sud, 5 |
| Principal pays fuites et accès | Tunisie, 7 |

### Répartition globale

| Type d'incident | Nombre | Pourcentage |
|---|---:|---:|
| Ransomware | 18 | 42,9 % |
| Fuites de données | 18 | 42,9 % |
| Ventes d'accès | 6 | 14,3 % |
| **Total** | **42** | **100 %** |

~~~mermaid
pie showData
    title Répartition globale des incidents - juillet 2026
    "Ransomware" : 18
    "Fuites de données" : 18
    "Ventes d'accès" : 6
~~~

## 2. Répartition par pays

| Pays | Occurrences géographiques |
|---|---:|
| 🇪🇬 Égypte | 7 |
| 🇹🇳 Tunisie | 7 |
| 🇲🇦 Maroc | 6 |
| 🇿🇦 Afrique du Sud | 6 |
| 🇳🇬 Nigeria | 4 |
| 🇩🇿 Algérie | 4 |
| 🇨🇮 Côte d'Ivoire | 3 |
| 🇬🇭 Ghana | 2 |
| 🇧🇼 Botswana | 1 |
| 🇨🇲 Cameroun | 1 |
| 🇰🇪 Kenya | 1 |
| 🇸🇸 Soudan du Sud | 1 |
| **Total** | **43** |

~~~mermaid
xychart-beta
    title "Occurrences géographiques par pays - juillet 2026"
    x-axis ["Égypte","Tunisie","Maroc","Afrique du Sud","Nigeria","Algérie","Côte d’Ivoire","Ghana","Botswana","Cameroun","Kenya","Soudan du Sud"]
    y-axis "Occurrences" 0 --> 8
    bar [7,7,6,6,4,4,3,2,1,1,1,1]
~~~

## 3. Ransomware contre fuites et ventes d'accès

| Pays | Ransomware | Fuites et ventes d'accès | Total géographique |
|---|---:|---:|---:|
| Égypte | 2 | 5 | 7 |
| Tunisie | 0 | 7 | 7 |
| Maroc | 2 | 4 | 6 |
| Afrique du Sud | 5 | 1 | 6 |
| Nigeria | 2 | 2 | 4 |
| Algérie | 0 | 4 | 4 |
| Côte d'Ivoire | 2 | 1 | 3 |
| Ghana | 1 | 1 | 2 |
| Cameroun | 1 | 0 | 1 |
| Botswana | 1 | 0 | 1 |
| Kenya | 1 | 0 | 1 |
| Soudan du Sud | 1 | 0 | 1 |
| **Total** | **18** | **25** | **43** |

Les 25 occurrences de fuites et de ventes d'accès comprennent l'allocation géographique supplémentaire de la fiche relative aux documents d'identité du Nigeria et de la Côte d'Ivoire.

## 4. Ventilation régionale

| Région | Pays inclus | Occurrences | Ransomware | Fuites et ventes d'accès | Répartition |
|---|---|---:|---:|---:|---|
| Afrique du Nord | Égypte, Tunisie, Maroc, Algérie | **24** | 4 | 20 | 🟧🟧🟧🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Afrique australe | Afrique du Sud, Botswana | **7** | 6 | 1 | 🟧🟧🟧🟧🟧🟧 🟦 |
| Afrique de l'Ouest et centrale | Nigeria, Côte d'Ivoire, Ghana, Cameroun | **10** | 6 | 4 | 🟧🟧🟧🟧🟧🟧 🟦🟦🟦🟦 |
| Afrique de l'Est | Kenya, Soudan du Sud | **2** | 2 | 0 | 🟧🟧 |
| **Total** | **12 pays** | **43** | **18** | **25** | *🟧 Ransomware \| 🟦 Fuites et ventes d'accès* |

~~~mermaid
xychart-beta
    title "Occurrences géographiques par région - juillet 2026"
    x-axis ["Afrique du Nord","Afrique australe","Afrique de l'Ouest et centrale","Afrique de l'Est"]
    y-axis "Occurrences" 0 --> 26
    bar [24,7,10,2]
~~~

## 5. Répartition sectorielle

| Secteur | Fiches | Part | Barre |
|---|---:|---:|---:|
| Gouvernement / Administration | 11 | 26,2 % | ███████████ |
| Télécommunications | 5 | 11,9 % | █████ |
| Santé / Médical | 4 | 9,5 % | ████ |
| Éducation / Universités | 3 | 7,1 % | ███ |
| E-commerce / Distribution | 3 | 7,1 % | ███ |
| Technologie / Ingénierie | 3 | 7,1 % | ███ |
| Pétrole et énergie | 2 | 4,8 % | ██ |
| Secteurs identifiés à occurrence unique | 11 | 26,2 % | ███████████ |
| **Total** | **42** | **100 %** |  |
~~~mermaid
xychart-beta
    title "Répartition sectorielle - juillet 2026"
    x-axis ["Gouvernement","Télécommunications","Santé","Éducation","E-commerce","Technologie","Pétrole et énergie","Secteurs unitaires"]
    y-axis "Fiches" 0 --> 12
    bar [11,5,4,3,3,3,2,11]
~~~

Le groupe des secteurs unitaires comprend les holdings d'investissement, la finance, le transport, l'immobilier, les mines, la comptabilité, le voyage, l'industrie chimique, la sécurité, les jeux et le caoutchouc ou l'agriculture.

## 6. Acteurs et sources les plus actifs

| Acteur ou source | Fiches | Activité principale |
|---|---:|---|
| arcusmedia | 4 | Ransomware |
| dragonforce | 3 | Ransomware |
| krybit | 2 | Ransomware |
| BIGBROTHER | 2 | Ventes d'accès et republications |
| thegentlemen | 2 | Ransomware |
| Phantom Atlas | 2 | Fuites de données |
| Autres sources nommées | 27 | Activités diverses |

## 7. Tendances CTI

- Les ransomware et les fuites de données représentent chacun 18 fiches.
- Six offres concernent des environnements publics, télécoms ou administratifs.
- Des documents d'identité et des éléments liés aux passeports apparaissent dans plusieurs fiches.
- Le gouvernement et l'administration restent le principal groupe sectoriel.
- Planet Sport et Adex illustrent la difficulté de distinguer une nouvelle compromission d'une republication.
- La qualité des preuves varie des exports structurés aux simples revendications.

## 8. Priorités de surveillance SOC

| Priorité | Point de surveillance |
|---|---|
| Élevée | Accès privilégiés, VPN, webmail et portails administratifs exposés |
| Élevée | Exports massifs depuis les référentiels d'identité, de santé, d'éducation et de paiement |
| Élevée | Nouveaux comptes administrateurs, élévations de privilèges et sessions inhabituelles |
| Moyenne | Réutilisation d'identifiants, récupération abusive de comptes et paiements anormaux |
| Moyenne | Republications et offres d'accès concernant des filiales nationales |

## 9. Conclusion

Juillet 2026 compte **42 fiches d'incidents** et **43 occurrences géographiques**. Les ransomware et les fuites de données sont à parts égales, tandis que six offres de vente d'accès ajoutent un risque spécifique lié au courtage d'accès. L'Afrique du Nord concentre les fuites et les accès ; l'Afrique du Sud et l'Afrique de l'Ouest et centrale présentent une pression ransomware plus forte.

Pour le détail, consulter les fiches mensuelles dans [CyberAttackAfrica/2026/07-july/victims_FR.md](../../../CyberAttackAfrica/2026/07-july/victims_FR.md).
