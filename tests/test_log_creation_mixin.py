import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


class TestLogCreationMixin:
    def test_mixin_inheritance(self) -> None:
        """Тест, что миксин правильно наследуется"""
        assert hasattr(Product, "__repr__")
        assert hasattr(Smartphone, "__repr__")
        assert hasattr(LawnGrass, "__repr__")

    def test_repr_format_consistency(self) -> None:
        """Тест согласованности формата __repr__"""
        product = Product("Test", "Desc", 100.0, 5)
        smartphone = Smartphone("Phone", "Desc", 1000.0, 2, 85.0, "Model", 128, "Black")
        lawn_grass = LawnGrass("Grass", "Desc", 500.0, 10, "Country", "14 days", "Green")

        assert product.__repr__().startswith("Product(")
        assert smartphone.__repr__().startswith("Smartphone(")
        assert lawn_grass.__repr__().startswith("LawnGrass(")

    def test_repr_contains_class_name(self) -> None:
        """Тест, что __repr__ содержит имя класса"""
        product = Product("Test", "Desc", 100.0, 5)

        assert product.__class__.__name__ in repr(product)

    def test_creation_messages_contain_class_name(self, capsys: pytest.CaptureFixture) -> None:
        """Тест, что сообщения о создании содержат имя класса"""
        Product("Test", "Desc", 100.0, 5)
        Smartphone("Phone", "Desc", 1000.0, 2, 85.0, "Model", 128, "Black")
        captured = capsys.readouterr()

        assert "Product(" in captured.out
        assert "Smartphone(" in captured.out
