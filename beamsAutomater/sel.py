# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
import time
import os
from pick import pick

DELAY = 5


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver = webdriver.Firefox(service=Service("./geckodriver"))
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="./chromedriver")

# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# # chrome_options.add_argument("--headless")
# chrome_options.add_argument('--no-sandbox')
# # chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.maximize_window()
driver.get("https://beams.beaconhouse.edu.pk/home/")


def get_label(option): return option.text


# def isPageLoaded(ele, driver=driver, by=By.CSS_SELECTOR):
#     while True:
#         try:
#             myElem = WebDriverWait(driver, 120).until(
#                 EC.presence_of_element_located(by=by, value='IdOfMyElement'))
#             break
#         except TimeoutException:
#             print("Loading took too much time!")
#             continue


def resetFrame(newFrame, sleep=3, driver=driver):
    time.sleep(sleep / 2)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(by=By.ID, value=newFrame))
    time.sleep(sleep / 2)


def getElement(value, driver=driver, by=By.CSS_SELECTOR):
    while True:
        try:
            ele = driver.find_element(by=by, value=value)
            return ele

        except ValueError as e:
            continue
        except NoSuchElementException as e:
            continue
        except StaleElementReferenceException as e:
            continue


def getElements(value, driver=driver, by=By.CSS_SELECTOR):
    while True:
        try:
            ele = driver.find_elements(by=by, value=value)
            return ele

        except ValueError as e:
            continue
        except NoSuchElementException as e:
            continue
        except StaleElementReferenceException as e:
            continue


inputs = driver.find_elements(by=By.CSS_SELECTOR, value=".form-control")
inputs[0].send_keys('86134')
inputs[1].send_keys('shanza143')
inputs[1].send_keys(Keys.ENTER)

# go to old beams
time.sleep(DELAY)
# isPageLoaded()
driver.get("https://beams.beaconhouse.edu.pk/home.php")

# gradebook button
driver.execute_script("parent.addTab('Gradebook','iconCls','//beams.beaconhouse.edu.pk/students/sam/dashboard/sam_branches.php?mobile=');")

# selecting branch
samBranches = "ii_//beams.beaconhouse.edu.pk/students/sam/dashboard/sam_branches.php"
resetFrame(samBranches)

# branch input
getElement("input", by=By.TAG_NAME).click()

# select button
getElement(".bss_form_button").click()
time.sleep(DELAY)

# assessment entry
resetFrame("ii_students/sam/dashboard/index.php")
getElement("ext-gen11", by=By.ID).click()
time.sleep(DELAY)

clear()
desc = input("Enter description: ")
marks = int(input("Enter marks: "))
selections = ["Class: ", "Section: ", "Subject: ", "Semester: ",
              "Assessment: ", "Paper Type: ", "Type of Test: "]


assEntryFrame = "ii_students/assessment/sam_class_assessment_entry.php"
for i, selection in enumerate(selections):
    while True:
        resetFrame(assEntryFrame, sleep=0)
        entries = getElements(".bss_form_textbox")
        # time.sleep(0)

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

# max marks field
getElement("#br_max_marks").send_keys(f"{marks}")
# description field
getElement("#br_desc").send_keys(f"{desc}")
# refresh button
getElement("#aaaa").click()

# store student names
resetFrame(assEntryFrame)
xpath = "//td[@class='x-grid3-col x-grid3-cell x-grid3-td-std_name ']//div"
students = getElements(xpath, by=By.XPATH)
studentNames = []
for student in students:
    studentNames.append(student.text)

# entry job
xpath = f"//td[@class='x-grid3-col x-grid3-cell x-grid3-td-std_grade ']"
entries = getElements(xpath, by=By.XPATH)

results = []
total = 0
for i, ele in enumerate(entries):
    resetFrame(assEntryFrame, sleep=0.2)
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
    getElement(stuInp, by=By.XPATH).send_keys(f"{obtained}\n")

print(results)

resetFrame(assEntryFrame)
# save button
# getElement("#ext-gen22").click()
time.sleep(5)
driver.quit()
