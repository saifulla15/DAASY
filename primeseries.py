def is_prime(n, divisor=2):
    if n <= 2:
        return n == 2
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)


def print_primes(start, end):
    if start <= end:
        if is_prime(start):
            print(start)
        print_primes(start + 1, end)


print_primes(1, 10)
