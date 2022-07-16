import re

# Read in the file
with open('/Users/romansozinov/Documents/Клиенты Mac/Аскар Европак/Рассылки/Списки/Контур Компас/01.06.22/Email 3 сегмент Производство кроме Свердл обл  2 сегмент 2022-06-01 15-43.txt', 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('	', '\n')

filedata = re.sub('\n+', '\n', filedata)


# Write the file out again
with open('/Users/romansozinov/Documents/Клиенты Mac/Аскар Европак/Рассылки/Списки/Контур Компас/01.06.22/file.txt', 'w') as file:
  file.write(filedata)
  



