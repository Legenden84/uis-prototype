import dash_bootstrap_components as dbc
from markdown import *

edit_modal = dbc.Modal(
    [
        dbc.ModalBody(
            [
                dcc.Textarea(
                    placeholder="Indtast kommentar."
                )
            ]
        ),
        dbc.ModalFooter(
            [
                dbc.Button(
                    "OK",
                    id="close-edit",
                    n_clicks=0
                )
            ]
        ),
    ],
    id="modal-edit",
    keyboard=False,
    backdrop="static",
    style={
        "position": "absolute",
        "border": "2px solid black",
        "margin-top": "450px",
        "top": "0",
        "left": "50%",
        "height": "525px",
        "width": "350px",
        "transform": "translate(-50%, -50%)",
        "background-color": "#F7F7F7",
    },
)

modal_open_sfo = dbc.Button("?",
                                id="open-sfo",
                                color="primary",
                                style={
                                    "height": "20px",
                                    "width": "20px",
                                    "font-size": "14px",
                                    "font-family": "Calibri",
                                    "backgroundColor": "#16425D",
                                    "color": "white",
                                    "border-top-left-radius": "8px",
                                    "border-top-right-radius": "8px",
                                    "border-bottom-left-radius": "8px",
                                    "border-bottom-right-radius": "8px",
                                    "margin-right": "6px",
                                    "margin-top": "6px",
                                })

modal_sfo = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Vejledning"),
                    style={
                        "font-family": "Calibri",
                        "font-size": "20px",
                        "margin-left": "8px"},
                    close_button=False),
    dbc.ModalBody(help_text),
    dbc.ModalFooter(
        dbc.Button("Luk",
                    id="close-sfo",
                    className="modal-button",
                    style={
                        "height": "35px",
                        "width": "200px",
                        "font-size": "20px",
                        "font-family": "Calibri",
                        "backgroundColor": "#16425D",
                        "color": "white",
                        "border-top-left-radius": "5px",
                        "border-top-right-radius": "5px",
                        "border-bottom-left-radius": "5px",
                        "border-bottom-right-radius": "5px",
                        })),
    ],
    id="modal-sfo",
    keyboard=False,
    backdrop="static",
    style={
        "position": "absolute",
        "border": "2px solid black",
        "margin-top": "450px",
        "top": "0",
        "left": "50%",
        "height": "525px",
        "width": "350px",
        "transform": "translate(-50%, -50%)",
        "background-color": "#F7F7F7"
    }
)

modal_open_skole = dbc.Button("?",
                                id="open-skole",
                                color="primary",
                                n_clicks=0,
                                style={
                                    "height": "20px",
                                    "width": "20px",
                                    "font-size": "14px",
                                    "font-family": "Calibri",
                                    "backgroundColor": "#16425D",
                                    "color": "white",
                                    "border-top-left-radius": "8px",
                                    "border-top-right-radius": "8px",
                                    "border-bottom-left-radius": "8px",
                                    "border-bottom-right-radius": "8px",
                                    "margin-right": "6px",
                                    "margin-top": "6px",
                                })

modal_skole = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Vejledning"),
                    style={
                        "font-family": "Calibri",
                        "font-size": "32px",

                        "margin-left": "8px"},
                    close_button=False),
    dbc.ModalBody(help_text),
    dbc.ModalFooter(
        dbc.Button("Luk",
                id="close-skole",
                className="modal-button",
                style={
                    "height": "35px",
                    "width": "200px",
                    "font-size": "20px",
                    "font-family": "Calibri",
                    "backgroundColor": "#16425D",
                    "color": "white",
                    "border-top-left-radius": "5px",
                    "border-top-right-radius": "5px",
                    "border-bottom-left-radius": "5px",
                    "border-bottom-right-radius": "5px",
                    })),
    ],
    id="modal-skole",
    keyboard=False,
    backdrop="static",
    style={
        "position": "absolute",
        "border": "2px solid black",
        "margin-top": "450px",
        "top": "0",
        "left": "50%",
        "height": "525px",
        "width": "350px",
        "transform": "translate(-50%, -50%)",
        "background-color": "#F7F7F7"
    }
)
