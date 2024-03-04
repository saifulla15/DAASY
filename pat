def pattern(n):
    if n == 0:
        return
    pattern(n - 1)
    print(" ".join(str(i) for i in range(1, n + 1)))


pattern(4)
