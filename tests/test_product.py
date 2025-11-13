from src.product import Product


def test_product_initialization() -> None:
    """Тест инициализации продукта"""
    name = "Test name"
    description = "Test description"
    price = 123.45
    quantity = 6

    product = Product(name, description, price, quantity)
    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity


def test_product_attributes_types() -> None:
    """Тест типов атрибутов Product"""

    product = Product("Test", "Desc", 100.0, 5)
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)
