from selenium.webdriver.common.by import By

from test_selenium_20210627.po.base_page import BasePage


class MainPage(BasePage):
    _CONTACT = (By.ID, "menu_contacts")

    def goto_contact_page(self):
        from test_selenium_20210627.po.contact_page import ContactPage
        self.find_and_click(*self._CONTACT)
        return ContactPage(self.driver)
