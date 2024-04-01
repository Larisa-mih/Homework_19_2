from django.core.management import BaseCommand
from catalog.models import Category, Product, Contacts
import json
from django.db import connection

from config.settings import BASE_DIR


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(f"{BASE_DIR}/fixtures/catalog_data.json", encoding="UTF-8") as f:
            data = json.load(f)
        list_categories = []
        for category in data:
            if 'category' in category['model']:
                list_categories.append(category)
        return list_categories

    @staticmethod
    def json_read_products():
        with open(f"{BASE_DIR}/fixtures/catalog_data.json", encoding="UTF-8") as f:
            data = json.load(f)
        list_products = []
        for product in data:
            if 'product' in product['model']:
                list_products.append(product)
        return list_products

    @staticmethod
    def json_read_contacts():
        with open(f"{BASE_DIR}/fixtures/catalog_data.json", encoding="UTF-8") as f:
            data = json.load(f)
        list_contacts = []
        for contacts in data:
            if 'contacts' in contacts['model']:
                list_contacts.append(contacts)
        return list_contacts

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()
        Contacts.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE catalog_category, catalog_product, catalog_contacts RESTART IDENTITY CASCADE;")


        product_for_create = []
        category_for_create = []
        contact_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
            Category(id=category['pk'],
                     name=category["fields"]["name"],
                     description=category["fields"]["description"])
        )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
            Product(id=product['pk'],
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    image=product["fields"]["image"],
                    category=Category.objects.get(pk=product["fields"]["category"]),
                    price=product["fields"]["price"],
                    created_at=product["fields"]["created_at"],
                    updated_at=product["fields"]["updated_at"])
            )

        Product.objects.bulk_create(product_for_create)

        for contact in Command.json_read_contacts():
            contact_for_create.append(
            Contacts(id=contact['pk'],
                     first_name=contact["fields"]["first_name"],
                     last_name=contact["fields"]["last_name"],
                     email=contact["fields"]["email"])
            )

        Contacts.objects.bulk_create(contact_for_create)
