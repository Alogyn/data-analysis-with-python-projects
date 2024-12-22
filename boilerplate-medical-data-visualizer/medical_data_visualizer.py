import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5 Melt the DataFrame
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )
    
    # 6 Group data for plotting
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    
    # 7 Create the catplot
    cat_plot = sns.catplot(
        x="variable", y="total", hue="value", col="cardio",
        data=df_cat, kind="bar", height=5, aspect=1
    )
    
    # 8 Save the figure
    fig = cat_plot.fig
    
    # 9 Save the plot and return it
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11 Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # 12 Calculate the correlation matrix
    corr = df_heat.corr()
    
    # 13 Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 14 Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 15 Draw the heatmap
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".1f",
        cmap="coolwarm", square=True, cbar_kws={"shrink": .5}, ax=ax
    )
    
    # 16 Save the plot and return it
    fig.savefig('heatmap.png')
    return fig