from selenium import webdriver
import time

from selenium.webdriver.common.by import By

url = "https://www.python.org/"
driver_path = "C:/Users/ARisss/Desktop/PythonProjects/chromedriver-win64/chromedriver-win64/chromedriver.exe"


service = webdriver.ChromeService(executable_path=driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

events_text = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
events_date = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li/time')

events = {

}

for i in range(len(events_date)):
    events[i] = {
        "time": events_date[i].text,
        "name": events_text[i].text
    }
print(events)


iframe = driver.find_element(By.XPATH , '//*[@id="container"]/li[7]/ul/li[5]/a')
driver.execute_script('arguments[0].scrollIntoView(true)', iframe)


# driver.quit()