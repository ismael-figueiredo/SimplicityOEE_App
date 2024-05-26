import dash_bootstrap_components as dbc
from dash import dcc, html

layout = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(["Dashboard "]),
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        [
                                                            dbc.Label(["Setor"]),
                                                            dcc.Dropdown(
                                                                id="filter_setor",
                                                                value=([]),
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
                                                                id="filter_maquina",
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
                                                                    dbc.Label(
                                                                        ["Período"]
                                                                    ),
                                                                ]
                                                            ),
                                                            html.Div(
                                                                [
                                                                    dcc.DatePickerRange(
                                                                        id="datapicker1",
                                                                        start_date_placeholder_text="Início",
                                                                        end_date_placeholder_text="Fim",
                                                                        display_format="DD MM YYYY",
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
                                            html.H6("Qnt Produzida"),
                                            dcc.Graph(
                                                id="card-graph1",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                            html.Div(
                                                id="qnt_produzida_text",
                                                children=[],
                                                style={
                                                    "fontSize": "20px",
                                                    "textAlign": "center",
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=2,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H6("Qnt Rejeitada"),
                                            dcc.Graph(
                                                id="card-graph3",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                            html.Div(
                                                id="refugo_text",
                                                children=[],
                                                style={
                                                    "fontSize": "20px",
                                                    "textAlign": "center",
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=2,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H6("Hrs Setup"),
                                            dcc.Graph(
                                                id="card-graph2",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                            html.Div(
                                                id="hrs_setup_text",
                                                children=[],
                                                style={
                                                    "fontSize": "20px",
                                                    "textAlign": "center",
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=2,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H6("Hrs Paradas"),
                                            dcc.Graph(
                                                id="card-graph4",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                            html.Div(
                                                id="hrs_paradas_text",
                                                children=[],
                                                style={
                                                    "fontSize": "20px",
                                                    "textAlign": "center",
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=2,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H6("Hrs Produtivas"),
                                            dcc.Graph(
                                                id="card-graph5",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                            html.Div(
                                                id="hrs_produtivas_text",
                                                children=[],
                                                style={
                                                    "fontSize": "20px",
                                                    "textAlign": "center",
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=2,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H6("Hrs Disponiveis"),
                                            dcc.Graph(
                                                id="card-graph6",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                            html.Div(
                                                id="hrs_disponiveis_text",
                                                children=[],
                                                style={
                                                    "fontSize": "20px",
                                                    "textAlign": "center",
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=2,
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
                                            html.H3("OEE"),
                                            dcc.Graph(
                                                id="oee-graph",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=3,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H3("Performace"),
                                            dcc.Graph(
                                                id="performace-graph",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=3,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H3("Disponibilidade"),
                                            dcc.Graph(
                                                id="disp-graph",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=3,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H3("Qualidade"),
                                            dcc.Graph(
                                                id="quali-graph",
                                                config={
                                                    "displayModeBar": False,
                                                    "showTips": False,
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=3,
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
                                            dbc.Accordion(
                                                [
                                                    dbc.AccordionItem(
                                                        [
                                                            html.H4("OEE"),
                                                            html.P(
                                                                "OEE, ou Eficiência Geral dos Equipamentos (em inglês, Overall Equipment Effectiveness), é uma métrica padrão que avalia o quão bem um sistema de manufatura está funcionando. É usado principalmente em ambientes industriais para monitorar e melhorar a eficiência da produção."
                                                            ),
                                                            html.P(
                                                                "A fórmula para calcular o OEE é:"
                                                            ),
                                                            html.P(
                                                                "OEE = Disponibilidade × Performance × Qualidade",
                                                                style={
                                                                    "margin-left": "20px"
                                                                },
                                                            ),
                                                            html.Hr(),
                                                            html.H4("Disponibilidade"),
                                                            html.P(
                                                                "A disponibilidade nos diz quanto tempo o equipamento produziu em relação ao tempo total disponível para produção:"
                                                            ),
                                                            html.P(
                                                                "Disponibilidade% = (Tempo produzindo / Tempo programado para produzir) * 100%",
                                                                style={
                                                                    "margin-left": "20px"
                                                                },
                                                            ),
                                                            html.P(
                                                                "Quanto maior o tempo produzindo, maior a disponibilidade. Quanto menor a disponibilidade, maior é o tempo que o equipamento ficou parado."
                                                            ),
                                                            html.Hr(),
                                                            html.H4("Performance"),
                                                            html.P(
                                                                "A performance nos diz quão bem o equipamento produziu, enquanto estava produzindo, e está relacionado com a velocidade de operação do equipamento:"
                                                            ),
                                                            html.P(
                                                                "Performance% = (Tempo Ciclo Padrão / Tempo Ciclo Real) * 100%",
                                                                style={
                                                                    "margin-left": "20px"
                                                                },
                                                            ),
                                                            html.P(
                                                                "A Performance instantânea do equipamento pode ser medida comparando o tempo ciclo real com o tempo ciclo padrão."
                                                            ),
                                                            html.Hr(),
                                                            html.H4("Qualidade"),
                                                            html.P(
                                                                "A qualidade nos diz a qualidade daquilo que saiu da máquina, ou seja, quantos itens bons foram produzidos em relação ao total de itens produzidos:"
                                                            ),
                                                            html.P(
                                                                "Qualidade% = (Quantidade de Bons / Quantidade Total Produzida) * 100%",
                                                                style={
                                                                    "margin-left": "20px"
                                                                },
                                                            ),
                                                            html.P(
                                                                "A qualidade somente será 100% quando Quantidade de Ruins for igual à ZERO. Itens retrabalhados ou reclassificados não são considerados bons."
                                                            ),
                                                        ],
                                                        title="Informações sobre OEE (Eficiência Geral dos Equipamentos)",
                                                    ),
                                                ],
                                                start_collapsed=True,
                                                style={"background-color": "#303030"},
                                            )
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
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
                                            html.H3("Refugo por motivo"),
                                            dcc.Graph(
                                                id="refugo-fig",
                                                config={
                                                    "displayModeBar": True,
                                                    "showTips": True,
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H3("Paradas por motivo"),
                                            dcc.Graph(
                                                id="paradas-fig",
                                                config={
                                                    "displayModeBar": True,
                                                    "showTips": True,
                                                },
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        width=6,
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
                                            html.H3("Produção"),
                                            dcc.Graph(
                                                id="line-graph",
                                                config={
                                                    "displayModeBar": True,
                                                    "showTips": True,
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
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H3("Produção real X Produção teórica"),
                                            dcc.Graph(
                                                id="line-graph-comp",
                                                config={
                                                    "displayModeBar": True,
                                                    "showTips": True,
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
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H3("Paradas"),
                                            dcc.Graph(
                                                id="line-graph1",
                                                config={
                                                    "displayModeBar": True,
                                                    "showTips": True,
                                                },
                                            ),
                                        ],
                                        style={"padding-top": "10px"},
                                    )
                                ]
                            )
                        ],
                        width=12,
                    )
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
                                            html.H3("Ocorrências"),
                                            dcc.Graph(
                                                id="line-graph3",
                                                config={
                                                    "displayModeBar": True,
                                                    "showTips": True,
                                                },
                                            ),
                                        ],
                                        style={"padding-top": "10px"},
                                    )
                                ]
                            )
                        ],
                        width=12,
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
                                            html.H3("Setup"),
                                            dcc.Graph(
                                                id="line-graph2",
                                                config={
                                                    "displayModeBar": True,
                                                    "showTips": True,
                                                },
                                            ),
                                        ],
                                    )
                                ]
                            )
                        ],
                        width=12,
                    ),
                ],
                className="main_row g-2 my-auto",
            ),
        ],
        fluid=True,
    )
)

