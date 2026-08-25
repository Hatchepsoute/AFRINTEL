# Ryuk / Wizard Spider - Profil Acteur & Ransomware

👉🏾 [**English version available here**](./ryuk_profile.md)

**AFRINTEL Threat Actor Intelligence**

- **Ransomware / Malware :** Ryuk
- **Logiciel MITRE ATT&CK :** S0446
- **Groupe malveillant associé :** Wizard Spider
- **Groupe MITRE ATT&CK :** G0102
- **Alias historique/actuel ATT&CK :** UNC1878 (parmi les alias de Wizard Spider)
- **Type de menace :** Ransomware / Big-game hunting
- **Motivation :** Financière
- **Cas DFIR de référence :** Ryuk Speed Run - 2 Hours to Ransom
- **Date du cas :** 2020
- **Géographie :** Cas DFIR externe de référence ; pas une victime africaine AFRINTEL
- **Statut :** Référence historique / étude de tradecraft
- **Dernière mise à jour :** 25 août 2026

---

## 1. Note de modélisation

Ryuk est **un malware/ransomware**, pas un acteur malveillant à lui seul.

MITRE ATT&CK référence Ryuk comme logiciel **S0446** et liste **Wizard Spider (G0102)** ainsi que **FIN6 (G0037)** parmi les groupes ayant utilisé Ryuk. MITRE inclut actuellement **UNC1878** parmi les alias de Wizard Spider.

AFRINTEL distingue donc :

- **Ryuk** - ransomware / malware ;
- **Wizard Spider / UNC1878** - acteur / cluster d'intrusion ;
- **ce cas DFIR** - comportements observés dans un incident précis ;
- **les TTP génériques Ryuk** - renseignement acteur/malware qui ne doit pas être appliqué automatiquement à chaque incident Ryuk.

---

## 2. Synthèse de renseignement

The DFIR Report a documenté une intrusion réelle au cours de laquelle les opérateurs sont passés de **l'exécution de BazarLoader au déploiement de Ryuk en environ deux heures**, puis au chiffrement complet de l'environnement environ trois heures après l'exécution initiale.

Le cas fournit une chaîne de preuves comprenant phishing, BazarLoader, Cobalt Strike, reconnaissance Active Directory, Rubeus/Kerberoasting, Zerologon, mouvement latéral RDP/SMB, exfiltration FTP, déploiement de Ryuk, hashes, infrastructure réseau et mappings ATT&CK.

AFRINTEL utilise ce cas comme **référence DFIR** et ne suppose pas que cette chaîne ait été utilisée dans toutes les intrusions Ryuk.

---

## 3. Cas DFIR de référence - Ryuk Speed Run

**Source principale :** The DFIR Report  
**Publication :** 5 novembre 2020  
**Type de preuve :** Investigation DFIR / réponse à incident

| Temps approx. | Phase | Activité | Preuve |
|---|---|---|---|
| T+00 | Accès initial | L'utilisateur suit un lien de phishing et télécharge BazarLoader | DFIR_OBSERVED |
| T+00 | Exécution | L'utilisateur exécute BazarLoader | DFIR_OBSERVED |
| < T+05 | Discovery | `net view`, `nltest`, découverte domaines/groupes | DFIR_OBSERVED |
| ~ T+07 | Discovery | AdFind utilisé pour la reconnaissance AD | DFIR_OBSERVED |
| < T+10 | C2 | Déploiement de beacons Cobalt Strike | DFIR_OBSERVED |
| Début intrusion | Persistance | Tâches planifiées et clé Registry Run | DFIR_OBSERVED |
| Début intrusion | Élévation de privilèges | Exploitation Zerologon (`CVE-2020-1472`) pour obtenir Domain Admin | DFIR_OBSERVED |
| Début intrusion | Credential Access | Rubeus utilisé pour le Kerberoasting | DFIR_OBSERVED |
| Début intrusion | Defense Evasion | Injection dans `svchost.exe` | DFIR_OBSERVED |
| ~ T+60 | Mouvement latéral | RDP + SMB/ADMIN$ vers les contrôleurs de domaine | DFIR_OBSERVED |
| Avant impact | Exfiltration | Sorties AdFind/Rubeus envoyées par FTP vers `5.2.70.149:21` | DFIR_OBSERVED |
| ~ T+120 | Impact | Début du déploiement Ryuk via RDP | DFIR_OBSERVED |
| ~ T+180 | Impact | Chiffrement de l'environnement terminé | DFIR_OBSERVED |

**Note analytique :** les deux heures correspondent au début du déploiement Ryuk, pas à la fin de toute l'intrusion.

---

## 4. Mapping MITRE ATT&CK

