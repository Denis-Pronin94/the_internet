import allure

from pages.welcome_to_the_internet_page import AddAndRemoveElementsPage

from selenium import webdriver


@allure.suite('TestWelcomeToTheInternet')
class TestWelcomeToTheInternet:
    """Сьют - TestWelcomeToTheInternet."""

    @allure.title('Check add_and_remove_elements')
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
