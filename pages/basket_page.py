from playwright.sync_api import Page

class BasketPage():
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        self.page = page

        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.cart_list = page.locator(".cart_list")
        self.cart_items = page.locator(".cart_item")
        self.button_checkout = page.locator('#checkout')
        self.price_items = page.locator(".inventory_item_price")

    def open_cart(self):
        self.page.goto(self.URL)

    # Возвращает товар по его названию
    def get_item_name(self, product_name:str):
        return self.item_name.filter(has_text=product_name)

    # Возваорщает названия всех товаров в корзине
    def get_all_cart_items(self):
        return self.item_name.all_inner_texts()

    # Принимает название товара и удаляет его из корзины
    def remove_item_from_cart(self, product_name:str):
        card = self.cart_items.filter(has_text=product_name)
        button = card.locator("button")
        if button.inner_text() == "Remove":
            button.click()
        return button

    # Возвращает сумму всех товаров в корзине
    def get_sum_all_price_item_from_cart(self):
        prices_text = self.price_items.all_text_contents()
        prices = [float(p.replace("$", "")) for p in prices_text]
        price_sum = sum(prices)
        return price_sum

    # Переход в чекаут
    def open_checkout(self):
        self.button_checkout.click()
