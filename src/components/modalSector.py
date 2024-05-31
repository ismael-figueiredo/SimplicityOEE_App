import sqlite3

import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app

layout = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle([html.Strong("Cadastrar/Excluir setor")])),
        dbc.ModalBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Setor:")]),
                                dbc.Input(
                                    id="modal-sector-input-name",
                                    type="text",
                                    placeholder="Digite o setor",
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
                                    id="modal-sector-error-message",
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
                                    id="modal-sector-add-button",
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
                                                    id="modal-sector-select-delete",
                                                    options=[],
                                                    placeholder="Selecione um setor",
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
                                    id="modal-sector-delete-button",
                                ),
                            ],
                            title="Deseja deletar um setor?",
                        ),
                    ],
                    start_collapsed=True,
                    id="modal-sector-delete-accordion",
                ),
            ]
        ),
    ],
    id="modal-sector",
    backdrop="static",
    scrollable=True,
)


@app.callback(
    Output("modal-sector", "is_open"),
    [
        Input("open-modal-sector", "n_clicks"),
        Input("modal-sector-add-button", "n_clicks"),
    ],
    [State("modal-sector", "is_open")],
)
def toggle_sector_modal(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open
