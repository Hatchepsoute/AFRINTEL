# Rapport CTI annuel AFRINTEL - Cybermenaces en Afrique - 2024

👉🏾 [English version](./README.md)

## 1. Synthèse exécutive

Après réévaluation complète de la chronologie, des republications et des dossiers en attente, AFRINTEL retient **119 cyberincidents canoniques dans 30 pays africains en 2024**.

La baseline précédente de 117 est corrigée par la résolution de deux dossiers : **ACAO**, désormais rattaché au **26 juillet 2024** comme `Data Leak` corroboré, et **Misr Pharmacies**, rattaché au **30 décembre 2024** comme `Data Leak / Claim - Unverified`. ACAO ne constitue pas un nouvel ajout par rapport au dépôt historique de 128 fiches : sa fiche était déjà présente en novembre mais avait été temporairement sortie pour chronologie non résolue ; elle est maintenant déplacée vers juillet. Misr Pharmacies est un ajout supplémentaire résolu grâce à la publication originale préservée.

Le paysage est dominé par **Ransomware : 91 (76,5 %)**, suivi de **Data Leak : 13 (10,9 %)**, **System Intrusion : 7**, **Access Sale : 4**, **DDoS : 2**, **Defacement : 1** et **Operational Fraud : 1**. `Account Takeover` et `Malware` restent à 0.

Les pays les plus représentés sont **Afrique du Sud 36**, **Égypte 14**, **Nigeria 7** et **Tunisie 6**. Les principaux secteurs sont **Finance / Banking 18**, **Government / Administration 17** et **Professional / Business Services 12**.

La maturité de preuve reste hétérogène : **86 Claim - Unverified**, **15 Claim - Data Sample Published**, **15 Confirmed**, **2 Corroborated** et **1 Attempted**. Ces positions de preuve ne doivent pas être confondues avec le type technique.

> **Principe de chronologie :** un vieux dataset republié en 2024 reste une observation CTI utile mais n'est pas compté comme nouvelle attaque 2024. Une première publication 2024 dont la date technique de compromission est inconnue peut être rattachée à 2024 en indiquant clairement cette incertitude.

## 2. Migration et corrections

| Élément | Effet sur le comptage |
|---|---:|
| Corpus dépôt corrigé antérieur | 128 |
| Découvertes historiques / cross-year retirées | -17 |
| Doublon eTrade/eRIS retiré | -1 |
| 8 omissions 2024 validées ajoutées | +8 |
| Misr Pharmacies résolu et ajouté | +1 |
| ACAO déplacé de novembre vers juillet | 0 |
| **Baseline finale** | **119** |

ACAO a été réintégré après découverte d'une publication du 26 juillet 2024, d'un repost explicite le 12 novembre et d'une publication ultérieure le 24 décembre avec échantillon cohérent. Misr Pharmacies est désormais classé Data Leak à partir du post original du 30 décembre, mais reste `Claim - Unverified` car les fichiers divulgués ne sont plus disponibles pour analyse indépendante.

## 3. Méthodologie

- 9 types canoniques AFRINTEL.
- Incident date / meilleure fenêtre temporelle soutenue prioritaire.
- Date de publication, repost et découverte AFRINTEL séparées.
- Historical reposts exclus du comptage annuel mais archivés.
- DDoS compté par campagne.
- Tentatives gérées par statut.
- Aucun claim n'est converti en confirmation sans preuve.

## 4. Évolution mensuelle

| Mois | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware | Operational Fraud |
|---|---|---|---|---|---|---|---|---|---|---|
| Janvier | 7 | 4 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 |
| Février | 8 | 6 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Mars | 9 | 8 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Avril | 9 | 5 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| Mai | 9 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Juin | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Juillet | 10 | 7 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Août | 16 | 14 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Septembre | 6 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Octobre | 11 | 8 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Novembre | 15 | 12 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| Décembre | 16 | 11 | 3 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |

```mermaid
timeline
    title AFRINTEL - Volume mensuel canonique 2024
    Janvier : 7 incidents
    Février : 8 incidents
    Mars : 9 incidents
    Avril : 9 incidents
    Mai : 9 incidents
    Juin : 3 incidents
    Juillet : 10 incidents
    Août : 16 incidents
    Septembre : 6 incidents
    Octobre : 11 incidents
    Novembre : 15 incidents
    Décembre : 16 incidents
```

## 5. Types d'incident

