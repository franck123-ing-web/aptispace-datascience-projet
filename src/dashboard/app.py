import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import shap

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# =====================================================
# CONFIGURATION PAGE
# =====================================================

st.set_page_config(
    page_title="🏠 Smart House Price AI",
    page_icon="🏠",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
    }

    h1, h2, h3 {
        color: #1f2937;
    }

    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# TITRE
# =====================================================

st.title("🏠 Smart House Price Prediction Dashboard")

st.markdown("""
Bienvenue dans cette application de Data Science dédiée à la prédiction des prix immobiliers.

Cette plateforme permet de :
- analyser les données immobilières,
- comprendre le fonctionnement du modèle,
- interpréter les erreurs de prédiction,
- expliquer les décisions de l’intelligence artificielle,
- simuler un prix immobilier en temps réel.
""")

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/raw/train.csv")

df = load_data()

st.success("✅ Dataset chargé avec succès")

# =====================================================
# VARIABLES ET DONNÉES
# =====================================================

df["TotalSF"] = df["GrLivArea"] + df["TotalBsmtSF"]
df["HouseAge"] = df["YrSold"] - df["YearBuilt"]
df["QualityScore"] = df["OverallQual"] * df["OverallCond"]

features = [
    "GrLivArea",
    "OverallQual",
    "GarageCars",
    "TotalBsmtSF",
    "YearBuilt",
    "TotalSF",
    "HouseAge",
    "QualityScore"
]

df_model = df[features + ["SalePrice"]].dropna()

X = df_model[features]
y = df_model["SalePrice"]

# =====================================================
# VISUALISATION DES DONNÉES
# =====================================================

st.header(" Compréhension des données immobilières")

st.markdown("""
Avant de créer le modèle d’intelligence artificielle, il est important de comprendre les données immobilières utilisées.

Les graphiques suivants permettent d’observer :
- la distribution des prix,
- la relation entre la taille des maisons et leur prix.
""")

# Distribution des prix

fig_hist = px.histogram(
    df,
    x="SalePrice",
    nbins=50,
    title="Distribution des prix des maisons"
)

st.plotly_chart(fig_hist, use_container_width=True)

st.markdown("""
Ce graphique montre que la majorité des maisons possèdent des prix moyens,
mais certaines maisons ont des prix beaucoup plus élevés.
""")

# Relation surface / prix

fig_scatter = px.scatter(
    df,
    x="GrLivArea",
    y="SalePrice",
    color="OverallQual",
    title="Surface habitable vs Prix"
)

st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("""
On observe que :
- les grandes maisons ont souvent des prix plus élevés,
- la qualité générale influence fortement le prix.
""")

# =====================================================
# ENTRAÎNEMENT IA
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

with st.spinner("Entraînement du modèle IA..."):
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

# =====================================================
# COMMUNICATION MÉTIER
# =====================================================

st.header(" Communication et interprétation métier")

st.markdown("""
Cette partie explique :
- comment le modèle fonctionne,
- comment il prend ses décisions,
- quelles erreurs il peut produire,
- et comment utiliser correctement les estimations.
""")

# =====================================================
# SCHÉMA GLOBAL
# =====================================================

schema_df = pd.DataFrame({
    "Étapes": [
        "Données\nimmobilières",
        "Nettoyage\ndonnées",
        "Apprentissage\nIA",
        "Analyse\nmaisons similaires",
        "Estimation\nprix"
    ],
    "Ordre": [1, 2, 3, 4, 5]
})

fig_schema = px.line(
    schema_df,
    x="Étapes",
    y="Ordre",
    markers=True,
    title="Fonctionnement global du système"
)

fig_schema.update_traces(
    line=dict(width=5),
    marker=dict(size=18)
)

fig_schema.update_layout(
    yaxis_visible=False,
    showlegend=False
)

st.plotly_chart(fig_schema, use_container_width=True)

st.markdown("""
Le système fonctionne en plusieurs étapes :

1. récupération des données immobilières,
2. nettoyage des données,
3. apprentissage par intelligence artificielle,
4. comparaison avec des maisons similaires,
5. estimation automatique du prix.
""")

# =====================================================
# ÉVALUATION DU MODÈLE
# =====================================================

st.subheader(" Comprendre les performances du modèle")

mae = mean_absolute_error(y_test, preds)
rmse = np.sqrt(mean_squared_error(y_test, preds))
r2 = r2_score(y_test, preds)

col1, col2, col3 = st.columns(3)

col1.metric("MAE", f"{int(mae):,} €")
col2.metric("RMSE", f"{int(rmse):,} €")
col3.metric("R²", round(r2, 3))

st.markdown("""
- MAE → erreur moyenne du modèle
- RMSE → pénalise davantage les grosses erreurs
- R² → plus proche de 1 = meilleur modèle
""")

# =====================================================
# RÉEL VS PRÉDICTION
# =====================================================

st.subheader(" Comparaison réel vs prédiction")

fig1, ax1 = plt.subplots()

ax1.scatter(y_test, preds, alpha=0.5)

ax1.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red"
)

ax1.set_title("Prix réel vs Prix prédit")
ax1.set_xlabel("Prix réel")
ax1.set_ylabel("Prix prédit")

