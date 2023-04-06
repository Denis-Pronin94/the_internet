import random

import allure

from locators.the_internet_locators import AddAndRemoveElementsLocators, BasicAuthPageLocators

from pages.base_page import BasePage

from selenium.common import TimeoutException


class AddAndRemoveElementsPage(BasePage):
    """AddAndRemoveElementsPage."""

    locators = AddAndRemoveElementsLocators()

    @allure.step("Добавление елементов")
    def add_elements(self) -> tuple:
        """Добавляем и возвращаем кол-во елементов."""
        with allure.step('Добавляем рандомное кол-во елементов.'):
            random_number = random.randint(1, 100)
            item_click = 0
            while item_click < random_number:
                self.element_is_visible(self.locators.ADD_ELEMENT_BUTTON).click()
                item_click = item_click + 1
            list_elements = self.elements_are_present(self.locators.LIST_ELEMENTS)
        with allure.step('Возвращаем кол-во елементов.'):
            return item_click, len(list_elements)

    @allure.step("Удаление элементов.")
    def remove_elements(self) -> bool:
        """Удаляем все элементы и проверяем их отсутствие."""
        with allure.step('Удаляем все элементы и проверяем их отсутствие.'):
            list_elements = self.elements_are_present(self.locators.LIST_ELEMENTS)
            item_remove_click = 0
            try:
                while item_remove_click <= len(list_elements):
                    self.element_is_visible(self.locators.LAST_ELEMENT).click()
                    item_remove_click = item_remove_click + 1
                self.element_is_present(self.locators.LIST_ELEMENTS)
            except TimeoutException:
                return False
            return True


class BasicAuthPage(BasePage):
    """BasicAuthPage."""

    locators = BasicAuthPageLocators()

    @allure.step("Возвращаем текст успешной авторизации.")
    def return_text_auth(self) -> tuple:
        """Возвращаем текст успешной авторизации."""
        with allure.step('Возвращаем header.'):
            header = self.element_is_present(self.locators.HEADER).text
        with allure.step('Возвращаем text.'):
            text = self.element_is_present(self.locators.TEXT).text
        return header, text
