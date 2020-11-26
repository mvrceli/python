from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

with open("Python/Selenium/nike/proxies.txt", "r+") as e:
    emails = [email.strip() for email in e]

password = input("What is the password for all accounts?\n")

with open("Python/Selenium/nike/proxies.txt", "r+") as p:
    proxies = [proxy.strip() for proxy in p]
    print(proxies)


#Ask for product page and make sure it works
product_page = input("Enter Nike splash page:\n")
if product_page[:4] == "http":
    product_page_final = product_page
else:
    product_page_final = "https://" + product_page

if product_page_final[:4] == "http":
    pass
else:
    print("Error") 
    quit()


for i in proxies and e in emails:
    PROXY = i
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",

    }
    with webdriver.Chrome('/Users/Jan/Desktop/Code/chromedriver.exe') as driver:

        driver.get("https://www.nike.com/pl/launch")
        time.sleep(1)
        print("Connected with",PROXY)
        driver.fullscreen_window()

        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/header/div[1]/section/div/ul/li[1]/button').click()
        time.sleep(0.2)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[2]/input').send_keys(e)
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[3]/input').send_keys(password + Keys.ENTER)
        time.sleep(2)

        driver.get(product_page_final)
        time.sleep(1)
        driver.minimize_window()


