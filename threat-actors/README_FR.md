# AFRINTEL - Renseignement sur les acteurs de menace

👉🏾 [**English version**](./README.md)

Cette section regroupe les profils d'acteurs de menace et les études de cas DFIR utilisés par AFRINTEL pour comprendre les modes opératoires derrière les incidents cyber qui touchent les organisations africaines.

L'objectif est simple : ne pas s'arrêter au nom affiché sur un leak site. Il faut distinguer ce qui est connu sur l'acteur, ce qui appartient à une campagne et ce qui est réellement confirmé dans un incident précis.

## Analyses disponibles

| Entrée | Type | Contenu principal | Langues |
|---|---|---|---|
| [Akira](./akira/akira_profile_FR.md) | Profil acteur / ransomware | TTP, CVE, outils, exfiltration, évolution du ransomware | FR / EN |
| [NightSpire](./nightspire/profile_FR.md) | Profil acteur / ransomware | Victimologie africaine, TTP d'incident, IoC, limites d'attribution | FR / EN |
| [PYSA / Mespinoza](./pysa-mespinoza/dfir_case_study_FR.md) | Étude de cas DFIR | Intrusion de huit heures, vol d'identifiants, RDP, Koadic, Empire, exfiltration | FR / EN |
| [Ryuk / Wizard Spider](./ryuk/ryuk_profile_FR.md) | Malware / acteur + référence DFIR | Séparation des entités, BazarLoader, Cobalt Strike, Zerologon, déploiement Ryuk | FR / EN |
| [UNC6040 / Salesforce](./unc6040-salesforce/case_study_FR.md) | Campagne SaaS / cluster | Vishing, Connected Apps malveillantes, abus OAuth, exfiltration API Salesforce | FR / EN |
| [Qilin / Agenda](./qilin/profile_FR.md) | Profil acteur / ransomware | Accès VPN, vol d'identifiants, ESXi, exfiltration, évolution des campagnes Qilin | FR / EN |
| [Gunra](./gunra/profile_FR.md) | Profil acteur / ransomware | Exploitation Fortinet, dump NTDS, tunnels SSH, vol cloud, inhibition de restauration | FR / EN |

## Comment AFRINTEL qualifie le renseignement

AFRINTEL sépare quatre notions.

### Preuve

- **Observé** - directement vu dans une télémétrie, une analyse malware, une investigation DFIR ou une source primaire.
- **Rapporté** - documenté par une source technique, institutionnelle ou DFIR fiable.
- **Évalué** - conclusion analytique basée sur plusieurs éléments disponibles.
- **Inféré** - relation plausible, mais les preuves restent insuffisantes pour une conclusion forte.

### Portée

- **Niveau acteur** - comportement associé à l'acteur ou à l'écosystème ransomware dans son ensemble.
- **Niveau campagne** - comportement lié à une campagne ou à un cluster d'activité défini.
- **Niveau incident** - comportement confirmé dans une intrusion documentée.
- **Niveau victime** - preuve directement liée à une victime suivie par AFRINTEL.

### Confiance

AFRINTEL utilise les niveaux **Élevée**, **Moyenne** et **Faible**. Le niveau de confiance mesure la qualité et la cohérence des preuves, pas la gravité de l'incident.

### Provenance

La source d'une information importante doit rester visible : AFRINTEL, DFIR, CERT/autorité, éditeur de sécurité, MITRE ATT&CK ou autre source CTI.

## Règle analytique principale

Une revendication ransomware contre une victime ne prouve **pas** que toutes les TTP connues de ce ransomware ont été utilisées dans l'incident.

Par exemple, si une victime Akira apparaît dans AFRINTEL, les informations générales sur Mimikatz, RClone ou PowerTool ne deviennent pas automatiquement des preuves propres à cette victime. Il faut une preuve spécifique à l'incident.

La même règle s'applique aux IoC. Les hashes, domaines et adresses IP historiques doivent rester liés à leur date et à leur contexte. Ils ne doivent pas être présentés comme une infrastructure active sans nouvelle validation.

## Priorité des sources

En cas de différence entre plusieurs sources, AFRINTEL donne la priorité à :

1. la télémétrie d'incident et les preuves DFIR primaires ;
2. les CERT, autorités et avis des forces de l'ordre ;
3. les recherches techniques bien documentées des éditeurs de sécurité ;
4. MITRE ATT&CK pour la taxonomie et le contexte des entités ;
5. les dépôts CTI communautaires comme pistes de recherche complémentaires.

Les dépôts communautaires sont utiles pour trouver des pistes, mais les éléments importants doivent être vérifiés dans la source d'origine quand elle est disponible.

## Prompt analyste réutilisable

Le prompt utilisé pour créer ou auditer les fiches de cette section est disponible ici :

- [PROMPT.md](./PROMPT.md)

---

**AFRINTEL - African Cyber Threat Intelligence**
