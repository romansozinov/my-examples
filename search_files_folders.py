# Импортировать модуль shutil
import shutil
import os
# Импортировать модуль пути из ОС
from os import path, walk
from datetime import datetime



start_time = datetime.now()

# spisok_fotos = [
#     '12-2.jpg',
#     'S7 (Орех+ Монолит 84) 3_4 сзади.png',
#     'S7 (Орех+ Монолит 97) сбоку.png',
#     'S7 (Орех+ Монолит 84) 3_4 сзади.png',
#     '333.png',
#     '222.png',
#     '111.png'
# ]

spisok_fotos = [
    'igr_1-03e30515153ea88038ecdf599c9f2bf6.jpg','igrushka_2-152204b2f439035729a1c59ef5d51c23.jpg','igr_3-9fc2bde535d40606fe471d3b265afc4c.jpg','igr_5-0f610fd31914a2af6a799ca05ec0549d.jpg','igr_6-f961b8ae6186e166fa0fad70f9aa3799.jpg','igrushka_7-7a8246bb31364b836283ced18da0b09c.jpg','igr_8-305bb863148f52cd2d4b86c5045a24b6.jpg','13hq.jpeg','igr_22-7e2ae1e80c5541321177579daf606d24.jpg','igr_21-01ac68f5d7b9b0b8f365e4c4b7dce7c7.jpg','igrushka_9-f34ff685f15389ea14695715c98e8a78.jpg','igr_10-8c98224811fd66cc1d8a8484f84d78d8.jpg','4dc804ea7c99aa6b30f0c4d5b65c43d9.jpg','igrushka_11-b9850cf5ab3184b20faefde2a5c1af56.jpg','igr_12-b3bd47e9b68fca8fc8aa2b1bb8ae0742.jpg','igr_13-26d1b77153a1b3ee92f90572ff70a816.jpg','igr_Zayac2-33bbd61024375f8c371119b5f260084c.jpg','igr_15-fa27f322ed24131810c34a6fd248b554.jpg','igr_mouse-7fa94b4a355eaf79fa7a6523f78a6a08.jpg','igr_17-56be1112571faacabdda4c10a65f76b9.jpg','igrushka_18-91292d6fcef7fccfb7db70df62ac6638.jpg','igrushka_16-432ff62a58780f58f1198fe487ae9d2f.jpg','igrushka_4-8ef29fb0aa01e1501a70c6f4b19b4036.jpg','igr_23-9d3b4bc4574386c92b67077bb8a752ff.jpg','igr_30-e39e6307ea019a44bc1094ca366b6a5f.jpg','product-389595-1.jpg|product-389595-2.jpg','igr_Liza1-06359fe51cbce63c256b32af20222152.jpg','igr_Anya1-59530bcdd2404b335ea2719abf825b61.jpg','igr_29-811784fa0a44e3f0dd5a2764f24cba9c.jpg','zaya_fon-bae41abca32229c8c80e77263b490461.jpg','Krokodil_1-064be9b4b8eecd0069cc52e9574dd947.jpg','igr-bd35c079a680a90af34d1e353f7b66b7.jpg'  
]

# spisok_urls = zip(spisok_urls) 

# source_dir = "/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir"
# target_dir = "/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/target_dir"

# Задайте имя файла с путем
source_dir = "/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir/"
# source_dir = "/Users/romansozinov/Downloads/All_fotos/"

spisok = []

for adress, dirs, files in os.walk(source_dir):
    for file in files:
        full_path = os.path.join(adress, file)
        spisok.append(full_path)

        for foto in spisok_fotos:  # [0:1] - скачать только одну ссылку  

            # Проверьте, существует ли файл

            if foto in full_path:

                # Задайте путь к каталогу, в который будет перемещен файл

                target_dir = "/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/target_dir"
                # target_dir = "/Users/romansozinov/Downloads/All_fotos_result"

                # Переместите файл в новое место

                new_location = shutil.copy(f"/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir/{foto}", target_dir) # move, вместо copy - перенос файлов
                # new_location = shutil.copy(f"/Users/romansozinov/Downloads/All_fotos_result/{foto}", target_dir) # move, вместо copy - перенос файлов

                # Распечатать новое расположение файла

                # print("% s перемещен в указанное место,% s" % (f"/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir/{foto}" , new_location))
                print("Готово!")

            else :

                # Распечатать сообщение, если файл не существует

                print ("Файл не существует.")           



print("\n".join(spisok))





 














# folderpath = '/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir/'

# # for dirname, subdirs, files in os.walk(folderpath):
#     # for fname in files:
#         # full_path = os.path.join(dirname, fname)
#         # print(dirname)
#         # print(fname)
#         # print(full_path)


#         # for foto in folderpath:  # [0:1] - скачать только одну ссылку 


# for foto in spisok_fotos:

#     for dirname, subdirs, files in os.walk(folderpath):
#         # Проверьте, существует ли файл

#         if path.exists(foto):

#             # Задайте путь к каталогу, в который будет перемещен файл

#             target_dir = "/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/target_dir"

#             # Переместите файл в новое место

#             new_location = shutil.copy(f"/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir/{foto}", target_dir) # move, вместо copy - перенос файлов

#             # Распечатать новое расположение файла

#             # print("% s перемещен в указанное место,% s" % (f"/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir/{fname}" , new_location))

#         else :

#             # Распечатать сообщение, если файл не существует

#             print ("Файл не существует.")   



















    # for foto in folderpath:  # [0:1] - скачать только одну ссылку  

    #     # Проверьте, существует ли файл

    #     if path.exists(f"/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir/{foto}"):

    #         # Задайте путь к каталогу, в который будет перемещен файл

    #         target_dir = "/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/target_dir"

    #         # Переместите файл в новое место

    #         new_location = shutil.copy(f"/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir/{foto}", target_dir) # move, вместо copy - перенос файлов

    #         # Распечатать новое расположение файла

    #         print("% s перемещен в указанное место,% s" % (f"/Users/romansozinov/MyProjects/Web-Parser-Python/examples/search_fotos/source_dir/{foto}" , new_location))

    #     else :

    #         # Распечатать сообщение, если файл не существует

    #         print ("Файл не существует.")    
























# part = "111"
# files = [file for file in os.listdir(source_dir)
#             if os.path.isfile(file) and part in file]
# for file in files:
#     shutil.copy2(os.path.join(source_dir, file), target_dir)               


end_time = datetime.now()
print('Start time: {}'.format(start_time))
print('End time: {}'.format(end_time))
print('Duration: {}'.format(end_time - start_time))





