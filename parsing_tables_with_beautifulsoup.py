from datetime import datetime
from pandas import ExcelWriter
from bs4 import BeautifulSoup
import requests
import pandas
import openpyxl

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8',
}


def info(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    # количество страниц
    pages_block = soup.find('p', class_='text-muted float-right font-small-3 mb-0 mt-2')
    pages = pages_block.get_text().split(' ')[-1].replace('.', '').rstrip()
    # заголовок таблицы
    title = soup.h1.get_text()
    print(f'Таблица: {title}. Количество страниц: {pages}')
    return title


def parse(url):
    title = info(url)
    data = []
    pages = int(input('Введите кол-во страниц для сбора: '))
    for page in range(1, int(pages) + 1):
        link = f'{url}{page}/'
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        # целевая таблица
        tables = soup.find('tbody')

        # проход по строкам
        for stats in tables.find_all('tr'):
            # находим каждую ячейку строки
            rows = stats.find_all('td')

            # проверки на то что значение может быть пустое
            try:
                col0 = rows[0].text.strip()
            except:
                col0 = ''

            try:
                col1 = rows[1].text.strip()
            except:
                col1 = ''

            try:
                col2 = rows[2].text.strip()
            except:
                col2 = ''

            try:
                col3 = rows[3].text.strip()
            except:
                col3 = ''

            try:
                col4 = rows[4].text.strip()
            except:
                col4 = ''

            # заполняем список данными
            data.append({
                'Диапазон IP-адресов': col0,
                'Страна': col1,
                'Государство / Регион': col2,
                'город': col3,
                'ISP (Интернет-провайдер)': col4
            })
        print(f'Сбор данных с {page} страницы из {pages}...')
    print(f'Сбор данных завершен. Собрано {len(data)} строк.')
    save_data(data, title)


def save_data(data, title):
    # сохраняем в эксель
    date_time = datetime.now()
    date = date_time.strftime("%d-%m-%Y")
    df = pandas.DataFrame(data)
    writer = ExcelWriter(f'{title} {date}.xlsx')
    df.to_excel(writer, 'Лист1')
    writer.save()
    print(f'Данные сохранены в файл "{title} {date}.xlsx"')


if __name__ == "__main__":
    parse('https://awebanalysis.com/ru/ipv4-directory/')
