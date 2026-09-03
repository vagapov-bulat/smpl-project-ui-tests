import allure
from pages.basket_page import BasketPage
from playwright.sync_api import Page, expect

class BasketSteps:
    def __init__(self, page:Page):
        self.page = page
        self.basket_page = BasketPage(self.page)

    # Открываем страницу корзины
    @allure.step("Открываем страницу корзины")
    def open_basket_page(self):
        self.basket_page.open_cart()
        return self

    # Получаем товар по его названию
    def get_item_name(self, product_name:str):
        return self.basket_page.get_item_name(product_name)

    # Получаем Названия всех товаров в корзине
    def get_all_cart_items(self):
        return self.basket_page.get_all_cart_items()

    # Принимаем название товара и удаляем его из корзины
    def remove_item_from_cart(self, product_name:str):
        return self.basket_page.remove_item_from_cart(product_name)

    # Получаем сумму всех товаров в корзине
    def get_sum_all_price_item_from_cart(self):
        return self.basket_page.get_sum_all_price_item_from_cart()

    # Переход на страницу Чекаута
    def open_checkout(self):
        self.basket_page.open_checkout()
        return self
