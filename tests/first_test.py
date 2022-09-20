import pytest
from app.calculator import Calculator


class TestCalc: # Название класса тестов
    def setup(self):   #Предварительный метод setup в котором мы подключаем тестируемый объек Калькулятор
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):       # Простой тест, который проверяет, что функция возвращает корректный результат
        assert self.calc.multiply(self, 2 ,2) == 4

    def test_multiply_calculator_failed(self): # Умножение
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculator_corrуctly(self): # Деление
        assert self.calc.division(self, 6, 2) == 3

    def test_division_calculator_failed(self):
        assert self.calc.division(self, 6, 2) != 3

    def test_subtraction_calculator_correctly(self): # Вычитание
        assert self.calc.subtraction(self, 9, 6) == 3

    def test_subtraction_calculator_failed(self):
        assert self.calc.subtraction(self, 9, 6) != 3

    def test_adding_calculator_correctly(self): # Сложение
        assert self.calc.subtraction(self, 9, 6) == 15

    def test_adding_calculator_failed(self):
        assert self.calc.subtraction(self, 9, 6) != 15







