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
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_ingredients_count_is_six(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_available_sauces_count_is_three(self):
        db = Database()
        ingredients = db.available_ingredients()
        sauces = list(filter(lambda i: i.get_type() == INGREDIENT_TYPE_SAUCE, ingredients))
        assert len(sauces) == 3

    def test_available_fillings_count_is_three(self):
        db = Database()
        ingredients = db.available_ingredients()
        fillings = list(filter(lambda i: i.get_type() == INGREDIENT_TYPE_FILLING, ingredients))
        assert len(fillings) == 3

    def test_hot_sauce_price_is_100(self):
        db = Database()
        ingredients = db.available_ingredients()
        hot_sauce = next(filter(lambda i: i.get_name() == 'hot sauce', ingredients))
        assert hot_sauce.get_price() == 100

    def test_mocked_ingredients_has_one_sauce(self):
        mock_ingredients = [
            Ingredient("hot sauce", INGREDIENT_TYPE_SAUCE),
            Ingredient("lettuce", INGREDIENT_TYPE_FILLING)
        ]
        with patch.object(Database, 'available_ingredients', return_value=mock_ingredients):
            db = Database()
            sauces = list(filter(lambda i: i.get_type() == INGREDIENT_TYPE_SAUCE, db.available_ingredients()))
            assert len(sauces) == 1

    def test_mocked_ingredients_has_no_sauces(self):
        mock_ingredients = [
            Ingredient("lettuce", INGREDIENT_TYPE_FILLING),
            Ingredient("tomato", INGREDIENT_TYPE_FILLING)
        ]
        with patch.object(Database, 'available_ingredients', return_value=mock_ingredients):
            db = Database()
            sauces = list(filter(lambda i: i.get_type() == INGREDIENT_TYPE_SAUCE, db.available_ingredients()))
            assert len(sauces) == 0

    def test_mocked_ingredients_has_two_fillings(self):
        mock_ingredients = [
            Ingredient("lettuce", INGREDIENT_TYPE_FILLING),
            Ingredient("tomato", INGREDIENT_TYPE_FILLING)
        ]
        with patch.object(Database, 'available_ingredients', return_value=mock_ingredients):
            db = Database()
            fillings = list(filter(lambda i: i.get_type() == INGREDIENT_TYPE_FILLING, db.available_ingredients()))
            assert len(fillings) == 2
