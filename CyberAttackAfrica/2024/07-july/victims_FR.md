# Cyberincidents AFRINTEL - Juillet 2024 - corpus canonique (11 fiches)

👉🏾 [English version](./victims.md)

> Ce fichier contient uniquement les incidents retenus dans les statistiques canoniques 2024. Les découvertes historiques, republications, doublons et dossiers à chronologie non résolue sont conservés séparément à la racine 2024.


### 01 Juillet 2024
#### 🇹🇳 Tunisie - Maxcess-logistics
- **Acteur / Groupe:** killsec
- **Secteur:** Transport / Logistics
- **Site web:** [maxcess-logistics.com](https://www.maxcess-logistics.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** Maxcess-logistics est une organisation basée en Tunisie, classée dans Transport / Logistics dans le corpus AFRINTEL.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.

### 02 Juillet 2024
#### 🇪🇹 Éthiopie - F.D.R.E Defence War College (domaine cité : nwc.ndu.edu)

- **Acteur / Groupe:** TheColorYellow
- **Contexte source:** Publication de vente de données sur RaidForums
- **Secteur:** Defense / Security
- **Statut:** Claim - Data Sample Published
- **Site web:** [dwc.edu.et](https://dwc.edu.et/wc/) (organisation observée dans les échantillons) ; domaine cité par l'acteur : nwc.ndu.edu
- **Niveau de confiance:** Medium
- **Niveau d'impact:** Level 4
- **Type d'incident:** Data Leak
- **Date de découverte:** 02 juillet 2024

- **Note de fiabilité:**
  La publication de TheColorYellow annonce une victime présentée comme le « National War College of Ethiopia » et cite le domaine nwc.ndu.edu. Ce domaine correspond au National War College de la National Defense University des États-Unis. Toutefois, les cinq fichiers PNG fournis localement présentent l'emblème et l'en-tête en amharique du « F.D.R.E Defence War College » éthiopien, ainsi que des documents internes, un inventaire de 29 postes et un tableau de 17 entrées téléphoniques. Une erreur de domaine dans l'annonce, une confusion de nom ou une attribution technique incorrecte restent donc possibles. AFRINTEL retient comme organisation observée le F.D.R.E Defence War College et conserve nwc.ndu.edu comme domaine annoncé mais non vérifié.

- **Description:**
  Les éléments visibles correspondent au F.D.R.E Defence War College, établissement d’enseignement militaire éthiopien. Le lien officiel observé pour cette organisation est [dwc.edu.et](https://dwc.edu.et/wc/). Le domaine nwc.ndu.edu reste uniquement le domaine cité dans l’annonce de l’acteur.

- **Analyse:**
  L'acteur TheColorYellow affirme détenir 747 Mo de courriels confidentiels prétendument volés directement sur le serveur Exchange de l'établissement, exportés sous forme de fichiers de boîtes aux lettres PST, et propose ces données pour 500 $ avec recours à un escrow. Le répertoire local fourni contient cinq PNG, mais aucun PST, EML, MSG ou export Exchange. Les images comprennent des documents institutionnels, un avis en chinois pour les étudiants internationaux, un inventaire visible de 29 postes et un tableau visible de 17 entrées téléphoniques. Ces éléments sont cohérents avec des documents internes du F.D.R.E Defence War College et renforcent l'attribution de l'échantillon, mais ne confirment ni l'accès au serveur Exchange, ni l'existence des 747 Mo, ni l'exhaustivité ou l'origine des données. L'OCR amharique et chinois n'a pas été utilisé pour transcrire les valeurs ; aucun nom, numéro, identifiant matériel ou numéro de téléphone n'est reproduit.

### 5 Juillet 2024
#### 🇿🇦 Afrique du Sud - National health laboratory services (NHLS)
- **Acteur / Groupe:** blacksuit
- **Secteur:** Healthcare / Medical
- **Site web:** [nhls.ac.za](https://www.nhls.ac.za)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** Le National Health Laboratory Service (NHLS) est une organisation sud-africaine de services de laboratoires publics, classée dans Healthcare / Medical.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.

### 10 Juillet 2024

#### 🇩🇿 Algérie - EmploiPartner
- **Date de l'incident:** 10 Juillet 2024
- **Date de publication initiale / source retenue:** 14 juillet 2024
- **Date de découverte AFRINTEL:** 23 août 2026 - audit rétrospectif
- **Précision chronologique:** Date du mercredi 10 juillet supportée par les sources de l'audit.
- **Acteur / Groupe:** Unknown
- **Secteur:** Professional / Business Services
- **Site web:** [emploipartner.com](https://www.emploipartner.com/)
- **Statut:** Victim Confirmed
- **Type d'incident:** System Intrusion
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 3
- **Analyse:** EmploiPartner a indiqué avoir détecté et maîtrisé une intrusion non autorisée, lancé une enquête et renforcé sa plateforme. Les sources publiques utilisées dans l'audit ne suffisent pas à confirmer une exfiltration de données, un ransomware, un DDoS ou une vente d'accès. AFRINTEL retient `System Intrusion`.
- **Sources publiques:** [Le Jeune Indépendant](https://www.jeune-independant.net/wp-content/uploads/2024/07/EDITION-14-07-2024.pdf) | [KonBriefing](https://konbriefing.com/en-topics/cyber-attacks-2024.html) | [EmploiPartner](https://www.emploipartner.com/)

----------------------------

### 12 Juillet 2024
#### 🇺🇬 Ouganda - Ministère de l'Éducation et des Sports

- **Date de l'incident :** Non établie ; la date ci-dessous correspond à la publication de l'offre d'accès
- **Date de publication initiale :** 12 juillet 2024 à 06:53 (heure affichée ; fuseau non indiqué)
- **Date de découverte AFRINTEL :** 25 septembre 2026 (capture fournie)
- **Acteur / Groupe :** 303 (compte de forum affiché ; identité et affiliation non vérifiées)
- **Secteur :** Gouvernement / Administration
- **Site web :** [education.go.ug](https://www.education.go.ug/)
- **Statut :** Claim - Unverified
- **Type d'incident :** Access Sale
- **Sous-type :** Offre d'accès administrateur WordPress
- **Niveau de confiance :** Medium
- **Niveau d'impact :** Level 3

- **Description :** Le Ministère de l'Éducation et des Sports de l'Ouganda est présenté dans la publication comme la cible d'une offre d'accès administrateur WordPress associée à `education.go.ug`.

- **Analyse :**

  **Observed :** La capture fournie montre une publication de forum intitulée « Uganda Ministry of Education WordPress Access (Administration Account) », attribuée au compte **303** et horodatée au 12 juillet 2024 à 06:53, avec une modification affichée à 06:54. Elle cite le site `https://www.education.go.ug/` et annonce un accès WordPress administrateur. La zone contenant les identifiants est masquée par le forum et n'a pas été consultée, reproduite ni testée.

  **Assumption :** Le nom de la publication et le domaine cité rendent plausible un lien avec le ministère ougandais. Ils ne permettent pas d'établir que l'accès était réel, actuel, administrateur, ni qu'il concernait l'infrastructure du ministère plutôt qu'un composant tiers.

  **Unknown :** la validité des identifiants, les privilèges effectifs, le vecteur et la date d'obtention de l'accès, les systèmes concernés, toute modification de contenu, toute exposition de données, toute exploitation et toute confirmation du ministère ou d'une autorité restent inconnus.

- **Évaluation des risques :** si l'offre était authentique, un accès administrateur WordPress pourrait permettre la modification de contenus publics, la diffusion de fausses informations, l'usage du site pour le phishing ou l'accès à des données liées à la gestion du site. La publication ne confirme aucun de ces effets.

- **Recommandations :**
1. Préserver les journaux WordPress, d'hébergement, WAF, authentification et administration couvrant juillet 2024 et toute période encore disponible.
2. Examiner les comptes administrateurs, les rôles, les extensions, les thèmes, les accès SFTP ou d'hébergement et les modifications de contenu ou de configuration.
3. Réinitialiser les accès d'administration et révoquer les sessions selon l'enquête défensive du ministère ; activer une MFA résistante au phishing lorsque possible.
4. Ne pas tenter de récupérer, consulter ou tester les identifiants annoncés.
5. Surveiller les défacements, contenus frauduleux et campagnes de phishing imitant les services du ministère.

- **Sources / Éléments de preuve :** publication de forum visible dans la capture fournie le 25 septembre 2026 ; URL originale et contenu masqué non consultés.

### 13 Juillet 2024
#### 🇰🇪 Kenya - Kenya urban roads authority (KURA)
- **Acteur / Groupe:** hunters
- **Secteur:** Transport / Logistics
- **Site web:** [kura.go.ke](https://www.kura.go.ke)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** La Kenya Urban Roads Authority (KURA) est une autorité publique kenyane chargée des infrastructures routières urbaines, classée dans Transport / Logistics.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.

### 17 Juillet 2024
#### 🇿🇼 Zimbabwe - Zb financial holdings
- **Acteur / Groupe:** madliberator
- **Secteur:** Finance / Banking
- **Site web:** [zb.co.zw](https://www.zb.co.zw)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 3
- **Description victime:** ZB Financial Holdings est une organisation financière zimbabwéenne classée dans Finance / Banking.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.

### 17 Juillet 2024
#### 🇿🇦 Afrique du Sud - Cities network
- **Acteur / Groupe:** madliberator
- **Secteur:** Professional / Business Services
- **Site web:** [sacities.net](https://www.sacities.net)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** South African Cities Network est classé dans Professional / Business Services dans le corpus AFRINTEL.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.

### 17 Juillet 2024
#### 🇪🇬 Égypte - Assih
- **Acteur / Groupe:** lockbit3
- **Secteur:** Professional / Business Services
- **Site web:** [assih.com](https://www.assih.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** Assih est une organisation basée en Égypte, classée dans Professional / Business Services dans le corpus AFRINTEL.


- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.

### 22 Juillet 2024
#### 🇿🇦 Afrique du Sud - Sibanye-stillwater
- **Acteur / Groupe:** ransomhouse
- **Secteur:** Mining / Extractive Industries
- **Site web:** [sibanyestillwater.com](https://www.sibanyestillwater.com)
- **Statut:** Claim - Unverified
- **Type d'incident:** Ransomware
- **Niveau de confiance:** Low
- **Niveau d'impact:** Level 2
- **Description victime:** Sibanye-Stillwater est une organisation minière basée en Afrique du Sud, classée dans Mining / Extractive Industries.

---

- **Note de fiabilité:**
  La fiche documente une publication sur un leak site ransomware, sans échantillon technique ni confirmation indépendante de la victime dans le matériel fourni. AFRINTEL ne confirme donc ni l'intrusion, ni le chiffrement, ni l'exfiltration sur la seule base de cette publication.
### 26 Juillet 2024

#### 🇲🇦 Maroc - Arab Civil Aviation Organization (ACAO)
- **Date de compromission:** Inconnue - au plus tard le 26 juillet 2024
- **Date de publication initiale observée:** 26 juillet 2024
- **Date de republication observée:** 12 novembre 2024
- **Publication ultérieure observée:** 24 décembre 2024
- **Acteur / Groupe:** vjvjvj
- **Affiliation revendiquée:** The Night Hunters - selon le post observé
- **Secteur:** Aviation
- **Site web:** [acao.org.ma](https://acao.org.ma)
- **Statut:** Corroborated
- **Type d'incident:** Data Leak
- **Niveau de confiance:** High
- **Niveau d'impact:** Level 4
- **Description victime:** L'Arab Civil Aviation Organization (ACAO) est une organisation intergouvernementale basée à Rabat, au Maroc, active dans la coordination de l'aviation civile entre États arabes.
- **Analyse:** AFRINTEL dispose désormais d'une chronologie plus complète. Une publication du 26 juillet 2024 annonce une base ACAO et fournit un échantillon ainsi qu'une archive annoncée. Une publication du 12 novembre 2024 est explicitement marquée `[REPOST]`, ce qui indique qu'elle ne constitue pas une nouvelle compromission. Une autre publication du 24 décembre 2024 revendique à nouveau une compromission et affiche un échantillon de données associé à ACAO. Les éléments visibles dans les captures et le fichier structuré examiné sont cohérents avec des données liées à l'écosystème ACAO et de l'aviation civile, notamment des informations de contact, fonctions et éléments professionnels. AFRINTEL ne reproduit aucune donnée personnelle brute. Ces éléments corroborent l'existence d'une exposition de données, mais ne permettent pas d'établir la date technique exacte de l'accès initial ni de prouver que la publication de décembre correspond à une seconde intrusion indépendante.
- **Qualification de la preuve:** `Corroborated`. Plusieurs publications distinctes se recoupent et des échantillons cohérents avec ACAO sont visibles. Il n'existe toutefois pas de confirmation publique de la victime ou d'une autorité identifiée dans les éléments examinés.
- **Source / provenance:** Publications underground observées et analysées par AFRINTEL ; captures conservées. Aucune URL opérationnelle du forum ou de téléchargement n'est publiée.

----------------------------
