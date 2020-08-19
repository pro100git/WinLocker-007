#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from tkinter import Tk, Entry, Label
import psutil
import keyboard


Taskmgr = 'taskmgr.exe'
cmd = 'cmd.exe'
powershell = 'powershell.exe'
powershell_ise = 'powershell_ise.exe'
regedit = 'regedit.exe'
mmc = 'mmc.exe'
msconfig = 'msconfig.exe'
ProcessHacker = 'ProcessHacker.exe'
iexplore = 'iexplore.exe'
game = 'game.exe'


with open(r'C:\pas.txt', 'r') as pas: # В файл pas.txt пишем свой пароль
    data = pas.read()

def callback(event):
    global k,entry
    if entry.get() == data:
        k = True

def on_closing():
    root.attributes("-fullscreen", True) # на весь экран
    root.attributes('-topmost', 1) # поверх всех окон
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()
    root.bind('<Alt-KeyPress-s>', callback) # Сочетание клавиш, вместо Enter (можно изменить)

root = Tk() # Создание окна
root.title("007") # Заголовочное название
root.attributes("-fullscreen",True) # Расширение под экран
root.configure(background="#1c1c1c")
entry = Entry(root,show='➤',font='Arial 15', fg="red")# Поле ввода
entry.place(width=350,height=30,x=500,y=400) # Координаты и размеры
label0 = Label(root,text="\n\n\n\n\n\n\n\n\n\n__¶¶¶________________________________________\n \
__¶¶¶¶¶______________________________________\n \
__¶¶¶¶¶¶_____________________________________\n \
__¶¶¶¶¶¶_____________________________________\n \
__¶¶¶¶¶¶_____________________________________\n \
__¶¶¶¶¶¶_____________________________________\n \
__¶¶¶¶¶¶_____________________________________\n \
__¶¶¶¶¶¶_____________________________________\n \
__¶¶¶¶¶¶_____________________________________\n \
__¶¶¶¶¶¶_____________________________________\n \
__¶¶¶¶¶¶_____________________________________\n \
__¶¶¶¶¶¶¶¶___________________________________\n \
__¶¶¶¶¶¶¶¶__¶________________________________\n \
__¶¶¶¶¶¶¶¶__¶¶_______________________________\n \
__¶¶¶¶¶¶¶¶__¶¶¶______________________________\n \
__¶¶¶¶¶¶¶¶__¶¶¶______________________________\n \
__¶¶¶¶¶¶¶¶__¶¶¶______________________________\n \
__¶¶¶¶¶¶¶¶__¶¶¶¶¶____________________________\n \
__¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶__________________________\n \
__¶¶¶¶¶¶¶¶__¶¶¶__¶¶¶¶________________________\n \
___¶¶¶¶¶¶¶__¶¶¶____¶¶¶¶______________________\n \
________¶¶__¶¶¶______¶¶¶¶____________________\n \
__¶¶¶¶______¶¶¶¶_______¶¶¶___________________\n \
__¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶___¶¶___________________\n \
__¶¶¶¶¶¶¶¶¶¶____¶¶¶¶____¶¶___________________\n \
__¶¶¶¶¶¶¶¶¶¶¶¶__________¶¶___________________\n \
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶___________________\n \
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶___________________\n \
__¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶____¶¶___________________\n \
__¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶___¶___________________\n \
__¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶_____________________\n \
__¶¶¶¶¶________¶¶¶¶¶¶¶¶¶¶____________________\n \
__¶¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶__________________\n \
__¶¶¶¶¶___________¶¶¶¶¶¶¶¶¶¶¶________________\n \
__¶¶¶¶¶_____________¶¶¶¶¶¶¶¶¶¶¶______________\n \
__¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶¶¶¶____________\n \
__¶¶¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶¶¶¶__________\n \
___¶¶¶¶¶¶¶¶¶¶____________¶¶¶¶¶¶¶¶¶¶¶¶________\n \
______¶¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶¶¶¶¶¶_____\n \
_________¶¶¶¶________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶__\n \
____________¶__________________¶¶¶¶¶¶¶¶¶¶¶¶__\n \
______¶¶¶¶¶__¶___________________¶¶¶¶¶¶¶¶¶¶__\n \
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶__\n \
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶¶¶¶__\n \
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶__\n \
_¶¶¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______________\n \
__¶¶¶¶___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________\n \
__¶¶¶¶¶_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________\n \
__¶¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶________\n \
___¶¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶¶¶_______\n \
____¶¶¶¶¶¶¶¶¶________________¶¶¶¶¶¶¶¶¶¶¶_____\n \
______¶¶¶¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶____\n \
_______¶¶¶¶¶¶¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶¶___\n \
_________¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶¶¶¶¶¶¶__\n \
___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________¶¶¶¶¶¶__\n \
_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶¶¶¶_\n \
_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶¶_\n \
___________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__\n \
____¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___\n \
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶____\n \
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶________\n \
_¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________\n \
_¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________\n \
__¶¶¶¶____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________\n \
__¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________\n \
___¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶¶¶________\n \
____¶¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶¶¶______\n \
_____¶¶¶¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶_____\n \
______¶¶¶¶¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶____\n \
________¶¶¶¶¶¶¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶___\n \
__________¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶¶¶¶¶¶__\n \
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶¶¶¶__\n \
______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶__\n \
________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶__\n \
____________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__\n \
_______________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___\n \
____________________________¶¶¶¶¶¶¶¶¶¶¶______",font='Arial 5', fg="red", background="#1c1c1c") # Надпись 1
label0.grid(row=0,column=0) # Координаты надписи 1
label1 = Label(root,text="Write the Password and Press Enter",font='Broadway 20', fg="red", background="#1c1c1c") # Надпись 2
label1.place(x=420,y=330) # Координаты надписи 2

def block():
    try:
        keyboard.block_key('Del')
        keyboard.block_key('Esc')
        keyboard.block_key('Windows')
        keyboard.block_key('Tab')
    except:
        return

    try:
        for proc in psutil.process_iter():
            if proc.name() == game:
                proc.kill()

        for proc in psutil.process_iter():
            if proc.name() == iexplore:
                proc.kill()

        for proc in psutil.process_iter():
            if proc.name() == ProcessHacker:
                proc.kill()

        for proc in psutil.process_iter():
            if proc.name() == msconfig:
                proc.kill()

        for proc in psutil.process_iter():
            if proc.name() == mmc:
                proc.kill()

        for proc in psutil.process_iter():
            if proc.name() == regedit:
                proc.kill()

        for proc in psutil.process_iter():
            if proc.name() == Taskmgr:
                proc.kill()

        for proc in psutil.process_iter():
            if proc.name() == cmd:
                proc.kill()

        for proc in psutil.process_iter():
            if proc.name() == powershell:
                proc.kill()

        for proc in psutil.process_iter():
            if proc.name() == powershell_ise:
                proc.kill()
    except:
        return


k = False
while k != True:
    block()
    on_closing()
