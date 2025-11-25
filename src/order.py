from src.base_product import BaseProduct
from src.log_creation_mixin import LogCreationMixin
from src.product_container import ProductContainer


class Order(LogCreationMixin, ProductContainer):
    """Класс для представления заказа"""

    def __init__(self, product: BaseProduct, quantity: int) -> None:
        """
        Инициализация заказа.

        Args:
            product: Купленный товар
            quantity: Количество купленного товара
        """
        self._product = product
        self._quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Строковое представление заказа"""
        return (
            f"Заказ: {self.product.name}, количество: {self.quantity} шт., "
            f"итоговая стоимость: {self.total_cost:.2f} руб."
        )

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта Order"""
        return f"Order(product={self.product!r}, quantity={self.quantity})"

    @property
    def product(self) -> BaseProduct:
        """Геттер для купленного товара"""
        return self._product

    @property
    def quantity(self) -> int:
        """Геттер для количества купленного товара"""
        return self._quantity

    @property
    def products(self) -> list[BaseProduct]:
        """Свойство для получения списка продуктов (в заказе всегда один продукт)"""
        return [self._product]

    @property
    def total_quantity(self) -> int:
        """Общее количество товаров в заказе"""
        return self._quantity

    @property
    def total_cost(self) -> float:
        """Итоговая стоимость заказа"""
        return self._product.price * self._quantity
