# 📊 Mon Projet Data Science

[![CI Compilation Pipeline](https://github.com/aptitek/aptispace-datascience-projet/actions/workflows/ci.yml/badge.svg)](https://github.com/aptitek/aptispace-datascience-projet/actions/workflows/ci.yml)
[![GitHub Release](https://img.shields.svg/github/v/release/aptitek/aptispace-datascience-projet?color=blue&label=Dernier%20Release)](../../releases/latest)
[![Quarto](https://img.shields.svg/badge/Quarto-v1.4+-1a73e8.svg?logo=quarto)](https://quarto.org)
[![Typst](https://img.shields.svg/badge/Typst-PDF-3fca3f.svg)](https://typst.app)
[![Python](https://img.shields.svg/badge/Python-3.12-fecd3c.svg?logo=python)](https://python.org)

> **Bienvenue dans le portail d'accueil de notre Projet Data Science.**
> Ce dépôt contient l'intégralité du pipeline analytique (de l'acquisition multi-sources des données jusqu'à l'évaluation et la communication des résultats).
>
> Pour préserver la propreté de l'historique et simplifier la collaboration, **toutes les compilations de rapports sont déportées sur notre intégration continue (CI)**. Les livrables finaux sont publiés automatiquement à chaque mise à jour.

---

## 📥 Livrables du Projet (Rapports & Supports)

Les rapports compilés dans tous les formats, ainsi que le code source exécutable et ses journaux, sont mis à jour en temps réel à chaque push et disponibles au téléchargement sur la **[dernière version du Release GitHub](../../releases/latest)**.

| Format | Description | Lien de Téléchargement |
| :--- | :--- | :--- |
| **📄 Rapport PDF** | Rapport complet mis en page de haute qualité via **Typst** | [**Télécharger le PDF**](../../releases/download/latest/rapport.pdf) |
| **🌐 Rapport Interactif** | Rapport HTML complet intégrant le tableau de bord dynamique **Observable JS (OJS)** | [**Télécharger l'HTML**](../../releases/download/latest/rapport.html) |
| **📝 Rapport Markdown** | Version de lecture rapide optimisée pour l'affichage GitHub | [**Consulter le Markdown**](../../releases/download/latest/README.md) |
| **🧠 Scripts Python** | Archive compressée des scripts extraits de tous les notebooks | [**Télécharger les Sources (.zip)**](../../releases/download/latest/sources.zip) |
| **🪵 Journaux d'Exécution** | Archive de tous les logs de compilation et d'exécution | [**Télécharger les Logs (.zip)**](../../releases/download/latest/logs.zip) |

*Note : Si vous avez forké ce dépôt, vos propres compilations seront disponibles dans l'onglet **Releases** de votre propre dépôt GitHub après l'exécution du pipeline Actions.*

---

## 📂 Structure du Projet

```text
├── .github/workflows/      # Pipelines d'intégration continue
├── build/                  # Fichiers de compilation générés (exclus de Git)
│   ├── src/                # Scripts Python extraits des notebooks
│   ├── logs/               # Rapports d'exécution de chaque étape
│   ├── notebooks/          # Fichiers Quarto Markdown intermédiaires
│   └── report/             # PDF, HTML et Markdown compilés finaux
├── data/                   # Dossier de stockage des données
│   ├── raw/                # Données brutes sources
│   └── processed/          # Données nettoyées après Wrangling
├── notebooks/              # Travaux pratiques (fichiers .ipynb d'origine)
│   ├── 01_acquisition.ipynb
│   ├── 02_wrangling.ipynb
│   ├── ...
├── report/                 # Modèles et configurations des rapports
│   ├── rapport.qmd         # Fichier maître du rapport
│   └── slides.qmd          # Support de soutenance RevealJS
└── tools/                  # Utilitaires de compilation et de preprocessing
```

---

## 🛠️ Exécuter et compiler localement

Toutes les tâches du projet sont orchestrées simplement via le gestionnaire de tâches **Go-Task** (`task`).

### 1. Prérequis

Assurez-vous d'avoir installé :
- [Python 3.12](https://www.python.org/)
- [Quarto CLI](https://quarto.org/docs/get-started/)
- [Go-Task](https://taskfile.dev/installation/)

Installez ensuite les dépendances du projet :
```bash
pip install -r requirements.txt
```

### 2. Commandes de compilation rapides

Depuis la racine du projet, lancez :

* **Compiler l'intégralité du pipeline et des rapports** (génère tout dans `build/`) :
  ```bash
  task render
  ```
* **Prévisualiser dynamiquement le rapport dans le navigateur** (rechargement automatique lors de la saisie) :
  ```bash
  task preview
  ```
* **Compiler uniquement le guide d'installation** :
  ```bash
  task install-guide
  ```
* **Nettoyer tous les fichiers temporaires et compilations locales** :
  ```bash
  task clean
  ```

---

<<<<<<< HEAD
*Développé dans le cadre du projet fil rouge de Data Science.*
=======
## Chapitre 6 : Travaux Pratiques d’Évaluation & Robustesse

# 🧪 Étape 6 : Évaluation Métrique & Robustesse (Squelette Étudiant)

Cette étape correspond au sixième chapitre du cours. L’objectif est de
mettre en place un protocole d’évaluation rigoureux (splits d’évaluation
adaptés) et de calculer les métriques clés de performance pour valider
scientifiquement la qualité de vos modèles.

### 1. Préparation de l’environnement

### 2. Évaluation du modèle Tabulaire

**À COMPLÉTER PAR L’ÉTUDIANT :** Calculez et interprétez les métriques
d’erreur sur vos prédictions (MAE, RMSE, R²).

### 3. Protocole de Validation Croisée (Out-of-Fold / Chronologique)

**À COMPLÉTER PAR L’ÉTUDIANT :** Décrivez et codez (ou documentez) une
stratégie de validation croisée adaptée au comportement temporel de vos
données pour valider la robustesse de votre modèle sans fuite
d’information.

------------------------------------------------------------------------

# Data Storytelling et Communication

## Chapitre 7 : Travaux Pratiques de Storytelling

# 📢 Étape 7 : Data Storytelling & Communication (Squelette Étudiant)

Cette étape correspond au septième et dernier chapitre de data science.
L’objectif est de synthétiser vos résultats pour des profils métiers ou
décideurs et de proposer des visualisations interactives ou dynamiques
pour valoriser vos conclusions.

### 1. Préparation de l’environnement

### 2. Synthèse métier et Storytelling

**À COMPLÉTER PAR L’ÉTUDIANT :** Traduisez vos métriques techniques en
impacts stratégiques (par exemple, gains financiers, réduction de coûts,
amélioration de la sécurité, etc.).

<div id="plotly-22832f08-72ec-4fd6-8f94-e28319c1edfb"
style="width:100%; height:400px; background: white; border-radius: 8px;">

</div>

<script type="text/javascript">
  document.addEventListener("DOMContentLoaded", function() {
    if (typeof Plotly !== 'undefined') {
      Plotly.newPlot('plotly-22832f08-72ec-4fd6-8f94-e28319c1edfb', [{"type": "scatter", "x": [1, 2, 3], "y": [10, 15, 13], "mode": "lines+markers", "name": "Donn\u00e9es de Test"}], {"title": "Mon Graphique Plotly de Test"}, {"responsive": true});
    } else {
      console.error("Plotly library is not loaded.");
    }
  });
</script>

### 3. Visualisation Interactive (Plotly)

**À COMPLÉTER PAR L’ÉTUDIANT :** Générez un graphique interactif (par
exemple en utilisant Plotly ou des éléments OJS dans le document final)
pour permettre aux décideurs d’interagir dynamiquement avec vos données.

<div id="plotly-b710acc6-d2c3-49c1-8448-5c00fad65e93"
style="width:100%; height:400px; background: white; border-radius: 8px;">

</div>

<script type="text/javascript">
  document.addEventListener("DOMContentLoaded", function() {
    if (typeof Plotly !== 'undefined') {
      Plotly.newPlot('plotly-b710acc6-d2c3-49c1-8448-5c00fad65e93', [{"type": "scatter", "x": [1, 2, 3], "y": [10, 15, 13], "mode": "lines+markers", "name": "Donn\u00e9es de Test"}], {"title": "Mon Graphique Plotly de Test"}, {"responsive": true});
    } else {
      console.error("Plotly library is not loaded.");
    }
  });
</script>

## Présentation des Résultats (Livrables Interactifs)

<div class="panel-tabset">

### 📺 Diaporama de Soutenance (RevealJS)

Ci-dessous est intégré le squelette de votre diaporama de soutenance
RevealJS. Utilisez-le pour présenter votre démarche aux décideurs de
façon professionnelle.

<iframe src="slides.html" width="100%" height="500px" style="border: 1px solid #e2e8f0; border-radius: 8px; background: white;">

</iframe>

### 📊 Exemple de Dashboard Dynamique (OJS / Plotly)

Voici un exemple minimal de code montrant comment intégrer un graphique
dynamique contrôlé par un composant d’interface utilisateur en
Observable JS (OJS).

<div style="background: #f8fafc; padding: 1.5rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 1.5rem;">
  <div style="margin-bottom: 1rem; font-family: sans-serif;">
    <label for="selectedCategory-select" style="font-weight: 600; margin-right: 0.5rem; color: #1e293b;">Filtrer par Catégorie :</label>
    <select id="selectedCategory-select" style="padding: 0.5rem; border-radius: 4px; border: 1px solid #cbd5e1; background: white; color: #1e293b;">
      <option value="Toutes" selected>Toutes</option>
      <option value="A">A</option>
      <option value="B">B</option>
      <option value="C">C</option>
    </select>
  </div>
  
</div>

<script type="text/javascript">
  document.addEventListener("DOMContentLoaded", function() {
    const data = [
  {timestamp: "2026-05-18T00:00:00Z", value: 10.5, category: "A"},
  {timestamp: "2026-05-18T02:00:00Z", value: 12.1, category: "A"},
  {timestamp: "2026-05-18T04:00:00Z", value: 14.7, category: "A"},
  {timestamp: "2026-05-18T05:00:00Z", value: 15.2, category: "A"},
  {timestamp: "2026-05-18T06:00:00Z", value: 16.0, category: "B"},
  {timestamp: "2026-05-18T07:00:00Z", value: 18.3, category: "B"},
  {timestamp: "2026-05-18T09:00:00Z", value: 21.5, category: "B"},
  {timestamp: "2026-05-18T10:00:00Z", value: 22.0, category: "B"},
  {timestamp: "2026-05-18T12:00:00Z", value: 25.4, category: "C"},
  {timestamp: "2026-05-18T13:00:00Z", value: 26.1, category: "C"},
  {timestamp: "2026-05-18T15:00:00Z", value: 28.9, category: "C"},
  {timestamp: "2026-05-18T16:00:00Z", value: 30.2, category: "C"}
];

    function updatePlot(category) {
      if (typeof Plotly === 'undefined') {
        console.error("Plotly is not loaded");
        return;
      }
      // Boutons de sélection interactifs OJS
      // Données simulées réactives
      // Filtrage réactif de la donnée
      const filteredData = category === "Toutes" 
        ? data 
        : data.filter(d => d.category === category)
      // Tracé interactif avec la librairie Plotly
      Plotly.newPlot('dynamic-chart', [{
        x: filteredData.map(d => d.timestamp),
        y: filteredData.map(d => d.value),
        type: 'scatter',
        mode: 'lines+markers',
        marker: {color: '#1A73E8', size: 8},
        line: {shape: 'spline', color: '#1A73E8', width: 3}
      }], {
        title: 'Évolution Dynamique des Valeurs (Filtrée)',
        margin: {t: 50, b: 50, l: 50, r: 50},
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        xaxis: {gridcolor: '#E5E7EB'},
        yaxis: {gridcolor: '#E5E7EB'}
      })
    }

    const select = document.getElementById("selectedCategory-select");
    if (select) {
      select.addEventListener("change", function(e) {
        updatePlot(e.target.value);
      });
      updatePlot(select.value);
    }
  });
</script>






</div>

------------------------------------------------------------------------

# Utilisation de l’Intelligence Artificielle

Dans une démarche de transparence scientifique et académique, cette
section détaille la manière dont les outils d’Intelligence Artificielle
(IA) générative ont été intégrés tout au long de la réalisation de ce
projet.

## Cartographie de l’utilisation de l’IA

| Outil d’IA | Cas d’usage (Pourquoi ?) | Méthode d’utilisation (Comment ?) | Rôle et Validation Humaine |
|:---|:---|:---|:---|
| **\[Outil d’IA\]** | *\[À compléter par les étudiants\]* | *\[À compléter par les étudiants\]* | *\[À compléter par les étudiants\]* |

## Principes de Rigueur et Responsabilité

1.  **Responsabilité intellectuelle** : L’équipe assume l’entière
    responsabilité des analyses, des choix de modèles et des conclusions
    présentées dans ce rapport.
2.  **Lutte contre les hallucinations** : Chaque suggestion technique a
    fait l’objet d’une validation empirique.
3.  **Protection des données** : Aucun jeu de données confidentiel ou
    sensible n’a été soumis à des modèles tiers en ligne.

------------------------------------------------------------------------

# Bibliographie

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-pandas2020" class="csl-entry">

McKinney, Wes. 2020. *Python for Data Analysis: Data Wrangling with
Pandas, NumPy, and IPython*. O’Reilly Media.

</div>

</div>

<script type="ojs-module-contents">
eyJjb250ZW50cyI6W119
</script>

<div id="exercise-loading-indicator"
class="exercise-loading-indicator d-none d-flex align-items-center gap-2">

<div id="exercise-loading-status" class="d-flex gap-2">

</div>

<div class="spinner-grow spinner-grow-sm">

</div>

</div>

<script type="vfs-file">
W10=
</script>
>>>>>>> refs/remotes/origin/main