| Type | Fiches | Part |
|---|---|---|
| Ransomware | 91 | 76,5 % |
| Data Leak | 13 | 10,9 % |
| Access Sale | 4 | 3,4 % |
| DDoS | 2 | 1,7 % |
| Defacement | 1 | 0,8 % |
| Account Takeover | 0 | 0,0 % |
| System Intrusion | 7 | 5,9 % |
| Malware | 0 | 0,0 % |
| Operational Fraud | 1 | 0,8 % |

```mermaid
pie showData
    title Types d'incident - AFRINTEL 2024
    "Ransomware" : 91
    "Data Leak" : 13
    "Access Sale" : 4
    "DDoS" : 2
    "Defacement" : 1
    "System Intrusion" : 7
    "Operational Fraud" : 1
```

## 6. Pays x type

| Pays | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware | Operational Fraud |
|---|---|---|---|---|---|---|---|---|---|---|
| Afrique du Sud | 36 | 32 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Égypte | 14 | 11 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nigeria | 7 | 4 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| Tunisie | 6 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Cameroun | 4 | 2 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| Namibie | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Maroc | 4 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kenya | 4 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Côte d'Ivoire | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Libye | 3 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Seychelles | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Burkina Faso | 3 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| Algérie | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Zimbabwe | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Angola | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Sénégal | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Éthiopie | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ghana | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tanzanie | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Soudan | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Malawi | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Cabo Verde | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Congo | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Djibouti | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Maurice | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mozambique | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Madagascar | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Mauritanie | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Zambie | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Botswana | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## 7. Répartition régionale

| Région | Fiches | Part |
|---|---|---|
| Afrique australe | 49 | 41,2 % |
| Afrique du Nord | 31 | 26,1 % |
| Afrique de l'Ouest | 18 | 15,1 % |
| Afrique de l'Est | 11 | 9,2 % |
| Afrique centrale | 5 | 4,2 % |
| Océan Indien | 5 | 4,2 % |

## 8. Répartition sectorielle

| Secteur | Fiches | Part |
|---|---|---|
| Finance / Banque | 18 | 15,1 % |
| Gouvernement / Administration | 17 | 14,3 % |
| Services professionnels / Business | 12 | 10,1 % |
| Industrie / Fabrication | 11 | 9,2 % |
| Santé / Médical | 10 | 8,4 % |
| Technologie / IT | 9 | 7,6 % |
| Éducation / Université | 7 | 5,9 % |
| Commerce / E-commerce | 7 | 5,9 % |
| Télécommunications | 5 | 4,2 % |
| Énergie / Services publics | 4 | 3,4 % |
| Médias / Divertissement | 3 | 2,5 % |
| Agriculture / Agro-industrie | 3 | 2,5 % |
| Transport / Logistique | 3 | 2,5 % |
| Aviation | 3 | 2,5 % |
| Eau / Services publics | 2 | 1,7 % |
| Juridique / Justice | 2 | 1,7 % |
| Construction / Immobilier | 1 | 0,8 % |
| Défense / Sécurité | 1 | 0,8 % |
| Mines / Industries extractives | 1 | 0,8 % |

## 9. Acteurs / groupes

| Acteur / Groupe | Fiches | Part |
|---|---|---|
| Unknown | 18 | 15,1 % |
| lockbit3 | 17 | 14,3 % |
| ransomhub | 12 | 10,1 % |
| killsec | 10 | 8,4 % |
| hunters | 8 | 6,7 % |
| spacebears | 5 | 4,2 % |
| arcusmedia | 4 | 3,4 % |
| blacksuit | 3 | 2,5 % |
| darkvault | 3 | 2,5 % |
| sarcoma | 3 | 2,5 % |
| FunkSec | 3 | 2,5 % |
| incransom | 2 | 1,7 % |
| madliberator | 2 | 1,7 % |
| ransomhouse | 2 | 1,7 % |
| meow | 2 | 1,7 % |
| raworld | 2 | 1,7 % |
| moneymessage | 2 | 1,7 % |
| Sentap | 2 | 1,7 % |
| cnHunter | 1 | 0,8 % |
| medusa | 1 | 0,8 % |
| dragonforce | 1 | 0,8 % |
| EgyptLeaks | 1 | 0,8 % |
| Pedi | 1 | 0,8 % |
| eldorado | 1 | 0,8 % |
| cactus | 1 | 0,8 % |

`Unknown` correspond à l'absence d'attribution. ACAO est attribué au compte `vjvjvj` pour la publication initiale observée ; Satanic est le compte de publication pour Misr Pharmacies.

## 10. Maturité des preuves

