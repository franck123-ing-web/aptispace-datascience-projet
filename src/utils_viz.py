import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import List, Optional

def set_custom_style(theme: str = 'light'):
    """
    Applique une charte graphique premium pour toutes les visualisations du projet.
    Met en place une typographie soignée, des grilles discrètes et des palettes harmonieuses.
    
    Parameters:
    -----------
    theme : str, default 'light'
        Thème général des graphiques : 'light' (sleek minimaliste) ou 'dark' (cyberpunk sobre).
    """
    colors_light = ["#1A73E8", "#D93025", "#188038", "#F29900", "#70757A"]
    colors_dark = ["#8AB4F8", "#F28B82", "#81C995", "#FDD663", "#9AA0A6"]
    
    selected_colors = colors_light if theme == 'light' else colors_dark
    
    sns.set_theme(style="whitegrid" if theme == 'light' else "darkgrid")
    
    plt.rcParams.update({
        'figure.dpi': 120,
        'axes.labelsize': 11,
        'axes.titlesize': 13,
        'axes.titleweight': 'bold',
        'xtick.labelsize': 9.5,
        'ytick.labelsize': 9.5,
        'grid.color': '#E5E7EB' if theme == 'light' else '#374151',
        'grid.linestyle': '--',
        'grid.linewidth': 0.6,
        'legend.frameon': True,
        'legend.facecolor': '#FFFFFF' if theme == 'light' else '#1F2937',
        'legend.edgecolor': 'none',
        'legend.fontsize': 9,
        'axes.prop_cycle': plt.cycler(color=selected_colors)
    })
    
    print(f"🎨 Charte graphique '{theme}' initialisée avec succès.")

def plot_traffic_density(df: pd.DataFrame, 
                         station_id: Optional[str] = None) -> plt.Figure:
    """
    Génère un graphique linéaire de la densité moyenne de trafic (vélos vs bus)
    par heure de la journée, montrant les profils journaliers d'activité.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame enrichi avec les colonnes 'hour', 'bike_count', 'bus_count', 'station_id'.
    station_id : Optional[str], default None
        Si spécifié, filtre le graphique sur une station spécifique.
        
    Returns:
    --------
    plt.Figure
        La figure Matplotlib créée.
    """
    # TODO: Écrire le code de traçage du profil journalier vélos (axe gauche) et bus (axe droit)
    # Indices :
    # 1. Calculez les moyennes et écarts-types par heure en groupant par 'hour'.
    # 2. Utilisez ax.plot() pour les vélos et ax.fill_between() pour leur intervalle de confiance.
    # 3. Créez un axe secondaire droit avec ax2 = ax.twinx() pour y tracer la courbe des bus.
    raise NotImplementedError("La fonction plot_traffic_density doit être implémentée par l'étudiant dans src/utils_viz.py")

def plot_correlation_matrix(df: pd.DataFrame, columns: List[str]) -> plt.Figure:
    """
    Génère une carte de chaleur (heatmap) élégante montrant la corrélation
    entre différentes variables (météo, pollution, comptage de transit).
    
    Parameters:
    -----------
    df : pd.DataFrame
        Le DataFrame d'entrée.
    columns : List[str]
        Les colonnes numériques à inclure.
        
    Returns:
    --------
    plt.Figure
        La figure Matplotlib créée.
    """
    # TODO: Tracage de la heatmap de corrélations de Spearman
    # Indices :
    # 1. Calculez la matrice de corrélation avec df[columns].corr(method='spearman').
    # 2. Créez un masque pour masquer la partie supérieure redondante (avec np.triu et np.ones_like).
    # 3. Appelez sns.heatmap() en passant le masque et un cmap divergent (ex: sns.diverging_palette).
    raise NotImplementedError("La fonction plot_correlation_matrix doit être implémentée par l'étudiant dans src/utils_viz.py")

def plot_weather_vs_active_transit(df: pd.DataFrame) -> plt.Figure:
    """
    Crée un nuage de points dynamique montrant la relation entre
    la température et le nombre de cyclistes, coloré par le niveau de pollution.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Le DataFrame.
        
    Returns:
    --------
    plt.Figure
        La figure créée.
    """
    # TODO: Tracé du nuage de points température vs vélos coloré par pm25 avec courbe de tendance
    # Indices :
    # 1. Supprimez les lignes contenant des valeurs nulles sur ces trois variables.
    # 2. Utilisez ax.scatter() avec c=df['pm25'] et un colormap (ex: cmap='viridis_r').
    # 3. Calculez et tracez une ligne d'ajustement de tendance (avec np.polyfit et np.poly1d).
    raise NotImplementedError("La fonction plot_weather_vs_active_transit doit être implémentée par l'étudiant dans src/utils_viz.py")
