
# https://www.andreyolegovich.ru/code/python/isinstance.php?ysclid=l7orkrmpcb752982823

# str (строка)
# list (список)
# tuple (кортеж)
# dict (словарь)
# set (множество)
# bool (логический тип данных)
# range object (a type of iterable)

# str (строка) или (текст):
var_str = 'heihei.ru'

# list (список):
var_list = ['heihei.ru','topbicycle.ru','urn.su']

# tuple (кортеж):
var_tuple = ('andreyolegovich.ru', 'aredel.com')

# пример простого словаря
dictionary = {'Огонёк': 'уменьш. от слова "Огонь"'}

# пример множества
integer_num_set = {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}

# Boolean Type: bool (логический тип данных) В каком-то смысле наиболее простой и самый понятный из всех типов данных. У bool есть всего два значения:
# Истина (True);
# Ложь (False)
# Однако за этой простотой кроется колоссальный пласт теории в виде булевой алгебры.
# # пример bool:
# pravda = True,
# lozh = False
var_bool = True

# range object (a type of iterable)
# Крутая особенность языка Python состоит в наличии в нём встроенной функции range(), которая способна генерировать непрерывную последовательность целых чисел:
# r = range(10)
# print(r)
# > range(0, 10)

# for i in r:
#     print(i, end=' ')
# > 0 1 2 3 4 5 6 7 8 9
# Она крайне удобна для создания циклов for.
var_range = range(0,9)

print(type(var_str))
print(type(var_list))
print(type(var_tuple))
print(type(dictionary))
print(type(integer_num_set))
print(type(var_bool))
print(type(var_range))



