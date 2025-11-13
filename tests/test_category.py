from src.category import Category
from src.product import Product


def test_category_initialization(sample_products: list[Product]) -> None:
    name = "Test name"
    description = "Test descriptions"
    category = Category(name, description, sample_products)

    assert category.name == name
    assert category.description == description
    assert category.products == sample_products


def test_category_count_increment() -> None:
    """Тест подсчета количества категорий"""
    category1 = Category("Category 1", "Desc 1", [])
    initial_count = Category.category_count
    category2 = Category("Category 2", "Desc 2", [])

    assert Category.category_count == initial_count + 1
    assert category1.category_count == Category.category_count
    assert category2.category_count == Category.category_count


def test_product_count_increment(sample_products: list[Product]) -> None:
    """Тест подсчета количества продуктов"""
    initial_product_count = Category.product_count
    category = Category("Test Category", "Test Desc", sample_products)

    assert Category.product_count == initial_product_count + len(sample_products)
    assert category.product_count == Category.product_count


def test_empty_category() -> None:
    """Тест создания категории без продуктов"""
    category = Category("Empty Category", "No products", [])

    assert category.name == "Empty Category"
    assert category.description == "No products"
    assert category.products == []
    assert category.get_products_count() == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_attributes_types(sample_products: list[Product]) -> None:
    """Тест типов атрибутов Category"""
    category = Category("Test", "Desc", sample_products)

    assert isinstance(category.name, str)
    assert isinstance(category.description, str)
    assert isinstance(category.products, list)
    assert isinstance(Category.category_count, int)
    assert isinstance(Category.product_count, int)


def test_get_products_count_method(sample_products: list[Product]) -> None:
    """Тест метода get_products_count"""
    category = Category("Test Category", "Test Desc", sample_products)
    products_count = category.get_products_count()

    assert products_count == len(sample_products)
    assert products_count == 2
