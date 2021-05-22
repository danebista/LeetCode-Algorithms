class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        cache={}
        def bottomUp(i, j):
            
            if (i,j) in cache: return cache[(i,j)]
            
            if i>=m and j>=n:
                return True
            
            
            if j>=n:
                return False
            
            if i>=m:
                for k in range(j, n):
                    if p[k]!="*":
                        return False
                return True
          
            if p[j]=="*":
                cache[(i,j)]=bottomUp(i,j+1) or bottomUp(i+1,j)
                return cache[(i,j)]
            
            if s[i] == p[j] or p[j] =="?":
                cache[(i,j)]= bottomUp(i+1,j+1)
                return cache[(i,j)]
            
            cache[(i,j)]= False
            return cache[(i,j)]
        return bottomUp(0,0)