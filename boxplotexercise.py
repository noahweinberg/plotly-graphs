import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 
import numpy as np 

df = pd.read_csv(r'C:/Users/noahw/Desktop/Intro Vis/abalone.csv')


np.random.choice(df['rings'], 10, replace=False)