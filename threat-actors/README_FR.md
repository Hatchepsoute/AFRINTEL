# AFRINTEL - Renseignement sur les acteurs de menace

👉🏾 [**English version available here**](./README.md)

Cette section regroupe les profils d’acteurs de menace et les analyses de campagne AFRINTEL, avec un focus sur les menaces affectant les organisations africaines.

Les analyses combinent notamment :

- le profilage des acteurs de menace et l’analyse de la victimologie ;
- le mapping des TTP avec MITRE ATT&CK ;
- l’analyse des malwares et outils utilisés ;
- la corrélation des IoC et infrastructures lorsqu’ils sont disponibles ;
- l’analyse des chronologies d’incident et de campagne ;
- l’attribution basée sur des niveaux de confiance ;
- la distinction entre renseignement observé, rapporté, évalué et inféré.

---

## Profils d’acteurs de menace

| Acteur de menace | Type | Contenu analytique | Langues |
|---|---|---|---|
| NightSpire | Ransomware / Extorsion | Victimologie africaine, TTP, outils, IoC, évaluation d’attribution | EN / FR |
| Akira | Ransomware / RaaS | TTP, vulnérabilités, outils, artefacts techniques, renseignement orienté détection | EN / FR |

---

## Principe analytique

AFRINTEL n’applique pas automatiquement les TTP connues d’un acteur à chaque victime africaine qui lui est associée.

Les éléments suivants sont maintenus séparément afin d’éviter toute sur-attribution :

- les revendications publiques des acteurs ;
- les observations techniques ;
- les évaluations analytiques ;
- les éléments confirmés de manière indépendante.

---

## Modèle de qualification des preuves

AFRINTEL utilise quatre niveaux principaux :

### Observé

Élément directement constaté dans une télémétrie technique, une analyse de malware, une investigation de réponse à incident ou une source primaire.

### Rapporté

Élément documenté par une source externe fiable, telle qu’un CERT, une autorité, un éditeur de sécurité ou une équipe DFIR.

### Évalué

Conclusion analytique fondée sur plusieurs observations ou éléments de renseignement disponibles.

### Inféré

Relation plausible pour laquelle les preuves techniques sont encore insuffisantes pour établir une attribution forte.

---

## Objectif

L’objectif de cette section est de transformer les données de victimes AFRINTEL en renseignement plus opérationnel en reliant :

```text
Acteur de menace
        │
        ├── TTP / MITRE ATT&CK
        ├── Malware / Outils
        ├── IoC / Infrastructure
        ├── Campagnes
        └── Victimologie africaine
