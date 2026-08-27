# Gunra - Profil acteur & ransomware

👉🏾 [**English version available here**](./profile.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Groupe :** Gunra
- **Alias / Branding connu :** Golden Community
- **Type de menace :** Ransomware / Double extorsion
- **Modèle opératoire :** Ransomware-as-a-Service (RaaS)
- **Motivation principale :** Financière
- **Plateformes :** Windows et Linux
- **Première observation FBI :** Avril 2025
- **Passage au RaaS formel :** Janvier 2026
- **Source principale :** Avis conjoint #StopRansomware AA26-222A
- **Statut :** Surveillance active
- **Dernière mise à jour :** 27 août 2026

---

## 1. Synthèse

Gunra est une opération ransomware observée par le FBI à partir d'avril 2025. En janvier 2026, les opérateurs ont développé un programme RaaS formel diffusé sur des forums underground.

L'opération utilise la double extorsion : les affiliés volent les données avant le chiffrement puis menacent de les publier ou de les vendre en cas de non-paiement.

L'avis conjoint publié en août 2026 par le FBI, la CISA, la NSA, le DC3, l'USSS et la police nationale sud-coréenne documente des attaques contre des administrations, des infrastructures critiques et des entreprises dans plusieurs pays.

Gunra a aussi recruté des pentesters et des profils issus de la sécurité offensive comme apporteurs d'accès initiaux contre une part de la rançon.

> **Règle AFRINTEL :** les affiliés Gunra peuvent utiliser des méthodes différentes. Les TTP publiées dans l'avis gouvernemental ne sont pas automatiquement attribuées à chaque victime Gunra.

---

## 2. Observation AFRINTEL en Afrique

### 23 avril 2025 - Égypte - Dar Al Teb

AFRINTEL a enregistré une revendication ransomware Gunra visant **Dar Al Teb**, un centre médical égyptien.

- **Pays :** Égypte
- **Secteur :** Santé
- **Site :** daralteb.com
- **Statut :** Revendication - Échantillon de données publié
- **Niveau de confiance :** Élevé
- **Niveau d'impact :** Niveau 4

AFRINTEL a analysé des échantillons comprenant des données médicales sensibles ainsi que du matériel lié à l'infrastructure interne. Les éléments disponibles soutiennent avec un niveau de confiance élevé l'hypothèse d'une compromission réelle et importante.

Le matériel technique comprenait aussi des artefacts liés au réseau interne et à l'accès distant. AFRINTEL ne reproduit pas les données patients, secrets ni paramètres d'accès internes.

**Limite importante :** l'avis gouvernemental 2026 agrège les TTP observées sur plusieurs victimes. AFRINTEL ne considère pas que toutes ces techniques ont forcément été utilisées contre Dar Al Teb.

**Preuve :** Échantillon observé / analyse AFRINTEL  
**Portée :** Niveau victime  
**Confiance :** Élevée  
**Provenance :** AFRINTEL

---

## 3. Accès initial

L'avis conjoint indique que Gunra obtient principalement l'accès en exploitant des vulnérabilités connues sur des équipements exposés à Internet, en particulier des pare-feux et des passerelles VPN.

### Vulnérabilités documentées

| CVE | Produit | Rôle |
|---|---|---|
| CVE-2024-55591 | FortiOS / FortiProxy | Contournement d'authentification / accès initial |
| CVE-2025-24472 | FortiOS / FortiProxy | Contournement d'authentification / accès initial |

ATT&CK :

- **T1190 - Exploit Public-Facing Application**

La police nationale sud-coréenne a également observé l'exploitation de problèmes d'exposition d'identifiants et de contrôles SSH insuffisants sur des passerelles VPN exposées.

Gunra a aussi exploité des identifiants par défaut lorsque les mécanismes de verrouillage de compte étaient absents.

Techniques :

- **T1078.001 - Valid Accounts: Default Accounts**
- **T1078.002 - Valid Accounts: Domain Accounts**
- **T1133 - External Remote Services**

---

## 4. Persistance et Command & Control

Gunra a modifié des comptes existants pour conserver son accès.

Dans un cas documenté, les attaquants ont modifié un compte inutilisé afin de contourner l'obligation de changement de mot de passe.

- **T1098 - Account Manipulation**

Les attaquants ont également téléchargé OpenSSH depuis une infrastructure externe puis utilisé SSH pour établir des tunnels persistants entre des systèmes compromis.

- **T1105 - Ingress Tool Transfer**
- **T1572 - Protocol Tunneling**

---

## 5. Credential Access

Gunra utilise plusieurs méthodes pour récupérer des secrets et des sessions.

### Dump NTDS

Le FBI a observé `secretsdump.py` utilisé contre des contrôleurs de domaine afin d'extraire les hashes depuis NTDS.

- **T1003.003 - OS Credential Dumping: NTDS**

Ces éléments ont ensuite permis :

- **T1550.002 - Pass the Hash**
- **T1550.003 - Pass the Ticket**

### Sniffing et vol de session

Dans un environnement victime, Gunra a abusé des fonctions de contrôle réseau d'un SSL-VPN afin de récupérer les identifiants et informations de session VDI transmis par les utilisateurs.

- **T1040 - Network Sniffing**
- **T1539 - Steal Web Session Cookie**

### Contournement MFA

Les attaquants ont modifié les fichiers de traitement d'authentification d'un portail VDI afin qu'une valeur OTP choisie par l'attaquant soit systématiquement acceptée.

- **T1556.006 - Modify Authentication Process: Multi-Factor Authentication**

### Password stores

Gunra a également récupéré une clé de chiffrement sur un serveur de contrôle d'accès Hiware, puis l'a utilisée pour déchiffrer des mots de passe de serveurs d'entreprise.

- **T1555 - Credentials from Password Stores**
- **T1003 - OS Credential Dumping**

---

## 6. Discovery et furtivité

Le binaire Gunra parcourt les fichiers et répertoires des volumes accessibles en utilisant les API Windows natives.

- **T1106 - Native API**
- **T1083 - File and Directory Discovery**

Les attaquants énumèrent aussi les connexions réseau actives afin d'identifier les systèmes internes accessibles.

- **T1049 - System Network Connections Discovery**

Comportements de furtivité documentés :

- effacement de l'historique des commandes ;
- suppression ou nettoyage de journaux réseau/système ;
- reconnaissance menée tard le soir ou tôt le matin ;
- utilisation de `IsDebuggerPresent` ;
- exclusion de certains dossiers et fichiers système du chiffrement.

---

## 7. Mouvement latéral

Gunra utilise largement Impacket.

Outils documentés :

- `psexec.py` ;
- `smbclient.py` ;
- `secretsdump.py`.

Mécanismes de déplacement latéral :

- SMB / partages administratifs ;
- RDP ;
- pass-the-hash ;
- pass-the-ticket.

Techniques :

- **T1021.001 - Remote Desktop Protocol**
- **T1021.002 - SMB/Windows Admin Shares**
- **T1550.002 - Pass the Hash**
- **T1550.003 - Pass the Ticket**

---

## 8. Collection et exfiltration

Gunra collecte des documents métier, bases de données, données personnelles et emails internes.

### Données cloud

Le FBI a observé un exécutable malveillant nommé `main.exe` utilisé pour cibler Microsoft OneDrive et Microsoft SharePoint.

Techniques :

- **T1530 - Data from Cloud Storage**
- **T1114 - Email Collection**
- **T1005 - Data from Local System**

### Archivage et transfert

Outils observés :

- 7-Zip ;
- WinRAR ;
- RClone ;
- FileZilla.

Pour au moins une victime, des archives contenant des données sensibles ont été envoyées vers **Mega**, avec des volumes allant jusqu'à plusieurs dizaines de téraoctets.

Techniques :

- **T1560 - Archive Collected Data**
- **T1567 - Exfiltration Over Web Service**
- **T1048 - Exfiltration Over Alternative Protocol**

> L'avis conjoint documente clairement Mega et FTP/FileZilla. AFRINTEL n'utilise donc pas comme formulation générique « exfiltration masquée via des utilitaires système » sans preuve propre à un incident.

---

## 9. Impact

Gunra utilise un encrypteur multi-thread reposant sur **ChaCha20 + RSA-4096**.

L'avis documente des versions Windows et Linux ainsi que le chiffrement de systèmes critiques, dont des serveurs de bases de données et des NAS.

- **T1486 - Data Encrypted for Impact**

### Extensions

```text
.ENCRT
.CRYPT
```

`.CRYPT` apparaît dans un échantillon documenté en juillet 2025.

### Note de rançon

Le texte de l'avis documente principalement :

```text
R3ADM3.txt
```

Une transcription d'un tableau ATT&CK repris dans certains miroirs affiche `R34DM3.txt`. AFRINTEL conserve `R3ADM3.txt` comme valeur principale et note cette différence de transcription au lieu d'en faire deux IoC distincts.

---

## 10. Inhibition de la restauration

L'exemple Gunra documenté dans l'avis gouvernemental **n'est pas** :

```text
vssadmin.exe delete shadows /all /quiet
```

Le comportement publié utilise WMI/WMIC pour supprimer des Shadow Copies ciblées :

```text
cmd.exe /c C:\Windows\System32\wbem\WMIC.exe shadowcopy where "ID='{GUID}'" delete
```

Techniques :

- **T1047 - Windows Management Instrumentation**
- **T1059.003 - Windows Command Shell**
- **T1490 - Inhibit System Recovery**

Dans un autre incident, Gunra a également supprimé des sauvegardes et archives stockées au niveau du datacenter principal et du site de reprise.

> AFRINTEL ne retient pas « modification du registre pour bloquer les alertes de sécurité » comme TTP Gunra principale, car l'avis conjoint utilisé ici ne confirme pas cette affirmation.

---

## 11. Outils notables

| Outil | Rôle documenté |
|---|---|
| Impacket `psexec.py` | Mouvement latéral |
| Impacket `smbclient.py` | SMB / déplacement |
| Impacket `secretsdump.py` | Dump NTDS |
| OpenSSH | Tunnel persistant |
| 7-Zip | Archivage |
| WinRAR | Archivage |
| RClone | Collecte / transfert |
| FileZilla | Exfiltration FTP |
| MobaXterm | Administration distante |
| AnyDesk | Accès distant |
| Google Remote Desktop | Accès distant |
| Mimikatz | Credential Access |

La présence d'un de ces outils n'est pas une preuve suffisante d'activité Gunra.

---

## 12. Détection et Threat Hunting

| Signal | Intérêt |
|---|---|
| Exploitation de FortiOS/FortiProxy vulnérables | Accès initial |
| Nouveau compte privilégié ou compte Fortinet modifié | Persistance |
| `secretsdump.py` contre un contrôleur de domaine | Dump NTDS |
| OpenSSH téléchargé sur un système qui ne l'utilise pas normalement | Tunnel persistant |
| RDP inattendu depuis des sessions VDI | Mouvement latéral |
| Fichiers d'authentification VDI modifiés | Contournement MFA |
| `main.exe` accédant à OneDrive/SharePoint | Collecte cloud |
| Archives volumineuses suivies de Mega ou FTP | Exfiltration |
| Suppression de Shadow Copies via WMIC | Inhibition de restauration |
| `.ENCRT` ou `R3ADM3.txt` | Activité de chiffrement |

Ces signaux doivent être corrélés avec le contexte avant toute attribution.

---

## 13. Évaluation AFRINTEL

Le brouillon initial identifiait correctement Gunra comme un nouveau RaaS ayant pris de l'ampleur en 2026, mais plusieurs détails techniques devaient être corrigés.

Les éléments les mieux documentés à ce stade sont :

- exploitation de vulnérabilités Fortinet ;
- abus de comptes par défaut ou compromis ;
- dump NTDS et vol de sessions ;
- tunnels SSH ;
- mouvement latéral RDP/SMB ;
- collecte OneDrive/SharePoint ;
- exfiltration Mega et FTP ;
- suppression de Shadow Copies via WMI ;
- chiffrement Windows et Linux.

AFRINTEL maintient une séparation stricte entre ces TTP gouvernementales et les preuves propres à la victime Dar Al Teb.

---

## 14. Sources

- CISA / FBI / NSA / DC3 / USSS / KNPA - **#StopRansomware: Gunra Ransomware (AA26-222A)**  
  https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a
- CISA - Avis de publication  
  https://content.govdelivery.com/accounts/USDHSCISA/bulletins/4244745
- NSA - *Guidance to Defend Against Gunra Ransomware*  
  https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4567025/nsa-joins-fbi-and-others-in-releasing-guidance-to-defend-against-gunra-ransomwa/
- AFRINTEL - Dar Al Teb / Égypte, 23 avril 2025

---

**AFRINTEL - African Cyber Threat Intelligence**
