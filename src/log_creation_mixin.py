from typing import Any


class LogCreationMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация с логированием создания объекта"""
        super().__init__(*args, **kwargs)
        print(f"Создан объект: {self!r}")

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта"""
        class_name = self.__class__.__name__

        params = []
        for param_name in dir(self):
            if param_name.startswith("_"):
                continue

            try:
                value = getattr(self, param_name)
                if callable(value):
                    continue
            except AttributeError:
                continue

            if isinstance(value, str):
                params.append(f"'{value}'")
            else:
                params.append(str(value))

        return f"{class_name}({', '.join(params)})"
