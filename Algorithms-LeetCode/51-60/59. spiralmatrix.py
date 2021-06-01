class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if  n==0: return None
        if n==1: return [[1]]
        
        rs=0 
        re=n
        cs=0
        ce=n
      
        res=[[0 for i in range(n)] for i in range(n)]
        n=1
        while (re>rs and ce>cs):
            
            for i in range(cs, ce):
                res[rs][i]=n
                n+=1
            for j in range(rs+1, re):
                res[j][ce-1]=n
                n+=1
            
            for i in range(ce-2, cs-1, -1):
                res[re-1][i]=n
                n+=1
            
            for j in range(re-2, rs, -1):
                res[j][cs]=n
                n+=1
            
            rs+=1
            cs+=1
            re-=1
            ce-=1
        
        return res        
        