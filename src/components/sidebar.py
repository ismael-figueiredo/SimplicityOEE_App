import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from flask_login import logout_user

from app import *

layout = dbc.Card(
    [
        html.Div(id="div-ghost"),
        html.Img(
            src="/assets/logo.png",
            className="align-self-center",
            style={
                "width": "150px",
                "height": "150px",
            },
        ),
        html.P(
            "Simplicity MES App",
            className="text-center",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
                dbc.NavLink("Time-line", href="/timeline", active="exact"),
                dbc.NavLink("Usuários", id="open-modal-user", active="exact"),
                dbc.NavLink("Setores", id="open-modal-sector", active="exact"),
                dbc.NavLink(
                    "Máquinas",
                    id="open-modal-machine",
                    active="exact",
                ),
                dbc.NavLink("Tempos", active="exact"),
                dbc.NavLink("sair", id="logout", href="/login", active="exact"),
            ],
            vertical=True,
            pills=True,
            id="nav_buttons",
            style={"margin-bottom": "50px"},
        ),
    ],
    style={"width": "100%", "margin-top": "8px"},
)


@app.callback(Output("div-ghost", "children"), [Input("logout", "n_clicks")])
def logout(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    logout_user()
    return ""
