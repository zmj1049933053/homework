# Generated by Selenium IDE
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSearch():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_search(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.set_window_size(1024, 728)
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹")
        self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "su").click()
        element = self.driver.find_element(By.LINK_TEXT, "采购")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹 - 百度百科").click()
        self.vars["win6689"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win6689"])
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.close()

    def test_remote(self):
        self.opt = webdriver.ChromeOptions()
        self.opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=self.opt)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.driver.get_cookies()
        with open("data_cookie.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookies, f)

    def test_add_member(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("data_cookie.yaml", encoding="UTF-8") as f:
            data_yaml = yaml.safe_load(f)
        for cookie in data_yaml:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # 点击添加成员
        self.driver.find_elements_by_link_text("添加成员")[0].click()

        # 填写信息
        self.driver.find_element_by_id("username").send_keys("信小呆")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("呆呆")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("123456")
        self.driver.execute_script("$(\"[name='gender'][value=2]\").click()")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13012341234")
        self.driver.find_element_by_id("memberAdd_telephone").send_keys("027-123456")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("13012341234@163.com")
        self.driver.find_element_by_id("memberEdit_address").send_keys("湖北武汉")
        self.driver.find_element_by_id("memberAdd_title").send_keys("测试开发工程师")
        self.driver.execute_script("$(\"[name='extern_position_set'][value='custom']\").click()")
        self.driver.find_element_by_name("extern_position").send_keys("测试开发工程师")
        #保存信息
        self.driver.find_element_by_link_text("保存").click()
        sleep(5)
        #获取新增成员并断言
        new_member = self.driver.find_element(By.CSS_SELECTOR, "[title='信小呆']")
        assert new_member.text == "信小呆"