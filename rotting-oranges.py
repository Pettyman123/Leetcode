from collections import deque 

import sys

def orangesRotting(grid: list[list[int]]) -> int:
    num_minutes = -1
    m, n = len(grid), len(grid[0])
    empty , fresh , rotten = 0, 1, 2
    queue = deque()
    num_fresh = 0 

    for i in range(m):
        for j in range(n):
            if grid[i][j] == rotten:
                queue.append((i, j))
            elif grid[i][j] == fresh:
                num_fresh += 1 

    if num_fresh ==0:
        return 0
    
    while queue:
        num_minutes += 1
        for _ in range(len(queue)):
            for i_off, j_off in [(0,1), (1,0), (-1,0), (0,-1)]:
                r, c = i + i_off , j + j_off
                if 0 <= r < m and 0 <= c < n and grid[r][c] == fresh:
                    grid[r][c] = rotten
                    num_fresh -=1
                    queue.append((r, c))

    if num_fresh>0:
        return -1
    else:
        return num_minutes
    

print(orangesRotting([[2,1,1], [1,1,0], [0,1,1]]))