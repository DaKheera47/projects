# setup selenium with firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import time
import os
from datetime import datetime, timedelta
import argparse
import sys


email = "admin"
password = "a3922"
# clear console


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def resetFrame(driver, newFrame, sleep=3):
    time.sleep(sleep)
    driver.switch_to.default_content()
    # driver.switch_to.frame(driver.find_element(by=By.ID, value=newFrame))
    xpath = f"//frame[@name='{newFrame}']"
    print(driver.find_element(by=By.XPATH, value=xpath).text)
    driver.switch_to.frame(driver.find_element(by=By.XPATH, value=xpath))


t1 = time.perf_counter()

options = Options()
options.headless = False
driver = webdriver.Firefox(
    options=options, service=Service("./geckodriver.exe"))

driver.set_page_load_timeout(120)
driver.implicitly_wait(120)

# webdriver setup
driver.get("http://192.168.10.1")


# email field
driver.find_elements(by=By.CSS_SELECTOR,
                     value="input.form_input")[0].send_keys(email)
driver.find_elements(by=By.CSS_SELECTOR,
                     value="input.form_input")[1].send_keys(password)

# sign in button
xpath = "input.button"
driver.find_element(by=By.CSS_SELECTOR, value=xpath).click()

time.sleep(3)
resetFrame(driver, "menufrm")
# a tag contains text
# a tag href

xpath = "//a[contains(text(),'Management')]"
# xpath = "//a[href='backupsettings.html']"
while True:
    try:
        # status = driver.find_element(by=By.CSS_SELECTOR, value=cls)
        ele = driver.find_elements(by=By.TAG_NAME, value="a")

        for e in ele:
            print(e.text)

        driver.find_element(by=By.XPATH, value=xpath).click()
        driver.find_element_by_link_text("Management").click()
        break
    except ElementClickInterceptedException:
        continue
    except NoSuchElementException:
        continue

resetFrame(driver, "menufrm")
# a tag contains text
xpath = "//a[contains(text(),'Reboot')]"
xpath = "//a[href='resetrouter.html']"
while True:
    try:
        # status = driver.find_element(by=By.CSS_SELECTOR, value=cls)
        ele = driver.find_elements(by=By.TAG_NAME, value="a")

        # for e in ele:
        #     print(e.text)

        driver.find_element(by=By.XPATH, value=xpath).click()
        driver.find_element_by_link_text("Management").click()
        break
    except ElementClickInterceptedException:
        continue
    except NoSuchElementException:
        continue

resetFrame(driver, "basefrm")
# a tag contains text
cls = "input#buttonReboot"
while True:
    try:
        status = driver.find_element(by=By.CSS_SELECTOR, value=cls)
        break
    except ElementClickInterceptedException:
        continue
    except NoSuchElementException:
        continue

driver.close()
