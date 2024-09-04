#!/usr/bin/python3
"""script for alx interview prime number game"""


def is_prime(n):
    """ check if n is a prime number """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """define the winner in the game """
    maria_wins = 0
    ben_wins = 0

    if x < 1 or not nums:
        return None
    # Iterate through the given nums array
    # representing the different rounds of the game.
    for n in nums:
        # initialize a list of available numbers from 1 to n
        available_numbers = list(range(1, n + 1))
        # whose turn it is (Maria or Ben).
        maria_turn = True

        while available_numbers:
            if maria_turn:
                for num in available_numbers[:]:
                    if is_prime(num):
                        available_numbers.remove(num)
                        for i in range(num, n + 1, num):
                            if i in available_numbers:
                                available_numbers.remove(i)
                        maria_turn = False
                        break
                else:
                    ben_wins += 1
                    break
            else:
                for num in available_numbers[:]:
                    if is_prime(num):
                        available_numbers.remove(num)
                        for i in range(num, n + 1, num):
                            if i in available_numbers:
                                available_numbers.remove(i)
                        maria_turn = True
                        break
                else:
                    maria_wins += 1
                    break

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
