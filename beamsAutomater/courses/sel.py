# selenium 4
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import os
from pick import pick

DELAY = 5

# driver setup
driver = webdriver.Firefox(service=Service("./geckodriver.exe"))
driver.maximize_window()

# login
driver.get("https://prism.beaconhouse.net/")
name = driver.find_element(by=By.ID, value="inputName")
password = driver.find_element(by=By.ID, value="inputPassword")
name.send_keys("86134")
password.send_keys("shanza143")
password.send_keys(Keys.ENTER)

# quiz
time.sleep(DELAY)
link = "https://prism.beaconhouse.net/mod/quiz/attempt.php?attempt=241845&cmid=4255"
driver.get(link)

questions = driver.find_elements(by=By.CSS_SELECTOR, value="div.answer")


# 0 --> true, 1 --> false
# continuous learning
# q1
# answerString = "010010100110"
# q2
# answerString = "100101110"
# q3
# answerString = "101001110010"
# q4
answerString = "111010101"

for i, question in enumerate(questions):
    div = question.find_elements(by=By.CSS_SELECTOR, value="div")
    for j, answer in enumerate(div):
        label = answer.find_element(by=By.CSS_SELECTOR, value="label")
        inp = answer.find_element(by=By.CSS_SELECTOR, value="input")
        # print(answerString[i])
        if answerString[i] == str(j):
            print(i, j, label.text)
            inp.click()
            break

# driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Finish attempt')]").click()
# driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Submit all and finish')]").click()
# driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Submit all and finish')]").click()

driver.find_element(by=By.CSS_SELECTOR, value="input.btn").click()
driver.find_element(by=By.CSS_SELECTOR, value="button.btn.btn-secondary").click()
time.sleep(DELAY)
driver.find_element(by=By.CSS_SELECTOR, value="input.btn.btn-primary").click()

results = driver.find_elements(by=By.CSS_SELECTOR, value="div.specificfeedback").text

answerString = ""
for result in results:
    result = result.text

    if "incorrect" in result:
        answerString += "1"
    elif "correct" in result:
        answerString += "0"

print(answerString)

# time.sleep(30)
# driver.close()
