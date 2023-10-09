import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from typing import Protocol


class Presenter(Protocol):
    
    def load_csv(file_path:str):
        ...

    def get_raw_data() -> str:
        ...

    def get_processed_data() -> str:
        ...

    def process_data(option:str):
        ...

    def export_data(file_path:str):
        ...


class View(tk.Tk):

    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Data Processing GUI")

    def init_ui(self, presenter: Presenter):
        
        self.presenter = presenter

        # Create the widgets for the GUI
        load_button = tk.Button(self.root, text="Load CSV", command=self.load_csv)
        show_input_data_button = tk.Button(
            self.root, text="Show input data", command=self.show_input_data
        )
        analyze_button = tk.Button(self.root, text="Analyze Data", command=self.analyze_data)
        # Create a variable to store the selected option
        self.selected_option = tk.StringVar(self.root)
        # Create a list of options
        options = ["All", "Temperature", "Humidity", "CO2"]
        # Set the default selected option
        self.selected_option.set(options[0])
        # Create an OptionMenu widget
        option_menu = tk.OptionMenu(self.root, self.selected_option, *options)

        export_button = tk.Button(self.root, text="Export Data", command=self.export_data)
        # Create a Text widget to display the data
        self.text_widget = tk.Text(self.root)

        # Arrange the widgets in the main window
        self.text_widget.pack(side=tk.BOTTOM)
        load_button.pack(side=tk.LEFT)
        show_input_data_button.pack(side=tk.LEFT)
        analyze_button.pack(side=tk.LEFT)
        option_menu.pack(side=tk.LEFT)
        export_button.pack(side=tk.LEFT)

        # Start the main loop
        self.root.mainloop()


    def load_csv(self):
        # Code to load the CSV file
        file_path = fd.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.presenter.load_csv(file_path)
        mb.showinfo("Import", "Data successfully loaded!")

    def show_input_data(self):
        data = self.presenter.get_raw_data()
        # Clear widget from previous data
        self.text_widget.delete("1.0", tk.END)
        try:
            # Set the text of the widget to the data
            self.text_widget.insert(tk.END, data)
        except NameError:
            mb.showinfo("Error", "No data to show!")

    def analyze_data(self):
        if self.presenter.get_raw_data() == "":
            mb.showerror("Error", "Please load data first!")
            return
        self.presenter.process_data(self.selected_option.get())
        # Clear widget from previous data
        self.text_widget.delete("1.0", tk.END)
        # set the text of the widget to the data
        self.text_widget.insert(tk.END, str(self.presenter.get_processed_data()))

    def export_data(self):
        file_path = fd.asksaveasfile(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )
        if file_path is not None:
            self.presenter.export_data(file_path)
            mb.showinfo("Export", "Data exported successfully!")