def decrease(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
             grid[i][j] = (grid[i][j] - 1) % 4
    

def step(grid: list[list[int]]):
    height = len(grid)
    width = len(grid[0])
    neighbours = set()
    for i in range(height):
        for j in range(width):
            grid[i][j] = (grid[i][j] - 1) % 4
            if grid[i][j]:
                continue
            if i > 0:
                neighbours.add((i - 1, j))
            if i < height - 1:
                neighbours.add((i + 1, j))
            if j > 0:
                neighbours.add((i, j - 1))
            if j < width - 1:
                neighbours.add((i, j + 1))
    for n in neighbours:
        grid[n[0]][n[1]] = 0

def same(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False
    return True

def encode(grid):
    return [''.join(['O' if cell else '.' for cell in row]) for row in grid]

def decode(grid):
    return [[2 if cell == 'O' else 0 for cell in row] for row in grid]

from pprint import pprint

def bomberMan(n: int, grid: list[str]):
    grid = decode(grid)
    decrease(grid)
    step(grid)
    loop_start = [row.copy() for row in grid]
    loop_len = 0
    while loop_len < n - 3:
        step(grid)
        loop_len += 1
        if same(grid, loop_start):
            break
    if loop_len + 3 == n:
        return encode(grid)
    to_do = n - 3 % loop_len
    for _ in range(to_do):
        step(grid)
    return encode(grid) 