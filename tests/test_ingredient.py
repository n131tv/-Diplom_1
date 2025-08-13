import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price_returns_correct_value(self):
        """Проверка: метод get_price возвращает корректную цену ингредиента."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        assert ingredient.get_price() == 15

    def test_get_name_returns_correct_value(self):
        """Проверка: метод get_name возвращает корректное название ингредиента."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        assert ingredient.get_name() == 'Соус традиционный галактический'

    def test_get_type_returns_sauce_for_sauce_ingredient(self):
        """Проверка: метод get_type возвращает 'SAUCE' для ингредиента-соуса."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        assert ingredient.get_type() == 'SAUCE'

    def test_get_type_returns_filling_for_filling_ingredient(self):
        """Проверка: метод get_type возвращает 'FILLING' для ингредиента-начинки."""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 300)
        assert ingredient.get_type() == 'FILLING'

