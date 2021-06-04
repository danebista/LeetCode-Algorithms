class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: 
            return grid
        if (len(grid))==0:
            return grid
        
        dp=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    
        dp[0][0]= grid[0][0]
    
        for i in range(1, len(grid[0])):
            dp[0][i]= dp[0][i-1]+ grid[0][i]
        
        for j in range(1, len(grid)):
            dp[j][0]= dp[j-1][0] + grid[j][0]
        
        for i in range(1,len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j]= grid[i][j]+min(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
        