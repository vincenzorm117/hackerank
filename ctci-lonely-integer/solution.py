

import sys


def toggle(mask, k):
    isOn = 1 << k & mask
    if isOn:
        return ~(1 << k) & mask
    else:
        return (1 << k) | mask

def lonely_integer(a):
    mask = 0
    for x in a:
        mask = toggle(mask, x)
    lonelyInteger = 0
    while 0 < mask:
        if (mask & 1) == 1:
            return lonelyInteger
        lonelyInteger += 1
        mask = mask >> 1

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
