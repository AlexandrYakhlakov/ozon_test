from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # self.driver.get(url)

    def get(self, url):
        self.driver.get(url)

    def go_back(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh()

    def get_text(self, selector, index=0):
        element = self._element(selector, index)
        return element.text

    def _element(self, selector: dict, index: int):
        if 'id' in selector.keys():
            by = By.ID
            selector = selector['id']
        elif 'class_name' in selector.keys():
            by = By.CLASS_NAME
            selector = selector['class_name']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        return self.driver.find_elements(by=by, value=selector)[index]

    def _click(self, selector, index=0):
        element = self._element(selector, index)
        element.click()

    def _send_keys(self, selector, value, index=0):
        element = self._element(selector, index)
        element.clear()
        element.send_keys(value)

    def _move_to_element(self, selector, index=0):
        element = self._element(selector, index)
        actions = ActionChains(self.driver)
        actions.move_to_element(to_element=element)
        actions.perform()
