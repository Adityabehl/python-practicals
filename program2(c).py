# 2.l. Generate first n prime numbers
def first_n_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
n=int(input("enter the amount of primes you want"))
print(f"The first {n} prime numbers: {first_n_primes(n)}")
