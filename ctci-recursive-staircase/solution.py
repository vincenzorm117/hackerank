def findNumberOfWaysToClimbStairs(n):
    N = max(n+1, 4)
    a = [-1] * N
    a[0], a[1], a[2] = 1, 1, 2
    for i in range(3, N):
        a[i] = a[i-1] + a[i-2] + a[i-3]
    return a

s = int(input().strip())
nums = []
for a0 in range(s):
    n = int(input().strip())
    nums.append(n)
a = findNumberOfWaysToClimbStairs(max(nums))
for a0 in nums:
    print(a[a0])
