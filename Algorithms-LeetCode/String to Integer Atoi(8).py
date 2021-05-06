class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        
        symbol=1
        
        res =0
        while i< len(s) and s[i]==' ':
            
            
            i+=1
        if i<len(s) and s[i]=="-":
            symbol*=-1
            i+=1
        elif i<len(s) and s[i]=="+":
            i+=1
        
        validNos=set('0123456789')
        while i<len(s) and s[i] in validNos:
            res=res*10+int(s[i])
            i+=1
        
        final=res* symbol
      
        final=0 if final ==0 else min(final, 2**31-1) if final>0 else max(final, -2**31) 
        
        return final