from dash import dcc, html
import dash_daq as daq
import dash_bootstrap_components as dbc

# tab 1 - overblik
overblik = [
    html.P("This is tab 1.",
           style={
                "margin-top": "0px",
                "padding-top": "0px",
                "height": "536px",
                "backgroundColor": "#D8E1E8",
                "font-family": "Ubuntu"})
]

# tab 2 - fravær
absence = [
    dcc.Tabs(
        id="absence-tab",
        value="tab-2-skole",
        children=[
            dcc.Tab(
                label="SFO",
                value="tab-2-sfo",
                children=[
                    html.H1("SFO sygemelding", style={"text-align": "center", "font-size": "20px", "font-family": "Ubuntu"}),
                    dcc.Markdown(
                        """
                        Bemærk, at dit barn automatisk raskmeldes, så hvis dit barn fortsat er syg, skal
                        du registrere sygdom næste morgen.
                        """,
                        style={
                            "margin-left": "8px",
                            "margin-right": "8px",
                            "margin-top": "0px",
                            "padding-top": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                daq.BooleanSwitch(
                                    id="bw-1-1",
                                    on=False,
                                    color="#16425D",
                                    style={"text-align": "left", "padding-top": "12px", "margin-left": "25px"}
                                ),
                            ]),
                        ),
                        dbc.Col([
                            html.Button('-', id='button-1-1-dec', n_clicks=0, style={'display': 'inline-block', "margin-top": "12px"}),
                            html.H2(children='0', id='counter-1-1', style={"font-size": "16px", 'display': 'inline-block', 'margin': '0 10px', "padding-top": "12px"}),
                            html.Button('+', id='button-1-1-inc', n_clicks=0, style={'display': 'inline-block', "margin-top": "8px"})
                        ]),
                        dbc.Col(
                            dcc.Markdown("Barn 1", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                daq.BooleanSwitch(
                                    id="bw-1-2",
                                    on=False,
                                    color="#16425D",
                                    style={"text-align": "left", "padding-top": "12px", "margin-left": "25px"}
                                ),
                            ]),
                        ),
                        dbc.Col([
                            html.Button('-', id='button-1-2-dec', n_clicks=0, style={'display': 'inline-block', "margin-top": "12px"}),
                            html.H2(children='0', id='counter-1-2', style={"font-size": "16px", 'display': 'inline-block', 'margin': '0 10px', "padding-top": "12px"}),
                            html.Button('+', id='button-1-2-inc', n_clicks=0, style={'display': 'inline-block', "margin-top": "8px"})
                        ]),
                        dbc.Col(
                            dcc.Markdown("Barn 2", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                daq.BooleanSwitch(
                                    id="bw-1-3",
                                    on=False,
                                    color="#16425D",
                                    style={"text-align": "left", "padding-top": "12px", "margin-left": "25px"}
                                ),
                            ]),
                        ),
                        dbc.Col([
                            html.Button('-', id='button-1-3-dec', n_clicks=0, style={'display': 'inline-block', "margin-top": "12px"}),
                            html.H2(children='0', id='counter-1-3', style={"font-size": "16px", 'display': 'inline-block', 'margin': '0 10px', "padding-top": "12px"}),
                            html.Button('+', id='button-1-3-inc', n_clicks=0, style={'display': 'inline-block', "margin-top": "8px"})
                        ]),
                        dbc.Col(
                            dcc.Markdown("Barn 3", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dcc.Markdown(
                        """
                        Bemærkninger kan tilføjes i feltet nedenfor. Bemærk, hvis du ikke markerer et barn som syg.
                        Vil du der blot gives en besked i forbindelse med fravær der gør at barnet ikke kan være tilstede
                        ved hele undervisningen. (F.eks. tandlæge besøg.)
                        """,
                        style={
                            "margin-left": "8px",
                            "margin-right": "8px",
                            "margin-bottom": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dcc.Textarea(
                        id="text-area",
                        placeholder="Indtast kommentar",
                        style={"margin-left": "8px", 'width': '94%', 'height': 45},
                    ),
                    html.Div([
                        html.Button(
                            "Registrer fravær",
                            id="button",
                            n_clicks=0,
                        ),
                    ],
                        className="centered-button"
                    ),
                ],
                style={
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#F7F7F7",
                    "font-family": "Ubuntu"},
                selected_style={
                    "color": "white",
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#16425D",
                    "font-family": "Ubuntu"},
                className="custom-tabs-container",
                selected_className="custom-tab--selected"
            ),
            dcc.Tab(
                label="SKOLE",
                value="tab-2-skole",
                children=[
                    html.H1("Skole sygemelding", style={"text-align": "center", "font-size": "20px", "font-family": "Ubuntu"}),
                    dcc.Markdown(
                        """
                        Bemærk, at dit barn automatisk raskmeldes, så hvis dit barn fortsat er syg, skal
                        du registrere sygdom næste morgen.
                        """,
                        style={
                            "margin-left": "8px",
                            "margin-right": "8px",
                            "margin-bottom": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                daq.BooleanSwitch(
                                    id="bw-2-1",
                                    on=False,
                                    color="#16425D",
                                    style={"text-align": "left", "padding-top": "12px", "margin-left": "25px"}
                                ),
                            ]),
                        ),
                        dbc.Col([
                            html.Button('-', id='button-2-1-dec', n_clicks=0, style={'display': 'inline-block', "margin-top": "12px"}),
                            html.H2(children='0', id='counter-2-1', style={"font-size": "16px", 'display': 'inline-block', 'margin': '0 10px', "padding-top": "12px"}),
                            html.Button('+', id='button-2-1-inc', n_clicks=0, style={'display': 'inline-block', "margin-top": "8px"})
                        ]),
                        dbc.Col(
                            dcc.Markdown("Barn 1", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                daq.BooleanSwitch(
                                    id="bw-2-2",
                                    on=False,
                                    color="#16425D",
                                    style={"text-align": "left", "padding-top": "12px", "margin-left": "25px"}
                                ),
                            ]),
                        ),
                        dbc.Col([
                            html.Button('-', id='button-2-2-dec', n_clicks=0, style={'display': 'inline-block', "margin-top": "12px"}),
                            html.H2(children='0', id='counter-2-2', style={"font-size": "16px", 'display': 'inline-block', 'margin': '0 10px', "padding-top": "12px"}),
                            html.Button('+', id='button-2-2-inc', n_clicks=0, style={'display': 'inline-block', "margin-top": "8px"})
                        ]),
                        dbc.Col(
                            dcc.Markdown("Barn 2", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                daq.BooleanSwitch(
                                    id="bw-2-3",
                                    on=False,
                                    color="#16425D",
                                    style={"text-align": "left", "padding-top": "12px", "margin-left": "25px"}
                                ),
                            ]),
                        ),
                        dbc.Col([
                            html.Button('-', id='button-2-3-dec', n_clicks=0, style={'display': 'inline-block', "margin-top": "12px"}),
                            html.H2(children='0', id='counter-2-3', style={"font-size": "16px", 'display': 'inline-block', 'margin': '0 10px', "padding-top": "12px"}),
                            html.Button('+', id='button-2-3-inc', n_clicks=0, style={'display': 'inline-block', "margin-top": "8px"})
                        ]),
                        dbc.Col(
                            dcc.Markdown("Barn 3", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dcc.Markdown(
                        """
                        Bemærkninger kan tilføjes i feltet nedenfor. Bemærk, hvis du ikke markerer et barn som syg.
                        Vil du der blot gives en besked i forbindelse med fravær der gør at barnet ikke kan være tilstede
                        ved hele undervisningen. (F.eks. tandlæge besøg.)
                        """,
                        style={
                            "margin-left": "8px",
                            "margin-right": "8px",
                            "margin-bottom": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dcc.Textarea(
                        id="text-area",
                        placeholder="Indtast kommentar",
                        style={"margin-left": "8px", 'width': '94%', 'height': 45},
                    ),
                    html.Div([
                        html.Button(
                            "Registrer fravær",
                            id="button",
                            n_clicks=0,
                        ),
                    ],
                        className="centered-button"
                    ),
                ],
                style={
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#F7F7F7",
                    "font-family": "Ubuntu"},
                selected_style={
                    "color": "white",
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#16425D",
                    "font-family": "Ubuntu"},
                className="custom-tabs-container",
                selected_className="custom-tab--selected"
            ),
        ],
        style={
            "margin-bottom": "0px",
            "padding-bottom": "0px",
            "height": "30px",
        },
        className="custom-tabs-container",
    ),
]

# tab 3 - tid
time = [
    html.P("This is tab 3.",
           style={
                "margin-top": "0px",
                "height": "536px",
                "backgroundColor": "#D8E1E8",
                "font-family": "Ubuntu"}),
]