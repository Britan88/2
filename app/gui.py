import asyncio
import tkinter as tk
from tkinter import messagebox

from auth import check_login
from parser import parse_wb


def start_gui():
    root = tk.Tk()
    root.title("WB Parser")

    tk.Label(root, text="Логин").pack()
    login = tk.Entry(root)
    login.pack()

    tk.Label(root, text="Пароль").pack()
    password = tk.Entry(root, show="*")
    password.pack()

    def run_parser():
        asyncio.run(parse_wb())
        messagebox.showinfo("Готово", "Парсинг завершён")

    def login_click():
        if check_login(login.get(), password.get()):
            run_parser()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")

    tk.Button(root, text="Войти", command=login_click).pack()
    root.mainloop()
