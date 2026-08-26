# Ryuk / Wizard Spider - Ransomware, contexte acteur et référence DFIR

👉🏾 [**English version**](./ryuk_profile.md)

**AFRINTEL Threat Actor Intelligence**

- **Ransomware / Malware :** Ryuk
- **Logiciel MITRE ATT&CK :** S0446
- **Groupe associé :** Wizard Spider
- **Groupe MITRE ATT&CK :** G0102
- **Groupes associés / alias :** UNC1878, FIN12 et d'autres noms listés par MITRE ATT&CK
- **Type de menace :** Ransomware / Big-game hunting
- **Motivation :** Financière
- **Référence DFIR :** Ryuk Speed Run - 2 Hours to Ransom
- **Date du cas :** 5 novembre 2020
- **Géographie :** cas DFIR externe, pas une victime africaine AFRINTEL
- **Statut :** Référence historique de tradecraft
- **Dernière mise à jour :** 26 août 2026

---

## 1. Note de modélisation des entités

Ryuk est **un malware**, pas un acteur à lui seul. MITRE ATT&CK référence Ryuk comme logiciel **S0446**. Wizard Spider est suivi séparément comme groupe **G0102**, avec UNC1878 parmi les noms de groupes associés.

AFRINTEL maintient donc ces entités séparées :

```text
Ryuk (malware)
Wizard Spider / UNC1878 (contexte acteur)
Ryuk Speed Run (un incident DFIR)
```

La présence d'un binaire Ryuk dans un autre incident ne suffit pas, à elle seule, pour attribuer cet incident à Wizard Spider.

---

## 2. Synthèse du renseignement

The DFIR Report a documenté une intrusion réelle passée de l'exécution de BazarLoader au déploiement de Ryuk en environ deux heures. Le chiffrement complet de l'environnement s'est terminé environ trois heures après l'exécution initiale de BazarLoader.

Le cas comprend phishing, BazarLoader, Cobalt Strike, reconnaissance Active Directory, Rubeus/Kerberoasting, exploitation de Zerologon (`CVE-2020-1472`), injection de processus, mouvement latéral RDP/SMB, exfiltration FTP et déploiement de Ryuk.

Cette fiche sépare les **preuves de l'incident** du contexte plus large lié à Wizard Spider et Ryuk.

---

## 3. Chronologie DFIR

| Temps approx. | Activité | Preuve | Portée | Confiance | Provenance |
|---|---|---|---|---|---|
| T+00 | Lien de phishing, téléchargement puis exécution de BazarLoader | Observé | Incident | Élevée | The DFIR Report |
| < T+05 | `net view`, `nltest` et découverte du domaine | Observé | Incident | Élevée | The DFIR Report |
| ~ T+07 | AdFind utilisé pour la reconnaissance Active Directory | Observé | Incident | Élevée | The DFIR Report |
| < T+10 | Déploiement de beacons Cobalt Strike | Observé | Incident | Élevée | The DFIR Report |
| Début | Tâches planifiées et clé Registry Run | Observé | Incident | Élevée | The DFIR Report |
| Début | Zerologon exploité pour obtenir Domain Admin | Observé | Incident | Élevée | The DFIR Report |
| Début | Rubeus utilisé pour le Kerberoasting | Observé | Incident | Élevée | The DFIR Report |
| Début | Injection dans `svchost.exe` | Observé | Incident | Élevée | The DFIR Report |
| ~ T+60 | Mouvement RDP et SMB/ADMIN$ vers les contrôleurs de domaine | Observé | Incident | Élevée | The DFIR Report |
| Avant impact | Sorties AdFind/Rubeus exfiltrées par FTP vers `5.2.70.149:21` | Observé | Incident | Élevée | The DFIR Report |
| ~ T+120 | Début du déploiement Ryuk via RDP | Observé | Incident | Élevée | The DFIR Report |
| ~ T+180 | Chiffrement de l'environnement terminé | Observé | Incident | Élevée | The DFIR Report |

La formule **"2 Hours to Ransom"** correspond au début du déploiement Ryuk, pas à la fin de toute l'attaque.

