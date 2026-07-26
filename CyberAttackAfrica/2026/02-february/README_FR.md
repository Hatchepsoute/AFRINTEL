[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Breach-red)
![Period](https://img.shields.io/badge/Period-February%202026-lightgrey)
![Intel Type](https://img.shields.io/badge/Intel%20Type-CTI-purple)

# Rapport CTI - Cyberattaques en Afrique (février 2026)

👉🏾 [**English version available here**](./README.md)

## 1. Synthèse exécutive

Février 2026 compte **20 incidents cyber** recensés dans **14 pays africains**, tous attribués à des groupes ransomware ou d'extorsion de données. Le fait marquant est la publication
de données sensibles attribuées à la **DAF Sénégal**, comprenant des informations citoyennes et biométriques consultées par AFRINTEL. Le volume de **139 To** est revendiqué par
l'acteur, mais n'a pas pu être mesuré à partir des éléments accessibles. Points clés :

- **20 incidents ransomware / extorsion de données (100 %)**.
- **14 pays** touchés : l'**Afrique du Sud** (3), l'**Égypte** (3), le **Ghana** (2) et le **Nigeria** (2) en tête.
- **11 acteurs distincts** : **thegentlemen** (5 incidents) domine, suivi de **0APT** (3) et **LockBit 5.0** (3).
- Le secteur de l'aviation sous pression soutenue : BlueSky Somalia, Nile Air Égypte, Air Côte d'Ivoire tous revendiqués en février.
- À noter : 0APT, responsable de 3 revendications à fort volume (BlueSky 3,5 To, Global Media Alliance 2,5 To, Vertex Law 850 Go), a ensuite disparu des sites de fuite publics.

> **Note :** La revendication Diesel-Electric Afrique du Sud (LockBit 5.0, 27 février) pourrait se chevaucher avec une revendication distincte du même acteur pour la même victime en mars 2026. Vérification indépendante requise.

### 📋 Liste des victimes

👉🏾 [Voir la liste complète des victimes](./victims_FR.md)

## 2. Méthodologie

- **Périmètre** : 54 pays africains.
- **Période** : 1-28 février 2026 (incidents divulgués ou revendiqués durant ce mois ; les dates réelles d'attaque peuvent être antérieures).
- **Sources** : Dark web, DLS (sites de fuite), OSINT, canaux Telegram, forums underground.
- **Inclusion** : Incidents revendiqués ou attribués publiquement, avec victime, pays et secteur identifiés.
- **Typologie** : tous les incidents du mois sont attribués à des groupes ransomware ou d’extorsion de données. Le chiffrement, l’interruption opérationnelle et le vecteur d’accès initial ne sont pas présumés lorsque la source documente uniquement une victime publiée ou une revendication d’exfiltration. Aucune activité autonome de courtier en données n’a été identifiée.

## 3. Vue d'ensemble

| Indicateur | Valeur |
|------------|--------|
| Total des victimes | 20 |
| Pays touchés | 14 |
| Acteurs distincts | 11 |
| Ransomware / extorsion de données | 20 (100 %) |

**Pays les plus ciblés :**
- 🇿🇦 Afrique du Sud : 3 victimes
- 🇪🇬 Égypte : 3 victimes
- 🇬🇭 Ghana : 2 victimes
- 🇳🇬 Nigeria : 2 victimes
- 🇸🇳 Sénégal : 1 victime
- 🇸🇴 Somalie : 1 victime
- 🇹🇿 Tanzanie : 1 victime
- 🇰🇪 Kenya : 1 victime
- 🇲🇺 Maurice : 1 victime
- 🇹🇳 Tunisie : 1 victime
- 🇸🇩 Soudan : 1 victime
- 🇨🇮 Côte d'Ivoire : 1 victime
- 🇲🇦 Maroc : 1 victime
- 🇳🇦 Namibie : 1 victime

```mermaid
pie
 title Nombre de victimes par pays (février 2026)
 "Afrique du Sud (3)" : 3
 "Égypte (3)" : 3
 "Ghana (2)" : 2
 "Nigeria (2)" : 2
 "Sénégal (1)" : 1
 "Somalie (1)" : 1
 "Tanzanie (1)" : 1
 "Kenya (1)" : 1
 "Maurice (1)" : 1
 "Tunisie (1)" : 1
 "Soudan (1)" : 1
 "Côte d'Ivoire (1)" : 1
 "Maroc (1)" : 1
 "Namibie (1)" : 1
```

**Top 3 des plus grandes fuites revendiquées :**
| Rang | Victime | Acteur | Volume |
|:---:|---------|--------|-------:|
| 1 | 🇸🇳 DAF SÉNÉGAL | The Green Blood Group | 139 To |
| 2 | 🇸🇴 BlueSky Aviation (Somalie) | 0APT | 3,5 To |
| 3 | 🇬🇭 Global Media Alliance (Ghana) | 0APT | 2,5 To |

**Acteurs les plus prolifiques :**
| Acteur | Incidents | Pays |
|--------|:---------:|------|
| thegentlemen | 5 | Kenya, Ghana, Égypte, Afrique du Sud, Tunisie |
| 0APT | 3 | Somalie, Ghana, Tanzanie |
| LockBit 5.0 | 3 | Maurice, Égypte, Afrique du Sud |
| incransom | 2 | Nigeria, Côte d'Ivoire |
| vect | 1 | Afrique du Sud |
| tengu | 1 | Maroc |
| payload | 1 | Égypte |
| apt73/bashe | 1 | Soudan |
| qilin | 1 | Namibie |
| killsec | 1 | Nigeria |
| The Green Blood Group | 1 | Sénégal |

```mermaid
pie
 title Acteurs les plus actifs (février 2026)
 "thegentlemen (5)" : 5
 "0APT (3)" : 3
 "LockBit 5.0 (3)" : 3
 "incransom (2)" : 2
 "Autres - 1 chacun (7)" : 7
```

## 4. Synthèse géographique

> **Pour le détail de chaque incident, voir [`victims_FR.md`](./victims_FR.md).**

- **Répartition :** 20 incidents concernent 14 pays. L’Afrique du Sud et l’Égypte en comptent 3 chacune, tandis que le Ghana et le Nigéria en comptent 2 chacun.
- **Activité des acteurs :** TheGentlemen arrive en tête avec 5 incidents, suivi de 0APT et LockBit 5.0 avec 3 incidents chacun.
- **Signal sectoriel :** BlueSky Aviation, Nile Air et Air Côte d’Ivoire montrent une pression soutenue sur le secteur aérien dans trois pays.
- **Revendications volumétriques :** les 139 To attribués à DAF Sénégal et les trois revendications de 0APT sont significatifs, mais les volumes et les détails des compromissions ne sont pas confirmés indépendamment.

---

## 5. Analyse détaillée par type d'incident

### 5.1 Ransomware et extorsion de données (20 incidents)

| Pays | Incidents | Acteurs principaux |
|------|:---------:|-------------------|
| Afrique du Sud | 3 | thegentlemen, vect, LockBit 5.0 |
| Égypte | 3 | thegentlemen, payload, LockBit 5.0 |
| Ghana | 2 | 0APT, thegentlemen |
| Nigeria | 2 | killsec, incransom |
| Sénégal | 1 | The Green Blood Group (139 To) |
| Somalie | 1 | 0APT (3,5 To) |
| Tanzanie | 1 | 0APT (850 Go) |
| Kenya | 1 | thegentlemen |
| Maurice | 1 | LockBit 5.0 |
| Tunisie | 1 | thegentlemen |
| Soudan | 1 | apt73/bashe (3,5 Go publiés) |
| Côte d'Ivoire | 1 | incransom |
| Maroc | 1 | tengu |
| Namibie | 1 | qilin |

**Observations clés :**
- **0APT** a émergé comme nouvel acteur prolifique début février (3 revendications en 5 jours) puis a disparu des DLS publics.
- **Secteur aérien** : 3 compagnies aériennes revendiquées (BlueSky Somalie, Nile Air Égypte, Air Côte d'Ivoire) par 3 acteurs différents. Ciblage opportuniste indépendant probable.
- **thegentlemen** poursuit son rythme de janvier 2026 avec 5 nouvelles revendications dans 4 pays.
- **LockBit 5.0** revendique 3 victimes, confirmant sa continuité opérationnelle sous le branding LockBit 5.x.

## 6. Impact sectoriel

| Secteur | Incidents | Pourcentage |
|---------|:---------:|:-----------:|
| Gouvernement / Administration | 3 | 15,0 % |
| Airlines / Aviation | 3 | 15,0 % |
| Énergie | 2 | 10,0 % |
| Finance / Banque / FinTech | 2 | 10,0 % |
| Mines / Extraction | 2 | 10,0 % |
| Juridique | 1 | 5,0 % |
| Médias | 1 | 5,0 % |
| Hôtellerie | 1 | 5,0 % |
| Conseil IT | 1 | 5,0 % |
| Immobilier | 1 | 5,0 % |
| Agriculture | 1 | 5,0 % |
| Commerce de détail | 1 | 5,0 % |
| Comptabilité | 1 | 5,0 % |

```mermaid
pie
 title Répartition sectorielle (février 2026)
 "Gouvernement (3)" : 3
 "Aviation (3)" : 3
 "Énergie (2)" : 2
 "Finance (2)" : 2
 "Mines (2)" : 2
 "Juridique (1)" : 1
 "Médias (1)" : 1
 "Hôtellerie (1)" : 1
 "Conseil IT (1)" : 1
 "Immobilier (1)" : 1
 "Agriculture (1)" : 1
 "Commerce (2)" : 2
```

**Enseignements :**
- Gouvernement, aviation et énergie forment le cluster infrastructures critiques (8 incidents, 40 %).
- La concentration aviation (3 compagnies aériennes en un mois) est inédite dans les archives AFRINTEL.
- La violation DAF Sénégal (données gouvernementales biométriques) représente un scénario d'impact de niveau 4 si confirmé.

## 7. Profil des acteurs de menaces

| Acteur | Type | Incidents | Cibles principales |
|--------|------|:---------:|-------------------|
| thegentlemen | Groupe ransomware | 5 | Multi-secteur, 4 pays |
| 0APT | Inconnu (disparu) | 3 | Aviation, médias, juridique |
| LockBit 5.0 | Ransomware | 3 | Hôtellerie, gouvernement, automobile |
| incransom | Ransomware | 2 | Énergie, aviation |
| The Green Blood Group | Ransomware / extorsion | 1 | Sénégal (gouvernement) |
| apt73/bashe | Ransomware | 1 | Soudan (agriculture) |
| vect | Ransomware | 1 | Afrique du Sud (énergie) |
| tengu | Ransomware | 1 | Maroc (comptabilité) |
| payload | Ransomware | 1 | Égypte (immobilier) |
| killsec | Ransomware | 1 | Nigeria (fintech) |
| qilin | Ransomware | 1 | Namibie (commerce) |

**Notes sur les acteurs :**
- **0APT** : Revendications à fort volume sans preuves publiées. Disparu après février. Faible niveau de confiance jusqu'à vérification.
- **The Green Blood Group** : Première apparition AFRINTEL. Revendication de 139 To sur un gouvernement.
- **LockBit 5.0** : Troisième mois consécutif d'activité africaine.

### 7.1 Niveau de risque

| Pays | Niveau de risque |
|------|----------------|
| Sénégal | 🔴 Critique (139 To gouvernement + biométrie) |
| Afrique du Sud | 🔴 Élevé (3 incidents : gouvernement, énergie, automobile) |
| Égypte | 🔴 Élevé (3 incidents dont un ministère gouvernemental) |
| Soudan | 🟠 Moyen-Élevé (fuite partielle confirmée, secteur agricole critique) |
| Somalie | 🟠 Moyen (secteur aérien) |
| Nigeria | 🟠 Moyen (fintech + secteur pétrolier) |
| Autres | 🟡 Faible-Moyen |

## 8. Tendances clés et lacunes de renseignement

### Tendances

1. **DAF Sénégal - violation potentiellement record** : 139 To incluant des données biométriques est une revendication extraordinaire. Si confirmée, elle marquerait une escalade significative des attaques contre les gouvernements ouest-africains.
2. **Secteur aérien sous attaque** : trois compagnies aériennes revendiquées en un mois dans trois pays par trois acteurs différents. Ciblage opportuniste indépendant plutôt que campagne coordonnée.
3. **Émergence et disparition de 0APT** : trois revendications à fort volume en 5 jours puis silence. Soit le groupe a atteint ses objectifs, soit les revendications étaient fabriquées, soit un acteur existant a testé un nouveau pseudonyme.
4. **thegentlemen maintient le rythme** : cinq incidents en février après six en janvier confirme un tempo opérationnel panafricain soutenu.
5. **Persistance de LockBit 5.0** : trois revendications confirment la continuité africaine sous le branding LockBit 5.x.

### Lacunes

- La revendication de 139 To DAF Sénégal n'est pas vérifiée de manière indépendante. Aucune déclaration de la victime ni confirmation externe.
- L'identité réelle, les outils et l'infrastructure de 0APT sont inconnus.
- Diesel-Electric Afrique du Sud : chevauchement potentiel entre les revendications de février et mars 2026 à confirmer.
- Les capacités et activités antérieures de The Green Blood Group ne sont pas documentées.

## 9. Cartographie MITRE ATT&CK (contextuelle)

| Phase | Technique | Portée analytique |
| :--- | :--- | :--- |
| Accès initial | T1566 - Phishing | Hypothèse de détection défensive, non observée à partir des seules revendications |
| Accès initial | T1190 - Exploit Public-Facing Application | Hypothèse de détection défensive, non observée à partir des seules revendications |
| Accès par comptes | T1078 - Valid Accounts | Pertinent pour les ventes d’accès ou d’identifiants, sans confirmer leur utilisation |
| Collecte | T1005 - Data from Local System | Hypothèse contextuelle lorsque des données internes sont publiées, le mécanisme de collecte restant inconnu |
| Impact | T1486 - Data Encrypted for Impact | Pertinent pour la préparation ransomware, sans confirmer un chiffrement pour chaque fiche |

> Ces techniques constituent des hypothèses défensives. Une revendication, une vente de données ou une publication sur un site de fuite ne suffit pas à les considérer comme observées.

## 10. Recommandations

### Pour les gouvernements et entreprises africains

- **Protection des données biométriques** : les organisations détenant des bases de données biométriques nationales doivent les traiter comme des actifs de plus haute sensibilité avec des sauvegardes hors ligne, des contrôles d'accès stricts et une détection en temps réel des flux de données sortants.
- **Détection d'exfiltration par volume** : mettre en place des seuils de transferts sortants ; 139 To ne peuvent pas quitter un réseau inaperçus avec une surveillance adéquate.
- **Durcissement du secteur aérien** : les systèmes technologiques opérationnels (OT) des aéroports et compagnies aériennes doivent être segmentés des réseaux informatiques.
- **Plans de réponse aux incidents ransomware** : tous les ministères gouvernementaux doivent disposer de playbooks IR testés avec des sauvegardes hors ligne vérifiées.

### Pour les analystes CTI

- Suivre **The Green Blood Group** pour des revendications supplémentaires ou des publications de preuves.
- Surveiller **0APT** pour une réapparition sous le même pseudonyme ou un pseudonyme alternatif.
- Vérifier la **double revendication Diesel-Electric** (février + mars) auprès des communications de la victime.
- Surveiller l'expansion d'**apt73/bashe** vers l'Afrique centrale et de l'Est (Soudan : première apparition AFRINTEL pour cette région).

## 11. Recommandations SOC tactiques

### Priorités de détection

- **Détection d'exfiltration à grande échelle (T1041)** : alerte sur les transferts sortants dépassant 10 Go en 24 heures depuis des systèmes non de sauvegarde
- **Déploiement ransomware (T1486)** : surveiller les événements de modification de masse de fichiers, la suppression VSS et les signatures de processus de chiffrement
- **Mouvement latéral pré-chiffrement** : détecter l'utilisation anormale de comptes admin, les chaînes RDP, l'utilisation de PsExec ou d'outils similaires
- **Surveillance aviation et OT** : segmenter les systèmes de réservation et opérationnels ; détecter les connexions non autorisées entre segments

### Sources de surveillance

- EDR / Sysmon
- DLP (Data Loss Prevention) : alertes sur les volumes sortants
- Analyse de flux réseau (NetFlow/IPFIX)
- Journaux firewall / proxy
- Journaux de gestion des identités et des accès

## 12. Recommandations stratégiques

- Les gouvernements d'Afrique de l'Ouest doivent établir des **exigences minimales de sécurité IT pour les systèmes d'administration gouvernementale**, suite à la revendication DAF Sénégal.
- Créer un **partage d'informations transfrontalier pour le secteur aérien** entre les équipes CERT d'Afrique du Nord, de l'Ouest et de l'Est.
- Développer des **cadres nationaux de protection des données biométriques** avec des contrôles de sécurité spécifiques pour les bases de données gouvernementales contenant empreintes digitales, données de reconnaissance faciale et enregistrements d'identité.
- Les **registres d'infrastructures critiques** doivent imposer des délais de signalement des incidents cyber pour une meilleure conscience situationnelle régionale.

## 13. Conclusion

Février 2026 est avant tout marqué par l'ampleur et la sensibilité de la revendication DAF Sénégal : si confirmés, 139 To de données citoyennes et biométriques constitueraient l'une des violations gouvernementales les plus significatives de l'histoire cyber africaine. Au-delà de ce cas unique, le mois démontre un paysage de menaces large et diversifié : 14 pays, 11 acteurs, et une intensité particulière sur l'aviation, l'énergie et les entités gouvernementales critiques. thegentlemen, LockBit 5.0 et 0APT (brièvement) maintiennent tous un rythme opérationnel élevé. AFRINTEL continue de surveiller tous les groupes actifs et mettra à jour les évaluations au fur et à mesure de la vérification.

**AFRINTEL** - Cyber Threat Intelligence africaine
[GitHub AFRINTEL](https://github.com/Hatchepsoute/AFRINTEL)
