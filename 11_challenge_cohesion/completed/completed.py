from enum import Enum, auto
import pandas as pd
import os


class Option(Enum):
    All = auto()
    Temperature = auto()
    Humidity = auto()
    CO2 = auto()


def load_data(csv_file_path: str) -> pd.DataFrame:
    if not os.path.exists(csv_file_path):
        raise FileExistsError(f"Could not find CSV file {csv_file_path}")

    data = pd.read_csv(csv_file_path)
    return data


def filter_data(data: pd.DataFrame, option: Option) -> pd.DataFrame:
    match option:
        case Option.All:
            return data
        case _:
            return data.loc[data["Sensor"] == option.name]


def process_data(data: pd.DataFrame) -> pd.DataFrame:

    df = data.set_index(['Timestamp', 'Device', 'Sensor'])
    df = df.unstack('Sensor')

    df.Value.Humidity /= 100
    df.Value.Temperature += 273.15
    df.Value.CO2 += 23

    return df.stack('Sensor').reset_index()


def main() -> None:

    option = Option.All

    data = load_data("sensor_data.csv")
    processed_data = process_data(data)
    filtered_data = filter_data(processed_data, option)

    print(filtered_data)


if __name__ == "__main__":
    main()
