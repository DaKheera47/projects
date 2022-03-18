from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://smallseotools.com/plagiarism-checker/")

# finding main text box on the page
elem = driver.find_element_by_css_selector("#textBox")
elem.clear()

elem.send_keys(input("ROCKET LEAGUE: "))
elem.send_keys(Keys.RETURN)

time.sleep(10)

driver.close()