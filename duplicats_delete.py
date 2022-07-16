ints_list = [1, 2, 3, 4, 3, 2]

ints_list2 = list(dict.fromkeys(ints_list))
print(ints_list2)  # [1, 2, 3, 4]  