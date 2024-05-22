mcol = "#0E294B"  # Цвет фона
frcol = "#ffd870"  # Цвет текста рамочек, прямоугольников итд.
txtcol = "#ffffcc"  # Цвет текста

space = 50  # Отступ между кнопками
width = 400
height = 100  # Высота и ширина кнопки
ofsett = 75  # Отступ сверху

from tkinter import *
from math import *
from enum import Enum

class State(Enum):
    Title = 0
    Menu = 1
    Description = 2
    Errors = 3
    Table0 = 4
    Table1 = 5
    Lines = 6
    Help = 7

pos = State.Title
class Row0:
    def __init__(self, widget):
        self.check_num = (scr.register(self.is_num), "%P", "%V")
        self.error = Label(widget, text='', font="Arial 24", foreground=frcol, background=mcol)
        self.size = Entry(widget, foreground=txtcol, background=mcol, validate="all", validatecommand=self.check_num)
        self.length = Entry(widget, foreground=txtcol, background=mcol, validate="all", validatecommand=self.check_num)
        self.result = Label(widget, text='', font="Arial 24", foreground=frcol, background=mcol)
        self.maxval = 300

    def is_num(self, value, op):
        try:
            if value != value.strip():
                return False
            v = float(value)
            if v >= self.maxval or len(value) >= 5:
                return False
            if op == 'focusout':
                self.calc()
            return True
        except:
            return False

    def w_list(self):
        return [self.error, self.size, self.length, self.result]

    def calc(self):
        try:
            print(f"{self.length.get()}")
            d = float(self.length.get()) / float(self.size.get())
            ar = float(self.error.cget('text')) * float(self.size.get())
            self.result.config(text=f"{d:.2f} +- {ar}")
        except:
            self.result.config(text='')

    def set_error(self, error):
        self.error.config(text=f"{error}")
        self.calc()

scr = Tk()
scr.geometry("192x1080")
h = Canvas(scr, width=1920, height=1080, bg=mcol)
h.pack(fill=BOTH, expand=True)
widget = None

def display(new):
    h.delete('all')
    global widget
    if widget:
        widget.pack_forget()
    widget = new
    if new is not None:
        new.pack(fill=BOTH, expand=True)

'''

#настройка таблицы значений 2
n2 = 6
m2 = 6


txt2 = [[None, "Объект", 'Макс. измеренная\n величина, мм', ' Мин. измеренная\n величина, мм', ' Макс. реальная\n величина, км', ' Мин. реальная\n величина, км'],
       ['1', "Море Дождей", None, None, None, None],
       ['2', "Море Ясности", None, None, None, None],
       ['3', "Горы Аппенины", None, None, None, None],
       ['4', "Море Кризисов", None, None, None, None],
       ['5', "Кратер Платон", None, None, None, None]]
'''

# Подфункции
def title():
    h1 = Canvas(h, width=1900, height=1000, bg=mcol)
    Label(h1, anchor="c", text="Зачетная работа", font="ARIAL 42", foreground=frcol, background=mcol).pack()
    Label(h1, anchor="c", text="Определение погрешности косвенных измерений", font="ARIAL 46", foreground=frcol, background=mcol).pack(pady=20)
    Label(h1, anchor="c", text="Выполнила ученица 9 класса Г", font="ARIAL 28", foreground=txtcol, background=mcol).pack(pady=10)
    Label(h1, anchor="c", text="Шрамова Надежда", font="ARIAL 28", foreground=txtcol, background=mcol).pack()
    Label(h1, anchor="c", text="Для перехода в меню нажмите клавишу пробела", font="ARIAL 24", foreground=frcol, background=mcol).pack(pady=10, side=BOTTOM)
    Label(h1, anchor="c", text="2023 - 2024 учебный год", font="ARIAL 24", foreground=txtcol, background=mcol).pack(side=BOTTOM)
    display(h1)

