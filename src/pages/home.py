import dash_bootstrap_components as dbc
from dash import html


def render_layout(login_state):
    template = dbc.Container(children=[html.H1("home")], style={"margin": "20px"})

    return template


#
