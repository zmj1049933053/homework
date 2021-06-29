from selenium.webdriver.common.by import By

from test_selenium_20210627.po.base_page import BasePage


class DeptPage(BasePage):
    _DEPTNAME = (By.CSS_SELECTOR, '[name="name"]')
    _PARTYLIST = (By.CSS_SELECTOR, ".js_toggle_party_list")
    _SUBMIT = (By.CSS_SELECTOR, '#__dialog__MNDialog__ [d_ck="submit"]')
    _PARENTDEPT = (By.CSS_SELECTOR, ".qui_dropdownMenu .jstree-anchor", -1)

    def edit_dept(self, dept_name):
        from test_selenium_20210627.po.contact_page import ContactPage
        self.find_and_send_keys(*self._DEPTNAME, dept_name)
        self.find_and_click(*self._PARTYLIST)
        self.finds_and_click(*self._PARENTDEPT)
        self.find_and_click(*self._SUBMIT)
        return ContactPage(self.driver)
