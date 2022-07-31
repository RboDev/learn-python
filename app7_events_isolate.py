"""
https://shiny.rstudio.com/py/docs/reactive-events.html

We don't want than a input cause the dependant function to execute.
Typical case here only want the Compute button triggers the invalidation.


"""

import asyncio

from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", 1, 100, 1),
    ui.input_action_button("compute", "Compute Now"),
    ui.output_text_verbatim("txt"),
)


def server(input: Inputs, output: Outputs, session: Session):

    @output
    @render.text
    async def txt():
        input.compute()         # triggers when compute button is pressed
        await asyncio.sleep(2)  # simulate long computation

        with reactive.isolate():
            # the input slider will not cause the invalidation
            return f"Result: {input.n()}"


app = App(app_ui, server)

