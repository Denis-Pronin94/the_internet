from selenium.webdriver.common.by import By


class AddAndRemoveElementsLocators:
    """Локаторы для теста test_add_and_remove_elements."""

    ADD_ELEMENT_BUTTON = (By.XPATH, '//button[@onclick="addElement()"]')
    LIST_ELEMENTS = (By.XPATH, '//button[@class="added-manually"]')
    LAST_ELEMENT = (By.XPATH, '//button[@class="added-manually"][last()]')
