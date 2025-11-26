from typing import Optional, cast

from src.base_product import BaseProduct
from src.log_creation_mixin import LogCreationMixin


class Product(LogCreationMixin, BaseProduct):
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация продукта.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество в наличии

        Raises:
            ValueError: Если количество товара равно нулю
        """
        self._name = name
        self._description = description
        self.__price = price
        if quantity != 0:
            self._quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен. ")
        super().__init__()

    def __str__(self) -> str:
        """Строковое отображение товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "BaseProduct") -> float:
        """Сложение товаров - возвращает общую стоимость всех товаров"""
        if type(other) is not type(self):
            raise TypeError("Нельзя складывать товары разных классов. ")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def name(self) -> str:
        """Геттер для названия продукта"""
        return self._name

    @property
    def description(self) -> str:
        """Геттер для описания продукта"""
        return self._description

    @property
    def price(self) -> float:
        """Геттер получения цены продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены продукта с проверкой на случай если цена равна или ниже нуля"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная. ")
            return

        if new_price > self.__price:
            self.__price = new_price
            print(f"Цена товара {self.name} успешно повышена до {new_price}. ")
            return

        if new_price < self.__price:
            while True:
                verification = input(
                    f"Цена товара {self.name} понижается с {self.__price} до {new_price}.\n"
                    f"Подтвердите понижение цены (y/n): "
                )

                if verification.lower() == "y":
                    self.__price = new_price
                    print(f"Цена товара {self.name} успешно изменена на {new_price}. ")
                    return
                elif verification.lower() == "n":
                    print(f"Изменение цены товара {self.name} отменено. ")
                    return
                else:
                    print("Некорректный ввод. Пожалуйста, введите 'y' для подтверждения или 'n' для отмены. ")

    @property
    def quantity(self) -> int:
        """Геттер для количества продукта"""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """Сеттер для количества продукта"""
        self._quantity = value

    @classmethod
    def new_product(cls, product_data: dict, product_list: Optional[list["BaseProduct"]] = None) -> "Product":
        """
        Класс-метод для создания нового продукта с проверкой дубликатов.

        Args:
            product_data: Словарь с данными продукта
            product_list: Список существующих продуктов для проверки дубликатов

        Returns:
            Product: Созданный или обновленный продукт
        """
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен. ")

        if product_list is not None:
            for existing_product in product_list:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    if price > existing_product.price:
                        existing_product.price = price
                    return cast(Product, existing_product)

        return cls(name, description, price, quantity)
