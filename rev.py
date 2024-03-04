def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)


num = 12345
print("Original number:", num)
print("Reversed number:", reverse_number(num))
