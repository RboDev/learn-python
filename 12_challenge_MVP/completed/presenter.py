from typing import Protocol
from model import Model


class View(Protocol):

    def init_ui(self, presenter: "Presenter"):
        ...

    def mainloop(self):
        ...


class Presenter():

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def run(self):
        self.view.init_ui(self)
        self.view.mainloop()

    def load_csv(self, file_path: str):
        self.model.load_data(file_path)

    
    def get_raw_data(self) -> str:
        if self.model.raw_data.empty:
            return ""
        else:
            return str(self.model.raw_data)


    def get_processed_data(self) -> str:
        if self.model.processed_data.empty:
            return ""
        else:
            return str(self.model.processed_data)

    def process_data(self, option: str):
        self.model.process_data(option)

    def export_data(self, file_path: str):
        self.model.export_data(file_path)
