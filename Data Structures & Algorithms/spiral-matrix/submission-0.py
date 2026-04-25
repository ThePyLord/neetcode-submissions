class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_boundary,left_boundary = 0, 0 # top, left
        ROWS, COLS = len(matrix), len(matrix[0]) # bottom, right
        res = []

        while top_boundary < ROWS and left_boundary < COLS:
            # Get every value in the top row
            for i in range(left_boundary, COLS):
                res.append(matrix[top_boundary][i])
            top_boundary += 1
            # Get every value in the right column
            for i in range(top_boundary, ROWS):
                res.append(matrix[i][COLS-1])
            COLS -= 1

            if not (left_boundary < COLS and top_boundary < ROWS):
                break
                
            # Get every value in the bottom row
            for i in range(COLS - 1, left_boundary - 1, -1):
                res.append(matrix[ROWS - 1][i])
            ROWS -= 1

            # Get every value in left column
            for i in range(ROWS - 1, top_boundary - 1, -1):
                res.append(matrix[i][left_boundary])
            left_boundary += 1
        return res