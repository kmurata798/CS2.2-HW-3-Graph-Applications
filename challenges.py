def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    # count to store each new island found
    count = 0
    # If the grid is empty, return 0
    if not grid:
        return count

    y_max = len(grid)
    x_max = len(grid[0])
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count
    
def dfs(grid, i, j):
    # if i < 0 or j < 0 or i >= len(grid) or grid[i][j] != '1':
        # return
    if 0 <= i < len(grid[0]) and 0 <= y < len(grid) and grid[i][j] == "1":
        grid[i][j] = '0'
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)

# # Test Cases
# map1 = [
#     [1, 1, 1, 1, 0],
#     [1, 1, 0, 1, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]
# assert numIslands(map1) == 1

# map2 = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 1]
# ]
# assert numIslands(map2) == 3