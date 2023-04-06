import allure

from config import NAME, PASSWORD

from pages.the_internet_page import (
    AddAndRemoveElementsPage,
    BasicAuthPage,
    CheckBoxesPage,
    ContextMenuPage,
    DigestAuthenticationPage,
)

from selenium import webdriver


@allure.suite('TestWelcomeToTheInternet.')
class TestWelcomeToTheInternet:
    """Сьют - TestWelcomeToTheInternet."""

    @allure.title('Check add_and_remove_elements.')
    def test_add_and_remove_elements(self, driver: webdriver):
        """Тест - добавление и удаление елемента."""
        add_and_remove_elements = AddAndRemoveElementsPage(
            driver,
            'http://the-internet.herokuapp.com/add_remove_elements/',
        )
        add_and_remove_elements.open()
        item_click, list_elements = add_and_remove_elements.add_elements()
        list_elements_after = add_and_remove_elements.remove_elements()
        assert item_click == list_elements
        assert list_elements_after is False

    @allure.title('Check basic_auth.')
    def test_basic_auth(self, driver: webdriver):
        """Тест - авторизация."""
        basic_auth = BasicAuthPage(
            driver,
            f'http://{NAME}:{PASSWORD}@the-internet.herokuapp.com/basic_auth',
        )
        basic_auth.open()
        header, text = basic_auth.return_text_auth()
        assert header == 'Basic Auth'
        assert text == 'Congratulations! You must have the proper credentials.'

    @allure.title('Check сheck_boxes.')
    def test_check_boxes(self, driver: webdriver):
        """Тест - проверка чек-боксов."""
        check_boxes = CheckBoxesPage(
            driver,
            'http://the-internet.herokuapp.com/checkboxes',
        )
        check_boxes.open()
        check_box_1 = check_boxes.check_box_1()
        check_box_2 = check_boxes.check_box_2()
        assert check_box_1 is True
        assert check_box_2 is False

    @allure.title('Check context_menu.')
    def test_context_menu(self, driver: webdriver):
        """Тест - проверка чек-боксов."""
        context_menu = ContextMenuPage(
            driver,
            'http://the-internet.herokuapp.com/context_menu',
        )
        context_menu.open()
        alert_text = context_menu.right_click()
        assert alert_text == 'You selected a context menu'
        context_menu.close_alert()

    @allure.title('Check digest_authentication.')
    def test_digest_authentication(self, driver: webdriver):
        """Тест - авторизация."""
        digest_authentication = DigestAuthenticationPage(
            driver,
            f'http://{NAME}:{PASSWORD}@the-internet.herokuapp.com/digest_auth',
        )
        digest_authentication.open()
        header, text = digest_authentication.return_text_auth()
        assert header == 'Digest Auth'
        assert text == 'Congratulations! You must have the proper credentials.'
