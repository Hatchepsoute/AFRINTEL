# NightSpire - Profil acteur / ransomware

👉🏾 [**English version**](./profile.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Opération :** NightSpire
- **Type de menace :** Ransomware / Vol de données / Extorsion
- **Motivation :** Financière
- **Premiers signalements publics :** 2025
- **Zone africaine observée par AFRINTEL :** Égypte
- **Modèle opératoire :** Non établi de manière ferme ; les sources publiques divergent sur un éventuel modèle RaaS
- **Statut :** Surveillance active
- **Dernière mise à jour :** 26 août 2026

---

## 1. Synthèse du renseignement

NightSpire est une opération ransomware associée au vol de données, à l'extorsion et au chiffrement. Les sources publiques ne s'accordent pas complètement sur son modèle opératoire. AFRINTEL ne présente donc pas le RaaS comme un fait confirmé.

Une investigation Huntress publiée en 2026 apporte des preuves utiles au niveau incident. Dans ce cas, l'acteur a utilisé RDP, Chrome Remote Desktop, AnyDesk, Everything, 7-Zip et MEGASync avant l'exécution du ransomware NightSpire. Huntress insiste aussi sur le fait que les TTP peuvent varier d'un incident à l'autre et selon les éventuels affiliés.

AFRINTEL suit séparément des revendications NightSpire contre des organisations égyptiennes. Le cas Huntress ne prouve pas que la même chaîne d'attaque a été utilisée contre ces victimes africaines.

---

## 2. Observations AFRINTEL en Afrique

| Date | Pays | Victime | Secteur | Preuve | Portée | Confiance | Provenance |
|---|---|---|---|---|---|---|---|
| 24 mai 2026 | Égypte | Papa John's Egypt | Restauration / Food & Beverage | Revendication ransomware | Revendication propre à la victime | Élevée | Suivi victimes AFRINTEL |
| 24 mai 2026 | Égypte | Rawaj Consumer Finance | Services financiers | Revendication ransomware | Revendication propre à la victime | Élevée | Suivi victimes AFRINTEL |
| 26 mai 2026 | Égypte | B Investments (Basata / Basatamfi) | Services financiers / Private Equity | Revendication ransomware | Revendication propre à la victime | Élevée | Suivi victimes AFRINTEL |

AFRINTEL a observé trois revendications NightSpire visant des organisations égyptiennes en trois jours. Deux des trois victimes appartiennent au secteur financier. C'est utile pour la victimologie et le suivi de campagne, mais les preuves techniques propres aux victimes restent insuffisantes pour leur attribuer les TTP observées dans l'investigation externe.

---

## 3. TTP documentées au niveau incident par Huntress

| Tactique | Technique | ATT&CK | Comportement | Preuve | Portée | Confiance | Provenance |
|---|---|---|---|---|---|---|---|
| Mouvement latéral | Remote Desktop Protocol | T1021.001 | Accès à un endpoint via RDP | Observé | Incident | Élevée | Huntress, incident mars 2026 |
| C2 / Persistance | Remote Desktop Software | T1219.002 | Chrome Remote Desktop et AnyDesk installés comme footholds | Observé | Incident | Élevée | Huntress |
| Discovery | File and Directory Discovery | T1083 | Everything utilisé pour localiser et consulter des fichiers | Observé | Incident | Élevée | Huntress |
| Collection | Archive via Utility | T1560.001 | 7-Zip utilisé pour archiver des fichiers | Observé | Incident | Élevée | Huntress |
| Exfiltration | Exfiltration to Cloud Storage | T1567.002 | MEGASync exécuté et évalué comme probablement utilisé pour l'exfiltration | Évalué | Incident | Moyenne | Huntress |
| Impact | Data Encrypted for Impact | T1486 | Exécution de l'encrypteur NightSpire | Observé | Incident | Élevée | Huntress |

Huntress n'a **pas** confirmé l'affirmation de la note de rançon concernant 2,5 To de données volées. AFRINTEL ne considère donc pas ce volume comme vérifié.

---

## 4. Outils observés dans le cas Huntress

| Outil | Rôle | Preuve | Portée |
|---|---|---|---|
| RDP | Accès distant dans le cas documenté | Observé | Incident |
| Chrome Remote Desktop | Foothold / accès distant | Observé | Incident |
| AnyDesk | Foothold / accès distant | Observé | Incident |
| Everything | Recherche de fichiers / support à la collecte | Observé | Incident |
| 7-Zip | Préparation / archivage | Observé | Incident |
| MEGASync | Exfiltration probable | Évalué | Incident |
| VMware Workstation | Installé dans l'environnement compromis | Observé | Incident |
| WPS Office | Installé dans l'environnement compromis | Observé | Incident |

VMware Workstation et WPS Office ont été observés, mais la source n'établit pas clairement leur rôle malveillant exact.

---

## 5. IoC historiques issus des investigations Huntress

| Indicateur | Contexte | Date / Portée | Confiance |
|---|---|---|---|
| `bde50a42efc079edde1a314243ad339db2d42e343fbbcd39117803b0f5960355` | SHA-256, `enc.exe` | Incident du 2 déc. 2025 | Élevée |
| `ad67031e2ca68764fe1a7d6632c02b02a299d59efb920710011a9a2ccf4399b7` | SHA-256, `enc.exe` | Incident du 25 mars 2026 | Élevée |
| `.nspire` | Extension de fichiers chiffrés | Incident déc. 2025 | Élevée |
| `_nightspire_readme.txt` | Note de rançon | Incident déc. 2025 | Élevée |
| `[nspire_msg].txt` | Note de rançon | Incident mars 2026 | Élevée |

Ce sont des indicateurs historiques propres à des incidents. AFRINTEL ne dit pas qu'ils ont été observés contre les trois victimes égyptiennes ci-dessus.

---

## 6. Pistes de détection et Threat Hunting

Corrélations utiles :

- accès RDP suivi de l'installation de Chrome Remote Desktop ou AnyDesk ;
- nouvel outil de prise en main à distance sur un poste qui ne l'utilisait pas auparavant ;
- Everything suivi d'accès à des dossiers sensibles ;
- archivage 7-Zip juste après la phase de découverte ;
- exécution de MEGASync depuis un endpoint compromis ;
- combinaison inhabituelle accès distant + découverte + archivage + cloud sync ;
- création de fichiers `.nspire` ou des notes de rançon documentées.

Comme plusieurs outils sont légitimes, le contexte et la filiation des processus sont plus importants qu'un simple nom d'exécutable.

---

## 7. Évaluation d'attribution

L'association avec les victimes africaines repose sur les revendications NightSpire suivies par AFRINTEL. Les TTP des sections 3 et 4 viennent d'un incident Huntress distinct.

AFRINTEL les modélise donc séparément :

```text
Contexte acteur NightSpire
        +-- revendications victimes africaines AFRINTEL
        +-- TTP niveau incident Huntress
```

Aucune preuve propre aux victimes ne démontre actuellement que le mode opératoire Huntress a été utilisé contre B Investments, Rawaj Consumer Finance ou Papa John's Egypt.

### Lacunes pour les cas africains

- vecteur d'accès initial ;
- hashes malware ;
- infrastructure attaquante ;
- artefacts d'authentification ;
- mouvement latéral ;
- canal et volume d'exfiltration ;
- méthode de déploiement du ransomware.

---

## 8. Sources

- Huntress - **Decoding NightSpire: Ransomware IOCs Aren't Set in Stone**
- MITRE ATT&CK
- AFRINTEL - Renseignement victimes ransomware africaines, mai 2026

---

**AFRINTEL - African Cyber Threat Intelligence**
