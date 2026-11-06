# AFRINTEL - Revue qualité et traçabilité | Mars 2026

**Date :** 6 novembre 2026  
**Sources principales :** `victims(20261106-085832).md` et `victims_FR(20261106-085832).md` fournis par l'utilisateur.  
**Revue :** recherche publique ciblée pour les domaines institutionnels et confirmations officielles ; aucune nouvelle consultation des archives sensibles ni test d'identifiants.

## 1. Vérifications de cohérence

| Contrôle | Source historique | Résultat audité |
|---|---|---|
| Fiches explicitement présentes | Titre « 45 », résumé « 41 » | **45 fiches FR et 45 fiches EN** |
| Typologie | 19 ransomwares + 21 fuites + 1 fraude = 41 | **19 ransomwares + 24 fuites + 1 vente d'accès + 1 fraude = 45** |
| Lieux | Afrique du Sud 13/14, Égypte 9, Maroc 8 | **Afrique du Sud 17 ; Égypte 8 ; Maroc 8** |
| Sénégal | 1 | **2 : DGCPT (vente d'accès), UBA (fraude)** |
| Ransomware marqué par un groupe | Nombre constant | **19 revendications/publications** |
| Acteur CrowStealer | Ancien graphique : 5 | **4 entrées portant explicitement le libellé CrowStealer** |
| Libellés attribués | Nombre non stable dans les synthèses | **29 libellés distincts connus et 2 fiches non attribuées** |
| Dossier multi-pays | Confusion possible multi-comptage | **Loozap = 1 fiche ; pays couverts non dupliqués** |
| Statuts | Deux statuts hors taxonomie v2 | **Standard Bank = `Incident Confirmed by Victim` ; UBA = `Under Investigation` avec corroboration CERT** |

**Note :** ces chiffres représentent des **fiches documentaires de mars**, pas un décompte vérifié d'incidents techniques nouveaux survenus pendant mars. Le total canonique intermensuel devra être finalisé après rapprochement des duplications.

## 2. Sites officiels vérifiés et corrigés

| Fiche | Domaine d'origine | Site proposé | Type de vérification | Limite |
|---|---|---|---|---|
| Buffalo City Metropolitan Municipality | `*.gov.za` | **[buffalocitymetro.gov.za](https://www.buffalocitymetro.gov.za/)** ; [autre domaine gouvernemental répertorié](https://www.buffalocity.gov.za/) | [Annuaire officiel gov.za](https://www.gov.za/nso/about-government/contact-directory/ec-municipalities/buffalo-city-metropolitan-municipality) + site municipal | Existence institutionnelle, **pas compromission confirmée** |
| Northern Cape Department of Roads & Public Works | `*.gov.za` | **[ncrpw.ncpg.gov.za](http://ncrpw.ncpg.gov.za/)** | [Annuaire des départements provinciaux](https://provincialgovernment.co.za/units/view/94/northern-cape/roads-and-public-works) | Domaine répertorié ; disponibilité du site non garantie ; aucune attribution forensique |
| Standard Bank South Africa | Aucun champ `Site web` | **[standardbank.co.za](https://www.standardbank.co.za/southafrica/personal)** | [Communication officielle du 23 mars](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank) et [14 avril](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-data-incident-update-14-april) | Compromission de données confirmée, **systèmes transactionnels non accédés selon la banque** |
| Egypt Waste Management Regulatory Authority (WMRA) | `garb.gov.eg` | **[wmra.gov.eg/en](https://wmra.gov.eg/en/)** | Portail WMRA officiel publiquement accessible | **Ne pas affirmer** une relation technique entre les domaines ni une fuite établie |

Les domaines ajoutés sont conservés dans les fichiers victimes FR et EN. Les fiches indiquent explicitement quand un lien technique entre domaine et jeu de données **n'est pas établi**.

## 3. Corrections analytiques importantes

1. **Standard Bank :** l'organisation confirme l'existence d'un incident le 23 mars 2026. Le périmètre décrit le 14 avril concerne les applications administratives et documentaires ; aucun scénario de compromission des transactions ne doit être déduit de la fuite.
2. **UBA Sénégal :** le [ngCERT](https://cert.gov.ng/advisories/alert-on-cyber-enabled-atm-cash-out-attacks-targeting-african-financial-institutions) cite 3 421 retraits et plus de 2 millions USD. Il s'agit d'une corroboration externe du fraude/cash-out ; **aucune confirmation de la victime ni technique d'intrusion précise** n'a été produite dans cette revue. L'événement technique date de janvier 2026, sa documentation AFRINTEL de mars.
3. **Remita :** la [NDPC a ouvert une enquête](https://www.premiumtimesng.com/news/top-news/869669-ndpc-investigates-remita-sterling-bank-for-alleged-data-breach.html). Cela ne confirme pas les 3 To annoncés, la validité de secrets ni l'atteinte aux systèmes de chaque banque citée dans les archives.
4. **Gauteng :** la revendication Kazu de mai 2026 reste **une revendication liée non canonique**, non ajoutée aux chiffres de mars.
5. **Diesel-Electric :** fiches de février et mars portant un groupe similaire ; doublon intermensuel **à vérifier**, sans retrait silencieux de la fiche de mars.
6. **Antériorité documentaire :** Eventing South Africa, Loozap et Semsar Masr comportent des dates initiales de janvier 2026 ; Bridges remonte à février ; les activités alléguées en Guinée remontent à 2025.
7. **Données privées :** aucune identité individuelle, aucun mot de passe, secret, hash, pièce KYC, journal nominatif ni lien de téléchargement clandestin n'est ajouté à la sortie.
8. **Classification sectorielle :** voir `VALIDATION.json`. Une seule famille primaire attribuée par fiche ; gouvernance = 11, éducation = 6, technologies/prestataires = 5, finances = 4 et ingénierie = 4.

## 4. Interprétation des niveaux de preuve

- `Claim - Unverified` : publication revendiquée sans corroboration suffisante.
- `Claim - Data Sample Published` : échantillon décrit ; ni origine ni ensemble complet nécessairement vérifiés.
- `Data Fully Published` : une publication est classée complète dans le corpus ; cela **ne confirme pas** le volume ou l'intrusion initiale.
- `Incident Confirmed by Victim` : reconnaissance directe (Standard Bank).
- `Under Investigation` : statut conservé pour cas non totalement élucidés, notamment UBA Sénégal (fraude corroborée par CERT, accès initial et auteurs inconnus), et dossier santé Guinée.

**Décompte après normalisation :** 16 `Claim - Unverified`, 15 `Claim - Data Sample Published`, 11 `Data Fully Published`, 1 `Incident Confirmed by Victim`, 2 `Under Investigation` = **45 fiches**.

## 5. Rapport et graphiques

Les rapports utilisent uniquement les **graphiques corrigés générés depuis les 45 fiches**, dans le dossier `assets/`. Les anciens graphiques fournis ne sont pas recopiés car ils ne reflètent pas tous les dossiers. Les visualisations de secteurs utilisent une grille de familles normalisées au lieu de reproduire une quarantaine de libellés uniques sur un camembert illisible.

### Contrôles à automatiser dans le dépôt

- CI : recompter `^####`, vérifier les en-têtes FR/EN et la présence d'un type principal et d'un statut autorisé.
- CI : valider `country`, `actor`, `sector`, `date_initial_post`, `date_detected`, `evidence_type`, `source_url`, `linked_claims` ; refuser les totaux contradictoires.
- CI : détecter chevauchements intermensuels (`domain` + victime + marque + similarité de publication), sans supprimer sans preuve.
- CI : exiger la présence d'images `assets/*.png` effectivement référencées dans les `README`.
- CTI : conserver les preuves de première main, l'historique des corrections et la distinction *Observed / Claimed / Unknown* pour chaque fiche.

**À confirmer ultérieurement :** identité technique des organisations derrière les données quand seule une publication de forum existe ; volume réel des archives ; impact opérationnel ; éventuelles nouvelles confirmations officielles. Cette revue ne prétend pas avoir vérifié l'intégralité des 45 événements auprès des victimes.
