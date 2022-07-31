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
    @reactive.event(input.compute) # does not compute at startup (wait user to push the button)
    # @reactive.event(input.compute, ignore_none=False) # * force the computation when session starts
    async def txt():
        # inside the function, reactive dependencies are ignored
        await asyncio.sleep(2)  # simulate long computation
        return f"Result: {input.n()}"


app = App(app_ui, server)

