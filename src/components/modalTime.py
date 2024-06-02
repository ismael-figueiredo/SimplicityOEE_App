import re
import sqlite3
from datetime import datetime

import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app

# ========= Layout ========= #
layout = dbc.Modal(
    [
        dbc.ModalHeader(
            dbc.ModalTitle([html.Strong("Cadastrar novo tempo por operação")])
        ),
        dbc.ModalBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Setor:")]),
                                dbc.Select(
                                    id="modal-time-select-sector",
                                    options=[],
                                    placeholder="Selecione um setor",
                                ),
                            ],
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Máquina:")]),
                                dbc.Select(
                                    id="modal-time-select-machine",
                                    placeholder="Selecione a máquina",
                                    options=[],
                                ),
                            ],
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Operação:")]),
                                dbc.Select(
                                    id="modal-time-select-operation",
                                    placeholder="Selecione a operação",
                                    options=[],
                                ),
                            ],
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Item:")]),
                                dbc.Input(
                                    id="modal-time-input-item",
                                    type="number",
                                    placeholder="Digite o código",
                                    maxLength=6,
                                ),
                            ],
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Tempo:")]),
                                dbc.Input(
                                    id="modal-time-imput-time",
                                    type="text",
                                    placeholder="Digite o tempo",
                                    minLength=8,
                                ),
                            ],
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P(
                                    id="modal-time-error-message",
                                    style={"display": "none", "color": "red"},
                                ),
                            ],
                            width=12,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Row([html.Br()]),
                                dbc.Button(
                                    "Adicionar",
                                    class_name="btn btn-success btn-lg",
                                    id="modal-time-add-button",
                                    style={"margin-bottom": "20px"},
                                ),
                            ],
                            width=4,
                        ),
                    ]
                ),
            ]
        ),
    ],
    id="modal-time",
    backdrop="static",
    scrollable=True,
)


@app.callback(
    Output("modal-time", "is_open"),
    [
        Input("open-modal-time", "n_clicks"),
        Input("modal-time-add-button", "n_clicks"),
    ],
    [State("modal-time", "is_open")],
)
def toggle_time_modal(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open


@app.callback(
    Output("modal-time-imput-time", "value"), [Input("modal-time-imput-time", "value")]
)
def update_output(value):
    if value is not None and value != "":
        # Remove todos os caracteres que não sejam dígitos
        value = re.sub(r"\D", "", value)

        # Limita a entrada a 6 dígitos (HHMMSS)
        value = value[:6]

        if len(value) > 4:
            value = (
                value[:2] + ":" + value[2:4] + ":" + value[4:]
            )  # Formata como HH:MM:SS
        elif len(value) > 2:
            value = value[:2] + ":" + value[2:]  # Formata como HH:MM
        else:
            value = value  # Deixa como está se tiver 2 dígitos ou menos
    else:
        value = ""  # Valor inicial se não houver entrada

    return value
