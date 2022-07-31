from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
import pandas as pd
import seaborn as sns
from pathlib import Path

sns.set_theme()

long_breeds = pd.read_csv(Path(__file__).parent / "dog_traits_long.csv")
options_traits = long_breeds.trait.unique().tolist()
options_breeds = long_breeds.breed.unique().tolist()


app_ui = ui.page_fluid(
    ui.input_selectize('traits','Traits',choices=options_traits, multiple=True),
    ui.input_selectize('breeds','Breeds',choices=options_breeds, multiple=True),
    ui.output_plot('barchart')
)


def server(input: Inputs, output: Outputs, session: Session):

    @output
    @render.plot
    def barchart():
        
        # get inputs
        indx_trait = long_breeds.trait.isin(input.traits())
        indx_breed = long_breeds.breed.isin(input.breeds())

        # filter data
        df = long_breeds[indx_breed & indx_trait]
        df['dummy'] = 1

        # plot
        p = sns.catplot(
            data = df, kind="bar",
            y='rating', x='dummy', hue='trait',
            col='breed', col_wrap=3,
        )

        p.set_xlabels("")
        p.set_xticklabels("")
        p.set_titles(col_template="{col_name}")

        return p


app = App(app_ui, server)
