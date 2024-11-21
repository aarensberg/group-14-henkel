# Analyse de l'Impact des Investissements et des Performances Commerciales de Henkel

Ce dépôt contient l'analyse complète des données de ventes et des investissements marketing de Henkel dans les enseignes Leroy Merlin et Bricomarché. Il inclut des scripts Python pour explorer les relations entre les investissements et les ventes, identifier des clusters de points de vente, et générer des visualisations des performances.

## 📂 Structure du Projet

- `investment_impact.py`  
  Analyse l’impact des investissements marketing sur les ventes à l’aide d’un algorithme de régression linéaire multiple.  
  **Principales sorties :**  
  - Coefficients d'impact des investissements marketing.  
  - Prédictions de ventes basées sur différents niveaux d’investissements.

- `map.py`  
  Utilise le package `pgeocode` pour géocoder les points de vente Bricomarché et Leroy Merlin présents dans les datasets.  
  **Principales sorties :**  
  - Coordonnées géographiques des points de vente.  
  - Cartographie interactive pour visualiser la répartition géographique des magasins.

- `performance_analysis.py`  
  Utilise un algorithme de clustering (`K-Means`) pour regrouper les points de vente en fonction de leurs performances.  
  **Principales sorties :**  
  - Segmentation des magasins selon leurs caractéristiques (ventes, investissements, ROI).  
  - Graphiques pour explorer les groupes identifiés.

- `roi_analysis.py`  
  Génère des visualisations pour analyser le retour sur investissement (ROI) des actions marketing dans les points de vente.  
  **Principales sorties :**  
  - Barres comparatives ROI par enseigne et par rayon.  
  - Identification des points de vente les plus performants et sous-performants.

- `sales_evolution_analysis.py`  
  Analyse l'évolution des ventes de Henkel dans les points de vente des deux enseignes sur plusieurs périodes.  
  **Principales sorties :**  
  - Graphiques d’évolution mensuelle et annuelle des ventes.  
  - Analyse des tendances par famille de produits et région.

## ⚙️ Prérequis

Assurez-vous d'avoir les outils suivants installés :  
- Python 3.7 ou supérieur.  
- Les bibliothèques Python suivantes :  
```bash
pip install pandas matplotlib seaborn scikit-learn pgeocode
```

## 🚀 Utilisation

	1.	Clonez le dépôt :
 
```bash
git clone https://github.com/votre-utilisateur/henkel-performance-analysis.git
cd henkel-performance-analysis
```

	2.	Exécutez les scripts selon vos besoins :
 
	•	Analyse de l’impact des investissements :
```bash
python investment_impact.py
```

	•	Géolocalisation et cartographie :
```bash
python map.py
```

	•	Analyse des performances avec clustering :
```bash
python performance_analysis.py
```

	•	Analyse du retour sur investissement :
```bash
python roi_analysis.py
```

	•	Analyse de l’évolution des ventes :
```bash
python sales_evolution_analysis.py
```

## 📊 Résultats et Insights

Ce projet fournit :

	•	Une compréhension approfondie des relations entre investissements marketing et performances des ventes.
	•	Une segmentation des points de vente pour une allocation optimisée des ressources.
	•	Des visualisations claires pour appuyer des décisions stratégiques.

## 🗂️ Organisation des Données

Les datasets analysés comprennent des informations sur :

	•	Les ventes annuelles par point de vente et par catégorie.
	•	Les investissements marketing par type et modalité.
	•	Les visites en magasin et leurs évolutions.

🌍 À propos

Ce projet a été réalisé pour présenter une analyse stratégique des performances commerciales de Henkel dans des enseignes de bricolage. Les scripts n'ont pas été développés pour être extensibles et réutilisables car les données de ventes et des investissements marketing de Henkel ne peuvent pas être fournis avec.

Pour toute question ou suggestion, n’hésitez pas à ouvrir une issue dans ce dépôt.

Auteur : Alessandro Arensberg
Licence : Ce projet est sous licence MIT.
