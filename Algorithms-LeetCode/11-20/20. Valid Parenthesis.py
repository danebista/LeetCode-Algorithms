class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)==0: return False
        
        res = []
        
        for i in s:
            
            if i=='(' or i=='{' or i=='[':
                res.append(i)
                
            elif i==')' and len(res)>0 and res[len(res)-1]=='(':
                res.pop()
            
            elif i=='}' and len(res)>0 and res[len(res)-1]=='{':
                res.pop()
            
            elif i==']' and len(res)>0 and res[len(res)-1]=='[':
                res.pop()
            else:
                return False
            
        return len(res)==0
        