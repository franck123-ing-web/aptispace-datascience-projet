# 📊 Projet Data Science — Prédiction des Prix Immobiliers

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Quarto](https://img.shields.io/badge/Quarto-Report-blue.svg)](https://quarto.org/)
[![Typst](https://img.shields.io/badge/Typst-PDF-black.svg)](https://typst.app/)
[![Scikit-Learn](https://img.shields.io/badge/MachineLearning-ScikitLearn-orange.svg)](https://scikit-learn.org/)

> **Bienvenue dans le portail de notre projet de Data Science appliqué à l’immobilier.**
>
> Ce dépôt contient l’intégralité du pipeline analytique permettant de :
>
> - charger et préparer les données,
> - analyser le marché immobilier,
> - entraîner plusieurs modèles de Machine Learning,
> - prédire automatiquement le prix de maisons,
> - expliquer les décisions du modèle grâce à l’Explainable AI (SHAP),
> - et communiquer les résultats via une application Streamlit interactive.
>
> Toutes les compilations des rapports sont générées automatiquement afin de centraliser les livrables du projet.

---

# 📥 Livrables du Projet

Les différents rapports générés automatiquement sont disponibles dans le dossier :

```text
build/report/
```

| Format | Description | Emplacement |
| :--- | :--- | :--- |
| 📄 Rapport PDF | Rapport scientifique complet compilé avec Typst | `build/report/rapport.pdf` |
| 🌐 Rapport HTML | Rapport interactif Quarto | `build/report/rapport.html` |
| 📝 Rapport Markdown | Version Markdown du rapport | `report/rapport.md` |

---

# 📂 Structure du Projet

```text
├── build/
│   └── report/
│       ├── rapport.html
│       ├── rapport.pdf
│       └── rapport.typ
│
├── data/
│   └── raw/
│       └── train.csv
│
├── notebooks/
│   ├── 01_dataset_loading.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_visualization.ipynb
│   ├── 04_modeling.ipynb
│   ├── 05_feature_engineering.ipynb
│   ├── 06_model_comparison.ipynb
│   ├── 07_hyperparameter_tuning.ipynb
│   └── 08_model_explainability.ipynb
        09_model_evaluation.ipynb
        10_model_communication.ipynb
        eda_housing.ipynb
│
├── report/
│   ├── rapport.qmd
│   └── rapport.md
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🏠 Objectif du Projet

L’objectif principal du projet est de construire un système intelligent capable d’estimer automatiquement le prix d’une maison à partir de ses caractéristiques.

Le modèle prend notamment en compte :

- la surface habitable,
- la qualité générale,
- la taille du sous-sol,
- l’année de construction,
- le nombre de garages,
- et plusieurs variables dérivées créées grâce au Feature Engineering.

Le projet permet également :

- d’analyser les données immobilières,
- d’évaluer les performances des modèles,
- de comprendre les erreurs de prédiction,
- et d’interpréter les décisions prises par l’intelligence artificielle.

---

# 🧠 Technologies Utilisées

## Data Science & Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- SHAP

## Visualisation

- Matplotlib
- Seaborn
- Plotly

## Déploiement & Reporting

- Streamlit
- Quarto
- Typst

---

# 🧹 Pipeline Data Science

Le pipeline complet du projet suit les étapes suivantes :

```text
Chargement des données
        ↓
Nettoyage des données
        ↓
Analyse exploratoire (EDA)
        ↓
Feature Engineering
        ↓
Séparation Train / Test
        ↓
Entraînement des modèles
        ↓
Évaluation des performances
        ↓
Explainable AI (SHAP)
        ↓
Application Streamlit
```

---

# 🤖 Modèles de Machine Learning

Plusieurs modèles ont été étudiés :

- Régression Linéaire
- Decision Tree Regressor
- Random Forest Regressor

Le modèle final retenu est :

## ✅ Random Forest Regressor

Car il offre les meilleures performances sur le dataset immobilier.

---

# 📈 Évaluation du Modèle

Les performances sont évaluées avec plusieurs métriques :

| Métrique | Description |
| :--- | :--- |
| MAE | Erreur moyenne absolue |
| RMSE | Pénalise davantage les grosses erreurs |
| R² Score | Mesure globale de qualité du modèle |

Le projet intègre également :

- un graphique Réel vs Prédiction,
- une analyse des erreurs,
- une interprétation SHAP,
- et des visualisations interactives.

---

# 🧠 Explainable AI (SHAP)

Le projet utilise SHAP afin de comprendre :

- quelles variables influencent le plus le prix,
- pourquoi certaines maisons sont estimées plus cher,
- et comment le modèle prend ses décisions.

Cette étape améliore la transparence et l’interprétabilité du système.

---

# 🚀 Lancer le Projet

## 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 2. Lancer l’application Streamlit

```bash
 streamlit run src/dashboard/app.py
```

---

## 3. Générer le rapport Quarto

Depuis la racine du projet :

```bash
quarto render report/rapport.qmd
```

Les fichiers générés seront disponibles dans :

```text
build/report/
```

---

# 📄 Génération du Rapport PDF

Le rapport PDF est généré automatiquement grâce à :

- Quarto
- Typst

Commande utilisée :

```bash
quarto render report/rapport.qmd --to typst
```

---

# 📚 Dataset Utilisé

Dataset Kaggle :

## House Prices — Advanced Regression Techniques

Ce dataset contient des données réelles de ventes immobilières aux États-Unis.

---

# 👨‍💻 Auteur

- Franck Joel Nzokou

---

# 📖 Bibliographie

- Documentation Scikit-Learn
- Documentation Pandas
- Documentation SHAP
- Documentation Streamlit
- Documentation Quarto
- Kaggle — House Prices Advanced Regression Techniques
