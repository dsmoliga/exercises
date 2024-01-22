import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdm7YE6ElbBVp1Muo2vIzmw8M9CHmlZsvyu8IgY497PKHhfVw/viewform?usp=sf_link"

request = requests.get(ZILLOW_URL)
data = request.text

soup = BeautifulSoup(data, "html.parser")

# Getting addresses of apartments
apartment_addresses = soup.select("address")

all_addresses = [address.get_text().strip().replace(" | ", " ")
                 for address in apartment_addresses]

# Getting links to see these apartments
link_addresses = soup.select(".StyledPropertyCardDataWrapper a")

all_link_addresses = [link["href"] for link in link_addresses]

# Getting prices of apartments
apartment_prices = soup.select(".PropertyCardWrapper span")
all_apartment_prices = [price.get_text().strip("+/mo").split("+")[0]
                        for price in apartment_prices]


# Starting selenium and filling forms with data
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_addresses)):
    driver.get(FORMS_URL)
    time.sleep(10)

    address = driver.find_element(
        By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price = driver.find_element(
        By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link = driver.find_element(
        By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_btn = driver.find_element(
        By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    address.send_keys(all_addresses[n])
    price.send_keys(all_apartment_prices[n])
    link.send_keys(all_link_addresses[n])
    submit_btn.click()
