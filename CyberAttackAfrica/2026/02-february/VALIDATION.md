# AFRINTEL - Contrôle qualité du rapport CTI, février 2026

## Vérifications réalisées

- Sources : `victims_FR(20261106-081918).md` et `victims(20261106-081918).md`, transmis par l'utilisateur.
- **27 fiches dans chaque version** ; parité d'ordre des victimes vérifiée.
- **20 fiches Ransomware** et **7 fiches Data Leak** ; le résumé initial indiquant **21 incidents (20 + 1)** était obsolète.
- **14 pays couverts**. Le jeu Nigeria / Côte d'Ivoire est un seul dossier multi-pays ; il est représenté par une catégorie `MULTI NG/CI` dans les comptes géographiques pour éviter le double comptage.
- États documentaires : **18 Claim - Unverified, 7 Claim - Data Sample Published, 2 Data Fully Published**. Aucune confirmation explicite par la victime dans les fiches de février.
- Images originales : les graphiques de type d'incident, de géographie, de secteurs et d'acteurs couvrent les **20 dossiers ransomware seulement**, pas le corpus de 27. Les graphiques joints au rapport ont été **recalculés intégralement**.
- Comparaison janvier 2026 : **31 observations**, dont 19 ransomware, 10 data leaks, une vente d'accès et un défacement. Comparaison en nombre de dossiers, non en attaques confirmées.
- Secteurs : classification analytique harmonisée dans les tableaux du rapport ; la catégorie « Administration et données identitaires » comprend une revendication multi-pays sans administration victime identifiée.
- Région : Maurice distinguée sous « Océan Indien » ; Soudan sous « Afrique de l'Est » ; ces conventions sont documentées.

## Modifications **proposées uniquement dans les copies livrées** des fichiers victimes

1. `victims_FR.md` et `victims.md` : en-têtes corrigés pour annoncer **27 dossiers = 20 ransomware + 7 fuites**. Ne pas présenter automatiquement ces 27 dossiers comme 27 intrusions indépendantes.
2. Deux fiches `Al Akhawayn University` et `Chezpara.ma` : champ `Type d'incident` / `Incident type` ajouté explicitement comme **Data Leak**, ce qui était déjà indiqué dans leurs titres et descriptions.
3. **Aucune donnée de victime, volume, acteur, échantillon ou date n'a été inventée ou ajoutée**. Les copies locales sont des propositions éditoriales : les fichiers sources transmis ne sont pas modifiés.

## Lacunes conservées

- Plusieurs fiches utilisent des secteurs bruts imprécis : `Ghana Bauxite` décrit comme « service public » alors que l'activité métier est minière ; `Wells Fargo Kenya` décrit comme « banque » alors que le contexte correspond à la sécurité/logistique. Le rapport utilise le **secteur métier explicite** mais ne modifie pas les intitulés des fiches initiales.
- `DAF SÉNÉGAL` : 139 To revendiqués dans la synthèse source, sans vérification étayée dans la fiche. Volume non présenté comme prouvé.
- `0APT` : 6,85 To cumulés sont cités dans la synthèse source, sans ventilation technique par victime. Ce volume n'est pas repris comme exfiltration confirmée.
- `Air Côte d'Ivoire` : environ 208 Go indiqués par le site de fuite ; un document de paie lié à 529 personnes et daté de 2022 est décrit comme échantillon examinable. Le document ne valide pas le volume global.
- `HIMS University` : total annoncé **28 124**, sous-totaux affichés **28 004**, écart de **120**.
- `Heliopolis University` : **19 790** revendiqués, **62** comptes décrits dans un classeur échantillon.
- `Diesel-Electric` : rapprochement à faire avec les publications de décembre 2025 et de mars 2026 avant toute conclusion de nouvelle intrusion.
- Aucun échantillon sensible original n'a été fourni ici pour revalidation. Les assertions concernant les analyses d'échantillons sont **rapportées à partir des fiches AFRINTEL**, non reconduites par une analyse indépendante dans cette génération.

## Contrôles de publication

- Les 14 graphiques FR/EN sous `assets/` sont inclus dans le dossier ; les liens Markdown pointent vers des fichiers existants.
- Les deux README présentent les mêmes chiffres, sans prétendre établir une compromission officielle.
- Les cartes de risque P1/P2 du rapport constituent des **priorités de revue**, pas des niveaux d'impact forensique assignés aux victimes.
- Rapports et presentation : diffusion `TLP:CLEAR`, aucune valeur personnelle ou clé d'accès brute reproduite.

**Avant commit :** relire et approuver les modifications apportées aux copies de `victims_FR.md` et `victims.md` ; conserver les dates et l'ordre de publication ; synchroniser les graphiques avec la même convention régionale.
