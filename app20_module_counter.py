"""
https://shiny.rstudio.com/py/docs/workflow-modules.html

Shiny modules allow you to create re-usable application components
"""

from shiny import App, reactive, render, ui, module

custom_label = "Some Counter"

@module.ui
def counter_ui(custom_label:str = "Increment counter"):
    return ui.div(
        {"style":"boarder: 1px solid #ccc; border-radius: 5px; margin: 5px 0;"},
        ui.h2("This is " + custom_label),
        ui.input_action_button('button', label=custom_label),
        ui.output_text_verbatim('out'),
    )

@module.server
def counter_server(input, output, session, starting_value=0):
    count = reactive.Value(starting_value)

    @reactive.Effect
    @reactive.event(input.button)
    def _():
        count.set(count() + 1)

    @output
    @render.text
    def out():
        return f"Click count is {count()}"

#app = App(counter_ui, counter_server)