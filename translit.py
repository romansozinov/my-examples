# https://docs-python.ru/packages/modul-transliterate-python/

from transliterate import translit
from transliterate import slugify

ru_text = 'Удобный мангал, на котором можно всё!'
text = translit(ru_text, language_code='ru', reversed=True)
print(text)


text = 'Функция крутая! Для составления URL-адреса, ЧПУ!!!'
url = slugify(text)
print(url)
