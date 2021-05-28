class Solution:
    def totalNQueens(self, n: int) -> int:
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
                ans.append(a)
                return 
         
               
            for i in range(n):
                if valid(rowNo, i):
                    a[rowNo][i]='Q'
                    solver(rowNo+1)
                    a[rowNo][i]='.'
            
            return 
        solver(0)
        return len(ans)