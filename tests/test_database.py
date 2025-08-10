from unittest.mock import patch
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class Ingredient:
    def __init__(self, name, type_, price=0):
        self._name = name
        self._type = type_
        self._price = price

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_price(self):
        return self._price


class TestDataBase:

    def test_available_buns_count_is_three(self):
        """Проверка: доступно ровно три булочки"""
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_ingredients_count_is_six(self):
        """Проверка: доступно ровно шесть ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_available_sauces_count_is_three(self):
        """Проверка: доступно ровно три соуса"""
        db = Database()
        sauces = [i for i in db.available_ingredients() if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_available_fillings_count_is_three(self):
        """Проверка: доступно ровно три начинки"""
        db = Database()
        fillings = [i for i in db.available_ingredients() if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    def test_hot_sauce_price_is_100(self):
        """Проверка: цена на 'hot sauce' равна 100"""
        db = Database()
        hot_sauce = next(i for i in db.available_ingredients() if i.get_name() == 'hot sauce')
        assert hot_sauce.get_price() == 100

    def test_available_sauces_count_is_less_than_three(self):
        """Альтернативный сценарий: доступно менее трёх соусов (мокаем данные)"""
        mock_ingredients = [
            Ingredient("hot sauce", INGREDIENT_TYPE_SAUCE),
            Ingredient("lettuce", INGREDIENT_TYPE_FILLING)
        ]

        with patch.object(Database, 'available_ingredients', return_value=mock_ingredients):
            db = Database()
            sauces = [i for i in db.available_ingredients() if i.get_type() == INGREDIENT_TYPE_SAUCE]
            assert len(sauces) == 1  # Явно проверяем, что соус один
