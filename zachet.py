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


class RowBase:
    def __init__(self, widget, *values):
        self.check_num = (scr.register(self.is_num), "%P", "%V")
        self.error = Label(widget, text='', font="Arial 24", foreground=frcol, background=mcol)
        self.size = Entry(widget, foreground=txtcol, background=mcol, validate="all", validatecommand=self.check_num)
        self.length = Entry(widget, foreground=txtcol, background=mcol, validate="all", validatecommand=self.check_num)
        self.values = values

    def reset(self):
        self.size.delete(0, END)
        self.size.insert(0, f"{self.values[0]}")
        self.length.delete(0, END)
        self.length.insert(0, f"{self.values[1]}")
        self.calc()

    def is_num(self, value, op):
        try:
            if value != value.strip():
                return False
            v = float(value)
            if v >= self.maxval or len(value) >= 7:
                return False
            if op == 'focusout':
                self.calc()
            return True
        except:
            return False

    def set_error(self, error):
        print(f"Error:{error}, {self.__class__.__name__}")
        self.error.config(text=f"{error}")


class Row0(RowBase):
    def __init__(self, widget, *args):
        super().__init__(widget, *args)
        self.result = Label(widget, text='', font="Arial 24", foreground=frcol, background=mcol)
        self.maxval = 300


    def w_list(self):
        return [self.error, self.size, self.length, self.result]
    def calc(self):
        try:
            print(f"{self.length.get()}")
            d = float(self.length.get()) / float(self.size.get())
            ar = float(self.error.cget('text')) / float(self.size.get())
            self.result.config(text=f"{d:.2f} +- {ar:.2f}")
        except:
            self.result.config(text='')

    def set_error(self, error):
        self.error.config(text=f"{error}")
        self.calc()


class Row1(RowBase):
    def __init__(self, widget, name, *args):
        super().__init__(widget, *args)
        self.maxmoon = Label(widget, text='', font="Arial 24", foreground=frcol, background=mcol)
        self.minmoon = Label(widget, text='', font="Arial 24", foreground=frcol, background=mcol)
        self.maxval = 1000
        self.obj = Label(widget, text=name, font="Arial 24", foreground=frcol, background=mcol)

    def w_list(self):
        return [self.obj, self.size, self.length, self.maxmoon, self.minmoon]


    def calc(self):
        try:
            ma = float(self.size.get())
            mi = float(self.length.get())
            ar = float(self.error.cget('text')) * 19
            print(mi, ma, ar)
            self.maxmoon.config(text=f"{ma * 19:.2f} +- {ar:.2f}")
            self.minmoon.config(text=f"{mi * 19:.2f} +- {ar:.2f}")
        except:
            import traceback
            traceback.print_exc()
            self.maxmoon.config(text='')
            self.minmoon.config(text='')


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
    for (name, func) in [("Описание", description.draw), ("Погрешности", arrogance.draw), ("Таблица №1", table.draw), ("Таблица №2", table1.draw), ("Числовая прямая", graphics), ("Помощь", helper)]:
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
        h1.create_image(960, 440, image=self.images[self.idx], anchor="c")
        Label(h1, text="Для переключения на страницу назад нажмите клавишу PgUp", font="Arial 22", foreground=frcol,
              background=mcol).pack(pady=5, side=BOTTOM)
        Label(h1, text="Для переключения на страницу вперед нажмите клавишу PgDn", font="Arial 22", foreground=frcol,
              background=mcol).pack(pady=10, side=BOTTOM)
        display(h1)


description = Description()


class Errors:
    def __init__(self):
        self.table = [["Цена\n деления, мм", "Инструментальная\n погрешность, мм"], [1, 1.5]]
        self.check_float = scr.register(self.is_float)
        self.prepare()


    def is_float(self, value, op):
        try:
            if value != value.strip():
                return False
            v = float(value)
            if v >= 3 or len(value) >= 5:
                return False
            if op == 'focusout' or True:
                table.set_error(v)
                table1.set_error(v)
            return True
        except:
            import traceback
            traceback.print_exc()
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
                e = Entry(h2, foreground=txtcol, background=mcol, font="Arial 24", validate="all", validatecommand=(self.check_float, "%P", "%V"))
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
        self.defaults = [[10, 25],
                         [15, 32],
                         [20, 43],
                         [25, 55],
                         [30, 69]]
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
        Label(h1, text="Для автоматического заполнения таблицы нажмите клавишу F3", font="Arial 24",
              foreground=frcol, background=mcol).pack(pady=10, side=BOTTOM)
        h2 = Canvas(h1, bg=mcol)
        for x, cell in enumerate(self.header):
            Label(h2, text=cell, font="Arial 24", foreground=frcol, background=mcol).grid(row=0, column=x, pady=10, padx=10)
        for y, vals in enumerate(self.defaults):
            row = Row0(h2, *vals)
            for x, wid in enumerate(row.w_list()):
                wid.grid(row=y+1, column=x, pady=10, padx=10)
            self.table.append(row)
        self.set_error(1)
        h2.pack()

    def draw(self):
        global pos
        pos = State.Table0
        display(self.widget)
        
    def reset(self):
        for row in self.table:
            row.reset()

              
