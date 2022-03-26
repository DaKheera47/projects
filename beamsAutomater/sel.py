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


def resetFrame(driver, newFrame, sleep=3):
    time.sleep(sleep)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(by=By.ID, value=newFrame))


# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver = webdriver.Firefox(service=Service("./geckodriver.exe"))
driver.maximize_window()
driver.get("https://beams.beaconhouse.edu.pk/home/")

inputs = driver.find_elements(by=By.CSS_SELECTOR, value=".form-control")
inputs[0].send_keys('86134')
inputs[1].send_keys('shanza143')
inputs[1].send_keys(Keys.ENTER)

# go to old beams
time.sleep(3)
driver.get("https://beams.beaconhouse.edu.pk/home.php")
# time.sleep(7)

resetFrame(driver, "ii_core/mobile_app/sch_diary.php")
gradebook = driver.find_element(by=By.LINK_TEXT, value="Gradebook")
gradebook.click()

# selecting branch
resetFrame(
    driver, "ii_//beams.beaconhouse.edu.pk/students/sam/dashboard/sam_branches.php")
selectButton = driver.find_element(by=By.TAG_NAME, value="input")
selectButton.click()
selectButton = driver.find_element(
    by=By.CSS_SELECTOR, value=".bss_form_button")
selectButton.click()

# assessment entry
resetFrame(driver, "ii_students/sam/dashboard/index.php")
assessmentEntry = driver.find_element(by=By.ID, value="ext-gen11")
assessmentEntry.click()

# actual entry process
classToSelect = 10
section = "Silver"
marks = 30
desc = "Paper Two"
selections = [f"CAIE O LEVEL - Class {classToSelect}", section,
              "Urdu B 0539", "End of Year", "Assessment", "Single",  "End of Unit"]

for i, selection in enumerate(selections):
    resetFrame(
        driver, "ii_students/assessment/sam_class_assessment_entry.php", sleep=1)
    entries = driver.find_elements(by=By.CLASS_NAME, value="bss_form_textbox")
    select = Select(entries[i])
    select.select_by_visible_text(selection)

maxMarks = driver.find_element(by=By.ID, value="br_max_marks")
maxMarks.send_keys(f"{marks}")

description = driver.find_element(by=By.ID, value="br_desc")
description.send_keys(f"{desc}")

refresh = driver.find_element(by=By.ID, value="aaaa")
refresh.click()

# entry job
resetFrame(driver, "ii_students/assessment/sam_class_assessment_entry.php")
students = driver.find_elements(
    by=By.XPATH, value="//td[@class='x-grid3-col x-grid3-cell x-grid3-td-std_name ']//div")
# print(len(students))
# for student in students:
#     driver.execute_script("arguments[0].scrollIntoView()", student)
#     print(student.text)

className = 'x-grid3-col x-grid3-cell x-grid3-td-std_grade '
entries = driver.find_elements(by=By.XPATH, value=f"//td[@class='{className}']")

print(f"Max marks: {marks}")
for i in range(len(entries)):
    resetFrame(driver, "ii_students/assessment/sam_class_assessment_entry.php", sleep=0)
    student = students[i]
    e = entries[i]

    driver.execute_script("arguments[0].scrollIntoView()", e)
    e.click()
    inp = driver.find_element(by=By.XPATH, value="//input[@id='ext-comp-1003']")
    # marks = input(f"{student.text}: ")
    obtained = random.randint(0, 30)
    print(f"{student.text}: {obtained}/{marks}")
    inp.send_keys(f"{obtained}")
    inp.send_keys(Keys.ENTER)

# time.sleep(30)
# driver.close()
