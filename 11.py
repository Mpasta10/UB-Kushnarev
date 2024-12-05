from tkinter import *
from tkinter import ttk, messagebox, filedialog
#Создание окна
window = Tk()
window.title('Кушнарев Алексей Валерьевич')
window.geometry('1280x720')
#Создание Вкладок
notebook = ttk.Notebook()
notebook.pack(expand = True, fill = BOTH)
frame1 = Frame(notebook)
frame2 = Frame(notebook)
frame3 = Frame(notebook)
frame1.pack(expand = True, fill = BOTH)
frame2.pack(expand = True, fill = BOTH)
frame3.pack(expand = True, fill = BOTH)
notebook.add(frame1, text = 'Калькулятор')
notebook.add(frame2, text = 'Чекбоксы')
notebook.add(frame3, text = 'Текст')

##Первая Вкладка
#Валидация
def valid(inStr, acttyp):
    if acttyp == '1':
        if not inStr in '1234567890-.':
            return False
    return True
#Организация вывода значений
lbl = Label(frame1, text = ' =  ')
lbl.grid(column=4, row=0)

def answer(ans,  col = 'black'):
    lbl.configure(text = ' = ' + f'{ans}', fg = f'{col}')

def selected():
    try:
        selection = combo.get()
        if selection == '+':
            ans = float(num1.get()) + float(num2.get())
            answer(ans)
        if selection == '-':
            ans = float(num1.get()) - float(num2.get())
            answer(ans)
        if selection == '*':
            ans = float(num1.get()) * float(num2.get())
            answer(ans)
        if selection == '/':
            ans = float(num1.get()) / float(num2.get())
            answer(ans)
    except ZeroDivisionError or ValueError:
        answer(ans = 'Операция невозможна', col = 'red')
#Организация ввода значений
num1 = Entry(frame1, width = 10, validate = 'key', validatecommand = (Entry.register(func = valid, self = frame1), '%S', '%d'))
num1.grid(column = 0, row = 0)
num1.focus()
combo = ttk.Combobox(frame1, width = 10, state = 'readonly', values = ('+', '-', '*', '/'))
combo.grid(column=1, row=0)
num2 = Entry(frame1, width = 10, validate = 'key', validatecommand = (Entry.register(func = valid, self = frame1), '%S', '%d'))
num2.grid(column = 2, row = 0)
butt1 = Button(frame1, width = 10, text = 'Посчитать', command = selected)
butt1.grid(column = 1, row = 1)
##Вторая вкладка
c1, c2, c3 = IntVar(), IntVar(), IntVar()
k1, k2, k3 = False, False, False
#Чекбоксы
def sel_check():
    global k1, k2, k3
    if c1.get() == 1:
        k1 = True
    else:
        k1 = False

    if c2.get() == 1:
        k2 = True
    else:
        k2 = False

    if c3.get() == 1:
        k3 = True
    else:
        k3 = False
    
check1 = Checkbutton(frame2, width = 10, text = "Первый", var = c1, command = sel_check)
check1.grid(column = 0, row = 0)
check2 = Checkbutton(frame2, width = 10, text = "Второй", var = c2, command = sel_check)
check2.grid(column = 1, row = 0)
check3 = Checkbutton(frame2, width = 10, text = "Третий", var = c3, command = sel_check)
check3.grid(column = 2, row = 0)
#Кнопка
def clicked():
    if k1 == True:
        messagebox.showinfo('Я знаю что...', 'Вы выбрали Первый вариант')
    if k2 == True:
        messagebox.showinfo('Я знаю что...', 'Вы выбрали Второй вариант')
    if k3 == True:
        messagebox.showinfo('Я знаю что...', 'Вы выбрали Третий вариант')
butt2 = Button(frame2, width = 10, text = 'Кнопка', command = clicked)
butt2.grid(column = 1, row = 1)

##Третья вкладка
#Меню
def menuclick():
    file = filedialog.askopenfile(filetypes = (('Text files', '*.txt'), ('all files', '*.*')))
    for item in file.readlines():
        text.insert(END, item)
menu = Menu(window)
menu.add_command(label='Файл', command = menuclick)
window.config(menu = menu)
#Текст
text = Text(frame3, wrap = WORD)
text.pack(expand = True, fill = BOTH)
window.mainloop()