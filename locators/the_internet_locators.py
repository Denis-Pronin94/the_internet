from selenium.webdriver.common.by import By


class AddAndRemoveElementsLocators:
    """Локаторы для теста test_add_and_remove_elements."""

    ADD_ELEMENT_BUTTON = (By.XPATH, '//button[@onclick="addElement()"]')
    LIST_ELEMENTS = (By.XPATH, '//button[@class="added-manually"]')
    LAST_ELEMENT = (By.XPATH, '//button[@class="added-manually"][last()]')


class BasicAuthPageLocators:
    """Локаторы для теста test_basic_auth."""

    HEADER = (By.XPATH, '//div[@class="example"]/h3')
    TEXT = (By.XPATH, '//div[@class="example"]/p')


class CheckBoxesPageLocators:
    """Локаторы для теста test_basic_auth."""

    CHECK_BOX_1 = (By.XPATH, '//input[@type="checkbox"][1]')
    CHECK_BOX_2 = (By.XPATH, '//input[@type="checkbox"][2]')
    CHECK_BOX_ACTIVATE_1 = (By.XPATH, '//input[@checked=""][1]')
    CHECK_BOX_ACTIVATE_2 = (By.XPATH, '//input[@checked=""][2]')


class ContextMenuPageLocators:
    """Локаторы для теста test_context_menu."""

    BOX = (By.XPATH, '//div[@id="hot-spot"]')


class DigestAuthenticationPageLocators:
    """Локаторы для теста test_digest_authentication."""

    HEADER = (By.XPATH, '//div[@class="example"]/h3')
    TEXT = (By.XPATH, '//div[@class="example"]/p')


class DropdownListPageLocators:
    """Локаторы для теста test_dropdown_list."""

    LIST = (By.XPATH, '//select[@id="dropdown"]')
    DEFAULT_TEXT = (By.XPATH, '//option[@selected="selected"]')
    OPTION_1 = (By.XPATH, '//option[@value="1"]')
    OPTION_2 = (By.XPATH, '//option[@value="2"]')


class DynamicallyLoadedPageLocators:
    """Локаторы для теста test_dynamically_loaded."""

    EXAMPLE_1 = (By.XPATH, '//a[@href="/dynamic_loading/1"]')
    START_BUTTON = (By.XPATH, '//div[@id="start"]/button')
    FINISH = (By.XPATH, '//div[@id="finish"]')
    EXAMPLE_2 = (By.XPATH, '//a[@href="/dynamic_loading/2"]')
