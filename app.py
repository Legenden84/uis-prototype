from dash import ctx, dash, dash_table, dcc, html, no_update
from dash.dependencies import Input, Output, State
from header import header
from navbar import navbar
from tabs import calender, noshow, overblik, messages
import pandas as pd

# fethching style sheets
external_stylesheets = [
    "assets/style.css",
    "https://raw.githubusercontent.com/plotly/dash-sample-apps/",
    "master/apps/dash-oil-and-gas/assets/styles.css"
]
overblik_src = "/assets/overblik_deselect.png"
kalender_src = "/assets/kalender_deselect.png"
beskeder_src = "/assets/beskeder_deselect.png"
nowshow_src = "/assets/noshow_deselect.png"

overblik_select = "/assets/overblik_select.png"
kalender_select = "/assets/kalender_select.png"
beskeder_select = "/assets/beskeder_select.png"
nowshow_select = "/assets/noshow_select.png"

data = {"Navn": ["Hans", "Rosa", "Jimmie"],
        "SFO": ["", "", ""],
        "Skole": ["", "", ""]
        }

df = pd.DataFrame(data)

table = html.Div(
    id="table-div",
    children=[
        dash_table.DataTable(
            id="table",
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
        )
    ], style={"display": "block", "margin-left": "8px", "margin-right": "8px", "margin-bottom": "500px"}
)

content = html.Div(
    id="page-content",
    children=overblik,
    style={"height": "554px"}
)

register = html.Div([
                html.Button(
                    "Registrer fravær",
                    id="button-register",
                    n_clicks=0,
                    className="centered-button",
                    style={"align-text": "center"}
                ),
            ], style={
                "border": "1px solid black",
                "align-text": "center",
                "position": "absolute",
                "margin-bottom": "8px",
                "bottom": "0",
            }
)

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                prevent_initial_callbacks=True,
                suppress_callback_exceptions=True,
)
# server = app.server
server = app.server

# create layout
app.layout = html.Div([header, content, table, navbar],
                        style={
                            "display": "flex",
                            "border": "1px solid black",
                            "flex-direction": "column",
                            "backgroundColor": "#D8E1E8",
                            "width": "375px",
                            "height": "667px",
                            "margin": "auto",
                            "font-family": "Calibri",
                            "position": "relative",
                            "padding-bottom": "50px"
                        },
                      )


# callbacks
@app.callback(
    [
        Output("page-content", "children"),
        Output("button-1", "children"),
        Output("button-2", "children"),
        Output("button-3", "children"),
        Output("button-4", "children"),
        Output("table-div", "style"),
    ],
    [
        Input("button-1", "n_clicks"),
        Input("button-2", "n_clicks"),
        Input("button-3", "n_clicks"),
        Input("button-4", "n_clicks"),
    ],
    [
        State("button-1", "children"),
        State("button-2", "children"),
        State("button-3", "children"),
        State("button-4", "children"),
    ],
)
def update_button_images(btn1_clicks, btn2_clicks, btn3_clicks, btn4_clicks,
                         btn1_children, btn2_children, btn3_children, btn4_children):
    if (btn1_clicks, btn2_clicks, btn3_clicks, btn4_clicks) == (0, 0, 0, 0):
        return no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update

    content = []
    button1 = html.Img(src=overblik_src)
    button2 = html.Img(src=kalender_src)
    button3 = html.Img(src=beskeder_src)
    button4 = html.Img(src=nowshow_src)

    if not ctx.triggered:
        button_id = None
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "button-1":
        content = overblik
        button1 = html.Img(src=overblik_select)
        button2 = html.Img(src=kalender_src)
        button3 = html.Img(src=beskeder_src)
        button4 = html.Img(src=nowshow_src)
        style = {"display": "block", "margin-left": "8px", "margin-right": "8px", "margin-bottom": "500px"}

    elif button_id == "button-2":
        content = calender
        button1 = html.Img(src=overblik_src)
        button2 = html.Img(src=kalender_select)
        button3 = html.Img(src=beskeder_src)
        button4 = html.Img(src=nowshow_src)
        style = {"display": "none", "margin-left": "8px", "margin-right": "8px", "margin-bottom": "500px"}

    elif button_id == "button-3":
        content = messages
        button1 = html.Img(src=overblik_src)
        button2 = html.Img(src=kalender_src)
        button3 = html.Img(src=beskeder_select)
        button4 = html.Img(src=nowshow_src)
        style = {"display": "none", "margin-left": "8px", "margin-right": "8px", "margin-bottom": "500px"}

    elif button_id == "button-4":
        content = noshow
        button1 = html.Img(src=overblik_src)
        button2 = html.Img(src=kalender_src)
        button3 = html.Img(src=beskeder_src)
        button4 = html.Img(src=nowshow_select)
        style = {"display": "none", "margin-left": "8px", "margin-right": "8px", "margin-bottom": "500px"}

    return content, button1, button2, button3, button4, style


