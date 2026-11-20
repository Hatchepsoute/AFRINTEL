![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple)

# Liste des victimes africaines de cyberattaques en novembre 2026 (2 fiches)

👉🏾 [**Version anglaise disponible ici**](./victims.md)

## Novembre 2026

**Statut du suivi mensuel : Brouillon** - corpus initial de deux fiches publiées ou observées en novembre 2026. Les statistiques mensuelles ne sont pas générées dans cette étape.

### 16 novembre 2026

#### 🇪🇬 Égypte - Egyptian Drug Store (`egyptiandrugstore.com`) [Data Leak]
- **Date de publication initiale :** 16 novembre 2026 à 11 h 30
- **Date d'export affichée dans la publication :** novembre 2026
- **Date de l'incident :** Non établie
- **Acteur / Groupe :** Sophia
- **Secteur :** Commerce / Pharmacie / E-commerce
- **Site web associé :** [egyptiandrugstore.com](http://egyptiandrugstore.com/)
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Nature de l'offre :** Vente revendiquée d'une base de données ; échantillon visible, accès au corpus complet non vérifié
- **Volume revendiqué :** 10 000 enregistrements, non vérifié
- **Niveau de confiance :** Medium pour l'existence de la publication, la cohérence du schéma et l'association contextuelle au domaine ; l'origine technique et l'exhaustivité restent non corroborées
- **Niveau d'impact :** Level 4
- **Type de source :** Publication de forum underground et capture visuelle d'un échantillon de base de données

- **Description victime :** Egyptian Drug Store est présenté dans la publication comme un site de commerce en ligne associé à une activité de pharmacie ou de distribution de produits de santé. Le domaine affiché dans la publication est `egyptiandrugstore.com`.

- **Analyse :** La publication du 16 novembre 2026 est placée dans une catégorie de vente et présente une prétendue « 10K Full Database ». Elle indique explicitement que les acheteurs doivent envoyer un message pour acheter la base et affiche ensuite une section « Samples » contenant un extrait structuré. Il s'agit donc d'une offre de vente d'une base de données revendiquée, accompagnée d'un échantillon visible. Le volume de 10 000 enregistrements, le caractère complet de la base et la remise effective du corpus à un acheteur restent non vérifiés.

  La capture expose plusieurs représentations tabulaires compatibles avec une base de données de commerce en ligne :

  1. **Table clients :** identifiants client et boutique, prénom et nom, adresse électronique, téléphone, fax, adresse associée, groupe client, statut et approbation ;
  2. **Champs de compte et de session :** colonnes nommées `password`, `salt`, `token`, panier, liste de souhaits, inscription à une newsletter et adresse IP ; la capture ne permet pas de déterminer l'algorithme de hachage, la validité actuelle des valeurs ou l'existence de mots de passe en clair ;
  3. **Table adresses :** identifiants de clients et d'adresses, société, identifiant fiscal, lignes d'adresse, ville, code postal, pays et zone administrative ;
  4. **Table commandes :** identifiants de commande et de facture, informations client, coordonnées de facturation et de livraison, moyen et code de paiement, montant, devise, statut, adresse IP, agent utilisateur et langue préférée.

  La combinaison des colonnes `customer_group_id`, `cart`, `wishlist`, `order_status_id`, `payment_method`, `payment_code`, `shipping_method` et `currency_code` est compatible avec une application de commerce en ligne de type OpenCart. Il s'agit d'une inférence structurelle et non d'une preuve de la plateforme utilisée ni de l'origine technique des données.

  Les données visibles semblent concerner plusieurs pays et plusieurs devises, ce qui peut correspondre à une clientèle internationale ou à un export commercial historique. La capture ne permet pas de calculer le nombre de clients uniques, de commandes, de pays, de transactions ou de personnes affectées. Aucun total financier fiable ne peut être établi à partir de l'image.

  **Observed :** Publication horodatée du 16 novembre 2026 à 11 h 30 ; catégorie de vente affichée ; domaine `egyptiandrugstore.com` ; date d'export indiquée comme novembre 2026 ; invitation à contacter le vendeur pour acheter une base annoncée à 10 000 enregistrements ; section « Samples » présentant des tables clients, adresses et commandes ; colonnes relatives à des données personnelles, comptes, commandes, paiements et informations techniques.

  **Assumption :** La présence du domaine, du nom de la boutique et d'un schéma cohérent de commerce en ligne rend plausible l'association contextuelle de l'échantillon avec Egyptian Drug Store. Cette cohérence ne confirme pas que les fichiers proviennent des serveurs de l'entreprise, qu'ils ont été acquis par l'auteur de la publication ou qu'ils représentent la totalité de sa base de production.

  **Unknown :** Système source, vecteur et date d'accès, méthode d'acquisition, nombre réel de lignes et de personnes, unicité des comptes, validité des mots de passe ou jetons, statut des adresses IP, intégrité de l'export, période couverte, présence de données de paiement complètes, exfiltration, confirmation de l'entreprise et notification à une autorité compétente.

- **Périmètre et limites de l'analyse :** L'analyse est structurelle et préliminaire, fondée sur une capture visuelle ; le fichier CSV original et la base annoncée n'étaient pas disponibles. Les données personnelles, adresses, identifiants, valeurs d'authentification, jetons et adresses IP visibles n'ont pas été transcrits, testés ou ajoutés au dépôt. La capture ne permet pas une analyse exhaustive, une déduplication, un comptage fiable ou une validation des 10 000 enregistrements revendiqués.
- **Évaluation des risques :** Si l'échantillon est authentique, l'exposition pourrait faciliter le credential stuffing, la prise de contrôle de comptes, le phishing ciblé, la fraude aux commandes et aux paiements, l'usurpation de clients, la fraude à la livraison, l'exploitation d'informations fiscales et la corrélation de données personnelles et techniques. Les champs `password`, `salt` et `token` imposent une vérification et une rotation contrôlées côté opérateur, sans présumer qu'une valeur exploitable est encore active.
- **Recommandations SOC / CTI :** Préserver les journaux web, application, base de données, IAM, administration et commandes couvrant au minimum la période précédant le 16 novembre ; rechercher les exports massifs, requêtes inhabituelles, accès privilégiés et transferts sortants ; réinitialiser les secrets et sessions après validation du périmètre ; vérifier les fonctions de paiement, commandes, livraison et comptes clients ; surveiller le phishing, les prises de contrôle et les fraudes liées aux commandes ; notifier les parties compétentes selon la réglementation applicable.
- **Sources / Éléments de preuve :** Publication de forum underground et capture visuelle fournie le 17 novembre 2026 ; domaine et nom de boutique visibles dans la publication. Aucun lien criminel, identifiant, adresse, secret, jeton ou valeur brute n'est reproduit dans le dépôt.

### 17 novembre 2026

#### 🇲🇦 Maroc - Établissement Ard Essalam 2, Salé [Data Leak]
- **Date de publication initiale :** 17 novembre 2026
- **Date de l'incident :** Non établie
- **Acteur / Groupe :** Blacknet00
- **Secteur :** Éducation / Enseignement privé
- **Portée administrative revendiquée :** Académie régionale d'éducation et de formation de Rabat-Salé-Kénitra
- **Établissement identifié dans les échantillons :** Ard Essalam 2, Salé
- **Statut :** Claim - Data Sample Published
- **Type d'incident :** Data Leak
- **Niveau de confiance :** Medium pour l'existence de la publication et l'association contextuelle des échantillons à Ard Essalam 2 ; l'origine technique des fichiers et la compromission restent non corroborées
- **Niveau d'impact :** Level 4
- **Type de source :** Publication de forum underground et cinq échantillons JPEG fournis localement, examinés en lecture seule

- **Description victime :** Ard Essalam 2 est un établissement scolaire privé situé à Salé. Les certificats visibles portent l'en-tête de l'Académie régionale d'éducation et de formation de Rabat-Salé-Kénitra et de la Direction provinciale de Salé. Des sources publiques associent également l'établissement « مؤسسة أرض السلام 2 » à Salé, sans constituer une confirmation de l'incident.

- **Analyse :** La publication observée le 17 novembre 2026 affirme viser l'écosystème éducatif de Rabat-Salé-Kénitra et présente des documents attribués à cet environnement. L'analyse visuelle des cinq JPEG fournis met en évidence des certificats scolaires présentés comme officiels pour l'année 2026-2027, une photographie d'enfant et un extrait partiel de tableau contenant des informations relatives à des enseignants ou membres du personnel. Les catégories visibles comprennent notamment des noms, dates de naissance, identifiants scolaires, niveaux d'études, matières enseignées et coordonnées. Les valeurs individuelles ne sont pas reproduites.

  La publication affirme également l'existence d'extraits d'actes de naissance contenant des informations familiales et des numéros d'identification nationale. Ces éléments n'étaient pas visibles dans les cinq échantillons examinés et restent uniquement revendiqués. La présence d'un en-tête de l'Académie régionale et de la Direction provinciale sur les certificats ne démontre pas que les systèmes de ces administrations ont été compromis. Elle ne permet pas non plus d'établir que l'établissement Ard Essalam 2 constitue le système source des fichiers.

  **Observed :** Publication du 17 novembre 2026 ; cinq fichiers JPEG locaux examinés en lecture seule ; certificats scolaires, photographie d'enfant et extrait de tableau visibles ; association contextuelle des certificats à Ard Essalam 2, à Salé et à l'AREF Rabat-Salé-Kénitra.

  **Assumption :** La cohérence entre le nom de l'établissement lisible sur les certificats, la localisation à Salé et les références administratives rend plausible l'association des échantillons à Ard Essalam 2. Cette cohérence ne confirme ni l'origine technique des fichiers, ni leur méthode d'acquisition, ni une compromission de l'établissement ou de l'AREF.

  **Unknown :** Date et vecteur d'accès, système source, authenticité indépendante des documents, nombre de personnes concernées, volume total, exhaustivité, présence réelle des actes de naissance revendiqués, identité de l'auteur, exfiltration et confirmation par l'établissement, l'AREF ou une autorité compétente.

- **Périmètre et limites de l'analyse :** Les cinq JPEG fournis ont été examinés visuellement en lecture seule. Leur taille cumulée est de 446 573 octets. Aucun fichier natif, export, base de données ou corpus complet n'a été fourni. Les données personnelles visibles, noms, identifiants, coordonnées et photographies ne sont pas reproduits dans le dépôt. L'analyse porte uniquement sur les éléments visibles dans les échantillons fournis.
- **Évaluation des risques :** Si les documents sont authentiques et proviennent d'un accès non autorisé, les risques potentiels comprennent l'usurpation d'identité, le phishing ciblé, la fraude documentaire, l'exploitation de données de mineurs, l'atteinte à la vie privée des familles et l'usurpation de membres du personnel. Ces risques ne constituent pas une confirmation de l'incident.
- **Recommandations SOC / CTI :** Préserver les journaux IAM, applications scolaires, bases de données, postes d'administration et systèmes de stockage ; examiner les exports massifs, accès privilégiés et transferts sortants ; révoquer les sessions et secrets potentiellement exposés ; vérifier les règles de partage et les comptes tiers ; renforcer la MFA, la segmentation et la surveillance des accès aux données d'élèves ; préparer les notifications réglementaires selon la procédure applicable.
- **Sources / Éléments de preuve :** Publication du forum underground et cinq JPEG fournis localement ; [fiche publique de l'Établissement Ard Essalam 2 à Salé](https://www.schoolandcollegelistings.com/MA/Sal%C3%A9/277600618767530/Etablissement-Ard-Essalam-2) ; [document public mentionnant مؤسسة أرض السلام 2 à Salé](https://s4a988bdcec69bd04.jimcontent.com/download/version/1742606078/module/14453774392/name/classement%20final%20des%20arts%20martiaux%20scolaire%202025.pdf). Les fichiers locaux et les données personnelles restent hors du dépôt.

