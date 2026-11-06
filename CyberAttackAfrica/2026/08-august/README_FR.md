![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-244768)
![Périmètre](https://img.shields.io/badge/Couverture-54%20pays%20africains-217e82)
![Période](https://img.shields.io/badge/P%C3%A9riode-Ao%C3%BBt%202026-d59a43)
![Démarche](https://img.shields.io/badge/M%C3%A9thode-OSINT%20%7C%20CTI-637a92)

# AFRINTEL - Rapport mensuel de renseignement cyber
## Cybermenaces en Afrique | Août 2026

👉🏾 [English version](./README.md) · [Fiches victimes FR](./victims_FR.md) · [Fiches EN](./victims.md) · [Statistiques JSON](./STATISTIQUES_2026-08.json)

**Période couverte :** 1er au 31 août 2026  
**Périmètre :** veille de 54 pays africains ; 10 pays représentés dans le corpus du mois  
**Destinataires :** directions générales, RSSI, DSI, directions des risques, CERT et analystes CTI/SOC  
**Sources de collecte :** sites de publication de groupes ransomware sur le Dark Web, forums underground, espaces de divulgation et de vente de données du Dark Web et du Deep Web, échantillons disponibles, communiqués des organisations et sources publiques de recoupement.

> **Note de fiabilité.** Une fiche publiée par un groupe criminel établit l'existence d'une **revendication observée**, pas automatiquement une intrusion. Les données examinées peuvent étayer l'association avec une organisation sans démontrer leur origine technique. Les confirmations officielles sont indiquées explicitement. Les chiffres mesurent les dossiers **documentés par AFRINTEL**, pas l'ensemble des cyberattaques survenues en Afrique. Les données personnelles brutes, identifiants et secrets ne sont pas reproduits dans ce rapport.

---

## 1. Synthèse exécutive - décisions à retenir

En août 2026, AFRINTEL documente **33 signalements dans 10 pays africains** : **18 dossiers ransomware (54,5 %)**, **14 fuites de données (42,4 %)** et **1 vente d'accès (3,0 %)**. Ces chiffres représentent des **publications, échantillons et événements documentés**, et non 33 compromissions confirmées. Le suivi distingue systématiquement la revendication, la cohérence des documents et la confirmation d'une organisation.

L'**Afrique du Sud (12)** est la plus représentée, devant l'**Égypte (5)** et l'**Algérie (5)**. Cela décrit la visibilité des sources collectées, non une comparaison de la sécurité des pays. Les publications examinées concernent des données d'identité, d'administration, de finance et d'emploi ; ces informations peuvent favoriser la fraude, l'usurpation et le phishing ciblé.

**Point de vigilance :** la publication visant **Yalidine** du **20 août 2026** est comptabilisée comme un **signalement à vérifier**, classé `Under Investigation` avec une confiance `Low`. L'origine des CSV n'est pas établie. La date de découverte retenue pour son suivi est alignée sur la publication du **20 août** ; ce choix de classement ne constitue pas une preuve d'observation technique à cette date. Aucune confirmation publique propre à la revendication d'août 2026 n'a été retrouvée lors de la recherche du 5 novembre 2026. Le démenti publié par Yalidine dans la presse en décembre 2025 concerne une autre allégation et ne tranche pas le cas de 2026.

**Message aux décideurs :** une revendication doit entraîner une vérification proportionnée, pas une conclusion de compromission automatique. La cartographie des données sensibles, le contrôle des accès, les sauvegardes testées et une détection contextualisée permettent de réduire l'exposition.

### 1.1 Comparaison avec juillet 2026 - signalements documentés

La même unité de comptage est utilisée : **une fiche de signalement documenté**, avec son niveau de preuve précisé séparément. Le corpus de juillet comprend **47 fiches** et celui d'août **33**. Il s'agit d'une évolution de la **couverture documentaire AFRINTEL**, pas d'une mesure de la fréquence réelle des cyberattaques.

| Indicateur | Juillet 2026 | Août 2026 | Évolution |
|---|---:|---:|---:|
| **Total des dossiers** | **47** | **33** | **−14 (−29,8 %)** |
| Ransomware | 18 | 18 | 0 (stable) |
| Fuites de données | 21 | 14 | −7 (−33,3 %) |
| Ventes d'accès | 6 | 1 | −5 (−83,3 %) |
| Défacement | 2 | 0 | −2 (−100 %) |

![Comparaison juillet–août](./assets/comparison_jul_aug_2026_FR.png)

### 1.2 Règle de comptage et continuité avec septembre

| Indicateur | Valeur | Interprétation |
|---|---:|---|
| Signalements documentés en août | **33** | Revendications, divulgations et événements confirmés ; confirmation et confiance mesurées séparément |
| Dossiers sous investigation dans ce total | **1** | Yalidine : attribution du fichier non corroborée |
| Base août utilisée dans la comparaison de septembre | **33** | 18 ransomware, 14 fuites et 1 vente d'accès |

Cette règle évite de faire disparaître un signalement au seul motif qu'il n'est pas confirmé. Un signalement compté n'est **pas un incident techniquement confirmé**. Les doublons de publication d'un même événement sont consolidés afin de ne pas gonfler les totaux.

## 2. Périmètre, sources, dates et limites de vérification

AFRINTEL surveille les sites de divulgation ransomware, forums clandestins, plateformes de vente ou de diffusion de données, échantillons accessibles, communications officielles et sources publiques de corroboration. Les 54 pays africains relèvent du périmètre de veille ; **10 pays figurent dans les 33 dossiers retenus**. L'absence de dossier n'implique aucune absence d'incident.

**Quatre dates ne doivent pas être confondues :** la date de l'incident (si établie), la **date initiale de publication**, la **date de découverte AFRINTEL** et la **date du dernier contrôle documenté**. La date retenue pour la ventilation mensuelle correspond à la publication ou à l'événement daté lorsqu'il est documenté, y compris lorsqu'AFRINTEL l'intègre rétrospectivement. Par exemple, la publication concernant **six universités égyptiennes** date du 21 août mais son intégration AFRINTEL mentionnée dans la fiche est du 4 novembre ; la communication publique de **Cartrack** suit un événement d'août et la fiche a été intégrée en septembre. Ces cas ne prouvent pas une intrusion survenue au moment de la découverte.

Un dossier peut concerner plusieurs organisations ou pays : **la publication commune relative aux six universités est comptée une fois**, conformément à la décision de regroupement de la fiche. Les doublons de publication et les rééditions ne doivent pas augmenter le dénominateur.

**Échelle des preuves :** publication observée ; échantillon effectivement examiné ; recoupement documentaire ; confirmation explicite d'une victime ou d'une autorité ; inconnues techniques. Une preuve de publication n'est pas une preuve de chiffrement ; un échantillon cohérent n'établit pas automatiquement son origine technique ou sa date d'obtention. La confiance porte sur des faits précis, pas sur une validation générale de toutes les affirmations de l'acteur.

**Limite de cette édition :** les chiffres et détails relatifs aux échantillons sont **repris des contrôles consignés dans les fiches victimes**. Les archives clandestines brutes, les documents personnels et les journaux des organisations **n'ont pas été réanalysés** pour cette correction du rapport. En revanche, les 33 fiches dans les deux langues, les catégories de base et leurs totaux ont été rapprochés. Un audit documentaire ne remplace pas une investigation DFIR, une confirmation officielle ou une vérification d'authenticité complète.

[Consulter les fiches en français](./victims_FR.md) · [Version anglaise](./victims.md) · [Statistiques de référence](./STATISTIQUES_2026-08.json)

## 3. Panorama chiffré

### 3.1 Types de signalements - 33 dossiers

| Type | Dossiers | Part |
|---|---:|---:|
| **Ransomware** | **18** | **54,5 %** |
| **Fuite de données** | **14** | **42,4 %** |
| **Vente d'accès** | **1** | **3,0 %** |
| **Total** | **33** | **100 %** |

![Types de signalements](./assets/types_august_2026_FR.png)

Les 18 dossiers ransomware ne prouvent pas tous un chiffrement. La vente d'accès demeure une annonce non confirmée par une démonstration de fonctionnement.

### 3.2 Répartition géographique - 33 dossiers

| Pays | Dossiers | Part |
|---|---:|---:|
| Afrique du Sud | 12 | 36,4 % |
| Égypte | 5 | 15,2 % |
| Algérie | 5 | 15,2 % |
| Maroc | 3 | 9,1 % |
| Nigeria | 2 | 6,1 % |
| Kenya | 2 | 6,1 % |
| Maurice | 1 | 3,0 % |
| Cameroun | 1 | 3,0 % |
| Gabon | 1 | 3,0 % |
| Libye | 1 | 3,0 % |
| **Total** | **33** | **100 %** |

![Répartition géographique](./assets/countries_august_2026_FR.png)

L'Afrique du Nord compte **14 dossiers**, l'Afrique australe **12**, l'Afrique de l'Est **3**, l'Afrique de l'Ouest **2** et l'Afrique centrale **2**. L'absence de publication dans un pays ne démontre pas l'absence de menace.

### 3.3 Statuts documentaires - 33 dossiers

| Statut dans les fiches | Dossiers | Lecture CTI |
|---|---:|---|
| `Claim - Data Sample Published` | 13 | Publication accompagnée d'un échantillon, origine technique à établir |
| `Claim - Unverified` | 12 | Revendication sans confirmation indépendante suffisante |
| `Data Fully Published` | 4 | Divulgation déclarée complète, exhaustivité à évaluer |
| `Victim Confirmed` | 3 | Incident reconnu, sans attribution technique automatique du groupe |
| `Under Investigation` | 1 | Yalidine, signalement inclus et attribution non corroborée |
| **Total** | **33** | **Statuts de preuve, pas 33 compromissions** |

![Niveaux de preuve](./assets/evidence_august_2026_FR.png)

### 3.4 Confiance et impact potentiel

| Niveau de confiance | Dossiers | Impact potentiel | Dossiers |
|---|---:|---|---:|
| `Very High` | 3 | `Level 4` | 22 |
| `High` | 13 | `Level 3` | 8 |
| `Medium` | 7 | `Level 2` | 3 |
| `Low` | 9 | - | - |
| Confiance composite `High` (corpus) / `Medium` (attribution) | 1 | - | - |
| **Total** | **33** | **Total** | **33** |

Le niveau de confiance mesure la solidité des éléments analysés. Le niveau d'impact décrit les conséquences potentielles : il ne confirme pas la compromission ni des dommages effectivement constatés.

## 4. Analyse par type d'incident

### 4.1 Ransomware - publication criminelle et incidents établis

Les **18 dossiers** couvrent des situations de preuve différentes. **DC Partner**, le **Furniture Bargaining Council** et **Cartrack South Africa** ont fait l'objet de confirmations d'incident par les organisations concernées. Chez DC Partner, la confirmation du 7 août concernait un ransomware tandis que l'entreprise indiquait maintenir ses services opérationnels ; le rapprochement avec une revendication KRYBIT ne constitue pas une attribution forensique. Le Furniture Bargaining Council a reconnu le chiffrement de certains serveurs ; l'attribution à DeadLock n'est pas établie par cette seule déclaration. Cartrack a indiqué avoir détecté un ransomware le **26 août**, puis isolé les serveurs concernés et restauré sa plateforme ; sa déclaration ne désigne pas formellement un groupe auteur.

D'autres dossiers, notamment **ASHA Microfinance Bank**, **The Courier Guy** et le **Conseil Gabonais des Chargeurs**, disposent d'éléments documentaires structurés dont la lecture apporte une information concrète sur les risques de fraude, d'usurpation et de reconnaissance secondaire. Pour **CCA Bank**, l'analyse repose sur une publication attribuée à Everest et un **inventaire technique** de fichiers, non sur la lecture exhaustive des fichiers sources. Les volumes ou échéances annoncés par les groupes ne sont pas considérés comme confirmés.

**Point de vigilance :** un compte à rebours expiré sans divulgation accessible ne prouve ni négociation réussie, ni paiement, ni revente, ni inexistence des données. Ces situations restent à qualifier dossier par dossier.

### 4.2 Fuites de données - identités, administrations et prestataires

Les **13 dossiers canoniques** de fuite de données touchent des univers variés : administrations, enseignement supérieur, recrutement, services financiers, sécurité, télécommunications et commerce en ligne. Ils révèlent un même risque transversal : des données structurées publiées ou réutilisées peuvent alimenter des fraudes ciblées longtemps après leur première exposition.

Les dossiers les plus instructifs comprennent : **mPowa**, avec **2 585 CV** et **26 675 points géographiques** constatés dans un export Firebase ; **SnapStar Talent**, avec 300 candidatures cohérentes entre un CSV et un fichier TXT ; **RAMED**, avec **1 098 685 enregistrements** analysés et des photographies associées à une partie des dossiers ; et le dossier groupé de **six universités égyptiennes**, avec **7 762 241 enregistrements dans six CSV** et **5 540 documents** inventoriés. Ces chiffres décrivent les corpus examinés ; ils ne prouvent pas le vecteur d'accès ni le nombre de personnes uniques.

Le dossier **DGSN/DGST au Maroc** appelle une lecture particulièrement prudente : l'analyse décrit un corpus de **70 381 lignes** associables à des personnels, tandis que les institutions ont **démenti une intrusion directe** dans leurs systèmes et évoqué une origine tierce. La publication de données associées à des personnes ne confirme pas la compromission du système d'information de leur employeur.

### 4.3 Vente d'accès - un signal de risque, pas une preuve d'accès fonctionnel

Une annonce visant un **accès VPN présenté comme lié au ministère algérien du Commerce** est classée `Access Sale`. Le vendeur demande **500 USD**, mais aucun accès opérationnel ni niveau de privilège n'est démontré. Une organisation concernée doit vérifier ses accès distants et les usages anormaux, sans conclure à une intrusion à partir de l'annonce seule.

## 5. Secteurs exposés - classification normalisée

Chaque signalement reçoit un seul secteur principal, sans modifier la description professionnelle précise dans les fiches.

| Code | Secteur principal | Dossiers |
|---|---|---:|
| FIN | Finance / Banque | 6 |
| GOV | Gouvernement / Administration | 6 |
| EMP | Emploi / Recrutement | 3 |
| IND | Industrie / Ingénierie | 2 |
| RES | Restauration | 2 |
| HEA | Santé / Pharmaceutique | 2 |
| LOG | Transport / Logistique | 2 |
| AGR | Agriculture / Agroalimentaire | 1 |
| ECO | Commerce / E-commerce | 1 |
| REA | Immobilier | 1 |
| AUT | Mobilité / Automobile | 1 |
| MED | Médias / Édition | 1 |
| LAB | Relations sociales / Travail | 1 |
| SPO | Sports / Fédérations | 1 |
| TOU | Tourisme / Voyage | 1 |
| TEL | Télécommunications / Médias | 1 |
| EDU | Éducation / Université | 1 |
| **Total** | | **33** |

![Secteurs normalisés](./assets/sectors_august_2026_FR.png)

La finance et l'administration concentrent chacune **6 dossiers** ; les services d'emploi/recrutement en regroupent **3**. Le transport/logistique en compte **2**, dont Yalidine au statut `Under Investigation`. La visibilité d'un secteur dans ce corpus n'est pas une mesure directe de son risque réel.

## 6. Acteurs et comptes de publication - activité visible, attribution prudente

| Acteur / compte affiché | Dossiers associés | Lecture CTI |
|---|---:|---|
| KRYBIT | 6 | Mentions dans plusieurs pays ; attribution technique à confirmer dossier par dossier |
| TelephoneHooliganism | 3 | Trois publications visant des organisations algériennes, **dont Yalidine non corroborée** |
| Orova | 2 | Publications concernant l'Afrique du Sud et l'Égypte |
| exfilar | 2 | Publications concernant des environnements liés à Firebase |
| TheGentlemen | 2 | Deux organisations mentionnées |
| MedusaLocker | 2 | Deux dossiers en contexte ransomware |
| INC Ransom | 2 | Deux dossiers associés à ce nom |

![Acteurs et comptes représentés](./assets/actors_august_2026_FR.png)

**Attention à l'attribution :** ces nombres recensent des noms de groupes ou de comptes **affichés dans les publications**, et non des identités techniques démontrées. La confirmation d'un incident par une organisation ne suffit pas à identifier le groupe réellement impliqué.

## 7. Tendances, limites et besoins de collecte

**Ce qui est établi :** dans les dossiers documentés, la catégorie ransomware reste stable à **18**, tandis que les dossiers de fuite diminuent de **21 à 14** et ceux de vente d'accès de **6 à 1**. Ces évolutions reflètent le corpus documenté et ses règles d'inclusion, **pas un indice de recul du risque réel**. Les 33 fiches suivies d'août restent disponibles pour l'historique et le dossier Yalidine n'est pas effacé.

**Ce qui mérite un approfondissement :** origine technique des fichiers et des exports ; validité actuelle des accès, comptes et liens ; portée réelle des volumes annoncés ; chronologie des divulgations après les comptes à rebours. Ces inconnues nécessitent un recoupement documentaire ou une vérification autorisée par l'organisation concernée. L'expiration d'un compte à rebours ne démontre ni paiement de rançon ni publication intégrale.

**Ce que la veille ne permet pas de conclure :** la répartition pays/secteurs ne mesure pas la qualité de la protection nationale ; une identité ou un domaine cités dans un échantillon ne prouvent pas un accès au SI principal ; un volume total annoncé n'est pas un volume vérifié. Les documents issus de la collecte clandestine ne doivent pas être diffusés dans les annexes publiques.

**Prochaine action de qualité :** appliquer une grille identique aux 47 dossiers de juillet, aux 33 signalements documentés d'août et aux dossiers de septembre ; conserver les dates de publication, découverte, dernière vérification et qualification dans des champs séparés, puis recalculer les comparaisons historiques et canoniques.

## 8. MITRE ATT&CK - correspondances contextuelles, non attributions

| Hypothèse défensive | Technique ATT&CK | Télémétrie pertinente | Limite analytique |
|---|---|---|---|
| Abus d'identifiants légitimes | `T1078` - Valid Accounts | IAM, SSO, VPN, authentification, journaux de comptes | Usage non démontré pour tous les dossiers |
| Exploitation d'applications exposées | `T1190` - Exploit Public-Facing Application | WAF, applications, reverse proxy, traces d'erreur | Le vecteur initial est généralement inconnu |
| Accès à des référentiels de données | `T1213` - Data from Information Repositories | DLP, audit DB, fichiers et dépôts documentaires | Nature de l'accès et permissions à vérifier |
| Accès à des données stockées dans le cloud | `T1530` - Data from Cloud Storage | Cloud audit, règles de stockage, appels API | Misconfiguration plausible, exploit non établi |
| Chiffrement à des fins d'impact | `T1486` - Data Encrypted for Impact | EDR, FIM, fichiers et services | Applicable lorsque le chiffrement est confirmé, par exemple FBC |

Ces techniques servent de **pistes de détection préventive**. Le rapport ne prétend pas avoir reconstitué une chaîne d'attaque MITRE pour chaque publication observée.

## 9. Priorités stratégiques pour les directions

| Décision | Responsable | Résultat attendu | Justification documentaire |
|---|---|---|---|
| **P1 - Gouverner les données sensibles** | RSSI + métiers + DPO | Inventaire des référentiels RH, identité, finance et des personnes habilitées | Plusieurs échantillons portent sur ces catégories |
| **P1 - Maîtriser les accès et services exposés** | DSI + équipes IAM / Cloud | MFA sur les accès privilégiés, règles de stockage vérifiées, jetons inutiles révoqués après qualification | Dossiers cloud et vente d'accès revendiquée |
| **P1 - Préserver la continuité** | DSI + exploitation | Test de restauration réel et délais documentés sur un service critique | Incidents ransomware reconnus et revendications d'extorsion |
| **P2 - Encadrer les tiers** | RSSI + achats + juridique | Cartographie des prestataires, clauses de signalement et habilitations fournisseurs | Données client et chaîne de prestation potentiellement concernées |

**Règle d'activation :** ces priorités sont transversales. Si une organisation identifie une exposition ou compromission confirmée la concernant, elle déclenche son processus de réponse à incident selon les faits observés, ses obligations et ses impacts propres - et non selon une simple mention sur un site criminel.

## 10. Scénarios SOC à tester - hypothèses défensives

Les conditions ci-dessous sont **des exemples de logique analytique**, pas des IoC observés en août. Les seuils doivent être ajustés au trafic habituel, au volume des données et à la sensibilité métier.

| Hypothèse / ATT&CK | Télémétrie minimale | Corrélation proposée | Réduction des faux positifs / validation |
|---|---|---|---|
| **Export massif inhabituel** · T1213 | Audit SGBD, API Gateway, DLP, IAM | Sur une fenêtre glissante de 30 min : volume d'export supérieur à la référence du compte, accès à des tables sensibles, puis transfert sortant atypique | Exclure ETL et sauvegardes autorisés ; rejouer un export de test ; mesurer la précision des alertes |
| **Compte privilégié utilisé hors profil** · T1078 | SSO/IdP, VPN, PAM, EDR | Nouvel appareil ou réseau + connexion privilégiée + première consultation d'un dépôt sensible en 60 min | Recouper changements, astreintes et VPN d'entreprise ; vérifier identité et MFA |
| **Stockage cloud à permissions excessives** · T1530 (contexte) | CloudTrail / journaux équivalents, audit ACL et IAM, stockage objet | Passage d'un objet ou dépôt à un accès public, suivi de lectures inhabituelles ou de téléchargements répétés | Distinguer fichiers publics légitimes ; vérifier l'état des ACL avant de qualifier l'accès |
| **Préparation possible d'exfiltration** · T1560 (hypothèse) | EDR, audit fichiers, proxy, DNS | Compression inhabituelle de fichiers métier suivie d'une hausse du trafic sortant | Exclure maintenance, archives et transferts approuvés ; rechercher la chronologie de processus |
| **Chiffrement anormal** · T1486 | EDR, FIM, journaux fichiers, sauvegardes | Modification rapide d'un grand nombre de fichiers + processus atypique ou arrêt de services | Tester sur journaux simulés ; exclure tâches de migration/chiffrement légitimes |
| **Accès fournisseur hors périmètre** · T1078 (hypothèse) | PAM, VPN, IAM, applicatif | Compte tiers + horaire ou ressource nouvelle + export ou modification de privilèges | Vérifier fenêtres de support autorisées et liste contractuelle des ressources |

**Workflow SOC :** (1) vérifier la qualité du journal et l'identité du compte ; (2) recouper l'alerte avec les changements et les activités métier ; (3) analyser le périmètre des données et l'éventuel transfert ; (4) escalader selon la gravité et la confirmation ; (5) documenter les exceptions puis améliorer la règle. Les contrôles doivent être validés sur des données autorisées avant mise en production.

**Portée MITRE :** les techniques décrivent des **hypothèses comportementales**. Seul le chiffrement reconnu chez le Furniture Bargaining Council autorise ici à discuter T1486 comme effet confirmé au niveau déclaré ; il ne permet pas d'attribuer automatiquement le responsable technique.

## 11. Feuille de route à 7, 30 et 90 jours

| Échéance | Responsable | Action et livrable vérifiable | Indicateur de résultat |
|---|---|---|---|
| **7 jours** | RSSI + SOC | Recenser les accès privilégiés et identifier les journaux indisponibles sur les actifs critiques | % des accès et actifs critiques couverts |
| **7 jours** | DSI + sauvegardes | Réaliser une restauration isolée et consigner le temps réel de reprise | Restauration validée ; temps de reprise mesuré |
| **30 jours** | Propriétaires de données + DSI | Classer les référentiels sensibles et restreindre les exports non justifiés | % des dépôts classifiés et surveillés |
| **30 jours** | SOC / Detection Engineering | Tester trois règles comportementales (exports, comptes, chiffrement) et documenter les exceptions | Tests réussis ; faux positifs ; sources manquantes |
| **90 jours** | RSSI + achats + juridique | Passer en revue les tiers critiques et leurs accès, compléter les notifications contractuelles | % des tiers contrôlés et écarts clos |
| **90 jours** | Direction + comité de crise | Simuler fuite de données et indisponibilité ; décider des critères d'escalade | Compte rendu, décisions et actions suivies |

**Message de gestion :** la veille sert à déclencher des **vérifications proportionnées et mesurables**. La correction des statistiques et la protection des personnes font partie du même effort de confiance, pas d'une communication de crise généralisée.

## 12. Conclusion

Le mois d'août 2026 confirme l'utilité d'une veille centrée sur les **preuves disponibles**, et non sur la seule visibilité des groupes criminels. Les organisations africaines ne doivent ni ignorer les publications ni les traiter comme des preuves définitives de compromission. La réponse efficace consiste à **qualifier le signal**, **évaluer l'exposition réelle**, **protéger les personnes et les services**, puis **vérifier que les contrôles fonctionnent**.

**AFRINTEL** - Cyber Threat Intelligence & SOC  
[Dépôt GitHub AFRINTEL](https://github.com/Hatchepsoute/AFRINTEL) · [Fiches victimes août 2026](./victims_FR.md)
