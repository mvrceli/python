import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


#Setup Terminal
os.system("clear")

#Setup Keyboard
keyboard = Controller()

#Specify Website
print("Choose between allegro and amazon")
website = input()
if website == "allegro":
    website_new = "https://allegro.pl"
if website == "amazon":
    website_new = "https://www.amazon.co.uk"


print("What is your desired item?")
item = input()

print("What is your email address?")
email = input()

#Use account for testing

print("What is your password to your account?")
password = input()

#Use password for testing

#Specify Driver
driver = webdriver.Chrome('/PATH/Desktop/chromedriver')
if website_new == "allegro":
    driver.get("https://allegro.pl/listing?string=" +item)
if website_new == "amazon":
    driver.get("https://www.amazon.co.uk")

driver.set_page_load_timeout("10")
driver.get(website_new)
time.sleep(1)

actions = ActionChains(driver)

#Fullscreen
driver.fullscreen_window()

#Captcha Bypass
driver.refresh()

#Specific Website Code
time.sleep(0.1)
if website_new == "https://www.amazon.co.uk":
    driver.find_element_by_class_name("field-keywords").click()
    time.sleep(0.1)
    keyboard.type(item)
    time.sleep(0.1)
    driver.find_element_by_class_name("nav-input").click()
    time.sleep(0.1)
    driver.find_element_by_class_name("aok-relative").click()
    time.sleep(0.1)
    driver.find_element_by_id("buy-now-button").click()
    time.sleep(0.5)
    driver.find_element_by_id("ap_email").click()
    time.sleep(0.5)
    keyboard.type(email)
    time.sleep(0.5)
    driver.find_element_by_id("continue").click()
    time.sleep(0.5)
    keyboard.type(password)
    driver.find_element_by_id("signInSubmit").click()
    time.sleep(0.1)


if website_new == "https://allegro.pl":
    actions.move_by_offset(900,500).click().perform()
    for i in range(0,6):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    driver.find_element_by_class_name("_d25db_3K7x6").click()
    time.sleep(0.1)
    keyboard.type(item)
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    driver.find_element_by_class_name("_00d6b80").click()
    time.sleep(0.1)
    for i in range(0,10):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.1)
    time.sleep(0.1)
    driver.find_element_by_id("add-to-cart-button").click()
    time.sleep(0.5)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(0.3)
    driver.find_element_by_class_name("_b99lj").click()
    time.sleep(0.3)
    driver.find_element_by_id("username").click()
    time.sleep(0.2)
    keyboard.type(email)
    time.sleep(0.2)
    driver.find_element_by_id("password").click()
    time.sleep(0.1)
    keyboard.type(password)
    time.sleep(0.1)
    driver.find_element_by_class_name("ng-binding").click()

    
