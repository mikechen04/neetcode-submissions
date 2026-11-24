class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # iterate through the row of the board:
        # create a set
        # iterate through each row, if its seen before than return false
        # otherwise add the square to the set

        # then another for loop thru the columns
        # another set, and another for loop
        # if its seen before return false, otherwise add to the set

        # then for squares, make another for loop and a set
        # then two nested for loops each the size of a square which is 3
        # row = (square // 3) * 3 + i
        # col = (square % 3) * 3 + j
        # if board[r][c] already in seen, return false else add it to the set

        m, n = len(board), len(board[0])
        for i in range(m):
            row = set()
            for r in range(n):
                if board[i][r] == '.':
                    continue
                if board[i][r] in row:
                    return False
                row.add(board[i][r])
        
        for i in range(m):
            col = set()
            for c in range(n):
                if board[c][i] == '.':
                    continue
                if board[c][i] in col:
                    return False
                col.add(board[c][i])
        
        for i in range(m):
            sq = set()
            for j in range(3):
                for k in range(3):
                    row = (i // 3) * 3 + j
                    col = (i % 3) * 3 + k
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in sq:
                        return False
                    sq.add(board[row][col])

        return True