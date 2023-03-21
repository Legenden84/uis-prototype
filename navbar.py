from dash import html

# Define bavbar items as dicts
beskeder = {"src": "/assets/beskeder_deselect.png", "selected_src": "/assets/beskeder_select.png"}
kalender = {"src": "/assets/kalender_deselect.png", "selected_src": "/assets/kalender_select.png"}
overblik = {"src": "/assets/overblik_deselect.png", "selected_src": "/assets/overblik_select.png"}

# Define the navbar layout
navbar = html.Div([
    html.Img(id="item1", src=beskeder["src"], n_clicks=0, className="navbar-item"),
    html.Img(id="item2", src=kalender["src"], n_clicks=0, className="navbar-item"),
    html.Img(id="item3", src=overblik["src"], n_clicks=0, className="navbar-item"),
])