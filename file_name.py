
# https://all-python.ru/osnovy/put-imya-i-rasshirenie-fajla.html?ysclid=l7oztp12fi515821224#imya-fajla
# Имя файла
# Чтобы узнать имя файла из полной строки с путем, воспользуемся методом basename модуля os.
import os
name = os.path.basename(r'/Users/romansozinov/MyProjects/GitHub my projects/my-examples/file.txt')
print(name)
# file.txt
# Здесь перед строкой вставил r, чтобы подавить возможное возникновение служебных символов. Например, в данном случае если не указать r, то \f считалось бы символом перевода страницы.

# Без расширения
# Теперь разберемся, как в Python узнать имя файла без расширения. Воспользуемся методом splittext. В этот раз для примера возьмем файл с двойным расширением, чтобы проверить, как будут в этой ситуации работать стандартны функции.
from os import path
full_name = path.basename(r'/Users/romansozinov/MyProjects/GitHub my projects/my-examples/file.tar.gz')
name = path.splitext(full_name)[0]
print(name)
# file.tar

# Видно, что последнее расширение архиватора gz было отброшено, в то время как расширение несжатого архива tar осталось в имени.
# Если же нам нужно только имя, то можно отбросить все символы полученной строки, которые идут после первой точки. Символ точки тоже отбросим.
# Дополним предыдущий пример следующим кодом:
index = name.index('.')
print(name[:index])
# file