import dash_bootstrap_components as dbc
from dash import dcc, html

from app import *

dash.register_page(__name__)


def render_layout():
    template = dbc.Container(
        children=[
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    html.Div(
                                        [
                                            html.Legend(
                                                [
                                                    html.Strong(f"Usuário: "),
                                                    html.Span("ismael"),
                                                    html.Strong("Máquina: "),
                                                    html.Span("Torno 1"),
                                                ],
                                                style={
                                                    "display": "flex",
                                                    "gap": "1rem",
                                                },
                                            ),
                                            html.Legend(
                                                [
                                                    dcc.Link("Sair", href="#"),
                                                ],
                                                style={
                                                    "justify-content": "end",
                                                    "display": "flex",
                                                    "gap": "1rem",
                                                },
                                            ),
                                        ],
                                        style={
                                            "justify-content": "space-between",
                                            "display": "flex",
                                            "gap": "1rem",
                                        },
                                    ),
                                ]
                            ),
                            dbc.Row(
                                [
                                    html.Div(
                                        [
                                            html.Img(
                                                src="/assets/logo.png",
                                                className="justify-content-center",
                                                style={
                                                    "width": "180px",
                                                    "height": "180px",
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "textAlign": "center",
                                        },
                                    )
                                ]
                            ),
                            dbc.Row(
                                [
                                    html.P(
                                        id="error-message-title",
                                        style={"display": "none", "color": "red"},
                                    ),
                                    dbc.Button(
                                        "Produção",
                                        id="open-producao",
                                        color="success",
                                        className="btn-lg justify-content-center",
                                        style={
                                            "font-size": "50px",
                                            "height": "100px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                ]
                            ),
                            dbc.Row([html.Br()]),
                            dbc.Row(
                                [
                                    dbc.Button(
                                        "Setup",
                                        href="#",
                                        color="warning",
                                        class_name="btn-lg ",
                                        style={
                                            "font-size": "50px",
                                            "height": "100px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                ]
                            ),
                            dbc.Row([html.Br()]),
                            dbc.Row(
                                [
                                    dbc.Button(
                                        "Paradas",
                                        href="#",
                                        color="danger",
                                        class_name="btn-lg ",
                                        style={
                                            "font-size": "50px",
                                            "height": "100px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                ]
                            ),
                            dbc.Row([html.Br()]),
                            dbc.Row(
                                [
                                    dbc.Button(
                                        "Consulta",
                                        href="#",
                                        color="info",
                                        class_name="btn-lg ",
                                        style={
                                            "font-size": "50px",
                                            "height": "100px",
                                            "font-weight": "bold",
                                        },
                                    ),
                                ]
                            ),
                        ]
                    )
                ],
                style={"margin": "20px"},
            ),
        ]
    )
    return template
