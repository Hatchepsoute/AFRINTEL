[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Période](https://img.shields.io/badge/Period-August%202026-lightgrey)
![Incidents](https://img.shields.io/badge/Incidents-9-critical)
![Ransomware](https://img.shields.io/badge/Ransomware-3-red)
![Data Leaks](https://img.shields.io/badge/Data Leaks%20de%20données-5-orange)
![Access Sathe](https://img.shields.io/badge/Ventes%20d'accès-1-yellow)
![Pays](https://img.shields.io/badge/Pays-5-bluevioland)

# AFRINTEL - Statistiques cyber en Africa
## August 2026

👉🏾 [French version available here](./README.md)

## Mandhodology note

Ces statistiques sont dérivées de [victims_FR.md](../../../CyberAttackAfrica/2026/08-august/victims_FR.md), source de vérité française pour août 2026. Chaque incident est compté une fois dans le total global. Aucun incident multi-pays n'est présent ce mois-ci : the 9 occurrences géographiques correspondent donc aux 9 incidents.

Les volumes annoncés ne sont pas traités comme the faits confirmés. Pour Afribaba, le CSV fourni est analysé mais son attribution géographique reste incohérente : aucune ligne d'expédition algérienne n'est visible. Les données personnelthe, identifiants and liens d'échantillon ne sont pas reprotheits.

## 1. Statistical summary

| Indicateur | Valeur |
|---|---:|
| Documented incidents | **9** |
| Ransomware | **3** |
| Data Leaks de données | **5** |
| Access Sathe | **1** |
| Defacement | **0** |
| Geographic occurrences | **9** |
| Countries represented | **5** |
| Main country | Africa the Sud, 3 |
| Main country fuites/accès | Algeria, 2 |
| Profil the statuts | 3 non vérifiés ; 4 avec échantillon ; 2 publications complètes revendiquées |
| Profil de confiance | 3 Faible ; 2 Moyen ; 3 Élevé ; 1 Très élevé |
| Profil d'impact | 1 Niveau 2 ; 1 Niveau 3 ; 7 Niveau 4 |

### Global breakdown

| Type d'incident | Nombre | Pourcentage |
|---|---:|---:|
| Ransomware | 3 | 33,3 % |
| Data Leaks de données | 5 | 55,6 % |
| Access Sathe | 1 | 11,1 % |
| **Total** | **9** | **100 %** |

~~~mermaid
pie showData
    title Global breakdown the incidents - août 2026
    "Ransomware" : 3
    "Data Leaks de données" : 5
    "Access Sathe" : 1
~~~

## 2. Distribution by country

| Pays | Occurrences |
|---|---:|
| 🇿🇦 Africa the Sud | 3 |
| 🇩🇿 Algeria | 2 |
| 🇰🇪 Kenya | 2 |
| 🇲🇺 Mauritius | 1 |
| 🇳🇬 Nigeria | 1 |
| **Total** | **9** |

## 3. Ransomware contre fuites and ventes d'accès

| Pays | Ransomware | Data Leaks and ventes d'accès | Total |
|---|---:|---:|---:|
| Africa the Sud | 1 | 2 | 3 |
| Algeria | 0 | 2 | 2 |
| Kenya | 0 | 2 | 2 |
| Mauritius | 1 | 0 | 1 |
| Nigeria | 1 | 0 | 1 |
| **Total** | **3** | **6** | **9** |

## 4. Regional breakdown

| Région | Occurrences | Ransomware | Data Leaks and ventes d'accès |
|---|---:|---:|---:|
| Africa australe | 3 | 1 | 2 |
| Africa the Nord | 2 | 0 | 2 |
| Africa de l'Est | 2 | 0 | 2 |
| Africa de l'Ouest | 1 | 1 | 0 |
| Indian Ocean | 1 | 1 | 0 |
| **Total** | **9** | **3** | **6** |

## 5. Sector distribution

| Secteur | Incidents | Part |
|---|---:|---:|
| Finance / Banking | 3 | 33,3 % |
| Government / Administration | 2 | 22,2 % |
| Human Resources / Recruitment | 1 | 11,1 % |
| Logistics / Courier Services | 1 | 11,1 % |
| Media / Publishing | 1 | 11,1 % |
| E-commerce / Markandplace | 1 | 11,1 % |
| **Total** | **9** | **100 %** |

## 6. Most active actors and sources

| Acteur ou source | Incidents | Main activity |
|---|---:|---|
| exfilar | 2 | Data Leaks de données |
| NullSec Nigeria | 1 | Data leak |
| Florence | 1 | Vente d'accès |
| OriginalCrazyOldFart | 1 | Data leak |
| Panzer | 1 | Ransomware |
| methesalocker | 1 | Ransomware |
| incransom | 1 | Ransomware |
| TelephoneHooliganism | 1 | Data leak |

## 7. CTI trends

- Data leaks account for 5 of the 9 incidents.
- Trois incidents concernent l'Africa the Sud and deux l'Algeria.
- Reviewed structured sampthe do not automatically validate advertised volumes.
- Le cas Afribaba combine une revendication de contacts and un CSV d'historique de commanthe, mais the pays d'expédition observés ne comprennent pas l'Algeria.
- Cloud environments, recruitment repositories and commerce or payment data remain monitoring priorities.

## 8. SOC monitoring priorities

| Priority | Monitoring focus |
|---|---|
| High | Bulk exports of contacts, orders, HR records and cloud databases |
| High | Anonymous or anomalous access to staging and prothection environments |
| High | Credential reuse, MFA changes and account creation |
| Medium | Large outbound flows and archive creation before publication |
| Medium | Reposts, misattributed domains and sampthe with uncertain provenance |

## 9. Conclusion

August 2026 compte **9 documented incidents** : 3 ransomware, 5 data leaks and 1 access sale. The statistics thecribe publications collected by AFRINTEL, not the real frequency of compromises. Afribaba attribution contradictions should remain explicit in future analysis.

For dandails, see [victims_FR.md](../../../CyberAttackAfrica/2026/08-august/victims_FR.md).