| Position de preuve | Fiches | Part |
|---|---|---|
| Claim - Unverified | 86 | 72,3 % |
| Confirmed | 15 | 12,6 % |
| Claim - Data Sample Published | 15 | 12,6 % |
| Corroborated | 2 | 1,7 % |
| Attempted | 1 | 0,8 % |

### Confiance

| Confiance | Fiches | Part |
|---|---|---|
| Low | 84 | 70,6 % |
| Very High | 16 | 13,4 % |
| Medium | 13 | 10,9 % |
| High | 6 | 5,0 % |

### Impact

| Impact | Fiches | Part |
|---|---|---|
| Level 3 | 54 | 45,4 % |
| Level 2 | 47 | 39,5 % |
| Level 4 | 18 | 15,1 % |

## 11. Étude comparative S1 vs S2

| Indicateur | S1 2024 | S2 2024 | Évolution |
|---|---|---|---|
| Total | 45 | 74 | +29 (+64,4 %) |
| Ransomware | 34 | 57 | +23 (+67,6 %) |
| Data Leak | 4 | 9 | +5 (+125,0 %) |
| Access Sale | 1 | 3 | +2 (+200,0 %) |
| DDoS | 2 | 0 | -2 (-100,0 %) |
| Defacement | 0 | 1 | +1 (nouveau) |
| Account Takeover | 0 | 0 | Stable |
| System Intrusion | 3 | 4 | +1 (+33,3 %) |
| Malware | 0 | 0 | Stable |
| Operational Fraud | 1 | 0 | -1 (-100,0 %) |

Le **S1 compte 45 incidents** et le **S2 74**, soit **+29 (+64,4 %)** dans le corpus documenté. Le principal moteur est le ransomware, mais le S2 bénéficie aussi de deux Data Leak supplémentaires désormais correctement intégrés : ACAO en juillet et Misr Pharmacies en décembre. Cette comparaison mesure le corpus, pas un taux exhaustif de compromission.

## 12. Analyse CTI par type

### Ransomware - 91
La majorité des fiches ransomware provient de publications d'acteurs. Les confirmations publiques fortes restent une minorité ; la présence sur un leak site n'établit pas systématiquement le chiffrement.

### Data Leak - 13
Le total intègre désormais ACAO et Misr Pharmacies. ACAO est `Corroborated` grâce à plusieurs publications et échantillons cohérents. Misr Pharmacies reste `Claim - Unverified` car le dump annoncé n'est plus disponible pour validation indépendante. Les vieux datasets republiés sont exclus du millésime.

### System Intrusion - 7
Cette catégorie évite de forcer Eneo, Malawi Passport, GTBank, EmploiPartner, CNE Mozambique et d'autres dossiers dans ransomware/data leak lorsque la preuve ne le permet pas.

### Access Sale - 4
Une offre d'accès ne prouve ni validité, ni utilisation, ni exfiltration.

### DDoS - 2
Central Bank of Libya et Moneyweb sont comptés comme campagnes confirmées.

### Defacement - 1 / Operational Fraud - 1
NBS Nigeria et DPWI restent les seuls cas de leurs catégories.

## 13. Republications historiques et doublons

**17 découvertes historiques/cross-year** restent archivées hors statistiques. Le doublon eTrade/eRIS de mars reste exclu. ACAO ne figure plus dans les pending : sa chronologie 2024 est suffisamment établie pour le rattacher à juillet.

## 14. Intelligence gaps

- vecteurs d'accès initial souvent inconnus ;
- date technique exacte de compromission non publique pour plusieurs claims ;
- volumes revendiqués rarement vérifiables intégralement ;
- distinction entre republication, réexploitation et seconde intrusion parfois impossible sans comparaison forensique ;
- conclusions DFIR publiques limitées.

## 15. Recommandations

### Organisations
MFA résistante au phishing, PAM, segmentation, sauvegardes immuables, durcissement des interfaces publiques et plans de réponse à incident.

### SOC
Centraliser EDR, IAM, VPN, WAF, DNS, proxy, cloud et logs applicatifs ; détecter exports massifs, archives inhabituelles, changements privilégiés et transferts sortants.

### CTI
Préserver distinctement incident, publication initiale, repost, découverte et confirmation ; suivre les datasets historiques comme risque d'exposition sans les recompter comme nouvelles attaques.

## 16. Conclusion

La baseline AFRINTEL 2024 corrigée contient **119 incidents canoniques dans 30 pays**. La résolution d'ACAO et de Misr Pharmacies améliore la chronologie sans transformer les éléments inconnus en faits.

**AFRINTEL** - TLP:CLEAR
