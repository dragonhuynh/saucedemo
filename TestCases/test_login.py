import sys

sys.path.append(".")
import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from TestCases.base_test import BaseTest
from Pages.products_page import ProductsPage
from Objects.account import Account


class saucedemo(BaseTest):
    """A sample test class to show how page object works"""

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_login_successfully_standard(self):
        login_page = LoginPage(self.driver)
        
        account = Account("standard_user", "secret_sauce")
        login_page.login_object(account)

    def test_login_successfully_locked(self):
        login_page = LoginPage(self.driver)
        account = Account("locked_out_user", "secret_sauce")
        login_page.login_object(account)
        print()

    def test_login_successfully_problem(self):
        login_page = LoginPage(self.driver)
        login_page.login("problem_user", "secret_sauce")
        products_page = ProductsPage(self.driver)
        print(products_page.get_broken_image())
        account = Account("problem_user", "secret_sauce")
        login_page.login_object(account)

    def test_login_successfully_performance(self):
        login_page = LoginPage(self.driver)
        account = Account("performance_glitch_user", "secret_sauce")
        login_page.login_object(account)

    #     print(result_page.get_message())
    #     self.assertIn("You logged into a secure area!", result_page.get_message())


if __name__ == "__main__":
    unittest.main()
