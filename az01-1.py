import pandas as pd

# Структура Series
## Создаем список
data = [1, 2, 3, 4, 5]
## Сохраним этот список в переменную series
series = pd.Series(data)
print(series)

# Структура Dataframe
## Создаем словарь с названиями столбцов и значениями, которые будут содержаться в этих столбцах
data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
}
## Преобразуем созданный словарь data в датафрейм, то есть, в таблицу. Для этого используем функцию df
df = pd.DataFrame(data)
print(df)

## Сохраняем в отдельный файл
df.to_csv('output.csv', index=False)
