# UNC6040 - Vishing OAuth Salesforce & vol de données SaaS

👉🏾 [**English version**](./case_study.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Cluster :** UNC6040
- **Type de menace :** Vol de données SaaS / précurseur d'extorsion
- **Vecteur principal :** Vishing / ingénierie sociale
- **Environnement ciblé :** Salesforce et services SaaS connectés
- **Motivation :** Financière
- **Activité suivie :** 2025-2026
- **Preuves techniques utilisées ici :** publications GTIG / Mandiant de 2025
- **Statut :** Surveillance active
- **Dernière mise à jour :** 26 août 2026

---

## 1. Synthèse

UNC6040 est un cluster financièrement motivé suivi par Google Threat Intelligence Group. Ses opérateurs se font passer pour le support informatique lors d'appels téléphoniques et poussent les utilisateurs à effectuer des actions qui donnent accès à Salesforce.

Un scénario fréquent consiste à faire autoriser une Connected App Salesforce malveillante. Les premières campagnes utilisaient souvent une version modifiée ou usurpée de Salesforce Data Loader. GTIG a ensuite observé un passage vers des applications personnalisées, généralement des scripts Python, qui remplissent une fonction de collecte similaire.

Le point important est que l'attaquant n'a pas besoin d'exploiter une vulnérabilité Salesforce. L'accès repose sur la manipulation de l'utilisateur et l'abus de mécanismes SaaS légitimes : autorisation d'application, OAuth et API.

AFRINTEL distingue l'intrusion initiale UNC6040 des activités d'extorsion ultérieures. GTIG suit ce second cluster sous le nom **UNC6240**, qui a revendiqué le nom **ShinyHunters** dans ses échanges avec des victimes.

---

## 2. Chaîne d'attaque

```text
Vishing / faux support IT
        │
        ▼
L'utilisateur autorise une Connected App malveillante
        │
        ▼
Accès OAuth / application à Salesforce
        │
        ▼
Data Loader ou application personnalisée
        │
        ▼
Collecte massive via API
        │
        ▼
Exfiltration des données Salesforce
        │
        ├── pivot possible vers Okta / Microsoft 365
        │
        ▼
Extorsion ultérieure
        │
        └── suivie séparément par GTIG sous UNC6240
```

---

## 3. Mapping MITRE ATT&CK

| Tactique | Technique | ID | Comportement | Preuve | Portée | Confiance | Provenance |
|---|---|---|---|---|---|---|---|
| Accès initial | Spearphishing Voice | T1566.004 | Les opérateurs se font passer pour le support IT pendant des appels de vishing | Observé | Campagne | Élevée | GTIG / Mandiant |
| Persistance | Cloud Application Integration | T1671 | La victime est poussée à autoriser une Connected App Salesforce malveillante | Observé | Campagne | Élevée | GTIG / Mandiant + MITRE ATT&CK |
| Contexte accès SaaS | Application Access Token | T1550.001 | Les jetons OAuth / applicatifs peuvent être utilisés pour accéder aux ressources SaaS après autorisation | Rapporté / Évalué | Campagne | Moyenne | GTIG / Mandiant + normalisation ATT&CK |

### Note sur T1528

**T1528 - Steal Application Access Token** ne doit pas être attribué automatiquement à l'étape d'autorisation. Dans le scénario principal UNC6040, la victime est manipulée pour autoriser l'application. T1528 ne doit être utilisé que lorsqu'il existe une preuve qu'un jeton d'accès applicatif a réellement été volé.

Cette distinction évite de présenter tout abus OAuth comme un vol de token.

---

## 4. Collection et exfiltration

UNC6040 a été observé en train d'extraire rapidement des données Salesforce après l'obtention de l'accès.

Les méthodes rapportées comprennent :

- Salesforce Data Loader ;
- applications personnalisées, notamment des outils Python ;
- requêtes REST / API ;
- activité Bulk API ;
- exports de rapports et de listes ;
- téléchargement massif de fichiers ou de pièces jointes.

GTIG a également observé des pivots vers d'autres services cloud avec des identifiants récupérés par vishing ou credential harvesting, notamment **Okta** et **Microsoft 365**.

**Preuve :** Observé  
**Portée :** Campagne  
**Confiance :** Élevée  
**Provenance :** GTIG / Mandiant

---

## 5. Infrastructure et schémas d'accès

GTIG indique qu'UNC6040 a principalement utilisé des adresses IP **Mullvad VPN** pour accéder aux environnements Salesforce et exfiltrer les données. Des activités plus récentes ont également utilisé **Tor** pour certaines phases d'ingénierie sociale et de collecte automatisée.

Dans certaines investigations, l'infrastructure de phishing hébergeait aussi de fausses pages Okta servant à récupérer des identifiants ou des codes MFA.

> Une adresse VPN ou Tor est un élément de contexte. Elle ne constitue pas, à elle seule, une preuve d'attribution.

---

## 6. Pistes de détection

Signaux Salesforce utiles :

| Signal | Pourquoi le surveiller |
|---|---|
| `LoginType = Remote Access 2.0` | Authentification OAuth / Connected App |
| Nouvelle Connected App inconnue | Intégration potentiellement malveillante |
| Scopes larges `api`, `refresh_token`, `offline_access` | Accès API étendu ou durable |
| Volume élevé de `Query`, `QueryMore`, `QueryAll` | Collecte automatisée possible |
| Valeurs élevées de `RowsProcessed` / `RecordCount` | Extraction en masse possible |
| Téléchargements `BulkApiResultEvent` | Signal d'exfiltration via Bulk API |
| Exports massifs de rapports / listes | Collecte CRM possible |
| Téléchargement massif de fichiers / pièces jointes | Vol de données possible |
| OAuth suivi rapidement d'un export API | Corrélation à forte valeur |
| OAuth Salesforce puis connexion Okta/M365 depuis la même IP à risque | Signal de pivot inter-SaaS |

Télémétrie utile :

- `LoginEvent` / `LoginEventStream` ;
- `Setup Audit Trail` ;
- `PermissionSetEvent` ;
- `ApiEvent` / `ApiEventStream` ;
- `BulkApiResultEvent` ;
- `ReportEvent` / `ReportEventStream` ;
- `ListViewEvent` / `ListViewEventStream` ;
- `FileEvent` / `FileEventStore` ;
- `ApiAnomalyEvent` ;
- `ReportAnomalyEvent`.

Ce sont des pistes de Threat Hunting et de détection. Leur présence ne prouve pas, à elle seule, une activité UNC6040.

---

## 7. Limite d'attribution

UNC6040 partage certaines méthodes d'ingénierie sociale avec d'autres acteurs financièrement motivés, notamment des groupes liés à l'écosystème plus large **The Com**. La ressemblance des techniques de vishing ou le ciblage d'Okta ne suffit pas à fusionner ces acteurs.

AFRINTEL garde donc séparés :

- UNC6040 - vishing Salesforce et vol de données ;
- UNC6240 - activité d'extorsion ultérieure suivie par GTIG ;
- UNC3944 / Scattered Spider - cluster distinct avec des techniques sociales parfois proches.

**Évaluation :** ces recouvrements sont utiles pour le hunting, mais ne constituent pas une preuve directe d'attribution.

---

## 8. Lacunes de renseignement

Pour une victime précise, il faut confirmer avant toute attribution au niveau victime :

- le nom et le client ID de la Connected App ;
- les scopes OAuth accordés ;
- le compte ayant autorisé l'application ;
- l'IP / ASN source et la chronologie de session ;
- les appels API et les volumes de données ;
- si des tokens ont réellement été volés ou simplement émis après autorisation ;
- si d'autres plateformes SaaS ont été consultées ;
- si l'extorsion ultérieure peut être reliée aux mêmes opérateurs.

---

## 9. Sources

- Google Threat Intelligence Group - *The Cost of a Call: From Voice Phishing to Data Extortion*, 4 juin 2025
- Mandiant / Google Threat Intelligence - *UNC6040 Proactive Hardening Recommendations*, 30 septembre 2025
- MITRE ATT&CK - T1566.004 Spearphishing Voice
- MITRE ATT&CK - T1671 Cloud Application Integration / Salesforce Data Exfiltration
- MITRE ATT&CK - T1550.001 Application Access Token

---

**AFRINTEL - African Cyber Threat Intelligence**
