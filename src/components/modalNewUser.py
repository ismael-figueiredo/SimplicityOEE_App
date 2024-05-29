import sqlite3
import time

import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import *

layout = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle([html.Strong("Cadastrar/Excluir Usuário")])),
        dbc.ModalBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Setor:")]),
                                dbc.Select(
                                    id="mnu-add-sector",
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
                                dbc.Label([html.Strong("Acesso:")]),
                                dbc.Select(
                                    id="mnu-add-role",
                                    options=[
                                        {
                                            "label": "Administrador",
                                            "value": "admin",
                                        },
                                        {
                                            "label": "Operador",
                                            "value": "operator",
                                        },
                                    ],
                                    placeholder="Selecione um nível de acesso",
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
                                dbc.Label([html.Strong("Nome:")]),
                                dbc.Input(
                                    id="mnu-add-name",
                                    type="text",
                                    placeholder="Digite o nome",
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
                                html.P(
                                    id="mnu-error-message",
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
                                    href="/refresh",
                                    class_name="btn btn-success btn-lg",
                                    id="mnu-add-user",
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
                                                dbc.Label([html.Strong("Setor:")]),
                                                dbc.Select(
                                                    id="mnu-delete-sector",
                                                    options=[],
                                                    placeholder="Selecione um setor",
                                                ),
                                            ],
                                            width=6,
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Label(
                                                    [html.Strong("Funcionário:")]
                                                ),
                                                dbc.Select(
                                                    id="mnu-select-delete-user",
                                                    options=[],
                                                    placeholder="Selecione um funcionário",
                                                ),
                                            ],
                                            width=6,
                                        ),
                                    ]
                                ),
                                html.Br(),
                                dbc.Button(
                                    "Deletar",
                                    color="warning",
                                    id="mnu-delete-user",
                                ),
                            ],
                            title="Deseja deletar um funcionário?",
                        ),
                    ],
                    start_collapsed=True,
                    id="delete-user",
                ),
            ]
        ),
    ],
    id="modal-new-user",
    backdrop="static",
    scrollable=True,
)


import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from app import app


@app.callback(
    Output("modal-new-user", "is_open"),
    [Input("open-modal-new-user", "n_clicks"), Input("mnu-delete-user", "n_clicks")],
    [State("modal-new-user", "is_open")],
)
def toggle_modal_new_user(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open
   
