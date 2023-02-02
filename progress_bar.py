## https://youtu.be/KvucFLbgESM

import time
from alive_progress import alive_it
from alive_progress.styles import showtime, Show
# showtime(Show.BARS) # Demo


# ###### простой вариант
# from tqdm import tqdm
# for a in tqdm (range (100), desc="Loading…."):
#     time.sleep(0.05)
#     pass


total = 100
for item in alive_it(list(range(total)), bar="halloween"):
    time.sleep(0.05)
    print(item)






# # объявляем список животных, которых мы лечим в ветклинике
# animals = ['собака', 'кошка', 'попугай', 'хомяк', 'морская свинка']

# # получаем длину списка и перебираем все его элементы
# for i in alive_it(range(len(animals)), bar="halloween"):
#     time.sleep(0.15)
#     # и выводим их по одному на экран
#     print(animals[i])



# from alive_progress import alive_bar
# import time

# steps = ["slovo",2,3,4,5,6,7]
# with alive_bar(total=len(steps), title="Operation X", theme='smooth') as bar:
#     for s in steps:
#         bar.text = f"Working on Step {s}..."
#         time.sleep(2)
#         bar()