---

## 4. Mapping MITRE ATT&CK du cas

| Tactique | Technique | ATT&CK | Comportement | Preuve | Provenance |
|---|---|---|---|---|---|
| Accès initial | Spearphishing Link | T1566.002 | Lien menant à BazarLoader | Observé | The DFIR Report |
| Exécution | User Execution | T1204 | L'utilisateur exécute BazarLoader | Observé | The DFIR Report |
| Defense Evasion | Process Injection | T1055 | Injection dans `svchost.exe` | Observé | The DFIR Report |
| Defense Evasion | Code Signing | T1553.002 | BazarLoader et des binaires liés à Cobalt Strike utilisent des certificats de signature | Observé | The DFIR Report |
| Persistance | Scheduled Task | T1053.005 | Tâches planifiées sur l'hôte initial | Observé | The DFIR Report |
| Persistance | Registry Run Keys / Startup Folder | T1547.001 | Persistance via clé Run | Observé | The DFIR Report |
| Élévation de privilèges | Exploitation for Privilege Escalation | T1068 | Zerologon (`CVE-2020-1472`) | Observé | The DFIR Report |
| Credential Access | Kerberoasting | T1558.003 | Rubeus utilisé pour le Kerberoasting | Observé | The DFIR Report |
| Discovery | Domain Trust Discovery | T1482 | `nltest` / AdFind | Observé | The DFIR Report |
| Discovery | Permission Groups Discovery: Domain Groups | T1069.002 | Énumération groupes de domaine | Observé | The DFIR Report |
| Discovery | Account Discovery: Domain Account | T1087.002 | Énumération des comptes de domaine | Observé | The DFIR Report |
| Discovery | Remote System Discovery | T1018 | Découverte des systèmes | Observé | The DFIR Report |
| Mouvement latéral | Remote Desktop Protocol | T1021.001 | RDP vers DC et serveurs | Observé | The DFIR Report |
| Mouvement latéral | SMB/Windows Admin Shares | T1021.002 | Payloads copiés via `ADMIN$` | Observé | The DFIR Report |
| Exécution | Service Execution | T1569.002 | Exécutables distants lancés comme services | Observé | The DFIR Report |
| Exfiltration | Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol | T1048.003 | Données de découverte envoyées par FTP | Observé | The DFIR Report |
| Impact | Service Stop | T1489 | Services/processus Veeam et SQL arrêtés avant chiffrement | Observé | The DFIR Report + mapping AFRINTEL |
| Impact | Data Encrypted for Impact | T1486 | Chiffrement Ryuk | Observé | The DFIR Report |

---

## 5. Outils et malwares

| Outil / Malware | Rôle | Preuve | Portée |
|---|---|---|---|
| BazarLoader | Malware initial / backdoor | Observé | Incident |
| Cobalt Strike | Post-exploitation / C2 | Observé | Incident |
| AdFind | Reconnaissance Active Directory | Observé | Incident |
| Rubeus | Kerberoasting | Observé | Incident |
| Exploit Zerologon | Élévation de privilèges | Observé | Incident |
| Module AD PowerShell | Reconnaissance des contrôleurs de domaine | Observé | Incident |
| RDP | Mouvement latéral / déploiement Ryuk | Observé | Incident |
| SMB / ADMIN$ | Transfert de payloads | Observé | Incident |
| Ryuk | Impact ransomware | Observé | Incident |

---

## 6. Infrastructure réseau et IoC historiques

| Indicateur | Contexte |
|---|---|
| `dghns.xyz` | C2 BazarLoader |
| `34.222.33.48:443` | C2 BazarLoader |
| `checktodrivers.com` | Cobalt Strike suspecté |
| `45.153.240.240:443` | Cobalt Strike suspecté |
| `topservicebooster.com` | Cobalt Strike suspecté |
| `108.62.12.121:443` | Cobalt Strike suspecté |
| `chaseltd.top` | C2 / gate |
| `161.117.191.245:80` | C2 |
| `5.2.70.149:21` | Destination d'exfiltration FTP |

### Empreintes TLS du cas

