class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        rs,cs=0,0
        re,ce=len(matrix), len(matrix[0])
        res=[]
        
        while(re>rs and ce>cs):
            for i in range(cs, ce):
                res.append(matrix[rs][i])
            
            for j in range(rs+1, re):
                res.append(matrix[j][ce-1])
            
            if re!=rs+1:
                for i in range(ce-2, cs-1,-1):
                    res.append(matrix[re-1][i])
            
            if ce!=cs+1:
                for j in range(re-2, rs, -1):
                    res.append(matrix[j][cs])
            
            re-=1
            ce-=1
            rs+=1
            cs+=1
        
        return res
        