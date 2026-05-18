import pandas as pd
import numpy as np
from typing import List, Union

def load_raw_data(file_path: str) -> pd.DataFrame:
    """
    Charge le jeu de données brut depuis le chemin spécifié.
    
    Parameters:
    -----------
    file_path : str
        Le chemin d'accès au fichier CSV brut.
        
    Returns:
    --------
    pd.DataFrame
        Le DataFrame chargé.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Données chargées avec succès. Dimensions : {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Erreur lors du chargement des données : {e}")
        raise e

def clean_dates(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """
    Nettoie et uniformise la colonne de dates du DataFrame en gérant
    les formats multiples (ex: ISO standard et format français DD/MM/YYYY HH:MM).
    
    Parameters:
    -----------
    df : pd.DataFrame
        Le DataFrame d'entrée.
    date_col : str
        Le nom de la colonne contenant les dates.
        
    Returns:
    --------
    pd.DataFrame
        Le DataFrame avec la colonne de dates uniformisée au type datetime64.
    """
    # TODO: Écrire le code de nettoyage des formats de dates hétérogènes
    # Indices : Utilisez pd.to_datetime avec les options format='mixed' ou dayfirst=True
    raise NotImplementedError("La fonction clean_dates doit être implémentée par l'étudiant dans src/data_clean.py")

def impute_missing_values(df: pd.DataFrame, method: str = 'interpolate') -> pd.DataFrame:
    """
    Traite les valeurs manquantes dans le DataFrame selon la stratégie choisie.
    - Pour la météo (température, humidité), l'interpolation linéaire temporelle est recommandée.
    - Pour les comptages, une imputation par interpolation ou par médiane groupée peut être appliquée.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Le DataFrame avec colonnes nettoyées et indexé par le temps ou trié chronologiquement.
    method : str, default 'interpolate'
        Méthode d'imputation : 'interpolate' (linéaire), 'median' (médiane) ou 'ffill' (Forward fill).
        
    Returns:
    --------
    pd.DataFrame
        Le DataFrame avec les valeurs imputées.
    """
    # TODO: Écrire le code d'imputation des valeurs nulles (NaNs)
    # Indices : Pensez à isoler les colonnes numériques et à utiliser df.interpolate() ou df.fillna()
    raise NotImplementedError("La fonction impute_missing_values doit être implémentée par l'étudiant dans src/data_clean.py")

def handle_outliers(df: pd.DataFrame, 
                    columns: List[str], 
                    temp_range: tuple = (-20.0, 45.0),
                    bike_max: float = 1000.0) -> pd.DataFrame:
    """
    Détecte et traite les anomalies (outliers) physiques connues :
    - Les températures aberrantes hors de l'intervalle temp_range sont remplacées par NaN (pour être interpolées ensuite).
    - Les comptages négatifs de vélos sont mis à 0.
    - Les comptages de vélos extrêmes (> bike_max) sont plafonnés ou remplacés par NaN.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Le DataFrame d'entrée.
    columns : List[str]
        Les colonnes numériques à auditer.
    temp_range : tuple, default (-20.0, 45.0)
        Intervalle plausible de températures en Celsius.
    bike_max : float, default 1000.0
        Comptage de vélo horaire maximum physiquement réaliste pour une piste cyclable.
        
    Returns:
    --------
    pd.DataFrame
        Le DataFrame traité.
    """
    # TODO: Détecter et traiter les valeurs aberrantes physiques
    # Indices : Utilisez des masques booléens pour identifier les lignes hors intervalle
    # et remplacez les par np.nan ou mettez-les à 0 selon la consigne.
    raise NotImplementedError("La fonction handle_outliers doit être implémentée par l'étudiant dans src/data_clean.py")

def feature_engineering(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """
    Enrichit le jeu de données en créant des caractéristiques temporelles
    essentielles à l'analyse exploratoire et aux modèles de Machine Learning.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Le DataFrame d'entrée (la colonne date_col doit déjà être au format datetime).
    date_col : str
        Le nom de la colonne temporelle.
        
    Returns:
    --------
    pd.DataFrame
        Le DataFrame avec de nouvelles variables explicatives.
    """
    # TODO: Extraire les caractéristiques temporelles
    # Indices : Utilisez les accesseurs de dates de Pandas (df[date_col].dt.hour, .dt.dayofweek, etc.)
    # Et calculez les encodages trigonométriques sinus/cosinus de l'heure avec np.sin/np.cos.
    raise NotImplementedError("La fonction feature_engineering doit être implémentée par l'étudiant dans src/data_clean.py")
