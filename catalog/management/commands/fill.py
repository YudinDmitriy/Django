import json
from django.core.management import BaseCommand
from catalog.models import Product, Categories


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        categories = []
        with open("catalog_categories_data.json", encoding='utf-16') as f:
            # file_content = f.read()
            templates = json.load(f)
        for i in templates:
            category = i['fields']
            categories.append(category)
        return categories

    @staticmethod
    def json_read_products():
        products = []
        with open("catalog_product_data.json", encoding='utf-16') as f:
            # file_content = f.read()
            templates = json.load(f)
        for i in templates:
            product = i['fields']
            products.append(product)
        return products

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Categories.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []


        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Categories(category_name=category['category_name'], description=category['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Categories.objects.bulk_create(category_for_create)


        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(product_name=product['product_name'], description=product['description'],
                        product_image=product['product_image'],
                        category=Categories.objects.get(pk=product['category']), unit_price=product['unit_price'],
                        created_at=product['created_at'], updated_at=product['updated_at'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)