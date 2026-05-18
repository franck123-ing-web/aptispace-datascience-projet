import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


# ======================
# CONFIG
# ======================
st.set_page_config(
    page_title="AI House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 AI House Price Prediction")

st.markdown("""
Bienvenue 👋  
Cette application utilise des modèles de Machine Learning pour estimer le prix d’un logement à partir de ses caractéristiques principales (surface, qualité, année de construction, etc.).  
Elle permet aussi de visualiser les facteurs qui influencent le plus les prix.
""")



# ======================
# LOAD DATA
# ======================
@st.cache_data
def load_data():
    return pd.read_csv("data/raw/train.csv")

df = load_data()


# ======================
# FEATURE ENGINEERING
# ======================
df["TotalSF"] = df["GrLivArea"] + df["TotalBsmtSF"]
df["HouseAge"] = df["YrSold"] - df["YearBuilt"]
df["QualityScore"] = df["OverallQual"] * df["OverallCond"]


# ======================
# MODEL
# ======================
features = ["GrLivArea", "OverallQual", "YearBuilt", "TotalSF", "HouseAge", "QualityScore"]

df_model = df[features + ["SalePrice"]].dropna()

X = df_model[features]
y = df_model["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=400, max_depth=15, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)


# ======================
# SIDEBAR INPUT
# ======================
st.sidebar.header("🏡 Simulation maison")

gr = st.sidebar.slider("Surface habitable", 500, 5000, 1500)
qual = st.sidebar.slider("Qualité", 1, 10, 5)
year = st.sidebar.slider("Année construction", 1900, 2020, 2000)


# derived features
total_sf = gr * 1.2
age = 2026 - year
quality_score = qual * 5


input_data = pd.DataFrame([[
    gr,
    qual,
    year,
    total_sf,
    age,
    quality_score
]], columns=features)


prediction = model.predict(input_data)[0]


# ======================
# OUTPUT
# ======================
st.markdown("## 💰 Prix estimé")

st.metric("Prix maison", f"{int(prediction):,} €")

st.metric("Erreur moyenne modèle (MAE)", f"{int(mae):,} €")


# ======================
# FEATURE IMPORTANCE
# ======================
st.markdown("## 📊 Importance des variables")

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values("Importance")

st.bar_chart(importance.set_index("Feature"))


# ======================
# DATA PREVIEW
# ======================
st.markdown("## 📄 Aperçu dataset")
st.dataframe(df.head())