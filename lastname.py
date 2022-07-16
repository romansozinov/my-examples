lastname = input("Whats your Lastname?") #введите фамилию

# # замена с помощью цикла и условия
# print(lastname) # вывод фамилии

# lastname_change = "" # создадим пустую переменную для сравнения её с символами в переменной lastname

# for search_letter in lastname: # пройдемся и сравним по циклу все символы фамилии lastname с новой переменной search_letter
#     if search_letter == "в": # если search_letter равна букве в,
#         search_letter = "!" # то присваиваем переменной search_letter знак !
#     lastname_change = lastname_change + search_letter # и добавляем к пустой переменной lastname_change знак ! из search_letter
# print(lastname_change)
# # END замена с помощью цикла и условия


print(str(lastname).replace('в', '!')) # заменяет в строке букву в на знак !
