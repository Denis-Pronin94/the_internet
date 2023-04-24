import random

import allure

from locators.the_internet_locators import (
    AddAndRemoveElementsLocators,
    BasicAuthPageLocators,
    CheckBoxesPageLocators,
    ContextMenuPageLocators,
    DigestAuthenticationPageLocators,
    DropdownListPageLocators,
    DynamicallyLoadedPageLocators,
)

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


class CheckBoxesPage(BasePage):
    """CheckboxesPage."""

    locators = CheckBoxesPageLocators()

    @allure.step("Кликаем на 1-ый чек-бокс и возвращаем его статус.")
    def check_box_1(self) -> bool:
        """Кликаем на 1-ый чек-бокс и возвращаем его статус."""
        self.element_is_visible(self.locators.CHECK_BOX_1).click()
        try:
            self.element_is_present(self.locators.CHECK_BOX_ACTIVATE_1)
        except TimeoutException:
            return False
        return True

    @allure.step("Кликаем на 2-ой чек-бокс и возвращаем его статус.")
    def check_box_2(self) -> bool:
        """Кликаем на 2-ой чек-бокс и возвращаем его статус."""
        self.element_is_visible(self.locators.CHECK_BOX_2).click()
        try:
            self.element_is_present(self.locators.CHECK_BOX_ACTIVATE_2)
        except TimeoutException:
            return False
        return True


class ContextMenuPage(BasePage):
    """ContextMenuPage."""

    locators = ContextMenuPageLocators()

    @allure.step("Кликаем правой кнопкой мыши и возвращаем текст алерта.")
    def right_click(self) -> str:
        """Кликаем правой кнопкой мыши и возвращаем текст алерта."""
        self.action_right_click(self.element_is_visible(self.locators.BOX))
        alert_text = self.driver.switch_to.alert
        return alert_text.text

    @allure.step("Закрываем алерт.")
    def close_alert(self):
        """Закрываем алерт."""
        self.driver.switch_to.alert.accept()


class DigestAuthenticationPage(BasePage):
    """BasicAuthPage."""

    locators = DigestAuthenticationPageLocators()

    @allure.step("Возвращаем текст успешной авторизации.")
    def return_text_auth(self) -> tuple:
        """Возвращаем текст успешной авторизации."""
        with allure.step('Возвращаем header.'):
            header = self.element_is_present(self.locators.HEADER).text
        with allure.step('Возвращаем text.'):
            text = self.element_is_present(self.locators.TEXT).text
        return header, text


class DropdownListPage(BasePage):
    """DragAndDropPage."""

    locators = DropdownListPageLocators()

    def dropdown(self) -> tuple:
        """Возвращаем текст всех строк дропдауна."""
        default_text = self.element_is_visible(self.locators.DEFAULT_TEXT)
        self.element_is_visible(self.locators.LIST).click()
        self.element_is_visible(self.locators.OPTION_1).click()
        value_1 = self.element_is_visible(self.locators.OPTION_1)
        self.element_is_visible(self.locators.LIST).click()
        self.element_is_visible(self.locators.OPTION_2).click()
        value_2 = self.element_is_visible(self.locators.OPTION_2)
        return default_text.text, value_1.text, value_2.text


class DynamicallyLoadedPage(BasePage):
    """DynamicallyLoadedPage."""

    locators = DynamicallyLoadedPageLocators()

    def example_1(self) -> str:
        """Возвращаем текст первого примера."""
        self.element_is_visible(self.locators.EXAMPLE_1).click()
        self.element_is_visible(self.locators.START_BUTTON).click()
        text_example_1 = self.element_is_visible(self.locators.FINISH)
        return text_example_1.text

    def example_2(self) -> str:
        """Возвращаем текст второго примера."""
        self.element_is_visible(self.locators.EXAMPLE_2).click()
        self.element_is_visible(self.locators.START_BUTTON).click()
        text_example_2 = self.element_is_present(self.locators.FINISH)
        return text_example_2.text
