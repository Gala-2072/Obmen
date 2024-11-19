import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb

from bottle import response


def exchange():
    code=entry.get().upper()
    if code:
        try:
            response=requests.get('https://github.com/Gala-2072/Obmen.git')
            response.raise_for_status()
            data=response.json()
            if code in data['rates']:
                exchange_rate=data['rates'][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate} {code} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")



window=Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")


Label(text="Введите код валюты").pack(padx=10, pady=10)

entry=Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена валюты", command=exchange).pack(padx=10, pady=10)

window.mainloop()