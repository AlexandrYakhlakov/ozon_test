from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


class Element:

    driver: WebDriver = None

    def __init__(self, selector):
        self.selector = selector

    @classmethod
    def set_driver(cls, driver):
        cls.driver = driver

    def __elements(self):
        selector = self.selector
        if 'id' in selector.keys():
            by = By.ID
            self.selector = selector['id']
        elif 'class_name' in selector.keys():
            by = By.CLASS_NAME
            self.selector = selector['class_name']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            self.selector = selector['xpath']
        return self.driver.find_elements(by=by, value=self.selector)

    def click(self, index=0):
        element = self.__elements()[index]
        element.click()

    def send_keys(self, value, index=0):
        element = self.__elements()[index]
        element.clear()
        element.send_keys(value)

    def move_to_element(self, index=0):
        element = self.__elements()[index]
        actions = ActionChains(self.driver)
        actions.move_to_element(to_element=element)
        actions.perform()

    def element_is_displayed(self, index=0):
        return self.__elements()[index].is_displayed()

    def get_text(self, index=0):
        return self.__elements()[index].text