# callback: child 1-1
@app.callback(
        Output(component_id="counter-1-1", component_property="children"),
        Output(component_id="button-1-1-inc", component_property="n_clicks"),
        Output(component_id="button-1-1-dec", component_property="n_clicks"),
        Output(component_id="button-1-1-inc", component_property="style"),
        Output(component_id="button-1-1-dec", component_property="style"),
    [
        Input(component_id="button-1-1-inc", component_property="n_clicks"),
        Input(component_id="button-1-1-dec", component_property="n_clicks"),
        Input(component_id="range-slider-1-1", component_property="value"),
    ],
)
def toggle_kid_1_1(n_click_inc, n_click_dec, range_val):
    if n_click_dec - n_click_inc > 0:

        return no_update, no_update, no_update, 0, 0, no_update, no_update

    if range_val != [12, 17]:
        inc_button_style = {"display": "none", "margin-top": "12px"}
        dec_button_style = {"display": "none", "margin-top": "12px"}

        mode = "Timer"
        counter = range_val[1] - range_val[0]
        display = f"{mode}: {counter}"

        return display, 0, 0, inc_button_style, dec_button_style

    else:
        inc_button_style = {"display": "inline-block", "margin-top": "12px"}
        dec_button_style = {"display": "inline-block", "margin-top": "12px"}

        mode = "Dage"

        if n_click_inc - n_click_dec >= 0:
            counter = n_click_inc - n_click_dec
        else:
            counter = 0
        display = f"{mode}: {counter}"

        return display, no_update, no_update, inc_button_style, dec_button_style


# callback: child 1-2
@app.callback(
        Output(component_id="counter-1-2", component_property="children"),
        Output(component_id="button-1-2-inc", component_property="n_clicks"),
        Output(component_id="button-1-2-dec", component_property="n_clicks"),
        Output(component_id="button-1-2-inc", component_property="style"),
        Output(component_id="button-1-2-dec", component_property="style"),
    [
        Input(component_id="button-1-2-inc", component_property="n_clicks"),
        Input(component_id="button-1-2-dec", component_property="n_clicks"),
        Input(component_id="range-slider-1-2", component_property="value"),
    ],
)
def toggle_kid_1_2(n_click_inc, n_click_dec, range_val):
    if n_click_dec - n_click_inc > 0:
        return no_update, no_update, no_update, 0, 0, no_update, no_update

    if range_val != [12, 17]:
        inc_button_style = {"display": "none", "margin-top": "12px"}
        dec_button_style = {"display": "none", "margin-top": "12px"}

        mode = "Timer"
        counter = range_val[1] - range_val[0]
        display = f"{mode}: {counter}"

        return display, 0, 0, inc_button_style, dec_button_style

    else:
        inc_button_style = {"display": "inline-block", "margin-top": "12px"}
        dec_button_style = {"display": "inline-block", "margin-top": "12px"}

        mode = "Dage"

        if n_click_inc - n_click_dec >= 0:
            counter = n_click_inc - n_click_dec
        else:
            counter = 0
        display = f"{mode}: {counter}"

        return display, no_update, no_update, inc_button_style, dec_button_style


