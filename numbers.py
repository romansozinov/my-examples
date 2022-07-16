# N = int(input("Введите размер списка: "))
# spam = list(range(1, N+1))
# print(spam)

# num = int(input("Введите размер списка: "))
# spisok = list(range(1, num+1))
# b = ['Beginn{}'.format(number) for number in spisok]
# print(b)




# foods = ['pie','apple','bread']
# phrase = 'I like'
# end = 'end'
# statement = [phrase + j for j in foods] 
# print(statement)


links = [
    'link1', 
    'link2', 
    'link3', 
    'link42'
    ]
ddd = ['ddd']    
for i, link in enumerate(links, 1):                                                                                                          
        print(f'{i}{link}ddd')



# MyList = [1,2,3]
# bufer_lst =[]
 
# for element in MyList:
#     bufer_lst.append(element +1 + int("wefwcwe"))
 
# MyList = bufer_lst
# print(MyList)


# num = int(input("Введите размер списка: ")
# spisok = list(range(1, num+1))
# for i, item in enumerate(spisok):
#     print("beginn",i + 1, "end")




# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# for i, m in enumerate(months, 1):  # начитать нумерацию с 1
#    print(f'{i}: {m}')



# items = ['молоко', 'сыр', 'творог', 'кефир', 'яблоко']
# for i, item in enumerate(items):
#     print(i + 1, item)



# items = ['молоко', 'сыр', 'творог', 'кефир', 'яблоко']
# for i, item in enumerate(items):
#     print(i + 1, item)



# list = ['apple','1','5']
# for x,y in enumerate(list, start=1):
#     print(f'{x}{y},')




# from requests.models import PreparedRequest
# url = 'http://example.com/search?q=question'
# params = {'lang':'en','tag':'python'}
# req = PreparedRequest()
# req.prepare_url(url, params)
# print(req.url)