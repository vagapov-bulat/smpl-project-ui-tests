from playwright.sync_api import expect
from catalog_page import CatalogPage
from basket_page import BasketPage
from checkout_page_one import CheckoutPageOne
from checkout_page_two import CheckoutPageTwo
from catalog_steps import CatalogSteps
from checkout_steps import CheckoutSteps
from basket_steps import BasketSteps


def test_cart_checkout(auth_page):
    # Step Obj init
    catalog_steps = CatalogSteps(auth_page)
    basket_steps = BasketSteps(auth_page)
    checkout_steps = CheckoutSteps(auth_page)

    # 1. Проверяем, что мы на странице каталога
    expect(auth_page).to_have_url(CatalogPage.URL)

    # 2. Добавляем товары в корзину
    catalog_steps.add_to_cart("Sauce Labs Fleece Jacket")
    catalog_steps.add_to_cart("Sauce Labs Bolt T-Shirt")

    # 3. Переходим в корзину
    catalog_steps.go_to_cart_page()
    expect(auth_page).to_have_url(BasketPage.URL)

    # 4. Проверяем соответствие лежащих товаров с выбранными
    item_names = basket_steps.get_all_cart_items()
    assert "Sauce Labs Fleece Jacket" in item_names
    assert "Sauce Labs Bolt T-Shirt" in item_names

    # 5. Считаем сумму товаров в корзине
    prices_sum_from_cart = basket_steps.get_sum_all_price_item_from_cart()

    # 6. Переходим в Checkout
    basket_steps.open_checkout()
    expect(auth_page).to_have_url(CheckoutPageOne.URL)

    # 7. Заполняем поля и нажимаем Continue
    checkout_steps.enter_checkout("Ivan", "Ivanov", "440044")

    # Чекаем, что перешли на следующий шаг Чекаута
    expect(auth_page).to_have_url(CheckoutPageTwo.URL)

    # 8. Сравниваем Item Total с подсчитанной суммой
    item_total_text = checkout_steps.get_item_total_price_from_checkout()
    assert item_total_text == prices_sum_from_cart

    # Считаем сумму Tax
    tax_text = checkout_steps.get_sum_tax_from_checkout()

    # 9. Считаем итоговую сумму с учетом налога
    final_sum_price = tax_text + item_total_text

    # Выводим Total с страницы
    total_text = checkout_steps.get_sum_total_price_from_checkout()

    # 10. Сравниваем общую сумму (с налогом)
    assert final_sum_price == total_text

    # 11. Завершаем покупку и проверяем сообщение о завершении
    checkout_steps.click_finish_button()
    expect(auth_page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    thank_label = auth_page.locator(".complete-header", has_text="Thank you for your order!")
    expect(thank_label).to_be_visible()
