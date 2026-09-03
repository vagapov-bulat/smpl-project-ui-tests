from playwright.sync_api import expect
from tests.pages.catalog_page import CatalogPage
from tests.steps.login_steps import LoginSteps
from tests.steps.catalog_steps import CatalogSteps

class TestLogin():
    def test_auth_login_standart_user(self, page):
        # LoginSteps инициализация
        login_steps = LoginSteps(page)
        catalog_steps = CatalogSteps(page)

        # Открываем страницу для логина и Вводим данные для авторизации
        login_steps.open_login_page().login("standard_user", "secret_sauce")
        expect(page).to_have_url(CatalogPage.URL)

        # Разлогиниваемся
        catalog_steps.logout()

    def test_auth_logout_visual_user(self, page: Page):
        # LoginSteps инициализация
        login_steps = LoginSteps(page)
        catalog_steps = CatalogSteps(page)

        # Открываем страницу для логина и Вводим данные для авторизации
        login_steps.open_login_page().login("visual_user", "secret_sauce")
        expect(page).to_have_url(CatalogPage.URL)

        # Разлогиниваемся
        catalog_steps.logout()

    def test_auth_logout_locked_out_user(self, page:Page):
        # LoginSteps инициализация
        login_steps = LoginSteps(page)

        # Открываем страницу для логина и Вводим данные для авторизации
        login_steps.open_login_page().login("locked_out_user", "secret_sauce")

        error = login_steps.get_error_text()
        assert "locked" in error