def main_menu():
    h1 = Canvas(h, bg=mcol)
    Label(h1, text="Меню", font="Arial 38", background=mcol, foreground=txtcol).pack(pady=10)
    for (name, func) in [("Описание", description.draw), ("Погрешности", arrogance.draw), ("Таблица №1", table.draw), ("Таблица №2", None), ("Числовые прямые", None), ("Помощь", helper)]:
        Button(h1, text=name, command=func, height=6, width=20, background=mcol, foreground=txtcol).pack(pady=10)
    Label(h1, anchor="c", text="Для перехода в раздел нажмите на\nпрямоугольник левой кнопкой мыши",
                  font="ARIAL 24", background=mcol, foreground=frcol).pack(pady=10, side=BOTTOM)
    display(h1)

class Description:
    def __init__(self):
        self.images = []
        self.idx = 0
        img_ns = ["im1.png", "im2.png", "moon.png"]
        for name in img_ns:
            self.images.append(PhotoImage(file=name))

    def shift(self, n):
        if pos != State.Description:
            return
        self.idx += n
        if self.idx < 0:
            self.idx = 0
        elif self.idx >= len(self.images):
            self.idx = len(self.images) - 1
        self.draw()
    def draw(self):
        print("draw")
        h1 = Canvas(h, bg=mcol)
        global pos
        pos = State.Description
        Label(h1, text="Описание", font="Arial 36", foreground=txtcol, background=mcol).pack()
        Label(h1, text="Для выхода в меню нажмите Escape", font="Arial 24", foreground=frcol, background=mcol).pack(
            side=BOTTOM)
        h1.create_image(960, 540, image=self.images[self.idx], anchor="c")
        Label(h1, text="Для переключения на страницу назад нажмите клавишу PgUp", font="Arial 22", foreground=frcol,
              background=mcol).pack(pady=5, side=BOTTOM)
        Label(h1, text="Для переключения на страницу вперед нажмите клавишу PgDn", font="Arial 22", foreground=frcol,
              background=mcol).pack(pady=10, side=BOTTOM)
        display(h1)
description = Description()


class Errors:
    def __init__(self):
        self.table = [["Цена\n деления, мм", "Инструментальная\n погрешность, мм"], [1, 1.5]]
        self.check_float = (scr.register(self.is_float), "%P")
        self.prepare()


    def is_float(self, value):
        try:
            v = float(value)
            if v >= 1.9 or len(value) > 5:
                return False
            table.set_error(v)
            return True
        except:
            return False

    def prepare(self):
        self.widget = h1 = Canvas(h, bg=mcol)
        Label(h1, text="Погрешности", font="Arial 36", foreground=txtcol, background=mcol).pack(pady=10)
        Label(h1, text="Для выхода в меню нажмите Escape", font="Arial 24", foreground=frcol, background=mcol).pack(pady=10, side=BOTTOM)
        h2 = Canvas(h1, bg=mcol)
        for y, cell in enumerate(self.table[0]):
            Label(h2, text=cell, foreground=txtcol, background=mcol, font="Arial 24").grid(row=0, column=y, pady=10)
        for y, row in enumerate(self.table[1:]):
            for x, cell in enumerate(row):
                print(x, y, cell)
                e = Entry(h2, foreground=txtcol, background=mcol, font="Arial 24", validate="key", validatecommand=self.check_float)
                e.insert(0, str(cell))
                e.grid(row=y + 1 , column=x)
        h2.pack()
    def draw(self):
        global pos
        pos = State.Errors
        display(self.widget)

