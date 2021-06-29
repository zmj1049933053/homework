from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver_name: WebDriver = None):
        if driver_name is None:
            ops = webdriver.ChromeOptions()
            ops.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=ops)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(2)
        else:
            self.driver = driver_name

    def find(self, location, element):
        return self.driver.find_element(location, element)

    def finds(self, location, element):
        return self.driver.find_elements(location, element)

    def find_and_click(self, location, element):
        return self.driver.find_element(location, element).click()

    def find_and_send_keys(self, location, element, value):
        return self.driver.find_element(location, element).send_keys(value)

    def finds_and_click(self, location, element, index):
        return self.driver.find_elements(location,element)[index].click()