```text
BazarLoader
JA3:  9e10692f1b7f78228b2d4e424db3a98c
JA3s: 2b33c1374db4ddf06942f92373c0b54b

checktodrivers.com
JA3:  37f463bf4616ecd445d4a1937da06e19
JA3s: ae4edc6faf64d08308082ad26be60767

topservicebooster.com
JA3:  2c14bfb3f8a2067fbc88d8345e9f97f3
JA3s: 649d6810e8392f63dc311eecb6b7098b
```

Ce sont des IoC historiques du cas 2020 et non une infrastructure actuelle par défaut.

---

## 7. IoC fichiers de l'incident

| Fichier | SHA-256 |
|---|---|
| `Report-Review20-10.exe.exe` | `0d468fc1b02bbc7c3050c67e0a80b580c69abd8eea5f8dad06c7d7ff396f7789` |
| `Firefox.exe` | `3fc65b7e7967353f340ead51617558a23f14447ab91d974268f53ab0c17052e0` |
| `pagefilerpqy.exe` | `a4468c28e4830acf526209c0da25536ff0f682a0239ced1983a08d1ddd476963` |
| `pagefileU6Gl.sys` | `13671077b66a29874a2578b5240319092ef2a1043228e433e9b006b5e53e7513` |
| `pagefilerpqy.sys` | `8241649609f88ccd2a0a5b233a07a538ec313ff6adf695aa44a969dbca39f67d` |
| `AdFind.exe` | `68d0f5659cf3cc1cf53519e1be482ca9a63f2deebdcd2cb7ee12515adc6db0a7` |
| `PL64.exe` | `a7514209db9d9c7c51927308d4f0b491464e11391af3c6ae31cb87d91fac995d` |
| `fx2-12_multi_for_crypt_x86.exe` | `34007d53a8e64bf1dbbeace9e4878fb209878e6a6843251895d4dc9c2699056e` |

---

## 8. Pistes de détection et Threat Hunting

Signaux utiles :

- téléchargement de phishing suivi de l'exécution de BazarLoader ;
- reconnaissance domaine quelques minutes après la première exécution ;
- AdFind et Rubeus très tôt dans la chronologie ;
- Cobalt Strike rapidement après l'accès initial ;
- exploitation Zerologon suivie d'activité Domain Admin ;
- RDP depuis le beachhead vers les contrôleurs de domaine ;
- exécutables copiés dans `ADMIN$` puis exécutés comme services ;
- FTP vers un serveur externe inhabituel après génération des sorties de discovery ;
- arrêt massif de services Veeam/SQL juste avant le chiffrement ;
- déploiement Ryuk depuis les contrôleurs de domaine via RDP.

---

## 9. Évaluation d'attribution

Le rapport DFIR fait référence au suivi FireEye de UNC1878 et note un alignement avec le tradecraft Ryuk. MITRE ATT&CK liste actuellement UNC1878 parmi les noms de groupes associés à Wizard Spider.

AFRINTEL enregistre donc cette relation comme un **contexte d'attribution**, pas comme une règle universelle :

```text
Incident DFIR
  +-- uses --> BazarLoader
  +-- uses --> Cobalt Strike
  +-- uses --> AdFind / Rubeus
  +-- exploits --> CVE-2020-1472
  +-- deploys --> Ryuk (S0446)
  +-- attribution context --> UNC1878 / Wizard Spider (G0102)
```

### Lacunes de renseignement

Le cas public ne permet pas d'établir :

- l'identité des opérateurs individuels ;
- que toutes les intrusions Ryuk utilisent la même équipe ;
- que l'infrastructure est restée active après 2020 ;
- que toute infection Ryuk doit être attribuée à Wizard Spider ;
- une motivation étatique ou géopolitique pour cet incident.

---

## 10. Sources

- The DFIR Report - **Ryuk Speed Run, 2 Hours to Ransom**, 5 novembre 2020
- MITRE ATT&CK - **Ryuk S0446**
- MITRE ATT&CK - **Wizard Spider G0102**

---

**AFRINTEL - African Cyber Threat Intelligence**
