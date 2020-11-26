import os
import random
os.system("clear")

# patient_list = []

patient_num = random.randint(0,100000000)

# patient_list.append(patient_num)
# if patient_num in patient_list:
#     patient_num = random.randint(0,100000000)
name = input("Input first name:\n")
os.system("clear")
lastname = input("Input last name:\n")
os.system("clear")
alias = input("Input alias:\n")
os.system("clear")
city = input("Input city:\n")
os.system("clear")
postalcode = input("Input postal code:\n")
os.system("clear")
street = input("Input for street:\n")
os.system("clear")
pn = int(input("Input phone number:\n"))
os.system("clear")
email = input("Input email:\n")
os.system("clear")
date_infection = input("Input date of infection (DD-MM-YYYY):\n")
os.system("clear")
today = input("Input today's date:\n")
os.system("clear")


postalcode = str(postalcode)
pn = str(pn)
date_infection = str(date_infection)
today = str(today)

info = [name, lastname, alias, city, postalcode, street, pn, email, date_infection, today]

for l in info:
    if l == "":
        print("You didn't add all info!")
        quit()

patient_num = str(patient_num)
print(info)
with open("/Users/PATH/Desktop/Programming/IB/problem sets/tracing/contact.txt", "r+") as f:
     old = f.read() 
     f.seek(0) 
     f.write("\n" + old + "\n") 
     f.write(patient_num + "\n")
     for i in info:
        i = i + "\n"
        f.write(i)
        
