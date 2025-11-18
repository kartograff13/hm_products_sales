import pytest

from src.category import Category
from src.product import Product


def test_category_iterator_initialization(sample_products: list[Product]) -> None:
    """Тест инициализации итератора"""
    category = Category("Test Category", "Test Description", sample_products)
    iterator = iter(category)

    assert iterator._category == category
    assert iterator._index == 0


def test_category_iterator_iteration(sample_products: list[Product]) -> None:
    """Тест перебора товаров через итератор"""
    category = Category("Test Category", "Test Description", sample_products)
    iterated_products = []

    for product in category:
        iterated_products.append(product)

    assert len(iterated_products) == len(sample_products)
    assert iterated_products == sample_products


def test_category_iterator_multiple_iterations(sample_products: list[Product]) -> None:
    """Тест нескольких итераций по одной категории"""
    category = Category("Test Category", "Test Description", sample_products)
    first_iteration = list(category)
    second_iteration = []

    for product in category:
        second_iteration.append(product)

    assert first_iteration == second_iteration
    assert len(first_iteration) == len(sample_products)


def test_category_iterator_empty_category() -> None:
    """Тест итератора для пустой категории"""
    category = Category("Empty Category", "No products", [])
    products = list(category)

    assert products == []
    assert len(products) == 0


def test_category_iterator_stop_iteration(sample_products: list[Product]) -> None:
    """Тест корректного завершения итерации"""
    category = Category("Test Category", "Test Description", sample_products)
    iterator = iter(category)

    for _ in range(len(sample_products)):
        product = next(iterator)
        assert isinstance(product, Product)

    with pytest.raises(StopIteration):
        next(iterator)


def test_category_iterator_iter_method() -> None:
    """Тест метода __iter__ итератора"""
    category = Category("Test Category", "Test Description", [])
    iterator = iter(category)
    iterator_iter = iter(iterator)

    assert iterator_iter is iterator
    assert isinstance(iterator_iter, type(iterator))
