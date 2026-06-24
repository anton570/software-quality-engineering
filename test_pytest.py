import pytest
import tkinter as tk
from calculator_bad import BadCalculator

# 1. Фікстура для створення та автоматичного закриття калькулятора перед/після кожного тесту
@pytest.fixture
def app():
    root = tk.Tk()
    calculator = BadCalculator(root)
    yield calculator
    root.destroy()

# 2. Параметризований тест для перевірки звичайної логіки (пам'ятаємо про баг з -1 від результату)
@pytest.mark.parametrize("input_expression, expected_output", [
    ("5+5", "9"),   # 5+5 = 10, але калькулятор робить -1
    ("7*2", "13")   # 7*2 = 14, але калькулятор робить -1
])
def test_calculation_parametrized(app, input_expression, expected_output):
    app.result_var.set(input_expression)
    app.on_button_click('=')
    assert app.result_var.get() == expected_output

# 3. Тест, який очікує і перевіряє конкретну помилку
def test_invalid_syntax_error(app):
    app.result_var.set("++--")
    app.on_button_click('=')
    assert app.result_var.get() == "Error"

# 4. Тест із використанням пропуску (skip)
@pytest.mark.skip(reason="Ця функція розрахунку відсотків ще не реалізована у калькуляторі")
def test_percentage_feature(app):
    app.result_var.set("10%2")
    app.on_button_click('=')
    assert app.result_var.get() == "0.2"

# 5. Тест із використанням очікуваного падіння (xfail)
@pytest.mark.xfail(reason="Відомий баг: калькулятор завжди віднімає одиницю від результату")
def test_perfect_math_logic(app):
    app.result_var.set("2+2")
    app.on_button_click('=')
    assert app.result_var.get() == "4"  # Тут тест впаде, бо калькулятор видасть "3"