class Table1:
    def __init__(self):
        self.table = []
        self.header = ["Объект", 'Макс. измеренная\nвеличина, мм', 'Мин. измеренная\nвеличина, мм', 'Макс. реальная\nвеличина, км', 'Мин. реальная\nвеличина, км']
        self.obj = [["Море Дождей", 56, 35],
                    ["Море Ясности", 34, 25],
                    ["Горы Аппенины", 26, 8.5],
                    ["Море Кризисов", 24, 15.5],
                    ["Кратер Платон", 6.5, 3.5]]
        self.prepare()

    def reset(self):
        for row in self.table:
            row.reset()

    def prepare(self):
        self.widget = h1 = Canvas(h, bg=mcol)
        Label(h1, text="Таблица №2", font="Arial 36", foreground=txtcol, background=mcol).pack(pady=10)
        Label(h1, text="Для выхода в меню нажмите Escape", font="Arial 24", foreground=frcol, background=mcol).pack(
            pady=10, side=BOTTOM)
        Label(h1, text="Для переключения между ячейками таблицы нажмите клавишу Tab или Shift + Tab", font="Arial 24",
              foreground=frcol, background=mcol).pack(pady=10, side=BOTTOM)
        Label(h1, text="Для автоматического заполнения таблицы нажмите клавишу F3", font="Arial 24",
              foreground=frcol, background=mcol).pack(pady=10, side=BOTTOM)
        h2 = Canvas(h1, bg=mcol)
        for x, cell in enumerate(self.header):
            Label(h2, text=cell, font="Arial 24", foreground=frcol, background=mcol).grid(row=0, column=x, pady=10, padx=10)
        for y, name in enumerate(self.obj):
            row = Row1(h2, *name)
            for x, wid in enumerate(row.w_list()):
                wid.grid(row=y + 1, column=x, pady=10, padx=10)
            self.table.append(row)
        h2.pack()

    def set_error(self, error):
        for row in self.table:
            row.set_error(error)

    def draw(self):
        global pos
        pos = State.Table1
        display(self.widget)


table = Table()
table1 = Table1()
arrogance = Errors()

line_image = PhotoImage(file='line.png')

def graphics():
    h1 = Canvas(h, bg=mcol)
    global pos
    pos = State.Lines
    Label(h1, text="Числовая прямая", font="Arial 36", foreground=txtcol, background=mcol).pack(pady=10)
    Label(h1, text="Для выхода в меню нажмите Escape", font="Arial 24", foreground=frcol, background=mcol).pack(side=BOTTOM, pady=10)
    h1.create_image(1920/2, 1080/2, image=line_image, anchor='c')
    display(h1)


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
    Label(h1, anchor="w", text="- Для автоматического заполнения таблицы нажмите клавишу F3", font="Arial 24",
          foreground=txtcol, background=mcol).pack()
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
    elif pos == State.Table0:
        table.draw()
    elif pos == State.Table1:
        table1.draw()
    elif pos == State.Lines:
        graphics()


def main(e):
    global pos
    if pos == State.Title:
        if e.keysym == "space":
            pos = State.Menu
        position(pos)


def on_escape(e):
    global pos
    if pos != State.Menu and pos != State.Title:
        pos = State.Menu
        main_menu()


def on_f3(e):
    global pos
    print('auto', pos)
    if pos == State.Table0:
        print('table0 auto')
        table.reset()
    elif pos == State.Table1:
        table1.reset()


scr.bind("<Prior>", lambda e: description.shift(-1))
scr.bind("<Next>", lambda e: description.shift(1))

scr.bind("<KeyRelease>", main)
scr.bind("<Escape>", on_escape)
scr.bind("<F3>", on_f3)

scr.bind("<Button-1>", main)
title()
scr.mainloop()
