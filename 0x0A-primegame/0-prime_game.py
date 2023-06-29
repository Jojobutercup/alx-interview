#!/usr/bin/python3


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(num):
        while True:
            num += 1
            if is_prime(num):
                return num

    def remove_multiples(nums, prime):
        for i in range(prime, len(nums), prime):
            nums[i] = 0

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [1] * (n + 1)
        primes[0] = primes[1] = 0

        prime = 2
        while prime <= n:
            if primes[prime] == 1:
                remove_multiples(primes, prime)
            prime = get_next_prime(prime)

        # Count the number of primes remaining
        count = sum(primes)

        if count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
