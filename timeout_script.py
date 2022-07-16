from datetime import datetime
import time



start_time = datetime.now()

# Тут выполняются действия
time.sleep(2)

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))
print('Start time: {}'.format(start_time))
print('End time: {}'.format(end_time))

## второй вариант

start_time = datetime.now()

# Тут выполняются действия
time.sleep(5)

print(datetime.now() - start_time)


### форматы вывода времени https://pythonru.com/osnovy/modul-time-v-python