from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# In Case you need to use different web drivers, it must be specified which browsers
# to use. Note: you alse need to install the webdriver for each browser.
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()


driver.set_page_load_timeout(5)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("100 page machine learning book")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)

# Here we can place the current url and store it in a variable to be used later
browser_url = driver.current_url
print(browser_url)
print("Test Ran Successfully")

# Close the window and stop the test here
driver.quit()
