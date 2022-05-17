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
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import random
import os
from pick import pick

DELAY = 5


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def resetFrame(driver, newFrame, sleep=3):
    time.sleep(sleep / 2)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(by=By.ID, value=newFrame))
    time.sleep(sleep / 2)


# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver = webdriver.Firefox(service=Service("./geckodriver.exe"))
driver.maximize_window()
driver.get("https://beams.beaconhouse.edu.pk/home/")

inputs = driver.find_elements(by=By.CSS_SELECTOR, value=".form-control")
inputs[0].send_keys('86134')
inputs[1].send_keys('shanza143')
inputs[1].send_keys(Keys.ENTER)

# go to old beams
time.sleep(DELAY)
driver.get("https://beams.beaconhouse.edu.pk/home.php")

while True:
    try:
        resetFrame(driver, "ii_core/mobile_app/sch_diary.php", sleep=DELAY)
        gradebook = driver.find_element(by=By.LINK_TEXT, value="Gradebook")
        gradebook.click()
        break
    except NoSuchElementException as e:
        print(e)
        continue

# selecting branch
samBranches = "ii_//beams.beaconhouse.edu.pk/students/sam/dashboard/sam_branches.php"
resetFrame(driver, samBranches)

while True:
    try:
        selectButton = driver.find_element(by=By.TAG_NAME, value="input")
        selectButton.click()
        break
    except NoSuchElementException as e:
        print(e)
        continue

branchSelect = ".bss_form_button"
selectButton = driver.find_element(by=By.CSS_SELECTOR, value=branchSelect)
selectButton.click()
time.sleep(DELAY)

# assessment entry
resetFrame(driver, "ii_students/sam/dashboard/index.php")
assessmentEntry = driver.find_element(by=By.ID, value="ext-gen11")
assessmentEntry.click()
time.sleep(DELAY)

clear()
desc = input("Enter description: ")
marks = int(input("Enter marks: "))
selections = ["Class: ", "Section: ", "Subject: ", "Semester: ",
              "Assessment: ", "Paper Type: ", "Type of Test: "]


def get_label(option): return option.text


assEntryFrame = "ii_students/assessment/sam_class_assessment_entry.php"
for i, selection in enumerate(selections):
    while True:
        resetFrame(driver, assEntryFrame, sleep=0)
        entries = driver.find_elements(by=By.CLASS_NAME, value="bss_form_textbox")
        time.sleep(0.15)

        try:
            select = Select(entries[i])
            # loop through options in select element
            sel, index = pick(select.options[1:],
                              selection, options_map_func=get_label)
            break
        except ValueError as e:
            continue

        except StaleElementReferenceException as e:
            continue

    # compensating for removing "Select" Option
    select.select_by_index(index + 1)
    clear()

maxMarks = driver.find_element(by=By.ID, value="br_max_marks")
maxMarks.send_keys(f"{marks}")

description = driver.find_element(by=By.ID, value="br_desc")
description.send_keys(f"{desc}")

# refresh button
refresh = driver.find_element(by=By.ID, value="aaaa")
refresh.click()

# entry job
resetFrame(driver, assEntryFrame)
xpath = "//td[@class='x-grid3-col x-grid3-cell x-grid3-td-std_name ']//div"
students = driver.find_elements(by=By.XPATH, value=xpath)

studentNames = []
for student in students:
    studentNames.append(student.text)

# entry job
xpath = f"//td[@class='x-grid3-col x-grid3-cell x-grid3-td-std_grade ']"
entries = driver.find_elements(by=By.XPATH, value=xpath)

results = []
total = 0
for i, ele in enumerate(entries):
    resetFrame(driver, assEntryFrame, sleep=0.2)
    clear()
    print(f"Max marks: {marks}")
    print(f"Description: {desc}")

    # average
    if i != 0:
        avg = total / i
        print(f"Average: {avg :.2f}")

    print()

    student = students[i]
    e = entries[i]

    # print previous students
    for ri, r in enumerate(results, start=1):
        print(f"{ri :02}. {r['name']}: {r['marks']}/{marks}")

    # click on student input
    driver.execute_script("arguments[0].scrollIntoView()", e)
    e.click()

    # get obtained from user
    while True:
        obtained = int(input(f"{i + 1 :02}. {student.text}: "))
        if obtained <= marks:
            break

    total += obtained
    results.append({"name": student.text, "marks": obtained})

    # get input and send data
    stuInp = "//input[@id='ext-comp-1003']"
    inp = driver.find_element(by=By.XPATH, value=stuInp)
    inp.send_keys(f"{obtained}")
    inp.send_keys(Keys.ENTER)

print(results)

resetFrame(driver, assEntryFrame)
# save
saveBtn = driver.find_element(by=By.ID, value="ext-gen22").click()
time.sleep(5)
driver.quit()
