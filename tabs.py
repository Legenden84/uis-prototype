from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_daq as daq

from help import *
import support_functions as sf


# tab 1 - overblik
overblik = [
    html.P("This is tab 1.",
           style={
                "margin-top": "0px",
                "padding-top": "0px",
                "height": "536px",
                "backgroundColor": "#D8E1E8",
                "font-family": "Liberation Sans",})
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
                    html.Div([
                        html.H1("SFO sygemelding", style={"display": "inline-block", "text-align": "center", "font-size": "20px", "font-family": "Liberation Sans",}),
                        modal_open_sfo, modal_sfo,
                    ], style={"display": "flex", "justify-content": "space-between", "margin-left": "8px"}),
                    top_remark,
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-1-1")
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-1-1",
                            children=[
                                sf.create_dec_button("1-1"),
                                sf.create_counter("1-1"),
                                sf.create_inc_buttons("1-1"),
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 1", style={"font-family": "Liberation Sans", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        html.Div(
                            id="range-slider-div-1-1",
                            children=[
                                dcc.RangeSlider(min=12, max=17, step=1,
                                                value=[12, 17],
                                                id="range-slider-1-1",
                                                marks={
                                                    i: {
                                                        "label": str(i),
                                                        "style": {"color": "#16425D"},
                                                    } for i in range(18)
                                                },
                                                className="range-slider"),
                        ], style={"display": "None"}),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-1-2")
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-1-2",
                            children=[
                                sf.create_dec_button("1-2"),
                                sf.create_counter("1-2"),
                                sf.create_inc_buttons("1-2")
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 2", style={"font-family": "Liberation Sans", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        html.Div(
                            id="range-slider-div-1-2",
                            children=[
                                dcc.RangeSlider(min=12, max=17, step=1,
                                                value=[12, 17],
                                                id="range-slider-1-2",
                                                marks={
                                                    i: {
                                                        "label": str(i),
                                                        "style": {"color": "#16425D"},
                                                    } for i in range(18)
                                                },
                                                className="range-slider"),
                            ]),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-1-3"),
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-1-3",
                            children=[
                                sf.create_dec_button("1-3"),
                                sf.create_counter("1-3"),
                                sf.create_inc_buttons("1-3"),
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 3", style={"font-family": "Liberation Sans", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        html.Div(
                            id="range-slider-div-1-3",
                            children=[
                                dcc.RangeSlider(min=12, max=17, step=1,
                                                value=[12, 17],
                                                id="range-slider-1-3",
                                                marks={
                                                    i: {
                                                        "label": str(i),
                                                        "style": {"color": "#16425D"},
                                                    } for i in range(18)
                                                },
                                                className="range-slider"),
                        ]),
                    ]),
                    html.Div([
                        bottom_remark,
                        dcc.Textarea(
                            id="text-area-sfo",
                            placeholder="Indtast kommentar",
                            style={"margin-left": "8px", "width": "353px", "height": 95},
                        ),
                        html.Div([
                            html.Button(
                                "Registrer fravær",
                                id="button-sfo",
                                n_clicks=0,
                                className="centered-button",
                                style={"padding-top": "4px", "align-text": "center"}
                            ),
                        ],
                            style={"display": "flex", "justify-content": "center"}
                            ),
                        ], style={
                            "align-text": "center",
                            "position": "absolute",
                            "margin-bottom": "8px",
                            "bottom": "0",
                        }
                    ),
                ],
                style={
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#F7F7F7",
                    "font-family": "Liberation Sans", "font-weight": "bold"},
                selected_style={
                    "color": "white",
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#16425D",
                    "font-family": "Liberation Sans", "font-weight": "bold"},
                className="custom-tabs-container",
                selected_className="custom-tab--selected"
            ),
            dcc.Tab(
                label="SKOLE",
                value="tab-2-skole",
                children=[
                    html.Div([
                        html.H1("Skole sygemelding", style={"display": "inline-block", "text-align": "center", "font-size": "20px", "font-family": "Liberation Sans"}),
                        modal_open_skole, modal_skole,
                    ], style={"display": "flex", "justify-content": "space-between", "margin-left": "8px"}),
                    top_remark,
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-2-1"),
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-2-1",
                            children=[
                                sf.create_dec_button("2-1"),
                                sf.create_counter("2-1"),
                                sf.create_inc_buttons("2-1"),
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 1", style={"font-family": "Liberation Sans",  "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        html.Div(
                            id="range-slider-div-2-1",
                            children=[
                                dcc.RangeSlider(min=8, max=15, step=1,
                                                value=[8, 15],
                                                id="range-slider-2-1",
                                                marks={
                                                    i: {
                                                        "label": str(i),
                                                        "style": {"color": "#16425D"},
                                                    } for i in range(16)
                                                },
                                                className="range-slider"),
                        ]),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-2-2"),
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-2-2",
                            children=[
                                sf.create_dec_button("2-2"),
                                sf.create_counter("2-2"),
                                sf.create_inc_buttons("2-2"),
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 2", style={"font-family": "Liberation Sans",  "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        html.Div(
                            id="range-slider-div-2-2",
                            children=[
                                dcc.RangeSlider(min=8, max=15, step=1,
                                                value=[8, 15],
                                                id="range-slider-2-2",
                                                marks={
                                                    i: {
                                                        "label": str(i),
                                                        "style": {"color": "#16425D"},
                                                    } for i in range(16)
                                                },
                                                className="range-slider"),
                        ]),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-2-3"),
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-2-3",
                            children=[
                                sf.create_dec_button("2-3"),
                                sf.create_counter("2-3"),
                                sf.create_inc_buttons("2-3"),
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 3", style={"font-family": "Liberation Sans",  "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        html.Div(
                            id="range-slider-div-2-3",
                            children=[
                                dcc.RangeSlider(min=8, max=15, step=1,
                                                value=[8, 15],
                                                id="range-slider-2-3",
                                                marks={
                                                    i: {
                                                        "label": str(i),
                                                        "style": {"color": "#16425D"},
                                                    } for i in range(16)
                                                },
                                                className="range-slider"),
                        ]),
                    ]),
                    html.Div([
                        bottom_remark,
                        dcc.Textarea(
                            id="text-area-sfo",
                            placeholder="Indtast kommentar",
                            style={"margin-left": "8px", "width": "353px", "height": 95},
                        ),
                        html.Div([
                            html.Button(
                                "Registrer fravær",
                                id="button-sfo",
                                n_clicks=0,
                                className="centered-button",
                                style={"padding-top": "4px", "align-text": "center"}
                            ),
                        ],
                            style={"display": "flex", "justify-content": "center"}
                            ),
                        ], style={
                            "align-text": "center",
                            "position": "absolute",
                            "margin-bottom": "8px",
                            "bottom": "0",
                        }
                    ),
                ],
                style={
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#F7F7F7",
                    "font-family": "Liberation Sans", "font-weight": "bold"},
                selected_style={
                    "color": "white",
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#16425D",
                    "font-family": "Liberation Sans", "font-weight": "bold"},
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
tider = [
    html.P("This is tab 3.",
           style={
                "margin-top": "0px",
                "height": "536px",
                "backgroundColor": "#D8E1E8",
                "font-family": "Liberation Sans"}),
]
