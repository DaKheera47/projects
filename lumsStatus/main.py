# setup selenium with firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime
import argparse
import sys
from selenium.webdriver.firefox.service import Service


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--refresh", help="how often to refresh data [mins]")
parser.add_argument("-i", "--iterations", help="how many times to check")
parser.add_argument("-e", "--email", help="email to login to LUMS Portal")
parser.add_argument("-p", "--password",
                    help="password to login to LUMS Portal")
parser.add_argument(
    "-b", "--browser", help="show what the browser is doing throughout the process", action="store_true")
args = parser.parse_args()


mins = int(args.refresh)
iterations = args.iterations
email = args.email
password = args.password
if not args.iterations:
    iterations = sys.maxsize
iterations = int(iterations)


# clear console
def clear():
    os.system("cls" if os.name == "nt" else "clear")


for i in range(iterations):
    t1 = time.perf_counter()

    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    options = Options()
    options.headless = not args.browser
    driver = webdriver.Firefox(
        options=options, service=Service("./geckodriver.exe"))

    driver.set_page_load_timeout(120)
    driver.implicitly_wait(120)

    # clear()
    # webdriver setup
    driver.get("https://admissions.lums.edu.pk/application/")

    # email field
    xpath = "//input[@type='email']"
    driver.find_element(by=By.XPATH, value=xpath).send_keys(email)

    # password field
    xpath = "//input[@type='password']"
    driver.find_element(by=By.XPATH, value=xpath).send_keys(password)

    # sign in button
    xpath = "//button[@type='submit']"
    driver.find_element(by=By.XPATH, value=xpath).click()

    cls = "span.label-inline"
    while True:
        try:
            status = driver.find_element(by=By.CSS_SELECTOR, value=cls).text
            break
        except ElementClickInterceptedException:
            continue
        except NoSuchElementException:
            continue

    clear()
    print(f"Refreshed at: {datetime.now()}")
    print(f"Status: {status}")
    driver.close()

    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()}: {status}\n")

    timeTaken = time.perf_counter() - t1

    print(f"Time taken: {timeTaken :.0f}s")
    if timeTaken < 60 * mins and i < iterations - 1:
        print(f"Sleep for: {(60 * mins) - timeTaken :.0f}s")
        time.sleep((60 * mins) - timeTaken)
