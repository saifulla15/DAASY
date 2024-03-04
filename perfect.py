def is_perfect(num):
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num


def find_perfect_numbers(n):
    perfect_numbers = []
    for i in range(1, n + 1):
        if is_perfect(i):
            perfect_numbers.append(i)
    return perfect_numbers


limit = 10000
print("Perfect numbers up to", limit, ":", find_perfect_numbers(limit))
