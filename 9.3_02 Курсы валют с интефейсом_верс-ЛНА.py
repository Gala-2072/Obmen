from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_currency_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def exchange():
    target_code= target_combobox.get()
    base_code_1 = base_combobox.get()
    base_code_2= base_combobox.get()

    if target_code and base_code_1 and base_code_2:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code_1}')
            response.raise_for_status()

            data = response.json()

            if target_code  in data['rates']:
 exchange_rate = data['rates'][target_code]
 base_1 = currencies[base_code_1]
 base_2 = currencies[base_code_2]
 target =currencies[target_code]
 mb.showinfo("Курс обмена", f"Курс {exchange_rate:.2f} {target} за 1 {base_1}. Курс {exchange_rate:.2f} {target} за 1 {base_2}.")
            else:
                mb.showerror("Ошибка", f"Валюта {target} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x200")

Label(text="Базовая валюта 1:", height=2).pack()
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack()

Label(text="Базовая валюта 2:", height=2).pack()
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack()




Label(text="Целевая валюта:").pack()
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack()
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = Label(height=2)
currency_label.pack()

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()