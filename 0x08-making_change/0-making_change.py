#!/usr/bin/python3
"""
Coin change making problem
"""


def makeChange(coins, total):
    """
    Make change for a given total using the fewest number of coins
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[total] == total + 1 else dp[total]
