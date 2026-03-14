# bank.py

import tkinter as tk
from datetime import datetime

main_window = tk.Tk()
main_window.title("Мой банк")
WIDTH = 800
HEIGHT = 600
main_window.geometry(f"{WIDTH}x{HEIGHT}")
main_window.resizable(False, False)

header_label = tk.Label(main_window, text="Мой банк",
        font=("Arial", 20, "bold"), fg="#2c3e50")
header_label.pack(pady=20)

balance_frame = tk.Frame(main_window, bg="#349db", 
    padx=30, pady=20)
balance_frame.pack(pady=10)


main_window.mainloop()



# config.py


TITLE = "Авторизация"
WIDTH = 800
HEIGHT = 600
ICON = "icons.ico"

# main.py

# name = input("Введи свое имя: ")
# age = int(input("Сколько тебе лет: "))
# NUMBER = 45
# print(f"======Калькулятор для {name}======")
# if age < 18: 
#     print(f"Прости дорогой {name}, но доступ закрыт!")
# else:
#     a, b, op = float(input()), float(input()), input()
#     print("Результат: ", eval(f"{a}{op}{b}"))

# # /
# # *
import tkinter as tk
from config import *

main_window = tk.Tk()
main_window.title(TITLE)
main_window.geometry(f"{WIDTH}x{HEIGHT}")
main_window.iconbitmap(ICON)

textBox = tk.Text(main_window, width=15, height=1)
textBox.pack()

button = tk.Button(main_window, text="Сказать привет", 
                command=lambda:print(
                    textBox.get(1.0, tk.END)
                ))
button.pack()


main_window.mainloop()
