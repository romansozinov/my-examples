# -*- coding: utf-8 -*-
import csv
import numpy as np
import pandas as pd
import dask.dataframe as dd
# import datetime
import time
from datetime import timedelta


def main():
    
    filename = '100m.csv'

    # ### сгенерим файл csv на 1 млн. рандомных записей и 100 млн. строк.  https://www.youtube.com/watch?v=PpROGV72k_A
    # df = pd.DataFrame(np.random.randint(1, 10 ** 2, size=(10 ** 2, 10)), columns=list('ABCDEFGHIJ'))
    # df.to_csv(f'examples/2gis/{filename}')
    # ### END сгенерим файл csv на 1 млн. рандомных записей и 100 млн. строк.

    # ### конвертируем CSV в формат parquet для ускорения работы с таблицами в 10 раз
    # df = dd.read_csv(f'examples/2gis/{filename}')
    # df.to_parquet('examples/2gis/100m_parquet')
    # ### END конвертируем CSV в формат parquet для ускорения работы с таблицами в 10 раз

    st = time.time()
    df1 = dd.read_csv(f'/Users/romansozinov/MyProjects/GitHub my projects/my-examples/2gis/{filename}')
    print(df1['B'].mean().compute())
    print(time.time() - st)

    st = time.time()
    df2 = dd.read_parquet(f'/Users/romansozinov/MyProjects/GitHub my projects/my-examples/2gis/100m_parquet/part.*.parquet')
    print(df2['B'].mean().compute())
    print(time.time() - st)    




if __name__ == '__main__':
    main()





# # with open("examples/2gis/2gis.csv", newline = '') as csvfile:
### https://www.youtube.com/watch?v=3lpqHCvHOAk
# with open("/Users/romansozinov/Клиенты Mac/Рассылки и базы/2Gis Мой парсинг/2Гис Москва, Все рубрики, кроме власть, жкх и прочие (только колонки с данными для рандомизации).csv", newline = '') as csvfile:
#     reader = csv.DictReader(csvfile,delimiter=";")
#     for row in reader:
#         # print(row['№'],'|',row['Дата Обновления'],row['Дата Добавления'],row['Название'])
#         print(row['№'],'|',row['Дата Обновления'],'|',row['Название'])
# # with open("new_file.csv", 'w', newline = '') as csvfile:
# #     writer = csv.writer(csvfile, delimiter=";")
# #     writer.writerow(["row 1 el 1","row 1 el 2","row 1 el 3"])
# #     writer.writerow(["row 2 el 1","row 2 el 2","row 2 el 3"])
# #     writer.writerow(["row 3 el 1","row 3 el 2","row 3 el 3"])






### Колонки 2Гис.

# 1) Вся РФ, кроме Москвы и СПб.Все рубрики, кроме власть, жкх и прочие

# "№"	"Дата Обновления"	"Дата Добавления"	"Название"	"Тип"	"Страна"	"Регион"	"Населенный Пункт"	"Район"	"Индекс"	"Адрес"	"Комментарий к адресу"	"Раздел"	"Подраздел"	"Рубрика"	"Ключевое слово"	"Телефоны"	"Сотовый"	"Метро (Остановка)"	"Email"	"Сайт"	"Vk.com"	"Twitter.com"	"Facebook.com"	"Instagram.com"	"X"	"Y"	"Количество Филиалов"	"Рейтинг"	"Количество  Отзывов"	"Главное Фото"	"Средний Чек"	"Дополнительно"	"Время Работы"	"Заголовок"	"Информация"	"Описание"

# 2) 2Гис Москва, Все рубрики, кроме власть, жкх и прочие (только колонки с данными для рандомизации)

# №	Дата Обновления	Название	Тип	Регион	Населенный Пункт	Район	Индекс	Адрес	Комментарий к адресу	Раздел	Подраздел	Рубрика	Телефоны	Сотовый	Метро (Остановка)	Email	Сайт	Vk.com	Twitter.com	Facebook.com	Instagram.com	X	Y	Количество Филиалов	Рейтинг	Заголовок	Описание


### END Колонки 2Гис.
