import tkinter as tk
import random

git_hub = "https://github.com/ваш_логин/ваш_репозиторий"

facts = [
    "Бананы радиоактивны и излучают небольшое количество гамма-излучения.",
    "Человек может обойтись без пищи до 2 месяцев, а без воды — всего несколько дней.",
    "Голубые киты ежедневно потребляют около 4 тонн пищи.",
    "Пчёлы могут распознавать лица людей.",
    "Существует 6 000 видов бананов, а не только один.",
    "Осьминоги имеют три сердца и голубую кровь.",
    "Страусы бегают быстрее лошадей.",
    "Смех заразителен и может передаваться между людьми.",
    "В Антарктиде есть действующий вулкан Эребус.",
    "Шоколад смертельно опасен для собак и кошек."
]

def show_fact():
    random_fact = random.choice(facts)
    fact_label.config(text=random_fact)

root = tk.Tk()
root.title("Случайные интересные факты")
root.geometry("700x250")

root.configure(bg='#f0f0f0')

title_label = tk.Label(
    root,
    text="Интересные факты о мире",
    font=("Arial", 16, "bold"),
    bg='#f0f0f0',
    fg='#2c3e50'
)
title_label.pack(pady=20)

fact_label = tk.Label(
    root,
    text="Нажмите на кнопку, чтобы узнать интересный факт!",
    font=("Arial", 12),
    bg='#ffffff',
    fg='#34495e',
    wraplength=600,
    relief="solid",
    borderwidth=2,
    padx=20,
    pady=20
)
fact_label.pack(pady=20, padx=20, ipadx=10, ipady=10)

show_button = tk.Button(
    root,
    text="Показать факт",
    font=("Arial", 14, "bold"),
    bg='#3498db',
    fg='white',
    activebackground='#2980b9',
    activeforeground='white',
    cursor="hand2",
    command=show_fact,
    padx=20,
    pady=10
)
show_button.pack(pady=10)

root.mainloop()