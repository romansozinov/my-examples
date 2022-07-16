from bs4 import BeautifulSoup
import re

src = "<div class=\"test\">Зонт1</div><div>Зонт2</div><div>other stuff</div>"

soup = BeautifulSoup(src, "lxml")

div_1 = soup.find_all('div', text="Зонт2")
num = len(div_1)
print(num)  # [<div>test1</div>]
print(div_1)

div_2 = soup.find_all(
    'div',
    text=re.compile(r'\bЗонт1\b'))  # \btext\b между двумя \b точное вхождение
num = len(div_2)
print(num)  # [<div>test1</div> <div>test2</div>]
print(div_2)
