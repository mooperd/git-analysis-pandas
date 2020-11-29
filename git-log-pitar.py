import pandas as pd
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)
dataframe = pd.read_csv("git-log-2020.csv")
dataframe['date'] = pd.to_datetime(dataframe['date'])
top_three = dataframe.groupby(pd.Grouper(key='date', freq='M'))['email'].value_counts().sort_values(ascending = False).head(3)

print(top_three)

    
# 

# dataframe.groupby(pd.Grouper(key='date', freq='M'))['email'].value_counts().sort_values(ascending = False).head(3))


# grouped_dataframe_count = dataframe.groupby([pd.Grouper(key='date', freq='M'), "email"])[["subject"]].count()
# grouped_dataframe_agg = dataframe.groupby([pd.Grouper(key='date', freq='M'), "email"])[["subject"]].agg(['count'])

# grouped_dataframe_count.groupby(pd.Grouper(key='date', freq='M'))['email'].value_counts().sort_values(ascending = False).head(3)

#print(grouped_dataframe_count["subject"].transform(max))
# Select all the users that have contributed more than 20 times.
# print(grouped_dataframe_count[grouped_dataframe_count['subject'] > 20])



# grouped_dataframe_agg = dataframe.groupby([pd.Grouper(key='date', freq='M'), "email"]).agg({'subject': {lambda x: x.nlargest(2).count() }})

