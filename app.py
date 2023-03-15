from dash import dash, dcc, html
from dash.dependencies import Input, Output
from header import header
from tabs import absence, overblik, time

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
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#F7F7F7",
                    "font-family": "Ubuntu",},
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
                label="FRAVÆR",
                value="tab-2",
                children=absence,
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
                label="TID",
                value="tab-3",
                children=time,
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
            "padding-bottom": "0px",
            "margin-bottom": "2px",
            "height": "30px",
        },
        className="custom-tabs-container",
    ),
])



# create layout
app.layout = html.Div([header, body],
                      style={
                            "backgroundColor": "#D8E1E8",
                            "width": "375px",
                            "height": "667px",
                            "margin": "auto",
                            "border": "1px solid black",
                            "font-family": "Ubuntu",},
                      )


# callbacks
@app.callback(
    Output(component_id="counter-1-1", component_property="children"),
    [
        Input(component_id="button-1-1-inc", component_property="n_clicks"),
        Input(component_id="button-1-1-dec", component_property="n_clicks"),
        Input(component_id="timer-1-1", component_property="value")
    ],
)
def update_counter_1_1(inc, dec, mode):
    value = inc - dec
    display = "Dage"
    if mode == ["Timer"]:
        display = "Timer"
    elif mode == [] or None:
        display = "Dage"

    if value >= 0:
        return f"{display}: {value}"
    else:
        value = 0
        return f"{display}: {value}"


@app.callback(
    Output(component_id="counter-1-2", component_property="children"),
    [
        Input(component_id="button-1-2-inc", component_property="n_clicks"),
        Input(component_id="button-1-2-dec", component_property="n_clicks"),
        Input(component_id="timer-1-2", component_property="value")
    ],
)
def update_counter_1_2(inc, dec, mode):
    value = inc - dec
    display = "Dage"
    if mode == ["Timer"]:
        display = "Timer"
    elif mode == [] or None:
        display = "Dage"

    if value >= 0:
        return f"{display}: {value}"
    else:
        value = 0
        return f"{display}: {value}"


@app.callback(
    Output(component_id="counter-1-3", component_property="children"),
    [
        Input(component_id="button-1-3-inc", component_property="n_clicks"),
        Input(component_id="button-1-3-dec", component_property="n_clicks"),
        Input(component_id="timer-1-3", component_property="value")
    ],
)
def update_counter_1_3(inc, dec, mode):
    value = inc - dec
    display = "Dage"
    if mode == ["Timer"]:
        display = "Timer"
    elif mode == [] or None:
        display = "Dage"

    if value >= 0:
        return f"{display}: {value}"
    else:
        value = 0
        return f"{display}: {value}"


@app.callback(
    Output(component_id="counter-2-1", component_property="children"),
    [
        Input(component_id="button-2-1-inc", component_property="n_clicks"),
        Input(component_id="button-2-1-dec", component_property="n_clicks"),
        Input(component_id="timer-2-1", component_property="value")
    ],
)
def update_counter_2_1(inc, dec, mode):
    value = inc - dec
    display = "Dage"
    if mode == ["Timer"]:
        display = "Timer"
    elif mode == [] or None:
        display = "Dage"

    if value >= 0:
        return f"{display}: {value}"
    else:
        value = 0
        return f"{display}: {value}"


@app.callback(
    Output(component_id="counter-2-2", component_property="children"),
    [
        Input(component_id="button-2-2-inc", component_property="n_clicks"),
        Input(component_id="button-2-2-dec", component_property="n_clicks"),
        Input(component_id="timer-2-2", component_property="value")
    ],
)
def update_counter_2_2(inc, dec, mode):
    value = inc - dec
    display = "Dage"
    if mode == ["Timer"]:
        display = "Timer"
    elif mode == [] or None:
        display = "Dage"

    if value >= 0:
        return f"{display}: {value}"
    else:
        value = 0
        return f"{display}: {value}"


@app.callback(
    Output(component_id="counter-2-3", component_property="children"),
    [
        Input(component_id="button-2-3-inc", component_property="n_clicks"),
        Input(component_id="button-2-3-dec", component_property="n_clicks"),
        Input(component_id="timer-2-3", component_property="value")
    ],
)
def update_counter_2_3(inc, dec, mode):
    value = inc - dec
    display = "Dage"
    if mode == ["Timer"]:
        display = "Timer"
    elif mode == [] or None:
        display = "Dage"

    if value >= 0:
        return f"{display}: {value}"
    else:
        value = 0
        return f"{display}: {value}"

# create server object
if __name__ == '__main__':
    app.run_server(debug=True)
