def sieve_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while (p**2 <= n):
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    return [i for i, is_prime in enumerate(primes) if is_prime]

n = int(input("Enter an upper limit for prime numbers: "))
if n < 2:
    print("There are no prime numbers in the given range.")
else:
    prime_list = sieve_eratosthenes(n)
    print(f"Prime numbers up to {n}:")
    print(prime_list)
