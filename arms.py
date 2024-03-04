a = int(input())
order = len(str(a))
sum = 0
temp = a
while (a > 0):
    digit = a % 10
    sum = sum+(digit**order)
    a = a//10
if (sum == temp):
    print("armstrong")
else:
    print("not")
