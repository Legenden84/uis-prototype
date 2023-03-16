import dash_bootstrap_components as dbc

modal_open_skole = dbc.Button("?",
                                id="open-skole",
                                color="primary",
                                n_clicks=0,
                                style={
                                "height": "20px",
                                "width": "20px",
                                "font-size": "14px",
                                "font-family": "Ubuntu",
                                "backgroundColor": "#16425D",
                                "color": "white",
                                "border-top-left-radius": "8px",
                                "border-top-right-radius": "8px",
                                "border-bottom-left-radius": "8px",
                                "border-bottom-right-radius": "8px",
                                "margin-right": "6px",
                                "margin-top": "6px",
                                })

modal_skole = dbc.Modal(
    [
        dbc.ModalHeader("Modal header"),
        dbc.ModalBody("Modal body"),
        dbc.ModalFooter(dbc.Button("Close", id="close-skole", className="ml-auto")),
    ],
    id="modal-skole",
)

modal_open_sfo = dbc.Button("?",
                                id="open-sfo",
                                color="primary",
                                style={
                                "height": "20px",
                                "width": "20px",
                                "font-size": "14px",
                                "font-family": "Ubuntu",
                                "backgroundColor": "#16425D",
                                "color": "white",
                                "border-top-left-radius": "8px",
                                "border-top-right-radius": "8px",
                                "border-bottom-left-radius": "8px",
                                "border-bottom-right-radius": "8px",
                                "margin-right": "6px",
                                "margin-top": "6px",
                                })

modal_sfo = dbc.Modal(
    [
        dbc.ModalHeader("Modal header"),
        dbc.ModalBody("Modal body"),
        dbc.ModalFooter(dbc.Button("Close", id="close-sfo", className="ml-auto")),
    ],
    id="modal-sfo",
)