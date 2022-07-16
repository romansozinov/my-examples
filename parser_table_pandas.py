import pandas as pd
from xml.etree import ElementTree as ET

table_data = pd.read_html('https://html5book.ru/html-table/')


table = ET.XML(table_data)
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]
    print(dict(zip(headers, values)))