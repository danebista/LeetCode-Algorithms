class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solver(board)
        return None
    
        """
        Do not return anything, modify board in-place instead.
        """
    
    def solver(self,board):
        position =self.findEmptySquare(board)
        
        if not position:
            return True
        
        for i in range(1,10):
            validSquare = self.checkValidSquare(board, position, i)
            if validSquare:
                board[position[0]][position[1]] = str(i)
                
                if self.solver(board) == True:
                    return True
                board[position[0]][position[1]] = '.'
        
        return False
        
    def checkValidSquare(self, board, pos, num):
        for i in range(9):
            if board[pos[0]][i] != '.' and i!=pos[1] and board[pos[0]][i] == str(num):
                return False
        for j in range(9):
            if board[j][pos[1]] != '.' and j != pos[0] and board[j][pos[1]] == str(num):
                return False
        box_x= pos[0]//3
        box_y= pos[1]//3
        
        for i in range(box_x *3, box_x*3+3):
            for j in range(box_y*3, box_y*3+3):
                if board[i][j] != '.' and pos != (i,j) and board[i][j] == str(num):
                    return False
        return True
    def findEmptySquare(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return (i,j)
        return False