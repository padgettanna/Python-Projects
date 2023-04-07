from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = '/filepath'
s = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=op)


driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
timeout = time.time() + 10
five_min = time.time() + 5*60

while time.time() < five_min:
    cookie.click()
    if time.time() > timeout:
        cookie_count = driver.find_element(By.ID, "money").text
        if "," in cookie_count:
            cookie_count = cookie_count.replace(",", "")
        money = int(cookie_count)
        items = driver.find_elements(By.CSS_SELECTOR, "#store div")
        all_items = [item.get_attribute("id") for item in items if item.get_attribute("class") == ""]
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                prices.append(cost)
        all_prices_items = {int(price): item for (price, item) in zip(prices, all_items)}
        item_to_buy_price = max(all_prices_items.keys())
        item_to_buy_id = all_prices_items[item_to_buy_price]
        driver.find_element(By.ID, f"{item_to_buy_id}").click()
        timeout = time.time() + 10
    if time.time() > five_min:
        score = driver.find_element(By.ID, "cps").text
        print(score)
        break

driver.quit()
