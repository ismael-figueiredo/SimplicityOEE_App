import hashlib

import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from flask_login import login_user

from app import *

card_style = {
    "width": "300px",
    "min-height": "300px",
    "padding-top": "25px",
    "padding-right": "25px",
    "padding-left": "25px",
    "margin": "auto",
}


def render_layout():

    login = dbc.Card(
        [
            html.Div(
                [
                    html.Img(
                        src="/assets/logo.png",
                        className="justify-content-center",
                        style={
                            "width": "150px",
                            "height": "150px",
                            "margin-left": "7px",
                        },
                    ),
                ],
                style={"padding": "30px"},
            ),
            dbc.Input(id="user_login", placeholder="Nome de usuário", type="text"),
            html.Br(),
            dbc.Input(id="pwd_login", placeholder="Senha", type="password"),
            html.Br(),
            dbc.Button("Login", id="login_button"),
            html.Span(id="error_login", style={"text-align": "center"}),
            html.Br(),
            html.Span(
                "Simplicity MES App V 1.0 ©CreatedBy IsmaelFigueiredo",
                style={
                    "text-align": "center",
                    "font-size": "10px",
                    "margin": "2px",
                    "font-style": "italic",
                },
            ),
        ],
        style=card_style,
    )
    return login


# =========  Callbacks Page1  =========== #
@app.callback(
    Output("login-state", "data"),
    Output("error_login", "children"),  
    Input("login_button", "n_clicks"),
    [State("user_login", "value"), State("pwd_login", "value")],
)
def successful(n_clicks, username, password):
    if n_clicks is None:
        raise PreventUpdate

    user = Users.query.filter_by(name=username).first()
    if user and password is not None:
        # Criptografar a senha fornecida para comparação
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == user.password:
            login_user(user)
            return "success", "success"  
        else:
            return "error", "Usuário ou senha incorretos."
    else:
        return "error", "Usuário ou senha incorretos."
