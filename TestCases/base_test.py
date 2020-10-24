import os
import sys
import unittest
from selenium import webdriver
#from TestData.TestData import TestData

sys.path.append(".")


# Base Class for the tests
class BaseTest(unittest.TestCase):

  @classmethod
  def setUp(self):
    # Setting up how we want Chrome to run
    self.driver = webdriver.Chrome(executable_path=r'C:\Users\longh\OneDrive\File_tong_hop\Documents\GitHub\saucedemo\Drivers\chromedriver.exe')
    self.driver.maximize_window()
   
  @classmethod
  def tearDown(self):
    # To do the cleanup after test has executed.
    self.driver.close()
    try:
      self.driver.quit()
    except Exception as e:
      pass
