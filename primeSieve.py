# Prime Number Sieve
# http://inventwithpython.com/hacking (BSD Licensed)

import math


def isPrime(num):
    # Returns True if num is a prime number, otherwise False.

    # Note: Generally, isPrime() is slower than primeSieve().
    if num < 2:
        return False

    # See if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def primeSieve(sieveSize):
    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.

    sieve = [True] * sieveSize
    sieve[0] = False # Zero and one are not prime numbers
    sieve[1] = False

    # Create the sieve
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    # Compile the list of primes
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

    return primes