# Qilin / Agenda - Profil acteur & ransomware

👉🏾 [**English version available here**](./profile.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Groupe :** Qilin (anciennement Agenda)
- **Type de menace :** Ransomware / Double extorsion
- **Modèle opératoire :** Ransomware-as-a-Service (RaaS)
- **Motivation principale :** Financière
- **Plateformes connues :** Windows, Linux, VMware ESXi et environnements virtualisés
- **Activité :** Active depuis 2022
- **Statut :** Surveillance active
- **Dernière mise à jour :** 27 août 2026

---

## 1. Synthèse

Qilin est une opération RaaS mature active depuis 2022. Le groupe combine vol de données, extorsion et chiffrement, avec une part importante des intrusions réalisée par des affiliés.

L'activité de Qilin a fortement augmenté en 2025 et 2026. Le rapport ransomware 2026 de Black Kite recense **1 358 publications de victimes** attribuées à Qilin sur sa période d'observation, contre 250 sur la période précédente. Ce chiffre correspond à des publications ou revendications observées et ne doit pas être présenté comme 1 358 compromissions indépendamment confirmées.

Cisco Talos a documenté plusieurs incidents Qilin en 2025 et montre que les affiliés ne suivent pas tous exactement la même chaîne d'attaque.

> **Règle AFRINTEL :** les TTP connues au niveau de Qilin ne sont pas automatiquement appliquées à chaque victime revendiquée. Il faut des éléments techniques propres à la victime pour parler de TTP spécifiques à l'incident.

---

## 2. Observation AFRINTEL en Afrique

### 8 mai 2026 - Égypte - Imex International

AFRINTEL a enregistré une revendication ransomware Qilin visant **Imex International**, une société égyptienne spécialisée dans la logistique et le transport de fret.

- **Pays :** Égypte
- **Secteur :** Logistique & Transport
- **Site :** imex-logistics.com
- **Statut :** Ransomware revendiqué
- **Portée de la preuve :** Association victime / revendication

AFRINTEL ne dispose pas actuellement de télémétrie propre à cette victime permettant d'affirmer que les TTP générales décrites dans cette fiche ont été utilisées contre Imex International.

**Preuve :** Revendication observée  
**Portée :** Association au niveau victime  
**Confiance :** Élevée pour la revendication ; insuffisante pour attribuer des TTP à la victime  
**Provenance :** AFRINTEL

---

## 3. Accès initial

### Comptes valides et services d'accès distant

Cisco Talos indique que, dans certains incidents 2025, les attaquants ont probablement utilisé des identifiants administrateur auparavant exposés sur le dark web pour accéder à des VPN.

Talos évalue ce lien avec une **confiance moyenne** et précise qu'il existe une corrélation temporelle entre l'exposition des identifiants et l'intrusion, sans preuve définitive que l'un a directement causé l'autre.

Techniques ATT&CK :

- **T1078 - Valid Accounts**
- **T1133 - External Remote Services**
- **T1110 / T1110.003 - Brute Force / Password Spraying**

Dans le cas documenté, l'absence de MFA sur le VPN a fortement facilité l'accès.

### CVE-2026-50751 - Check Point VPN

Check Point a documenté l'exploitation active de **CVE-2026-50751**, une vulnérabilité de contournement d'authentification affectant certaines configurations Remote Access VPN et Mobile Access utilisant l'ancien protocole IKEv1.

Check Point évalue avec une **confiance moyenne** que l'acteur observé est financièrement motivé et utilise le ransomware Qilin. Au moins un cas post-compromission a été associé à un affilié Qilin.

- **ATT&CK :** T1190 - Exploit Public-Facing Application
- **Preuve :** Rapporté
- **Portée :** Niveau campagne
- **Confiance :** Moyenne
- **Provenance :** Check Point Research

### CVE-2026-0257 - Palo Alto Networks GlobalProtect

Arctic Wolf a investigué plusieurs intrusions en juin 2026 ayant commencé par l'exploitation de **CVE-2026-0257** sur des équipements Palo Alto Networks et ayant abouti au déploiement de Qilin.

- **ATT&CK :** T1190
- **Preuve :** Observé / Rapporté
- **Portée :** Niveau incident / campagne
- **Confiance :** Élevée
- **Provenance :** Arctic Wolf Labs

### Exclusion importante

**CVE-2025-61882 sur Oracle E-Business Suite n'est pas intégrée comme TTP Qilin.**

Les rapports techniques publics relient cette campagne Oracle EBS à **CL0P**, dans un contexte de vol de données et d'extorsion. AFRINTEL ne l'utilise donc pas comme vecteur d'accès Qilin.

---

## 4. Discovery

Talos a observé l'utilisation de commandes Windows classiques et d'outils Active Directory.

```text
nltest /dclist:<Domain>
net user <Username> /domain
whoami.exe /priv
tasklist /FI "IMAGENAME eq explorer.exe" /FO CSV /NH
```

PowerShell est également utilisé pour l'énumération AD :

```powershell
Import-Module ActiveDirectory
Get-ADComputer -Filter * | Select-Object -ExpandProperty DNSHostName
```

Techniques associées :

- **T1482 - Domain Trust Discovery**
- **T1018 - Remote System Discovery**
- **T1087.002 - Domain Account Discovery**
- **T1033 - System Owner/User Discovery**
- **T1057 - Process Discovery**
- **T1046 - Network Service Discovery**
- **T1082 - System Information Discovery**
- **T1059.001 - PowerShell**

**Preuve :** Observé  
**Portée :** Niveau incident / tradecraft acteur  
**Confiance :** Élevée  
**Provenance :** Cisco Talos

---

## 5. Credential Access

Talos a identifié un dossier protégé par mot de passe contenant plusieurs outils liés au vol d'identifiants, notamment Mimikatz, des outils NirSoft, SharpDecryptPwd et des scripts personnalisés.

Un script batch modifie WDigest :

```text
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /f /d 1
```

SharpDecryptPwd est utilisé pour récupérer des identifiants enregistrés dans différents logiciels, notamment WinSCP, Navicat, TeamViewer, FileZilla, Chrome et RDCMan.

Techniques associées :

- **T1003 - OS Credential Dumping**
- **T1555 - Credentials from Password Stores**

**Preuve :** Observé  
**Portée :** Niveau incident  
**Confiance :** Élevée  
**Provenance :** Cisco Talos

> AFRINTEL ne présente pas RedLine ou Lumma comme une source systématique d'identifiants pour Qilin. Les sources retenues confirment l'usage d'identifiants exposés sur le dark web, mais pas ces deux familles de stealers comme méthode générale de Qilin.

---

## 6. Mouvement latéral et accès distant

Les comportements observés incluent RDP, PsExec, SMB / partages administratifs Windows, modification des paramètres RDP et utilisation d'outils RMM.

Exemple d'activation RDP :

```text
reg add HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

Talos a également observé des outils d'accès distant comme AnyDesk, Chrome Remote Desktop, Distant Desktop, GoToDesk, QuickAssist et ScreenConnect.

Un encrypteur Qilin a aussi été distribué via PsExec :

```text
cmd /C [PsExec] -accepteula \\IP -c -f -h -d -i <encryptor>.exe --password [PASSWORD] --spread --spread-process
```

Techniques :

- **T1021.001 - Remote Desktop Protocol**
- **T1021.002 - SMB/Windows Admin Shares**
- **T1219 - Remote Access Software**
- **T1569.002 - Service Execution**

---

## 7. Defense Evasion

Talos a documenté du PowerShell obfusqué et plusieurs tentatives visant à réduire la visibilité EDR.

Comportements observés :

- désactivation d'AMSI ;
- désactivation de la validation TLS ;
- modification de Restricted Admin ;
- arrêt ou désinstallation de composants EDR ;
- utilisation de `dark-kill` et HRSword ;
- effacement des journaux Windows.

Exemple :

```text
sc create dark type= kernel binPath=dark.sys
sc start dark
sc delete dark
```

Techniques :

- **T1562.001 - Impair Defenses**
- **T1070.001 - Clear Windows Event Logs**
- **T1112 - Modify Registry**
- **T1059.001 - PowerShell**

---

## 8. Collection et exfiltration

Un script VBS a été observé consolidant des identifiants dans `result.txt`, puis les envoyant vers un serveur SMTP contrôlé par l'attaquant.

WinRAR a aussi été utilisé pour préparer des données. Talos documente également **Cyberduck** avec **Backblaze** comme destination cloud dans certains incidents Qilin.

Techniques :

- **T1560.001 - Archive via Utility**
- **T1048 - Exfiltration Over Alternative Protocol**
- **T1537 - Transfer Data to Cloud Account**

> **Cloudflare Tunnel n'est pas présenté ici comme canal d'exfiltration Qilin par défaut.** Les sources retenues documentent plutôt Cyberduck/Backblaze, SMTP et d'autres mécanismes.

---

## 9. Ciblage VMware / ESXi

Talos a observé des scripts PowerShell capables de se connecter à vCenter, énumérer datacenters et clusters, désactiver HA et DRS, énumérer les hôtes ESXi, modifier des mots de passe root, activer SSH, envoyer un payload dans `/tmp` et l'exécuter sur plusieurs hôtes.

**Preuve :** Observé  
**Portée :** Niveau incident / tradecraft acteur  
**Confiance :** Élevée  
**Provenance :** Cisco Talos

---

## 10. Impact et inhibition de la restauration

Talos a observé la modification du service VSS et la suppression des Shadow Copies.

```text
cmd /C net start vss
cmd /C wmic service where name='vss' call ChangeStartMode Manual
cmd /C vssadmin.exe Delete Shadows /all /quiet
cmd /C net stop vss
cmd /C wmic service where name='vss' call ChangeStartMode Disabled
```

Techniques :

- **T1490 - Inhibit System Recovery**
- **T1489 - Service Stop**
- **T1486 - Data Encrypted for Impact**

La configuration Qilin contient aussi des listes de processus et services à arrêter, notamment des composants de sauvegarde, bases de données et sécurité.

> AFRINTEL n'utilise pas `net stop "VeeamEndpointBackupSvc"` comme commande Qilin documentée tant qu'une source d'incident ne montre pas précisément cette ligne de commande.

---

## 11. Pistes de détection et Threat Hunting

| Signal | Intérêt |
|---|---|
| Connexion VPN depuis une infrastructure inhabituelle | Accès initial potentiel |
| VPN réussi après de nombreuses tentatives NTLM | Compromission par identifiants |
| `UseLogonCredential=1` | Affaiblissement WDigest |
| Activation RDP par registre | Préparation d'accès distant |
| PsExec distribuant un binaire protégé par mot de passe | Déploiement ransomware |
| `dark.sys`, HRSword ou tentative de désinstallation EDR | Defense Evasion |
| Effacement massif des journaux | Anti-forensic |
| Suppression VSS | Inhibition de restauration |
| PowerShell ciblant vCenter / ESXi | Ciblage virtualisation |
| Historique Cyberduck vers un cloud inhabituel | Exfiltration possible |

Ces signaux servent à la détection. Pris isolément, ils ne constituent pas une preuve d'attribution à Qilin.

---

## 12. Évaluation AFRINTEL

Qilin est un RaaS à très forte activité avec de nombreux affiliés. Les investigations disponibles montrent des variations importantes d'un incident à l'autre.

AFRINTEL sépare donc :

- le renseignement **niveau acteur** ;
- les campagnes d'exploitation de vulnérabilités ;
- les TTP observées dans des incidents documentés ;
- les preuves propres aux victimes AFRINTEL.

Une revendication Qilin sur un leak site ne suffit pas à déterminer le CVE utilisé, la source des identifiants, l'outil d'exfiltration ou le mode de déploiement de l'encrypteur.

---

## 13. Sources

- Cisco Talos - *Uncovering Qilin attack methods exposed through multiple cases*  
  https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/
- Check Point Research - *Active Exploitation of CVE-2026-50751*  
  https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/
- Arctic Wolf Labs - *Exploitation of CVE-2026-0257 Leads to Qilin Ransomware*  
  https://arcticwolf.com/resources/blog/exploitation-of-cve-2026-0257-leads-to-qilin-ransomware/
- Black Kite - *2026 Ransomware Report*  
  https://blackkite.com/reports/2026-ransomware-report
- AFRINTEL - Victimes ransomware africaines, mai 2026

---

**AFRINTEL - African Cyber Threat Intelligence**
