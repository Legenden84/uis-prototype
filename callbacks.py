from dash import dash
from dash.dependencies import Input, Output

# fethching style sheets
external_stylesheets = [
    "assets/style.css",
    "https://raw.githubusercontent.com/plotly/dash-sample-apps/",
    "master/apps/dash-oil-and-gas/assets/styles.css"
]

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
)
# server = app.server
server = app.server

# callbacks
@app.callback(
    Output(component_id="counter-1-1", component_property="children"),
    [
        Input(component_id="button-1-1-inc", component_property="n_clicks"),
        Input(component_id="button-1-1-dec", component_property="n_clicks")
    ],
)
def update_counter_1_1(inc, dec):
    value = inc - dec
    if value >= 0:
        return f"{value}"
    else:
        return "0"


@app.callback(
    Output(component_id="counter-1-2", component_property="children"),
    [
        Input(component_id="button-1-2-inc", component_property="n_clicks"),
        Input(component_id="button-1-2-dec", component_property="n_clicks")
    ],
)
def update_counter_1_2(inc, dec):
    value = inc - dec
    if value >= 0:
        return f"{value}"
    else:
        return "0"


@app.callback(
    Output(component_id="counter-1-3", component_property="children"),
    [
        Input(component_id="button-1-3-inc", component_property="n_clicks"),
        Input(component_id="button-1-3-dec", component_property="n_clicks")
    ],
)
def update_counter_1_3(inc, dec):
    value = inc - dec
    if value >= 0:
        return f"{value}"
    else:
        return "0"


@app.callback(
    Output(component_id="counter-2-1", component_property="children"),
    [
        Input(component_id="button-2-1-inc", component_property="n_clicks"),
        Input(component_id="button-2-1-dec", component_property="n_clicks")
    ],
)
def update_counter_2_1(inc, dec):
    value = inc - dec
    if value >= 0:
        return f"{value}"
    else:
        return "0"


@app.callback(
    Output(component_id="counter-2-2", component_property="children"),
    [
        Input(component_id="button-2-2-inc", component_property="n_clicks"),
        Input(component_id="button-2-2-dec", component_property="n_clicks")
    ],
)
def update_counter_2_2(inc, dec):
    value = inc - dec
    if value >= 0:
        return f"{value}"
    else:
        return "0"


@app.callback(
    Output(component_id="counter-2-3", component_property="children"),
    [
        Input(component_id="button-2-3-inc", component_property="n_clicks"),
        Input(component_id="button-2-3-dec", component_property="n_clicks")
    ],
)
def update_counter_2_3(inc, dec):
    value = inc - dec
    if value >= 0:
        return f"{value}"
    else:
        return "0"