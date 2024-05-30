import sqlite3
import time

import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import *

layout = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle([html.Strong("Cadastrar/Excluir máquina")])),
        dbc.ModalBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Setor:")]),
                                dbc.Select(
                                    id="modal-machine-sector-select",
                                    options=[],
                                    placeholder="Selecione um setor",
                                ),
                            ],
                            width=8,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Máquina:")]),
                                dbc.Input(
                                    id="modal-machine-name-input",
                                    type="text",
                                    placeholder="Digite o nome da máquina",
                                ),
                            ],
                            width=8,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Loading(
                                    id="modal-machine-loading-add",
                                    type="default",
                                    children=html.Div(id="modal-machine-add-output"),
                                    fullscreen=True,
                                ),
                                dcc.Loading(
                                    id="modal-machine-loading-delete",
                                    type="default",
                                    children=html.Div(id="modal-machine-delete-output"),
                                    fullscreen=True,
                                ),
                                html.P(
                                    id="modal-machine-error-msg",
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
                                html.Br(),
                                dbc.Button(
                                    "Adicionar",
                                    class_name="btn btn-success btn-lg",
                                    id="modal-machine-add-button",
                                    style={"margin-bottom": "20px"},
                                ),
                            ],
                            width=4,
                        ),
                    ]
                ),
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            [
                                dbc.Alert(
                                    "Deletar pode afetar o funcionamento da aplicação!",
                                    dismissable=True,
                                    is_open=True,
                                    color="danger",
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Label([html.Strong("Máquina:")]),
                                                dbc.Select(
                                                    id="modal-machine-select-delete",
                                                    options=[],
                                                    placeholder="Selecione uma máquina para deletar",
                                                ),
                                            ],
                                            width=8,
                                        ),
                                    ]
                                ),
                                html.Br(),
                                dbc.Button(
                                    "Deletar",
                                    color="warning",
                                    id="modal-machine-delete-button",
                                ),
                            ],
                            title="Deseja deletar uma máquina?",
                        ),
                    ],
                    start_collapsed=True,
                    id="modal-machine-delete-accordion",
                ),
            ]
        ),
    ],
    id="modal-machine",
    backdrop="static",
    scrollable=True,
)


@app.callback(
    Output("modal-machine", "is_open"),
    [
        Input("open-modal-machine", "n_clicks"),
        Input("modal-machine-delete-button", "n_clicks"),
    ],
    [State("modal-machine", "is_open")],
)
def toggle_new_user_modal(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open
