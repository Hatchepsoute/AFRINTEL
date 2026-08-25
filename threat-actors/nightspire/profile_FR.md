# NightSpire - Profil de l’acteur de menace

👉🏾 [**English version available here**](./profile.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Groupe :** NightSpire
- **Type de menace :** Ransomware / Extorsion
- **Motivation :** Financière
- **Activité suivie par AFRINTEL :** Oui
- **Zone géographique principale observée par AFRINTEL :** Égypte
- **Statut de l’évaluation :** Surveillance active
- **Dernière mise à jour :** 25 août 2026

---
## 1. Synthèse du renseignement

NightSpire est une opération ransomware associée au vol de données, à l’extorsion et au chiffrement de fichiers.

Des rapports publics de réponse à incident montrent que des intrusions associées à NightSpire peuvent impliquer des logiciels légitimes de prise en main à distance ainsi que des outils commerciaux utilisés pour l’accès distant, la découverte de fichiers, la préparation des données et leur exfiltration.

AFRINTEL suit les activités de NightSpire affectant des organisations africaines et maintient une distinction stricte entre :

- les revendications du groupe ransomware ;
- les observations techniques documentées de manière indépendante ;
- les évaluations analytiques AFRINTEL ;
- les éléments techniques confirmés pour une victime spécifique.

La présence d’une organisation sur le site de fuite de NightSpire ne démontre pas, à elle seule, que l’ensemble des TTP connues de NightSpire ont été utilisées contre cette organisation.

---

## 2. Observations AFRINTEL en Afrique

| Date | Pays | Victime | Secteur | Élément de preuve AFRINTEL |
|---|---|---|---|---|
| 24 mai 2026 | Égypte | Papa John's Egypt | Restauration / Food & Beverage | Revendication ransomware NightSpire |
| 24 mai 2026 | Égypte | Rawaj Consumer Finance | Services financiers | Revendication ransomware NightSpire |
| 26 mai 2026 | Égypte | B Investments (Basata / Basatamfi) | Services financiers / Private Equity | Revendication ransomware NightSpire |

### Évaluation AFRINTEL

AFRINTEL a observé un cluster de trois revendications NightSpire visant des organisations égyptiennes sur une période de trois jours.

Deux des trois organisations opèrent dans le secteur financier, tandis que la troisième appartient au secteur de la restauration.

Cette concentration temporelle et géographique constitue un élément pertinent pour l’analyse de la victimologie et le suivi de campagne.

Cependant, AFRINTEL ne dispose actuellement d’aucune télémétrie propre à ces victimes permettant de démontrer que les TTP documentées dans les investigations externes sur NightSpire ont été utilisées contre
ces trois organisations égyptiennes.

**Niveau de confiance :** élevé concernant les revendications du groupe et l’association avec les victimes ; preuves insuffisantes pour attribuer des TTP spécifiques à chaque victime.

---

## 3. Comportements opérationnels documentés de NightSpire

Les comportements suivants proviennent d’investigations techniques indépendantes et ne doivent pas être automatiquement attribués à chaque sincident NightSpire suivi par AFRINTEL.

| Tactique ATT&CK | Technique | ID ATT&CK | Comportement observé | Type de preuve | Confiance |
|---|---|---|---|---|---|
| Mouvement latéral | Remote Desktop Protocol | T1021.001 | Accès à un endpoint via RDP | Observé | Élevée |
| Command & Control | Remote Desktop Software | T1219.002 | Déploiement de Chrome Remote Desktop et AnyDesk pour l’accès distant / la persistance | Observé | Élevée |
| Découverte | File and Directory Discovery | T1083 | Utilisation d’Everything pour rechercher et accéder aux fichiers | Observé | Élevée |
| Collection | Archive via Utility | T1560.001 | Utilisation de 7-Zip pour archiver des fichiers sélectionnés | Observé | Élevée |
| Exfiltration | Exfiltration to Cloud Storage | T1567.002 | Exécution de MEGASync pendant l’intrusion, probablement utilisé pour l’exfiltration | Évalué | Moyenne |
| Impact | Data Encrypted for Impact | T1486 | Exécution du ransomware NightSpire et chiffrement de fichiers | Observé | Élevée |

---

## 4. Outils observés

| Outil | Usage | Statut de preuve |
|---|---|---|
| RDP | Accès distant | Observé |
| Chrome Remote Desktop | Accès distant / Persistance | Observé |
| AnyDesk | Accès distant / Persistance | Observé |
| Everything | Découverte de fichiers / Support à la collecte | Observé |
| 7-Zip | Préparation / Archivage des données | Observé |
| MEGASync | Exfiltration potentielle de données | Évalué |
| VMware Workstation | Observé dans l’environnement compromis | Observé |
| WPS Office | Observé dans l’environnement compromis | Observé |

---

## 5. Indicateurs de compromission

Les indicateurs suivants ont été rapportés lors d’investigations
indépendantes liées à NightSpire.

| Type d’indicateur | Contexte | Confiance |
|---|---|---|
| SHA-256 | Échantillon de l’encrypteur NightSpire - décembre 2025 | Élevée |
| SHA-256 | Échantillon de l’encrypteur NightSpire - mars 2026 | Élevée |
| Extension de fichier | `.nspire` utilisée pour les fichiers chiffrés | Élevée |
| Note de rançon | `_nightspire_readme.txt` | Élevée |
| Note de rançon | `[nspire_msg].txt` | Élevée |

AFRINTEL n’affirme pas que ces indicateurs ont été observés contre les victimes africaines listées ci-dessus, sauf si des éléments techniques propres aux incidents permettent de le confirmer.

---

## 6. Évaluation de l’attribution

### Modèle de qualification des preuves

AFRINTEL utilise quatre niveaux de qualification :

**Observé**  
Élément directement observé dans une télémétrie technique, une analyse de malware, une investigation de réponse à incident ou une source primaire.

**Rapporté**  
Élément documenté par une source externe fiable de renseignement ou de réponse à incident.

**Évalué**  
Conclusion analytique obtenue à partir de plusieurs observations et éléments disponibles.

**Inféré**  
Relation plausible pour laquelle les preuves techniques disponibles restent insuffisantes pour établir une attribution forte.

### Évaluation actuelle de NightSpire

L’association entre NightSpire et les organisations africaines répertoriées par AFRINTEL repose sur les revendications publiques du groupe ransomware.

Des éléments indépendants issus d’investigations de réponse à incident documentent par ailleurs des outils et TTP associés à des opérations NightSpire.

AFRINTEL ne dispose cependant pas, à ce stade, de suffisamment d’éléments techniques pour affirmer que la même chaîne d’intrusion a été utilisée contre B Investments, Rawaj Consumer Finance ou Papa John's Egypt.

Cette distinction permet d’éviter que des renseignements au niveau de l’acteur soient présentés à tort comme de la télémétrie propre à une victime spécifique.

---

## 7. Notes analytiques

Les investigations externes montrent des variations entre plusieurs incidents NightSpire, notamment au niveau de l’encrypteur, du nom des notes de rançon et des outils utilisés.

NightSpire ne doit donc pas être modélisé comme disposant d’un ensemble figé et immuable d’IOC ou de TTP.

Plusieurs hypothèses peuvent expliquer ces variations :

- évolution de l’opération ransomware ;
- modification du mode opératoire des attaquants ;
- intervention de différents affiliés ou équipes d’intrusion ;
- utilisation d’outils spécifiques selon les campagnes.

Dans AFRINTEL, les renseignements NightSpire doivent donc être maintenus sur deux niveaux :

1. **Niveau acteur** - comportements connus et documentés ;
2. **Niveau incident** - techniques effectivement confirmées pour une victime précise.

---

## 8. Lacunes de renseignement AFRINTEL

Les principales lacunes actuelles concernant les incidents NightSpire affectant des organisations africaines sont les suivantes :

- vecteur d’accès initial ;
- hashes de malware propres aux victimes ;
- infrastructure utilisée par l’attaquant ;
- artefacts d’authentification ;
- techniques de mouvement latéral confirmées ;
- canal d’exfiltration confirmé ;
- méthode exacte de déploiement et de chiffrement.

Ces éléments devront être mis à jour si de nouvelles preuves techniques
deviennent publiquement disponibles ou sont obtenues dans le cadre
des analyses AFRINTEL.

---

## 9. Sources

- Huntress - *Decoding NightSpire: Ransomware IOCs Aren't Set in Stone*
- MITRE ATT&CK - T1021.001 Remote Desktop Protocol
- MITRE ATT&CK - T1219.002 Remote Desktop Software
- MITRE ATT&CK - T1083 File and Directory Discovery
- MITRE ATT&CK - T1560.001 Archive via Utility
- MITRE ATT&CK - T1567.002 Exfiltration to Cloud Storage
- MITRE ATT&CK - T1486 Data Encrypted for Impact
- AFRINTEL - Renseignement sur les victimes ransomware africaines - Mai 2026

---

**AFRINTEL - African Cyber Threat Intelligence**
