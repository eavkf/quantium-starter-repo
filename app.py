from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('data/daily_sales_data.csv')
fig = px.line(df, x='date', y='sales')

app.layout = html.Div(children=[
    html.H1(children='Sales of Pink Morsel Over Time'),
    dcc.Graph(
        id='pinkmorsel-over-time',
        figure=fig
    )
])

app.run()
