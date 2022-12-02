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
from pandas.tseries.offsets import BDay #to find business days

ELECTRICITY_QUANTITY_ID = 1
REFERENCE_TEMP = 10
MAX_COOLING_TEMP = 30


def join_temperature(temperatures: pd.DataFrame, consumptions: pd.DataFrame, facility_meters: pd.DataFrame) -> None:
    """
        Task 1, join the temperature data (which uses facility id) to consumption data (which uses meter id).
        facility_meter_df contains mapping between facility and meter
    """
    # ...
    fac_id = []
    print(consumptions['meter_id'])
    for m_id in consumptions['meter_id'].values.tolist():
        for fm in facilities_meters_list:
            
            if m_id in fm:
                fac_id.append(facilities[facilities_meters_list.index(fm)])
    
    consumptions['facility_id'] = fac_id
    #print(consumptions)

    consumptions_new = temperatures.merge(consumptions,how="right", on=['facility_id','timestamp'])
    
    #mean imputation for missing value removal
    from sklearn.impute import SimpleImputer

    mean_imputer = SimpleImputer(strategy='mean')
    consumptions_new['temperature'] = mean_imputer.fit_transform(consumptions_new['temperature'].values.reshape(-1,1))
    consumptions_new['value'] = mean_imputer.fit_transform(consumptions_new['value'].values.reshape(-1,1))
   

    return consumptions_new


def filter_to_weekdays(consumptions: pd.DataFrame) -> pd.DataFrame:
    """
        Task 2, filter out saturdays and sundays from the consumption data
    """
    # ...
    isBusinessDay = BDay().onOffset
    BusinessDay = consumptions["timestamp"].map(isBusinessDay)
    consumptions["BusinessDay"] =  BusinessDay
    
    #print(len(consumptions))
    consumptions = consumptions[consumptions.BusinessDay == True]
    #print(len(consumptions))

    return consumptions


def add_watts_per_square(facility_consumptions: list, facility_area: list) -> list:
    """
        Task 3, create new "column" which is W/m2
        Hint: formula is 'consumption * 1000 / facility_area'
    """
    # ...
    watts_per_square = []
    
    for item in range(0,len(facility_consumptions)):
        #print(facility_consumption[item])
        result = facility_consumptions[item] * 1000 / facility_area[item]
        #print(result)
        watts_per_square.append(result)

    return watts_per_square


def linear_regression(facility_consumptions: pd.DataFrame) -> Tuple[np.array, np.array, float, float]:
    """
        Task 4, model temperature relationship with Watts per square using linear regression
        and return resulting x, y, slope and intercept. Do the regression model only those consumptions
        that are above REFERENCE_TEMP
    """
    # Hint: cooling_consumptions = [... > REFERENCE_TEMP]
    # ...
    #print(type(facility_consumptions['temperature']))
    cooling_consumptions = facility_consumptions[(facility_consumptions['temperature'] > REFERENCE_TEMP) & (facility_consumptions['temperature'] < MAX_COOLING_TEMP)]
    X = cooling_consumptions['temperature'].to_numpy().reshape((-1, 1))
    #print(X)
    y = cooling_consumptions['W/m2'].to_numpy()
    reg = LinearRegression().fit(X, y)
    slope = reg.coef_

    intercept = reg.intercept_

    return X,y,slope,intercept


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
    plt.scatter(x_series,y_series)
    y_reg = reg_intercept + reg_slope * x_series
    plt.plot(x_series, y_reg, 'r')
    plt.show()

    return


facilities = [194, 209, 1066, 3971, 33606]
consumption_df, temperature_df, facility_meter_df = data_reader.read_data()
consumption_df = consumption_df.sort_values(by=['meter_id']) 
temperature_df = temperature_df.sort_values(by=['facility_id']) 
facility_meter_df = facility_meter_df.sort_values(by=['facility_id']) 

facilities_meters_list = []

for i in facilities:
    meter_list = []
    for j in facility_meter_df.loc[facility_meter_df['facility_id'] == i, 'meter_id']:
        meter_list.append(j)
    facilities_meters_list.append(meter_list)


consumpions_combined = join_temperature(temperature_df, consumption_df, facility_meter_df)

consumpions_ready = filter_to_weekdays(consumpions_combined)


values = consumpions_ready['value'].values.tolist()
areas_df = facility_meter_df[['facility_id','area']] 
areas_df = areas_df.drop_duplicates()

#print(areas_df['area'])
list1 = areas_df['area'].values.tolist()
#print(list1)
area_list = []


for m in consumpions_ready['facility_id'].values.tolist():
    #print(facilities.index(m))
    area_list.append(list1[facilities.index(m)])

# df1['area'] = area_list

consumpions_ready['W/m2'] = add_watts_per_square(values, area_list) 

x,y,slope,intercept = linear_regression(consumpions_ready)

for facility_id in facilities:
    print(f'Analyzing {facility_id} now...')

plot_results(consumpions_ready, x, y, slope,intercept)