from src.product import Product


class Smartphone(Product):
    """Класс-наследник класса Product для представления продукта смартфон"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализация продукта.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество в наличии
            efficiency: Производительность
            model: Модель
            memory: Объём встроенной памяти
            color: Цвет
        """
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта Smartphone"""
        return (
            f"Smartphone('{self.name}', '{self.description}', {self.price}, "
            f"{self.quantity}, {self.efficiency}, '{self.model}', {self.memory}, '{self.color}')"
        )
