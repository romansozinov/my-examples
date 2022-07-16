# -*- coding: utf-8 -*-

from datetime import datetime
import time



a = input("Введите первое число: ")
b = input("Введите второе число: ")
c = "Числа одинаковые :)"
d = "Числа разные :("

start_time = datetime.now()

# if a==b:
#     print(c)
# else:
#     print(d)    



### для сокращения времени выполнения скрипта (в данном примере на 15% быстрее), можно сократить кол-во строк кода так:
print(c) if a == b else print(d)



end_time = datetime.now()
print('Start time: {}'.format(start_time))
print('End time: {}'.format(end_time))
print('Duration: {}'.format(end_time - start_time))