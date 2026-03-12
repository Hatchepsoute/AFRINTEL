# Groupe Ransomware DevMan - Profil Complet

**Date d'analyse :** 2026-03-08  
**Source :** Halcyon Threat Intelligence (octobre 2025) et recherches internes  
**Niveau de menace :** 7.2 (Élevé)  
**Statut actuel :** Actif (signalé en octobre 2025, avec des opérations soutenues jusqu'en 2026)

---

## Description
Apparu en **avril 2025**, DevMan est un **groupe de ransomware fermé** qui opère comme **affilié multi‑RaaS** (Qilin, DragonForce, Apos, RansomHub) tout en menant ses propres attaques directes. Il conserve un contrôle total sur le cycle de vie des attaques et cible les petites et moyennes entreprises, avec des seuils de chiffre d'affaires de **100 M$+ pour les infrastructures critiques** et **50 M$+ pour la santé**.

Malgré le **doxing de GangExposed en juin 2025**, le groupe a rapidement évolué vers une **version 2.0** (réécrite en Rust) et continue d'acquérir des victimes en Asie‑Pacifique, en Amérique du Nord et en Europe.

---

## Classifications et affiliations
- **Type :** Groupe fermé – aucun recrutement externe d'affiliés ; attaques directes avec des outils propriétaires.
- **Partenariats multi‑RaaS :**
  - **Qilin** (principal) – part des revenus de 80‑85 %.
  - **DragonForce** (lignée technique, utilisation du builder).
  - **Apos, RansomHub** – rôles d'affiliés supplémentaires.
  - Anciennes connexions avec **INC Ransom**.
- **Ciblage basé sur le chiffre d'affaires :**  
  - Infrastructures critiques : ≥ 100 M$ de CA annuel.  
  - Santé : ≥ 50 M$ de CA annuel.

---

## Chronologie de l'évolution
| Version | Période        | Caractéristiques principales                                                                 |
|---------|----------------|----------------------------------------------------------------------------------------------|
| 1.0     | avr. – juin 2025 | Basé sur C++, builder DragonForce, site de fuite TOR (v1), rançon de 60 000 à 2,5 M$.       |
| 2.0     | juil. 2025 –   | Implémentation Rust, nouvelle infrastructure TOR, déploiement GPO, rançon de 1 M$ à 91 M$.  |

- **Juin 2025 :** Doxing GangExposed → abandon temporaire par les affiliés.
- **Juillet 2025 :** Migration rapide vers Rust, maintien du rythme des attaques.

---

## Lignée technique
- Fuite du code source de **Conti** (fév. 2022) → **DragonForce** (2023‑2024) → **DevMan** (avr. 2025).
- Caractéristiques communes : modèles de notes de rançon identiques, exploitation de l'API Windows Restart Manager, chiffrement à trois modes, utilisation du builder DragonForce.

---

## Détails techniques clés

| Élément                | Détails                                                                                                                                     |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Chiffrement**        | Hybride AES‑256 (CBC) + RSA‑2048. Trois modes : complet, en‑tête seulement, personnalisé. Hérité de DragonForce/Conti.                    |
| **Extensions de fichiers** | Version 1.0 : `.DEVMAN`, `.devmanv1`, `.yAGRTb`<br>Version 2.0 : `.devman1`<br>Défaut du builder : `e47qfsnz2trbkhnt.devman`               |
| **Notes de rançon**    | `README.devmanv1.txt` (v1), `README.txt`, `README.yAGRTb.txt`                                                                               |
| **Exfiltration**       | Priorité à l'extorsion de données. En général 50‑300 Go, max 2,5 To. Téléversement sur **Mega.nz**. Sites de fuite TOR dédiés avec comptes à rebours. |
| **Communication**      | Architecture hors ligne (pas de balise C2). Après compromission : protocole **TOX**, services cachés **TOR**, email `devman@cyberfear.com`. |
| **Vitesse de déploiement** | Abus de l'API Windows Restart Manager (contournement des verrous de fichiers), scripts PowerShell/CMD, déploiement par GPO (v2.0).       |
| **Paiement**           | Bitcoin, via portefeuilles affiliés (structure Qilin : 80‑85 % pour l'affilié).                                                            |

### Sites de fuite TOR
- Version 1.0 : `qljmlmp4psnn3wqskkf3alqquatymo6hntficb4rhq5n76kuogcv7zyd.onion`
- Version 2.0 : `wugurgyscp5rxpihef5vl6b6m5ont3b6sezhl7boboso2enib2k3q6qd.onion`

---

## Activités et ciblage
- **Nombre de victimes :** 40‑50 confirmées (T2 2025), 70‑86 au total (T3 2025). Pic d'activité en mai 2025.
- **Répartition géographique :**  
  - **Asie‑Pacifique** (>60 %) : Taïwan, Thaïlande, Chine, Japon, Singapour.  
  - **Secondaire :** Afrique du Sud, Égypte, Kenya.  
  - **Expansion :** Europe, Amérique du Nord (secteurs gouvernemental et énergétique, sept. 2025).
- **Secteurs les plus touchés :**  
  Industrie manufacturière, services aux entreprises/professionnels, IT & télécoms, commerce de détail, construction, santé, gouvernement, infrastructures critiques.

---

## Mode opératoire (cartographie MITRE ATT&CK)

| Tactic                | Technique ID      | Nom                                                | Implémentation par DevMan                                                                                 |
|-----------------------|-------------------|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Accès initial**     | T1566             | Phishing                                           | Pièces jointes malveillantes                                                                              |
|                       | T1078             | Valid Accounts                                     | Brute‑force RDP, pulvérisation de mots de passe, credential stuffing                                     |
|                       | T1190             | Exploit Public‑Facing Application                  | Passerelles VPN, interfaces de gestion, serveurs Microsoft Exchange (pas de CVE spécifique)              |
| **Exécution**         | T1059.001         | Command and Scripting Interpreter: PowerShell      | Scripts PowerShell et cmd pour déployer la charge utile                                                   |
|                       | T1569.002         | System Services: Service Execution                 | PsExec                                                                                                    |
| **Persistance**       | T1547.001         | Boot or Logon Autostart Execution: Registry Run Keys | Modifications du registre dans `HKCU\...\Run`                                                           |
|                       | T1543.003         | Create or Modify System Process: Windows Service   | Création de services malveillants                                                                         |
|                       | T1053.005         | Scheduled Task/Job: Scheduled Task                 | Tâches planifiées                                                                                         |
| **Élévation de privilèges** | T1543.003, T1053.005 | (idem ci‑dessus)                               |                                                                                                           |
| **Contournement des défenses** | T1562.001 | Impair Defenses: Disable or Modify Tools           | Termine les AV, EDR, logiciels de sauvegarde                                                              |
|                       | T1070             | Indicator Removal on Host                          | Suppression rapide de clés de registre (ms), altération des journaux                                     |
|                       | T1027             | Obfuscated Files or Information                    | Implémentation Rust (v2.0) pour échapper à la détection par signature                                    |
|                       | T1484.001         | Domain Policy Modification: Group Policy Modification | Déploiement GPO (v2.0) pour distribution à l'échelle du domaine                                          |
| **Accès aux identifiants** | T1003        | OS Credential Dumping                              | Mimikatz (mémoire LSASS)                                                                                  |
|                       | T1555             | Credentials from Password Stores                    | Info‑stealer personnalisé pour Chrome, Firefox, Edge                                                      |
| **Découverte**        | T1482             | Domain Trust Discovery                              | BloodHound                                                                                                |
|                       | T1018             | Remote System Discovery                             | SoftPerfect Network Scanner                                                                                |
|                       | T1135             | Network Share Discovery                             | Scan SMB des partages administratifs                                                                      |
| **Mouvement latéral** | T1021.002         | Remote Services: SMB/Windows Admin Shares           | Propagation par PsExec                                                                                     |
|                       | T1021.001         | Remote Services: Remote Desktop Protocol            | RDP avec identifiants volés                                                                                |
|                       | T1484.001         | (idem) – GPO également utilisé pour mouvement latéral |                                                                                                           |
| **Collecte**          | T1114             | Email Collection                                    | (probable, mais non détaillé)                                                                             |
| **Commande et contrôle** | T1071         | Application Layer Protocol                          | C2 minimal ; si nécessaire : TOX, TOR                                                                     |
| **Exfiltration**      | T1041             | Exfiltration Over C2 Channel                        | Exfiltration avant chiffrement vers l'infrastructure des attaquants                                       |
|                       | T1567             | Exfiltration Over Web Service                       | Téléversement sur Mega.nz (en général 50‑300 Go, max 2,5 To)                                              |
| **Impact**            | T1486             | Data Encrypted for Impact                           | Chiffrement des fichiers avec trois modes ; abus de l'API Windows Restart Manager                         |
|                       | T1491.001         | Defacement: Internal Defacement                     | Changement du fond d'écran (Windows 10 uniquement)                                                        |
|                       | T1529             | System Shutdown/Reboot                              | Redémarrage forcé                                                                                          |
|                       | T1490             | Inhibit System Recovery                             | Suppression des clichés de volume (VSS)                                                                   |

---

## Indicateurs de compromission (IoC)

### Empreintes de fichiers (SHA256 / MD5)
- **SHA256 principale version 1.0 :** `df5ab9015833023a03f92a797e20196672c1d6525501a9f9a94a45b0904c7403`
- **SHA256 secondaire version 1.0 :** `018494565257ef2b6a4e68f1c3e7573b87fc53bd5828c9c5127f31d37ea964f8`
- **MD5 principale version 1.0 :** `e84270afa3030b48dc9e0c53a35c65aa`

### Domaines / URL (services cachés TOR)
- Site de fuite version 1.0 : `qljmlmp4psnn3wqskkf3alqquatymo6hntficb4rhq5n76kuogcv7zyd.onion`
- Site de fuite version 2.0 : `wugurgyscp5rxpihef5vl6b6m5ont3b6sezhl7boboso2enib2k3q6qd.onion`
- Email de contact pour les victimes : `devman@cyberfear.com`

### TOX ID
`9D97F166730F865F793E2EA07B173C742A6302879DE1B0BBB03817A5A04B572FBD82F984981D`

### Chemins de fichiers / clés de registre
- Sessions temporaires de Windows Restart Manager :  
  `HKEY_CURRENT_USER\Software\Microsoft\RestartManager\Session0000`
- Persistance via la clé Run :  
  `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`

### Extensions de fichiers (fichiers chiffrés / notes de rançon)
- `.DEVMAN`, `.devmanv1`, `.yAGRTb` (v1)
- `.devman1` (v2)
- Nom déterminé par défaut du builder : `e47qfsnz2trbkhnt.devman`
- Notes de rançon : `README.devmanv1.txt`, `README.txt`, `README.yAGRTb.txt`

### Indicateurs de processus / comportementaux
- Mutex codé en dur : `hsfjuukjzloqu28oajh727190` (haute fiabilité)
- Trafic SMB anormal ciblant les partages administratifs (ADMIN$, C$)
- Exfiltration massive vers `mega.nz`
- Suppressions rapides de clés de registre (millisecondes)
- Utilisation de l'API Windows Restart Manager pour contourner les verrous de fichiers

---

## Exploits et vulnérabilités
| Exploit / vecteur d'attaque                      | CVE   | CVSS | Description                                                                                |
|--------------------------------------------------|-------|------|--------------------------------------------------------------------------------------------|
| Phishing, brute‑force RDP, credential stuffing   | N/A   | N/A  | Accès initial par interaction utilisateur ou faiblesse des identifiants.                   |
| Services non corrigés exposés (VPN, Exchange)    | N/A   | N/A  | Exploitation de vulnérabilités connues sans ciblage CVE spécifique ; repose sur des systèmes non patchés. |
| Abus de l'API Windows Restart Manager             | N/A   | N/A  | API légitime utilisée de manière malveillante pour déverrouiller les fichiers pendant le chiffrement. |

*Aucune CVE n'est actuellement associée à DevMan dans les bases de données publiques (NVD, CISA KEV).*

---

## Recommandations pour la détection et l'atténuation
1. **Surveiller les IoC comportementaux :**
   - Abus de l'API Windows Restart Manager (création/suppression rapide de sessions registre).
   - Suppressions rapides de clés de registre.
   - Scans SMB volumineux pour les partages administratifs.
   - Connexions vers Mega.nz ou des nœuds de sortie TOR.
2. **Renforcer les identifiants :**
   - Activer l'AMF pour tous les services exposés (RDP, VPN).
   - Utiliser des mots de passe forts et uniques, surveiller les tentatives de brute‑force.
3. **Limiter les outils d'administration :**
   - Restreindre l'utilisation de PsExec, PowerShell à distance et des tâches planifiées aux administrateurs autorisés.
   - Activer la journalisation et les alertes sur leur utilisation.
4. **Protéger les sauvegardes :**
   - Stocker les sauvegardes hors ligne ou dans un stockage immuable pour empêcher leur suppression.
5. **Corriger les services externes :**
   - Maintenir à jour les passerelles VPN, les serveurs Exchange et les interfaces de gestion.
6. **Déployer des solutions EDR :**
   - Se concentrer sur la détection comportementale (création de processus anormaux, modifications du registre, trafic SMB).

---

## Références
- [Profil du groupe Halcyon – DevMan](https://www.halcyon.ai/threat-group/devman) (octobre 2025)
- Analyse interne des IoC et TTP observés.

**Dernière mise à jour :** 2026-03-08