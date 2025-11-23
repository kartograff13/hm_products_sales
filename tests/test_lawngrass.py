from src.lawngrass import LawnGrass


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


def test_lawngrass_addition() -> None:
    """Тест сложения продуктов газонная трава"""
    grass1 = LawnGrass("Grass1", "Desc1", 500.0, 5, "Country1", "14 days", "Green")
    grass2 = LawnGrass("Grass2", "Desc2", 700.0, 3, "Country2", "21 days", "Dark Green")

    total_value = grass1 + grass2
    expected_value = (500.0 * 5) + (700.0 * 3)

    assert total_value == expected_value
