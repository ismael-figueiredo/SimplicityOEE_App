from datetime import date, datetime, timedelta

import dash_bootstrap_components as dbc
import plotly.figure_factory as ff
from dash import dcc, html

from app import *

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H1(["Timeline de produção"]),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        dbc.Label(["Setor"]),
                                                        dcc.Dropdown(
                                                            id="filter_setor2",
                                                            value=[],
                                                            clearable=False,
                                                            multi=True,
                                                            options=[],
                                                        ),
                                                    ],
                                                    width=6,
                                                ),
                                                dbc.Col(
                                                    [
                                                        dbc.Label(["Máquina"]),
                                                        dcc.Dropdown(
                                                            id="filter_maquina2",
                                                            value=[],
                                                            clearable=False,
                                                            multi=True,
                                                            options=[],
                                                        ),
                                                    ],
                                                    width=6,
                                                ),
                                            ]
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        dbc.Row(
                                                            [
                                                                dbc.Label(["Período"]),
                                                            ]
                                                        ),
                                                        html.Div(
                                                            [
                                                                dcc.DatePickerRange(
                                                                    id="datapicker2",
                                                                    start_date_placeholder_text="Início",
                                                                    end_date_placeholder_text="Fim",
                                                                    start_date=datetime.combine(
                                                                        date.today(),
                                                                        datetime.min.time(),
                                                                    )
                                                                    + timedelta(
                                                                        hours=6
                                                                    ),
                                                                    end_date=datetime.combine(
                                                                        date.today(),
                                                                        datetime.min.time(),
                                                                    )
                                                                    + timedelta(
                                                                        hours=24
                                                                    ),
                                                                    style={
                                                                        "border": "0px solid black"
                                                                    },
                                                                )
                                                            ]
                                                        ),
                                                    ],
                                                    width=12,
                                                )
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            ],
            className="main_row g-2 my-auto",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        dcc.Graph(
                                            id="time-line",
                                            config={
                                                "displayModeBar": False,
                                                "showTips": False,
                                            },
                                        ),
                                    ],
                                    style={"padding-top": "10px"},
                                )
                            ]
                        )
                    ]
                )
            ],
            className="main_row g-2 my-auto",
        ),
    ],
    fluid=True,
    style={"width": "100%", "height": "100%", "padding-bottom": "10px"},
)