# callback: child 1-3
@app.callback(
        Output(component_id="counter-1-3", component_property="children"),
        Output(component_id="button-1-3-inc", component_property="n_clicks"),
        Output(component_id="button-1-3-dec", component_property="n_clicks"),
        Output(component_id="button-1-3-inc", component_property="style"),
        Output(component_id="button-1-3-dec", component_property="style"),
    [
        Input(component_id="button-1-3-inc", component_property="n_clicks"),
        Input(component_id="button-1-3-dec", component_property="n_clicks"),
        Input(component_id="range-slider-1-3", component_property="value"),
    ],
)
def toggle_kid_1_3(n_click_inc, n_click_dec, range_val):
    if n_click_dec - n_click_inc > 0:

        return no_update, no_update, no_update, 0, 0, no_update, no_update

    if range_val != [12, 17]:
        inc_button_style = {"display": "none", "margin-top": "12px"}
        dec_button_style = {"display": "none", "margin-top": "12px"}

        mode = "Timer"
        counter = range_val[1] - range_val[0]
        display = f"{mode}: {counter}"

        return display, 0, 0, inc_button_style, dec_button_style

    else:
        inc_button_style = {"display": "inline-block", "margin-top": "12px"}
        dec_button_style = {"display": "inline-block", "margin-top": "12px"}

        mode = "Dage"

        if n_click_inc - n_click_dec >= 0:
            counter = n_click_inc - n_click_dec
        else:
            counter = 0
        display = f"{mode}: {counter}"

        return display, no_update, no_update, inc_button_style, dec_button_style


# callback: child 2-1
@app.callback(
        Output(component_id="counter-2-1", component_property="children"),
        Output(component_id="button-2-1-inc", component_property="n_clicks"),
        Output(component_id="button-2-1-dec", component_property="n_clicks"),
        Output(component_id="button-2-1-inc", component_property="style"),
        Output(component_id="button-2-1-dec", component_property="style"),
    [
        Input(component_id="button-2-1-inc", component_property="n_clicks"),
        Input(component_id="button-2-1-dec", component_property="n_clicks"),
        Input(component_id="range-slider-2-1", component_property="value"),
    ],
)
def toggle_kid_2_1(n_click_inc, n_click_dec, range_val):
    if n_click_dec - n_click_inc > 0:

        return no_update, no_update, no_update, 0, 0, no_update, no_update

    if range_val != [8, 15]:
        inc_button_style = {"display": "none", "margin-top": "12px"}
        dec_button_style = {"display": "none", "margin-top": "12px"}

        mode = "Timer"
        counter = range_val[1] - range_val[0]
        display = f"{mode}: {counter}"

        return display, 0, 0, inc_button_style, dec_button_style

    else:
        inc_button_style = {"display": "inline-block", "margin-top": "12px"}
        dec_button_style = {"display": "inline-block", "margin-top": "12px"}

        mode = "Dage"

        if n_click_inc - n_click_dec >= 0:
            counter = n_click_inc - n_click_dec
        else:
            counter = 0
        display = f"{mode}: {counter}"

        return display, no_update, no_update, inc_button_style, dec_button_style


# callback: child 2-2
@app.callback(
        Output(component_id="counter-2-2", component_property="children"),
        Output(component_id="button-2-2-inc", component_property="n_clicks"),
        Output(component_id="button-2-2-dec", component_property="n_clicks"),
        Output(component_id="button-2-2-inc", component_property="style"),
        Output(component_id="button-2-2-dec", component_property="style"),
    [
        Input(component_id="button-2-2-inc", component_property="n_clicks"),
        Input(component_id="button-2-2-dec", component_property="n_clicks"),
        Input(component_id="range-slider-2-2", component_property="value"),
    ],
)
def toggle_kid_2_2(n_click_inc, n_click_dec, range_val):
    if n_click_dec - n_click_inc > 0:

        return no_update, no_update, no_update, 0, 0, no_update, no_update

    if range_val != [8, 15]:
        inc_button_style = {"display": "none", "margin-top": "12px"}
        dec_button_style = {"display": "none", "margin-top": "12px"}

        mode = "Timer"
        counter = range_val[1] - range_val[0]
        display = f"{mode}: {counter}"

        return display, 0, 0, inc_button_style, dec_button_style

    else:
        inc_button_style = {"display": "inline-block", "margin-top": "12px"}
        dec_button_style = {"display": "inline-block", "margin-top": "12px"}

        mode = "Dage"

        if n_click_inc - n_click_dec >= 0:
            counter = n_click_inc - n_click_dec
        else:
            counter = 0
        display = f"{mode}: {counter}"

        return display, no_update, no_update, inc_button_style, dec_button_style


