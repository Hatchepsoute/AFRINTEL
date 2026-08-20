[![AFRINTEL](https://img.shields.io/badge/AFRINTEL-Cyber%20Threat%20Intelligence-blue)](https://github.com/Hatchepsoute/AFRINTEL)
![Scope](https://img.shields.io/badge/Scope-Africa-orange)
![Threat Type](https://img.shields.io/badge/Threat-Ransomware-red)
![Data Source](https://img.shields.io/badge/Data%20Source-OSINT-darkgreen)
![Intel Type](https://img.shields.io/badge/Intel-CTI-purple) ![Période](https://img.shields.io/badge/Période-2025-blue)
# Rapport CTI : Cyberattaques en Afrique - Juillet 2025 (21 victimes)
👉🏾 [**English version available here**](./README.md)

## 1. Résumé exécutif
- **Nombre total d'attaques recensées** : 21
- **Acteurs les plus actifs** : Dark 07x Team (5 attaques), Inconnu (2), Hepd (1), sanji_shi5 (1), d4rk4rmy (1), Evil_BYTE_Officiel (1), nightspire (1), Keymous (1), Phantom Atlas (1), lynx (1), devman (1), incransom (1), Mercobyte (1), Gh1nDar (1), Wieko (1), BabayoSysteam (1).
- **Secteurs les plus ciblés** : Administrations publiques (6), Banque/Finance (4), Éducation/Formation (4), Télécommunications (2), Association professionnelle/Bâtiment (1), Industrie minière (1), Services postaux/financiers (1), Diplomatie/Gouvernement (1), Commerce/E-commerce (1).
- **Pays les plus touchés** : Tunisie (5), Maroc (4), Algérie (2), Kenya (2), Nigeria (1), Afrique du Sud (1), Tanzanie (1), Égypte (1), Namibie (1), Mauritanie (1), Érythrée (1), Burundi (1).
- **Volumes de données revendiqués notables** : Rançon de 2,27 M$ demandée pour eehc.gov.eg (Égypte). FNBTP (Maroc) : base de données de 180 lignes / 14 colonnes publiée gratuitement. Ambassade d'Érythrée aux États-Unis : revendication non vérifiée portant sur environ 5 000 enregistrements de citoyens. PesaBay (Burundi) : base de données complète de 1 850 enregistrements publiée. Autres volumes non précisés.


## 2. Méthodologie
Ce rapport de Cyber Threat Intelligence (CTI) présente une analyse détaillée des cyberattaques survenues en Afrique durant le mois de juillet 2025. Les informations sont issues de sources OSINT et de sites de fuites de groupes ransomware, compilées dans le cadre du projet AFRINTEL. L'objectif est de fournir une vision claire des tendances, des acteurs menaçants, des secteurs ciblés et des indicateurs de compromission associés.


## 3. Vue d'ensemble

### 3.1 Répartition par groupe/acteur
| Groupe/Acteur | Nombre d'attaques |
|---------------|-------------------|
| Dark 07x Team | 5                 |
| Hepd          | 1                 |
| d4rk4rmy      | 1                 |
| Evil_BYTE_Officiel | 1            |
| nightspire    | 1                 |
| Keymous       | 1                 |
| Phantom Atlas | 1                 |
| lynx          | 1                 |
| devman        | 1                 |
| incransom     | 1                 |
| Mercobyte     | 1                 |
| Wieko         | 1                 |
| sanji_shi5    | 1                 |
| Inconnu       | 2                 |
| Gh1nDar       | 1                 |
| BabayoSysteam | 1                 |
| **Total**     | **21**            |

```mermaid
pie showData
    title Répartition des attaques par acteur (juillet 2025)
    "Dark 07x Team" : 5
    "Hepd" : 1
    "d4rk4rmy" : 1
    "Evil_BYTE_Officiel" : 1
    "nightspire" : 1
    "Keymous" : 1
    "Phantom Atlas" : 1
    "lynx" : 1
    "devman" : 1
    "incransom" : 1
    "Mercobyte" : 1
    "Wieko" : 1
    "sanji_shi5" : 1
    "Inconnu" : 2
    "Gh1nDar" : 1
    "BabayoSysteam" : 1
```
### 3.2 Répartition par secteur d'activité

| Secteur | Nombre d'attaques |
|---------|-------------------|
| Administrations publiques| 6 |
| Banque / Finance| 4 |
| Éducation / Formation | 4 |
| Télécommunications | 2 |
| Association professionnelle / Bâtiment | 1 |
| Industrie minière | 1 |
| Services postaux / financiers | 1 |
| Diplomatie / Gouvernement | 1 |
| Commerce / E-commerce | 1 |
| **Total** | **21** |

```mermaid
pie showData
    title Répartition par secteur d'activité (Juillet 2025)
    "Administrations publiques" : 6
    "Banque / Finance" : 4
    "Éducation / Formation" : 4
    "Télécommunications" : 2
    "Association professionnelle" : 1
    "Industrie minière" : 1
    "Services postaux / financiers" : 1
    "Diplomatie / Gouvernement" : 1
    "Commerce / E-commerce" : 1
```
### 3.3 Répartition par pays
| Pays | Nombre d'attaques |
|------|-------------------|
| 🇹🇳 Tunisie | 5 |
| 🇲🇦 Maroc | 4 |
| 🇩🇿 Algérie | 2 |
| 🇿🇦 Afrique du Sud | 1 |
| 🇳🇬 Nigeria | 1 |
| 🇹🇿 Tanzanie | 1 |
| 🇰🇪 Kenya | 2 |
| 🇪🇬 Égypte | 1 |
| 🇳🇦 Namibie | 1 |
| 🇲🇷 Mauritanie | 1 |
| 🇪🇷 Érythrée | 1 |
| 🇧🇮 Burundi | 1 |
| **Total** | **21** |

```mermaid
pie showData
    title Répartition par pays (Juillet 2025)
    "🇹🇳 Tunisie" : 5
    "🇲🇦 Maroc" : 4
    "🇩🇿 Algérie" : 2
    "🇳🇬 Nigeria" : 1
    "🇿🇦 Afrique du Sud" : 1
    "🇹🇿 Tanzanie" : 1
    "🇰🇪 Kenya" : 2
    "🇪🇬 Égypte" : 1
    "🇳🇦 Namibie" : 1
    "🇲🇷 Mauritanie" : 1
    "🇪🇷 Érythrée" : 1
    "🇧🇮 Burundi" : 1
```


<!-- AFRINTEL_CURRENT_MODEL_START -->
### 3.4 Vue globale standardisée

| Pays | Ransomware | Exposition des données (fuites + accès) | Total | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| 🇹🇳 Tunisie | 0 | 5 | 5 |  🟦🟦🟦🟦🟦 |
| 🇲🇦 Maroc | 0 | 4 | 4 |  🟦🟦🟦🟦 |
| 🇩🇿 Algérie | 0 | 2 | 2 |  🟦🟦 |
| 🇰🇪 Kenya | 1 | 1 | 2 | 🟧 🟦 |
| 🇪🇬 Égypte | 1 | 0 | 1 | 🟧 |
| 🇪🇷 Érythrée | 0 | 1 | 1 |  🟦 |
| 🇲🇷 Mauritanie | 0 | 1 | 1 |  🟦 |
| 🇳🇦 Namibie | 1 | 0 | 1 | 🟧 |
| 🇳🇬 Nigeria | 0 | 1 | 1 |  🟦 |
| 🇿🇦 Afrique du Sud | 1 | 0 | 1 | 🟧 |
| 🇹🇿 Tanzanie | 1 | 0 | 1 | 🟧 |
| 🇧🇮 Burundi | 0 | 1 | 1 |  🟦 |

```mermaid
pie showData
    title Types d’incidents
    "Ransomware" : 5
    "Fuites de données + ventes d’accès" : 16
```

### Vue agrégée mensuelle de l’exposition

La vue CTI mensuelle regroupe les fuites de données et les ventes d’accès sous **exposition des données** : **16 fiches** (76,2% du corpus mensuel). Les fiches sources restent la référence ; une vente d’accès ne prouve pas à elle seule l’exfiltration de données.


### Répartition géographique par région

| Région | Occurrences | Ransomware | Exposition des données (fuites + accès) | Distribution |
| :--- | ---: | ---: | ---: | :--- |
| Afrique du Nord | 13 | 1 | 12 | 🟧 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 |
| Afrique australe | 2 | 2 | 0 | 🟧🟧 |
| Afrique de l’Ouest | 1 | 0 | 1 |  🟦 |
| Afrique centrale | 0 | 0 | 0 |  |
| Afrique de l’Est | 5 | 2 | 3 | 🟧🟧 🟦🟦🟦 |

```mermaid
xychart
    title "Occurrences par région"
    x-axis ["NA","SA","AO","AC","AE"]
    y-axis "Occurrences" 0 --> 14
    bar [13,2,1,0,5]
```
Légende : NA = Afrique du Nord ; SA = Afrique australe ; AO = Afrique de l’Ouest ; AC = Afrique centrale ; AE = Afrique de l’Est

### Répartition sectorielle

| Secteur | Fiches | Part | Activité |
| :--- | ---: | ---: | :--- |
| Gouvernement / administration | 9 | 42,9% | ██████████ |
| Finance / banque | 6 | 28,6% | ███████ |
| Éducation / universités | 2 | 9,5% | ██ |
| Technologies / informatique | 2 | 9,5% | ██ |
| Commerce / E-commerce | 1 | 4,8% | █ |
| Énergie / services publics | 1 | 4,8% | █ |

### Acteurs / groupes les plus présents

| Acteur / Groupe | Fiches | Activité |
| :--- | ---: | :--- |
| Dark 07x Team | 5 | ██████████ |
| Unknown | 2 | ████ |
| Evil_BYTE_Officiel | 1 | ██ |
| Gh1nDar | 1 | ██ |
| Hepd | 1 | ██ |
| Keymous | 1 | ██ |
| Mercobyte | 1 | ██ |
| Phantom Atlas | 1 | ██ |
| Wieko | 1 | ██ |
| d4rk4rmy | 1 | ██ |
<!-- AFRINTEL_CURRENT_MODEL_END -->

### Comparaison avec le mois précédent

À partir des fiches incidents validées comme source de comptage, juillet 2025 compte **21** incidents contre **21** le mois précédent (aucune variation de **0** ; **+0.0%**). Cette comparaison décrit les publications enregistrées par AFRINTEL et ne prouve pas à elle seule une évolution de l'activité des attaquants ni un impact confirmé sur les victimes.

| Indicateur | Mois précédent | Mois en cours | Variation |
|---|---:|---:|---:|
| Fiches incidents enregistrées | 21 | 21 | 0 (+0.0%) |

## 4. Analyse détaillée par type d'incident

## 5. Impact sectoriel
- **Banque/Finance** : 4 attaques (CIBN, BTK, Banque de Tunisie, BH Bank). Dark 07x Team a ciblé trois banques tunisiennes et Hepd a visé l'organisme de régulation nigérian, montrant une attention soutenue au secteur financier.
- **Administrations publiques** : 4 revendications (eehc.gov.eg, Otjiwarongo Municipality, Ministère des Finances tunisien, Portail QCE Mauritanie).
- **Éducation/Formation** : 4 attaques (Twaweza, ABF, UM6P, Ministère de l’Éducation). La publication de Wieko annonce une combo list multi-établissements et n’établit pas une compromission du SI central du ministère.
- **Télécommunications** : 2 attaques (IWACLUB, Adrian Kenya). Keymous et lynx ont ciblé des entreprises du secteur au Maroc et au Kenya.
- **Association professionnelle/Bâtiment** : 1 attaque (FNBTP) par Evil_BYTE_Officiel, exposant une base de données d'adhérents de 180 lignes publiée gratuitement.
- **Industrie minière** : 1 attaque (MAFATE) par d4rk4rmy en Afrique du Sud.
- **Diplomatie/Gouvernement** : 1 revendication non vérifiée (Ambassade d'Érythrée aux États-Unis) par Gh1nDar, concernant la représentation diplomatique d'un État africain à l'étranger.
- **Commerce/E-commerce** : 1 fuite concernant PesaBay au Burundi, avec publication complète d'une base de données de 1 850 comptes contenant des données de contact d'utilisateurs.


## 6. Profil des acteurs
### 6.1 Profil des acteurs

Les comptages d'acteurs et de sources restent ceux documentés en section 3 et dans les fiches victimes sources. L'attribution est conservée uniquement au niveau étayé par les éléments publics.

### 6.2 Évaluation du risque

Les pays et secteurs présentant plusieurs fiches ou des fonctions publiques, éducatives, sanitaires, financières ou critiques doivent faire l'objet d'une validation prioritaire. Il s'agit d'un signal de priorisation OSINT, et non d'une confirmation de compromission ou d'impact.

- **Tunisie** : 5 attaques, toutes menées par Dark 07x Team, ciblant le gouvernement et le secteur bancaire. La Tunisie est le pays le plus touché du mois, avec une campagne coordonnée.
- **Maroc** : 4 revendications (FNBTP, IWACLUB, UM6P, Ministère de l’Éducation) impliquant Evil_BYTE_Officiel, Keymous, Mercobyte et Wieko.
- **Nigeria** : 1 attaque (CIBN) par Hepd, visant l'organisme de régulation bancaire.
- **Afrique du Sud** : 1 attaque (MAFATE) par d4rk4rmy dans le secteur minier.
- **Tanzanie** : 1 attaque (Twaweza) par nightspire, touchant une ONG éducative.
- **Kenya** : 2 fiches (ICT Authority et Adrian Kenya), concernant une infrastructure numérique publique et un prestataire télécom/ingénierie.
- **Égypte** : 1 attaque (eehc.gov.eg) par devman, avec une demande de rançon élevée.
- **Namibie** : 1 attaque (Otjiwarongo Municipality) par incransom, visant une administration locale.
- **Mauritanie** : 1 revendication non attribuée (Portail QCE), une plateforme publique de qualification du personnel et des entreprises, avec un échantillon examiné localement de CV, cartes d'identité nationale, diplômes et contrats de travail notariés.
- **Érythrée** : 1 revendication non vérifiée (Ambassade d'Érythrée aux États-Unis) par Gh1nDar, visant une représentation diplomatique érythréenne plutôt qu'une entité domestique.
- **Burundi** : 1 fuite concernant la place de marché PesaBay, attribuée au compte BabayoSysteam, avec publication complète d'une base de 1 850 enregistrements.

L'Afrique du Nord (Tunisie, Maroc, Algérie, Égypte et Mauritanie) concentre 13 fiches sur 21. L'Afrique de l'Est atteint 5 fiches avec l'ajout du cas burundais.

### 6.1 Chronologie des attaques
```mermaid
timeline
    title AFRINTEL Juillet 2025 - Chronologie des attaques

    section 01 Juillet
        Hepd : CIBN (🇳🇬 Nigeria)
    section 08 Juillet
        d4rk4rmy : MAFATE (🇿🇦 Afrique du Sud)
    section 09 Juillet
        Evil_BYTE_Officiel : FNBTP (🇲🇦 Maroc)
    section 13 Juillet
        nightspire : Twaweza (🇹🇿 Tanzanie)
    section 14 Juillet
        Keymous : IWACLUB (🇲🇦 Maroc)
    section 15 Juillet
        lynx : Adrian Kenya (🇰🇪 Kenya)
        devman : eehc.gov.eg (🇪🇬 Égypte)
        incransom : Otjiwarongo (🇳🇦 Namibie)
        Inconnu : Portail QCE (🇲🇷 Mauritanie)
    section 18 Juillet
        Mercobyte : UM6P (🇲🇦 Maroc)
    section 25 Juillet
        Dark 07x Team : Ministère Finances (🇹🇳 Tunisie)
        Dark 07x Team : ABF (🇹🇳 Tunisie)
        Dark 07x Team : BTK Bank (🇹🇳 Tunisie)
        Dark 07x Team : Banque de Tunisie (🇹🇳 Tunisie)
    section 27 Juillet
        Gh1nDar : Ambassade d'Érythrée (🇪🇷 Érythrée)
    section 28 Juillet
        Dark 07x Team : BH Bank (🇹🇳 Tunisie)
    section 29 Juillet
        Wieko : Ministère de l’Éducation (🇲🇦 Maroc)
    section 30 Juillet
        BabayoSysteam : PesaBay (🇧🇮 Burundi)
```
        

## 7. Tendances et lacunes de renseignement
### 7.1 Tendances observées

Les répartitions par pays, secteur, acteur et type d'incident présentées ci-dessus constituent les tendances traçables du mois. Elles décrivent le corpus surveillé et n'établissent pas une campagne plus large sans éléments indépendants.

### 7.2 Lacunes de renseignement

Les rapports disponibles ne permettent pas d'établir pour chaque revendication le vecteur d'accès initial, l'exfiltration complète, la confirmation par la victime, la chronologie de remédiation ou l'impact opérationnel. Aucun détail DFIR public n'est inclus dans le corpus consulté pour cette fiche mensuelle ; cette absence est limitée aux sources examinées.

## 8. Cartographie MITRE ATT&CK (contextuelle)
| Phase | ID technique | Nom | Association à l'incident |
|---|---|---|---|
| Collecte | T1005 | Data from Local System | Correspondance contextuelle pour une collecte ou exposition revendiquée ; la méthode n'est pas confirmée. |
| Collecte | T1213 | Data from Information Repositories | Correspondance contextuelle pour les dossiers ou référentiels décrits publiquement ; la méthode n'est pas confirmée. |

Ces correspondances ATT&CK sont contextuelles et défensives. Elles ne prouvent pas qu'un acteur donné a utilisé la technique.

### Contextual observations
- **Campagnes coordonnées** : Dark 07x Team a mené plusieurs attaques simultanées contre des cibles tunisiennes, montrant une planification avancée.
- **Compromission de comptes (ATO)** : observée sur BTK Bank et BH Bank, avec mise en vente d'accès.
- **Exfiltration de données sensibles** : données financières, identités, informations sur l'élite bancaire (CIBN).
- **Demande de rançon** : devman a exigé 2,27 M$ pour eehc.gov.eg.
- **Opérations d'influence** : Mercobyte a publié des photos d'étudiants avec un message politique, allant au-delà de l'extorsion classique.
- **Hacktivisme** : Dark 07x Team semble avoir des motivations multiples (financières et politiques).
- **Publication gratuite / divulgation réputationnelle** : Evil_BYTE_Officiel a publié gratuitement la base de données FNBTP plutôt que de la vendre, cohérent avec une motivation réputationnelle plutôt que purement financière.
- **Circulation de jeux de données non attribués** : le cas du Portail QCE (Mauritanie) implique un échantillon de documents de qualification de personnel circulant sans acteur revendicateur ni post de forum identifié.
- **Exposition de données de comptes e-commerce** : la base PesaBay publiée contient des données de contact et des statuts de compte pouvant faciliter le phishing, le spam et l'usurpation d'identité.


## 9. Recommandations
- **Tunisie** : les institutions financières et gouvernementales doivent renforcer leur cybersécurité de manière urgente face à des campagnes coordonnées. Mettre en place une cellule de veille et de réponse aux incidents.
- **Secteur bancaire** : les banques (CIBN, BTK, BT, BH) doivent revoir leurs protocoles d'authentification et segmenter leurs réseaux pour limiter les compromissions de comptes.
- **Éducation** : les universités (UM6P), académies (ABF) et ONG éducatives (Twaweza) doivent protéger les données personnelles et former le personnel aux risques.
- **Administrations publiques** : renforcer la sécurité des sites web et portails gouvernementaux (eehc.gov.eg, Otjiwarongo, Portail QCE Mauritanie), imposer des contrôles d'accès stricts sur les plateformes traitant des pièces d'identité nationale, et mettre en place des sauvegardes hors ligne.
- **Tous secteurs** : sensibiliser les employés aux risques de phishing, mettre en place l'authentification multi-facteurs et des audits de sécurité réguliers.
- **Plateformes e-commerce** : limiter les exports de comptes, journaliser les consultations massives et notifier les utilisateurs concernés après validation interne de l'incident.


## 10. Recommandations SOC et tactiques
### Observé

Les sources publiques documentent des revendications, des publications ou du matériel exposé. Elles ne fournissent pas à elles seules une télémétrie prouvant une technique ou une compromission active.

### Hypothèses

L'abus d'identifiants, un stockage exposé, des contrôles d'accès faibles ou des privilèges d'export excessifs peuvent expliquer certaines expositions, mais chaque hypothèse doit être vérifiée par l'organisation concernée.

### Préventif

Surveiller les journaux d'identité, VPN, cloud, bases de données, messagerie et transferts sortants. Imposer une MFA résistante au phishing, le moindre privilège, la segmentation, des sauvegardes testées et la révocation rapide des jetons ou identifiants.

## 11. Recommandations stratégiques
1. **Risques observés :** prioriser la validation des organisations, secteurs et types de données documentés dans le corpus mensuel.
2. **Hypothèses :** tester les chemins possibles liés aux identifiants, au stockage cloud et aux exports excessifs sans les présenter comme des faits établis.
3. **Socle préventif :** maintenir l'inventaire des actifs, la classification des données, les exercices de réponse, les plans de reprise et les procédures coordonnées de sécurité, de droit et de protection des données.

## 12. Conclusion
Juillet 2025 a été marqué par une campagne majeure du groupe **Dark 07x Team** contre la Tunisie, avec cinq attaques visant le gouvernement et le secteur bancaire. La diversité des acteurs et des cibles s'étend également au commerce électronique avec la publication visant PesaBay au Burundi. La demande de rançon de 2,27 M$ en Égypte et les fuites de données sensibles observées dans plusieurs pays soulignent l'urgence d'une coopération régionale renforcée. Le cas de l'Érythrée reste une revendication non vérifiée visant la représentation diplomatique d'un État africain à l'étranger.


### Auteur
*Adama ASSIONGBON*  
*Consultant SOC & Cyber Threat Intelligence*  
[LinkedIn Profile](https://www.linkedin.com/in/adama-assiongbon-9029893a/)
