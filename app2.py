from shiny import ui, App, render
import pandas as pd
from matplotlib import pyplot as plt

app_ui = ui.page_fluid(
    # inputs
    ui.input_checkbox(id="x1", label="Checkbox"),
    ui.input_numeric("n1","Number", value=10),
    ui.input_slider("x2", "Slider", value=10, min=0, max=20),
    # outputs
    ui.output_text("some_text"),
    ui.output_table("a_data_frame"),
    ui.output_plot("a_scatter_plot"),
)

def server(input, output, session):

    @output
    @render.text
    def some_text():
        return "hello, world!"

    @output
    @render.table
    def a_data_frame():
        return pd.DataFrame({
            'x':[1,2,3],
            'y':[0,1,0]
        })

    @output
    @render.plot
    def a_scatter_plot():
        df = pd.DataFrame({
            'x':[1,2,3],
            'y':[0,1,0]
        })

        return df.plot()

        


app = App(app_ui, server)
