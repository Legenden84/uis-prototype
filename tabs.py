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
                    html.H1("SFO sygemelding", style={"text-align": "center", "font-family": "Ubuntu"}),
                    dcc.Markdown(
                        """
                        Bemærk, at dit barn automatisk raskmeldes, så hvis dit barn fortsat er syg, skal
                        du registrere sygdom næste morgen.
                        """,
                        style={
                            "margin-left": "5px",
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
                        dbc.Col(
                            dcc.Markdown("Barn 3", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dcc.Markdown(
                        """
                        Eventuelle bemærkninger kan skrives i besked feltet nedenfor.
                        """,
                        style={
                            "margin-left": "5px",
                            "margin-bottom": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dcc.Textarea(
                        id="text-area",
                        value="Kommentar felt.",
                        style={"margin-left": "8px", 'width': '94%', 'height': 95},
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
                    html.H1("Skole sygemelding", style={"text-align": "center", "font-family": "Ubuntu"}),
                    dcc.Markdown(
                        """
                        Bemærk, at dit barn automatisk raskmeldes, så hvis dit barn fortsat er syg, skal
                        du registrere sygdom næste morgen.
                        """,
                        style={
                            "margin-left": "5px",
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
                        dbc.Col(
                            dcc.Markdown("Barn 3", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dcc.Markdown(
                        """
                        Eventuelle bemærkninger kan skrives i besked feltet nedenfor.
                        """,
                        style={
                            "margin-left": "5px",
                            "margin-bottom": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dcc.Textarea(
                        id="text-area",
                        value="Kommentar felt.",
                        style={"margin-left": "8px", 'width': '94%', 'height': 95},
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