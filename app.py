from dash import ctx, dash, dcc, html, no_update
from dash.dependencies import Input, Output, State
from header import header
from navbar import navbar
from tabs import calender, noshow, overblik, messages

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

content = html.Div(
    id="page-content",
    children=[],
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
                suppress_callback_exceptions=True,
                meta_tags=[{"name": "viewport",
                            "content": "width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,"}]
)
# server = app.server
server = app.server

# main layout
body = html.Div([
    dcc.Tabs(
        id="tabs",
        value="tab-1",
        children=[
            dcc.Tab(
                label="OVERBLIK",
                value="tab-1",
                children=overblik,
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
                label="FRAVÆR",
                value="tab-2",
                children=noshow,
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
                label="TIDER",
                value="tab-3",
                children=messages,
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
            "padding-bottom": "0px",
            "margin-bottom": "2px",
            "height": "30px",
        },
        className="custom-tabs-container",
    ),
])


# create layout
app.layout = html.Div([header, content, navbar],
                        style={
                            "display": "flex",
                            "flex-direction": "column",
                            "backgroundColor": "#D8E1E8",
                            "width": "375px",
                            "height": "667px",
                            "margin": "auto",
                            "border": "1px solid black",
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
        State("button-4", "children")
    ],
)
def update_button_images(btn1_clicks, btn2_clicks, btn3_clicks, btn4_clicks, btn1_children, btn2_children, btn3_children, btn4_children):
    if (btn1_clicks, btn2_clicks, btn3_clicks, btn4_clicks) == (0, 0, 0, 0):
        return no_update, no_update, no_update, no_update, no_update

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

    elif button_id == "button-2":
        content = calender
        button1 = html.Img(src=overblik_src)
        button2 = html.Img(src=kalender_select)
        button3 = html.Img(src=beskeder_src)
        button4 = html.Img(src=nowshow_src)

    elif button_id == "button-3":
        content = messages
        button1 = html.Img(src=overblik_src)
        button2 = html.Img(src=kalender_src)
        button3 = html.Img(src=beskeder_select)
        button4 = html.Img(src=nowshow_src)

    elif button_id == "button-4":
        content = noshow
        button1 = html.Img(src=overblik_src)
        button2 = html.Img(src=kalender_src)
        button3 = html.Img(src=beskeder_src)
        button4 = html.Img(src=nowshow_select)

    return content, button1, button2, button3, button4

@app.callback(
        Output(component_id="range-slider-div-1-1", component_property="style"),
        Output(component_id="button-col-1-1", component_property="style"),
        [
            Input(component_id="bool-switch-1-1", component_property="on"),
        ]
)
def switch_1_1(switch):
    if switch == True:
        range_div = {"display": "block"}
        button_col = {"display": "block", "padding-top": "5px"}
    else:
        range_div = {"display": "none"}
        button_col = {"display": "none", "padding-top": "5px"}

    return range_div, button_col


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

        return dash.no_update, dash.no_update, dash.no_update, 0, 0, dash.no_update, dash.no_update

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

        return display, dash.no_update, dash.no_update, inc_button_style, dec_button_style


@app.callback(
        Output(component_id="range-slider-div-1-2", component_property="style"),
        Output(component_id="button-col-1-2", component_property="style"),
        [
            Input(component_id="bool-switch-1-2", component_property="on"),
        ]
)
def switch_1_2(switch):
    if switch == True:
        range_div = {"display": "block"}
        button_col = {"display": "block", "padding-top": "5px"}
    else:
        range_div = {"display": "none"}
        button_col = {"display": "none", "padding-top": "5px"}

    return range_div, button_col


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
        return dash.no_update, dash.no_update, dash.no_update, 0, 0, dash.no_update, dash.no_update

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

        return display, dash.no_update, dash.no_update, inc_button_style, dec_button_style


@app.callback(
        Output(component_id="range-slider-div-1-3", component_property="style"),
        Output(component_id="button-col-1-3", component_property="style"),
        [
            Input(component_id="bool-switch-1-3", component_property="on"),
        ]
)
def switch_1_2(switch):
    if switch == True:
        range_div = {"display": "block"}
        button_col = {"display": "block", "padding-top": "5px"}
    else:
        range_div = {"display": "none"}
        button_col = {"display": "none", "padding-top": "5px"}

    return range_div, button_col


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

        return dash.no_update, dash.no_update, dash.no_update, 0, 0, dash.no_update, dash.no_update

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

        return display, dash.no_update, dash.no_update, inc_button_style, dec_button_style


@app.callback(
        Output(component_id="range-slider-div-2-1", component_property="style"),
        Output(component_id="button-col-2-1", component_property="style"),
        [
            Input(component_id="bool-switch-2-1", component_property="on"),
        ]
)
def switch_1_2(switch):
    if switch == True:
        range_div = {"display": "block"}
        button_col = {"display": "block", "padding-top": "5px"}
    else:
        range_div = {"display": "none"}
        button_col = {"display": "none", "padding-top": "5px"}

    return range_div, button_col


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

        return dash.no_update, dash.no_update, dash.no_update, 0, 0, dash.no_update, dash.no_update

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

        return display, dash.no_update, dash.no_update, inc_button_style, dec_button_style


@app.callback(
        Output(component_id="range-slider-div-2-2", component_property="style"),
        Output(component_id="button-col-2-2", component_property="style"),
        [
            Input(component_id="bool-switch-2-2", component_property="on"),
        ]
)
def switch_1_2(switch):
    if switch == True:
        range_div = {"display": "block"}
        button_col = {"display": "block", "padding-top": "5px"}

    else:
        range_div = {"display": "none"}
        button_col = {"display": "none", "padding-top": "5px"}

    return range_div, button_col


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

        return dash.no_update, dash.no_update, dash.no_update, 0, 0, dash.no_update, dash.no_update

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

        return display, dash.no_update, dash.no_update, inc_button_style, dec_button_style


@app.callback(
        Output(component_id="range-slider-div-2-3", component_property="style"),
        Output(component_id="button-col-2-3", component_property="style"),
        [
            Input(component_id="bool-switch-2-3", component_property="on"),
        ]
)
def switch_1_2(switch):
    if switch == True:
        range_div = {"display": "block"}
        button_col = {"display": "block", "padding-top": "5px"}
    else:
        range_div = {"display": "none"}
        button_col = {"display": "none", "padding-top": "5px"}

    return range_div, button_col


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

        return dash.no_update, dash.no_update, dash.no_update, 0, 0, dash.no_update, dash.no_update

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

        return display, dash.no_update, dash.no_update, inc_button_style, dec_button_style


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


# create server object
if __name__ == "__main__":
    app.run_server(debug=True)