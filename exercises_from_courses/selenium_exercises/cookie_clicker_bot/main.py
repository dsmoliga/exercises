from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Kepping chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

# Starting driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Getting cookie to click
cookie = driver.find_element(By.ID, value="cookie")


# Get store items ids
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
items_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5   # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds
    if time.time() > timeout:

        # Getting prices from <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Converting <b> tags into int price
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Creating dictionary of store items with prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_ids[n]

        # Getting our actual cookie count
        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookies_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookies_count > cost:
                affordable_upgrades[cost] = id

        # Buying the most expensive upgrade that we can afford
        highest_value_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_value_upgrade]

        driver.find_element(By.ID, value=to_purchase_id).click()
        cookies_count -= highest_value_upgrade

        # Adding another 5 seconds until next check
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break

driver.quit()
