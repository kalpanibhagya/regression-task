# pylint: disable=E1101
# pylint: disable=C0114
# pylint: disable=C0301
# pylint: disable=W0613
# pylint: disable=C0116
from typing import Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import data_reader


ELECTRICITY_QUANTITY_ID = 1
REFERENCE_TEMP = 10
MAX_COOLING_TEMP = 30


def join_temperature(temperatures: pd.DataFrame, consumptions: pd.DataFrame, facility_meters: pd.DataFrame) -> None:
    """
        Task 1, join the temperature data (which uses facility id) to consumption data (which uses meter id).
        facility_meter_df contains mapping between facility and meter
    """
    # ...
    return consumptions


def filter_to_weekdays(consumptions: pd.DataFrame) -> pd.DataFrame:
    """
        Task 2, filter out saturdays and sundays from the consumption data
    """
    # ...
    return consumptions


def add_watts_per_square(facility_consumptions: pd.DataFrame, facility_area: float) -> None:
    """
        Task 3, create new "column" which is W/m2
        Hint: formula is 'consumption * 1000 / facility_area'
    """
    # ...
    return


def linear_regression(facility_consumptions: pd.DataFrame) -> Tuple[np.array, np.array, float, float]:
    """
        Task 4, model temperature relationship with Watts per square using linear regression
        and return resulting x, y, slope and intercept. Do the regression model only those consumptions
        that are above REFERENCE_TEMP
    """
    # Hint: cooling_consumptions = [... > REFERENCE_TEMP]
    # ...
    return [],[],0,0


def plot_results(
    week_day_consumptions: pd.DataFrame,
    x_series: np.array,
    y_series: np.array,
    reg_slope: float,
    reg_intercept: float) -> None:
    """
        Task 5, plot the result
    """
    # ...
    return


facilities = [194, 209, 1066, 3971, 33606]
consumption_df, temperature_df, facility_meter_df = data_reader.read_data()
consumpions_combined = join_temperature(temperature_df, consumption_df, facility_meter_df)
consumpions_ready = filter_to_weekdays(consumpions_combined)
for facility_id in facilities:
    print(f'Analyzing {facility_id} now...')
