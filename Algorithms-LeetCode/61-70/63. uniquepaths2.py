class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        if obstacleGrid[0][0]==1: return 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j]=1
                else:
                    obstacleGrid[i][j]=0
        
      
        for j in range(len(obstacleGrid[0])):
            if j>0 and j-1>=0:
         
                if obstacleGrid[0][j]==0:
    
                    continue
                obstacleGrid[0][j]=0 if obstacleGrid[0][j-1]==0 else 1
        
   
        for i in range(len(obstacleGrid)):
            if i>0 and i-1>=0:
                if obstacleGrid[i][0]==0:
                    continue
                obstacleGrid[i][0]=0 if obstacleGrid[i-1][0]==0 else 1
   
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    continue
                
                obstacleGrid[i][j]= obstacleGrid[i-1][j]+ obstacleGrid[i][j-1]
        
        return obstacleGrid[-1][-1]
                    