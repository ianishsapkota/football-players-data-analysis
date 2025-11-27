import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("attacking.csv")


#top 10 assists
top10_assists = df.sort_values(by='assists', ascending=False).head(10)
print(top10_assists)

#top 10 dribbles
top10_dribbles = df.sort_values(by='dribbles',ascending=False).head(10)
print(top10_dribbles)

#playrs position distribution
position_counts = df['position'].value_counts()
plt.pie(position_counts,labels = position_counts.index)
plt.title("Distribution of Players Position")



#assist per club
assists_per_club = df.groupby('club')['assists'].sum()

plt.bar(assists_per_club.index, assists_per_club.values)
plt.xticks(rotation=90)
plt.title("Assists per Club (Sorted)")
plt.xlabel("Club")
plt.ylabel("Assists")
plt.show()

#most valuable player for the club in terms of assist
df.loc[df.groupby('club')['assists'].idxmax(), ['club', 'player_name', 'assists']]
