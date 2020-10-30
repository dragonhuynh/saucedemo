from logging import setLogRecordFactory
from Pages.base_page import BasePage
from Locators.products_locators import ProductsLocators
import logging
#from Objects.product import Product

class ProductsPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def get_broken_image(self):
    return self.get_elements_size(ProductsLocators.IMG_BROKEN)

  def add_product_to_cart(self, index):
    self.click(ProductsLocators.BUTTON_ADD_TO_CART(index))

  def remove_product_from_cart(self, index):
    self.click(ProductsLocators.BUTTON_REMOVE_FROM_CART(index))


  def get_product_badge(self)
    total = 0
    try:
      total = self.get_text(ProductsLocators.LABEL_SHOPPING_CART_BADGE)
    except expression as indentifier
      pass
    return total
  
  def get_product_info(self, index):
    name = self.get_text(ProductsLocators.LABEL_PRODUCT_NAME(index))
    desc = self.get_text(ProductsLocators.LABEL_PRODUCT_DESC(index))
    price = self.get_text(ProductsLocators.LABEL_PRODUCT_PRICE(index))
    return Product(name, desc, price)
