# Akira - Profil de l’acteur de menace

👉🏾 [**English version available here**](./akira_profile.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Groupe :** Akira
- **Type de menace :** Ransomware / Extorsion
- **Modèle opératoire :** Ransomware-as-a-Service (RaaS)
- **Motivation principale :** Financière
- **Période couverte :** 2024-2026
- **Environnements ciblés :** Windows, VMware ESXi, Hyper-V, Nutanix AHV
- **Statut de l’évaluation :** Surveillance active
- **Dernière mise à jour :** 25 août 2026

---

## 1. Synthèse du renseignement

Akira est une opération ransomware active depuis 2023, associée à des attaques contre des environnements Windows et des infrastructures de virtualisation.

Les versions historiques du ransomware ont été principalement développées en C++, tandis que des variantes plus récentes, notamment **Megazord** et **Akira_v2**, utilisent Rust.

Les campagnes attribuées à Akira reposent généralement sur une combinaison d’accès initial via services exposés, comptes VPN compromis ou vulnérabilités, reconnaissance interne, vol d’identifiants, exfiltration de données et chiffrement.

> **Qualification AFRINTEL :**  
> Les TTP ci-dessous correspondent à des comportements documentés au niveau de l’écosystème Akira par le FBI, la CISA et leurs partenaires. Elles ne doivent pas être automatiquement attribuées à chaque victime Akira suivie par AFRINTEL sans preuve technique spécifique à l’incident.

---

## 2. TTPs clés documentés

### 2.1 Accès initial

- **T1190 - Exploit Public-Facing Application**
  - Exploitation de vulnérabilités affectant des systèmes exposés à Internet.
  - Exploitation documentée de **CVE-2023-20269** sur Cisco ASA / FTD.
  - Exploitation documentée de **CVE-2024-40766** sur SonicWall.

- **T1078 - Valid Accounts**
  - Utilisation de comptes VPN compromis.

- **T1110 / T1110.003 - Brute Force / Password Spraying**
  - Tentatives de brute force et de password spraying contre des comptes VPN.

- **T1566.001 / T1566.002 - Spearphishing**
  - Utilisation de pièces jointes ou de liens malveillants.

- **T1068 - Exploitation for Privilege Escalation**
  - Exploitation de serveurs Veeam vulnérables, notamment via **CVE-2023-27532** et **CVE-2024-40711**.

**Type de preuve :** Rapporté / Observé par les autorités partenaires  
**Confiance :** Élevée

---

### 2.2 Reconnaissance et découverte interne

- **T1046 - Network Service Discovery**
  - Utilisation de **Advanced IP Scanner**, **NetScan** et **SoftPerfect Network Scanner** pour identifier les hôtes, ports, équipements réseau et partages accessibles.

- **T1018 - Remote System Discovery**
  - Utilisation de commandes Windows et de `nltest` pour identifier les systèmes et contrôleurs de domaine.

- **T1482 - Domain Trust Discovery**
  - Reconnaissance des relations de confiance Active Directory.

- **T1069.001 / T1069.002 - Permission Groups Discovery**
  - Utilisation de commandes `net` pour identifier les groupes administrateurs locaux et Domain Admins.

**Outils observés :**
- Advanced IP Scanner
- NetScan
- SoftPerfect Network Scanner
- `net.exe`
- `nltest`

**Confiance :** Élevée

---

### 2.3 Accès aux identifiants

- **T1003 - OS Credential Dumping**
  - Utilisation de **Mimikatz** et **LaZagne** pour extraire des informations d’authentification.

- **T1003.001 - LSASS Memory**
  - Tentatives de récupération des secrets contenus dans la mémoire du processus LSASS.
  - Utilisation documentée de `rundll32.exe` avec `comsvcs.dll` afin de générer un dump mémoire de LSASS.

- **T1555.003 / T1555.004**
  - Extraction de credentials depuis les navigateurs et le Windows Credential Manager via des outils tels que NetExec ou Mimikatz.

**Type de preuve :** Observé / Rapporté  
**Confiance :** Élevée

---

### 2.4 Collection et exfiltration

- **T1560.001 - Archive via Utility**
  - Utilisation de **WinRAR** pour compresser les données avant exfiltration.

- **T1567.002 - Exfiltration to Cloud Storage**
  - Utilisation de **RClone** pour synchroniser et exfiltrer des données vers des services de stockage cloud tels que **MEGA**.

- **T1048 - Exfiltration Over Alternative Protocol**
  - Utilisation de **WinSCP** et **FileZilla** pour transférer des données.

- **T1537 - Transfer Data to Cloud Account**
  - Utilisation de services ou comptes cloud pour transférer des données compromises.

**Outils observés :**
- RClone
- WinSCP
- FileZilla
- WinRAR
- MEGA

**Confiance :** Élevée

---

### 2.5 Command & Control et accès distant

Akira utilise également plusieurs outils légitimes de prise en main à distance ou de tunneling pouvant être détournés pour maintenir un accès ou établir des canaux de communication :

- AnyDesk
- RustDesk
- MobaXterm
- Cloudflare Tunnel
- Ngrok
- LogMeIn

Ces outils ne sont pas malveillants en eux-mêmes. Leur attribution à une activité Akira nécessite un contexte technique complémentaire.

---

### 2.6 Impact et inhibition de la restauration

- **T1486 - Data Encrypted for Impact**
  - Chiffrement des environnements Windows et des infrastructures de virtualisation.

- **T1490 - Inhibit System Recovery**
  - Suppression des Volume Shadow Copies afin de limiter les possibilités de restauration.

Des versions récentes du ransomware peuvent cibler :

- Windows ;
- VMware ESXi ;
- Hyper-V ;
- Nutanix AHV.

Les variantes documentées incluent notamment :

- **Akira**
- **Akira_v2**
- **Megazord**

Les variantes historiques Akira utilisent principalement C++, tandis que Megazord et Akira_v2 introduisent des composants écrits en Rust.

**Confiance :** Élevée

---

## 3. Artefacts techniques documentés

| Artefact | Type | Usage | ATT&CK |
|---|---|---|---|
| `Advanced IP Scanner` | Outil | Reconnaissance réseau | T1046 |
| `NetScan` | Outil | Scan réseau / ports | T1046 |
| `Mimikatz` | Outil | Credential dumping | T1003 |
| `rundll32.exe` + `comsvcs.dll` | LOLBin | Dump LSASS | T1003.001 |
| `RClone` | Outil | Exfiltration cloud | T1567.002 |
| `WinSCP` | Outil | Transfert de données | T1048 |
| `WinRAR` | Outil | Archivage avant exfiltration | T1560.001 |
| `vssadmin.exe` | LOLBin | Suppression des copies VSS | T1490 |
| `Akira_v2` | Ransomware | Chiffrement | T1486 |
| `Megazord` | Ransomware | Chiffrement | T1486 |

---

## 4. Exemples de lignes de commande / comportements

Les commandes ou comportements suivants sont pertinents pour la détection lorsqu’ils apparaissent dans un contexte compatible avec une intrusion ransomware :

```text
vssadmin.exe delete shadows /all /quiet
rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump <PID> <output.dmp> full
rclone.exe copy ...
```

> Ces artefacts doivent être corrélés avec le contexte d’exécution, le parent process, l’utilisateur, l’hôte, les connexions réseau et la chronologie de l’incident afin de limiter les faux positifs.

---

## 5. Vulnérabilités associées à des opérations Akira

| CVE | Produit | Usage documenté |
|---|---|---|
| CVE-2023-20269 | Cisco ASA / FTD | Accès initial |
| CVE-2024-40766 | SonicWall | Accès initial |
| CVE-2023-27532 | Veeam Backup & Replication | Exploitation de serveur vulnérable |
| CVE-2024-40711 | Veeam Backup & Replication | Exploitation de serveur vulnérable |

---

## 6. Évaluation AFRINTEL

Les TTP présentés dans cette fiche correspondent à des comportements documentés au niveau de l’écosystème Akira.

AFRINTEL distingue systématiquement :

- les **TTP connues de l’acteur** ;
- les **TTP observées lors d’une investigation indépendante** ;
- les **TTP confirmées pour une victime AFRINTEL** ;
- les **TTP évaluées ou inférées**.

Une revendication Akira contre une organisation africaine ne suffit donc pas à conclure que l’ensemble de cette chaîne d’attaque a été utilisée contre cette victime.

### Niveaux de preuve

- **Observé :** élément directement vu dans de la télémétrie, une analyse malware, une réponse à incident ou une source primaire.
- **Rapporté :** élément publié par une source technique ou institutionnelle fiable.
- **Évalué :** conclusion analytique fondée sur plusieurs éléments disponibles.
- **Inféré :** relation plausible mais insuffisamment étayée techniquement.

---

## 7. Lacunes de renseignement à traiter au niveau incident

Pour chaque victime Akira suivie par AFRINTEL, les éléments suivants doivent être recherchés avant d’attribuer des TTP au niveau de la victime :

- vecteur d’accès initial ;
- compte ou identité compromis ;
- CVE réellement exploitée ;
- infrastructure de commande et contrôle ;
- hash du ransomware ou des outils ;
- commandes observées ;
- mécanisme de déplacement latéral ;
- canal d’exfiltration ;
- méthode de suppression des sauvegardes ;
- méthode de déploiement du ransomware.

---

## 8. Sources

- FBI / CISA / DC3 / HHS et partenaires internationaux - **#StopRansomware: Akira Ransomware (AA24-109A)**
- MITRE ATT&CK
- Sources techniques complémentaires AFRINTEL selon les incidents étudiés

---

**AFRINTEL - African Cyber Threat Intelligence**
