from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_USERNAME = "your username"
TWITTER_PASSWORD = "your password"
MY_PROVIDER = "your internet provider"
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_driver_path = 'your driver path'
        self.s = Service(self.chrome_driver_path)
        self.op = webdriver.ChromeOptions()
        self.op.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.s, options=self.op)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        check_speed = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        check_speed.click()
        time.sleep(45)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/'
                                                       'span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                     '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        username = self.driver.find_element(By.CLASS_NAME, "r-30o5oe")
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_elements(By.CLASS_NAME, "r-30o5oe")
        password[1].send_keys(TWITTER_PASSWORD)
        password[1].send_keys(Keys.ENTER)
        time.sleep(10)
        tweet = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        tweet.send_keys(f"Hey, {MY_PROVIDER}. My down speed is {self.down} and up is {self.up} instead of "
                        f"{PROMISED_DOWN}down & {PROMISED_UP}up.")
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                          'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/'
                                                          'div/div[2]/div[3]/div/span/span')
        tweet_button.click()
        time.sleep(10)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
time.sleep(10)
bot.tweet_provider()
