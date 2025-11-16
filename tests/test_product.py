from unittest.mock import MagicMock, patch

import pytest

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


def test_price_getter() -> None:
    """Тест геттера price"""
    product = Product("Test Product", "Description", 150.0, 10)

    assert product.price == 150.0


def test_price_setter_positive() -> None:
    """Тест сеттера price с корректным значением"""
    product = Product("Test Product", "Description", 100.0, 10)
    product.price = 150.0

    assert product.price == 150.0


def test_price_setter_negative_price() -> None:
    """Тест сеттера price с отрицательным значением"""
    product = Product("Test Product", "Description", 100.0, 10)

    with patch("builtins.print") as mock_print:
        product.price = -50.0

        assert product.price == 100.0

        mock_print.assert_called_with("Цена не должна быть нулевая или отрицательная. ")


def test_price_setter_zero_price() -> None:
    """Тест сеттера цены с нулевым значением"""
    product = Product("Test Product", "Description", 100.0, 10)

    with patch("builtins.print") as mock_print:
        product.price = 0.0

        assert product.price == 100.0

        mock_print.assert_called_with("Цена не должна быть нулевая или отрицательная. ")


def test_price_increase() -> None:
    """Тест повышения цены (без подтверждения)"""
    product = Product("Test Product", "Description", 100.0, 10)

    with patch("builtins.print") as mock_print:
        product.price = 150.0

        assert product.price == 150.0

        mock_print.assert_called_with("Цена товара Test Product успешно повышена до 150.0. ")


@patch("builtins.input")
def test_price_decrease_with_confirmation(mock_input: MagicMock) -> None:
    """Тест понижения цены с подтверждением (y)"""
    product = Product("Test Product", "Description", 100.0, 10)
    mock_input.return_value = "y"

    with patch("builtins.print") as mock_print:
        product.price = 80.0

        assert product.price == 80.0

        mock_input.assert_called_once()
        mock_print.assert_called_with("Цена товара Test Product успешно изменена на 80.0. ")


@patch("builtins.input")
def test_price_decrease_with_rejection(mock_input: MagicMock) -> None:
    """Тест понижения цены с отказом (n)"""
    product = Product("Test Product", "Description", 100.0, 10)
    mock_input.return_value = "n"

    with patch("builtins.print") as mock_print:
        product.price = 80.0

        assert product.price == 100.0

        mock_input.assert_called_once()
        mock_print.assert_called_with("Изменение цены товара Test Product отменено. ")


@patch("builtins.input")
def test_price_decrease_with_invalid_input_then_confirmation(mock_input: MagicMock) -> None:
    """Тест понижения цены с некорректным вводом, затем подтверждением"""
    product = Product("Test Product", "Description", 100.0, 10)
    mock_input.side_effect = ["invalid", "x", "y"]

    with patch("builtins.print") as mock_print:
        product.price = 80.0

        assert product.price == 80.0
        assert mock_input.call_count == 3

        mock_print.assert_any_call("Некорректный ввод. Пожалуйста, введите 'y' для подтверждения или 'n' для отмены. ")


def test_new_product_creation() -> None:
    """Тест создания нового продукта через класс-метод"""
    product_data = {"name": "New Product", "description": "New Description", "price": 200.0, "quantity": 15}

    product = Product.new_product(product_data)

    assert product.name == "New Product"
    assert product.description == "New Description"
    assert product.price == 200.0
    assert product.quantity == 15


def test_new_product_with_duplicate() -> None:
    """Тест создания продукта с дубликатом (обновление существующего)"""
    existing_product = Product("Existing Product", "Description", 100.0, 10)
    product_list = [existing_product]

    product_data = {"name": "Existing Product", "description": "Updated Description", "price": 150.0, "quantity": 5}

    with patch("builtins.print") as mock_print:
        result = Product.new_product(product_data, product_list)

        assert result is existing_product
        assert result.quantity == 15
        assert result.price == 150.0

        mock_print.assert_called_with("Цена товара Existing Product успешно повышена до 150.0. ")


def test_new_product_with_duplicate_lower_price() -> None:
    """Тест создания продукта с дубликатом с более низкой ценой"""
    existing_product = Product("Existing Product", "Description", 100.0, 10)
    product_list = [existing_product]

    product_data = {"name": "Existing Product", "description": "Updated Description", "price": 80.0, "quantity": 5}

    result = Product.new_product(product_data, product_list)

    assert result is existing_product
    assert result.quantity == 15
    assert result.price == 100.0


def test_new_product_without_duplicate() -> None:
    """Тест создания нового продукта без дубликатов"""
    existing_product = Product("Existing Product", "Description", 100.0, 10)
    product_list = [existing_product]

    product_data = {"name": "Different Product", "description": "Different Description", "price": 200.0, "quantity": 5}

    result = Product.new_product(product_data, product_list)

    assert result is not existing_product
    assert result.name == "Different Product"
    assert result.price == 200.0
    assert result.quantity == 5


def test_new_product_with_none_list() -> None:
    """Тест создания нового продукта с пустым списком (None)"""
    product_data = {"name": "New Product", "description": "New Description", "price": 200.0, "quantity": 15}

    product = Product.new_product(product_data, None)

    assert product.name == "New Product"
    assert product.description == "New Description"
    assert product.price == 200.0
    assert product.quantity == 15


def test_private_price_attribute() -> None:
    """Тест на приватность аттрибута __price"""
    product = Product("Test Product", "Description", 100.0, 10)

    with pytest.raises(AttributeError):
        _ = product.__price  # type: ignore
