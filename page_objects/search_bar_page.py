from page_objects.base import BasePage
from page_objects.element import Element
from locators import Header


class SearchBarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        Element.set_driver(driver)

    search_bar = Element(Header.search_bar.search_bar)
    clear_search_bar = Element(Header.search_bar.clear_search)
    search_button = Element(Header.search_bar.search_button)
    search_suggestions = Element(Header.search_bar.search_suggestions_popup)
