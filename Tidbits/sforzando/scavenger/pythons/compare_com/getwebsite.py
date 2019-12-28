import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
driver.quit()
