spisok = ['Доcпехи бога 1', 'Доcпехи бога 2', 'Доcпехи бога 3']

spisok = zip(spisok) 

for i in spisok:    
    print(f"Вывод данных поочередно: {i[0]}")






l1 = ['Доcпехи бога', 'Доcпехи бога 2', 'Доcпехи бога 3']
l2 = ['1984', '1991', '1995']

_l = zip(l1, l2)

for i in _l:    
    print(f"Название: {i[0]}")
    print(f"Год выпуска: {i[1]}")    
