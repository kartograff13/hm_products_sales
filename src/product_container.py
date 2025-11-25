from abc import ABC, abstractmethod

from src.base_product import BaseProduct


class ProductContainer(ABC):
    """Абстрактный базовый класс для контейнеров продуктов"""

    @abstractmethod
    def __init__(self) -> None:
        """Абстрактный метод инициализации"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления"""
        pass

    @property
    @abstractmethod
    def products(self) -> list[BaseProduct]:
        """Абстрактное свойство для получения списка продуктов"""
        pass

    @property
    @abstractmethod
    def total_quantity(self) -> int:
        """Абстрактное свойство для получения общего количества товаров"""
        pass

    @property
    @abstractmethod
    def total_cost(self) -> float:
        """Абстрактное свойство для получения общей стоимости"""
        pass
