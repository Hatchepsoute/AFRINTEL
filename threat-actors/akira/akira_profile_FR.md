# Akira - Profil acteur / ransomware

👉🏾 [**English version**](./akira_profile.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Opération :** Akira
- **Type de menace :** Ransomware / Double extorsion
- **Modèle opératoire :** Ransomware-as-a-Service (RaaS)
- **Motivation :** Financière
- **Activité suivie :** 2023-2026
- **Périmètre des preuves techniques de cette fiche :** rapports publics jusqu'en novembre 2025
- **Environnements ciblés :** Windows, VMware ESXi, Hyper-V, Nutanix AHV
- **Statut :** Surveillance active
- **Dernière mise à jour :** 26 août 2026

---

## 1. Synthèse du renseignement

Akira est une opération ransomware financièrement motivée, active depuis 2023. Les rapports publics montrent un mélange de comptes compromis, services distants exposés, exploitation d'équipements en bordure de réseau et de systèmes non corrigés, reconnaissance interne rapide, vol d'identifiants, exfiltration puis chiffrement.

La mise à jour de novembre 2025 de l'avis FBI/CISA/DC3/HHS a élargi les TTP connues d'Akira. Elle documente notamment l'usage de comptes VPN compromis, le password spraying, SSH, l'exploitation de Veeam, la création de comptes de domaine, l'accès à LSASS/SAM/NTDS, la désactivation de protections, le tunneling, les outils de prise en main à distance et les capacités d'Akira_v2.

Les premières versions d'Akira étaient surtout développées en C++. Megazord et Akira_v2 ont introduit des encrypteurs en Rust. L'avis conjoint indique que Megazord n'est probablement plus utilisé depuis 2024, alors qu'Akira_v2 représente une évolution plus récente.

> **Limite AFRINTEL :** ces éléments sont des comportements au niveau acteur ou rapportés dans des incidents externes. Ils ne doivent pas être attribués à une victime AFRINTEL sans preuve propre à l'incident.

---

## 2. TTP principales

| Tactique | Technique | ATT&CK | Comportement | Preuve | Portée | Confiance | Provenance |
|---|---|---|---|---|---|---|---|
| Accès initial | Exploit Public-Facing Application | T1190 | Exploitation de produits VPN, edge et sauvegarde vulnérables | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Accès initial | Valid Accounts | T1078 | Utilisation de comptes VPN compromis | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Accès initial | External Remote Services | T1133 | Accès via services distants exposés, notamment RDP/VPN | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Credential Access | Brute Force | T1110 | Brute force contre VPN et SSH | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Credential Access | Password Spraying | T1110.003 | SharpDomainSpray utilisé pour le password spraying | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Exécution | Visual Basic | T1059.005 | Scripts VB utilisés pour exécuter des commandes malveillantes | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Persistance | Create Domain Account | T1136.002 | Création de comptes de domaine ; `itadm` observé dans certains cas | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Credential Access | LSASS Memory | T1003.001 | Accès à LSASS ; Mimikatz et LaZagne également documentés | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Credential Access | Security Account Manager | T1003.002 | Extraction de données SAM/SYSTEM dans des opérations documentées | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Credential Access | NTDS | T1003.003 | Extraction de `NTDS.dit` via un workflow impliquant la VM d'un contrôleur de domaine | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Discovery | Network Service Discovery | T1046 | Advanced IP Scanner, NetScan et outils similaires | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Discovery | Remote System Discovery | T1018 | `nltest` et commandes Windows pour identifier les systèmes/DC | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Discovery | Domain Trust Discovery | T1482 | Énumération des relations de confiance | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Defense Evasion | Disable or Modify Tools | T1562.001 | PowerTool/BYOVD et suppression d'EDR | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Defense Evasion | Disable or Modify System Firewall | T1562.004 | Modifications du pare-feu observées | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Mouvement latéral | Remote Desktop Protocol | T1021.001 | RDP utilisé dans le réseau compromis | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Mouvement latéral | SSH | T1021.004 | SSH utilisé pour l'accès et le déplacement latéral | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| C2 | Proxy | T1090 | Ngrok/SystemBC utilisés comme proxy ou pour masquer le trafic | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| C2 | Ingress Tool Transfer | T1105 | Téléchargement d'outils et de beacons Cobalt Strike ; STONESTOP utilisé comme loader | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| C2 | Remote Access Software | T1219 | Abus d'AnyDesk, LogMeIn et d'autres outils légitimes | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| C2 | Protocol Tunneling | T1572 | Ngrok utilisé pour encapsuler le trafic dans HTTPS | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Collection | Archive via Utility | T1560.001 | WinRAR utilisé pour préparer les données | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Exfiltration | Exfiltration Over Alternative Protocol | T1048 | WinSCP et outils similaires utilisés pour le transfert | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Exfiltration | Transfer Data to Cloud Account | T1537 | Stockage cloud utilisé comme destination d'exfiltration | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Exfiltration | Exfiltration to Cloud Storage | T1567.002 | RClone utilisé pour synchroniser des données vers le cloud | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Impact | Data Encrypted for Impact | T1486 | Chiffrement de systèmes Windows et d'infrastructures virtuelles | Rapporté | Acteur | Élevée | Avis FBI/CISA |
| Impact | Inhibit System Recovery | T1490 | Suppression des copies VSS sous Windows | Rapporté | Acteur | Élevée | Avis FBI/CISA |

---

## 3. Vulnérabilités documentées dans des opérations Akira

| CVE | Produit / contexte | Usage documenté | Confiance |
|---|---|---|---|
| CVE-2020-3259 | Cisco ASA / FTD | Accès initial / exposition d'identifiants | Élevée |
| CVE-2023-20269 | Cisco ASA / FTD | Accès initial | Élevée |
| CVE-2020-3580 | Cisco ASA / FTD | Ajoutée dans la mise à jour de novembre 2025 | Élevée |
| CVE-2023-28252 | Microsoft Windows CLFS | CVE associée à Akira dans l'avis 2025 ; vulnérabilité d'élévation de privilèges Windows | Élevée pour l'association ; contexte à vérifier par incident |
| CVE-2024-37085 | VMware ESXi | Contournement d'authentification ; CVE associée à Akira dans l'avis 2025 | Élevée |
| CVE-2023-27532 | Veeam Backup & Replication | Exploitation de serveurs Veeam non corrigés | Élevée |
| CVE-2024-40711 | Veeam Backup & Replication | Exploitation / élévation de privilèges selon le contexte | Élevée |
| CVE-2024-40766 | SonicWall SonicOS | Accès initial ; également liée à la chaîne de l'incident AHV de juin 2025 | Élevée |

AFRINTEL ne suppose pas qu'une de ces CVE a été utilisée contre une victime africaine Akira sans preuve propre à l'incident.

---

## 4. Outils et malwares

| Outil / Malware | Rôle | Preuve | Portée |
|---|---|---|---|
| Advanced IP Scanner / NetScan | Découverte réseau | Rapporté | Acteur |
| Mimikatz / LaZagne / NetExec | Accès aux identifiants | Rapporté | Acteur |
| SharpDomainSpray | Password spraying | Rapporté | Acteur |
| AnyDesk / LogMeIn / MobaXterm | Accès distant / mouvement latéral | Rapporté | Acteur |
| Impacket / `wmiexec.py` | Exécution distante | Rapporté | Acteur |
| PowerTool | Désactivation de processus antivirus | Rapporté | Acteur |
| POORTRY | Abus BYOVD | Rapporté | Acteur |
| STONESTOP | Loader / installateur de payloads | Rapporté | Acteur |
| SystemBC | RAT / proxy bot | Rapporté | Acteur |
| Cobalt Strike | Post-exploitation / C2 | Rapporté | Acteur |
| Ngrok / Cloudflare Tunnel | Tunneling / C2 / support à l'exfiltration | Rapporté | Acteur |
| RClone / WinSCP / FileZilla | Transfert / exfiltration | Rapporté | Acteur |
| WinRAR | Archivage des données | Rapporté | Acteur |
| Akira_v2 | Encrypteur ransomware | Rapporté | Acteur |
| Megazord | Encrypteur Rust historique ; probablement plus utilisé depuis 2024 | Rapporté | Acteur |

Les outils d'administration légitimes ne sont pas malveillants en eux-mêmes. Il faut les replacer dans le contexte de l'incident.

---

## 5. Artefacts ransomware

Extensions documentées :

```text
.akira
.powerranges
.akiranew
.aki
```

Noms de notes de rançon documentés :

```text
fn.txt
akira_readme.txt
akiranew.txt   # rapporté dans certaines activités Linux/ESXi Akira_v2
```

Akira_v2 est écrit en Rust et offre un contrôle plus fin du chiffrement, notamment pour les environnements virtuels. Les rapports publics documentent également des opérations contre VMware ESXi, Hyper-V et, dans un incident de juin 2025, des disques de VM Nutanix AHV.

---

## 6. Pistes de détection et Threat Hunting

Signaux utiles à corréler :

- nouvel accès VPN/RDP/SSH inhabituel suivi d'une reconnaissance rapide ;
- password spraying contre les accès distants ;
- création d'un compte administrateur de domaine inattendu comme `itadm` ;
- `nltest`, Advanced IP Scanner ou NetScan juste après un accès distant ;
- accès anormal à LSASS, SAM ou NTDS ;
- apparition d'AnyDesk, LogMeIn, MobaXterm, Ngrok ou SystemBC ;
- tentative de suppression d'EDR ou utilisation de PowerTool/BYOVD ;
- outils déposés dans `PerfLogs` ;
- `WebClient.DownloadString()` suivi d'une activité Cobalt Strike ;
- RClone/WinSCP après création d'archives volumineuses ;
- suppression VSS suivie d'un chiffrement massif.

Ce sont des pistes de hunting, pas des règles d'attribution autonomes.

---

## 7. Évaluation AFRINTEL

Cette fiche doit surtout servir de **contexte au niveau acteur**. Elle montre ce que des affiliés Akira ont fait dans différents incidents documentés.

Pour une victime AFRINTEL, il faut établir séparément le vecteur d'accès, la CVE exploitée, le compte compromis, les outils, le mouvement latéral, l'exfiltration et la méthode de déploiement du ransomware avant d'attribuer des TTP au niveau victime.

### Lacunes à traiter au niveau victime

- vecteur d'accès initial ;
- compte compromis exact ;
- CVE réellement exploitée ;
- infrastructure C2 ;
- hashes des outils et du ransomware ;
- lignes de commande observées ;
- mécanisme de mouvement latéral ;
- destination d'exfiltration ;
- méthode de chiffrement / déploiement.

---

## 8. Sources

- FBI / CISA / DC3 / HHS - **#StopRansomware: Akira Ransomware (AA24-109A)**, mise à jour du 13 novembre 2025
- MITRE ATT&CK
- Renseignement AFRINTEL lorsqu'un incident africain spécifique est cité

---

**AFRINTEL - African Cyber Threat Intelligence**
