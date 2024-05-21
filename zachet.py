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

scr = Tk()
scr.geometry("1920x1080")
h = Canvas(scr, width=1920, height=1080, bg=mcol)
h.pack(fill=BOTH, expand=True)
widget = None

def clear():
    global widget
    if widget:
        widget.pack_forget()
    widget = None
    h.delete('all')

'''#настройка таблицы значений
n = 5
m = 6
m_ofsett = 1  # Отступ информации от границ таблицы в яч. по У
n_ofsett = 1  # Отступ информации от границ таблицы в яч. по Х
tab_height = 100  # Высота ячейки
tab_width = 240  # Ширина ячейки

x0 = 200  # Отступ по Х
y0 = 100  # Отступ по У
x, y = 2, 1  # Начальная позиция курсора в таблице

#настройка таблицы значений 2
n2 = 6
m2 = 6
m2_ofsett = 1  # Отступ информации от границ таблицы в яч. по У
n2_ofsett = 1  # Отступ информации от границ таблицы в яч. по Х
tab2_height = 100  # Высота ячейки
tab2_width = 240  # Ширина ячейки

x02 = 200  # Отступ по Х
y02 = 100  # Отступ по У
x2, y2 = 2, 1  # Начальная позиция курсора в таблице

# Настройка таблицы погрешностей
ar_x, ar_y = 1, 1
#summ = 0
#count = 1
ar_n = 3
ar_m = 2
arn_ofsett = 1
arm_ofsett = 1
artab_width = 400  # Ширина ячейки погрешности
artab_height = 100  # Высота ячейки погрешности
ar_x0 = 370
ar_y0 = 100

ar_txt = [[' Инструмент', " Цена\n деления, мм", " Инструментальная\n погрешность, мм"],
          [" Линейка", 1, 1,5]]

txt = [["№", " Цена\n деления", " Число\n горошин", " Длина\n ряда", " Диаметр\n горошин"],
       ['1', [ar_txt[1][2]], None, None, None],
       ['2', [ar_txt[1][2]], None, None, None],
       ['3', [ar_txt[1][2]], None, None, None],
       ['4', [ar_txt[1][2]], None, None, None],
       ['5', [ar_txt[1][2]], None, None, None]]

txt2 = [[None, "Объект", 'Макс. измеренная\n величина, мм', ' Мин. измеренная\n величина, мм', ' Макс. реальная\n величина, км', ' Мин. реальная\n величина, км'],
       ['1', "Море Дождей", None, None, None, None],
       ['2', "Море Ясности", None, None, None, None],
       ['3', "Горы Аппенины", None, None, None, None],
       ['4', "Море Кризисов", None, None, None, None],
       ['5', "Кратер Платон", None, None, None, None]]

def table():
    global x, y, x0, y0
    h.delete("all")
    h.create_text(1920 / 2, ofsett / 2, text="Таблица. Часть 2", font="Arial 36", fill=txtcol)
    h.create_text(960, 960, text="Для выхода в меню нажмите Escape", font="Arial 24", fill=frcol)
    h.create_text(960, 1020, text="Для переключения на таблицу 2 нажмите F", font="Arial 24", fill=frcol)
    for i in range(m + 1):
        h.create_line((x0, y0 + i * tab_height), (x0 + n * tab_width, y0 + i * tab_height), fill=frcol, width=3)
    for j in range(n + 1):
        h.create_line((x0 + j * tab_width, y0), (x0 + j * tab_width, y0 + m * tab_height), fill=frcol, width=3)
    point[0] = h.create_line((x0 + x * tab_width + 10, y0 + y * tab_height), (x0 + x * tab_width + 10,
                             y0 + y * tab_height + 30), fill="red", width=2)  # курсор таблицы'''

# Подфункции
def title():
    h.delete("all")
    h.create_text(960, 100, anchor="c", text="Зачетная работа", font="ARIAL 42",
                  fill=frcol)
    h.create_text(960, 160, anchor="c", text="Определение погрешности косвенных измерений", font="ARIAL 46",
                  fill=frcol)
    h.create_text(960, 220, anchor="c", text="Выполнила ученица 9 класса Г", font="ARIAL 28", fill=txtcol)
    h.create_text(960, 260, anchor="c", text="Шрамова Надежда", font="ARIAL 28", fill=txtcol)
    h.create_text(960, 960, anchor="c", text="2023 - 2024 учебный год", font="ARIAL 24", fill=txtcol)
    h.create_text(960, 1020, anchor="c", text="Для перехода в меню нажмите клавишу пробела", font="ARIAL 24", fill=frcol)

