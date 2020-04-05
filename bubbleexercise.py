import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv(r'C:/Users/noahw/Desktop/Intro Vis/mpg.csv')

type(df['horsepower'])

data = [go.Scatter(x=df['weight'], 
                    y=df['acceleration'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(size=2*df['mpg'],
                    color=df['cylinders'],
                    showscale=True))]

layout = go.Layout(title='Bubble Chart')

fig=go.Figure(data=data, layout=layout)
pyo.plot(fig)