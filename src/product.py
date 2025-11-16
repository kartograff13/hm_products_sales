from typing import Optional


class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация продукта.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    @classmethod
    def new_product(cls, product_data: dict, product_list: Optional[list["Product"]] = None) -> "Product":
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

        if product_list is not None:
            for existing_product in product_list:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    if price > existing_product.price:
                        existing_product.price = price
                    return existing_product

        return cls(name, description, price, quantity)
