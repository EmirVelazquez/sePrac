from selenium import webdriver
import time

# In Case you need to use different web drivers, it must be specified which browsers
# to use. Note: you alse need to install the webdriver for each browser.
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()


driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("100 page machine learning book")
driver.find_element_by_name("btnK").click()
time.sleep(4)
driver.quit()
