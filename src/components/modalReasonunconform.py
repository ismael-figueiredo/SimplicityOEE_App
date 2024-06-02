import sqlite3

import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app

layout = dbc.Modal(
    [
        dbc.ModalHeader(
            dbc.ModalTitle([html.Strong("Cadastrar motivo de não conformidade")])
        ),
        dbc.ModalBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Motivo:")]),
                                dbc.Input(
                                    id="modal-reason-unconform-input-name",
                                    type="text",
                                    placeholder="Digite o motivo",
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
                                    id="modal-reason-unconform-error-message",
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
                                    id="modal-reason-unconform-add-button",
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
    id="modal-reason-unconform",
    backdrop="static",
    scrollable=True,
)


@app.callback(
    Output("modal-reason-unconform", "is_open"),
    [
        Input("open-modal-reason-unconform", "n_clicks"),
        Input("modal-reason-unconform-add-button", "n_clicks"),
    ],
    [State("modal-reason-unconform", "is_open")],
)
def toggle_reason_unconform_modal(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open
