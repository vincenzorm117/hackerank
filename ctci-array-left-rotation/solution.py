def array_left_rotation(a, n, k):
    if k == 0 or n == 0:
        return a
    newArray = list(a)
    for i in range(n):
        index = (i+k)%n
        newArray[i] = a[index]
    return newArray

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
