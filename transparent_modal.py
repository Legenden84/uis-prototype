from dash import html
import dash_bootstrap_components as dbc

transparent_modal_2_1 = dbc.Modal(
    [
        dbc.ModalHeader("Modal Header"),
        dbc.ModalBody("This is the content of the modal"),
        dbc.ModalFooter(
            dbc.Button("Close", id="close", className="ml-auto")
        ),
    ],
    id="transparent-modal-2-1",
    # is_open=False,
    keyboard=False,
    backdrop="static",
    style={
        "border": "none",
        "backgroundColor": "red",
        # "position": "absolute"
    }
)