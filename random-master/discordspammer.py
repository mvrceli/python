from dhooks import Webhook
import random

h1 = ""
h2 = ""
h3 = ""
h4 = ""

length = int(input("How many iterations?\n"))
for i in range(0,length):
    data = ["", "", "", ""]
    data = random.choice(data)
    hook = Webhook(random.choice([h1,h2,h3,h4]))
    hook.send(data)
