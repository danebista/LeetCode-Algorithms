class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)==0: return False
  
        res=[]
        for i in s:
            
            if i ==")" and len(res)>0 and res[len(res)-1]=="(":
                
                res.pop()
                continue
                    
            elif i=="]" and len(res)>0 and res[len(res)-1]=="[":
                res.pop()
                continue
            
            elif i=="}" and len(res)>0 and res[len(res)-1]=="{":
                res.pop()
                continue
            
            elif i =="(" or i=="[" or i=="{":
                res.append(i)
                continue
            return False
        
        return len(res)==0