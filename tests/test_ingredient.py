import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price_returns_correct_value(self):
        """
        Проверка: метод get_price возвращает корректную цену ингредиента.
        """
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        assert ingredient.get_price() == 15

    def test_get_name_returns_correct_value(self):
        """
        Проверка: метод get_name возвращает корректное название ингредиента.
        """
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        assert ingredient.get_name() == 'Соус традиционный галактический'

    @pytest.mark.parametrize(
        "type_, name, price, expected_type",
        [
            (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15, 'SAUCE'),
            (INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 300, 'FILLING'),
        ]
    )
    def test_get_type_returns_correct_value(self, type_, name, price, expected_type):
        """
        Проверка: метод get_type возвращает корректный тип ингредиента.
        """
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_type() == expected_type

