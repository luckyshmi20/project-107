import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("sports.csv")

print(df)

fig = go.Figure(go.Bar
                (x="Distance(Km)", 
                 y=['Basketball', 'Tennis', 'Hockey', 'Football', 'Cricket', 'BaseBall'],orientation = 'h'))
fig.show()