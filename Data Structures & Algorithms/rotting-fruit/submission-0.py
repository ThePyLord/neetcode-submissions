class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins, fresh = 0, 0
        q = deque([])
        ROWS, COLS = len(grid), len(grid[0])

        # Count fresh oranges and add all sources of rotting oranges
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i,j])


        def get_dirs(i,j):
            return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for i,j in get_dirs(r,c):
                    if (i < 0 or j < 0 or i == ROWS or j == COLS or grid[i][j] != 1):
                        continue
                    grid[i][j] = 2 # Mark this as a rotten orange
                    fresh -= 1
                    q.append([i,j]) # Add this new position to the rotten oranges
            mins += 1

        return mins if fresh == 0 else -1