from unicodedata import name
from dash import Dash, html, dcc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
app = dash.Dash(name="app", sharing=True,server=server.server,url_base_pathname="/")
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
server = app.server
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port='80')

