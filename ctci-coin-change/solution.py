#!/bin/python3


def make_change(coins, n):
    memo = [0] * (n+1)
    memo[0] = 1
    for coin in coins:
        for i in range(1, n+1):
            if i >= coin:
                memo[i] += memo[i - coin]
    return memo[n]

    


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
