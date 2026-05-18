# 🚲 Kit de Démarrage : Projet Fil Rouge "La Mobilité Urbaine Durable"

Bienvenue dans l'espace de travail de votre projet fil rouge de Data Science ! Ce kit contient une structure de projet professionnelle prête à l'emploi pour vous guider de l'exploration des données jusqu'à la modélisation prédictive et la rédaction de votre rapport final.

---

## 📋 Contexte et Objectifs

En tant que Data Scientist pour une grande métropole, votre mission est de concevoir un pipeline analytique et prédictif complet en croisant les flux de mobilité urbaine (vélos, bus, trafic) avec des données météorologiques et de qualité de l'air.

Le projet est structuré en deux grands jalons :
1. **Jalon 1 (Intermédiaire - 8 pts) :** Data Wrangling, Audit de qualité des données, et Analyse Exploratoire (EDA) visuelle.
2. **Jalon 2 (Final - 12 pts) :** Modélisation prédictive sur données tabulaires, Computer Vision (CNN) sur images de caméras de trafic, et Data Storytelling (Quarto).

---

## 📂 Structure du Projet

Voici l'organisation de vos dossiers :

```text
projet/
│
├── README.md                  # Ce guide de démarrage
├── .gitignore                 # Fichiers exclus de Git (ex: modèles lourds, venv, données brutes volumineuses)
├── requirements.txt           # Liste des dépendances Python requises
│
├── data/                      # Dossier de stockage des données
│   ├── raw/                   # Données brutes originales et immuables
│   └── processed/             # Données nettoyées prêtes pour les modèles
│
├── notebooks/                 # Vos carnets de recherche Jupyter
│   ├── 01_data_wrangling.ipynb      # [JALON 1] Acquisition, fusion et nettoyage
│   ├── 02_eda_visualisation.ipynb   # [JALON 1] Analyse exploratoire des tendances et corrélations
│   ├── 03_modelisation_pred.ipynb   # [JALON 2] Modélisation prédictive (séries temporelles/tabular)
│   └── 04_vision_cnn_tf.ipynb       # [JALON 2] Analyse d'images via réseaux de neurones (CNN)
│
├── src/                       # Modules Python réutilisables (code propre)
│   ├── __init__.py            # Initialisation du module
│   ├── data_clean.py          # Fonctions de nettoyage automatisé de la donnée
│   └── utils_viz.py           # Fonctions de visualisation premium et chart-templates
│
└── report/                    # Votre livrable de communication finale
    ├── rapport.qmd            # Rapport dynamique Quarto (combine texte, code et rendus)
    ├── references.bib         # Bibliographie BibTeX pour vos citations scientifiques
    └── assets/                # Logos, schémas de pipeline exportés, etc.
```

---

## 🛠️ Installation et Démarrage Rapide

### 1. Cloner ou initialiser votre projet
Assurez-vous d'ouvrir votre terminal dans le répertoire du projet `projet/`.

### 2. Créer et activer un environnement virtuel Python
Il est fortement recommandé d'utiliser un environnement virtuel isolé pour éviter les conflits de versions.

* **Sur Linux / macOS :**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Sur Windows :**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Installer les dépendances
Une fois l'environnement activé, installez toutes les dépendances requises :
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurer le noyau Jupyter (Kernel)
Pour utiliser cet environnement virtuel dans vos notebooks Jupyter, enregistrez le kernel :
```bash
python -m ipykernel install --user --name=venv-mobilite --display-name="Python (Projet Mobilité)"
```

Dans Jupyter, veillez à bien sélectionner le kernel **"Python (Projet Mobilité)"** pour exécuter vos blocs de code.

---

## 📊 Jeu de Données de Démonstration

Pour vous aider à démarrer instantanément sans chercher de données externes, un premier jeu de données brut simulé est disponible à l'emplacement suivant : `data/raw/raw_sensor_traffic.csv`. 

Ce fichier contient :
* Des timestamps (dates/heures) sur une période continue.
* Des identifiants de stations de capteurs.
* Le décompte des vélos (`bike_count`) et bus (`bus_count`).
* Des conditions climatiques associées (température, humidité).
* Un indice de pollution de l'air (`pm25`).

> [!WARNING]
> Ce jeu de données contient volontairement des valeurs manquantes, des types incorrects (ex: dates en chaînes de caractères) et des anomalies (outliers) que vous devrez auditer et traiter lors du **Jalon 1**.

---

## 🏁 Évaluation et Barème (Rappel)

### Jalon 1 (8 points)
* **Data Wrangling (3 pts) :** Rigueur du nettoyage, gestion intelligente des valeurs manquantes (imputation), fusion et création de variables explicatives.
* **Rigueur de l'EDA (3 pts) :** Identification des corrélations clés, détection des anomalies, analyse des tendances temporelles et géographiques.
* **Pertinence Visuelle (2 pts) :** Utilisation de graphiques professionnels, lisibles, avec des axes clairs et une palette de couleurs soignée.

### Jalon 2 (12 points)
* **Architecture Modèle (4 pts) :** Modélisation supervisée ou non supervisée rigoureuse, split train/test respectueux des séries temporelles, et conception d'un CNN avec TensorFlow pour la brique image.
* **Rigueur d'Évaluation (3 pts) :** Interprétation et comparaison méticuleuse des métriques d'erreur.
* **Data Storytelling (3 pts) :** Clarté de la restitution, interactivité éventuelle, structure globale professionnelle du rapport.
* **Qualité Transverse (2 pts) :** Présence d'un schéma de pipeline de données en Mermaid, et précision générale.

Bon travail et bon code ! 🚀
