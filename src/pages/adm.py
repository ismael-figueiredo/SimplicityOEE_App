import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output

from app import *
from src.components import sidebar


def render_layout():
    layout = dbc.Container(
        children=[
            dbc.Row(
                [
                    dbc.Col([sidebar.layout], md=2),
                    dbc.Col([html.Div(id="page-content")], md=10),
                ]
            ),
        ],
        fluid=True,
        style={"padding": "0px"},
        className="dbc",
    )

    return layout
