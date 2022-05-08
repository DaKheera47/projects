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
import itertools

DELAY = 5
quizNum = 4





def getResult(driver, chosenAnswer):
    # quiz
    link = "https://prism.beaconhouse.net/course/view.php?id=134"
    driver.get(link)

    quizzes = driver.find_elements(by=By.CSS_SELECTOR, value="div.activityinstance a")
    for quiz in quizzes:
        if f"quiz {quizNum}" in quiz.text.lower():
            quiz.click()
            break

    time.sleep(DELAY)
    btns = driver.find_elements(by=By.CSS_SELECTOR, value="button.btn.btn-secondary[type='submit']")
    for btn in btns:
        if "attempt" in btn.text.lower():
            btn.click()
            break

    time.sleep(DELAY)
    questions = driver.find_elements(by=By.CSS_SELECTOR, value="div.answer")

    # # q1
    # chosenAnswer = ["c", "b", ["c", "b"], "b", ["a", "d"]]
    # # q2
    # chosenAnswer = ["b", "a", "b", "a", "c"]
    # # q3
    # chosenAnswer = ["c", "c", ["a", "c"], "c"]
    # # q4
    # chosenAnswer = ["d", "c", "d"]

    for i, question in enumerate(questions):
        div = question.find_elements(by=By.CSS_SELECTOR, value="div")
        for j, answer in enumerate(div):
            label = answer.find_element(by=By.CSS_SELECTOR, value="span.answernumber")
            inp = answer.find_element(by=By.CSS_SELECTOR, value="input:not([type='hidden'])")

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

    return results



def testGetResult(i, chosenAnswer):
    answer = []

    for j in chosenAnswer:
        if j == "c":
            answer.append({"text": "correct",})
        else:
            answer.append({"text": "Incorrect",})
        


    return answer
    








# # driver setup
# driver = webdriver.Firefox(service=Service("./geckodriver.exe"))
# driver.maximize_window()

# # login
# driver.get("https://prism.beaconhouse.net/")
# name = driver.find_element(by=By.ID, value="inputName")
# password = driver.find_element(by=By.ID, value="inputPassword")
# name.send_keys("86134")
# password.send_keys("shanza143")
# password.send_keys(Keys.ENTER)

# time.sleep(DELAY)

# check all options if they are correct or not
questions = [{"answers": 4}, {"answers": 4}, {"answers": 4}]
# questions = [{"answers": 6}, {"answers": 2}, {
#     "answers": 4}, {"answers": 3}, {"answers": 2}]

results = []


for i, question in enumerate(questions):
    temp = []
    answer = question["answers"]

    for j in range(answer):
        # get ord of a
        temp.append(chr(ord("a") + j))

    results.append(temp)



possibleAnswers = list(itertools.product(*results))
print(len(possibleAnswers))
possibleAnswers = reversed(possibleAnswers)

newAnswer = []

foundAnswer = []
for i, chosenAnswer in enumerate(possibleAnswers):
    chosenAnswer = list(chosenAnswer)
    print(f"{chosenAnswer = }")

    try:
        for ans in newAnswer:
            if ans != "Z":
                try:
                    ind = chosenAnswer.index(ans)
                    chosenAnswer[ind] = ans
                except ValueError:
                    pass
    except NameError:
        pass

    print(f"{chosenAnswer = }")


    # for j, char in enumerate(foundAnswer):
    #     if char != 0:
    #         print(j, char)
    #         chosenAnswer[j] = char


    # results = getResult(driver, chosenAnswer)
    results = testGetResult(i, chosenAnswer)
    print(f"{results = }")

    for k, result in enumerate(results, start=1):
        result = result["text"].lower()

        if "incorrect" in result:
            # print(f"Question: {k}")
            # newAnswer.append("Z")
            pass
        elif "correct" in result:
            for l, char in enumerate(foundAnswer):
                if char == 0:
                    foundAnswer.append(chosenAnswer[len(newAnswer)])
                    # print(foundAnswer)
                    break

            newAnswer.insert(0, chosenAnswer[k])

    print(f"{foundAnswer = }")
    print(f"{newAnswer = }")
    print("----------")

    # time.sleep(30)
    # driver.close()
