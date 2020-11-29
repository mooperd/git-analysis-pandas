import pandas as pd
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)
dataframe = pd.read_csv("git-log-2020.csv")

dataframe['date'] = pd.to_datetime(dataframe['date'], errors="coerce")

grouped_dataframe = dataframe.groupby([pd.Grouper(key='date', freq='M'), "email"])[["comment"]].count()
grouped_dataframe.sort_values("comment", ascending=False)
