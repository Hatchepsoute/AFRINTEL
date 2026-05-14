# Victimes africaines - Mai 2026

### 01 Mai 2026
#### 🇪🇹 Éthiopie - National Oil Ethiopia PLC (NOC)  [Fuite de données]

- **Acteur / Groupe :** MDGhost
- **Secteur :** Énergie / Pétrole & Gaz / Infrastructure critique
- **Site web :** [nationaloilethiopia.com](https://www.nationaloilethiopia.com/)
- **Statut :** Compromission revendiquée / Publication technique et vente de données
- **Description victime :** National Oil Ethiopia PLC (NOC) est une entreprise énergétique stratégique éthiopienne spécialisée dans les activités pétrolières, la distribution de carburants et les opérations énergétiques nationales. Une publication découverte le 01 Mai 2026 sur un forum cybercriminel revendique une compromission complète de l’infrastructure de l’organisation avec exfiltration de plusieurs bases de données critiques totalisant environ 1,3 To de données. L’acteur affirme avoir compromis l’environnement interne via une vulnérabilité Microsoft Exchange ProxyLogon avant d’obtenir un accès étendu aux systèmes internes, serveurs Active Directory, bases ERP et infrastructures réseau. Les données revendiquées incluent informations clients, contrats, salaires, emails, données financières, inventaires, données de production, informations personnelles (PII) et opérations métier internes.

- **Analyse technique préliminaire :**
  - ERP principal revendiqué : ~800 Go
  - Taille totale revendiquée : ~1,3 To
  - Nombre de tables : 512
  - Table `transaction` : ~45,6 millions d’enregistrements
  - Table `production data` : ~98,7 millions d’enregistrements
  - Table `financial record` : ~23,4 millions d’enregistrements
  - Table `inventory` : ~12,3 millions d’enregistrements

- **Éléments d’infrastructure observés :**
  - Présence d’un environnement Active Directory `noc.com.et`
  - Serveurs Windows Server 2008 R2 et 2012 R2 détectés
  - Multiples hôtes Windows XP encore actifs dans l’infrastructure
  - Services LDAP, SMB, RDP, Exchange, MySQL et serveurs web accessibles
  - Références à l’utilisation de reverse shell Metasploit et tunneling Ligolo
  - Mention d’un déploiement final de ransomware après compromission complète

- **Évaluation CTI :**
  L’exposition revendiquée suggère une compromission avancée et durable de l’environnement interne avec risque élevé pour :
  - les opérations énergétiques,
  - les données financières,
  - les systèmes industriels et logistiques,
  - ainsi que la confidentialité des données clients et employés.

- **IoC / Artefacts techniques mentionnés :**  
  Domaine interne observé : `noc.com.et`  
  Hôtes observés : `V-HOF-ADC`, `BACKUPSRV`, `SRVBACKUP`, `S-HOF-TMG-001`  
  Vulnérabilité mentionnée : Microsoft Exchange ProxyLogon  
  Outils mentionnés : Metasploit, Ligolo :contentReference[oaicite:0]{index=0}
  
### Remarque CTI

Cette victime a fait l’objet de **deux revendications distinctes par différents acteurs cybercriminels** :

1. **ByteToBreach** - publication initiale datée du 24 Mars 2026  
2. **MDGhost** - nouvelle publication observée le 01 Mai 2026

Les deux publications revendiquent :
- une compromission complète de l’infrastructure de National Oil Ethiopia PLC (NOC),
- l’exfiltration de bases de données massives,
- des données ERP,
- des informations financières et opérationnelles,
- ainsi qu’un accès étendu à l’environnement interne.

Les éléments techniques publiés présentent plusieurs similarités (ERP volumineux, Active Directory, données métiers, ProxyLogon, accès internes), ce qui peut suggérer :
- une revente/republication du même dataset,
- un partage d’accès entre acteurs,
- une fuite secondaire après compromission initiale,
- ou des opérations distinctes exploitant la même intrusion historique.

À ce stade, il n’est pas possible de confirmer avec certitude si les deux acteurs disposent d’accès indépendants ou s’il s’agit d’une réutilisation du même corpus de données.
---
### 04 Mai 2026
#### 🇩🇿 Algérie - Ministère de l’Industrie Pharmaceutique [Fuite de données]

- **Acteur / Groupe :** kamalsheikhxx
- **Secteur :** Gouvernement / Santé / Industrie pharmaceutique
- **Statut :** Publication de dump complet revendiquée

- **Description :** Une publication sur un forum cybercriminel revendique la fuite d’environ 34,3 Go de données attribuées au Ministère algérien de l’Industrie Pharmaceutique, comprenant plus de 52 000 fichiers et 17 800 dossiers couvrant la période 2019–2025.

- **Données observées :**
  - rapports d’importation de médicaments
  - factures et déclarations douanières
  - registres commerciaux pharmaceutiques
  - données personnelles de responsables
  - autorisations officielles
  - inventaires pharmaceutiques
  - listes de substances psychotropes
  - documents PDF, Excel, Word et ZIP

- **Analyse CTI :**
  Les données exposées suggèrent une compromission potentielle de documents réglementaires, commerciaux et administratifs sensibles liés au secteur pharmaceutique algérien. Les risques incluent espionnage économique, fraude documentaire et exploitation d’informations réglementaires sensibles.

- **Note CTI :**
  La structure documentaire et les catégories de fichiers publiées renforcent la crédibilité potentielle de la fuite revendiquée.
  ---
  
  ### 06 Mai 2026
#### 🇿🇦 Afrique du Sud - Consumer Goods Council of South Africa (CGCSA) [Fuite de données]

- **Acteur / Groupe :** XOverStm / Stormous
- **Secteur :** Commerce / Distribution / Conseil industriel
- **Site web :** [cgcsa.co.za](https://www.cgcsa.co.za/)
- **Statut :** Publication de dump complet revendiquée

- **Description :** Une publication sur un forum cybercriminel revendique la diffusion d’environ 20 Go de données attribuées au Consumer Goods Council of South Africa (CGCSA). L’acteur affirme publier les données après un échec de négociation et un démenti public de la compromission.

- **Données observées :**
  - bases clients
  - rapports internes
  - scripts et documents administratifs
  - factures et rapports exécutifs
  - sauvegardes comptables
  - bases Sage200EVO SQL
  - données financières et commerciales

- **Analyse CTI :**
  Les éléments publiés suggèrent une exposition de données commerciales, comptables et clients potentiellement sensibles liées au secteur sud-africain de la distribution et des biens de consommation. Les risques incluent fraude financière, espionnage commercial et compromission d’informations clients.

- **Note CTI :**
  La publication mentionne explicitement un conflit post-compromission avec la victime ainsi que la diffusion publique des données via plusieurs archives.
---

### 12 Mai 2026
#### 🇲🇦 Maroc - SDTM / Groupe Barid Al-Maghrib

- **Acteur /Groupe :** Sejjil
- **Secteur :** Logistique / Transport / Services postaux / ERP
- **Organisation ciblée :** SDTM – Groupe Barid Al-Maghrib
- **Site web :** [poste.ma](https://www.poste.ma)
- **Statut :** Fuite de données / Revendication
- **Description victime :**  
  SDTM est une filiale logistique du Groupe Barid Al-Maghrib spécialisée dans le transport, la distribution, la gestion de flotte et les services associés aux opérations postales et financières au Maroc.

- **Description de la fuite :**  
  Une publication apparue le 12 mai 2026 revendique l’exposition complète de l’infrastructure ERP et financière de SDTM. L’auteur affirme détenir 129 fichiers CSV structurés provenant de systèmes SAGE ERP, passerelles SMS, données bancaires et plateformes internes associées aux opérations logistiques et financières.

- **Analyse des échantillons :**  
  Les échantillons observés contiennent des métadonnées administratives, comptes utilisateurs ERP, hashes MD5 de mots de passe, tokens de session actifs, adresses email professionnelles, informations d’agences, numéros de téléphone, données financières internes, identifiants RIB, désignations de comptes et informations clients incluant CIN et adresses physiques.

- **CTI Note :**  
  Les données publiées suggèrent une compromission profonde d’environnements ERP et applicatifs internes. La présence de tokens actifs, comptes administratifs et données financières structurées pourrait faciliter des opérations de fraude, d’accès persistant ou de compromission latérale. Le volume exact et l’authenticité complète de l’ensemble revendiqué restent à confirmer indépendamment.
