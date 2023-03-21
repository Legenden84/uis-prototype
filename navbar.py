from dash import html

image1 = "/assets/overblik_deselected.png"
image2 = "/assets/kalender_deselected.png"
image3 = "/assets/beskeder_deselected.png"

navbar = html.Div([
    html.Div(
        [
            html.Button(
                html.Img(
                    id="img1",
                    src=image1, style={"width": "50px", "height": "50px"}),
                    id="button-1",
                    n_clicks=0,
                    style={"border": "none", "background-color": "white", "margin-right": "10px"},
            ),
            html.Button(
                html.Img(
                    id="img2",
                    src=image2, style={"width": "50px", "height": "50px"}),
                    id="button-2",
                    n_clicks=0,
                    style={"border": "none", "background-color": "white", "margin-right": "10px"},
            ),
            html.Button(
                html.Img(
                    id="img3",
                    src=image3, style={"width": "50px", "height": "50px"}),
                    id="button-3",
                    n_clicks=0,
                    style={"border": "none", "background-color": "white"},
            ),
        ],
        style={"display": "flex", "justify-content": "center", "margin-top": "50px"},
    )
])