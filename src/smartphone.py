from src.product import Product


class Smartphone(Product):
    """Класс-наследник класса Product для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str) -> None:
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
            color: цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

