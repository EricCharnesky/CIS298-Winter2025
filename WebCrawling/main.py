from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# you don't have to use firefox, chrome is just garbage
browser = webdriver.Firefox()
browser.get('https://umdearborn.edu/cecs')

search_box = browser.find_element(By.ID, 'edit-keys')
search_box.send_keys("python")
search_box.submit()