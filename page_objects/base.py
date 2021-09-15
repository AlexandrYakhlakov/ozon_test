from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys


class BasePage:
    KEY = {'esc': Keys.ESCAPE}

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def go_back(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh()

    def press_key(self, key):
        if key in self.KEY.keys():
            key = self.KEY[key]
        ActionChains(self.driver).key_down(key).key_up(key).perform()
