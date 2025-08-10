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

    """ Тест на получение доступных булочек """
    def test_bun_count_is_three(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    """ Тест на получение всех доступных ингредиентов """
    def test_all_ingredients_listed(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    """ Тест: доступны ровно три соуса """
    def test_three_sauces_available(self):
        db = Database()
        sauces = [i for i in db.available_ingredients() if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    """ Тест: доступны ровно три начинки """
    def test_three_fillings_available(self):
        db = Database()
        fillings = [i for i in db.available_ingredients() if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    """ Тест: цена на hot sauce корректна """
    def test_hot_sauce_price_is_correct(self):
        db = Database()
        hot_sauce = next(i for i in db.available_ingredients() if i.get_name() == 'hot sauce')
        assert hot_sauce.get_price() == 100

    """ Тест: альтернативный сценарий — доступно менее трёх соусов """
    def test_less_than_three_sauces_available(self):
        mock_ingredients = [
            Ingredient("hot sauce", INGREDIENT_TYPE_SAUCE),
            Ingredient("lettuce", INGREDIENT_TYPE_FILLING)
        ]

        with patch.object(Database, 'available_ingredients', return_value=mock_ingredients):
            db = Database()
            sauces = [i for i in db.available_ingredients() if i.get_type() == INGREDIENT_TYPE_SAUCE]
            assert len(sauces) < 3
