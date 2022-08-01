"""
https://shiny.rstudio.com/py/docs/reactive-values.html
"""

from shiny import App, reactive, render, ui

app_ui = ui.page_fluid(
    ui.input_action_button("toggle", "Toggle value"),
    ui.output_text_verbatim("txt")
)


def server(input, output, session):

    # A reactive value
    x = reactive.Value(True)

    # reactive function to button click
    @reactive.Effect
    @reactive.event(input.toggle)
    def _():
        # change the reactive value
        x.set(not x())

    # output that depends of the reactive value
    @output
    @render.text
    def txt():
        return str(x())


app = App(app_ui, server)
