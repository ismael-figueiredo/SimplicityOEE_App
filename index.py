import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from flask_login import LoginManager, current_user

from app import *
from src.pages import home, login

login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = "/login"


# =========  Layout  =========== #
app.layout = html.Div(
    children=[
        dcc.Loading(id="loading-icon", children=[], type="circle", fullscreen=True),
        dcc.Store(id="url-value-store"),
        dcc.Store(id="login-state", data=""),
        dcc.Store(id="register-state", data=""),
        dcc.Location(id="base-url", refresh=False),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            id="page-content",
                            children=[html.H1("Simple OEE Aplication")],
                            style={
                                "height": "100vh",
                                "display": "flex",
                                "justify-content": "center",
                            },
                        )
                    ]
                ),
            ]
        ),
    ],
    style={
        "height": "100vh",
    },
)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.callback(
    Output("base-url", "pathname"),
    [Input("login-state", "data")],
)
def render_page_content(login_state):
    ctx = dash.callback_context
    if ctx.triggered:
        trigg_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if trigg_id == "login-state" and login_state == "success":
            return "/"
        if trigg_id == "login-state" and login_state == "error":
            return "/login"


@app.callback(
    Output("page-content", "children"),
    Input("base-url", "pathname"),
    [State("login-state", "data")],
)
def render_page_content(pathname, login_state):
    if pathname == "/login":
        return login.render_layout(login_state)

    if pathname == "/home" or pathname == "/":
        if current_user.is_authenticated:
            return home.render_layout(login_state)
        else:
            return login.render_layout(login_state)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8052, debug=True)
