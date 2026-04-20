class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        print(f'iterating up to {len(matrix)//2} rows')
        matrix.reverse()
        for r in range(len(matrix)):
            # matrix[r], matrix[len(matrix) - r - 1] = matrix[len(matrix) - r - 1], matrix[r]
            for c in range(r + 1, len(matrix)):
                print(f'[BEFORE] ({r}, {c}) transpose:{matrix[r][c]}')
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                print(f'[AFTER] ({r}, {c}) transpose:{matrix[r][c]}')
        
        print(matrix)