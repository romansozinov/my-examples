# -*- coding: UTF-8 -*-
from os import link
import json
import csv
import os
from os import path, listdir
from os.path import getsize, join
from time import ctime
import random
import re
import time
import requests
from random import choice
from bs4 import BeautifulSoup

# proxy https://youtu.be/4Ijgdtk65mM
import pickle

from itertools import cycle
from requests_html import HTMLSession
from datetime import datetime


# считаем и выводим данные о файлах в папке
folder = 'folder-file-size/folder/'
for name in listdir(folder):
    full_name = path.join(folder, name)
    
    if path.isfile(full_name):
        name_, _ext = path.splitext(name)
        time_info = [ctime(fn(full_name)) for fn in (path.getatime, path.getmtime, path.getctime)]
        sizefile = os.stat(full_name)
        file = {
            # 'каталог': folder,
            'файл': full_name,
            'файл_имя': name_,
            'файл_расширение': _ext,
            'время последнего доступа': time_info[0],
            'время последнего изменения': time_info[1],
            'время создания': time_info[2],
            'размер файла': sizefile.st_size,
        }
    print('\n'.join('{:<30} : {}'.format(*f) for f in sorted(file.items())), '\n')
# END считаем и выводим данные о файлах в папке