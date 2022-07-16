'''
Сколько надо выпить альтернативного напитка, чтобы принять такую же дозу алкоголя?
'''
print("\n########################")
print("Посчитаем, сколько надо выпить другого алкогольного напитка, чтобы принять такую же дозу алкоголя, как от первого напитка.")
print("########################\n")


print("Введите название первого напитка, который хотите выпить?\n")
napitok = input() 

# Создадим функцию для проверки ввода числа с разделителем точка, а не запятая.
def percent_napitok_point():
    # Бесконечный цикл, который продолжает выполняться  
    # до возникновения исключения
    while True:

        try:
            print("\nСколько % алкоголя в 100 мл. напитка", napitok, "? Введите цифру.\n")            
            global percent_napitok # global - сначала объявим переменную percent_napitok глобальной для использования дальше в других функциях и в коде
            percent_napitok = float(input())
            # while percent_napitok == 0:
            #     try:
            #         percent_napitok = int(input())
            #     except Exception:
            #         print("\nВведите цифру!\n")

            print("\nСколько мл. напитка", napitok, "в 1 сосуде?\n")
            nado_napitok_ml = int(input())

            print("\nСколько таких сосудов напитка", napitok, "Вы хотите выпить?\n")
            nado_napitok_banka = int(input())       
            global result_napitok_ml # global - сначала объявим переменную result_napitok_ml глобальной для использования дальше в других функциях и в коде

            result_napitok_ml = nado_napitok_ml * nado_napitok_banka
            global result_napitok_aclohol
            result_napitok_aclohol = percent_napitok * result_napitok_ml / 96
            
            print("\nВы выпьете", result_napitok_ml, "мл.", "или", nado_napitok_banka, "сосудов", "по", nado_napitok_ml,"мл. напитка", napitok, "крепостью", percent_napitok,"%.", "И примете дозу чистого алкоголя", result_napitok_aclohol, "мл." )  
        
        # Если полученный ввод не число с разделителем точка, будет вызвано исключение
        except ValueError:            
            # Цикл будет повторяться до правильного ввода с разделителем точка, вместо запятой
            print("\nОшибка, Вы ввели число с разделителем долей запятая! Введите % алкоголя в 100 мл. этого напитка", napitok, "с разделителем чисел точка, а не запятая)?\n")

        # При успешном вводе числа с разделителем точка,  
        # цикл закончится.
        else:
            break

# Вызываем функцию
percent_napitok_point()



print("------------------------\n")



print("Введите название альтернативного напитка, на который Вы хотите заменить напиток", napitok, "?\n")
napitok_zamena = input()  

# Создадим функцию для проверки ввода числа с разделителем точка, а не запятая.
def percent_napitok_zamena_point():  
    # Бесконечный цикл, который продолжает выполняться  
    # до возникновения исключения
    while True:

        try:                     
            print("\nСколько % алкоголя в 100 мл. второго напитка", napitok_zamena, ", которым хотите заменить первый напиток", napitok, "?\n")
            percent_napitok_zamena = float(input())  

            result_nado_ml = result_napitok_ml * percent_napitok / percent_napitok_zamena   

            print("\nВместо", result_napitok_ml, "мл. напитка", napitok, "крепостью", percent_napitok, "%", "Вам нужно выпить", result_nado_ml, "мл. второго напитка", napitok_zamena, "крепостью", percent_napitok_zamena,"мл.!\n")
            print("------------------------\n")
            print("Интересно, а сколько надо принять сосудов второго напитка, чтобы выпить столько же", result_napitok_aclohol,"мл. чистого алкоголя?\n")
            print("Введите сколько мл. в 1 сосуде второго напитка", napitok_zamena, "?\n")
            napitok_zamena_ml = int(input())

            result_zamena_banok = result_nado_ml / napitok_zamena_ml
            result_napitok_zamena_aclohol = percent_napitok_zamena * result_nado_ml / 96
            result_napitok_zamena_ml = result_zamena_banok * napitok_zamena_ml

            print("\nВам нужно выпить", result_napitok_zamena_ml, "мл. второго напитка", napitok_zamena, "или", result_zamena_banok, "сосудов вместимостью", napitok_zamena_ml,"мл.", "вместо", result_napitok_ml, "мл.", "напитка", napitok,", чтобы принять столько же", result_napitok_zamena_aclohol,"мл. чистого алкоголя!\n")
        # Если полученный ввод не число с разделителем точка, будет вызвано исключение
        except ValueError:            
            # Цикл будет повторяться до правильного ввода с разделителем точка, вместо запятой
            print("\nОшибка, Вы ввели число с разделителем долей запятая! Введите % алкоголя в 100 мл. этого напитка", napitok_zamena, "с разделителем чисел точка, а не запятая)?\n")

        # При успешном вводе числа с разделителем точка,  
        # цикл закончится.
        else:
            break

# Вызываем функцию
percent_napitok_zamena_point()