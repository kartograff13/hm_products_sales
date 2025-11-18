from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.category import Category  # type: ignore
    from src.product import Product  # type: ignore


class CategoryIterator:
    """Класс-итератор для перебора товаров в категории"""

    def __init__(self, category: "Category") -> None:
        """
        Инициализация итератора.

        Args:
            category: Объект категории для итерации
        """
        self._category = category
        self._index = 0

    def __iter__(self) -> "CategoryIterator":
        """Возвращает сам итератор"""
        return self

    def __next__(self) -> "Product":
        """
        Возвращает следующий товар в категории.

        Returns:
            Следующий объект Product

        Raises:
            StopIteration: Когда товары закончились
        """
        products = self._category.get_products_objects()

        if self._index < len(products):
            product = products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration
