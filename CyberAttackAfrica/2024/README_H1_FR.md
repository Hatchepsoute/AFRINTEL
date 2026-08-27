# Rapport CTI semestriel AFRINTEL - Cybermenaces en Afrique - S1 2024

## 1. Synthèse exécutive

Sur janvier-juin 2024, AFRINTEL retient **46 incidents canoniques dans 16 pays**. Le ransomware représente **34 fiches (73,9 %)**, devant Data Leak **5 (10,9 %)**. Les pays les plus représentés sont **Afrique du Sud (18)**, **Égypte (7)**, puis plusieurs pays à 2 fiches. L'ajout rétrospectif concerne la Data Leak de Daeyang University au Malawi, publiée le 25 janvier.

### 1.1 Comparaison S1 vs S2 2024

Le S1 constitue la première moitié de la baseline 2024 corrigée ; la comparaison S1/S2 est présentée dans le rapport S2 et dans le rapport annuel.

## 2. Méthodologie

Même taxonomie, même politique de dates et mêmes règles de preuve que les rapports mensuels. Les reposts historiques et doublons sont exclus des statistiques canoniques mais conservés dans des registres séparés.

## 3. Évolution mensuelle

| Mois | Total | Ransomware | Data Leak | Access Sale | DDoS | Defacement | Account Takeover | System Intrusion | Malware | Operational Fraud |
|---|---|---|---|---|---|---|---|---|---|---|
| Janvier | 8 | 4 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 |
| Février | 8 | 6 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Mars | 9 | 8 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Avril | 9 | 5 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| Mai | 9 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Juin | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## 4. Types d'incident

| Type | Fiches | Part |
|---|---|---|
| Ransomware | 34 | 73,9 % |
| Data Leak | 5 | 10,9 % |
| Access Sale | 1 | 2,2 % |
| DDoS | 2 | 4,3 % |
| Defacement | 0 | 0,0 % |
| Account Takeover | 0 | 0,0 % |
| System Intrusion | 3 | 6,5 % |
| Malware | 0 | 0,0 % |
| Operational Fraud | 1 | 2,2 % |

```mermaid
pie showData
    title Types d'incident - S1 2024
    "Ransomware" : 34
    "Data Leak" : 5
    "Access Sale" : 1
    "DDoS" : 2
    "System Intrusion" : 3
    "Operational Fraud" : 1
```

## 5. Répartition géographique

| Pays | Fiches | Part |
|---|---|---|
| Afrique du Sud | 18 | 39,1 % |
| Égypte | 7 | 15,2 % |
| Cameroun | 2 | 4,3 % |
| Tunisie | 2 | 4,3 % |
| Côte d'Ivoire | 2 | 4,3 % |
| Namibie | 2 | 4,3 % |
| Maroc | 2 | 4,3 % |
| Libye | 2 | 4,3 % |
| Angola | 1 | 2,2 % |
| Malawi | 2 | 4,3 % |
| Cabo Verde | 1 | 2,2 % |
| Seychelles | 1 | 2,2 % |
| Burkina Faso | 1 | 2,2 % |
| Nigeria | 1 | 2,2 % |
| Sénégal | 1 | 2,2 % |
| Congo | 1 | 2,2 % |

## 6. Régions

| Région | Fiches | Part |
|---|---|---|
| Afrique australe | 23 | 50,0 % |
| Afrique du Nord | 13 | 28,3 % |
| Afrique de l'Ouest | 6 | 13,0 % |
| Afrique centrale | 3 | 6,5 % |
| Océan Indien | 1 | 2,2 % |

## 7. Secteurs

| Secteur | Fiches | Part |
|---|---|---|
| Gouvernement / Administration | 8 | 17,4 % |
| Finance / Banque | 8 | 17,4 % |
| Services professionnels / Business | 4 | 8,7 % |
| Industrie / Fabrication | 4 | 8,7 % |
| Santé / Médical | 4 | 8,7 % |
| Énergie / Services publics | 3 | 6,5 % |
| Technologie / IT | 3 | 6,5 % |
| Médias / Divertissement | 3 | 6,5 % |
| Éducation / Université | 3 | 6,5 % |
| Commerce / E-commerce | 2 | 4,3 % |
| Eau / Services publics | 1 | 2,2 % |
| Construction / Immobilier | 1 | 2,2 % |
| Agriculture / Agro-industrie | 1 | 2,2 % |
| Juridique / Justice | 1 | 2,2 % |

## 8. Acteurs / groupes

| Acteur / Groupe | Fiches |
|---|---|
| lockbit3 | 14 |
| Unknown | 10 |
| hunters | 4 |
| ransomhub | 4 |
| spacebears | 2 |
| arcusmedia | 2 |
| cnHunter | 1 |
| medusa | 1 |
| X0Frankenstein | 1 |

## 9. Maturité des preuves

| Preuve | Fiches | Part |
|---|---|---|
| Claim - Unverified | 32 | 69,6 % |
| Confirmed | 10 | 21,7 % |
| Claim - Data Sample Published | 4 | 8,7 % |

## 10. Analyse CTI

- **Ransomware : 34**. Une présence sur leak site ne prouve pas toujours le chiffrement.
- **Data Leak : 5**. Le total inclut désormais Daeyang University (Malawi), dont l'échantillon SQL visible soutient la classification Data Leak ; les 224k+ lignes revendiquées restent non vérifiées.
- **System Intrusion : 3**. Utilisé lorsque l'accès/intrusion est mieux soutenu qu'un ransomware ou une fuite.
- **Access Sale : 1**, **DDoS : 2**, **Defacement : 0**, **Operational Fraud : 1**.

## 11. Principaux constats

- top secteurs : Gouvernement / Administration (8), Finance / Banque (8), Services professionnels / Business (4);
- top acteurs/labels : lockbit3 (14), Unknown (10), hunters (4), ransomhub (4), spacebears (2);
- `Unknown` reste une absence d'attribution ;
- la maturité de preuve doit être lue séparément du type technique.

## 12. Intelligence gaps

Vecteurs initiaux, dates techniques, volumes exacts, exfiltration et conclusions DFIR restent incomplets pour une partie du corpus.

## 13. Recommandations

MFA résistante au phishing, PAM, segmentation, sauvegardes immuables, centralisation des journaux et suivi séparé des reposts historiques.

## 14. Conclusion

Le S1 2024 retient **46 incidents canoniques**.

**AFRINTEL** - TLP:CLEAR
