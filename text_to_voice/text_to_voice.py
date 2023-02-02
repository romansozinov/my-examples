
# https://azzrael.ru/yandex-speechkit-python
# https://cloud.yandex.ru/services/speechkit


# from gtts import gTTS #Подключили библиотеку

# ru = open("/Users/romansozinov/MyProjects/GitHub my projects/my-examples/text_to_voice/draft.txt", "r").read().replace("\n", " ")

# # ru = str('Добрый день!') #Задали текст на русском языке
# # de = str('Guten tag!') #Задали текст на немецком языке (в качестве примера)
 
# tts_ru = gTTS(ru, lang='ru') #Обозначили язык нашего текста
# # tts_de = gTTS(de, lang='de') #Обозначили язык нашего текста
# with open('/Users/romansozinov/MyProjects/GitHub my projects/my-examples/text_to_voice/voice.mp3', 'wb') as f: #Создали файл в который будем писать звук из текста
#     tts_ru.write_to_fp(f) #Записываем в файл озвучку русского текста
#     # tts_de.write_to_fp(f) #Записываем в файл озвучку немецкого текста




import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Irina':
        tts.setProperty('voice', voice.id)

tts.setProperty("rate", 150)
tts.setProperty("volume", 1)

ru = open("/Users/romansozinov/MyProjects/GitHub my projects/my-examples/text_to_voice/draft.txt", "r").read().replace("\n", " ")
tts.say(ru) # tts.say('Задали текст на русском языке')
tts.runAndWait()






