def rec(n):
    if n <= 1:
        return n
    else:
        return (rec(n-1)+rec(n-2))


k = 10
if k <= 0:
    print("invalid")
rec(5)
