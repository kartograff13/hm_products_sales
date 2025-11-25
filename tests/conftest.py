from typing import Callable

import pytest
from _pytest.capture import CaptureResult

from src.base_product import BaseProduct
from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products() -> list[BaseProduct]:
    """Фикстура с тестовыми продуктами"""
    return [Product("Product 1", "Description 1", 123.45, 10), Product("Product 2", "Description 2", 678.9, 20)]


@pytest.fixture(autouse=True)
def reset_counters() -> None:
    """Фикстура автоматически сбрасывает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def capture_creation_logs(capsys: pytest.CaptureFixture) -> Callable[[], CaptureResult]:
    """Фикстура для перехвата логов создания объектов"""

    def _capture() -> CaptureResult:
        return capsys.readouterr()

    return _capture
