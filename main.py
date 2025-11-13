import json

from src.category import Category
from src.product import Product


def load_data_from_json(file_path: str) -> list[Category]:
    """
    Загружает данные о категориях и товарах из JSON файла и создает объекты классов.

    Args:
        file_path: Путь к JSON файлу с данными

    Returns:
        list[Category]: Список объектов категорий с товарами
    """
    categories = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        for category_data in data:
            products = []
            for product_data in category_data["products"]:
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)

            category = Category(
                name=category_data["name"], description=category_data["description"], products=products
            )
            categories.append(category)

    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
    except KeyError as e:
        print(f"Ошибка: Неверная структура JSON файла - отсутствует ключ {e}")
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный JSON в файле {file_path}")
    except Exception as e:
        print(f"Неизвестная ошибка при загрузке данных: {e}")

    return categories


def print_category_info(category: Category) -> None:
    """
    Выводит информацию о категории и ее товарах.

    Args:
        category: Объект категории для вывода информации
    """
    print(f"\n--- Категория: {category.name} ---")
    print(f"Описание: {category.description}")
    print(f"Количество товаров: {category.get_products_count()}")
    print("Товары:")
    for product in category.products:
        print(f"  - {product.name}: {product.price} руб. (остаток: {product.quantity} шт.)")


def main() -> None:
    """Основная функция программы"""
    categories = load_data_from_json("data/products.json")

    if categories:
        print("Данные успешно загружены из JSON файла!")
        print("=" * 50)

        for category in categories:
            print_category_info(category)

        print("\n" + "=" * 50)
        print("ОБЩАЯ СТАТИСТИКА:")
        print(f"Всего категорий: {Category.category_count}")
        print(f"Всего товаров: {Category.product_count}")

    else:
        print("Не удалось загрузить данные из JSON. Используем тестовые данные.")
        print("=" * 50)

        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        print("Информация о продуктах:")
        for product in [product1, product2, product3]:
            print(f"{product.name}: {product.price} руб., остаток: {product.quantity} шт.")

        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3],
        )

        product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
        category2 = Category(
            "Телевизоры",
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            [product4],
        )

        print("\n" + "=" * 50)
        for category in [category1, category2]:
            print_category_info(category)

        print("\n" + "=" * 50)
        print("ОБЩАЯ СТАТИСТИКА:")
        print(f"Всего категорий: {Category.category_count}")
        print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
