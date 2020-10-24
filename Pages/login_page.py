from Pages.base_page import BasePage
from Locators.login_locator import LoginPageLocators
import logging


class LoginPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.navigate_to("https://www.saucedemo.com/")
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def login(self, username, password):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, password)
    self.click(LoginPageLocators.BUTTON_LOGIN)

  def login_object(self, account):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, account.username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, account.password)
    self.click(LoginPageLocators.BUTTON_LOGIN)
