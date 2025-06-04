import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format  # глобальный формат с запятыми и 2 знаками

df = pd.read_csv('dz.csv')
print(df)

print("\n")

df["City"] = df["City"].fillna("Другой")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df)

print("\n")

group = df.groupby('City')['Salary'].mean()
print(group)

df.to_csv('dz_ver1.csv', index=False)