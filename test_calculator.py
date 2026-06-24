import unittest
import tkinter as tk
from calculator_bad import BadCalculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        # Виконується автоматично перед кожним тестом
        self.root = tk.Tk()
        self.app = BadCalculator(self.root)

    def tearDown(self):
        # Виконується автоматично після кожного тесту
        self.root.destroy()

    def test_clear_button(self):
        # Тест кнопки очищення 'C'
        self.app.result_var.set("999")
        self.app.on_button_click('C')
        self.assertEqual(self.app.result_var.get(), "0")

    def test_division_by_zero(self):
        # Тест нашої обробки ділення на нуль
        self.app.result_var.set("10/0")
        self.app.on_button_click('=')
        self.assertEqual(self.app.result_var.get(), "Zero Dev")

    def test_bad_calculation_logic(self):
        # Тест специфічної логіки нашого калькулятора (він робить результат -1)
        self.app.result_var.set("5+5")
        self.app.on_button_click('=')
        self.assertEqual(self.app.result_var.get(), "9")

if __name__ == "__main__":
    unittest.main()