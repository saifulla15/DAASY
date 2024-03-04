k = int(input("enter the number"))
if k < 2:
    print("enter the valid numbers ")
for i in range(2, k):
    if k % i == 0:
        print("it is not prime")
        break
else:
    print("its prime")
