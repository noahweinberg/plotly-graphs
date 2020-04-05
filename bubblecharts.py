import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv(r'C:/Users/noahw/Desktop/Intro Vis/mpg.csv')

data = [go.Scatter(x=df['horsepower'], 
                    y=df['mpg'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(size=2*df['weight']/300,
                    color=df['cylinders'],
                    showscale=True))]

layout = go.Layout(title='Bubble Chart')

fig=go.Figure(data=data, layout=layout, hovermode='closest')
pyo.plot(fig)