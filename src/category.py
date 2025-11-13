from src.product import Product


class Category:
    """Класс для представления категории товара"""

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
