class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        res = []
        for _ in range(COLS):
            res.append([0] * ROWS)

        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]

        return res
