import tkinter as tk
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.select import Select
from datetime import datetime
from threading import Timer

#Setup Keyboard
keyboard = Controller()


window = tk.Tk()
window.title("BOT")
window.geometry("800x600")
#window.config(bg="red")


# FUNCTIONS
def full_name_input():
    full_name_in = str(full_n.get())

def email_input():
    email_in = str(email.get())

def telephone_input():
    telephone_in = str(phone.get())

def address_input():
    address_in = str(address.get())

def city_input():
    city_in = str(city.get())

def zipc_input():
    zipc_in = str(zipc.get())

def country_input():
    country_in = str(country.get())

def card_input():
    card_in = str(card.get())

def cardn_input():
    cardn_in = str(cardn.get())


def submit():
    driver = webdriver.Chrome('/Users/22czarnecki_j/Downloads/chromedriver')
    driver.set_page_load_timeout("10")
    driver.get("https://www.supremenewyork.com/shop/all/t-shirts")
    time.sleep(0.1)

    driver.find_element_by_partial_link_text("Burnt").click()
    
    driver.find_element_by_name("commit").click()
    
    driver.find_element_by_class_name("checkout").click()
    

    driver.find_element_by_id('order_billing_name').click()
    keyboard.type(str(full_n.get()))

    driver.find_element_by_id('order_email').click()
    keyboard.type(str(email.get()))

    driver.find_element_by_id('order_tel').click()
    keyboard.type(str(phone.get()))

    driver.find_element_by_id('bo').click()
    keyboard.type(str(address.get()))

    driver.find_element_by_id('order_billing_city').click()
    keyboard.type(str(city.get()))

    driver.find_element_by_id('order_billing_zip').click()
    keyboard.type(str(zipc.get()))

    driver.find_element_by_id('order_billing_country').click()
    time.sleep(0.05)
    keyboard.type(str(country.get()))
    time.sleep(0.5)
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.release(Key.enter)

    driver.find_element_by_id('credit_card_type').click()
    time.sleep(0.05)
    keyboard.type(str(card.get()))
    time.sleep(0.5)
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.release(Key.enter)

    driver.find_element_by_id('cnb').click()
    keyboard.type(str(cardn.get()))



# LABEL
title =  tk.Label(text="Supreme Bot", font=("Futura", 30))
title.place(relx=0.7, rely=0.7, anchor='center')
title.grid(column=2, row=0)

label_name = tk.Label(text="Full Name:")
label_name.grid(column=0, row=1)

label_email = tk.Label(text="Email:")
label_email.grid(column=2, row=1)

label_phone = tk.Label(text="Telephone:")
label_phone.grid(column=0, row=4)

label_address = tk.Label(text="Address:")
label_address.grid(column=2, row=4)

label_city = tk.Label(text="City:")
label_city.grid(column=0, row=6)

label_zipc = tk.Label(text="Zip Code:")
label_zipc.grid(column=2, row=6)

label_country = tk.Label(text="Country:")
label_country.grid(column=0, row=8)

label_card = tk.Label(text="Card Type:")
label_card.grid(column=2, row=8)

label_cardn = tk.Label(text="Card Number:")
label_cardn.grid(column=0, row=10)


# ENTRY
full_n = tk.Entry()
full_n.grid(column=1, row=1)

email = tk.Entry()
email.grid(column=3, row=1)

phone = tk.Entry()
phone.grid(column=1, row=4)

address = tk.Entry()
address.grid(column=3, row=4)

city = tk.Entry()
city.grid(column=1, row=6)

zipc = tk.Entry()
zipc.grid(column=3, row=6)

country = tk.Entry()
country.grid(column=1, row=8)

card = tk.Entry()
card.grid(column=3, row=8)

cardn = tk.Entry()
cardn.grid(column=1, row=10)

# BUTTONS



buttontest = tk.Button(text="ENTER CREDENTIALS", command=full_name_input and email_input and telephone_input and address_input and city_input and zipc_input and country_input and card_input and cardn_input)
buttontest.grid(column=2, row=11, pady=10)
# START PROGRAM BUTTON

button3 = tk.Button(text="START", command=submit) 
button3.grid(column=2, row=12, padx=30, pady=15)
window.mainloop()



