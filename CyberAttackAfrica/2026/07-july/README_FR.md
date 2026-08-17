# AFRINTEL — Cyberattaques en Afrique, juillet 2026

👉🏾 [Read the English version](./README.md) · [Liste complète des victimes](./victims_FR.md)

## Résumé exécutif

Juillet n’a pas été le mois d’un seul groupe. AFRINTEL a recensé 42 fiches d’incidents dans 12 pays ce mois-ci : 18 revendications ransomware, 18 fuites de données, 6 offres de vente d’accès.

L’Égypte et la Tunisie arrivent en tête avec sept occurrences chacune, suivies du Maroc (6) et de l’Afrique du Sud, également à 6. Une fiche, un jeu de photos de pièces d’identité, touche à la fois le Nigeria et la Côte d’Ivoire : comptée une fois comme incident, deux fois sur la carte.

Ce qui marque ce mois-ci dépasse le seul ransomware : dossiers fonciers, données d’identité, fichiers médicaux, comptes universitaires, paiements de services publics, accès revendiqués à des systèmes gouvernementaux. AFRINTEL a pu recouper une partie de ces éléments sur échantillon ou capture d’écran. Le reste demeure la parole d’un acteur.

## Méthode

La source de ce rapport est [victims_FR.md](./victims_FR.md). Chaque fiche est comptée une fois, à la date de détection AFRINTEL. En additionnant la colonne pays, on arrive à 43 et non 42 : la fiche multi-pays compte deux fois géographiquement, et l’entité nationale de MTN reste non précisée.

Un volume annoncé reste une revendication tant qu’aucun élément ne vient l’étayer ; une publication de forum ne vaut pas confirmation à elle seule. Aucun défacement ce mois-ci.

## Répartition géographique

| Pays | Occurrences |
| :--- | ---: |
| 🇪🇬 Égypte | 7 |
| 🇹🇳 Tunisie | 7 |
| 🇲🇦 Maroc | 6 |
| 🇿🇦 Afrique du Sud | 6 |
| 🇳🇬 Nigeria | 4 |
| 🇩🇿 Algérie | 4 |
| 🇨🇮 Côte d’Ivoire | 3 |
| 🇬🇭 Ghana | 2 |
| 🇧🇼 Botswana | 1 |
| 🇨🇲 Cameroun | 1 |
| 🇰🇪 Kenya | 1 |
| 🇸🇸 Soudan du Sud | 1 |
| **Total géographique** | **43** |

~~~pie showData
title Occurrences géographiques — juillet 2026
"Égypte" : 7
"Tunisie" : 7
"Maroc" : 6
"Afrique du Sud" : 6
"Nigeria" : 4
"Algérie" : 4
"Côte d’Ivoire" : 3
"Ghana" : 2
"Botswana" : 1
"Cameroun" : 1
"Kenya" : 1
"Soudan du Sud" : 1
~~~

## Types d’incidents

| Type | Fiches | Part |
| :--- | ---: | ---: |
| 🟧 Ransomware | 18 | 42,9 % |
| 🟦 Fuite de données | 18 | 42,9 % |
| 🟪 Vente d’accès | 6 | 14,3 % |
| **Total** | **42** | **100 %** |

Les revendications ransomware se concentrent autour de quatre noms : arcusmedia (4), dragonforce (3), krybit (2), thegentlemen (2). Ce sont des publications sur site de fuite, pas la preuve qu’un chiffrement, un vol de données ou une perturbation a réellement eu lieu.

Le volet fuite de données est plus hétérogène : documents d’identité, données médicales, comptes universitaires, dossiers publics, bases commerciales. Les six offres d’accès portent sur du Fortinet, du webmail ou des portails allégués. Qu’un accès soit annoncé ne garantit pas qu’il fonctionne.

## Les dossiers marquants

Le ministère égyptien de l’Agriculture produit l’un des dossiers les plus solides du mois : correspondances, contrats, paiements, inspections, inventaires techniques, captures d’application, un ensemble vraiment cohérent. Si le matériel est authentique, il ouvre la voie à la fraude foncière, à la falsification de documents et au phishing construit sur des dossiers réels.

Nerasolgh, au Ghana, mérite aussi qu’on s’y arrête. Les exports examinés montrent des structures clients, personnel et paiements USSD, avec des champs bancaires, de géolocalisation, de hachages de mots de passe et de transactions. L’acteur revendique 26 millions d’enregistrements ; ce qui a pu être examiné est bien plus modeste. L’écart reste entier.

Heliopolis University et HIMS ne doivent pas être confondus, même s’ils se ressemblent sur le papier. L’échantillon d’Heliopolis montre des structures de comptes parents et étudiants. La publication HIMS revendique des données étudiants, personnel, finance et paiement. Aucun des deux volumes annoncés n’a été confirmé indépendamment, et dans les deux cas, ce sont les échantillons structurés qui renseignent le plus, pas les chiffres mis en avant.

Adex, en Tunisie, était une republication explicite par BIGBROTHER. La capture montre une interface d’administration avec un nombre d’enregistrements proche du « 15k » annoncé, ce qui rend l’accès plausible. Cela n’établit ni l’identité de l’intrus initial ni l’ampleur réelle des données.

