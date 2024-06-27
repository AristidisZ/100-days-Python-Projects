from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://en.wikipedia.org/wiki/Main_Page"
driver_path = "chromedriver-win64/chromedriver-win64/chromedriver.exe"

service = webdriver.ChromeService(executable_path=driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
print(number)

# portal = driver.find_element(By.LINK_TEXT, 'Wikipedia')
# portal.click()

button_search = driver.find_element(By.XPATH, '//*[@id="p-search"]/a/span[1]')  # Use find_element instead of find_elements
button_search.click()
search = driver.find_element(By.NAME, 'search')
search.send_keys("python", Keys.ENTER)

# //*[@id="searchform"]/div/div/div[1]/input

time.sleep(5)
driver.quit()