import numpy as np

def feature_engineering(df):

    df = df.copy()

    # surface totale
    df["TotalSF"] = df["GrLivArea"] + df["TotalBsmtSF"]

    # âge maison
    df["HouseAge"] = df["YrSold"] - df["YearBuilt"]

    # qualité globale pondérée
    df["QualityScore"] = df["OverallQual"] * df["OverallCond"]

    # log prix (meilleure distribution ML)
    df["LogPrice"] = np.log1p(df["SalePrice"])

    return df