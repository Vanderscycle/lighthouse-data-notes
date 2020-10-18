#ccf (cool Custom Function)

import pandas as pd
import numpy as np

#SQLite 3 functions:
# w4-d2-mini project3 has the best implementation so falt
import sqlite3
from sqlite3 import Error

connection = 'test'

# sql modules
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# To execute queries in SQLite, use cursor.execute().
def ex_q(connection, query): # execute query
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def er_q(connection, query): #execute read query
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def display_query(query,connection=connection):
    q = er_q(query,connection)
    return pd.read_sql_query(q, connection)

#Data cleaning/Feature engineering functions:
#w3-d3 data-prep-module
# needs to be made into a function
for cat in catVariables.columns.tolist():
    print(f'There are {data[cat].nunique()} unique {cat}')
    print(f'{data[cat].unique()} \n')

# missing data as a percentage of your DF    
def how_much_missing_data (df):
    """ Functions that takes a pd.DF and returns the total of missing values per columns:
        - count of how many are missing
        - from a scale 1(100%) to 0(0%)
        - dtypes    
    """
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    types = df.dtypes
    # also the scale is from 0 to 1
    missing_data = pd.concat([total, percent,types], axis=1, keys=['Total', 'Percent','dtypes'])
    return missing_data 


#data exploration (peek at the unique value)
def unique_df_cols(data):    
    catVariables = data[data.dtypes[~(data.dtypes == 'float') | (data.dtypes == 'int')].index.tolist()]
    numVariables = data[data.dtypes[(data.dtypes == 'float') | (data.dtypes == 'int')].index.tolist()]
    print('Only printing the first 20 unique variables')
    print('Categorical variables','\n')
    for cat in catVariables.columns.tolist():
        print(f'There are {data[cat].nunique()} unique {cat}')
        print(f'{data[cat].unique()[:20]} \n')
    print('Numerical variables','\n')
    for num in numVariables.columns.tolist():
        print(f'There are {data[num].nunique()} unique {num}')
        print(f'{data[num].unique()[:20]} \n')


# PCA analysis
# create a function that takes the df and k and spits outs all the graphs


# cookbook 
## pandas recipes

#Second fastest iteration method
# don't forget that the get and set takes an underscore before
for i in df.index:
    val = df._get_value(i,'Outlet_Establishment_Year')
    #if you want to use days years/months/days 
    op = dt.date.today().year - val
    df._set_value( i,'year_operations',op)

## plot cookbook

### Matplotlib
# plt.style.use('dark_background')
# plt.rcParams["figure.figsize"] = (12,8)