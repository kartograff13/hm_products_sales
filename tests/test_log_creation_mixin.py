import pytest

from src.lawngrass import LawnGrass
from src.log_creation_mixin import LogCreationMixin
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


class ProblematicAttributeTestClass(LogCreationMixin):
    """Тестовый класс с проблемным атрибутом, вызывающим AttributeError"""

    def __init__(self, normal_value: str = "test") -> None:
        """
        Инициализация тестового класса.

        Args:
            normal_value: Нормальное значение для атрибута
        """
        self.normal_attr = normal_value
        self._private_attr = "private"
        self._problem_attr = None
        super().__init__()

    @property
    def problem_attr(self) -> str:
        """Свойство, которое вызывает AttributeError при доступе"""
        if self._problem_attr is None:
            raise AttributeError("Simulated attribute error")
        return self._problem_attr


def test_repr_with_attribute_error() -> None:
    """Тест обработки AttributeError в методе __repr__"""
    test_obj = ProblematicAttributeTestClass("normal_value")

    with pytest.raises(AttributeError, match="Simulated attribute error"):
        _ = test_obj.problem_attr

    repr_str = repr(test_obj)

    assert "ProblematicAttributeTestClass" in repr_str
    assert "'normal_value'" in repr_str

    assert "_private_attr" not in repr_str
    assert "'private'" not in repr_str
    assert "problem_attr" not in repr_str


def test_repr_empty_object() -> None:
    """Тест __repr__ для объекта без атрибутов"""

    class EmptyClass(LogCreationMixin):
        """Пустой класс для тестирования"""

        def __init__(self) -> None:
            """Инициализация без атрибутов"""
            super().__init__()

    empty_obj = EmptyClass()
    repr_str = repr(empty_obj)

    assert repr_str == "EmptyClass()"
