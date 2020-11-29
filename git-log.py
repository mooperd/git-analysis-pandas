import pandas as pd
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)
dataframe = pd.read_csv("git-log-2020.csv")

dataframe['date'] = pd.to_datetime(dataframe['date'])
grouped_dataframe_count = dataframe.groupby([pd.Grouper(key='date', freq='M'), "email"])[["subject"]].count()

# Select all the users that have contributed more than 20 times.
print(grouped_dataframe[grouped_dataframe['subject'] > 20])


