from src.product import Product


class Category:
    """Класс для представления категории товара"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список продуктов в категории
        """
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def get_products_count(self) -> int:
        """Метод для получения количества продуктов в категории"""
        return len(self.products)
