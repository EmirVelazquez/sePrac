# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNyTimes():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_nyTimes(self):
    # Test name: nyTimes
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.nytimes.com/")
    # 2 | setWindowSize | 515x218 | 
    self.driver.set_window_size(515, 218)
    # 3 | runScript | window.scrollTo(0,5.599999904632568) | 
    self.driver.execute_script("window.scrollTo(0,5.599999904632568)")
    # 4 | click | linkText=U.S. | 
    self.driver.find_element(By.LINK_TEXT, "U.S.").click()
    # 5 | runScript | window.scrollTo(0,784) | 
    self.driver.execute_script("window.scrollTo(0,784)")
    # 6 | runScript | window.scrollTo(0,1072.800048828125) | 
    self.driver.execute_script("window.scrollTo(0,1072.800048828125)")
    # 7 | runScript | window.scrollTo(0,1332) | 
    self.driver.execute_script("window.scrollTo(0,1332)")
    # 8 | click | css=.css-6n7j50:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-6n7j50:nth-child(2)").click()
    # 9 | type | id=search-tab-input | economy
    self.driver.find_element(By.ID, "search-tab-input").send_keys("economy")
    # 10 | runScript | window.scrollTo(0,1516.800048828125) | 
    self.driver.execute_script("window.scrollTo(0,1516.800048828125)")
  