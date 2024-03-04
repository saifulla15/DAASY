num1 = 48
num2 = 18
while num2:
    num1, num2 = num2, num1 % num2
print(num1)
