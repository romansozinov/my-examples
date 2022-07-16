
from unittest import result


def helloUsers(username, profession):
    """ Функция приветствия пользователя и его профессия """
    
    # print(f'Hello, {username}! Are you {profession}.')
    # print('-' * 20)
    
    return (f'Hello, {username}! Are you {profession}.')
    return ('-' * 20)
        
# helloUsers('Roman','Programmer')
# helloUsers('Pepe','Driver')
# helloUsers('Ana','Medico')

print(helloUsers('Roman','Programmer'))
print(helloUsers('Pepe','Driver'))
print(helloUsers('Ana','Medico'))
print('-' * 20)
result = helloUsers('Roman','Programmer')
print(result)

