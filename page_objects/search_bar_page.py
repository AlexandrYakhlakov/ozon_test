from .base import BasePage
from locators import Header


class SearchBarPage(BasePage):
    def click_search_bar(self):
        self._click(selector=Header.search_bar.input_search)

    def input_search_bar(self, search):
        self._send_keys(selector=Header.search_bar.input_search, value=search)

    def clear_search_bar(self):
        self._click(selector=Header.search_bar.clear_search)
        return self.get_text()

    def select_search_category(self, category: str):
        self._click(selector=Header.search_bar.select_category)
        i = 0
        selector_category = Header.search_bar.category_items
        while True:
            text = self.get_text(selector=selector_category,index=i)
            print(text)
            if text == category:
                self._click(selector_category, index=i)
                break
            i += 1

    def type_category(self):
        return self.get_text(selector=Header.search_bar.selected_category)

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(15)
# page = SearchBarPage(driver)
# page.get('https://ozon.ru')
# page.select_search_category('Книги')