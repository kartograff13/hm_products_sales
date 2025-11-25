from typing import TYPE_CHECKING

from src.base_product import BaseProduct

if TYPE_CHECKING:
    from src.category_iterator import CategoryIterator


class Category:
    """Класс для представления категории товара"""

    name: str
    description: str
    __products: list[BaseProduct]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[BaseProduct]) -> None:
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список продуктов в категории
        """
        self.name = name
        self.description = description
        self.__products = []

        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def __str__(self) -> str:
        """Строковое отображение категории товара"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> "CategoryIterator":
        """
        Возвращает итератор для перебора товаров в категории.

        Returns:
            Объект CategoryIterator
        """
        from src.category_iterator import CategoryIterator

        return CategoryIterator(self)

    def add_product(self, product: BaseProduct) -> None:
        """
        Добавления товара в категорию.

        Args:
            product: Объект товара для добавления

        Raises:
            TypeError: Если product не является экземпляром Product или его подклассов
        """
        if not isinstance(product, BaseProduct) or not issubclass(type(product), BaseProduct):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    def get_products_count(self) -> int:
        """Метод для получения количества товаров в категории"""
        return len(self.__products)

    @property
    def products(self) -> list[str]:
        """Геттер для получения списка товаров в list[str]"""
        return [str(product) + "\n" for product in self.__products]

    def get_products_objects(self) -> list[BaseProduct]:
        """Возвращает список объектов (продуктов) для проверки дубликатов"""
        return self.__products
