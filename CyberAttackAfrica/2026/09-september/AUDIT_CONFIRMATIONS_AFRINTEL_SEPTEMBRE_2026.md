# AFRINTEL — Audit OSINT des confirmations d'incidents (corpus de septembre 2026)

**Date de vérification :** 18 octobre 2026  
**Périmètre :** 41 fiches FR/EN du corpus AFRINTEL de septembre 2026.  
**Méthode :** distinction entre une reconnaissance officielle, une corroboration institutionnelle/journalistique, la confirmation d'une exposition chez un sous-traitant, et une simple revendication sur un site criminel. La publication d'un échantillon ou sa cohérence documentaire ne prouve pas nécessairement l'intrusion, le chiffrement ou l'exfiltration. L'absence de confirmation publique à cette date n'établit pas l'absence d'incident.

## Bilan

| Catégorie de preuve | Fiches | Interprétation |
|---|---:|---|
| Incident chez l'entité confirmé directement ou corroboré indépendamment | **13** | L'existence d'un incident est documentée ; la qualification, le vecteur et le groupe ne sont pas nécessairement tous établis. |
| Exposition indirecte de données chez un partenaire, sans intrusion démontrée chez l'organisation nommée | **2** | Cas Hollard et Guardrisk, à traiter séparément des compromissions directes. |
| Revendication / indice documentaire sans confirmation indépendante d'une intrusion | **26** | Conserver en *Claim / Unverified* et ne pas comptabiliser comme incident directement confirmé. |
| **Total** | **41** | Plusieurs incidents confirmés se sont déroulés de janvier à août 2026, et non en septembre. |

## Incidents confirmés ou corroborés (13)

