class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        
        if len(digits)==0 : return []
        
        mapping=[0,1,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
   
        def findLetter(current, index):
            if index == len(digits):
                res.append(current)
                return;
            
            values = mapping[int(digits[index])]
            for i in values:
                findLetter(current+i, index+1)
        
        
        
        findLetter('', 0)
        
        return res
        