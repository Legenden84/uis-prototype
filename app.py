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

        Output(component_id="checklist-1-1", component_property="options"),
    [
        Input(component_id="bool-switch-1-1", component_property="on"),
    ],
)
def toggle_kid_1_1(switch):
    options = [
        {"label": "Tid", "value": "Tid", "disabled": True},
    ]
    if switch == True:
        for option in options:
            option["disabled"] = False
    # else:
    #     options = [{"label": "Tid", "value": "Tid"}]
    print(options)
    return options

# create server object
if __name__ == "__main__":
    app.run_server(debug=True)
