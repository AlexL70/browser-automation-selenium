from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


USERNAME = os.getenv("DEMOQA_USER")
PASSWORD = os.getenv("DEMOQA_PWD")

# Setup connection options
chrome_options = Options()
chrome_options.add_argument("--disable-search-enghine-choice-screen")

prefs = {"download.default_directory": os.getcwd()}
chrome_options.add_experimental_option("prefs", prefs)

service = Service("./chromedriver/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
# Open the browser and load page
driver.get("https://demoqa.com/login")

# Locate controls
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#userName")))
pawword_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
login_button = driver.find_element(By.CSS_SELECTOR, "#login")

# Fill in and submit the form
username_input.send_keys(USERNAME)
pawword_input.send_keys(PASSWORD)
# login_button.click() – This will allow to avoid the “Element is not clickable” error
driver.execute_script("arguments[0].click();", login_button)

# Locate the Elements drop-down and Text Box menu
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#item-0")))
text_box.click()

# Locata the form fields
full_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#userName")))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#userEmail")))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#currentAddress")))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#permanentAddress")))
submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")

# Fill in the form fields and submit the form
full_name_field.send_keys("John Doe")
email_field.send_keys("john.doe@someemail.com")
current_address_field.send_keys(
    "123 Main Street, Some City, Some State, 12345")
permanent_address_field.send_keys(
    "123 Permanent Street, Permanent City, Permanent State, 12345")
driver.execute_script("arguments[0].click();", submit_button)

# Download file
upload_and_download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#item-7")))
upload_and_download.click()
download_button = driver.find_element(By.CSS_SELECTOR, "#downloadButton")
driver.execute_script("arguments[0].click();", download_button)

input("Press Enter to close the browser")
driver.quit()
