import praktikum.ingredient_types
from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database


class TestBurger:

    def test_set_bun_assigns_correct_bun(self):
        """Проверка: метод set_buns корректно устанавливает булку."""
        burger = Burger()
        bun = Bun('Name_bun', 100.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_appends_filling_to_list(self):
        """Проверка: метод add_ingredient добавляет начинку в список."""
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = 'cutlet'

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    def test_add_ingredient_appends_sauce_to_list(self):
        """Проверка: метод add_ingredient добавляет соус в список."""
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = 'hot sauce'

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE

    def test_remove_ingredient_deletes_from_list(self):
        """Проверка: метод remove_ingredient удаляет ингредиент по индексу."""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_get_price_returns_correct_total_with_one_ingredient(self):
        """Проверка: метод get_price возвращает корректную сумму с одним ингредиентом."""
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[0])  # Цена булки: 100
        burger.add_ingredient(db.available_ingredients()[0])  # hot sauce: 100
        # Общая цена: 100*2 + 100 = 300
        assert burger.get_price() == 300.0

    def test_get_price_returns_correct_total_with_multiple_ingredients(self):
        """Проверка: метод get_price возвращает корректную сумму с несколькими ингредиентами."""
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[0])  # Цена булки: 100
        burger.add_ingredient(db.available_ingredients()[0])  # hot sauce: 100
        burger.add_ingredient(db.available_ingredients()[3])  # cutlet: 100
        # Общая цена: 100*2 + 100 + 100 = 400
        assert burger.get_price() == 400.0

    def test_get_receipt_returns_expected_format_with_sauce(self):
        """Проверка: метод get_receipt возвращает корректный чек с соусом."""
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[0])  # black bun
        burger.add_ingredient(db.available_ingredients()[0])  # hot sauce

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            "Price: 300"
        )
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_returns_expected_format_with_filling(self):
        """Проверка: метод get_receipt возвращает корректный чек с начинкой."""
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[0])  # black bun
        burger.add_ingredient(db.available_ingredients()[3])  # cutlet

        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 300"
        )
        assert burger.get_receipt() == expected_receipt

    def test_move_ingredient_moves_from_higher_to_lower_index(self):
        """Проверка: метод move_ingredient перемещает ингредиент с большего на меньший индекс."""
        burger = Burger()
        ingredients = [
            Mock(get_name=lambda: 'Lettuce'),
            Mock(get_name=lambda: 'Tomato'),
            Mock(get_name=lambda: 'Cheese')
        ]
        for ing in ingredients:
            burger.add_ingredient(ing)

        burger.move_ingredient(2, 0)  # Перемещаем Cheese на первую позицию

        assert [i.get_name() for i in burger.ingredients] == ['Cheese', 'Lettuce', 'Tomato']

    def test_move_ingredient_moves_from_lower_to_higher_index(self):
        """Проверка: метод move_ingredient перемещает ингредиент с меньшего на больший индекс."""
        burger = Burger()
        ingredients = [
            Mock(get_name=lambda: 'Lettuce'),
            Mock(get_name=lambda: 'Tomato'),
            Mock(get_name=lambda: 'Cheese')
        ]
        for ing in ingredients:
            burger.add_ingredient(ing)

        burger.move_ingredient(0, 2)  # Перемещаем Lettuce на последнюю позицию

        assert [i.get_name() for i in burger.ingredients] == ['Tomato', 'Cheese', 'Lettuce']

