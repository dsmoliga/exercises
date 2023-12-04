from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        # Privacy policy accept
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

        # Starting internet speedtest
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(50)

        # Closing pop-up
        self.driver.find_element(
            By.CSS_SELECTOR, ".celebration-modal div p button").click()

        # Getting download and upload speeds
        self.download_speed = self.driver.find_element(
            By.CLASS_NAME, "download-speed").text
        self.upload_speed = self.driver.find_element(
            By.CLASS_NAME, "upload-speed").text

    def twitter_login(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)

        # Catching an iframe
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//iframe[starts-with(@src, 'https://accounts.google.com/gsi/button')]")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="container"]/div/div[2]/span[1]'))).click()

        ### Log-in with Google ###
        # Getting window handles
        self.main_page = self.driver.current_window_handle
        self.window_handles = self.driver.window_handles

        for handle in self.window_handles:
            if handle != self.main_page:
                login_page = handle

        # Switching to pop-up window
        self.driver.switch_to.window(login_page)

        # Sending credentials
        google_mail_input = self.driver.find_element(
            By.XPATH, '//*[@id="identifierId"]')
        google_mail_input.send_keys(TWITTER_EMAIL)
        google_mail_input.send_keys(Keys.ENTER)

        time.sleep(3)

        google_password_input = self.driver.find_element(
            By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        google_password_input.send_keys(TWITTER_PASSWORD)
        google_password_input.send_keys(Keys.ENTER)

        time.sleep(2)

        # Login confirmation
        try:
            self.driver.find_element(
                By.XPATH, '//*[@id="confirm_yes"]').click()
        except NoSuchElementException:
            self.driver._switch_to.window(self.main_page)

        self.driver._switch_to.window(self.main_page)
        time.sleep(10)

        # Cookies accept
        self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div/span/span').click()

    def tweet_provider(self):
        self.twitter_login()
        # Preparing the tweet
        tweet_window = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_window.send_keys(
            f"Hey, my download speed is: {self.download_speed}Mb/s and upload is: {self.upload_speed}Mb/s!")
