from datetime import datetime
import time
import os

start_time = datetime.now()

###
# Самый простой способ удалить все файлы в папке/удалить все файлы. https://fooobar.com/questions/10881/delete-folder-contents-in-python
files = os.listdir("myparser/json/")
for f in files:
    os.remove("myparser/json/" + f)
###
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))