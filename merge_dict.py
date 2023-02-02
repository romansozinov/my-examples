#######
#######
# обединяем списки в один

l1 = [[1, 2, 3], [4, 5, 6]]
print(sum(l1, [])) # [1, 2, 3, 4, 5, 6]

from itertools import chain
print(list(chain.from_iterable(l1))) # [1, 2, 3, 4, 5, 6]

l2 = [['12', '34'], ['56', '78']]
print(list(map(''.join, l2))) # ['1234', '5678']

a = [i ** 2 for i in range(1,11)]
print(a) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]