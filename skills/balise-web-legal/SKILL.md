---
name: balise-web-legal
description: "Auditer et préparer les informations juridiques d'un site, d'une application ou d'un service numérique multi-juridiction : mentions légales, politique de confidentialité, information au point de collecte, politique et interface cookies, informations e-commerce et plan d'implémentation. Utiliser en priorité pour les juridictions d'Afrique francophone — Bénin, Burkina Faso, Cameroun, RCA, Tchad, Comores, Congo, Côte d'Ivoire, Gabon, Guinée, Mali, Niger, RDC, Sénégal et Togo — et pour leurs superpositions avec le Ghana, la France/UE (RGPD) ou le Canada/Québec."
---

# Conformité juridique des sites

Travailler comme assistant de recherche, d'audit et de rédaction. Partir du produit et des traitements réels, puis déterminer les juridictions et documents requis. Une page juridique ne prouve jamais, à elle seule, la conformité opérationnelle.

## Principes obligatoires

1. Ne pas appliquer le RGPD, la CNIL française, la loi québécoise ou une durée standard par automatisme.
2. Distinguer l'établissement de l'éditeur, les marchés ciblés, les personnes concernées, les lieux de traitement, les prestataires, les transferts et les critères extraterritoriaux de chaque loi.
3. Vérifier en ligne le texte en vigueur, ses modifications, sa publication, son entrée en vigueur, ses décrets et les formalités de l'autorité compétente.
4. Ne jamais inventer identité, forme, RCCM, IFU, capital, représentant, récépissé, autorisation, hébergeur, prestataire, cookie, finalité, base juridique, durée ou transfert.
5. Séparer : fait observé, information fournie, exigence sourcée, interprétation, recommandation et élément non vérifié.
6. Ne pas déclarer un site « conforme » sans preuve sur les traitements, contrats, mesures, formalités et comportement réel de l'interface.

## Références à lire

- Lire [applicability-router.md](references/applicability-router.md) au début de chaque mission.
- Lire [audit-and-evidence.md](references/audit-and-evidence.md) pour inspecter un produit existant ou cadrer un produit en construction.
- Lire [document-set.md](references/document-set.md) pour déterminer les pages et informations nécessaires.
- Lire [privacy-notice.md](references/privacy-notice.md) avant de rédiger ou réviser une politique de confidentialité.
- Lire [cookies-and-interface.md](references/cookies-and-interface.md) pour les traceurs, le bandeau et la gestion des préférences.
- Lire [legal-notices-ecommerce.md](references/legal-notices-ecommerce.md) pour l'identification de l'éditeur et les informations e-commerce.
- Lire le profil approprié : [jurisdictions-west-africa.md](references/jurisdictions-west-africa.md), [jurisdictions-central-africa.md](references/jurisdictions-central-africa.md), [jurisdictions-comoros.md](references/jurisdictions-comoros.md), [jurisdictions-eu-france.md](references/jurisdictions-eu-france.md) ou [international-overlays.md](references/international-overlays.md).
- Lire [verification-and-delivery.md](references/verification-and-delivery.md) avant toute livraison.

## Workflow

### 1. Cadrer

Relever le propriétaire du service, les entités impliquées, le type de produit, les pays d'établissement et de ciblage, les catégories d'utilisateurs, le secteur, les langues, les fonctions et le stade du projet. Demander seulement les informations susceptibles de changer le droit applicable ou le contenu.

### 2. Auditer

Inventorier pages, formulaires, comptes, paiements, messages, fichiers, journaux, traceurs, stockage local, SDK, contenus embarqués, prestataires, hébergement, transferts et paramètres de consentement. Marquer chaque élément `observé`, `fourni`, `déduit à confirmer` ou `inconnu`.

### 3. Router

Produire une matrice par juridiction et par matière : données personnelles, communications/traceurs, identité de l'éditeur, commerce électronique, consommation, secteur réglementé et paiements. Utiliser le skill compagnon `balise-ohada` s'il est disponible pour les questions nationales ou OHADA qui dépassent les pages du site. À défaut, isoler ces questions, effectuer la recherche officielle nécessaire et signaler les points qui exigent une validation locale. Si le droit UE ou français est applicable, traiter directement ce régime avec [jurisdictions-eu-france.md](references/jurisdictions-eu-france.md), sans remplacer les obligations africaines également applicables.

### 4. Définir le jeu documentaire

Décider séparément si le produit requiert : mentions légales, politique de confidentialité, notices courtes au point de collecte, politique cookies, interface de consentement, CGU, CGV, informations précontractuelles, procédure d'exercice des droits ou informations d'application mobile.

### 5. Rédiger

Rédiger à partir des faits vérifiés et des exigences sourcées. Utiliser des marqueurs `[À CONFIRMER]` pour les données manquantes qui empêchent la finalisation. Ne pas transformer une formalité à accomplir en numéro fictif. Préserver les variantes nationales lorsqu'une fusion serait trompeuse.

### 6. Contrôler l'implémentation

Vérifier que les liens sont accessibles avant la collecte, que les notices courtes renvoient au bon document, que l'interface respecte les choix, que les traceurs observés correspondent au tableau publié et que les versions linguistiques sont cohérentes.

### 7. Livrer

Livrer les projets, la matrice des sources, le registre des informations manquantes et le plan d'implémentation. Indiquer la date de vérification et les limites. Recommander une validation locale lorsque le texte officiel est inaccessible, la formalité incertaine, le risque élevé ou plusieurs lois entrent en conflit.
