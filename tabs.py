from dash import dcc, html
from help import *
from bool_switch import *
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
                    html.Div([
                        html.H1("SFO sygemelding", style={"display": "inline-block", "text-align": "center", "font-size": "20px", "font-family": "Ubuntu"}),
                        modal_open_sfo, modal_sfo,
                    ], style={"display": "flex", "justify-content": "space-between", "margin-left": "8px"}),
                    top_remark,
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                create_switch("bool-switch-1-1")
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-1-1",
                            children=[
                                html.Button("-", id="button-1-1-dec", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"}),
                                html.H2(children="0", id="counter-1-1", style={"font-size": "16px", "font-family": "Ubuntu", "display": "inline-block", "margin": "0 10px", "padding-top": "12px"}),
                                html.Button("+", id="button-1-1-inc", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"})
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 1", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        html.Div(
                            id="range-slider-div-1-1",
                            children=[
                                dcc.RangeSlider(min=8, max=15, step=1,
                                                value=[8, 15],
                                                id="range-slider-1-1",
                                                marks={
                                                    i: {
                                                        "label": str(i),
                                                        "style": {"color": "#16425D"},
                                                    } for i in range(16)
                                                },
                                                className="range-slider"),
                        ], style={"display": "None"}),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                create_switch("bool-switch-1-2")
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-1-2",
                            children=[
                                html.Button("-", id="button-1-2-dec", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"}),
                                html.H2(children="0", id="counter-1-2", style={"font-size": "16px", "font-family": "Ubuntu", "display": "inline-block", "margin": "0 10px", "padding-top": "12px"}),
                                html.Button("+", id="button-1-2-inc", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"})
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 2", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        html.Div(
                            id="range-slider-div-1-2",
                            children=[
                                dcc.RangeSlider(min=8, max=15, step=1,
                                                value=[8, 15],
                                                id="range-slider-1-2",
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
                                create_switch("bool-switch-1-3"),
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-1-3",
                            children=[
                                html.Button("-", id="button-1-3-dec", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"}),
                                html.H2(children="0", id="counter-1-3", style={"font-size": "16px", "font-family": "Ubuntu", "display": "inline-block", "margin": "0 10px", "padding-top": "12px"}),
                                html.Button("+", id="button-1-3-inc", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"})
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 3", style={"font-family": "Ubuntu", "margin-right": "25px"})
                        ),
                    ], style={"display": "flex", "justify-content": "space-between",}),
                    dbc.Row([
                        html.Div(
                            id="range-slider-div-1-3",
                            children=[
                                dcc.RangeSlider(min=8, max=15, step=1,
                                                value=[8, 15],
                                                id="range-slider-1-3",
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
                                style={
                                    "height": "35px",
                                    "width": "200px",
                                    "font-size": "20px",
                                    "font-family": "Ubuntu",
                                    "backgroundColor": "#16425D",
                                    "color": "white",
                                    "border-top-left-radius": "5px",
                                    "border-top-right-radius": "5px",
                                    "border-bottom-left-radius": "5px",
                                    "border-bottom-right-radius": "5px",
                                    }
                            ),
                        ],
                            className="centered-button"),
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
                    html.Div([
                        html.H1("Skole sygemelding", style={"display": "inline-block", "text-align": "center", "font-size": "20px", "font-family": "Ubuntu"}),
                        modal_open_skole, modal_skole,
                    ], style={"display": "flex", "justify-content": "space-between", "margin-left": "8px"}),
                    top_remark,
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                create_switch("bool-switch-2-1"),
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-2-1",
                            children=[
                                html.Button("-", id="button-2-1-dec", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"}),
                                html.H2(children="0", id="counter-2-1", style={"font-size": "16px", "font-family": "Ubuntu", "display": "inline-block", "margin": "0 10px", "padding-top": "12px"}),
                                html.Button("+", id="button-2-1-inc", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"})
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 1", style={"font-family": "Ubuntu", "margin-right": "25px"})
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
                                create_switch("bool-switch-2-2"),
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-2-2",
                            children=[
                                html.Button("-", id="button-2-2-dec", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"}),
                                html.H2(children="0", id="counter-2-2", style={"font-size": "16px", "font-family": "Ubuntu", "display": "inline-block", "margin": "0 10px", "padding-top": "12px"}),
                                html.Button("+", id="button-2-2-inc", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"})
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 2", style={"font-family": "Ubuntu", "margin-right": "25px"})
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
                                create_switch("bool-switch-2-3"),
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-2-3",
                            children=[
                                html.Button("-", id="button-2-3-dec", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"}),
                                html.H2(children="0", id="counter-2-3", style={"font-size": "16px", "font-family": "Ubuntu", "display": "inline-block", "margin": "0 10px", "padding-top": "12px"}),
                                html.Button("+", id="button-2-3-inc", n_clicks=0, style={"display": "inline-block", "margin-top": "12px"})
                            ], style={"display": "none", "padding-top": "5px"}),
                        dbc.Col(
                            dcc.Markdown("Barn 3", style={"font-family": "Ubuntu", "margin-right": "25px"})
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
                            id="text-area-skole",
                            placeholder="Indtast kommentar",
                            style={"margin-left": "8px", "width": "353px", "height": 95},
                        ),
                        html.Div([
                            html.Button(
                                "Registrer fravær",
                                id="button-skole",
                                n_clicks=0,
                                style={
                                    "height": "35px",
                                    "width": "200px",
                                    "font-size": "20px",
                                    "font-family": "Ubuntu",
                                    "backgroundColor": "#16425D",
                                    "color": "white",
                                    "border-top-left-radius": "5px",
                                    "border-top-right-radius": "5px",
                                    "border-bottom-left-radius": "5px",
                                    "border-bottom-right-radius": "5px",
                                    }
                            ),
                        ],
                            className="centered-button"),
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
tider = [
    html.P("This is tab 3.",
           style={
                "margin-top": "0px",
                "height": "536px",
                "backgroundColor": "#D8E1E8",
                "font-family": "Ubuntu"}),
]
