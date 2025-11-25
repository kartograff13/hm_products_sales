from abc import ABC, abstractmethod
from typing import Optional


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Абстрактный метод инициализации продукта"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления"""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения товаров"""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер для цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """Абстрактный сеттер для цены"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict, product_list: Optional[list["BaseProduct"]] = None) -> "BaseProduct":
        """Абстрактный класс-метод для создания нового продукта"""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Абстрактный геттер для названия"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Абстрактный геттер для описания"""
        pass

    @property
    @abstractmethod
    def quantity(self) -> int:
        """Абстрактный геттер для количества"""
        pass

    @quantity.setter
    @abstractmethod
    def quantity(self, value: int) -> None:
        """Абстрактный сеттер для количества"""
        pass
