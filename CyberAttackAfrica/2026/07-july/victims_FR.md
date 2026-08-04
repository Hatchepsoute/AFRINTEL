
### 21 juillet 2026
#### 🇹🇳 Tunisie - Ministère de la Justice
- **Acteur / Groupe :** R3V4ULT
- **Secteur :** Gouvernement / Justice / Administration publique
- **Site web :** [justice.gov.tn](https://justice.gov.tn)
- **Statut :** Fuite de données 
- **Description :**
Le ministère tunisien de la Justice est l’administration publique chargée du secteur judiciaire en Tunisie. Ses activités couvrent notamment l’administration des juridictions, des établissements pénitentiaires et des services judiciaires.

- **Analyse :**

L’acteur R3V4ULT a publié sur un forum cybercriminel un premier ensemble de données présenté comme provenant du ministère tunisien de la Justice. La publication, motivée par un discours hacktiviste lié aux interruptions d’eau et d’électricité en Tunisie, contient deux liens de téléchargement et annonce de possibles divulgations supplémentaires.

Le fichier CSV analysé comprend 6 599 contacts uniques, structurés selon quatre champs : prénom, nom, adresse e-mail et domaine. Parmi ces entrées, 6 593 adresses utilisent les domaines institutionnels justice.gov.tn, mail.justice.gov.tn, e-justice.tn ou mail.e-justice.tn. Aucun mot de passe, hash, jeton d’authentification ou contenu de messagerie n’a été identifié.

L’échantillon comprend également un document administratif numérisé de trois pages, daté du 23 octobre 2024, contenant des références internes, des lignes budgétaires, des montants, des cachets et des signatures. Les dépenses visibles concernent notamment l’eau, l’électricité, le gaz, les télécommunications, les loyers, le transport, la maintenance, les fournitures administratives et certaines dépenses médicales liées aux détenus. Une demande d’approvisionnement en carburant est également visible dans la publication.

Les fichiers observés constituent un échantillon initial et non une publication complète. Ils ne permettent pas de confirmer un accès aux boîtes de messagerie, la compromission d’identifiants ou le vecteur d’intrusion. Les données exposées peuvent toutefois faciliter le phishing ciblé, l’usurpation d’agents publics, la cartographie des services judiciaires et la préparation de fraudes reposant sur des références administratives crédibles.

Comme le rappelle un proverbe éthiopien, « Quand les toiles d’araignée s’unissent, elles peuvent ligoter un lion. » Le ministère devrait renforcer l’authentification multifacteur, surveiller les usages anormaux des comptes institutionnels et rechercher l’origine de l’exposition.

Le secteur gouvernemental restant particulièrement exposé aux fuites de données en Afrique, les autres administrations doivent considérer cette publication comme une alerte sectorielle, contrôler leurs annuaires exposés, informer leurs équipes SOC et sensibiliser les agents aux campagnes de phishing susceptibles de réutiliser ces informations.

---
### 24 juillet 2026
#### 🇲🇦 Maroc - Distamed

- **Acteur / Groupe :** anisanas2
- **Secteur :** Santé / Équipements médicaux
- **Site web :** [distamed.ma](https://distamed.ma)
- **Statut :** Claim - Data Sample Published

- **Description :**

Distamed est une entreprise marocaine spécialisée dans les équipements médicaux et les solutions numériques de santé. Elle intervient notamment dans les domaines de la cardiologie, de la pneumologie, de la neurologie, du diagnostic du sommeil, de la réadaptation et de l’imagerie médicale.

- **Analyse :**

L’acteur anisanas2 affirme avoir extrait les données de Distamed et propose les archives internes de l’entreprise à la vente pour **5 000 USD**. La publication annonce également une future divulgation de l’ensemble des données.

Les fichiers analysés contiennent **8 823 lignes de patients**, dont 8 776 distinctes, avec des noms, dates de naissance, âges, numéros de CNIE, téléphones, villes, assurances et dates de visite. Ils comprennent également **8 147 entrées clients**, **1 195 entrées présentées comme une liste de médecins**, **1 550 contrats**, **1 455 factures** et **3 251 règlements**.

Les documents observés incluent aussi des rapports médicaux contenant des pathologies, des résultats d’examens et des conclusions cliniques. Certaines entrées font référence à des hôpitaux publics et militaires marocains.

La cohérence entre les données administratives, médicales et financières confirme une exposition importante. Cependant, l’affirmation selon laquelle l’archive complète remonterait à 2013 n’est pas démontrée par les éléments analysés, dont les dates observées couvrent principalement la période **2018 à 2026**.

Cette exposition présente des risques élevés d’atteinte au secret médical, d’usurpation d’identité, de fraude documentaire, de fraude à la facturation et de phishing ciblé contre les patients, les médecins et les établissements partenaires.

- **Recommandations :**

1. Analyser les accès, exports et téléchargements inhabituels, puis révoquer immédiatement les comptes, sessions et clés potentiellement compromis.
2. Informer les personnes et institutions concernées, puis renforcer la surveillance des fraudes à l’identité, aux factures et aux changements de coordonnées bancaires.

---

