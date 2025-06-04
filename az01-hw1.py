import pandas as pd

df = pd.read_csv('gdp_per_capita.csv')

print(df.head())

print(df.tail())

print(df.info())

print(df.describe())

print(df[['Entity', 'Year', 'GDP per capita']])