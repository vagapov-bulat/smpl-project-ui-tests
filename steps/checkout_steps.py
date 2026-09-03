import allure
from tests.pages.checkout_page_two import CheckoutPageTwo
from tests.pages.checkout_page_one import CheckoutPageOne
from tests.pages.login_page import LoginPage
from playwright.sync_api import Page, expect

class CheckoutSteps:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_page_one = CheckoutPageOne(self.page)
        self.checkout_page_two = CheckoutPageTwo(self.page)

    # Метод заполняет поля и сжем кнопку "Continue"
    @allure.step("Заполняем поля и нажимаем Continue")
    def enter_checkout(self, first_name:str, last_name:str, zip_code:str):
        self.checkout_page_one.enter_checkout(first_name, last_name, zip_code)
        return self

    @allure.step("Считаем сумму товаров поля Item total")
    def get_item_total_price_from_checkout(self):
        return self.checkout_page_two.get_item_total_price_from_checkout()

    @allure.step("Получаем сумму товаров поля Tax")
    def get_sum_tax_from_checkout(self):
        return self.checkout_page_two.get_sum_tax_from_checkout()

    @allure.step("Получаем сумму товаров поля Total")
    def get_sum_total_price_from_checkout(self):
        return self.checkout_page_two.get_sum_total_price_from_checkout()

    @allure.step("Нажимает кнопку Finish")
    def click_finish_button(self):
        self.checkout_page_two.click_finish_button()
        return self
