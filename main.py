import pandas as pd
from tabulate import tabulate

#due to enormous size of our data set and the pandas' interpretetion of column of unknown type as <object> (which is quite memory-intensive) we need to manually define data type of each column

dtypes={
    "FL_DATE": "str",
    "AIRLINE": "str",
    "AIRLINE_CODE": "str",
    "FL_NUMBER": "int",
    "ORIGIN": "str",
    "ORIGIN_CITY": "str",
    "DEST": "str",
    "DEST_CITY": "str",
    "CRS_DEP_TIME": "int",
    "DEP_DELAY": "float64",
    "TAXI_OUT": "float64",
    "TAXI_IN": "float64",
    "CRS_ARR_TIME": "int",
    "ARR_DELAY": "float64",
    "CANCELLED": "bool",
    "CANCELLATION_CODE": "str",
    "DIVERTED": "bool",
    "DISTANCE": "int",
    "DELAY_DUE_CARRIER": "float64",
    "DELAY_DUE_WEATHER": "float64",
    "DELAY_DUE_NAS": "float64",
    "DELAY_DUE_SECURITY": "float64",
    "DELAY_DUE_LATE_AIRCRAFT": "float64"
}

data_set = pd.read_csv('clean_data_set.csv', dtype=dtypes)

data_set_origin = data_set[['ORIGIN', 'ORIGIN_CITY']]

data_set_dest = data_set[['DEST', 'DEST_CITY']]

data_set_origin.columns = ['AIRPORT', 'CITY']
data_set_dest.columns = ['AIRPORT', 'CITY']

data_set_airports = pd.concat([data_set_origin, data_set_dest], ignore_index=True)

data_set_airports = data_set_airports.drop_duplicates()



#cretating a dictionary of airports and their cities
airports_dict = dict(zip(data_set_airports.AIRPORT, data_set_airports.CITY))
print(airports_dict)

