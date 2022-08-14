from shiny import App, render, ui
import plotly.express as px
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
            ui.output_image('plot')
        ),
    ),
)


def server(input, output, session):

    @output
    @render.image
    def plot():
        samples = np.random.normal(
            loc=input.mean(),
            scale=input.sd(),
            size=input.size()
        )

        fig = px.histogram(samples, nbins=input.bins())
        return fig.to_image('png')


app = App(app_ui, server)
