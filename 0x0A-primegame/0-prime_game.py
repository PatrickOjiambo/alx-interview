#!/usr/bin/python3
"""
Prime gamers
"""


def isWinner(x, nums):
    """_summary_

    Args:
        x (_type_): _description_
        nums (_type_): _description_
    """
    def sieve(n):
        primes = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (primes[p] is True):
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        primes[0] = False
        primes[1] = False
        return primes

    Maria = 0
    Ben = 0
    for n in nums:
        primes = sieve(n)
        sum_primes = sum(primes)
        if sum_primes % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
