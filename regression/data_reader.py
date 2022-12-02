"""
Reads CSV files and returns dataframes containing data for task. No need to touch these
"""
import os
from typing import Tuple
import pandas as pd

def read_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Read csv, convert to local Europe/Helsinki format and return as dataframes
    """
    directory_path = os.path.join(os.getcwd(), 'regression', 'files')
    consumption_df = pd.read_csv(os.path.join(directory_path, 'consumptions.csv'))
    temperature_df = pd.read_csv(os.path.join(directory_path, 'temperatures.csv'))
    facility_meter_df = pd.read_csv(os.path.join(directory_path, 'facilities.csv'))
    consumption_df['timestamp'] = pd.to_datetime(consumption_df['timestamp'])
    consumption_df['timestamp'] = consumption_df['timestamp'].dt.tz_convert('Europe/Helsinki')
    temperature_df['timestamp'] = pd.to_datetime(temperature_df['timestamp'])
    temperature_df['timestamp'] = temperature_df['timestamp'].dt.tz_convert('Europe/Helsinki')
    return consumption_df,temperature_df,facility_meter_df
