from src.base_product import BaseProduct
from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_category_initialization(sample_products: list[BaseProduct]) -> None:
    """Тест корректности инициализации объекта Category"""
    name = "Test name"
    description = "Test descriptions"
    category = Category(name, description, sample_products)

    assert category.name == name
    assert category.description == description

    expected_products = ["Product 1, 123.45 руб. Остаток: 10 шт.\n", "Product 2, 678.9 руб. Остаток: 20 шт.\n"]

    assert category.get_products_info == expected_products


def test_category_count_increment() -> None:
    """Тест подсчета количества категорий"""
    category1 = Category("Category 1", "Desc 1", [])
    initial_count = Category.category_count
    category2 = Category("Category 2", "Desc 2", [])

    assert Category.category_count == initial_count + 1
    assert category1.category_count == Category.category_count
    assert category2.category_count == Category.category_count


def test_product_count_increment(sample_products: list[BaseProduct]) -> None:
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


def test_category_attributes_types(sample_products: list[BaseProduct]) -> None:
    """Тест типов атрибутов Category"""
    category = Category("Test", "Desc", sample_products)

    assert isinstance(category.name, str)
    assert isinstance(category.description, str)
    assert isinstance(category.products, list)
    assert isinstance(Category.category_count, int)
    assert isinstance(Category.product_count, int)


def test_get_products_count_method(sample_products: list[BaseProduct]) -> None:
    """Тест метода get_products_count"""
    category = Category("Test Category", "Test Desc", sample_products)
    products_count = category.get_products_count()

    assert products_count == len(sample_products)
    assert products_count == 2


def test_add_product_method(sample_products: list[BaseProduct]) -> None:
    """Тест метода add_product"""
    category = Category("Test Category", "Test Description", [])
    init_count = category.get_products_count()
    init_total_count = Category.product_count

    new_product = Product("New Product", "New Desc", 100.5, 5)
    category.add_product(new_product)

    assert category.get_products_count() == init_count + 1
    assert Category.product_count == init_total_count + 1

    expected_product_string = "New Product, 100.5 руб. Остаток: 5 шт.\n"

    assert expected_product_string in category.get_products_info


def test_products_getter_format(sample_products: list[BaseProduct]) -> None:
    """Тест формата вывода геттера products"""
    category = Category("Test Category", "Test Desc", sample_products)
    products_list = category.get_products_info

    expected_formats = ["Product 1, 123.45 руб. Остаток: 10 шт.\n", "Product 2, 678.9 руб. Остаток: 20 шт.\n"]

    assert products_list == expected_formats


def test_get_products_objects_method(sample_products: list[BaseProduct]) -> None:
    """Тест метода get_products_objects"""
    category = Category("Test Category", "Test Desc", sample_products)
    products_objects = category.get_products_objects()

    assert isinstance(products_objects, list)
    assert len(products_objects) == 2
    assert all(isinstance(product, Product) for product in products_objects)

    assert products_objects[0].name == "Product 1"
    assert products_objects[1].name == "Product 2"
    assert products_objects[0].price == 123.45
    assert products_objects[1].price == 678.9


def test_products_encapsulation() -> None:
    """Тест инкапсуляции списка продуктов"""
    category = Category("Test Category", "Test Desc", [])

    assert hasattr(category, "get_products_objects")
    assert hasattr(category, "add_product")
    assert hasattr(category, "products")

    assert category.get_products_count() == 0
    assert category.products == []


def test_products_list_integrity(sample_products: list[BaseProduct]) -> None:
    """Тест целостности списка продуктов после операций"""
    category = Category("Test Category", "Test Desc", sample_products)

    initial_count = category.get_products_count()
    initial_products = category.get_products_info.copy()

    new_product = Product("Additional Product", "Additional Desc", 50.0, 3)
    category.add_product(new_product)

    assert category.get_products_count() == initial_count + 1
    assert len(category.get_products_info) == initial_count + 1

    for product_str in initial_products:
        assert product_str in category.get_products_info

    assert "Additional Product, 50.0 руб. Остаток: 3 шт.\n" in category.get_products_info


def test_category_str_representation(sample_products: list[BaseProduct]) -> None:
    """Тест строкового представления категории"""
    category = Category("Смартфоны", "Мобильные устройства", sample_products)
    expected_str = "Смартфоны, количество продуктов: 30 шт."

    assert str(category) == expected_str

    new_product = Product("New Phone", "Description", 50000.0, 5)
    category.add_product(new_product)
    updated_str = "Смартфоны, количество продуктов: 35 шт."

    assert str(category) == updated_str


def test_add_product_combined_validation() -> None:
    """Тест комбинированной проверки с isinstance и issubclass"""
    category = Category("Test Category", "Test Description", [])

    valid_objects = [
        Product("Product", "Desc", 100.0, 5),
        Smartphone("Smartphone", "Desc", 200.0, 3, 80.0, "Model", 64, "Black"),
        LawnGrass("LawnGrass", "Desc", 300.0, 2, "Country", "14 days", "Green"),
    ]

    for obj in valid_objects:
        try:
            category.add_product(obj)
            print(f"Успешно добавлен: {type(obj).__name__}")
        except TypeError:
            print(f"Ошибка при добавлении: {type(obj).__name__}")

    invalid_objects = ["string", 123, 45.67, None, ["list"], {"dict": "value"}]

    for obj in invalid_objects:  # type: ignore
        try:
            category.add_product(obj)  # type: ignore
            print(f"Не вызвана ошибка для: {type(obj).__name__}")
        except TypeError:
            print(f"Корректно заблокирован: {type(obj).__name__}")

    assert category.get_products_count() == 3


def test_category_total_cost(sample_products: list[BaseProduct]) -> None:
    """Тест расчета общей стоимости товаров в категории"""
    category = Category("Test Category", "Test Description", sample_products)

    expected_cost = (123.45 * 10) + (678.9 * 20)
    assert category.total_cost == expected_cost
