# AFRINTEL - Protocole de preuve pour les rapports CTI (FR/EN)

## Positionnement éditorial

Les rapports AFRINTEL sont des analyses CTI post-publication. Ils confrontent les déclarations des acteurs aux pièces rendues accessibles **quand elles existent** : inventaires, aperçus et données divulguées pour les extorsions ransomware ; échantillons structurés et documents pour les fuites de données. La portée des conclusions dépend des éléments effectivement examinés. Les confirmations de victimes, autorités et CERT sont distinguées des revendications.

## Formulation de référence (FR)

> AFRINTEL a procédé à une analyse post-divulgation des éléments accessibles dans les dossiers documentés. Pour les revendications ransomware accompagnées d'une publication de données, l'examen a porté sur les arborescences, aperçus et documents divulgués, afin de caractériser les informations exposées et leurs impacts métiers. Pour les fuites de données, les échantillons disponibles ont été examinés en lecture seule : formats, schémas, champs, dates, cohérence des enregistrements et volumes réellement observés. Les totaux annoncés par les auteurs sont rapprochés des éléments consultés, sans les présenter comme vérifiés lorsqu'ils ne le sont pas. Lorsqu'aucun échantillon n'est accessible, AFRINTEL qualifie la revendication sans conclure à une compromission confirmée.

## Reference wording (EN)

> AFRINTEL performed post-disclosure analysis of the material available for documented cases. When a ransomware claim was accompanied by released data, analysts reviewed file trees, previews and disclosed documents to assess the information exposed and its business impact. For data leaks, available samples were examined read-only for formats, schemas, fields, dates, record consistency and actual observed counts. Actor-advertised totals were compared with reviewed material, without treating unseen volumes as verified. Where no sample was available, the claim was qualified without asserting a confirmed compromise.

## Choix des verbes

| Source probatoire | Verbes appropriés | À éviter sans corroboration |
|---|---|---|
| Publication seule | « revendique », « annonce », « cite » | « a compromis », « a exfiltré » |
| Aperçu, arborescence | « montre », « indique », « est cohérent avec » | « confirme le volume total » |
| Échantillon étudié | « l'examen montre », « les lignes observées contiennent » | « prouve le dump complet » |
| Publication complète constatée | « les fichiers accessibles ont été publiés » | « tous les fichiers de la victime sont exposés » |
| Communiqué officiel | « l'organisation confirme [fait précis] » | étendre la confirmation à d'autres hypothèses |

## Traçabilité minimum par dossier

Date de publication initiale ; date de découverte AFRINTEL ; acteur ou compte publiant ; institution et domaine vérifiés séparément de la compromission ; nature de l'élément examiné ; résultat précis de cet examen ; volume annoncé versus échantillon observé ; statut et niveau de confiance ; points à élucider ; conséquences métier et hypothèses SOC.

**Règle :** affirmer avec précision ce qui a été analysé. Être explicite sur ce qui ne l'a pas été. La crédibilité ne nécessite ni surinterprétation ni accumulation de précautions de langage.