st.pyplot(fig1)

st.markdown("""
Chaque point représente une maison.

La ligne rouge représente une prédiction parfaite.

Plus les points sont proches de cette ligne :
- plus les prédictions sont précises,
- plus le modèle est performant.
""")

# =====================================================
# ERREURS
# =====================================================

st.subheader(" Analyse des erreurs")

errors = y_test - preds

fig2, ax2 = plt.subplots()

ax2.hist(errors, bins=40)

ax2.set_title("Distribution des erreurs")
ax2.set_xlabel("Erreur")
ax2.set_ylabel("Nombre de maisons")

st.pyplot(fig2)

st.markdown("""
Une erreur correspond à la différence entre :
- le prix réel,
- et le prix prédit.

Lorsque les erreurs sont proches de zéro,
cela signifie que le modèle prédit correctement les prix.
""")

# =====================================================
# EXEMPLE CONCRET D'ERREUR
# =====================================================

st.subheader(" Exemple concret d’erreur")

real_price = 200000
predicted_price = 183569

difference = abs(real_price - predicted_price)

example_error = pd.DataFrame({
    "Type": ["Prix réel", "Prix prédit"],
    "Prix": [real_price, predicted_price]
})

fig_error = px.bar(
    example_error,
    x="Type",
    y="Prix",
    text="Prix",
    title="Exemple d’erreur du modèle"
)

st.plotly_chart(fig_error, use_container_width=True)

st.markdown(f"""
Dans cet exemple :

- le prix réel était de {real_price:,} €
- le modèle a prédit {predicted_price:,} €
- l’erreur est de {difference:,} €

Cette différence peut être causée par :
- des informations absentes du dataset,
- la localisation exacte,
- l’état réel de la maison,
- les fluctuations du marché immobilier.
""")

# =====================================================
# IMPORTANCE VARIABLES
# =====================================================

st.header(" Variables importantes pour le modèle")

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values("Importance")

st.bar_chart(importance.set_index("Feature"))

st.markdown("""
Les variables les plus importantes influencent davantage les décisions du modèle.

La surface habitable et la qualité générale sont souvent les plus influentes.
""")

# =====================================================
# SHAP
# =====================================================

st.header(" Explicabilité du modèle (SHAP)")

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_test)

# Renommer les colonnes en français
X_test_fr = X_test.rename(columns={
    "GrLivArea": "Surface habitable",
    "OverallQual": "Qualité générale",
    "GarageCars": "Nombre de garages",
    "TotalBsmtSF": "Surface sous-sol",
    "YearBuilt": "Année construction",
    "TotalSF": "Surface totale",
    "HouseAge": "Âge maison",
    "QualityScore": "Score qualité"
})

fig = plt.figure(figsize=(10, 6))

shap.summary_plot(
    shap_values,
    X_test_fr,
    show=False
)

plt.xlabel("Impact sur le prix de la maison")
plt.ylabel("Variables explicatives")

st.pyplot(fig)

st.markdown("""
SHAP permet de comprendre :
- quelles variables augmentent le prix,
- quelles variables diminuent le prix,
- l’impact exact de chaque caractéristique.

Plus une variable est située vers la droite,
plus elle augmente le prix estimé.
""")

# =====================================================
# EXEMPLES DE PRÉDICTIONS
# =====================================================

st.header(" Exemples de prédictions")

sample = pd.DataFrame({
    "Prix réel": y_test.values[:10],
    "Prix prédit": preds[:10]
})

sample["Erreur"] = abs(
    sample["Prix réel"] - sample["Prix prédit"]
)

st.dataframe(sample)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🏠 Simulation Immobilière")

st.sidebar.markdown("""
Modifiez les caractéristiques de la maison afin de simuler un prix immobilier en temps réel.
""")

surface = st.sidebar.slider(
    "Surface habitable",
    500,
    5000,
    1500
)

quality = st.sidebar.slider(
    "Qualité générale",
    1,
    10,
    5
)

garage = st.sidebar.slider(
    "Nombre de garages",
    0,
    5,
    2
)

basement = st.sidebar.slider(
    "Surface sous-sol",
    0,
    3000,
    800
)

year = st.sidebar.slider(
    "Année construction",
    1900,
    2026,
    2005
)

# =====================================================
# CALCUL
# =====================================================

total_sf = surface + basement
house_age = 2026 - year
quality_score = quality * 5

input_data = pd.DataFrame([[
    surface,
    quality,
    garage,
    basement,
    year,
    total_sf,
    house_age,
    quality_score
]], columns=features)

prediction = model.predict(input_data)[0]

# =====================================================
# PRÉDICTION FINALE
# =====================================================

st.header(" Simulation finale du prix immobilier")

price = f"{int(prediction):,} €"

st.markdown(f"""
<div style="
    background:white;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:32px;
    font-weight:bold;
    box-shadow:0px 3px 12px rgba(0,0,0,0.1);
    color:#1f77b4;
">
🏠 {price}
</div>
""", unsafe_allow_html=True)

st.info(f"""
Surface : {surface} m²  
Qualité : {quality}/10  
Garage : {garage}  
Sous-sol : {basement} m²  
Année : {year}
""")
