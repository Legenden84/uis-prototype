from dash import html
import dash_bootstrap_components as dbc

transparent_modal_1_1 = dbc.Modal(
    [
        dbc.ModalBody(
            [
                html.H1("Test")
            ]
        )
    ],
    id="transparent-modal-1-1",
    keyboard=False,
    backdrop="static",
    style={
        "border": "none",
        "backgroundColor": "#D8E1E8",
        "position": "absolute"
    }
)