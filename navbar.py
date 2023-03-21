from dash import html

overblik_pic = "/assets/overblik_deselect.png"
kalender_pic = "/assets/kalender_deselect.png"
beskeder_pic = "/assets/beskeder_deselect.png"

navbar = html.Div([
    html.Div(
        [
            html.Button(
                html.Img(
                    id="img1",
                    src=overblik_pic,
                    style={
                        "height": "55px",
                        "width": "93px",
                        "margin-left": "0px",
                        "margin-right": "0px",
                        "padding-left": "0px",
                        "padding-right": "0px",
                    }),
                    id="button-1",
                    n_clicks=0,
                    style={
                        "border": "none",
                        "margin-left": "0px",
                        "margin-right": "0px",
                        "padding-left": "0px",
                        "padding-right": "0px",
                    },
            ),
            html.Button(
                html.Img(
                    id="img2",
                    src=kalender_pic,
                    style={
                        "height": "55px",
                        "width": "93px",
                        "margin-left": "0px",
                        "margin-right": "0px",
                        "padding-left": "0px",
                        "padding-right": "0px",
                    }),
                    id="button-2",
                    n_clicks=0,
                    style={
                        "border": "none",
                        "margin-left": "0px",
                        "margin-right": "0px",
                        "padding-left": "0px",
                        "padding-right": "0px",
                    },
            ),
            html.Button(
                html.Img(
                    id="img3",
                    src=beskeder_pic,
                    style={
                        "height": "55px",
                        "width": "93px",
                        "margin-left": "0px",
                        "margin-right": "0px",
                        "padding-left": "0px",
                        "padding-right": "0px",
                    }),
                    id="button-3",
                    n_clicks=0,
                    style={
                        "border": "none",
                        "margin-left": "0px",
                        "margin-right": "0px",
                        "padding-left": "0px",
                        "padding-right": "0px",
                    },
            ),
        ],
        style={
            "position": "absolute",
            "bottom": "0px",
            "width": "100%",
            "display": "flex",
            "justify-content": "center",
            "padding": "0px",
            "box-sizing": "border-box",
        },
    )
])