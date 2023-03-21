from dash import html

image1 = "/assets/overblik_deselect.png"
image2 = "/assets/kalender_deselect.png"
image3 = "/assets/beskeder_deselect.png"

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
        style={"display": "flex", "justify-content": "space-between", "margin-top": "50px"},
    )
])