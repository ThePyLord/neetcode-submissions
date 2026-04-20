class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS):
                return
            if grid[r][c] != '1':
                return

            grid[r][c] = 'v'
            dfs(r, c - 1) # left
            dfs(r - 1, c) # up
            dfs(r, c + 1) # right
            dfs(r + 1, c) # down

        num_islas = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    num_islas += 1
                    dfs(i, j)

        return num_islas