# callback: child 2-3
@app.callback(
        Output(component_id="counter-2-3", component_property="children"),
        Output(component_id="button-2-3-inc", component_property="n_clicks"),
        Output(component_id="button-2-3-dec", component_property="n_clicks"),
        Output(component_id="button-2-3-inc", component_property="style"),
        Output(component_id="button-2-3-dec", component_property="style"),
    [
        Input(component_id="button-2-3-inc", component_property="n_clicks"),
        Input(component_id="button-2-3-dec", component_property="n_clicks"),
        Input(component_id="range-slider-2-3", component_property="value"),
    ],
)
def toggle_kid_2_3(n_click_inc, n_click_dec, range_val):
    if n_click_dec - n_click_inc > 0:

        return no_update, no_update, no_update, 0, 0, no_update, no_update

    if range_val != [8, 15]:
        inc_button_style = {"display": "none", "margin-top": "12px"}
        dec_button_style = {"display": "none", "margin-top": "12px"}

        mode = "Timer"
        counter = range_val[1] - range_val[0]
        display = f"{mode}: {counter}"

        return display, 0, 0, inc_button_style, dec_button_style

    else:
        inc_button_style = {"display": "inline-block", "margin-top": "12px"}
        dec_button_style = {"display": "inline-block", "margin-top": "12px"}

        mode = "Dage"

        if n_click_inc - n_click_dec >= 0:
            counter = n_click_inc - n_click_dec
        else:
            counter = 0
        display = f"{mode}: {counter}"

        return display, no_update, no_update, inc_button_style, dec_button_style


