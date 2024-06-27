from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://orteil.dashnet.org/experiments/cookie/"
driver_path = "../chromedriver-win64/chromedriver-win64/chromedriver.exe"

service = webdriver.ChromeService(executable_path=driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, '#store div')
items_ids = [item.get_attribute("id") for item in items][:8]
# print(items_ids)

timeout = time.time() + 5
# print(timeout)
five_min = time.time() + 60*5 # 5minutes

while cookie:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_price = []

        for i in all_prices:
            element_text = i.text
            if element_text != "":
                cost = element_text.split("-")[1].strip().replace(",", "")
                item_price.append(cost)

        cookie_upgrades = {}

        for n in range(len(item_price)):
            cookie_upgrades[item_price[n]] = items_ids[n]
        # print(cookie_upgrades)

        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        # print(money_element)
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, ids in cookie_upgrades.items():
            if cookie_count > int(cost):
                affordable_upgrades[cost] = ids

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id  = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5
        # print(timeout)

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

driver.quit()

