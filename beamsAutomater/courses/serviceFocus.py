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
import pickle
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

time.sleep(DELAY)

# quiz
link = "https://prism.beaconhouse.net/course/view.php?id=133"
driver.get(link)

quizNum = 1

quizzes = driver.find_elements(by=By.CSS_SELECTOR, value="div.activityinstance a")
for quiz in quizzes:
    if f"quiz {quizNum}" in quiz.text.lower():
        quiz.click()
        break

try:
    myElem = WebDriverWait(browser, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-secondary[type='submit']")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")


# time.sleep(DELAY)
btns = driver.find_elements(by=By.CSS_SELECTOR, value="button.btn.btn-secondary[type='submit']")
for btn in btns:
    if "attempt" in btn.text.lower():
        btn.click()
        break


try:
    myElem = WebDriverWait(browser, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.answer")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")


questions = driver.find_elements(by=By.CSS_SELECTOR, value="div.answer")

# q1
chosenAnswer = ["b", "b", "d", "a", "a"]
# q2
# q3
# q4

for i, question in enumerate(questions):
    div = question.find_elements(by=By.CSS_SELECTOR, value="div")
    for j, answer in enumerate(div):
        label = answer.find_element(by=By.CSS_SELECTOR, value="span.answernumber")
        inp = answer.find_element(by=By.CSS_SELECTOR, value="input")

        label = label.text.replace(".", "")

        # check if chosenAnswer is a list
        if isinstance(chosenAnswer[i], list):
            print(i, j, label)
            inp = answer.find_element(by=By.CSS_SELECTOR, value="input[type='checkbox']")
            for choice in chosenAnswer[i]:
                if choice == label:
                    inp.click()
            # break

        if chosenAnswer[i] == label:
            print(i, j, label)
            inp.click()
            break

# end test
driver.find_element(by=By.CSS_SELECTOR, value="input.mod_quiz-next-nav.btn.btn-primary").click()
time.sleep(DELAY)
btns = driver.find_elements(by=By.CSS_SELECTOR, value="button.btn.btn-secondary")
for btn in btns:
    if "submit" in btn.text.lower():
        btn.click()
        break
time.sleep(DELAY)
btns = driver.find_elements(by=By.CSS_SELECTOR, value="input.btn.btn-primary")
for btn in btns:
    # get value of input
    if "submit" in btn.get_attribute("value").lower():
        btn.click()
        break

# get results and calculate correct
time.sleep(DELAY)
results = driver.find_elements(by=By.CSS_SELECTOR, value="div.specificfeedback")

newAnswer = []
for i, result in enumerate(results, start=1):
    result = result.text

    if "incorrect" in result:
        print(f"Question: {i}")
        newAnswer.append("E")
    elif "correct" in result:
        newAnswer.append(chosenAnswer[len(newAnswer)])

# print(chosenAnswer)
print(newAnswer)

# time.sleep(30)
# driver.close()