# callback: toggle transparent modal 1-1
@app.callback(
        [
            Output(component_id="button-col-1-1", component_property="style"),
            Output(component_id="range-slider-div-1-1", component_property="style"),
            Output(component_id="grey-out-but-1-1", component_property="data"),
            Output(component_id="grey-out-range-1-1", component_property="data"),
            Output(component_id="interval-1-1", component_property="disabled"),
        ],
        [
            Input(component_id="interval-1-1", component_property="n_intervals"),
            Input(component_id="button-register-sfo", component_property="n_clicks"),
        ],
        [
            State(component_id="bool-switch-1-1", component_property="on"),
            State(component_id="grey-out-but-1-1", component_property="data"),
            State(component_id="grey-out-range-1-1", component_property="data"),
            State(component_id="interval-1-1", component_property="disabled"),
        ]
)
def toggle_transparent_modal_1_1(n_intervals, n_clicks, switch, state_but, state_range, disabled):
    if not disabled and n_intervals:
        if (state_but == {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"} and state_range == {"opacity": "0.5", "pointer-events": "none"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"} and state_range == {"opacity": "1", "pointer-events": "auto"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == [] and state_range == []):
            return no_update, no_update, no_update, no_update, True

    if n_clicks and switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"}
        range_style = {"opacity": "0.5", "pointer-events": "none"}
        return button_col_style, range_style, button_col_style, range_style, False

    elif n_clicks and not switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"}
        range_style = {"opacity": "1", "pointer-events": "auto"}
        return button_col_style, range_style, button_col_style, range_style, False

    return no_update, no_update, no_update, no_update, no_update


# callback: toggle transparent modal 1-2
@app.callback(
        [
            Output(component_id="button-col-1-2", component_property="style"),
            Output(component_id="range-slider-div-1-2", component_property="style"),
            Output(component_id="grey-out-but-1-2", component_property="data"),
            Output(component_id="grey-out-range-1-2", component_property="data"),
            Output(component_id="interval-1-2", component_property="disabled"),
        ],
        [
            Input(component_id="interval-1-2", component_property="n_intervals"),
            Input(component_id="button-register-sfo", component_property="n_clicks"),
        ],
        [
            State(component_id="bool-switch-1-2", component_property="on"),
            State(component_id="grey-out-but-1-2", component_property="data"),
            State(component_id="grey-out-range-1-2", component_property="data"),
            State(component_id="interval-1-2", component_property="disabled"),
        ]
)
def toggle_transparent_modal_1_2(n_intervals, n_clicks, switch, state_but, state_range, disabled):
    if not disabled and n_intervals:
        if (state_but == {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"} and state_range == {"opacity": "0.5", "pointer-events": "none"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"} and state_range == {"opacity": "1", "pointer-events": "auto"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == [] and state_range == []):
            return no_update, no_update, no_update, no_update, True

    if n_clicks and switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"}
        range_style = {"opacity": "0.5", "pointer-events": "none"}
        return button_col_style, range_style, button_col_style, range_style, False

    elif n_clicks and not switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"}
        range_style = {"opacity": "1", "pointer-events": "auto"}
        return button_col_style, range_style, button_col_style, range_style, False

    return no_update, no_update, no_update, no_update, no_update


# callback: toggle transparent modal 1-3
@app.callback(
        [
            Output(component_id="button-col-1-3", component_property="style"),
            Output(component_id="range-slider-div-1-3", component_property="style"),
            Output(component_id="grey-out-but-1-3", component_property="data"),
            Output(component_id="grey-out-range-1-3", component_property="data"),
            Output(component_id="interval-1-3", component_property="disabled"),
        ],
        [
            Input(component_id="interval-1-3", component_property="n_intervals"),
            Input(component_id="button-register-sfo", component_property="n_clicks"),
        ],
        [
            State(component_id="bool-switch-1-3", component_property="on"),
            State(component_id="grey-out-but-1-3", component_property="data"),
            State(component_id="grey-out-range-1-3", component_property="data"),
            State(component_id="interval-1-3", component_property="disabled"),
        ]
)
def toggle_transparent_modal_1_3(n_intervals, n_clicks, switch, state_but, state_range, disabled):
    if not disabled and n_intervals:
        if (state_but == {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"} and state_range == {"opacity": "0.5", "pointer-events": "none"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"} and state_range == {"opacity": "1", "pointer-events": "auto"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == [] and state_range == []):
            return no_update, no_update, no_update, no_update, True

    if n_clicks and switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"}
        range_style = {"opacity": "0.5", "pointer-events": "none"}
        return button_col_style, range_style, button_col_style, range_style, False

    elif n_clicks and not switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"}
        range_style = {"opacity": "1", "pointer-events": "auto"}
        return button_col_style, range_style, button_col_style, range_style, False

    return no_update, no_update, no_update, no_update, no_update


# callback: toggle transparent modal 2-1
@app.callback(
        [
            Output(component_id="button-col-2-1", component_property="style"),
            Output(component_id="range-slider-div-2-1", component_property="style"),
            Output(component_id="grey-out-but-2-1", component_property="data"),
            Output(component_id="grey-out-range-2-1", component_property="data"),
            Output(component_id="interval-2-1", component_property="disabled"),
        ],
        [
            Input(component_id="interval-2-1", component_property="n_intervals"),
            Input(component_id="button-register-skole", component_property="n_clicks"),
        ],
        [
            State(component_id="bool-switch-2-1", component_property="on"),
            State(component_id="grey-out-but-2-1", component_property="data"),
            State(component_id="grey-out-range-2-1", component_property="data"),
            State(component_id="interval-2-1", component_property="disabled"),
        ]
)
def toggle_transparent_modal_2_1(n_intervals, n_clicks, switch, state_but, state_range, disabled):
    if not disabled and n_intervals:
        if (state_but == {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"} and state_range == {"opacity": "0.5", "pointer-events": "none"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"} and state_range == {"opacity": "1", "pointer-events": "auto"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == [] and state_range == []):
            return no_update, no_update, no_update, no_update, True

    if n_clicks and switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"}
        range_style = {"opacity": "0.5", "pointer-events": "none"}
        return button_col_style, range_style, button_col_style, range_style, False

    elif n_clicks and not switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"}
        range_style = {"opacity": "1", "pointer-events": "auto"}
        return button_col_style, range_style, button_col_style, range_style, False

    return no_update, no_update, no_update, no_update, no_update


# callback: toggle transparent modal 2-2
@app.callback(
        [
            Output(component_id="button-col-2-2", component_property="style"),
            Output(component_id="range-slider-div-2-2", component_property="style"),
            Output(component_id="grey-out-but-2-2", component_property="data"),
            Output(component_id="grey-out-range-2-2", component_property="data"),
            Output(component_id="interval-2-2", component_property="disabled"),
        ],
        [
            Input(component_id="interval-2-2", component_property="n_intervals"),
            Input(component_id="button-register-skole", component_property="n_clicks"),
        ],
        [
            State(component_id="bool-switch-2-2", component_property="on"),
            State(component_id="grey-out-but-2-2", component_property="data"),
            State(component_id="grey-out-range-2-2", component_property="data"),
            State(component_id="interval-2-2", component_property="disabled"),
        ]
)
def toggle_transparent_modal_2_2(n_intervals, n_clicks, switch, state_but, state_range, disabled):
    if not disabled and n_intervals:
        if (state_but == {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"} and state_range == {"opacity": "0.5", "pointer-events": "none"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"} and state_range == {"opacity": "1", "pointer-events": "auto"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == [] and state_range == []):
            return no_update, no_update, no_update, no_update, True

    if n_clicks and switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"}
        range_style = {"opacity": "0.5", "pointer-events": "none"}
        return button_col_style, range_style, button_col_style, range_style, False

    elif n_clicks and not switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"}
        range_style = {"opacity": "1", "pointer-events": "auto"}
        return button_col_style, range_style, button_col_style, range_style, False

    return no_update, no_update, no_update, no_update, no_update


# callback: toggle transparent modal 2-3
@app.callback(
        [
            Output(component_id="button-col-2-3", component_property="style"),
            Output(component_id="range-slider-div-2-3", component_property="style"),
            Output(component_id="grey-out-but-2-3", component_property="data"),
            Output(component_id="grey-out-range-2-3", component_property="data"),
            Output(component_id="interval-2-3", component_property="disabled"),
        ],
        [
            Input(component_id="interval-2-3", component_property="n_intervals"),
            Input(component_id="button-register-skole", component_property="n_clicks"),
        ],
        [
            State(component_id="bool-switch-2-3", component_property="on"),
            State(component_id="grey-out-but-2-3", component_property="data"),
            State(component_id="grey-out-range-2-3", component_property="data"),
            State(component_id="interval-2-3", component_property="disabled"),
        ]
)
def toggle_transparent_modal_2_3(n_intervals, n_clicks, switch, state_but, state_range, disabled):
    if not disabled and n_intervals:
        if (state_but == {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"} and state_range == {"opacity": "0.5", "pointer-events": "none"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"} and state_range == {"opacity": "1", "pointer-events": "auto"}):
            return state_but, state_range, state_but, state_range, True

        elif (state_but == [] and state_range == []):
            return no_update, no_update, no_update, no_update, True

    if n_clicks and switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "0.5", "pointer-events": "none"}
        range_style = {"opacity": "0.5", "pointer-events": "none"}
        return button_col_style, range_style, button_col_style, range_style, False

    elif n_clicks and not switch:
        button_col_style = {"display": "block", "padding-top": "5px", "opacity": "1", "pointer-events": "auto"}
        range_style = {"opacity": "1", "pointer-events": "auto"}
        return button_col_style, range_style, button_col_style, range_style, False

    return no_update, no_update, no_update, no_update, no_update


# callback: update dash table sfo
@app.callback(
    Output(component_id="table", component_property="data", allow_duplicate=True),
    [Input(component_id="button-register-sfo", component_property="n_clicks")],
    [
        State(f"bool-switch-1-{i}", component_property="on") for i in range(1, 4)
    ] +
    [
        State(f"range-slider-1-{i}", component_property="value") for i in range(1, 4)
    ] +
    [
        State(f"button-1-{i}-inc", component_property="n_clicks") for i in range(1, 4)
    ] +
    [
        State(f"button-1-{i}-dec", component_property="n_clicks") for i in range(1, 4)
    ] +
    [
        State(component_id="table", component_property="data"),
    ],
)
def update_table(n_clicks, *args):
    data = args[-1]
    updates = []

    for i in range(1, 4):
        switch = args[i - 1]
        value = args[i + 2]
        inc = args[i + 5]
        dec = args[i + 8]
        days = inc - dec

        if switch:
            if value == [12, 17]:
                if days == 1:
                    data[i - 1]["SFO"] = "Idag"
                elif days == 0:
                    data[i - 1]["SFO"] = ""
                else:
                    data[i - 1]["SFO"] = f"{days} dage"
            else:
                data[i - 1]["SFO"] = f"Fra {value[0]} til {value[1]}"
        else:
            data[i - 1]["SFO"] = ""

        updates.append(data[i - 1])

    return updates


# callback: update dash table skole
@app.callback(
    Output(component_id="table", component_property="data", allow_duplicate=True),
    [Input(component_id="button-register-skole", component_property="n_clicks")],
    [
        State(f"bool-switch-2-{i}", component_property="on") for i in range(1, 4)
    ] +
    [
        State(f"range-slider-2-{i}", component_property="value") for i in range(1, 4)
    ] +
    [
        State(f"button-2-{i}-inc", component_property="n_clicks") for i in range(1, 4)
    ] +
    [
        State(f"button-2-{i}-dec", component_property="n_clicks") for i in range(1, 4)
    ] +
    [
        State(component_id="table", component_property="data"),
    ],
)
def update_table(n_clicks, *args):
    data = args[-1]
    updates = []

    for i in range(1, 4):
        switch = args[i - 1]
        value = args[i + 2]
        inc = args[i + 5]
        dec = args[i + 8]
        days = inc - dec

        if switch:
            if value == [8, 15]:
                if days == 1:
                    data[i - 1]["Skole"] = "Idag"
                elif days == 0:
                    data[i - 1]["Skole"] = ""
                else:
                    data[i - 1]["Skole"] = f"{days} dage"
            else:
                data[i - 1]["Skole"] = f"Fra {value[0]} til {value[1]}"
        else:
            data[i - 1]["Skole"] = ""

        updates.append(data[i - 1])

    return updates


# callback: toggle help skole
@app.callback(
    Output(component_id="modal-skole", component_property="is_open"),
    [
        Input(component_id="open-skole", component_property="n_clicks"),
        Input(component_id="close-skole", component_property="n_clicks")
    ],
    [
        State(component_id="modal-skole", component_property="is_open")
    ]
)
def toggle_help_skole(open, close, is_open):
    if open or close:
        return not is_open
    return is_open


# callback: toggle help sfo
@app.callback(
    Output(component_id="modal-sfo", component_property="is_open"),
    [
        Input(component_id="open-sfo", component_property="n_clicks"),
        Input(component_id="close-sfo", component_property="n_clicks")
    ],
    [
        State(component_id="modal-sfo", component_property="is_open")
    ]
)
def toggle_help_sfo(open, close, is_open):
    if open or close:
        return not is_open
    return is_open


# callback: toggle edit button sfo
@app.callback(
    Output(component_id="modal-edit-sfo", component_property="is_open"),
    [
        Input(component_id="edit-btn-1-1", component_property="n_clicks"),
        Input(component_id="edit-btn-1-2", component_property="n_clicks"),
        Input(component_id="edit-btn-1-3", component_property="n_clicks"),
        Input(component_id="close-edit-sfo", component_property="n_clicks")
    ],
    [
        State(component_id="modal-edit-sfo", component_property="is_open")
    ]
)
def toggle_edit(open_edit2_1, open_edit2_2, open_edit2_3, close_edit, is_open):
    if any([open_edit2_1, open_edit2_2, open_edit2_3, is_open]):
        return not is_open
    elif close_edit:
        return is_open


# callback: toggle edit button skole
@app.callback(
    Output(component_id="modal-edit-skole", component_property="is_open"),
    [
        Input(component_id="edit-btn-2-1", component_property="n_clicks"),
        Input(component_id="edit-btn-2-2", component_property="n_clicks"),
        Input(component_id="edit-btn-2-3", component_property="n_clicks"),
        Input(component_id="close-edit-skole", component_property="n_clicks")
    ],
    [
        State(component_id="modal-edit-skole", component_property="is_open")
    ]
)
def toggle_edit(open_edit2_1, open_edit2_2, open_edit2_3, close_edit, is_open):
    if any([open_edit2_1, open_edit2_2, open_edit2_3, is_open]):
        return not is_open
    elif close_edit:
        return is_open

# create server object
if __name__ == "__main__":
    app.run_server(debug=True)
