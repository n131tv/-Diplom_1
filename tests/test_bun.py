import pytest
from praktikum.bun import Bun


class TestBun:

    def test_get_name_returns_correct_value(self):
        """
        Проверка: метод get_name возвращает корректное название булки.
        """
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'

    @pytest.mark.parametrize("name, price", [
        ("Флюоресцентная булка R2-D3", 988),
        ("Булка без названия", 0),
        ("Булка с отрицательной ценой", -50),
        ("Булка с плавающей ценой", 99.99),
    ])
    def test_get_price_returns_correct_value(self, name, price):
        """
        Проверка: метод get_price возвращает корректную цену булки
        для различных входных данных.
        """
        bun = Bun(name, price)
        assert bun.get_price() == price

