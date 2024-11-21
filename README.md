# Analyse de l'Impact des Investissements et des Performances Commerciales de Henkel

Ce dépôt contient les scripts développés pour analyser les données de ventes et les investissements marketing de Henkel dans les enseignes Leroy Merlin et Bricomarché.  
⚠️ **Important :** Les datasets utilisés pour cette analyse sont confidentiels et ne sont pas inclus dans ce dépôt. Seuls les scripts sont fournis.

## 📂 Structure du Projet

- **`investment_impact.py`**  
  Implémente une régression linéaire multiple pour évaluer l'impact des investissements marketing sur les ventes.  
  **Objectif principal :** Identifier les facteurs d’investissement ayant le plus d’impact sur les performances commerciales.

- **`map.py`**  
  Utilise le package `pgeocode` pour géocoder les points de vente Bricomarché et Leroy Merlin.  
  **Objectif principal :** Fournir une représentation géographique des points de vente pour des analyses spatiales.

- **`performance_analysis.py`**  
  Applique un clustering (K-Means) pour regrouper les points de vente en fonction de leurs performances.  
  **Objectif principal :** Identifier des segments de magasins homogènes pour guider les décisions stratégiques.

- **`roi_analysis.py`**  
  Analyse le retour sur investissement (ROI) des actions marketing via des visualisations interactives.  
  **Objectif principal :** Identifier les points de vente les plus rentables et les zones d'amélioration.

- **`sales_evolution_analysis.py`**  
  Génère des visualisations pour explorer l'évolution des ventes sur plusieurs périodes.  
  **Objectif principal :** Comprendre les tendances de ventes par famille de produits, point de vente et région.

## 🚫 Datasets Confidentiels

Les scripts de ce dépôt nécessitent des datasets contenant :  
- Les ventes annuelles par point de vente.  
- Les budgets marketing associés.  
- Les données de visites en magasin.  

Cependant, **ces données sont confidentielles et ne sont pas publiées dans ce dépôt**. Elles sont uniquement accessibles aux collaborateurs autorisés de Henkel.

## 📊 Résultats Attendus

Grâce aux scripts fournis, il est possible de :  
1. **Quantifier l’impact des investissements marketing** sur les ventes.  
2. **Identifier des segments de magasins** performants ou sous-performants.  
3. **Visualiser les tendances** des ventes pour des décisions éclairées.  
4. **Optimiser l'allocation des ressources** pour maximiser le ROI.
