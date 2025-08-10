import praktikum.ingredient_types
from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database


class TestBurger:

    def test_set_bun_assigns_correct_bun(self):
        """
        Проверка: метод set_buns корректно устанавливает булку.
        """
        burger = Burger()
        bun = Bun('Name_bun', 100.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_appends_to_list(self):
        """
        Проверка: метод add_ingredient добавляет ингредиент в список.
        """
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Name_bun'
        mock_ingredient.get_price.return_value = 9.0
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient)

        ingredient = burger.ingredients[0]
        assert ingredient.get_name() == 'Name_bun'
        assert ingredient.get_price() == 9.0
        assert ingredient.get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    def test_remove_ingredient_deletes_from_list(self):
        """
        Проверка: метод remove_ingredient удаляет ингредиент по индексу.
        """
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_get_price_returns_correct_total(self):
        """
        Проверка: метод get_price возвращает корректную сумму стоимости бургера.
        """
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[0])  # Цена булки: 100
        burger.add_ingredient(db.available_ingredients()[0])  # hot sauce: 100
        burger.add_ingredient(db.available_ingredients()[3])  # cutlet: 100
        # Общая цена: 100 (булка) * 2 + 100 + 100 = 400
        assert burger.get_price() == 400.0

    def test_get_receipt_returns_expected_format(self):
        """
        Проверка: метод get_receipt возвращает чек в ожидаемом формате.
        """
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[0])  # black bun
        burger.add_ingredient(db.available_ingredients()[0])  # hot sauce
        burger.add_ingredient(db.available_ingredients()[3])  # cutlet

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 400"
        )
        assert burger.get_receipt() == expected_receipt

    def test_move_ingredient_changes_order_correctly(self):
        """
        Проверка: метод move_ingredient корректно меняет порядок ингредиентов.
        """
        burger = Burger()

        ingredient1 = Mock()
        ingredient1.get_name.return_value = 'Lettuce'
        ingredient2 = Mock()
        ingredient2.get_name.return_value = 'Tomato'
        ingredient3 = Mock()
        ingredient3.get_name.return_value = 'Cheese'

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        # Начальный порядок
        assert [i.get_name() for i in burger.ingredients] == ['Lettuce', 'Tomato', 'Cheese']

        # Перемещаем Cheese (индекс 2) на позицию 0
        burger.move_ingredient(2, 0)

        # Новый порядок
        assert [i.get_name() for i in burger.ingredients] == ['Cheese', 'Lettuce', 'Tomato']

