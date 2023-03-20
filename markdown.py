from dash import dcc

help_text = dcc.Markdown(
    """
    Bla bla bla bla bla bla bla bla bla bla bla bla bla bla...
    """,
    style={"font-family": "Calibri",  "margin-left": "8px"}
)

top_remark = dcc.Markdown(
                        """
                        Bemærk, at du selv skal melde dig barn rask, hvis det
                        forekommer at sygdomsforløb ophører.
                        """,
                        style={
                            "margin-left": "8px",
                            "margin-right": "8px",
                            "margin-top": "0px",
                            "padding-top": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Calibri",
                            "font-size": "12px"},
)

bottom_remark = dcc.Markdown(
                            """
                            Bemærkninger kan tilføjes i feltet nedenfor.
                            """,
                            style={
                                "margin-left": "8px",
                                "margin-right": "8px",
                                "margin-bottom": "0px",
                                "backgroundColor": "#D8E1E8",
                                "font-family": "Calibri",
                                "font-size": "12px"}
)