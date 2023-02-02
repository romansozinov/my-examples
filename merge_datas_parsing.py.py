from bs4 import BeautifulSoup
import re

#######
#######
# обединяем данные парсинга в список

html = '<body><p>example <b>text</b> example</p></body>'
soup = BeautifulSoup(html, 'html.parser')

stripped_strings_list = []
for string in soup.stripped_strings: # Note: stripped_strings удаляет лишние пробелы и переносы строк
    stripped_strings_list.append(string)
print(stripped_strings_list)






