import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv(r'C:/Users/noahw/Desktop/Intro Vis/2018WinterOlympics.csv')
print(df.head())


trace1 = go.Bar(x=df['NOC'], y=df['Gold'], 
                name='Gold', marker={'color':'#d4af37'})


trace2 = go.Bar(x=df['NOC'], y=df['Silver'], 
                name='Silver', marker={'color':'#bec2cb'})


trace3 = go.Bar(x=df['NOC'], y=df['Bronze'], 
                name='Bronze', marker={'color':'#804a00'})


data = [trace1, trace2, trace3]
layout = go.Layout(title='Medals',barmode='stack')
fig = go.Figure(data=data,layout=layout)

pyo.plot(fig)