| Tactique | Technique | ID | Comportement observé | Preuve |
|---|---|---|---|---|
| Initial Access | Spearphishing Link | T1566.002 | Lien de phishing menant à BazarLoader | DFIR_OBSERVED |
| Execution | User Execution | T1204 | Exécution de BazarLoader par l'utilisateur | DFIR_OBSERVED |
| Defense Evasion | Process Injection | T1055 | Injection dans `svchost.exe` | DFIR_OBSERVED |
| Persistence | Scheduled Task | T1053.005 | Tâches planifiées sur le beachhead | DFIR_OBSERVED |
| Persistence | Registry Run Keys / Startup Folder | T1547.001 | Persistance par clé Run | DFIR_OBSERVED |
| Privilege Escalation | Exploitation for Privilege Escalation | T1068 | Zerologon | DFIR_OBSERVED |
| Credential Access | Kerberoasting | T1558.003 | Rubeus | DFIR_OBSERVED |
| Discovery | Domain Trust Discovery | T1482 | `nltest` / AdFind | DFIR_OBSERVED |
| Discovery | Domain Groups | T1069.002 | Énumération des groupes de domaine | DFIR_OBSERVED |
| Discovery | Domain Account | T1087.002 | Énumération comptes/personnes | DFIR_OBSERVED |
| Discovery | Remote System Discovery | T1018 | Énumération des systèmes | DFIR_OBSERVED |
| Lateral Movement | Remote Desktop Protocol | T1021.001 | RDP vers DC et serveurs | DFIR_OBSERVED |
| Lateral Movement | SMB/Windows Admin Shares | T1021.002 | Payloads via `ADMIN$` | DFIR_OBSERVED |
| Execution | Service Execution | T1569.002 | Exécution distante en tant que service | DFIR_OBSERVED |
| Exfiltration | Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol | T1048.003 | Exfiltration FTP | DFIR_OBSERVED |
| Defense Evasion | Code Signing | T1553.002 | Binaires signés utilisés pendant l'intrusion | DFIR_OBSERVED |
| Impact | Data Encrypted for Impact | T1486 | Chiffrement Ryuk | DFIR_OBSERVED |

**Limite :** The DFIR Report fournit la preuve de l'incident ; MITRE ATT&CK fournit la taxonomie et le contexte acteur/logiciel.

---

## 5. Artefacts de reconnaissance

```text
net view /all
net view /all /domain
nltest /domain_trusts /all_trusts
net localgroup "administrator"
net group "domain admins" /dom
```

```text
AdFind.exe -f "(objectcategory=person)"
AdFind.exe -f "(objectcategory=computer)"
AdFind.exe -f "(objectcategory=organizationalUnit)"
AdFind.exe -sc trustdmp
AdFind.exe -subnets -f "(objectCategory=subnet)"
AdFind.exe -f "(objectcategory=group)"
AdFind.exe -gcb -sc trustdmp
```

---

## 6. Outils et malwares

| Outil / Malware | Rôle | Preuve |
|---|---|---|
| BazarLoader | Malware initial / backdoor | DFIR_OBSERVED |
| Cobalt Strike | C2 et post-exploitation | DFIR_OBSERVED |
| AdFind | Reconnaissance Active Directory | DFIR_OBSERVED |
| Rubeus | Kerberoasting | DFIR_OBSERVED |
| Exploit Zerologon | Élévation de privilèges | DFIR_OBSERVED |
| Module AD PowerShell | Discovery depuis le contrôleur de domaine | DFIR_OBSERVED |
| RDP | Mouvement latéral / déploiement Ryuk | DFIR_OBSERVED |
| SMB / ADMIN$ | Transfert de payloads | DFIR_OBSERVED |
| Ryuk | Impact ransomware | DFIR_OBSERVED |

---

## 7. C2 et infrastructure réseau

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

### Empreintes TLS

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

---

## 8. IOCs fichiers spécifiques à l'incident

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

Ce sont des **IOCs historiques spécifiques à l'incident de 2020**, pas de l'infrastructure Ryuk actuelle.

---

## 9. Évaluation d'attribution

Le rapport DFIR fait référence au suivi FireEye de **UNC1878** et indique une concordance avec les TTP Ryuk observées.

Contexte MITRE ATT&CK actuel :

- Ryuk = **S0446**
- Wizard Spider = **G0102**
- UNC1878 est actuellement un alias de Wizard Spider
- Ryuk est référencé parmi les logiciels utilisés par Wizard Spider
- FIN6 est également référencé comme groupe ayant utilisé Ryuk

AFRINTEL modélise donc :

```text
Incident
  +-- uses --> BazarLoader
  +-- uses --> Cobalt Strike
  +-- uses --> AdFind
  +-- uses --> Rubeus
  +-- exploits --> CVE-2020-1472
  +-- deploys --> Ryuk (S0446)
  +-- attribution context --> UNC1878 / Wizard Spider
```

AFRINTEL ne considère **pas** que la simple détection de Ryuk suffit à attribuer un incident indépendant à Wizard Spider.

---

## 10. Modèle de preuve

- **DFIR_OBSERVED** - directement documenté dans l'investigation.
- **EXTERNAL_REPORTED** - rapporté par une source CTI externe crédible.
- **ATTACK_CONTEXT** - taxonomie/relation MITRE ATT&CK actuelle.
- **ANALYST_MAPPED** - comportement normalisé par AFRINTEL vers ATT&CK.
- **INFERRED** - plausible mais non confirmé.

---

## 11. Artefact exclu

Le named pipe Cobalt Strike :

```text
\\.\pipe\msagent_xx
```

n'est **pas documenté dans le cas Ryuk Speed Run cité** et est donc exclu des IOCs spécifiques à cet incident.

---

## 12. Lacunes de renseignement

Le cas public ne permet pas d'établir :

- l'identité des opérateurs individuels ;
- que toutes les intrusions Ryuk utilisent la même équipe ;
- que l'infrastructure historique est restée active après l'incident ;
- que toute infection Ryuk doit être attribuée à Wizard Spider ;
- une motivation étatique ou géopolitique pour cet incident.

---

## 13. Sources

- The DFIR Report - Ryuk Speed Run, 2 Hours to Ransom  
  https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/

- MITRE ATT&CK - Ryuk S0446  
  https://attack.mitre.org/software/S0446/

- MITRE ATT&CK - Wizard Spider G0102  
  https://attack.mitre.org/groups/G0102/

---

**AFRINTEL - African Cyber Threat Intelligence**
