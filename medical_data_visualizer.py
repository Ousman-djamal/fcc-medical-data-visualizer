import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
height_m_aucarre=(df["height"]*0.01)**2
imc=df["weight"]/height_m_aucarre
df['overweight'] = np.where(imc > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,  
                  value_vars=['cholesterol', 'gluc','smoke','alco','active','overweight'],
                  var_name='variable', 
                  value_name='value')


    # 6
    df_cat = pd.melt(df,  id_vars=['cardio'],
                  value_vars=['active', 'alco','cholesterol','gluc','overweight','smoke'],
                  var_name='variable', 
                  value_name='value')
   


    

    # 7



    # 8
    g = sns.catplot(
    data=df_cat,
    x="variable",
    hue="value",
    col="cardio",
    kind="count"
    )

    g.set_axis_labels("variable", "total")

    fig = g.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 12))
    # 15
    sns.heatmap(
        corr, 
        mask=mask,          # Applique le masque pour cacher le triangle supérieur
        annot=True,         # Affiche les valeurs de corrélation dans les cases
        fmt=".1f",          # Arrondit les valeurs à 1 décimale (ex: 0.1)
        center=0,           # Centre la palette de couleurs sur 0
        square=True,        # Force les cases à être de parfaits carrés
        linewidths=.5,      # Ajoute une fine ligne de séparation entre les cases
        cbar_kws={"shrink": .5}, # Réduit légèrement la taille de la barre de légende
        ax=ax
    )


    # 16
    fig.savefig('heatmap.png')
    return fig
