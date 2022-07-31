import shiny


"""
https://shiny.rstudio.com/py/docs/putting-it-together.html

Parsing and displaying a CSV file
"""

import pandas as pd
from io import StringIO

csv_text = """
a,b,c
1,2,3
"""


# shinyapp code snippet
from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui

app_ui = ui.page_fluid(
    ui.input_text_area("csv_txt", "CSV Text", value="a, b\n1,2"),
    ui.output_table("parsed_data"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.table
    def parsed_data():
        txt = input.csv_txt()
        df = pd.read_csv(StringIO(txt))
        return df


app = App(app_ui, server)
