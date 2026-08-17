[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware%20%26%20Data%20Breach-red)
![Period](https://img.shields.io/badge/Period-January%202026-lightgrey)
![Intel Type](https://img.shields.io/badge/Intel%20Type-CTI-purple)

# Rapport CTI - Cyberattaques en Afrique (janvier 2026)

👉🏾 [**English version available here**](./README.md)

## 1. Synthèse exécutive

Janvier 2026 a rapporté **21 incidents cyber** contre des cibles africaines, revendiqués ou détectés dans le mois. Le ransomware a mené la danse, avec deux groupes actifs au-delà des frontières, aux côtés de deux fuites de données, une vente d'accès et un défacement gouvernemental coordonné. Points clés :

- **17 revendications ransomware (81,0 %)**, **2 fuites de données (9,5 %)**, **1 vente d’accès (4,8 %)** et **1 défacement (4,8 %)**.
- **12 pays** touchés : **l'Afrique du Sud** (4 incidents) et le **Kenya** (4) sont les plus ciblés, suivis de l'**Égypte** (3).
- **11 acteurs identifiés** et **1 défacement non attribué** : **thegentlemen** (6 fiches) et **tengu** (5) regroupent 11 fiches dans 7 pays distincts.
- Les secteurs gouvernemental, financier et des transports représentent la majorité des victimes.
- Incidents critiques : défacement coordonné de 7+ sites de l’État nigérien affichant des messages politiques liés à la situation géopolitique du pays, fuite de données PixPay Sénégal (paiement mobile), fuite de données AOM Aviation Maroc (base de données aviation), et l'acteur IAB Bigbrother vendant de manière répétée des accès à l'infrastructure gouvernementale togolaise.

### 📋 Liste des victimes

👉🏾 [Voir la liste complète des victimes](./victims_FR.md)

## 2. Méthodologie

- **Périmètre** : 54 pays africains.
- **Période** : 1-31 janvier 2026 (incidents divulgués ou revendiqués durant ce mois ; les dates réelles d'attaque peuvent être antérieures).
- **Sources** : Dark web, DLS (sites de fuite), OSINT, canaux Telegram, forums underground, rapports médias.
- **Inclusion** : Incidents revendiqués ou attribués publiquement, avec victime, pays et secteur identifiés.
- **Typologie** :
  - *Ransomware* : publication d’une victime ou revendication par un groupe ransomware. Le chiffrement n’est pas présumé sans élément probant.
  - *Fuite de données / intrusion* : exfiltration non chiffrée, base de données vendue ou publiée.
  - *Vente d'accès* : vente d'identifiants compromis ou d'accès à des systèmes par un Initial Access Broker (IAB).
  - *Défacement* : modification visuelle de sites web, souvent à des fins politiques ou idéologiques.

## 3. Vue d'ensemble

| Indicateur | Valeur |
|------------|--------|
| Total des victimes | 21 |
| Pays touchés | 12 |
| Acteurs distincts | 12 |
| Incidents ransomware | 17 (81,0 %) |
| Vente d'accès (IAB) | 1 (4,8 %) |
| Fuites de données | 2 (9,5 %) |
| Défacement | 1 (4,8 %) |

**Pays les plus ciblés :**
- 🇿🇦 Afrique du Sud : 4 victimes
- 🇰🇪 Kenya : 4 victimes
- 🇪🇬 Égypte : 3 victimes
- 🇲🇦 Maroc : 2 victimes
- 🇹🇬 Togo : 1 victime
- 🇳🇪 Niger : 1 victime (7+ sites gouvernementaux)
- 🇸🇳 Sénégal : 1 victime
- 🇲🇿 Mozambique : 1 victime
- 🇹🇿 Tanzanie : 1 victime
- 🇲🇺 Maurice : 1 victime
- 🇩🇿 Algérie : 1 victime
- 🇹🇳 Tunisie : 1 victime

```mermaid
pie
 title Nombre de victimes par pays - janvier 2026
 "Afrique du Sud (4)" : 4
 "Kenya (4)" : 4
 "Egypte (3)" : 3
 "Maroc (2)" : 2
 "Togo (1)" : 1
 "Niger (1)" : 1
 "Senegal (1)" : 1
 "Mozambique (1)" : 1
 "Tanzanie (1)" : 1
 "Maurice (1)" : 1
 "Algerie (1)" : 1
 "Tunisie (1)" : 1
```

**Type d'incident par pays :**
| Pays | Ransomware | Fuite de données | Vente d'accès | Défacement |
|------|:----------:|:----------------:|:-------------:|:----------:|
| Afrique du Sud | 4 | 0 | 0 | 0 |
| Kenya | 4 | 0 | 0 | 0 |
| Égypte | 3 | 0 | 0 | 0 |
| Maroc | 1 | 1 | 0 | 0 |
| Togo | 0 | 0 | 1 | 0 |
| Niger | 0 | 0 | 0 | 1 |
| Sénégal | 0 | 1 | 0 | 0 |
| Mozambique | 1 | 0 | 0 | 0 |
| Tanzanie | 1 | 0 | 0 | 0 |
| Maurice | 1 | 0 | 0 | 0 |
| Algérie | 1 | 0 | 0 | 0 |
| Tunisie | 1 | 0 | 0 | 0 |

```mermaid
pie
 title Repartition par type d incident - janvier 2026
 "Ransomware (17)" : 17
 "Fuite de donnees (2)" : 2
 "Vente d acces (1)" : 1
 "Defacement (1)" : 1
```

**Acteurs les plus prolifiques :**
| Acteur | Type | Incidents | Pays ciblés |
|--------|------|:---------:|------------|
| thegentlemen | Ransomware | 6 | Égypte, Kenya, Maurice, Afrique du Sud |
| tengu | Ransomware | 5 | Algérie, Égypte, Kenya, Maroc, Tunisie |
| blackshrantac | Ransomware | 1 | Kenya |
| vect | Ransomware | 1 | Afrique du Sud |
| qilin | Ransomware | 1 | Mozambique |
| devman | Ransomware | 1 | Kenya |
| direwolf | Ransomware | 1 | Égypte |
| benzona | Ransomware | 1 | Tanzanie |
| skra1a | Courtier de données | 1 | Maroc |
| breach3d | Courtier de données | 1 | Sénégal |
| Bigbrother | Initial Access Broker | 1 | Togo |
| Non revendiqué | Défacement | 1 | Niger |

```mermaid
pie
 title Acteurs les plus actifs - janvier 2026
 "thegentlemen (6)" : 6
 "tengu (5)" : 5
 "Autres - 1 chacun (10)" : 10
```

## 4. Synthèse géographique

> **Pour le détail de chaque incident, voir [`victims_FR.md`](./victims_FR.md).**

- **Concentration :** l'Afrique du Sud et le Kenya à 4 incidents chacun, l'Égypte suit avec 3. À eux trois, ça fait 11 des 21 fiches du mois.
- **Activité ransomware :** 17 revendications au total. TheGentlemen en couvre 6 à lui seul, tengu 5, et les deux se sont montrés sur plusieurs régions plutôt que de rester cantonnés à une zone.
- **Autres types d'incidents :** deux fuites de données, une vente d'accès visant l'infrastructure gouvernementale togolaise, et un défacement coordonné de sites gouvernementaux nigériens complètent le tableau du mois.
- **Exposition notable :** PixPay et AOM Aviation ont chacun rendu publiques des données financières et aéronautiques ; jusqu'où va vraiment cette exposition dépend d'éléments qu'AFRINTEL n'a pas pu vérifier de manière indépendante.

---

## 5. Analyse détaillée par type d'incident

### 5.1 Ransomware et ventes d'accès (18 revendications)

| Pays | Attaques | Acteurs principaux |
|------|:--------:|-------------------|
| Afrique du Sud | 4 | thegentlemen (3), vect (1) |
| Kenya | 4 | thegentlemen, devman, blackshrantac, tengu |
| Égypte | 3 | thegentlemen, direwolf, tengu |
| Maroc | 1 | tengu |
| Mozambique | 1 | qilin |
| Tanzanie | 1 | benzona |
| Maurice | 1 | thegentlemen |
| Algérie | 1 | tengu |
| Tunisie | 1 | tengu |
| Togo | 1 | Bigbrother (IAB, vente d'accès) |

**Observations clés :**
- **thegentlemen** et **tengu** totalisent à eux deux 11 des 21 fiches (52 %) dans 7 pays distincts. Rien dans les sources de janvier ne relie pourtant les deux groupes entre eux.
- Le 20 janvier a été la journée la plus chargée, 5 revendications rien qu'en Afrique du Sud et au Kenya : Paltrack, Rola, Witzenberg, CPF, NSSF.
- **Bigbrother/Togo** ressemble à un cas d'école d'IAB : un accès SSH proposé en septembre 2025, puis un nouvel accès revendiqué en janvier. Un accès qui persiste comme ça augmente le risque qu'une opération plus lourde suive.

### 5.2 Fuites de données (2 incidents)

| Victime | Acteur | Secteur | Données exposées |
|---------|--------|---------|-----------------|
| PixPay (Sénégal) | breach3d | FinTech / Paiement mobile | Base de données financières |
| AOM Aviation Group (Maroc) | skra1a | Transport aérien / Aviation civile | Base de données aviation |

### 5.3 Défacement (1 incident)

| Victime | Acteur | Secteur | Portée |
|---------|--------|---------|--------|
| Sites gouvernementaux nigériens (7+) | Non revendiqué | Administration publique | Coordonné, à motivation politique |

## 6. Impact sectoriel

| Secteur | Incidents | Pourcentage |
|---------|:---------:|:-----------:|
| Gouvernement / Administration publique | 4 | 19,0 % |
| Services financiers / FinTech | 4 | 19,0 % |
| Transport / Logistique | 3 | 14,3 % |
| Industrie / Ingénierie | 3 | 14,3 % |
| Technologie / Informatique | 2 | 9,5 % |
| Santé | 1 | 4,8 % |
| Mines | 1 | 4,8 % |
| Agroalimentaire | 1 | 4,8 % |
| Tourisme | 1 | 4,8 % |
| Aviation | 1 | 4,8 % |

```mermaid
pie
 title Repartition sectorielle - janvier 2026
 "Gouvernement (4)" : 4
 "Finance (4)" : 4
 "Transport (3)" : 3
 "Industrie (3)" : 3
 "Technologie (2)" : 2
 "Sante (1)" : 1
 "Mines (1)" : 1
 "Agroalimentaire (1)" : 1
 "Tourisme (1)" : 1
 "Aviation (1)" : 1
```

**Enseignements :**
- Gouvernement et services financiers sont à égalité en tête, 4 incidents chacun, deux secteurs qui restent attractifs mois après mois.
- Les listings ransomware de janvier touchent des organisations liées à l'eau, au transport, aux ports et aux mines. Ça établit l'exposition sectorielle, ça ne dit rien sur un éventuel arrêt d'activité, les fiches sources ne vont pas jusque-là.
- Les ONG de santé, CCBRT Tanzanie en l'occurrence, ressortent comme une catégorie sous-protégée à surveiller.

## 7. Profil des acteurs de menaces

| Acteur | Type | Incidents | Cibles principales |
|--------|------|:---------:|-------------------|
| thegentlemen | Groupe ransomware | 6 | Égypte, Kenya, Maurice, Afrique du Sud |
| tengu | Groupe ransomware | 5 | Algérie, Égypte, Kenya, Maroc, Tunisie |
| blackshrantac | Ransomware | 1 | Kenya (services publics) |
| vect | Ransomware | 1 | Afrique du Sud (ingénierie) |
| qilin | Ransomware | 1 | Mozambique (infrastructure) |
| devman | Ransomware | 1 | Kenya (sécurité sociale) |
| direwolf | Ransomware | 1 | Égypte (ingénierie) |
| benzona | Ransomware | 1 | Tanzanie (ONG santé) |
| skra1a | Courtier de données | 1 | Maroc (aviation) |
| breach3d | Courtier de données | 1 | Sénégal (fintech) |
| Bigbrother | Initial Access Broker | 1 | Togo (gouvernement) |
| Non revendiqué | Défacement | 1 | Niger (gouvernement) |

**Acteurs émergents :** benzona, vect, direwolf (première apparition dans AFRINTEL).

### 7.1 Niveau de risque

| Pays | Niveau de risque |
|------|----------------|
| Afrique du Sud | 🔴 Élevé (4 ransomwares, industrie/gouvernement) |
| Kenya | 🔴 Élevé (4 ransomwares, institutions publiques critiques) |
| Égypte | 🟠 Moyen-Élevé (3 ransomwares, secteurs multiples) |
| Maroc | 🟠 Moyen (fuite de données + ransomware) |
| Togo | 🟠 Moyen (deux publications IAB, septembre 2025 et janvier 2026) |
| Niger | 🟠 Moyen (défacement coordonné, attribution non résolue) |
| Autres | 🟡 Faible-Moyen |

## 8. Tendances clés et lacunes de renseignement

### Tendances

1. **thegentlemen et tengu dominent le mois.** À eux deux, 52 % des fiches de janvier, thegentlemen dans 4 pays, tengu dans 5, sept pays distincts une fois les deux combinés.
2. **Le Kenya se démarque.** Les 4 incidents touchent tous des institutions publiques : eau, retraites, sécurité sociale, mines. Ça ne ressemble pas à de l'opportunisme dispersé, plutôt à un ciblage délibéré des infrastructures liées au gouvernement.
3. **Le Togo revient sans cesse.** Bigbrother a vendu un accès en septembre 2025, puis en a revendiqué un nouveau en janvier. Deux publications sur la même infrastructure gouvernementale, c'est déjà une raison suffisante pour lancer la revue des accès et des identifiants maintenant, pas plus tard.
4. **Les sites gouvernementaux nigériens sont tombés ensemble.** Plus de sept sites de l'État défigurés avec le même message politique, mais la source ne dit pas quelle dépendance technique commune l'opération a exploitée.
5. **Deux secteurs sans lien ont fui des données.** PixPay (paiement mobile) et AOM Aviation (aviation civile) n'ont rien en commun à part être deux publications de données, pas de quoi parler de tendance sectorielle sur cette seule base.

### Lacunes

- Les attaquants du défacement nigérien restent non attribués.
- L'acheteur de l'accès Bigbrother et la nature de l'accès exploité sont inconnus.
- Les volumes réels de données dans les incidents de fuite n'ont pas été vérifiés de manière indépendante.

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

- **Gestion des correctifs** : priorité aux applications web (CMS, portails gouvernementaux, plateformes financières).
- **Surveillance IAB** : toute revendication de vente d'accès à une infrastructure gouvernementale doit déclencher une rotation immédiate des identifiants et un audit forensique.
- **MFA obligatoire** : tous les comptes privilégiés et accès VPN doivent utiliser l'authentification multi-facteurs.
- **Réponse aux incidents** : établir des playbooks IR dédiés aux scénarios ransomware et défacement, incluant des protocoles de communication.
- **Risque tiers** : les logiciels logistiques (Paltrack), les plateformes aviation et les prestataires fintech doivent être inclus dans les évaluations de sécurité.

### Pour les analystes CTI

- Suivre les nouvelles publications de **thegentlemen** et **tengu** ; les deux groupes apparaissent ensemble dans 7 pays distincts en janvier.
- Surveiller **Bigbrother** pour de nouvelles revendications d'accès au gouvernement togolais et l'activité des acheteurs potentiels.
- Surveiller les opérations de suivi liées au défacement nigérien (possible escalade après reconnaissance).
- Émettre une alerte si des données PixPay ou AOM apparaissent sur des marchés secondaires.

## 11. Recommandations SOC tactiques

### Priorités de détection

- Surveiller les **patterns de déploiement ransomware (T1486)** : événements de chiffrement de fichiers, suppression de copies shadow, modification rapide de fichiers
- Détecter l'**activité de staging IAB** : connexions VPN inhabituelles, activité en dehors des heures normales sur des comptes privilégiés, signaux de mouvement latéral
- Pister l'**exfiltration de données (T1041)** : transferts sortants volumineux, utilisation de services de stockage cloud, connexions vers des nœuds de sortie Tor
- Pour les portails gouvernementaux : surveiller les **journaux d'applications web** pour les tentatives d'exploitation (T1190)

### Sources de surveillance

- EDR / Sysmon
- Journaux firewall / proxy
- Journaux DNS
- Journaux de gestion des identités et des accès
- Pare-feu applicatif web (WAF)
- Journaux d'authentification VPN

## 12. Recommandations stratégiques

- Établir des **mécanismes de partage CTI régionaux** entre les gouvernements d'Afrique de l'Est (Kenya, Tanzanie, Mozambique) face à l'activité ransomware transfrontalière.
- Imposer des **standards de sécurité minimaux** pour les sites gouvernementaux en Afrique de l'Ouest (correctifs CMS, pare-feu applicatifs) suite au défacement massif nigérien.
- Créer des **listes de surveillance IAB nationales** : quand l'infrastructure gouvernementale d'un pays apparaît sur des forums criminels, un protocole de réponse structuré doit être prédéfini.
- Prioriser les **exigences de sécurité réglementaires FinTech** : les plateformes de paiement mobile détiennent des données financières à une échelle qui rend les fuites très dommageables.

## 13. Conclusion

Janvier se solde par 21 fiches d'incidents dans 12 pays. Le ransomware en représente 17, et thegentlemen plus tengu couvrent à eux seuls 11 fiches dans 7 pays. Le reste du mois, deux publications de données, une vente d'accès, un défacement coordonné, complète le tableau. L'Afrique du Sud et le Kenya arrivent en tête sur le volume, l'Égypte juste derrière. Entre les trois, l'activité a touché l'Afrique du Nord, de l'Ouest, de l'Est et australe.

**AFRINTEL** - Cyber Threat Intelligence africaine
[GitHub AFRINTEL](https://github.com/Hatchepsoute/AFRINTEL)
