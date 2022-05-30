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
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
import time
import os
from pick import pick

DELAY = 3


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
            print(e)
            continue
        except NoSuchElementException as e:
            print(e)
            continue
        except StaleElementReferenceException as e:
            print(e)
            continue
        except ElementNotInteractableException as e:
            print(e)
            continue


def getElements(value, driver=driver, by=By.CSS_SELECTOR):
    while True:
        try:
            ele = driver.find_elements(by=by, value=value)
            return ele

        except ValueError as e:
            print(e)
            continue
        except NoSuchElementException as e:
            print(e)
            continue
        except StaleElementReferenceException as e:
            print(e)
            continue
        except ElementNotInteractableException as e:
            print(e)
            continue


inputs = driver.find_elements(by=By.CSS_SELECTOR, value=".form-control")
inputs[0].send_keys('86134')
inputs[1].send_keys('shanza143')
inputs[1].send_keys(Keys.ENTER)

# go to old beams
time.sleep(DELAY)
# time.sleep(7)
driver.get("https://beams.beaconhouse.edu.pk/home.php")

# gradebook button
driver.execute_script(
    "parent.addTab('Gradebook','iconCls','//beams.beaconhouse.edu.pk/students/sam/dashboard/sam_branches.php?mobile=');")

# selecting branch
samBranches = "ii_//beams.beaconhouse.edu.pk/students/sam/dashboard/sam_branches.php"
resetFrame(samBranches)
time.sleep(DELAY)

# branch input
getElement("input", by=By.TAG_NAME).click()

# select button
getElement(".bss_form_button").click()
time.sleep(DELAY)

# assessment entry
resetFrame("ii_students/sam/dashboard/index.php")
getElement("ext-gen19", by=By.ID).click()
time.sleep(DELAY)

clear()
selections = ["Branch: ", "Class: ", "Section: ", "Subject: ", "Term: "]

assEntryFrame = "ii_students/assessment/sta_prep_result_main.php"
for i, selection in enumerate(selections):
    while True:
        resetFrame(assEntryFrame, sleep=0)
        entries = getElements(".bss_form_textbox")

        try:
            select = Select(entries[i])

            # if select only has one option, choose that option
            if len(select.options) == 2:
                index = 0
                break

            print([x.text for x in select.options])
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


getElement("//input[@value='B']", by=By.XPATH).click()
getElement("//input[@value='Refresh']", by=By.XPATH).click()
getElement("//input[@value='Generate']", by=By.XPATH).click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()

time.sleep(10)
driver.quit()
