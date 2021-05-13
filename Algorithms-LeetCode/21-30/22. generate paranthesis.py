class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def calculateResult(l,r, seq)->None:
            if l==0 and r==0:
                
                result.append(seq)
                
                return None;
            if l<0 or r<0:
                return None;
            
            if l==r:
                
                calculateResult(l-1, r, seq+"(")
                return None;
                
            elif l<r :
                
                if l==0 and r>0: 
             
                    calculateResult(l, r-1, seq+")")
                    return None;
                    
                
                calculateResult(l-1,r, seq+"(")
                calculateResult(l,r-1, seq+")")
                
            return None;
            
        calculateResult(n,n,"")
        return result
        