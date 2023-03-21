from dash import ctx, dash, dcc, html
from dash.dependencies import Input, Output, State
from header import header
from tabs import absence, overblik, tider
import dash_bootstrap_components as dbc

# fethching style sheets
external_stylesheets = [
    "assets/style.css",
    "https://raw.githubusercontent.com/plotly/dash-sample-apps/",
    "master/apps/dash-oil-and-gas/assets/styles.css"
]

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets],
                suppress_callback_exceptions=True,
                meta_tags=[{"name": "viewport",
                            "content": "width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,"}]
)
# server = app.server
server = app.server

# Define bavbar items as dicts
overblik_dict = {"src": "/assets/overblik_deselect.png", "selected_src": "/assets/overblik_select.png"}
kalender_dict = {"src": "/assets/kalender_deselect.png", "selected_src": "/assets/kalender_select.png"}
beskeder_dict = {"src": "/assets/beskeder_deselect.png", "selected_src": "/assets/beskeder_select.png"}



# Define the navbar layout
navbar = html.Div([
    html.Img(id="nav-overblik", src=overblik_dict["src"], n_clicks=0,),
    html.Img(id="nav-kalender", src=kalender_dict["src"], n_clicks=0,),
    html.Img(id="nav-beskeder", src=beskeder_dict["src"], n_clicks=0,),
])

beskeder_content = []

# create layout
app.layout = html.Div(
    [
        header,
        html.Div(
            id="page-content",
            children=[]
        ),
        html.Div([
            navbar
        ], style={"position": "absolute", "bottom": "0"})
    ],
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

# creating navbar callback for selecting items
@app.callback(
    [
        Output(component_id="nav-overblik", component_property="src"),
        Output(component_id="nav-kalender", component_property="src"),
        Output(component_id="nav-beskeder", component_property="src"),
        Output(component_id="page-content", component_property="children")
    ],
    [
        Input(component_id="nav-overblik", component_property="n_clicks"),
        Input(component_id="nav-kalender", component_property="n_clicks"),
        Input(component_id="nav-beskeder", component_property="n_clicks"),
    ],
    [
        State(component_id="nav-overblik", component_property="src"),
        State(component_id="nav-kalender", component_property="src"),
        State(component_id="nav-beskeder", component_property="src"),
    ]
)
def update_navbar(n_clicks_overblik, n_clicks_kalender, n_clicks_beskeder, src_overblik, src_kalender, src_beskeder):
    selected_item_id = ctx.triggered[0]["prop_id"].split(".")[0]
    content = []
    if selected_item_id == "nav-overblik":
        content = overblik
        return [overblik_dict["selected_src"], kalender_dict["src"], beskeder_dict["src"], content]
    elif selected_item_id == "nav-kalender":
        content = absence
        return [overblik_dict["src"], kalender_dict["selected_src"], beskeder_dict["src"], content]
    elif selected_item_id == "nav-beskeder":
        content = tider
        return [overblik_dict["src"], kalender_dict["src"], beskeder_dict["selected_src"], content]
    else:
        return [src_overblik, src_kalender, src_beskeder, content]


# callbacks
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
