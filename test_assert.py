import tkinter as tk
from calculator_bad import BadCalculator

# Ініціалізуємо базові об'єкти програми для перевірки
root = tk.Tk()
app = BadCalculator(root)

print("Запуск тестів за допомогою assert...")

# Тест 1: Перевірка очищення екрана (кнопка 'C')
app.result_var.set("125")
app.on_button_click('C')
assert app.result_var.get() == "0", "Помилка: Кнопка очищення 'C' не скинула екран на 0!"

# Тест 2: Перевірка нашої обробки ділення на нуль
app.result_var.set("5/0")
app.on_button_click('=')
assert app.result_var.get() == "Zero Dev", "Помилка: Ділення на нуль не повернуло 'Zero Dev'!"

print("Усі assert-тести пройдено успішно!")