| Organisation | Période de l'événement | Élément de confirmation | Portée à ne pas exagérer |
|---|---|---|---|
| Constantia Pharmacy (Afrique du Sud) | Janvier 2026 | [Enquête MyBroadband](https://mybroadband.co.za/news/security/623956-hacker-rescues-south-african-pharmacy-from-cyber-attack.html) sur un chiffrement observé sur un serveur | Enquête journalistique corroborante, non notification formelle de la victime. |
| Land Bank (Afrique du Sud) | Janvier 2026 | [ITWeb](https://www.itweb.co.za/article/land-bank-tightens-security-after-ransomware-attack/raYAyMorlOl7J38N) relate l'attaque et les mesures de remédiation | Date initiale antérieure au corpus septembre. |
| Standard Bank South Africa | Mars 2026 | [Communication officielle de la banque](https://www.standardbank.co.za/southafrica/news-and-media/newsroom/an-important-message-from-standard-bank) | Pas de preuve d'impact sur les fonds ou le cœur transactionnel. |
| Ahmed Al-Kadi Private Hospital (Afrique du Sud) | Avril 2026 | [Notification officielle](https://ahmedalkadi.com/notification-of-data-incident/) | Confirmation d'intrusion et de chiffrement d'une partie de l'environnement. |
| CHPC / supercalculateur Lengau (Afrique du Sud) | Mai 2026 | [ITWeb et investigations institutionnelles](https://www.itweb.co.za/article/cause-of-breach-on-sas-supercomputer-revealed/KPNG878NLeGq4mwD) | Intrusion / interruption HPC, pas ransomware confirmé. |
| MIP Holdings (Afrique du Sud) | Juin 2026 | [Déclaration d'un client, LegalWise](https://www.legalwise.co.za/media-centre/statement-regarding-third-party-cybersecurity-incident) | Incident chez le fournisseur, non nécessairement chez chaque client. |
| SEEG / EDAN (Gabon) | Juin 2026 | [Gouvernement gabonais](https://gouvernement.ga/2026/06/15/systeme-edan-retablissement-confirme-et-dispositif-de-protection-renforce-par-letat/) sur la perturbation de service | Sabotage allégué ; accès externe et exfiltration non établis. |
| MINEFOP (Cameroun) | Juillet 2026 | [Alerte du CIRT national](https://cirt.cm/alerte-de-securite-campagne-antonkill-web-defacement-ciblant-les-institutions-sous-joomla-et-helix3/) | Défacement web, pas compromission de l'ensemble du réseau. |
| Rectron (Afrique du Sud) | Juillet 2026 | [Annonce de marché de Mustek](https://www2.sharenet.co.za/v3/sens_display.php?scode=MST&seq=33&tdate=20260722130100) | Incident reconnu, groupe et exfiltration à qualifier séparément. |
| Site de la présidence kényane | Juillet 2026 | [Information gouvernementale relayée](https://www.aa.com.tr/fr/afrique/kenya-le-site-officiel-de-la-pr%C3%A9sidence-pirat%C3%A9-des-hackers-r%C3%A9clament-une-rancon-en-bitcoin/4002284) | Défacement du site `president.go.ke`, non l'ensemble du SI de l'État. |
| Cartrack South Africa | Août 2026 | [Communication officielle Cartrack](https://cartrack.co.za/platform/resources/news) | Confirmation de ransomware, attribution Dire Wolf non établie par ce seul avis. |
| **RelyComply (Afrique du Sud)** | **Septembre 2026** | [Déclaration officielle du 16 septembre](https://relycomply.com/relycomply-cyber-incident-what-happened-and-what-you-can-do/) | Accès non autorisé via un zero-day de logiciel tiers ; attribution Direwolf et chiffrement non établis. |
| **Ministère de la Défense et des anciens combattants (Namibie)** | **Septembre 2026** | [The Register](https://www.theregister.com/cyber-crime/2026/09/21/ransomhouse-picks-a-fight-with-namibias-defense-establishment/5297816) rapporte la confirmation et l'association à RansomHouse par NAM-CSIRT | Périmètre reconnu : réseau du ministère. Chiffrement, exfiltration et secrets militaires non confirmés. |

## Exposition de données chez des partenaires (2)

| Organisation nommée sur leak site | Situation établie | Source |
|---|---|---|
| **Hollard Insurance Group (Afrique du Sud)** | Données de certains assurés exposées en lien avec l'incident **MIP Holdings** de juin. Hollard indique n'avoir trouvé aucune preuve de compromission de ses propres systèmes. | [Déclaration Hollard relayée par FAnews](https://www.fanews.co.za/article/company-news-results/1/hollard/1301/hollard-statement-regarding-reported-cyber-threat-claims/44724) |
| **Guardrisk (Afrique du Sud)** | Données d'environ **6 000 polices obsèques** concernées chez le gestionnaire tiers **CoverCubed**. Guardrisk nie une compromission de ses propres systèmes. | [Réponse de Guardrisk à MyBroadband, 30 septembre 2026](https://mybroadband.co.za/news/security/669576-momentum-group-company-responds-to-data-breach-claims.html) |

## Revendications non confirmées indépendamment (26)

Medical and Dental Council of Nigeria ; Madinaty (détenteur de données inconnu) ; Centre Atlantique Formation ; Badr University in Cairo ; SEPE Angola ; Apollo 21 ; FCT-IRS Nigeria ; ARCA Unlimited Architects ; AFRICA-TECH (Mali) ; Pharma 5 ; First National Bank ; TikoHUB ; HCCD (Égypte) ; Mecca High Feed Factory ; Seashell Hospital ; VSB Attorneys ; Nile Projects Trading ; La Sultana Hotel Group ; Egyptian Airports Company ; Opérations de support PayPal / Transcom ; Siinqee Bank ; Grupolider ; Air Tanzania ; Armada Credit Bureau ; Majani Insurance Brokers ; BCX / Business Connexion.

**Précision sur Pharma 5 (18 octobre 2026) :** AFRINTEL a reçu deux captures, dont une page lisible de spécifications du service qualité (`DE01 / PG / MQ / 036`, salicylamide). Le fournisseur **MEDILIFE S.R.L.** et son adresse professionnelle sont cohérents avec une fiche publique italienne ; **JQC (Huayin) Pharmaceutical** référence le salicylamide sur son catalogue officiel. Ces recoupements renforcent le **lien documentaire avec la chaîne d’approvisionnement**, mais ne confirment ni une intrusion, ni le chiffrement, ni les **50 Go** annoncés par INC Ransom. La fiche reste donc classée parmi les revendications non confirmées indépendamment. Voir les fiches FR/EN pour la traçabilité SHA-256 et les sources.

**Note sur le niveau de preuve :** Centre Atlantique Formation, SEPE, Apollo 21, ARCA et AFRICA-TECH disposent d'indices ou d'archives analysés par AFRINTEL. Leur classification ci-dessus signifie *absence de confirmation indépendante de l'incident dans les sources publiques examinées*, et non absence de données ou d'indices. Ces preuves doivent continuer d'être distinguées des annonces d'une autorité ou de la victime.

## Règle de classification recommandée

1. **Victim Confirmed / Government Confirmed** : reconnaissance de l'accès non autorisé, du défacement ou d'un incident par l'organisation, un régulateur ou une autorité, ou corroboration journalistique technique suffisamment précise (*Corroborated*).
2. **Third-Party Exposure Confirmed** : données reconnues comme exposées via fournisseur ou partenaire sans intrusion chez l'entité citée.
3. **Claim - Unverified / Data Sample Published** : simple revendication, catalogue OSINT ou contenu d'échantillon n'établissant pas indépendamment l'accès au SI victime.

**Important :** la confirmation de l'accès non autorisé ne signifie pas la confirmation de l'attribution au groupe, du ransomware en tant que chiffrement, du paiement ou du volume annoncé.
