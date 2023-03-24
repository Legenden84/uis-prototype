from dash import dash_table, dcc, html
from help import *
from transparent_modal import *
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd
import support_functions as sf

# tab 1 - overblik
overblik = [
    html.Div([
        overblik_top_remark,
    ],
    style={
        "margin-left": "8px",
        "margin-right": "8px"
    })
]

# tab 2 - kalender
calender = [
    html.P("This is tab 2.",
           style={
                "margin-top": "0px",
                "padding-top": "0px",
                "height": "536px",
                "backgroundColor": "#D8E1E8",
                "font-family": "Calibri",})
]

# tab 3 - kalender
messages = [
    html.P("This is tab 3.",
           style={
                "margin-top": "0px",
                "padding-top": "0px",
                "height": "536px",
                "backgroundColor": "#D8E1E8",
                "font-family": "Calibri",})
]

# tab 4 - fravær
noshow = [
    dcc.Tabs(
        id="absence-tab",
        value="tab-2-skole",
        children=[
            dcc.Tab(
                label="SFO",
                value="tab-2-sfo",
                children=[
                    html.Div([
                        html.H1("SFO sygemelding", style={"display": "inline-block", "text-align": "center", "font-size": "20px", "font-family": "Calibri",}),
                        modal_open_sfo, modal_sfo,
                    ], style={"display": "flex", "justify-content": "space-between", "margin-left": "8px"}),
                    top_remark,
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-1-1"),
                                dcc.Interval(id="transparent-modal-1-1-interval", interval=100, n_intervals=0, disabled=False),
                                dcc.Store(id="transparent-modal-1-1-store", data=False, storage_type="session"),
                                dcc.Store(id="transparent-modal-1-1-small-store", data=False, storage_type="session"),
                                transparent_modal_1_1,
                                transparent_modal_1_1_small,
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-1-1",
                            children=[
                                sf.create_dec_button("1-1"),
                                sf.create_counter("1-1"),
                                sf.create_inc_buttons("1-1"),
                            ], style={"display": "block", "padding-top": "5px"}),
                        dbc.Col(
                            html.Div([
                                dcc.Markdown("Hans", style={"font-family": "Calibri",  "margin-right": "16px"}),
                                html.Button(
                                    id="edit-btn-1-1",
                                    children=[
                                        html.Img(
                                            src="/assets/edit-btn.png",
                                            style={
                                                "height": "21px",
                                                "width": "23px",
                                            })
                                    ],
                                    style={
                                        "height": "21px",
                                        "width": "23px",
                                        "border": "none",
                                        "margin-left": "0px",
                                        "margin-right": "16px",
                                        "padding-left": "0px",
                                        "padding-right": "0px",
                                    }),
                                    edit_modal_sfo,
                            ], style={"display": "flex", "align-items": "center"}),
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
                                                persistence=True,
                                                persistence_type="session",
                                                className="range-slider"),
                        ], style={"display": "block"}),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-1-2"),
                                dcc.Interval(id="transparent-modal-1-2-interval", interval=100, n_intervals=0, disabled=False),
                                dcc.Store(id="transparent-modal-1-2-store", data=False, storage_type="session"),
                                dcc.Store(id="transparent-modal-1-2-small-store", data=False, storage_type="session"),
                                transparent_modal_1_2,
                                transparent_modal_1_2_small,
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-1-2",
                            children=[
                                sf.create_dec_button("1-2"),
                                sf.create_counter("1-2"),
                                sf.create_inc_buttons("1-2")
                            ], style={"display": "block", "padding-top": "5px"}),
                        dbc.Col(
                            html.Div([
                                dcc.Markdown("Rosa", style={"font-family": "Calibri",  "margin-right": "16px"}),
                                html.Button(
                                    id="edit-btn-1-2",
                                    children=[
                                        html.Img(
                                            src="/assets/edit-btn.png",
                                            style={
                                                "height": "21px",
                                                "width": "23px",
                                            })
                                    ],
                                    style={
                                        "height": "21px",
                                        "width": "23px",
                                        "border": "none",
                                        "margin-left": "0px",
                                        "margin-right": "16px",
                                        "padding-left": "0px",
                                        "padding-right": "0px",
                                    }),
                            ], style={"display": "flex", "align-items": "center"}),
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
                                                persistence=True,
                                                persistence_type="session",
                                                className="range-slider"),
                            ]),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-1-3"),
                                dcc.Interval(id="transparent-modal-1-3-interval", interval=100, n_intervals=0, disabled=False),
                                dcc.Store(id="transparent-modal-1-3-store", data=False, storage_type="session"),
                                dcc.Store(id="transparent-modal-1-3-small-store", data=False, storage_type="session"),
                                transparent_modal_1_3,
                                transparent_modal_1_3_small,
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-1-3",
                            children=[
                                sf.create_dec_button("1-3"),
                                sf.create_counter("1-3"),
                                sf.create_inc_buttons("1-3"),
                            ], style={"display": "block", "padding-top": "5px"}),
                        dbc.Col(
                            html.Div([
                                dcc.Markdown("Jimmie", style={"font-family": "Calibri",  "margin-right": "16px"}),
                                html.Button(
                                    id="edit-btn-1-3",
                                    children=[
                                        html.Img(
                                            src="/assets/edit-btn.png",
                                            style={
                                                "height": "21px",
                                                "width": "23px",
                                            })
                                    ],
                                    style={
                                        "height": "21px",
                                        "width": "23px",
                                        "border": "none",
                                        "margin-left": "0px",
                                        "margin-right": "16px",
                                        "padding-left": "0px",
                                        "padding-right": "0px",
                                    }),
                            ], style={"display": "flex", "align-items": "center"}),
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
                                                persistence=True,
                                                persistence_type="session",
                                                className="range-slider"),
                        ]),
                    ]),
                    html.Div([
                        html.Div([
                            html.Button(
                                "Registrer fravær",
                                id="button-register-sfo",
                                n_clicks=0,
                                className="centered-button",
                                style={"align-text": "center"}
                            ),
                        ],
                            style={"display": "flex", "justify-content": "center",}
                            ),
                        ], style={
                            "text-align": "center",
                            "position": "absolute",
                            "margin-bottom": "68px",
                            "bottom": "0",
                            "left": "88px"
                        }
                    ),
                ],
                style={
                    "padding": "1px",
                    "height": "30px",
                    "backgroundColor": "#F7F7F7",
                    "font-family": "Calibri",
                    "font-size": "20px",
                    "font-weight": "bold"},
                selected_style={
                    "color": "white",
                    "padding": "1px",
                    "height": "30px",
                    "backgroundColor": "#16425D",
                    "font-family": "Calibri",
                    "font-size": "20px",
                    "font-weight": "bold"},
                className="custom-tabs-container",
                selected_className="custom-tab--selected"
            ),
            dcc.Tab(
                label="SKOLE",
                value="tab-2-skole",
                children=[
                    html.Div([
                        html.H1("Skole sygemelding", style={"display": "inline-block", "text-align": "center", "font-size": "20px", "font-family": "Calibri"}),
                        modal_open_skole, modal_skole,
                    ], style={"display": "flex", "justify-content": "space-between", "margin-left": "8px"}),
                    top_remark,
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-2-1"),
                                dcc.Interval(id="transparent-modal-2-1-interval", interval=100, n_intervals=0, disabled=False),
                                dcc.Store(id="transparent-modal-2-1-store", data=False, storage_type="session"),
                                dcc.Store(id="transparent-modal-2-1-small-store", data=False, storage_type="session"),
                                transparent_modal_2_1,
                                transparent_modal_2_1_small,
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-2-1",
                            children=[
                                sf.create_dec_button("2-1"),
                                sf.create_counter("2-1"),
                                sf.create_inc_buttons("2-1"),
                            ], style={"display": "block", "padding-top": "5px"}),
                        dbc.Col(
                            html.Div([
                                dcc.Markdown("Hans", style={"font-family": "Calibri",  "margin-right": "16px"}),
                                html.Button(
                                    id="edit-btn-2-1",
                                    children=[
                                        html.Img(
                                            src="/assets/edit-btn.png",
                                            style={
                                                "height": "21px",
                                                "width": "23px",
                                            })
                                    ],
                                    style={
                                        "height": "21px",
                                        "width": "23px",
                                        "border": "none",
                                        "margin-left": "0px",
                                        "margin-right": "16px",
                                        "padding-left": "0px",
                                        "padding-right": "0px",
                                    }),
                                    edit_modal_skole,
                            ], style={"display": "flex", "align-items": "center"}),
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
                                                persistence=True,
                                                persistence_type="session",
                                                className="range-slider"),
                        ]),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-2-2"),
                                dcc.Interval(id="transparent-modal-2-2-interval", interval=100, n_intervals=0, disabled=False),
                                dcc.Store(id="transparent-modal-2-2-store", data=False, storage_type="session"),
                                dcc.Store(id="transparent-modal-2-2-small-store", data=False, storage_type="session"),
                                transparent_modal_2_2,
                                transparent_modal_2_2_small,
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-2-2",
                            children=[
                                sf.create_dec_button("2-2"),
                                sf.create_counter("2-2"),
                                sf.create_inc_buttons("2-2"),
                            ], style={"display": "block", "padding-top": "5px"}),
                        dbc.Col(
                            html.Div([
                                dcc.Markdown("Rosa", style={"font-family": "Calibri",  "margin-right": "16px"}),
                                html.Button(
                                    id="edit-btn-2-2",
                                    children=[
                                        html.Img(
                                            src="/assets/edit-btn.png",
                                            style={
                                                "height": "21px",
                                                "width": "23px",
                                            })
                                    ],
                                    style={
                                        "height": "21px",
                                        "width": "23px",
                                        "border": "none",
                                        "margin-left": "0px",
                                        "margin-right": "16px",
                                        "padding-left": "0px",
                                        "padding-right": "0px",
                                    }),
                            ], style={"display": "flex", "align-items": "center"}),
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
                                                persistence=True,
                                                persistence_type="session",
                                                className="range-slider"),
                        ]),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                sf.create_switch("bool-switch-2-3"),
                                dcc.Interval(id="transparent-modal-2-3-interval", interval=100, n_intervals=0, disabled=False),
                                dcc.Store(id="transparent-modal-2-3-store", data=False, storage_type="session"),
                                dcc.Store(id="transparent-modal-2-3-small-store", data=False, storage_type="session"),
                                transparent_modal_2_3,
                                transparent_modal_2_3_small,
                            ]),
                        ),
                        dbc.Col(
                            id="button-col-2-3",
                            children=[
                                sf.create_dec_button("2-3"),
                                sf.create_counter("2-3"),
                                sf.create_inc_buttons("2-3"),
                            ], style={"display": "block", "padding-top": "5px"}),
                        dbc.Col(
                            html.Div([
                                dcc.Markdown("Jimmie", style={"font-family": "Calibri",  "margin-right": "16px"}),
                                html.Button(
                                    id="edit-btn-2-3",
                                    children=[
                                        html.Img(
                                            src="/assets/edit-btn.png",
                                            style={
                                                "height": "21px",
                                                "width": "23px",
                                            })
                                    ],
                                    style={
                                        "height": "21px",
                                        "width": "23px",
                                        "border": "none",
                                        "margin-left": "0px",
                                        "margin-right": "16px",
                                        "padding-left": "0px",
                                        "padding-right": "0px",
                                    }),
                            ], style={"display": "flex", "align-items": "center"}),
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
                                                persistence=True,
                                                persistence_type="session",
                                                className="range-slider"),
                        ]),
                    ]),
                    html.Div([
                        html.Div([
                            html.Button(
                                "Registrer fravær",
                                id="button-register-skole",
                                n_clicks=0,
                                className="centered-button",
                                style={"align-text": "center"}
                            ),
                        ],
                            style={"display": "flex", "justify-content": "center",}
                            ),
                        ], style={
                            "text-align": "center",
                            "position": "absolute",
                            "margin-bottom": "68px",
                            "bottom": "0",
                            "left": "88px"
                        }
                    ),
                ],
                style={
                    "padding": "1px",
                    "height": "30px",
                    "backgroundColor": "#F7F7F7",
                    "font-family": "Calibri",
                    "font-size": "20px",
                    "font-weight": "bold"},
                selected_style={
                    "color": "white",
                    "padding": "1px",
                    "height": "30px",
                    "backgroundColor": "#16425D",
                    "font-family": "Calibri",
                    "font-size": "20px",
                    "font-weight": "bold"},
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

