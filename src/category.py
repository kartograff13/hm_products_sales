from typing import TYPE_CHECKING

from src.base_product import BaseProduct
from src.product_container import ProductContainer
from src.zero_quantity_error import ZeroQuantityError

if TYPE_CHECKING:
    from src.category_iterator import CategoryIterator


class Category(ProductContainer):
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
        return f"{self.name}, количество продуктов: {self.total_quantity} шт."

    def __iter__(self) -> "CategoryIterator":
        """
        Возвращает итератор для перебора товаров в категории.

        Returns:
            Объект CategoryIterator
        """
        from src.category_iterator import CategoryIterator

        return CategoryIterator(self)

    @property
    def products(self) -> list[BaseProduct]:
        """Свойство для получения списка объектов продуктов"""
        return self.__products

    @property
    def total_quantity(self) -> int:
        """Общее количество товаров в категории"""
        return sum(product.quantity for product in self.__products)

    @property
    def total_cost(self) -> float:
        """Общая стоимость всех товаров в категории"""
        return sum(product.price * product.quantity for product in self.__products)

    def add_product(self, product: BaseProduct) -> None:
        """
        Добавления товара в категорию.

        Args:
            product: Объект товара для добавления

        Raises:
            TypeError: Если product не является экземпляром Product или его подклассов
            ZeroQuantityError: Если количество товара равно нулю
        """
        try:
            if not isinstance(product, BaseProduct) or not issubclass(type(product), BaseProduct):
                raise TypeError("Можно добавлять только объекты класса Product или его наследников")

            if product.quantity == 0:
                raise ZeroQuantityError(
                    f"Товар '{product.name}' имеет нулевое количество и не может быть добавлен в категорию"
                )

            self.__products.append(product)
            Category.product_count += 1
            print(f"Товар '{product.name}' успешно добавлен в категорию '{self.name}'")
        except (TypeError, ZeroQuantityError) as e:
            print(f"Ошибка при добавлении товара: {e}")
            raise
        finally:
            print("Обработка добавления товара в категорию завершена")

    def get_products_count(self) -> int:
        """Метод для получения количества товаров в категории"""
        return len(self.__products)

    @property
    def get_products_info(self) -> list[str]:
        """Геттер для получения списка товаров в list[str]"""
        return [str(product) + "\n" for product in self.__products]

    def get_products_objects(self) -> list[BaseProduct]:
        """Возвращает список объектов (продуктов) для проверки дубликатов"""
        return self.__products

    def middle_price(self) -> float:
        """
        Рассчитывает среднюю цену товаров в категории.

        Returns:
            Средняя цена товаров в категории. Если в категории нет товаров, возвращает 0.
        """
        try:
            return self.total_cost / self.total_quantity
        except ZeroDivisionError:
            return 0.0
