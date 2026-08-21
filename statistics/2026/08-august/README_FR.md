[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Périmètre](https://img.shields.io/badge/Périmètre-Afrique-orange)
![Période](https://img.shields.io/badge/Période-Août%202026-lightgrey)
![Incidents](https://img.shields.io/badge/Incidents-9-critical)
![Ransomware](https://img.shields.io/badge/Ransomware-3-red)
![Fuites](https://img.shields.io/badge/Fuites%20de%20données-5-orange)
![Ventes d'accès](https://img.shields.io/badge/Ventes%20d'accès-1-yellow)
![Pays](https://img.shields.io/badge/Pays-5-blueviolet)

# AFRINTEL - Statistiques cyber en Afrique
## Août 2026

👉🏾 [Version anglaise disponible ici](./README.md)

## Note méthodologique

Ces statistiques sont dérivées de [victims_FR.md](../../../CyberAttackAfrica/2026/08-august/victims_FR.md), source de vérité française pour août 2026. Chaque incident est compté une fois dans le total global. Aucun incident multi-pays n'est présent ce mois-ci : les 9 occurrences géographiques correspondent donc aux 9 incidents.

Les volumes annoncés ne sont pas traités comme des faits confirmés. Pour Afribaba, le CSV fourni est analysé mais son attribution géographique reste incohérente : aucune ligne d'expédition algérienne n'est visible. Les données personnelles, identifiants et liens d'échantillon ne sont pas reproduits.

## 1. Résumé statistique

| Indicateur | Valeur |
|---|---:|
| Incidents documentés | **9** |
| Ransomware | **3** |
| Fuites de données | **5** |
| Ventes d'accès | **1** |
| Défacement | **0** |
| Occurrences géographiques | **9** |
| Pays représentés | **5** |
| Principal pays | Afrique du Sud, 3 |
| Principal pays fuites/accès | Algérie, 2 |
| Profil des statuts | 3 non vérifiés ; 4 avec échantillon ; 2 publications complètes revendiquées |
| Profil de confiance | 3 Faible ; 2 Moyen ; 3 Élevé ; 1 Très élevé |
| Profil d'impact | 1 Niveau 2 ; 1 Niveau 3 ; 7 Niveau 4 |

### Répartition globale

| Type d'incident | Nombre | Pourcentage |
|---|---:|---:|
| Ransomware | 3 | 33,3 % |
| Fuites de données | 5 | 55,6 % |
| Ventes d'accès | 1 | 11,1 % |
| **Total** | **9** | **100 %** |

~~~mermaid
pie showData
    title Répartition globale des incidents - août 2026
    "Ransomware" : 3
    "Fuites de données" : 5
    "Ventes d'accès" : 1
~~~

## 2. Répartition par pays

| Pays | Occurrences |
|---|---:|
| 🇿🇦 Afrique du Sud | 3 |
| 🇩🇿 Algérie | 2 |
| 🇰🇪 Kenya | 2 |
| 🇲🇺 Maurice | 1 |
| 🇳🇬 Nigeria | 1 |
| **Total** | **9** |

## 3. Ransomware contre fuites et ventes d'accès

| Pays | Ransomware | Fuites et ventes d'accès | Total |
|---|---:|---:|---:|
| Afrique du Sud | 1 | 2 | 3 |
| Algérie | 0 | 2 | 2 |
| Kenya | 0 | 2 | 2 |
| Maurice | 1 | 0 | 1 |
| Nigeria | 1 | 0 | 1 |
| **Total** | **3** | **6** | **9** |

## 4. Ventilation régionale

| Région | Occurrences | Ransomware | Fuites et ventes d'accès |
|---|---:|---:|---:|
| Afrique australe | 3 | 1 | 2 |
| Afrique du Nord | 2 | 0 | 2 |
| Afrique de l'Est | 2 | 0 | 2 |
| Afrique de l'Ouest | 1 | 1 | 0 |
| Océan Indien | 1 | 1 | 0 |
| **Total** | **9** | **3** | **6** |

## 5. Répartition sectorielle

| Secteur | Incidents | Part |
|---|---:|---:|
| Finance / Banque | 3 | 33,3 % |
| Gouvernement / Administration | 2 | 22,2 % |
| Ressources humaines / Recrutement | 1 | 11,1 % |
| Logistique / Services de courrier | 1 | 11,1 % |
| Médias / Édition | 1 | 11,1 % |
| Commerce en ligne / Marketplace | 1 | 11,1 % |
| **Total** | **9** | **100 %** |

## 6. Acteurs et sources les plus actifs

| Acteur ou source | Incidents | Activité principale |
|---|---:|---|
| exfilar | 2 | Fuites de données |
| NullSec Nigeria | 1 | Fuite de données |
| Florence | 1 | Vente d'accès |
| OriginalCrazyOldFart | 1 | Fuite de données |
| Panzer | 1 | Ransomware |
| medusalocker | 1 | Ransomware |
| incransom | 1 | Ransomware |
| TelephoneHooliganism | 1 | Fuite de données |

## 7. Tendances CTI

- Les fuites de données représentent 5 des 9 incidents.
- Trois incidents concernent l'Afrique du Sud et deux l'Algérie.
- Les échantillons structurés examinés ne valident pas automatiquement les volumes revendiqués.
- Le cas Afribaba combine une revendication de contacts et un CSV d'historique de commandes, mais les pays d'expédition observés ne comprennent pas l'Algérie.
- Les environnements cloud, les référentiels de recrutement et les données de commerce ou de paiement restent des priorités de surveillance.

## 8. Priorités de surveillance SOC

| Priorité | Point de surveillance |
|---|---|
| Élevée | Exports massifs de contacts, commandes, dossiers RH et bases cloud |
| Élevée | Accès anonymes ou anormaux aux environnements de préproduction et de production |
| Élevée | Réutilisation d'identifiants, changements MFA et créations de comptes |
| Moyenne | Flux sortants volumineux et création d'archives avant publication |
| Moyenne | Republications, domaines mal attribués et échantillons à provenance incertaine |

## 9. Conclusion

Août 2026 compte **9 incidents documentés** : 3 ransomware, 5 fuites de données et 1 vente d'accès. Les statistiques décrivent les publications collectées par AFRINTEL, et non la fréquence réelle des compromissions. Les contradictions d'attribution du cas Afribaba doivent rester visibles dans toute analyse ultérieure.

Pour le détail, consulter [victims_FR.md](../../../CyberAttackAfrica/2026/08-august/victims_FR.md).
