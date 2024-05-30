import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app

layout = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle(html.Strong("Cadastrar/Excluir Usuário"))),
        dbc.ModalBody(
            [
                dbc.Row(
                    dbc.Col(
                        [
                            dbc.Label(html.Strong("Setor:")),
                            dbc.Select(
                                id="new-user-modal-sector-select",
                                options=[],
                                placeholder="Selecione um setor",
                            ),
                        ],
                        width=8,
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            dbc.Label(html.Strong("Acesso:")),
                            dbc.Select(
                                id="new-user-modal-role-select",
                                options=[
                                    {"label": "Administrador", "value": "admin"},
                                    {"label": "Operador", "value": "operator"},
                                ],
                                placeholder="Selecione um nível de acesso",
                            ),
                        ],
                        width=8,
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            dbc.Label(html.Strong("Nome:")),
                            dbc.Input(
                                id="new-user-modal-name-input",
                                type="text",
                                placeholder="Digite o nome",
                            ),
                        ],
                        width=8,
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        html.P(
                            id="new-user-modal-error-message",
                            style={"display": "none", "color": "red"},
                        ),
                        width=12,
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            html.Br(),
                            dbc.Button(
                                "Adicionar",
                                href="/refresh",
                                color="success",
                                id="new-user-modal-add-btn",
                                style={"margin-bottom": "20px"},
                            ),
                        ],
                        width=4,
                    )
                ),
                dbc.Accordion(
                    dbc.AccordionItem(
                        [
                            dbc.Alert(
                                "Deletar pode afetar o funcionamento da aplicação!",
                                color="danger",
                                dismissable=True,
                                is_open=True,
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            dbc.Label(html.Strong("Setor:")),
                                            dbc.Select(
                                                id="new-user-modal-delete-sector-select",
                                                options=[],
                                                placeholder="Selecione um setor",
                                            ),
                                        ],
                                        width=6,
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Label(html.Strong("Funcionário:")),
                                            dbc.Select(
                                                id="new-user-modal-delete-user-select",
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
                                id="new-user-modal-delete-btn",
                            ),
                        ],
                        title="Deseja deletar um funcionário?",
                    ),
                    start_collapsed=True,
                    id="new-user-modal-delete-accordion",
                ),
            ]
        ),
    ],
    id="new-user-modal",
    backdrop="static",
    scrollable=True,
)


@app.callback(
    Output("new-user-modal", "is_open"),
    [
        Input("open-new-user-modal-btn", "n_clicks"),
        Input("new-user-modal-delete-btn", "n_clicks"),
    ],
    [State("new-user-modal", "is_open")],
)
def toggle_new_user_modal(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open
