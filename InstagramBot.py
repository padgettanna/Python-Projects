import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = 'Your driver path'
USERNAME = "your username"
PASSWORD = "your password"
ACCOUNT = "instagram account to follow"


class InstaFollower:

    def __init__(self, path):
        self.s = Service(path)
        self.op = webdriver.ChromeOptions()
        self.op.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.s, options=self.op)
        self.follower_list = []

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        self.driver.find_element(By.CLASS_NAME, "x1i10hfl").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "_a9_1").click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}")
        time.sleep(5)
        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        followers.click()
        time.sleep(5)
        follower_accounts = self.driver.find_element(By.CSS_SELECTOR, 'div._aano')
        time.sleep(5)
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_accounts)
            time.sleep(5)
        self.follower_list = self.driver.find_elements(By.CSS_SELECTOR, "div._aano div div div button")

    def follow(self):
        try:
            for i in self.follower_list:
                i.click()
                time.sleep(2)
        except selenium.common.exceptions.ElementClickInterceptedException:
            cancel = self.driver.find_element(By.CSS_SELECTOR, 'button._a9--._a9_1')
            cancel.click()
            time.sleep(2)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
