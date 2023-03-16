import dash_daq as daq

def create_switch(id: str):
    switch = daq.BooleanSwitch(
        id=id,
        color="#16425D",
        style={"text-align": "left", "padding-top": "12px", "margin-left": "25px", "display": "inline-block"}
    )
    return switch