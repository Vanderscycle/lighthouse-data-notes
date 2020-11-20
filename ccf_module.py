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
# for cat in catVariables.columns.tolist():
#     print(f'There are {data[cat].nunique()} unique {cat}')
#     print(f'{data[cat].unique()} \n')

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
# add argument if the user want to see the values and if so how many
def unique_df_cols(data):    
    catVariables = data[data.dtypes[~(data.dtypes == 'float') | (data.dtypes == 'int')].index.tolist()]
    numVariables = data[data.dtypes[(data.dtypes == 'float') | (data.dtypes == 'int')].index.tolist()]
    print('Only printing the first 20 unique variables')
    print('Categorical variables --------------------------------------------','\n')
    for cat in catVariables.columns.tolist():
        print(f'There are {data[cat].nunique()} unique {cat}')
        print(f'{data[cat].unique()[:20]} \n')
    print('Numerical variables --------------------------------------------','\n')
    for num in numVariables.columns.tolist():
        print(f'There are {data[num].nunique()} unique {num}')
        print(f'The median is  {data[num].median()}, mean {data[num].mean()}\n')
        print(f'{data[num].unique()[:20]} \n')


# PCA analysis
# create a function that takes the df and k and spits outs all the graphs


# cookbook 
## pandas recipes

#Second fastest iteration method
# don't forget that the get and set takes an underscore before
# for i in df.index:
#     val = df._get_value(i,'Outlet_Establishment_Year')
#     #if you want to use days years/months/days 
#     op = dt.date.today().year - val
#     df._set_value( i,'year_operations',op)

## plot cookbook

### Matplotlib
# plt.style.use('dark_background')
# plt.rcParams["figure.figsize"] = (12,8)

# To do:


# don't forget ToDenseTransformer after one hot encoder

class ToDenseTransformer():
    
    # here you define the operation it should perform
    def transform(self, X, y=None, **fit_params):
        return X.todense()

    # just return self
    def fit(self, X, y=None, **fit_params):
        return self

def get_word(n, tokenizer):
      for word, index in tokenizer.word_index.items():
          if index == n:
              return word
      return None
      
def decoder(preds,eng_tokenizer):    
    """ for w9-d4-project"""
    preds_text = []
    for i in preds:
        temp = []
        for j in range(len(i)):
                t = get_word(i[j], eng_tokenizer)
                if j > 0:
                    if (t == get_word(i[j-1], eng_tokenizer)) or (t == None):
                        temp.append('')
                    else:
                        temp.append(t)
                else:
                    if(t == None):
                            temp.append('')
                    else:
                            temp.append(t) 

        preds_text.append(' '.join(temp))
    return preds_text
    
from tensorflow.keras.preprocessing.sequence import pad_sequences
# encode and pad sequences
def encode_sequences(tokenizer, length, lines):
         # integer encode sequences
         seq = tokenizer.texts_to_sequences(lines)
         # pad sequences with 0 values
         seq = pad_sequences(seq, maxlen=length, padding='post')
         return seq

