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
import constants
import data_reader

def join_temperature(temperatures: pd.DataFrame, consumptions: pd.DataFrame, facility_meters: pd.DataFrame) -> None:
    """
        Task 1, join the temperature data (which uses facility id) to consumption data (which uses meter id).
        facility_meter_df contains mapping between facility and meter
    """
    # ...
    return consumptions


def filter_to_weekdays(consumptions: pd.DataFrame) -> None:
    """
        Task 2, filter out saturdays and sundays from the consumption data
    """
    # ...
    return


def add_watts_per_square(facility_consumptions_df: pd.DataFrame, facility_area: float) -> None:
    """
        Task 3, create new "column" which is W/m2
        Hint: formula is 'consumption * 1000 / area'
    """
    # ...
    return


def linear_regression(cooling_consumptions: pd.DataFrame) -> Tuple[np.array, np.array, float, float]:
    """
        Task 4, do the linear regression "temperature with w/m2 ANTTI!" and return: x, y, slope and intercept
    """
    # ...
    return [],[],0,0


def plot_results() -> None:
    """
        Task 5, plot the result
    """
    # ...
    return


facilities = [194, 209, 1066, 3971, 33606]
consumption_df, temperature_df, facility_meter_df = data_reader.read_data()
for facility_id in facilities:
    print(f'Analyzing {facility_id} now...')
    