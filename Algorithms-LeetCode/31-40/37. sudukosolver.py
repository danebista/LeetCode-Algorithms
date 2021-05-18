class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        return self.solve(board)
       
    def solve(self, board):
        position = self.findEmpty(board)
        if not position :
            return True
        
        
        for i in range(1,10):
            if self.validBoardSquare(board, i, position):
                board[position[0]][position[1]]=str(i)
                
                if (self.solve(board)):
                    return True
                board[position[0]][position[1]]='.'  
        return False    
    
    def findEmpty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    return (i,j)
                
        return None
    
    def validBoardSquare(self, board,num, pos):
        
        for i in range(9):
            if board[pos[0]][i] != '.' and int(board[pos[0]][i]) == num and i!=pos[1]:
                return False
        for j in range(9):
            if board[j][pos[1]] != '.' and int(board[j][pos[1]])==num and j!=pos[0]:
                return False
        
        box_x=pos[0]//3
        box_y=pos[1]//3
        for i in range(box_x * 3, box_x*3+3):
            for j in range(box_y *3, box_y*3+3):
                if board[i][j] != '.' and int(board[i][j])==num and (i,j)!=pos:
                    return False
        
        return True
