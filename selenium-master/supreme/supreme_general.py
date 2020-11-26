from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

infos = {}

category = input("What sub-category are do you want?\n")
keyword = input("Enter main keyword:\n")

link_final = "https://www.supremenewyork.com/shop/all/" + category

with open("Python/Selenium/supreme/info.txt", "r+") as f:
    for line in f:
        name, value = line.split("=")
        infos[name] = (value)


#BILLING
name = infos["name"] 
email = infos["email"] 
phone = infos["phone"]
street = infos["street"] 
city = infos["city"] 
post = infos["post"]
country = infos["country"]
c_type = infos["c_type"]
c_num = infos["c_num"]
c_cvv = infos["c_cvv"]
c_month = infos["c_month"]
c_year = infos["c_year"]


#WEBSITE
print(f'Getting URL {link_final}')

driver = webdriver.Chrome()
driver.get(link_final)

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input"))
#     )
# finally:
#     driver.quit()

# time.sleep(2)

driver.find_element_by_partial_link_text(keyword).click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input").click()
time.sleep(0.2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/a[2]").click()
time.sleep(0.2)

driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[1]/input").send_keys(name)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[2]/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[3]/input").send_keys(phone)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[4]/div[1]/input").send_keys(street)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[6]/input").send_keys(city)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[7]/div[1]/input").send_keys(post)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[7]/div[2]/select").send_keys(country + Keys.ENTER)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/select").send_keys(c_type + Keys.ENTER)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[3]/div[1]/input").send_keys(c_num)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[3]/div[2]/div[1]/select[1]").send_keys(c_month + Keys.ENTER)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[3]/div[2]/div[1]/select[2]").send_keys(c_year + Keys.ENTER)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[3]/div[2]/div[2]/input").send_keys(c_cvv)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p/label/div/ins").click()


