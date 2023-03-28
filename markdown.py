from dash import dcc

overblik_top_remark = dcc.Markdown(
    """
    I dette faneblad kan du danne dig et overblik over dine registrede sygemeldinger.
    """,
    style={"font-family": "Calibri",  "margin-left": "8px"}
)

help_text_sfo = dcc.Markdown(
    """
    Følg vejledningen nedenfor ved sygemelding:
    * Marker barnet vha. knappen til venstre for
      barnet.

    * Vælg antal dage ved at trykke +/-

    * Ønsker du at registrer fravær i mindre end
      en dag. Kan du anvende intervallet.

    * Tryk registrer fravær.
    """,
    style={"font-family": "Calibri",  "margin-left": "8px", "white-space": "pre"}
)

help_text_skole = dcc.Markdown(
    """
    Følg vejledningen nedenfor ved sygemelding:
    * Marker barnet vha. knappen til venstre for
      barnet.

    * Vælg antal dage ved at trykke +/-

    * Ønsker du at registrer fravær i mindre end
      en dag. Kan du anvende intervallet.

    * Tryk registrer fravær.

    NB: Såfremt at du sygemelder et barn i mindst én
    hel dag. Vil SFO automatisk blive registret. Ønsker
    du kun at sygemelde barnet i skolen. Skal du der-
    for selv fjerne registregingen i SFO.
    """,
    style={"font-family": "Calibri",  "margin-left": "8px", "white-space": "pre"}
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