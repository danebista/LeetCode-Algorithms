class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res=[0 for x in s]
        if len(res)==0: return 0
        
        for i in range(len(s)):
            
            if s[i]==')':
                if i-1<0: 
                    continue
                
                if s[i-1]=='(':
                    res[i]=  res[i-2]+2
                    continue
                
                if i-res[i-1]-1<0:
                    continue
                
                if s[i-res[i-1]-1]=='(':
                    res[i]=res[i-1]+ 2+ res[i-res[i-1]-2]
                
        
        return max(res)
