"""
https://shiny.rstudio.com/py/docs/ui-page-layouts.html
"""


from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np


app_ui = ui.page_fluid(
    ui.panel_title("Simulate a normal distribution"),

    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider('size', 'Sample size', value=250, min=0, max=1000),
            ui.input_numeric('mean', "Mean", 0),
            ui.input_numeric('sd', "Standard deviation", 1),
            ui.input_slider('bins', 'Number of bins',
                            value=20, min=0, max=100),
        ),
        ui.panel_main(
            ui.output_plot('plot')
        ),
    ),
)


def server(input, output, session):

    @output
    @render.plot
    def plot():
        samples = np.random.normal(
            loc=input.mean(),
            scale=input.sd(),
            size=input.size()
        )

        fig, ax = plt.subplots()
        ax.hist(samples, input.bins(), density=True)
        return fig


app = App(app_ui, server)
