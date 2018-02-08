#!/bin/python3

import sys

def solve(arr, money):
    hash = {}
    for i in range(len(arr)):
        index = i+1
        value = arr[i]
        complement = money - value
        if complement in hash:
            complementIndex = hash[complement]
            if complementIndex < index:
                print(complementIndex, index)
            else:
                print(index, complementIndex)
            break
        hash[value] = index



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
