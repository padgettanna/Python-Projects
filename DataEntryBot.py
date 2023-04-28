from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = 'your driver path'
ZILLOW = "https://www.zillow.com"
ZILLOW_URL = "listings link"
GFORM_LINK = "your google forms link"
params = {
    "User-Agent": "your user-agent",
    "Accept-Language": "your accept-language",
    "sec-ch-ua": 'your sec-ch-ua',
}

s = Service(CHROME_DRIVER_PATH)
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=op)

link = requests.get(ZILLOW_URL, headers=params)
soup = BeautifulSoup(link.content, "lxml")
all_links = soup.find_all(attrs={"data-test": "property-card-link"})
all_prices = soup.find_all(attrs={"data-test": "property-card-price"})
all_addresses = soup.find_all(attrs={"data-test": "property-card-addr"})
links_list = [link["href"] for link in all_links]
links = []
[links.append(link) for link in links_list if link not in links]

for link in range(len(links)):
    if ZILLOW not in links[link]:
        links[link] = ZILLOW + links[link]
prices = [price.text[0:6] for price in all_prices]
addresses = [address.text.split("|")[-1].strip() for address in all_addresses]

driver.get(GFORM_LINK)
time.sleep(5)

for n in range(len(links)):
    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                  '/div/div[1]/div/div[1]/input')
    address_field.send_keys(addresses[n])
    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                '/div/div[1]/div/div[1]/input')
    price_field.send_keys(prices[n])
    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                               '/div/div[1]/div/div[1]/input')
    link_field.send_keys(links[n])
    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()
    another_response_link = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response_link.click()
