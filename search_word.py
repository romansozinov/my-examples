# поиск слов по наличию букв с помощью регулярных выражений библиотеки re

import re

# words = "меня звать Олег, мне 35 лет"
# search_word = "звать"
# if re.search(r'\bзвать\b', words):
#     print(search_word) # выводит слово, если нашлось полное совпадение



products_upsells = "'\"2528\":{\"name\":{\"value\":\"NDL_2894\",\"class\":\".product-NDL-info-main NDLwefwefef .product-nam {\"value\":\"NDL_2893\"'"

# print(*filter(lambda x: 'N' in x, products_upsells))



# text = "Hregerwg The film Titanic NDL_2894 was released in 1998"
# result = re.match(r"[a-zA-z]+", text)
# print(result.group(0)) # выводит первое слово в тексте


result = re.findall(r'[NDL]\w+', products_upsells)
print (result) # выводит все слова, содержащие буквы NDL


# words = ['Python', 'NDL_2894 wewefwef', 'easy', 'to', 'learn']
# print(*filter(lambda x: 'N' in x, words)) # выводит полное содержимое текста, если найдена буква N