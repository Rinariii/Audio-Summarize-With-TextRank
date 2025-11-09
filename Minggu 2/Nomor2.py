rows, cols = 3, 5
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
]

r, c = 0, 0
t = 1

def state(t, r, c, grid):
    print(f"t = {t}")
    for i in range(len(grid)):
        row_str = []
        for j in range(len(grid[0])):
            if i == r and j == c:
                row_str.append('x')
            else:
                row_str.append(str(grid[i][j]))
        print(" ".join(row_str))

def clean(r, c, grid):
    if grid[r][c] == 1:
        grid[r][c] = 0

def traverse(r, direction, cols):
    if direction == 'L2R':
        cols_range = range(cols)
    else:
        cols_range = range(cols - 1, -1, -1)
    for c in cols_range:
        yield c

for r in range(rows):
    direction = 'L2R' if (r % 2 == 0) else 'R2L'
    if r%2 == 0:
        direction = "L2R"
    else :
        direction = "R2L"
        
    for c in traverse(r, direction, cols):
        clean(r, c, grid)
        state(t, r, c, grid)
        t += 1
