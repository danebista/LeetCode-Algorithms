class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if len(digits)==0: return res
        n=len(digits)
        mapping=['0','1','abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def letterCombiner(curr, index):
        
            if index==n:
                res.append(curr)
                return;
            
            letters= mapping[int(digits[index])]
       
            for i in range(len(letters)):
              
                letterCombiner(curr+letters[i],index+1)
        
        letterCombiner('',0)
        
        
        return res