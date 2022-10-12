"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError()
    #2 is the first prime, so is added to the list
    list = [2]
    n = 3
    while len(list) < number_of_primes:
        #f: every odd number, starting from 3
        f = 3
        """The largest a prime factor can be is the root of n,
        this is because even if a number larger than root n can divide
        n, there is also a number smaller than root n which is the quotient.
        So by checking up to root n we know that we have checked all factor pairs"""
        while f * f <= n:
            #if the number we are checking is divisible by f then it is not prime
            if n % f == 0:
                break
            #check next odd number
            else:
                f += 2
        #if all odd numbers less than or equal to root n are checked, and none of them divide n, then n is prime
        else:
            list.append(n)
        #increment n to next odd number
        n += 2
    return list
