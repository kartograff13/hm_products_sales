class ZeroQuantityError(Exception):
    """Класс для исключения товаров с нулевым количеством"""

    def __init__(self, message: str = "Нельзя добавить товар с нулевым количеством") -> None:
        self.message = message
        super().__init__(self.message)