class Table:
    def __init__(self):
        self.table = []
        self.header = ["Цена\nделения, мм", "Число\nгорошин, шт", "Длина\nряда, мм", "Диаметр\nгорошин, мм"]
        self.prepare()

    def set_error(self, error):
        for row in self.table:
            row.set_error(error)


    def prepare(self):
        self.widget = h1 = Canvas(h, bg=mcol)
        Label(h1, text="Таблица №1", font="Arial 36", foreground=txtcol, background=mcol).pack(pady=10)
        Label(h1, text="Для выхода в меню нажмите Escape", font="Arial 24", foreground=frcol, background=mcol).pack(pady=10, side=BOTTOM)
        Label(h1, text="Для переключения между ячейками таблицы нажмите клавишу Tab или Shift + Tab", font="Arial 24", foreground=frcol, background=mcol).pack(
            pady=10, side=BOTTOM)
        h2 = Canvas(h1, bg=mcol)
        for x, cell in enumerate(self.header):
            Label(h2, text=cell, font="Arial 24", foreground=frcol, background=mcol).grid(row=0, column=x, pady=10, padx=10)
        for y in range(5):
            row = Row0(h2)
            for x, wid in enumerate(row.w_list()):
                wid.grid(row=y+1, column=x, pady=10, padx=10)
            self.table.append(row)
        self.set_error(1)
        h2.pack()

    def draw(self):
        global pos
        pos = State.Errors

        display(self.widget)
table = Table()
arrogance = Errors()

def helper():
    h1 = Canvas(h, bg=mcol)
    global pos
    print("Draw help")
    pos = State.Help
    Label(h1, text="Помощь", font="Arial 36", foreground=txtcol, background=mcol).pack()
    Label(h1, anchor="w", text="- Для того, чтобы попасть в нужный вам раздел,\n кликните на прямоугольник этого раздела в меню\n левой кнопкой мыши",
                  font="Arial 24", foreground=txtcol, background=mcol).pack(pady=10)
    Label(h1, anchor="w", text="- Для того, чтобы листать страницы в описании вперед, нажмите клавишу Page Down,\n а назад -- клавишу Page Up",
                  font="Arial 24", foreground=txtcol, background=mcol).pack(pady=10)
    Label(h1, anchor="w", text="- Для того, чтобы попасть в меню из любого отдела,\n нажмите клавишу Escape", font="Arial 24",
          foreground=txtcol, background=mcol).pack(pady=10)
    Label(h1, anchor="w", text="- Для переключения между ячейками таблицы нажмите клавишу Tab или Shift + Tab", font="Arial 24",
          foreground=txtcol, background=mcol).pack(pady=10)
    #Label(h1, anchor="w", text="- Для того, чтобы автоматически заполнить таблицы,\n нажмите клавишу F3", font="Arial 24",
    #      foreground=txtcol, background=mcol).pack()
    Label(h1, text="Для выхода в меню нажмите Escape", font="Arial 24", foreground=frcol, background=mcol).pack(side=BOTTOM)
    display(h1)

def position(pos):
    if pos == State.Title:
        title()
    elif pos == State.Menu:
        main_menu()
    elif pos == State.Description:
        description.draw()
    elif pos == State.Help:
        helper()
    elif pos == State.Errors:
        arrogance.draw()
    '''
    elif pos == State.Table0:
        table()
    elif pos == State.Table1:
    print('table2')
        table2()
    elif pos == State.Lines:
        graphics()'''

def menu_event(e):
    pass
    #if e.type == EventType.ButtonPress and e.num == 1 and :
def main(e):
    if e.type == EventType.ButtonPress:
        print(f'Button: {e.num}')
    global pos
    if pos == State.Menu:
        return menu_event(e)
    if pos == State.Title:
        if e.keysym == "space":
            pos = State.Menu
        position(pos)
    '''if pos == 3 or pos == 4 or pos == 5:
        move_input(e)'''
    if pos != 3 and pos != 4 and pos != 5:
        costyl1 = 0

def on_escape(e):
    global pos
    print(f"Escape: {pos}")
    if pos != State.Menu and pos != State.Title:
        pos = State.Menu
        main_menu()

scr.bind("<Prior>", lambda e: description.shift(-1))
scr.bind("<Next>", lambda e: description.shift(1))

scr.bind("<KeyRelease>", main)
scr.bind("<Escape>", on_escape)

scr.bind("<Button-1>", main)
title()
scr.mainloop()