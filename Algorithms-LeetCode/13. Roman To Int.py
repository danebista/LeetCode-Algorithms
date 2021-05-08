class Solution:
    def romanToInt(self, s: str) -> int:
        length=len(s)-1
        diction={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        
        total=0
        for i in range(len(s)):
            if length<0: return total
            
            curr=diction[s[length]]
           
            if length-1>=0 and diction[s[length-1]]<curr:
           
                total=total+(curr+diction[s[length-1]]-2*diction[s[length-1]])
          
                length-=1
            else:
                total=total+curr
            length-=1
        return total