import pandas as pd


def celcius_to_kelvin(temperature: float) -> float:
    return temperature + 273.15


def convert_to_scale_0_1(value: float) -> float:
    return value / 100


def compensate_for_sensor_bias(value: float, bias: float = 23) -> float:
    return value + bias


class Model:

    def __init__(self):
        self._raw_data = pd.DataFrame()
        self._processed_data = pd.DataFrame()

    @property
    def raw_data(self):
        return self._raw_data

    @property
    def processed_data(self):
        return self._processed_data

    def load_data(self, file_path: str):
        self._raw_data = pd.read_csv(file_path)
        self._processed_data = pd.DataFrame()

    def export_data(self, file_path: str):
        self._processed_data.to_csv(file_path, index=False)

    def process_data(self, option: str):

        data = self._raw_data
        processed_data: list[pd.DataFrame] = []

        if option in ("Temperature", "Humidity", "CO2"):
            data = data.loc[data["Sensor"] == option]

        for _, row in data.iterrows():
            processed_row = self.process_row(row)
            processed_data.append(processed_row)

        self._processed_data = pd.DataFrame(processed_data)

    def process_row(self, row: pd.DataFrame) -> pd.DataFrame:
        sensor: str = row["Sensor"]
        value: float = row["Value"]
        processing_fn = {
            "Temperature": celcius_to_kelvin,
            "Humidity": convert_to_scale_0_1,
            "CO2": compensate_for_sensor_bias,
        }
        row["Value"] = processing_fn[sensor](value)
        return row
