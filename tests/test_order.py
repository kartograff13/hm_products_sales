import pytest

from src.lawngrass import LawnGrass
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


class TestOrder:
    """Тесты для класса Order"""

    def test_order_initialization(self) -> None:
        """Тест инициализации заказа"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        order = Order(product, 3)

        assert order.product == product
        assert order.quantity == 3

    def test_order_total_cost(self) -> None:
        """Тест расчета итоговой стоимости заказа"""
        product = Product("Test Product", "Test Description", 150.0, 10)
        order = Order(product, 2)

        assert order.total_cost == 300.0

    def test_order_total_quantity(self) -> None:
        """Тест общего количества товаров в заказе"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        order = Order(product, 5)

        assert order.total_quantity == 5

    def test_order_products_list(self) -> None:
        """Тест списка продуктов в заказе"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        order = Order(product, 2)
        products = order.products

        assert len(products) == 1
        assert products[0] == product

    def test_order_str_representation(self) -> None:
        """Тест строкового представления заказа"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        order = Order(product, 3)
        expected_str = "Заказ: Test Product, количество: 3 шт., итоговая стоимость: 300.00 руб."

        assert str(order) == expected_str

    def test_order_repr_representation(self) -> None:
        """Тест repr представления заказа"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        order = Order(product, 3)
        repr_str = repr(order)

        assert "Order(" in repr_str
        assert "product=" in repr_str
        assert "quantity=3" in repr_str

    def test_order_with_smartphone(self) -> None:
        """Тест заказа со смартфоном"""
        smartphone = Smartphone(
            name="Test Phone",
            description="Test Description",
            price=1000.0,
            quantity=5,
            efficiency=80.5,
            model="Test Model",
            memory=128,
            color="Black",
        )
        order = Order(smartphone, 2)

        assert order.product == smartphone
        assert order.total_cost == 2000.0
        assert order.total_quantity == 2

    def test_order_with_lawngrass(self) -> None:
        """Тест заказа с газонной травой"""
        lawn_grass = LawnGrass(
            name="Test Grass",
            description="Test Description",
            price=500.0,
            quantity=10,
            country="Test Country",
            germination_period="14 days",
            color="Green",
        )
        order = Order(lawn_grass, 5)

        assert order.product == lawn_grass
        assert order.total_cost == 2500.0
        assert order.total_quantity == 5

    def test_order_creation_logging(self, capsys: pytest.CaptureFixture) -> None:
        """Тест логирования при создании заказа"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        Order(product, 3)
        captured = capsys.readouterr()

        assert "Создан объект: " in captured.out
        assert "Order(" in captured.out

    def test_order_inherits_from_product_container(self) -> None:
        """Тест, что Order наследуется от ProductContainer"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        order = Order(product, 3)

        assert hasattr(order, "products")
        assert hasattr(order, "total_quantity")
        assert hasattr(order, "total_cost")
        assert hasattr(order, "__str__")