def main_menu():
    global widget
    clear()

    h1 = Canvas(h, width=1900, height=1000, bg=mcol)
    h1.pack(fill=BOTH, expand=True)

    '''
    h.create_text(1920 / 2, ofsett / 2, text="Меню", fill=txtcol, font="Arial 38")
    h.create_text(960, 1020, anchor="c", text="Для перехода в раздел нажмите на\nпрямоугольник левой кнопкой мыши",
                  font="ARIAL 24", fill=frcol)
    '''
    Label(h1, text="Меню", font="Arial 38", background=mcol, foreground=txtcol).pack(pady=10)

    for (name, func) in [("Описание", description), ("Погрешности", None), ("Таблица #1", None), ("Таблица #2", None), ("Числовые прямые", None), ("Помощь", helper)]:
        Button(h1, text = name, command=func, height=6, width=20, background=mcol, foreground=txtcol).pack(pady=10)

    Label(h1, anchor="c", text="Для перехода в раздел нажмите на\nпрямоугольник левой кнопкой мыши",
                  font="ARIAL 24", background=mcol, foreground=frcol).pack(pady=10)

    widget = h1

def description():
    global pos
    pos = State.Description
    h.delete("all")
    h.create_text(1920 / 2, ofsett / 2, text="Описание", font="Arial 36", fill=txtcol)
    h.create_text(960, 960, text="Для выхода в меню нажмите Escape", font="Arial 24", fill=frcol)
    im_1 = PhotoImage(file="зачет(1).png")
    pic1 = h.create_image(960, 540, image=im_1, anchor="c")
    im_2 = PhotoImage(file="зачет(1).png")
    pic2 = h.create_image(960, 540, image=im_2, anchor="c")
    im_3 = PhotoImage(file="зачет(1).png")
    pic3 = h.create_image(960, 540, image=im_3, anchor="c")
    h.create_text(960, 75, text="Страница 1", font="Arial 24", fill=txtcol)
    h.create_text(960, 1000, text="Для переключения на страницу вперед нажмите клавишу PgDn", font="Arial 22", fill=frcol)

def helper():
    global pos
    print("Draw help")
    pos = State.Help
    clear()
    h.create_text(1920 / 2, ofsett / 2, text="Помощь", font="Arial 36", fill=txtcol)
    h.create_text(450, 300, anchor="w",
                  text="- Для того, чтобы попасть в нужный вам раздел,\n кликните на прямоугольник этого раздела в меню\n левой кнопкой мыши",
                  font="Arial 24", fill=txtcol)
    h.create_text(450, 400, anchor="w",
                  text="- Для того, чтобы листать страницы в описании веперд, нажмите клавишу Page Down,\n а назад -- клавишу Page Up",
                  font="Arial 24", fill=txtcol)
    h.create_text(450, 480, anchor="w",
                  text="- Для того, чтобы попасть в меню из любого отдела,\n нажмите клавишу Escape",
                  font="Arial 24", fill=txtcol)
    h.create_text(450, 560, anchor="w",
                  text="- Для того, чтобы попасть во вторую таблицу, нажмите клавишу F,\n а в первую -- клавишу В",
                  font="Arial 24", fill=txtcol)
    h.create_text(450, 640, anchor="w",
                  text="- Для того, чтобы автоматически заполнить таблицы,\n нажмите клавишу F3",
                  font="Arial 24", fill=txtcol)

    h.create_text(960, 960, text="Для выхода в меню нажмите Escape", font="Arial 24", fill=frcol)

def position(pos):
    if pos == State.Title:
        title()
    elif pos == State.Menu:
        main_menu()
    elif pos == State.Description:
        description()
#    elif pos == State.Table0:
#        table()
    elif pos == State.Help:
        helper()
    '''elif pos == State.Errors:
            arrogance()
    elif pos == State.Table1:
    print('table2')
        table2()
    elif pos == State.Lines:
        graphics()'''

def menu_event(e):
    pass
    #if e.type == EventType.ButtonPress and e.num == 1 and :
def main(e):
    print(f'Event: {e.keysym}')
    if e.type == EventType.ButtonPress:
        print(f'Button: {e.num}')
    global pos, height, space, ofsett, point, x, y, costyl1
    if pos == State.Menu:
        return menu_event(e)
    if e.keysym == "space":
        if pos == State.Title:
            pos = State.Menu
        position(pos)
    if e.keysym == "Escape":
        if pos != State.Menu and pos != State.Title:
            pos = State.Menu
        print(pos)
        position(pos)
    '''if pos == 3 or pos == 4 or pos == 5:
        move_input(e)'''
    if pos != 3 and pos != 4 and pos != 5:
        costyl1 = 0

scr.bind("<KeyRelease>", main)
scr.bind("<Button-1>", main)
title()
scr.mainloop()