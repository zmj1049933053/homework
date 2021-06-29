import pytest

from test_selenium_20210627.po.main_page import MainPage


class TestAddDept:
    def setup(self):
        self.main_page = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("dept_name", [
        ("部门1"),
        ("部门2"),
        ("部门3")
    ])
    def test_add_dept(self, dept_name):
        results = self.main_page.goto_contact_page().goto_add_dept().edit_dept(dept_name).get_dept_names()
        assert dept_name in results
