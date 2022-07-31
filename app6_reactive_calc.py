"""
https://shiny.rstudio.com/py/docs/reactive-calculations.html
"""


from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui

app_ui = ui.page_fluid(
    ui.input_slider("x", "Choose a Number", 1, 100, 10),
    ui.output_text_verbatim("txt1"),
    ui.output_text_verbatim("txt2"),
)


def server(input: Inputs, output: Outputs, session: Session):

    @reactive.Calc
    def x_times_2():
        val = input.x()*2
        print(f"Running x_times_2(), result is {val}.")
        return val


    @output
    @render.text
    def txt1():
        return f'x times 2 is "{x_times_2()}"'

    @output
    @render.text
    def txt2():
        return f'x times 2 is "{x_times_2()}"'


app = App(app_ui, server)
