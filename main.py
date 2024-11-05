from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


USERNAME = os.getenv("DEMOQA_USER")
PASSWORD = os.getenv("DEMOQA_PWD")


class WebAutomation:
    def __init__(self, download_folder: str) -> None:
        # Setup connection options
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-enghine-choice-screen")

        prefs = {"download.default_directory": download_folder}
        chrome_options.add_experimental_option("prefs", prefs)

        service = Service("./chromedriver/chromedriver")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login(self, username, password):
        # Open the browser and load page
        self.driver.get("https://demoqa.com/login")

        # Locate controls
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#userName")))
        pawword_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
        login_button = self.driver.find_element(By.CSS_SELECTOR, "#login")

        # Fill in and submit the form
        username_input.send_keys(username)
        pawword_input.send_keys(password)
        # login_button.click() – This will allow to avoid the “Element is not clickable” error
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the Elements drop-down and Text Box menu
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#item-0")))
        text_box.click()

        # Locata the form fields
        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#userName")))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#userEmail")))
        current_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#currentAddress")))
        permanent_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#permanentAddress")))
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "#submit")

        # Fill in the form fields and submit the form
        full_name_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download_file(self):
        # Download file
        upload_and_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#item-7")))
        upload_and_download.click()
        download_button = self.driver.find_element(
            By.CSS_SELECTOR, "#downloadButton")
        self.driver.execute_script("arguments[0].click();", download_button)

    def close_browser(self):
        self.driver.quit()


if __name__ == "__main__":
    wa = WebAutomation(os.getcwd())
    wa.login(USERNAME, PASSWORD)
    wa.fill_form("John Doe", "john.doe@someemail.com", "123 Main Street, Some City, Some State, 12345",
                 "123 Permanent Street, Permanent City, Permanent State, 12345")
    wa.download_file()

    input("Press Enter to close the browser")
    wa.close_browser()
