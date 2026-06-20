[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Month](https://img.shields.io/badge/Month-F%C3%A9vrier%202024-lightgrey)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)
![TLP](https://img.shields.io/badge/TLP-CLEAR-brightgreen)

# Rapport CTI - Février 2024 : Expansion géographique vers l'Afrique du Nord et de l'Ouest

👉🏾 [English version available here](./README.md)

### 1. Résumé exécutif

En février 2024, l'Afrique a enregistré **5 victimes** documentées d'attaques par ransomware dans 4 pays. Par rapport à janvier (3 victimes, toutes en Afrique du Sud), le mois marque une **expansion géographique nette**, l'Égypte, la Tunisie, la Côte d'Ivoire et l'Afrique du Sud sont toutes ciblées. Quatre groupes ransomware distincts sont actifs.

👉🏾 [Liste des victimes](./victims_FR.md)

**Chiffres clés :**
- 🔹 **5 victimes** identifiées
- 🔹 **4 groupes actifs** : Medusa (1), Hunters (1), LockBit3 (2), DragonForce (1)
- 🔹 **Pays touchés** : Afrique du Sud (2), Égypte (1), Tunisie (1), Côte d'Ivoire (1)
- 🔹 **Secteurs** : Services numériques/Télécom, Industrie, Santé & Recherche, Biens de consommation, Services publics

---

### 2. Chronologie des attaques

| Date | Victime | Pays | Groupe ransomware |
|------|---------|------|-------------------|
| 6 février | ArpuPlus | Égypte | Medusa |
| 10 février | SOPEM Tunisie | Tunisie | Hunters |
| 13 février | The Aurum Institute | Afrique du Sud | LockBit3 |
| 27 février | Nouvelle Parfumerie Gandour (NPGCI) | Côte d'Ivoire | LockBit3 |
| 29 février | ERWAT | Afrique du Sud | DragonForce |

```mermaid
timeline
    title Attaques ransomware en Afrique - Février 2024
    6 février : ArpuPlus (Égypte) - Medusa
    10 février : SOPEM Tunisie (Tunisie) - Hunters
    13 février : The Aurum Institute (Afrique du Sud) - LockBit3
    27 février : NPGCI (Côte d'Ivoire) - LockBit3
    29 février : ERWAT (Afrique du Sud) - DragonForce
```

---

### 3. Analyse des victimes

#### 3.1 Par pays

| Pays | Nombre d'attaques |
|------|-----------------|
| Afrique du Sud | 2 |
| Égypte | 1 |
| Tunisie | 1 |
| Côte d'Ivoire | 1 |

```mermaid
pie showData
    title Répartition par pays - Février 2024 (5 victimes)
    "Afrique du Sud" : 2
    "Égypte" : 1
    "Tunisie" : 1
    "Côte d'Ivoire" : 1
```

#### 3.2 Par secteur

| Secteur | Nombre |
|---------|--------|
| Services numériques / Télécom | 1 |
| Industrie (Métallurgie) | 1 |
| Santé & Recherche | 1 |
| Biens de consommation (Cosmétiques) | 1 |
| Services publics (Traitement des eaux) | 1 |

```mermaid
xychart-beta
    title "Secteurs ciblés - Février 2024"
    x-axis ["Numérique/Télécom", "Industrie", "Santé", "Biens conso.", "Services publics"]
    y-axis "Nombre d'attaques" 0 to 2
    bar [1, 1, 1, 1, 1]
```

#### 3.3 Groupes ransomware

| Groupe ransomware | Nombre d'attaques |
|-----------------|-----------------|
| LockBit3 | 2 |
| Medusa | 1 |
| Hunters | 1 |
| DragonForce | 1 |

```mermaid
gantt
    title Groupes ransomware actifs - Février 2024
    dateFormat X
    axisFormat %s
    section LockBit3
    LockBit3 : 0, 2
    section Medusa
    Medusa : 0, 1
    section Hunters
    Hunters : 0, 1
    section DragonForce
    DragonForce : 0, 1
```

---

### 4. Points d'attention

- **Expansion géographique** : Février 2024 est le premier mois à voir des attaques simultanées en Afrique du Nord (Égypte, Tunisie), Afrique de l'Ouest (Côte d'Ivoire) et Afrique australe (Afrique du Sud).
- **Première apparition de DragonForce** : le groupe revendique ERWAT (traitement des eaux usées desservant 3,5 millions de personnes), une attaque d'infrastructure critique signalant un intérêt pour les services essentiels.
- **Santé sous pression** : The Aurum Institute, organisation majeure de recherche VIH/Tuberculose, est ciblée par LockBit3, des données de santé publique sensibles sont exposées.
- **Industrie ouest-africaine** : NPGCI (cosmétiques grand public, Abidjan) marque la première victime ouest-africaine de LockBit3 en 2024.
- **Services numériques en Afrique du Nord** : ArpuPlus (Égypte) illustre un intérêt croissant pour les opérateurs télécom et les fournisseurs de services à valeur ajoutée de la zone MENA.

---

```mermaid
xychart-beta
    title "Évolution mensuelle des attaques (Jan - Fév 2024)"
    x-axis ["Jan", "Fév"]
    y-axis "Nombre d'attaques" 0 to 6
    bar [3, 5]
```

### 5. Recommandations

| Domaine | Action recommandée |
|---------|--------------------|
| Infrastructures critiques (eau, énergie) | Segmenter les réseaux OT/IT, maintenir des sauvegardes hors ligne, surveiller les accès SCADA. |
| Santé & Recherche | Chiffrer les bases de données de recherche, restreindre les accès externes, surveiller l'exfiltration. |
| Fournisseurs numériques/Télécom | Corriger les vulnérabilités d'API, surveiller les fuites de credentials. |
| Industrie | Auditer l'exposition des systèmes industriels, renforcer la protection endpoint. |
| Toutes organisations | Surveiller DragonForce et Medusa comme groupes émergents, analyser leurs IOCs. |

---

*Rapport généré à partir des données OSINT AFRINTEL. Diffusion libre (TLP:CLEAR)*
