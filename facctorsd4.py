def find_factors(n, divisor=1, factors=None):
    if factors is None:
        factors = []

    if divisor > n:
        return factors

    if n % divisor == 0:
        factors.append(divisor)

    return find_factors(n, divisor + 1, factors)


n = 24
print("Factors of", n, "are:", find_factors(n))
