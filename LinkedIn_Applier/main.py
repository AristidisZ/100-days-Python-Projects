from selenium import webdriver
import time

from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

EMAIL = "aristidiszotka@gmail.com"
PASSWORD = "Meliodas5849li"
PHONE = 6943690861

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3847005491&distance=25&f_AL=true&f_E=1%2C2%2C3&f_WT=1%2C3%2C2&geoId=107227464&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'
driver_path = "C:/Users/ARisss/Desktop/PythonProjects/chromedriver-win64/chromedriver-win64/chromedriver.exe"

service = webdriver.ChromeService(executable_path=driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
#
time.sleep(2)
sign_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
sign_in.click()

email_input = driver.find_element(By.ID, 'username')
email_input.send_keys(EMAIL)
time.sleep(1)
# #
password_input = driver.find_element(By.ID, 'password').send_keys(PASSWORD)
time.sleep(1)
agree_join = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(15)

# iframe = driver.find_element(By.CSS_SELECTOR, '.jobs-list-feedback')
# driver.execute_script('arguments[0].scrollIntoView();', iframe)
# time.sleep(1)
# title_links = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results-list')
# jobs = []
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, "..jobs-s-apply--fadein button")
        apply_button.click()

        time.sleep(5)

        try:
            next_button = WebDriverWait(driver, 10).until(
                element_to_be_clickable((By.CLASS_NAME, 'artdeco-button__text')))
            if next_button:
                next_button.click()
        except TimeoutException:
            print("No 'Next' button found. Stopping.")



    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