Planet Sport reste un dossier à double fil à suivre séparément. LockBit 5 avait listé le domaine en avril ; une publication gratuite attribuée à Mozvo est apparue en juillet sur la même cible. Republication, revente, lien d’affiliation : plusieurs hypothèses tiennent, aucune n’est tranchée. Les deux fiches restent liées, pas fusionnées.

Zenith Bank apparaît elle aussi deux fois, dans une revendication de données antérieure et dans une revendication ransomware de juillet. De quoi justifier une surveillance renforcée. Pas de quoi conclure à la même compromission.

## Impact sectoriel

| Secteur | Fiches | Part |
| :--- | ---: | ---: |
| Gouvernement / Administration | 11 | 26,8 % |
| Santé / Médical | 4 | 9,8 % |
| Télécommunications | 5 | 11,9 % |
| Éducation / Universités | 3 | 7,3 % |
| E-commerce / Distribution | 3 | 7,3 % |
| Technologie / Ingénierie | 3 | 7,3 % |
| Pétrole et énergie | 2 | 4,9 % |
| Portefeuille d'investissement / Énergie | 1 | 2,4 % |
| Finance / Banque | 1 | 2,4 % |
| Transport / Logistique | 1 | 2,4 % |
| Immobilier | 1 | 2,4 % |
| Mines | 1 | 2,4 % |
| Comptabilité / Audit | 1 | 2,4 % |
| Voyage / Événementiel | 1 | 2,4 % |
| Industrie chimique | 1 | 2,4 % |
| Services de sécurité | 1 | 2,4 % |
| Jeux / Divertissement | 1 | 2,4 % |
| Caoutchouc / Agriculture | 1 | 2,4 % |
| **Total** | **42** | **100 %** |

Les systèmes publics restent la cible la plus frappée : marchés publics, justice, emploi, identité, foncier, services publics. Le risque ne s’arrête pas à la publication. Usurpation d’identité, faux dossiers et ingénierie sociale bâtie sur des données publiques volées peuvent continuer à rapporter bien après.

## Acteurs et sources

| Acteur / source | Fiches | Activité principale |
| :--- | ---: | --- |
| arcusmedia | 4 | Ransomware |
| dragonforce | 3 | Ransomware |
| krybit | 2 | Ransomware |
| BIGBROTHER | 2 | Vente d’accès / republication |
| thegentlemen | 2 | Ransomware |
| Phantom Atlas | 2 | Fuite de données |
| Autres sources nommées | 27 | Activités diverses |

Un nom qui revient ne fait pas une campagne. Ce mois mélange comptes sources, republications et revendications à la qualité de preuve très inégale : le tableau des acteurs est un décompte, pas une carte de la menace.

## Évaluation du risque

- 🔴 **Élevé :** Égypte, Tunisie et Maroc.
- 🟠 **Moyen :** Afrique du Sud, Nigeria, Algérie, Ghana, Côte d’Ivoire et Soudan du Sud.
- 🟡 **Faible à moyen :** Kenya, Cameroun et Botswana.

Les principales inconnues restent la confirmation par les victimes, les volumes réels, le vecteur d’accès, l’intégralité des archives et la remédiation.

## Correspondances MITRE ATT&CK contextuelles

| Phase | Technique | Contexte |
| :--- | :--- | :--- |
| Accès initial | T1190 — Exploit Public-Facing Application | Portails, applications et services exposés. |
| Accès initial | T1078 — Valid Accounts | Accès webmail, Fortinet et comptes privilégiés allégués. |
| Accès aux identifiants | T1003 — OS Credential Dumping | Revendications mentionnant des identifiants ou des hachages. |
| Collecte | T1213 — Data from Information Repositories | Référentiels publics, universitaires et d’entreprise. |
| Exfiltration | T1041 — Exfiltration Over C2 Channel | Hypothèse contextuelle, non confirmée pour chaque fiche. |
| Impact | T1486 — Data Encrypted for Impact | Seulement lorsque le chiffrement est documenté. |

## Recommandations

Administrations publiques : cloisonner les systèmes d’identité, de foncier, de justice et d’emploi, imposer la MFA à tous les comptes admin, alerter sur les exports massifs. Universités et établissements de santé : invalider les sessions exposées, renouveler les identifiants, vérifier la réutilisation des mots de passe. Télécoms et acteurs financiers : surveiller les règles de transfert de messagerie, les connexions VPN, les comptes privilégiés et tout ce qui touche aux paiements.

Rien d’exotique là-dedans. Sauvegardes hors ligne testées, journaux centralisés, préservation encadrée des preuves, plan de réponse couvrant aussi bien le ransomware que la simple exposition de données : c’est toujours ce qui fait la différence le jour où l’une de ces revendications s’avère réelle.

## Conclusion

Juillet dessine une menace large et inégale. Le ransomware ne faiblit pas, mais les fuites et les offres d’accès entraînent une part croissante de données d’identité, de santé, d’éducation, d’administration et de paiement. Une partie de ce rapport repose sur du matériel qu’AFRINTEL a pu examiner. Une autre reste la parole d’un acteur. Garder cette ligne visible, c’est ce qui donne sa valeur au bilan mensuel.

**AFRINTEL — Adama ASSIONGBON, Consultant SOC & CTI**  
[Repository](https://github.com/Hatchepsoute/AFRINTEL)
