class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            seen = set()
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])
            
        for c in range(cols):
            seen = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])

        for square in range(rows):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True
