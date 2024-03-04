s = "syf ulla"
ss = s.split()
ll = ''.join(ss)
print(ll)
k = ll[::-1]
print(k)
if ll == k:
    print("its palindrome")
else:
    print("it is not palindrome")
