class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_col = image[sr][sc]
        if init_col == color:
            return image
        ROWS, COLS = len(image), len(image[0])
        q = deque([(sr, sc)])
        image[sr][sc] = color

        def get_neighbours(r, c):
            return [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        while q:
            r, c = q.popleft()
            ns = get_neighbours(r, c)
            for nx, ny in ns:
                if 0 <= nx < ROWS and 0 <= ny < COLS and image[nx][ny] == init_col:
                    image[nx][ny] = color
                    q.append((nx, ny))

        return image