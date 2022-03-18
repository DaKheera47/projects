# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://beams.beaconhouse.edu.pk/home/")

inputs = driver.find_elements(by=By.CSS_SELECTOR, value=".form-control")
inputs[0].send_keys('86134')
inputs[1].send_keys('shanza143')
inputs[1].send_keys(Keys.ENTER)

time.sleep(3)
# go to old beams
driver.get("https://beams.beaconhouse.edu.pk/home.php")
time.sleep(10)

driver.switch_to.frame(driver.find_element(by=By.ID, value="ii_core/mobile_app/sch_diary.php"))

gradebook = driver.find_element(by=By.LINK_TEXT, value="Gradebook")
gradebook.click()


time.sleep(2)
driver.switch_to.frame(driver.find_element(by=By.ID, value="ii_//beams.beaconhouse.edu.pk/students/sam/dashboard/sam_branches.php"))
selectButton = driver.find_element(by=By.TAG_NAME, value="input")
selectButton.click()
print(f"{selectButton.text = !r}")

selectButton = driver.find_element(by=By.CSS_SELECTOR, value=".bss_form_button")
print(f"{selectButton = !r}")
selectButton.click()

time.sleep(2)
driver.switch_to.frame(driver.find_element(by=By.TAG_NAME, value="iframe"))
assessmentEntry = driver.find_element(by=By.CSS_SELECTOR, value=".asses")
assessmentEntry.click()
# closeButton = driver.find_element(by=By.CSS_SELECTOR, value=".fad")
# closeButton.click()


time.sleep(30)
driver.close()
