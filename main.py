from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


NAME_SELECTOR="#userName"
PASSWORD_SELECTOR="#password"

USERNAME=os.getenv("DEMOQA_USER")
PASSWORD=os.getenv("DEMOQA_PWD")

# Setup connection options
chrome_options = Options()
chrome_options.add_argument("--disable-search-enghine-choice-screen")
service = Service("./chromedriver/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
# Open the browser and load page
driver.get("https://demoqa.com/login")

# Locate controls
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, NAME_SELECTOR)))
pawword_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD_SELECTOR)))
login_button = driver.find_element(By.CSS_SELECTOR, "#login")

# Fill in and submit the form
username_input.send_keys(USERNAME)
pawword_input.send_keys(PASSWORD)
# login_button.click() – This will allow to avoid the “Element is not clickable” error
driver.execute_script("arguments[0].click();", login_button)

input("Press Enter to close the browser")
driver.quit()
