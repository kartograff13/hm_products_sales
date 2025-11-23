from src.smartphone import Smartphone


def test_smartphone_initialization() -> None:
    """Тест инициализации продукта смартфон"""
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

    assert smartphone.name == "Test Phone"
    assert smartphone.description == "Test Description"
    assert smartphone.price == 1000.0
    assert smartphone.quantity == 5

    assert smartphone.efficiency == 80.5
    assert smartphone.model == "Test Model"
    assert smartphone.memory == 128
    assert smartphone.color == "Black"


def test_smartphone_inheritance() -> None:
    """Тест наследования от базового класса Product"""
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

    assert isinstance(smartphone, Smartphone)

    assert hasattr(smartphone, "price")
    assert hasattr(smartphone, "quantity")
    assert hasattr(smartphone, "__add__")


def test_smartphone_addition() -> None:
    """Тест сложения продуктов смартфон"""
    smartphone1 = Smartphone("Phone1", "Desc1", 1000.0, 2, 80.0, "Model1", 64, "Black")
    smartphone2 = Smartphone("Phone2", "Desc2", 1500.0, 3, 85.0, "Model2", 128, "White")

    total_value = smartphone1 + smartphone2
    expected_value = (1000.0 * 2) + (1500.0 * 3)

    assert total_value == expected_value
