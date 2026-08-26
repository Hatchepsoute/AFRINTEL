# UNC6040 — Étude de cas : Vishing OAuth Salesforce & Vol de données SaaS

👉🏾 [**English version available here**](./case_study.md)

**AFRINTEL Threat Actor Intelligence**

- **Acteur / Groupe :** UNC6040
- **Type de menace :** Vol de données SaaS / Extorsion
- **Vecteur principal :** Vishing / Ingénierie sociale
- **Environnement ciblé :** Salesforce / SaaS
- **Motivation principale :** Financière
- **Période documentée :** 2025–2026
- **Source principale :** Google Threat Intelligence Group / Mandiant
- **Niveau de confiance :** Élevé
- **Dernière mise à jour AFRINTEL :** 26 août 2026

---

## 1. Synthèse

UNC6040 est un cluster financièrement motivé spécialisé dans les campagnes de vishing visant les environnements Salesforce.

Les opérateurs se font passer pour le support informatique et persuadent les utilisateurs d'autoriser une Connected App malveillante dans leur instance Salesforce.

L'application observée est fréquemment une version modifiée ou usurpée de Salesforce Data Loader.

Cette méthode permet à l'attaquant d'accéder directement aux données Salesforce via les API SaaS, sans nécessiter une compromission initiale du réseau interne traditionnel.

> **Qualification AFRINTEL :**  
> AFRINTEL distingue les accès SaaS obtenus par ingénierie sociale, les autorisations OAuth accordées par l'utilisateur et les compromissions techniques directes. Une autorisation OAuth obtenue par manipulation ne signifie pas que le périmètre réseau principal a été compromis.

---

## 2. Accès initial

### T1566.004 — Spearphishing Voice

L'acteur contacte la victime par téléphone en se faisant passer pour un membre du support informatique.

La victime est guidée vers la page de configuration des Connected Apps Salesforce et invitée à autoriser une application contrôlée par l'attaquant.

**Preuve :** Observé  
**Confiance :** Élevée

---

## 3. Autorisation OAuth

### T1528 — Steal Application Access Token

L'autorisation de l'application fournit à l'acteur un accès OAuth permettant d'interagir avec les ressources Salesforce au nom de l'utilisateur.

Dans ce scénario, le token n'est pas nécessairement obtenu par compromission technique du poste utilisateur : l'accès est accordé à la suite de la manipulation de la victime.

**Preuve :** Observé  
**Confiance :** Élevée

---

## 4. Persistance SaaS

### T1671 — Cloud Application Integration

L'application OAuth autorisée peut permettre à l'acteur de conserver un accès aux données SaaS à travers l'intégration cloud.

Les refresh tokens peuvent permettre l'obtention de nouveaux access tokens sans imposer une nouvelle authentification interactive de l'utilisateur.

> `T1098.003` ne doit pas être utilisé ici par défaut : cette technique correspond à l'ajout de rôles ou permissions cloud, ce qui n'est pas le comportement principal observé dans cette campagne.

**Preuve :** Observé / Évalué  
**Confiance :** Élevée

---

## 5. Utilisation des tokens

### T1550.001 — Application Access Token

Une fois l'accès OAuth obtenu, l'acteur utilise l'application et les tokens associés pour effectuer des appels API Salesforce sans passer par le processus classique d'authentification utilisateur.

**Preuve :** Observé  
**Confiance :** Élevée

---

## 6. Collection et exfiltration

UNC6040 a été observé utilisant Salesforce Data Loader pour extraire rapidement des volumes importants de données.

Les activités peuvent inclure :

- requêtes API ;
- Bulk API ;
- exports de rapports ;
- récupération de contacts et comptes ;
- extraction de données sensibles présentes dans le CRM.

### Sources de télémétrie Salesforce pertinentes

- `ApiEventStream`
- `BulkApiResultEvent`
- `ReportEventStream`
- `ListViewEventStream`
- `FileEvent`
- `LoginEvent`

**Preuve :** Observé  
**Confiance :** Élevée

---

## 7. Mouvement latéral SaaS

Après l'accès à Salesforce, UNC6040 a également été observé utilisant des identifiants récupérés par vishing ou credential harvesting pour accéder à d'autres plateformes cloud, notamment :

- Okta ;
- Microsoft 365.

Cela représente un mouvement latéral entre services SaaS plutôt qu'un mouvement latéral Windows classique.

**Preuve :** Rapporté / Observé selon les incidents  
**Confiance :** Élevée

---

## 8. Infrastructure observée

UNC6040 a notamment utilisé des adresses IP associées à des services VPN pour accéder aux environnements Salesforce et procéder aux opérations d'extraction.

L'infrastructure de phishing a également été utilisée pour héberger des pages imitant des services d'identité comme Okta.

> Les IoC réseau doivent être contextualisés par date et incident. Une adresse IP de VPN commercial n'est pas malveillante en elle-même.

---

## 9. Artefacts de détection

| Signal | Contexte |
|---|---|
| `LoginType = Remote Access 2.0` | Authentification OAuth Salesforce |
| Connected App inconnue | Application non approuvée ou nouvellement autorisée |
| Nouvel OAuth grant | Autorisation potentiellement malveillante |
| Scopes `api`, `refresh_token`, `offline_access` | Accès étendu / durable |
| Bulk API inhabituel | Extraction massive |
| Nombre élevé de `Query` / `QueryMore` | Collecte API |
| Connexion depuis VPN / infrastructure inhabituelle | Signal contextuel |
| Export massif après OAuth | Chaîne OAuth → exfiltration |

---

## 10. Chaîne analytique

```text
Vishing
   │
   ▼
Usurpation du support IT
   │
   ▼
Autorisation d'une Connected App
   │
   ▼
OAuth Access / Refresh Token
   │
   ├── T1671
   ├── T1528
   └── T1550.001
   │
   ▼
Salesforce API / Data Loader
   │
   ▼
Collecte massive de données
   │
   ▼
Exfiltration
   │
   ▼
Pivot SaaS possible → Okta / Microsoft 365
   │
   ▼
Extorsion
```

---

## 11. Évaluation AFRINTEL

Cette campagne illustre une évolution importante des chaînes d'attaque : la compromission du périmètre réseau traditionnel n'est plus nécessaire pour provoquer une fuite majeure.

Une autorisation OAuth légitime obtenue par ingénierie sociale peut fournir directement un accès à des données SaaS sensibles.

Pour le SOC, la détection doit donc inclure la télémétrie d'identité, OAuth, Connected Apps et API SaaS en plus des journaux endpoint et réseau.

AFRINTEL distingue systématiquement :

- les autorisations OAuth obtenues par manipulation ;
- les tokens effectivement observés comme compromis ;
- les appels API anormaux ;
- l'exfiltration confirmée ;
- les pivots vers d'autres services SaaS ;
- les relations uniquement évaluées ou inférées.

---

## 12. Sources

- Google Threat Intelligence Group / Mandiant — *The Cost of a Call: From Voice Phishing to Data Extortion*
- Mandiant — *Cybercrime Observations from the Frontlines: UNC6040 Proactive Hardening Recommendations*
- MITRE ATT&CK — T1566.004
- MITRE ATT&CK — T1528
- MITRE ATT&CK — T1550.001
- MITRE ATT&CK — T1671

---

**AFRINTEL — African Cyber Threat Intelligence**
