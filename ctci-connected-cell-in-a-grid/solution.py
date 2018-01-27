
def getBiggestRegion(grid):
    def findCount(x, y):
        q = [(x,y)]
        grid[x][y] = 2
        count = 0
        while 0 < len(q):
            x, y = q.pop()
            count += 1
            for i in range(-1,2):
                for j in range(-1,2):
                    x2, y2 = x+i, y+j
                    if 0 <= x2 and x2 < n and 0 <= y2 and y2 < m:
                        if grid[x2][y2] == 1:
                            q.append((x2,y2))
                            grid[x2][y2] = 2
        return count
    n, m = len(grid), len(grid[0])
    biggestRegion = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1:
                biggestRegion = max(biggestRegion, findCount(x,y))
    return biggestRegion



n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
