import allure

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    """Базовый Page."""

    def __init__(self, driver: webdriver, url: str):
        """Базовый driver и url."""
        self.driver = driver
        self.url = url

    def open(self):
        """Открыть браузер."""
        self.driver.get(self.url)

    @allure.step('Find a visible element')
    def element_is_visible(self, locator: str, timeout: int = 5) -> wait.mro():
        """Видимый элемент."""
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Find visible elements')
    def elements_are_visible(self, locator: str, timeout: int = 5) -> wait.mro():
        """Видимые элементы."""
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Find a present element')
    def element_is_present(self, locator: str, timeout: int = 5) -> wait.mro():
        """Не обязательно видимый элемент."""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Find present elements')
    def elements_are_present(self, locator: str, timeout: int = 5) -> wait.mro():
        """Не обязательно видимые элементы."""
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Find a not visible element')
    def element_is_not_visible(self, locator: str, timeout: int = 5) -> wait.mro():
        """Не видимый элемент."""
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Find clickable elements')
    def element_is_clickable(self, locator: str, timeout: int = 5) -> wait.mro():
        """Кликабельный элемент."""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Go to specified element')
    def go_to_element(self, element: str):
        """Переместиться к элементы."""
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Double click')
    def action_double_click(self, element: str):
        """Двойной клик."""
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step('Right click')
    def action_right_click(self, element: str):
        """Клик правой кнопкой мыши."""
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()
