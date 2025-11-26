import pytest

from src.category import Category
from src.order import Order
from src.product import Product
from src.zero_quantity_error import ZeroQuantityError


class TestZeroQuantityError:
    """Тесты для исключения ZeroQuantityError"""

    def test_zero_quantity_error_initialization(self) -> None:
        """Тест инициализации исключения ZeroQuantityError"""
        error = ZeroQuantityError("Тестовое сообщение")

        assert str(error) == "Тестовое сообщение"

    def test_add_product_with_zero_quantity_to_category(self) -> None:
        """Тест добавления товара с нулевым количеством в категорию"""
        category = Category("Test Category", "Test Description", [])
        product = Product("Zero Product", "Description", 100.0, 1)

        product.quantity = 0

        with pytest.raises(ZeroQuantityError,
                           match="Товар 'Zero Product' имеет нулевое количество и не может быть добавлен в категорию"):
            category.add_product(product)

    def test_create_order_with_zero_quantity(self) -> None:
        """Тест создания заказа с нулевым количеством"""
        product = Product("Test Product", "Description", 100.0, 10)

        with pytest.raises(ZeroQuantityError, match="Нельзя создать заказ с нулевым количеством товара 'Test Product'"):
            Order(product, 0)

    def test_successful_product_addition(self) -> None:
        """Тест успешного добавления товара в категорию"""
        category = Category("Test Category", "Test Description", [])
        product = Product("Test Product", "Description", 100.0, 5)

        category.add_product(product)

        assert category.get_products_count() == 1

    def test_successful_order_creation(self) -> None:
        """Тест успешного создания заказа"""
        product = Product("Test Product", "Description", 100.0, 10)

        order = Order(product, 3)

        assert order.quantity == 3
        assert order.total_cost == 300.0

    def test_order_with_product_that_became_zero(self) -> None:
        """Тест заказа, когда товар стал с нулевым количеством после создания"""
        product = Product("Test Product", "Description", 100.0, 10)

        order = Order(product, 2)

        assert order.quantity == 2

        product.quantity = 0

        assert order.total_cost == 200.0
