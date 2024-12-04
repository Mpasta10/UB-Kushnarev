from tkinter import *
import requests
from pprint import pprint
import json
window = Tk()
window.geometry('900x600')
window.title('Json enjoyer')
def clicked():
    check = ('id', 'company', 'created_at', 'email', 'name', 'url')
    username = ent.get()
    url = f'https://api.github.com/users/{username}'
    user_data = requests.get(url).json()
    with open('data_file.json', 'w') as write_file:
        user_data2 = {}
        for key, item in user_data.items():
            if key in check:
                user_data2[f'{key}'] = item
        json.dump(user_data2, write_file, indent = 4)
lbl = Label(window, text = 'Введите имя')
lbl.grid(column = 0, row = 0)
ent = Entry(window, width =20, text = 'Введите имя')
ent.grid(column = 1, row = 0)  
butt = Button(window, width = 10, text = 'Получить', command = clicked)
butt.grid(column = 2, row = 0)
window.mainloop()