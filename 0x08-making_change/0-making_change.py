#!/usr/bin/python3
"""
Coin Change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each value
    min_coins = [float('inf')] * (total + 1)

    # There are 0 coins needed to make a total of 0
    min_coins[0] = 0

    # Compute the minimum number of coins for each value from 1 to the total
    for value in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= value:
                # Use the coin and subtract its value from the current total
                remaining = value - coin
                """Update the minimum number of coins
                needed for the remaining total"""
                min_coins[value] = min(
                        min_coins[value], min_coins[remaining] + 1
                        )

    # If no combination of coins can make the total, return -1
    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
