import numpy as np
import pandas as pd
import matplotlib as plt

df = pd.read_csv("attacking.csv")

top10_assists = df.sort_values(by='assists', ascending=False).head(10)
print(top10_assists)

top10_dribbles = df.sort_values(by='dribbles',ascending=False).head(10)
print(top10_dribbles)
