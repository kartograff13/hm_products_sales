import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_lawngrass_initialization() -> None:
    """Тест инициализации продукта газонная трава"""
    lawn_grass = LawnGrass(
        name="Test Grass",
        description="Test Description",
        price=500.0,
        quantity=10,
        country="Test Country",
        germination_period="14 days",
        color="Green",
    )

    assert lawn_grass.name == "Test Grass"
    assert lawn_grass.description == "Test Description"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 10

    assert lawn_grass.country == "Test Country"
    assert lawn_grass.germination_period == "14 days"
    assert lawn_grass.color == "Green"


def test_lawngrass_inheritance() -> None:
    """Тест наследования от базового класса Product"""
    lawn_grass = LawnGrass(
        name="Test Grass",
        description="Test Description",
        price=500.0,
        quantity=10,
        country="Test Country",
        germination_period="14 days",
        color="Green",
    )

    assert isinstance(lawn_grass, LawnGrass)

    assert hasattr(lawn_grass, "price")
    assert hasattr(lawn_grass, "quantity")
    assert hasattr(lawn_grass, "__add__")


def test_lawngrass_addition_same_class() -> None:
    """Тест сложения продукта газонная трава одного класса"""
    grass1 = LawnGrass("Grass1", "Desc1", 500.0, 5, "Country1", "14 days", "Green")
    grass2 = LawnGrass("Grass2", "Desc2", 700.0, 3, "Country2", "21 days", "Dark Green")

    total_value = grass1 + grass2
    expected_value = (500.0 * 5) + (700.0 * 3)

    assert total_value == expected_value


def test_lawngrass_addition_different_classes_error() -> None:
    """Тест ошибки при сложении продукта газонная трава с товарами других классов"""
    lawn_grass = LawnGrass("Grass", "Desc", 500.0, 5, "Country", "14 days", "Green")
    product = Product("Product", "Desc", 300.0, 10)
    smartphone = Smartphone("Phone", "Desc", 1000.0, 2, 80.0, "Model", 64, "Black")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов. "):
        _ = lawn_grass + product

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов. "):
        _ = lawn_grass + smartphone

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов. "):
        _ = product + lawn_grass


def test_lawngrass_zero_quantity_initialization() -> None:
    """Тест создания товара газонная трава с нулевым количеством (должен вызывать ValueError)"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен. "):
        LawnGrass(
            name="Test Grass",
            description="Test Description",
            price=500.0,
            quantity=0,
            country="Test Country",
            germination_period="14 days",
            color="Green",
        )
