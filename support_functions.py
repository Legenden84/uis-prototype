from dash import html
import dash_daq as daq


def create_switch(id: str):
    switch = daq.BooleanSwitch(
        id=id,
        color="#16425D",
        style={"text-align": "left", "padding-top": "12px", "margin-left": "25px", "display": "inline-block"}
    )
    return switch


def create_inc_buttons(id: str):
    increase = html.Button("+",
                           id="button-" + id + "-inc",
                           n_clicks=0,
                           style={"display": "inline-block", "margin-top": "12px"})
    return increase


def create_counter(id: str):
    counter = html.H2(children="0",
                      id="counter-" + id,
                      style={
                        "font-size": "16px",
                        "font-family": "Calibri",
                        "display": "inline-block",
                        "margin": "0 10px",
                        "padding-top": "12px"})
    return counter


def create_dec_button(id: str):
    decrease = html.Button("-",
                           id="button-" + id + "-dec",
                           n_clicks=0,
                           style={"display": "inline-block", "margin-top": "12px"})
    return decrease