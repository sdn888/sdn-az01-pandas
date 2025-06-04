import pandas as pd
df = pd.read_csv('World-happiness-report-2024.csv')
# Если датасет находится в формате Excel, вместо csv необходимо прописать read_excel.

print(df.head())

print(df.tail())

print(df.info())

print(df.describe())

print(df['Country name'])

print(df[['Country name', 'Regional indicator']])

print(df.loc[56]) # вывод определенной строки - например номер 56

print(df.loc[56, 'Healthy life expectancy'])

print(df[df['Healthy life expectancy'] > 0.7])
