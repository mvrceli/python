num1 = int(input("Input first number:\n"))
num2 = int(input("Input second number:\n"))

def gcf(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    for x in range(num1,0,-1):
        if num1 % x == 0 and num2 % x == 0:
            return x

print("The greatest common factor of", num1,"and",num2,"is",str(gcf(num1,num2)))
