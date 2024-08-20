#!/usr/bin/python3
"""determine the fewest number of coins needed to meet a given amount"""


def makeChange(coins, total):
    """make  change"""
    if total <= 0:
        return 0

    # Sort coins in descending order to use the largest coins first
    coins.sort(reverse=True)
    change = 0

    for i in coins:
        # print(total)
        # print(i)
        while i <= total:
            # print(total)
            total -= i
            change += 1
            # print(total)
        if total == 0:
            break
    # print(total)
    if total > 0:
        return -1
    return change
