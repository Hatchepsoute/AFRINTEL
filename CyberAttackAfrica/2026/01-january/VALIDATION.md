# AFRINTEL | Contrôle qualité de janvier 2026

- **Périmètre recalculé :** 31 fiches FR et 31 fiches EN, dans le même ordre.
- **Catégories :** Ransomware 19 + Data Leak 10 + Access Sale 1 + Defacement 1 = **31**.
- **Pays :** 13 pays, somme des occurrences nationales = **31**.
- **Régions :** Afrique du Nord 13 + Afrique australe 7 + Afrique de l'Est 6 + Afrique de l'Ouest 4 + océan Indien 1 = **31**.
- **Secteurs normalisés :** 13 catégories, somme = **31**.
- **Statuts :** 15 `Claim - Unverified`, 11 `Claim - Data Sample Published`, 2 `Data Fully Published`, 1 `Corroborated`, 1 `Victim Confirmed`, 1 `Under Investigation` = **31**.
- **Étiquettes d'acteurs :** TheGentlemen 6 + tengu 5 + dark07x 2 + autres étiquettes individuelles 15 + sans attribution humaine fiable 3 = **31**.
- **Comparaison décembre :** recomptage du couple `victims_FR.md` / `victims.md` de décembre 2025 sur GitHub, 20 cartes dans chaque langue, dont 14 `Ransomware` et 6 `Data Leak`. Le résumé historique indique encore 19 et doit être actualisé. Le comparatif reste indiqué comme provisoire.
- **Anomalie d'en-tête janvier :** le fichier français parle de 23 incidents mais ventile 17 + 2 + 1 + 1, soit 21 ; le fichier anglais annonce 21. Les deux contiennent en réalité 31 fiches. Une correction des en-têtes sources est recommandée avant mise à jour du dépôt.
- **Graphiques utilisateur :** 23 observations dans la répartition des types. Remplacés ici par 10 images corrigées et localisées (5 FR, 5 EN).
- **Limites conservées :** aucun nouvel examen des données brutes, aucune confirmation inventée, aucune PII ou secret reproduit. Les statuts des fiches ne sont pas modifiés.

## Intégration GitHub

Placer `README_FR.md`, `README.md` et le dossier `assets/` dans :

`CyberAttackAfrica/2026/01-january/`

Les liens relatifs des deux rapports pointent vers les fichiers `victims_FR.md` et `victims.md` déjà attendus dans ce dossier.

Avant commit, corriger les résumés des deux fichiers `victims*` de janvier et, séparément, le décalage historique de décembre 2025, puis refaire le contrôle FR/EN et les statistiques dérivées.
