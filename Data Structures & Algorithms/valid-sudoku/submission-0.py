class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMask = [[0]*9 for _ in range(9)] 
        colMask = [[0]*9 for _ in range(9)] 
        subRowMask = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                subBox = (i // 3) * 3 + (j // 3)
                if rowMask[i][int(board[i][j])-1] == 1:
                    return False
                elif colMask[j][int(board[i][j])-1] == 1:
                    return False
                elif subRowMask[subBox][int(board[i][j])-1] == 1:
                    return False                        
                else:
                    rowMask[i][int(board[i][j])-1] = 1
                    colMask[j][int(board[i][j])-1] = 1
                    subRowMask[subBox][int(board[i][j])-1] = 1
        return True
            
