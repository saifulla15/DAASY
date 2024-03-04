n = int(input())
a = 0
b = 1
if n < 0:
    print("invalid")
elif n == 1:
    print(a)
for i in range(2, n):
    sum = a+b
    a = b
    b = sum
print(sum)
