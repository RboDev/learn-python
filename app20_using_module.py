from shiny import App, ui
from app20_module_counter import counter_server, counter_ui

app_ui = ui.page_fluid(
    counter_ui("counter1", "Counter1"),
    counter_ui("counter2", "Counter2"),
)


def server(input, outpu, session):
    counter_server("counter1")
    counter_server("counter2")


app = App(app_ui, server)
