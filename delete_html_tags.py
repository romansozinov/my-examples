# Python. Удалить html-теги из текста

import re

# 1 Если нужно просто подчистить текст от всех тегов (т.е. убрать все, что содержится в угловых скобках), то это можно сделать так:
html = '<b>Hello</b> and <a href="">bye</a>'
text = re.sub('<.*?>', '', html)
print ("1 Подчистить текст от всех тегов: ", text)

# 2 А если, например, надо удалить все ссылки вместе с текстом, то подойдет следующее решение:
html = '<b>Hello</b> and <a href="">bye</a>'
text = re.sub('<a.*?</a>', '', html)
print ("2 Удалить все ссылки вместе с текстом: ", text)

# 3 Удалить только определенный тег:
html = '<b>Hello</b> and <a href="">bye</a> <ul><li>Spisok</li></ul>'
text = re.sub('<ul>|</ul>', '', html)
print ("3 Удалить только определенный тег: ", text)




# 3.2 Удалить только определенные теги
# Использование анализатора HTML намного надежнее, чем использование регулярных выражений. Регулярное выражение не должно использоваться для анализа вложенных структур, таких как HTML.
# Вот рабочая реализация, которая перебирает все теги HTML и для тех, кто не p или br, удаляет их из тега:

from bs4 import BeautifulSoup

mystring = '<b>Ctrong</b> and <a href="">link</a> <ul><li>Spisok</li></ul> or <br> <p>Paragraph</p>'

soup = BeautifulSoup(mystring,'html.parser')
for e in soup.find_all():
    if e.name in ['p','br']:
        e.unwrap()
print ("3.2 Удалить только определенные теги: ",  soup)
# Выход:

# aaa<p>Radio and<br/> television.<br/></p><p>very<br> popular in the world today.</br></p><p>Millions of people watch TV. </p><p>That’s because a radio is very small 98.2%</p><p>and it‘s easy to carry. haha100%</p>bb



# 3.3 Удалить все теги, кроме определенных
# Использование анализатора HTML намного надежнее, чем использование регулярных выражений. Регулярное выражение не должно использоваться для анализа вложенных структур, таких как HTML.
# Вот рабочая реализация, которая перебирает все теги HTML и для тех, кто не p или br, удаляет их из тега:

from bs4 import BeautifulSoup

mystring = '<b>Ctrong</b> and <a href="">link</a> <ul><li>Spisok</li></ul> or <br> <p>Paragraph</p>'

soup = BeautifulSoup(mystring,'html.parser')
for e in soup.find_all():
    if e.name not in ['p','br']:
        e.unwrap()
print ("3.3 Удалить все теги, кроме определенных: ",  soup)
# Выход:

# aaa<p>Radio and<br/> television.<br/></p><p>very<br> popular in the world today.</br></p><p>Millions of people watch TV. </p><p>That’s because a radio is very small 98.2%</p><p>and it‘s easy to carry. haha100%</p>bb





# # 3.1 Удалить только определенный тег:
# html = '<b>Hello</b> and <a href="">bye</a> <ul><li>Spisok</li></ul>'
# text = re.sub('<ul>|</ul>' and '<li>|</li>', '', html)
# print ("3.1 Удалить только определенные теги: ", text)

# # 3.2 Удалить только определенные теги:

# html = '<b>Hello</b> and <a href="">bye</a> <ul><li>Spisok</li></ul>'
# text = re.sub('<ul>|</ul>' and '<li>|</li>', '', html)
# print ("3.2 Удалить только определенные теги: ", text)

# 4 Удалить все html теги:
html = '<b>Strong</b> <FNT name="Century Schoolbook" size="22">Title eferfe wefqwfwqef</FNT> <br>NEW</br> and <a href="">bye</a>'
text = re.sub('<[A-Za-z\/][^>]*>', '', html)
print ("4 Удалить все html теги: ", text)
# print (re.sub('<[A-Za-z\/][^>]*>', '', html))

# 5 В этом примере удаляем пробелы в начале и конце строки и символы переноса строки. Отредактируйте под свои нужды.
html = " balabla\n     blaster  zzz "
text = re.sub("^\s+|\n|\r|\s+$", '', html)
print ("5 Удаляем пробелы в начале и конце строки и символы переноса строки: ", text)

# 6 если вам нужно удалить вообще все пробельные символы (включая переводы строк и табуляцию):
html = " balabla\n     blaster  zzz "
text = re.sub(r'\s', '', html)
print ("6 Удалить вообще все пробельные символы (включая переводы строк и табуляцию): ", text)

# 7 если нужно удалить только лишние пробелы (оставить один)
html = " balabla\n     blaster  zzz "
text = re.sub(r'\s+', ' ', html)
print ("7 Удалить только лишние пробелы (оставить один): ", text)

# 8 удаляем только символ переноса строки
html = "\n bla bla \n\n bla\n"
text = html.replace("\n","") 
print ("8 Удаляем только символ переноса строки: ", text)

# 9 удаляем символ переноса строки и лишние пробелы
html = "\n bla bla \n\n bla\n"
text = html.replace("\n","") # удаляем символ переноса строки
text = re.sub(r'\s+', ' ', text) # удалим лишние пробелы
print ("9 Удаляем символ переноса строки и лишние пробелы: ", text)

# 10 удаляем символ переноса строки, лишние пробелы, и пробелы спереди и сзади.
html = " \n bla bla \n\n bla\n     "
text = html.replace("\n","") # удаляем символ переноса строки
text = re.sub(r'\s+', ' ', text) # удалим лишние пробелы
text = text.strip() # удалим пробелы спереди и сзади
print ("10 Удаляем символ переноса строки, лишние пробелы, и пробелы спереди и сзади: ", text)

# 11 удаляем символ переноса строки \n.
new = '\n bla bla \n\n bla\n'
bla = new.replace('\n', '')
print ("11 удаляем символ переноса строки: ", bla)

# 11.11 удаляем символ переноса строки \n и несколько других символов.
new = '\n bla bla \n\n bla\n | / ! yes'
bla = new.replace('\n', '').replace('|', '').replace('/', '').replace('!', '').replace('yes', '')
print ("11.11 удаляем символ переноса строки и несколько других символов: ", bla)


