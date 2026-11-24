class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])

        for i in range(m):
            seen = set()
            for r in range(n):
                if board[i][r] == '.':
                    continue
                if board[i][r] in seen:
                    return False
                seen.add(board[i][r])
        
        for i in range(m):
            seen = set()
            for c in range(n):
                if board[c][i] == '.':
                    continue
                if board[c][i] in seen:
                    return False
                seen.add(board[c][i])
        
        for i in range(m):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (i//3) * 3 + r
                    col = (i%3) * 3 + c
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True