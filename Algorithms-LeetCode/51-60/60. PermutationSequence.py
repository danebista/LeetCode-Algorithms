class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=[1]
        f=1
        for i in range(1,n):
            f*=i
            
            fact.append(f)
        
        numbers=[str(i+1) for i in range(n)]
        res=''
        
        def permute(r, k1, result):
            if r<=1:
                
                result+=numbers.pop()
        
                return result
           
            index = k1//fact[r-1]
            
            if (k1 % fact[r-1]==0):
                index-=1
            
            result+=numbers[index]
    
            
            numbers.remove(numbers[index])
            
            k1-=fact[r-1] * index
            return permute(r-1, k1, result)
        
        res = permute(n,k, '')

    
        return res
        