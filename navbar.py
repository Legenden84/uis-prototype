from dash import html

navbar = html.Div([
    html.Div(
        [
            html.Button(
                id="button-1",
                children=html.Img(
                    id="img1",
                    src="/assets/overblik_select.png",
                    style={
                        "height": "55px",
                        "width": "93px",
                    }),
                n_clicks=0,
                style={
                    "height": "55px",
                    "border": "none",
                    "margin-left": "0px",
                    "margin-right": "0px",
                    "padding-left": "0px",
                    "padding-right": "0px",
                },
            ),
            html.Button(
                id="button-2",
                children=html.Img(
                    id="img2",
                    src="/assets/kalender_deselect.png",
                    style={
                        "height": "55px",
                        "width": "93px",
                        "margin-left": "0px",
                        "margin-right": "0px",
                        "padding-left": "0px",
                        "padding-right": "0px",
                    }),
                n_clicks=0,
                style={
                    "height": "55px",
                    "border": "none",
                    "margin-left": "0px",
                    "margin-right": "0px",
                    "padding-left": "0px",
                    "padding-right": "0px",
                },
            ),
            html.Button(
                id="button-3",
                children=html.Img(
                    id="img3",
                    src="/assets/beskeder_deselect.png",
                    style={
                        "height": "55px",
                        "width": "93px",
                        "margin-left": "0px",
                        "margin-right": "0px",
                        "padding-left": "0px",
                        "padding-right": "0px",
                    }),
                n_clicks=0,
                style={
                    "height": "55px",
                    "border": "none",
                    "margin-left": "0px",
                    "margin-right": "0px",
                    "padding-left": "0px",
                    "padding-right": "0px",
                },
            ),
            html.Button(
                id="button-4",
                children=html.Img(
                    id="img4",
                    src="/assets/noshow_deselect.png",
                    style={
                        "height": "55px",
                        "width": "94px",
                        "margin-left": "0px",
                        "margin-right": "0px",
                        "padding-left": "0px",
                        "padding-right": "0px",
                    }),
                n_clicks=0,
                style={
                    "height": "55px",
                    "border": "none",
                    "width": "94px",
                    "margin-left": "0px",
                    "margin-right": "0px",
                    "padding-left": "0px",
                    "padding-right": "0px",
                },
            ),
        ],
        style={
            "position": "absolute",
            "height": "55px",
            "bottom": "0px",
            "width": "100%",
            "display": "flex",
            "justify-content": "center",
            "padding": "0px",
            "box-sizing": "border-box",
        },
    )
], style={"margin-top": "0px", "margin-bottom": "0px",})