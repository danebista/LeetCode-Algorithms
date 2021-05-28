class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        a=[['.' for j in range(n)] for i in range(n)]
       
        def valid(row, col):
            for i in range(n):
                if a[i][col]=='Q':
                    return False
        
            for i in range(n):
                if (row+i<n and col+i<n):
                    if a[row+i][col+i]=='Q':
                        return False
        
                if (row-i>=0 and col-i>=0):
                    if a[row-i][col-i]=='Q':
                        return False
        
                if (row-i>=0 and col+i<n):
                    if a[row-i][col+i]=='Q':
                        return False
                    
                if (row+i<n and col-i>=0):
                    if a[row+i][col-i]=='Q':
                        return False
        
            return True
        
        def solver(rowNo):
            if rowNo == n:
                b=[]
                for i in a :
                    b.append(''.join(i))
                
                ans.append(b)
                return 
         
               
            for i in range(n):
                if valid(rowNo, i):
                    a[rowNo][i]='Q'
                    solver(rowNo+1)
                    a[rowNo][i]='.'
            
            return 
        solver(0)
        return ans
        