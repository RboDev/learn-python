import pandas as pd


def celcius_to_kelvin(temperature: float) -> float:
    return temperature + 273.15


def convert_to_scale_0_1(value: float) -> float:
    return value / 100


def compensate_for_sensor_bias(value: float, bias: float = 23) -> float:
    return value + bias


def process_data(data: pd.DataFrame, option: str) -> pd.DataFrame:
    if option in ("Temperature", "Humidity", "CO2"):
        data = data.loc[data["Sensor"] == option]

    return data.apply(process_row, axis=1)


def process_row(row: pd.Series) -> pd.Series:
    sensor: str = row["Sensor"]
    value: float = row["Value"]
    processing_fn = {
        "Temperature": celcius_to_kelvin,
        "Humidity": convert_to_scale_0_1,
        "CO2": compensate_for_sensor_bias,
    }
    row["Value"] = processing_fn[sensor](value)
    return row


def main() -> None:
    raw_data = pd.read_csv("sensor_data.csv")
    processed_data = process_data(data=raw_data, option="All")
    print(processed_data)


if __name__ == "__main__":
    main()
