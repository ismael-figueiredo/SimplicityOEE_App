import dash_bootstrap_components as dbc
from dash import html


def render_layout():
    layout = (
        dbc.Container(
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Header(
                                    children=[
                                        html.A(
                                            html.I(
                                                className="fa fa-angle-double-left",
                                                id="back-home",
                                            ),
                                            href="/home",
                                        ),
                                        html.H1(
                                            [html.Strong("Produção")],
                                            style={"textAlign": "center"},
                                        ),
                                        html.Img(
                                            src="/assets/logo.png",
                                            style={
                                                "height": "50px",
                                                "width": "50px",
                                            },
                                        ),
                                    ],
                                    style={
                                        "display": "flex",
                                        "justify-content": "space-between",
                                    },
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    className="tabela",
                                                    id="table-production-container",
                                                    children=[],
                                                ),
                                                html.Div(
                                                    id="text-production",
                                                    children=[],
                                                    style={
                                                        "fontSize": "15px",
                                                        "textAlign": "center",
                                                    },
                                                ),
                                                html.Div(
                                                    id="texte-production-2",
                                                    children=[],
                                                    style={
                                                        "fontSize": "15px",
                                                        "textAlign": "center",
                                                    },
                                                ),
                                                html.Div(
                                                    id="text-production-3",
                                                    children=[],
                                                    style={
                                                        "fontSize": "15px",
                                                        "textAlign": "center",
                                                    },
                                                ),
                                                dbc.Row(html.Br()),
                                                html.Div(id="table", children=[]),
                                                dbc.Row(
                                                    [
                                                        html.Div(
                                                            className="cronometro",
                                                            id="cronometro-container",
                                                            children=[],
                                                            style={
                                                                "position": "relative",
                                                                "width": "500px",
                                                                "height": "150px",
                                                                "display": "flex",
                                                                "align-items": "center",
                                                                "padding": "10px",
                                                                "width": "100%",
                                                                "height": "100%",
                                                            },
                                                        ),
                                                    ]
                                                ),
                                                dbc.Row(html.Br()),
                                                dbc.Row(
                                                    [
                                                        dbc.Button(
                                                            color="warning",
                                                            id="open-nao-conformidade",
                                                            children=[
                                                                "Não conformidade"
                                                            ],
                                                            style={
                                                                "font-size": "18px",
                                                                "height": "70px",
                                                                "font-weight": "bold",
                                                                "width": "100%",
                                                            },
                                                        ),
                                                    ],
                                                ),
                                                dbc.Row(
                                                    [
                                                        html.Br(),
                                                    ]
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Button(
                                                            "Encerrar produção",
                                                            id="open-saida-producao",
                                                            color="danger",
                                                            className="btn-lg",
                                                            style={
                                                                "font-size": "20px",
                                                                "height": "70px",
                                                                "font-weight": "bold",
                                                            },
                                                        ),
                                                    ],
                                                ),
                                                html.Br(),
                                                dbc.Row(
                                                    [
                                                        dbc.Button(
                                                            "Instrução de trabalho",
                                                            id="open-modal-IT-pr",
                                                            color="primary",
                                                            className="btn-lg",
                                                        ),
                                                    ],
                                                    style={
                                                        "margin-bottom": "20px",
                                                    },
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        )
                    ]
                ),
            ],
            id="producao-content",
            style={
                "display": "flex",
                "padding-top": "1rem",
                "align-self": "start",
                "flex-direction": "column",
                "width": "100%",
            },
        ),
    )
    return layout
