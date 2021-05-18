class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_key, c_key, b_key = set(), set(), set()
        
        
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    row=(i, board[i][j])
                    col=(j, board[i][j])
                    brd=(i//3, j//3, board[i][j])
                    
                    if (row in r_key) or (col in c_key) or (brd in b_key):
                        return False
                    
                    r_key.add(row)
                    c_key.add(col)
                    b_key.add(brd)
                    
        
                    
                
        return True
        