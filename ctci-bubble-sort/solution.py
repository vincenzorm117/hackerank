n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def bubbleSort(a):
    L = len(a)
    swapCount = 0
    for i in range(L):
        for j in range(L-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapCount += 1
    return (swapCount, a[0], a[L-1])

bubbleInfo = bubbleSort(a)
print('Array is sorted in %d swaps.' % bubbleInfo[0])
print('First Element: %d' % bubbleInfo[1])
print('Last Element: %d' % bubbleInfo[2])