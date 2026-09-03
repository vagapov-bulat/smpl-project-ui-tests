import allure
from tests.pages.catalog_page import CatalogPage
from tests.pages.login_page import LoginPage
from playwright.sync_api import Page, expect

class CatalogSteps:

    def __init__(self, page: Page):
        self.page = page
        self.catalog_page = CatalogPage(self.page)

    # Открываем страницу каталога
    @allure.step("Открываем страницу каталога")
    def open_catalog_page(self):
        self.catalog_page.open()
        return self

    # Логаут
    @allure.step("Логаут")
    def logout(self):
        self.catalog_page.logout()

        # Проверяем, что вернулись на нужный URL и видна кнопка логина
        expect(self.page).to_have_url(LoginPage.URL)
        expect(self.page.locator("#login-button")).to_be_visible()
        return self

    # Сортировка
    @allure.step("Сортировка по фильтру")
    def sort_items_by(self, option:str):
        self.catalog_page.sort_catalog_items(option)
        return self

    # Работа с корзиной
    @allure.step("Переход на страницу корзины")
    def go_to_cart_page(self):
        self.catalog_page.open_cart()
        return self

    @allure.step("Добоавить товар в корзину")
    def add_to_cart(self, product_name:str):
        button = self.catalog_page.add_to_cart(product_name)
        return button

    @allure.step("Удалить товар из корзины")
    def remove_from_cart(self, product_name:str):
        button = self.catalog_page.remove_from_cart(product_name)
        return button

    @allure.step("Количество товаров в корзине")
    def get_cart_count(self) -> int:
        return self.catalog_page.get_cart_count()

    @allure.step("Счетчик товаров в бейдже корзины")
    def cart_badge(self):
        return self.catalog_page.cart_badge()

    # Работа с карточками товаров
    @allure.step("Получае количество карточек товаров в каталоге")
    def get_product_count(self) -> int:
        return self.catalog_page.get_product_count()

    @allure.step("Cбор названий всех товаров")
    def get_product_names(self) -> list[str]:
        return self.catalog_page.get_product_names()

    @allure.step("Получаем список цен товаров")
    def get_product_prices(self) -> list[float]:
        return self.catalog_page.get_product_prices()

    @allure.step("Открытие страницы деталей товаров по product_name")
    def open_product_details(self, product_name:str):
        return self.catalog_page.open_product_details(product_name)
