from time import sleep

from selenium.webdriver.common.by import By

from test_selenium_20210627.po.base_page import BasePage


class ContactPage(BasePage):
    _ADDDEPTBTN = (By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap")
    _CREATEBTN = (By.CSS_SELECTOR, ".js_create_party")
    _DEPTNAMES = (By.CSS_SELECTOR, ".member_colLeft_bottom .jstree-anchor")
    def goto_add_dept(self):
        from test_selenium_20210627.po.dept_page import DeptPage
        self.find_and_click(*self._ADDDEPTBTN)
        self.find_and_click(*self._CREATEBTN)
        return DeptPage(self.driver)

    def get_dept_names(self):
        sleep(1)
        dept_names = []
        elements = self.finds(*self._DEPTNAMES)
        for element in elements:
            dept_names.append(element.get_attribute("text"))
        print(dept_names)
        return dept_names
