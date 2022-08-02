"""
   https://shiny.rstudio.com/py/docs/reactive-mutable.html

   https://pypi.org/project/pyrsistent/ for immutable types lits -> PVector
"""

from shiny import App, reactive, render, render_text, ui

app_ui = ui.page_fluid(
    ui.input_numeric("x", "Enter a value to add to the list", 1),
    ui.input_action_button("submit", "Add Value"),
    ui.p(
        ui.output_text_verbatim("out")
    )
)


def server(input, output, session):

    # stores all the values submitted values by the user
    user_provided_values = reactive.Value([])

    @reactive.Effect
    @reactive.event(input.submit)
    def add_value_to_list():
        # values = user_provided_values().copy() # * Works if we copy (will mutate the list)
        # values.append(input.x())
        # user_provided_values.set(values)  # does not work either

        # Or use the copy on update technique
        user_provided_values.set(user_provided_values() + [input.x()])

    @output
    @render.text
    def out():
        return f"Values: {user_provided_values()}"


app = App(app_ui, server)
