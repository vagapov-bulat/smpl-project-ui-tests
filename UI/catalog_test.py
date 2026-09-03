from playwright.sync_api import expect
from tests.pages.login_page import LoginPage
from tests.pages.catalog_page import CatalogPage
from tests.steps.login_steps import LoginSteps
from tests.steps.catalog_steps import CatalogSteps

class TestCatalog:
    def test_catalog_count_product(self, auth_page):
        # Catalog Steps init
        catalog_steps = CatalogSteps(auth_page)
        # Проверяем URL
        expect(auth_page).to_have_url(CatalogPage.URL)

        # Считаем количество товаров на странице и проверяем
        product_count = catalog_steps.get_product_count()
        assert product_count == 6

    def test_sorted_by_name_a_z(self, auth_page):
        # Catalog Steps init
        catalog_steps = CatalogSteps(auth_page)
        # Проверяем URL
        expect(auth_page).to_have_url(CatalogPage.URL)

        # A-Z Sorting
        catalog_steps.sort_items_by("az")

        # Получаем списко названий товаров
        names = catalog_steps.get_product_names()

        # Проверяем, что список отсортирован по имени A-Z
        assert names == sorted(names)

    def test_sorted_by_name_z_a(self, auth_page):
        # Catalog Steps init
        catalog_steps = CatalogSteps(auth_page)
        # Проверяем URL
        expect(auth_page).to_have_url(CatalogPage.URL)

        # Z-A Sorting
        catalog_steps.sort_items_by("za")

        # Получаем списко названий товаров
        names = catalog_steps.get_product_names()

        # Проверяем, что список отсортирован по имени ZA
        assert names == sorted(names, reverse=True)

    def test_sort_by_prica_low_to_high(self, auth_page):
        # Catalog Steps init
        catalog_steps = CatalogSteps(auth_page)

        # LOHI Sorting
        catalog_steps.sort_items_by("lohi")

        # Получаем списко названий товаров
        prices = catalog_steps.get_product_names()

        # Проверяем, что список отсортирован по имени A-Z
        assert prices == sorted(prices)

    def test_sort_by_prica_high_to_low(self, auth_page):
        # Catalog Steps init
        catalog_steps = CatalogSteps(auth_page)

        # HILO Sorting
        catalog_steps.sort_items_by("hilo")

        # Получаем списко названий товаров
        prices = catalog_steps.get_product_names()

        assert prices == sorted(prices, reverse=True)

    def test_add_to_cart(self, auth_page):
        # Catalog Steps init
        catalog_steps = CatalogSteps(auth_page)

        # Добавляем товар в корзину
        button = catalog_steps.add_to_cart("Sauce Labs Onesie")

        # Проверка кнопки (смена текста)
        expect(button).to_have_text("Remove")

        # Проверка, что в корзине 1 товар
        assert catalog_steps.get_cart_count() == 1

    def test_add_to_cart_and_remove(self, auth_page):
        # Catalog Steps init
        catalog_steps = CatalogSteps(auth_page)

        # Добавляем товар в корзину
        button = catalog_steps.add_to_cart("Sauce Labs Onesie")

        # Проверка кнопки (смена текста)
        expect(button).to_have_text("Remove")

        # Проверка, что в корзине 1 товар
        assert catalog_steps.get_cart_count() == 1

        # Удаляем товар
        remove_button = catalog_steps.remove_from_cart("Sauce Labs Onesie")

        # Проверяем, что на кнопке сменилась надпись
        expect(remove_button).to_have_text("Add to cart")
        # Проверям, что корзина пустая
        assert catalog_steps.get_cart_count() == 0

    def test_product_dateails_onesie(self, auth_page):
        # Catalog Steps init
        catalog_steps = CatalogSteps(auth_page)

        # Сохраняем инфу о товаре
        name, price, detail_name, detail_price = catalog_steps.open_product_details("Sauce Labs Onesie")

        # Проверки
        assert name == detail_name
        assert price == detail_price
