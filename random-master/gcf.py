amount = int(input("How many numbers:\n"))
number_list = []
for i in range(0,amount):
    number = int(input("Enter number:\n"))
    number_list.append(number)
    
works = True
gcf_list = []
num_min = min(number_list)
num_max = max(number_list)

for i in range(num_min,num_max,1):
    if num_min % i == 0:
        gcf = i
        gcf_list.append(gcf)
    break
for i in number_list:
    if i % gcf == 0: 
        pass
    elif i % gcf != 0:
        works = False
        break

if works == False:
    print("Your gcf is 1")
else:
    print("Your GCF is:",gcf)

    